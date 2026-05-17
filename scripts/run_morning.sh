#!/usr/bin/env bash
# run_morning.sh — Pipeline complet du matin (Argus-IA v2.5).
# 21 étapes : Apprentissage → Quant → Geo → Crypto → Prix → Quality Gate → Macro → Calendar → News
#             → Watchman → Major Events → Accounting → Sector → Social → FX → Event
#             → Transcripts → Validation → Recommandations → Paper Trading → Update Context
#
# Architecture : 4 phases
#   Phase A (parallèle) : agents indépendants (learn_from_errors, agent_quant, agent_geo)
#   Phase B (séquentielle) : fetch données brutes + quality gate (crypto, prices, quality, macro, calendar, news)
#   Phase C (parallèle) : agents dépendants de latest.json (8 agents)
#   Phase D (séquentielle) : agrégation finale (validation, reco, paper trading, update context)

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE_DIR"

# Activate virtual environment if present
if [ -f "$BASE_DIR/.venv/bin/activate" ]; then
    source "$BASE_DIR/.venv/bin/activate"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Lockfile — empêche le lancement simultané
# ─────────────────────────────────────────────────────────────────────────────
LOCK_FILE="$BASE_DIR/data/.pipeline.lock"
REPORT_FILE="$BASE_DIR/data/pipeline_report_$(date -u +%Y-%m-%d).json"

check_lock() {
    if [ -f "$LOCK_FILE" ]; then
        local locked_pid
        locked_pid="$(python3 -c "import sys,json; d=json.load(open('$LOCK_FILE')); print(d.get('pid',''))")"
        if [ -n "$locked_pid" ] && kill -0 "$locked_pid" 2>/dev/null; then
            echo "ERROR: Pipeline déjà en cours (PID $locked_pid)."
            echo "       Utilisez 'make status' pour surveiller, ou"
            echo "       'rm $LOCK_FILE' si le pipeline est bloqué."
            exit 1
        else
            echo "WARN: Lockfile stale détecté (PID $locked_pid mort). Suppression."
            rm -f "$LOCK_FILE"
        fi
    fi
}

write_lock() {
    python3 -c "import json,sys; json.dump({'pid':$$,'started_at':'$(date -u +%Y-%m-%dT%H:%M:%SZ)','version':'2.4'},open('$LOCK_FILE','w'))"
}

remove_lock() {
    rm -f "$LOCK_FILE"
}

# ─────────────────────────────────────────────────────────────────────────────
# Logging & Checkpoints
# ─────────────────────────────────────────────────────────────────────────────
LOG_DIR="$BASE_DIR/logs"
mkdir -p "$LOG_DIR"
DATE_STR="$(date -u +%Y-%m-%d)"
PIPELINE_LOG="$LOG_DIR/${DATE_STR}_pipeline.log"
CHECKPOINT_FILE="$BASE_DIR/data/.pipeline_checkpoint"

# Fichier temporaire pour accumuler les résultats de chaque step
STEPS_LOG="$(mktemp)"

cleanup() {
    rm -f "$STEPS_LOG"
    remove_lock
}
trap cleanup EXIT INT TERM

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

# Helper pour logger le résultat d'un step
log_step_result() {
    local num="$1"
    local name="$2"
    local status="$3"
    echo "{\"step\":$num,\"name\":\"$name\",\"status\":\"$status\",\"ts\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}" >> "$STEPS_LOG"
}

