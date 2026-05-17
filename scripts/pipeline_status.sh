#!/usr/bin/env bash
# pipeline_status.sh — Surveille l'avancement du pipeline depuis un autre terminal.
#
# Usage:
#   ./scripts/pipeline_status.sh          → état actuel + dernières lignes du log
#   ./scripts/pipeline_status.sh --watch  → tail -f du log en temps réel
#   ./scripts/pipeline_status.sh --wait   → attend la fin et affiche le résumé

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DATE_STR="$(date -u +%Y-%m-%d)"
LOG_FILE="$BASE_DIR/logs/${DATE_STR}_pipeline.log"
LOCK_FILE="$BASE_DIR/data/.pipeline.lock"
CHECKPOINT_FILE="$BASE_DIR/data/.pipeline_checkpoint"
REPORT_FILE="$BASE_DIR/data/pipeline_report_${DATE_STR}.json"

show_status() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo " Argus-IA — Pipeline Status"
    echo " Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # 1. Lockfile
    if [ -f "$LOCK_FILE" ]; then
        local lock_json cpid started
        lock_json="$(cat "$LOCK_FILE")"
        cpid="$(echo "$lock_json" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pid',''))")"
        started="$(echo "$lock_json" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('started_at',''))")"
        if kill -0 "$cpid" 2>/dev/null; then
            echo " Status  : RUNNING (PID $cpid, started $started)"
        else
            echo " Status  : ZOMBIE (PID $cpid mort — lockfile stale)"
            rm -f "$LOCK_FILE"
        fi
    else
        echo " Status  : NOT RUNNING"
    fi

    # 2. Rapport JSON (si disponible)
    if [ -f "$REPORT_FILE" ]; then
        echo ""
        echo "─── Rapport du jour ───"
        python3 <<EOF
import json, sys
from pathlib import Path
r = json.loads(Path("$REPORT_FILE").read_text())
summary = r.get("summary", {})
print(f" Date:        {r['date']}")
print(f" Status:      {r['status']}")
print(f" Duration:    {r['duration_sec']}s")
print(f" Phases:      A={r['phases']['A']} B={r['phases']['B']} C={r['phases']['C']} D={r['phases']['D']}")
print(f" Steps:       {summary.get('agents_ok',0)} OK / {summary.get('agents_skipped',0)} skipped / {summary.get('agents_failed',0)} failed")
print(f" Tickers:     {summary.get('tickers_fetched',0)} OK / {summary.get('tickers_failed',0)} KO")
print(f" DRAFTs:      {summary.get('drafts_init',0)} init + {summary.get('drafts_refresh',0)} refresh")

failed = [s for s in r.get('steps',[]) if s['status'] == 'failed']
if failed:
    print("\n Failed steps:")
    for s in failed:
        print(f"   [{s['step']}] {s['name']}")
EOF
    fi

    # 3. Checkpoint
    if [ -f "$CHECKPOINT_FILE" ]; then
        echo ""
        echo "─── Checkpoint actuel ───"
        python3 -c "import json; d=json.load(open('$CHECKPOINT_FILE')); print(f\" Step {d.get('step','')} — {d.get('status','')}\")"
    fi

    # 4. Dernières lignes du log
    if [ -f "$LOG_FILE" ]; then
        local lines
        lines="$(wc -l < "$LOG_FILE" | tr -d ' ')"
        echo ""
        echo " Log file   : $LOG_FILE ($lines lignes)"
        echo ""
        echo "─── Dernières 15 lignes ───"
        tail -n 15 "$LOG_FILE"
    else
        echo " Log file   : introuvable ($LOG_FILE)"
    fi

    echo ""
    echo " Commandes utiles :"
    echo "   make status                → voir cet état"
    echo "   make wait-pipeline         → attendre la fin + notification"
    echo "   tail -f $LOG_FILE          → suivre le log en temps réel"
}

watch_log() {
    if [ -f "$LOG_FILE" ]; then
        echo "Suivi du log en temps réel (Ctrl+C pour quitter)..."
        tail -n 20 -f "$LOG_FILE"
    else
        echo "Log introuvable. Le pipeline n'a peut-être pas encore démarré."
        exit 1
    fi
}

wait_for_completion() {
    if [ ! -f "$LOCK_FILE" ]; then
        echo "Aucun pipeline en cours (pas de lockfile)."
        # Si un rapport existe déjà pour aujourd'hui, l'afficher
        if [ -f "$REPORT_FILE" ]; then
            echo ""
            python3 <<EOF
import json
from pathlib import Path
r = json.loads(Path("$REPORT_FILE").read_text())
print(f"Dernier rapport : {r['date']} — {r['status']} en {r['duration_sec']}s")
EOF
        fi
        exit 0
    fi

    local cpid started
    cpid="$(python3 -c "import json; d=json.load(open('$LOCK_FILE')); print(d.get('pid',''))")"
    started="$(python3 -c "import json; d=json.load(open('$LOCK_FILE')); print(d.get('started_at',''))")"
    echo "Attente de la fin du pipeline (PID $cpid, started $started)..."

    while kill -0 "$cpid" 2>/dev/null; do
        if [ -f "$CHECKPOINT_FILE" ]; then
            local cp
            cp="$(python3 -c "import json; d=json.load(open('$CHECKPOINT_FILE')); print(f\"Step {d.get('step','')} — {d.get('status','')}\")")"
            printf "\r Step: %-40s" "$cp"
        fi
        sleep 2
    done

    printf "\n"
    echo "Pipeline terminé."

    if [ -f "$REPORT_FILE" ]; then
        echo ""
        echo "─── Résumé final ───"
        python3 <<EOF
import json
from pathlib import Path
r = json.loads(Path("$REPORT_FILE").read_text())
s = r.get("summary", {})
print(f"Status:    {r['status']}")
print(f"Duration:  {r['duration_sec']}s")
print(f"Steps:     {s.get('agents_ok',0)} OK / {s.get('agents_skipped',0)} skipped / {s.get('agents_failed',0)} failed")
print(f"Tickers:   {s.get('tickers_fetched',0)} OK / {s.get('tickers_failed',0)} KO")
EOF
    elif [ -f "$LOG_FILE" ]; then
        echo ""
        echo "─── Dernières lignes du log ───"
        tail -n 5 "$LOG_FILE"
    fi

    # macOS notification
    if command -v osascript >/dev/null 2>&1; then
        osascript -e 'display notification "Pipeline Argus-IA terminé." with title "Argus-IA"'
    fi
}

case "${1:-}" in
    --watch|-w)
        watch_log
        ;;
    --wait|-W)
        wait_for_completion
        ;;
    *)
        show_status
        ;;
esac
