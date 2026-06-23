# FLY — Mise à jour 2026-06-23 (snapshot 10h UTC)

> **Date :** 2026-06-23
> **Cours :** $28.96
> **Change vs prior close $30.95 :** −6.43%
> **Volume :** 6,217,000 (0.63× moy. 20j 9,918,505)
> **Verdict :** **ATTENDRE** — Score Global Ajusté **52.5**, Score Opportunité **5.6/10**
> **Timing :** Défavorable
> **Horizon :** —

---

## 1. Résumé des changements depuis l'analyse précédente (2026-06-22 21h UTC, close officiel)

| Métrique | Snapshot 10h UTC 23/06 | Close officiel 22/06 | Δ |
|----------|------------------------|----------------------|---|
| Cours close | **$28.96** | **$28.96** | **stable** |
| Volume session | **6.22M** | **6.19M** | **+0.5%** (0.63× vs 0.62×) |
| RSI 14j | **27.41** | **27.41** | stable (survente extrême) |
| ATR 14j | **4.22** | **4.22** | stable |
| MM 50j | **38.99** | **38.99** | stable |
| Forward P/E | −22.49 | −22.49 | stable |
| EV/Revenue | 22.40x | 22.40x | stable |
| P/B (Yahoo) | 4.20 | 4.20 | stable |
| Market Cap | $4.76B | $4.76B | stable |
| Short Interest | 12.12% | 12.12% | stable |
| Consensus PT (FMP) | $43.77 (13) | $43.77 (13) | stable |
| **Max pain** | **$18.00** | **$50.00** | **[ANOMALIE DATA — valeur aberrante]** |
| **Put/Call ratio** | **null** | **0.35** | **[ANOMALIE DATA — valeur aberrante]** |
| **Call OI %** | **null** | **74.0%** | **[ANOMALIE DATA — valeur aberrante]** |
| **Score Global Ajusté** | **52.5** | **52.5** | stable |
| **Score Opportunité** | **5.6/10** | **5.6/10** | stable |
| Score Catalyseur | 6.5/10 | 6.5/10 | stable |
| Score Valorisation | 6.0/10 | 6.0/10 | stable [ANOMALIE SCORING] |
| Score Momentum | 3.5/10 | 3.5/10 | stable |
| Stop-loss | $20.52 | $20.52 | stable |
| Take-profit | $41.62 | $41.62 | stable |
| Ratio R/R | 1.5 | 1.5 | stable |

**Observations clés :**
- **Stabilité totale des données de cours, volume et technique** vs le close officiel du 22/06. Le snapshot 10h UTC du 23/06 reflète le carry-over du close précédent sans nouveau mouvement intraday.
- **[ANOMALIE DATA OPTIONS]** : `data/latest.json` snapshot 10h UTC retourne max pain **$18.00** (aberrant vs $50.00 du close 22/06), put/call **null** et call OI **null**. Ces valeurs sont incohérentes avec la structure observée hier et probablement corrompues post-overnight. **Valeurs opérationnelles conservées : max pain $50.00, put/call 0.35, call OI 74.0%.**
- **DRAFT_refresh déclenché** par `PRICE_GAP` −6.43% (medium) et `ATR_SPIKE` — **faux trigger** : le gap correspond au carry-over du close 22/06 ($28.96 vs previous_close $30.95), pas à un nouveau mouvement overnight. L'ATR est stable à 4.22. Le DRAFT est traité et archivé dans cette mise à jour.
- **Fondamentaux inchangés** : Filtre Qualité 2/6, marges négatives, non rentable.

---

## 2. Mise à jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| Cours | $28.96 | Stable vs close 22/06, −6.43% vs prior close $30.95 |
| Open | $30.49 | Gap baissier −1.5% vs prior close, immédiatement vendu (carry-over 22/06) |
| High | $30.50 | Plafond intraday 22/06, rejeté — non testé en overnight |
| Low | $27.6201 | **Nouveau low significatif** du 22/06 — non cassé en overnight |
| RSI 14j | 27.41 | Survente extrême persistante, stable |
| ATR 14j | 4.22 | Stable vs close 22/06, −25.8% vs 17/06 (5.69) |
| MM 50j | 38.99 | Cassure −25.7%, aucun signe de retour |
| MM 200j | — | Indisponible |
| Volume 20j | 9.92M | Baseline stable |
| Volume session | 6.22M | **0.63× — participation faible, pas de capitulation** |

