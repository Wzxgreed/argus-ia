# AXA — Mise à jour Quotidienne (snapshot 10:00 UTC)

> **Date :** 2026-06-09
> **Snapshot :** 2026-06-09T10:00:20 UTC
> **Type :** `_update.md` (snapshot 10h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-08_update_17h.md` (snapshot 17h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 08/06 17h | État 09/06 10h | Changement |
|---------|---------------|----------------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Erreur Yahoo | `No price history` | `No price history` | **Confirmé stable** |
| Tickers KO pipeline | 4 / 29 | 4 / 29 | **Stable** |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | +1.76% | **+1.42%** | **−0.34 pt** |
| XLF return 60j | +7.33% | **+6.98%** | **−0.35 pt** |
| XLF RS 20j vs SPY | +1.20% | **+1.21%** | **Stable (+0.01 pt)** |
| XLF RS 60j vs SPY | −4.34% | **−4.31%** | **Stable (+0.03 pt)** |
| XLF momentum score | 3.99/10 | **4.0/10** | **Stable** |
| Rang sectoriel XLF | 3e/11 | **4e/11** | **Recul d'un rang** |
| Signal macro | NEUTRAL | **NEUTRAL** | **Stable** |
| Earnings FMP | J0 (2026-06-08) sans détails | **J0 (2026-06-09) sans détails** | **Pattern persistant** |

**Verdict :** Stabilité globale confirmée vs close 08/06. AXA reste l'un des 4 tickers structurellement KO sur 29. Légère dégradation du contexte sectoriel XLF (return 20j/60j −0.34/−0.35 pt, recul au rang 4e/11) sans impact sur le scoring.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-09T10:00:20 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — légère dégradation vs close 08/06 :**
- Return 20j : **+1.42%** (vs SPY +0.22%) — dégradation −0.34 pt vs 08/06 17h
- Return 60j : **+6.98%** (vs SPY +11.29%) — dégradation −0.35 pt
- RS 20j vs SPY : **+1.21%** — stable (+0.01 pt)
- RS 60j vs SPY : **−4.31%** — amélioration marginale (+0.03 pt)
- Momentum score : **4.0/10** — stable
- Rang sectoriel : **4e/11** (was 3e/11) — recul d'un rang, dépassé par XLE
- Crossover : aucun sur XLF — stable
- Signal macro : **`NEUTRAL`** — inchangé

**Interprétation :** Le secteur Financials affiche un léger reflux des returns 20j et 60j par rapport au close d'hier, sans mutation de tendance. La force relative reste stable. Le recul au rang 4e/11 reflète une relative sous-performance vs Energy (XLE) qui a gagné du momentum. Sans données AXA, le titre n'a pas bénéficié (ni subi) de mutation de marché intrajournalière. Le placeholder Momentum 5.0/10 est maintenu par convention.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-09) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-09"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- Le preview `AXA_2026-06-09_preview.md` reste un template vierge (prédictions non remplies) — **12e jour consécutif de pattern J0 sans résolution**.
- **Impact sur la thèse :** impossible à évaluer. Le pipeline ne récupère ni le consensus ni les résultats effectifs pour ce ticker.

**Accounting Risk :** Fichier `data/accounting_risk_*.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-09.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-09.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-09.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-06-09.json`) :
- Exposition FX : **25%** (export, primary currency USD — classification générique par défaut)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢 — stable

**Géopolitique** (`geo_2026-06-09.json`) :
- Score géopolitique : **2/10** (faible exposition)
- Aucun événement géopolitique spécifique à AXA détecté.
- Flag : 🟢 — stable

**Social Sentiment** (`social_sentiment_2026-06-09.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs close 08/06 |
|-------|--------|--------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** Le contexte XLF est légèrement dégradé vs le close d'hier (return 20j −0.34 pt, return 60j −0.35 pt, recul au rang 4e/11). Cependant, la force relative reste stable et le signal macro `NEUTRAL` est inchangé. Le secteur Financials conserve un momentum de 4.0/10.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🟡 Thèse ATTENDRE confirmée — STABILITÉ GLOBALE VS CLOSE 08/06, DONNÉES TOUJOURS MANQUANTES

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Aucune mutation détectée entre le close 08/06 et le snapshot 10h00 UTC du 09/06.** Le pipeline a produit un snapshot 10h00 UTC avec 25 tickers OK sur 29 (identique à hier). Le contexte sectoriel XLF affiche une légère dégradation des returns 20j (+1.42% vs +1.76%) et 60j (+6.98% vs +7.33%), avec un recul au rang 4e/11 (was 3e). La force relative reste stable (RS 20j +1.21%, RS 60j −4.31%). Le signal macro `NEUTRAL` est inchangé.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-09) mais sans estimates ni détails — **12e occurrence consécutive** du pattern sans résolution. Le preview `AXA_2026-06-09_preview.md` reste un template vierge.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-09T10:00:20 UTC*
