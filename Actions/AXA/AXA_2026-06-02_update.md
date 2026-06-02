# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-02
> **Snapshot :** 2026-06-02T17:00:16 UTC
> **Type :** `_update.md` (post-pipeline 17h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-02_update.md` (snapshot 13h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 13h00 | État 17h00 | Changement |
|---------|-----------|-----------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 4 / 29 | **4 / 29** | **Stable** (AXA, AST, QTBS, ASTSPACE) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | −0.94% | **−0.17%** | 🟢 **Amélioration absolue (+77 bp)** |
| XLF return 60j | +0.91% | **+2.34%** | 🟢 **Amélioration absolue (+143 bp)** |
| XLF RS 20j vs SPY | −6.20% | **−5.99%** | 🟢 Légère amélioration relative (+21 bp) |
| XLF RS 60j vs SPY | −10.73% | **−10.96%** | 🔴 Dégradation relative (−23 bp) |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Signal macro | ROTATION_TO_CYCLICAL | **NEUTRAL** | 🔴 **Neutralisation du signal** |
| Earnings FMP | J0 (2026-06-02) sans détails | **J0 (2026-06-02) sans détails** | **Stable** |

**Verdict :** 25e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (`error: true`, `reason: "No price history"`). Cependant, **mutation significative du contexte sectoriel et macro détectée** entre 13h00 et 17h00 UTC :
- Le signal macro a été **neutralisé** (`ROTATION_TO_CYCLICAL` → `NEUTRAL`), indiquant un affaiblissement de la dynamique de rotation sectorielle observée depuis le 1er juin.
- Le secteur Financials (XLF) affiche une **amélioration absolue marquée** sur 20j (+77 bp) et 60j (+143 bp), probablement portée par le rebond du marché (SPY +5.81% sur 20j, +13.30% sur 60j).
- En termes relatifs, le RS 20j s'améliore marginalement (+21 bp) mais le RS 60j se creuse légèrement (−23 bp), confirmant que le secteur peine à suivre l'accélération du broad market.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-02T17:00:16 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — amélioration absolue mais sous-performance relative persistante :**
- Return 20j : −0.17% (vs −0.94% à 13h00, vs SPY +5.81%)
- Return 60j : +2.34% (vs +0.91% à 13h00, vs SPY +13.30%)
- RS 20j vs SPY : −5.99% (vs −6.20% à 13h00, amélioration +21 bp)
- RS 60j vs SPY : −10.96% (vs −10.73% à 13h00, dégradation −23 bp)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 3e/11 (stable, par artefact de classement — XLK domine avec momentum 10.0/10)
- Crossover : aucun sur XLF (`crossover: null`)
- Signal macro : **`NEUTRAL`** (vs `ROTATION_TO_CYCLICAL` à 13h00) — neutralisation de la rotation sectorielle

**Interprétation :** L'amélioration absolue du XLF sur 20j et 60j est une évolution positive pour le secteur Financials, mais elle reste **entièrement dictée par le rebond du broad market** (SPY a gagné +77 bp à 20j et +166 bp à 60j entre les deux snapshots). Le secteur ne surperforme pas — il suit avec un décalage. Le momentum score reste à 0.0/10, confirmant l'absence de dynamique propre. La neutralisation du signal macro (`NEUTRAL`) retire le headwind explicite de "rotation hors Financials" mais n'établit pas de vent favorable. Sans données AXA, l'évaluation de la force relative du titre vs son secteur reste impossible. Le placeholder Momentum 5.0/10 est maintenu mais mérite un ajustement à la baisse compte tenu du RS 60j dégradé (−10.96%).

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-06-02) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-02"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données. Pattern récurrent d'un earnings glissant sans résolution depuis le 20/05. C'est le 9e jour consécutif de J0 FMP sans détails exploitables.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-02.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-02.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-02.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-06-02.json`) :
- Exposition FX : **25%** (export, primary currency USD — *classification générique par défaut*)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢

**Géopolitique** (`geo_risk_2026-05-17.json`) :
- Score géopolitique : **2/10** (faible exposition)
- Aucun événement géopolitique spécifique à AXA détecté.
- Flag : 🟢

**Social Sentiment** (`social_sentiment_2026-06-02.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 13h00 |
|-------|--------|-----------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** La mutation la plus significative entre 13h00 et 17h00 est la **neutralisation du signal macro** (`ROTATION_TO_CYCLICAL` → `NEUTRAL`) et l'amélioration absolue du XLF (+77 bp à 20j, +143 bp à 60j). Cependant :
1. Le momentum sectoriel reste à 0.0/10 — pas de dynamique propre.
2. Le RS 60j vs SPY se dégrade (−10.96% vs −10.73%), confirmant la sous-performance structurelle.
3. Sans données AXA, le score Opportunité reste figé sur des placeholders. Le Momentum 5.0/10 est maintenu par convention mais pourrait mériter un ajustement à ~4.5/10 compte tenu du headwind sectoriel persistant.
4. La neutralisation du signal macro est marginalement positive (retrait d'un malus explicite de rotation hors Financials) mais ne constitue pas un catalyseur suffisant pour modifier la thèse.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🔴 Thèse ATTENDRE confirmée — DONNÉES STRUCTURELLEMENT MANQUANTES, CONTEXTE SECTORIEL LÉGÈREMENT AMÉLIORÉ

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant depuis au moins le 18/05. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Mutation sectorielle à 17h00 UTC :** le signal macro a été **neutralisé** (`ROTATION_TO_CYCLICAL` → `NEUTRAL`), et le secteur Financials (XLF) affiche une **amélioration absolue** sur 20j (−0.17% vs −0.94% à 13h00) et 60j (+2.34% vs +0.91%). Cette amélioration est portée par le rebond du broad market (SPY +5.81% / +13.30%) et non par une dynamique propre du secteur — le momentum score reste à 0.0/10. En termes relatifs, le RS 60j vs SPY se creuse légèrement (−10.96% vs −10.73%), confirmant que Financials reste en distribution structurelle vs le marché. La neutralisation du signal macro est une évolution favorable mais insuffisante pour modifier la thèse.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-02) mais sans estimates ni détails — 9e jour consécutif de J0 non résolu.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-02T17:00:16 UTC*
