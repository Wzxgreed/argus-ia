# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Snapshot :** 2026-06-01T13:00:19 UTC
> **Type :** `_update.md` (post-pipeline 13h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-01_update.md` (snapshot 10h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 10h00 | État 13h00 | Changement |
|---------|-----------|-----------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 4 / 28 | **4 / 28** | **Stable** (AXA, AST, QTBS, ASTSPACE) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | −1.06% | **−1.06%** | **Stable** |
| XLF return 60j | +0.67% | **+0.67%** | **Stable** |
| XLF RS 20j vs SPY | −6.32% | **−6.32%** | **Stable** |
| XLF RS 60j vs SPY | −10.05% | **−10.05%** | **Stable** |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Signal macro | ROTATION_TO_DEFENSIVE | **ROTATION_TO_DEFENSIVE** | **Stable** |
| Earnings FMP | J0 (2026-06-01) sans détails | **J0 (2026-06-01) sans détails** | **Stable** |

**Verdict :** 20e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument Euronext Paris, non coté US). Aucune variation inter-snapshot détectée entre 10h00 et 13h00 UTC sur les métriques sectorielles, macro ou de scoring. Le secteur Financials (XLF) maintient sa sous-performance relative vs SPY (−6.32% sur 20j, −10.05% sur 60j) avec un momentum nul.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-01T13:00:19 UTC).

**Contexte sectoriel (XLF) — strictement inchangé vs snapshot 10h00 :**
- Return 20j : −1.06% (vs SPY +5.26%)
- Return 60j : +0.67% (vs SPY +10.72%)
- RS 20j vs SPY : −6.32% (stable)
- RS 60j vs SPY : −10.05% (stable)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 4e/11 (stable, hors top 3 et bottom 3)
- Crossover : aucun (stable)

**Interprétation :** Le secteur financier reste en phase de distribution relative vs le marché, avec un creusement structurel à 60j (−10.05% vs SPY). Le signal macro `ROTATION_TO_DEFENSIVE` pénalise les cycliques dont Financials, sans mutation entre les deux snapshots du jour. Sans données AXA, l'évaluation de la force relative du titre vs son secteur reste impossible. Le placeholder Momentum 5.0/10 mériterait un ajustement à la baisse si les données étaient disponibles, compte tenu du headwind sectoriel persistant.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-06-01) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-01"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données. Pattern récurrent d'un earnings glissant sans résolution depuis le 20/05.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-01.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-01.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-01.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-06-01.json`) :
- Exposition FX : **25%** (export, primary currency USD)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned

**Géopolitique** (`geo_risk_latest.json`) :
- Fichier absent (date 2026-05-17). Aucun événement géopolitique spécifique à AXA détecté.

**Social Sentiment** (`social_sentiment_2026-06-01.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 10h00 |
|-------|--------|------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🔴 Thèse ATTENDRE confirmée — DONNÉES STRUCTURELLEMENT MANQUANTES

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 28 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant depuis au moins le 18/05. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US). Aucune mutation inter-snapshot n'a été détectée entre 10h00 et 13h00 UTC. Le contexte sectoriel (XLF) affiche une sous-performance relative stable à 20j (−6.32%) et creusée à 60j (−10.05%), dans un environnement de rotation vers la défensive. L'earnings FMP reste à J0 glissant sans estimates exploitables.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-01T13:00:19 UTC*
