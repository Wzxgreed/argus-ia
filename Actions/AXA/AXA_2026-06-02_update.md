# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-02
> **Snapshot :** 2026-06-02T13:00:01 UTC
> **Type :** `_update.md` (post-pipeline 13h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-02_update.md` (snapshot 10h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 10h00 | État 13h00 | Changement |
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
| XLF return 20j | −0.94% | **−0.94%** | **Stable** |
| XLF return 60j | +0.91% | **+0.91%** | **Stable** |
| XLF RS 20j vs SPY | −6.20% | **−6.20%** | **Stable** |
| XLF RS 60j vs SPY | −10.73% | **−10.73%** | **Stable** |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Signal macro | ROTATION_TO_CYCLICAL | **ROTATION_TO_CYCLICAL** | **Stable** |
| Earnings FMP | J0 (2026-06-02) sans détails | **J0 (2026-06-02) sans détails** | **Stable** |

**Verdict :** 24e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (`error: true`, `reason: "No price history"`). Aucune mutation inter-snapshot détectée entre 10h00 et 13h00 UTC. Le secteur Financials (XLF) affiche une **stabilité totale** sur toutes les fenêtres. Le signal macro reste `ROTATION_TO_CYCLICAL`, porté par XLK (return 20j +20.94%, momentum 10.0/10) et le crossover haussier de XLE.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-02T13:00:01 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — stabilité totale vs snapshot 10h00 :**
- Return 20j : −0.94% (stable vs 10h00, vs SPY +5.26%)
- Return 60j : +0.91% (stable vs 10h00, vs SPY +11.64%)
- RS 20j vs SPY : −6.20% (stable)
- RS 60j vs SPY : −10.73% (stable)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 3e/11 (stable, par artefact de classement)
- Crossover : aucun sur XLF (BULLISH_CROSSOVER sur XLE uniquement)
- Signal macro : `ROTATION_TO_CYCLICAL` (stable)

**Interprétation :** La stabilité totale du XLF confirme l'absence de catalyseur sectoriel pour le secteur Financials. Sans données AXA, l'évaluation de la force relative du titre vs son secteur reste impossible. Le placeholder Momentum 5.0/10 est maintenu mais mériterait un ajustement à la baisse si les données étaient disponibles, compte tenu du headwind sectoriel persistant (−10.73% à 60j vs SPY).

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-06-02) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-02"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données. Pattern récurrent d'un earnings glissant sans résolution depuis le 20/05. C'est le 8e jour consécutif de J0 FMP sans détails exploitables.

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

**Note sectorielle :** La stabilité totale du XLF (aucune mutation vs snapshot 10h00) confirme l'absence de catalyseur sectoriel. Le secteur Financials reste en distribution relative structurelle vs le marché (−10.73% sur 60j). Sans données AXA, le score Opportunité reste figé sur des placeholders. Le signal macro `ROTATION_TO_CYCLICAL` est stable.

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

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant depuis au moins le 18/05. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Stabilité sectorielle à 13h00 UTC :** le signal macro reste `ROTATION_TO_CYCLICAL`, porté par la surperformance de XLK (+20.94% sur 20j, momentum 10.0/10) et le crossover haussier de XLE. XLF (Financials) affiche une **stabilité totale** vs snapshot 10h00 (return 20j −0.94%, return 60j +0.91%, RS 20j −6.20%, RS 60j −10.73%, momentum 0.0/10). Le secteur financier reste classé 3e/11 par artefact de classement, sans momentum propre et en distribution relative structurelle vs le marché.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-02) mais sans estimates ni détails — 8e jour consécutif de J0 non résolu.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-02T13:00:01 UTC*
