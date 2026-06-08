# AST — Mise à jour Quotidienne

> **Date :** 2026-06-08
> **Type :** Update matin (snapshot 10:00 UTC)
> **Source :** data/latest.json (fetched_at 2026-06-08T10:00:16 UTC), data/recommandations_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/validation_report.txt

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-03_update.md` (snapshot 10:00 UTC 03/06)

| Élément | 03/06 (10:00 UTC) | 08/06 (10:00 UTC) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >31 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$118.17** | **$93.60** | **🔴 CORRECTION −12.76%** |
| Volume ASTS | 21.29M (0.78×) | **23.90M (0.87×)** | **Stable sous moyenne** — +12.3% en volume, 0.87× vs 0.78× |
| RSI ASTS | 72.58 | **54.36** | **🟢 SORTIE DU SURACHAT** (−18.2 pts) |
| ATR ASTS | 12.22 | **13.19** | **+7.9%** — volatilité en hausse |
| MM 50j ASTS | 87.67 | **88.42** | **+0.9%** — cours reste au-dessus |
| Distance MM50j ASTS | +34.8% | **+5.9%** | Normalisation mécanique |
| Low intraday ASTS | 108.80 | **90.905** | **Nouveau low** — cassure support $108.80 |
| High intraday ASTS | 118.74 | **104.49** | **−12.0%** — résistance abaissée |
| Short interest ASTS | 17.60% | **17.60%** | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | **$94.54 (12 analysts)** | Stable — pas de révision sell-side |
| Premium vs consensus ASTS | **+25.0%** | **−1.0%** | **🟢 NORMALISATION MAJEURE** — cours sous consensus |
| Score ASTS (agent) | 29.8/100 (ÉVITER) | **48.5/100 (ATTENDRE)** | **🔼 UPGRADE +18.7 pts** |
| Timing ASTS (agent) | Défavorable | **Favorable** | **🟢 BASCULE** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | Placeholder stable |
| Options max pain ASTS | $40.0 (anomalie JSON) | **$45.0** | Anomalie JSON persistante — toujours aberrant |
| Options put/call ASTS | null | **null** | Données manquantes persistantes |
| Options call OI ASTS | null | **null** | Données manquantes persistantes |
| Échéance options ASTS | 2026-06-05 | **2026-06-12** | **+4 jours** — nouvelle échéance |
| Earnings FMP AST | 2026-06-03 (days_until: 0) | **2026-06-08 (days_until: 0)** | **Placeholder glissant J=0 persistant — 14+ jours** |
| Earnings ASTS (yfinance) | 2026-08-10 (68j) | **2026-08-10 (63j)** | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | NEUTRAL | **NEUTRAL** | Stable (XLK top1, momentum 10.0) |

**Constat :** Le snapshot du 08/06 marque une **inflexion technique et valuationnelle majeure** sur ASTS. Après une correction de **−12.76%** en séance (close $93.60 vs $107.29 previous close), le cours est revenu **légèrement sous le consensus analystes** ($94.54) pour la première fois depuis plusieurs semaines. Le RSI est sorti de la zone de surachat (>70) pour se stabiliser à **54.36** (neutre-haussier). L'agent a upgradé ASTS de **ÉVITER (29.8/100) à ATTENDRE (48.5/100)** avec un timing requalifié **Favorable**. AST reste sans aucune donnée de cours (>31 snapshots consécutifs).

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 10:00 UTC (08/06) | Valeur précédente (03/06) | Δ |
|-----------|-------------------------|---------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur >31 snapshots consécutifs. L'earnings FMP placeholder glissant au **2026-06-08** (`days_until: 0`, 14+ jours de glissement) n'a pas produit de résultats intégrés au pipeline.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 10:00 UTC (08/06) | Valeur précédente (03/06) | Δ |
|-----------|-------------------------|---------------------------|---|
| Cours close | **$93.60** | $118.17 | **🔴 −12.76%** |
| Open | **$103.33** | $109.91 | **−5.98%** (gap baissier) |
| High intraday | **$104.49** | $118.74 | **−12.0%** |
| Low intraday | **$90.905** | $108.80 | **−16.4%** — cassure support |
| Volume séance | **23.90M** | 21.29M | **+12.3%** — 0.87× moy. 20j |
| RSI 14j | **54.36** | 72.58 | **🟢 −18.2 pts — sortie surachat** |
| ATR 14j | **13.19** | 12.22 | **+7.9%** |
| MM 50j | **88.42** | 87.67 | **+0.9%** |
| Distance MM50j | **+5.9%** | +34.8% | Normalisation mécanique |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−30.1%** | −11.7% | Éloignement du high |

**Verdict timing ASTS (proxy) :** 🟡 **CORRECTION MAJEURE — NORMALISATION TECHNIQUE EN COURS** — La séance du 08/06 a vu une correction de **−12.76%** avec un gap baissier à l'ouverture ($103.33 vs close précédent $107.29) et un low à **$90.905** (cassure du support immédiat $108.80 identifié le 03/06). Le RSI à **54.36** est sorti de la zone de surachat et se situe désormais en zone neutre favorable (50–60). Le cours reste au-dessus de la MM50j (**$88.42**, +5.9%), ce qui constitue le support technique majeur à court terme. La résistance immédiate est repositionnée à la zone **$103.33–104.49** (gap baissier). Un franchissement au-dessus de **$104.50** réactiverait le biais haussier ; une cassure sous **$88.42** (MM50j) ouvrirait la voie vers la zone **$80–85**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 10:00 UTC (08/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 10:00 UTC (08/06) | Valeur précédente (03/06) | Δ |
|---------|-------------------------|---------------------------|---|
| Market cap | **$36.33B** | $45.86B | **−20.8%** (baisse mécanique) |
| Forward P/E | **−456.14** | −397.70 | **Dégradation** — perte plus élevée pricée |
| EV/Revenue | **335.6×** | 422.0× | **−20.5%** — amélioration mécanique |
| EV/EBITDA | **−90.10** | −113.30 | Amélioration mécanique |
| Beta | **2.634** | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision |
| Premium vs consensus | **−1.0%** | +25.0% | **🟢 NORMALISATION MAJEURE** |
| Price to book | **13.43** | — | Nouvelle donnée FMP |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Aucune révision sell-side n'a été enregistrée malgré la correction de −12.76%. La société n'est pas profitable (net margin −4.82%, operating margin −4.06%). Le retour du cours sous le consensus analystes ($93.60 vs $94.54) élimine le premium extrême qui justifiait l'aversion de l'agent. Cependant, les multiples restent extrêmement élevés (EV/Revenue 335.6×, forward P/E −456.14), confirmant le caractère spéculatif du titre.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :**
  - Max pain **$45.0** dans `data/latest.json` — **🚨 ANOMALIE JSON PERSISTANTE** : cette valeur est aberrante (cours $93.60, écart −52%). La valeur opérationnelle historique **$120.0** est obsolète post-correction. Le max pain ne peut pas être interprété fiablement avec cette anomalie persistante.
  - Put/call ratio **null** (données manquantes) — impossible à évaluer
  - Call OI **null** (données manquantes) — impossible à évaluer
  - Échéance prochaine : **2026-06-12** (dans 4 jours)
  - **Interprétation :** la persistance de l'anomalie options empêche une lecture fine du positionnement. L'échéance 2026-06-12 dans 4 jours reste un risque gamma à surveiller.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $93.60 = **−1.0% sous le consensus** (normalisation vs +25.0% précédemment)
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant, geo, accounting (inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable. ASTS price_change_pct enregistré à **−12.76%**
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-08** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 25/05, **14+ jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 63`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **NEUTRAL** maintenu. XLK reste top1 sector (momentum 10.0). ASTS (Technology) sousperforme massivement le secteur en séance (−12.76%) — correction idiosyncratique, non liée à la rotation sectorielle.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 10:00 UTC (08/06) | Pondération | Note |
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

