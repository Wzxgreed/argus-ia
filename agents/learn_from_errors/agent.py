#!/usr/bin/env python3
"""
learn_from_errors.py — Boucle d'apprentissage automatique + calibration des scores.

Chaque matin :
1. Vérifie les fenêtres de suivi ouvertes (BACKTESTING.md, SUIVI_PRIX_CIBLES.md)
2. Récupère les performances réelles via yfinance, met à jour les verdicts
3. Extrait des règles d'apprentissage sur les erreurs
4. **CALIBRATION AUTO** : calcule les win rates par fourchette de score et ajuste

Intégration : bash scripts/run_morning.sh (étape 0, avant fetch_prices)
"""

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent

BACKTESTING_PATH = BASE_DIR / "Opportunités" / "BACKTESTING.md"
SUIVI_PRIX_PATH = BASE_DIR / "Actions" / "SUIVI_PRIX_CIBLES.md"
APPRENTISSAGES_PATH = BASE_DIR / "Agents" / "APPRENTISSAGES.md"
POST_MORTEMS_DIR = BASE_DIR / "Agents" / "POST_MORTEMS"
CALIBRATION_REPORT_PATH = BASE_DIR / "data" / "calibration_report_latest.json"

today = datetime.now(timezone.utc).date()

# Seuils de verdict (tolerance ±2%)
HIT_THRESHOLD = 0.02
MISS_THRESHOLD = -0.02

YF_TIMEOUT = 15  # seconds per HTTP call

# Fenêtres actives
HORIZONS_BT = {"J+5": 5, "J+20": 20, "J+60": 60}
HORIZONS_PC = {"J+30": 30, "J+90": 90, "J+180": 180}

# ---------------------------------------------------------------------------
# Calibration targets (win rate par fourchette de score)
# ---------------------------------------------------------------------------
CALIBRATION_TARGETS = {
    (9.0, 10.0): 0.70,
    (8.0, 8.99): 0.65,
    (7.0, 7.99): 0.55,
    (6.0, 6.99): 0.50,
}
MIN_SIGNALS_FOR_CALIBRATION = 10
WIN_RATE_TOLERANCE = 0.15  # écart > 15pts pour déclencher un ajustement


# ---------------------------------------------------------------------------
# Markdown table parsing helpers
# ---------------------------------------------------------------------------


def parse_markdown_table(text: str, header_keywords: list[str]) -> list[dict]:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if not any(kw.lower() in " ".join(cols).lower() for kw in header_keywords):
            continue
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        header = cols
        rows = []
        for j in range(i + 2, len(lines)):
            row_line = lines[j].strip()
            if not row_line.startswith("|"):
                break
            cells = [c.strip() for c in row_line.split("|")[1:-1]]
            if len(cells) != len(header):
                continue
            rows.append({header[idx]: cells[idx] for idx in range(len(header))})
        return rows
    return []


def replace_table_rows(text: str, header_keywords: list[str], new_rows: list[dict]) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if not any(kw.lower() in " ".join(cols).lower() for kw in header_keywords):
            continue
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        header = cols
        end_idx = i + 2
        for j in range(i + 2, len(lines)):
            if not lines[j].strip().startswith("|"):
                end_idx = j
                break
            end_idx = j + 1
        new_lines = [line, lines[i + 1]]
        for row in new_rows:
            cells = [str(row.get(col, "")).strip() for col in header]
            new_lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines[:i] + new_lines + lines[end_idx:])
    return text


