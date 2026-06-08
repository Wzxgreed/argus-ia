# AST — Mise à jour Quotidienne

> **Date :** 2026-06-08
> **Type :** Close officiel 21h UTC
> **Source :** data/latest.json (fetched_at 2026-06-08T21:00:01 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/validation_report.txt

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-08_update.md` (snapshot 17:00 UTC)

| Élément | 17:00 UTC | 21:00 UTC (close) | Changement |
|---------|-----------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >33 snapshots consécutifs** |
| Cours ASTS (proxy) | **$92.955** | **$92.06** | **-0.97%** vs 17h, **−1.65% séance** |
| Open ASTS | $97.00 | **$97.13** | Légère révision à la hausse |
| High intraday ASTS | $97.00 | **$97.00** | Stable (high intraday confirmé) |
| Low intraday ASTS | $91.91 | **$90.81** | **-1.2%** (retour sous le low 17h, mais au-dessus du low 13h $90.905) |
| Volume ASTS | 7.71M | **13.55M** | **Volume final révisé à la hausse** (0.50× moy. 20j vs 0.29× à 17h) |
| RSI ASTS | 52.75 | **52.33** | **-0.42 pt** — consolidation neutre |
| ATR ASTS | 12.97 | **13.05** | **+0.6%** (volatilité stable) |
| MM 50j ASTS | $88.52 | **$88.50** | Stable — support dynamique |
| Distance MM50j ASTS | +5.0% | **+4.0%** | Réduction mécanique (cours plus bas) |
| Short interest ASTS | 17.60% | **17.60%** | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision sell-side |
| Premium vs consensus ASTS | -1.7% | **-2.6%** | Normalisation mécanique consolidée |
| Score ASTS (agent) | 51.0/100 (ATTENDRE) | **51.0/100 (ATTENDRE)** | Inchangé |
| Score AST (agent) | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | Placeholder stable |
| Options ASTS | max pain $120.0, P/C 0.7, call OI 59.0% | **Identique** | Stable |
| Échéance options ASTS | 2026-06-12 | **2026-06-12** | Dans 4 jours (inchangé) |
| Earnings FMP AST | 2026-06-08 (days_until: 0) | **2026-06-08 (days_until: 0)** | Placeholder glissant J=0 persistant — 15+ jours |
| Earnings ASTS (yfinance) | 2026-08-10 (63j) | **2026-08-10 (63j)** | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | NEUTRAL | **NEUTRAL** | Stable (XLK top1, momentum 10.0) |
| Social sentiment AST/ASTS | 0 mention | 0 mention | Stable |
| FX exposure AST/ASTS | 25% placeholder, neutral | 25% placeholder, neutral | Stable |
| Validation report | 5 errors (>2) | **5 errors (>2)** | [DONNÉES PARTIELLES] — pas de critical, AST en erreur connue |

**Constat :** Le close officiel 21h UTC confirme la **poursuite de la consolidation post-correction** sur ASTS, avec un recul supplémentaire de **−1.65%** en séance pour clôturer à **$92.06**. Le volume final à **13.55M (0.50×)** est plus élevé que le snapshot intraday 17h (7.71M), suggérant des transactions en fin de séance (possiblement des ajustements de positions avant l'échéance options du 12/06). Le RSI consolide à **52.33** (zone neutre favorable). L'anomalie structurelle sur AST persiste (>33 snapshots sans données). L'agent maintient ASTS à **51.0/100 (ATTENDRE)** — le score Opportunité (5.1/10) reste sous le seuil d'achat.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 21:00 UTC (08/06) | Valeur précédente (17:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur **>33 snapshots consécutifs** (18/05 → 08/06). L'earnings FMP placeholder glissant au **2026-06-08** (`days_until: 0`, 15+ jours de glissement) n'a pas produit de résultats intégrés au pipeline.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 21:00 UTC (08/06) | Valeur précédente (17:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | **$92.06** | $92.955 | **−0.97% vs 17h, −1.65% séance** |
| Open | **$97.13** | $97.00 | **+0.1%** (légère révision) |
| High intraday | **$97.00** | $97.00 | Stable |
| Low intraday | **$90.81** | $91.91 | **-1.2%** (retour sous low 17h) |
| Volume séance | **13.55M** | 7.71M | **Volume final révisé +75.7%** (0.50× moy. 20j) |
| RSI 14j | **52.33** | 52.75 | **-0.42 pt — consolidation neutre** |
| ATR 14j | **13.05** | 12.97 | **+0.6%** |
| MM 50j | **$88.50** | $88.52 | **Stable** |
| Distance MM50j | **+4.0%** | +5.0% | Réduction mécanique |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **-31.2%** | -30.5% | Éloignement marginal |

**Verdict timing ASTS (proxy) :** 🟡 **CONSOLIDATION POST-CORRECTION — VOLUME FINAL RÉVISÉ À LA HAUSSE, SUPPORT MM50 INTACT** — La séance du 08/06 se termine avec une poursuite de la correction (−1.65%) pour clôturer à **$92.06**. Le low à **$90.81** est inférieur au low du snapshot 17h ($91.91) mais supérieur au low du snapshot 13h ($90.905), ce qui maintient une zone de support comprise entre **$90.80–91.00**. Le RSI à **52.33** consolide dans la zone neutre favorable (50–60). Le cours reste au-dessus de la MM50j (**$88.50**, +4.0%). Le volume final à **13.55M (0.50×)** est nettement supérieur au snapshot 17h (7.71M), suggérant des ajustements de positions en fin de séance — probablement liés à l'échéance options **2026-06-12** dans 4 jours. La résistance immédiate reste la zone **$97.00** (high intraday) ; un franchissement au-dessus réactiverait le biais haussier. La MM50j à **$88.50** reste le support technique majeur à court terme. Une cassure ouvrirait la voie vers la zone **$85–88** puis le low intraday à **$90.81**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 21:00 UTC (08/06) | Valeur précédente | Δ |
|---------|--------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 21:00 UTC (08/06) | Valeur précédente (17:00 UTC) | Δ |
|---------|--------------------------|-------------------------------|---|
| Market cap | **$35.73B** | $36.08B | **-1.0%** (baisse mécanique) |
| Forward P/E | **-448.635** | -452.997 | **Amélioration mécanique** (+4.36 pts) |
| EV/Revenue | **335.6×** | 335.6× | Stable |
| EV/EBITDA | **-90.096** | -90.10 | Stable |
| Beta | **2.634** | 2.634 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision |
| Premium vs consensus | **-2.6%** | -1.7% | Normalisation mécanique consolidée |
| Price to book | **13.21** | 13.34 | **-1.0%** |
| Sector | Technology | Technology | Stable |
| Industry | Communication Equipment | Communication Equipment | Stable |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Aucune révision sell-side n'a été enregistrée malgré la poursuite de la correction. Le retour du cours sous le consensus analystes ($92.06 vs $94.54, premium **-2.6%**) confirme la normalisation du premium (vs +25.0% début juin). Cependant, les multiples restent extrêmement élevés (EV/Revenue 335.6×, forward P/E -448.635), confirmant le caractère spéculatif du titre.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS — STABLE :**
  - Max pain **$120.0** dans `data/latest.json` (snapshot 21h UTC) — inchangé vs 17h
  - Put/call ratio **0.7** — inchangé, **🟢 SIGNAL HAUSSIER**
  - Call OI **59.0%** — inchangé, **🟢 MAJORITÉ CALLS**
  - Échéance prochaine : **2026-06-12** (dans 4 jours)
  - **Interprétation :** le positionnement options reste nettement haussier (put/call 0.7, call OI 59.0%) malgré la correction de -1.65% en séance. Le max pain à **$120.0** (+30.3% au-dessus du cours) constitue un aimant gamma distant. L'échéance 2026-06-12 dans 4 jours maintient un risque gamma significatif : si le cours se rapproche de $95–97, la pression de réachet gamma par les dealers pourrait amplifier les mouvements. Le volume final révisé à la hausse (13.55M vs 7.71M à 17h) peut refléter des ajustements de positions options en prévision de l'échéance.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $92.06 = **-2.6% sous le consensus** (normalisation consolidée vs +25.0% précédemment). Publishers FMP : TheFly + StreetInsider.
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant, geo, accounting (inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable. ASTS price_change_pct enregistré à **-1.65%**
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-08** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 25/05, **15+ jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 63`) via yfinance, estimations EPS $-0.29 à $-0.17, Revenues $0.0B
- **Sector rotation :** signal **NEUTRAL** maintenu. XLK reste top1 sector (momentum 10.0). ASTS (Technology) sousperforme le secteur en séance (-1.65% vs séance précédente) — consolidation idiosyncratique.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 21:00 UTC (08/06) | Pondération | Note |
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

