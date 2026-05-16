#!/usr/bin/env python3
"""
paper_trading.py — Paper Trading Engine Argus-IA.

Simule des trades virtuels basés sur les signaux du système.
Règles d'entrée :
  • Score Opportunité ≥ 7/10 (lu dans WATCHLIST_SCORES.md ou _init.md)
  • Filtre Qualité ≥ 4/6
  • Accounting risk ≠ 🔴 CRITICAL (pas de M-Score > -1.78 ni Z < 1.81)
  • Pas de position ouverte sur ce ticker

Règles de sizing :
  • Méthode ATR-based (position size = risk $ / (2×ATR))
  • Kelly partiel (Kelly fraction = 0.25)
  • Max 10% du capital par position
  • Max 5 positions ouvertes simultanées

Règles de sortie :
  • Stop-loss = cours d'entrée − 2×ATR (même méthode que l'analyse technique)
  • Take-profit dynamique = +3×ATR (ratio risque/rendement 1.5)
  • Time stop = J+60 si ni SL ni TP n'est atteint
  • Score Opportunité < 4/10 → exit anticipé

Journal : Portefeuille/PAPER_TRADES.md
Positions : Portefeuille/PAPER_POSITIONS.json
Performance : Portefeuille/PAPER_PERFORMANCE.md

Usage : python scripts/paper_trading.py
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yfinance as yf

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PORTEFEUILLE_DIR = BASE_DIR / "Portefeuille"
ACTIONS_DIR = BASE_DIR / "Actions"

PAPER_POSITIONS_PATH = PORTEFEUILLE_DIR / "PAPER_POSITIONS.json"
PAPER_TRADES_PATH = PORTEFEUILLE_DIR / "PAPER_TRADES.md"
PAPER_PERFORMANCE_PATH = PORTEFEUILLE_DIR / "PAPER_PERFORMANCE.md"

# Paramètres
INITIAL_CAPITAL = 100_000.0
RISK_PER_TRADE_PCT = 0.01   # 1% du capital par trade
MAX_POSITION_PCT = 0.10     # 10% max du capital par position
MAX_OPEN_POSITIONS = 5
KELLY_FRACTION = 0.25
SL_ATR_MULT = 2.0
TP_ATR_MULT = 3.0
TIME_STOP_DAYS = 60
SCORE_ENTRY_THRESHOLD = 7.0
SCORE_EXIT_THRESHOLD = 4.0


def load_latest() -> dict:
    latest = DATA_DIR / "latest.json"
    if not latest.exists():
        return {}
    try:
        with open(latest, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def load_accounting_risk() -> dict:
    path = DATA_DIR / "accounting_risk_latest.json"
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def load_paper_positions() -> list:
    if not PAPER_POSITIONS_PATH.exists():
        return []
    try:
        with open(PAPER_POSITIONS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_paper_positions(positions: list) -> None:
    PORTEFEUILLE_DIR.mkdir(parents=True, exist_ok=True)
    with open(PAPER_POSITIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(positions, f, indent=2, ensure_ascii=False, default=str)


def extract_score_from_init(ticker: str) -> float:
    """Extrait le Score Opportunité du dernier _init.md."""
    action_dir = ACTIONS_DIR / ticker
    if not action_dir.exists():
        return 0.0
    # Trouver le dernier _init.md
    init_files = sorted(action_dir.glob("*_init.md"))
    if not init_files:
        return 0.0
    try:
        text = init_files[-1].read_text(encoding="utf-8")
        # Cherche "Score Opportunité : X.X/10" ou similaire
        m = re.search(r"Score Opportunit[ée]\s*[:=]?\s*(\d+\.?\d*)", text)
        if m:
            return float(m.group(1))
    except Exception:
        pass
    return 0.0


def extract_filtre_qualite_from_init(ticker: str) -> int:
    """Extrait le Filtre Qualité score du dernier _init.md."""
    action_dir = ACTIONS_DIR / ticker
    if not action_dir.exists():
        return 0
    init_files = sorted(action_dir.glob("*_init.md"))
    if not init_files:
        return 0
    try:
        text = init_files[-1].read_text(encoding="utf-8")
        # Cherche "Score Qualité total : X/6"
        m = re.search(r"Score Qualit[ée].*?(\d)\s*/\s*6", text)
        if m:
            return int(m.group(1))
    except Exception:
        pass
    return 0


def get_accounting_risk(ticker: str, accounting: dict) -> dict:
    """Récupère les alertes accounting pour un ticker."""
    analysis = accounting.get("analysis", {})
    return analysis.get(ticker, {})


def calc_position_size(capital: float, entry: float, atr: float, kelly: float = None) -> tuple:
    """
    Calcule la taille de position en shares.
    Règles :
      1. Risk-based : risk$ / (SL distance) = shares
      2. Max position = 10% du capital
      3. Kelly partiel (si dispo)
    """
    risk_dollars = capital * RISK_PER_TRADE_PCT
    sl_distance = SL_ATR_MULT * atr
    shares_risk = int(risk_dollars / sl_distance) if sl_distance > 0 else 0

    # Max position capital
    max_shares_capital = int((capital * MAX_POSITION_PCT) / entry) if entry > 0 else 0

    # Kelly sizing (optional)
    shares_kelly = float('inf')
    if kelly and kelly > 0:
        kelly_position = capital * kelly * KELLY_FRACTION
        shares_kelly = int(kelly_position / entry) if entry > 0 else 0

    shares = min(shares_risk, max_shares_capital, shares_kelly)
    return max(shares, 0), risk_dollars


def check_entry_conditions(ticker: str, snapshot: dict, accounting: dict) -> dict:
    """Vérifie si un ticker remplit les conditions d'entrée."""
    score = extract_score_from_init(ticker)
    qualite = extract_filtre_qualite_from_init(ticker)
    acc = get_accounting_risk(ticker, accounting)

    data = snapshot.get("prices", {}).get(ticker, {})
    price = data.get("price", {})
    tech = data.get("technical", {})
    close = price.get("close")
    atr = tech.get("atr14")

    conditions = {
        "score_ok": score >= SCORE_ENTRY_THRESHOLD,
        "qualite_ok": qualite >= 4,
        "accounting_ok": acc.get("risk_level", "🟢 CLEAN") != "🔴 CRITICAL",
        "price_ok": close is not None and close > 0,
        "atr_ok": atr is not None and atr > 0,
        "score": score,
        "qualite": qualite,
        "accounting_risk": acc.get("risk_level", "N/A"),
        "close": close,
        "atr": atr,
    }
    conditions["entry_ok"] = all([
        conditions["score_ok"],
        conditions["qualite_ok"],
        conditions["accounting_ok"],
        conditions["price_ok"],
        conditions["atr_ok"],
    ])
    return conditions


