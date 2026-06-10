# ASTS — Mise à Jour Snapshot 10h UTC (2026-06-10)

> **Snapshot 10h UTC** : données techniques partielles (close NaN, ATR/MM50 null), anomalie options JSON récurrente, downgrade mécanique **ATTENDRE → SURVEILLER** (Score Global 48,5/100, −10 pts). Divergence price vs close officiel 09/06 ($92,06 vs $88,71). RSI **51,78** (+1,51 pt), volume normalisé **1,01×** stable. Profil fondamental spéculatif extrême inchangé. Thèse modifiée avec réserves.

---

## Résumé des Changements depuis le Close 21h UTC 09/06

| Indicateur | Close 21h UTC 09/06 | Snapshot 10h UTC 10/06 | Delta |
|-----------|---------------------|------------------------|-------|
| **Cours** | **$88,71** | **$92,06** (previous_close) | **+$3,35 (+3,78%)** 🔴 |
| Close réel | $88,71 | **NaN** | **[DONNÉES PARTIELLES]** 🔴 |
| RSI 14j | **50,27** | **51,78** | **+1,51 pts** 🟢 |
| ATR 14j | $13,29 | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| MM50 | $88,70 | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| Volume rel. | **1,01×** | **1,01×** (26,69M vs 26,41M) | **Stable** 🟢 |
| Market Cap | $34,43B | **$34,43B** | **—** 🟢 |
| Forward P/E | −432,31 | **−432,31** | **—** 🟢 |
| EV/Revenue (Yahoo) | 330,20× | **318,42×** | **−11,78×** 🟢 |
| P/B (Yahoo) | 12,73× | **12,73×** | **—** 🟢 |
| Consensus PT | $94,54 | **$94,54** | **—** 🟢 |
| Short Interest | 17,60% | **18,39%** | **+0,79 pt** 🟡 |
| Max Pain | $120,00 (fiable) | **$45,00** (aberrant) | **[ANOMALIE JSON]** 🔴 |
| Put/Call Ratio | 0,74 | **null** | **[ANOMALIE JSON]** 🔴 |
| Call OI % | 57,4% | **null** | **[ANOMALIE JSON]** 🔴 |
| **Score Global ajusté** | **58,5 (ATTENDRE)** | **48,5 (SURVEILLER)** | **−10,0 pts** 🔴 |

**Verdict :** le snapshot 10h UTC du 2026-06-10 présente des **données techniques partielles** (close NaN, ATR14 null, MM50 null) et une **anomalie options JSON récurrente** (max pain $45 aberrant vs $120 opérationnel). Le downgrade mécanique vers **SURVEILLER** (48,5/100) résulte principalement de la dégradation du score Valorisation (4,0/10) et de l'impossibilité de confirmer la tenue du support MM50 $88,70 en l'absence de données actualisées. Le RSI remonte légèrement à 51,78 (+1,51 pt) mais reste dans la zone neutre. Le volume normalisé 1,01× est stable — liquidité institutionnelle maintenue.

> **Note importante :** le `previous_close` Yahoo affiche $92,06, ce qui diverge du close officiel 21h UTC du 09/06 ($88,71). Cette divergence de +$3,35 (+3,78%) est probablement un artefact de données partielles ou de delay de snapshot.

---

## Mise à Jour Technique

- **Cours :** [DONNÉES PARTIELLES] — close NaN dans `latest.json`. `previous_close` $92,06 diverge du close officiel $88,71 du 09/06
- **RSI 14j :** **51,78** — zone neutre, légère hausse (+1,51 pt vs 50,27). Pas de surachat ni de survente
- **ATR 14j :** **null** — donnée manquante. Dernier ATR connu $13,29 (15,0% du cours). Impossible de calculer les niveaux SL/TP
- **MM50 :** **null** — donnée manquante. Dernière valeur connue $88,70. Perte de ce support = risque de retour vers $80–$85
- **MM200 :** N/A
- **Volume 10h :** 26,69M vs moy. 20j 26,41M (**1,01×**) — **stable**. La liquidité institutionnelle reste normalisée, ce qui valide que le mouvement de prix est réel
- **52W high :** $133,86 — repli à **−33,7%** (inchangé)
- **52W low :** $35,33
- **Short Interest :** 18,39% (+0,79 pt) — léger regain de shorts, pas de setup squeeze
- **Supports clés (mémoire) :** MM50 $88,70 (non confirmé) ; $85,50 (low du 09/06) ; $80,00 (psychologique)
- **Résistances clés :** $92,06 (previous_close) ; $97,13 (open du 09/06) ; $100,00 (psychologique — **rejet confirmé le 09/06**) ; $115,00 (ancien support)
- **Timing verdict :** **Indéterminable** — absence de close, ATR et MM50 empêche toute évaluation technique fiable. La structure du 09/06 (rejet $100, close sur MM50) reste baissière à court terme
- **Score Momentum :** [DONNÉES PARTIELLES] — RSI neutre, volume stable, mais absence de MM50 et de close

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. La mutation reste **exclusivement technique/scoring**.

