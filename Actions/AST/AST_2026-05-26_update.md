# AST — Mise à jour Quotidienne

> **Date :** 2026-05-26
> **Type :** Update finale (snapshot 21:00 UTC)
> **Source :** data/latest.json (21:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-26_update.md` (snapshot 17:00 UTC)

| Élément | Snapshot 17:00 UTC | Snapshot 21:00 UTC | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | Cours **$125.96** (+18.99%) | Cours **$119.70** (+13.07%) | **−4.97% vs snapshot 17h, correction intraday** |
| Volume ASTS | 29.56M | **47.17M** | **+59.6%, 2.07× moyenne 20j** |
| RSI ASTS | 83.77 | **82.58** | **−1.19 pt, surchauffe persistante** |
| Intraday high ASTS | $127.10 | $127.10 (même high) | — |
| 52W high ASTS | 129.89 | 129.89 | Close $119.70 = 92.2% du 52W high |
| Options ASTS | max pain 120, P/C 0.78, call OI 56.2% | max pain 120, P/C 0.78, call OI 56.2% | **Stable — close $119.70 juste sous max pain** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable |
| Score ASTS (agent) | 36.0/100 (SURVEILLER) | 36.0/100 (SURVEILLER) | Stable |
| Earnings FMP AST | 2026-05-26 (days_until: 0) | 2026-05-26 (days_until: 0) | Confirmé |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |

**Constat :** Le snapshot 21:00 UTC confirme la **stabilité totale** de l'absence de données de marché pour AST. C'est le **15e snapshot consécutif** (18/05 → 26/05) sans historique de prix. ASTS corrige de son intraday high ($127.10) pour clôturer à **$119.70** (+13.07%), avec un volume massif de **47.17M** (2.07× moyenne 20j), confirmant une forte participation institutionnelle/rétail sur un catalyseur non capturé par le pipeline sous le ticker AST.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur snapshot 21:00 UTC | Valeur précédente (17:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur snapshot 21:00 UTC | Valeur précédente (17:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | **$119.70** | $125.96 | **−4.97%** (correction intraday) |
| Volume | **47.17M** | 29.56M | **+59.6%** |
| Volume relatif | **2.07× moy. 20j** | 1.35× | Forte accélération de la participation |
| RSI 14j | **82.58** | 83.77 | **−1.19 pt** |
| ATR 14j | 10.14 | 10.14 | Stable |
| MM 50j | 84.87 | 84.99 | −0.12 pt |
| 52W high | 129.89 | 129.89 | Close = 92.2% du 52W high |
| Intraday high | 127.10 | 127.10 | Même high — rejet au-dessus de $125 |

**Verdict timing ASTS (proxy) :** 🔴 **SURCHAUFFE EXTRÊME** — RSI 82.58 (>80), volume ×2 sur séance de correction intraday. Le close $119.70 sous le max pain ($120) et sous l'intraday high ($127.10) suggère un rejet technique au contact de la zone $125-130. Call wall à 120, max pain 120. Momentum haussier mais risque de pullback technique élevé.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur snapshot 21:00 UTC | Valeur précédente | Δ |
|---------|--------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur snapshot 21:00 UTC |
|---------|--------------------------|
| Market cap | $46.46B |
| Forward P/E | −402.85 |
| EV/Revenue | 378.74× |
| EV/EBITDA | −101.67 |
| Beta | 2.598 |
| Short interest | 18.14% |

Pas de fondamentaux attractifs — valorisation purement spéculative sur la technologie satellite direct-to-device (D2D). Le consensus analystes ($92.25) reste **+29.8% sous le close** ($119.70), confirmant la surchauffe de la valorisation.

---

## 4. Mise à jour sentiment / options / news

- **News AST :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json`
- **News ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` — mais le volume ×2 et le gap de +13.07% suggèrent fortement une news non capturée par le pipeline (probablement liée à l'earnings programmé ce jour sous le ticker AST, ou à un contrat/annonce technique sur le D2D satellite)
- **Options ASTS :** max pain 120.0, put/call ratio 0.78, call OI 56.2% — configuration bullish, call wall à 120. Le close $119.70 est juste sous le max pain ($120), zone de friction technique
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 10 analystes, price target moyen $92.25 — cours actuel $119.70 = **+29.8% au-dessus du consensus**, signal de surchauffe
- **Quant :** pas de signaux historiques pour AST — p-value insuffisante
- **Geo / Accounting / Sector / FX / Events :** aucune donnée spécifique pour AST
- **FX exposure AST/ASTS :** exposition 25% (placeholder), direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-05-26** (`days_until: 0`) via FMP — résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 76`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 2026-05-26 (21:00 UTC) | Pondération | Note |
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

| Axe | Score 2026-05-26 (21:00 UTC) | Pondération | Note |
|-----|-----------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur potentiel (news non capturée) mais non vérifiable |
| Valorisation | 3.0/10 | 40% | EV/Revenue 378×, forward P/E −402.85, consensus +29.8% sous cours |
| Momentum | 6.0/10 | 25% | Gap haussier +13.07%, volume ×2, RSI 82.58 — surchauffe |
| **Score Opportunité** | **4.1/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **41.0/100** | — | SURVEILLER |
| **Score Global Ajusté** | **36.0/100** | — | SURVEILLER |

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy.

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
| Prix entrée | Cours close | $119.70 |
| Stop-loss | $119.70 − 2×10.14 | **$99.42** |
| Take-profit | $119.70 + 3×10.14 | **$150.12** |
| Ratio R/R | (150.12−119.70)/(119.70−99.42) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — CONFIRMÉE ET RENFORCÉE AU SNAPSHOT 21:00 UTC**

AST n'est pas évaluable en l'état. La situation est strictement inchangée pour AST depuis le snapshot 17:00 UTC du 26/05, mais le close final d'ASTS renforce l'anomalie structurelle :

1. **Anomalie structurelle confirmée et renforcée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). ASTS affiche un cours de **$119.70** (+13.07%, volume 47.17M, RSI 82.58) avec un gap haussier massif post-Memorial Day et une digestion intraday (high $127.10, close $119.70). Le mouvement de +13.07% sur un volume ×2 suggère un catalyseur majeur (probablement lié à l'earnings programmé ce jour sous le ticker erroné AST, ou à une annonce D2D) que le système ne capte pas sous AST.
2. **Earnings du 26/05 non exploitable :** FMP signale un earnings AST le 2026-05-26 (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le gap de +13.07% sur ASTS suggère que ce catalyseur a affecté ASTS.
3. **Qualité des données :** AST fait partie des 3 tickers KO sur 26 requêtés (`tickers_ko: 3`), aux côtés d'AXA et QTBS. AST est absent du quality gate (alors qu'ASTS y figure comme `excluded` pour stale_price_history — ce qui prouve que le système reçoit au moins un historique pour ASTS, contrairement à AST).
4. **Close ASTS sous max pain :** le close $119.70 est juste sous le max pain $120, avec un call wall à 120. Cela suggère une possible consolidation ou correction technique à court terme après le gap haussier.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel pullback technique post-gap (RSI 82.58, call wall 120, consensus $92.25 vs cours $119.70). Le niveau $105-110 (previous close + support psychologique) serait une zone de repli naturelle.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 21:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
