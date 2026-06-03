# ASTSPACE — Mise à jour Snapshot 10h UTC (2026-06-03)

> **Date :** 2026-06-03
> **Type :** Update matin (snapshot 10:00 UTC)
> **Source :** data/latest.json (10h UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/upcoming_events_latest.json, data/validation_report.txt, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `ASTSPACE_2026-06-02_update.md` (snapshot 21:00 UTC)

| Élément | Snapshot 21h UTC 02/06 | Snapshot 10h UTC 03/06 | Changement |
|---------|----------------------|------------------------|------------|
| Erreur Yahoo ASTSPACE | `No price history` | `No price history` | **Stable — 33 snapshots consécutifs** |
| ASTS (proxy) close | **$118,17** | **$118,17** | **Stable** |
| Volume ASTS (journée) | 20,93M (0,76×) | **21,29M (0,78×)** | **Stable (+1,7%)** |
| RSI ASTS | **72,58** | **72,58** | **Inchangé (surachat persistant)** |
| ATR ASTS | **$12,22** | **$12,22** | **Inchangé** |
| MM 50j ASTS | **$87,67** | **$87,67** | **Inchangé** |
| Score ASTS (agent) | **29,8/100** (ÉVITER) | **29,8/100** (ÉVITER) | **Stable** |
| Score ASTSPACE (agent) | **55,2/100** (ATTENDRE) | **55,2/100** (ATTENDRE) | **Stable — placeholder** |
| Max Pain ASTS (JSON) | **$120,00** | **$40,00** | **Anomalie JSON détectée** 🔴 |
| Max Pain ASTS (opérationnel) | **$120,00** | **$120,00** | **Stable (valeur conservée)** |
| Put/Call ASTS (JSON) | **1,09** | **null** | **Anomalie JSON détectée** 🔴 |
| Put/Call ASTS (opérationnel) | **1,09** | **1,09** | **Stable (valeur conservée)** |
| Call OI % ASTS (JSON) | **47,9%** | **null** | **Anomalie JSON détectée** 🔴 |
| Call OI % ASTS (opérationnel) | **47,9%** | **47,9%** | **Stable (valeur conservée)** |
| EV/Revenue ASTS (Yahoo) | **378,01×** | **422,04×** | **+44,0× mécanique** 🔴 |
| Premium vs consensus ASTS | +25,0% | **+25,0%** | **Stable** |
| Signal sectoriel | NEUTRAL | **NEUTRAL** | **Stable** |
| Earnings placeholder ASTSPACE | J=0 (02/06) | **J=0 (03/06)** | **Glissement persistant** 🔴 |

**Constat :** Le snapshot 10h UTC confirme la **stabilité totale** du proxy ASTS. La clôture reste à **$118,17** avec un volume stable à **0,78×** la moyenne 20j (21,29M vs 27,47M). Le RSI persiste en **zone de surachat à 72,58** (>70). Le score agent ASTS reste **ÉVITER 29,8/100** — stable à un niveau extrêmement bas. Le signal sectoriel reste **NEUTRAL**. ASTSPACE reste totalement indisponible.

**Anomalies JSON détectées et traitées :**
- Max Pain Yahoo est passé de $120,00 à **$40,00** dans le JSON (aberrant, écart −66% vs cours) → **valeur opérationnelle $120,00 conservée**
- Put/Call ratio passé à **null** dans le JSON → **valeur opérationnelle 1,09 conservée**
- Call OI % passé à **null** dans le JSON → **valeur opérationnelle 47,9% conservée**

**Mutation fondamentale mécanique :** EV/Revenue Yahoo est remonté mécaniquement de 378,01× à **422,04×** (+44,0× vs veille). Cette augmentation est probablement liée à une mise à jour du denominateur (revenue LTM) dans la base Yahoo plutôt qu'à un mouvement de valorisation réel. Le cours étant inchangé, le multiple s'est mécaniquement gonflé.

---

## 2. Mise à jour technique

### ASTSPACE (données officielles)

| Indicateur | Valeur 10h | Valeur 21h 02/06 | Δ |
|-----------|-----------|------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 | Placeholder 50 | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing ASTSPACE :** [NON ÉVALUABLE] — absence totale de données techniques depuis 33+ snapshots.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 10h | Valeur 21h 02/06 | Δ |
|-----------|-----------|------------------|---|
| Cours close | **$118,17** | $118,17 | **Stable** |
| Open | 109,91 | 109,91 | **Stable** |
| High intraday | **118,74** | 118,74 | **Stable** |
| Low intraday | **108,80** | 108,80 | **Stable** |
| Volume (journée) | **21,29M** | 20,93M | **+0,36M (+1,7%)** |
| Volume relatif | **0,78× moy. 20j** | 0,76× | **Stable** |
| RSI 14j | **72,58** | 72,58 | **Inchangé** 🔴 |
| ATR 14j | **$12,22** | $12,22 | **Inchangé** |
| MM 50j | **$87,67** | $87,67 | **Inchangé** |
| Distance MM50j | **+34,7%** | +34,7% | **Stable** 🔴 |
| 52W high | 133,86 | 133,86 | Stable |
| Distance 52W high | **−11,7%** | −11,7% | **Stable** |
| Max pain options (opérationnel) | **$120,00** | $120,00 | **Stable** |
| Put/call ratio (opérationnel) | **1,09** | 1,09 | **Stable** |
| Call OI % (opérationnel) | **47,9%** | 47,9% | **Stable** |

**Verdict timing ASTS (proxy) :** 🔴 **DÉFAVORABLE — SURACHAT PERSISTANT SUR VOLUME SOUS MOYENNE** — Le cours reste figé à $118,17 avec un volume stable à 0,78× la moyenne 20j. Le RSI persiste en **surachat (>70)** à 72,58. Le cours est à **+34,7% au-dessus de la MM50** ($87,67), éloignant tout support proche. Le Max Pain $120,00 n'est plus qu'à **+1,5%** du cours, réduisant l'asymétrie gamma. L'expiration options **J+2** (2026-06-05) exerce une pression de pinning haussier atténuée par la proximité du cours avec le Max Pain.

---

## 3. Mise à jour fondamentale

### ASTSPACE (données officielles)

| Métrique | Valeur 10h | Valeur 21h 02/06 | Δ |
|---------|-----------|------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

### ASTS (proxy)

| Métrique | Valeur 10h | Valeur 21h 02/06 | Δ |
|---------|-----------|------------------|---|
| Market cap | **$45,86B** | $45,86B | **Stable** |
| Forward P/E | **−397,70** | −397,70 | **Stable** 🔴 |
| EV/Revenue (Yahoo) | **422,04×** | 378,01× | **+44,0× mécanique** 🔴 |
| P/B (Yahoo) | **16,96×** | 16,96× | **Stable** 🔴 |
| Beta | 2,598 | 2,598 | Stable |
| Short interest | 17,60% | 17,60% | Stable |
| Consensus PT | $94,54 (12 analysts) | $94,54 (12 analysts) | Stable |
| Premium vs consensus | **+25,0%** | +25,0% | **Stable** 🔴 |

Aucun nouveau fondamental déclenché. La mutation est **exclusivement mécanique** (EV/Revenue gonflé de +44,0× sans mouvement de cours). Le profil reste non rentable avec des multiples spéculatifs extrêmes. La divergence consensus reste **+25,0%** ($118,17 vs PT $94,54) — risque de downgrades persistant.

**Risque sectoriel :** Le signal sectoriel reste **NEUTRAL**. XLK (Technology) reste #1 du ranking (momentum score 10,0), mais XLC (Communication Services) est dans le **bottom 3** (momentum score 0,0). Le malus sectoriel persiste pour ASTS.

---

## 4. Mise à jour sentiment / options / news

- **News ASTSPACE :** aucune entrée Yahoo Finance ni FMP
- **News ASTS :** aucune entrée Yahoo Finance — silence médiatique total malgré le niveau élevé
- **Options ASTS (anomalie JSON détectée et traitée) :**
  - Max pain JSON brut : **$40,00** (aberrant, écart −66% vs cours) → **valeur opérationnelle $120,00 conservée**
  - Put/Call JSON brut : **null** → **valeur opérationnelle 1,09 conservée**
  - Call OI % JSON brut : **null** → **valeur opérationnelle 47,9% conservée**
  - Max pain opérationnel : **$120,00** (écart **+1,5%** vs cours $118,17)
  - Put/call opérationnel : **1,09** (skew put modéré, sentiment légèrement baissier)
  - Call OI opérationnel : **47,9%** (domination call modérée)
  - Nearest expiry : **2026-06-05 (J+2)**
  - **Lecture :** le cours $118,17 reste extrêmement proche du Max Pain $120. Le pinning gamma à l'expiration J+2 exerce une pression haussière **fortement atténuée** (gap +1,5%). Le put/call 1,09 reste équilibré. Si le cours consolide autour de $118–$120 à l'approche de l'expiration, le max pain $120 reste un aimant haussier mais l'upside technique est désormais limité à ~+1,5%. Un rejet sous $118 renforcerait la pression baissière vers le support $115.
- **Social sentiment :** 0 mention Reddit pour ASTSPACE et ASTS — silence retail total
- **Upgrades/downgrades ASTS :** 12 analysts, PT moyen $94,54 — stable. Risque de révisions à la baisse persistant (divergence +25,0%)
- **Quant :** pas de signaux historiques pour ASTSPACE — p-value insuffisante (p=1,0, n=0)
- **Geo / Accounting / Events :** aucune donnée spécifique
- **FX exposure ASTSPACE :** exposition 25%, direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - ASTSPACE : earnings signalé le **2026-06-03** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (>6j de décalage, glissé du 29/05 au 03/06)
  - ASTS : earnings le **2026-08-10** (`days_until: 68`) via yfinance, estimations EPS $−0,29 à $−0,17, Revenues $0,0B
- **Sector rotation :** signal **NEUTRAL** stable. Technology (XLK) top1 sector (momentum score 10,0). Communication Services (XLC) dans le **bottom 3** (momentum score 0,0). Malus sectoriel maintenu pour ASTS.

---

## 5. Scoring global

### ASTSPACE (données officielles — placeholder)

| Axe | Score 10h | Pondération | Note |
|-----|-----------|-------------|------|
| Catalyseur | 6,5/10 (placeholder) | 35% | [NON FONDÉ] |
| Valorisation | 5,0/10 (placeholder) | 40% | [NON FONDÉ] |
| Momentum | 5,0/10 (placeholder) | 25% | [NON FONDÉ] |
| **Score Opportunité** | **5,5/10** | — | Placeholder — **non utilisable** |
| **Score Global** | **55,2/100** | — | Placeholder — **non utilisable** |
| **Score Global Ajusté** | **55,2/100** | — | Placeholder — **non utilisable** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, à titre indicatif uniquement)

