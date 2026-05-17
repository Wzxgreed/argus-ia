#!/usr/bin/env python3
"""Fixtures et configuration commune pour la suite de tests Argus-IA."""

import json
import sys
from pathlib import Path

import pytest

# Ensure repo root is on PYTHONPATH for agents.* imports
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


TESTS_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = TESTS_DIR / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    """Chemin vers le dossier de fixtures."""
    return FIXTURES_DIR


@pytest.fixture
def sample_watchlist() -> dict:
    """Configuration watchlist minimale pour les tests."""
    return {
        "tickers": [
            {
                "ticker": "AAPL",
                "name": "Apple Inc.",
                "sector": "Tech",
                "priority": "high",
                "exchange": "NASDAQ",
                "notes": "Test ticker",
                "crypto_exposed": False,
            },
            {
                "ticker": "IREN",
                "name": "IREN Limited",
                "sector": "IA Infrastructure",
                "priority": "medium",
                "exchange": "NASDAQ",
                "notes": "Crypto-exposed test",
                "crypto_exposed": True,
            },
        ],
        "macro_symbols": {
            "spx": "^GSPC",
            "vix": "^VIX",
            "us10y": "^TNX",
            "wti": "CL=F",
            "bitcoin": "BTC-USD",
        },
        "settings": {
            "fetch_time": "08:30",
            "timezone": "America/New_York",
            "data_source_primary": "yfinance",
            "data_source_secondary": "fmp",
            "fmp_api_key_env": "FMP_API_KEY",
            "validation_enabled": True,
            "history_retention_days": 180,
        },
    }


@pytest.fixture
def sample_snapshot() -> dict:
    """Snapshot latest.json complet et valide pour les tests de validation."""
    return {
        "meta": {
            "date": "2026-05-16",
            "source": "yfinance",
            "fetched_at": "2026-05-16T08:30:00+00:00",
            "tickers_requested": ["AAPL", "IREN"],
            "tickers_ok": 2,
            "tickers_ko": 0,
        },
        "prices": {
            "AAPL": {
                "ticker": "AAPL",
                "error": False,
                "price": {
                    "open": 190.50,
                    "high": 192.30,
                    "low": 189.80,
                    "close": 191.20,
                    "previous_close": 190.00,
                    "volume": 45000000,
                    "volume_avg_20d": 52000000,
                    "change_pct": 0.63,
                },
                "technical": {
                    "rsi14": 58.4,
                    "atr14": 3.25,
                    "mm50": 188.50,
                    "mm200": 182.30,
                    "golden_cross": True,
                },
                "fundamentals": {
                    "market_cap": 2950000000000,
                    "pe_ratio": 29.5,
                    "forward_pe": 26.2,
                    "ev_ebitda": 22.1,
                    "sector": "Technology",
                    "industry": "Consumer Electronics",
                    "beta": 1.2,
                    "short_interest_pct": 0.0052,
                },
                "options": {
                    "max_pain": 190.0,
                    "put_call_ratio": 0.85,
                    "call_oi_pct": 54.1,
                    "expiration_nearest": "2026-05-23",
                },
                "timestamp": "2026-05-16T08:30:00+00:00",
            },
            "IREN": {
                "ticker": "IREN",
                "error": False,
                "price": {
                    "open": 8.50,
                    "high": 8.90,
                    "low": 8.35,
                    "close": 8.72,
                    "previous_close": 8.45,
                    "volume": 5200000,
                    "volume_avg_20d": 4800000,
                    "change_pct": 3.20,
                },
                "technical": {
                    "rsi14": 62.1,
                    "atr14": 0.45,
                    "mm50": 7.85,
                    "mm200": 6.90,
                    "golden_cross": True,
                },
                "fundamentals": {
                    "market_cap": 1200000000,
                    "pe_ratio": None,
                    "forward_pe": 18.5,
                    "sector": "Technology",
                    "industry": "Cryptocurrency Mining",
                    "beta": 2.4,
                    "short_interest_pct": 0.08,
                },
                "options": {
                    "max_pain": 8.50,
                    "put_call_ratio": 1.12,
                    "call_oi_pct": 47.2,
                    "expiration_nearest": "2026-05-23",
                },
                "timestamp": "2026-05-16T08:30:00+00:00",
            },
        },
        "macro": {
            "meta": {"date": "2026-05-16", "source": "yfinance"},
            "data": {
                "spx": {"value": 5120.5, "change_pct": 0.42},
                "vix": {"value": 14.8, "change_pct": -2.1},
                "us10y": {"value": 4.42, "change_pct": 0.05},
                "wti": {"value": 79.5, "change_pct": 1.2},
                "bitcoin": {"value": 67500.0, "change_pct": 2.1},
            },
        },
    }


@pytest.fixture
def snapshot_with_errors() -> dict:
    """Snapshot avec des erreurs pour tester la tolérance."""
    return {
        "meta": {
            "date": "2026-05-16",
            "source": "yfinance",
            "fetched_at": "2026-05-16T08:30:00+00:00",
            "tickers_requested": ["AAPL", "BADTKR"],
            "tickers_ok": 1,
            "tickers_ko": 1,
        },
        "prices": {
            "AAPL": {
                "ticker": "AAPL",
                "error": False,
                "price": {
                    "open": 190.50,
                    "high": 192.30,
                    "low": 189.80,
                    "close": 191.20,
                    "previous_close": 190.00,
                    "volume": 45000000,
                    "volume_avg_20d": 52000000,
                    "change_pct": 0.63,
                },
                "technical": {
                    "rsi14": 58.4,
                    "atr14": 3.25,
                    "mm50": 188.50,
                    "mm200": 182.30,
                    "golden_cross": True,
                },
                "fundamentals": {
                    "market_cap": 2950000000000,
                    "pe_ratio": 29.5,
                    "sector": "Technology",
                },
                "options": {},
                "timestamp": "2026-05-16T08:30:00+00:00",
            },
            "BADTKR": {
                "ticker": "BADTKR",
                "error": True,
                "reason": "No price history",
            },
        },
        "macro": {
            "meta": {"date": "2026-05-16", "source": "yfinance"},
            "data": {
                "spx": {"value": 5120.5, "change_pct": 0.42},
            },
        },
    }


@pytest.fixture
def mock_yf_history():
    """Retourne un DataFrame pandas simulant l'historique 6 mois d'un ticker."""
    import pandas as pd
    import numpy as np

    dates = pd.date_range(end="2026-05-16", periods=130, freq="D")
    np.random.seed(42)
    base = 190.0
    returns = np.random.normal(0.001, 0.015, len(dates))
    closes = base * np.exp(np.cumsum(returns))
    df = pd.DataFrame(
        {
            "Open": closes * (1 - np.abs(np.random.normal(0, 0.005, len(dates)))),
            "High": closes * (1 + np.abs(np.random.normal(0, 0.008, len(dates)))),
            "Low": closes * (1 - np.abs(np.random.normal(0, 0.008, len(dates)))),
            "Close": closes,
            "Volume": np.random.randint(30_000_000, 60_000_000, len(dates)),
        },
        index=dates,
    )
    return df
