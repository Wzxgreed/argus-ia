#!/usr/bin/env python3
"""
yahoo_client.py — Client HTTP direct pour Yahoo Finance (requests + timeout).

Remplace yfinance pour tous les appels réseau afin d'éviter les hangs
au niveau C (libcurl) non-interruptibles par Python.

Endpoints utilisés :
  • v8/finance/chart       → historique des prix (RSI, ATR, MM)
  • v10/finance/quoteSummary → info entreprise (marketCap, P/E, beta, sector...)
  • v7/finance/options       → chaines d'options (max pain, put/call ratio)
  • v1/finance/search        → news du ticker

Usage :
    from yahoo_client import YahooClient
    client = YahooClient()
    hist = client.get_history("AAPL")
    info = client.get_info("AAPL")
    opts = client.get_options("AAPL")
    news = client.get_news("AAPL")
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DEFAULT_TIMEOUT = 15  # seconds
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}


class YahooClient:
    """Client Yahoo Finance REST avec timeout garanti."""

    def __init__(self, timeout: int = DEFAULT_TIMEOUT):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.timeout = timeout

    # -----------------------------------------------------------------------
    # Historique des prix  (v8/finance/chart)
    # -----------------------------------------------------------------------
    def get_history(self, ticker: str, period: str = "6mo", interval: str = "1d") -> dict:
        """
        Récupère l'historique des prix.
        Retourne un dict structuré compatible avec l'ancien format yfinance,
        ou {"error": True, "reason": "..."} en cas d'échec.
        """
        # Conversion période → timestamps
        now = datetime.now(timezone.utc)
        period_map = {
            "1mo": 30,
            "3mo": 90,
            "6mo": 180,
            "1y": 365,
            "2y": 730,
            "5y": 1825,
        }
        days = period_map.get(period, 180)
        period1 = int((now.timestamp() - days * 86400))
        period2 = int(now.timestamp())

        url = (
            f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
            f"?period1={period1}&period2={period2}&interval={interval}"
        )

        try:
            resp = self.session.get(url, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.Timeout:
            return {"error": True, "reason": f"Timeout ({self.timeout}s)"}
        except requests.exceptions.HTTPError as e:
            return {"error": True, "reason": f"HTTP {e.response.status_code}"}
        except Exception as e:
            return {"error": True, "reason": str(e)}

        chart = data.get("chart", {})
        error = chart.get("error")
        if error:
            return {"error": True, "reason": error.get("description", "Unknown chart error")}

        result = chart.get("result", [None])[0]
        if not result:
            return {"error": True, "reason": "Empty chart result"}

        timestamps = result.get("timestamp", [])
        quote = result.get("indicators", {}).get("quote", [{}])[0]
        adjclose = result.get("indicators", {}).get("adjclose", [{}])[0]

        opens = quote.get("open", [])
        highs = quote.get("high", [])
        lows = quote.get("low", [])
        closes = adjclose.get("adjclose", quote.get("close", []))
        volumes = quote.get("volume", [])

        if not timestamps or not closes:
            return {"error": True, "reason": "No price data in chart"}

        # Construire la structure DataFrame-like
        rows = []
        for i in range(len(timestamps)):
            if closes[i] is None:
                continue
            rows.append({
                "Open": opens[i],
                "High": highs[i],
                "Low": lows[i],
                "Close": closes[i],
                "Volume": volumes[i] if volumes else 0,
            })

        if len(rows) < 2:
            return {"error": True, "reason": "Insufficient price data"}

        return {
            "error": False,
            "rows": rows,
            "meta": {
                "ticker": ticker,
                "period": period,
                "interval": interval,
                "rows_count": len(rows),
            },
        }

    # -----------------------------------------------------------------------
    # Info entreprise  (v10/finance/quoteSummary)
    # -----------------------------------------------------------------------
    def get_info(self, ticker: str) -> dict:
        """
        Récupère les métadonnées entreprise (marketCap, P/E, beta, sector...).
        """
        modules = "summaryDetail,defaultKeyStatistics,price,assetProfile"
        url = (
            f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}"
            f"?modules={modules}"
        )

        try:
            resp = self.session.get(url, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.Timeout:
            return {"error": True, "reason": f"Timeout ({self.timeout}s)"}
        except requests.exceptions.HTTPError as e:
            return {"error": True, "reason": f"HTTP {e.response.status_code}"}
        except Exception as e:
            return {"error": True, "reason": str(e)}

        qs = data.get("quoteSummary", {})
        if qs.get("error"):
            return {"error": True, "reason": qs["error"].get("description", "Unknown")}

        result = qs.get("result", [{}])[0]
        if not result:
            return {"error": True, "reason": "Empty quoteSummary result"}

        price = result.get("price", {})
        summary = result.get("summaryDetail", {})
        stats = result.get("defaultKeyStatistics", {})
        profile = result.get("assetProfile", {})

        def _raw(field: dict) -> Any:
            if isinstance(field, dict):
                return field.get("raw") if "raw" in field else field.get("fmt")
            return field

        info = {
            "marketCap": _raw(price.get("marketCap")),
            "trailingPE": _raw(summary.get("trailingPE")),
            "forwardPE": _raw(summary.get("forwardPE")),
            "enterpriseToEbitda": _raw(summary.get("enterpriseToEbitda")),
            "enterpriseToRevenue": _raw(summary.get("enterpriseToRevenue")),
            "priceToBook": _raw(summary.get("priceToBook")),
            "dividendYield": _raw(summary.get("dividendYield")),
            "beta": _raw(summary.get("beta")),
            "shortPercentOfFloat": _raw(stats.get("shortPercentOfFloat")),
            "floatShares": _raw(stats.get("floatShares")),
            "sharesOutstanding": _raw(stats.get("sharesOutstanding")),
            "fiftyTwoWeekHigh": _raw(summary.get("fiftyTwoWeekHigh")),
            "fiftyTwoWeekLow": _raw(summary.get("fiftyTwoWeekLow")),
            "sector": profile.get("sector") or price.get("sector"),
            "industry": profile.get("industry") or price.get("industry"),
        }

        # Nettoyer les None
        info = {k: v for k, v in info.items() if v is not None}
        return {"error": False, "data": info}

    # -----------------------------------------------------------------------
    # Options  (v7/finance/options)
    # -----------------------------------------------------------------------
    def get_options(self, ticker: str) -> dict:
        """
        Récupère la chaine d'options la plus proche.
        Retourne : expirations, calls, puts, max pain approximé.
        """
        url = f"https://query1.finance.yahoo.com/v7/finance/options/{ticker}"

        try:
            resp = self.session.get(url, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.Timeout:
            return {"error": True, "reason": f"Timeout ({self.timeout}s)"}
        except requests.exceptions.HTTPError as e:
            return {"error": True, "reason": f"HTTP {e.response.status_code}"}
        except Exception as e:
            return {"error": True, "reason": str(e)}

        oc = data.get("optionChain", {})
        if oc.get("error"):
            return {"error": True, "reason": oc["error"].get("description", "Unknown")}

        result = oc.get("result", [{}])[0]
        if not result:
            return {"error": True, "reason": "Empty option chain"}

        expirations = result.get("expirationDates", [])
        if not expirations:
            return {"error": True, "reason": "No expirations available"}

        options = result.get("options", [{}])[0]
        calls = options.get("calls", [])
        puts = options.get("puts", [])

        # Calculer max pain approximé (strike avec max OI combiné)
        oi_by_strike = {}
        for c in calls:
            s = c.get("strike", {}).get("raw", c.get("strike", 0))
            oi = c.get("openInterest", {}).get("raw", c.get("openInterest", 0))
            oi_by_strike[s] = oi_by_strike.get(s, 0) + oi
        for p in puts:
            s = p.get("strike", {}).get("raw", p.get("strike", 0))
            oi = p.get("openInterest", {}).get("raw", p.get("openInterest", 0))
            oi_by_strike[s] = oi_by_strike.get(s, 0) + oi

        max_pain = None
        if oi_by_strike:
            max_pain = max(oi_by_strike, key=oi_by_strike.get)

        call_oi = sum(c.get("openInterest", {}).get("raw", c.get("openInterest", 0)) for c in calls)
        put_oi = sum(p.get("openInterest", {}).get("raw", p.get("openInterest", 0)) for p in puts)
        total_oi = call_oi + put_oi
        call_oi_pct = round(call_oi / total_oi * 100, 1) if total_oi > 0 else None
        put_call_ratio = round(put_oi / call_oi, 2) if call_oi > 0 else None

        return {
            "error": False,
            "expirations": expirations,
            "nearest_expiration": expirations[0],
            "max_pain": max_pain,
            "put_call_ratio": put_call_ratio,
            "call_oi_pct": call_oi_pct,
            "call_count": len(calls),
            "put_count": len(puts),
        }

    # -----------------------------------------------------------------------
    # News  (v1/finance/search)
    # -----------------------------------------------------------------------
    def get_news(self, ticker: str, limit: int = 10) -> list[dict]:
        """
        Récupère les news récentes pour un ticker.
        """
        url = (
            f"https://query1.finance.yahoo.com/v1/finance/search"
            f"?q={ticker}&newsCount={limit}"
        )

        try:
            resp = self.session.get(url, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.Timeout:
            return []
        except requests.exceptions.HTTPError:
            return []
        except Exception:
            return []

        news = data.get("news", [])
        items = []
        for n in news:
            items.append({
                "uuid": n.get("uuid", ""),
                "title": n.get("title", ""),
                "summary": n.get("summary", ""),
                "publisher": n.get("publisher", ""),
                "link": n.get("link", ""),
                "published": n.get("published", ""),
            })
        return items


# ---------------------------------------------------------------------------
# Helpers pour le calcul technique (anciennement dans pandas)
# ---------------------------------------------------------------------------

def calc_rsi(prices: list[float], period: int = 14) -> float | None:
    """Calcule le RSI 14j depuis une liste de closes."""
    if len(prices) < period + 1:
        return None
    gains = []
    losses = []
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        gains.append(max(diff, 0))
        losses.append(max(-diff, 0))

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period

    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)


def calc_atr(highs: list[float], lows: list[float], closes: list[float], period: int = 14) -> float | None:
    """Calcule l'ATR 14j."""
    if len(closes) < period + 1:
        return None
    trs = []
    for i in range(1, len(closes)):
        tr1 = highs[i] - lows[i]
        tr2 = abs(highs[i] - closes[i - 1])
        tr3 = abs(lows[i] - closes[i - 1])
        trs.append(max(tr1, tr2, tr3))

    if len(trs) < period:
        return None
    atr = sum(trs[:period]) / period
    for i in range(period, len(trs)):
        atr = (atr * (period - 1) + trs[i]) / period
    return round(atr, 2)


