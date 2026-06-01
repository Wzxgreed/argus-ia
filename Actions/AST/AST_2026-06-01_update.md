# AST — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Type :** Update après-midi (snapshot 13:00 UTC)
> **Source :** data/latest.json (fetched_at 13:00:02 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_2026-06-01.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-06-01_update.md` (snapshot 10:00 UTC)

| Élément | 10:00 UTC (01/06) | 13:00 UTC (01/06) | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — >21 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$113.41** | **$113.41** | **Stable** |
| Volume ASTS | 54.81M (2.08×) | 54.81M (2.08×) | Stable |
| RSI ASTS | 69.79 | 69.79 | Stable |
| ATR ASTS | 12.02 | 12.02 | Stable |
| MM 50j ASTS | 86.88 | 86.88 | Stable |
| 52W high ASTS | 133.86 | 133.86 | Stable |
| Short interest ASTS | 17.60% | 17.60% | Stable |
| Consensus PT ASTS | $94.54 (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus ASTS | +19.9% | +19.9% | Stable |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable — placeholder |
| Score ASTS (agent) | 38.5/100 (SURVEILLER) | 38.5/100 (SURVEILLER) | Stable |
| Earnings FMP AST | 2026-06-01 (days_until: 0) | 2026-06-01 (days_until: 0) | **Placeholder glissant J=0 non résolu — 6j de glissement** |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |
| News AST / ASTS | 0 | 0 | Stable |
| Events corporates AST | 0 | 0 | Stable |

**Constat :** Le snapshot 13:00 UTC confirme la **stabilité totale** de l'absence de données de marché pour AST (>21 snapshots consécutifs sans mutation). Le proxy ASTS est **inchangé** à **$113.41** sur un volume de **54.81M (2.08× moyenne 20j)**. Aucune news, aucun événement corporate, aucun mouvement d'options ni de consensus analystes n'a été détecté entre 10:00 et 13:00 UTC.

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 13:00 UTC (01/06) | Valeur précédente (10:00 UTC 01/06) | Δ |
|-----------|-------------------------|-----------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 13:00 UTC (01/06) | Valeur précédente (10:00 UTC 01/06) | Δ |
|-----------|-------------------------|-----------------------------------|---|
| Cours close | **$113.41** | $113.41 | **Stable** |
| Open | 113.46 | 113.46 | Stable |
| High intraday | 115.50 | 115.50 | Stable |
| Low intraday | 105.37 | 105.37 | Stable |
| Volume | **54.81M** | 54.81M | Stable |
| Volume relatif | **2.08× moy. 20j** | 2.08× | Stable |
| RSI 14j | **69.79** | 69.79 | Stable |
| ATR 14j | **12.02** | 12.02 | Stable |
| MM 50j | **86.88** | 86.88 | Stable |
| Distance MM50j | **+30.5%** | +30.5% | Stable |
| 52W high | 133.86 | 133.86 | Stable |
| Distance 52W high | **−15.3%** | −15.3% | Stable |

**Verdict timing ASTS (proxy) :** 🟡 **CORRECTION TECHNIQUE POST-SQUEEZE — CONFIRMÉE STABLE** — Le cours est stable à $113.41 après le gap baissier de −14.79% observé ce matin. Le RSI à 69.79 reste dans la zone haussière mais hors surchauffe extrême. Le low à $105.37 (proche de la zone de support $105–110) a été testé et tenu en séance. Aucun rebond ni extension de la baisse n'a eu lieu entre 10:00 et 13:00 UTC, ce qui suggère une **consolidation techniqueshort-term** avant la prochaine impulsion. La rupture du support $105 sur volume élevé ouvrirait la voie vers $95–100 (zone du max pain historique $120 moins l'expansion ATR).

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 13:00 UTC (01/06) | Valeur précédente | Δ |
|---------|-------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 13:00 UTC (01/06) | Valeur précédente (10:00 UTC) | Δ |
|---------|-------------------------|------------------------------|---|
| Market cap | **$44.02B** | $44.02B | **Stable** |
| Forward P/E | **−381.68** | −381.68 | Stable |
| EV/Revenue | **405.3×** | 405.3× | Stable |
| EV/EBITDA | **−108.80** | −108.80 | Stable |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 17.60% | Stable |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | Stable |
| Premium vs consensus | **+19.9%** | +19.9% | Stable |

Pas de mutation fondamentale entre 10:00 et 13:00 UTC. La valorisation reste purement spéculative sur la technologie satellite direct-to-device (D2D). Le premium vs consensus de +19.9% est une prime élevée mais moins extrême qu'à la fin mai (+40.2%). La couverture analyste (12 analysts) et le PT moyen ($94.54) sont inchangés.

---

## 4. Mise à jour sentiment / options / news

- **News AST :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-06-01.json` — **0 article pour AST, 0 pour ASTS**
- **Options ASTS :** max pain **40.0** (données corrompues / placeholder — le max pain précédent $120 a disparu du snapshot), put/call ratio et call OI non disponibles. **Anomalie options persistante** à noter.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $113.41 = **+19.9% au-dessus du consensus**
- **Quant :** pas de signaux historiques pour AST — p-value insuffisante (p=1.0, n=0)
- **Geo / Accounting / Events :** aucune donnée spécifique pour AST
- **FX exposure AST/ASTS :** exposition 25% (placeholder), direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-01** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 26/05, 6 jours de glissement), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 70`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **ROTATION_TO_DEFENSIVE** détecté. Technology (XLK) reste top1 sector avec momentum score 10.0. Industrials (XLI) et Energy (XLE) sous-performants — XLE en bearish crossover. Pas d'impact direct sur ASTS/AST.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 13:00 UTC (01/06) | Pondération | Note |
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

| Axe | Score 13:00 UTC (01/06) | Pondération | Note |
|-----|------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur potentiel (news non capturée, révision PT analystes) mais non vérifiable |
| Valorisation | 3.0/10 | 40% | EV/Revenue 405×, forward P/E −381.68, consensus +19.9% sous cours |
| Momentum | 5.0/10 | 25% | Correction −14.79% confirmée stable, RSI 69.79 sorti de surchauffe |
| **Score Opportunité** | **3.9/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **38.5/100** | — | SURVEILLER |
| **Score Global Ajusté** | **38.5/100** | — | **SURVEILLER** |

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Neutre
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. Le score **SURVEILLER (38.5/100)** reflète le soulagement technique (RSI 69.79, premium consensus compressé à +19.9%) mais la configuration reste risquée (distribution sur volume ×2 en matinée, ATR en expansion 12.02).

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
| Prix entrée | Cours close | $113.41 |
| Stop-loss | $113.41 − 2×12.02 | **$89.37** |
| Take-profit | $113.41 + 3×12.02 | **$149.47** |
| Ratio R/R | (149.47−113.41)/(113.41−89.37) | **1.5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL à $89.37 et le TP à $149.47 sont inchangés vs 10:00 UTC** en l'absence de mutation de cours ou d'ATR. Le niveau $105 (low intraday) reste le support immédiat à surveiller.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — STABILITÉ CONFIRMÉE À 13:00 UTC**

AST n'est pas évaluable en l'état. La situation pour AST est strictement inchangée entre le snapshot 10:00 UTC et le snapshot 13:00 UTC du 01/06 :

1. **Anomalie structurelle confirmée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). ASTS affiche un cours stable à **$113.41** sur un volume de **54.81M (2.08× moyenne 20j)**, confirmant la correction post-squeeze après le rallye parabolique de fin mai ($129.335 au close 27/05).
2. **Distribution technique confirmée stable :** le volume matinal ×2.08 reste le signal dominant de la séance. L'absence de rebond entre 10:00 et 13:00 UTC suggère une consolidation technique avant la prochaine impulsion. Le RSI à 69.79 reste élevé mais hors zone de surchauffe extrême.
3. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-01** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **26/05** (6 jours de décalage non résolu). Si un résultat a été publié, il n'est pas intégré dans `data/latest.json`.
4. **Score agent ASTS stable :** le score reste à **SURVEILLER (38.5/100)**, reflétant la compression du premium consensus (+19.9% vs +40.2% fin mai) et la sortie du RSI de la zone >80. Le ticker reste non qualifié (score < 6/10).
5. **Qualité des données :** AST fait partie des 4 tickers KO sur 28 requêtés (`tickers_ko: 4`), aux côtés d'ASTSPACE, AXA et QTBS. AST est absent du quality gate (alors qu'ASTS y figure avec des données complètes).
6. **Consensus analystes ASTS :** le passage de 10 à 12 analysts et la révision du PT à la hausse ($92.25 → $94.54) observés ce matin sont confirmés stables à 13:00 UTC. Le sell-side a intégré un catalyseur positif (probablement lié à l'earnings du Q1 2026 ou à un contrat D2D) malgré la correction de cours.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel rebond technique. Le niveau **$105–110** est la zone de support naturelle (low intraday $105.37 + MM50j $86.88 comme support structurel plus profond). Une cassure sous $105 sur volume élevé ouvrirait la voie vers $95–100. Un rebond au-dessus de $120 (ancien max pain) réactiverait la configuration haussière.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 13:00 UTC, fetched_at 2026-06-01T13:00:02.278720+00:00), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_2026-06-01.json — aucune donnée hallucinée.*
