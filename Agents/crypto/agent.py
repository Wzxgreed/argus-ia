#!/usr/bin/env python3
"""
agent_crypto.py — Agent Crypto-Correlation.

Protocol : `Agents/AGENT_CRYPTO.md`

Analyse la corrélation entre les tickers crypto-exposés et les cryptomonnaies
(BTC, ETH). Calcule NAV, premium/discount, beta, et détecte les divergences.
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yfinance as yf
import pandas as pd

from agents.base import BaseAgent
from agents.schemas import CryptoReport, CryptoTickerAnalysis, Meta


class CryptoAgent(BaseAgent):
    name = "crypto"
    output_schema = CryptoReport

    CRYPTO_SYMBOLS = {
        "BTC": "BTC-USD",
        "ETH": "ETH-USD",
    }

    def get_crypto_tickers(self) -> list[str]:
        try:
            config = self.config
            return [t["ticker"] for t in config.get("tickers", []) if t.get("crypto_exposed", False)]
        except Exception:
            return ["IREN"]

    def fetch_history(self, ticker: str, period: str = "90d") -> pd.DataFrame | None:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period)
            if hist.empty:
                return None
            return hist
        except Exception as e:
            self.log("ERROR", "fetch_error", ticker=ticker, error=str(e))
            return None

    def calculate_correlation(self, df1: pd.DataFrame, df2: pd.DataFrame, window: int = 30) -> float:
        combined = pd.DataFrame({
            "t1": df1["Close"],
            "t2": df2["Close"]
        }).dropna()
        if len(combined) < window:
            return 0.0
        r1 = combined["t1"].pct_change().dropna()
        r2 = combined["t2"].pct_change().dropna()
        if len(r1) < window:
            return 0.0
        corr = r1.iloc[-window:].corr(r2.iloc[-window:])
        return round(float(corr), 3) if not pd.isna(corr) else 0.0

    def calculate_beta(self, df_stock: pd.DataFrame, df_crypto: pd.DataFrame) -> float:
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

    def calculate_r2(self, df_stock: pd.DataFrame, df_crypto: pd.DataFrame) -> float:
        corr = self.calculate_correlation(df_stock, df_crypto, window=min(90, len(df_stock)))
        return round(corr ** 2, 3)

    def estimate_nav(self, ticker: str, btc_price: float) -> dict:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info or {}
            market_cap = info.get("marketCap")
            if not market_cap or not btc_price:
                return {"nav_estimate": None, "premium_pct": None}
            nav_estimate = market_cap * 0.6
            premium_pct = round((market_cap - nav_estimate) / nav_estimate * 100, 1)
            return {
                "nav_estimate": nav_estimate,
                "market_cap": market_cap,
                "premium_pct": premium_pct,
            }
        except Exception as e:
            self.log("ERROR", "nav_estimation_error", ticker=ticker, error=str(e))
            return {"nav_estimate": None, "premium_pct": None}

    def get_btc_price(self) -> float | None:
        try:
            btc = yf.Ticker(self.CRYPTO_SYMBOLS["BTC"])
            hist = btc.history(period="5d")
            if hist.empty:
                return None
            return round(float(hist["Close"].iloc[-1]), 2)
        except Exception as e:
            self.log("ERROR", "btc_price_error", error=str(e))
            return None

    def calculate_divergence_score(self, df_stock: pd.DataFrame, df_crypto: pd.DataFrame) -> float:
        combined = pd.DataFrame({
            "stock": df_stock["Close"],
            "crypto": df_crypto["Close"]
        }).dropna()
        if len(combined) < 7:
            return 0.0
        stock_7d = (combined["stock"].iloc[-1] / combined["stock"].iloc[-7] - 1) if len(combined) >= 7 else 0
        crypto_7d = (combined["crypto"].iloc[-1] / combined["crypto"].iloc[-7] - 1) if len(combined) >= 7 else 0
        stock_30d = (combined["stock"].iloc[-1] / combined["stock"].iloc[-30] - 1) if len(combined) >= 30 else 0
        crypto_30d = (combined["crypto"].iloc[-1] / combined["crypto"].iloc[-30] - 1) if len(combined) >= 30 else 0
        diff_7d = abs(stock_7d - crypto_7d)
        diff_30d = abs(stock_30d - crypto_30d)
        score = min((diff_7d + diff_30d) * 20, 10.0)
        return round(score, 1)

    def run(self) -> CryptoReport:
        self.log("INFO", "start")
        crypto_tickers = self.get_crypto_tickers()
        if not crypto_tickers:
            self.log("INFO", "no_crypto_tickers")
            return CryptoReport(meta=Meta(date=self.date_str, agent=self.name), analysis={})

        btc_price = self.get_btc_price()
        self.log("INFO", "btc_price", price=btc_price)

        results: dict[str, CryptoTickerAnalysis] = {}

        for ticker in crypto_tickers:
            df_stock = self.fetch_history(ticker, period="90d")
            df_btc = self.fetch_history(self.CRYPTO_SYMBOLS["BTC"], period="90d")

            if df_stock is None or df_btc is None:
                self.log("WARNING", "data_unavailable", ticker=ticker)
                continue

            corr_30d = self.calculate_correlation(df_stock, df_btc, window=30)
            corr_90d = self.calculate_correlation(df_stock, df_btc, window=min(90, len(df_stock)))
            beta_btc = self.calculate_beta(df_stock, df_btc)
            r2_btc = self.calculate_r2(df_stock, df_btc)
            divergence = self.calculate_divergence_score(df_stock, df_btc)
            nav_data = self.estimate_nav(ticker, btc_price) if btc_price else {"nav_estimate": None, "premium_pct": None}

            results[ticker] = CryptoTickerAnalysis(
                correlation_30d=corr_30d,
                correlation_90d=corr_90d,
                beta_btc=beta_btc,
                r2_btc=r2_btc,
                divergence_score=divergence,
                nav_estimate=nav_data.get("nav_estimate"),
                market_cap=nav_data.get("market_cap"),
                premium_pct=nav_data.get("premium_pct"),
                verdict=(
                    "Corrélation forte" if corr_30d > 0.7 else
                    "Corrélation modérée" if corr_30d > 0.4 else
                    "Faible corrélation"
                ),
            )

            self.log(
                "INFO",
                "ticker_analyzed",
                ticker=ticker,
                corr30d=corr_30d,
                beta=beta_btc,
                r2=r2_btc,
                div=divergence,
                premium=nav_data.get("premium_pct"),
            )

        return CryptoReport(
            meta=Meta(date=self.date_str, agent=self.name, btc_price=btc_price),
            analysis=results,
        )


if __name__ == "__main__":
    sys.exit(CryptoAgent.cli_entry())
