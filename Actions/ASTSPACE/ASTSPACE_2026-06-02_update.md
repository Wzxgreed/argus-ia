# ASTSPACE — Mise à Jour Snapshot 17h UTC (2026-06-02)

> **Date :** 2026-06-02
> **Type :** Update soir (snapshot 17:00 UTC)
> **Source :** data/latest.json (17h UTC), data/recommandations_2026-06-02.json, data/sector_rotation_2026-06-02.json, data/upcoming_events_2026-06-02.json, data/validation_report.txt

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `ASTSPACE_2026-06-02_update.md` (snapshot 13:00 UTC)

| Élément | Snapshot 13h UTC | Snapshot 17h UTC | Changement |
|---------|----------------|------------------|------------|
| Erreur Yahoo ASTSPACE | `No price history` | `No price history` | **Stable — 31+ snapshots consécutifs** |
| ASTS (proxy) close | **$105,65** | **$115,27** | **+9,11%** 🔴 |
| Volume ASTS (17h) | 27,11M (1,00×) | **13,18M (0,49×)** | **Collapse −51%** 🔴 |
| RSI ASTS | **61,89** | **71,77** | **+9,88 pts (surachat)** 🔴 |
| ATR ASTS | **$12,18** | **$12,07** | **−$0,11** |
| MM 50j ASTS | **$87,11** | **$87,62** | **+$0,51** |
| Score ASTS (agent) | **44,8/100** (SURVEILLER) | **29,8/100** (ÉVITER) | **−15 pts** 🔴 |
| Score ASTSPACE (agent) | **55,2/100** (ATTENDRE) | **55,2/100** (ATTENDRE) | **Stable — placeholder** |
| Max Pain ASTS | **$120,00** | **$120,00** | **Stable** |
| Put/Call ASTS | **1,09** | **1,09** | **Stable** |
| Call OI % ASTS | **47,9%** | **47,9%** | **Stable** |
| Premium vs consensus ASTS | +11,75% | **+21,9%** | **Creusement mécanique** 🔴 |
| Signal sectoriel | ROTATION_TO_CYCLICAL | **NEUTRAL** | **Neutralisation** 🟡 |

**Constat :** Le snapshot 17h UTC marque une **rupture technique majeure** sur le proxy ASTS : explosion haussière de **+9,11%** à **$115,27** sur un **volume collapse alarmant de 0,49×** (13,18M vs moy. 27,05M). Le RSI remonte brutalement en **zone de surachat à 71,77** (+9,88 pts). La divergence consensus se creuse mécaniquement à **−21,9%** ($115,27 vs PT $94,54). L'Agent Recommandation a downgradé ASTS de **SURVEILLER (44,8/100) à ÉVITER (29,8/100)**. Le signal sectoriel a été **neutralisé** : passage de `ROTATION_TO_CYCLICAL` à `NEUTRAL`. ASTSPACE reste totalement indisponible.

---

## 2. Mise à jour technique

### ASTSPACE (données officielles)

| Indicateur | Valeur 17h | Valeur 13h | Δ |
|-----------|-----------|-----------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 | Placeholder 50 | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing ASTSPACE :** [NON ÉVALUABLE] — absence totale de données techniques depuis 31+ snapshots.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 17h | Valeur 13h | Δ |
|-----------|-----------|-----------|---|
| Cours close | **$115,27** | $105,65 | **+9,11%** |
| Open | 109,91 | 108,67 | **+1,24** |
| High intraday | **116,76** | 111,28 | **+5,48** |
| Low intraday | **108,80** | 101,21 | **+7,59** |
| Volume (17h) | **13,18M** | 27,11M | **−13,93M** |
| Volume relatif | **0,49× moy. 20j** | 1,00× | **−0,51×** 🔴 |
| RSI 14j | **71,77** | 61,89 | **+9,88 pts** 🔴 |
| ATR 14j | **$12,07** | $12,18 | **−$0,11** |
| MM 50j | **$87,62** | $87,11 | **+$0,51** |
| Distance MM50j | **+31,4%** | +21,3% | **+10,1 pp** |
| 52W high | 133,86 | 133,86 | Stable |
| Distance 52W high | **−13,9%** | −21,1% | **+7,2 pp** |
| Max pain options | **$120,00** | $120,00 | **Stable** |
| Put/call ratio | **1,09** | 1,09 | **Stable** |
| Call OI % | **47,9%** | 47,9% | **Stable** |

