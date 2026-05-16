#!/usr/bin/env python3
"""
agent_fx.py — Agent FX Exposure.

Mesure l'exposition de chaque ticker aux fluctuations de change (USD, EUR, JPY, CNY)
et chiffre l'impact estimé sur les revenus et les EPS.

Usage:
    python scripts/agent_fx.py

Output:
    data/fx_exposure_YYYY-MM-DD.json  (symlink latest)
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
LATEST_PATH = DATA_DIR / "latest.json"

# Exposition FX par défaut par secteur (estimation basée sur données sectorielles)
# Valeurs = % revenus hors-USD estimés
SECTOR_FX_EXPOSURE = {
    "Tech": {"exposure_pct": 55, "primary_currency": "EUR/CNY", "direction": "export"},
    "Semi-conducteurs / IA": {"exposure_pct": 60, "primary_currency": "CNY/EUR", "direction": "export"},
    "Énergie": {"exposure_pct": 40, "primary_currency": "USD", "direction": "commodity_usd"},
    "Défense / Aérospatial": {"exposure_pct": 25, "primary_currency": "USD", "direction": "domestic_usd"},
    "Infrastructure IA / Hardware": {"exposure_pct": 45, "primary_currency": "EUR/CNY", "direction": "export"},
    "IA Infrastructure / Bitcoin Mining": {"exposure_pct": 15, "primary_currency": "CAD", "direction": "mixed"},
    "Financial Services": {"exposure_pct": 20, "primary_currency": "USD", "direction": "domestic_usd"},
    "Healthcare": {"exposure_pct": 30, "primary_currency": "EUR", "direction": "export"},
    "Consommation discrétionnaire": {"exposure_pct": 40, "primary_currency": "EUR/CNY", "direction": "export"},
    "Matériaux / Mines": {"exposure_pct": 50, "primary_currency": "USD", "direction": "commodity_usd"},
    "Utilities": {"exposure_pct": 5, "primary_currency": "USD", "direction": "domestic_usd"},
    "Immobilier (REIT)": {"exposure_pct": 10, "primary_currency": "USD", "direction": "domestic_usd"},
}

# Impact estimé par direction et devise
# DXY +1% → impact sur revenus (approximatif)
IMPACT_MATRIX = {
    "export": {  # Exportateur US : bénéficie d'un USD faible, pénalisé par USD fort
        "eur": -3.0,   # DXY +1% → EUR/USD baisse → exports US plus chers en Europe
        "cny": -4.0,   # DXY +1% → USD/CNY hausse → exports US plus chers en Chine
        "jpy": -2.5,
        "cad": -1.5,
        "gbp": -2.0,
        "mxn": -2.0,
    },
    "import": {  # Importateur US : bénéficie d'un USD fort
        "eur": +2.5,   # DXY +1% → imports depuis Europe moins chers
        "cny": +3.5,
        "jpy": +2.0,
        "cad": +1.5,
        "gbp": +1.5,
        "mxn": +2.0,
    },
    "commodity_usd": {  # Commodités en USD : bénéficie d'un USD fort (commodités moins chères en USD)
        "usd": +2.0,   # DXY +1% → commodities en baisse en USD → coûts moins chers
    },
    "domestic_usd": {  # Domestic pur
        "usd": 0.0,
    },
    "mixed": {  # Mixte
        "usd": -0.5,
        "cad": -0.5,
    },
}


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_latest_snapshot():
    if not LATEST_PATH.exists():
        return {}
    with open(LATEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_fx_changes(snapshot: dict) -> dict:
    """Extrait les variations FX depuis le snapshot macro."""
    macro_data = snapshot.get("macro", {}).get("data", {})
    fx = {}
    for key in ["dxy", "eurusd", "usdjpy"]:
        item = macro_data.get(key, {})
        if item and item.get("value") is not None:
            fx[key] = {
                "value": item["value"],
                "change_pct": item.get("change_pct", 0),
            }
    return fx


def estimate_ticker_fx_exposure(ticker_data: dict, snapshot: dict) -> dict:
    """
    Estime l'exposition FX d'un ticker à partir de son secteur et des données disponibles.
    """
    ticker = ticker_data["ticker"]
    sector = ticker_data.get("sector", "")

    # Cherche le mapping sectoriel
    sector_config = None
    for sec_key, sec_val in SECTOR_FX_EXPOSURE.items():
        if sec_key.lower() in sector.lower():
            sector_config = sec_val
            break

    if sector_config is None:
        # Défaut : exposition modérée
        sector_config = {"exposure_pct": 25, "primary_currency": "USD", "direction": "export"}

    exposure_pct = sector_config["exposure_pct"]
    direction = sector_config["direction"]

    # Données FX
    fx = get_fx_changes(snapshot)
    dxy_change = fx.get("dxy", {}).get("change_pct", 0)
    eurusd_change = fx.get("eurusd", {}).get("change_pct", 0)

    # Calcul de l'impact estimé sur revenus
    # Simplification : on utilise la variation DXY comme proxy principal
    # DXY hausse = USD fort = généralement négatif pour exportateurs US
    impact_revenue_pct = 0.0
    if direction == "export":
        # DXY +1% → revenus hors-USD convertis en USD = baisse
        impact_revenue_pct = dxy_change * (-exposure_pct / 100) * 1.5
    elif direction == "import":
        # DXY +1% → imports moins chers = positif
        impact_revenue_pct = dxy_change * (exposure_pct / 100) * 0.8
    elif direction == "commodity_usd":
        # DXY +1% → commodities en baisse = coûts moins chers = positif
        impact_revenue_pct = dxy_change * (exposure_pct / 100) * 0.5
    elif direction == "mixed":
        impact_revenue_pct = dxy_change * (-exposure_pct / 100) * 0.3

    # Impact EPS (leveraging opérationnel approximatif)
    impact_eps_pct = impact_revenue_pct * 1.5

    # Score FX Impact /10
    # Haut = mauvais (exposition + headwind)
    # Bas = bon (peu d'exposition ou tailwind)
    headwind_score = min(abs(impact_revenue_pct) * 2, 10)
    if impact_revenue_pct < 0:
        direction_label = "headwind"
    elif impact_revenue_pct > 0:
        direction_label = "tailwind"
    else:
        direction_label = "neutral"

    # Détection divergence
    price_change = snapshot.get("prices", {}).get(ticker, {}).get("price", {}).get("change_pct", 0)
    expected_change = impact_revenue_pct * 0.3  # Le cours ne bouge pas 1:1 avec le FX
    divergence = price_change - expected_change if expected_change != 0 else 0

    divergence_flag = "aligned"
    if abs(divergence) > 3:
        divergence_flag = "underperformance" if divergence < 0 else "outperformance"

    return {
        "ticker": ticker,
        "sector": sector,
        "exposure_pct": exposure_pct,
        "direction": direction,
        "primary_currency": sector_config["primary_currency"],
        "dxy_change_pct": round(dxy_change, 2),
        "eurusd_change_pct": round(eurusd_change, 2),
        "impact_revenue_pct": round(impact_revenue_pct, 2),
        "impact_eps_pct": round(impact_eps_pct, 2),
        "fx_impact_score": round(headwind_score, 1),
        "direction_label": direction_label,
        "price_change_pct": round(price_change, 2) if price_change else None,
        "expected_price_change_pct": round(expected_change, 2),
        "divergence_flag": divergence_flag,
        "flag": "🔴" if headwind_score >= 7 else "🟡" if headwind_score >= 4 else "🟢",
    }


def main():
    print("[fx] Starting FX exposure scan...", file=sys.stderr)

    config = load_config()
    tickers_data = config.get("tickers", [])
    snapshot = load_latest_snapshot()

    if not snapshot:
        print("[fx] ERROR: No snapshot found at data/latest.json", file=sys.stderr)
        return 1

    fx = get_fx_changes(snapshot)
    if not fx:
        print("[fx] WARNING: No FX data in snapshot", file=sys.stderr)

    print(f"[fx] DXY change: {fx.get('dxy', {}).get('change_pct', 'N/A')}%", file=sys.stderr)
    print(f"[fx] EUR/USD change: {fx.get('eurusd', {}).get('change_pct', 'N/A')}%", file=sys.stderr)

    results = []
    for ticker_data in tickers_data:
        ticker = ticker_data["ticker"]
        print(f"[fx] Analyzing {ticker}...", file=sys.stderr)
        exposure = estimate_ticker_fx_exposure(ticker_data, snapshot)
        results.append(exposure)

        print(
            f"[fx]   {ticker}: Score {exposure['fx_impact_score']}/10 "
            f"{exposure['flag']} | {exposure['direction_label']} | "
            f"Impact EPS: {exposure['impact_eps_pct']}%",
            file=sys.stderr
        )

    # Build report
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report = {
        "meta": {
            "date": date_str,
            "dxy_change_pct": fx.get("dxy", {}).get("change_pct", 0),
            "eurusd_change_pct": fx.get("eurusd", {}).get("change_pct", 0),
            "usdjpy_change_pct": fx.get("usdjpy", {}).get("change_pct", 0),
            "tickers_analyzed": len(results),
            "flagged_high": sum(1 for r in results if r["fx_impact_score"] >= 7),
        },
        "tickers": results,
    }

    # Write report
    output_path = DATA_DIR / f"fx_exposure_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "fx_exposure_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    flagged = [r["ticker"] for r in results if r["fx_impact_score"] >= 7]
    print(
        f"[fx] Report written → {output_path} | "
        f"Analyzed: {len(results)} | Flagged: {len(flagged)}",
        file=sys.stderr
    )

    if flagged:
        print(f"[fx] 🔴 High FX-risk tickers: {', '.join(flagged)}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
