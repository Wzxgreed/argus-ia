#!/usr/bin/env bash
# run_morning.sh — Pipeline complet du matin (Argus-IA v2.2).
# 19 étapes : Apprentissage → Quant → Geo → Crypto → Prix → Macro → Calendar → Watchman → Major Events → Accounting → Sector Rotation → Social Sentiment → FX Exposure → Event-Driven → Transcripts → Validation → Recommandations → Paper Trading → Draft Check

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE_DIR"

# Activate virtual environment if present
if [ -f "$BASE_DIR/.venv/bin/activate" ]; then
    source "$BASE_DIR/.venv/bin/activate"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Logging & Checkpoints
# ─────────────────────────────────────────────────────────────────────────────
LOG_DIR="$BASE_DIR/logs"
mkdir -p "$LOG_DIR"
DATE_STR="$(date -u +%Y-%m-%d)"
PIPELINE_LOG="$LOG_DIR/${DATE_STR}_pipeline.log"
CHECKPOINT_FILE="$BASE_DIR/data/.pipeline_checkpoint"

# Logging helper
log() {
    local level="$1"
    shift
    local msg="$(date -u '+%Y-%m-%dT%H:%M:%SZ') [$level] $*"
    echo "$msg"
    echo "$msg" >> "$PIPELINE_LOG"
}

# Checkpoint helpers
write_checkpoint() {
    local step="$1"
    local status="$2"
    echo "{\"date\":\"$DATE_STR\",\"step\":\"$step\",\"status\":\"$status\",\"ts\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}" > "$CHECKPOINT_FILE"
}

read_checkpoint() {
    if [ -f "$CHECKPOINT_FILE" ]; then
        cat "$CHECKPOINT_FILE"
    else
        echo "{\"date\":\"\",\"step\":\"\",\"status\":\"\"}"
    fi
}

clear_checkpoint() {
    rm -f "$CHECKPOINT_FILE"
}

# Run a pipeline step with logging and checkpointing
run_step() {
    local num="$1"
    local name="$2"
    local cmd="$3"
    local allow_fail="${4:-false}"

    log "INFO" "[$num/19] $name"
    write_checkpoint "$num" "running"

    set +e
    eval "$cmd" >> "$PIPELINE_LOG" 2>&1
    local exit_code=$?
    set -e

    if [ $exit_code -ne 0 ]; then
        if [ "$allow_fail" = "true" ]; then
            log "WARN" "[$num/19] $name exited with code $exit_code (allowed)"
            write_checkpoint "$num" "skipped"
            return 0
        else
            log "ERROR" "[$num/19] $name FAILED with code $exit_code"
            write_checkpoint "$num" "failed"
            log "ERROR" "Pipeline aborted at step $num. See $PIPELINE_LOG"
            exit $exit_code
        fi
    fi

    write_checkpoint "$num" "ok"
    log "INFO" "[$num/19] $name OK"
    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Argus-IA — Morning Data Pipeline"
echo " Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo " Log: $PIPELINE_LOG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log "INFO" "Pipeline started"

# Check if resuming from checkpoint
CHECKPOINT=$(read_checkpoint)
if [ -n "$CHECKPOINT" ] && [ "$(echo "$CHECKPOINT" | grep -o '"status":"failed"' || true)" ]; then
    log "INFO" "Resuming from checkpoint: $CHECKPOINT"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Pipeline Steps
# ─────────────────────────────────────────────────────────────────────────────

run_step  0 "Learning loop"          "python3 scripts/learn_from_errors.py"           false
run_step  1 "Quantitative analysis" "python3 scripts/agent_quant.py"                  false
run_step  2 "Geopolitical scan"     "python3 scripts/agent_geo.py"                    false
run_step  3 "Crypto-correlation"    "python3 scripts/agent_crypto.py"                 false
run_step  4 "Fetching prices"       "python3 scripts/fetch_prices.py"                 false
run_step  5 "Fetching macro data"   "python3 scripts/fetch_macro.py"                  false
run_step  6 "Fetching calendar"     "python3 scripts/fetch_calendar.py"               false
run_step  7 "Proactive watchman"    "python3 scripts/agent_watchman.py"               false
run_step  8 "Detecting major events" "python3 scripts/detect_major_events.py"          false
run_step  9 "Accounting risk scan"  "python3 scripts/agent_accounting.py"             true
run_step 10 "Sector rotation scan"   "python3 scripts/agent_sector_rotation.py"        true
run_step 11 "Social sentiment scan"  "python3 scripts/agent_social.py"               true
run_step 12 "FX exposure scan"       "python3 scripts/agent_fx.py"                   true
run_step 13 "Event-Driven scan"      "python3 scripts/agent_event_driven.py"           true
run_step 14 "NLP Transcripts (opt)"  "python3 scripts/fetch_transcripts.py"            true
run_step 15 "Validating data"        "python3 scripts/validate.py"                    false
run_step 16 "Recommendation engine"  "python3 scripts/agent_recommandation.py"        false
run_step 17 "Paper trading engine"   "python3 scripts/paper_trading.py"               true
run_step 18 "Checking DRAFTs"        "bash -c 'echo DRAFT check done'"               true

# ─────────────────────────────────────────────────────────────────────────────
# Validation output
# ─────────────────────────────────────────────────────────────────────────────
if [ -f "$BASE_DIR/data/validation_report.txt" ]; then
    echo ""
    echo "📊 DATA FILES AVAILABLE:"
    echo "   Prices+Macro:       data/$DATE_STR.json"
    echo "   Validation:         data/validation_report.txt"
    echo "   Quant Report:       data/quant_report_$DATE_STR.json"
    echo "   Geo Risk:           data/geo_risk_$DATE_STR.json"
    echo "   Crypto Correlation: data/crypto_correlation_$DATE_STR.json"
    echo "   FX Exposure:        data/fx_exposure_$DATE_STR.json"
    echo "   Event-Driven:       data/events_$DATE_STR.json"
    echo "   Recommandations:    data/recommandations_$DATE_STR.json"
    echo "   Upcoming Events:    data/upcoming_events_$DATE_STR.json"
    if [ -f "$BASE_DIR/data/transcripts_NLP_$DATE_STR.json" ]; then
        echo "   Transcripts:        data/transcripts_NLP_$DATE_STR.json"
    fi
fi

# ─────────────────────────────────────────────────────────────────────────────
# Draft Check
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "Checking for pending DRAFT analyses..."
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

if [ "$DRAFT_INIT_COUNT" -eq 0 ] && [ "$DRAFT_REFRESH_COUNT" -eq 0 ]; then
    log "INFO" "No pending DRAFTs."
else
    log "INFO" "$DRAFT_INIT_COUNT init DRAFT(s) + $DRAFT_REFRESH_COUNT full refresh(es) ready for LLM completion."
fi

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
clear_checkpoint
log "INFO" "Pipeline complete — 19/19 steps done."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Pipeline complete — 19/19 steps done."
echo " Next: read data/latest.json + data/validation_report.txt + Alertes/UPCOMING_EVENTS.md"
echo " Log: $PIPELINE_LOG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
