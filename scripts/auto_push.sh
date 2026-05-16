#!/usr/bin/env bash
# auto_push.sh — Commit + push automatique des changements générés par les agents.
# Usage: ./scripts/auto_push.sh ["message de commit optionnel"]

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE_DIR"

# Ensure git user is configured
if [ -z "$(git config --get user.email 2>/dev/null || true)" ]; then
    git config user.email "argus-ia@bot.local"
    git config user.name "Argus-IA Bot"
fi

# Stage generated artefacts + project files that agents may modify
git add data/ Actions/ Actualités/ Opportunités/ Alertes/ Portefeuille/ Agents/ logs/ scripts/ Makefile README.md requirements.txt pyproject.toml .github/ CLAUDE.md INSTALL.md 2>/dev/null || true

# Commit only if there are changes
if git diff --cached --quiet; then
    echo "[auto_push] No changes to commit."
    exit 0
fi

MSG="${1:-Agent snapshot — $(date -u +%Y-%m-%dT%H:%M:%SZ)}"
git commit -m "$MSG" || true

if git push origin main; then
    echo "[auto_push] Pushed to GitHub successfully."
else
    echo "[auto_push] Push failed — check network or credentials."
    exit 1
fi
