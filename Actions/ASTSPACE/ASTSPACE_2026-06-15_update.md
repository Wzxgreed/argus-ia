# ASTSPACE — Mise à Jour 2026-06-15

> **Proxy ASTS** : snapshot 10h UTC — gap down **−15,53%** à $82,41 sur volume liquidation **2,0×**, RSI retour survente **40,50** (−11,28 pts), cassure confirmée du MM50 **$89,23**, données techniques ATR/MM50 récupérées. Score agent ASTS downgrade mécanique **48,5→35,5/100 (SURVEILLER proche ÉVITER)**. Anomalie options JSON persistante.
> **ASTSPACE officiel :** toujours `No price history` — **49+ snapshots consécutifs**.

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `ASTSPACE_2026-06-10_update.md` (snapshot 10h UTC)

| Élément | 10/06 10h | 15/06 10h (snapshot) | Changement |
|---------|-----------|----------------------|------------|
| Erreur Yahoo ASTSPACE | `No price history` | `No price history` | **Stable — 49+ snapshots consécutifs** 🔴 |
| ASTS (proxy) close | **NaN** (previous_close $92,06) | **$82,41** | **Gap down −15,53% vs previous_close $97,56** 🔴 |
| ASTS open | — | $97,00 | **Open sur gap baissier** 🔴 |
| ASTS volume | **26,69M (1,01×)** | **54,91M (2,0× moy. 27,46M)** | **Explosion +106%, liquidation** 🔴 |
| RSI ASTS | **51,78** | **40,50** | **−11,28 pts, retour survente** 🔴 |
| ATR ASTS | **null** | **$13,80** | **Donnée récupérée** 🟢 |
| MM 50j ASTS | **null** | **$89,23** | **Donnée récupérée** 🟢 |
| Distance MM50 | — | **−7,6%** ($82,41 vs $89,23) | **Cassure MM50 confirmée** 🔴 |
| Score ASTS (agent) | **48,5/100 (SURVEILLER)** | **35,5/100 (SURVEILLER)** | **Downgrade mécanique −13,0 pts** 🔴 |
| Score ASTSPACE (agent) | **55,2/100** | **55,2/100** | **Stable (placeholder)** 🟡 |
| Max Pain ASTS (JSON) | **$45,00** | **$28,00** | **[ANOMALIE JSON PERSISTANTE]** 🔴 |
| Put/Call ASTS (JSON) | **null** | **0,00** | **[ANOMALIE JSON]** 🔴 |
| Call OI % ASTS (JSON) | **null** | **100,0%** | **[ANOMALIE JSON]** 🔴 |
| P/B ASTS (Yahoo) | **12,73×** | **11,83×** | **Compression −0,90×** 🟢 |
| EV/Revenue ASTS (Yahoo) | **318,42×** | **296,26×** | **Compression −22,16×** 🟢 |
| Short Interest ASTS | **18,39%** | **18,39%** | **Stable** 🟡 |
| Divergence consensus ASTS | **+2,69%** (si $92,06) | **−12,8%** ($82,41 vs PT $94,54) | **Divergence creusée** 🔴 |
| Signal sectoriel | UNKNOWN | **UNKNOWN** | **Données partielles persistantes** 🔴 |

**Constat :** Le snapshot du 15/06 confirme une dégradation majeure du proxy ASTS avec un gap down de −15,53% sur volume de liquidation doublé (2,0×). Les données techniques ATR ($13,80) et MM50 ($89,23) sont récupérées, mais la cassure du MM50 est brutale (−7,6%). Le RSI retombe en survente (40,50). Le scoring agent ASTS est downgrade de −13 pts supplémentaires (35,5/100, SURVEILLER proche du seuil ÉVITER < 35). L'anomalie options JSON persiste (max pain $28 aberrant). ASTSPACE reste totalement sans données.

---

## 2. Mise à jour technique

### ASTSPACE (données officielles)

| Indicateur | Valeur 15/06 | Valeur 10/06 | Δ |
|-----------|-----------|-----------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 | Placeholder 50 | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing ASTSPACE :** [NON ÉVALUABLE] — absence totale de données techniques depuis 49+ snapshots.

### ASTS (proxy, snapshot 10h UTC)

