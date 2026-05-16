#!/usr/bin/env python3
"""Tests unitaires pour agent_watchman.py."""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from agent_watchman import (
    consolidate_events,
    days_until,
    fetch_earnings_fmp,
    fetch_earnings_yahoo,
    fetch_insider_trades,
    fetch_upgrades_downgrades,
    generate_preview,
    is_future_date,
    load_config,
    parse_date,
    scan_news_proactive,
    today_str,
)


# ─────────────────────────────────────────────────────────────────────────────
# Helpers / Pure functions
# ─────────────────────────────────────────────────────────────────────────────


class TestParseDate:
    def test_iso_format(self):
        assert parse_date("2026-05-16") == "2026-05-16"

    def test_datetime_string(self):
        assert parse_date("2026-05-16 14:30:00") == "2026-05-16"

    def test_none_returns_none(self):
        assert parse_date(None) is None

    def test_invalid_returns_none(self):
        assert parse_date("not-a-date") is None


class TestDaysUntil:
    def test_future_date(self):
        future = (datetime.now(timezone.utc) + __import__("datetime").timedelta(days=5)).strftime("%Y-%m-%d")
        assert days_until(future) == 5

    def test_past_date(self):
        past = (datetime.now(timezone.utc) - __import__("datetime").timedelta(days=5)).strftime("%Y-%m-%d")
        assert days_until(past) == -5

    def test_invalid_returns_none(self):
        assert days_until("bad-date") is None


class TestIsFutureDate:
    def test_today_is_future(self):
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        assert is_future_date(today) is True

    def test_past_is_not_future(self):
        past = (datetime.now(timezone.utc) - __import__("datetime").timedelta(days=1)).strftime("%Y-%m-%d")
        assert is_future_date(past) is False


class TestTodayStr:
    def test_returns_today(self):
        expected = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        assert today_str() == expected


class TestConsolidateEvents:
    def test_dedup_same_type_date(self):
        events = [
            {"type": "earnings", "date": "2026-05-20", "severity": "high"},
            {"type": "earnings", "date": "2026-05-20", "severity": "high"},
            {"type": "news_test", "date": None, "severity": "medium"},
        ]
        result = consolidate_events("AAPL", events)
        # Un seul earnings après déduplication
        assert len(result) == 2
        assert result[0]["ticker"] == "AAPL"

    def test_sort_by_severity_then_days(self):
        events = [
            {"type": "low", "date": "2026-05-20", "severity": "low"},
            {"type": "high", "date": "2026-05-18", "severity": "high"},
            {"type": "med", "date": "2026-05-16", "severity": "medium"},
        ]
        result = consolidate_events("AAPL", events)
        assert result[0]["type"] == "high"
        assert result[1]["type"] == "med"
        assert result[2]["type"] == "low"


# ─────────────────────────────────────────────────────────────────────────────
# Source 1 — Earnings
# ─────────────────────────────────────────────────────────────────────────────


