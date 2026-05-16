#!/usr/bin/env python3
"""
agent_crypto.py — Agent Crypto-Correlation.

Analyse la corrélation entre les tickers crypto-exposés et les cryptomonnaies
(BTC, ETH). Calcule NAV, premium/discount, beta, et détecte les divergences.

Usage:
    python scripts/agent_crypto.py

Output:
    data/crypto_correlation_YYYY-MM-DD.json
"""

import json
import math
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yfinance as yf
import pandas as pd

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"

# Crypto tickers mapping (yfinance symbols)
CRYPTO_SYMBOLS = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
}

# Tickers considérés comme crypto-exposed
def get_crypto_tickers() -> list[str]:
    """Lit config/watchlist.json pour trouver les tickers crypto_exposed."""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
        return [t["ticker"] for t in config.get("tickers", []) if t.get("crypto_exposed", False)]
    except Exception:
        # Fallback — IREN est le seul crypto-exposed connu
        return ["IREN"]


def fetch_history(ticker: str, period: str = "90d") -> pd.DataFrame | None:
    """Récupère l'historique de prix via yfinance."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        if hist.empty:
            return None
        return hist
    except Exception as e:
        print(f"[crypto] Error fetching {ticker}: {e}", file=sys.stderr)
        return None


def calculate_correlation(df1: pd.DataFrame, df2: pd.DataFrame, window: int = 30) -> float:
    """Calcule la corrélation Pearson sur la fenêtre commune."""
    # Aligner les deux séries sur les dates communes
    combined = pd.DataFrame({
        "t1": df1["Close"],
        "t2": df2["Close"]
    }).dropna()

    if len(combined) < window:
        return 0.0

    # Calcul des rendements
    r1 = combined["t1"].pct_change().dropna()
    r2 = combined["t2"].pct_change().dropna()

    if len(r1) < window:
        return 0.0

    # Corrélation sur la dernière fenêtre
    corr = r1.iloc[-window:].corr(r2.iloc[-window:])
    return round(float(corr), 3) if not pd.isna(corr) else 0.0


def calculate_beta(df_stock: pd.DataFrame, df_crypto: pd.DataFrame) -> float:
    """Beta = Cov(stock, crypto) / Var(crypto)."""
    combined = pd.DataFrame({
        "stock": df_stock["Close"],
        "crypto": df_crypto["Close"]
    }).dropna()

    if len(combined) < 20:
        return 0.0

    r_stock = combined["stock"].pct_change().dropna()
    r_crypto = combined["crypto"].pct_change().dropna()

    aligned = pd.DataFrame({"stock": r_stock, "crypto": r_crypto}).dropna()
    if len(aligned) < 20:
        return 0.0

    cov = aligned["stock"].cov(aligned["crypto"])
    var = aligned["crypto"].var()
    if var == 0:
        return 0.0
    return round(float(cov / var), 3)


def calculate_r2(df_stock: pd.DataFrame, df_crypto: pd.DataFrame) -> float:
    """R² = coefficient de détermination."""
    corr = calculate_correlation(df_stock, df_crypto, window=min(90, len(df_stock)))
    return round(corr ** 2, 3)


def estimate_nav(ticker: str, btc_price: float) -> dict:
    """
    Estimation simplifiée du NAV pour un miner de BTC.
    Nécessite des données de filing — ici on utilise une heuristique basée sur
    le market cap et le prix du BTC.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info or {}
        market_cap = info.get("marketCap")

        if not market_cap or not btc_price:
            return {"nav_estimate": None, "premium_pct": None}

        # Heuristique très simplifiée :
        # NAV ≈ market_cap × 0.6 (si le miner a une forte composante crypto)
        # C'est une approximation grossière — le vrai NAV nécessite les holdings BTC
        nav_estimate = market_cap * 0.6
        premium_pct = round((market_cap - nav_estimate) / nav_estimate * 100, 1)

        return {
            "nav_estimate": nav_estimate,
            "market_cap": market_cap,
            "premium_pct": premium_pct,
        }
    except Exception as e:
        print(f"[crypto] NAV estimation error for {ticker}: {e}", file=sys.stderr)
        return {"nav_estimate": None, "premium_pct": None}


