#!/usr/bin/env python3
"""
fmp_client.py — Client HTTP pour Financial Modeling Prep (FMP) — Stable API.

Base URL : https://financialmodelingprep.com/stable
Compatible avec les abonnements post-août 2025 (non-legacy).

Usage:
    from fmp_client import FMPClient
    fmp = FMPClient()
    profile = fmp.get_profile("AAPL")
    ratios = fmp.get_ratios("AAPL")
    price_target = fmp.get_price_target_summary("AAPL")
"""

import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env.local"

# Charger .env.local si présent (prime sur .env)
if ENV_PATH.exists():
    load_dotenv(ENV_PATH, override=True)

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE_URL = "https://financialmodelingprep.com/stable"


class FMPClient:
    """Client FMP avec session réutilisable (pool de connexions)."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or FMP_API_KEY
        if not self.api_key:
            print("[FMP] Warning: FMP_API_KEY not found. Set it in .env.local", file=sys.stderr)
        # Session réutilisable → pool de connexions HTTP keep-alive
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Argus-IA/1.0 (github.com/Wzxgreed/argus-ia) "
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36"
            ),
            "Accept": "application/json",
        })

    def _get(self, endpoint: str, params: dict = None) -> dict | list:
        """GET request vers la Stable API FMP avec retry, backoff et caching."""
        if not self.api_key:
            return {"error": True, "reason": "FMP_API_KEY missing"}

        url = f"{FMP_BASE_URL}/{endpoint}"
        p = params or {}
        p["apikey"] = self.api_key

        # Statements, ratios et key-metrics changent rarement → cache activé
        cache_endpoints = {"income-statement", "balance-sheet-statement", "cash-flow-statement", "ratios", "key-metrics", "profile"}
        use_cache = endpoint in cache_endpoints

        from http_utils import http_get
        data = http_get(url, params=p, session=self.session, timeout=15, use_cache=use_cache)

        if isinstance(data, dict) and data.get("error"):
            return data
        if isinstance(data, dict) and "Error Message" in data:
            return {"error": True, "reason": data["Error Message"]}
        return data

    # ------------------------------------------------------------------
    # Core data (Stable API — disponibles sur tous les plans)
    # ------------------------------------------------------------------
    def get_quote(self, ticker: str) -> list:
        """Cours et données de marché en temps réel."""
        return self._get("quote", {"symbol": ticker})

    def get_profile(self, ticker: str) -> list:
        """Profil entreprise (secteur, industrie, employés, description)."""
        return self._get("profile", {"symbol": ticker})

    # ------------------------------------------------------------------
    # Analyst & Valuation (Stable API)
    # ------------------------------------------------------------------
    def get_price_target_summary(self, ticker: str) -> list:
        """Consensus analystes : nombre et prix cible moyen."""
        return self._get("price-target-summary", {"symbol": ticker})

    # ------------------------------------------------------------------
    # Financial ratios & metrics (Stable API)
    # ------------------------------------------------------------------
    def get_ratios(self, ticker: str, period: str = "annual", limit: int = 1) -> list:
        """Ratios financiers détaillés (ROE, marges, leverage...)."""
        return self._get("ratios", {"symbol": ticker, "period": period, "limit": limit})

    def get_key_metrics(self, ticker: str, period: str = "annual", limit: int = 1) -> list:
        """Métriques clés (EV multiples, returns, working capital...)."""
        return self._get("key-metrics", {"symbol": ticker, "period": period, "limit": limit})

    # ------------------------------------------------------------------
    # Statements (Stable API — si disponible selon plan)
    # ------------------------------------------------------------------
    def get_income_statement(self, ticker: str, period: str = "annual", limit: int = 8) -> list:
        return self._get("income-statement", {"symbol": ticker, "period": period, "limit": limit})

    def get_balance_sheet(self, ticker: str, period: str = "annual", limit: int = 8) -> list:
        return self._get("balance-sheet-statement", {"symbol": ticker, "period": period, "limit": limit})

    def get_cash_flow(self, ticker: str, period: str = "annual", limit: int = 8) -> list:
        return self._get("cash-flow-statement", {"symbol": ticker, "period": period, "limit": limit})

    # ------------------------------------------------------------------
    # Transcripts — Plan supérieur requis (Starter/Essential insuffisants)
    # ------------------------------------------------------------------
    def get_earning_call_transcript(self, ticker: str, year: int = None, quarter: int = None) -> dict:
        """
        Transcript d'earnings call.
        ⚠️  Nécessite un plan FMP supérieur (Enterprise+). Retourne 402 sinon.
        """
        params = {"symbol": ticker}
        if year is not None:
            params["year"] = year
        if quarter is not None:
            params["quarter"] = quarter
        return self._get("earning-call-transcript", params)

    # ------------------------------------------------------------------
    # Helper : merge FMP Stable data into Yahoo snapshot structure
    # ------------------------------------------------------------------
    def enrich_ticker(self, ticker: str, yahoo_block: dict) -> dict:
        """
        Prend un bloc Yahoo et ajoute les données FMP Stable disponibles.
        Retourne le bloc enrichi.
        Les endpoints indisponibles (upgrades, insiders, DCF) sont ignorés silencieusement.
        """
        if not self.api_key:
            return yahoo_block

        block = dict(yahoo_block)

        # --- Profile (secteur, industrie, description, employés) ---
        profile = self.get_profile(ticker)
        if isinstance(profile, list) and profile:
            p = profile[0]
            # Complète les données Yahoo si absentes
            if not block.get("fundamentals", {}).get("sector"):
                block.setdefault("fundamentals", {})
                block["fundamentals"]["sector"] = p.get("sector")
                block["fundamentals"]["industry"] = p.get("industry")
                block["fundamentals"]["employees"] = p.get("fullTimeEmployees")
                block["fundamentals"]["country"] = p.get("country")
                block["fundamentals"]["website"] = p.get("website")
                block["fundamentals"]["ceo"] = p.get("ceo")
                block["fundamentals"]["description"] = p.get("description")
                block["fundamentals"]["exchange"] = p.get("exchange")

        # --- Price Target Summary (consensus analystes) ---
        pt = self.get_price_target_summary(ticker)
        if isinstance(pt, list) and pt:
            p = pt[0]
            block["fmp_consensus"] = {
                "price_target_avg": p.get("lastYearAvgPriceTarget") or p.get("allTimeAvgPriceTarget"),
                "price_target_low": None,
                "price_target_high": None,
                "num_analysts": p.get("lastYearCount") or p.get("allTimeCount"),
                "num_analysts_last_month": p.get("lastMonthCount"),
                "num_analysts_last_quarter": p.get("lastQuarterCount"),
                "publishers": p.get("publishers"),
            }

        # --- Ratios (dernier trimestre / année) ---
        ratios = self.get_ratios(ticker, period="annual", limit=1)
        if isinstance(ratios, list) and ratios:
            r = ratios[0]
            block["fmp_ratios"] = {
                "roe": r.get("returnOnEquity"),
                "roic": r.get("returnOnInvestedCapital"),
                "roa": r.get("returnOnAssets"),
                "gross_margin": r.get("grossProfitMargin"),
                "operating_margin": r.get("operatingProfitMargin"),
                "ebitda_margin": r.get("ebitdaMargin"),
                "net_margin": r.get("netProfitMargin"),
                "debt_equity": r.get("debtToEquityRatio"),
                "debt_assets": r.get("debtToAssetsRatio"),
                "interest_coverage": r.get("interestCoverageRatio"),
                "current_ratio": r.get("currentRatio"),
                "quick_ratio": r.get("quickRatio"),
                "asset_turnover": r.get("assetTurnover"),
                "receivables_turnover": r.get("receivablesTurnover"),
                "payables_turnover": r.get("payablesTurnover"),
                "inventory_turnover": r.get("inventoryTurnover"),
                "price_to_earnings": r.get("priceToEarningsRatio"),
                "price_to_book": r.get("priceToBookRatio"),
                "price_to_sales": r.get("priceToSalesRatio"),
                "price_to_fcf": r.get("priceToFreeCashFlowRatio"),
                "enterprise_value_multiple": r.get("enterpriseValueMultiple"),
                "effective_tax_rate": r.get("effectiveTaxRate"),
                "dividend_yield": r.get("dividendYieldPercentage"),
                "revenue_per_share": r.get("revenuePerShare"),
                "book_value_per_share": r.get("bookValuePerShare"),
                "date": r.get("date"),
                "period": r.get("period"),
            }

        # --- Key Metrics (EV multiples, returns, working capital) ---
        km = self.get_key_metrics(ticker, period="annual", limit=1)
        if isinstance(km, list) and km:
            k = km[0]
            block["fmp_key_metrics"] = {
                "market_cap": k.get("marketCap"),
                "enterprise_value": k.get("enterpriseValue"),
                "ev_to_sales": k.get("evToSales"),
                "ev_to_ebitda": k.get("evToEBITDA"),
                "ev_to_operating_cash_flow": k.get("evToOperatingCashFlow"),
                "ev_to_fcf": k.get("evToFreeCashFlow"),
                "net_debt_to_ebitda": k.get("netDebtToEBITDA"),
                "return_on_equity": k.get("returnOnEquity"),
                "return_on_assets": k.get("returnOnAssets"),
                "return_on_invested_capital": k.get("returnOnInvestedCapital"),
                "return_on_capital_employed": k.get("returnOnCapitalEmployed"),
                "earnings_yield": k.get("earningsYield"),
                "free_cash_flow_yield": k.get("freeCashFlowYield"),
                "working_capital": k.get("workingCapital"),
                "invested_capital": k.get("investedCapital"),
                "tangible_asset_value": k.get("tangibleAssetValue"),
                "capex_to_revenue": k.get("capexToRevenue"),
                "capex_to_operating_cash_flow": k.get("capexToOperatingCashFlow"),
                "capex_to_depreciation": k.get("capexToDepreciation"),
                "stock_based_compensation_to_revenue": k.get("stockBasedCompensationToRevenue"),
                "days_sales_outstanding": k.get("daysOfSalesOutstanding"),
                "days_payables_outstanding": k.get("daysOfPayablesOutstanding"),
                "days_inventory_outstanding": k.get("daysOfInventoryOutstanding"),
                "cash_conversion_cycle": k.get("cashConversionCycle"),
                "date": k.get("date"),
                "period": k.get("period"),
            }

        return block