def check_exit_conditions(position: dict, snapshot: dict) -> dict:
    """Vérifie si une position ouverte doit être clôturée."""
    ticker = position["ticker"]
    entry_price = position["entry_price"]
    entry_date = datetime.fromisoformat(position["entry_date"])
    sl = position["stop_loss"]
    tp = position["take_profit"]

    data = snapshot.get("prices", {}).get(ticker, {})
    price = data.get("price", {})
    close = price.get("close")
    if close is None:
        return {"exit": False}

    # SL / TP
    if close <= sl:
        return {"exit": True, "reason": "STOP_LOSS", "price": close, "pnl_pct": (close - entry_price) / entry_price * 100}
    if close >= tp:
        return {"exit": True, "reason": "TAKE_PROFIT", "price": close, "pnl_pct": (close - entry_price) / entry_price * 100}

    # Time stop
    if (datetime.now(timezone.utc) - entry_date).days >= TIME_STOP_DAYS:
        return {"exit": True, "reason": "TIME_STOP", "price": close, "pnl_pct": (close - entry_price) / entry_price * 100}

    # Score opportunité < 4
    current_score = extract_score_from_init(ticker)
    if current_score < SCORE_EXIT_THRESHOLD:
        return {"exit": True, "reason": "SCORE_EXIT", "price": close, "pnl_pct": (close - entry_price) / entry_price * 100}

    return {"exit": False}


