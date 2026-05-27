# AST — Mise à jour Quotidienne

> **Date :** 2026-05-27
> **Type :** Update après-midi (snapshot 13:00 UTC)
> **Source :** data/latest.json (13:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-27_update.md` (snapshot 10:00 UTC)

| Élément | Snapshot 10:00 UTC (27/05) | Snapshot 13:00 UTC (27/05) | Changement |
|---------|---------------------------|---------------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | Cours **$119.70** (+13.07%) | Cours **$119.70** (+13.07%) | **Stable** |
| Volume ASTS | 48.08M (2.10× moy. 20j) | **48.08M** (2.10× moy. 20j) | Stable |
| RSI ASTS | 82.58 | **82.58** | Stable |
| ATR ASTS | 10.14 | **10.14** | Stable |
| MM 50j ASTS | 84.87 | **84.87** | Stable |
| 52W high ASTS | 129.89 | 129.89 | Close $119.70 = 92.2% du 52W high |
| Options ASTS | max pain 40.0 (anomalie JSON) | **max pain 120.0, P/C 0.76, call OI 57.0%** | **Anomalie JSON résolue** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable |
| Score ASTS (agent) | 36.0/100 (SURVEILLER) | 36.0/100 (SURVEILLER) | Stable |
| Earnings FMP AST | 2026-05-27 (days_until: 0) | 2026-05-27 (days_until: 0) | **Placeholder glissant J=0 non résolu** |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |

**Constat :** Le snapshot 13:00 UTC confirme la **stabilité totale** de l'absence de données de marché pour AST. C'est le **17e snapshot consécutif** (18/05 → 27/05) sans historique de prix. ASTS affiche des données techniques strictement inchangées par rapport au snapshot 10:00 UTC ($119.70, RSI 82.58, ATR 10.14). L'anomalie options JSON détectée ce matin (max pain 40.0 aberrant) est **résolue** : le snapshot 13:00 UTC retourne max pain **120.0**, put/call ratio **0.76**, call OI **57.0%** — valeurs cohérentes avec le close $119.70 et confirmant la structure haussière des options. Le volume de 48.08M (2.10× moyenne 20j) confirme la forte participation institutionnelle/rétail sur un catalyseur non capturé par le pipeline sous le ticker AST.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur snapshot 13:00 UTC (27/05) | Valeur précédente (10:00 UTC 27/05) | Δ |
|-----------|--------------------------------|-----------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur snapshot 13:00 UTC (27/05) | Valeur précédente (10:00 UTC 27/05) | Δ |
|-----------|----------------------------------|-----------------------------------|---|
| Cours close | **$119.70** | $119.70 | **Stable** |
| Volume | **48.08M** | 48.08M | Stable |
| Volume relatif | **2.10× moy. 20j** | 2.10× | Stable |
| RSI 14j | **82.58** | 82.58 | Stable |
| ATR 14j | **10.14** | 10.14 | Stable |
| MM 50j | **84.87** | 84.87 | Stable |
| 52W high | 129.89 | 129.89 | Close = 92.2% du 52W high |
| Intraday high | 127.10 | 127.10 | Même high — rejet au-dessus de $125 confirmé |

**Verdict timing ASTS (proxy) :** 🔴 **SURCHAUFFE EXTRÊME** — RSI 82.58 (>80), volume ×2 persistant. Le close $119.70 sous l'intraday high ($127.10) confirme le rejet technique au contact de la zone $125-130. Configuration inchangée depuis le 26/05.

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur snapshot 13:00 UTC (27/05) | Valeur précédente | Δ |
|---------|----------------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur snapshot 13:00 UTC (27/05) |
|---------|----------------------------------|
| Market cap | $46.46B |
| Forward P/E | −402.85 |
| EV/Revenue | 427.42× |
| EV/EBITDA | −114.74 |
| Beta | 2.598 |
| Short interest | 18.14% |

Pas de fondamentaux attractifs — valorisation purement spéculative sur la technologie satellite direct-to-device (D2D). Le consensus analystes ($92.25) reste **+29.8% sous le close** ($119.70), confirmant la surchauffe de la valorisation. Aucun changement fondamental depuis le snapshot 10:00 UTC.

---

## 4. Mise à jour sentiment / options / news

- **News AST :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json`
- **News ASTS :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` — mais le volume ×2 persistant et le gap de +13.07% suggèrent fortement une news non capturée par le pipeline (probablement liée à l'earnings programmé sous le ticker erroné AST, ou à un contrat/annonce technique sur le D2D satellite)
- **Options ASTS :** **anomalie JSON résolue** — max pain **120.0** (vs 40.0 aberrant ce matin), put/call ratio **0.76**, call OI **57.0%** (vs 56.2% précédemment). Configuration bullish confirmée : call wall à 120, max pain 120. Le close $119.70 est juste sous le max pain ($120), zone de friction technique inchangée. La résolution de l'anomalie confirme la fiabilité du parsing options pour ce snapshot.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 10 analystes, price target moyen $92.25 — cours actuel $119.70 = **+29.8% au-dessus du consensus**, signal de surchauffe inchangé
- **Quant :** pas de signaux historiques pour AST — p-value insuffisante
- **Geo / Accounting / Sector / Events :** aucune donnée spécifique pour AST
- **FX exposure AST/ASTS :** exposition 25% (placeholder), direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-05-27** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 26/05), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 75`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 2026-05-27 (13:00 UTC) | Pondération | Note |
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

| Axe | Score 2026-05-27 (13:00 UTC) | Pondération | Note |
|-----|-----------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur potentiel (news non capturée) mais non vérifiable |
| Valorisation | 3.0/10 | 40% | EV/Revenue 427×, forward P/E −402.85, consensus +29.8% sous cours |
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

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — CONFIRMÉE AU SNAPSHOT 13:00 UTC**

AST n'est pas évaluable en l'état. La situation est strictement inchangée depuis le snapshot 10:00 UTC du 27/05 :

1. **Anomalie structurelle confirmée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). ASTS affiche un cours de **$119.70** (volume 48.08M, RSI 82.58) avec un gap haussier massif post-Memorial Day confirmé stable. Le mouvement de +13.07% sur un volume ×2 suggère un catalyseur majeur que le système ne capte pas sous AST.
2. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le 2026-05-27 (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le placeholder glisse depuis le 26/05 sans résolution.
3. **Qualité des données :** AST fait partie des 3 tickers KO sur 26 requêtés (`tickers_ko: 3`), aux côtés d'AXA et QTBS. AST est absent du quality gate (alors qu'ASTS y figure comme `excluded` pour stale_price_history — ce qui prouve que le système reçoit au moins un historique pour ASTS, contrairement à AST).
4. **Anomalie options JSON résolue :** le snapshot 13:00 UTC confirme max_pain **120.0**, put/call ratio **0.76**, call OI **57.0%** — valeurs cohérentes avec le close $119.70. L'anomalie 40.0 détectée ce matin était un artefact de parsing transitoire.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel pullback technique post-gap (RSI 82.58, consensus $92.25 vs cours $119.70). Le niveau $105-110 (previous close + support psychologique) reste une zone de repli naturelle.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 13:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
