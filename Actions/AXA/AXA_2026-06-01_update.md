# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Snapshot :** 2026-06-01T21:00:20 UTC
> **Type :** `_update.md` (post-pipeline 21h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-01_update.md` (snapshot 17h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 17h00 | État 21h00 | Changement |
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
| XLF return 20j | −1.13% | **−0.94%** | 🟢 Légère amélioration (+19 bp) |
| XLF return 60j | +0.72% | **+0.91%** | 🟢 Légère amélioration (+19 bp) |
| XLF RS 20j vs SPY | −6.28% | **−6.20%** | 🟢 Légère amélioration (+8 bp) |
| XLF RS 60j vs SPY | −10.81% | **−10.73%** | 🟢 Légère amélioration (+8 bp) |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Signal macro | ROTATION_TO_CYCLICAL | **ROTATION_TO_CYCLICAL** | **Stable** |
| Earnings FMP | J0 (2026-06-01) sans détails | **J0 (2026-06-01) sans détails** | **Stable** |

**Verdict :** 22e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (`error: true`, `reason: "No price history"`). Aucune mutation inter-snapshot détectée entre 17h00 et 21h00 UTC. Le secteur Financials (XLF) enregistre une **légère amélioration marginale** sur toutes les fenêtres (+8 à +19 bp), sans changer de signal ni de rang sectoriel (3e/11). Le signal macro reste `ROTATION_TO_CYCLICAL`, porté par XLK (return 20j +20.94%, momentum 10.0/10) et le crossover haussier de XLE.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-01T21:00:20 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — stabilité avec légère amélioration marginale :**
- Return 20j : −0.94% (vs −1.13% à 17h00, vs SPY +5.26%)
- Return 60j : +0.91% (vs +0.72% à 17h00, vs SPY +11.64%)
- RS 20j vs SPY : −6.20% (vs −6.28% à 17h00)
- RS 60j vs SPY : −10.73% (vs −10.81% à 17h00)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 3e/11 (stable, par artefact de classement)
- Crossover : aucun sur XLF (BULLISH_CROSSOVER sur XLE uniquement)
- Signal macro : `ROTATION_TO_CYCLICAL` (stable vs 17h00)

**Interprétation :** L'amélioration marginale du XLF (+8 bp à 60j, +19 bp à 20j) est trop faible pour modifier la thèse. Le secteur Financials reste en distribution relative structurelle vs le marché (−10.73% sur 60j). Sans données AXA, l'évaluation de la force relative du titre vs son secteur reste impossible. Le placeholder Momentum 5.0/10 est maintenu mais mériterait un ajustement à la baisse si les données étaient disponibles, compte tenu du headwind sectoriel persistant.

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
- Exposition FX : **25%** (export, primary currency USD — *classification générique par défaut*)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned

**Géopolitique** (`geo_2026-06-01.json`) :
- Score géopolitique : **2/10** (faible exposition)
- Aucun événement géopolitique spécifique à AXA détecté.
- Flag : 🟢

**Social Sentiment** (`social_sentiment_2026-06-01.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 17h00 |
|-------|--------|------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** L'amélioration marginale du XLF (+8 bp à 60j, +19 bp à 20j) ne modifie pas le score Opportunité d'AXA car (i) aucune donnée de prix n'est disponible pour recalculer le Momentum, (ii) XLF n'affiche aucun momentum propre (0.0/10), et (iii) le headwind sectoriel structurel reste intact (−10.73% sur 60j vs SPY). Le signal macro `ROTATION_TO_CYCLICAL` est stable.

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

**Stabilité sectorielle à 21h00 UTC :** le signal macro reste `ROTATION_TO_CYCLICAL`, porté par la surperformance de XLK (+20.94% sur 20j, momentum 10.0/10) et le crossover haussier de XLE. XLF (Financials) enregistre une légère amélioration marginale (+8 bp RS 60j, +19 bp return 20j) mais reste sans momentum propre (0.0/10) et en distribution relative structurelle vs le marché (−10.73% à 60j). Le secteur financier reste classé 3e/11 par artefact de classement.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-01T21:00:20 UTC*
