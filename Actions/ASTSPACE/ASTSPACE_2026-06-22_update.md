# ASTSPACE — Mise à Jour (2026-06-22, snapshot 13h UTC)

> **Proxy ASTS** : snapshot 13h UTC 2026-06-22 — **stabilité totale des données de cotation** par rapport au snapshot 10h. Cours **$80,66** (inchangé), volume **31,68M** (inchangé), RSI **32,75** (inchangé), ATR **$10,66** (inchangé). **Anomalie options JSON RÉSOLUE** (max pain $100,00 cohérent, put/call 0,70, call OI 58,9%). Score agent ASTS **39,2/100 (SURVEILLER)** inchangé. **ASTSPACE officiel :** toujours `No price history` — **61e snapshot consécutif sans données propres**.

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `ASTSPACE_2026-06-22_update.md` (snapshot 10h UTC)

| Élément | 22/06 10h | 22/06 13h | Changement |
|---------|-----------|-----------|------------|
| Erreur Yahoo ASTSPACE | `No price history` | `No price history` | **Stable — 61 snapshots consécutifs** 🔴 |
| ASTS (proxy) close | **$80,66** | **$80,66** | **0,00%** 🟡 |
| ASTS change % | −5,58% | −5,58% | **Stable** 🟡 |
| ASTS volume | 31,68M (1,117×) | 31,68M (1,117×) | **Stable** 🟡 |
| RSI ASTS | **32,75** | **32,75** | **Stable** 🟡 |
| ATR ASTS | **$10,66** | **$10,66** | **Stable** 🟡 |
| MM 50j ASTS | **$88,42** | **$88,42** | **Stable** 🟡 |
| Distance MM50 | **−8,78%** | **−8,78%** | **Stable** 🟡 |
| Score ASTS (agent) | **39,2/100 (SURVEILLER)** | **39,2/100 (SURVEILLER)** | **Stable** 🟡 |
| Score ASTSPACE (agent) | **55,2/100 (ATTENDRE)** | **55,2/100 (ATTENDRE)** | **Stable (placeholder)** 🟡 |
| Max Pain ASTS (JSON brut) | **$45,00** (aberrant) | **$100,00** (cohérent) | **Anomalie RÉSOLUE** 🟢 |
| Put/Call ASTS (JSON brut) | **null** | **0,70** | **Anomalie RÉSOLUE** 🟢 |
| Call OI % ASTS (JSON brut) | **null** | **58,9%** | **Anomalie RÉSOLUE** 🟢 |
| Forward P/E ASTS | **−393,08** | **−393,08** | **Stable** 🟡 |
| EV/Revenue ASTS (Yahoo) | **290,11×** | **290,11×** | **Stable** 🟡 |
| P/B ASTS (Yahoo) | **11,58×** | **11,58×** | **Stable** 🟡 |
| Divergence consensus ASTS | **−14,7%** | **−14,7%** | **Stable** 🟡 |
| Signal sectoriel | NEUTRAL (artefact) | NEUTRAL (artefact) | **Stable** 🟡 |

**Constat :** Le snapshot 13h UTC confirme une **stabilité totale** des données de cotation du proxy ASTS par rapport au snapshot 10h. La seule évolution matérielle est la **résolution de l'anomalie options JSON** : max pain revenu à $100,00 (cohérent), put/call 0,70 et call OI 58,9% — valeurs opérationnelles à nouveau fiables. Le positionnement options est légèrement haussier (call OI > 50%, put/call < 1,0). Le score agent ASTS reste inchangé à 39,2/100 (SURVEILLER). L'anomalie structurelle ASTSPACE persiste (61 snapshots sans données).

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

**Verdict timing ASTSPACE :** [NON ÉVALUABLE] — absence totale de données techniques depuis 61 snapshots consécutifs.

### ASTS (proxy, snapshot 13h UTC 22/06)

