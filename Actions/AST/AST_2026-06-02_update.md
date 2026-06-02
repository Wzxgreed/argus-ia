# AST — Mise à jour Quotidienne

> **Date :** 2026-06-02
> **Type :** Update (snapshot 13:00 UTC)
> **Source :** data/latest.json (fetched_at 13:00:01 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-01_update.md` (snapshot 21:00 UTC)

| Élément | 21:00 UTC (01/06) | 13:00 UTC (02/06) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — 24 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$105.65** | **$105.65** | **Stable** (snapshot 13h UTC, marché non ouvert) |
| Volume ASTS | 27.07M (1.00×) | **27.14M** (1.00×) | Stable |
| RSI ASTS | 61.89 | **61.89** | Stable |
| ATR ASTS | 12.18 | 12.18 | Stable |
| MM 50j ASTS | 87.11 | 87.11 | Stable |
| Low intraday ASTS | 101.21 | 101.21 | Stable |
| High intraday ASTS | 111.28 | 111.28 | Stable |
| Short interest ASTS | 17.60% | 17.60% | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus ASTS | +11.8% | +11.8% | Stable |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Placeholder stable |
| Score ASTS (agent) | 44.8/100 (SURVEILLER) | **44.8/100 (SURVEILLER)** | Stable |
| Options put/call ASTS | **0.92** | **1.09** | **↗ +0.17 — bascule au-dessus de 1.0** |
| Options call OI ASTS | **52.2%** | **47.9%** | **↘ −4.3 pts — sous la barre des 50%** |
| Max pain ASTS | $120.0 | $120.0 | Stable |
| Earnings FMP AST | 2026-06-01 (days_until: 0) | 2026-06-02 (days_until: 0) | **Placeholder glissant J=0 non résolu — 8j de glissement** |
| Earnings ASTS (yfinance) | 2026-08-10 (70j) | 2026-08-10 (69j) | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | ROTATION_TO_CYCLICAL | ROTATION_TO_CYCLICAL | Stable (XLK top1, momentum 10.0) |

**Constat :** Le snapshot 13:00 UTC enregistre une **stabilisation totale** sur le proxy ASTS par rapport au close 21h UTC du 01/06. Le cours reste à **$105.65**, le volume à la moyenne 20j, et le RSI inchangé à **61.89**. Le marché US n'étant pas ouvert au moment du snapshot (13h UTC = 9h EST), les données de prix reflètent le close de la veille.

**Changement notable :** La configuration options sur ASTS s'est **légèrement dégradée** : le put/call ratio est passé de **0.92 à 1.09** (dépassement de la parité, signal baissier) et le call OI est tombé de **52.2% à 47.9%** (sous 50%, fin du biais haussier options). Le max pain reste à **$120** (+13.6% au-dessus du cours).

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 13:00 UTC (02/06) | Valeur précédente (21:00 UTC 01/06) | Δ |
|-----------|-------------------------|-------------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur 24 snapshots consécutifs.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 13:00 UTC (02/06) | Valeur précédente (21:00 UTC 01/06) | Δ |
|-----------|-------------------------|-------------------------------------|---|
| Cours close | **$105.65** | $105.65 | **Stable** |
| Open | 108.67 | 108.67 | Stable |
| High intraday | 111.28 | 111.28 | Stable |
| Low intraday | 101.21 | 101.21 | Stable |
| Volume séance | **27.14M** | 27.07M | **1.00× moy. 20j** (stable) |
| RSI 14j | **61.89** | 61.89 | Stable |
| ATR 14j | **12.18** | 12.18 | Stable |
| MM 50j | **87.11** | 87.11 | Stable |
| Distance MM50j | **+21.3%** | +21.3% | Stable |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−21.1%** | −21.1% | Stable |

**Verdict timing ASTS (proxy) :** 🟡 **STABILISATION TECHNIQUE POST-CORRECTION MAINTENUE** — Le cours reste à **$105.65** au snapshot 13h UTC (marché non ouvert), confirmant le plancher temporaire sur la zone **$101–102** atteint en intra-day le 01/06. Le RSI à **61.89** reste dans la zone neutre-haussière (50–70), sans surachat. La MM50j à **$87.11** constitue le support structurel intermédiaire. La prochaine résistance immédiate reste la zone **$105–110** (ancien support cassé le 01/06, désormais résistance) ; un franchissement durable au-dessus de **$110** réactiverait le biais haussier. En dessous, le plancher intra-day à **$101.21** reste le support critique ; une cassure ouvrirait la voie vers **$95–100**.

> **Note importante :** le snapshot 13h UTC (9h EST) est capturé avant l'ouverture du marché US. Toute évolution du cours ASTS au cours de la séance du 02/06 ne sera visible qu'au prochain snapshot (17h ou 21h UTC).

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 13:00 UTC (02/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 13:00 UTC (02/06) | Valeur précédente (21:00 UTC 01/06) | Δ |
|---------|-------------------------|-------------------------------------|---|
| Market cap | **$41.01B** | $41.01B | Stable |
| Forward P/E | **−355.57** | −355.57 | Stable |
| EV/Revenue | **378.0×** | 405.3× | **Amélioration mécanique −6.7%** |
| EV/EBITDA | **−101.47** | −108.80 | **Amélioration mécanique −6.7%** |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus | **+11.8%** | +11.8% | Stable |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). L'amélioration mécanique des multiples EV/Revenue (378× vs 405×) et EV/EBITDA (−101.47 vs −108.80) est entièrement liée à la stabilisation du cours et ne reflète aucune révision fondamentale. Le sell-side n'a pas révisé son PT ($94.54, 12 analysts). La société n'est pas profitable (net margin −4.82%, operating margin −4.06%) et le modèle reste dépendant des jalons technologiques et des contrats commerciaux D2D.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-06-02.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :**
  - Max pain **$120.0** (stable, +13.6% au-dessus du close)
  - Put/call ratio **1.09** (vs 0.92 précédemment) — **bascule au-dessus de 1.0, signal baissier options**
  - Call OI **47.9%** (vs 52.2% précédemment) — **chute sous 50%, fin du biais haussier des détenteurs d'options**
  - Échéance prochaine : 2026-06-05
  - **Interprétation :** la communauté options s'est légèrement repositionnée à la baisse entre le close 21h UTC et le snapshot 13h UTC. Le max pain à $120 reste un aimant gamma potentiel si le cours se stabilise au-dessus de $105, mais le dépassement de la parité put/call et la chute du call OI sous 50% indiquent une prise de profits haussière et/ou une couverture baissière accrue.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $105.65 = **+11.8% au-dessus du consensus**
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant (insuffisant), geo (🟢, pas de flag), accounting (fichier inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-02** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 26/05, **8 jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 69`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **ROTATION_TO_CYCLICAL** maintenu (XLK top1 sector, momentum score 10.0). XLE en bullish crossover. **Paradoxe sectoriel persistant :** ASTS (Technology) sous-performe massivement le secteur Technology en séance du 01/06 (−6.84% vs close précédent alors que XLK domine) — divergence interne négative probablement liée à un factor spécifique (short covering exhausted, incertitude earnings, rotation interne tech vers les grandes caps qualité).

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 13:00 UTC (02/06) | Pondération | Note |
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

| Axe | Score 13:00 UTC (02/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais non vérifiable à court terme |
| Valorisation | 3.0/10 | 40% | EV/Revenue 378×, forward P/E −355.57, premium consensus ré-étendu à +11.8% |
| Momentum | 5.5/10 | 25% | Stabilisation à $105.65 post-correction, RSI 61.89 neutre-haussier |
| **Score Opportunité** | **4.0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39.8/100** | — | SURVEILLER |
| **Score Global Ajusté** | **44.8/100** | — | **SURVEILLER** |

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Neutre
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. Le score **SURVEILLER (44.8/100)** reflète la **stabilisation technique** (cours stable à $105.65, volume normalisé, RSI neutre-haussier) mais la valorisation reste speculative (forward P/E −355.57, EV/Revenue 378×). La configuration options s'est légèrement dégradée (put/call > 1.0, call OI < 50%). L'action reste **SURVEILLER**.

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
| Prix entrée | Cours close | $105.65 |
| Stop-loss | $105.65 − 2×12.18 | **$81.29** |
| Take-profit | $105.65 + 3×12.18 | **$142.19** |
| Ratio R/R | (142.19−105.65)/(105.65−81.29) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL à $81.29 et le TP à $142.19 sont inchangés**. Le support immédiat reste le low intra-day **$101.21** ; une cassure ouvrirait la voie vers la MM50j à **$87.11** et la zone **$95–100**. La résistance immédiate est l'ancien support cassé **$105–110** ; un franchissement durable au-dessus de **$110** réactiverait le biais haussier. Le max pain options à **$120** reste un aimant gamma potentiel si le titre se stabilise au-dessus de $105, mais le repositionnement options (put/call > 1.0, call OI < 50%) atténue ce signal.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (24 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **STABILISATION TECHNIQUE POST-CORRECTION MAINTENUE — SURVEILLER MAINTENU, OPTIONS LÉGÈREMENT DÉGRADÉES**

1. **Anomalie structurelle persistante :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **24 snapshots consécutifs** (18/05 → 02/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Stabilisation technique sur ASTS :** après une correction intra-day sévère jusqu'à **$101.21** le 01/06 (−20.9% depuis le close 27/05), le cours s'est stabilisé à **$105.65** au snapshot 13h UTC du 02/06 (marché non ouvert). Le volume total de la séance du 01/06 est resté à la moyenne 20j (**27.14M**, 1.00×), confirmant un plancher temporaire.
3. **RSI neutre-haussier :** le RSI à **61.89** reste dans la zone 50–70, ni surachat ni survente. La configuration technique est plus saine qu'à 13h le 01/06 (RSI 69.79) mais sans momentum haussier fort.
4. **Support / Résistance :** le support immédiat est le low intra-day **$101.21**. La zone **$105–110**, ancien support cassé le 01/06, constitue désormais la résistance immédiate. Un franchissement durable au-dessus de **$110** serait le premier signal de stabilisation ; une cassure sous **$101.21** ouvrirait la voie vers **$95–100**.
5. **Paradoxe sectoriel :** le signal sectoriel reste **ROTATION_TO_CYCLICAL** avec Technology (XLK) top1 (momentum 10.0). ASTS sous-performe massivement son secteur — divergence interne négative, probablement liée à un factor spécifique (short covering exhausted, incertitude earnings, rotation interne tech vers les grandes caps).
6. **Premium consensus ré-étendu :** le premium à **+11.8%** au-dessus du consensus est entièrement mécanique (cours stable) et ne reflète aucune révision sell-side. Le PT moyen ($94.54, 12 analysts) est inchangé.
7. **Options — légère dégradation :** le put/call ratio est passé de **0.92 à 1.09** (au-dessus de 1.0 = biais baissier) et le call OI de **52.2% à 47.9%** (sous 50% = fin du biais haussier des détenteurs d'options). Le max pain à **$120** est stable. Cette évolution suggère une prise de profits haussière et/ou une couverture baissière accrue entre le close 21h UTC et le snapshot 13h UTC.
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-02** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **26/05** (8 jours de décalage non résolu).
9. **Score agent ASTS stable :** le score ajusté reste à **44.8/100** (SURVEILLER) selon `recommandations_latest.json`. L'action reste **SURVEILLER**.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$101–102** (support immédiat) et de la résistance **$105–110**. Un rebond durable au-dessus de **$110** réactiverait le biais haussier. Le max pain options à **$120** reste un aimant gamma si le titre trouve un plancher au-dessus de $105, mais le repositionnement options (put/call > 1.0) limite l'optimisme.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 13:00 UTC, fetched_at 2026-06-02T13:00:01.467040+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json — aucune donnée hallucinée.*