| Axe | Score 10h | Pondération | Note |
|-----|-----------|-------------|------|
| Catalyseur | 4,0/10 | 35% | Catalyseur absent, explosion non catalysée, earnings dans 68j |
| Valorisation | 3,0/10 | 40% | EV/Revenue 422×, divergence consensus +25,0% |
| Momentum | 5,5/10 | 25% | Cours $118,17 (stable), RSI surachat 72,58, volume 0,78× |
| **Score Opportunité** | **4,0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39,8/100** | — | SURVEILLER |
| **Score Global Ajusté** | **29,8/100** | — | **ÉVITER** |

**Action recommandée par l'agent :** ÉVITER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle. Le score **29,8/100** est stable depuis le snapshot 21h 02/06. La configuration reste dégradée : cours surévalué sur volume sous moyenne, RSI surachat persistant, divergence consensus extrême (+25,0%). L'agent maintient la thèse **ÉVITER**.

---

## 6. Niveaux SL / TP / Ratio R/R

### ASTSPACE (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy, à titre indicatif uniquement)

| Niveau | Calcul | Valeur |
|--------|--------|--------|
| Prix entrée | Cours close | $118,17 |
| Stop-loss | $118,17 − 2×12,22 | **$93,73** |
| Take-profit | $118,17 + 3×12,22 | **$154,83** |
| Ratio R/R | (154,83−118,17)/(118,17−93,73) | **1,5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle. Le SL à $93,73 correspond approximativement à la zone de support $93–$95 (gap entre le low précédent et la MM50). Le TP $154,83 est 15,7% au-dessus du 52W high ($133,86) — probabilité d'atteinte très faible sans catalyseur majeur. La zone d'intérêt potentielle reste **$95–$100** (alignement consensus). Le ratio R/R 1,5 est inchangé mais le risque de slippage vers le SL est accru (RSI surachat, volume sous moyenne).

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — STABILITÉ TOTALE DU PROXY ASTS À $118,17 SUR VOLUME 0,78×, RSI SURACHAT 72,58 PERSISTANT, SCORE ÉVITER 29,8/100 MAINTENU, ANOMALIES OPTIONS JSON TRAITÉES**