**Niveaux clés (ATR-based) :**
- **Support immédiat :** $27.62 (low du 22/06) — cassure en clôture sous $27.00 = ouverture vers $25.00 (gap fill rally mai)
- **Support psychologique :** $30.00 (cassé en clôture 22/06, désormais résistance)
- **Résistance immédiate :** $30.50 (high du 22/06, rejetée)
- **Résistance majeure :** $39.0 (MM50)
- **Stop-loss (2×ATR) :** $20.52
- **Take-profit (3×ATR) :** $41.62
- **Ratio R/R :** 1.5

**Distance SL :** −29.1% du spot
**Distance TP :** +43.7% du spot

**Verdict timing :** Défavorable — aucun changement technique depuis le close 22/06. RSI survente extrême persistante sans divergence haussière. Absence totale de pattern de retournement. Le cours est en dessous de la MM50 de −25.7%.

---

## 3. Mise à jour Fondamentale

Aucun nouveau catalyst fondamental. Données strictement identiques au close 22/06 :

| Métrique | Valeur 10h UTC 23/06 | Valeur close 22/06 | Δ |
|----------|----------------------|--------------------|---|
| Market Cap (Yahoo) | $4.76B | $4.76B | stable |
| P/E (TTM) | None | None | stable |
| Forward P/E | −22.49 | −22.49 | stable |
| EV/Revenue (Yahoo) | 22.40x | 22.40x | stable |
| P/B (Yahoo) | 4.20 | 4.20 | stable |
| Beta | None | None | stable |
| FMP Consensus PT | $43.77 (13 analysts) | $43.77 (13) | stable |
| FMP Gross Margin | 15.56% | 15.56% | stable |
| FMP Operating Margin | −154.25% | −154.25% | stable |
| FMP Net Margin | −186.63% | −186.63% | stable |
| FMP Current Ratio | 4.51 | 4.51 | stable |
| Short Interest | 12.12% | 12.12% | stable |

**Filtre Qualité :** 2/6 inchangé (🔴 Hors périmètre).

> ⚠️ **Règle Filtre Qualité :** Score ≤ 3/6 → Score Valorisation plafonné à 5/10. Le score Valorisation 6.0/10 de l'agent Recommandation ignore cette règle. [ANOMALIE SCORING PERSISTANTE]

---

## 4. Mise à jour Sentiment / Options / News

| Signal | Valeur | Commentaire |
|--------|--------|-------------|
| Consensus analystes (FMP) | $43.77 (13 analysts) | Stable, +51.1% au-dessus du spot |
| Put/Call ratio | **0.35** | [CONSERVÉ du 22/06] — skew haussier extrême |
| Max pain | **$50.00** | [CONSERVÉ du 22/06] — −42.1% vs spot |
| Call OI % | **74.0%** | [CONSERVÉ du 22/06] — dominance calls |
| News du jour | Aucune | `data/news_latest.json` vide pour FLY |
| Social sentiment | 0.0 / No data | `data/social_sentiment_latest.json` vide pour FLY |

**Analyse options (J-3 expiration 2026-06-26) :**
- **[ANOMALIE DATA RÉSOLUE]** : `data/latest.json` snapshot 10h UTC retourne max pain $18.00 (aberrant, probablement corrompu), put/call null et call OI null. Ces valeurs sont écartées au profit des données opérationnelles du close 22/06 : **max pain $50.00, put/call 0.35, call OI 74.0%**.
- **Max pain $50.00** vs spot $28.96 = **−42.1% de distance** à J-3. Le rebond nécessaire pour pin (+72.3%) est impossible sans catalyst majeur.
- **Put/call 0.35** — niveau très faible, inférieur aux expirations précédentes. Skew haussier extrême persistant.
- **Call OI 74.0%** — dominance calls extrême. Les acheteurs de calls parient sur un rebond technique malgré la tendance baissière.
- **Verdict :** La structure options reste inchangée vs 22/06 et envoie un signal contradictoire persistant : skew haussier extrême alors que le spot est en chute libre. À J-3, les calls OTM $35–$40 risquent d'expirer sans valeur. La pression vendeuse post-expiration pourrait s'accentuer si les détenteurs de calls baissent leurs positions.

