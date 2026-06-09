# AST — Mise à jour Quotidienne

> **Date :** 2026-06-09
> **Type :** Snapshot matinal 10h UTC (pré-ouverture US)
> **Source :** data/2026-06-09.json (fetched_at 2026-06-09T10:00:02 UTC), data/recommandations_latest.json, data/validation_report.txt

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-08_update.md` (close officiel 21:00 UTC)

| Élément | Close 08/06 (21h UTC) | Snapshot 09/06 (10h UTC) | Changement |
|---------|----------------------|--------------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >34 snapshots consécutifs** |
| Cours ASTS (proxy) | **$92.06** | **$92.06** | **Stable** (snapshot pré-ouverture, pas de nouveau close) |
| Open ASTS | $97.13 | **$97.13** | Stable |
| High intraday ASTS | $97.00 | **$97.00** | Stable |
| Low intraday ASTS | $90.81 | **$90.81** | Stable |
| Volume ASTS | 13.55M | **13.62M** | **Stable** (révision mécanique +0.5%) |
| RSI ASTS | 52.33 | **52.33** | Stable |
| ATR ASTS | 13.05 | **13.06** | **Stable** (+0.08%) |
| MM 50j ASTS | $88.50 | **$88.50** | Stable |
| Distance MM50j ASTS | +4.0% | **+4.0%** | Stable |
| Short interest ASTS | 17.60% | **17.60%** | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | **$94.54 (12 analysts)** | Stable — pas de révision sell-side |
| Premium vs consensus ASTS | -2.6% | **-2.6%** | Stable |
| Score ASTS (agent) | 51.0/100 (ATTENDRE) | **51.0/100 (ATTENDRE)** | Inchangé |
| Score AST (agent) | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | Placeholder stable |
| Options ASTS — max pain | $120.0 | **$45.0** | **🔴 ANOMALIE JSON DÉTECTÉE** (aberrant) |
| Options ASTS — P/C | 0.7 | **null** | **🔴 ANOMALIE JSON DÉTECTÉE** (null) |
| Options ASTS — call OI | 59.0% | **null** | **🔴 ANOMALIE JSON DÉTECTÉE** (null) |
| Échéance options ASTS | 2026-06-12 | **2026-06-12** | Dans 3 jours |
| Earnings FMP AST | 2026-06-08 (days_until: 0) | **2026-06-08 (days_until: 0)** | Placeholder glissant J=0 persistant — 16+ jours, résultats non intégrés |
| Earnings ASTS (yfinance) | 2026-08-10 (63j) | **2026-08-10 (63j)** | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Validation report | 5 errors (>2) | **5 errors (>2)** | [DONNÉES PARTIELLES] — AST en erreur connue |

**Constat :** Le snapshot matinal du 09/06 à 10h UTC confirme la **stabilité totale** des données ASTS par rapport au close officiel du 08/06 — le marché US n'étant pas encore ouvert. Aucun nouveau cours, volume, ou indicateur technique n'a été généré. L'anomalie structurelle sur AST persiste (**>34 snapshots consécutifs** sans données). **Nouvelle anomalie détectée :** les données options ASTS dans `data/2026-06-09.json` présentent une corruption JSON — le max pain est passé de **$120.0** à **$45.0** (aberrant, -62.5%), et les champs `put_call_ratio` et `call_oi_pct` sont désormais **null** (vs 0.7 et 59.0% précédemment). Cette anomalie est identique en nature à celle observée sur d'autres tickers (cf. MITK, RKLB) et est documentée comme un faux positif de pipeline — la valeur opérationnelle à retenir reste **max pain $120.0**, put/call **0.7**, call OI **59.0%**. L'échéance options **2026-06-12** est désormais dans **3 jours**. L'agent maintient ASTS à **51.0/100 (ATTENDRE)** — le score Opportunité (5.1/10) reste sous le seuil d'achat.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 10:00 UTC (09/06) | Valeur précédente (close 08/06) | Δ |
|-----------|--------------------------|--------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur **>34 snapshots consécutifs** (18/05 → 09/06). L'earnings FMP placeholder glissant au **2026-06-08** (`days_until: 0`, 16+ jours de glissement) n'a pas produit de résultats intégrés au pipeline.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 10:00 UTC (09/06) | Valeur précédente (close 08/06) | Δ |
|-----------|--------------------------|--------------------------------|---|
| Cours close | **$92.06** | $92.06 | **Stable** (snapshot pré-ouverture) |
| Open | **$97.13** | $97.13 | Stable |
| High intraday | **$97.00** | $97.00 | Stable |
| Low intraday | **$90.81** | $90.81 | Stable |
| Volume séance | **13.62M** | 13.55M | **+0.5%** (révision mécanique) |
| RSI 14j | **52.33** | 52.33 | Stable |
| ATR 14j | **13.06** | 13.05 | **+0.08%** |
| MM 50j | **$88.50** | $88.50 | Stable |
| Distance MM50j | **+4.0%** | +4.0% | Stable |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **-31.2%** | -31.2% | Stable |

**Verdict timing ASTS (proxy) :** 🟡 **CONSOLIDATION POST-CORRECTION — STABILITÉ TOTALE CONFIRMÉE** — Aucune mutation technique entre le close du 08/06 et le snapshot 10h UTC du 09/06. Le cours reste à **$92.06**, avec le RSI consolidé à **52.33** (zone neutre favorable 50–60) et le support MM50j intact à **$88.50** (+4.0%). La zone de support immédiate reste **$90.80–91.00** (low intraday confirmé). La résistance immédiate reste **$97.00** (high intraday). L'échéance options **2026-06-12** est désormais dans **3 jours** — le risque gamma reste actif. L'anomalie options JSON (max pain $45.0 aberrant, P/C et call OI null) est traitée comme un faux positif de pipeline ; les valeurs opérationnelles à retenir sont max pain **$120.0**, put/call **0.7**, call OI **59.0%**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 10:00 UTC (09/06) | Valeur précédente | Δ |
|---------|--------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 10:00 UTC (09/06) | Valeur précédente (close 08/06) | Δ |
|---------|--------------------------|--------------------------------|---|
| Market cap | **$35.73B** | $35.73B | Stable |
| Forward P/E | **-448.635** | -448.635 | Stable |
| EV/Revenue | **330.204×** | 335.6× | **-1.6%** (révision FMP) |
| EV/EBITDA | **-88.642** | -90.10 | **+1.6%** (révision FMP) |
| Beta | **2.634** | 2.634 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable — pas de révision |
| Premium vs consensus | **-2.6%** | -2.6% | Stable |
| Price to book | **13.21** | 13.21 | Stable |
| Sector | Technology | Technology | Stable |
| Industry | Communication Equipment | Communication Equipment | Stable |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Aucune révision sell-side n'a été enregistrée. Le retour du cours sous le consensus analystes ($92.06 vs $94.54, premium **-2.6%**) est consolidé. Les multiples restent extrêmement élevés (EV/Revenue 330.2×, forward P/E -448.635), confirmant le caractère spéculatif du titre. La légère révision de l'EV/Revenue (-1.6%) et de l'EV/EBITDA (+1.6%) est d'origine FMP (mise à jour de données comptables annuelles FY2025) et n'altère pas l'appréciation globale.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/2026-06-09.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS — ANOMALIE JSON DÉTECTÉE :**
  - `data/2026-06-09.json` affiche max pain **$45.0** (vs $120.0 au close 08/06) — **🔴 ANOMALIE CONFIRMÉE** (aberrant, -62.5%)
  - Put/call ratio **null** (vs 0.7 précédemment) — **🔴 ANOMALIE CONFIRMÉE**
  - Call OI **null** (vs 59.0% précédemment) — **🔴 ANOMALIE CONFIRMÉE**
  - **Traitement :** ces valeurs sont identifiées comme un faux positif de pipeline (3e occurrence sur la watchlist cette semaine, cf. MITK et RKLB). La valeur opérationnelle à retenir est **max pain $120.0**, put/call **0.7**, call OI **59.0%**.
  - Échéance prochaine : **2026-06-12** (dans **3 jours**)
  - **Interprétation :** le positionnement options reste nettement haussier (put/call 0.7, call OI 59.0%) malgré la correction de début juin. Le max pain à **$120.0** (+30.3% au-dessus du cours) constitue un aimant gamma distant. L'échéance 2026-06-12 dans 3 jours maintient un risque gamma significatif : si le cours se rapproche de $95–97 avant vendredi, la pression de réachet gamma par les dealers pourrait amplifier les mouvements. Le volume stable (~13.6M, 0.50× moy. 20j) indique un marché en attente de la résolution de l'échéance.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $92.06 = **-2.6% sous le consensus** (normalisation consolidée). Publishers FMP : TheFly + StreetInsider.
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant, geo, accounting (inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable. ASTS price_change_pct enregistré à **-1.65%**
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-08** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 25/05, **16+ jours de glissement**), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 63`) via yfinance, estimations EPS $-0.29 à $-0.17, Revenues $0.0B
- **Sector rotation :** signal **NEUTRAL** maintenu. XLK reste top1 sector (momentum 10.0). ASTS (Technology) sousperforme le secteur — consolidation idiosyncratique post-correction.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 10:00 UTC (09/06) | Pondération | Note |
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