ASTSPACE n'est pas évaluable en l'état. La situation est stable sur le proxy ASTS :

1. **Anomalie structurelle confirmée :** ASTSPACE est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis 33+ snapshots consécutifs (erreur Yahoo : *No price history*).
2. **Stabilité technique du proxy ASTS :** Cours **$118,17** (inchangé vs close 02/06), volume **21,29M** (0,78× moy. 27,47M), RSI **72,58** (inchangé, surachat), ATR **$12,22** (inchangé), MM50 **$87,67** (inchangée).
3. **Anomalies options JSON détectées et traitées :** Max Pain brut $40,00 (aberrant) → **valeur opérationnelle $120,00 conservée**. Put/Call et Call OI passés à null dans le JSON → **valeurs opérationnelles 1,09 et 47,9% conservées**.
4. **Mutation fondamentale mécanique :** EV/Revenue remonté de 378,01× à **422,04×** (+44,0×) sans mouvement de cours — gonflement mécanique du denominateur.
5. **Divergence consensus stable :** Premium mécanique **+25,0%** ($118,17 vs PT $94,54). Risque de downgrades persistant.
6. **Score agent ASTS stable à ÉVITER :** Score global ajusté **29,8/100** maintenu — seuil ÉVITER (< 35) toujours franchi.
7. **Signal sectoriel stable :** NEUTRAL. XLK top1, XLC bottom3. Malus sectoriel maintenu.
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings ASTSPACE le **2026-06-03** (`days_until: 0`), glissement persistant depuis le **29/05** (>6j de décalage).

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer ASTSPACE de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence accrue :** Le niveau **$118,17** est le premier support immédiat. La **MM50 $87,67** reste le support structurel profond. La zone d'intérêt potentielle reste **$95–$100** (alignement consensus). Attention à l'expiration options **J+2** (2026-06-05) — le cours proche du Max Pain $120 réduit l'asymétrie technique à +1,5% uniquement. Le put/call 1,09 et le call OI < 50% indiquent une prudence persistante des options traders.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 10:00 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/events_latest.json, data/validation_report.txt — aucune donnée hallucinée.*
