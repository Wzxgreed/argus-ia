#!/usr/bin/env bash
# run_morning.sh — Pipeline complet du matin (Argus-IA v3.0).
# Délègue l'exécution à agents/orchestrator.py (DAG Python).
# Ce script conserve : lockfile pre-check, draft detection, auto-push, notification.
#
# Usage : ./scripts/run_morning.sh

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE_DIR"

# Activate virtual environment if present
if [ -f "$BASE_DIR/.venv/bin/activate" ]; then
    source "$BASE_DIR/.venv/bin/activate"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Config paths
# ─────────────────────────────────────────────────────────────────────────────
DATE_STR="$(date -u +%Y-%m-%d)"
LOG_DIR="$BASE_DIR/logs"
mkdir -p "$LOG_DIR"
PIPELINE_LOG="$LOG_DIR/${DATE_STR}_pipeline.log"
REPORT_FILE="$BASE_DIR/data/pipeline_report_${DATE_STR}.json"
LOCK_FILE="$BASE_DIR/data/.pipeline.lock"

# Logging helper
log() {
    local level="$1"
    shift
    local msg="$(date -u '+%Y-%m-%dT%H:%M:%SZ') [$level] $*"
    echo "$msg"
    echo "$msg" >> "$PIPELINE_LOG"
}

# ─────────────────────────────────────────────────────────────────────────────
# Pre-check lockfile (orchestrator also checks, but early exit is friendlier)
# ─────────────────────────────────────────────────────────────────────────────
if [ -f "$LOCK_FILE" ]; then
    locked_pid="$(python3 -c "import json; d=json.load(open('$LOCK_FILE')); print(d.get('pid',''))")"
    if [ -n "$locked_pid" ] && kill -0 "$locked_pid" 2>/dev/null; then
        echo "ERROR: Pipeline déjà en cours (PID $locked_pid)."
        echo "       make status  → surveiller"
        echo "       rm $LOCK_FILE → débloquer"
        exit 1
    else
        echo "WARN: Lockfile stale détecté (PID $locked_pid mort). Suppression."
        rm -f "$LOCK_FILE"
    fi
fi

STARTED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
START_TIME=$(date +%s)

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Argus-IA — Morning Data Pipeline (Orchestrator v3)"
echo " Date: $STARTED_AT"
echo " Log: $PIPELINE_LOG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log "INFO" "Pipeline started"

# ─────────────────────────────────────────────────────────────────────────────
# RUN ORCHESTRATOR
# ─────────────────────────────────────────────────────────────────────────────
set +e
python3 agents/orchestrator.py >> "$PIPELINE_LOG" 2>&1
ORCH_EXIT=$?
set -e

if [ $ORCH_EXIT -ne 0 ]; then
    log "ERROR" "Orchestrator exited with code $ORCH_EXIT. See $PIPELINE_LOG"
    # Keep lockfile cleanup to orchestrator's finally block, but ensure stale removal here
    rm -f "$LOCK_FILE"
    exit $ORCH_EXIT
fi

log "INFO" "Orchestrator completed successfully."

# ─────────────────────────────────────────────────────────────────────────────
# Post-processing : enrich report with drafts + tickers stats
# ─────────────────────────────────────────────────────────────────────────────
DRAFT_INIT_COUNT=0
while IFS= read -r draft; do
    log "WARN" "DRAFT detected: $draft"
    DRAFT_INIT_COUNT=$((DRAFT_INIT_COUNT + 1))
done < <(find Actions -maxdepth 2 -name '*_DRAFT_init.md' -print 2>/dev/null || true)

DRAFT_REFRESH_COUNT=0
while IFS= read -r draft; do
    log "WARN" "FULL REFRESH detected: $draft"
    DRAFT_REFRESH_COUNT=$((DRAFT_REFRESH_COUNT + 1))
done < <(find Actions -maxdepth 2 -name '*_DRAFT_refresh.md' -print 2>/dev/null || true)

