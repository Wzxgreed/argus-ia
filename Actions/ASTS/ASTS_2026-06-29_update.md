# ASTS — Mise à Jour 2026-06-29 (Snapshot 10h UTC)

> **Close $71,45** : rebond technique +8,88% vs previous close $65,62, mais sur **volume sous-moyenne 0,85×** et **cassure confirmée du pivot absolu $72,59** au close. **Short Interest aggravé** à 20,98% (+2,59 pts vs 23/06). Score global JSON dégradé **46,8/100 (SURVEILLER)** vs 50,5 (ATTENDRE) au snapshot 17h UTC 23/06. Thèse **modifiée de ATTENDRE à SURVEILLER** — le rebond n'a pas réparé la cassure structurelle du pivot et la pression vendeuse s'intensifie.

---

## Résumé des Changements depuis l'Analyse Précédente (Snapshot 17h UTC 23/06)

| Indicateur | Snapshot 17h UTC 23/06 | Snapshot 10h UTC 29/06 | Delta |
|-----------|------------------------|------------------------|-------|
| **Cours** | **$76,15** | **$71,45** | **−6,17%** 🔴 |
| Change % session | +4,04% (vs $73,19) | **+8,88%** (vs $65,62) | **Rebond isolé** 🟡 |
| Cumul inter-sessions | — | **$76,15 → $65,62 → $71,45** | **−6,17% net** 🔴 |
| **RSI 14j** | **25,31** | **34,39** | **+9,08 pts** 🟢 |
| **ATR 14j** | **$9,87** | **$8,50** | **−$1,37** 🟢 |
| **MM50** | **$87,68** | **$86,23** | **−$1,45** (mécanique) 🟡 |
| **Cours vs MM50** | **−13,1%** | **−17,1%** | **Aggravation écart** 🔴 |
| **Volume rel.** | **0,438×** (12,10M) | **0,85×** (22,16M) | **+94%** 🟡 |
| Volume absolu | 12,10M | **22,16M** | **+83%** 🟡 |
| Market Cap (Yahoo) | $29,56B | **$27,73B** | **−$1,83B** 🔴 |
| Forward P/E | −371,10 | **−348,20** | **Légère amélioration mécanique** 🟢 |
| EV/Revenue (Yahoo) | 263,831× | **257,711×** | **−6,1×** 🟢 |
| P/B (Yahoo) | 10,930× | **10,255×** | **−0,675 pt** 🟢 |
| **Short Interest** | **18,39%** | **20,98%** | **+2,59 pts** 🔴 |
| Consensus PT | $94,54 | **$94,54** | **—** 🟢 |
| Divergence consensus | +24,1% | **+32,3%** | **Upside mécanique accru** 🟡 |
| **Options Max Pain (JSON)** | **$100,00** | **$45,00** | **Anomalie JSON récurrente** 🔴 |
| Options Put/Call (JSON) | 0,69 | **null** | **Anomalie JSON** 🔴 |
| Options Call OI % (JSON) | 59,3% | **null** | **Anomalie JSON** 🔴 |
| **Score Global ajusté (JSON)** | **50,5 (ATTENDRE)** | **46,8 (SURVEILLER)** | **−3,7 pts** 🔴 |
| **Score Opportunité** | **5,3/10** | **5,5/10** | **+0,2 pt** 🟢 |
| **Score Momentum** | **5,0/10** | **4,0/10** | **−1,0 pt** 🔴 |
| **Score Catalyseur** | **6,0/10** | **6,5/10** | **+0,5 pt** 🟢 |
| **Score Valorisation** | **5,0/10** | **5,5/10** | **+0,5 pt** 🟢 |