- **Market Cap :** $34,43B — inchangé
- **Forward P/E :** −432,31 (profil non rentable, inchangé)
- **EV/EBITDA :** −85,48
- **EV/Revenue :** **318,42×** (Yahoo) / **355,70×** (FMP annual FY2025) — compression mécanique de −11,78× Yahoo vs close 09/06
- **P/B :** 12,73× (Yahoo) / 10,10× (FMP annual) — inchangé
- **Beta :** 2,634 — sensibilité très supérieure au marché (inchangée)
- **Short Interest :** 18,39% (+0,79 pt) — pas de squeeze setup
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes) — inchangé
- **Divergence consensus :** upside mécanique **+2,69%** si cours = $92,06 (previous_close) ; **+6,59%** si cours = $88,71 (close 09/06)
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK** (`quality_gate_2026-06-10.json`)

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-10 émet un signal macro **UNKNOWN** (données partielles — tous les secteurs affichent momentum_score 10,0 avec returns NaN). XLC reste dans le **bottom 3** (tied). Faiblesse sectorielle persistante — malus sectoriel maintenu.

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence consensus **positive** si cours ~$88,71 (+6,59%) mais mécaniquement réduite si `previous_close` $92,06 (+2,69%)
- **Options :**
  - **Max Pain :** **$45,00** — **anomalie JSON récurrente** (valeur aberrante, identique aux anomalies des 03/06 et 09/06 matin). Valeur opérationnelle conservée : **$120,00**
  - **Put/Call Ratio :** **null** — anomalie JSON. Dernière valeur fiable : **0,74**
  - **Call OI % :** **null** — anomalie JSON. Dernière valeur fiable : **57,4%**
  - Nearest expiry : **2026-06-12** (J+2)
  - **Lecture :** le pinning gamma vers $120 reste théoriquement haussier mais le gap s'est creusé avec le rejet de $100 le 09/06. L'anomalie JSON empêche toute lecture fiable des flux options
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_2026-06-10.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_2026-06-10.json` — score 2/10, pas d'événement pertinent)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-10

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+61) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-06-12 (J+2)** — max pain opérationnel $120 au-dessus du spot (+35,3% si spot ~$88,71)

---

## Scoring Global — Snapshot 10h UTC (2026-06-10)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 5,0/10 | 35% | Aucun catalyseur imminent, earnings dans 61j. Structure options théoriquement haussière (call OI 57,4%, put/call 0,74) mais anomalie JSON empêche confirmation |
| Valorisation | 4,0/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue 318×). Consensus offre upside mécanique mais fondamentaux non rentables. Score dégradé par rapport à l'analyse précédente (4,5/10) |
| Momentum | 6,0/10 | 25% | RSI 51,78 neutre, volume normalisé stable 1,01×. Absence de close, ATR et MM50 empêche toute évaluation fiable du momentum technique |
| **Score Opportunité** | **4,8/10** | | |

**Malus / Bonus appliqués (règles agents) :**
- Malus **DONNÉES PARTIELLES** : close NaN, ATR null, MM50 null — impossibilité de confirmer la tenue du support MM50 $88,70
- Malus **ANOMALIE OPTIONS JSON** : max pain $45 aberrant, put/call et call OI null — perte de signal options
- Malus ATR_SPIKE (mémoire) : volatilité intraday extrême persistante (15,0% du cours, range 17,4% le 09/06)
- Malus REJET_100 (mémoire) : test et rejet de $100,94 le 09/06 — structure baissière
- Bonus VOLUME_NORMALISÉ : volume 1,01× — liquidité institutionnelle maintenue
- Malus sectoriel (XLC bottom 3) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (`accounting_risk_latest.json` absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite :** 48,5/100 — Seuil **SURVEILLER (35–49)**. Downgrade de −10,0 pts vs close 21h UTC 09/06 (58,5 ATTENDRE).

> **Note :** le JSON `recommandations_2026-06-10.json` attribue à ASTS un score global ajusté de **48,5/100** avec action **SURVEILLER**, timing **Neutre**. Ce downgrade est principalement mécanique : il reflète l'impossibilité de confirmer la tenue du support MM50 et la dégradation du score Valorisation (4,0/10) dans un contexte de données partielles.

---

## Niveaux et Ratio R/R

- **Cours actuel :** [INDÉTERMINÉ] — close NaN. `previous_close` $92,06 (diverge du close officiel $88,71)
- **Stop-loss suggéré :** **Impossible à calculer** — ATR14 null. Dernier SL connu : $62,13 (cours − 2×ATR = $88,71 − $26,58)
- **Take-profit suggéré :** **Impossible à calculer** — ATR14 null. Dernier TP connu : $128,58 (cours + 3×ATR = $88,71 + $39,87)
- **Ratio R/R :** **Indéterminable**

**Révision :** SL et TP non révisables en l'absence d'ATR et de close fiable. Les derniers niveaux connus ($62,13 / $128,58) restent valables mécaniquement mais avec une confiance réduite.

- Le consensus analystes ($94,54) offre un upside de **+$2,48** si cours = $92,06 ou de **+$5,83** si cours = $88,71
- **Zone d'intérêt potentielle :** indéterminable sans MM50
- **Résistance immédiate :** $92,06 (previous_close) ; $97,13 (open du 09/06) ; $100,00 (psychologique — rejet confirmé)
- **Alerte MM50 :** le niveau $88,70 n'est pas confirmé dans ce snapshot. Si le cours réel est sous MM50 → risque de retour vers $80–$85

---

## Conclusion

**Thèse modifiée : ATTENDRE → SURVEILLER — snapshot 10h UTC avec données techniques partielles (close NaN, ATR/MM50 null), anomalie options JSON récurrente, score global ajusté 48,5/100 (−10 pts).**

Le snapshot du 2026-06-10 10h UTC révèle une **dégradation mécanique du scoring** sans nouvelle information fondamentale ou technique fiable. Le downgrade vers SURVEILLER (48,5/100) est principalement dû à :

1. **L'absence de données techniques clés** (close NaN, ATR14 null, MM50 null), ce qui empêche de confirmer que le cours tient au-dessus du support MM50 $88,70 établi le 09/06
2. **La dégradation du score Valorisation à 4,0/10** (vs 4,5/10), probablement liée à l'impossibilité de recalculer les multiples avec un close fiable
3. **L'anomalie options JSON récurrente** qui prive le signal d'une confirmation haussière (put/call 0,74, call OI 57,4%)

**Changements structurants depuis le close 21h UTC 09/06 :**
1. **Downgrade mécanique SURVEILLER** — score global 48,5/100 (−10 pts), hors de la zone ATTENDRE
2. **Données techniques partielles** — close NaN, ATR14 null, MM50 null. Impossibilité de confirmer la tenue du support
3. **RSI 51,78** (+1,51 pt) — reste neutre, légère amélioration sans signification
4. **Volume normalisé 1,01×** — stable, liquidité institutionnelle maintenue (signal positif)
5. **Short Interest 18,39%** (+0,79 pt) — léger regain de shorts
6. **Anomalie options JSON récurrente** — max pain $45 aberrant, données options corrompues
7. **Divergence price vs close 09/06** — `previous_close` $92,06 vs close officiel $88,71 (+3,78%)
8. **Signal sectoriel UNKNOWN** — données sectorielles partielles (tous les secteurs à momentum_score 10,0)
9. **Profil fondamental inchangé** — non rentable, EV/Revenue 318×, P/B 12,73×
10. **Aucun événement corporate** — pas de catalyseur

**Alertes actives :**
- **DONNÉES PARTIELLES** — close NaN, ATR14 null, MM50 null. Impossibilité de confirmer la tenue du support MM50 $88,70
- **ANOMALIE OPTIONS JSON** — max pain $45 aberrant (valeur opérationnelle $120 conservée), put/call et call OI null
- **ATR_SPIKE (haut)** — volatilité extrême persistante (15,0% du cours, range intraday 17,4% le 09/06)
- **REJET_100** — test et rejet de $100,94 le 09/06 — structure baissière
- **Profil non rentable** — multiples négatifs, aucune visibilité sur la rentabilité
- **Secteur Communication Services (XLC)** — bottom 3 persistant
- **Short Interest élevé** — 18,39%, pas de squeeze setup mais pression vendeuse présente

**Verdict opérationnel :** la configuration du 10/06 10h UTC est **techniquement indéterminable** en raison des données partielles. Le downgrade vers SURVEILLER est **mécanique** et non fondé sur une nouvelle information. La structure baissière du 09/06 (rejet $100, close sur MM50) reste le dernier signal technique fiable. Le volume normalisé stable est le seul élément positif.

**Prochaines étapes :**
- Surveiller impérativement le **close officiel du 10/06** pour confirmer ou infirmer la tenue du MM50 $88,70
- Si close < MM50 ($88,70) sur volume >0,8× → révision vers **SURVEILLER** confirmée avec objectif $80–$85
- Si close > $90 sur volume maintenu (>0,8×) → possibilité de retour vers ATTENDRE
- Le niveau $100 reste une résistance majeure — ne pas entrer long sans confirmation de break au-dessus de $100 sur volume >1,0×
- Monitoring comportement options J+2 (expiration 2026-06-12) autour du max pain opérationnel $120
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (breakout confirmé au-dessus de $100) avant toute entrée
- **Ne pas entrer long sans close fiable au-dessus de $92 sur volume >0,8×**

---

*Généré par le système Argus-IA — Snapshot 2026-06-10 10h UTC (données partielles : close NaN, RSI 51,78, volume 1,01×, score global 48,5 SURVEILLER, anomalie options JSON, thèse modifiée ATTENDRE → SURVEILLER)*
