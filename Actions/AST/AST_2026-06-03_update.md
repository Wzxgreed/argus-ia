# AST — Mise à jour Quotidienne

> **Date :** 2026-06-03
> **Type :** Update matin (snapshot 10:00 UTC)
> **Source :** data/latest.json (fetched_at 2026-06-03T10:00:18 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-02_update.md` (snapshot 21:00 UTC)

| Élément | 21:00 UTC (02/06) | 10:00 UTC (03/06) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >26 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$118.17** | **$118.17** | **Stable** (snapshot pre-market, marché non ouvert à 10h UTC) |
| Volume ASTS | 20.93M (0.76×) | **21.29M (0.78×)** | **Stable** — légère révision mécanique +2% |
| RSI ASTS | 72.58 | **72.58** | Stable |
| ATR ASTS | 12.22 | 12.22 | Stable |
| MM 50j ASTS | 87.67 | 87.67 | Stable |
| Low intraday ASTS | 108.80 | 108.80 | Stable (plancher de séance 02/06 conservé) |
| High intraday ASTS | 118.74 | 118.74 | Stable |
| Short interest ASTS | 17.60% | 17.60% | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision sell-side |
| Premium vs consensus ASTS | +25.0% | **+25.0%** | Stable |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Placeholder stable |
| Score ASTS (agent) | 29.8/100 (ÉVITER) | 29.8/100 (ÉVITER) | **Stable** |
| Options max pain ASTS | $120.0 | **$40.0** | **🚨 ANOMALIE JSON DÉTECTÉE** — valeur aberrante, opérationnelle $120.0 conservée |
| Options put/call ASTS | 1.09 | **null** | Dégradation données options (JSON incomplet) |
| Options call OI ASTS | 47.9% | **null** | Dégradation données options (JSON incomplet) |
| Échéance options ASTS | 2026-06-05 | 2026-06-05 | Stable (dans 2 jours) |
| Earnings FMP AST | 2026-06-02 (days_until: 0) | **2026-06-03 (days_until: 0)** | **Placeholder glissant J=0 persistant — 11 jours de glissement** |
| Earnings ASTS (yfinance) | 2026-08-10 (69j) | **2026-08-10 (68j)** | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | NEUTRAL | NEUTRAL | Stable (XLK top1, momentum 10.0) |

**Constat :** Le snapshot 10:00 UTC du 03/06 confirme la **stabilité totale** des données par rapport au close du 02/06. ASTS reste à **$118.17** (pre-market, marché US non ouvert à 10h UTC). Le volume est légèrement révisé à **21.29M (0.78×)** vs 20.93M précédemment — la sous-participation vs moyenne 20j persiste. Le RSI à **72.58** et le max pain opérationnel à **$120** (anomalie JSON 40.0 détectée et traitée) confirment la configuration risquée. L'agent maintient ASTS sur **ÉVITER (29.8/100)**. L'earnings FMP pour AST a glissé au **2026-06-03** (`days_until: 0`) — **11 jours de glissement consécutifs non résolus**, confirmant le caractère placeholder de cette date.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 10:00 UTC (03/06) | Valeur précédente (21:00 UTC 02/06) | Δ |
|-----------|-------------------------|-------------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur >26 snapshots consécutifs.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 10:00 UTC (03/06) | Valeur précédente (21:00 UTC 02/06) | Δ |
|-----------|-------------------------|-------------------------------------|---|
| Cours close | **$118.17** | $118.17 | **Stable** (pre-market) |
| Open | 109.91 | 109.91 | Stable |
| High intraday | **118.74** | 118.74 | Stable |
| Low intraday | **108.80** | 108.80 | Stable (plancher de séance 02/06) |
| Volume séance | **21.29M** | 20.93M | **Stable** (0.78× moy. 20j) |
| RSI 14j | **72.58** | 72.58 | Stable — surachat consolidé |
| ATR 14j | **12.22** | 12.22 | Stable |
| MM 50j | **87.67** | 87.67 | Stable |
| Distance MM50j | **+34.8%** | +34.8% | Stable |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−11.7%** | −11.7% | Stable |

**Verdict timing ASTS (proxy) :** 🔴 **STABILITÉ PRE-MARKET EN SURACHAT — RISQUE DE RETOURNEMENT PERSISTANT** — Le cours à **$118.17** est inchangé vs le close du 02/06 (snapshot pre-market à 10h UTC, marché non ouvert). Le volume révisé à **21.29M (0.78×)** contre 27.47M moy. 20j confirme une participation institutionnelle toujours inférieure à la normale. Le RSI à **72.58** reste en zone de surachat (>70). Le low intra-day à **$108.80** et le high à **$118.74** définissent la fourchette de la séance du 02/06. La résistance immédiate reste la zone **$118.74–120.00** (high intra-day + max pain options opérationnel). Un franchissement durable au-dessus de **$120** réactiverait le biais haussier ; en dessous, le support reste **$108.80** puis la zone **$115–116**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 10:00 UTC (03/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 10:00 UTC (03/06) | Valeur précédente (21:00 UTC 02/06) | Δ |
|---------|-------------------------|-------------------------------------|---|
| Market cap | **$45.86B** | $45.86B | Stable |
| Forward P/E | **−397.70** | −397.70 | Stable |
| EV/Revenue | **422.0×** | 422.0× | Stable |
| EV/EBITDA | **−113.30** | −113.30 | Stable |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision |
| Premium vs consensus | **+25.0%** | +25.0% | Stable |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Aucune révision sell-side n'a été enregistrée. La société n'est pas profitable (net margin −4.82%, operating margin −4.06%) et le modèle reste dépendant des jalons technologiques et des contrats commerciaux D2D.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :**
  - Max pain **$40.0** dans `data/latest.json` — **🚨 ANOMALIE JSON DÉTECTÉE** : cette valeur est aberrante (cours $118.17, écart −66%). La valeur opérationnelle **$120.0** (consensus des snapshots précédents) est conservée pour l'analyse.
  - Put/call ratio **null** (données manquantes dans le snapshot) — impossible à évaluer
  - Call OI **null** (données manquantes dans le snapshot) — impossible à évaluer
  - Échéance prochaine : **2026-06-05** (dans 2 jours)
  - **Interprétation :** la dégradation des données options (max pain aberrant, put/call et call OI passés à null) empêche une lecture fiable du positionnement options. Le max pain opérationnel à $120 reste le niveau critique à surveiller avec l'échéance 2026-06-05 dans 2 jours.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $118.17 = **+25.0% au-dessus du consensus** (divergence extrême)
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant (date 2026-05-17, insuffisant), geo (2026-05-17, pas de flag), accounting (fichier inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable. ASTS price_change_pct enregistré à **+11.85%**
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-03** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 25/05, **11 jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 68`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **NEUTRAL** maintenu. XLK reste top1 sector (momentum 10.0). **Paradoxe sectoriel persistant :** ASTS (Technology) surperforme massivement le secteur Technology en séance (+11.85% sur la séance du 02/06 alors que XLK est déjà top1) — divergence interne positive, probablement liée à un factor spécifique (short covering, squeeze technique, approche du max pain $120) plutôt qu'à la rotation sectorielle.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 10:00 UTC (03/06) | Pondération | Note |
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

| Axe | Score 10:00 UTC (03/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais non vérifiable à court terme |
| Valorisation | 3.0/10 | 40% | EV/Revenue 422×, forward P/E −397.70, premium consensus +25.0% |
| Momentum | 5.5/10 | 25% | Rebond technique +11.85% mais volume 0.78× (sous moyenne), RSI surachat 72.58 |
| **Score Opportunité** | **4.0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39.8/100** | — | ÉVITER |
| **Score Global Ajusté** | **29.8/100** | — | **ÉVITER** |

**Action recommandée par l'agent :** ÉVITER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. Le score **ÉVITER (29.8/100)** reflète la **configuration technique risquée** (rebond en surachat sur volume inférieur à la moyenne, RSI 72.58, signal sectoriel neutralisé) et la **valorisation speculative** (forward P/E −397.70, EV/Revenue 422×, premium consensus +25.0%). La dégradation des données options (max pain aberrant 40.0, put/call et call OI passés à null) empêche une lecture fine du positionnement mais ne change pas la conclusion. L'action reste classée **ÉVITER**.

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

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Les niveaux sont inchangés** vs le snapshot 21:00 UTC 02/06 (cours stable à $118.17, ATR stable à 12.22). Le support immédiat est le low intra-day **$108.80** ; une cassure ouvrirait la voie vers la zone **$115–116** puis la MM50j à **$87.67**. La résistance immédiate est la zone **$118.74–120.00** (high intra-day + max pain options opérationnel) ; un franchissement durable au-dessus de **$120** réactiverait le biais haussier. Le max pain options opérationnel à **$120** avec échéance 06-05 (dans 2 jours) est le niveau critique à surveiller. **⚠️ Anomalie options JSON :** le snapshot retourne un max pain de $40.0 (aberrant vs cours $118.17) — la valeur opérationnelle $120.0 est conservée.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>26 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🔴 **STABILITÉ PRE-MARKET EN SURACHAT — ÉVITER MAINTENU**

1. **Anomalie structurelle persistante :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **>26 snapshots consécutifs** (18/05 → 03/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Stabilité pre-market sur ASTS :** le cours reste à **$118.17** au snapshot 10:00 UTC du 03/06 (marché US non ouvert, données du close 02/06 reportées). Aucun mouvement nouveau n'est enregistré depuis le rebond de **+11.85%** de la séance du 02/06.
3. **Volume toujours sous moyenne :** le volume révisé à **21.29M (0.78×)** contre 27.47M moy. 20j confirme une participation institutionnelle inférieure à la normale. Ce n'est pas un signal de désengagement massif, mais ce n'est pas non plus une confirmation de la tendance haussière.
4. **RSI consolidé en surachat :** le RSI à **72.58** reste au-dessus de 70, confirmant la zone de surachat. Cette configuration sans nouveau catalyseur fondamental est interprétée comme un risque de retournement élevé.
5. **Support / Résistance :** le support immédiat est le low intra-day **$108.80** (plancher de la séance du 02/06). La zone **$118.74–120.00** constitue la résistance immédiate (high intra-day + max pain options opérationnel). Un franchissement durable au-dessus de **$120** serait le premier signal de stabilisation ; une cassure sous **$108.80** ouvrirait la voie vers **$115–116** puis la MM50j à **$87.67**.
6. **Anomalie options JSON :** le snapshot retourne un max pain de **$40.0** pour ASTS (vs $120.0 précédemment), valeur aberrante étant donné le cours à $118.17. Le put/call ratio et le call OI sont passés à **null**. Ces données dégradées empêchent une lecture fine du positionnement options mais ne changent pas la conclusion — l'échéance 2026-06-05 (dans 2 jours) avec max pain opérationnel à $120 reste le risque gamma dominant.
7. **Premium consensus extrème :** le premium reste à **+25.0%** au-dessus du consensus ($94.54, 12 analysts). Aucune révision sell-side n'a été enregistrée. Le cours est 25.0% au-dessus du prix cible moyen des analystes — une divergence rare et fragile.
8. **Agent maintient ÉVITER :** l'agent maintient ASTS sur **ÉVITER (29.8/100)** — stable vs 21:00 UTC 02/06. Ce maintien reflète la persistance du surachat technique, du volume sous moyenne et de la valorisation speculative.
9. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-03** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (11 jours de décalage non résolu). Le preview `AST_2026-06-03_preview.md` existe mais est un template vide — aucune prédiction n'a été renseignée.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$118.74–120.00** (résistance immédiate + max pain gamma opérationnel) et du support **$108.80**. Le volume sous moyenne et le RSI surachat 72.58 suggèrent un risque élevé de consolidation ou de pullback dès l'approche de $120. La thèse sur ASTS reste **ÉVITER**.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 10:00 UTC, fetched_at 2026-06-03T10:00:18.184576+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
