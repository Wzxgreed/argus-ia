# AXA — Mise à jour Quotidienne

> **Date :** 2026-06-08
> **Snapshot :** 2026-06-08T10:00:02 UTC
> **Type :** `_update.md` (post-pipeline 10h00 UTC)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-03_update.md` (snapshot 10h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 03/06 | État 08/06 | Changement |
|---------|-----------|-----------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 5 / 29 | **4 / 29** | **Amélioration** (SPCX résolu) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | −0.23% | **+1.45%** | **Amélioration +1.68 pp** |
| XLF return 60j | +2.28% | **+5.90%** | **Amélioration +3.62 pp** |
| XLF RS 20j vs SPY | −6.02% | **+0.64%** | **Amélioration +6.66 pp** |
| XLF RS 60j vs SPY | −10.99% | **−3.45%** | **Amélioration +7.54 pp** |
| XLF momentum score | 0.0/10 | **4.0/10** | **Amélioration significative** |
| Signal macro | NEUTRAL | **NEUTRAL** | **Stable** |
| Earnings FMP | J0 (2026-06-03) sans détails | **J0 (2026-06-08) sans détails** | **Glissement J+5** |

**Verdict :** Le blocage de sourcing AXA persiste (`error: true`, `reason: "No price history"`) mais le contexte sectoriel (XLF) s'est **nettlement amélioré** sur les 5 jours écoulés. Le secteur Financials est passé de sous-performance structurelle (−11% RS 60j) à un écart quasi neutre (−3.45% RS 60j) avec un retour à la surperformance à 20j (+0.64% vs SPY). Le momentum sectoriel a bondi de 0.0/10 à 4.0/10. AXA reste l'un des 4 tickers structurellement KO sur 29.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-08T10:00:02 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel (XLF) — amélioration significative vs close 03/06 :**
- Return 20j : **+1.45%** (vs SPY +0.82%) — **amélioration de +1.68 pp** vs le −0.23% du 03/06
- Return 60j : **+5.90%** (vs SPY +9.35%) — **amélioration de +3.62 pp** vs le +2.28% du 03/06
- RS 20j vs SPY : **+0.64%** — **amélioration de +6.66 pp** vs le −6.02% du 03/06
- RS 60j vs SPY : **−3.45%** — **amélioration de +7.54 pp** vs le −10.99% du 03/06
- Momentum score : **4.0/10** — **amélioration de +4.0 pts** vs le 0.0/10 du 03/06
- Rang sectoriel : 3e/11 (stable, par artefact de classement — XLK domine avec momentum 10.0/10)
- Crossover : aucun sur XLF (`crossover: null`)
- Signal macro : **`NEUTRAL`** (stable vs 03/06)

**Interprétation :** La mutation sectorielle est **clairement favorable**. Le secteur Financials a récupéré sa force relative vs le broad market sur 20j et réduit de plus de moitié son retard à 60j. Sans données AXA, il est impossible de déterminer si le titre a bénéficié de ce rally sectoriel. Le placeholder Momentum 5.0/10 est maintenu par convention, mais le contexte technique sectoriel justifierait désormais un relèvement si les données individuelles étaient disponibles.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-08) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-08"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données. Pattern récurrent d'un earnings glissant sans résolution depuis mi-mai. C'est le **16e snapshot consécutif** environ avec ce pattern J0 non résolu.

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
- Exposition FX : **25%** (export, primary currency USD — *classification générique par défaut*)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢

**Géopolitique** (`geo_risk_2026-05-17.json`) :
- Score géopolitique : **2/10** (faible exposition)
- Aucun événement géopolitique spécifique à AXA détecté.
- Flag : 🟢

**Social Sentiment** (`social_sentiment_2026-06-08.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 03/06 |
|-------|--------|-----------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** L'amélioration du contexte XLF est **la mutation la plus significative** depuis le dernier update. Le secteur Financials est sorti de sa distribution relative vs le broad market (RS 20j désormais positif +0.64%). Le momentum score à 4.0/10 (vs 0.0/10 précédemment) reflète ce revirement. Cependant, sans données AXA, le score Opportunité reste figé sur des placeholders et ne reflète pas cette amélioration sectorielle.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🟡 Thèse ATTENDRE confirmée — CONTEXTE SECTORIEL NETTEMENT AMÉLIORÉ, DONNÉES TOUJOURS MANQUANTES

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Mutation sectorielle significative à 10h00 UTC :** le secteur Financials (XLF) affiche une **amélioration notable** vs le snapshot du 03/06 :
- RS 20j vs SPY : −6.02% → **+0.64%** (passage en surperformance à court terme)
- RS 60j vs SPY : −10.99% → **−3.45%** (réduction de deux tiers du sous-performance à moyen terme)
- Return 20j : −0.23% → **+1.45%**
- Momentum score : 0.0/10 → **4.0/10**
- Signal macro `NEUTRAL` inchangé

Cette amélioration sectorielle est un **relief pour la thèse** si les données AXA étaient disponibles. En l'absence de prix, le rating reste **ATTENDRE** avec un score placeholder de 55.2/100.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-08) mais sans estimates ni détails — pattern persistant depuis mi-mai sans résolution. Le preview `AXA_2026-06-08_preview.md` reste un template vierge (prédictions non remplies).

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100, mais le contexte sectoriel est désormais **moins défavorable** qu'il ne l'était début juin.

---

*Desk Argus-IA — Snapshot 2026-06-08T10:00:02 UTC*
