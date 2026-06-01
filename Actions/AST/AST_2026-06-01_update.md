# AST — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Type :** Update finale (snapshot 17:00 UTC)
> **Source :** data/latest.json (fetched_at 17:00:01 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-01_update.md` (snapshot 13:00 UTC)

| Élément | 13:00 UTC (01/06) | 17:00 UTC (01/06) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >22 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$113.41** | **$102.75** | **−9.40%** |
| Volume ASTS | 54.81M (2.08×) | 17.76M (0.67×) | **Effondrement −67.6%** |
| RSI ASTS | 69.79 | 60.09 | **Sortie zone haussière −9.7 pts** |
| ATR ASTS | 12.02 | 12.18 | **Expansion +1.3%** |
| MM 50j ASTS | 86.88 | 87.05 | Stable |
| Low intraday ASTS | 105.37 | **101.21** | **Cassure support $105–110** |
| High intraday ASTS | 115.50 | 111.28 | Compression range |
| Short interest ASTS | 17.60% | 17.60% | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus ASTS | +19.9% | **+8.7%** | **Compression −11.2 pts** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable — placeholder |
| Score ASTS (agent) | 38.5/100 (SURVEILLER) | **43.8/100 (SURVEILLER)** | **Upgrade +5.3 pts** |
| Score ajusté ASTS | 38.5/100 | **48.8/100** | Upgrade +10.3 pts |
| Earnings FMP AST | 2026-06-01 (days_until: 0) | 2026-06-01 (days_until: 0) | Placeholder glissant J=0 non résolu — 6j de glissement |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST | 0 | 0 | Stable |
| Signal sectoriel | ROTATION_TO_DEFENSIVE | **ROTATION_TO_CYCLICAL** | **Mutation majeure** |

**Constat :** Le snapshot 17:00 UTC enregistre une **mutation technique majeure** sur le proxy ASTS : correction de **−9.40%** supplémentaire en séance, portant le repli total depuis le close 27/05 ($129.335) à **−20.55%**. Le volume s'est effondré à **0.67× moyenne 20j**, signalant un désengagement des vendeurs et une absence de relance acheteuse. Le support $105–110 a été **cassé** avec un low à **$101.21**. Le RSI est sorti de la zone haussière à **60.09**. Le signal sectoriel est basculé en **ROTATION_TO_CYCLICAL** (XLK top1, momentum 10.0) — paradoxalement favorable au secteur Technology alors que ASTS sous-performe.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 17:00 UTC (01/06) | Valeur précédente (13:00 UTC) | Δ |
|-----------|-------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 17:00 UTC (01/06) | Valeur précédente (13:00 UTC) | Δ |
|-----------|-------------------------|-------------------------------|---|
| Cours close | **$102.75** | $113.41 | **−9.40%** |
| Open | 108.67 | 113.46 | Gap baissier −4.2% |
| High intraday | 111.28 | 115.50 | Compression −3.7% |
| Low intraday | **101.21** | 105.37 | **Cassure support −3.9%** |
| Volume | **17.76M** | 54.81M | **Effondrement −67.6%** |
| Volume relatif | **0.67× moy. 20j** | 2.08× | Retour sous moyenne |
| RSI 14j | **60.09** | 69.79 | **Sortie zone haussière −9.7 pts** |
| ATR 14j | **12.18** | 12.02 | Expansion +1.3% |
| MM 50j | **87.05** | 86.88 | +0.2% |
| Distance MM50j | **+18.0%** | +30.5% | Compression |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−23.2%** | −15.3% | Éloignement |

**Verdict timing ASTS (proxy) :** 🔴 **CORRECTION TECHNIQUE AGGRAVÉE — SUPPORT CASSÉ** — Le cours a ouvert en gap baissier à $108.67 (−4.2% vs close 13h) et a poursuivi sa chute jusqu'à **$101.21**, cassant le support immédiat $105–110 identifié ce matin. Le close à $102.75 confirme la rupture. Le volume en effondrement (**0.67× moyenne 20j**) est ambivalent : absence de panique massive (pas de distribution volume ×2), mais aussi absence de relance acheteuse sur les niveaux cassés. Le RSI à **60.09** sort de la zone haussière (>60) et s'approche de la neutralité — configuration moins surchauffée mais sans momentum haussier. La prochaine zone de support structurel se situe à **$95–100** (confluence avec le niveau psychologique $100 et l'expansion ATR). Une cassure sous **$100** ouvrirait la voie vers la MM50j à **$87.05**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 17:00 UTC (01/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 17:00 UTC (01/06) | Valeur précédente (13:00 UTC) | Δ |
|---------|-------------------------|-------------------------------|---|
| Market cap | **$39.89B** | $44.02B | **−9.4%** |
| Forward P/E | **−345.91** | −381.68 | Amélioration (moins négatif) |
| EV/Revenue | **405.3×** | 405.3× | Stable |
| EV/EBITDA | **−108.80** | −108.80 | Stable |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus | **+8.7%** | +19.9% | **Compression −11.2 pts** |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). La compression du premium consensus de **+19.9% à +8.7%** réduit le risque de correction par rapport aux attentes sell-side. Le forward P/E s'améliore mécaniquement (−345.91 vs −381.68) du fait de la baisse de cours, sans changement fondamental. La couverture analyste (12 analysts) et le PT moyen ($94.54) sont inchangés.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-06-01.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :** max pain **120.0** (réapparu et stable vs matin), put/call ratio **0.92** (hausse vs données corrompues précédentes), call OI **52.2%**. Le max pain à $120 est désormais **+16.8% au-dessus du cours**, créant une pression gamma potentielle vers le haut si le cours se stabilise.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $102.75 = **+8.7% au-dessus du consensus** (vs +19.9% à 13h)
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant, geo, accounting, events
- **FX exposure AST/ASTS :** exposition 25% (placeholder), direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-01** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 26/05, 6 jours de glissement), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 70`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **ROTATION_TO_CYCLICAL** détecté (mutation depuis ROTATION_TO_DEFENSIVE à 13h). Technology (XLK) reste top1 sector avec momentum score 10.0. XLE en bullish crossover. **Paradoxe sectoriel :** ASTS (Technology) sous-performe massivement (−9.4%) alors que son secteur domine le momentum — divergence négative interne au ticker, non au secteur.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 17:00 UTC (01/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35% | [NON FONDÉ] — aucun catalyseur vérifiable |
| Valorisation | 5.0/10 (placeholder) | 40% | [NON FONDÉ] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25% | [NON FONDÉ] — pas de cours, pas de momentum |
| **Score Opportunité** | **5.5/10** | — | Placeholder — **non utilisable pour décision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |
| **Score Global Ajusté** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)
**Timing :** Neutre
**Horizon :** —

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, à titre indicatif uniquement)

