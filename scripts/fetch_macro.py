#!/usr/bin/env python3
"""
fetch_macro.py — Snapshot quotidien des indicateurs macro.

Sources:
- yfinance pour indices, VIX, taux, FX, commodités, crypto

Usage:
    python scripts/fetch_macro.py

Output:
    Merge dans data/YYYY-MM-DD.json (section "macro")
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yfinance as yf

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def fetch_macro_data(symbols: dict) -> dict:
    result = {}
    for name, sym in symbols.items():
        try:
            ticker = yf.Ticker(sym)
            hist = ticker.history(period="5d", interval="1d")
            if hist.empty:
                result[name] = {"error": True, "reason": "No data"}
                continue
            last = hist.iloc[-1]
            prev = hist.iloc[-2] if len(hist) > 1 else last
            result[name] = {
                "symbol": sym,
                "value": round(float(last["Close"]), 4),
                "previous": round(float(prev["Close"]), 4),
                "change_pct": round((last["Close"] - prev["Close"]) / prev["Close"] * 100, 2),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        except Exception as e:
            result[name] = {"error": True, "reason": str(e)}
    return result


def detect_regime(macro: dict) -> dict:
    """
    Heuristique simple de détection du régime macro.
    Retourne : régime, pondération recommandée, malus/bonus.
    """
    vix = macro.get("vix", {}).get("value")
    dxy = macro.get("dxy", {}).get("value")
    us10y = macro.get("us10y", {}).get("value")
    wti = macro.get("wti", {}).get("value")
    spx_change = macro.get("spx", {}).get("change_pct")

    # Défauts
    regime = "Normal"
    weights = {"catalyst": 0.40, "valuation": 0.35, "momentum": 0.25}
    macro_bonus = 0.0
    notes = []

    if vix is not None:
        if vix > 30:
            regime = "Risk-off"
            weights = {"catalyst": 0.30, "valuation": 0.45, "momentum": 0.25}
            macro_bonus = -1.0
            notes.append(f"VIX={vix} >30 → Risk-off, Valorisation prime")
        elif vix < 15:
            regime = "Risk-on / Bull"
            weights = {"catalyst": 0.40, "valuation": 0.25, "momentum": 0.35}
            macro_bonus = +0.2
            notes.append(f"VIX={vix} <15 → Risk-on/Bull, Momentum prime")
        else:
            notes.append(f"VIX={vix} → Normal")

    if us10y is not None and wti is not None:
        # Stagflation heuristique : taux élevés + pétrole élevé
        if us10y > 4.5 and wti > 90:
            regime = "Stagflation"
            weights = {"catalyst": 0.35, "valuation": 0.40, "momentum": 0.25}
            macro_bonus = -1.5
            notes.append(f"10Y={us10y}% + WTI=${wti} → Stagflation, malus long-duration")

    if spx_change is not None and spx_change < -2:
        notes.append(f"S&P -{abs(spx_change)}% → pression vendeuse")

    return {
        "regime": regime,
        "weights": weights,
        "macro_bonus": macro_bonus,
        "notes": notes,
    }


def main():
    config = load_config()
    symbols = config.get("macro_symbols", {})
    date_str = today_str()
    data_path = DATA_DIR / f"{date_str}.json"

    print("[fetch_macro] Fetching macro data...", file=sys.stderr)
    macro = fetch_macro_data(symbols)
    regime_info = detect_regime(macro)

    macro_block = {
        "data": macro,
        "regime": regime_info,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Merge dans le fichier du jour (créé par fetch_prices ou standalone)
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            snapshot = json.load(f)
    else:
        snapshot = {
            "meta": {
                "date": date_str,
                "source": "yfinance",
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            },
            "prices": {},
        }

    snapshot["macro"] = macro_block
    snapshot["meta"]["fetched_at"] = datetime.now(timezone.utc).isoformat()

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False, default=str)

    # Mettre à jour latest.json si existe
    latest_link = DATA_DIR / "latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(data_path.relative_to(DATA_DIR))

    print(f"[fetch_macro] Written macro + regime={regime_info['regime']} to {data_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
