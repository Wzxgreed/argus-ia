#!/usr/bin/env bash
# scripts/analyse_ticker.sh
# Workflow : ajoute un ticker à la watchlist, fetch les données, puis l'analyse LLM
# Usage : ./scripts/analyse_ticker.sh [TICKER]

set -euo pipefail

TICKER="${1:-}"
if [ -z "$TICKER" ]; then
  echo "Usage: $0 <TICKER>"
  echo "Example: $0 NOK"
  exit 1
fi

CONFIG="config/watchlist.json"
WATCHLIST_DIR="$(dirname "$0")/.."
cd "$WATCHLIST_DIR"

# ── Étape 1 : Vérifier / ajouter le ticker à la watchlist ──────────────────────
if grep -q "\"ticker\": \"$TICKER\"" "$CONFIG"; then
  echo "✓ $TICKER déjà dans la watchlist"
else
  echo "➕ Ajout de $TICKER à la watchlist..."
  python3 -c "
import json, sys
with open('$CONFIG', 'r') as f:
    data = json.load(f)
name = input('Nom de l entreprise pour $TICKER : ')
sector = input('Secteur : ')
priority = input('Priorité (high/medium/low) [medium]: ') or 'medium'
exchange = input('Exchange (NYSE/NASDAQ/Euronext) : ')
notes = input('Notes : ')

data['tickers'].append({
    'ticker': '$TICKER',
    'name': name,
    'sector': sector,
    'priority': priority,
    'exchange': exchange,
    'notes': notes
})
with open('$CONFIG', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f'✓ $TICKER ajouté à la watchlist')
"
fi

# ── Étape 2 : Fetch des données ────────────────────────────────────────────────
echo ""
echo "📡 Fetch des données pour $TICKER (et tous les tickers watchlist)..."
source .venv/bin/activate
python3 scripts/fetch_prices.py --tickers "$TICKER"

echo ""
echo "✅ Données récupérées. Vérification :"
python3 -c "
import json
try:
    with open('data/latest.json') as f:
        d = json.load(f)
    p = d['prices'].get('$TICKER')
    if p:
        print(f'  Cours: \${p[\"price\"][\"close\"]}')
        print(f'  RSI: {p[\"technical\"][\"rsi14\"]}')
        print(f'  ATR: \${p[\"technical\"][\"atr14\"]}')
        print(f'  P/E: {p[\"fundamentals\"][\"pe_ratio\"]}')
        print(f'  Consensus: {p.get(\"fmp_consensus\", {}).get(\"price_target_avg\", \"N/A\")}')
    else:
        print('  ⚠️ $TICKER absent de latest.json')
except Exception as e:
    print(f'  ⚠️ Erreur: {e}')
"

# ── Étape 3 : Copier dans dist/data (si le frontend existe) ──────────────────
if [ -d "frontend/dist/data" ]; then
  echo ""
  echo "📦 Copie des données dans frontend/dist/data/..."
  cd frontend && node scripts/copy-data.js
  cd ..
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ $TICKER prêt pour analyse"
echo ""
echo "  Données disponibles dans :"
echo "    • data/latest.json"
echo "    • data/2026-05-17.json (snapshot daté)"
echo ""
echo "  Prochaine étape : lancer l'analyse LLM"
echo "    → 'Analyse $TICKER' dans Claude Code"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
