# ASTSPACE — Mise à Jour 2026-06-10 (snapshot 10h UTC)

> **Proxy ASTS** : snapshot 10h UTC avec données techniques partielles (close NaN, ATR/MM50 null), anomalie options JSON récurrente, downgrade mécanique **ATTENDRE → SURVEILLER** (Score Global 48,5/100, −10 pts). Divergence price vs close officiel 09/06 ($92,06 vs $88,71). RSI **51,78** (+1,51 pt), volume normalisé **1,01×** stable. Profil fondamental spéculatif extrême inchangé. Thèse proxy modifiée avec réserves.
> **ASTSPACE officiel :** toujours `No price history` — 42+ snapshots consécutifs.

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `ASTSPACE_2026-06-09_update.md` (close officiel 21h UTC)

| Élément | 09/06 21h | 10/06 10h (snapshot) | Changement |
|---------|-----------|----------------------|------------|
| Erreur Yahoo ASTSPACE | `No price history` | `No price history` | **Stable — 42+ snapshots consécutifs** 🔴 |
| ASTS (proxy) close JSON | **$88,71** | **$92,06** (`previous_close`) | **Divergence +$3,35 (+3,78%)** 🔴 |
| ASTS close réel | $88,71 | **NaN** | **[DONNÉES PARTIELLES]** 🔴 |
| Volume ASTS | **26,69M (1,01×)** | **26,69M (1,01×)** | **Stable** 🟢 |
| RSI ASTS | **50,27** | **51,78** | **+1,51 pts, neutre** 🟡 |
| ATR ASTS | **$13,29** | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| MM 50j ASTS | **$88,70** | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| Distance MM50j | **+0,01%** | — | **Non calculable** 🔴 |
| Score ASTS (agent) | **58,5/100 (ATTENDRE)** | **48,5/100 (SURVEILLER)** | **Downgrade −10,0 pts** 🔴 |
| Score ASTSPACE (agent) | **55,2/100** | **55,2/100** | **Stable (placeholder)** 🟡 |
| Max Pain ASTS (JSON) | **$120,00** | **$45,00** | **[ANOMALIE JSON RÉCURRENT]** 🔴 |
| Put/Call ASTS (JSON) | **0,74** | **null** | **[ANOMALIE JSON]** 🔴 |
| Call OI % ASTS (JSON) | **57,4%** | **null** | **[ANOMALIE JSON]** 🔴 |
| P/B ASTS (Yahoo) | **12,73×** | **12,73×** | **Stable** 🟡 |
| EV/Revenue ASTS (Yahoo) | **330,20×** | **318,42×** | **Compression −11,78×** 🟢 |
| Short Interest ASTS | **17,60%** | **18,39%** | **+0,79 pt** 🟡 |
| Divergence consensus ASTS | **−6,17%** | **+2,69%** (si $92,06) | **Divergence mécanique** 🟡 |
| Signal sectoriel | NEUTRAL | **UNKNOWN** | **Données partielles** 🔴 |
| Quality gate ASTS | OK | **OK** | **Stable** 🟢 |

**Constat :** Le snapshot 10h UTC du 10/06 confirme une dégradation mécanique du scoring proxy ASTS (downgrade ATTENDRE → SURVEILLER, 48,5/100) sans nouvelle information fondamentale. L'absence de close, ATR et MM50 empêche toute confirmation technique de la tenue du support MM50 $88,70 établi le 09/06. L'anomalie options JSON est récurrente (max pain $45 aberrant). Le volume reste normalisé (1,01×) — liquidité institutionnelle maintenue. L'échéance options du 12/06 est dans J+2.

---

## 2. Mise à jour technique

### ASTSPACE (données officielles)

| Indicateur | Valeur 10h | Valeur 09/06 21h | Δ |
|-----------|-----------|-----------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 | Placeholder 50 | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing ASTSPACE :** [NON ÉVALUABLE] — absence totale de données techniques depuis 42+ snapshots.

### ASTS (proxy, snapshot 10h UTC)

