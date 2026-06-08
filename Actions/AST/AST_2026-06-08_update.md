# AST — Mise à jour Quotidienne

> **Date :** 2026-06-08
> **Type :** Update soir (snapshot 17:00 UTC)
> **Source :** data/latest.json (fetched_at 2026-06-08T17:00:02 UTC), data/recommandations_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/validation_report.txt

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-08_update.md` (snapshot 13:00 UTC)

| Élément | 13:00 UTC | 17:00 UTC | Changement |
|---------|-----------|-----------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >32 snapshots consécutifs** |
| Cours ASTS (proxy) | **$93.60** | **$92.955** | **-0.69%** (légère poursuite de la correction) |
| Open ASTS | $103.33 | **$97.00** | Révision (open intraday réel vs données overnight) |
| High intraday ASTS | $104.49 | **$97.00** | Données intraday partielles — high révisé à la baisse |
| Low intraday ASTS | $90.905 | **$91.91** | Légère remontée du low intraday (+1.1%) |
| Volume ASTS | 23.90M | **7.71M** | **Volume intraday partiel** (0.29× moy. 20j vs 0.87× à 13h) |
| RSI ASTS | 54.36 | **52.75** | **-1.61 pt** — consolidation dans la zone neutre favorable |
| ATR ASTS | 13.19 | **12.97** | **-1.7%** (compression légère de la volatilité) |
| MM 50j ASTS | $88.42 | **$88.52** | **+0.1%** — support dynamique inchangé |
| Distance MM50j ASTS | +5.9% | **+5.0%** | Stable au-dessus de la MM50 |
| Short interest ASTS | 17.60% | **17.60%** | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision sell-side |
| Premium vs consensus ASTS | -1.0% | **-1.7%** | Légère dégradation mécanique |
| Score ASTS (agent) | 48.5/100 (ATTENDRE) | **51.0/100 (ATTENDRE)** | **+2.5 pts** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | Placeholder stable |
| Options ASTS | max pain $120.0, P/C 0.7, call OI 59.0% | **Identique** | Stable |
| Échéance options ASTS | 2026-06-12 | **2026-06-12** | Dans 4 jours (inchangé) |
| Earnings FMP AST | 2026-06-08 (days_until: 0) | **2026-06-08 (days_until: 0)** | Placeholder glissant J=0 persistant — 15+ jours |
| Earnings ASTS (yfinance) | 2026-08-10 (63j) | **2026-08-10 (63j)** | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | NEUTRAL | **NEUTRAL** | Stable (XLK top1, momentum 10.0) |
| Validation report | 5 errors (>2) | **5 errors (>2)** | [DONNÉES PARTIELLES] — pas de critical, AST en erreur connue |

**Constat :** Le snapshot 17h UTC confirme la **stabilité relative** d'ASTS vs le snapshot 13h, avec une légère poursuite de la correction (-0.69%) sur des volumes intraday très faibles (0.29× moyenne). Le RSI consolide à **52.75** (zone neutre favorable). L'anomalie structurelle sur AST persiste (>32 snapshots sans données). L'upgrade de l'agent sur ASTS (+2.5 pts, 48.5 → 51.0) reflète probablement une révision mécanique du momentum (7.0/10 inchangé) combinée à la stabilisation du cours au-dessus de la MM50j.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 17:00 UTC (08/06) | Valeur précédente (13:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur >32 snapshots consécutifs. L'earnings FMP placeholder glissant au **2026-06-08** (`days_until: 0`, 15+ jours de glissement) n'a pas produit de résultats intégrés au pipeline.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 17:00 UTC (08/06) | Valeur précédente (13:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | **$92.955** | $93.60 | **-0.69%** |
| Open | **$97.00** | $103.33 | **Révision** (open intraday réel) |
| High intraday | **$97.00** | $104.49 | **-7.2%** (high intraday partiel) |
| Low intraday | **$91.91** | $90.905 | **+1.1%** |
| Volume séance | **7.71M** | 23.90M | **Volume intraday partiel** (0.29× moy. 20j) |
| RSI 14j | **52.75** | 54.36 | **-1.61 pt — consolidation neutre** |
| ATR 14j | **12.97** | 13.19 | **-1.7%** |
| MM 50j | **$88.52** | $88.42 | **+0.1%** |
| Distance MM50j | **+5.0%** | +5.9% | Stable |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **-30.5%** | -30.1% | Éloignement marginal |

**Verdict timing ASTS (proxy) :** 🟡 **CONSOLIDATION POST-CORRECTION — VOLUME FAIBLE, SUPPORT MM50 INTACT** — La séance du 08/06 se poursuit avec une légère baisse supplémentaire (-0.69%) pour clôturer à **$92.955** en données snapshot 17h. Le low à **$91.91** reste supérieur au low du snapshot 13h ($90.905), ce qui suggère un soutien à la baisse. Le RSI à **52.75** consolide dans la zone neutre favorable (50–60). Le cours reste au-dessus de la MM50j (**$88.52**, +5.0%). Le volume intraday à **7.71M (0.29×)** est très faible, suggérant un manque de conviction vendeuse après la correction majeure de -12.76% en début de séance. La résistance immédiate est repositionnée à la zone **$97.00** (high intraday) ; un franchissement au-dessus réactiverait le biais haussier. La MM50j à **$88.52** reste le support technique majeur à court terme.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 17:00 UTC (08/06) | Valeur précédente | Δ |
|---------|--------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 17:00 UTC (08/06) | Valeur précédente (13:00 UTC) | Δ |
|---------|--------------------------|-------------------------------|---|
| Market cap | **$36.08B** | $36.33B | **-0.7%** (baisse mécanique) |
| Forward P/E | **-452.997** | -456.14 | **Amélioration mécanique** (+3.14 pts) |
| EV/Revenue | **335.6×** | 335.6× | Stable |
| EV/EBITDA | **-90.096** | -90.10 | Stable |
| Beta | **2.634** | 2.634 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision |
| Premium vs consensus | **-1.7%** | -1.0% | Légère dégradation mécanique |
| Price to book | **13.34** | 13.43 | **-0.7%** |
| Sector | Technology | Technology | Stable |
| Industry | Communication Equipment | Communication Equipment | Stable |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Aucune révision sell-side n'a été enregistrée malgré la correction. Le retour du cours sous le consensus analystes ($92.955 vs $94.54, premium **-1.7%**) confirme la normalisation du premium. Cependant, les multiples restent extrêmement élevés (EV/Revenue 335.6×, forward P/E -452.997), confirmant le caractère spéculatif du titre.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS — STABLE :**
  - Max pain **$120.0** dans `data/latest.json` (snapshot 17h UTC) — inchangé vs 13h
  - Put/call ratio **0.7** — inchangé, **🟢 SIGNAL HAUSSIER**
  - Call OI **59.0%** — inchangé, **🟢 MAJORITÉ CALLS**
  - Échéance prochaine : **2026-06-12** (dans 4 jours)
  - **Interprétation :** le positionnement options reste nettement haussier (put/call 0.7, call OI 59.0%) malgré la correction de -0.69% supplémentaire. Le max pain à **$120.0** (+29.1% au-dessus du cours) constitue un aimant gamma distant. L'échéance 2026-06-12 dans 4 jours maintient un risque gamma significatif : si le cours se rapproche de $100, la pression de réachet gamma par les dealers pourrait amplifier les mouvements.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $92.955 = **-1.7% sous le consensus** (normalisation vs +25.0% précédemment). Publishers FMP : TheFly + StreetInsider.
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant, geo, accounting (inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable. ASTS price_change_pct enregistré à **-0.69%**
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-08** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 25/05, **15+ jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 63`) via yfinance, estimations EPS $-0.29 à $-0.17, Revenues $0.0B
- **Sector rotation :** signal **NEUTRAL** maintenu. XLK reste top1 sector (momentum 10.0). ASTS (Technology) sousperforme le secteur en séance (-0.69% vs séance précédente) — consolidation idiosyncratique.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 17:00 UTC (08/06) | Pondération | Note |
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

