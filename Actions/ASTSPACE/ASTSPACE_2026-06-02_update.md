# ASTSPACE — Mise à Jour Snapshot 13h UTC (2026-06-02)

> **Date :** 2026-06-02
> **Type :** Update intraday (snapshot 13:00 UTC)
> **Source :** data/latest.json (13h UTC), data/recommandations_2026-06-02.json, data/sector_rotation_2026-06-02.json, data/upcoming_events_2026-06-02.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `ASTSPACE_2026-06-02_update.md` (snapshot 10:00 UTC)

| Élément | Snapshot 10h UTC | Snapshot 13h UTC | Changement |
|---------|------------------|------------------|------------|
| Erreur Yahoo ASTSPACE | `No price history` | `No price history` | **Stable — >30 snapshots consécutifs** |
| ASTS (proxy) close | **$105,65** | **$105,65** | **Stable** |
| Volume ASTS (total j.) | 27,07M (1,00×) | **27,11M** (1,00×) | **Stable** |
| RSI ASTS | **61,89** | **61,89** | **Stable** |
| ATR ASTS | **$12,18** | **$12,18** | **Stable** |
| MM 50j ASTS | **$87,11** | **$87,11** | **Stable** |
| Score ASTS (agent) | **44,8/100** (SURVEILLER) | **44,8/100** (SURVEILLER) | **Stable** |
| Score ASTSPACE (agent) | **55,2/100** (ATTENDRE) | **55,2/100** (ATTENDRE) | **Stable — placeholder** |
| Max Pain ASTS | **$40,00** (aberrant) | **$120,00** | **RÉSOLU** |
| Put/Call ASTS | **null** (corrompu) | **1,09** | **RÉSOLU** |
| Call OI % ASTS | **null** (corrompu) | **47,9%** | **RÉSOLU** |
| Premium vs consensus ASTS | +11,75% | +11,75% | **Stable** |
| Signal sectoriel | ROTATION_TO_CYCLICAL | ROTATION_TO_CYCLICAL | **Stable** |

**Constat :** Le snapshot 13h UTC confirme une **stabilité totale** des paramètres de marché du proxy ASTS. Le cours reste à **$105,65**, le RSI à **61,89**, le volume normalisé à **1,00×**. L'anomalie data quality détectée au snapshot 10h (Max Pain $40,00, Put/Call et Call OI null) est **résolue** : les données options sont de nouveau cohérentes (Max Pain $120,00, Put/Call 1,09, Call OI 47,9%). ASTSPACE reste totalement indisponible (erreur Yahoo persistante).

---

## 2. Mise à jour technique

### ASTSPACE (données officielles)

| Indicateur | Valeur 13h | Valeur 10h | Δ |
|-----------|-----------|-----------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 | Placeholder 50 | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing ASTSPACE :** [NON ÉVALUABLE] — absence totale de données techniques.

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur 13h | Valeur 10h | Δ |
|-----------|-----------|-----------|---|
| Cours close | **$105,65** | $105,65 | **—** |
| Open | 108,67 | 108,67 | — |
| High intraday | 111,28 | 111,28 | — |
| Low intraday | **101,21** | 101,21 | — |
| Volume (total j.) | **27,11M** | 27,07M | **+0,04M** |
| Volume relatif | **1,00× moy. 20j** | 1,00× | — |
| RSI 14j | **61,89** | 61,89 | — |
| ATR 14j | **$12,18** | $12,18 | — |
| MM 50j | **$87,11** | $87,11 | — |
| Distance MM50j | **+21,3%** | +21,3% | — |
| 52W high | 133,86 | 133,86 | Stable |
| Distance 52W high | **−21,1%** | −21,1% | — |
| Max pain options | **$120,00** | $40,00 (aberrant) | **RÉSOLU** |
| Put/call ratio | **1,09** | null | **RÉSOLU** |
| Call OI % | **47,9%** | null | **RÉSOLU** |

