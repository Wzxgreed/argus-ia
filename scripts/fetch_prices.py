#!/usr/bin/env python3
"""
fetch_prices.py — Snapshot quotidien des prix et métriques watchlist.

Sources:
- yfinance (gratuit, fiable pour cours/volumes/technique)
- FMP (optionnel, pour consensus, insider trades, earnings dates)

Usage:
    python scripts/fetch_prices.py

Output:
    data/YYYY-MM-DD.json  (merge avec le bloc macro ensuite)
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yfinance as yf
import pandas as pd

from fmp_client import FMPClient

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def calc_rsi(prices: pd.Series, period: int = 14) -> float:
    delta = prices.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return float(rsi.iloc[-1]) if not pd.isna(rsi.iloc[-1]) else None


def calc_atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> float:
    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.rolling(window=period).mean()
    return float(atr.iloc[-1]) if not pd.isna(atr.iloc[-1]) else None


def calc_mm(prices: pd.Series, period: int) -> float:
    mm = prices.rolling(window=period).mean()
    return float(mm.iloc[-1]) if not pd.isna(mm.iloc[-1]) else None


def fetch_ticker_data(ticker: str) -> dict:
    """
    Récupère cours, volumes, fondamentaux et métriques techniques via yfinance.
    Retourne un dict structuré ou un dict avec error=True.
    """
    try:
        stock = yf.Ticker(ticker)

        # --- Historique 6 mois pour les calculs techniques ---
        hist = stock.history(period="6mo", interval="1d")
        if hist.empty:
            return {"ticker": ticker, "error": True, "reason": "No price history"}

        close = hist["Close"]
        high = hist["High"]
        low = hist["Low"]
        volume = hist["Volume"]

        last = hist.iloc[-1]
        prev = hist.iloc[-2] if len(hist) > 1 else last

        # --- Prix ---
        price_block = {
            "open": round(float(last["Open"]), 4),
            "high": round(float(last["High"]), 4),
            "low": round(float(last["Low"]), 4),
            "close": round(float(last["Close"]), 4),
            "previous_close": round(float(prev["Close"]), 4),
            "volume": int(last["Volume"]),
            "volume_avg_20d": int(volume.tail(20).mean()),
            "change_pct": round((last["Close"] - prev["Close"]) / prev["Close"] * 100, 2),
        }

        # --- Technique ---
        tech_block = {
            "rsi14": round(calc_rsi(close, 14), 2) if calc_rsi(close, 14) else None,
            "atr14": round(calc_atr(high, low, close, 14), 2) if calc_atr(high, low, close, 14) else None,
            "mm50": round(calc_mm(close, 50), 2) if calc_mm(close, 50) else None,
            "mm200": round(calc_mm(close, 200), 2) if calc_mm(close, 200) else None,
            "golden_cross": bool(calc_mm(close, 50) > calc_mm(close, 200)) if (calc_mm(close, 50) and calc_mm(close, 200)) else None,
        }

        # --- Fondamentaux (info) ---
        info = stock.info or {}
        fundamentals_block = {
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "ev_ebitda": info.get("enterpriseToEbitda"),
            "ev_revenue": info.get("enterpriseToRevenue"),
            "price_to_book": info.get("priceToBook"),
            "dividend_yield": info.get("dividendYield"),
            "beta": info.get("beta"),
            "short_interest_pct": info.get("shortPercentOfFloat"),
            "shares_float": info.get("floatShares"),
            "shares_outstanding": info.get("sharesOutstanding"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
        }

        # --- Sentiment / Options (si dispo) ---
        options_block = {}
        try:
            # Dernière expiration pour approximer max pain
            expirations = stock.options
            if expirations:
                opt = stock.option_chain(expirations[0])
                calls = opt.calls
                puts = opt.puts
                total_oi = calls["openInterest"].sum() + puts["openInterest"].sum()
                if total_oi > 0:
                    call_oi_pct = round(calls["openInterest"].sum() / total_oi * 100, 1)
                    put_call_ratio = round(puts["openInterest"].sum() / calls["openInterest"].sum(), 2) if calls["openInterest"].sum() > 0 else None
                else:
                    call_oi_pct = None
                    put_call_ratio = None

                # Approximation max pain : strike avec max OI combiné
                oi_by_strike = pd.concat([
                    calls[["strike", "openInterest"]].rename(columns={"openInterest": "call_oi"}),
                    puts[["strike", "openInterest"]].rename(columns={"openInterest": "put_oi"})
                ])
                oi_by_strike = oi_by_strike.groupby("strike").sum()
                oi_by_strike["total_oi"] = oi_by_strike["call_oi"] + oi_by_strike["put_oi"]
                max_pain = round(float(oi_by_strike["total_oi"].idxmax()), 2) if not oi_by_strike.empty else None

                options_block = {
                    "max_pain": max_pain,
                    "put_call_ratio": put_call_ratio,
                    "call_oi_pct": call_oi_pct,
                    "expiration_nearest": expirations[0],
                }
        except Exception:
            pass

        return {
            "ticker": ticker,
            "error": False,
            "price": price_block,
            "technical": tech_block,
            "fundamentals": fundamentals_block,
            "options": options_block,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    except Exception as e:
        return {"ticker": ticker, "error": True, "reason": str(e)}


def main():
    config = load_config()
    tickers = [t["ticker"] for t in config["tickers"]]

    date_str = today_str()
    output_path = DATA_DIR / f"{date_str}.json"

    # --- FMP client (optionnel) ---
    fmp = FMPClient()
    fmp_active = bool(fmp.api_key)
    if fmp_active:
        print(f"[fetch_prices] FMP API key found — enriching with institutional data", file=sys.stderr)
    else:
        print(f"[fetch_prices] FMP API key not found — Yahoo Finance only", file=sys.stderr)

    snapshot = {
        "meta": {
            "date": date_str,
            "source": "yfinance" + (" + fmp" if fmp_active else ""),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "tickers_requested": tickers,
            "tickers_ok": 0,
            "tickers_ko": 0,
        },
        "prices": {},
    }

    for t in tickers:
        print(f"[fetch_prices] Fetching {t}...", file=sys.stderr)
        data = fetch_ticker_data(t)

        # Enrich with FMP if available and Yahoo fetch succeeded
        if not data.get("error") and fmp_active:
            print(f"[fetch_prices] Enriching {t} with FMP data...", file=sys.stderr)
            data = fmp.enrich_ticker(t, data)

        snapshot["prices"][t] = data
        if data.get("error"):
            snapshot["meta"]["tickers_ko"] += 1
        else:
            snapshot["meta"]["tickers_ok"] += 1

    # Écriture
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest.json
    latest_link = DATA_DIR / "latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(f"[fetch_prices] Written {output_path} ({snapshot['meta']['tickers_ok']} OK, {snapshot['meta']['tickers_ko']} KO)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