def get_btc_price() -> float | None:
    """Récupère le prix actuel du BTC via yfinance."""
    try:
        btc = yf.Ticker(CRYPTO_SYMBOLS["BTC"])
        hist = btc.history(period="5d")
        if hist.empty:
            return None
        return round(float(hist["Close"].iloc[-1]), 2)
    except Exception as e:
        print(f"[crypto] Error fetching BTC price: {e}", file=sys.stderr)
        return None


def calculate_divergence_score(df_stock: pd.DataFrame, df_crypto: pd.DataFrame) -> float:
    """
    Détecte les divergences entre le ticker et le crypto sur 7j et 30j.
    Score /10 — plus élevé = divergence majeure.
    """
    combined = pd.DataFrame({
        "stock": df_stock["Close"],
        "crypto": df_crypto["Close"]
    }).dropna()

    if len(combined) < 7:
        return 0.0

    # Rendements sur 7j et 30j
    stock_7d = (combined["stock"].iloc[-1] / combined["stock"].iloc[-7] - 1) if len(combined) >= 7 else 0
    crypto_7d = (combined["crypto"].iloc[-1] / combined["crypto"].iloc[-7] - 1) if len(combined) >= 7 else 0

    stock_30d = (combined["stock"].iloc[-1] / combined["stock"].iloc[-30] - 1) if len(combined) >= 30 else 0
    crypto_30d = (combined["crypto"].iloc[-1] / combined["crypto"].iloc[-30] - 1) if len(combined) >= 30 else 0

    # Divergence = différence de direction ou d'amplitude
    diff_7d = abs(stock_7d - crypto_7d)
    diff_30d = abs(stock_30d - crypto_30d)

    # Score basé sur la divergence
    score = min((diff_7d + diff_30d) * 20, 10.0)
    return round(score, 1)


def main():
    print("[crypto] Starting crypto-correlation analysis...", file=sys.stderr)

    crypto_tickers = get_crypto_tickers()
    if not crypto_tickers:
        print("[crypto] No crypto-exposed tickers found. Skipping.", file=sys.stderr)
        return 0

    btc_price = get_btc_price()
    print(f"[crypto] BTC price: ${btc_price:,}" if btc_price else "[crypto] BTC price unavailable", file=sys.stderr)

    results = {}

    for ticker in crypto_tickers:
        print(f"[crypto] Analyzing {ticker}...", file=sys.stderr)

        df_stock = fetch_history(ticker, period="90d")
        df_btc = fetch_history(CRYPTO_SYMBOLS["BTC"], period="90d")

        if df_stock is None or df_btc is None:
            print(f"[crypto]   Skipped — data unavailable", file=sys.stderr)
            continue

        corr_30d = calculate_correlation(df_stock, df_btc, window=30)
        corr_90d = calculate_correlation(df_stock, df_btc, window=min(90, len(df_stock)))
        beta_btc = calculate_beta(df_stock, df_btc)
        r2_btc = calculate_r2(df_stock, df_btc)
        divergence = calculate_divergence_score(df_stock, df_btc)

        nav_data = estimate_nav(ticker, btc_price) if btc_price else {"nav_estimate": None, "premium_pct": None}

        results[ticker] = {
            "correlation_30d": corr_30d,
            "correlation_90d": corr_90d,
            "beta_btc": beta_btc,
            "r2_btc": r2_btc,
            "divergence_score": divergence,
            **nav_data,
            "verdict": (
                "Corrélation forte" if corr_30d > 0.7 else
                "Corrélation modérée" if corr_30d > 0.4 else
                "Faible corrélation"
            ),
        }

        print(
            f"[crypto]   {ticker}: corr30d={corr_30d}, beta={beta_btc}, "
            f"r2={r2_btc}, div={divergence}, premium={nav_data.get('premium_pct', 'N/A')}%",
            file=sys.stderr
        )

    # Build report
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report = {
        "meta": {
            "date": date_str,
            "btc_price": btc_price,
            "tickers_analyzed": list(results.keys()),
        },
        "analysis": results,
    }

    output_path = DATA_DIR / f"crypto_correlation_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "crypto_correlation_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(f"[crypto] Report written → {output_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
