# AST — Mise à jour Quotidienne

> **Date :** 2026-06-02
> **Type :** Update (snapshot 17:00 UTC)
> **Source :** data/latest.json (fetched_at 17:00:02 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-02_update.md` (snapshot 13:00 UTC)

| Élément | 13:00 UTC (02/06) | 17:00 UTC (02/06) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — 25 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$105.65** | **$115.27** | **↗ +9.11% — rebond technique massif** |
| Volume ASTS | 27.14M (1.00×) | **13.18M** (0.49×) | **↘ −51% vs séance précédente, collapse alarmant** |
| RSI ASTS | 61.89 | **71.77** | **↗ +9.88 pts — entrée zone surachat (>70)** |
| ATR ASTS | 12.18 | 12.07 | Stable (contraction −0.9%) |
| MM 50j ASTS | 87.11 | **87.62** | Haussière mécanique (+0.6%) |
| Low intraday ASTS | 101.21 | **108.80** | Nouveau plancher plus haut |
| High intraday ASTS | 111.28 | **116.76** | Nouveau high intra-day |
| Short interest ASTS | 17.60% | 17.60% | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision sell-side |
| Premium vs consensus ASTS | +11.8% | **+21.9%** | **↗ +10.1 pts — ré-étalement mécanique massif** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Placeholder stable |
| Score ASTS (agent) | **44.8/100 (SURVEILLER)** | **29.8/100 (ÉVITER)** | **↘ −15.0 pts — downgrade massif** |
| Options put/call ASTS | 1.09 | 1.09 | Stable (biais baissier options inchangé) |
| Options call OI ASTS | 47.9% | 47.9% | Stable (sous 50%) |
| Max pain ASTS | $120.0 | $120.0 | Stable |
| Earnings FMP AST | 2026-06-02 (days_until: 0) | 2026-06-02 (days_until: 0) | Placeholder glissant J=0 non résolu — **9 jours de glissement** |
| Earnings ASTS (yfinance) | 2026-08-10 (69j) | 2026-08-10 (69j) | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | ROTATION_TO_CYCLICAL | **NEUTRAL** | **Neutralisé** (was ROTATION_TO_CYCLICAL) |

**Constat :** Le snapshot 17:00 UTC enregistre un **rebond technique massif de +9.11%** sur ASTS, portant le cours de **$105.65 à $115.27**. Cependant, ce rebond s'accompagne d'un **collapse du volume à 0.49×** la moyenne 20j (13.18M vs 27.05M), signalant une participation institutionnelle faible et un rebond potentiellement technique/short-covering sans conviction. Le RSI a franchi la barre des **70** (71.77, +9.88 pts), entrant en zone surachat. Le signal sectoriel a été **neutralisé à NEUTRAL** alors que XLK reste top1. L'agent a **downgradé massivement ASTS de SURVEILLER (44.8) à ÉVITER (29.8)** — une dégradation de 15 points, probablement pilotée par le surachat technique et le volume collapse.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 17:00 UTC (02/06) | Valeur précédente (13:00 UTC 02/06) | Δ |
|-----------|-------------------------|-------------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur 25 snapshots consécutifs.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 17:00 UTC (02/06) | Valeur précédente (13:00 UTC 02/06) | Δ |
|-----------|-------------------------|-------------------------------------|---|
| Cours close | **$115.27** | $105.65 | **↗ +9.11%** |
| Open | 109.91 | 108.67 | **↗ +1.14% en gap haussier** |
| High intraday | 116.76 | 111.28 | **↗ +4.92%** |
| Low intraday | 108.80 | 101.21 | **↗ +7.50% — nouveau plancher** |
| Volume séance | **13.18M** | 27.14M | **↘ 0.49× moy. 20j** (collapse −51% vs séance précédente) |
| RSI 14j | **71.77** | 61.89 | **↗ +9.88 pts — surachat** |
| ATR 14j | **12.07** | 12.18 | Stable (−0.9%) |
| MM 50j | **87.62** | 87.11 | Stable (+0.6%) |
| Distance MM50j | **+31.6%** | +21.3% | **Extension haussière +10.3 pts** |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−13.9%** | −21.1% | **Rapprochement +7.2 pts** |

**Verdict timing ASTS (proxy) :** 🔴 **REBOND TECHNIQUE ANÉMIQUE EN SURACHAT — RISQUE DE RETOURNEMENT ÉLEVÉ** — Le cours a rebondi de **+9.11%** à **$115.27** au cours de la séance du 02/06, mais sur un volume **effondré à 0.49×** la moyenne 20j (13.18M vs 27.05M). Cette divergence prix/volume est classiquement interprétée comme un **rebond de short-covering ou technique sans participation acheteuse**, plutôt que comme un renversement de tendance fondé. Le RSI à **71.77** franchit la zone de surachat (>70), accentuant le risque de consolidation ou de pullback. Le low intra-day à **$108.80** confirme un nouveau plancher plus haut que le précédent ($101.21), mais la résistance immédiate est désormais la zone **$116–120** (high intra-day + max pain options). Un franchissement durable au-dessus de **$120** réactiverait le biais haussier ; en dessous, le support reste **$108.80** puis la zone **$105–110**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 17:00 UTC (02/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 17:00 UTC (02/06) | Valeur précédente (13:00 UTC 02/06) | Δ |
|---------|-------------------------|-------------------------------------|---|
| Market cap | **$44.74B** | $41.01B | **↗ +9.11% mécanique** |
| Forward P/E | **−387.94** | −355.57 | **Dégradation mécanique −9.1%** |
| EV/Revenue | **378.0×** | 378.0× | Stable |
| EV/EBITDA | **−101.47** | −101.47 | Stable |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision |
| Premium vs consensus | **+21.9%** | +11.8% | **↗ +10.1 pts mécanique** |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). L'amélioration du market cap (+9.11%) et la dégradation mécanique du forward P/E (−387.94 vs −355.57) sont entièrement liées au rebond du cours et ne reflètent aucune révision fondamentale. Le sell-side n'a pas révisé son PT ($94.54, 12 analysts). Le premium au consensus s'est ré-étalé massivement à **+21.9%** (vs +11.8%), creusant la divergence entre le cours de marché et les attentes analystes. La société n'est pas profitable (net margin −4.82%, operating margin −4.06%) et le modèle reste dépendant des jalons technologiques et des contrats commerciaux D2D.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-06-02.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :**
  - Max pain **$120.0** (stable, +4.1% au-dessus du close)
  - Put/call ratio **1.09** (stable) — biais baissier options inchangé malgré le rebond du cours
  - Call OI **47.9%** (stable) — sous 50%, fin du biais haussier des détenteurs d'options
  - Échéance prochaine : 2026-06-05 (dans 3 jours)
  - **Interprétation :** la communauté options n'a PAS suivi le rebond du cours. Le put/call reste au-dessus de 1.0 et le call OI sous 50%, indiquant que les détenteurs d'options anticipent une consolidation ou un retournement. Le max pain à $120 reste un aimant gamma — si le titre se rapproche de cette zone avant vendredi, la pression gamma pourrait s'intensifier.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $115.27 = **+21.9% au-dessus du consensus** (divergence extrême)
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant (insuffisant), geo (🟢, pas de flag), accounting (fichier inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable. ASTS price_change_pct enregistré à **+9.11%** (vs null précédemment)
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-02** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 25/05, **9 jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 69`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **NEUTRAL** (vs ROTATION_TO_CYCLICAL précédemment). XLK reste top1 sector (momentum 10.0) mais le signal macro a été neutralisé. XLE en bullish crossover. **Paradoxe sectoriel aggravé :** ASTS a rebondi de +9.11% alors que le signal sectoriel s'est neutralisé — divergence interne probablement liée à un factor spécifique (short covering, squeeze technique) plutôt qu'à la rotation sectorielle.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 17:00 UTC (02/06) | Pondération | Note |
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

| Axe | Score 17:00 UTC (02/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais non vérifiable à court terme |
| Valorisation | 3.0/10 | 40% | EV/Revenue 378×, forward P/E −387.94, premium consensus ré-étendu à +21.9% |
| Momentum | 5.5/10 | 25% | Rebond technique +9.11% mais volume collapse 0.49×, RSI surachat 71.77 |
| **Score Opportunité** | **4.0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39.8/100** | — | ÉVITER |
| **Score Global Ajusté** | **29.8/100** | — | **ÉVITER** |

**Action recommandée par l'agent :** ÉVITER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. Le score **ÉVITER (29.8/100)** reflète la **dégradation technique** (rebond anémique sur volume collapse, RSI surachat 71.77, signal sectoriel neutralisé) et la **valorisation speculative** (forward P/E −387.94, EV/Revenue 378×, premium consensus +21.9%). Le downgrade de **−15.0 pts** (44.8 → 29.8) est cohérent avec la configuration technique fragilisée. La configuration options reste baissière (put/call > 1.0, call OI < 50%). L'action est désormais classée **ÉVITER**.

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
| Prix entrée | Cours close | $115.27 |
| Stop-loss | $115.27 − 2×12.07 | **$91.13** |
| Take-profit | $115.27 + 3×12.07 | **$151.48** |
| Ratio R/R | (151.48−115.27)/(115.27−91.13) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL à $91.13 et le TP à $151.48 sont révisés à la hausse** (+$9.84 et +$9.29 respectivement) en raison du rebond du cours. Le support immédiat est le low intra-day **$108.80** ; une cassure ouvrirait la voie vers la zone **$105–110** puis la MM50j à **$87.62**. La résistance immédiate est la zone **$116–120** (high intra-day + max pain options) ; un franchissement durable au-dessus de **$120** réactiverait le biais haussier. Le max pain options à **$120** reste un aimant gamma potentiel si le titre se rapproche de cette zone d'ici vendredi (échéance 06-05).

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (25 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🔴 **REBOND TECHNIQUE ANÉMIQUE EN SURACHAT — DOWNGRADÉ DE SURVEILLER À ÉVITER**

1. **Anomalie structurelle persistante :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **25 snapshots consécutifs** (18/05 → 02/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Rebond technique massif sur ASTS :** le cours a rebondi de **+9.11%** à **$115.27** au cours de la séance du 02/06, effaçant une partie de la correction du 01/06. Cependant, ce rebond s'accompagne d'un **volume collapse à 0.49×** la moyenne 20j (13.18M vs 27.05M), signalant une faible participation institutionnelle.
3. **RSI entré en surachat :** le RSI à **71.77** franchit la zone de surachat (>70), après être resté à 61.89 au snapshot 13h. Cette accélération technique sans fondamental est interprétée comme un risque de retournement élevé.
4. **Support / Résistance :** le support immédiat est le low intra-day **$108.80**. La zone **$116–120** constitue désormais la résistance immédiate (high intra-day + max pain options). Un franchissement durable au-dessus de **$120** serait le premier signal de stabilisation ; une cassure sous **$108.80** ouvrirait la voie vers **$105–110**.
5. **Paradoxe sectoriel aggravé :** le signal sectoriel est passé de **ROTATION_TO_CYCLICAL à NEUTRAL** alors que XLK reste top1 (momentum 10.0). ASTS a rebondi de +9.11% dans un contexte sectoriel neutralisé — divergence interne probablement liée à un factor spécifique (short covering, squeeze technique) plutôt qu'à la rotation sectorielle.
6. **Premium consensus extrême :** le premium s'est ré-étalé massivement à **+21.9%** au-dessus du consensus ($94.54, 12 analysts). Aucune révision sell-side n'a été enregistrée. Le cours est désormais 21.9% au-dessus du prix cible moyen des analystes — une divergence rare et fragile.
7. **Options — biais baissier inchangé :** le put/call ratio reste à **1.09** (au-dessus de 1.0, signal baissier) et le call OI à **47.9%** (sous 50%). Malgré le rebond du cours, la communauté options ne s'est pas repositionnée à la hausse. Le max pain à $120 reste un aimant gamma avec échéance 2026-06-05 (dans 3 jours).
8. **Agent downgrade massif :** l'agent a dégradé ASTS de **SURVEILLER (44.8/100) à ÉVITER (29.8/100)** — une chute de 15 points. Ce downgrade reflète probablement l'entrée en surachat technique, le volume collapse et le signal sectoriel neutralisé.
9. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-02** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (9 jours de décalage non résolu).

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$116–120** (résistance immédiate) et du support **$108.80**. Le rebond anémique sur volume collapse et le RSI surachat 71.77 suggèrent un risque élevé de consolidation ou de pullback. Le max pain options à **$120** avec échéance 06-05 est le niveau critique à surveiller. La thèse sur ASTS est **downgradée à ÉVITER**.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 17:00 UTC, fetched_at 2026-06-02T17:00:02.219865+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json — aucune donnée hallucinée.*
