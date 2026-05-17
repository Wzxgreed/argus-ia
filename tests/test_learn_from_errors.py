#!/usr/bin/env python3
"""Tests unitaires pour learn_from_errors.py (calibration engine)."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from learn_from_errors import (
    parse_score,
    parse_j20_verdict,
    compute_win_rates_by_bracket,
    detect_catalyst_streaks,
    CALIBRATION_TARGETS,
)


class TestParseScore:
    def test_standard(self):
        assert parse_score("7.2/10") == 7.2

    def test_no_denominator(self):
        assert parse_score("8.5") == 8.5

    def test_comma(self):
        assert parse_score("7,2/10") == 7.2

    def test_invalid(self):
        assert parse_score("—") is None

    def test_empty(self):
        assert parse_score("") is None


class TestParseJ20Verdict:
    def test_hit(self):
        verdict, ret = parse_j20_verdict("✅ Hit (+13.0%)")
        assert verdict == "hit"
        assert ret == pytest.approx(0.13)

    def test_miss(self):
        verdict, ret = parse_j20_verdict("❌ Miss (-7.0%)")
        assert verdict == "miss"
        assert ret == pytest.approx(-0.07)

    def test_scratch(self):
        verdict, ret = parse_j20_verdict("⚪ Scratch (+0.5%)")
        assert verdict == "scratch"
        assert ret == pytest.approx(0.005)

    def test_pending(self):
        verdict, ret = parse_j20_verdict("⏳ 2026-05-30")
        assert verdict == "pending"
        assert ret is None

    def test_invalidated(self):
        verdict, ret = parse_j20_verdict("🔄 Invalidé")
        assert verdict == "invalidated"
        assert ret is None


class TestComputeWinRatesByBracket:
    def test_basic(self):
        signals = [
            {"score": 7.2, "j20_verdict": "hit", "j20_return": 0.05},
            {"score": 7.5, "j20_verdict": "hit", "j20_return": 0.08},
            {"score": 6.5, "j20_verdict": "miss", "j20_return": -0.05},
            {"score": 8.5, "j20_verdict": "hit", "j20_return": 0.12},
            {"score": 9.5, "j20_verdict": "hit", "j20_return": 0.20},
        ]
        result = compute_win_rates_by_bracket(signals)

        assert "7.0-7.99" in result
        assert result["7.0-7.99"]["total"] == 2
        assert result["7.0-7.99"]["hits"] == 2
        assert result["7.0-7.99"]["win_rate"] == 1.0
        assert result["7.0-7.99"]["avg_return"] == pytest.approx(0.065)

        assert "6.0-6.99" in result
        assert result["6.0-6.99"]["total"] == 1
        assert result["6.0-6.99"]["misses"] == 1
        assert result["6.0-6.99"]["win_rate"] == 0.0

        assert "8.0-8.99" in result
        assert result["8.0-8.99"]["total"] == 1
        assert result["8.0-8.99"]["hits"] == 1

        assert "9.0-10.0" in result
        assert result["9.0-10.0"]["total"] == 1
        assert result["9.0-10.0"]["hits"] == 1

    def test_scratches_excluded(self):
        signals = [
            {"score": 7.0, "j20_verdict": "hit", "j20_return": 0.05},
            {"score": 7.0, "j20_verdict": "scratch", "j20_return": 0.01},
            {"score": 7.0, "j20_verdict": "miss", "j20_return": -0.05},
        ]
        result = compute_win_rates_by_bracket(signals)

        assert result["7.0-7.99"]["total"] == 3
        assert result["7.0-7.99"]["hits"] == 1
        assert result["7.0-7.99"]["misses"] == 1
        assert result["7.0-7.99"]["scratches"] == 1
        # Win rate = hits / (hits + misses) = 1 / 2 = 0.5
        assert result["7.0-7.99"]["win_rate"] == pytest.approx(0.5)

    def test_empty(self):
        result = compute_win_rates_by_bracket([])
        assert result == {}


class TestDetectCatalystStreaks:
    def test_three_misses(self):
        signals = [
            {"score": 7.0, "type": "Earnings beat", "j20_verdict": "miss"},
            {"score": 7.5, "type": "Earnings beat", "j20_verdict": "miss"},
            {"score": 6.8, "type": "Earnings beat", "j20_verdict": "miss"},
            {"score": 7.2, "type": "Upgrade analyste", "j20_verdict": "hit"},
        ]
        alerts = detect_catalyst_streaks(signals)

        assert len(alerts) == 1
        assert alerts[0]["type"] == "Earnings beat"
        assert alerts[0]["streak"] == "miss"
        assert "−0.5 pt" in alerts[0]["action"]

    def test_three_hits(self):
        signals = [
            {"score": 7.0, "type": "Upgrade analyste", "j20_verdict": "hit"},
            {"score": 7.5, "type": "Upgrade analyste", "j20_verdict": "hit"},
            {"score": 6.8, "type": "Upgrade analyste", "j20_verdict": "hit"},
        ]
        alerts = detect_catalyst_streaks(signals)

        assert len(alerts) == 1
        assert alerts[0]["streak"] == "hit"
        assert "+0.3 pt" in alerts[0]["action"]

    def test_no_streak(self):
        signals = [
            {"score": 7.0, "type": "Earnings beat", "j20_verdict": "miss"},
            {"score": 7.5, "type": "Earnings beat", "j20_verdict": "hit"},
        ]
        alerts = detect_catalyst_streaks(signals)
        assert len(alerts) == 0

    def test_multiple_catalysts(self):
        signals = [
            {"score": 7.0, "type": "Earnings beat", "j20_verdict": "miss"},
            {"score": 7.0, "type": "Earnings beat", "j20_verdict": "miss"},
            {"score": 7.0, "type": "Earnings beat", "j20_verdict": "miss"},
            {"score": 7.0, "type": "Upgrade analyste", "j20_verdict": "hit"},
            {"score": 7.0, "type": "Upgrade analyste", "j20_verdict": "hit"},
            {"score": 7.0, "type": "Upgrade analyste", "j20_verdict": "hit"},
        ]
        alerts = detect_catalyst_streaks(signals)
        assert len(alerts) == 2


class TestCalibrationTargets:
    def test_brackets_coverage(self):
        assert (9.0, 10.0) in CALIBRATION_TARGETS
        assert (8.0, 8.99) in CALIBRATION_TARGETS
        assert (7.0, 7.99) in CALIBRATION_TARGETS
        assert (6.0, 6.99) in CALIBRATION_TARGETS

    def test_targets_reasonable(self):
        for bracket, target in CALIBRATION_TARGETS.items():
            assert 0 < target <= 0.70
