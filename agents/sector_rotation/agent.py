#!/usr/bin/env python3
"""
agent_sector_rotation.py — Agent Rotation Sectorielle.

Protocol : `agents/sector_rotation/protocol.md`

Surveille la rotation sectorielle via les ETFs SPDR :
  • Calcul de la force relative (RS) 20j et 60j vs SPY
  • Détection des crossovers (RS 20j traverse RS 60j)
  • Corrélation avec le régime macro (risk-on / risk-off / stagflation)
  • Ranking sectoriel + signaux d'alerte

Output :
  data/sector_rotation_YYYY-MM-DD.json + symlink latest
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import yfinance as yf
import pandas as pd

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

SECTOR_ETFS = {
    "XLK": {"name": "Technology", "type": "cyclical_growth"},
    "XLE": {"name": "Energy", "type": "cyclical_value"},
    "XLF": {"name": "Financials", "type": "cyclical_value"},
    "XLI": {"name": "Industrials", "type": "cyclical"},
    "XLU": {"name": "Utilities", "type": "defensive"},
    "XLV": {"name": "Healthcare", "type": "defensive"},
    "XLP": {"name": "Consumer Staples", "type": "defensive"},
    "XLY": {"name": "Consumer Discretionary", "type": "cyclical_growth"},
    "XLB": {"name": "Materials", "type": "cyclical"},
    "XLRE": {"name": "Real Estate", "type": "rate_sensitive"},
    "XLC": {"name": "Communication Services", "type": "cyclical_growth"},
}

BENCHMARK = "SPY"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_history(ticker: str, period: str = "90d") -> pd.DataFrame | None:
    """Récupère l'historique de prix via yfinance."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        if hist.empty:
            return None
        return hist
    except Exception as e:
        print(f"[sector] Error fetching {ticker}: {e}", file=sys.stderr)
        return None


def calc_return(df: pd.DataFrame, days: int) -> float:
    """Calcule le rendement sur N jours glissants."""
    if df is None or len(df) < days + 1:
        return 0.0
    start = float(df["Close"].iloc[-(days + 1)])
    end = float(df["Close"].iloc[-1])
    return (end / start - 1) if start > 0 else 0.0


def relative_strength(sector_return: float, benchmark_return: float) -> float:
    """Force relative = excess return vs benchmark (pas un ratio de prix)."""
    if benchmark_return == 0:
        return sector_return
    return sector_return - benchmark_return


def detect_crossover(rs20: float, rs60: float, prev_rs20: float | None, prev_rs60: float | None) -> str | None:
    """Détecte un crossover de la force relative 20j vs 60j."""
    if prev_rs20 is None or prev_rs60 is None:
        return None
    was_below = prev_rs20 < prev_rs60
    is_above = rs20 > rs60
    was_above = prev_rs20 > prev_rs60
    is_below = rs20 < rs60

    if was_below and is_above:
        return "BULLISH_CROSSOVER"
    if was_above and is_below:
        return "BEARISH_CROSSOVER"
    return None


def load_macro_regime() -> str:
    """Lit le régime macro dans data/latest.json si disponible."""
    latest = DATA_DIR / "latest.json"
    if not latest.exists() or latest.is_symlink() and not latest.resolve().exists():
        return "UNKNOWN"
    try:
        with open(latest, "r", encoding="utf-8") as f:
            data = json.load(f)
        macro = data.get("macro", {})
        regime = macro.get("regime", "UNKNOWN")
        return regime if regime else "UNKNOWN"
    except Exception:
        return "UNKNOWN"


def regime_sector_score(sector_type: str, regime: str) -> float:
    """Score d'alignement secteur ↔ régime macro (-2 à +2)."""
    mapping = {
        "Risk-on/Bull": {
            "cyclical_growth": 2.0,
            "cyclical": 1.0,
            "cyclical_value": 0.5,
            "defensive": -1.5,
            "rate_sensitive": 0.0,
        },
        "Risk-off": {
            "defensive": 2.0,
            "rate_sensitive": 0.5,
            "cyclical_value": -0.5,
            "cyclical": -1.0,
            "cyclical_growth": -2.0,
        },
        "Stagflation": {
            "cyclical_value": 2.0,
            "cyclical": 1.0,
            "defensive": 0.5,
            "cyclical_growth": -1.0,
            "rate_sensitive": -1.5,
        },
        "Pre-FOMC": {
            "rate_sensitive": -1.0,
            "cyclical_growth": -0.5,
            "defensive": 0.5,
            "cyclical_value": 0.0,
        },
        "Normal": {
            "cyclical_growth": 1.0,
            "cyclical": 0.5,
            "defensive": 0.0,
            "cyclical_value": 0.0,
            "rate_sensitive": 0.0,
        },
        "Pre-earnings": {
            "cyclical_growth": 0.5,
            "cyclical": 0.0,
            "defensive": 0.0,
            "cyclical_value": 0.0,
            "rate_sensitive": 0.0,
        },
        "Recession": {
            "defensive": 2.0,
            "rate_sensitive": 1.0,
            "cyclical": -1.5,
            "cyclical_value": -1.0,
            "cyclical_growth": -2.0,
        },
    }
    return mapping.get(regime, {}).get(sector_type, 0.0)