# ─────────────────────────────────────────────────────────────────────────────
# Rapport JSON final
# ─────────────────────────────────────────────────────────────────────────────
generate_report() {
    local status="$1"
    local duration_sec="$2"
    local started_at="$3"
    local tickers_ok="${4:-0}"
    local tickers_ko="${5:-0}"
    local drafts_init="${6:-0}"
    local drafts_refresh="${7:-0}"

    python3 <<EOF
import json, sys
from pathlib import Path

steps = []
phases = {"A": "ok", "B": "ok", "C": "ok", "D": "ok"}
agents_ok = 0
agents_skipped = 0
agents_failed = 0

step_file = Path("$STEPS_LOG")
if step_file.exists():
    for line in step_file.read_text().strip().splitlines():
        if not line.strip():
            continue
        step = json.loads(line)
        steps.append(step)
        st = step["status"]
        if st == "ok":
            agents_ok += 1
        elif st == "skipped":
            agents_skipped += 1
        elif st == "failed":
            agents_failed += 1
            # Déterminer la phase
            num = step["step"]
            if num <= 2:
                phases["A"] = "failed"
            elif num <= 8:
                phases["B"] = "failed"
            elif num <= 16:
                phases["C"] = "failed"
            else:
                phases["D"] = "failed"

report = {
    "date": "$DATE_STR",
    "started_at": "$started_at",
    "finished_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "duration_sec": $duration_sec,
    "status": "$status",
    "phases": phases,
    "steps": steps,
    "summary": {
        "agents_ok": agents_ok,
        "agents_skipped": agents_skipped,
        "agents_failed": agents_failed,
        "total_steps": len(steps),
        "tickers_fetched": $tickers_ok,
        "tickers_failed": $tickers_ko,
        "drafts_init": $drafts_init,
        "drafts_refresh": $drafts_refresh,
    }
}

out = Path("$REPORT_FILE")
out.write_text(json.dumps(report, indent=2, ensure_ascii=False))
print(f"Report written: {out}")
EOF
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
            log_step_result "$num" "$name" "skipped"
            return 0
        else
            log "ERROR" "[$num] $name FAILED with code $exit_code"
            write_checkpoint "$num" "failed"
            log_step_result "$num" "$name" "failed"
            log "ERROR" "Pipeline aborted at step $num. See $PIPELINE_LOG"
            exit $exit_code
        fi
    fi

    write_checkpoint "$num" "ok"
    log "INFO" "[$num] $name OK"
    log_step_result "$num" "$name" "ok"
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
        local status="$([ $ec -eq 0 ] && echo "ok" || ([ "$allow_fail" = "true" ] && echo "skipped" || echo "failed"))"
        write_checkpoint "$num" "$status"
        log_step_result "$num" "$name" "$status"
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
        while IFS=: read -r step_num step_name step_exit; do
            log "ERROR" "  Step $step_num ($step_name) exited with code $step_exit"
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
check_lock
write_lock
STARTED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
START_TIME=$(date +%s)

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Argus-IA — Morning Data Pipeline"
echo " Date: $STARTED_AT"
echo " Log: $PIPELINE_LOG"
echo " Report: $REPORT_FILE"
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

run_step_bg  0 "Learning loop"          "python3 agents/learn_from_errors/agent.py"           false "$BG_RESULTS"
run_step_bg  1 "Quantitative analysis" "python3 agents/quant/agent.py"                  false "$BG_RESULTS"
run_step_bg  2 "Geopolitical scan"     "python3 agents/geo/agent.py"                    false "$BG_RESULTS"

wait_all_bg "$BG_RESULTS" "Phase A"

# ─────────────────────────────────────────────────────────────────────────────
# Phase B — Raw data fetch (sequential, produces latest.json)
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "=== Phase B : Raw data fetch (sequential) ==="

run_step  3 "Crypto-correlation"    "python3 agents/crypto/agent.py"                 false
run_step  4 "Fetching prices"       "python3 scripts/fetch_prices.py"                 false
run_step  5 "Data quality gate"     "python3 agents/data_quality_gate/agent.py"            false
run_step  6 "Fetching macro data"   "python3 scripts/fetch_macro.py"                  false
run_step  7 "Fetching calendar"     "python3 scripts/fetch_calendar.py"               false
run_step  8 "Fetching news"          "python3 agents/news_fetcher/agent.py"            false

# ─────────────────────────────────────────────────────────────────────────────
# Phase C — Dependent agents (parallel, all read latest.json)
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "=== Phase C : Dependent agents (parallel) ==="

run_step_bg  9 "Proactive watchman"    "python3 agents/watchman/agent.py"               false "$BG_RESULTS"
run_step_bg 10 "Detecting major events" "python3 agents/detect_major_events/agent.py"          false "$BG_RESULTS"
run_step_bg 11 "Accounting risk scan"  "python3 agents/accounting/agent.py"             true "$BG_RESULTS"
run_step_bg 12 "Sector rotation scan"   "python3 agents/sector_rotation/agent.py"        true "$BG_RESULTS"
run_step_bg 13 "Social sentiment scan"  "python3 agents/social/agent.py"               true "$BG_RESULTS"
run_step_bg 14 "FX exposure scan"       "python3 agents/fx/agent.py"                   true "$BG_RESULTS"
run_step_bg 15 "Event-Driven scan"      "python3 agents/event_driven/agent.py"           true "$BG_RESULTS"
run_step_bg 16 "NLP Transcripts (opt)"  "python3 agents/fetch_transcripts/agent.py"            true "$BG_RESULTS"

wait_all_bg "$BG_RESULTS" "Phase C"

# ─────────────────────────────────────────────────────────────────────────────
# Phase D — Final aggregation (sequential)
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "=== Phase D : Final aggregation (sequential) ==="

run_step 17 "Validating data"        "python3 scripts/validate.py"                    false
run_step 18 "Recommendation engine"  "python3 agents/recommandation/agent.py"        false
run_step 19 "Paper trading engine"   "python3 agents/paper_trading/agent.py"               true
run_step 20 "Update context memory"  "python3 agents/update_context/agent.py"              true

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
# Extract tickers stats from latest snapshot
# ─────────────────────────────────────────────────────────────────────────────
TICKERS_OK=0
TICKERS_KO=0
if [ -f "$BASE_DIR/data/$DATE_STR.json" ]; then
    TICKERS_OK="$(python3 -c "import sys,json; d=json.load(open('$BASE_DIR/data/$DATE_STR.json')); print(d.get('meta',{}).get('tickers_ok',0))")"
    TICKERS_KO="$(python3 -c "import sys,json; d=json.load(open('$BASE_DIR/data/$DATE_STR.json')); print(d.get('meta',{}).get('tickers_ko',0))")"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Auto-push to GitHub
# ─────────────────────────────────────────────────────────────────────────────
log "INFO" "Checking for changes to push to GitHub..."
GIT_PUSHED="false"
if bash "$BASE_DIR/scripts/auto_push.sh" "Pipeline matinal — snapshot du jour." >> "$PIPELINE_LOG" 2>&1; then
    log "INFO" "Changes pushed to GitHub successfully."
    GIT_PUSHED="true"
else
    log "INFO" "No changes to push or push failed."
fi

# ─────────────────────────────────────────────────────────────────────────────
# Footer + Rapport JSON
# ─────────────────────────────────────────────────────────────────────────────
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
clear_checkpoint

# Générer le rapport JSON final
generate_report "success" "$DURATION" "$STARTED_AT" "$TICKERS_OK" "$TICKERS_KO" "$DRAFT_INIT_COUNT" "$DRAFT_REFRESH_COUNT"

log "INFO" "Pipeline complete — 20/20 steps done in ${DURATION}s."

# Notification desktop (macOS)
if command -v osascript >/dev/null 2>&1; then
    osascript -e "display notification \"Pipeline Argus-IA terminé (${DURATION}s).\" with title \"Argus-IA\""
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Pipeline complete — 20/20 steps done."
echo " Duration: ${DURATION}s"
echo " Report: $REPORT_FILE"
echo " Next: read data/latest.json + data/validation_report.txt + Alertes/UPCOMING_EVENTS.md"
echo " Log: $PIPELINE_LOG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
