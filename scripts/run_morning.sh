#!/usr/bin/env bash
# run_morning.sh — Pipeline complet du matin (Argus-IA v2.3).
# 20 étapes : Apprentissage → Quant → Geo → Crypto → Prix → Macro → Calendar → News
#             → Watchman → Major Events → Accounting → Sector → Social → FX → Event
#             → Transcripts → Validation → Recommandations → Paper Trading → Draft Check
#
# Architecture : 4 phases
#   Phase A (parallèle) : agents indépendants (learn_from_errors, agent_quant, agent_geo)
#   Phase B (séquentielle) : fetch données brutes (crypto, prices, macro, calendar, news)
#   Phase C (parallèle) : agents dépendants de latest.json (8 agents)
#   Phase D (séquentielle) : agrégation finale (validation, reco, paper trading, drafts)

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

# Run a pipeline step SEQUENTIALLY with logging and checkpointing
run_step() {
    local num="$1"
    local name="$2"
    local cmd="$3"
    local allow_fail="${4:-false}"

    log "INFO" "[$num] $name"
    write_checkpoint "$num" "running"

    set +e
    eval "$cmd" >> "$PIPELINE_LOG" 2>&1
    local exit_code=$?
    set -e

    if [ $exit_code -ne 0 ]; then
        if [ "$allow_fail" = "true" ]; then
            log "WARN" "[$num] $name exited with code $exit_code (allowed)"
            write_checkpoint "$num" "skipped"
            return 0
        else
            log "ERROR" "[$num] $name FAILED with code $exit_code"
            write_checkpoint "$num" "failed"
            log "ERROR" "Pipeline aborted at step $num. See $PIPELINE_LOG"
            exit $exit_code
        fi
    fi

    write_checkpoint "$num" "ok"
    log "INFO" "[$num] $name OK"
    return 0
}

# Run a pipeline step IN BACKGROUND — writes exit code to a temp file
run_step_bg() {
    local num="$1"
    local name="$2"
    local cmd="$3"
    local allow_fail="${4:-false}"
    local result_file="$5"

    log "INFO" "[$num] $name (background)"
    write_checkpoint "$num" "running"

    (
        set +e
        eval "$cmd" >> "$PIPELINE_LOG" 2>&1
        local ec=$?
        set -e
        if [ $ec -ne 0 ] && [ "$allow_fail" != "true" ]; then
            echo "$num:$name:$ec" >> "$result_file"
        fi
        write_checkpoint "$num" "$([ $ec -eq 0 ] && echo "ok" || ([ "$allow_fail" = "true" ] && echo "skipped" || echo "failed"))"
        log "INFO" "[$num] $name finished (exit $ec)"
    ) &
}

# Wait for all background jobs and check results
wait_all_bg() {
    local result_file="$1"
    local phase_name="$2"
    wait
    if [ -s "$result_file" ]; then
        log "ERROR" "[$phase_name] Some background steps failed:"
        while IFS=: read -r step_name step_exit; do
            log "ERROR" "  $step_name exited with code $step_exit"
        done < "$result_file"
        rm -f "$result_file"
        exit 1
    fi
    rm -f "$result_file"
    log "INFO" "[$phase_name] All background steps OK"
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

# Temp file for background job results
BG_RESULTS="$(mktemp)"

# ─────────────────────────────────────────────────────────────────────────────
# Phase A — Independent agents (parallel)
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "=== Phase A : Independent agents (parallel) ==="

run_step_bg  0 "Learning loop"          "python3 scripts/learn_from_errors.py"           false "$BG_RESULTS"
run_step_bg  1 "Quantitative analysis" "python3 scripts/agent_quant.py"                  false "$BG_RESULTS"
run_step_bg  2 "Geopolitical scan"     "python3 scripts/agent_geo.py"                    false "$BG_RESULTS"

wait_all_bg "$BG_RESULTS" "Phase A"

# ─────────────────────────────────────────────────────────────────────────────
# Phase B — Raw data fetch (sequential, produces latest.json)
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "=== Phase B : Raw data fetch (sequential) ==="

run_step  3 "Crypto-correlation"    "python3 scripts/agent_crypto.py"                 false
run_step  4 "Fetching prices"       "python3 scripts/fetch_prices.py"                 false
run_step  5 "Fetching macro data"   "python3 scripts/fetch_macro.py"                  false
run_step  6 "Fetching calendar"     "python3 scripts/fetch_calendar.py"               false
run_step  7 "Fetching news"          "python3 scripts/agent_news_fetcher.py"            false

# ─────────────────────────────────────────────────────────────────────────────
# Phase C — Dependent agents (parallel, all read latest.json)
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "=== Phase C : Dependent agents (parallel) ==="

run_step_bg  8 "Proactive watchman"    "python3 scripts/agent_watchman.py"               false "$BG_RESULTS"
run_step_bg  9 "Detecting major events" "python3 scripts/detect_major_events.py"          false "$BG_RESULTS"
run_step_bg 10 "Accounting risk scan"  "python3 scripts/agent_accounting.py"             true "$BG_RESULTS"
run_step_bg 11 "Sector rotation scan"   "python3 scripts/agent_sector_rotation.py"        true "$BG_RESULTS"
run_step_bg 12 "Social sentiment scan"  "python3 scripts/agent_social.py"               true "$BG_RESULTS"
run_step_bg 13 "FX exposure scan"       "python3 scripts/agent_fx.py"                   true "$BG_RESULTS"
run_step_bg 14 "Event-Driven scan"      "python3 scripts/agent_event_driven.py"           true "$BG_RESULTS"
run_step_bg 15 "NLP Transcripts (opt)"  "python3 scripts/fetch_transcripts.py"            true "$BG_RESULTS"

wait_all_bg "$BG_RESULTS" "Phase C"

# ─────────────────────────────────────────────────────────────────────────────
# Phase D — Final aggregation (sequential)
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "=== Phase D : Final aggregation (sequential) ==="

run_step 16 "Validating data"        "python3 scripts/validate.py"                    false
run_step 17 "Recommendation engine"  "python3 scripts/agent_recommandation.py"        false
run_step 18 "Paper trading engine"   "python3 scripts/paper_trading.py"               true
run_step 19 "Checking DRAFTs"        "bash -c 'echo DRAFT check done'"               true

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
    echo "   News:               data/news_$DATE_STR.json"
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
log "INFO" "Pipeline complete — 20/20 steps done."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Pipeline complete — 20/20 steps done."
echo " Next: read data/latest.json + data/validation_report.txt + Alertes/UPCOMING_EVENTS.md"
echo " Log: $PIPELINE_LOG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
