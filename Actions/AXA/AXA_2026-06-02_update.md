# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-02
> **Snapshot :** 2026-06-02T21:00:14 UTC
> **Type :** `_update.md` (post-pipeline 21h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-02_update.md` (snapshot 17h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 17h00 | État 21h00 | Changement |
|---------|-----------|-----------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 5 / 29 | **5 / 29** | **Stable** (AXA, AST, QTBS, ASTSPACE, SPCX) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | −0.17% | **−0.23%** | 🔴 **Dégradation marginale (−6 bp)** |
| XLF return 60j | +2.34% | **+2.28%** | 🔴 **Dégradation marginale (−6 bp)** |
| XLF RS 20j vs SPY | −5.99% | **−6.02%** | 🔴 Dégradation relative (−3 bp) |
| XLF RS 60j vs SPY | −10.96% | **−10.99%** | 🔴 Dégradation relative (−3 bp) |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Signal macro | NEUTRAL | **NEUTRAL** | **Stable** |
| Earnings FMP | J0 (2026-06-02) sans détails | **J0 (2026-06-02) sans détails** | **Stable** |

**Verdict :** 26e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (`error: true`, `reason: "No price history"`). Le contexte sectoriel (XLF) affiche une **dégradation marginale** entre 17h00 et 21h00 UTC (−3 bp à −6 bp sur tous les horizons), sans impact matériel sur la thèse.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-02T21:00:14 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — dégradation marginale en séance US :**
- Return 20j : −0.23% (vs −0.17% à 17h00, vs SPY +5.79%)
- Return 60j : +2.28% (vs +2.34% à 17h00, vs SPY +13.28%)
- RS 20j vs SPY : −6.02% (vs −5.99% à 17h00, dégradation −3 bp)
- RS 60j vs SPY : −10.99% (vs −10.96% à 17h00, dégradation −3 bp)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 3e/11 (stable, par artefact de classement — XLK domine avec momentum 10.0/10)
- Crossover : aucun sur XLF (`crossover: null`)
- Signal macro : **`NEUTRAL`** (stable vs 17h00)

**Interprétation :** La dégradation marginale du XLF entre 17h00 et 21h00 (−6 bp en absolu, −3 bp en relatif) est d'amplitude négligeable et s'inscrit dans le bruit de marché. Le secteur Financials reste en sous-performance structurelle vs le broad market (SPY), avec un écart de force relative à 60j proche de −11%. Le momentum score à 0.0/10 confirme l'absence de dynamique propre. La neutralisation du signal macro (`NEUTRAL`) se maintient. Sans données AXA, l'évaluation de la force relative du titre vs son secteur reste impossible. Le placeholder Momentum 5.0/10 est maintenu par convention.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-06-02) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-02"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données. Pattern récurrent d'un earnings glissant sans résolution depuis le 20/05. C'est le **10e jour consécutif** de J0 FMP sans détails exploitables.

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

| Score | Valeur | Évolution vs snapshot 17h00 |
|-------|--------|-----------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** La dégradation marginale du XLF entre 17h00 et 21h00 (−3 bp à −6 bp) n'est pas significative au regard de la volatilité intrajournalière. Le secteur Financials reste en distribution relative vs le marché (RS 60j −10.99%). Le momentum score à 0.0/10 et le signal macro `NEUTRAL` sont inchangés. Sans données AXA, le score Opportunité reste figé sur des placeholders.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🔴 Thèse ATTENDRE confirmée — DONNÉES STRUCTURELLEMENT MANQUANTES, CONTEXTE SECTORIEL STABLE

**La thèse n'a pas changé.** AXA reste l'un des 5 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE, SPCX), avec un blocage de sourcing persistant depuis au moins le 18/05. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Mutation sectorielle à 21h00 UTC :** le secteur Financials (XLF) affiche une **dégradation marginale** par rapport au snapshot 17h00 : return 20j −0.23% (vs −0.17%), return 60j +2.28% (vs +2.34%), RS 20j −6.02% (vs −5.99%), RS 60j −10.99% (vs −10.96%). Ces variations (−3 bp à −6 bp) sont d'amplitude négligeable et ne modifient pas l'interprétation : Financials reste en sous-performance structurelle vs le broad market, avec un momentum propre à 0.0/10 et un signal macro `NEUTRAL` inchangé.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-02) mais sans estimates ni détails — **10e jour consécutif** de J0 non résolu.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-02T21:00:14 UTC*
