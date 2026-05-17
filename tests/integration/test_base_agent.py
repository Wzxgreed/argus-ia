#!/usr/bin/env python3
"""Integration tests for BaseAgent and utilities."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

import pytest
from pydantic import BaseModel

from agents.base import BaseAgent


class DummyReport(BaseModel):
    value: int = 42


class DummyAgent(BaseAgent):
    name = "dummy"
    output_schema = DummyReport

    def run(self):
        return DummyReport(value=99)


def test_base_agent_load_config():
    agent = DummyAgent()
    assert isinstance(agent.config, dict)
    assert "tickers" in agent.config or agent.config == {}


def test_base_agent_write_output(tmp_path, monkeypatch):
    agent = DummyAgent()
    # Override data_dir to a temp path for the test
    monkeypatch.setattr(agent, "data_dir", tmp_path)
    report = DummyReport(value=123)
    path = agent.write_output(report, dated_filename="dummy_2026-05-17.json", symlink_name="dummy_latest.json")
    assert path.exists()
    assert (tmp_path / "dummy_latest.json").exists() or (tmp_path / "dummy_latest.json").is_symlink()


def test_base_agent_main():
    agent = DummyAgent()
    # main() calls run() and write_output — we just check it returns 0
    # but we must avoid writing to real data dir; use monkeypatch
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        agent.data_dir = Path(td)
        assert agent.main() == 0