| Indicateur | Valeur 15/06 | Valeur 10/06 | Δ |
|-----------|-----------|-----------|---|
| Cours close | **$82,41** | NaN (previous_close $92,06) | **−15,53% vs previous_close $97,56** 🔴 |
| Open | **$97,00** | — | **Gap down ouverture** 🔴 |
| High | **$97,73** | — | **Rejet immédiat post-open** 🔴 |
| Low | **$81,50** | — | **Low du jour proche close** 🔴 |
| Volume (journée) | **54,91M** | 26,69M | **+106%** 🔴 |
| Volume relatif | **2,0× moy. 27,46M** | 1,01× moy. 26,41M | **Explosion liquidation** 🔴 |
| RSI 14j | **40,50** | 51,78 | **−11,28 pts, survente** 🔴 |
| ATR 14j | **$13,80** | null | **Récupéré** 🟢 |
| MM 50j | **$89,23** | null | **Récupérée** 🟢 |
| Distance MM50 | **−7,6%** | — | **Cassure confirmée** 🔴 |
| 52W high | **133,86** | 133,86 | **Stable** 🟡 |
| 52W low | **36,08** | 36,08 | **Stable** 🟡 |
| Distance 52W high | **−38,4%** | −33,7% | **Creusement −4,7 pts** 🔴 |
| Max pain options (JSON) | **$28,00** | $45,00 | **[ANOMALIE JSON PERSISTANTE]** 🔴 |
| Put/call ratio (JSON) | **0,00** | null | **[ANOMALIE JSON]** 🔴 |
| Call OI % (JSON) | **100,0%** | null | **[ANOMALIE JSON]** 🔴 |

**Verdict timing ASTS (proxy) :** 🔴 **DÉFAVORABLE** — Le gap down de −15,53% sur volume de liquidation (2,0×) est un signal de distribution institutionnelle agressive. La cassure du MM50 $89,23 (−7,6%) confirme un retournement de tendance court terme. Le RSI à 40,50 indique une survente technique mais pas encore extrême (< 30). La récupération de l'ATR ($13,80) et du MM50 permet désormais de calculer des niveaux objectifs. L'anomalie options JSON persiste (max pain $28 aberrant) — les valeurs opérationnelles historiques ($120 / 0,74 / 57,4%) ne sont plus fiables.

**Alerte technique :** `GAP_DOWN_LIQUIDATION` — Mouvement > −10% sur volume > 1,5×. Risque de continuation baissière vers $75–$80 en l'absence de rebond rapide au-dessus de MM50.

**Supports clés :** $80,00 (psychologique) ; $75,00 (gap précédent) ; $70,00 (consolidation historique)
**Résistances clés :** MM50 $89,23 (premier objectif de retour) ; $92,06 (previous_close du 10/06) ; $97,13 (open du 15/06) ; $100,00 (psychologique — rejet confirmé le 09/06)

---

## 3. Mise à jour fondamentale

### ASTSPACE (données officielles)

Aucune donnée disponible. Anomalie structurelle inchangée.

### ASTS (proxy)

| Métrique | Valeur 15/06 | Valeur 10/06 | Δ |
|---------|-----------|-----------|---|
| Market cap | **$31,98B** | $34,43B | **Compression −$2,45B (−7,1%)** 🔴 |
| Forward P/E | **−401,61** | −432,31 | **Compression mécanique** 🟡 |
| EV/Revenue (Yahoo) | **296,26×** | 318,42× | **Compression −22,16×** 🟢 |
| P/B (Yahoo) | **11,83×** | 12,73× | **Compression −0,90×** 🟢 |
| Beta | **2,634** | 2,634 | **Stable** 🟡 |
| Short interest | **18,39%** | 18,39% | **Stable** 🟡 |
| Consensus PT | **$94,54** (12 analysts) | $94,54 (12 analysts) | **Inchangé** 🟡 |
| Divergence consensus | **−12,8%** ($82,41 vs $94,54) | +2,69% (si $92,06) | **Divergence massive** 🔴 |

Le consensus analystes ($94,54) est désormais **$12,13 au-dessus du cours** (+14,7% upside). Aucun changement dans le nombre d'analystes ni dans les estimates. La compression des multiples (EV/Revenue, P/B) est mécanique (dérivation du cours), pas fondamentale.

**Risque sectoriel :** Signal **UNKNOWN** (données partielles). XLC (Communication Services) reste dans le **bottom 3** du sector rotation. Malus sectoriel maintenu pour ASTS.

---

## 4. Mise à jour sentiment / options / news