| Axe | Score 21:00 UTC (08/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 5.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais aucun catalyseur court terme vérifiable |
| Valorisation | 4.0/10 | 40% | EV/Revenue 335.6×, forward P/E -448.635 — reste spéculatif malgré la normalisation du premium consensus |
| Momentum | 7.0/10 | 25% | Correction consolidée, RSI 52.33 (neutre favorable), cours au-dessus MM50j, options haussières (P/C 0.7, call OI 59%) |
| **Score Opportunité** | **5.1/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **51.0/100** | — | ATTENDRE |
| **Score Global Ajusté** | **56.0/100** | — | **ATTENDRE** |

**Action recommandée par l'agent :** ATTENDRE
**Timing :** Favorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. L'agent maintient **51.0/100 (ATTENDRE)** avec timing **Favorable**. Le score Opportunité (5.1/10) reste sous le seuil d'achat (6.0/10) et la valorisation demeure spéculative (EV/Revenue 335.6×, forward P/E -448.635). L'action reste classée **ATTENDRE**.

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
| Prix entrée | Cours close | $92.06 |
| Stop-loss | $92.06 − 2×13.05 | **$65.96** |
| Take-profit | $92.06 + 3×13.05 | **$131.21** |
| Ratio R/R | (131.21−92.06)/(92.06−65.96) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour quantifier la volatilité du proxy. Le support immédiat est désormais la **MM50j à $88.50** ; une cassure ouvrirait la voie vers la zone **$85–88** puis le low intraday à **$90.81**. La résistance immédiate est la zone **$97.00** (high intraday confirmé). Un franchissement durable au-dessus de **$97.00** réactiverait le biais haussier. L'échéance options 2026-06-12 (dans 4 jours) avec max pain $120.0 (+30.3% du cours) maintient un risque gamma à surveiller : le positionnement haussier (P/C 0.7, call OI 59%) pourrait générer une pression de réachet si le cours remonte vers $95–97.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>33 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **CONFIRMÉE — CONSOLIDATION POST-CORRECTION, RESTE ATTENDRE**

1. **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **>33 snapshots consécutifs** (18/05 → 08/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Poursuite de la consolidation post-correction sur ASTS :** le cours a reculé de **−1.65%** en séance pour clôturer à **$92.06**, avec un low confirmé à **$90.81** (inférieur au low 17h $91.91, mais supérieur au low 13h $90.905). Le close officiel 21h confirme une **consolidation** après la correction majeure de début de séance.
3. **Volume final révisé à la hausse :** le volume à **13.55M (0.50×)** est nettement supérieur au snapshot intraday 17h (7.71M), suggérant des ajustements de positions en fin de séance — probablement liés à l'échéance options 2026-06-12 dans 4 jours. Ce volume reste sous la moyenne 20j (~27.05M), indiquant un manque de conviction directionnelle globale.
4. **RSI consolidé en zone neutre favorable :** le RSI à **52.33** (vs 52.75 à 17h) reste dans la zone 50–60, confirmant la sortie du surachat et l'absence de survente. Cette zone est favorable à un rebond technique si un catalyseur apparaît.
5. **Maintien au-dessus de la MM50j :** le cours à $92.06 reste à **+4.0%** de la MM50j ($88.50). Tant que ce support tient, la tendance haussière de moyen terme n'est pas invalidée. La marge de sécurité s'est toutefois réduite (vs +5.0% à 17h).
6. **Positionnement options haussier stable :** le put/call ratio à **0.7** et le call OI à **59.0%** sont inchangés vs 17h, confirmant que les acheteurs d'options anticipent un rebond. Le max pain à **$120.0** (+30.3%) reste un aimant gamma distant mais actif à 4 jours de l'échéance.
7. **Agent maintient ASTS à 51.0/100 (ATTENDRE) :** l'agent n'a pas révisé le score malgré la poursuite de la baisse. Le timing reste **Favorable** mais le score Opportunité (5.1/10) reste sous le seuil d'achat (6.0/10). La valorisation spéculative (EV/Revenue 335.6×, forward P/E -448.635) et l'absence de catalyseur court terme justifient le maintien en ATTENDRE.
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-08** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (15+ jours de décalage non résolu).
9. **Validation report >2 errors :** le rapport de validation compte **5 erreurs** (AST, AXA, QTBS, ASTSPACE, VRT schema). Aucune [CRITICAL] n'est déclarée. AST est en erreur connue. [DONNÉES PARTIELLES] noté pour le système global, sans impact direct sur l'analyse ASTS.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$88.50** (MM50j) — support technique majeur. Une cassure ouvrirait la voie vers $85–88. À la hausse, le franchissement de **$97.00** (high intraday confirmé) serait le premier signal technique positif. Le timing est requalifié **Favorable** mais le score Opportunité (5.1/10) reste insuffisant pour une entrée. La thèse sur ASTS reste **ATTENDRE**.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 21:00 UTC, fetched_at 2026-06-08T21:00:01.990837+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/validation_report.txt — aucune donnée hallucinée.*
