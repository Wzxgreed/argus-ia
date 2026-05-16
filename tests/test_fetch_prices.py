#!/usr/bin/env python3
"""Tests unitaires pour fetch_prices.py."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Inject scripts/ dans le path pour les imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fetch_prices import (
    calc_atr,
    calc_mm,
    calc_rsi,
    fetch_ticker_data,
    main,
    today_str,
)


# ─────────────────────────────────────────────────────────────────────────────
# Helpers / Pure functions
# ─────────────────────────────────────────────────────────────────────────────


class TestCalcRSI:
    def test_rsi_basic(self):
        import pandas as pd
        prices = pd.Series([100, 101, 102, 101, 103, 104, 105])
        rsi = calc_rsi(prices, period=5)
        assert rsi is not None
        assert 0 <= rsi <= 100

    def test_rsi_insufficient_data(self):
        import pandas as pd
        prices = pd.Series([100, 101])
        rsi = calc_rsi(prices, period=14)
        assert rsi is None

    def test_rsi_flat(self):
        import pandas as pd
        prices = pd.Series([100] * 20)
        rsi = calc_rsi(prices, period=14)
        # RSI peut être NaN si aucun gain/loss
        assert rsi is None or rsi == 100


class TestCalcATR:
    def test_atr_basic(self):
        import pandas as pd
        high = pd.Series([102, 103, 104])
        low = pd.Series([98, 99, 100])
        close = pd.Series([100, 101, 102])
        atr = calc_atr(high, low, close, period=2)
        assert atr is not None
        assert atr > 0

    def test_atr_insufficient_data(self):
        import pandas as pd
        high = pd.Series([102])
        low = pd.Series([98])
        close = pd.Series([100])
        atr = calc_atr(high, low, close, period=14)
        assert atr is None


class TestCalcMM:
    def test_mm_basic(self):
        import pandas as pd
        prices = pd.Series([100, 101, 102, 103, 104])
        mm = calc_mm(prices, period=3)
        assert mm is not None
        assert mm == pytest.approx(103.0)

    def test_mm_insufficient_data(self):
        import pandas as pd
        prices = pd.Series([100])
        mm = calc_mm(prices, period=50)
        assert mm is None


class TestTodayStr:
    def test_returns_date_format(self):
        from datetime import datetime, timezone
        expected = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        assert today_str() == expected


# ─────────────────────────────────────────────────────────────────────────────
# Integration-ish : fetch_ticker_data avec mock yfinance
# ─────────────────────────────────────────────────────────────────────────────


class TestFetchTickerData:
    @patch("fetch_prices.yf.Ticker")
    def test_successful_fetch(self, MockTicker, mock_yf_history):
        mock_stock = MagicMock()
        mock_stock.history.return_value = mock_yf_history
        mock_stock.info = {
            "marketCap": 2950000000000,
            "trailingPE": 29.5,
            "sector": "Technology",
            "industry": "Consumer Electronics",
            "beta": 1.2,
            "shortPercentOfFloat": 0.005,
        }
        mock_stock.options = []
        MockTicker.return_value = mock_stock

        result = fetch_ticker_data("AAPL")

        assert result["ticker"] == "AAPL"
        assert result["error"] is False
        assert "price" in result
        assert "technical" in result
        assert "fundamentals" in result
        assert result["price"]["close"] > 0
        assert result["technical"]["rsi14"] is not None
        assert result["technical"]["atr14"] is not None

    @patch("fetch_prices.yf.Ticker")
    def test_empty_history(self, MockTicker):
        import pandas as pd
        mock_stock = MagicMock()
        mock_stock.history.return_value = pd.DataFrame()
        MockTicker.return_value = mock_stock

        result = fetch_ticker_data("BADTKR")

        assert result["error"] is True
        assert "No price history" in result["reason"]

    @patch("fetch_prices.yf.Ticker")
    def test_exception_handling(self, MockTicker):
        MockTicker.side_effect = Exception("Network error")

        result = fetch_ticker_data("AAPL")

        assert result["error"] is True
        assert "Network error" in result["reason"]

    @patch("fetch_prices.yf.Ticker")
    def test_options_data(self, MockTicker, mock_yf_history):
        import pandas as pd
        mock_stock = MagicMock()
        mock_stock.history.return_value = mock_yf_history
        mock_stock.info = {}
        mock_stock.options = ["2026-05-23"]

        # Mock option chain
        mock_calls = pd.DataFrame({
            "strike": [190.0, 195.0, 200.0],
            "openInterest": [5000, 3000, 2000],
        })
        mock_puts = pd.DataFrame({
            "strike": [190.0, 185.0, 180.0],
            "openInterest": [4000, 2500, 1500],
        })
        mock_chain = MagicMock()
        mock_chain.calls = mock_calls
        mock_chain.puts = mock_puts
        mock_stock.option_chain.return_value = mock_chain

        MockTicker.return_value = mock_stock

        result = fetch_ticker_data("AAPL")

        assert result["error"] is False
        opts = result.get("options", {})
        assert "max_pain" in opts
        assert "put_call_ratio" in opts
        assert opts["expiration_nearest"] == "2026-05-23"


# ─────────────────────────────────────────────────────────────────────────────
# Main entry point
# ─────────────────────────────────────────────────────────────────────────────


class TestMain:
    @patch("fetch_prices.load_config")
    @patch("fetch_prices.FMPClient")
    @patch("fetch_prices.yf.Ticker")
    def test_main_writes_snapshot(self, MockTicker, MockFMP, mock_load_config, tmp_path, mock_yf_history):
        mock_load_config.return_value = {
            "tickers": [{"ticker": "AAPL"}],
        }

        mock_stock = MagicMock()
        mock_stock.history.return_value = mock_yf_history
        mock_stock.info = {"marketCap": 100}
        mock_stock.options = []
        MockTicker.return_value = mock_stock

        fmp_mock = MagicMock()
        fmp_mock.api_key = None
        MockFMP.return_value = fmp_mock

        # Override DATA_DIR
        with patch("fetch_prices.DATA_DIR", tmp_path):
            with patch("fetch_prices.CONFIG_PATH", tmp_path / "watchlist.json"):
                exit_code = main()

        assert exit_code == 0
        snapshot_files = list(tmp_path.glob("2026-05-*.json"))
        assert len(snapshot_files) == 1
        data = json.loads(snapshot_files[0].read_text())
        assert data["meta"]["tickers_ok"] == 1
        assert data["meta"]["tickers_ko"] == 0

    @patch("fetch_prices.load_config")
    def test_main_with_ko_ticker(self, mock_load_config, tmp_path):
        mock_load_config.return_value = {
            "tickers": [{"ticker": "AAPL"}, {"ticker": "BADTKR"}],
        }

        with patch("fetch_prices.DATA_DIR", tmp_path):
            with patch("fetch_prices.CONFIG_PATH", tmp_path / "watchlist.json"):
                with patch("fetch_prices.yf.Ticker") as MockTicker:
                    mock_stock = MagicMock()
                    import pandas as pd
                    mock_stock.history.return_value = pd.DataFrame()
                    MockTicker.return_value = mock_stock
                    exit_code = main()

        assert exit_code == 0
        snapshot_files = list(tmp_path.glob("2026-05-*.json"))
        assert len(snapshot_files) == 1
        data = json.loads(snapshot_files[0].read_text())
        assert data["meta"]["tickers_ok"] == 0
        assert data["meta"]["tickers_ko"] == 2