| Indicateur | Valeur 13h | Valeur 10h | Δ |
|-----------|-----------|-----------|---|
| Cours close | **$80,66** | **$80,66** | **0,00%** 🟡 |
| Open (snapshot) | **$85,30** | **$85,30** | **Stable** 🟡 |
| High | **$85,70** | **$85,70** | **Stable** 🟡 |
| Low | **$77,12** | **$77,12** | **Stable** 🟡 |
| Volume (journée) | **31,68M** | 31,68M | **Stable** 🟡 |
| Volume relatif | **1,117× moy. 28,35M** | 1,117× moy. 28,35M | **Stable** 🟡 |
| RSI 14j | **32,75** | 32,75 | **Stable** 🟡 |
| ATR 14j | **$10,66** | $10,66 | **Stable** 🟡 |
| MM 50j | **$88,42** | $88,42 | **Stable** 🟡 |
| Distance MM50 | **−8,78%** | −8,78% | **Stable** 🟡 |
| 52W high | **133,86** | 133,86 | **Stable** 🟡 |
| 52W low | **36,08** | 36,08 | **Stable** 🟡 |
| Distance 52W high | **−39,7%** | −39,7% | **Stable** 🟡 |
| Max pain options (JSON brut) | **$100,00** (cohérent) | $45,00 (aberrant) | **RÉSOLU** 🟢 |
| Put/call ratio (JSON brut) | **0,70** | null | **RÉSOLU** 🟢 |
| Call OI % (JSON brut) | **58,9%** | null | **RÉSOLU** 🟢 |

**Verdict timing ASTS (proxy) :** 🔴 **DÉFAVORABLE** — La configuration technique reste inchangée et fragilisée. Cours $80,66, gap vs MM50 −8,78%, RSI 32,75 en survente persistante, volume 1,117× sur séance baissière. La seule évolution positive est la résolution de l'anomalie options, qui rétablit la visibilité sur le positionnement des opérateurs : max pain $100 (cohérent avec l'historique), put/call 0,70 (léger skew haussier), call OI 58,9% (dominance légère des calls). Cela ne modifie pas la tendance baissière court terme mais élimine un brouillard de données.

**Alerte technique :** `RUPTURE_SUPPORT_82` + `EXPANSION_VOLUME_BAISSIERE` + `SURVENTE_PERSISTANTE` — Le support $82,11 reste cassé. L'expansion de volume sur séance baissière (−5,58%) est un signal de distribution. Le niveau clé reste le low du jour $77,12 ; cassure = risque de retour vers $75,00 puis $70,00.

**Supports clés :** $77,12 (low 22/06) ; $75,00 (psychologique) ; $70,00 (gap précédent)
**Résistances clés :** $82,11 (ancien support, désormais résistance) ; MM50 $88,42 (+9,6%) ; $89,60 (high 16/06) ; $92,06 (close 10/06) ; $97,56 (previous close avant gap down) ; $100,00 (psychologique + max pain)

---

## 3. Mise à jour fondamentale

### ASTSPACE (données officielles)

Aucune donnée disponible. Anomalie structurelle inchangée.

### ASTS (proxy)

| Métrique | Valeur 13h | Valeur 10h | Δ |
|---------|-----------|-----------|---|
| Market cap | **$31,31B** | $31,31B | **Stable** 🟡 |
| Forward P/E | **−393,08** | −393,08 | **Stable** 🟡 |
| EV/Revenue (Yahoo) | **290,11×** | 290,11× | **Stable** 🟡 |
| P/B (Yahoo) | **11,58×** | 11,58× | **Stable** 🟡 |
| Beta | **2,634** | 2,634 | **Stable** 🟡 |
| Short interest | **18,39%** | 18,39% | **Stable** 🟡 |
| Consensus PT | **$94,54** (12 analysts) | $94,54 (12 analysts) | **Inchangé** 🟡 |
| Divergence consensus | **−14,7%** | −14,7% | **Stable** 🟡 |

Aucune mutation fondamentale. Toutes les métriques sont stables entre les deux snapshots.

**Risque sectoriel :** Signal **NEUTRAL** (artefact). XLC (Communication Services) reste dans le **bottom 3** du sector rotation (momentum score 0,0). Malus sectoriel maintenu pour ASTS.

---

## 4. Mise à jour sentiment / options / news