**Verdict :** entre le 23/06 et le 29/06, le cours a subi une **dérive baissière inter-session de −13,8%** ($76,15 → $65,62) suivie d'un **rebond technique isolé de +8,88%** ($65,62 → $71,45). Le rebond du 29/06 s'opère sur un volume amélioré (0,85× vs 0,438×) mais reste **sous la moyenne 20j**. Le **pivot absolu $72,59 est cassé au close** ($71,45). Le **short interest s'aggrave à 20,98%**, signalant une intensification de la pression vendeuse. Le score global JSON dégrade la thèse de ATTENDRE (50,5) à SURVEILLER (46,8). Les fondamentaux spéculatifs extrêmes sont inchangés.

---

## Anomalies de Données

1. **Anomalie options JSON récurrente** : le max pain JSON est retombé à **$45,00** (valeur aberrante, vs $100,00 opérationnelle historique). Put/call et call OI % sont **nulls** dans le JSON. C'est la **10e occurrence** de cette anomalie depuis le 10/06. **Les valeurs opérationnelles calibrées manuellement sont conservées : max pain $100,00, put/call 0,70, call OI 58,9%**.
2. **Short Interest révisé à la hausse** : passage de 18,39% à 20,98% — hausse de +2,59 pts en 6 jours. Seuil psychologique des 20% franchi. Pression vendeuse accrue, pas de squeeze setup détecté (volume stable, pas de gap haussier sur volume explosion).
3. **Forward P/E mécanique** : −348,20 vs −371,10 — amélioration mécanique due à la baisse du cours entre les sessions, sans changement d'estimations EPS.
4. Le rapport de validation `data/validation_report.txt` ne signale ni erreur ni warning pour ASTS. AST (ticker distinct) est en erreur — ne pas confondre.

---

## Mise à Jour Technique

- **Cours :** $71,45 — rebond +8,88% vs previous close $65,62. **Cumul depuis le close 23/06 ($76,15) : −6,17%**. Le cours a probablement chuté en fin de semaine (24–28/06) pour atteindre $65,62, puis rebondir. Low du 29/06 : $64,51 — test du support psychologique $65,00
- **RSI 14j :** **34,39** — sortie de la **survente extrême** (25,31) mais reste en **zone de survente** (<35). Hausse de 9,08 pts, signal de relief technique mais pas de retournement de tendance
- **ATR 14j :** $8,50 (ATR relatif **11,9%** du cours) — volatilité en contraction (−$1,37 vs 23/06), mais reste élevée. Le trigger ATR_SPIKE du DRAFT est à la limite du seuil (11,90%)
- **MM50 :** $86,23 — cours **−17,1% sous** la moyenne. Écart **aggravé** vs −13,1% au 23/06. Résistance dynamique très lointaine
- **MM200 :** N/A
- **Volume :** 22,16M vs moy. 20j 26,04M (**0,85×**) — **volume en récupération** vs le collapse 0,438× du 23/06, mais **toujours sous la moyenne**. Lecture : le rebond du 29/06 attire un peu plus de liquidité que le rebond du 23, mais la direction reste incertaine. Pas de confirmation d'épuisement vendeur, pas de nouveaux acheteurs massifs non plus
- **52W high :** $133,86 — repli à **−46,6%** (vs −43,1% au 23/06)
- **52W low :** $36,08
- **Supports clés :** $64,51 (low du 29/06, **testé et tenu en séance**) ; $60,00 (zone de consolidation mai 2026) ; $55,00 (support structurel historique)
- **Résistances clés :** $72,59 (pivot absolu, **cassé au close**) ; $80,66 (previous close 22/06) ; $85,43 (vrai previous close 22/06) ; $86,23 (MM50) ; $100,00 (psychologique + max pain opérationnel)
- **Timing verdict :** **Défavorable** — aggravé. Cours sous MM50 avec écart extrême (−17,1%), pivot $72,59 cassé au close. Le rebond +8,88% n'a pas permis de récupérer le pivot
- **Score Momentum (JSON) :** 4,0/10 — dégradation de 1,0 pt vs 23/06. Le rebond n'a pas convaincu l'algorithme de scoring

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. Données fondamentales inchangées en substance, dérives mécaniques dues au rebond/baisse du cours.