**Verdict timing ASTS (proxy) :** 🔴 **DÉFAVORABLE — HAUSSE ANÉMIQUE SUR VOLUME COLLAPSE** — Le cours bondit de +9,11% à $115,27 mais sur un volume effondré à 0,49× la moyenne 20j, signalant une hausse sans participation institutionnelle. Le RSI retourne en **surachat (>70)** à 71,77, réactivant le risque de correction technique. Le cours est désormais à **+31,4% au-dessus de la MM50** ($87,62), éloignant tout support proche. Le low intraday $108,80 correspond approximativement à l'open du jour ($109,91) et constitue le premier support immédiat. La résistance $116,76 (high intraday) est à seulement **+4,1% du Max Pain $120,00**.

---

## 3. Mise à jour fondamentale

### ASTSPACE (données officielles)

| Métrique | Valeur 17h | Valeur 13h | Δ |
|---------|-----------|-----------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

### ASTS (proxy)

| Métrique | Valeur 17h | Valeur 13h | Δ |
|---------|-----------|-----------|---|
| Market cap | **$44,74B** | $41,01B | **+$3,73B** |
| Forward P/E | **−387,94** | −355,57 | **−32,37** 🔴 |
| EV/Revenue (Yahoo) | **378,01×** | 378,00× | **Stable** |
| P/B (Yahoo) | **16,55×** | 15,16× | **+1,39×** 🔴 |
| Beta | 2,598 | 2,598 | Stable |
| Short interest | 17,60% | 17,60% | Stable |
| Consensus PT | $94,54 (12 analysts) | $94,54 (12 analysts) | Stable |
| Premium vs consensus | **+21,9%** | +11,75% | **Creusement mécanique** 🔴 |

Aucun nouveau fondamental déclenché. La mutation est **exclusivement technique/pricing**. Le profil reste non rentable avec des multiples spéculatifs extrêmes. La divergence consensus se creuse mécaniquement à **+21,9%** ($115,27 vs $94,54) — risque de downgrades réactivé et aggravé.

**Risque sectoriel :** Le signal sectoriel a été **neutralisé** : passage de `ROTATION_TO_CYCLICAL` à `NEUTRAL`. XLK (Technology) reste #1 du ranking (momentum score 10,0), mais XLC (Communication Services) est dans le **bottom 3** (momentum score 0,0). La suppression du tailwind cyclique growth neutralise un potentiel support pour ASTS.

---

## 4. Mise à jour sentiment / options / news

- **News ASTSPACE :** aucune entrée Yahoo Finance ni FMP
- **News ASTS :** aucune entrée Yahoo Finance — silence médiatique total malgré le +9,11%
- **Options ASTS (stable vs snapshot 13h) :**
  - Max pain **$120,00** (écart **+4,1%** vs cours $115,27)
  - Put/call **1,09** (skew put modéré, sentiment légèrement baissier)
  - Call OI **47,9%** (domination call modérée)
  - Nearest expiry : **2026-06-05 (J+3)**
  - **Lecture :** le cours $115,27 est désormais beaucoup plus proche du Max Pain $120. Le pinning gamma à l'expiration J+3 exerce une pression haussière **atténuée** (le gap s'est réduit de +13,6% à +4,1%). Le put/call 1,09 reste équilibré. Si le cours consolide autour de $115–$116 à l'approche de l'expiration, le max pain $120 reste un aimant haussier mais l'upside technique est désormais limité à ~+4%
- **Social sentiment :** 0 mention Reddit pour ASTSPACE et ASTS — silence retail total malgré le +9,11%
- **Upgrades/downgrades ASTS :** 12 analysts, PT moyen $94,54 — stable. Risque de révisions à la baisse réactivé (divergence −21,9%)
- **Quant :** pas de signaux historiques pour ASTSPACE — p-value insuffisante (p=1,0, n=0)
- **Geo / Accounting / Events :** aucune donnée spécifique
- **FX exposure ASTSPACE :** exposition 25%, direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - ASTSPACE : earnings signalé le **2026-06-02** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (>5j de décalage)
  - ASTS : earnings le **2026-08-10** (`days_until: 69`) via yfinance, estimations EPS $−0,29 à $−0,17, Revenues $0,0B
- **Sector rotation :** signal **NEUTRAL** (was ROTATION_TO_CYCLICAL au snapshot 13h). Technology (XLK) top1 sector (momentum score 10,0). Communication Services (XLC) dans le **bottom 3** (momentum score 0,0). Malus sectoriel maintenu pour ASTS. La neutralisation du signal macro supprime un potentiel tailwind pour les cycliques growth.

---

## 5. Scoring global

### ASTSPACE (données officielles — placeholder)