| Axe | Score 10:00 UTC (08/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 5.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais aucun catalyseur court terme vérifiable |
| Valorisation | 4.0/10 | 40% | EV/Revenue 335.6×, forward P/E −456.14 — reste spéculatif malgré la normalisation du premium consensus |
| Momentum | 6.0/10 | 25% | Correction −12.76% mais RSI normalisé à 54.36, cours au-dessus MM50j |
| **Score Opportunité** | **4.8/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **48.5/100** | — | ATTENDRE |
| **Score Global Ajusté** | **53.5/100** | — | **ATTENDRE** |

**Action recommandée par l'agent :** ATTENDRE
**Timing :** Favorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. L'**upgrade de ÉVITER (29.8/100) à ATTENDRE (48.5/100)** reflète principalement : (1) la **sortie du surachat technique** (RSI 54.36 vs 72.58), (2) la **normalisation du premium consensus** (−1.0% vs +25.0%), et (3) le **maintien au-dessus de la MM50j** ($88.42). Cependant, le score Opportunité reste sous le seuil d'achat (4.8/10 < 6.0/10) et la valorisation demeure spéculative (EV/Revenue 335.6×, forward P/E −456.14). L'action reste classée **ATTENDRE**.

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
| Prix entrée | Cours close | $93.60 |
| Stop-loss | $93.60 − 2×13.19 | **$67.22** |
| Take-profit | $93.60 + 3×13.19 | **$133.17** |
| Ratio R/R | (133.17−93.60)/(93.60−67.22) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour quantifier la volatilité du proxy. Les niveaux sont **revus à la baisse** vs le snapshot du 03/06 (cours $118.17 → $93.60, ATR 12.22 → 13.19). Le support immédiat est désormais la **MM50j à $88.42** ; une cassure ouvrirait la voie vers la zone **$80–85** puis le low du jour à **$90.905** (déjà testé). La résistance immédiate est la zone **$103.33–104.49** (gap baissier + open/high du jour). Un franchissement durable au-dessus de **$104.50** réactiverait le biais haussier. L'échéance options 2026-06-12 (dans 4 jours) avec anomalie max pain persistante empêche une lecture fiable du risque gamma.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>31 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **MODIFIÉE — CORRECTION MAJEURE ET NORMALISATION, MAIS RESTE ATTENDRE**

1. **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **>31 snapshots consécutifs** (18/05 → 08/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Correction majeure sur ASTS :** le cours a chuté de **−12.76%** en séance pour clôturer à **$93.60**, avec un low à **$90.905** et un gap baissier à l'ouverture ($103.33 vs $107.29). Ce mouvement a effacé une partie significative du surchauffe technique accumulée depuis mai.
3. **Normalisation du premium consensus :** le cours est revenu **légèrement sous le consensus analystes** ($93.60 vs $94.54, premium **−1.0%**) pour la première fois depuis plusieurs semaines. Cette normalisation élimine le principal argument de surévaluation qui justifiait l'aversion de l'agent.
4. **Sortie du surachat technique :** le RSI est passé de **72.58 à 54.36** (zone neutre favorable). Cette sortie du surachat, combinée au retour sous le consensus, explique l'**upgrade agent ÉVITER → ATTENDRE (+18.7 pts)**.
5. **Support / Résistance revus :** le support immédiat est désormais la **MM50j à $88.42** (cours actuel +5.9%). Le low intra-day à **$90.905** a déjà été testé. La résistance immédiate est la zone **$103.33–104.49** (gap baissier). Un franchissement durable au-dessus de **$104.50** réactiverait le biais haussier ; une cassure sous **$88.42** (MM50j) ouvrirait la voie vers **$80–85**.
6. **Volume sous moyenne mais en hausse :** le volume à **23.90M (0.87×)** est resté sous la moyenne 20j (27.50M) mais en progression de +12.3% vs le 03/06. Cela suggère une vente ordonnée plutôt qu'un panic selling massif.
7. **Anomalie options JSON persistante :** le snapshot retourne un max pain de **$45.0** pour ASTS (valeur aberrante vs cours $93.60). Le put/call ratio et le call OI restent à **null**. Ces données dégradées empêchent une lecture fine du positionnement options. L'échéance 2026-06-12 (dans 4 jours) reste un risque gamma non quantifiable.
8. **Agent upgrade ATTENDRE avec timing Favorable :** l'agent a upgradé ASTS de **ÉVITER (29.8/100) à ATTENDRE (48.5/100)** avec un timing requalifié **Favorable**. Cependant, le score Opportunité (4.8/10) reste sous le seuil d'achat (6.0/10). La valorisation spéculative (EV/Revenue 335.6×, forward P/E −456.14) et l'absence de catalyseur court terme justifient le maintien en ATTENDRE.
9. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-08** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (14+ jours de décalage non résolu).

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$88.42** (MM50j) — support technique majeur. Une cassure ouvrirait la voie vers $80–85. À la hausse, le franchissement de **$104.50** (gap baissier) serait le premier signal technique positif. Le timing est requalifié **Favorable** mais le score Opportunité (4.8/10) reste insuffisant pour une entrée. La thèse sur ASTS passe de **ÉVITER à ATTENDRE**.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 10:00 UTC, fetched_at 2026-06-08T10:00:16.878894+00:00), data/recommandations_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/validation_report.txt — aucune donnée hallucinée.*
