#!/usr/bin/env python3
"""
yahoo_worker.py — Worker isolé pour fetcher les données Yahoo Finance.

Utilise yfinance (qui gère les cookies/redirects) mais s'exécute dans un
processus fils avec timeout OS, évitant les hangs au niveau C (libcurl).

Usage :
    python scripts/yahoo_worker.py TICKER

Output (stdout) :
    JSON avec les blocs price, technical, fundamentals, options.
"""

import json
import sys

import yfinance as yf
import pandas as pd


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


def fetch_all(ticker: str) -> dict:
    try:
        stock = yf.Ticker(ticker)

        # --- Historique ---
        hist = stock.history(period="6mo", interval="1d")
        if hist.empty:
            return {"ticker": ticker, "error": True, "reason": "No price history"}

        close = hist["Close"]
        high = hist["High"]
        low = hist["Low"]
        volume = hist["Volume"]
        last = hist.iloc[-1]
        prev = hist.iloc[-2] if len(hist) > 1 else last

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

        tech_block = {
            "rsi14": round(calc_rsi(close, 14), 2) if calc_rsi(close, 14) else None,
            "atr14": round(calc_atr(high, low, close, 14), 2) if calc_atr(high, low, close, 14) else None,
            "mm50": round(calc_mm(close, 50), 2) if calc_mm(close, 50) else None,
            "mm200": round(calc_mm(close, 200), 2) if calc_mm(close, 200) else None,
            "golden_cross": bool(calc_mm(close, 50) > calc_mm(close, 200)) if (calc_mm(close, 50) and calc_mm(close, 200)) else None,
        }

        # --- Fondamentaux ---
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

        # --- Options ---
        options_block = {}
        try:
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
        }

    except Exception as e:
        return {"ticker": ticker, "error": True, "reason": str(e)}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": True, "reason": "Missing ticker argument"}))
        sys.exit(1)

    ticker = sys.argv[1]
    result = fetch_all(ticker)
    print(json.dumps(result, default=str))