def compute_momentum_score(rs20: float, rs60: float, regime_score: float) -> float:
    """Score momentum composite /10."""
    # Base = moyenne des RS (pondérée courte)
    base = rs20 * 0.6 + rs60 * 0.4
    # Convertir en score 0-10 (base typique entre -0.10 et +0.10)
    score = (base + 0.05) * 100  # centrer
    score = max(0.0, min(10.0, score))
    # Ajustement régime
    score += regime_score
    return round(max(0.0, min(10.0, score)), 2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("[sector] Starting sector rotation scan...", file=sys.stderr)

    # Fetch benchmark
    df_spy = fetch_history(BENCHMARK, period="120d")
    if df_spy is None or len(df_spy) < 60:
        print("[sector] ⚠️ SPY data unavailable. Skipping.", file=sys.stderr)
        return 0

    spy_ret_20 = calc_return(df_spy, 20)
    spy_ret_60 = calc_return(df_spy, 60)
    print(f"[sector] SPY return: 20d={spy_ret_20:+.2%}, 60d={spy_ret_60:+.2%}", file=sys.stderr)

    # Fetch previous day's data for crossover detection (if available)
    prev_spy = df_spy.iloc[:-1] if len(df_spy) > 1 else None
    spy_ret_20_prev = calc_return(prev_spy, 20) if prev_spy is not None and len(prev_spy) >= 20 else None
    spy_ret_60_prev = calc_return(prev_spy, 60) if prev_spy is not None and len(prev_spy) >= 60 else None

    regime = load_macro_regime()
    print(f"[sector] Macro regime: {regime}", file=sys.stderr)

    results = []
    crossovers = []

    for ticker, meta in SECTOR_ETFS.items():
        print(f"[sector] Analyzing {ticker} ({meta['name']})...", file=sys.stderr)
        df = fetch_history(ticker, period="120d")
        if df is None or len(df) < 60:
            print(f"[sector]   Skipped — insufficient data", file=sys.stderr)
            continue

        ret_20 = calc_return(df, 20)
        ret_60 = calc_return(df, 60)

        rs20 = relative_strength(ret_20, spy_ret_20)
        rs60 = relative_strength(ret_60, spy_ret_60)

        # Crossover detection
        prev_df = df.iloc[:-1] if len(df) > 1 else None
        prev_rs20 = None
        prev_rs60 = None
        if prev_df is not None and len(prev_df) >= 60:
            p_ret20 = calc_return(prev_df, 20)
            p_ret60 = calc_return(prev_df, 60)
            p_spy20 = spy_ret_20_prev if spy_ret_20_prev is not None else calc_return(prev_spy, 20)
            p_spy60 = spy_ret_60_prev if spy_ret_60_prev is not None else calc_return(prev_spy, 60)
            if p_spy20 is not None and p_spy60 is not None:
                prev_rs20 = relative_strength(p_ret20, p_spy20)
                prev_rs60 = relative_strength(p_ret60, p_spy60)

        crossover = detect_crossover(rs20, rs60, prev_rs20, prev_rs60)

        regime_score = regime_sector_score(meta["type"], regime)
        momentum_score = compute_momentum_score(rs20, rs60, regime_score)

        entry = {
            "ticker": ticker,
            "name": meta["name"],
            "type": meta["type"],
            "return_20d": round(ret_20, 4),
            "return_60d": round(ret_60, 4),
            "rs_20d": round(rs20, 4),
            "rs_60d": round(rs60, 4),
            "regime": regime,
            "regime_alignment": round(regime_score, 2),
            "momentum_score": momentum_score,
            "crossover": crossover,
        }
        results.append(entry)

        if crossover:
            crossovers.append(entry)
            print(f"[sector]   ⚡ {crossover} on {ticker}", file=sys.stderr)
        else:
            print(f"[sector]   RS20={rs20:+.2%}, RS60={rs60:+.2%}, momentum={momentum_score}/10", file=sys.stderr)

    # Rank by momentum score descending
    ranked = sorted(results, key=lambda x: x["momentum_score"], reverse=True)

    # Determine top/bottom 3
    top3 = ranked[:3]
    bottom3 = ranked[-3:]

    # Composite signal
    signal = "NEUTRAL"
    if crossovers:
        bullish = sum(1 for c in crossovers if c["crossover"] == "BULLISH_CROSSOVER")
        bearish = sum(1 for c in crossovers if c["crossover"] == "BEARISH_CROSSOVER")
        if bullish > bearish:
            signal = "ROTATION_TO_CYCLICAL"
        elif bearish > bullish:
            signal = "ROTATION_TO_DEFENSIVE"

    report = {
        "meta": {
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "regime": regime,
            "spy_return_20d": round(spy_ret_20, 4),
            "spy_return_60d": round(spy_ret_60, 4),
            "sectors_scanned": len(SECTOR_ETFS),
            "sectors_ok": len(results),
            "signal": signal,
        },
        "ranking": ranked,
        "crossovers": crossovers,
        "top3": [{"ticker": r["ticker"], "name": r["name"], "momentum_score": r["momentum_score"]} for r in top3],
        "bottom3": [{"ticker": r["ticker"], "name": r["name"], "momentum_score": r["momentum_score"]} for r in bottom3],
    }

    date_str = report["meta"]["date"]
    output_path = DATA_DIR / f"sector_rotation_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "sector_rotation_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(f"[sector] Report → {output_path} | Signal: {signal}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
