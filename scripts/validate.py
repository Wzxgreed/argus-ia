#!/usr/bin/env python3
"""
validate.py — Sanity checks sur le snapshot quotidien.

Usage:
    python scripts/validate.py

Output:
    data/validation_report.txt  (lu par l'agent en début de session)
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORT_PATH = DATA_DIR / "validation_report.txt"


def load_latest() -> dict:
    latest = DATA_DIR / "latest.json"
    if not latest.exists():
        return {}
    target = latest.resolve()
    with open(target, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_snapshot(snapshot: dict) -> list:
    issues = []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # 1. Fichier vide ou mal formé
    if not snapshot:
        issues.append("[CRITICAL] Snapshot latest.json est vide ou inexistant.")
        return issues

    meta = snapshot.get("meta", {})
    prices = snapshot.get("prices", {})
    macro = snapshot.get("macro", {})

    # 2. Date du snapshot
    snap_date = meta.get("date", "")
    if snap_date != today:
        issues.append(f"[WARNING] Snapshot date={snap_date} ≠ today={today}. Données potentiellement obsolètes.")

    # 3. Vérification par ticker
    missing_tickers = []
    for ticker, data in prices.items():
        if data.get("error"):
            missing_tickers.append(ticker)
            issues.append(f"[ERROR] {ticker}: fetch failed — {data.get('reason', 'unknown')}")
            continue

        price = data.get("price", {})
        tech = data.get("technical", {})
        fund = data.get("fundamentals", {})
        opts = data.get("options", {})

        # 3a. Prix > 0
        close = price.get("close")
        if close is None or close <= 0:
            issues.append(f"[ERROR] {ticker}: close price missing or invalid ({close}).")

        # 3b. Variation < 50% (split ou flash crash)
        change_pct = price.get("change_pct")
        if change_pct is not None and abs(change_pct) > 50:
            issues.append(f"[WARNING] {ticker}: change {change_pct}% — possible stock split or data error.")

        # 3c. Volume > 0
        vol = price.get("volume")
        if vol is None or vol == 0:
            issues.append(f"[WARNING] {ticker}: volume is 0 — market closed or delisted?")

        # 3d. RSI dans range plausible
        rsi = tech.get("rsi14")
        if rsi is not None and (rsi < 0 or rsi > 100):
            issues.append(f"[ERROR] {ticker}: RSI={rsi} hors range [0,100].")

        # 3e. Short interest plausible
        si = fund.get("short_interest_pct")
        if si is not None and (si < 0 or si > 1.0):
            issues.append(f"[ERROR] {ticker}: SI={si} hors range [0,1].")

        # 3f. ATR plausible (pas 10x le prix)
        atr = tech.get("atr14")
        if atr is not None and close and atr > close * 10:
            issues.append(f"[ERROR] {ticker}: ATR={atr} > 10× close={close} — calcul error.")

        # 3g. Options : put/call ratio plausible
        pcr = opts.get("put_call_ratio")
        if pcr is not None and pcr < 0:
            issues.append(f"[ERROR] {ticker}: put/call ratio={pcr} < 0.")

    # 4. Macro checks
    macro_data = macro.get("data", {})
    for key, val in macro_data.items():
        if val.get("error"):
            issues.append(f"[WARNING] Macro {key}: fetch failed — {val.get('reason')}")

    vix = macro_data.get("vix", {}).get("value")
    if vix is not None and vix < 5:
        issues.append(f"[WARNING] VIX={vix} — valeur anormalement basse, vérifier données.")

    # 5. Résumé global
    total_tickers = len(prices)
    ok_tickers = total_tickers - len(missing_tickers)
    issues.insert(0, f"[SUMMARY] {ok_tickers}/{total_tickers} tickers OK. {len([i for i in issues if i.startswith('[ERROR]')])} errors, {len([i for i in issues if i.startswith('[WARNING]')])} warnings.")

    return issues


def main():
    snapshot = load_latest()
    issues = validate_snapshot(snapshot)

    report = "=" * 60 + "\n"
    report += f"VALIDATION REPORT — {datetime.now(timezone.utc).isoformat()}\n"
    report += "=" * 60 + "\n"
    for issue in issues:
        report += issue + "\n"
    report += "=" * 60 + "\n"
    report += "INSTRUCTION POUR L'AGENT :\n"
    report += "- Si [CRITICAL] ou >2 [ERROR] : STOP. Ne pas lancer l'analyse du jour.\n"
    report += "- Si [WARNING] sur un ticker : noter [DONNÉES PARTIELLES] dans l'analyse.\n"
    report += "- Si [SUMMARY] 100% OK : utiliser les données normalement.\n"
    report += "=" * 60 + "\n"

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    print(report, file=sys.stderr)

    # Exit code : 0 si OK, 1 si erreurs critiques
    critical = any("[CRITICAL]" in i for i in issues)
    errors = sum(1 for i in issues if i.startswith("[ERROR]"))
    if critical or errors > 2:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
