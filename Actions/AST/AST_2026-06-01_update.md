# AST — Mise à jour Quotidienne

> **Date :** 2026-06-01
> **Type :** Update matin (snapshot 10:00 UTC)
> **Source :** data/latest.json, data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-27_update.md` (snapshot 17:00 UTC)

| Élément | 27/05 (close) | 01/06 (close) | Changement |
|---------|---------------|---------------|------------|
| Erreur Yahoo AST | `No price history` | `No price history` | **Confirmé stable — 5j supplémentaires, >20 snapshots consécutifs** |
| Cours AST | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| ASTS (proxy) | **$129.335** | **$113.41** | **−14.79% en 4 séances** |
| Volume ASTS | 19.72M (0.85×) | **54.81M** (2.08×) | **Volume en explosion sur la baisse** |
| RSI ASTS | 83.14 | **69.79** | **−13.35 pts, surchauffe partiellement dissipée** |
| ATR ASTS | 10.41 | **12.02** | **+1.61 pt, volatilité en expansion** |
| MM 50j ASTS | 85.67 | **86.88** | **+1.21 pt, support dynamique** |
| 52W high ASTS | 129.89 | 133.86 | **Nouveau 52W high $133.86** (précédent close 27/05), close = 84.7% du high |
| Short interest ASTS | 18.14% | **17.60%** | **−0.54 pp** |
| Consensus PT ASTS | $92.25 (10 analysts) | **$94.54** (12 analysts) | **+2.5% révision à la hausse** |
| Premium vs consensus ASTS | +40.2% | **+19.9%** | **Compression de 20.3 pp** |
| Score AST (agent) | 55.2/100 (ATTENDRE) | 55.2/100 (ATTENDRE) | Stable — placeholder |
| Score ASTS (agent) | 29.8/100 (ÉVITER) | **38.5/100 (SURVEILLER)** | **Upgrade +8.7 pts — soulagement technique** |
| Earnings FMP AST | 2026-05-27 (days_until: 0) | **2026-06-01** (days_until: 0) | **Placeholder glissant J=0 non résolu — 5j de glissement** |
| Earnings ASTS (yfinance) | 2026-08-10 | 2026-08-10 | Stable |

**Constat :** Le snapshot du 01/06 confirme la **stabilité totale** de l'absence de données de marché pour AST (>20 snapshots consécutifs). En revanche, **ASTS corrige brutalement** : le cours chute de **$133.09 (previous close) à $113.41 (−14.79%)** sur un volume de **54.81M (2.08× moyenne 20j)**. Cette configuration — gap baissier + volume explosion sur la baisse + RSI qui sort de la zone >80 — est typique d'une **correction technique post-squeeze** après le rallye parabolique des 27–30/05. L'agent a upgradé ASTS de **ÉVITER (29.8) à SURVEILLER (38.5)**, reflétant le soulagement de la surchauffe (RSI 69.79 vs 83.14) et la compression du premium consensus (+19.9% vs +40.2%).

---

## 2. Mise à jour technique

### AST (données officielles)

| Indicateur | Valeur 01/06 | Valeur précédente (27/05) | Δ |
|-----------|-------------|---------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 01/06 | Valeur précédente (27/05) | Δ |
|-----------|-------------|---------------------------|---|
| Cours close | **$113.41** | $129.335 | **−14.79%** |
| Open | 113.46 | — | Gap ouverture neutre |
| High intraday | **115.50** | 129.38 | **Rejet haussier intraday faible** |
| Low intraday | **105.37** | — | **Test de $105 — support technique** |
| Volume | **54.81M** | 19.72M | **+178% — volume explosion sur baisse** |
| Volume relatif | **2.08× moy. 20j** | 0.85× | **Distribution signal** |
| RSI 14j | **69.79** | 83.14 | **−13.35 pts, sortie zone surachat** |
| ATR 14j | **12.02** | 10.41 | **+15.5%, volatilité en expansion** |
| MM 50j | **86.88** | 85.67 | **+1.21 pt, support dynamique** |
| Distance MM50j | **+30.5%** | +50.9% | **Compression de l'écartement haussier** |
| 52W high | 133.86 | 129.89 | **Nouveau record 30/05** |
| Distance 52W high | **−15.3%** | −0.4% | **Retour sous le sommet** |

**Verdict timing ASTS (proxy) :** 🟡 **CORRECTION TECHNIQUE POST-SQUEEZE** — Le gap baissier de −14.79% sur volume ×2.08 est un signal de distribution clair après l'excès de fin mai. Le RSI à 69.79 reste élevé (zone haussière) mais n'est plus en surchauffe extrême. Le low à $105.37 (proche de la MM50j +9.1%) a été testé et tenu. Toutefois, la rupture du support psychologique $110 sur volume élevé ouvrirait la voie vers $95–100 (zone du max pain précédent $120 moins l'expansion ATR).

---

## 3. Mise à jour fondamentale

### AST (données officielles)

| Métrique | Valeur 01/06 | Valeur précédente | Δ |
|---------|-------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur 01/06 | Valeur précédente (27/05) | Δ |
|---------|-------------|---------------------------|---|
| Market cap | **$44.02B** | $50.22B | **−12.3%** |
| Forward P/E | **−381.68** | −435.43 | **Légère amélioration mécanique** |
| EV/Revenue | **405.3×** | 427.4× | **Compression −5.2%** |
| EV/EBITDA | **−108.80** | −114.74 | **Stable** |
| Beta | 2.598 | 2.598 | Stable |
| Short interest | **17.60%** | 18.14% | **−0.54 pp** |
| Consensus PT | **$94.54** (12 analysts) | $92.25 (10 analysts) | **Révision +2.5%, couverture élargie** |
| Premium vs consensus | **+19.9%** | +40.2% | **Compression −20.3 pp** |

Pas de fondamentaux attractifs — valorisation purement spéculative sur la technologie satellite direct-to-device (D2D). La correction de −14.79% a ramené le premium vs consensus de +40.2% à +19.9%, ce qui reste une prime élevée mais moins extrême. L'ajout de 2 analystes (10 → 12) et la révision du PT à la hausse ($92.25 → $94.54) suggèrent que le sell-side intègre un catalyseur positif (probablement lié aux résultats du Q1 2026 ou à un contrat D2D).

---

## 4. Mise à jour sentiment / options / news

- **News AST :** aucune entrée Yahoo Finance ni FMP dans `data/latest.json` ni `data/news_2026-06-01.json`
- **News ASTS :** aucune entrée Yahoo Finance — mais la couverture analyste est passée de 10 à 12 et le PT moyen a été révisé à la hausse (+2.5%), ce qui suggère un catalyseur fondamental non capturé par le pipeline news
- **Options ASTS :** max pain **40.0** (données corrompues / placeholder — le max pain précédent $120 a disparu du snapshot), put/call ratio et call OI non disponibles. **Anomalie options** à noter.
- **Social sentiment :** 0 mention Reddit pour AST, 0 pour ASTS
- **Upgrades/downgrades AST :** pas de consensus analystes disponible (0 analystes)
- **Upgrades/downgrades ASTS :** 12 analystes, price target moyen $94.54 — cours actuel $113.41 = **+19.9% au-dessus du consensus**
- **Quant :** pas de signaux historiques pour AST — p-value insuffisante (p=1.0, n=0)
- **Geo / Accounting / Events :** aucune donnée spécifique pour AST
- **FX exposure AST/ASTS :** exposition 25% (placeholder), direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - AST : earnings signalé le **2026-06-01** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (J=0 depuis le 26/05, 5 jours de glissement), résultats non intégrés au pipeline
  - ASTS : earnings le **2026-08-10** (`days_until: 70`) via yfinance, estimations EPS $−0.29 à $−0.17, Revenues $0.0B
- **Sector rotation :** signal **ROTATION_TO_DEFENSIVE** détecté. Technology (XLK) reste top1 sector mais Industrials (XLI) et Energy (XLE) sous-performants. XLE en bearish crossover. Pas d'impact direct sur ASTS/AST.

---

## 5. Scoring global

### AST (données officielles — placeholder)

| Axe | Score 01/06 | Pondération | Note |
|-----|-------------|-------------|------|
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

| Axe | Score 01/06 | Pondération | Note |
|-----|-------------|-------------|------|
| Catalyseur | 4.0/10 | 35% | Catalyseur potentiel (news non capturée, révision PT analystes) mais non vérifiable |
| Valorisation | 3.0/10 | 40% | EV/Revenue 405×, forward P/E −381.68, consensus +19.9% sous cours |
| Momentum | 5.0/10 | 25% | Correction −14.79%, volume ×2.08 = distribution, RSI 69.79 sorti de surchauffe |
| **Score Opportunité** | **3.9/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **38.5/100** | — | SURVEILLER |
| **Score Global Ajusté** | **38.5/100** | — | **SURVEILLER** |

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Neutre
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **L'upgrade d'ÉVITER (29.8) à SURVEILLER (38.5)** reflète le soulagement technique (RSI 69.79, premium consensus compressé à +19.9%) mais la configuration reste risquée (distribution sur volume ×2, ATR en expansion).

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

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle et quantifier la volatilité du proxy. **Le SL a glissé de $108.52 (27/05) à $89.37 (01/06)** en raison de l'expansion de l'ATR (10.41 → 12.02) et de la correction du cours ($129.335 → $113.41). Le niveau $105 (low du jour) est un support intraday à surveiller.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — CORRECTION TECHNIQUE DU PROXY ASTS CONFIRMÉE**

AST n'est pas évaluable en l'état. La situation pour AST est strictement inchangée depuis le 27/05 :

1. **Anomalie structurelle confirmée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). ASTS affiche un cours de **$113.41 (−14.79%)** sur un volume de **54.81M (2.08× moyenne 20j)**, confirmant la correction post-squeeze après le rallye parabolique de fin mai ($129.335).
2. **Distribution technique :** le volume a explosé sur la baisse (2.08× moyenne), ce qui est un signal de distribution classique après un squeeze. Le RSI est descendu de 83.14 à 69.79 — soulagement partiel mais pas de retournement de tendance haussière.
3. **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-01** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **26/05** (5 jours de décalage non résolu). Si un résultat a été publié, il n'est pas intégré dans `data/latest.json`.
4. **Upgrade agent ASTS :** le score est passé de **ÉVITER (29.8/100)** à **SURVEILLER (38.5/100)**, reflétant la compression du premium consensus (+19.9% vs +40.2%) et la sortie du RSI de la zone >80. Toutefois, le ticker reste non qualifié (score < 6/10).
5. **Qualité des données :** AST fait partie des 4 tickers KO sur 28 requêtés (`tickers_ko: 4`), aux côtés d'ASTSPACE, AXA et QTBS. AST est absent du quality gate (alors qu'ASTS y figure avec des données complètes).
6. **Consensus analystes ASTS :** le passage de 10 à 12 analysts et la révision du PT à la hausse ($92.25 → $94.54) suggèrent que le sell-side a intégré un catalyseur positif (probablement lié à l'earnings du Q1 2026 ou à un contrat D2D) malgré la correction de cours.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel rebond technique. Le niveau **$105–110** est la zone de support naturelle (low du jour $105.37 + MM50j $86.88 comme support structurel plus profond). Une cassure sous $105 sur volume élevé ouvrirait la voie vers $95–100. Un rebond au-dessus de $120 (ancien max pain) réactiverait la configuration haussière.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 10:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
