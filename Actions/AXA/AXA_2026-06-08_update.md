# AXA — Mise à jour Quotidienne (snapshot 13:00 UTC)

> **Date :** 2026-06-08
> **Snapshot :** 2026-06-08T13:00:15 UTC
> **Type :** `_update.md` (snapshot 13h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-08_update.md` (snapshot 10h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 10h | État 13h | Changement |
|---------|----------|----------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Erreur Yahoo | `No price history` | `No price history` | **Confirmé stable** |
| Tickers KO pipeline | 4 / 29 | 4 / 29 | **Stable** |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | +1.45% | **+1.45%** | **Stable** |
| XLF return 60j | +5.90% | **+5.90%** | **Stable** |
| XLF RS 20j vs SPY | +0.64% | **+0.64%** | **Stable** |
| XLF RS 60j vs SPY | −3.45% | **−3.45%** | **Stable** |
| XLF momentum score | 4.0/10 | **4.0/10** | **Stable** |
| Signal macro | NEUTRAL | **NEUTRAL** | **Stable** |
| Earnings FMP | J0 (2026-06-08) sans détails | **J0 (2026-06-08) sans détails** | **Stable** |

**Verdict :** Stabilité totale confirmée entre les snapshots 10h00 et 13h00 UTC. AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE). Le blocage de sourcing persiste sans mutation.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-08T13:00:15 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — stabilité totale vs snapshot 10h :**
- Return 20j : **+1.45%** (vs SPY +0.82%) — strictement identique au snapshot 10h
- Return 60j : **+5.90%** (vs SPY +9.35%) — strictement identique
- RS 20j vs SPY : **+0.64%** — strictement identique
- RS 60j vs SPY : **−3.45%** — strictement identique
- Momentum score : **4.0/10** — strictement identique
- Rang sectoriel : 3e/11 — stable
- Crossover : aucun sur XLF — stable
- Signal macro : **`NEUTRAL`** — inchangé

**Interprétation :** Le contexte technique sectoriel est figé entre les deux snapshots. Sans données AXA, le titre n'a pas bénéficié (ni subi) de mutation de marché intrajournalière. Le placeholder Momentum 5.0/10 est maintenu par convention.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-08) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-08"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer. Pattern persistant depuis mi-mai sans résolution.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-08.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-08.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-08.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-06-08.json`) :
- Exposition FX : **25%** (export, primary currency USD — classification générique par défaut)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢 — stable

**Géopolitique** (`geo_2026-06-08.json`) :
- Score géopolitique : **2/10** (faible exposition)
- Aucun événement géopolitique spécifique à AXA détecté.
- Flag : 🟢 — stable

**Social Sentiment** (`social_sentiment_2026-06-08.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 10h |
|-------|--------|---------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** Le contexte XLF est strictement inchangé entre 10h et 13h. Le secteur Financials conserve sa position 3e/11 avec un momentum de 4.0/10.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🟡 Thèse ATTENDRE confirmée — STABILITÉ TOTALE VS SNAPSHOT 10H, DONNÉES TOUJOURS MANQUANTES

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Aucune mutation détectée entre 10h00 et 13h00 UTC.** Le pipeline a produit un snapshot 13h00 UTC avec 25 tickers OK sur 29 (identique à 10h). Le contexte sectoriel XLF est strictement figé : RS 20j +0.64%, RS 60j −3.45%, return 20j +1.45%, momentum 4.0/10. Le signal macro `NEUTRAL` est inchangé.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-08) mais sans estimates ni détails — pattern persistant depuis mi-mai sans résolution. Le preview `AXA_2026-06-08_preview.md` reste un template vierge (prédictions non remplies).

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-08T13:00:15 UTC*