TICKERS_OK=0
TICKERS_KO=0
if [ -f "$BASE_DIR/data/$DATE_STR.json" ]; then
    TICKERS_OK="$(python3 -c "import json; d=json.load(open('$BASE_DIR/data/$DATE_STR.json')); print(d.get('meta',{}).get('tickers_ok',0))")"
    TICKERS_KO="$(python3 -c "import json; d=json.load(open('$BASE_DIR/data/$DATE_STR.json')); print(d.get('meta',{}).get('tickers_ko',0))")"
fi

# Enrich existing report JSON if present
if [ -f "$REPORT_FILE" ]; then
    python3 <<EOF
import json, sys
from pathlib import Path

p = Path("$REPORT_FILE")
report = json.loads(p.read_text())
report.setdefault("summary", {})
report["summary"]["tickers_fetched"] = int("$TICKERS_OK")
report["summary"]["tickers_failed"] = int("$TICKERS_KO")
report["summary"]["drafts_init"] = int("$DRAFT_INIT_COUNT")
report["summary"]["drafts_refresh"] = int("$DRAFT_REFRESH_COUNT")
p.write_text(json.dumps(report, indent=2, ensure_ascii=False))
EOF
fi

# ─────────────────────────────────────────────────────────────────────────────
# Validation output listing
# ─────────────────────────────────────────────────────────────────────────────
if [ -f "$BASE_DIR/data/validation_report.txt" ]; then
    echo ""
    echo "📊 DATA FILES AVAILABLE:"
    for f in \
        "Prices+Macro:       data/$DATE_STR.json" \
        "Validation:         data/validation_report.txt" \
        "Quant Report:       data/quant_report_$DATE_STR.json" \
        "Geo Risk:           data/geo_risk_$DATE_STR.json" \
        "Crypto Correlation: data/crypto_correlation_$DATE_STR.json" \
        "News:               data/news_$DATE_STR.json" \
        "FX Exposure:        data/fx_exposure_$DATE_STR.json" \
        "Event-Driven:       data/events_$DATE_STR.json" \
        "Recommandations:    data/recommandations_$DATE_STR.json" \
        "Upcoming Events:    data/upcoming_events_$DATE_STR.json" \
        "Dashboard:          logs/dashboard_$DATE_STR.html" ; do
        echo "   $f"
    done
    if [ -f "$BASE_DIR/data/transcripts_NLP_$DATE_STR.json" ]; then
        echo "   Transcripts:        data/transcripts_NLP_$DATE_STR.json"
    fi
fi

# ─────────────────────────────────────────────────────────────────────────────
# Sync data files to frontend/dist/data/ so the Next.js dashboard stays fresh
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "Syncing fresh data to frontend/dist/data/ ..."
mkdir -p "$BASE_DIR/frontend/dist/data"
# Copy JSON files (follow symlinks so dist gets real files)
find "$BASE_DIR/data" -maxdepth 1 -name '*.json' -exec cp -L {} "$BASE_DIR/frontend/dist/data/" \;
# Also copy the dated snapshot so the dashboard can reference it
if [ -f "$BASE_DIR/data/$DATE_STR.json" ]; then
    cp -L "$BASE_DIR/data/$DATE_STR.json" "$BASE_DIR/frontend/dist/data/"
fi
log "INFO" "Data synced to frontend/dist/data/."

# ─────────────────────────────────────────────────────────────────────────────
# Auto-push to GitHub
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "Checking for changes to push to GitHub..."
if bash "$BASE_DIR/scripts/auto_push.sh" "Pipeline matinal — snapshot du jour." >> "$PIPELINE_LOG" 2>&1; then
    log "INFO" "Changes pushed to GitHub successfully."
else
    log "INFO" "No changes to push or push failed."
fi

# ─────────────────────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────────────────────
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

log "INFO" "Pipeline complete — duration ${DURATION}s."

# Notification desktop (macOS)
if command -v osascript >/dev/null 2>&1; then
    osascript -e "display notification \"Pipeline Argus-IA terminé (${DURATION}s).\" with title \"Argus-IA\""
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Pipeline complete."
echo " Duration: ${DURATION}s"
echo " Report: $REPORT_FILE"
echo " Dashboard: logs/dashboard_$DATE_STR.html"
echo " Log: $PIPELINE_LOG"
echo " Next: read data/latest.json + data/validation_report.txt + Alertes/UPCOMING_EVENTS.md"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
