#!/usr/bin/env bash
# run_morning.sh — Pipeline complet du matin (Argus-IA v2.0).
# 16 étapes : Apprentissage → Quant → Geo → Crypto → Prix → Macro → Calendar → Watchman → Major Events → Accounting → Sector Rotation → Social Sentiment → Transcripts → Validation → Paper Trading → Draft Check

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE_DIR"

# Activate virtual environment if present
if [ -f "$BASE_DIR/.venv/bin/activate" ]; then
    source "$BASE_DIR/.venv/bin/activate"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Argus-IA — Morning Data Pipeline"
echo " Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 0 — BOUCLE D'APPRENTISSAGE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[0/16] Learning loop — checking open tracking windows..."
python3 scripts/learn_from_errors.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 1 — ANALYSE QUANTITATIVE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[1/16] Quantitative analysis — Sharpe, significance, calibration..."
python3 scripts/agent_quant.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 2 — SCAN GÉOPOLITIQUE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[2/16] Geopolitical scan — events, exposure, scenarios..."
python3 scripts/agent_geo.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 3 — CORRÉLATION CRYPTO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[3/16] Crypto-correlation — BTC beta, NAV, divergence..."
python3 scripts/agent_crypto.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 4 — COLLECTE DES PRIX
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[4/16] Fetching prices (Yahoo + FMP Stable)..."
python3 scripts/fetch_prices.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 5 — MACRO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[5/16] Fetching macro data..."
python3 scripts/fetch_macro.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 6 — CALENDRIER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[6/16] Fetching calendar (earnings, economic)..."
python3 scripts/fetch_calendar.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 7 — WATCHMAN (surveillance proactive)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[7/16] Proactive watchman — earnings, CEO, insiders, news, upgrades..."
python3 scripts/agent_watchman.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 8 — DÉTECTION ÉVÉNEMENTS MAJEURS (full refresh)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[8/16] Detecting major events (gap, volume, news, earnings)..."
python3 scripts/detect_major_events.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 9 — ACCOUNTING RISK (fraude & qualité)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[9/16] Accounting risk scan — Beneish M-Score, Altman Z-Score, Piotroski F-Score..."
python3 scripts/agent_accounting.py || true

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 10 — SECTOR ROTATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[10/16] Sector rotation scan — relative strength vs SPY, crossovers, macro alignment..."
python3 scripts/agent_sector_rotation.py || true

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 11 — SOCIAL SENTIMENT (retail)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[11/16] Social media sentiment scan — Reddit retail sentiment, mention spikes, pump detection..."
python3 scripts/agent_social.py || true

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 12 — NLP TRANSCRIPTS (optionnel)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[12/16] NLP Transcript Analysis (FMP)..."
python3 scripts/fetch_transcripts.py || true

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 13 — VALIDATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[13/16] Validating data quality..."
if python3 scripts/validate.py; then
    echo ""
    echo "✅ VALIDATION PASSED — Ready for analysis."
    echo ""
    echo "📊 DATA FILES AVAILABLE:"
    echo "   Prices+Macro:       data/$(date -u +%Y-%m-%d).json"
    echo "   Validation:         data/validation_report.txt"
    echo "   Quant Report:       data/quant_report_$(date -u +%Y-%m-%d).json"
    echo "   Geo Risk:           data/geo_risk_$(date -u +%Y-%m-%d).json"
    echo "   Crypto Correlation: data/crypto_correlation_$(date -u +%Y-%m-%d).json"
    echo "   Upcoming Events:    data/upcoming_events_$(date -u +%Y-%m-%d).json"
    if [ -f "data/transcripts_NLP_$(date -u +%Y-%m-%d).json" ]; then
        echo "   Transcripts:        data/transcripts_NLP_$(date -u +%Y-%m-%d).json"
    fi
else
    echo ""
    echo "❌ VALIDATION FAILED — Review data/validation_report.txt before proceeding."
    exit 1
fi

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 14 — PAPER TRADING ENGINE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[14/16] Running paper trading engine..."
python3 scripts/paper_trading.py || true

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ÉTAPE 15 — CHECK DRAFTS PENDANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo ""
echo "[15/16] Checking for pending DRAFT analyses..."
DRAFT_INIT_COUNT=0
while IFS= read -r draft; do
    echo "  🟡 DRAFT detected: $draft"
    DRAFT_INIT_COUNT=$((DRAFT_INIT_COUNT + 1))
done < <(find Actions -maxdepth 2 -name '*_DRAFT_init.md' -print 2>/dev/null)

DRAFT_REFRESH_COUNT=0
while IFS= read -r draft; do
    echo "  🔴 FULL REFRESH detected: $draft"
    DRAFT_REFRESH_COUNT=$((DRAFT_REFRESH_COUNT + 1))
done < <(find Actions -maxdepth 2 -name '*_DRAFT_refresh.md' -print 2>/dev/null)

if [ "$DRAFT_INIT_COUNT" -eq 0 ] && [ "$DRAFT_REFRESH_COUNT" -eq 0 ]; then
    echo "  ✅ No pending DRAFTs."
else
    echo ""
    echo "  ⚡ Auto-trigger: $DRAFT_INIT_COUNT init DRAFT(s) + $DRAFT_REFRESH_COUNT full refresh(es) ready for LLM completion."
    echo "     The agent will complete them at next session startup (Étape 0a-7 / 0a-8)."
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Pipeline complete — 16/16 steps done."
echo " Next: read data/latest.json + data/validation_report.txt + Alertes/UPCOMING_EVENTS.md"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
