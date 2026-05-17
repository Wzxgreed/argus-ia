#!/usr/bin/env python3
"""
data_quality_gate.py — Détecteur de données pourries post-fetch.

S'exécute immédiatement après fetch_prices.py pour détecter :
  • Cours stale (close identique sur 2+ jours)
  • Volume anomalie (volume == 0 alors que marché ouvert)
  • Spread aberrant ((high-low)/close > seuil selon market cap)
  • High/Low incohérents
  • RSI/ATR placeholders (50.0 exact, 0.01)
  • Écart inter-jours > 25%
  • Données FMP placeholders (num_analysts == 0 + price_target_avg == 0)

Usage:
    python agents/data_quality_gate/agent.py

Output:
    data/quality_report_YYYY-MM-DD.json  (symlink quality_report_latest.json)
    Modifie data/latest.json in-place (ajoute _quality_gate par ticker)
"""

import json
import os
import re
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = DATA_DIR

# ---------------------------------------------------------------------------
# Seuils
# ---------------------------------------------------------------------------
STALE_DAYS_THRESHOLD = 2          # close identique sur N jours consécutifs
VOLUME_ZERO_THRESHOLD = 0           # volume == 0
SPREAD_THRESHOLDS = {
    "large": 0.15,   # market_cap > 50B
    "mid": 0.30,     # market_cap 10B–50B
    "small": 0.50,   # market_cap < 10B
}
RSI_PLACEHOLDER = 50.0
ATR_PLACEHOLDER_LOW = 0.01
ATR_PLACEHOLDER_HIGH = 0.01
CHANGE_PCT_ABERRANT = 25.0


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load_latest() -> dict:
    latest = DATA_DIR / "latest.json"
    if not latest.exists():
        return {}
    target = latest.resolve()
    with open(target, "r", encoding="utf-8") as f:
        return json.load(f)


def load_historical_snapshots(days: int = 3) -> list[dict]:
    """Charge les N derniers snapshots datés avant aujourd'hui."""
    today = date.today()
    snapshots = []
    for i in range(1, days + 1):
        d = today - __import__("datetime").timedelta(days=i)
        path = DATA_DIR / f"{d.isoformat()}.json"
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    snapshots.append(json.load(f))
            except Exception:
                pass
    return snapshots


def classify_market_cap(market_cap: float | None) -> str:
    if market_cap is None:
        return "small"
    if market_cap > 50_000_000_000:
        return "large"
    if market_cap > 10_000_000_000:
        return "mid"
    return "small"


def is_market_open(ticker_data: dict, hist_snapshots: list[dict]) -> bool:
    """Heuristique : si le ticker a eu du volume hier, le marché est probablement ouvert."""
    for snap in hist_snapshots:
        prev = snap.get("prices", {}).get(ticker_data.get("ticker"), {})
        vol = prev.get("price", {}).get("volume")
        if vol and vol > 0:
            return True
    # Fallback : si c'est un weekend
    weekday = datetime.now(timezone.utc).weekday()
    return weekday < 5  # Mon-Fri


def check_ticker(ticker: str, data: dict, hist_snapshots: list[dict]) -> dict:
    """Retourne un dict {status, reasons[]} pour un ticker."""
    reasons = []
    price = data.get("price", {})
    tech = data.get("technical", {})
    fund = data.get("fundamentals", {})
    opts = data.get("options", {})
    fmp = data.get("fmp_consensus", {})

    close = price.get("close")
    high = price.get("high")
    low = price.get("low")
    volume = price.get("volume")
    change_pct = price.get("change_pct")
    prev_close = price.get("previous_close")
    rsi = tech.get("rsi14")
    atr = tech.get("atr14")
    market_cap = fund.get("market_cap")
    mc_class = classify_market_cap(market_cap)

    # 1. Cours stale
    if close is not None and prev_close is not None:
        if close == prev_close and change_pct == 0:
            reasons.append({
                "type": "stale_price",
                "severity": "WARNING",
                "message": f"close({close}) == previous_close({prev_close}) et change_pct=0 — cours potentiellement stale",
            })
    stale_count = 0
    for snap in hist_snapshots:
        prev = snap.get("prices", {}).get(ticker, {})
        prev_close = prev.get("price", {}).get("close")
        if prev_close is not None and close is not None and prev_close == close:
            stale_count += 1
    if stale_count >= STALE_DAYS_THRESHOLD:
        reasons.append({
            "type": "stale_price_history",
            "severity": "CRITICAL",
            "message": f"close identique sur {stale_count + 1} jours consécutifs (incluant aujourd'hui)",
        })

    # 2. Volume anomalie
    if volume == 0 and is_market_open(data, hist_snapshots):
        reasons.append({
            "type": "zero_volume",
            "severity": "WARNING" if mc_class != "large" else "CRITICAL",
            "message": "volume == 0 alors que le marché semble ouvert",
        })

    # 3. Spread aberrant
    if close and high and low and close > 0:
        spread = (high - low) / close
        threshold = SPREAD_THRESHOLDS.get(mc_class, 0.50)
        if spread > threshold:
            reasons.append({
                "type": "abnormal_spread",
                "severity": "WARNING",
                "message": f"spread {(spread*100):.1f}% > seuil {threshold*100:.0f}% ({mc_class} cap)",
            })
        # High/Low incohérents
        if high < close:
            reasons.append({
                "type": "incoherent_high",
                "severity": "CRITICAL",
                "message": f"high({high}) < close({close})",
            })
        if low > close:
            reasons.append({
                "type": "incoherent_low",
                "severity": "CRITICAL",
                "message": f"low({low}) > close({close})",
            })

    # 4. RSI/ATR placeholders
    if rsi is not None and abs(rsi - RSI_PLACEHOLDER) < 0.01:
        reasons.append({
            "type": "rsi_placeholder",
            "severity": "WARNING",
            "message": f"RSI={rsi} (valeur par défaut suspecte 50.0)",
        })
    if atr is not None and 0 < atr <= ATR_PLACEHOLDER_HIGH:
        reasons.append({
            "type": "atr_placeholder",
            "severity": "WARNING",
            "message": f"ATR={atr} (valeur anormalement basse, probablement placeholder)",
        })

    # 5. Écart inter-jours aberrant
    if change_pct is not None and abs(change_pct) > CHANGE_PCT_ABERRANT:
        reasons.append({
            "type": "abnormal_change_pct",
            "severity": "WARNING",
            "message": f"change_pct={change_pct}% > {CHANGE_PCT_ABERRANT}% — vérifier événement majeur",
        })

    # 6. Données FMP placeholders
    if fmp:
        num_analysts = fmp.get("num_analysts")
        pt_avg = fmp.get("price_target_avg")
        if (num_analysts == 0 or num_analysts is None) and (pt_avg == 0 or pt_avg is None):
            reasons.append({
                "type": "fmp_placeholder",
                "severity": "WARNING",
                "message": "fmp_consensus vide (num_analysts=0, price_target_avg=0)",
            })

    # Détermination du status global
    if any(r["severity"] == "CRITICAL" for r in reasons):
        status = "excluded"
    elif reasons:
        status = "warning"
    else:
        status = "ok"

    return {"status": status, "reasons": reasons}