| Indicateur | Valeur 10h | Valeur 09/06 21h | Δ |
|-----------|-----------|-----------|---|
| Cours close | **NaN** | $88,71 | **[DONNÉES PARTIELLES]** 🔴 |
| Previous close | **$92,06** | — | **Divergence +$3,35 vs close 09/06** 🔴 |
| Volume (journée) | **26,69M** | 26,69M | **Stable** 🟢 |
| Volume relatif | **1,01× moy. 26,41M** | 1,01× | **Stable** 🟢 |
| RSI 14j | **51,78** | 50,27 | **+1,51 pts** 🟡 |
| ATR 14j | **null** | $13,29 | **[DONNÉES MANQUANTES]** 🔴 |
| MM 50j | **null** | $88,70 | **[DONNÉES MANQUANTES]** 🔴 |
| 52W high | 133,86 | 133,86 | **Stable** 🟡 |
| Distance 52W high | −33,7% | −33,7% | **Stable** 🟡 |
| Max pain options (JSON) | **$45,00** | $120,00 | **[ANOMALIE JSON RÉCURRENT]** 🔴 |
| Put/call ratio (JSON) | **null** | 0,74 | **[ANOMALIE JSON]** 🔴 |
| Call OI % (JSON) | **null** | 57,4% | **[ANOMALIE JSON]** 🔴 |

**Verdict timing ASTS (proxy) :** 🔴 **INDÉTERMINABLE — DONNÉES TECHNIQUES PARTIELLES** — Le snapshot 10h UTC ne fournit ni close, ni ATR, ni MM50. Impossible de confirmer la tenue du support MM50 $88,70 établi le 09/06. Le RSI à 51,78 reste dans la zone neutre (+1,51 pt). La normalisation du volume (1,01×) est le seul signal positif — liquidité institutionnelle maintenue. L'anomalie options JSON récurrente (max pain $45 aberrant, put/call et call OI null) prive le signal d'une confirmation haussière. L'échéance du 12/06 (J+2) rapproche.

**Alerte technique :** `DONNÉES_PARTIELLES` — close NaN, ATR14 null, MM50 null. Impossibilité de confirmer la tenue du support MM50 $88,70. Si le cours réel est sous MM50 → risque de retour vers $80–$85.

**Supports clés (mémoire) :** MM50 $88,70 (non confirmé) ; $85,50 (low du 09/06) ; $80,00 (psychologique)
**Résistances clés :** $92,06 (previous_close) ; $97,13 (open du 09/06) ; $100,00 (psychologique — rejet confirmé le 09/06) ; $120,00 (max pain opérationnel)

---

## 3. Mise à jour fondamentale

### ASTSPACE (données officielles)

Aucune donnée disponible. Anomalie structurelle inchangée.

### ASTS (proxy)

| Métrique | Valeur 10h | Valeur 09/06 21h | Δ |
|---------|-----------|-----------|---|
| Market cap | **$34,43B** | $34,43B | **—** 🟢 |
| Forward P/E | **−432,31** | −432,31 | **—** 🟢 |
| EV/Revenue (Yahoo) | **318,42×** | 330,20× | **Compression −11,78×** 🟢 |
| P/B (Yahoo) | **12,73×** | 12,73× | **—** 🟢 |
| Beta | **2,634** | 2,634 | **—** 🟢 |
| Short interest | **18,39%** | 17,60% | **+0,79 pt** 🟡 |
| Consensus PT | **$94,54** (12 analysts) | $94,54 (12 analysts) | **—** 🟢 |
| Divergence consensus | **+2,69%** (si $92,06) | −6,17% | **Divergence mécanique** 🟡 |

Le consensus analystes ($94,54) est désormais **$2,48 au-dessus du `previous_close` JSON ($92,06)** — upside mécanique réduit. Si le cours réel est $88,71 (close 09/06), l'upside reste **+$5,83 (+6,6%)**. Aucun changement dans le nombre d'analystes ni dans les estimates.

**Risque sectoriel :** Signal **UNKNOWN** (données partielles — tous les secteurs affichent momentum_score 10,0 avec returns NaN). XLC (Communication Services) reste dans le **bottom 3**. Malus sectoriel maintenu pour ASTS.

---

## 4. Mise à jour sentiment / options / news