| Axe | Score 17:00 UTC (01/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais non vérifiable à court terme |
| Valorisation | 4.0/10 | 40% | EV/Revenue 405×, forward P/E −345.91, premium consensus compressé à +8.7% |
| Momentum | 5.5/10 | 25% | Correction −9.40% en séance, RSI 60.09 sorti de surchauffe, support cassé |
| **Score Opportunité** | **4.4/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **43.8/100** | — | SURVEILLER |
| **Score Global Ajusté** | **48.8/100** | — | **SURVEILLER** |

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Neutre
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. Le score **SURVEILLER (48.8/100)** reflète la **compression du premium consensus** (+8.7% vs +19.9% à 13h, +40.2% fin mai) et la **sortie du RSI de la zone >60**, mais la configuration reste risquée (cassure du support $105–110, volume faible, absence de relance). L'upgrade de +10.3 pts sur le score ajusté est entièrement dû à la mechanical compression de la valorisation, pas à une amélioration fondamentale.

---

## 6. Niveaux SL / TP / Ratio R/R

### AST (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy, à titre indicatif uniquement)

| Niveau | Calcul | Valeur |
|--------|--------|--------|
| Prix entrée | Cours close | $102.75 |
| Stop-loss | $102.75 − 2×12.18 | **$78.39** |
| Take-profit | $102.75 + 3×12.18 | **$139.29** |
| Ratio R/R | (139.29−102.75)/(102.75−78.39) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL à $78.39 et le TP à $139.29 sont révisés à la baisse** du fait de l'expansion de l'ATR et de la chute de cours. Le support $105–110 est désormais **cassé** ; le niveau $101.21 (low intraday) est le support immédiat. Une cassure sous **$100** ouvrirait la voie vers la MM50j à **$87.05**. Le max pain options à **$120** reste un aimant gamma potentiel si stabilisation.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — CORRECTION ASTS AGGRAVÉE À 17:00 UTC**

AST n'est pas évaluable en l'état. La situation pour ASTS (proxy) s'est **détériorée techniquement** entre le snapshot 13:00 UTC et le snapshot 17:00 UTC du 01/06 :

1. **Anomalie structurelle confirmée :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). ASTS a corrigé de **−9.40%** supplémentaires en séance, portant le repli total depuis le 27/05 à **−20.55%**.
2. **Cassure technique confirmée :** le support $105–110 a été rompu avec un low à **$101.21**. Le close à $102.75 confirme la rupture. Le volume en effondrement (**0.67× moyenne 20j**) indique un désengagement des vendeurs mais aussi une absence totale de relance acheteuse sur les niveaux cassés.
3. **RSI en sortie de zone haussière :** le RSI est passé de **69.79 à 60.09**, sortant de la zone haussière et s'approchant de la neutralité. C'est mécaniquement plus sain, mais témoigne d'un momentum haussier éteint.
4. **Paradoxe sectoriel :** le signal sectoriel est basculé en **ROTATION_TO_CYCLICAL** avec Technology (XLK) top1 (momentum 10.0). ASTS sous-performe massivement son secteur — divergence interne négative, probablement liée à un factor spécifique (short covering exhausted, earnings incertitude, ou rotation interne tech vers les grandes caps).
5. **Premium consensus compressé :** le passage de **+19.9% à +8.7%** au-dessus du consensus réduit le risque de correction mécanique, mais ne constitue pas un catalyseur haussier. Le sell-side n'a pas révisé son PT ($94.54, 12 analysts).
6. **Options :** le max pain à **$120** est réapparu et stable, désormais **+16.8% au-dessus du cours** vs +5.8% à 13h — créant une pression gamma haussière potentielle si le cours se stabilise. Le put/call ratio à **0.92** et le call OI à **52.2%** suggèrent un léger biais haussier des détenteurs d'options.
7. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-01** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **26/05** (6 jours de décalage non résolu).
8. **Score agent ASTS révisé à la hausse :** le score ajusté passe de **38.5 à 48.8/100** (upgrade +10.3 pts), entièrement mécanique (compression valorisation + RSI plus bas), sans changement fondamental. L'action reste **SURVEILLER**.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel test de la zone **$95–100** (support psychologique + confluence ATR). Une cassure sous **$100** ouvrirait la voie vers la MM50j à **$87.05**. Un rebond au-dessus de **$105** (ancien support cassé, désormais résistance) serait le premier signe de stabilisation. Le max pain options à **$120** reste un aimant gamma si le titre trouve un plancher.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 17:00 UTC, fetched_at 2026-06-01T17:00:01.371409+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