def check_macro(latest: dict, hist_snapshots: list[dict]) -> list[dict]:
    reasons = []
    macro = latest.get("macro", {})
    if not macro:
        reasons.append({"type": "macro_missing", "severity": "CRITICAL", "message": "Bloc macro absent du snapshot"})
        return reasons

    regime = macro.get("regime")
    if not regime:
        reasons.append({"type": "macro_regime_missing", "severity": "WARNING", "message": "Régime macro non déterminé"})

    macro_data = macro.get("data", {})
    vix = macro_data.get("vix", {}).get("value")
    if vix is None:
        reasons.append({"type": "macro_vix_missing", "severity": "WARNING", "message": "VIX absent des données macro"})

    # Vérifier si le régime macro est identique depuis 2 jours (pas forcément un problème, juste un flag)
    same_regime_count = 0
    for snap in hist_snapshots:
        prev_regime = snap.get("macro", {}).get("regime")
        if prev_regime and prev_regime == regime:
            same_regime_count += 1
    # Pas d'alerte sur régime stable — c'est normal

    return reasons


def main():
    latest = load_latest()
    if not latest:
        print("[data_quality_gate] ERREUR: latest.json vide ou inexistant.", file=sys.stderr)
        return 1

    hist = load_historical_snapshots(days=3)
    prices = latest.get("prices", {})
    report = {
        "meta": {
            "date": today_str(),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "tickers_scanned": len(prices),
            "snapshots_history_used": len(hist),
        },
        "tickers": {},
        "global": {},
    }

    ok_count = 0
    warning_count = 0
    excluded_count = 0

    for ticker, data in prices.items():
        if data.get("error"):
            # Les tickers en erreur sont déjà signalés par fetch_prices
            continue
        result = check_ticker(ticker, data, hist)
        report["tickers"][ticker] = result
        data["_quality_gate"] = result

        if result["status"] == "ok":
            ok_count += 1
        elif result["status"] == "warning":
            warning_count += 1
        else:
            excluded_count += 1

    # Macro checks
    macro_reasons = check_macro(latest, hist)
    report["global"]["macro"] = macro_reasons
    report["global"]["summary"] = {
        "ok": ok_count,
        "warning": warning_count,
        "excluded": excluded_count,
    }

    # Écrire le rapport JSON
    date_str = today_str()
    report_path = REPORT_DIR / f"quality_report_{date_str}.json"
    with tempfile.NamedTemporaryFile(mode="w", dir=REPORT_DIR, delete=False, suffix=".json") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        temp_path = f.name
    os.replace(temp_path, report_path)

    # Symlink
    latest_link = REPORT_DIR / "quality_report_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(report_path.relative_to(REPORT_DIR))

    # Réécrire latest.json avec les champs _quality_gate injectés
    latest_path = DATA_DIR / f"{date_str}.json"
    if latest_path.exists():
        with tempfile.NamedTemporaryFile(mode="w", dir=DATA_DIR, delete=False, suffix=".json") as f:
            json.dump(latest, f, indent=2, ensure_ascii=False)
            temp_path = f.name
        os.replace(temp_path, latest_path)

        # Mettre à jour le symlink latest.json
        link = DATA_DIR / "latest.json"
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(latest_path.relative_to(DATA_DIR))

    # Log
    print(
        f"[data_quality_gate] {ok_count} OK, {warning_count} WARNING, {excluded_count} EXCLUDED",
        file=sys.stderr,
    )
    for ticker, result in report["tickers"].items():
        if result["status"] != "ok":
            sev = "🔴" if result["status"] == "excluded" else "🟡"
            msgs = "; ".join(r["message"] for r in result["reasons"])
            print(f"[data_quality_gate]   {sev} {ticker}: {msgs}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
