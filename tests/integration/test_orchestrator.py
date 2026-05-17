#!/usr/bin/env python3
"""Integration tests for the pipeline orchestrator and DAG."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

import pytest
from agents.orchestrator import build_dag, topological_levels, load_pipeline


def test_load_pipeline():
    definitions = load_pipeline()
    assert "agents" in definitions
    assert "learn_from_errors" in definitions["agents"]
    assert "recommandation" in definitions["agents"]


def test_build_dag():
    definitions = load_pipeline()
    dag = build_dag(definitions)
    assert isinstance(dag, dict)
    # Learn has no deps
    assert dag.get("learn_from_errors") == set()
    # Recommandation has many deps
    reco_deps = dag.get("recommandation", set())
    assert "validate" in reco_deps
    assert "quant" in reco_deps


def test_topological_levels_no_cycles():
    definitions = load_pipeline()
    dag = build_dag(definitions)
    levels = topological_levels(dag)
    # All agents appear exactly once across levels
    all_names = []
    for level in levels:
        all_names.extend(level)
    assert len(all_names) == len(set(all_names))
    assert set(all_names) == set(dag.keys())
    # Dependencies of level N must be in previous levels
    seen = set()
    for level in levels:
        for name in level:
            assert dag[name] <= seen, f"Agent {name} has unsatisfied deps"
        seen.update(level)


def test_dry_run():
    """Orchestrator dry-run should exit 0 and print levels."""
    import subprocess
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "agents" / "orchestrator.py"), "--dry-run"],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    assert result.returncode == 0, result.stderr
    assert "Level" in result.stdout
