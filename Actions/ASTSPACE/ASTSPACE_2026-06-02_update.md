# ASTSPACE — Mise à jour Snapshot 21h UTC (2026-06-02)

> **Date :** 2026-06-02
> **Type :** Update après-clôture (snapshot 21:00 UTC)
> **Source :** data/latest.json (21h UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/upcoming_events_latest.json, data/validation_report.txt

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `ASTSPACE_2026-06-02_update.md` (snapshot 17:00 UTC)

| Élément | Snapshot 17h UTC | Snapshot 21h UTC | Changement |
|---------|----------------|------------------|------------|
| Erreur Yahoo ASTSPACE | `No price history` | `No price history` | **Stable — 32 snapshots consécutifs** |
| ASTS (proxy) close | **$115,27** | **$118,17** | **+2,52%** 🔴 |
| Volume ASTS (journée) | 13,18M (0,49×) | **20,93M (0,76×)** | **Recovery +58,8%** 🟡 |
| RSI ASTS | **71,77** | **72,58** | **+0,81 pts (surachat persistant)** 🔴 |
| ATR ASTS | **$12,07** | **$12,22** | **+$0,15** |
| MM 50j ASTS | **$87,62** | **$87,67** | **+$0,05** |
| Score ASTS (agent) | **29,8/100** (ÉVITER) | **29,8/100** (ÉVITER) | **Stable** |
| Score ASTSPACE (agent) | **55,2/100** (ATTENDRE) | **55,2/100** (ATTENDRE) | **Stable — placeholder** |
| Max Pain ASTS | **$120,00** | **$120,00** | **Stable** |
| Put/Call ASTS | **1,09** | **1,09** | **Stable** |
| Call OI % ASTS | **47,9%** | **47,9%** | **Stable** |
| Premium vs consensus ASTS | +21,9% | **+25,0%** | **Creusement mécanique +3,1 pp** 🔴 |
| Signal sectoriel | NEUTRAL | **NEUTRAL** | **Stable** |

**Constat :** Le snapshot 21h UTC confirme la **rupture technique majeure** sur le proxy ASTS. La clôture à **$118,17** (+11,85% sur la séance, +2,52% vs snapshot 17h) s'accompagne d'un **volume recovery partiel** à 0,76× la moyenne 20j (20,93M vs 27,45M), contre 0,49× à 17h. Le RSI persiste en **zone de surachat à 72,58** (>70). La divergence consensus se creuse mécaniquement à **+25,0%** ($118,17 vs PT $94,54). Le score agent ASTS reste **ÉVITER 29,8/100** — stable mais à un niveau extrêmement bas. Le signal sectoriel reste **NEUTRAL**. ASTSPACE reste totalement indisponible.

---

## 2. Mise à jour technique

### ASTSPACE (données officielles)

| Indicateur | Valeur 21h | Valeur 17h | Δ |
|-----------|-----------|-----------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 | Placeholder 50 | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing ASTSPACE :** [NON ÉVALUABLE] — absence totale de données techniques depuis 32+ snapshots.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 21h | Valeur 17h | Δ |
|-----------|-----------|-----------|---|
| Cours close | **$118,17** | $115,27 | **+2,52%** |
| Open | 109,91 | 109,91 | **Stable** |
| High intraday | **118,74** | 116,76 | **+1,98** |
| Low intraday | **108,80** | 108,80 | **Stable** |
| Volume (journée) | **20,93M** | 13,18M | **+7,75M** |
| Volume relatif | **0,76× moy. 20j** | 0,49× | **+0,27×** 🟡 |
| RSI 14j | **72,58** | 71,77 | **+0,81 pts** 🔴 |
| ATR 14j | **$12,22** | $12,07 | **+$0,15** |
| MM 50j | **$87,67** | $87,62 | **+$0,05** |
| Distance MM50j | **+34,7%** | +31,4% | **+3,3 pp** 🔴 |
| 52W high | 133,86 | 133,86 | Stable |
| Distance 52W high | **−11,7%** | −13,9% | **+2,2 pp** |
| Max pain options | **$120,00** | $120,00 | **Stable** |
| Put/call ratio | **1,09** | 1,09 | **Stable** |
| Call OI % | **47,9%** | 47,9% | **Stable** |

**Verdict timing ASTS (proxy) :** 🔴 **DÉFAVORABLE — HAUSSE PERSISTANTE SUR VOLUME RECOVERY PARTIEL** — Le cours clôture à $118,17 (+11,85% sur la séance) avec un volume recovery partiel à 0,76× la moyenne 20j (vs 0,49× à 17h). Le RSI persiste en **surachat (>70)** à 72,58. Le cours est désormais à **+34,7% au-dessus de la MM50** ($87,67), éloignant tout support proche. Le Max Pain $120,00 n'est plus qu'à **+1,5%** du cours (vs +4,1% à 17h), réduisant l'asymétrie gamma. L'expiration options **J+3** (2026-06-05) exerce une pression de pinning haussier atténuée par la proximité du cours avec le Max Pain.

---

## 3. Mise à jour fondamentale

### ASTSPACE (données officielles)

| Métrique | Valeur 21h | Valeur 17h | Δ |
|---------|-----------|-----------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

### ASTS (proxy)

| Métrique | Valeur 21h | Valeur 17h | Δ |
|---------|-----------|-----------|---|
| Market cap | **$45,86B** | $44,74B | **+$1,12B** |
| Forward P/E | **−397,70** | −387,94 | **−9,76** 🔴 |
| EV/Revenue (Yahoo) | **378,01×** | 378,01× | **Stable** |
| P/B (Yahoo) | **16,96×** | 16,55× | **+0,41×** 🔴 |
| Beta | 2,598 | 2,598 | Stable |
| Short interest | 17,60% | 17,60% | Stable |
| Consensus PT | $94,54 (12 analysts) | $94,54 (12 analysts) | Stable |
| Premium vs consensus | **+25,0%** | +21,9% | **Creusement mécanique +3,1 pp** 🔴 |

Aucun nouveau fondamental déclenché. La mutation est **exclusivement technique/pricing**. Le profil reste non rentable avec des multiples spéculatifs extrêmes. La divergence consensus se creuse mécaniquement à **+25,0%** ($118,17 vs $94,54) — risque de downgrades aggravé.

**Risque sectoriel :** Le signal sectoriel reste **NEUTRAL**. XLK (Technology) reste #1 du ranking (momentum score 10,0), mais XLC (Communication Services) est dans le **bottom 3** (momentum score 0,0). Le malus sectoriel persiste pour ASTS.

---

## 4. Mise à jour sentiment / options / news

- **News ASTSPACE :** aucune entrée Yahoo Finance ni FMP
- **News ASTS :** aucune entrée Yahoo Finance — silence médiatique total malgré le +11,85%
- **Options ASTS (stable vs snapshot 17h) :**
  - Max pain **$120,00** (écart **+1,5%** vs cours $118,17)
  - Put/call **1,09** (skew put modéré, sentiment légèrement baissier)
  - Call OI **47,9%** (domination call modérée)
  - Nearest expiry : **2026-06-05 (J+3)**
  - **Lecture :** le cours $118,17 est désormais extrêmement proche du Max Pain $120. Le pinning gamma à l'expiration J+3 exerce une pression haussière **fortement atténuée** (le gap s'est réduit de +13,6% à +1,5%). Le put/call 1,09 reste équilibré. Si le cours consolide autour de $118–$120 à l'approche de l'expiration, le max pain $120 reste un aimant haussier mais l'upside technique est désormais limité à ~+1,5%. Un rejet sous $118 renforcerait la pression baissière vers le support $115.
