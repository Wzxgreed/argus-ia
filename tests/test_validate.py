#!/usr/bin/env python3
"""Tests unitaires pour validate.py."""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from validate import (
    load_latest,
    load_schema,
    main,
    validate_schema,
    validate_snapshot,
)


class TestLoadSchema:
    def test_loads_existing_schema(self):
        schema = load_schema()
        assert schema is not None
        assert schema.get("$schema") is not None
        assert "properties" in schema
        assert "meta" in schema["properties"]
        assert "prices" in schema["properties"]


class TestValidateSchema:
    def test_valid_snapshot(self, sample_snapshot):
        issues = validate_schema(sample_snapshot)
        assert any("JSON Schema validation passed" in i for i in issues)

    def test_missing_meta(self, sample_snapshot):
        bad = dict(sample_snapshot)
        del bad["meta"]
        issues = validate_schema(bad)
        assert any("JSON Schema violation" in i for i in issues)

    def test_invalid_rsi_range(self, sample_snapshot):
        bad = json.loads(json.dumps(sample_snapshot))
        bad["prices"]["AAPL"]["technical"]["rsi14"] = 150
        issues = validate_schema(bad)
        assert any("JSON Schema violation" in i for i in issues)

    def test_invalid_put_call_ratio(self, sample_snapshot):
        bad = json.loads(json.dumps(sample_snapshot))
        bad["prices"]["AAPL"]["options"]["put_call_ratio"] = -0.5
        issues = validate_schema(bad)
        assert any("JSON Schema violation" in i for i in issues)


class TestValidateSnapshot:
    def test_valid_snapshot(self, sample_snapshot):
        with patch("validate.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2026, 5, 16, tzinfo=timezone.utc)
            mock_dt.now(timezone.utc).strftime.return_value = "2026-05-16"
            issues = validate_snapshot(sample_snapshot)
            assert any("[SUMMARY]" in i for i in issues)
            assert sum(1 for i in issues if i.startswith("[ERROR]")) == 0

    def test_empty_snapshot(self):
        issues = validate_snapshot({})
        assert any("[CRITICAL]" in i for i in issues)

    def test_outdated_date(self, sample_snapshot):
        bad = dict(sample_snapshot)
        bad["meta"]["date"] = "2026-05-01"
        issues = validate_snapshot(bad)
        assert any("Snapshot date=" in i for i in issues)

    def test_error_ticker(self, sample_snapshot_with_errors):
        issues = validate_snapshot(sample_snapshot_with_errors)
        assert any("BADTKR: fetch failed" in i for i in issues)

    def test_invalid_rsi(self, sample_snapshot):
        bad = json.loads(json.dumps(sample_snapshot))
        bad["prices"]["AAPL"]["technical"]["rsi14"] = 150
        issues = validate_snapshot(bad)
        assert any("RSI=150 hors range" in i for i in issues)

    def test_flash_crash(self, sample_snapshot):
        bad = json.loads(json.dumps(sample_snapshot))
        bad["prices"]["AAPL"]["price"]["change_pct"] = -60
        issues = validate_snapshot(bad)
        assert any("change -60%" in i for i in issues)

    def test_negative_short_interest(self, sample_snapshot):
        bad = json.loads(json.dumps(sample_snapshot))
        bad["prices"]["AAPL"]["fundamentals"]["short_interest_pct"] = -0.1
        issues = validate_snapshot(bad)
        assert any("SI=-0.1 hors range" in i for i in issues)


class TestMain:
    def test_exit_zero_on_valid(self, sample_snapshot, tmp_path):
        with patch("validate.DATA_DIR", tmp_path):
            with patch("validate.REPORT_PATH", tmp_path / "validation_report.txt"):
                with patch("validate.load_latest", return_value=sample_snapshot):
                    with patch("validate.datetime") as mock_dt:
                        mock_dt.now.return_value = datetime(2026, 5, 16, tzinfo=timezone.utc)
                        mock_dt.now(timezone.utc).strftime.return_value = "2026-05-16"
                        exit_code = main()
        assert exit_code == 0
        assert (tmp_path / "validation_report.txt").exists()

    def test_exit_one_on_critical(self, tmp_path):
        with patch("validate.DATA_DIR", tmp_path):
            with patch("validate.REPORT_PATH", tmp_path / "validation_report.txt"):
                with patch("validate.load_latest", return_value={}):
                    exit_code = main()
        assert exit_code == 1
