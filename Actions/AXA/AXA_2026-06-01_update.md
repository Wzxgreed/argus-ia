# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Snapshot :** 2026-06-01T10:00:01 UTC
> **Type :** `_update.md` (post-pipeline matin)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-05-27_update.md` (snapshot 17h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 2026-05-27 | État 2026-06-01 | Changement |
|---------|----------------|----------------|------------|
| Cours | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 3 / 26 | **4 / 28** | 🔴 **Détérioration** (AXA, AST, QTBS, ASTSPACE) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | −0.96% | **−1.06%** | 🔴 **Dégradation −0.10pp** |
| XLF return 60j | +0.61% | **+0.67%** | 🟢 **Amélioration +0.06pp** |
| XLF RS 20j vs SPY | −6.33% | **−6.32%** | 🟢 **Stable** |
| XLF RS 60j vs SPY | −8.93% | **−10.05%** | 🔴 **Dégradation −1.12pp** |
| XLF momentum score | 0.0/10 | **0.0/10** | Stable |
| Earnings FMP | J0 (2026-05-27) | **J0 (2026-06-01)** | Date calendrier glissante, toujours sans détails |

**Verdict :** 19e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument non coté US — Euronext Paris). Le secteur Financials (XLF) poursuit sa sous-performance relative vs SPY (−6.32% sur 20j, −10.05% sur 60j), sans mutation notable par rapport au close du 27/05. L'earnings FMP reste à J0 glissant sans estimates exploitables.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-01T10:00:01 UTC).

**Contexte sectoriel (XLF) — stable vs close 2026-05-27 :**
- Return 20j : −1.06% (vs SPY +5.26%)
- Return 60j : +0.67% (vs SPY +10.72%)
- RS 20j vs SPY : −6.32% (stable vs −6.33% le 27/05)
- RS 60j vs SPY : −10.05% (dégradation de 1.12pp vs −8.93% le 27/05)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 4e/11 (stable, hors top 3 et bottom 3)

**Interprétation :** Le secteur financier poursuit sa phase de distribution relative vs le marché, avec un creusement du sous-performance à 60j (−10.05% vs SPY). Aucune mutation intermédiaire n'a été détectée entre le 27/05 et le 01/06. Le signal macro du jour est `ROTATION_TO_DEFENSIVE`, ce qui pénalise les secteurs cycliques dont Financials. Sans données AXA, on ne peut évaluer si le titre sur/sous-performe son secteur, mais le headwind sectoriel persiste. Si les données AXA étaient disponibles, le score Momentum placeholder (5.0/10) mériterait probablement un ajustement à la baisse compte tenu de l'écart RS 60j.

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
- Fichier absent. Aucun événement géopolitique spécifique à AXA détecté.

**Social Sentiment** (`social_sentiment_2026-06-01.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot précédent |
|-------|--------|--------------------------------|
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

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 28 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant depuis au moins le 18/05. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US). Le contexte sectoriel (XLF) affiche une sous-performance relative stable à 20j (−6.32%) mais creusée à 60j (−10.05%), dans un environnement de rotation vers la défensive.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-01T10:00:01 UTC*