- **Social sentiment :** 0 mention Reddit pour ASTSPACE et ASTS — silence retail total malgré le +11,85%
- **Upgrades/downgrades ASTS :** 12 analysts, PT moyen $94,54 — stable. Risque de révisions à la baisse aggravé (divergence +25,0%)
- **Quant :** pas de signaux historiques pour ASTSPACE — p-value insuffisante (p=1,0, n=0)
- **Geo / Accounting / Events :** aucune donnée spécifique
- **FX exposure ASTSPACE :** exposition 25%, direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - ASTSPACE : earnings signalé le **2026-06-02** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (>5j de décalage)
  - ASTS : earnings le **2026-08-10** (`days_until: 69`) via yfinance, estimations EPS $−0,29 à $−0,17, Revenues $0,0B
- **Sector rotation :** signal **NEUTRAL** stable. Technology (XLK) top1 sector (momentum score 10,0). Communication Services (XLC) dans le **bottom 3** (momentum score 0,0). Malus sectoriel maintenu pour ASTS.

---

## 5. Scoring global

### ASTSPACE (données officielles — placeholder)

| Axe | Score 21h | Pondération | Note |
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

| Axe | Score 21h | Pondération | Note |
|-----|-----------|-------------|------|
| Catalyseur | 4,0/10 | 35% | Catalyseur absent, explosion non catalysée, earnings dans 69j |
| Valorisation | 3,0/10 | 40% | EV/Revenue 378×, divergence consensus +25,0% |
| Momentum | 5,5/10 | 25% | Cours $118,17 (+11,85%), RSI surachat 72,58, volume 0,76× |
| **Score Opportunité** | **4,0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39,8/100** | — | SURVEILLER |
| **Score Global Ajusté** | **29,8/100** | — | **ÉVITER** |