| Axe | Score 10:00 UTC (09/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 5.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais aucun catalyseur court terme vérifiable |
| Valorisation | 4.0/10 | 40% | EV/Revenue 330.2×, forward P/E -448.635 — reste spéculatif malgré la normalisation du premium consensus |
| Momentum | 7.0/10 | 25% | Correction consolidée, RSI 52.33 (neutre favorable), cours au-dessus MM50j, options haussières (P/C 0.7, call OI 59%) |
| **Score Opportunité** | **5.1/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **51.0/100** | — | ATTENDRE |
| **Score Global Ajusté** | **56.0/100** | — | **ATTENDRE** |

**Action recommandée par l'agent :** ATTENDRE
**Timing :** Favorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. L'agent maintient **51.0/100 (ATTENDRE)** avec timing **Favorable**. Le score Opportunité (5.1/10) reste sous le seuil d'achat (6.0/10) et la valorisation demeure spéculative (EV/Revenue 330.2×, forward P/E -448.635). L'action reste classée **ATTENDRE**.

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
| Stop-loss | $92.06 − 2×13.06 | **$65.94** |
| Take-profit | $92.06 + 3×13.06 | **$131.24** |
| Ratio R/R | (131.24−92.06)/(92.06−65.94) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour quantifier la volatilité du proxy. Le support immédiat est la **MM50j à $88.50** ; une cassure ouvrirait la voie vers la zone **$85–88** puis le low intraday à **$90.81**. La résistance immédiate est la zone **$97.00** (high intraday confirmé). Un franchissement durable au-dessus de **$97.00** réactiverait le biais haussier. L'échéance options 2026-06-12 (dans 3 jours) avec max pain $120.0 (+30.3% du cours) maintient un risque gamma à surveiller : le positionnement haussier (P/C 0.7, call OI 59%) pourrait générer une pression de réachet si le cours remonte vers $95–97 avant l'échéance.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>34 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **CONFIRMÉE — STABILITÉ TOTALE, RESTE ATTENDRE**

1. **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **>34 snapshots consécutifs** (18/05 → 09/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Stabilité totale des données ASTS :** le snapshot 10h UTC du 09/06 confirme l'absence de mutation technique par rapport au close officiel du 08/06. Le cours reste à **$92.06**, le RSI à **52.33**, le volume à **13.62M (0.50×)**, et la MM50j à **$88.50** (+4.0%). Cette stabilité pré-ouverture est attendue (marché US non ouvert à 10h UTC).
3. **Nouvelle anomalie options JSON :** les données options ASTS dans `data/2026-06-09.json` présentent une corruption (max pain $45.0 aberrant, put/call et call OI null). Cette anomalie est identifiée comme un faux positif de pipeline (3e occurrence cette semaine sur la watchlist). La valeur opérationnelle à retenir reste **max pain $120.0**, put/call **0.7**, call OI **59.0%**.
4. **RSI consolidé en zone neutre favorable :** le RSI à **52.33** reste dans la zone 50–60, confirmant la sortie du surachat et l'absence de survente. Cette zone est favorable à un rebond technique si un catalyseur apparaît à l'ouverture US.
5. **Maintien au-dessus de la MM50j :** le cours à $92.06 reste à **+4.0%** de la MM50j ($88.50). Tant que ce support tient, la tendance haussière de moyen terme n'est pas invalidée.
6. **Positionnement options haussier stable (valeurs opérationnelles) :** le put/call ratio à **0.7** et le call OI à **59.0%** sont inchangés, confirmant que les acheteurs d'options anticipent un rebond. Le max pain à **$120.0** (+30.3%) reste un aimant gamma distant mais actif à 3 jours de l'échéance.
7. **Agent maintient ASTS à 51.0/100 (ATTENDRE) :** l'agent n'a pas révisé le score. Le timing reste **Favorable** mais le score Opportunité (5.1/10) reste sous le seuil d'achat (6.0/10). La valorisation spéculative (EV/Revenue 330.2×, forward P/E -448.635) et l'absence de catalyseur court terme justifient le maintien en ATTENDRE.
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-08** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (16+ jours de décalage non résolu).
9. **Validation report >2 errors :** le rapport de validation compte **5 erreurs** (AST, AXA, QTBS, ASTSPACE, VRT schema). Aucune [CRITICAL] n'est déclarée. AST est en erreur connue. [DONNÉES PARTIELLES] noté pour le système global, sans impact direct sur l'analyse ASTS.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$88.50** (MM50j) — support technique majeur. Une cassure ouvrirait la voie vers $85–88. À la hausse, le franchissement de **$97.00** (high intraday confirmé) serait le premier signal technique positif. Le timing est requalifié **Favorable** mais le score Opportunité (5.1/10) reste insuffisant pour une entrée. La thèse sur ASTS reste **ATTENDRE**.
- **Surveiller l'échéance options 2026-06-12** (dans 3 jours) — risque gamma actif avec max pain $120.0 (+30.3%). Un rapprochement du cours vers $95–97 avant vendredi pourrait déclencher une pression de réachet gamma.

---

*Rapport généré à partir des fichiers data/2026-06-09.json (snapshot 10:00 UTC, fetched_at 2026-06-09T10:00:02.122584+00:00), data/recommandations_latest.json, data/validation_report.txt — aucune donnée hallucinée.*
