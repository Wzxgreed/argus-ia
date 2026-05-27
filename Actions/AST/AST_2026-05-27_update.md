# AST — Mise à jour Quotidienne

> **Date :** 2026-05-27
> **Type :** Update finale (snapshot 17:00 UTC)
> **Source :** data/latest.json (17:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-27_update.md` (snapshot 13:00 UTC)

| Élément | Snapshot 13:00 UTC (27/05) | Snapshot 17:00 UTC (27/05) | Changement |
|---------|---------------------------|---------------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — 18e snapshot consécutif** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | Cours **$119.70** (+13.07%) | Cours **$129.335** (+8.05% vs veille) | **+8.05% sur la séance, +21.0% vs close 26/05 ($106.89)** |
| Volume ASTS | 48.08M (2.10× moy. 20j) | **19.72M** (0.85× moy. 20j) | **−59.0% — effondrement du volume en séance** |
| RSI ASTS | 82.58 | **83.14** | **+0.56 pt, surchauffe extrême aggravée** |
| ATR ASTS | 10.14 | **10.41** | **+0.27 pt, volatilité en expansion** |
| MM 50j ASTS | 84.87 | **85.67** | **+0.80 pt, écartement haussier** |
| 52W high ASTS | 129.89 | 129.89 | Close $129.335 = **99.6% du 52W high** |
| Intraday high ASTS | 127.10 | **129.38** | **Nouveau high de séance, à 0.4% du 52W high** |
| Options ASTS | max pain 120.0, P/C 0.76, call OI 57.0% | max pain 120.0, P/C 0.76, call OI 57.0% | **Stable** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable |
| Score ASTS (agent) | 36.0/100 (SURVEILLER) | **29.8/100 (ÉVITER)** | **Downgrade — malus surachat + valorisation** |
| Earnings FMP AST | 2026-05-27 (days_until: 0) | 2026-05-27 (days_until: 0) | **Placeholder glissant J=0 non résolu** |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |

**Constat :** Le snapshot 17:00 UTC confirme la **stabilité totale** de l'absence de données de marché pour AST (18e snapshot consécutif sans historique de prix). En revanche, **ASTS évolue fortement** : le cours bondit de **$119.70 à $129.335 (+8.05%)** sur une séance où le volume s'est **effondré à 19.72M (0.85× moyenne 20j)** contre 48.08M (2.10×) au snapshot 13:00 UTC. Ce rallye de l'après-midi sur volume décroissant est un signal technique majeur : il suggère soit un **short squeeze/gamma squeeze** (appel de marge sur les 18.14% de short interest), soit une **absorption institutionnelle** sur faible participation. Le close à **99.6% du 52W high** ($129.89) et le high intraday à **$129.38** (à 0.4% du record) indiquent une pression haussière extrême. L'agent a downgradé ASTS de **SURVEILLER (36.0) à ÉVITER (29.8)** en raison de la surchauffe technique (RSI 83.14) et de la valorisation désormais **+40.2% au-dessus du consensus** ($92.25).

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur snapshot 17:00 UTC (27/05) | Valeur précédente (13:00 UTC 27/05) | Δ |
|-----------|--------------------------------|-----------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur snapshot 17:00 UTC (27/05) | Valeur précédente (13:00 UTC 27/05) | Δ |
|-----------|----------------------------------|-----------------------------------|---|
| Cours close | **$129.335** | $119.70 | **+8.05%** |
| Volume | **19.72M** | 48.08M | **−59.0%** |
| Volume relatif | **0.85× moy. 20j** | 2.10× | **Retour sous moyenne** |
| RSI 14j | **83.14** | 82.58 | **+0.56 pt** |
| ATR 14j | **10.41** | 10.14 | **+0.27 pt** |
| MM 50j | **85.67** | 84.87 | **+0.80 pt** |
| 52W high | 129.89 | 129.89 | Close = **99.6%** du 52W high |
| Intraday high | **129.38** | 127.10 | **Nouveau high, à 0.4% du 52W** |
| Distance MM50j | **+50.9%** | +41.0% | Écartement haussier en accélération |

**Verdict timing ASTS (proxy) :** 🔴 **SURCHAUFFE EXTRÊME + RISQUE DE CLIMATIC BUYING** — RSI 83.14 (>80), close à 99.6% du 52W high, rallye de l'après-midi sur volume en chute libre (−59% vs snapshot 13h). La configuration ressemble à un **gamma squeeze** (call OI 57.0%, max pain $120, close $129.335 bien au-dessus) ou à un **short squeeze** (short interest 18.14%). Le risque de correction brutale est élevé si le 52W high ($129.89) résiste ou si le volume ne confirme pas la rupture.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur snapshot 17:00 UTC (27/05) | Valeur précédente | Δ |
|---------|----------------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur snapshot 17:00 UTC (27/05) | Valeur précédente (13:00 UTC) | Δ |
|---------|----------------------------------|------------------------------|---|
| Market cap | **$50.22B** | $46.46B | **+8.1%** |
| Forward P/E | **−435.43** | −402.85 | **Détérioration** |
| EV/Revenue | **427.42×** | 427.42× | Stable |
| EV/EBITDA | **−114.74** | −114.74 | Stable |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | 18.14% | 18.14% | Stable |
| Consensus PT | $92.25 (10 analystes) | $92.25 (10 analystes) | Stable |
| Premium vs consensus | **+40.2%** | +29.8% | **+10.4 pts** |

Pas de fondamentaux attractifs — valorisation purement spéculative sur la technologie satellite direct-to-device (D2D). Le consensus analystes ($92.25) est désormais **+40.2% sous le close** ($129.335), confirmant une surchauffe de valorisation rare. Le forward P/E s'est encore détérioré (−435.43), reflétant l'absence de visibilité bénéficiaire à court terme.

---

## 4. Mise à jour sentiment / options / news

- **News AST :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-05-27.json`
- **News ASTS :** aucune entrée Yahoo Finance ni FMP — mais le volume matinal ×2 et le rallye post-Memorial Day suggèrent fortement une news non capturée par le pipeline (probablement liée à l'earnings programmé sous le ticker erroné AST, ou à un contrat/annonce technique sur le D2D satellite)
- **Options ASTS :** max pain **120.0**, put/call ratio **0.76**, call OI **57.0%** — inchangés vs 13:00 UTC. Configuration bullish confirmée : le close $129.335 est **+7.8% au-dessus du max pain** ($120), ce qui crée une pression de gamma squeeze potentielle sur les calls ITM/ATM. Le call wall à 120 est largement dépassé.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 10 analystes, price target moyen $92.25 — cours actuel $129.335 = **+40.2% au-dessus du consensus**, signal de surchauffe extrême
- **Quant :** pas de signaux historiques pour AST — p-value insuffisante
- **Geo / Accounting / Sector / Events :** aucune donnée spécifique pour AST
- **FX exposure AST/ASTS :** exposition 25% (placeholder), direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-05-27** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 26/05), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 75`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 2026-05-27 (17:00 UTC) | Pondération | Note |
|-----|-----------------------------|-------------|------|
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

| Axe | Score 2026-05-27 (17:00 UTC) | Pondération | Note |
|-----|-----------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur potentiel (news non capturée) mais non vérifiable |
| Valorisation | 2.5/10 | 40% | EV/Revenue 427×, forward P/E −435.43, consensus +40.2% sous cours |
| Momentum | 5.5/10 | 25% | Gap haussier +8.05%, mais volume −59% = divergence baissière |
| **Score Opportunité** | **3.8/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **38.0/100** | — | ÉVITER |
| **Score Global Ajusté** | **29.8/100** | — | **ÉVITER** |

**Action recommandée par l'agent :** ÉVITER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le downgrade de SURVEILLER (36.0) à ÉVITER (29.8)** reflète l'aggravation de la surchauffe (RSI 83.14, premium consensus +40.2%) et la divergence volume/prix (rallye sur volume en chute libre).

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
| Prix entrée | Cours close | $129.335 |
| Stop-loss | $129.335 − 2×10.41 | **$108.52** |
| Take-profit | $129.335 + 3×10.41 | **$160.56** |
| Ratio R/R | (160.56−129.335)/(129.335−108.52) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL a glissé de $99.42 (13h) à $108.52 (17h)** en raison de l'expansion de l'ATR (10.14 → 10.41) et du nouveau close plus élevé.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — AGGRAVATION DU RISQUE SUR LE PROXY ASTS**

AST n'est pas évaluable en l'état. La situation pour AST est strictement inchangée depuis le snapshot 13:00 UTC du 27/05 :

1. **Anomalie structurelle confirmée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). ASTS affiche un cours de **$129.335** (+8.05% sur la séance, +21.0% vs close 26/05) avec un volume après-midi de **19.72M** (0.85× moyenne) contre 48.08M (2.10×) le matin. Ce pattern **rallye sur volume décroissant** est typique d'un gamma squeeze ou d'un short squeeze (short interest 18.14%).
2. **52W high en ligne de mire :** le high intraday à **$129.38** est à **0.4% du 52W high** ($129.89). Le close $129.335 est à **99.6% du record**. Toute résistance psychologique à $130 pourrait déclencher soit une rupture parabolique, soit un rejet violent.
3. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le 2026-05-27 (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le gap de +21% sur ASTS en 2 jours suggère que ce catalyseur a affecté ASTS.
4. **Downgrade agent ASTS :** le score est passé de **36.0/100 (SURVEILLER)** à **29.8/100 (ÉVITER)**, confirmant que la surchauffe technique et la valorisation hors norme (consensus +40.2% sous cours) rendent le ticker inappropriprié à l'entrée.
5. **Qualité des données :** AST fait partie des 3 tickers KO sur 26 requêtés (`tickers_ko: 3`), aux côtés d'AXA et QTBS. AST est absent du quality gate (alors qu'ASTS y figure comme `excluded` pour stale_price_history — ce qui prouve que le système reçoit au moins un historique pour ASTS, contrairement à AST).

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel pullback technique post-squeeze. Le niveau $120 (max pain + support psychologique) est la zone de repli naturelle. Une cassure sous $125 sur volume pourrait signaler le début de la correction.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 17:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
