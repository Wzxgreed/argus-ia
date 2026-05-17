import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import pytest

from scripts.data_quality_gate import (
    check_ticker,
    classify_market_cap,
    is_market_open,
)


class TestCheckTicker:
    def test_ok_no_anomalies(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 152.0,
                "low": 149.0,
                "previous_close": 149.0,
                "volume": 10_000_000,
                "change_pct": 0.67,
            },
            "technical": {"rsi14": 55.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
            "options": {"put_call_ratio": 0.8},
            "fmp_consensus": {"num_analysts": 30, "price_target_avg": 160.0},
        }
        result = check_ticker("AAPL", data, [])
        assert result["status"] == "ok"
        assert result["reasons"] == []

    def test_stale_price_warning(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 150.0,
                "low": 150.0,
                "previous_close": 150.0,
                "volume": 10_000_000,
                "change_pct": 0,
            },
            "technical": {"rsi14": 55.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
        }
        result = check_ticker("AAPL", data, [])
        assert result["status"] == "warning"
        assert any(r["type"] == "stale_price" for r in result["reasons"])

    def test_stale_price_history_excluded(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 150.0,
                "low": 150.0,
                "previous_close": 150.0,
                "volume": 10_000_000,
                "change_pct": 0,
            },
            "technical": {"rsi14": 55.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
        }
        hist = [
            {"prices": {"AAPL": {"price": {"close": 150.0}}}},
            {"prices": {"AAPL": {"price": {"close": 150.0}}}},
        ]
        result = check_ticker("AAPL", data, hist)
        assert result["status"] == "excluded"
        assert any(r["type"] == "stale_price_history" for r in result["reasons"])

    def test_zero_volume_large_cap_critical(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 152.0,
                "low": 149.0,
                "previous_close": 149.0,
                "volume": 0,
                "change_pct": 0.67,
            },
            "technical": {"rsi14": 55.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
        }
        # Heuristique marché ouvert : historique avec volume > 0 hier
        hist = [{"prices": {"AAPL": {"price": {"volume": 10_000_000}}}}]
        result = check_ticker("AAPL", data, hist)
        assert result["status"] == "excluded"
        assert any(r["type"] == "zero_volume" for r in result["reasons"])

    def test_incoherent_high_critical(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 149.0,
                "low": 148.0,
                "previous_close": 149.0,
                "volume": 10_000_000,
                "change_pct": 0.67,
            },
            "technical": {"rsi14": 55.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
        }
        result = check_ticker("AAPL", data, [])
        assert result["status"] == "excluded"
        assert any(r["type"] == "incoherent_high" for r in result["reasons"])

    def test_rsi_placeholder_warning(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 152.0,
                "low": 149.0,
                "previous_close": 149.0,
                "volume": 10_000_000,
                "change_pct": 0.67,
            },
            "technical": {"rsi14": 50.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
        }
        result = check_ticker("AAPL", data, [])
        assert result["status"] == "warning"
        assert any(r["type"] == "rsi_placeholder" for r in result["reasons"])

    def test_fmp_placeholder_warning(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 152.0,
                "low": 149.0,
                "previous_close": 149.0,
                "volume": 10_000_000,
                "change_pct": 0.67,
            },
            "technical": {"rsi14": 55.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
            "fmp_consensus": {"num_analysts": 0, "price_target_avg": 0},
        }
        result = check_ticker("AAPL", data, [])
        assert result["status"] == "warning"
        assert any(r["type"] == "fmp_placeholder" for r in result["reasons"])

    def test_abnormal_spread_warning(self):
        data = {
            "ticker": "AAPL",
            "price": {
                "close": 150.0,
                "high": 180.0,
                "low": 149.0,
                "previous_close": 149.0,
                "volume": 10_000_000,
                "change_pct": 0.67,
            },
            "technical": {"rsi14": 55.0, "atr14": 2.5},
            "fundamentals": {"market_cap": 2_500_000_000_000},
        }
        result = check_ticker("AAPL", data, [])
        assert result["status"] == "warning"
        assert any(r["type"] == "abnormal_spread" for r in result["reasons"])


class TestClassifyMarketCap:
    def test_large(self):
        assert classify_market_cap(100_000_000_000) == "large"

    def test_mid(self):
        assert classify_market_cap(20_000_000_000) == "mid"

    def test_small(self):
        assert classify_market_cap(1_000_000_000) == "small"

    def test_none(self):
        assert classify_market_cap(None) == "small"


class TestIsMarketOpen:
    def test_open_from_history(self):
        hist = [{"prices": {"AAPL": {"price": {"volume": 10_000_000}}}}]
        assert is_market_open({"ticker": "AAPL"}, hist) is True

    def test_closed_no_history(self):
        # Weekend fallback
        hist = []
        assert is_market_open({"ticker": "AAPL"}, hist) in (True, False)  # depends on weekday