def calc_mm(prices: list[float], period: int) -> float | None:
    """Calcule une moyenne mobile simple."""
    if len(prices) < period:
        return None
    return round(sum(prices[-period:]) / period, 2)


# ---------------------------------------------------------------------------
# Fonctions standalone pour compatibilité ancienne (get_ticker_news, etc.)
# ---------------------------------------------------------------------------

def get_ticker_news(ticker: str, limit: int = 10) -> list[dict]:
    """Récupère les news d'un ticker (compatible ancien agent_geo.py)."""
    client = YahooClient()
    return client.get_news(ticker, limit=limit)


def get_ticker_history(ticker: str, period: str = "6mo") -> dict:
    """Récupère l'historique d'un ticker."""
    client = YahooClient()
    return client.get_history(ticker, period=period)


def get_ticker_info(ticker: str) -> dict:
    """Récupère les infos d'un ticker."""
    client = YahooClient()
    return client.get_info(ticker)


def get_ticker_options(ticker: str) -> dict:
    """Récupère les options d'un ticker."""
    client = YahooClient()
    return client.get_options(ticker)


if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    client = YahooClient()
    print(f"Testing YahooClient with {ticker}...")
    hist = client.get_history(ticker)
    print(f"  History: {'OK' if not hist.get('error') else hist.get('reason')} ({hist.get('meta',{}).get('rows_count',0)} rows)")
    info = client.get_info(ticker)
    print(f"  Info: {'OK' if not info.get('error') else info.get('reason')}")
    opts = client.get_options(ticker)
    print(f"  Options: {'OK' if not opts.get('error') else opts.get('reason')}")
    news = client.get_news(ticker)
    print(f"  News: {len(news)} items")