| Axe | Score 17:00 UTC (08/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 5.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais aucun catalyseur court terme vérifiable |
| Valorisation | 4.0/10 | 40% | EV/Revenue 335.6×, forward P/E -452.997 — reste spéculatif malgré la normalisation du premium consensus |
| Momentum | 7.0/10 | 25% | Correction consolidée, RSI 52.75 (neutre favorable), cours au-dessus MM50j, options haussières (P/C 0.7, call OI 59%) |
| **Score Opportunité** | **5.1/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **51.0/100** | — | ATTENDRE |
| **Score Global Ajusté** | **56.0/100** | — | **ATTENDRE** |

**Action recommandée par l'agent :** ATTENDRE
**Timing :** Favorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. L'**upgrade de 48.5/100 (ATTENDRE) à 51.0/100 (ATTENDRE)** reflète : (1) la **consolidation technique** (RSI 52.75 vs 54.36, maintien au-dessus MM50j), (2) la **stabilité du positionnement options haussier** (P/C 0.7, call OI 59.0%), et (3) le **volume faible** suggérant un épuisement vendeur. Cependant, le score Opportunité reste sous le seuil d'achat (5.1/10 < 6.0/10) et la valorisation demeure spéculative (EV/Revenue 335.6×, forward P/E -452.997). L'action reste classée **ATTENDRE**.

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
| Prix entrée | Cours close | $92.955 |
| Stop-loss | $92.955 − 2×12.97 | **$67.02** |
| Take-profit | $92.955 + 3×12.97 | **$131.87** |
| Ratio R/R | (131.87−92.955)/(92.955−67.02) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour quantifier la volatilité du proxy. Le support immédiat est désormais la **MM50j à $88.52** ; une cassure ouvrirait la voie vers la zone **$80–85** puis le low intraday à **$91.91**. La résistance immédiate est la zone **$97.00** (high intraday du snapshot 17h). Un franchissement durable au-dessus de **$97.00** réactiverait le biais haussier. L'échéance options 2026-06-12 (dans 4 jours) avec max pain $120.0 (+29.1% du cours) maintient un risque gamma à surveiller : le positionnement haussier (P/C 0.7, call OI 59%) pourrait générer une pression de réachet si le cours remonte vers $97–100.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>32 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **CONFIRMÉE — CONSOLIDATION POST-CORRECTION, RESTE ATTENDRE**

1. **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **>32 snapshots consécutifs** (18/05 → 08/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Consolidation post-correction sur ASTS :** le cours a légèrement reculé de **-0.69%** supplémentaires pour clôturer à **$92.955** en snapshot 17h, avec un low à **$91.91** (supérieur au low 13h de $90.905). Le snapshot 17h confirme une **consolidation** après la correction majeure de -12.76% en début de séance.
3. **Volume intraday très faible :** le volume à **7.71M (0.29×)** est nettement sous la moyenne 20j (26.75M), suggérant un **manque de conviction vendeuse** après la correction. C'est un signal de stabilisation potentiel, à confirmer sur les prochaines séances.
4. **RSI consolidé en zone neutre favorable :** le RSI à **52.75** (vs 54.36 à 13h) reste dans la zone 50–60, confirmant la sortie du surachat et l'absence de survente. Cette zone est favorable à un rebond technique si un catalyseur apparaît.
5. **Maintien au-dessus de la MM50j :** le cours à $92.955 reste à **+5.0%** de la MM50j ($88.52). Tant que ce support tient, la tendance haussière de moyen terme n'est pas invalidée.
6. **Positionnement options haussier stable :** le put/call ratio à **0.7** et le call OI à **59.0%** sont inchangés vs 13h, confirmant que les acheteurs d'options anticipent un rebond. Le max pain à **$120.0** (+29.1%) reste un aimant gamma distant mais actif à 4 jours de l'échéance (2026-06-12).
7. **Agent a upgradé ASTS (+2.5 pts) :** l'agent a révisé ASTS à **51.0/100 (ATTENDRE)** avec un timing **Favorable**. Cependant, le score Opportunité (5.1/10) reste sous le seuil d'achat (6.0/10). La valorisation spéculative (EV/Revenue 335.6×, forward P/E -452.997) et l'absence de catalyseur court terme justifient le maintien en ATTENDRE.
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-08** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (15+ jours de décalage non résolu).
9. **Validation report >2 errors :** le rapport de validation compte **5 erreurs** (AST, AXA, QTBS, ASTSPACE, VRT schema). Aucune [CRITICAL] n'est déclarée. AST est en erreur connue. [DONNÉES PARTIELLES] noté pour le système global, sans impact direct sur l'analyse ASTS.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$88.52** (MM50j) — support technique majeur. Une cassure ouvrirait la voie vers $80–85. À la hausse, le franchissement de **$97.00** (high intraday) serait le premier signal technique positif. Le timing est requalifié **Favorable** mais le score Opportunité (5.1/10) reste insuffisant pour une entrée. La thèse sur ASTS reste **ATTENDRE**.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 17:00 UTC, fetched_at 2026-06-08T17:00:02.161195+00:00), data/recommandations_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/validation_report.txt — aucune donnée hallucinée.*
