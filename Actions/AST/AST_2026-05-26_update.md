# AST — Mise à jour Quotidienne

> **Date :** 2026-05-26
> **Type :** Update après-midi (snapshot 17:00 UTC)
> **Source :** data/latest.json (17:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-26_update.md` (snapshot 13:00 UTC)

| Élément | Snapshot 13:00 UTC | Snapshot 17:00 UTC | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (doublon probable) | Cours $105.86 (+10.01%) | Cours **$125.96** (+18.99%) | **+20.10 pts Δ, gap haussier massif** |
| Volume ASTS | 30.6M | 29.56M | Stable (1.35× moyenne 20j) |
| RSI ASTS | 74.5 | **83.77** | **+9.27 pts, surchauffe extrême** |
| 52W high ASTS | — | 127.10 (intraday) vs 129.89 (52W) | Proche du 52W high |
| Options ASTS | max pain 120, P/C 0.78, call OI 56.2% | max pain 120, P/C 0.78, call OI 56.2% | Stable |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable |
| Earnings FMP AST | 2026-05-26 (days_until: 0) | 2026-05-26 (days_until: 0) | Confirmé |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |

**Constat :** Le snapshot 17:00 UTC confirme la **stabilité totale** de l'absence de données de marché pour AST. C'est le **14e snapshot consécutif** (18/05 → 26/05) sans historique de prix. En revanche, **ASTS confirme massivement le doublon** avec une explosion de +18.99% à $125.96 (RSI 83.77, volume 29.56M), suggérant que le marché réagit fortement à un catalyseur sur AST SpaceMobile que le système ne capte pas sous le ticker erroné AST.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur snapshot 17:00 UTC | Valeur précédente (13:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur snapshot 17:00 UTC | Valeur précédente (13:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | **$125.96** | $105.86 | **+18.99%** |
| Volume | 29.56M | 30.6M | −3.4% |
| Volume relatif | 1.35× moy. 20j | 1.39× | Stable, au-dessus de la moyenne |
| RSI 14j | **83.77** | 74.5 | **+9.27 pts** |
| ATR 14j | 10.14 | — | — |
| MM 50j | 84.99 | — | — |
| 52W high | 129.89 | — | Intraday 127.10 = 97.8% du 52W high |

**Verdict timing ASTS (proxy) :** 🔴 **SURCHAUFFE EXTRÊME** — RSI 83.77 (>80), gap haussier +18.99% en une séance, proche du 52W high ($129.89). Call wall à 120, max pain 120. Momentum haussier mais risque de pullback technique élevé.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur snapshot 17:00 UTC | Valeur précédente | Δ |
|---------|--------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur snapshot 17:00 UTC |
|---------|--------------------------|
| Market cap | $48.9B |
| Forward P/E | −423.92 |
| EV/Revenue | 378.74× |
| EV/EBITDA | −101.67 |
| Beta | 2.598 |
| Short interest | 18.14% |

Pas de fondamentaux attractifs — valorisation purement spéculative sur la technologie satellite direct-to-device (D2D).

---

## 4. Mise à jour sentiment / options / news

- **News AST :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json`
- **News ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` — mais le mouvement de +18.99% suggère fortement une news non capturée par le pipeline (probablement liée à l'earnings programmé ce jour sous le ticker AST, ou à un contrat/annonce technique sur le D2D satellite)
- **Options ASTS :** max pain 120.0, put/call ratio 0.78, call OI 56.2% — configuration bullish, call wall à 120
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 10 analystes, price target moyen $92.25 — cours actuel $125.96 = **+36.6% au-dessus du consensus**, signal de surchauffe
- **Quant :** pas de signaux historiques pour AST — p-value insuffisante
- **Geo / Accounting / Sector / FX / Events :** aucune donnée spécifique pour AST
- **Upcoming events :**
  - AST : earnings signalé le **2026-05-26** (`days_until: 0`) via FMP — résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 76`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 2026-05-26 (17:00 UTC) | Pondération | Note |
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

Score Opportunité estimé ~5.5/10 — catalyseur potentiellement fort (si lié à news satellite) mais valorisation abyssale (EV/Revenue 378×, forward P/E −423.92) et surchauffe technique extrême (RSI 83.77). Cours +36.6% au-dessus du consensus analystes. Action : **ÉVITER** à ces niveaux.

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
| Prix entrée | Cours close | $125.96 |
| Stop-loss | $125.96 − 2×10.14 | **$105.68** |
| Take-profit | $125.96 + 3×10.14 | **$156.38** |
| Ratio R/R | (156.38−125.96)/(125.96−105.68) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — CONFIRMÉE ET RENFORCÉE AU SNAPSHOT 17:00 UTC**

AST n'est pas évaluable en l'état. La situation est strictement inchangée pour AST depuis le snapshot 13:00 UTC du 26/05, mais l'évolution violente d'ASTS renforce l'anomalie structurelle :

1. **Anomalie structurelle confirmée et renforcée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). ASTS affiche un cours de **$125.96** (+18.99%, volume 29.56M, RSI 83.77) avec un gap haussier massif post-Memorial Day. Le mouvement de +18.99% en une seule séance suggère un catalyseur majeur (probablement lié à l'earnings programmé ce jour sous le ticker erroné AST, ou à une annonce D2D) que le système ne capte pas sous AST.
2. **Earnings du 26/05 non exploitable :** FMP signale un earnings AST le 2026-05-26 (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le gap de +18.99% sur ASTS suggère que ce catalyseur a affecté ASTS.
3. **Qualité des données :** AST fait partie des 4 tickers KO sur 26 requêtés (`tickers_ko: 4`), aux côtés d'AXA, CYTOMX, QTBS. AST est absent du quality gate (alors qu'ASTS y figure comme `excluded` pour stale_price_history — ce qui prouve que le système reçoit au moins un historique pour ASTS, contrairement à AST).
4. **Post-Memorial Day :** le marché est ouvert aujourd'hui (2026-05-26), et ASTS a réagi violemment (+18.99%) tandis qu'AST reste muet — confirmant définitivement que le jour férié n'était pas la cause de l'absence de cotation pour AST.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel pullback technique post-gap (RSI 83.77, call wall 120, consensus $92.25 vs cours $125.96)

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 17:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
