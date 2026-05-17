#!/usr/bin/env python3
"""
agents/dashboard.py — Générateur de dashboard HTML pour le pipeline.

Usage :
    python agents/dashboard.py [--date YYYY-MM-DD]

Lit :
    data/pipeline_report_YYYY-MM-DD.json
    logs/metrics_YYYY-MM-DD.json  (optionnel)

Produit :
    logs/dashboard_YYYY-MM-DD.html
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Template

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"


def find_latest_report(date_str: str | None = None) -> Path | None:
    if date_str:
        p = DATA_DIR / f"pipeline_report_{date_str}.json"
        return p if p.exists() else None
    # find most recent
    candidates = sorted(DATA_DIR.glob("pipeline_report_*.json"), reverse=True)
    return candidates[0] if candidates else None


def find_metrics(date_str: str | None = None) -> dict:
    if date_str:
        p = LOGS_DIR / f"metrics_{date_str}.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8")).get("metrics", {})
    candidates = sorted(LOGS_DIR.glob("metrics_*.json"), reverse=True)
    if candidates:
        return json.loads(candidates[0].read_text(encoding="utf-8")).get("metrics", {})
    return {}


def generate_dashboard(date_str: str | None = None) -> Path:
    report_path = find_latest_report(date_str)
    if not report_path:
        raise FileNotFoundError("No pipeline report found.")

    report = json.loads(report_path.read_text(encoding="utf-8"))
    date = report.get("date", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    duration = report.get("duration_sec", 0)
    status = report.get("status", "unknown")
    summary = report.get("summary", {})
    steps = report.get("steps", [])
    phases = report.get("phases", {})
    metrics = find_metrics(date)

    status_class = "ok" if status == "success" else ("warn" if status == "partial" else "err")
    phases_ok = sum(1 for v in phases.values() if v == "ok")

    template_path = TEMPLATES_DIR / "dashboard.html"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    template = Template(template_path.read_text(encoding="utf-8"))

    html = template.render(
        date=date,
        duration=duration,
        status=status,
        status_class=status_class,
        agents_ok=summary.get("agents_ok", 0),
        agents_skipped=summary.get("agents_skipped", 0),
        agents_failed=summary.get("agents_failed", 0),
        total_steps=summary.get("total_steps", len(steps)),
        phases_ok=phases_ok,
        steps=steps,
        metrics=metrics,
        steps_json=json.dumps(steps),
        metrics_json=json.dumps(metrics),
    )

    out_dir = LOGS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"dashboard_{date}.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"[dashboard] Generated → {out_path}", file=sys.stderr)
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Argus-IA Dashboard Generator")
    parser.add_argument("--date", type=str, default=None, help="Date override (YYYY-MM-DD)")
    args = parser.parse_args()

    try:
        generate_dashboard(args.date)
        return 0
    except Exception as exc:
        print(f"[dashboard] ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