def replace_table_in_section(text: str, section_marker: str, table_header_keywords: list[str], new_rows: list[dict]) -> str:
    """Remplace un tableau qui apparaît APRÈS un marqueur de section donné."""
    lines = text.splitlines()
    section_start = None
    for i, line in enumerate(lines):
        if section_marker in line:
            section_start = i
            break
    if section_start is None:
        return text

    # Chercher le premier tableau après le marqueur
    for i in range(section_start, len(lines)):
        if not lines[i].strip().startswith("|"):
            continue
        cols = [c.strip() for c in lines[i].split("|")[1:-1]]
        if not any(kw.lower() in " ".join(cols).lower() for kw in table_header_keywords):
            continue
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        header = cols
        end_idx = i + 2
        for j in range(i + 2, len(lines)):
            if not lines[j].strip().startswith("|"):
                end_idx = j
                break
            end_idx = j + 1
        new_lines = [lines[i], lines[i + 1]]
        for row in new_rows:
            cells = [str(row.get(col, "")).strip() for col in header]
            new_lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines[:i] + new_lines + lines[end_idx:])
    return text


# ---------------------------------------------------------------------------
# Price helpers
# ---------------------------------------------------------------------------


def get_close_on_date(ticker: str, target_date: datetime.date) -> float | None:
    start = target_date - timedelta(days=10)
    end = target_date + timedelta(days=3)
    period1 = int(datetime.combine(start, datetime.min.time()).timestamp())
    period2 = int(datetime.combine(end, datetime.min.time()).timestamp())

    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        f"?period1={period1}&period2={period2}&interval=1d"
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        resp = requests.get(url, headers=headers, timeout=YF_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        result = data.get("chart", {}).get("result", [])
        if not result:
            return None
        timestamps = result[0].get("timestamp", [])
        closes = result[0].get("indicators", {}).get("quote", [{}])[0].get("close", [])
        if not timestamps or not closes:
            return None

        for ts, close in zip(timestamps, closes):
            if close is None:
                continue
            d = datetime.fromtimestamp(ts, tz=timezone.utc).date()
            if d == target_date:
                return round(float(close), 2)

        for ts, close in reversed(list(zip(timestamps, closes))):
            if close is None:
                continue
            d = datetime.fromtimestamp(ts, tz=timezone.utc).date()
            if d <= target_date:
                return round(float(close), 2)

        return None
    except requests.Timeout:
        print(f"[learn] Timeout ({YF_TIMEOUT}s) fetching price for {ticker} @ {target_date}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[learn] Error fetching price for {ticker} @ {target_date}: {e}", file=sys.stderr)
        return None


def parse_price(text: str) -> float | None:
    normalized = text.replace(",", ".")
    m = re.search(r"[\$~]?\s*([0-9]+\.?[0-9]*)", normalized)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def get_latest_json_price(ticker: str) -> float | None:
    latest = BASE_DIR / "data" / "latest.json"
    if not latest.exists():
        return None
    try:
        data = json.loads(latest.read_text(encoding="utf-8"))
        block = data.get("prices", {}).get(ticker, {})
        return block.get("price", {}).get("close")
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Verdict logic
# ---------------------------------------------------------------------------


def verdict_opportunity(return_pct: float) -> tuple[str, float]:
    ret = round(return_pct, 2)
    if ret >= HIT_THRESHOLD:
        return ("✅ Hit", ret)
    if ret <= MISS_THRESHOLD:
        return ("❌ Miss", ret)
    return ("⚪ Scratch", ret)


def verdict_price_target(price_target: float, reco: str, price_window: float) -> str:
    reco_up = any(w in reco.lower() for w in ["achat", "buy", "overweight", "accumuler", "conserver"])
    reco_down = any(w in reco.lower() for w in ["vente", "sell", "underweight", "réduire"])
    delta = price_window - price_target
    delta_pct = delta / price_target if price_target != 0 else 0

    if reco_up and delta_pct >= 0.10:
        return "✅ Hit"
    if reco_up and delta_pct >= 0:
        return "⚠️ Partiel"
    if reco_down and delta_pct <= -0.10:
        return "✅ Hit"
    if reco_down and delta_pct <= 0:
        return "⚠️ Partiel"
    if abs(delta_pct) <= 0.05:
        return "⚪ Scratch"
    return "❌ Miss"


# ---------------------------------------------------------------------------
# Post-mortem generation
# ---------------------------------------------------------------------------


def generate_post_mortem(ticker: str, signal_date: str, score: str,
                         signal_type: str, entry_price: float, horizon: str,
                         exit_price: float, return_pct: float,
                         verdict: str) -> dict:
    pm = {
        "ticker": ticker,
        "date_signal": signal_date,
        "date_post_mortem": today.isoformat(),
        "score": score,
        "type": signal_type,
        "horizon": horizon,
        "entry_price": entry_price,
        "exit_price": exit_price,
        "return_pct": return_pct,
        "verdict": verdict,
        "rule_extracted": None,
        "confidence": "faible",
    }

    if "stagflation" in signal_type.lower() or "macro" in signal_type.lower():
        pm["rule_extracted"] = (
            "Si régime Stagflation confirmé → pénaliser Score Catalyseur de −0.5 pt "
            "sur tous les tickers cycliques, quelle que soit la qualité du catalyseur annoncé."
        )
        pm["confidence"] = "moyenne"
    elif "earnings" in signal_type.lower():
        pm["rule_extracted"] = (
            "Si le signal est basé sur un earnings beat mais que le RSI > 65 au moment du signal "
            "→ pénaliser Momentum de −0.5 pt (réaction déjà priced-in)."
        )
        pm["confidence"] = "moyenne"
    elif return_pct < -0.15:
        pm["rule_extracted"] = (
            "Si le cours chute > 15% dans les 20 jours post-signal → vérifier si un événement "
            "macro majeur (guerre, régulation, guidance cut) a été ignoré dans l'analyse initiale. "
            "Appliquer malus −1 pt Score Catalyseur si événement macro non modélisé."
        )
        pm["confidence"] = "moyenne"
    else:
        pm["rule_extracted"] = (
            "Post-mortem générique : relire l'analyse originale pour identifier la cause racine "
            "(Macro / Valorisation / Timing / Qualité bénéfices) et formuler une règle corrective."
        )
        pm["confidence"] = "faible"

    return pm


def save_post_mortem(pm: dict) -> None:
    POST_MORTEMS_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{pm['ticker']}_{pm['date_signal']}_{pm['horizon']}_post_mortem.json"
    path = POST_MORTEMS_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(pm, f, indent=2, ensure_ascii=False, default=str)
    print(f"[learn] Post-mortem written → {path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# APPRENTISSAGES.md updater
# ---------------------------------------------------------------------------


def append_rule_to_apprentissages(rule_text: str, source: str, confidence: str) -> None:
    if not APPRENTISSAGES_PATH.exists():
        print("[learn] APPRENTISSAGES.md not found, skipping rule append.", file=sys.stderr)
        return

    text = APPRENTISSAGES_PATH.read_text(encoding="utf-8")
    if rule_text in text:
        print("[learn] Rule already present in APPRENTISSAGES.md, skipping.", file=sys.stderr)
        return

    marker = "## Règles actives issues des erreurs"
    if marker not in text:
        print("[learn] Marker not found in APPRENTISSAGES.md, skipping.", file=sys.stderr)
        return

    rule_block = (
        f"\n### Règle auto — {today.isoformat()}\n"
        f"- **Règle :** {rule_text}\n"
        f"- **Source :** {source}\n"
        f"- **Confiance :** {confidence}\n"
        f"- **Commentaire :** Extrait automatiquement par `learn_from_errors.py`. "
        f"À réévaluer après 3 mois ou 10 signaux supplémentaires.\n"
    )

    idx = text.index(marker) + len(marker)
    new_text = text[:idx] + rule_block + text[idx:]
    APPRENTISSAGES_PATH.write_text(new_text, encoding="utf-8")
    print(f"[learn] Rule appended to APPRENTISSAGES.md", file=sys.stderr)


def append_calibration_rule(rule_text: str, bracket: str, observed: float, target: float) -> None:
    """Ajoute une règle de calibration auto dans APPRENTISSAGES.md (section Calibration)."""
    if not APPRENTISSAGES_PATH.exists():
        print("[learn] APPRENTISSAGES.md not found, skipping calibration rule.", file=sys.stderr)
        return

    text = APPRENTISSAGES_PATH.read_text(encoding="utf-8")
    if rule_text in text:
        print("[learn] Calibration rule already present, skipping.", file=sys.stderr)
        return

    # Chercher la section "Ajustements de calibration actifs"
    marker = "### Ajustements de calibration actifs"
    if marker not in text:
        print("[learn] Calibration marker not found in APPRENTISSAGES.md, skipping.", file=sys.stderr)
        return

    # Insérer la nouvelle ligne après le header du tableau
    # Trouver la ligne de header | Ajustement | Motif | Depuis | Sur quel agent | Fin prévue |
    lines = text.splitlines()
    insert_idx = None
    for i, line in enumerate(lines):
        if marker in line:
            # Chercher la ligne de séparateur du tableau après le header
            for j in range(i + 1, min(i + 5, len(lines))):
                if "|" in lines[j] and "---" in lines[j]:
                    insert_idx = j + 1
                    break
            break

    if insert_idx is None:
        print("[learn] Could not find table separator in calibration section, skipping.", file=sys.stderr)
        return

    row = f"| {rule_text} | Win rate {bracket} = {observed:.0%} (cible {target:.0%}) | {today.isoformat()} | Scoring global | Réévaluer dans 20 signaux |"
    new_lines = lines[:insert_idx] + [row] + lines[insert_idx:]
    APPRENTISSAGES_PATH.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"[learn] Calibration rule appended to APPRENTISSAGES.md", file=sys.stderr)


# ---------------------------------------------------------------------------
# Calibration engine (NEW)
# ---------------------------------------------------------------------------


def parse_score(score_str: str) -> float | None:
    """Extrait un score numérique de '7.2/10', '7,2/10' ou '7.2'."""
    # Normaliser les décimales avec virgule
    normalized = score_str.replace(",", ".")
    m = re.search(r"([0-9]+\.?[0-9]*)", normalized)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def parse_j20_verdict(cell: str) -> tuple[str, float | None]:
    """
    Parse une cellule J+20 comme '✅ Hit (+13.0%)' ou '❌ Miss (-7.0%)'.
    Retourne (verdict, return_pct) où return_pct est un float (ex: 0.13 pour +13%).
    """
    cell = cell.strip()
    if cell.startswith("⏳"):
        return ("pending", None)
    if "✅ Hit" in cell:
        m = re.search(r"([+\-]?[0-9]+\.?[0-9]*)%", cell)
        ret = float(m.group(1)) / 100 if m else None
        return ("hit", ret)
    if "❌ Miss" in cell:
        m = re.search(r"([+\-]?[0-9]+\.?[0-9]*)%", cell)
        ret = float(m.group(1)) / 100 if m else None
        return ("miss", ret)
    if "⚪ Scratch" in cell:
        m = re.search(r"([+\-]?[0-9]+\.?[0-9]*)%", cell)
        ret = float(m.group(1)) / 100 if m else None
        return ("scratch", ret)
    if "🔄 Invalidé" in cell:
        return ("invalidated", None)
    return ("unknown", None)


def collect_completed_signals() -> list[dict]:
    """
    Parse BACKTESTING.md et retourne tous les signaux avec un verdict J+20 terminé
    (hit, miss, scratch ou invalidated).
    """
    if not BACKTESTING_PATH.exists():
        return []

    text = BACKTESTING_PATH.read_text(encoding="utf-8")
    rows = parse_markdown_table(text, ["Date signal", "Ticker", "Cours signal", "J+5"])
    signals = []

    for row in rows:
        ticker = row.get("Ticker", "").strip()
        score_str = row.get("Score", "").strip()
        signal_type = row.get("Type signal", "").strip()
        j20_cell = row.get("J+20", "").strip()

        if not ticker or not score_str:
            continue

        score = parse_score(score_str)
        if score is None:
            continue

        verdict, ret = parse_j20_verdict(j20_cell)
        if verdict == "pending":
            continue

        signals.append({
            "ticker": ticker,
            "score": score,
            "score_str": score_str,
            "type": signal_type,
            "j20_verdict": verdict,
            "j20_return": ret,
        })

    return signals


def compute_win_rates_by_bracket(signals: list[dict]) -> dict:
    """
    Calcule le win rate J+20 par fourchette de score.
    Un 'hit' = gagnant. Miss = perdant. Scratch = neutre (ne compte ni pour ni contre).
    """
    brackets = defaultdict(lambda: {"total": 0, "hits": 0, "misses": 0, "scratches": 0, "returns": []})

    for sig in signals:
        score = sig["score"]
        bracket = None
        for (low, high), _ in CALIBRATION_TARGETS.items():
            if low <= score <= high:
                bracket = f"{low}-{high}"
                break
        if bracket is None:
            continue

        b = brackets[bracket]
        b["total"] += 1
        if sig["j20_verdict"] == "hit":
            b["hits"] += 1
        elif sig["j20_verdict"] == "miss":
            b["misses"] += 1
        elif sig["j20_verdict"] == "scratch":
            b["scratches"] += 1
        if sig["j20_return"] is not None:
            b["returns"].append(sig["j20_return"])

    # Calculer les win rates
    result = {}
    for bracket, data in brackets.items():
        # Win rate = hits / (hits + misses) — scratches exclus
        denom = data["hits"] + data["misses"]
        win_rate = data["hits"] / denom if denom > 0 else 0.0
        avg_return = sum(data["returns"]) / len(data["returns"]) if data["returns"] else 0.0
        result[bracket] = {
            "total": data["total"],
            "hits": data["hits"],
            "misses": data["misses"],
            "scratches": data["scratches"],
            "win_rate": win_rate,
            "avg_return": avg_return,
        }

    return result


def detect_catalyst_streaks(signals: list[dict]) -> list[dict]:
    """
    Détecte les streaks de 3 hits ou 3 misses consécutifs sur le même type de catalyseur.
    Retourne une liste d'alertes à écrire dans APPRENTISSAGES.md.
    """
    # Grouper par type de catalyseur, trier par date (si disponible)
    # Pour simplifier, on regroupe tous les signaux du même type et on compte
    by_type = defaultdict(list)
    for sig in signals:
        by_type[sig["type"]].append(sig)

    alerts = []
    for ctype, sigs in by_type.items():
        if len(sigs) < 3:
            continue

        # Compter les hits / misses consécutifs (dans l'ordre du fichier)
        hits = [s for s in sigs if s["j20_verdict"] == "hit"]
        misses = [s for s in sigs if s["j20_verdict"] == "miss"]

        if len(misses) >= 3:
            alerts.append({
                "type": ctype,
                "streak": "miss",
                "count": len(misses),
                "action": f"Pénalité −0.5 pt sur le Score Catalyseur pour les signaux '{ctype}' sur les 5 prochains signaux.",
            })
        if len(hits) >= 3:
            alerts.append({
                "type": ctype,
                "streak": "hit",
                "count": len(hits),
                "action": f"Bonus +0.3 pt empirique sur le Score Catalyseur pour les signaux '{ctype}' sur les 5 prochains signaux.",
            })

    return alerts


def run_calibration() -> dict:
    """
    Moteur de calibration principal.
    1. Collecte les signaux terminés
    2. Calcule les win rates par fourchette
    3. Émet des règles de calibration si besoin
    4. Met à jour les tableaux de BACKTESTING.md
    5. Génère un rapport JSON
    """
    print("[learn] Starting calibration engine...", file=sys.stderr)

    signals = collect_completed_signals()
    if not signals:
        print("[learn] No completed J+20 signals found for calibration.", file=sys.stderr)
        return {"status": "no_data", "signals_checked": 0}

    print(f"[learn] {len(signals)} completed J+20 signals found.", file=sys.stderr)

    win_rates = compute_win_rates_by_bracket(signals)
    alerts = detect_catalyst_streaks(signals)

    # Émettre les ajustements
    adjustments = []
    for bracket, data in win_rates.items():
        if data["total"] < MIN_SIGNALS_FOR_CALIBRATION:
            continue

        # Trouver le target correspondant
        target = None
        for (low, high), t in CALIBRATION_TARGETS.items():
            br_name = f"{low}-{high}"
            if br_name == bracket:
                target = t
                break
        if target is None:
            continue

        observed = data["win_rate"]
        if observed < target - WIN_RATE_TOLERANCE:
            rule = (
                f"Win rate J+20 {bracket} = {observed:.0%} (cible {target:.0%}). "
                f"Appliquer malus −0.5 pt sur le Score Opportunité global "
                f"pour tous les signaux de cette fourchette jusqu'à réétalonnage."
            )
            append_calibration_rule(rule, bracket, observed, target)
            adjustments.append({
                "bracket": bracket,
                "observed_win_rate": observed,
                "target_win_rate": target,
                "action": "malus_-0.5",
                "signals_count": data["total"],
            })
            print(f"[learn] CALIBRATION ALERT: {bracket} win rate {observed:.0%} (target {target:.0%}) → malus -0.5pt", file=sys.stderr)
        elif observed > target + WIN_RATE_TOLERANCE:
            rule = (
                f"Win rate J+20 {bracket} = {observed:.0%} (cible {target:.0%}). "
                f"Appliquer bonus +0.3 pt sur le Score Opportunité global "
                f"pour confirmer le pattern gagnant."
            )
            append_calibration_rule(rule, bracket, observed, target)
            adjustments.append({
                "bracket": bracket,
                "observed_win_rate": observed,
                "target_win_rate": target,
                "action": "bonus_+0.3",
                "signals_count": data["total"],
            })
            print(f"[learn] CALIBRATION ALERT: {bracket} win rate {observed:.0%} (target {target:.0%}) → bonus +0.3pt", file=sys.stderr)

    # Émettre les streak alerts
    for alert in alerts:
        append_rule_to_apprentissages(
            alert["action"],
            f"Streak {alert['streak']} x{alert['count']} sur catalyseur '{alert['type']}'",
            "moyenne"
        )
        print(f"[learn] STREAK ALERT: {alert['type']} → {alert['action']}", file=sys.stderr)

    # Mettre à jour les tableaux agrégés dans BACKTESTING.md
    update_calibration_tables(win_rates, alerts)

    # Générer le rapport JSON
    report = {
        "date": today.isoformat(),
        "signals_total": len(signals),
        "win_rates_by_bracket": {
            k: {
                "total": v["total"],
                "hits": v["hits"],
                "misses": v["misses"],
                "win_rate": round(v["win_rate"], 4),
                "avg_return": round(v["avg_return"], 4),
            }
            for k, v in win_rates.items()
        },
        "adjustments": adjustments,
        "streak_alerts": alerts,
        "status": "calibrated" if adjustments else "ok",
    }

    CALIBRATION_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CALIBRATION_REPORT_PATH.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[learn] Calibration report → {CALIBRATION_REPORT_PATH}", file=sys.stderr)

    return report


def update_calibration_tables(win_rates: dict, alerts: list[dict]) -> None:
    """Met à jour les tableaux de calibration dans BACKTESTING.md."""
    if not BACKTESTING_PATH.exists():
        return

    text = BACKTESTING_PATH.read_text(encoding="utf-8")

    # Tableau "Par fourchette de score"
    rows = []
    for bracket, data in sorted(win_rates.items()):
        wr = f"{data['win_rate']:.0%}" if data['total'] > 0 else "—"
        avg_ret = f"{data['avg_return']:+.1%}" if data['total'] > 0 else "—"
        rows.append({
            "Score signal": bracket,
            "Signaux": str(data["total"]),
            "Win rate J+20": wr,
            "Gain moyen J+20": avg_ret,
        })

    if rows:
        text = replace_table_in_section(
            text,
            "### Par fourchette de score",
            ["Score signal", "Signaux", "Win rate"],
            rows
        )

    # Tableau "Par type de catalyseur"
    # Regrouper par type
    by_type = defaultdict(lambda: {"total": 0, "hits": 0})
    # Note: on n'a pas les types dans win_rates, il faudrait collecter plus d'infos
    # Pour l'instant, on ne met pas à jour ce tableau (les streak alerts suffisent)

    BACKTESTING_PATH.write_text(text, encoding="utf-8")
    print("[learn] BACKTESTING.md calibration tables updated.", file=sys.stderr)


# ---------------------------------------------------------------------------
# BACKTESTING updater
# ---------------------------------------------------------------------------


def process_backtesting() -> dict:
    stats = {"checked": 0, "hits": 0, "misses": 0, "scratches": 0, "post_mortems": 0}

    if not BACKTESTING_PATH.exists():
        print("[learn] BACKTESTING.md not found, skipping.", file=sys.stderr)
        return stats

    text = BACKTESTING_PATH.read_text(encoding="utf-8")
    rows = parse_markdown_table(text, ["Date signal", "Ticker", "Cours signal", "J+5"])
    if not rows:
        print("[learn] No backtesting table found.", file=sys.stderr)
        return stats

    updated_rows = []
    any_change = False

    for row in rows:
        ticker = row.get("Ticker", "").strip()
        signal_date_str = row.get("Date signal", "").strip()
        entry_price = parse_price(row.get("Cours signal", ""))
        score = row.get("Score", "").strip()
        signal_type = row.get("Type signal", "").strip()

        if not ticker or not signal_date_str or entry_price is None:
            updated_rows.append(row)
            continue

        try:
            signal_date = datetime.strptime(signal_date_str, "%Y-%m-%d").date()
        except ValueError:
            updated_rows.append(row)
            continue

        new_row = dict(row)
        for col_horizon, delta in HORIZONS_BT.items():
            if col_horizon not in new_row:
                continue
            cell = new_row[col_horizon].strip()
            if not cell.startswith("⏳"):
                continue

            target_date = signal_date + timedelta(days=delta)
            if target_date > today + timedelta(days=2):
                continue

            exit_price = get_close_on_date(ticker, target_date)
            if exit_price is None:
                if target_date == today:
                    exit_price = get_latest_json_price(ticker)
                if exit_price is None:
                    continue

            ret = (exit_price - entry_price) / entry_price
            verdict, ret_rounded = verdict_opportunity(ret)
            new_row[col_horizon] = f"{verdict} ({ret_rounded:+.1%})"
            stats["checked"] += 1
            if "✅ Hit" in verdict:
                stats["hits"] += 1
            elif "❌ Miss" in verdict:
                stats["misses"] += 1
                if col_horizon in ("J+20", "J+60"):
                    pm = generate_post_mortem(
                        ticker, signal_date_str, score, signal_type,
                        entry_price, col_horizon, exit_price, ret, verdict
                    )
                    save_post_mortem(pm)
                    append_rule_to_apprentissages(
                        pm["rule_extracted"],
                        f"Post-mortem {ticker} {signal_date_str} {col_horizon}",
                        pm["confidence"]
                    )
                    new_row["Post-mortem"] = f"[Post-mortem {today}]"
                    stats["post_mortems"] += 1
            else:
                stats["scratches"] += 1
            any_change = True

        updated_rows.append(new_row)

    if any_change:
        new_text = replace_table_rows(text, ["Date signal", "Ticker", "Cours signal", "J+5"], updated_rows)
        BACKTESTING_PATH.write_text(new_text, encoding="utf-8")
        print(f"[learn] BACKTESTING.md updated.", file=sys.stderr)

    return stats


# ---------------------------------------------------------------------------
# SUIVI_PRIX_CIBLES updater
# ---------------------------------------------------------------------------


def process_suivi_prix() -> dict:
    stats = {"checked": 0, "hits": 0, "partiels": 0, "misses": 0}

    if not SUIVI_PRIX_PATH.exists():
        print("[learn] SUIVI_PRIX_CIBLES.md not found, skipping.", file=sys.stderr)
        return stats

    text = SUIVI_PRIX_PATH.read_text(encoding="utf-8")
    rows = parse_markdown_table(text, ["Date analyse", "Ticker", "Prix cible", "J+30"])
    if not rows:
        print("[learn] No price target table found.", file=sys.stderr)
        return stats

    updated_rows = []
    any_change = False

    for row in rows:
        ticker = row.get("Ticker", "").strip()
        date_str = row.get("Date analyse", "").strip()
        price_target = parse_price(row.get("Prix cible", ""))
        reco = row.get("Reco", "").strip()
        entry_price = parse_price(row.get("Cours à l'analyse", ""))

        if not ticker or not date_str or price_target is None:
            updated_rows.append(row)
            continue

        try:
            analysis_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            updated_rows.append(row)
            continue

        new_row = dict(row)
        for col_horizon, delta in HORIZONS_PC.items():
            if col_horizon not in new_row:
                continue
            cell = new_row[col_horizon].strip()
            if not cell.startswith("⏳") and not cell.startswith("202"):
                continue

            target_date = analysis_date + timedelta(days=delta)
            if target_date > today + timedelta(days=2):
                continue

            window_price = get_close_on_date(ticker, target_date)
            if window_price is None:
                if target_date == today:
                    window_price = get_latest_json_price(ticker)
                if window_price is None:
                    continue

            verdict = verdict_price_target(price_target, reco, window_price)
            new_row[col_horizon] = verdict
            new_row["Verdict final"] = verdict
            stats["checked"] += 1
            if verdict == "✅ Hit":
                stats["hits"] += 1
            elif verdict == "⚠️ Partiel":
                stats["partiels"] += 1
            elif verdict == "❌ Miss":
                stats["misses"] += 1
                pm = generate_post_mortem(
                    ticker, date_str, "—", "Prix cible", entry_price or price_target,
                    col_horizon, window_price,
                    (window_price - (entry_price or price_target)) / (entry_price or price_target),
                    verdict
                )
                pm["rule_extracted"] = (
                    "Si prix cible rate avec une erreur > 20% → revérifier le Filtre Qualité "
                    "et les hypothèses de DCF avant prochaine émission de PT sur ce ticker."
                )
                save_post_mortem(pm)
                append_rule_to_apprentissages(
                    pm["rule_extracted"],
                    f"Post-mortem prix cible {ticker} {date_str}",
                    "moyenne"
                )
            any_change = True

        updated_rows.append(new_row)

    if any_change:
        new_text = replace_table_rows(text, ["Date analyse", "Ticker", "Prix cible", "J+30"], updated_rows)
        SUIVI_PRIX_PATH.write_text(new_text, encoding="utf-8")
        print(f"[learn] SUIVI_PRIX_CIBLES.md updated.", file=sys.stderr)

    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print(f"[learn] Starting learning loop — {today.isoformat()}", file=sys.stderr)

    bt_stats = process_backtesting()
    pc_stats = process_suivi_prix()

    total_checked = bt_stats["checked"] + pc_stats["checked"]
    total_hits = bt_stats["hits"] + pc_stats["hits"]
    total_misses = bt_stats["misses"] + pc_stats["misses"]

    print(
        f"[learn] Done — {total_checked} windows checked | "
        f"{total_hits} hits | {total_misses} misses | "
        f"{bt_stats['post_mortems']} post-mortems generated",
        file=sys.stderr
    )

    # Étape 4 : calibration automatique des scores
    calibration = run_calibration()

    return 0


if __name__ == "__main__":
    sys.exit(main())