class TestFetchEarningsFMP:
    def test_successful_fetch(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = [
            {
                "date": "2026-05-20",
                "fiscalDateEnding": "Q1 2026",
                "epsEstimate": "2.45",
                "revenueEstimate": "98000000000",
            }
        ]
        result = fetch_earnings_fmp(fmp_mock, "AAPL")
        assert len(result) == 1
        assert result[0]["type"] == "earnings"
        assert result[0]["date"] == "2026-05-20"
        assert "Est EPS $2.45" in result[0]["details"]

    def test_empty_response(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = []
        result = fetch_earnings_fmp(fmp_mock, "AAPL")
        assert result == []

    def test_error_response(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = {"error": True, "reason": "Rate limit"}
        result = fetch_earnings_fmp(fmp_mock, "AAPL")
        assert result == []


class TestFetchEarningsYahoo:
    @patch("agent_watchman.yf.Ticker")
    def test_dict_format(self, MockTicker):
        mock_stock = MagicMock()
        mock_stock.calendar = {
            "Earnings Date": ["2026-05-20"],
            "Earnings Low": 2.40,
            "Earnings High": 2.50,
            "Revenue Average": 98000000000,
        }
        MockTicker.return_value = mock_stock

        result = fetch_earnings_yahoo("AAPL")
        assert len(result) == 1
        assert result[0]["type"] == "earnings"

    @patch("agent_watchman.yf.Ticker")
    def test_none_calendar(self, MockTicker):
        mock_stock = MagicMock()
        mock_stock.calendar = None
        MockTicker.return_value = mock_stock

        result = fetch_earnings_yahoo("AAPL")
        assert result == []

    @patch("agent_watchman.yf.Ticker")
    def test_exception_handling(self, MockTicker):
        MockTicker.side_effect = Exception("Network error")
        result = fetch_earnings_yahoo("AAPL")
        assert result == []


# ─────────────────────────────────────────────────────────────────────────────
# Source 2 — News Scan
# ─────────────────────────────────────────────────────────────────────────────


class TestScanNewsProactive:
    @patch("agent_watchman.yf.Ticker")
    def test_detects_future_keywords(self, MockTicker):
        mock_stock = MagicMock()
        mock_stock.news = [
            {
                "content": {
                    "title": "Apple will announce new products next week",
                    "summary": "The company expects to reveal several innovations",
                    "pubDate": "2026-05-16T10:00:00Z",
                }
            }
        ]
        MockTicker.return_value = mock_stock

        result = scan_news_proactive("AAPL")
        assert len(result) >= 1
        assert any("will_announce" in ev["type"] for ev in result)

    @patch("agent_watchman.yf.Ticker")
    def test_no_match_returns_empty(self, MockTicker):
        mock_stock = MagicMock()
        mock_stock.news = [
            {
                "content": {
                    "title": "Random article about nothing special",
                    "summary": "No keywords here",
                }
            }
        ]
        MockTicker.return_value = mock_stock

        result = scan_news_proactive("AAPL")
        assert result == []

    @patch("agent_watchman.yf.Ticker")
    def test_deduplication(self, MockTicker):
        mock_stock = MagicMock()
        mock_stock.news = [
            {"content": {"title": "Apple will announce something", "summary": ""}},
            {"content": {"title": "Apple will announce something", "summary": ""}},
        ]
        MockTicker.return_value = mock_stock

        result = scan_news_proactive("AAPL")
        # Même titre = dédup
        assert len(result) == 1


# ─────────────────────────────────────────────────────────────────────────────
# Source 3 — Insider Trades
# ─────────────────────────────────────────────────────────────────────────────


class TestFetchInsiderTrades:
    def test_significant_purchase(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = [
            {
                "transactionType": "P - Purchase",
                "dollarValue": 2500000,
                "securitiesTransacted": 10000,
                "transactionPrice": 250.0,
                "transactionDate": "2026-05-10",
                "reportingName": "Tim Cook",
            }
        ]
        result = fetch_insider_trades(fmp_mock, "AAPL")
        assert len(result) == 1
        assert result[0]["type"] == "insider_buy"
        assert result[0]["value"] == 2500000

    def test_small_purchase_filtered_out(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = [
            {
                "transactionType": "P - Purchase",
                "dollarValue": 50000,
                "securitiesTransacted": 100,
                "transactionPrice": 500.0,
                "transactionDate": "2026-05-10",
                "reportingName": "John Doe",
            }
        ]
        result = fetch_insider_trades(fmp_mock, "AAPL")
        assert result == []

    def test_sale_included(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = [
            {
                "transactionType": "S - Sale",
                "dollarValue": 5000000,
                "securitiesTransacted": 20000,
                "transactionPrice": 250.0,
                "transactionDate": "2026-05-10",
                "reportingName": "CFO",
            }
        ]
        result = fetch_insider_trades(fmp_mock, "AAPL")
        assert len(result) == 1
        assert result[0]["type"] == "insider_sell"

    def test_error_response(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = {"error": True}
        result = fetch_insider_trades(fmp_mock, "AAPL")
        assert result == []


# ─────────────────────────────────────────────────────────────────────────────
# Source 4 — Upgrades / Downgrades
# ─────────────────────────────────────────────────────────────────────────────


class TestFetchUpgradesDowngrades:
    def test_upgrade_detected(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = [
            {
                "previousRating": "Hold",
                "newRating": "Buy",
                "publishingFirm": "Goldman Sachs",
                "publishedDate": "2026-05-15",
            }
        ]
        result = fetch_upgrades_downgrades(fmp_mock, "AAPL")
        assert len(result) == 1
        assert result[0]["type"] == "analyst_upgrade"
        assert "Goldman Sachs" in result[0]["details"]

    def test_downgrade_detected(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = [
            {
                "previousRating": "Buy",
                "newRating": "Sell",
                "publishingFirm": "Morgan Stanley",
                "publishedDate": "2026-05-15",
            }
        ]
        result = fetch_upgrades_downgrades(fmp_mock, "AAPL")
        assert len(result) == 1
        assert result[0]["type"] == "analyst_downgrade"

    def test_same_rating_ignored(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = [
            {
                "previousRating": "Buy",
                "newRating": "Buy",
                "publishingFirm": "Some Bank",
                "publishedDate": "2026-05-15",
            }
        ]
        result = fetch_upgrades_downgrades(fmp_mock, "AAPL")
        assert result == []

    def test_error_response(self):
        fmp_mock = MagicMock()
        fmp_mock._get.return_value = {"error": True}
        result = fetch_upgrades_downgrades(fmp_mock, "AAPL")
        assert result == []


# ─────────────────────────────────────────────────────────────────────────────
# Auto-generation helpers
# ─────────────────────────────────────────────────────────────────────────────


class TestGeneratePreview:
    def test_generates_preview_for_earnings_le_3j(self, tmp_path):
        with patch("agent_watchman.BASE_DIR", tmp_path):
            event = {
                "type": "earnings",
                "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "details": "Earnings Q1 2026",
                "source": "yfinance",
                "days_until": 0,
            }
            path = generate_preview("AAPL", event)
            assert path is not None
            assert path.exists()
            content = path.read_text()
            assert "Preview Événement" in content
            assert "AAPL" in content

    def test_no_preview_if_too_far(self, tmp_path):
        with patch("agent_watchman.BASE_DIR", tmp_path):
            event = {
                "type": "earnings",
                "date": (datetime.now(timezone.utc) + __import__("datetime").timedelta(days=10)).strftime("%Y-%m-%d"),
                "details": "Earnings Q2 2026",
                "source": "yfinance",
                "days_until": 10,
            }
            path = generate_preview("AAPL", event)
            assert path is None


# ─────────────────────────────────────────────────────────────────────────────
# Config loading
# ─────────────────────────────────────────────────────────────────────────────


class TestLoadConfig:
    def test_loads_existing_file(self, tmp_path):
        config_path = tmp_path / "watchlist.json"
        data = {"tickers": [{"ticker": "TEST"}]}
        config_path.write_text(json.dumps(data))
        with patch("agent_watchman.CONFIG_PATH", config_path):
            result = load_config()
            assert result["tickers"][0]["ticker"] == "TEST"
