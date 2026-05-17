#!/usr/bin/env python3
"""
agents/orchestrator.py — Runner Python du pipeline DAG.

Lit agents/pipeline.yaml, résout le graphe de dépendances,
puis exécute chaque niveau en parallèle via subprocess.

Usage :
    python agents/orchestrator.py           # run normal
    python agents/orchestrator.py --dry-run # vérifie le DAG
    python agents/orchestrator.py --agent=quant  # exécute un seul agent
"""

import argparse
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from agents.dashboard import generate_dashboard

# Make sure scripts/ is on PYTHONPATH for all spawned processes
BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = str(BASE_DIR / "scripts")
AGENTS_DIR = str(BASE_DIR / "agents")
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
PIPELINE_YAML = BASE_DIR / "agents" / "pipeline.yaml"


def set_env():
    pp = os.environ.get("PYTHONPATH", "")
    parts = [p for p in pp.split(":") if p]
    for d in (AGENTS_DIR, SCRIPTS_DIR, str(BASE_DIR)):
        if d not in parts:
            parts.insert(0, d)
    os.environ["PYTHONPATH"] = ":".join(parts)


def load_pipeline(path: Path = PIPELINE_YAML) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_dag(definitions: dict) -> dict[str, set[str]]:
    """Retourne un dict agent -> set(deps)."""
    dag: dict[str, set[str]] = {}
    for name, cfg in definitions.get("agents", {}).items():
        dag[name] = set(cfg.get("deps", []))
    return dag


def topological_levels(dag: dict[str, set[str]]) -> list[list[str]]:
    """
    Groupe les agents par niveau topologique.
    Chaque niveau peut s'exécuter en parallèle.
    """
    remaining = dict(dag)
    levels: list[list[str]] = []
    executed: set[str] = set()

    while remaining:
        # Agents dont toutes les dépendances sont satisfaites
        level = [
            name
            for name, deps in remaining.items()
            if deps <= executed
        ]
        if not level:
            raise ValueError(
                "Cyclic dependency or unsatisfied deps detected in pipeline. "
                f"Remaining: {list(remaining.keys())}"
            )
        levels.append(level)
        executed.update(level)
        for name in level:
            del remaining[name]

    return levels


def run_agent(
    name: str,
    cfg: dict,
    env: dict,
    log_dir: Path,
) -> dict[str, Any]:
    """Exécute un agent (script ou module Python) et retourne les métadonnées."""
    start = time.perf_counter()
    ts = datetime.now(timezone.utc).isoformat()

    # Détermine la commande
    if "script" in cfg:
        cmd = [sys.executable, str(BASE_DIR / cfg["script"])]
    else:
        module = cfg["module"]
        class_name = cfg.get("class", "")
        # Pour les agents BaseAgent, on lance via le module avec -c
        # ou on suppose qu'ils ont un __main__
        cmd = [sys.executable, "-m", module.replace(".", "")]
        # En réalité les agents ont if __name__ == '__main__'
        # donc on peut lancer directement le fichier .py
        agent_file = BASE_DIR / (module.replace(".", "/") + ".py")
        if agent_file.exists():
            cmd = [sys.executable, str(agent_file)]

    allow_fail = cfg.get("allow_fail", False)
    log_file = log_dir / f"{name}.log"

    try:
        with open(log_file, "w", encoding="utf-8") as lf:
            proc = subprocess.run(
                cmd,
                cwd=str(BASE_DIR),
                env=env,
                stdout=lf,
                stderr=subprocess.STDOUT,
                timeout=600,  # 10 min max par agent
            )
        duration = round(time.perf_counter() - start, 3)
        status = "ok" if proc.returncode == 0 else ("skipped" if allow_fail else "failed")
        return {
            "name": name,
            "status": status,
            "exit_code": proc.returncode,
            "duration_sec": duration,
            "ts": ts,
            "cmd": " ".join(cmd),
        }
    except subprocess.TimeoutExpired:
        duration = round(time.perf_counter() - start, 3)
        status = "skipped" if allow_fail else "failed"
        return {
            "name": name,
            "status": status,
            "exit_code": -9,
            "duration_sec": duration,
            "ts": ts,
            "error": "timeout",
        }
    except Exception as exc:
        duration = round(time.perf_counter() - start, 3)
        status = "skipped" if allow_fail else "failed"
        return {
            "name": name,
            "status": status,
            "exit_code": -1,
            "duration_sec": duration,
            "ts": ts,
            "error": str(exc),
        }