**Verdict timing ASTS (proxy) :** 🟡 **STABILITÉ TOTALE — ANOMALIE OPTIONS RÉSOLUE** — Le cours reste figé à $105,65 (clôture 2026-06-01 non révisée à ce stade intraday, les marchés US ouvrant à 13h30 UTC en juin). RSI 61,89 dans la zone neutre-haussière. Low $101,21 approche le support psychologique $100. L'anomalie options est résolue : Max Pain $120,00 rétabli (cohérent avec l'historique), mais le Put/Call a grimpé de **0,92 à 1,09** et le Call OI a reculé de **52,2% à 47,9%** depuis le snapshot 21h UTC 2026-06-01. Cette rotation vers les puts indique un léger pessimisme croissant des options traders à l'approche de l'expiration du 05/06 (J+3).

---

## 3. Mise à jour fondamentale

### ASTSPACE (données officielles)

| Métrique | Valeur 13h | Valeur 10h | Δ |
|---------|-----------|-----------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

### ASTS (proxy)

| Métrique | Valeur 13h | Valeur 10h | Δ |
|---------|-----------|-----------|---|
| Market cap | **$41,01B** | $41,01B | **—** |
| Forward P/E | **−355,57** | −355,57 | **—** |
| EV/Revenue | **378,00×** | 378,00× | **—** |
| P/B (Yahoo) | **15,16×** | 15,16× | **—** |
| Beta | 2,598 | 2,598 | Stable |
| Short interest | 17,60% | 17,60% | Stable |
| Consensus PT | $94,54 (12 analysts) | $94,54 (12 analysts) | Stable |
| Premium vs consensus | **+11,75%** | +11,75% | **—** |

Aucun nouveau fondamental. Le profil reste non rentable avec des multiples spéculatifs extrêmes. La divergence consensus reste creusée à **+11,75%** ($105,65 vs $94,54).

---

## 4. Mise à jour sentiment / options / news

- **News ASTSPACE :** aucune entrée Yahoo Finance ni FMP
- **News ASTS :** aucune entrée Yahoo Finance — silence médiatique total
- **Options ASTS (résolution anomalie) :**
  - Max pain **$120,00** (rétabli vs aberration $40,00 au snapshot 10h) — écart **+13,6%** vs cours $105,65
  - Put/call **1,09** (vs 0,92 au snapshot 21h UTC 2026-06-01) — **+0,17**, indicateur de prudence croissante
  - Call OI % **47,9%** (vs 52,2% au snapshot 21h UTC 2026-06-01) — **−4,3 pp**, baisse de l'exposition call
  - Nearest expiry : **2026-06-05 (J+3)**
  - **Lecture :** avec un put/call > 1 et un call OI < 50%, la configuration options est légèrement baissière à court terme. Le cours sous max pain ($120) reste favorable à un pinning gamma haussier vers $120, mais la rotation vers les puts atténue ce signal
- **Social sentiment :** 0 mention Reddit pour ASTSPACE et ASTS — silence retail
- **Upgrades/downgrades ASTS :** 12 analysts, PT moyen $94,54 — stable
- **Quant :** pas de signaux historiques pour ASTSPACE — p-value insuffisante (p=1,0, n=0)
- **Geo / Accounting / Events :** aucune donnée spécifique
- **FX exposure ASTSPACE :** exposition 25%, direction neutral, impact 0% — pas de facteur FX identifiable
- **Upcoming events :**
  - ASTSPACE : earnings signalé le **2026-06-02** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (>5j de décalage)
  - ASTS : earnings le **2026-08-10** (`days_until: 69`) via yfinance, estimations EPS $−0,29 à $−0,17, Revenues $0,0B
- **Sector rotation :** signal **ROTATION_TO_CYCLICAL** stable. Technology (XLK) top1 sector (momentum score 10,0). Communication Services (XLC) dans le **bottom 3** (momentum score 0,0). Malus sectoriel maintenu pour ASTS.

---

## 5. Scoring global

### ASTSPACE (données officielles — placeholder)

| Axe | Score 13h | Pondération | Note |
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

