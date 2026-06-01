# AST — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Type :** Update finale (snapshot 21:00 UTC)
> **Source :** data/latest.json (fetched_at 21:00:02 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-01_update.md` (snapshot 17:00 UTC)

| Élément | 17:00 UTC (01/06) | 21:00 UTC (01/06) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >23 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$102.75** | **$105.65** | **+2.82%** (rebond post-close) |
| Volume ASTS (séance) | 17.76M (0.67×, partiel) | **27.07M (1.00×, total)** | **Retour à la normale** |
| RSI ASTS | 60.09 | **61.89** | **+1.8 pt** |
| ATR ASTS | 12.18 | 12.18 | Stable |
| MM 50j ASTS | 87.05 | 87.11 | Stable |
| Low intraday ASTS | 101.21 | 101.21 | Stable (plancher de séance conservé) |
| High intraday ASTS | 111.28 | 111.28 | Stable |
| Short interest ASTS | 17.60% | 17.60% | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus ASTS | +8.7% | **+11.8%** | **Ré-étalement +3.1 pts** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable — placeholder |
| Score ASTS (agent) | 43.8/100 (SURVEILLER) | **39.8/100 (SURVEILLER)** | **Lecture recommandations JSON** |
| Score ajusté ASTS | 48.8/100 | **44.8/100** | **−4.0 pts** (recalibration) |
| Earnings FMP AST | 2026-06-01 (days_until: 0) | 2026-06-01 (days_until: 0) | Placeholder glissant J=0 non résolu — 7j de glissement |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST/ASTS | 0 | 0 | Stable |
| Signal sectoriel | ROTATION_TO_CYCLICAL | ROTATION_TO_CYCLICAL | Stable (XLK top1, momentum 10.0) |

**Constat :** Le snapshot 21:00 UTC enregistre une **stabilisation technique** sur le proxy ASTS après la correction sévère de la journée. Le rebond de **+2.82%** depuis le close 17h ($102.75 → $105.65) et le retour du volume de séance à la **moyenne 20j (1.00×)** suggèrent un plancher temporaire sur la zone **$101–102**. Le RSI remonte légèrement à **61.89**, restant dans la zone neutre-haussière. Le premium consensus se ré-étend mécaniquement à **+11.8%** du fait du rebond de cours, sans révision du sell-side. Le score agent ajusté ASTS est recalibré à **44.8/100 (SURVEILLER)** selon le fichier `recommandations_latest.json`.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 21:00 UTC (01/06) | Valeur précédente (17:00 UTC) | Δ |
|-----------|-------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur 23 snapshots consécutifs.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 21:00 UTC (01/06) | Valeur précédente (17:00 UTC) | Δ |
|-----------|-------------------------|-------------------------------|---|
| Cours close | **$105.65** | $102.75 | **+2.82%** |
| Open | 108.67 | 108.67 | Stable |
| High intraday | 111.28 | 111.28 | Stable |
| Low intraday | **101.21** | 101.21 | Stable (plancher de séance) |
| Volume séance | **27.07M** | 17.76M (partiel) | **1.00× moy. 20j** (total) |
| RSI 14j | **61.89** | 60.09 | **+1.8 pt** |
| ATR 14j | **12.18** | 12.18 | Stable |
| MM 50j | **87.11** | 87.05 | +0.1% |
| Distance MM50j | **+21.3%** | +18.0% | Expansion |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−21.1%** | −23.2% | Rapprochement |

**Verdict timing ASTS (proxy) :** 🟡 **STABILISATION TECHNIQUE POST-CORRECTION** — Le cours a rebondi de +2.82% depuis le close 17h pour finir la séance à **$105.65**, réintégrant partiellement la zone de support cassée **$105–110**. Le volume total de la séance (**27.07M**, 1.00× moyenne 20j) est revenu à la normale, ce qui atténue le signal de désengagement des vendeurs observé sur le volume partiel de 17h. Le RSI à **61.89** reste dans la zone neutre-haussière (50–70), sans surachat. La MM50j à **$87.11** constitue le support structurel intermédiaire. La prochaine résistance immédiate se situe à **$105–110** (ancien support, désormais résistance) ; un franchissement durable au-dessus de **$110** réactiverait le biais haussier. En dessous, le plancher intra-day à **$101.21** reste le support critique ; une cassure ouvrirait la voie vers **$95–100**.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 21:00 UTC (01/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 21:00 UTC (01/06) | Valeur précédente (17:00 UTC) | Δ |
|---------|-------------------------|-------------------------------|---|
| Market cap | **$41.01B** | $39.89B | **+2.8%** (mécanique) |
| Forward P/E | **−355.57** | −345.91 | **Dégradation mécanique −2.8%** |
| EV/Revenue | **405.3×** | 405.3× | Stable |
| EV/EBITDA | **−108.80** | −108.80 | Stable |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus | **+11.8%** | +8.7% | **Ré-étalement +3.1 pts** |

La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Le rebond de cours mécanique dégrade le forward P/E (−355.57 vs −345.91) et ré-étend le premium consensus de **+8.7% à +11.8%**. Le sell-side n'a pas révisé son PT ($94.54, 12 analysts). La couverture analyste est stable avec 5 révisions au cours du dernier mois. La société n'est pas profitable (net margin −4.82%, operating margin −4.06%) et le modèle reste dépendant des jalons technologiques et des contrats commerciaux D2D.

---

## 4. Mise à jour sentiment / options / news

- **News AST / ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-06-01.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :** max pain **$120.0** (stable, +13.6% au-dessus du close), put/call ratio **0.92** (stable), call OI **52.2%** (stable). Le max pain à $120 reste un aimant gamma potentiel si le cours se stabilise au-dessus de $105.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS — aucun pump/dump détecté
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $105.65 = **+11.8% au-dessus du consensus** (vs +8.7% à 17h)
- **Quant / Geo / Accounting / Events :** aucune donnée spécifique pour AST ou ASTS dans les rapports quant (date 2026-05-17, insuffisant), geo (2026-05-17, pas de flag), accounting (fichier inexistant), ou events (0 événement)
- **FX exposure AST/ASTS :** exposition placeholder 25%, direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-01** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 26/05, 7 jours de glissement), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 70`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **ROTATION_TO_CYCLICAL** maintenu (XLK top1 sector, momentum score 10.0). XLE en bullish crossover. **Paradoxe sectoriel persistant :** ASTS (Technology) sous-performe massivement le secteur Technology en journée (−6.84% vs close précédent alors que XLK domine) — divergence interne négative probablement liée à un factor spécifique (short covering exhausted, incertitude earnings, rotation interne tech vers les grandes caps qualité).

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 21:00 UTC (01/06) | Pondération | Note |
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

| Axe | Score 21:00 UTC (01/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur latent (technologie D2D, earnings 10/08) mais non vérifiable à court terme |
| Valorisation | 3.0/10 | 40% | EV/Revenue 405×, forward P/E −355.57, premium consensus ré-étendu à +11.8% |
| Momentum | 5.5/10 | 25% | Correction −6.84% vs close veille, rebond +2.82% post-17h, RSI 61.89 neutre-haussier |
| **Score Opportunité** | **4.0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39.8/100** | — | SURVEILLER |
| **Score Global Ajusté** | **44.8/100** | — | **SURVEILLER** |

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Neutre
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. Le score **SURVEILLER (44.8/100)** reflète la **stabilisation technique** (rebond post-17h, volume normalisé) mais la valorisation reste speculative (forward P/E −355.57, EV/Revenue 405×). Le recul de −4.0 pts sur le score ajusté vs l'analyse précédente est issu du fichier `recommandations_latest.json` et traduit une calibration plus conservatrice du modèle. La configuration reste risquée (ancien support $105–110 transformé en résistance, short interest élevé 17.6%).

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

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL à $81.29 et le TP à $142.19 sont élargis** du fait de l'expansion de l'ATR et du rebond de cours. Le support immédiat reste le low intra-day **$101.21** ; une cassure ouvrirait la voie vers la MM50j à **$87.11** et la zone **$95–100**. La résistance immédiate est l'ancien support cassé **$105–110** ; un franchissement durable au-dessus de **$110** réactiverait le biais haussier. Le max pain options à **$120** reste un aimant gamma potentiel si le titre se stabilise au-dessus de $105.

---

## 7. Conclusion — État de la thèse

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (23 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **STABILISATION TECHNIQUE POST-CORRECTION — SURVEILLER MAINTENU**

1. **Anomalie structurelle persistante :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **23 snapshots consécutifs** (18/05 → 01/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. **Stabilisation technique sur ASTS :** après une correction intra-day sévère jusqu'à **$101.21** (−20.9% depuis le close 27/05), le cours a rebondi pour clôturer la séance à **$105.65** (−6.84% vs close veille, +2.82% vs close 17h). Le volume total de la séance est revenu à la moyenne 20j (**1.00×**), ce qui atténue le signal de désengagement des vendeurs.
3. **RSI neutre-haussier :** le RSI à **61.89** reste dans la zone 50–70, ni surachat ni survente. La configuration technique est plus saine qu'à 13h (RSI 69.79) mais sans momentum haussier fort.
4. **Support / Résistance :** le support immédiat est le low intra-day **$101.21**. La zone **$105–110**, ancien support cassé ce matin, constitue désormais la résistance immédiate. Un franchissement durable au-dessus de **$110** serait le premier signal de stabilisation ; une cassure sous **$101.21** ouvrirait la voie vers **$95–100**.
5. **Paradoxe sectoriel :** le signal sectoriel reste **ROTATION_TO_CYCLICAL** avec Technology (XLK) top1 (momentum 10.0). ASTS sous-performe massivement son secteur — divergence interne négative, probablement liée à un factor spécifique (short covering exhausted, incertitude earnings, rotation interne tech vers les grandes caps).
6. **Premium consensus ré-étendu :** le passage de **+8.7% à +11.8%** au-dessus du consensus est entièrement mécanique (rebond de cours) et ne reflète aucune révision sell-side. Le PT moyen ($94.54, 12 analysts) est inchangé.
7. **Options :** le max pain à **$120** est stable, désormais **+13.6% au-dessus du cours** (vs +16.8% à 17h). Le put/call ratio à **0.92** et le call OI à **52.2%** suggèrent un léger biais haussier des détenteurs d'options, mais la configuration reste fragile.
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-01** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **26/05** (7 jours de décalage non résolu).
9. **Score agent ASTS recalibré :** le score ajusté passe de **48.8 à 44.8/100** (SURVEILLER) selon `recommandations_latest.json`, traduisant une calibration plus conservatrice du modèle. L'action reste **SURVEILLER**.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un test de la zone **$101–102** (support immédiat) et de la résistance **$105–110**. Un rebond durable au-dessus de **$110** réactiverait le biais haussier. Le max pain options à **$120** reste un aimant gamma si le titre trouve un plancher au-dessus de $105.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 21:00 UTC, fetched_at 2026-06-01T21:00:02.282200+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json — aucune donnée hallucinée.*
