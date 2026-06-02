# AST — Mise à jour Quotidienne

> **Date :** 2026-06-02
> **Type :** Update finale (snapshot 21:00 UTC)
> **Source :** data/latest.json (fetched_at 21:00:14 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-02_update.md` (snapshot 17:00 UTC)

| Élément | 17:00 UTC (02/06) | 21:00 UTC (02/06) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >25 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$115.27** | **$118.17** | **+2.51%** (extension du rebond technique) |
| Volume ASTS | 13.18M (0.49×) | **20.93M (0.76×)** | **Recovery partiel +59% vs 17h** |
| RSI ASTS | 71.77 | **72.58** | **+0.81 pt** — surachat consolidé |
| ATR ASTS | 12.07 | 12.22 | Stable (+1.2%) |
| MM 50j ASTS | 87.62 | 87.67 | Stable (+0.1%) |
| Low intraday ASTS | 108.80 | 108.80 | Stable (plancher de séance conservé) |
| High intraday ASTS | 116.76 | **118.74** | **Nouveau high intra-day** |
| Short interest ASTS | 17.60% | 17.60% | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision sell-side |
| Premium vs consensus ASTS | +21.9% | **+25.0%** | **Ré-étalement mécanique +3.1 pts** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Placeholder stable |
| Score ASTS (agent) | 29.8/100 (ÉVITER) | 29.8/100 (ÉVITER) | **Stable** |
| Options put/call ASTS | 1.09 | 1.09 | Stable (biais baissier options inchangé) |
| Options call OI ASTS | 47.9% | 47.9% | Stable (sous 50%) |
| Max pain ASTS | $120.0 | $120.0 | Stable — désormais **+1.5%** au-dessus du close |
| Earnings FMP AST | 2026-06-02 (days_until: 0) | 2026-06-02 (days_until: 0) | Placeholder glissant J=0 non résolu — **10 jours de glissement** |
| Earnings ASTS (yfinance) | 2026-08-10 (69j) | 2026-08-10 (69j) | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | NEUTRAL | NEUTRAL | Stable (XLK top1, momentum 10.0) |

**Constat :** Le snapshot 21:00 UTC enregistre une **extension du rebond technique** sur ASTS, portant le cours de **$115.27 à $118.17** (+2.51% depuis 17h, **+11.85% sur la séance** vs close veille). Le volume partiellement récupéré à **20.93M (0.76×)** contre 13.18M (0.49×) à 17h invalide partiellement le signal de collapse observé dans l'après-midi, bien que la participation reste sous la moyenne 20j. Le RSI consolidé à **72.58** creuse légèrement la zone de surachat (>70). Le premium consensus se ré-étend mécaniquement à **+25.0%** du fait du rebond de cours, sans révision du sell-side. L'agent maintient ASTS sur **ÉVITER (29.8/100)**. Le max pain options à **$120** n'est plus qu'à **+1.5%** du close, renforçant le risque d'une pression gamma croissante d'ici l'échéance du 05/06.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 21:00 UTC (02/06) | Valeur précédente (17:00 UTC) | Δ |
|-----------|-------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur >25 snapshots consécutifs.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 21:00 UTC (02/06) | Valeur précédente (17:00 UTC) | Δ |
|-----------|-------------------------|-------------------------------|---|
| Cours close | **$118.17** | $115.27 | **+2.51%** |
| Open | 109.91 | 109.91 | Stable |
| High intraday | **118.74** | 116.76 | **+1.69%** — nouveau high |
| Low intraday | **108.80** | 108.80 | Stable (plancher de séance) |
| Volume séance | **20.93M** | 13.18M (partiel) | **0.76× moy. 20j** (recovery +59% vs 17h) |
| RSI 14j | **72.58** | 71.77 | **+0.81 pt** — surachat consolidé |
| ATR 14j | **12.22** | 12.07 | Stable (+1.2%) |
| MM 50j | **87.67** | 87.62 | Stable (+0.1%) |
| Distance MM50j | **+34.8%** | +31.6% | **Extension haussière +3.2 pts** |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−11.7%** | −13.9% | **Rapprochement +2.2 pts** |

**Verdict timing ASTS (proxy) :** 🔴 **REBOND TECHNIQUE EXTENDU EN SURACHAT — VOLUME PARTIELLEMENT RÉCUPÉRÉ MAIS RISQUE DE RETOURNEMENT PERSISTANT** — Le cours a poursuivi son rebond de **+2.51%** supplémentaires pour clôturer à **$118.17**, portant le gain total de la séance à **+11.85%**. Le volume, initialement effondré à 0.49× à 17h, a partiellement récupéré à **0.76×** (20.93M vs 27.45M moy. 20j), ce qui atténue le signal de faible participation institutionnelle mais ne l'élimine pas. Le RSI à **72.58** consolide la zone de surachat (>70). Le low intra-day à **$108.80** confirme un plancher de séance solide ; la résistance immédiate est désormais la zone **$118.74–120.00** (high intra-day + max pain options). Un franchissement durable au-dessus de **$120** réactiverait le biais haussier ; en dessous, le support reste **$108.80** puis la zone **$115–116**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 21:00 UTC (02/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 21:00 UTC (02/06) | Valeur précédente (17:00 UTC) | Δ |
|---------|-------------------------|-------------------------------|---|
| Market cap | **$45.86B** | $44.74B | **+2.5%** (mécanique) |
| Forward P/E | **−397.70** | −387.94 | **Dégradation mécanique −2.5%** |
| EV/Revenue | **378.0×** | 378.0× | Stable |
| EV/EBITDA | **−101.47** | −101.47 | Stable |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision |
| Premium vs consensus | **+25.0%** | +21.9% | **↗ +3.1 pts mécanique** |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Le rebond de cours mécanique dégrade le forward P/E (−397.70 vs −387.94) et ré-étend le premium consensus à **+25.0%** (vs +21.9%). Le sell-side n'a pas révisé son PT ($94.54, 12 analysts). La société n'est pas profitable (net margin −4.82%, operating margin −4.06%) et le modèle reste dépendant des jalons technologiques et des contrats commerciaux D2D.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-06-02.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :**
  - Max pain **$120.0** (stable, **+1.5%** au-dessus du close — compression mécanique du spread)
  - Put/call ratio **1.09** (stable) — biais baissier options inchangé malgré le rebond du cours
  - Call OI **47.9%** (stable) — sous 50%, fin du biais haussier des détenteurs d'options
  - Échéance prochaine : **2026-06-05** (dans 3 jours)
  - **Interprétation :** la communauté options n'a PAS suivi l'extension du rebond. Le put/call reste au-dessus de 1.0 et le call OI sous 50%, indiquant que les détenteurs d'options anticipent une consolidation ou un retournement. Le max pain à $120, désormais à seulement +1.5% du close, constitue un **aimant gamma renforcé** — si le titre se rapproche de cette zone avant vendredi, la pression gamma pourrait s'intensifier et déclencher une consolidation rapide.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $118.17 = **+25.0% au-dessus du consensus** (divergence extrême, mécanique)
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant (date 2026-05-17, insuffisant), geo (2026-05-17, pas de flag), accounting (fichier inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable. ASTS price_change_pct enregistré à **+11.85%**
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-02** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 25/05, **10 jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 69`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **NEUTRAL** maintenu. XLK reste top1 sector (momentum 10.0) mais le signal macro reste neutralisé. XLE en bullish crossover. **Paradoxe sectoriel persistant :** ASTS (Technology) surperforme massivement le secteur Technology en séance (+11.85% alors que XLK est déjà top1) — divergence interne positive aujourd'hui, probablement liée à un factor spécifique (short covering, squeeze technique, approche du max pain $120) plutôt qu'à la rotation sectorielle.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 21:00 UTC (02/06) | Pondération | Note |
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

| Axe | Score 21:00 UTC (02/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais non vérifiable à court terme |
| Valorisation | 3.0/10 | 40% | EV/Revenue 378×, forward P/E −397.70, premium consensus ré-étendu à +25.0% |
| Momentum | 5.5/10 | 25% | Rebond technique +11.85% mais volume 0.76× (sous moyenne), RSI surachat 72.58 |
| **Score Opportunité** | **4.0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39.8/100** | — | ÉVITER |
| **Score Global Ajusté** | **29.8/100** | — | **ÉVITER** |

**Action recommandée par l'agent :** ÉVITER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. Le score **ÉVITER (29.8/100)** reflète la **configuration technique risquée** (rebond en surachat sur volume inférieur à la moyenne, RSI 72.58, signal sectoriel neutralisé) et la **valorisation speculative** (forward P/E −397.70, EV/Revenue 378×, premium consensus +25.0%). La configuration options reste baissière (put/call > 1.0, call OI < 50%). L'action reste classée **ÉVITER**.

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
| Prix entrée | Cours close | $118.17 |
| Stop-loss | $118.17 − 2×12.22 | **$93.73** |
| Take-profit | $118.17 + 3×12.22 | **$154.83** |
| Ratio R/R | (154.83−118.17)/(118.17−93.73) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL à $93.73 et le TP à $154.83 sont révisés à la hausse** (+$2.60 et +$2.35 respectivement) en raison du rebond du cours. Le support immédiat est le low intra-day **$108.80** ; une cassure ouvrirait la voie vers la zone **$115–116** puis la MM50j à **$87.67**. La résistance immédiate est la zone **$118.74–120.00** (high intra-day + max pain options) ; un franchissement durable au-dessus de **$120** réactiverait le biais haussier. Le max pain options à **$120** avec échéance 06-05 (dans 3 jours) est le niveau critique à surveiller.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>25 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🔴 **REBOND TECHNIQUE EXTENDU EN SURACHAT — ÉVITER MAINTENU**

1. **Anomalie structurelle persistante :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **>25 snapshots consécutifs** (18/05 → 02/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Rebond technique extendu sur ASTS :** le cours a rebondi de **+11.85%** sur la séance du 02/06 pour clôturer à **$118.17**, avec une extension de **+2.51%** entre 17h et 21h. Le volume partiellement récupéré à **20.93M (0.76×)** contre 13.18M (0.49×) à 17h atténue le signal de désengagement institutionnel, mais la participation reste sous la moyenne 20j.
3. **RSI consolidé en surachat :** le RSI à **72.58** reste au-dessus de 70, creusant légèrement la zone de surachat. Cette accélération technique sans fondamental est interprétée comme un risque de retournement élevé.
4. **Support / Résistance :** le support immédiat est le low intra-day **$108.80**. La zone **$118.74–120.00** constitue désormais la résistance immédiate (high intra-day + max pain options). Un franchissement durable au-dessus de **$120** serait le premier signal de stabilisation ; une cassure sous **$108.80** ouvrirait la voie vers **$115–116** puis la MM50j à **$87.67**.
5. **Paradoxe sectoriel :** le signal sectoriel reste **NEUTRAL** alors que XLK reste top1 (momentum 10.0). ASTS surperforme massivement son secteur aujourd'hui — divergence interne positive probablement liée à un factor spécifique (short covering, squeeze technique, approche du max pain $120) plutôt qu'à la rotation sectorielle.
6. **Premium consensus extrême :** le premium s'est ré-étalé massivement à **+25.0%** au-dessus du consensus ($94.54, 12 analysts). Aucune révision sell-side n'a été enregistrée. Le cours est désormais 25.0% au-dessus du prix cible moyen des analystes — une divergence rare et fragile.
7. **Options — biais baissier inchangé :** le put/call ratio reste à **1.09** (au-dessus de 1.0, signal baissier) et le call OI à **47.9%** (sous 50%). Malgré le rebond du cours, la communauté options ne s'est pas repositionnée à la hausse. Le max pain à $120, désormais à **+1.5%** du close, est un aimant gamma renforcé avec échéance 2026-06-05 (dans 3 jours).
8. **Agent maintient ÉVITER :** l'agent maintient ASTS sur **ÉVITER (29.8/100)** — stable vs 17h. Ce maintien reflète la persistance du surachat technique, du volume sous moyenne et de la valorisation speculative.
9. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-02** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (10 jours de décalage non résolu).

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$118.74–120.00** (résistance immédiate + max pain gamma) et du support **$108.80**. Le rebond sur volume partiellement récupéré et le RSI surachat 72.58 suggèrent un risque élevé de consolidation ou de pullback dès l'approche de $120. La thèse sur ASTS reste **ÉVITER**.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 21:00 UTC, fetched_at 2026-06-02T21:00:14.724099+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json — aucune donnée hallucinée.*
