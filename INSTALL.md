# Argus-IA — Installation & Configuration Rapide

![CI](https://github.com/sachajoly/argus-ia/actions/workflows/ci.yml/badge.svg)

> **Note :** Le badge CI ci-dessus s'activera une fois le repository poussé sur GitHub. Pour le moment, le workflow est prêt dans `.github/workflows/ci.yml`.

## 1. Prérequis

- Python 3.10+
- macOS / Linux / WSL

## 2. Installation (une seule fois)

```bash
cd /Users/sachajoly/Documents/Argus-IA

# Créer l'environnement virtuel
python3 -m venv .venv

# Activer l'environnement
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Vérifier l'installation
python scripts/fetch_prices.py
```

## 3. Configuration FMP (si vous avez une clé payante)

1. Copier `.env` en `.env.local` :
   ```bash
   cp .env .env.local
   ```

2. Éditer `.env.local` et remplacer `your_fmp_api_key_here` par votre clé FMP :
   ```bash
   FMP_API_KEY=abc123def456ghi789  # votre vraie clé
   ```

3. Le fichier `.env.local` est ignoré par Git — votre clé reste locale.

### Limitations du plan Starter ($19/mois)

Le plan **Starter** donne accès aux endpoints **Stable API** suivants :
- ✅ `quote`, `profile`
- ✅ `price-target-summary` (consensus analystes)
- ✅ `ratios`, `key-metrics` (données **annuelles** uniquement)
- ✅ `income-statement`, `balance-sheet-statement`, `cash-flow-statement` (annuel)

Le plan Starter **ne donne PAS accès** à :
- ❌ `earning-call-transcript` (transcripts) → 402, nécessite Enterprise+
- ❌ Données `quarterly` sur ratios/métriques → 402, nécessite plan supérieur
- ❌ `upgrades-downgrades`, `insider-trading`, `dcf` → 404/402

> **Conséquence :** `fetch_transcripts.py` fonctionnera mais retournera 0 transcript avec le message explicite "Plan FMP insuffisant". Les agents devront analyser les transcripts manuellement ou via d'autres sources. Le pipeline principal (`fetch_prices.py`) fonctionne pleinement avec les données annuelles.

## 4. Lancer le pipeline du matin

```bash
bash scripts/run_morning.sh
```

Ou manuellement (step by step) :
```bash
source .venv/bin/activate
python scripts/fetch_prices.py      # cours + volumes + technique + fondamentaux + options
python scripts/fetch_macro.py       # indices + VIX + taux + FX + commodités + régime macro
python scripts/fetch_calendar.py    # earnings dates + alertes imminentes
python scripts/fetch_transcripts.py # NLP transcripts (FMP uniquement — skipped si pas de clé)
python scripts/validate.py          # sanity checks + rapport
```

## 5. Résultat attendu

```
data/
├── 2026-05-16.json                    ← snapshot complet du jour (prix + macro + calendar)
├── latest.json                        ← symlink vers le snapshot actuel
├── validation_report.txt              ← "5/5 OK, 0 errors, 0 warnings"
├── transcripts_NLP_2026-05-16.json    ← analyse NLP management (si FMP activé)
├── transcripts_NLP_latest.json        ← symlink vers le dernier NLP
└── history/
    └── prices/                        ← (futur) timeseries pour backtesting
```

### Contenu du snapshot `YYYY-MM-DD.json`

```json
{
  "meta": { "date": "2026-05-16", "tickers_ok": 5, "tickers_ko": 0 },
  "prices": {
    "IREN": {
      "price": { "close": 52.94, "volume": 48511300, "change_pct": -9.35 },
      "technical": { "rsi14": 54.61, "atr14": 5.50, "mm50": 44.72 },
      "fundamentals": { "market_cap": 18919626752, "pe_ratio": 68.75 },
      "options": { "max_pain": 33.0, "put_call_ratio": 1.47 },
      "fmp_consensus": { "revenue_estimate": 890000000, "eps_estimate": 0.42 },
      "fmp_upgrades": { "upgrades": 3, "downgrades": 0 },
      "fmp_insiders": { "buys_count": 2, "sells_count": 0, "net_value_usd": 1450000 },
      "fmp_ratios": { "roe": 0.15, "roic": 0.12, "gross_margin": 0.45 }
    }
  },
  "macro": {
    "data": { "vix": {"value": 21.34}, "spx": {"value": 7412.84} },
    "regime": { "regime": "Stagflation", "weights": {"catalyst": 0.35, ...}, "macro_bonus": -1.5 }
  },
  "calendar": { "earnings": [...], "alerts": [] }
}
```

## 6. Intégration dans le workflow

L'agent lit automatiquement `data/latest.json` et `data/validation_report.txt` au début de chaque session (Étape 0a du `CLAUDE.md`).

**Règle absolue :** l'utilise exclusivement les chiffres de `latest.json`. Jamais de "devinettes".

---

## 7. CI et gestion des secrets (GitHub Actions)

Le workflow CI (`.github/workflows/ci.yml`) **ne dispose pas de clés API** et ne fetch jamais de données réelles en production. Il exécute uniquement :

- **Lint** et **format** (Ruff, Black)
- **Tests unitaires** avec mocks (`pytest -m "not integration and not slow"`)
- **Validation JSON Schema** sur un exemple statique

### Pourquoi pas de clés en CI ?

Les appels API (Yahoo Finance, FMP, Reddit) sont soumis à des rate-limits et nécessitent des credentials. Les tests d'intégration contre ces services doivent être lancés **localement** avec votre `.env.local`.

### Si vous voulez ajouter des tests d'intégration en CI

1. Allez dans **Settings > Secrets and variables > Actions** de votre repo GitHub
2. Ajoutez `FMP_API_KEY` (et autres secrets nécessaires)
3. Modifiez le workflow pour conditionner les tests d'intégration :
   ```yaml
   - name: Run integration tests
     if: github.event_name == 'push' && secrets.FMP_API_KEY != ''
     run: pytest tests/ -m integration -v
   ```
4. Gardez un oeil sur les rate-limits : les CI runners partagent des IP publiques.

### Fichiers sensibles

| Fichier | Rôle | Git-tracked ? |
|---------|------|---------------|
| `.env` | Template (clés vides) | Oui |
| `.env.local` | Vos vraies clés API | Non (`.gitignore`) |
| `data/latest.json` | Snapshot généré localement | Peut être commité par `auto_push.sh` |

> **Règle absolue :** ne jamais commiter `.env.local`. Le `.gitignore` le protège, mais vérifiez avant chaque `git add -A`.

---

## Dépendances

| Package | Version min | Usage |
|---------|-------------|-------|
| yfinance | >= 0.2.54 | Cours, volumes, fondamentaux Yahoo |
| pandas | >= 2.0 | Calculs RSI, ATR, moyennes mobiles |
| requests | >= 2.31 | Appels API FMP (futur) |
| python-dotenv | >= 1.0 | Chargement des clés API depuis `.env.local` |

---

## Dépannage

### `ModuleNotFoundError: No module named 'yfinance'`
→ Vous n'avez pas activé le venv : `source .venv/bin/activate`

### `yfinance` rate-limiting (erreurs après X tickers)
→ Normal avec Yahoo. Le script gère ça automatiquement. Si persistant : ajouter `time.sleep(2)` entre les tickers.

### `FMP_API_KEY` non trouvée
→ Vérifiez que `.env.local` existe et contient bien `FMP_API_KEY=...`
→ Le script chargera automatiquement `.env.local` via `python-dotenv`

### Données macro null (ex: DXY, taux)
→ Yahoo utilise des symboles spéciaux (`^TNX`, `DX-Y.NYB`). Vérifiez dans `config/watchlist.json` → `macro_symbols`.
