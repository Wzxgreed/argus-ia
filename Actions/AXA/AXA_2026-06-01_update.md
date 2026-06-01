# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Snapshot :** 2026-06-01T17:00:14 UTC
> **Type :** `_update.md` (post-pipeline 17h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-01_update.md` (snapshot 13h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 13h00 | État 17h00 | Changement |
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
| XLF return 20j | −1.06% | **−1.13%** | 🔴 Légère dégradation |
| XLF return 60j | +0.67% | **+0.72%** | 🟢 Stable |
| XLF RS 20j vs SPY | −6.32% | **−6.28%** | 🟢 Stable |
| XLF RS 60j vs SPY | −10.05% | **−10.81%** | 🔴 Creusement |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Signal macro | ROTATION_TO_DEFENSIVE | **ROTATION_TO_CYCLICAL** | 🟡 **Mutation** |
| Earnings FMP | J0 (2026-06-01) sans détails | **J0 (2026-06-01) sans détails** | **Stable** |

**Verdict :** 21e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (`error: true`, `reason: "No price history"`). Une **mutation sectorielle** est détectée entre 13h00 et 17h00 UTC : le signal macro bascule de `ROTATION_TO_DEFENSIVE` à `ROTATION_TO_CYCLICAL`, porté par le crossover haussier de XLE (Energy) et la domination de XLK (Technology, momentum 10.0/10). XLF (Financials) reste classé 3e/11 mais avec un momentum nul (0.0/10) et une sous-performance relative creusée à 60j (−10.81% vs SPY).

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-01T17:00:14 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — mutation signal macro détectée :**
- Return 20j : −1.13% (vs SPY +5.16%)
- Return 60j : +0.72% (vs SPY +11.53%)
- RS 20j vs SPY : −6.28% (stable vs −6.32% à 13h00)
- RS 60j vs SPY : −10.81% (dégradé vs −10.05% à 13h00)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 3e/11 (stable, mais par artefact de classement)
- Crossover : aucun sur XLF (BULLISH_CROSSOVER sur XLE uniquement)
- Signal macro : `ROTATION_TO_CYCLICAL` (mutation vs `ROTATION_TO_DEFENSIVE` à 13h00)

**Interprétation :** Le basculement du signal macro vers `ROTATION_TO_CYCLICAL` est principalement porté par XLK (return 20j +20.9%, momentum 10.0/10) et le crossover haussier de XLE. XLF (Financials) profite marginalement de ce reclassement (3e position sectorielle) mais sans momentum propre. Le creusement du RS 60j à −10.81% confirme que le secteur financier reste en phase de distribution relative structurelle vs le marché. Sans données AXA, l'évaluation de la force relative du titre vs son secteur reste impossible. Le placeholder Momentum 5.0/10 est maintenu mais mériterait un ajustement à la baisse si les données étaient disponibles.

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
- Fichier daté 2026-05-17. Aucun événement géopolitique spécifique à AXA détecté.

**Social Sentiment** (`social_sentiment_2026-06-01.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 13h00 |
|-------|--------|------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** Le basculement du signal macro à `ROTATION_TO_CYCLICAL` ne modifie pas le score Opportunité d'AXA car (i) aucune donnée de prix n'est disponible pour recalculer le Momentum, (ii) XLF n'affiche aucun momentum propre (0.0/10), et (iii) le creusement du RS 60j à −10.81% maintient un headwind sectoriel structurel.

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

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 28 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant depuis au moins le 18/05. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Mutation sectorielle détectée à 17h00 UTC :** le signal macro bascule de `ROTATION_TO_DEFENSIVE` à `ROTATION_TO_CYCLICAL`, porté par la surperformance de XLK (+20.9% sur 20j, momentum 10.0/10) et le crossover haussier de XLE. Cependant, XLF (Financials) n'enregistre aucun momentum propre (0.0/10) et voit son RS 60j vs SPY creuser à −10.81% (vs −10.05% à 13h00). Le secteur financier reste donc en distribution relative structurelle, malgré le reclassement sectoriel artificiel.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-01T17:00:14 UTC*