- **News ASTSPACE :** aucune entrée Yahoo Finance ni FMP — silence médiatique total
- **News ASTS :** aucune news spécifique dans le flux du 2026-06-22 identifiée comme déclencheur
- **Options ASTS (anomalie JSON RÉSOLUE) :**
  - Max Pain JSON brut : **$100,00** (cohérent — restauré)
  - Put/Call JSON brut : **0,70** (skew haussier léger)
  - Call OI % JSON brut : **58,9%** (dominance calls)
  - **Valeurs opérationnelles :** FIABLES — structure options évaluable à nouveau
  - Nearest expiry : **2026-06-26 (J+4)**
  - **Lecture :** Le positionnement options est légèrement haussier (call OI 58,9% > 50%, put/call 0,70 < 1,0). Le max pain $100 est cohérent avec l'historique et offre une cible technique si rebond. L'expiration J+4 maintient le risque de pinning gamma autour de $100, mais les données sont désormais fiables.
- **Social sentiment :** 0 mention Reddit pour ASTSPACE et ASTS — silence retail total. Score 0,0/10
- **Upgrades/downgrades ASTS :** 12 analysts, PT moyen $94,54 — inchangé
- **Quant :** pas de signaux historiques pour ASTSPACE — p-value insuffisante (p=1,0, n=0)
- **Geo / Accounting / Events :**
  - Geo risk score ASTS : non flaggé (pas de données spécifiques)
  - Accounting risk : non disponible (`accounting_risk_latest.json` absent)
  - Events : aucun événement corporate détecté
- **FX exposure ASTSPACE :** exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **Upcoming events :**
  - ASTSPACE : earnings signalé le **2026-06-22** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (>24j de décalage depuis le 29/05)
  - ASTS : earnings le **2026-08-10** (`days_until: 49`) via yfinance, estimations EPS $−0,29 à $−0,17, Revenues $0,0B
- **Sector rotation :** signal **NEUTRAL** (artefact). XLK (Technology) #1 du ranking (momentum 10,0). XLC (Communication Services) **bottom 3** persistant (momentum 0,0). Malus sectoriel maintenu pour ASTS.

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

### ASTS (proxy, snapshot 13h UTC 22/06)

| Axe | Score 13h | Pondération | Commentaire |
|-----|-----------|-------------|-------------|
| Catalyseur | 6,0/10 | 35% | Aucun catalyseur imminent, earnings dans 49j. Options rétablies (max pain $100, put/call 0,70, call OI 58,9%). Divergence consensus +17,2% |
| Valorisation | 5,0/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue 290×). Consensus offre upside +17,2% mais fondamentaux non rentables |
| Momentum | 2,5/10 | 25% | RSI 32,75 survente persistante, cours −8,78% sous MM50, volume 1,117× sur séance baissière = distribution. Configuration fragilisée |
| **Score Opportunité** | **4,7/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **47,2/100** | — | **SURVEILLER** |
| **Score Global Ajusté** | **39,2/100** | — | **SURVEILLER** (bas de fourchette) |

**Malus / Bonus appliqués (Agent Recommandation) :**
- Malus **COURS_SOUS_MM50** : cours $80,66 sous MM50 $88,42 (−8,78%) — résistance dynamique éloignée
- Malus **GAP_DOWN_NON_COMBLÉ** : close $80,66 vs previous close avant gap $97,56 — structure baissière renforcée
- Malus **RSI_SURVENTE** : RSI 32,75 en survente — momentum très faible
- Malus **VOLUME_DISTRIBUTION** : volume 1,117× sur séance baissière −5,58% — signe de distribution
- Malus **RUPTURE_SUPPORT** : cassure du support $82,11 (low 16/06 et 17/06) avec close $80,66
- Malus sectoriel (XLC bottom 3) : −0,5 pt — faiblesse sectorielle persistante
- **Bonus options rétablies** : max pain $100 cohérent, call OI 58,9% — élimine le brouillard de données, mais ne compense pas les malus techniques
- Aucun malus comptable (Quality Gate OK)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Défavorable
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle. Le score **39,2/100 (SURVEILLER)** est inchangé vs le snapshot 10h.

---

## 6. Niveaux SL / TP / Ratio R/R

### ASTSPACE (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy, snapshot 13h UTC 22/06)

**Niveaux inchangés (ATR $10,66) :**
- Prix d'entrée de référence : **$80,66**
- ATR 14j : **$10,66**
- Stop-loss suggéré = $80,66 − 2×$10,66 = **$59,34**
- Take-profit suggéré = $80,66 + 3×$10,66 = **$112,64**
- Ratio R/R = ($112,64 − $80,66) / ($80,66 − $59,34) = **1,5**

