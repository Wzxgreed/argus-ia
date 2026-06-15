# AXA — Mise à jour Quotidienne (snapshot 10h00 UTC)

> **Date :** 2026-06-15
> **Snapshot :** 2026-06-15T10:00:02 UTC
> **Type :** `_update.md`
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-10_update.md` (snapshot 10h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 10/06 10h | État 15/06 10h | Changement |
|---------|---------------|----------------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable — blocage structurel** |
| Erreur Yahoo | `No price history` | `No price history` | **Confirmé stable** |
| Tickers KO pipeline | 4 / 29 | 4 / 29 | **Stable (AXA, AST, QTBS, ASTSPACE)** |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable (placeholder)** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| Sector rotation XLF (RS 20j) | `NaN` (anomalie 10/06) | **+4.85%** | **✅ Récupération données — amélioration +2.04 pp vs 09/06** |
| Sector rotation XLF (momentum) | `10.0` (placeholder) | **6.73/10** | **✅ Récupération — amélioration +1.54 pt vs 09/06** |
| Sector rotation XLF (rang) | `UNKNOWN` | **2e/11** | **✅ Progression +1 place vs 09/06** |
| Signal macro | `UNKNOWN` (anomalie) | **`UNKNOWN`** | **Stable** |
| Earnings FMP | J0 (2026-06-10) sans détails | **J0 (2026-06-15) sans détails** | **Pattern glissant +5j** |

**Verdict :** Données AXA toujours indisponibles. **Récupération du fichier sectoriel** : `data/sector_rotation_2026-06-15.json` est désormais valide et montre une **amélioration continue** du contexte Financials (XLF) depuis le 09/06. Aucune mutation fondamentale ou technique sur AXA proprement dit — l'absence de données persiste.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-15T10:00:02 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel XLF — récupération confirmée :**
- Le fichier `data/sector_rotation_2026-06-15.json` est cette fois **valide** (vs anomalie NaN du 10/06).
- XLF : return 20j **+4.00%** (vs +2.50% le 09/06), return 60j **+9.48%** (vs +7.85% le 09/06).
- RS 20j vs SPY : **+4.85%** (vs +2.81% le 09/06) → **amélioration de +2.04 pp**.
- RS 60j vs SPY : **−2.97%** (vs −3.74% le 09/06) → **amélioration de +0.77 pp**.
- Momentum score : **6.73/10** (vs 5.19/10 le 09/06) → **+1.54 pt**.
- Rang sectoriel : **2e/11** (vs 3e/11 le 09/06) → **progression d'une place**.
- Crossover : `null` — aucun signal de crossover détecté.
- Signal macro : **`UNKNOWN`** (stable depuis le 02/06).

**Conséquence pour l'analyse :** en l'absence de données AXA, le contexte sectoriel reste le seul élément technique observable. L'amélioration du XLF est un vent de queue indirect pour le secteur assurance, mais ne permet pas de qualifier la dynamique propre d'AXA.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-15) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-15"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- Le preview `AXA_2026-06-15_preview.md` est un template vierge (prédictions non remplies) — **pattern persistant sans résolution**.
- **Impact sur la thèse :** impossible à évaluer. Le pipeline ne récupère ni le consensus ni les résultats effectifs pour ce ticker.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` **absent** — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-15.json`) | **Aucune** | AXA non listé ou vide — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-15.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-15.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-06-15.json`) :
- Exposition FX : **25%** (export, primary currency USD — classification générique par défaut)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢 — stable

**Géopolitique** (`geo_risk_2026-05-17.json` — dernier fichier disponible) :
- AXA non listé dans le rapport géopolitique.
- Aucun événement géopolitique spécifique détecté.
- Flag : 🟢 — stable

**Social Sentiment** (`social_sentiment_2026-06-15.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 10/06 |
|-------|--------|-----------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** Le contexte Financials (XLF) s'est **amélioré** entre le 09/06 et le 15/06 : RS 20j +4.85% (vs +2.81%), momentum 6.73/10 (vs 5.19/10), rang 2e/11 (vs 3e/11). Cependant, en l'absence de données propres à AXA, cet amélioration sectorielle ne modifie pas le scoring individuel du ticker.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🟡 Thèse ATTENDRE confirmée — DONNÉES AXA TOUJOURS MANQUANTES, CONTEXTE SECTORIEL EN AMÉLIORATION

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Récupération des données sectorielles.** Le fichier `data/sector_rotation_2026-06-15.json` est valide et montre une **amélioration continue** du secteur Financials depuis le 09/06 : RS 20j +4.85% (+2.04 pp), momentum 6.73/10 (+1.54 pt), rang 2e/11 (+1 place). Ce vent de queue sectoriel est favorable mais indirect — il ne compense pas l'absence totale de données sur AXA.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-15) mais sans estimates ni détails — 14e occurrence consécutive sans résolution. Le preview `AXA_2026-06-15_preview.md` reste un template vierge.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100. L'amélioration sectorielle du XLF est notée mais n'altère pas la recommandation en l'absence de données propres.

---

*Desk Argus-IA — Snapshot 2026-06-15T10:00:02 UTC*