**Action recommandée par l'agent :** ÉVITER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle. Le score **29,8/100** est stable depuis le snapshot 17h. La configuration reste dégradée : explosion haussière non catalysée sur volume recovery partiel, RSI surachat persistant, divergence consensus extrême (+25,0%). L'agent maintient la thèse **ÉVITER**.

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

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — EXPLOSION TECHNIQUE DU PROXY ASTS +11,85% À $118,17 SUR VOLUME RECOVERY PARTIEL, SCORE ÉVITER 29,8/100 MAINTENU**

ASTSPACE n'est pas évaluable en l'état. La situation s'est dégradée sur le proxy ASTS :

1. **Anomalie structurelle confirmée :** ASTSPACE est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis 32+ snapshots consécutifs (erreur Yahoo : *No price history*).
2. **Explosion technique du proxy ASTS :** Clôture **$118,17** (+11,85% sur la séance, +2,52% vs snapshot 17h) sur **volume recovery partiel 0,76×** (20,93M vs moy. 27,45M). Le volume a doublé depuis le snapshot 17h (13,18M) mais reste sous la moyenne 20j.
3. **Détérioration technique persistante :** RSI en **surachat 72,58** (+0,81 pts vs 17h). Cours à +34,7% au-dessus de la MM50 ($87,67). Distance au 52W high réduite à −11,7%.
4. **Divergence consensus extrême aggravée :** Premium mécaniquement creusé à **+25,0%** ($118,17 vs PT $94,54). Risque de downgrades réactivé et aggravé.
5. **Score agent ASTS stable à ÉVITER :** Score global ajusté **29,8/100** maintenu — seuil ÉVITER (< 35) toujours franchi.
6. **Signal sectoriel stable :** NEUTRAL. XLK top1, XLC bottom3. Malus sectoriel maintenu.
7. **Options : pinning gamma très proche :** Max Pain $120,00 (écart +1,5% vs cours). Put/Call 1,09, Call OI 47,9%. L'expiration J+3 (2026-06-05) exerce une pression haussière **fortement atténuée** (gap réduit à +1,5%).
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings ASTSPACE le **2026-06-02** (`days_until: 0`), glissement persistant depuis le **29/05**.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer ASTSPACE de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence accrue :** Le niveau **$115,27** (close 17h) est le premier support immédiat. La **MM50 $87,67** reste le support structurel profond. La zone d'intérêt potentielle reste **$95–$100** (alignement consensus). Attention à l'expiration options **J+3** (2026-06-05) — le cours proche du Max Pain $120 réduit l'asymétrie technique à +1,5% uniquement. Le put/call 1,09 et le call OI < 50% indiquent une prudence persistante des options traders.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 21:00 UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/events_latest.json, data/validation_report.txt — aucune donnée hallucinée.*
