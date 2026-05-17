"""agents/observability.py — Logging structuré + métriques pour tous les agents."""

import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


METRICS: dict[str, dict[str, Any]] = {}


def get_log_path(agent_name: str, date_str: str | None = None) -> Path:
    """Chemin du fichier JSONL de log pour un agent donné."""
    if date_str is None:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    base = Path(__file__).resolve().parent.parent / "logs" / "agents" / date_str
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{agent_name}.jsonl"


def log_structured(
    agent: str,
    level: str,
    event: str,
    **kwargs: Any,
) -> None:
    """Écrit une ligne JSONL structurée."""
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "level": level.upper(),
        "agent": agent,
        "event": event,
    }
    entry.update(kwargs)
    log_path = get_log_path(agent)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")


def timer(agent: str, event: str = "run"):
    """Context manager pour mesurer la durée d'une opération."""
    class _Timer:
        def __enter__(self):
            self.start = time.perf_counter()
            log_structured(agent, "INFO", f"{event}_start")
            return self

        def __exit__(self, exc_type, exc, tb):
            duration = time.perf_counter() - self.start
            if exc_type is None:
                log_structured(agent, "INFO", f"{event}_end", duration_sec=round(duration, 3))
                record_metric(agent, "duration_sec", round(duration, 3))
            else:
                log_structured(
                    agent,
                    "ERROR",
                    f"{event}_failed",
                    duration_sec=round(duration, 3),
                    error=str(exc),
                    error_type=exc_type.__name__ if exc_type else None,
                )
                record_metric(agent, "errors", 1)
            return False

    return _Timer()


def record_metric(agent: str, key: str, value: Any) -> None:
    """Stocke une métrique pour un agent."""
    if agent not in METRICS:
        METRICS[agent] = {}
    if key in METRICS[agent] and isinstance(value, (int, float)):
        if isinstance(METRICS[agent][key], (int, float)):
            METRICS[agent][key] += value
        else:
            METRICS[agent][key] = value
    else:
        METRICS[agent][key] = value


def get_metrics() -> dict[str, dict[str, Any]]:
    """Retourne une copie des métriques collectées."""
    return {k: dict(v) for k, v in METRICS.items()}


def reset_metrics() -> None:
    """Réinitialise les métriques (utile entre deux runs)."""
    METRICS.clear()


def write_metrics_report(date_str: str | None = None) -> Path:
    """Écrit un rapport JSON des métriques dans logs/."""
    if date_str is None:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    base = Path(__file__).resolve().parent.parent / "logs"
    base.mkdir(parents=True, exist_ok=True)
    path = base / f"metrics_{date_str}.json"
    data = {
        "date": date_str,
        "metrics": get_metrics(),
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    return path