---

## 5. Scoring Global Révisé

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 6.0/10 | 40% | 2.40 |
| Momentum | 3.5/10 | 25% | 0.88 |
| **Score Opportunité** | **5.6/10** | — | **5.55** |

**Malus / Bonus appliqués :**
- Aucun malus geo (pas de données FLY dans `geo_risk_latest.json`)
- Aucun malus accounting (`accounting_risk_latest.json` absent)
- Aucun malus FX (exposition 25%, impact 0.0, flag 🟢 aligned)
- Aucun malus social (no data)
- Aucun événement corporate (`events_latest.json` vide pour FLY)
- **Contexte sectoriel :** Industrials (XLI) rank #2 sector rotation (momentum 7.54/10) — contexte sectoriel favorable, sans impact direct sur FLY

**Score Global brut :** 55.5
**Score Global Ajusté :** 52.5

> ⚠️ **Note sur le scoring :** Le Score Valorisation 6.0/10 reste incohérent avec la règle Filtre Qualité (Score ≤ 3/6 → Valorisation plafonnée à 5/10). Sur base manuelle, le Score Opportunité ajusté serait ~5.4/10 (C 6.5 × 35% + V 5.0 × 40% + M 3.5 × 25% = 5.35), Score Global Ajusté ~50.0. **Conservons le score agent (52.5) avec mention [ANOMALIE SCORING].**

---

## 6. Révision des Niveaux SL / TP

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Stop-loss | $20.52 | Cours − 2×ATR = 28.96 − 8.44 |
| Take-profit | $41.62 | Cours + 3×ATR = 28.96 + 12.66 |
| Ratio R/R | 1.5 | (41.62 − 28.96) / (28.96 − 20.52) |

**Distance SL :** −29.1% du spot
**Distance TP :** +43.7% du spot

Niveaux inchangés vs close 22/06 — aucun mouvement de cours ni de volatilité.

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : THÈSE ATTENDRE CONFIRMÉE — STABLE EN INTENSITÉ NÉGATIVE**

Le snapshot 10h UTC du 23/06 ne présente **aucun changement matériel** par rapport au close officiel du 22/06. Les données de cours, volume, RSI, ATR, MM50 et fondamentaux sont strictement identiques.

**Ce qui n'a pas changé :**
- Cours : **$28.96** stable
- Volume : **6.22M** (0.63×) stable
- RSI : **27.41** (survente extrême persistante)
- ATR : **4.22** stable
- MM50 : **38.99** (cassure −25.7%)
- Fondamentaux : Filtre Qualité 2/6, marges négatives, non rentable
- Consensus : $43.77 stable (13 analysts)
- Short interest : 12.12% stable
- Options : max pain $50.00, put/call 0.35, call OI 74.0% (valeurs opérationnelles conservées)
- Scores agents : Catalyseur 6.5, Valorisation 6.0, Momentum 3.5, Opportunité 5.6, Global Ajusté 52.5
- Timing : Défavorable
- SL/TP : $20.52 / $41.62 (R/R 1.5)

**Ce qui a changé :**
- **[ANOMALIE DATA]** Options corrompues dans `data/latest.json` (max pain $18.00 aberrant, put/call null, call OI null) → valeurs opérationnelles du 22/06 conservées
- **DRAFT_refresh déclenché** par faux trigger PRICE_GAP / ATR_SPIKE → archivé dans cette mise à jour

**Risques clés :**
1. **Cassure support $27.00** — ouverture vers $25.00–$26.00 (zone gap fill rally mai)
2. **Absence de catalyst avant earnings** (42 jours) — risque de dérive baissière continue sur manque d'intérêt
3. **Expiration options J-3 (2026-06-26)** — calls OTM $35–$40 risquent d'expirer sans valeur, pression vendeuse potentielle post-expiration
4. **Volume sous moyenne** — 0.63× signale un désintérêt institutionnel, pas de capitulation = pas de bottoming

**Prochain catalyst :** Earnings Q2 2026 le **2026-08-04** (42 jours) — Est EPS −$0.61 à −$0.45, Rev $0.1B

**Pas de position recommandée — ATTENDRE.**