| Axe | Score 13h | Pondération | Note |
|-----|-----------|-------------|------|
| Catalyseur | 4,0/10 | 35% | Catalyseur absent, rebond non catalysé, earnings dans 69j |
| Valorisation | 3,0/10 | 40% | EV/Revenue 378×, divergence consensus −10,5% |
| Momentum | 5,5/10 | 25% | Cours stable $105,65, RSI 61,89, volume 1,00× |
| **Score Opportunité** | **4,0/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **39,8/100** | — | SURVEILLER |
| **Score Global Ajusté** | **44,8/100** | — | **SURVEILLER** |

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Neutre
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle. Le score **44,8/100** reste stable. La configuration est inchangée : profil spéculatif, divergence consensus, absence de catalyseur. La rotation options (put/call 1,09, call OI 47,9%) n'a pas suffi à dégrader le score global, mais elle renforce la prudence sur l'expiration J+3.

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
| Prix entrée | Cours close | $105,65 |
| Stop-loss | $105,65 − 2×12,18 | **$81,29** |
| Take-profit | $105,65 + 3×12,18 | **$142,19** |
| Ratio R/R | (142,19−105,65)/(105,65−81,29) | **1,5** |

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces niveaux sont fournis uniquement pour confirmer l'anomalie structurelle. Le SL à $81,29 correspond approximativement à la MM50 ($87,11) moins une marge de volatilité. Le TP $142,19 est 6,2% au-dessus du 52W high ($133,86) — probabilité d'atteinte faible sans catalyseur majeur. La zone d'intérêt potentielle reste **$95–$100** (alignement consensus). Avec le put/call remonté à 1,09 et le call OI sous 50%, le risque de continuation baissière vers le consensus est légèrement accru.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — STABILITÉ TOTALE DU PROXY ASTS, ANOMALIE OPTIONS RÉSOLUE**

ASTSPACE n'est pas évaluable en l'état. La situation reste structurellement inchangée :

1. **Anomalie structurelle confirmée :** ASTSPACE est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis >30 snapshots consécutifs (erreur Yahoo : *No price history*).
2. **Stabilité technique totale du proxy ASTS :** Cours $105,65, RSI 61,89, ATR $12,18, MM50 $87,11 — tous strictement identiques au snapshot 10h UTC et au close 21h UTC 2026-06-01.
3. **Résolution de l'anomalie options :** Max Pain $120,00 rétabli (vs aberration $40,00 au snapshot 10h). Put/Call 1,09 et Call OI 47,9% de nouveau disponibles. Cependant, la rotation vers les puts (0,92 → 1,09) et la baisse du call OI (52,2% → 47,9%) depuis le 01/06 indiquent une prudence croissante des options traders à l'approche de l'expiration J+3 (2026-06-05).
4. **Score agent ASTS :** stable à **44,8/100** (ajusté), catégorie SURVEILLER. Pas de mutation de scoring.
5. **Signal sectoriel stable :** ROTATION_TO_CYCLICAL. XLK top1, XLC bottom3. Malus sectoriel maintenu.
6. **Earnings placeholder glissant non résolu :** FMP signale un earnings ASTSPACE le **2026-06-02** (`days_until: 0`), glissement persistant depuis le **29/05**.
7. **Volume stable :** 27,11M vs moyenne 20j 27,02M = 1,00×. Normalisation maintenue.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer ASTSPACE de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS** pour un éventuel retest. Le niveau **$100** reste le support psychologique immédiat (low du jour $101,21). La **MM50 $87,11** est le support structurel plus profond. La zone d'intérêt potentielle reste **$95–$100** (alignement consensus). Attention à l'expiration options **J+3** (2026-06-05) avec un put/call remonté à 1,09 — risque gamma baissier accru si le cours casse sous $100.

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 13:00 UTC), data/recommandations_2026-06-02.json, data/sector_rotation_2026-06-02.json, data/upcoming_events_2026-06-02.json, data/social_sentiment_2026-06-02.json, data/fx_exposure_2026-06-02.json, data/events_2026-06-02.json, data/validation_report.txt — aucune donnée hallucinée.*
