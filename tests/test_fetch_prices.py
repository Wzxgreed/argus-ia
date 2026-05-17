#!/usr/bin/env python3
"""Tests unitaires pour fetch_prices.py et yahoo_client.py."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

from concurrent.futures import Future

import pytest

# Inject scripts/ dans le path pour les imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fetch_prices import (
    fetch_ticker_subprocess,
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
# Integration : fetch_ticker_subprocess avec mock subprocess
# ─────────────────────────────────────────────────────────────────────────────


class TestFetchTickerSubprocess:
    @patch("fetch_prices.subprocess.run")
    def test_successful_fetch(self, mock_run):
        payload = {
            "ticker": "AAPL",
            "error": False,
            "price": {"close": 190.5},
            "technical": {"rsi14": 55.0},
        }
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.stdout = json.dumps(payload)
        mock_run.return_value = mock_proc

        result = fetch_ticker_subprocess("AAPL")
        assert result["ticker"] == "AAPL"
        assert result["error"] is False
        assert "timestamp" in result

    @patch("fetch_prices.subprocess.run")
    def test_subprocess_timeout(self, mock_run):
        import subprocess as sp
        mock_run.side_effect = sp.TimeoutExpired(cmd="worker", timeout=30)

        result = fetch_ticker_subprocess("AAPL")
        assert result["error"] is True
        assert "Timeout" in result["reason"]

    @patch("fetch_prices.subprocess.run")
    def test_worker_error(self, mock_run):
        mock_proc = MagicMock()
        mock_proc.returncode = 1
        mock_proc.stderr = "Worker crashed"
        mock_run.return_value = mock_proc

        result = fetch_ticker_subprocess("BAD")
        assert result["error"] is True
        assert "Worker exit code 1" in result["reason"]


# ─────────────────────────────────────────────────────────────────────────────
# Main entry point
# ─────────────────────────────────────────────────────────────────────────────


class TestMain:
    @patch("fetch_prices.load_config")
    @patch("fetch_prices.FMPClient")
    @patch("fetch_prices.ThreadPoolExecutor")
    def test_main_writes_snapshot(self, MockExecutor, MockFMP, mock_load_config, tmp_path):
        mock_load_config.return_value = {
            "tickers": [{"ticker": "AAPL"}],
        }

        def make_future(result):
            f = Future()
            f.set_result(result)
            return f

        def submit_side_effect(fn, ticker):
            return make_future({
                "ticker": ticker,
                "error": False,
                "price": {"close": 190.5},
                "technical": {"rsi14": 55.0, "atr14": 5.0},
                "fundamentals": {"marketCap": 100},
            })

        mock_executor = MagicMock()
        mock_executor.__enter__ = MagicMock(return_value=mock_executor)
        mock_executor.__exit__ = MagicMock(return_value=False)
        mock_executor.submit.side_effect = submit_side_effect
        MockExecutor.return_value = mock_executor

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
    def test_main_with_ko_ticker(self, mock_load_config, tmp_path):
        mock_load_config.return_value = {
            "tickers": [{"ticker": "AAPL"}, {"ticker": "BADTKR"}],
        }

        def make_future(result):
            f = Future()
            f.set_result(result)
            return f

        def submit_side_effect(fn, ticker):
            return make_future({
                "ticker": ticker,
                "error": True,
                "reason": "Timeout",
            })

        mock_executor = MagicMock()
        mock_executor.__enter__ = MagicMock(return_value=mock_executor)
        mock_executor.__exit__ = MagicMock(return_value=False)
        mock_executor.submit.side_effect = submit_side_effect

        with patch("fetch_prices.ThreadPoolExecutor", return_value=mock_executor):
            with patch("fetch_prices.DATA_DIR", tmp_path):
                with patch("fetch_prices.CONFIG_PATH", tmp_path / "watchlist.json"):
                    exit_code = main()

        assert exit_code == 0
        snapshot_files = [f for f in tmp_path.glob("*.json") if not f.is_symlink()]
        assert len(snapshot_files) == 1
        data = json.loads(snapshot_files[0].read_text())
        assert data["meta"]["tickers_ok"] == 0
        assert data["meta"]["tickers_ko"] == 2