- **Market Cap :** $27,73B (Yahoo) / $25,32B (FMP)
- **Forward P/E :** −348,20 (profil non rentable, amélioration mécanique)
- **EV/EBITDA :** −69,182 (Yahoo) / −68,189 (FMP annual)
- **EV/Revenue :** 257,711× (Yahoo) / 355,7× (FMP annual) — multiples spéculatifs extrêmes persistants
- **P/B :** 10,255× (Yahoo) / 10,096× (FMP annual) — légère baisse mécanique Yahoo
- **Beta :** 2,634 — sensibilité très supérieure au marché
- **Short Interest :** **20,98%** (vs 18,39% au 23/06) — **hausse significative de +2,59 pts**. Pression vendeuse accrue, seuil des 20% franchi
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes, 2 couverts le mois dernier, 7 le trimestre dernier). Divergence **+32,3% upside** ($94,54 vs $71,45) — upside mécanique accru par la baisse inter-session
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK**

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-29 émet un signal macro **NEUTRAL** avec régime UNKNOWN. **XLC (Communication Services)** reste dans le **bottom 3** avec momentum_score **0,0**. XLK (Technology) est **top 1** (momentum_score 10,0). Malus sectoriel maintenu (−0,5 pt). ASTS est classé Technology mais son sous-secteur (Communication Equipment) est aligné avec XLC — faiblesse persistante.

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence consensus **+32,3% upside** (accru par la baisse inter-session)
- **Options (JSON anomalie — valeurs opérationnelles conservées) :**
  - **Max Pain (opérationnel) :** **$100,00** — Cours $71,45 reste **−28,6% sous le Max Pain**
  - **Put/Call Ratio (opérationnel) :** **0,70** — positionnement défensif/baissier stable
  - **Call OI % (opérationnel) :** **58,9%** — skew call stable
  - Nearest expiry : **2026-07-02** (J+3)
  - **Lecture :** le positionnement options n'a pas changé en substance. Les valeurs JSON étant corrompues, les valeurs opérationnelles historiques sont utilisées. Les calls OTM $80+ restent profondément OTM. Le max pain $100 est à +39,9% du spot — pinning gamma très improbable
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_2026-06-29.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_risk_latest.json` — pas de données récentes pertinentes)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-29 (`news_2026-06-29.json` vide). Le mouvement reste purement technique

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+42) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-07-02 (J+3)** — max pain $100 au-dessus du spot (+39,9%). Pinning gamma très improbable. Put/call 0,70 reflète un positionnement défensif stable

---

## Scoring Global — Snapshot 2026-06-29

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 6,5/10 | 35% | Aucun catalyseur imminent, earnings dans 42j. Structure options historiquement haussière (call OI 58,9%) mais stable. Put/call 0,70 = couverture baissière maintenue |
| Valorisation | 5,5/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue FMP 355,7×). Consensus offre un upside mécanique +32,3% mais fondamentaux non rentables. P/B 10,26× Yahoo — reste élevé |
| Momentum | 4,0/10 | 25% | RSI 34,39 en survente atténuée mais persistante, cours −17,1% sous MM50, volume 0,85× = rebond partiellement convaincu mais insuffisant. Configuration baissière dominante |
| **Score Opportunité** | **5,5/10** | | |

**Malus / Bonus appliqués (règles agents) :**
- Malus **COURS_SOUS_MM50 aggravé** : cours −17,1% sous MM50 $86,23 — écart extrême, aggravation vs −13,1%
- Malus **RSI_SURVENTE** : RSI 34,39 < 35 — survente technique persistante
- Malus **PIVOT_CASSE** : close $71,45 < pivot $72,59 — cassure confirmée du pivot absolu au close
- Malus **SHORT_INTEREST_AGGRAVE** : 20,98% > 20% — pression vendeuse accrue, seuil psychologique franchi
- Malus **VOLUME_SOUS_MOYENNE** : volume 0,85× — rebond partiel mais pas de confirmation de conviction
- Malus sectoriel (XLC bottom 3, momentum 0,0) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (`accounting_risk_latest.json` absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite (JSON) :** 54,8/100 → **46,8 ajusté** (−8,0 pts de malus). Seuil **SURVEILLER (35–49)**, milieu-haut de fourchette. Le JSON `recommandations_2026-06-29.json` attribue à ASTS un score global ajusté de **46,8/100** avec action **SURVEILLER**, timing **Défavorable**, SL $54,45, TP $96,95, ratio R/R 1,5.

---

## Niveaux et Ratio R/R

- **Cours actuel :** $71,45
- **Stop-loss suggéré :** $54,45 (cours − 2×ATR = $71,45 − $17,00)
- **Take-profit suggéré :** $96,95 (cours + 3×ATR = $71,45 + $25,50)
- **Ratio R/R :** 1,5:1

**Révision :** SL et TP **révisés** vs snapshot 17h UTC 23/06 (SL $56,41 / TP $105,76) en raison de la baisse du cours (−$4,70) et de la contraction ATR (−$1,37).
- Le SL à $54,45 correspond à la zone $55–$60 (support structurel historique majeur). Distance SL = 23,8% du cours
- Le TP $96,95 correspond au consensus analystes ($94,54) à +2,5% — probabilité d'atteinte faible sans catalyseur majeur
- Le consensus analystes ($94,54) est **+$23,09 au-dessus du cours** — upside consensus mécanique +32,3%
- **Zone d'intérêt potentielle :** $64–$66 (test du low du 29/06 + support psychologique)
- **Résistance immédiate :** $72,59 (pivot absolu, **cassé**) ; $80,66 (previous close 22/06) ; $85,43 (vrai previous close 22/06) ; $86,23 (MM50)
- **Alerte options J+3 :** Max Pain opérationnel $100 à +39,9%. Put/call 0,70 = couverture baissière structurée. Pinning gamma théoriquement possible mais très improbable sous $80
- **Alerte volume :** 0,85× = liquidité en récupération mais toujours sous la moyenne. Le rebond de +8,88% est plus convaincu que celui du 23/06 (0,438×) mais **pas encore confirmatoire d'un retournement**
- **Alerte short interest :** 20,98% — seuil des 20% franchi. Surveillance impérative du comportement des shorts

---

## Conclusion

**Thèse modifiée de ATTENDRE à SURVEILLER — avec prudence majeure.**

Le snapshot du 29/06 apporte un **rebond technique de +8,88%** à $71,45 qui efface partiellement la dérive baissière inter-session ($76,15 → $65,62, −13,8%). Le score global JSON dégrade la thèse de 50,5 (ATTENDRE) à 46,8 (SURVEILLER), franchissant le seuil inférieur de la fourchette ATTENDRE. **Ce rebond est partiellement convaincu mais insuffisant pour réparer la cassure structurelle.**

**Configuration technique :**
1. **Dérive baissière inter-session** : $76,15 → $65,62 (−13,8%) entre le 23/06 et le 28/06 — probablement une continuation de la distribution active
2. **Rebond +8,88% du 29/06** : s'opère sur volume 0,85× (meilleur que le 0,438× du 23/06 mais toujours sous la moyenne). Pas de confirmation de retournement de tendance
3. **Pivot $72,59 cassé au close** : close $71,45 < $72,59. Low $64,51 en séance = test du support $65. Le rebond intraday depuis $64,51 est positif, mais le close reste sous le pivot
4. **RSI en survente atténuée** : 34,39 — sortie de la survente extrême (25,31) mais reste <35. Pas de signal de retournement
5. **Écart MM50 aggravé** : −17,1% vs −13,1% — résistance dynamique très lointaine
6. **Short Interest aggravé** : 20,98% (+2,59 pts) — pression vendeuse accrue, pas de squeeze setup
7. **Options inchangées** (valeurs opérationnelles) : max pain $100 à +39,9%. Put/call 0,70 stable. Call OI 58,9%
8. **Score Momentum JSON** : 4,0/10 — dégradation de 1,0 pt, confirmant le scepticisme de l'algorithme
9. **Aucune news** : le mouvement est purement technique

**Alertes actives (mises à jour) :**
- **PIVOT_CASSE** — close $71,45 < pivot $72,59 — cassure confirmée du niveau absolu
- **COURS_SOUS_MM50 aggravé** — cours −17,1% sous MM50 $86,23 — écart extrême
- **RSI_SURVENTE** — RSI 34,39 < 35 — survente persistante
- **SHORT_INTEREST_AGGRAVE** — 20,98% > 20% — pression vendeuse accrue
- **VOLUME_SOUS_MOYENNE** — volume 0,85× — rebond sans pleine conviction
- **ATR_SPIKE** — ATR relatif 11,9% du cours ($8,50) — volatilité élevée
- **Profil non rentable** — EPS estimé négatif, multiples extrêmes
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (momentum_score 0,0)
- **Options J+3** — Max Pain opérationnel $100 à +39,9%. Put/call 0,70 = couverture baissière structurée
- **Anomalie options JSON** — max pain $45 aberrant, put/call null, call OI null (10e occurrence)

**Verdict opérationnel :** le rebond de +8,88% est **techniquement bienvenu et partiellement convaincu** (volume 0,85× vs 0,438× précédent), mais il **n'a pas permis de récupérer le pivot absolu $72,59**. Le close sous ce niveau est baissier. Le short interest à 20,98% est un signal d'alerte : les vendeurs à découvert s'empilent, ce qui augmente le risque de squeeze mais aussi la probabilité d'accélération baissière si le cours ne tient pas.

**Scénarios à court terme :**
- **Optimiste (15%)** : défense de $64,50, consolidation au-dessus de $70, puis rebond vers $75–$78 sur volume >1,0× dans les 2–3 prochains jours. Nécessite une confirmation au-dessus de $72,59
- **Central (45%)** : range $64–$72 avec volume modéré, attente d'un catalyseur. Le plus probable compte tenu du volume sous-moyenne et de la pression vendeuse
- **Pessimiste (40%)** : cassure confirmée de $64,50 au close sur volume >0,8×, accélération baissière vers $55–$60. Risque élevé si le short interest continue de monter

**Prochaines étapes :**
- Surveiller **impérativement** la tenue du niveau **$64,50** (low du 29/06) au close des prochaines sessions
- Surveiller le volume : si le rebond se confirme avec volume >1,0× → signal positivement convaincu. Si volume reste <0,8× → consolidation sans direction
- Si close > $72,59 sur volume >0,8× → réviser vers ATTENDRE (réparation du pivot)
- Si close < $64,50 sur volume >0,8× → réviser vers **ÉVITER** avec objectif $55–$60
- **Ne pas entrer long sans confirmation au-dessus de $86 (MM50) sur volume >0,8×**
- Monitoring comportement options J+3 (expiration 2026-07-02) — les calls $80+ sont menacés
- Monitoring short interest — seuil 20% franchi. Si >22% → risque de squeeze ou d'accélération baissière
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (breakout confirmé) avant toute entrée

---

*Généré par le système Argus-IA — Snapshot 2026-06-29, 10h UTC (cours $71,45, RSI 34,39, volume 0,85×, score global 46,8 SURVEILLER, divergence consensus +32,3%, cours −17,1% sous MM50 $86,23, low $64,51, options opérationnelles : max pain $100,00, put/call 0,70, call OI 58,9%, short interest 20,98%)*