> Le SL $59,34 est éloigné (26,4% sous le cours) et reflète la volatilité extrême du titre (beta 2,634, ATR 13,2% du cours). Le TP $112,64 correspond au max pain options rétabli ($100) avec marge. Toutefois, le momentum baissier actuel, la cassure du support $82,11 et l'expiration options J+4 rendent ces niveaux théoriques à court terme. Le risque immédiat reste un retour vers $75,00 puis $70,00 si le low $77,12 cède.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — PROXY ASTS EN SURVEILLER 39,2/100, CASSURE SUPPORT $82,11, EXPANSION VOLUME BAISSIÈRE 1,117×, RSI SURVENTE 32,75, GAP VS MM50 −8,78%, ANOMALIE OPTIONS JSON RÉSOLUE (MAX PAIN $100 COHÉRENT, CALL OI 58,9%), 61 SNAPSHOTS SANS DONNÉES FIABLES POUR ASTSPACE**

ASTSPACE n'est pas évaluable en l'état. Le snapshot 13h UTC du 22/06 confirme une **stabilité totale** du proxy ASTS par rapport au snapshot 10h, avec une **amélioration marginale** liée à la résolution de l'anomalie options :

1. **Anomalie structurelle confirmée :** ASTSPACE est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis **61 snapshots consécutifs** (erreur Yahoo : *No price history*).
2. **Cassure du support $82,11 confirmée :** Close $80,66 inchangé, low $77,12 inchangé. Ancien support devenu résistance.
3. **Expansion volume baissière stable :** 31,68M (1,117× moy. 28,35M) sur séance −5,58% — signe de distribution persistant.
4. **Anomalie options JSON RÉSOLUE :** Max pain $100 cohérent, put/call 0,70, call OI 58,9% — données opérationnelles fiables à nouveau. Positionnement légèrement haussier des opérateurs options.
5. **RSI en survente persistante :** 32,75 — inchangé, sans rebond structurel.
6. **Gap vs MM50 stable :** −8,78% ($80,66 vs $88,42). Aucun test de la MM50.
7. **Score ASTS stable :** Score global ajusté **39,2/100 (SURVEILLER)** — bas de zone SURVEILLER.
8. **Structure baissière confirmée :** Le rejet de $100 le 09/06, le gap down du 15/06, la rupture du 16/06 (−5,12%), la stabilité mécanique du 17/06 et la cassure du 22/06 (−5,58%) établissent une tendance baissière court terme confirmée sur 4 sessions.
9. **Short interest stable :** 18,39% — pas de setup squeeze, pas de couverture de shorts détectée.
10. **Divergence consensus stable :** −14,7% ($80,66 vs PT $94,54). Upside théorique inchangé mais non réalisé.
11. **Signal sectoriel NEUTRAL (artefact) :** XLC reste bottom 3 persistant. Malus sectoriel maintenu.
12. **Earnings placeholder glissant non résolu :** FMP signale un earnings ASTSPACE le **2026-06-22** (`days_until: 0`), glissement persistant depuis le **29/05** (>24j de décalage).

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer ASTSPACE de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence accrue :** Le setup reste SURVEILLER 39,2/100. La cassure du support $82,11 et l'expansion volume baissière sont des signaux négatifs
- **Si close < $77,12** (low 22/06) sur volume maintenu (>0,8×) → révision vers ÉVITER probable
- **Si close < $75,00** (psychologique) sur volume >0,5× → ÉVITER confirmé
- **Si rebond > $82,11** (ancien support) sur volume >1,0× → possibilité de retour vers SURVEILLER stable (42–45/100)
- **Si rebond > $88,42 (MM50)** sur volume >1,0× → révision vers ATTENDRE (50–55/100)
- **Le niveau $100** reste une résistance majeure — ne pas entrer long sans confirmation de break au-dessus de $100 sur volume >1,0×
- **Monitoring options J+4** (expiration 2026-06-26) — données rétablies, max pain $100 = cible pinning gamma
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (rebreak MM50 confirmé) avant toute entrée
- **Ne pas entrer long sans close fiable au-dessus de $88,42 (MM50) sur volume >0,8×**

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 13h UTC 2026-06-22), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json — aucune donnée hallucinée.*