- **News ASTSPACE :** aucune entrée Yahoo Finance ni FMP — silence médiatique total
- **News ASTS :** aucune news spécifique dans le flux du 2026-06-10
- **Options ASTS (anomalie JSON récurrente) :**
  - Max Pain JSON : **$45,00** (aberrant — identique aux anomalies des 03/06 et 09/06 matin) → **[ANOMALIE JSON]**
  - Put/Call JSON : **null** → **[ANOMALIE JSON]**
  - Call OI % JSON : **null** → **[ANOMALIE JSON]**
  - Valeur opérationnelle conservée : max pain **$120,00**, put/call **0,74**, call OI **57,4%**
  - Nearest expiry : **2026-06-12 (J+2)**
  - **Lecture :** l'anomalie JSON empêche toute lecture fiable des flux options. Le pinning gamma vers $120 reste théoriquement haussier mais le gap s'est creusé avec le rejet de $100 le 09/06.
- **Social sentiment :** 0 mention Reddit pour ASTSPACE et ASTS — silence retail total. Score 0,0/10
- **Upgrades/downgrades ASTS :** 12 analysts, PT moyen $94,54 — inchangé
- **Quant :** pas de signaux historiques pour ASTSPACE — p-value insuffisante (p=1,0, n=0)
- **Geo / Accounting / Events :** aucune donnée spécifique pour ASTS. Accounting risk non disponible. Geo risk score 2/10 (🟢). Events : aucun événement corporate détecté.
- **FX exposure ASTSPACE :** exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **Upcoming events :**
  - ASTSPACE : earnings signalé le **2026-06-10** (`days_until: 0`) via FMP — **placeholder glissant non résolu** (>12j de décalage)
  - ASTS : earnings le **2026-08-10** (`days_until: 61`) via yfinance, estimations EPS $−0,29 à $−0,17, Revenues $0,0B
- **Sector rotation :** signal **UNKNOWN** (données partielles). Tous les secteurs affichent momentum_score 10,0 avec returns NaN. XLC dans le **bottom 3** persistant. Malus sectoriel maintenu pour ASTS.

---

## 5. Scoring global

### ASTSPACE (données officielles — placeholder)

| Axe | Score 10h | Pondération | Note |
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

| Axe | Score 10h | Pondération | Commentaire |
|-----|----------|-------------|-------------|
| Catalyseur | 5,0/10 | 35% | Aucun catalyseur imminent, earnings dans 61j. Structure options théoriquement haussière mais anomalie JSON empêche confirmation |
| Valorisation | 4,0/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue 318×). Consensus offre upside mécanique mais fondamentaux non rentables. Score dégradé (vs 4,5/10) |
| Momentum | 6,0/10 | 25% | RSI 51,78 neutre, volume normalisé stable 1,01×. Absence de close, ATR et MM50 empêche toute évaluation fiable du momentum technique |
| **Score Opportunité** | **4,8/10** | — | Non qualifié pour position (score < 6) |
| **Score Global** | **48,5/100** | — | **SURVEILLER** |
| **Score Global Ajusté** | **48,5/100** | — | **SURVEILLER** |

**Malus / Bonus appliqués (Agent Recommandation) :**
- Malus **DONNÉES_PARTIELLES** : close NaN, ATR null, MM50 null — impossibilité de confirmer la tenue du support MM50 $88,70
- Malus **ANOMALIE_OPTIONS_JSON** : max pain $45 aberrant, put/call et call OI null — perte de signal options
- Malus ATR_SPIKE (mémoire) : volatilité intraday extrême persistante (15,0% du cours, range 17,4% le 09/06)
- Malus REJET_100 (mémoire) : test et rejet de $100,94 le 09/06 — structure baissière
- Bonus VOLUME_NORMALISÉ : volume 1,01× — liquidité institutionnelle maintenue
- Malus sectoriel (XLC bottom 3) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (Quality Gate OK)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Action recommandée par l'agent :** SURVEILLER
**Timing :** Neutre
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'ASTSPACE. Ces scores sont fournis uniquement pour confirmer l'anomalie structurelle. Le score **48,5/100 (SURVEILLER)** représente un **downgrade mécanique de −10,0 pts** vs le close 21h UTC 09/06 (58,5 ATTENDRE). Ce downgrade est principalement dû à l'absence de données techniques clés (close NaN, ATR14 null, MM50 null) et à la dégradation du score Valorisation (4,0/10), et non à une nouvelle information fondamentale négative.

---

## 6. Niveaux SL / TP / Ratio R/R

### ASTSPACE (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy, snapshot 10h UTC)