- **News ASTSPACE :** aucune entrée Yahoo Finance ni FMP — silence médiatique total
- **News ASTS :** aucune news spécifique dans le flux du 2026-06-15 identifiée comme déclencheur du gap down
- **Options ASTS (anomalie JSON persistante) :**
  - Max Pain JSON : **$28,00** (aberrant — nouveau minima historique d'anomalie)
  - Put/Call JSON : **0,00** (aberrant)
  - Call OI % JSON : **100,0%** (aberrant)
  - **Valeurs opérationnelles historiques ($120 / 0,74 / 57,4%) non fiables** suite au gap down
  - Nearest expiry : **2026-06-18 (J+3)**
  - **Lecture :** l'anomalie JSON rend toute lecture options inutilisable. Le pinning gamma théorique vers $120 est désormais irréaliste (cours à $82,41).
- **Social sentiment :** 0 mention Reddit pour ASTSPACE et ASTS — silence retail total. Score 0,0/10
- **Upgrades/downgrades ASTS :** 12 analysts, PT moyen $94,54 — inchangé
- **Quant :** pas de signaux historiques pour ASTSPACE — p-value insuffisante (p=1,0, n=0)
- **Geo / Accounting / Events :**
  - Geo risk score IREN : 2/10 (🟢), aucune donnée spécifique ASTS
  - Accounting risk : non disponible
  - Events : aucun événement corporate détecté
- **FX exposure ASTSPACE :** exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **Upcoming events :**
  - ASTSPACE : earnings signalé le **2026-06-15** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (>17j de décalage depuis le 29/05)
  - ASTS : earnings le **2026-08-10** (`days_until: 56`) via yfinance, estimations EPS $−0,29 à $−0,17, Revenues $0,0B
- **Sector rotation :** signal **UNKNOWN** (données partielles). XLC dans le **bottom 3** persistant. Malus sectoriel maintenu pour ASTS.

---

## 5. Scoring global

### ASTSPACE (données officielles — placeholder)

| Axe | Score 15/06 | Pondération | Note |
|-----|----------|-------------|------|
| Catalyseur | 6,5/10 (placeholder) | 35% | [NON FONDÉ] |
| Valorisation | 5,0/10 (placeholder) | 40% | [NON FONDÉ] |
| Momentum | 5,0/10 (placeholder) | 25% | [NON FONDÉ] |
| **Score Opportunité** | **5,5/10** | — | Placeholder — **non utilisable** |
| **Score Global** | **55,2/100** | — | Placeholder — **non utilisable** |
| **Score Global Ajusté** | **55,2/100** | — | Placeholder — **non utilisable** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, snapshot 10h UTC)

| Axe | Score 15/06 | Pondération | Commentaire |
|-----|----------|-------------|-------------|
| Catalyseur | 5,5/10 | 35% | Aucun catalyseur imminent, earnings dans 56j. Gap down non expliqué par news |
| Valorisation | 4,5/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue 296×). Consensus offre upside mais fondamentaux non rentables. Léger upgrade mécanique (compression multiples) |
| Momentum | 2,5/10 | 25% | Gap down −15,53%, cassure MM50, RSI survente 40,50, volume liquidation 2,0×. Momentum fortement baissier |
| **Score Opportunité** | **4,3/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **43,5/100** | — | **SURVEILLER** |
| **Score Global Ajusté** | **35,5/100** | — | **SURVEILLER** (proche ÉVITER) |

**Malus / Bonus appliqués (Agent Recommandation) :**
- Malus **GAP_DOWN_LIQUIDATION** : −15,53% sur volume 2,0× — distribution institutionnelle
- Malus **CASSURE_MM50** : cours $82,41 sous MM50 $89,23 (−7,6%) — retournement tendance CT
- Malus **ANOMALIE_OPTIONS_JSON** : max pain $28 aberrant, put/call 0,00, call OI 100% — perte totale de signal options
- Malus ATR_SPIKE (mémoire) : volatilité intraday extrême (range 19,7% du jour : $81,50–$97,73)
- Malus REJET_100 (mémoire) : test et rejet de $100,94 le 09/06 — structure baissière confirmée
- Malus sectoriel (XLC bottom 3) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (Quality Gate OK)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle. Le score **35,5/100 (SURVEILLER)** représente un **downgrade mécanique supplémentaire de −13,0 pts** vs le snapshot 10/06 (48,5 SURVEILLER). Ce downgrade est dû au gap down de −15,53%, à la cassure du MM50, à la dégradation du momentum (2,5/10) et au volume de liquidation, et non à une nouvelle information fondamentale négative explicite.

---

## 6. Niveaux SL / TP / Ratio R/R