def run_pipeline(dry_run: bool = False, single_agent: str | None = None) -> int:
    set_env()
    definitions = load_pipeline()
    dag = build_dag(definitions)
    levels = topological_levels(dag)

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" Argus-IA — Pipeline Orchestrator (Python DAG)")
    print(f" Date: {datetime.now(timezone.utc).isoformat()}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    if dry_run:
        print("\n=== DAG (topological levels) ===")
        for i, level in enumerate(levels, 1):
            print(f"  Level {i}: {', '.join(level)}")
        print("\n=== Agent configs ===")
        for name, cfg in definitions.get("agents", {}).items():
            print(f"  {name}: {cfg}")
        return 0

    # Lockfile — vérifie stale PID (seulement en mode pipeline complet)
    if not single_agent:
        lockfile = DATA_DIR / ".pipeline.lock"
        if lockfile.exists():
            try:
                data = json.loads(lockfile.read_text())
                old_pid = data.get("pid")
                if old_pid:
                    os.kill(old_pid, 0)
                    print(f"ERROR: Pipeline lockfile exists (PID {old_pid} alive).")
                    return 1
            except (ProcessLookupError, ValueError, OSError):
                pass  # PID mort → lockfile stale
            print("WARNING: Stale lockfile removed.")
            lockfile.unlink(missing_ok=True)
        lockfile.write_text(json.dumps({"pid": os.getpid(), "started_at": datetime.now(timezone.utc).isoformat()}))

    log_dir = LOGS_DIR / datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_dir.mkdir(parents=True, exist_ok=True)
    report_file = DATA_DIR / f"pipeline_report_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.json"

    env = dict(os.environ)
    env["PYTHONPATH"] = os.environ.get("PYTHONPATH", "")

    steps: list[dict] = []
    pipeline_start = time.perf_counter()
    phases = {"A": "ok", "B": "ok", "C": "ok", "D": "ok"}

    # Option : run un seul agent
    if single_agent:
        cfg = definitions.get("agents", {}).get(single_agent)
        if not cfg:
            print(f"ERROR: Agent '{single_agent}' not found in pipeline.yaml")
            return 1
        print(f"\n=== Single agent: {single_agent} ===")
        result = run_agent(single_agent, cfg, env, log_dir)
        steps.append(result)
        print(f"  {result['name']}: {result['status']} ({result['duration_sec']}s)")
        if result["status"] == "failed":
            return 1
        return 0

    # Run by levels
    phase_map = {}
    for name, cfg in definitions.get("agents", {}).items():
        # Simple heuristic: first 3 = phase A, next 6 = B, next 8 = C, rest = D
        # In reality we could tag phases in YAML, but this preserves compatibility
        idx = list(definitions.get("agents", {}).keys()).index(name)
        if idx < 3:
            phase_map[name] = "A"
        elif idx < 9:
            phase_map[name] = "B"
        elif idx < 17:
            phase_map[name] = "C"
        else:
            phase_map[name] = "D"

    try:
        for level_idx, level in enumerate(levels, 1):
            print(f"\n=== Level {level_idx} ({len(level)} agents) ===")
            with ThreadPoolExecutor(max_workers=min(len(level), 8)) as pool:
                futures = {
                    pool.submit(run_agent, name, definitions["agents"][name], env, log_dir): name
                    for name in level
                }
                for fut in as_completed(futures):
                    result = fut.result()
                    steps.append(result)
                    phase = phase_map.get(result["name"], "D")
                    if result["status"] == "failed":
                        phases[phase] = "failed"
                    print(f"  [{result['status'].upper()}] {result['name']} — {result['duration_sec']}s")

        # Rapport final
        duration = round(time.perf_counter() - pipeline_start, 3)
        ok = sum(1 for s in steps if s["status"] == "ok")
        skipped = sum(1 for s in steps if s["status"] == "skipped")
        failed = sum(1 for s in steps if s["status"] == "failed")

        report = {
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "started_at": datetime.now(timezone.utc).isoformat(),
            "duration_sec": duration,
            "status": "success" if failed == 0 else "partial" if ok > 0 else "failed",
            "phases": phases,
            "steps": steps,
            "summary": {
                "agents_ok": ok,
                "agents_skipped": skipped,
                "agents_failed": failed,
                "total_steps": len(steps),
            },
        }
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nReport written → {report_file}")

        if failed > 0:
            failed_names = [s["name"] for s in steps if s["status"] == "failed"]
            print(f"\nWARNING: {failed} agent(s) failed: {', '.join(failed_names)}")

        # Generate HTML dashboard
        try:
            dashboard_path = generate_dashboard()
            print(f"Dashboard generated → {dashboard_path}")
        except Exception as exc:
            print(f"Dashboard generation skipped: {exc}")

        print(f"\nPipeline complete — {len(steps)}/{len(steps)} steps in {duration}s.")
        return 0 if failed == 0 else 1

    finally:
        if not single_agent:
            lockfile.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Argus-IA Pipeline Orchestrator")
    parser.add_argument("--dry-run", action="store_true", help="Show DAG without running")
    parser.add_argument("--agent", type=str, default=None, help="Run a single agent")
    args = parser.parse_args()
    return run_pipeline(dry_run=args.dry_run, single_agent=args.agent)


if __name__ == "__main__":
    sys.exit(main())
