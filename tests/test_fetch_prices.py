#!/usr/bin/env python3
"""Tests unitaires pour fetch_prices.py et yahoo_client.py."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Inject scripts/ dans le path pour les imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fetch_prices import (
    YahooWorkerPool,
    main,
    today_str,
)
from yahoo_client import (
    calc_atr,
    calc_mm,
    calc_rsi,
)


# ─────────────────────────────────────────────────────────────────────────────
# Helpers / Pure functions  (signatures list-based, sans pandas)
# ─────────────────────────────────────────────────────────────────────────────


class TestCalcRSI:
    def test_rsi_basic(self):
        prices = [100, 101, 102, 101, 103, 104, 105]
        rsi = calc_rsi(prices, period=5)
        assert rsi is not None
        assert 0 <= rsi <= 100

    def test_rsi_insufficient_data(self):
        prices = [100, 101]
        rsi = calc_rsi(prices, period=14)
        assert rsi is None

    def test_rsi_flat(self):
        prices = [100] * 20
        rsi = calc_rsi(prices, period=14)
        assert rsi is None or rsi == 100


class TestCalcATR:
    def test_atr_basic(self):
        high = [102, 103, 104]
        low = [98, 99, 100]
        close = [100, 101, 102]
        atr = calc_atr(high, low, close, period=2)
        assert atr is not None
        assert atr > 0

    def test_atr_insufficient_data(self):
        high = [102]
        low = [98]
        close = [100]
        atr = calc_atr(high, low, close, period=14)
        assert atr is None


class TestCalcMM:
    def test_mm_basic(self):
        prices = [100, 101, 102, 103, 104]
        mm = calc_mm(prices, period=3)
        assert mm is not None
        assert mm == pytest.approx(103.0)

    def test_mm_insufficient_data(self):
        prices = [100]
        mm = calc_mm(prices, period=50)
        assert mm is None


class TestTodayStr:
    def test_returns_date_format(self):
        from datetime import datetime, timezone
        expected = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        assert today_str() == expected


# ─────────────────────────────────────────────────────────────────────────────
# YahooWorkerPool init / round-robin
# ─────────────────────────────────────────────────────────────────────────────


class TestYahooWorkerPoolInit:
    @patch("fetch_prices.subprocess.Popen")
    @patch("fetch_prices.YahooWorkerPool._readline")
    def test_single_worker_startup(self, mock_readline, mock_popen):
        mock_proc = MagicMock()
        mock_popen.return_value = mock_proc
        mock_readline.return_value = '{"status":"ready"}'

        pool = YahooWorkerPool(num_workers=1)
        assert len(pool.workers) == 1
        assert len(pool.locks) == 1
        pool.close()

    @patch("fetch_prices.subprocess.Popen")
    @patch("fetch_prices.YahooWorkerPool._readline")
    def test_default_one_worker(self, mock_readline, mock_popen):
        mock_proc = MagicMock()
        mock_popen.return_value = mock_proc
        mock_readline.return_value = '{"status":"ready"}'

        pool = YahooWorkerPool()  # default = 1
        assert pool.num_workers == 1
        pool.close()

    @patch("fetch_prices.subprocess.Popen")
    @patch("fetch_prices.YahooWorkerPool._readline")
    def test_worker_startup_timeout(self, mock_readline, mock_popen):
        mock_proc = MagicMock()
        mock_popen.return_value = mock_proc
        mock_readline.return_value = None  # timeout

        with pytest.raises(RuntimeError, match="timed out"):
            YahooWorkerPool(num_workers=1)


class TestYahooWorkerPoolFetch:
    @patch("fetch_prices.subprocess.Popen")
    @patch("fetch_prices.YahooWorkerPool._readline")
    def test_fetch_success(self, mock_readline, mock_popen):
        mock_proc = MagicMock()
        mock_popen.return_value = mock_proc
        mock_readline.side_effect = [
            '{"status":"ready"}',           # startup
            '{"ticker":"AAPL","error":false}',  # fetch response
        ]

        pool = YahooWorkerPool(num_workers=1)
        result = pool.fetch("AAPL")
        assert result["ticker"] == "AAPL"
        assert result["error"] is False
        assert "timestamp" in result
        pool.close()

    @patch("fetch_prices.subprocess.Popen")
    @patch("fetch_prices.YahooWorkerPool._readline")
    def test_fetch_timeout(self, mock_readline, mock_popen):
        mock_proc = MagicMock()
        mock_popen.return_value = mock_proc
        mock_readline.side_effect = [
            '{"status":"ready"}',
            None,  # fetch timeout
        ]

        pool = YahooWorkerPool(num_workers=1)
        result = pool.fetch("AAPL")
        assert result["error"] is True
        assert "Worker timeout" in result["reason"]
        pool.close()


# ─────────────────────────────────────────────────────────────────────────────
# Main entry point
# ─────────────────────────────────────────────────────────────────────────────


class TestMain:
    @patch("fetch_prices.load_config")
    @patch("fetch_prices.FMPClient")
    @patch("fetch_prices.YahooWorkerPool")
    def test_main_writes_snapshot(self, MockPool, MockFMP, mock_load_config, tmp_path):
        mock_load_config.return_value = {
            "tickers": [{"ticker": "AAPL"}],
        }

        mock_pool = MagicMock()
        mock_pool.fetch.return_value = {
            "ticker": "AAPL",
            "error": False,
            "price": {"close": 190.5},
            "technical": {"rsi14": 55.0, "atr14": 5.0},
            "fundamentals": {"marketCap": 100},
        }
        mock_pool.__enter__ = MagicMock(return_value=mock_pool)
        mock_pool.__exit__ = MagicMock(return_value=False)
        MockPool.return_value = mock_pool

        fmp_mock = MagicMock()
        fmp_mock.api_key = None
        MockFMP.return_value = fmp_mock

        with patch("fetch_prices.DATA_DIR", tmp_path):
            with patch("fetch_prices.CONFIG_PATH", tmp_path / "watchlist.json"):
                exit_code = main()

        assert exit_code == 0
        snapshot_files = [f for f in tmp_path.glob("*.json") if not f.is_symlink()]
        assert len(snapshot_files) == 1
        data = json.loads(snapshot_files[0].read_text())
        assert data["meta"]["tickers_ok"] == 1
        assert data["meta"]["tickers_ko"] == 0

    @patch("fetch_prices.load_config")
    @patch("fetch_prices.FMPClient")
    @patch("fetch_prices.YahooWorkerPool")
    def test_main_with_ko_ticker(self, MockPool, MockFMP, mock_load_config, tmp_path):
        mock_load_config.return_value = {
            "tickers": [{"ticker": "AAPL"}, {"ticker": "BADTKR"}],
        }

        mock_pool = MagicMock()
        def fetch_side_effect(ticker):
            return {
                "ticker": ticker,
                "error": True,
                "reason": "Timeout",
            }
        mock_pool.fetch.side_effect = fetch_side_effect
        mock_pool.__enter__ = MagicMock(return_value=mock_pool)
        mock_pool.__exit__ = MagicMock(return_value=False)
        MockPool.return_value = mock_pool

        fmp_mock = MagicMock()
        fmp_mock.api_key = None
        MockFMP.return_value = fmp_mock

        with patch("fetch_prices.DATA_DIR", tmp_path):
            with patch("fetch_prices.CONFIG_PATH", tmp_path / "watchlist.json"):
                exit_code = main()

        assert exit_code == 0
        snapshot_files = [f for f in tmp_path.glob("*.json") if not f.is_symlink()]
        assert len(snapshot_files) == 1
        data = json.loads(snapshot_files[0].read_text())
        assert data["meta"]["tickers_ok"] == 0
        assert data["meta"]["tickers_ko"] == 2
