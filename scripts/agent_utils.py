"""scripts/agent_utils.py — Helpers partagés pour tous les agents."""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"


def get_base_dir() -> Path:
    return BASE_DIR


def get_data_dir() -> Path:
    return DATA_DIR


def get_logs_dir() -> Path:
    return LOGS_DIR


def get_config_path() -> Path:
    return CONFIG_PATH


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {"tickers": []}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load_latest() -> dict:
    latest = DATA_DIR / "latest.json"
    if not latest.exists():
        return {}
    target = latest.resolve()
    with open(target, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json_atomic(path: Path, data: dict) -> None:
    """Écriture atomique via tempfile + os.replace."""
    import tempfile
    tmp = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".json", dir=path.parent, delete=False
    )
    json.dump(data, tmp, indent=2, ensure_ascii=False, default=str)
    tmp.flush()
    os.fsync(tmp.fileno())
    tmp.close()
    os.replace(tmp.name, path)


def create_symlink(source: Path, link_name: Path) -> None:
    """Crée ou remplace un symlink relatif."""
    if link_name.exists() or link_name.is_symlink():
        link_name.unlink()
    link_name.symlink_to(source)


def write_json_with_symlink(
    data: dict,
    dated_filename: str,
    symlink_name: str,
    output_dir: Path = DATA_DIR,
) -> Path:
    """
    Écrit un JSON daté et crée/maj un symlink vers le fichier daté.
    Retourne le chemin du fichier daté.
    """
    dated_path = output_dir / dated_filename
    write_json_atomic(dated_path, data)
    symlink_path = output_dir / symlink_name
    create_symlink(dated_path.name, symlink_path)
    return dated_path


def ensure_scripts_path() -> None:
    """Ajoute scripts/ au sys.path si absent (pour imports yahoo_client, fmp_client)."""
    scripts_dir = str(BASE_DIR / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)


def parse_markdown_table(text: str, header_keywords: list[str]) -> list[dict]:
    """Extrait une table markdown par mots-clés d'en-tête."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if not any(kw.lower() in " ".join(cols).lower() for kw in header_keywords):
            continue
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        header = cols
        rows = []
        for j in range(i + 2, len(lines)):
            row_line = lines[j].strip()
            if not row_line.startswith("|"):
                break
            cells = [c.strip() for c in row_line.split("|")[1:-1]]
            if len(cells) != len(header):
                continue
            rows.append({header[idx]: cells[idx] for idx in range(len(header))})
        return rows
    return []
