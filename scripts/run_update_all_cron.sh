#!/usr/bin/env bash
# run_update_all_cron.sh — Wrapper cron pour la mise à jour automatique des analyses.
# Lancé en arrière-plan, log dans logs/YYYY-MM-DD_update_all.log

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE_DIR"

# Activate virtual environment if present
if [ -f "$BASE_DIR/.venv/bin/activate" ]; then
    source "$BASE_DIR/.venv/bin/activate"
fi

exec "$BASE_DIR/venv/bin/python3" "$BASE_DIR/scripts/run_update_all.py" "$@"