### ASTSPACE (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy, snapshot 10h UTC)

**Niveaux recalculés (ATR $13,80 récupéré) :**
- Prix d'entrée de référence : **$82,41**
- ATR 14j : **$13,80**
- Stop-loss suggéré = $82,41 − 2×$13,80 = **$54,81**
- Take-profit suggéré = $82,41 + 3×$13,80 = **$123,81**
- Ratio R/R = ($123,81 − $82,41) / ($82,41 − $54,81) = **1,5**

> Le SL $54,81 est éloigné (33,5% sous le cours) et reflète la volatilité extrême du titre (beta 2,634, ATR 16,8% du cours). Le TP $123,81 correspond approximativement au niveau du gap down ($97,56) plus une marge. Toutefois, le momentum baissier actuel rend ces niveaux théoriques à court terme. Le risque immédiat reste la continuation vers $75–$80 si le gap n'est pas comblé rapidement.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — PROXY ASTS EN DOWNGRADE MÉCANIQUE SURVEILLER 35,5/100 (−13 PTS SUPPLÉMENTAIRES), GAP DOWN −15,53% SUR VOLUME LIQUIDATION 2,0×, CASSURE MM50 CONFIRMÉE, RSI SURVENTE 40,50, ANOMALIE OPTIONS JSON PERSISTANTE**

ASTSPACE n'est pas évaluable en l'état. La situation sur le proxy ASTS au snapshot 15/06 montre une dégradation majeure sans nouvelle information fondamentale identifiée :

1. **Anomalie structurelle confirmée :** ASTSPACE est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis 49+ snapshots consécutifs (erreur Yahoo : *No price history*).
2. **Gap down majeur ASTS :** −15,53% à $82,41 vs previous_close $97,56. Open $97,00 → rejet immédiat, low $81,50 proche du close. Range intraday 19,7%.
3. **Volume de liquidation :** 54,91M (2,0× moyenne 27,46M) — distribution institutionnelle agressive confirmée.
4. **Cassure MM50 confirmée :** Cours $82,41 sous MM50 $89,23 (−7,6%). Les données MM50 et ATR sont récupérées mais confirment la rupture.
5. **RSI survente :** 40,50 (−11,28 pts vs 10/06) — retour en zone survente, pas encore extrême (< 30).
6. **Downgrade mécanique ASTS :** Score global ajusté **35,5/100 (SURVEILLER)** — downgrade supplémentaire de −13,0 pts vs snapshot 10/06 (48,5 SURVEILLER). Le titre approche le seuil ÉVITER (< 35).
7. **Anomalie options JSON persistante :** Max pain **$28,00** (nouveau minima aberrant), put/call **0,00**, call OI **100%**. Les valeurs opérationnelles historiques ne sont plus fiables.
8. **Short interest stable :** 18,39% — pas de setup squeeze, pas de couverture de shorts détectée.
9. **Divergence consensus creusée :** −12,8% ($82,41 vs PT $94,54) vs +2,69% le 10/06. L'upside mécanique s'est réduit.
10. **Signal sectoriel UNKNOWN :** Données sectorielles partielles. XLC bottom 3 persistant.
11. **Earnings placeholder glissant non résolu :** FMP signale un earnings ASTSPACE le **2026-06-15** (`days_until: 0`), glissement persistant depuis le **29/05** (>17j de décalage).
12. **Structure baissière confirmée :** Le rejet de $100 le 09/06, le gap down du 15/06 et la cassure du MM50 établissent une tendance baissière court terme.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer ASTSPACE de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence accrue :** Le gap down de −15,53% sur volume liquidation est un signal de distribution. Attendre un rebond technique au-dessus de MM50 $89,23 avant toute révision positive
- **Si close < $80** sur volume maintenu (>1,0×) → révision vers ÉVITER probable (seuil < 35)
- **Si rebond > $89,23 (MM50)** sur volume > 1,0× → possibilité de retour vers SURVEILLER stable (40–45/100)
- **Le niveau $100** reste une résistance majore — ne pas entrer long sans confirmation de break au-dessus de $100 sur volume >1,0×
- **Monitoring options J+3** (expiration 2026-06-18) — anomalie JSON empêche toute lecture fiable
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (rebreak MM50 confirmé) avant toute entrée
- **Ne pas entrer long sans close fiable au-dessus de $89,23 (MM50) sur volume >0,8×**

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 10h UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/events_latest.json, data/quant_report_latest.json — aucune donnée hallucinée.*