**Impossibles à calculer — ATR14 null, close NaN.**
- Derniers niveaux connus (close 21h UTC 09/06) : SL $62,13 / TP $128,58 / R/R 1,5
- Ces niveaux restent valables mécaniquement mais avec une confiance réduite

> En l'absence d'ATR et de close fiable, aucun niveau SL/TP n'est révisable. Le dernier SL connu ($62,13) est distant. Le risque immédiat reste la perte du support MM50 $88,70 — si confirmée, objectif $80–$85.

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — PROXY ASTS EN DOWNGRADE MÉCANIQUE SURVEILLER 48,5/100 (−10 PTS), DONNÉES TECHNIQUES PARTIELLES (CLOSE NaN, ATR/MM50 NULL), ANOMALIE OPTIONS JSON RÉCURRENT, RSI 51,78 (+1,51 PT), VOLUME NORMALISÉ 1,01× STABLE, SHORT INTEREST 18,39% (+0,79 PT)**

ASTSPACE n'est pas évaluable en l'état. La situation sur le proxy ASTS au snapshot 10h UTC du 10/06 montre une dégradation mécanique sans nouvelle information fondamentale :

1. **Anomalie structurelle confirmée :** ASTSPACE est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis 42+ snapshots consécutifs (erreur Yahoo : *No price history*).
2. **Downgrade mécanique ASTS :** Score global ajusté **48,5/100 (SURVEILLER)** — downgrade de −10,0 pts vs close 21h UTC 09/06 (58,5 ATTENDRE). Ce downgrade est dû à l'absence de données techniques clés et à la dégradation du score Valorisation, et non à une nouvelle information négative.
3. **Données techniques partielles :** close NaN, ATR14 null, MM50 null. Impossibilité de confirmer la tenue du support MM50 $88,70 établi le 09/06.
4. **RSI neutre :** **51,78** — zone neutre, légère hausse de 1,51 pt. Pas de surachat ni de survente.
5. **Volume normalisé stable :** **26,69M** (1,01× moy. 26,41M) — la liquidité institutionnelle reste normalisée, ce qui valide que le mouvement de prix est réel.
6. **Anomalie options JSON récurrente :** Max pain **$45,00** (aberrant — identique aux anomalies des 03/06 et 09/06 matin). Valeur opérationnelle conservée : **$120,00**. Put/call et call OI null — perte de signal options.
7. **Short interest en hausse :** **18,39%** (+0,79 pt) — léger regain de shorts, pas de setup squeeze.
8. **Divergence price vs close 09/06 :** `previous_close` JSON $92,06 vs close officiel 21h UTC 09/06 $88,71 (+3,78%). Cette divergence est probablement un artefact de données partielles ou de delay de snapshot.
9. **Signal sectoriel UNKNOWN :** Données sectorielles partielles (tous les secteurs à momentum_score 10,0). XLC bottom 3 persistant.
10. **Earnings placeholder glissant non résolu :** FMP signale un earnings ASTSPACE le **2026-06-10** (`days_until: 0`), glissement persistant depuis le **29/05** (>12j de décalage).
11. **Structure baissière du 09/06 :** Le rejet de $100,94 et le close sur MM50 $88,70 restent le dernier signal technique fiable. En l'absence de confirmation au-dessus de MM50, le risque de retour vers $80–$85 persiste.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer ASTSPACE de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence accrue :** Le snapshot 10h UTC est techniquement indéterminable. Le downgrade vers SURVEILLER est mécanique. Attendre le **close officiel du 10/06** pour confirmer ou infirmer la tenue du MM50 $88,70
- **Si close < MM50 ($88,70)** sur volume >0,8× → révision vers SURVEILLER confirmée avec objectif $80–$85
- **Si close > $90** sur volume maintenu (>0,8×) → possibilité de retour vers ATTENDRE
- **Le niveau $100** reste une résistance majeure — ne pas entrer long sans confirmation de break au-dessus de $100 sur volume >1,0×
- **Monitoring comportement options J+2** (expiration 2026-06-12) autour du max pain opérationnel $120
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (breakout confirmé au-dessus de $100) avant toute entrée
- **Ne pas entrer long sans close fiable au-dessus de $92 sur volume >0,8×**

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 10h UTC), data/recommandations_latest.json, data/sector_rotation_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/events_latest.json, data/quant_report_latest.json, data/validation_report.txt — aucune donnée hallucinée.*