def open_position(ticker: str, conditions: dict, capital: float) -> dict:
    """Ouvre une position papier."""
    entry = conditions["close"]
    atr = conditions["atr"]
    shares, risk = calc_position_size(capital, entry, atr)

    if shares <= 0:
        return None

    sl = round(entry - SL_ATR_MULT * atr, 2)
    tp = round(entry + TP_ATR_MULT * atr, 2)
    position_value = round(shares * entry, 2)

    return {
        "ticker": ticker,
        "entry_date": datetime.now(timezone.utc).isoformat(),
        "entry_price": round(entry, 2),
        "shares": shares,
        "position_value": position_value,
        "stop_loss": sl,
        "take_profit": tp,
        "atr_at_entry": round(atr, 2),
        "score_at_entry": conditions["score"],
        "qualite_at_entry": conditions["qualite"],
        "accounting_risk_at_entry": conditions["accounting_risk"],
        "risk_dollars": round(risk, 2),
        "status": "OPEN",
    }


def close_position(position: dict, exit_result: dict) -> dict:
    """Clôture une position papier."""
    position["exit_date"] = datetime.now(timezone.utc).isoformat()
    position["exit_price"] = exit_result["price"]
    position["exit_reason"] = exit_result["reason"]
    position["pnl_pct"] = round(exit_result["pnl_pct"], 2)
    position["pnl_dollars"] = round(exit_result["pnl_pct"] / 100 * position["position_value"], 2)
    position["status"] = "CLOSED"
    return position


def log_trade(position: dict) -> None:
    """Log un trade dans PAPER_TRADES.md."""
    PORTEFEUILLE_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if not PAPER_TRADES_PATH.exists():
        header = "# 📋 Journal Paper Trading — Argus-IA\n\n"
        header += "| Date | Ticker | Type | Entrée | Shares | SL | TP | Sortie | Raison | P&L $ | P&L % |\n"
        header += "|------|--------|------|--------|--------|----|----|--------|--------|-------|-------|\n"
        PAPER_TRADES_PATH.write_text(header, encoding="utf-8")

    line = (
        f"| {date_str} | {position['ticker']} | {position['status']} | "
        f"${position.get('entry_price', 'N/A')} | {position.get('shares', 'N/A')} | "
        f"${position.get('stop_loss', 'N/A')} | ${position.get('take_profit', 'N/A')} | "
        f"${position.get('exit_price', '—')} | {position.get('exit_reason', '—')} | "
        f"${position.get('pnl_dollars', '—')} | {position.get('pnl_pct', '—')}% |\n"
    )
    existing = PAPER_TRADES_PATH.read_text(encoding="utf-8")
    PAPER_TRADES_PATH.write_text(existing + line, encoding="utf-8")


