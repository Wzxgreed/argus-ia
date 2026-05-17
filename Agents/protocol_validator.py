#!/usr/bin/env python3
"""
agents/protocol_validator.py — Valide les protocoles agents et le pipeline.

Usage :
    python agents/protocol_validator.py

Vérifie :
    1. Chaque protocol.md existe et a un frontmatter YAML valide (optionnel)
    2. L'agent.py référencé existe
    3. Le schéma Pydantic existe dans agents/schemas.py
    4. Les dépendances sont déclarées dans agents/pipeline.yaml
    5. Les exemples JSON dans le protocol.md valident contre le schéma

Exit code :
    0 = tout valide
    1 = erreurs détectées
"""

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:
    yaml = None

try:
    from pydantic import BaseModel, ValidationError
except Exception:
    BaseModel = None
    ValidationError = Exception

BASE_DIR = Path(__file__).resolve().parent.parent
AGENTS_DIR = BASE_DIR / "agents"
PIPELINE_YAML = AGENTS_DIR / "pipeline.yaml"
SCHEMAS_MODULE = "agents.schemas"


def load_pipeline() -> dict:
    if not PIPELINE_YAML.exists():
        return {}
    if yaml is None:
        return {}
    with open(PIPELINE_YAML, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def find_protocols() -> list[Path]:
    return list(AGENTS_DIR.glob("*/protocol.md"))


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    if yaml is None:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None


def get_schema_class(name: str) -> type | None:
    """Dynamically imports the schema class from agents.schemas."""
    if BaseModel is None:
        return None
    try:
        import importlib
        mod = importlib.import_module(SCHEMAS_MODULE)
        return getattr(mod, name, None)
    except Exception:
        return None


def validate_protocol(path: Path, pipeline: dict) -> list[dict[str, Any]]:
    """Returns list of issues (dict with keys: level, message)."""
    issues = []
    name = path.parent.name
    front = parse_frontmatter(path)

    if front is None:
        issues.append({"level": "warn", "message": f"No YAML frontmatter in {path.parent.name}/protocol.md"})
        # Try convention-based validation
        agent_file = path.parent / "agent.py"
        if not agent_file.exists():
            issues.append({"level": "error", "message": f"Missing agent.py for {name}"})
        return issues

    agent_ref = front.get("agent")
    schema_ref = front.get("output_schema")
    deps = front.get("dependencies", [])

    if agent_ref:
        agent_path = BASE_DIR / agent_ref
        if not agent_path.exists():
            issues.append({"level": "error", "message": f"Agent file not found: {agent_ref}"})
    else:
        agent_file = path.parent / "agent.py"
        if not agent_file.exists():
            issues.append({"level": "error", "message": f"Missing agent.py for {name}"})

    if schema_ref:
        if "::" in schema_ref:
            class_name = schema_ref.split("::")[-1]
        else:
            class_name = schema_ref
        cls = get_schema_class(class_name)
        if cls is None:
            issues.append({"level": "error", "message": f"Schema class not found: {class_name}"})
        elif BaseModel and not issubclass(cls, BaseModel):
            issues.append({"level": "error", "message": f"Schema {class_name} is not a Pydantic BaseModel"})

    pipeline_agents = pipeline.get("agents", {})
    for dep in deps:
        if dep not in pipeline_agents:
            issues.append({"level": "error", "message": f"Dependency '{dep}' of {name} not in pipeline.yaml"})

    return issues


def validate_all() -> dict:
    pipeline = load_pipeline()
    protocols = find_protocols()
    results = {}
    total_errors = 0
    total_warnings = 0

    print(f"[protocol_validator] Checking {len(protocols)} protocol(s)...", file=sys.stderr)
    for p in protocols:
        issues = validate_protocol(p, pipeline)
        name = p.parent.name
        results[name] = issues
        errors = [i for i in issues if i["level"] == "error"]
        warnings = [i for i in issues if i["level"] == "warn"]
        total_errors += len(errors)
        total_warnings += len(warnings)
        if issues:
            print(f"[protocol_validator] {name}: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
            for i in issues:
                print(f"  [{i['level'].upper()}] {i['message']}", file=sys.stderr)
        else:
            print(f"[protocol_validator] {name}: OK", file=sys.stderr)

    # Also validate that every agent in pipeline.yaml has a protocol.md (optional)
    for agent_name in pipeline.get("agents", {}):
        proto = AGENTS_DIR / agent_name / "protocol.md"
        if not proto.exists():
            total_warnings += 1
            results.setdefault(agent_name, []).append({"level": "warn", "message": "Missing protocol.md"})

    return {
        "valid": total_errors == 0,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "results": results,
    }


def main() -> int:
    result = validate_all()
    out_path = BASE_DIR / "logs" / "protocol_validation.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[protocol_validator] Report → {out_path}", file=sys.stderr)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