| Axe | Score 17h | Pondération | Note |
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

| Axe | Score 17h | Pondération | Note |
|-----|-----------|-------------|------|
| Catalyseur | 4,0/10 | 35% | Catalyseur absent, explosion non catalysée, earnings dans 69j |
| Valorisation | 3,0/10 | 40% | EV/Revenue 378×, divergence consensus −21,9% |
| Momentum | 5,5/10 | 25% | Cours $115,27 (+9,11%), RSI surachat 71,77, volume 0,49× |
| **Score Opportunité** | **4,0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39,8/100** | — | SURVEILLER |
| **Score Global Ajusté** | **29,8/100** | — | **ÉVITER** |

**Action recommandée par l'agent :** ÉVITER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle. Le score **29,8/100** est un downgrade de **15 points** depuis le snapshot 13h (44,8/100). La configuration s'est dégradée : explosion haussière non catalysée sur volume collapse, RSI surachat, divergence consensus extrême. L'agent a reclassé la thèse de **SURVEILLER à ÉVITER**.

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
| Prix entrée | Cours close | $115,27 |
| Stop-loss | $115,27 − 2×12,07 | **$91,13** |
| Take-profit | $115,27 + 3×12,07 | **$151,48** |
| Ratio R/R | (151,48−115,27)/(115,27−91,13) | **1,5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle. Le SL à $91,13 correspond approximativement à la zone de support $91–$95 (gap entre le low précédent et la MM50). Le TP $151,48 est 13,2% au-dessus du 52W high ($133,86) — probabilité d'atteinte très faible sans catalyseur majeur. La zone d'intérêt potentielle reste **$95–$100** (alignement consensus). Le ratio R/R 1,5 est inchangé mais le risque de slippage vers le SL est accru (RSI surachat, volume collapse).

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — EXPLOSION TECHNIQUE DU PROXY ASTS +9,11% SUR VOLUME COLLAPSE, DOWNGRADE AGENT DE SURVEILLER À ÉVITER**

ASTSPACE n'est pas évaluable en l'état. La situation s'est dégradée sur le proxy ASTS :

1. **Anomalie structurelle confirmée :** ASTSPACE est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis 31+ snapshots consécutifs (erreur Yahoo : *No price history*).
2. **Explosion technique du proxy ASTS :** Cours **$115,27** (+9,11% vs snapshot 13h) sur **volume collapse alarmant 0,49×** (13,18M vs moy. 27,05M). Mouvement fragile, probablement driven par gamma/options et short covering.
3. **Détérioration technique :** RSI remonté en **surachat 71,77** (+9,88 pts). Cours à +31,4% au-dessus de la MM50 ($87,62). Distance au 52W high réduite à −13,9%.
4. **Divergence consensus extrême :** Premium mécaniquement creusé à **+21,9%** ($115,27 vs PT $94,54). Risque de downgrades réactivé et aggravé.
5. **Downgrade agent ASTS :** Score global ajusté chuté de **44,8/100 (SURVEILLER) à 29,8/100 (ÉVITER)** — perte de 15 points. Seuil ÉVITER (< 35) franchi.
6. **Signal sectoriel neutralisé :** Passage de `ROTATION_TO_CYCLICAL` à `NEUTRAL`. XLK top1, XLC bottom3. Malus sectoriel maintenu.
7. **Options stable mais risque gamma réduit :** Max Pain $120,00 (écart +4,1% vs cours). Put/Call 1,09, Call OI 47,9%. Le pinning gamma à J+3 exerce une pression haussière atténuée (gap réduit).
8. **Earnings placeholder glissant non résolu :** FMP signale un earnings ASTSPACE le **2026-06-02** (`days_until: 0`), glissement persistant depuis le **29/05**.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer ASTSPACE de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence accrue :** Le niveau **$108,80** (low du jour) est le premier support immédiat. La **MM50 $87,62** reste le support structurel profond. La zone d'intérêt potentielle reste **$95–$100** (alignement consensus). Attention à l'expiration options **J+3** (2026-06-05) — le cours proche du Max Pain $120 réduit l'asymétrie technique. Le put/call 1,09 et le call OI < 50% indiquent une prudence persistante des options traders.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 17:00 UTC), data/recommandations_2026-06-02.json, data/sector_rotation_2026-06-02.json, data/upcoming_events_2026-06-02.json, data/social_sentiment_2026-06-02.json, data/fx_exposure_2026-06-02.json, data/events_2026-06-02.json, data/validation_report.txt — aucune donnée hallucinée.*