def update_performance(positions: list) -> None:
    """Met à jour le rapport de performance."""
    closed = [p for p in positions if p["status"] == "CLOSED"]
    open_pos = [p for p in positions if p["status"] == "OPEN"]

    total_pnl = sum(p.get("pnl_dollars", 0) for p in closed)
    wins = sum(1 for p in closed if p.get("pnl_dollars", 0) > 0)
    losses = sum(1 for p in closed if p.get("pnl_dollars", 0) < 0)
    win_rate = round(wins / len(closed) * 100, 1) if closed else 0

    # Capital actuel
    capital = INITIAL_CAPITAL + total_pnl
    for p in open_pos:
        # Approximation P&L ouvert
        try:
            stock = yf.Ticker(p["ticker"])
            hist = stock.history(period="2d")
            if not hist.empty:
                current = float(hist["Close"].iloc[-1])
                unrealized = (current - p["entry_price"]) * p["shares"]
                capital += unrealized
        except Exception:
            pass

    content = f"""# 📊 Performance Paper Trading — Argus-IA

> **Date :** {datetime.now(timezone.utc).strftime("%Y-%m-%d")}
> **Capital initial :** ${INITIAL_CAPITAL:,.2f}
> **Capital actuel :** ${capital:,.2f}
> **P&L total :** ${total_pnl:,.2f} ({(total_pnl/INITIAL_CAPITAL)*100:.2f}%)

---

## Statistiques

| Métrique | Valeur |
|----------|--------|
| Trades fermés | {len(closed)} |
| Gagnants | {wins} |
| Perdants | {losses} |
| Win rate | {win_rate}% |
| Positions ouvertes | {len(open_pos)} |

## Positions ouvertes

| Ticker | Entrée | Shares | SL | TP | Jours ouverts | Score entrée |
|--------|--------|--------|----|----|---------------|--------------|
"""
    for p in open_pos:
        days = (datetime.now(timezone.utc) - datetime.fromisoformat(p["entry_date"])).days
        content += f"| {p['ticker']} | ${p['entry_price']} | {p['shares']} | ${p['stop_loss']} | ${p['take_profit']} | {days}j | {p.get('score_at_entry', 'N/A')}/10 |\n"

    content += """
---

## Règles du système

- Entrée : Score Opportunité ≥ 7/10 + Filtre Qualité ≥ 4/6 + Accounting ≠ 🔴
- Sizing : Risk 1% du capital / (2×ATR), max 10% par position
- SL : Entrée − 2×ATR | TP : Entrée + 3×ATR | Time stop : J+60
- Exit anticipé : Score < 4/10
"""
    PAPER_PERFORMANCE_PATH.write_text(content, encoding="utf-8")


def main():
    print("[paper] Starting paper trading engine...", file=sys.stderr)
    snapshot = load_latest()
    accounting = load_accounting_risk()
    positions = load_paper_positions()

    if not snapshot:
        print("[paper] ⚠️ No latest.json found. Skipping.", file=sys.stderr)
        return 0

    config = None
    try:
        with open(BASE_DIR / "config" / "watchlist.json", "r", encoding="utf-8") as f:
            config = json.load(f)
    except Exception:
        pass
    tickers = [t["ticker"] for t in config.get("tickers", [])] if config else []

    # --- 1. Vérifier les positions ouvertes (exit) ---
    new_positions = []
    for pos in positions:
        if pos["status"] != "OPEN":
            new_positions.append(pos)
            continue

        exit_result = check_exit_conditions(pos, snapshot)
        if exit_result["exit"]:
            closed = close_position(pos, exit_result)
            new_positions.append(closed)
            log_trade(closed)
            print(
                f"[paper] 🔴 CLOSED {pos['ticker']} @ ${exit_result['price']} "
                f"({exit_result['reason']}) P&L: {exit_result['pnl_pct']:+.2f}%",
                file=sys.stderr
            )
        else:
            new_positions.append(pos)

    # --- 2. Capital actuel ---
    closed_pnl = sum(p.get("pnl_dollars", 0) for p in new_positions if p["status"] == "CLOSED")
    capital = INITIAL_CAPITAL + closed_pnl

    # --- 3. Chercher nouvelles entrées ---
    open_count = sum(1 for p in new_positions if p["status"] == "OPEN")
    open_tickers = {p["ticker"] for p in new_positions if p["status"] == "OPEN"}

    for ticker in tickers:
        if open_count >= MAX_OPEN_POSITIONS:
            break
        if ticker in open_tickers:
            continue

        conditions = check_entry_conditions(ticker, snapshot, accounting)
        if not conditions["entry_ok"]:
            continue

        position = open_position(ticker, conditions, capital)
        if position:
            new_positions.append(position)
            log_trade(position)
            open_count += 1
            capital -= position["position_value"]
            print(
                f"[paper] 🟢 OPENED {ticker} ${position['entry_price']} × {position['shares']} "
                f"(SL ${position['stop_loss']}, TP ${position['take_profit']}) "
                f"Score {position['score_at_entry']}/10 | Risk ${position['risk_dollars']}",
                file=sys.stderr
            )

    # Save
    save_paper_positions(new_positions)
    update_performance(new_positions)

    print(f"[paper] Capital: ${capital:,.2f} | Open: {open_count} | Closed P&L: ${closed_pnl:,.2f}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
