# ASTS — Mise à Jour Pré-Ouverture (2026-06-16)

> **Close $87,57** : stabilité mécanique pré-ouverture US — données brutes identiques au snapshot 21h UTC 15/06. Volume légèrement révisé à **23,92M / 0,867×** (vs 23,57M / 0,855×), RSI **36,00** inchangé, cours **−1,8% sous MM50 $89,13**. Anomalie options JSON **récurrente détectée et traitée** (max pain $28,0 aberrant → valeur opérationnelle $100,00 conservée). Score global ajusté **39,2/100 (SURVEILLER)** confirmé sans modification. Thèse **SURVEILLER confirmée** — le FULL REFRESH déclenché par `agents/detect_major_events` est classé **faux positif** (les triggers PRICE_GAP et ATR_SPIKE reflètent le close 15/06 déjà intégré).

---

## Résumé des Changements depuis le Snapshot 21h UTC 15/06

| Indicateur | Snapshot 21h UTC 15/06 | Pré-ouverture 16/06 | Delta |
|-----------|------------------------|---------------------|-------|
| **Cours** | **$87,57** | **$87,57** | **—** 🟢 |
| RSI 14j | **36,00** | **36,00** | **—** 🟢 |
| ATR 14j | **$12,80** | **$12,80** | **—** 🟢 |
| MM50 | **$89,13** | **$89,13** | **—** 🟢 |
| Cours vs MM50 | **−1,8%** | **−1,8%** | **—** 🟢 |
| **Volume rel.** | **0,855×** (23,57M) | **0,867×** (23,92M) | **+0,012× (+1,5%)** 🟡 |
| Volume absolu | 23,57M | **23,92M** | **+0,35M (+1,5%)** 🟡 |
| Market Cap | $33,99B | **$33,99B** | **—** 🟢 |
| Forward P/E | −426,75 | **−426,75** | **—** 🟢 |
| EV/Revenue (Yahoo) | 296,26× | **314,41×** | **+18,2×** 🔴 |
| EV/Revenue (FMP annual) | 355,70× | **355,70×** | **—** 🟢 |
| P/B (Yahoo) | 12,57× | **12,57×** | **—** 🟢 |
| Consensus PT | $94,54 | **$94,54** | **—** 🟢 |
| Divergence consensus | +7,97% | **+7,97%** | **—** 🟢 |
| Short Interest | 18,39% | **18,39%** | **—** 🟢 |
| **Max Pain** | **$100,00** | **$28,00 (anomalie JSON)** | **Aberrant** 🔴 |
| Put/Call Ratio | 0,44 | **0,00 (anomalie JSON)** | **Aberrant** 🔴 |
| Call OI % | 69,7% | **100,0% (anomalie JSON)** | **Aberrant** 🔴 |
| **Score Global ajusté** | **39,2 (SURVEILLER)** | **39,2 (SURVEILLER)** | **Inchangé** 🟢 |

**Verdict :** pré-ouverture du 16/06 affiche une **stabilité quasi-totale** vs le snapshot 21h UTC 15/06. Les données Yahoo Finance n'ont pas muté (close identique, RSI/ATR/MM50 inchangés). Le volume est légèrement révisé à la hausse (+0,35M) par le worker daemon, sans impact sur la lecture qualitative. L'unique changement notable est l'**anomalie options JSON récurrente** : max pain bascule à $28,0 (vs $100,0), put/call à 0,00, call OI à 100,0% — valeurs manifestement aberrantes. La valeur opérationnelle **$100,00** est conservée, cohérente avec l'historique et la structure du 15/06. L'écart EV/Revenue Yahoo 296,3× → 314,4× est un artefact mécanique (le ratio FMP annual 355,7× est stable et préféré). Le DRAFT_refresh déclenché par PRICE_GAP +6,26% et ATR_SPIKE 14,62% est un **faux positif** : ces signaux reflètent le close 15/06 déjà intégré dans l'analyse.

---

## Mise à Jour Technique

- **Cours :** $87,57 — identique au close 15/06. Aucun nouveau prix réel en pré-ouverture
- **RSI 14j :** **36,00** — proche de la zone de survente (<30), inchangé. La force relative interne reste stabilisée
- **ATR 14j :** $12,80 (ATR relatif **14,6%** du cours) — volatilité inchangée
- **MM50 :** $89,13 — cours **−1,8% sous** la moyenne, inchangé
- **MM200 :** N/A
- **Volume :** 23,92M vs moy. 20j 27,57M (**0,867×**) — léger retrait de −13,3% vs la moyenne, dans la norme d'une séance post-liquidation. La révision +0,35M vs le snapshot 21h n'altère pas la conclusion : rebond consolidé
- **52W high :** $133,86 — repli à **−34,6%**
- **52W low :** $36,08
- **Range intraday :** $83,985–$89,76 (données du 15/06)
- **Supports clés :** $83,99 (low 15/06) ; $82,41 (previous close) ; $80,00 (psychologique) ; $75,00 (support structurel)
- **Résistances clés :** $89,13 (MM50) ; $89,76 (high 15/06) ; $92,06 (close 10/06) ; $100,00 (psychologique + max pain opérationnel)
- **Timing verdict :** **Défavorable** — cours sous MM50, RSI proche survente, configuration fragile inchangée
- **Score Momentum :** 4,0/10 → **4,0/10** — inchangé (momentum faible, rebond consolidé mais non confirmé par un break technique)

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. Mutation **exclusivement technique/liquide**.

- **Market Cap :** $33,99B — stable
- **Forward P/E :** −426,75 (profil non rentable, inchangé)
- **EV/EBITDA :** −84,40
- **EV/Revenue :** **314,41× (Yahoo)** / **355,70× (FMP annual)** — écart Yahoo mécanique (+18× vs 15/06), FMP stable. Profil spéculatif extrême persistant
- **P/B :** 12,57× (Yahoo) / 10,10× (FMP annual) — stable
- **Beta :** 2,634 — sensibilité très supérieure au marché (inchangée)
- **Short Interest :** 18,39% (stable)
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes) — inchangé. Divergence **+7,97% upside**
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK**

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-16 émet un signal macro **NEUTRAL** avec régime UNKNOWN. XLC (Communication Services) reste dans le **bottom 3** (RS20d −3,35%). Faiblesse sectorielle persistante — mouvement d'ASTS **découplé** du secteur. Malus sectoriel maintenu (−0,5 pt).

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence consensus **+7,97% upside**
- **Options :**
  - **Anomalie JSON détectée et traitée :** max pain **$28,00** (aberrant, vs $100,00 au 15/06), put/call **0,00**, call OI **100,0%** — valeurs incohérentes
  - **Valeurs opérationnelles conservées :** max pain **$100,00**, put/call **0,44**, call OI **69,7%**
  - Nearest expiry : **2026-06-18** (J+2)
  - **Lecture :** le cours $87,57 reste **−12,4% sous le Max Pain opérationnel $100**. La structure options haussière (call OI dominant) reste théoriquement intacte. L'anomalie JSON du 16/06 est un **faux positif récurrent** (même pattern que les max pain $40/$45 des 02–03/06/2026)
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_2026-06-16.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_risk_latest.json` — pas de données récentes pertinentes)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-16. Le mouvement reste purement technique

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+55) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-06-18 (J+2)** — max pain opérationnel $100 au-dessus du spot (+14,2%) : pinning gamma haussier théorique

---

## Scoring Global — Pré-Ouverture 2026-06-16

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 5,5/10 | 35% | Aucun catalyseur imminent, earnings dans 55j. Structure options fiable et haussière (call OI 69,7%, put/call 0,44). Divergence consensus +7,97% |
| Valorisation | 4,5/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue FMP 355,7×). Consensus offre un upside mécanique +7,97% mais fondamentaux non rentables |
| Momentum | 4,0/10 | 25% | RSI 36,00 proche survente, cours −1,8% sous MM50. Volume 0,867× = rebond consolidé. Configuration fragile |
| **Score Opportunité** | **4,7/10** | | |

**Malus / Bonus appliqués (règles agents) :**
- Malus **COURS_SOUS_MM50** : cours −1,8% sous MM50 $89,13 — support dynamique non reconquis
- Malus **RSI_SURVENTE_APPROCHÉE** : RSI 36,00 proche survente — faiblesse interne persistante
- Bonus **VOLUME_CONSOLIDÉ** : volume 0,867× sur rebond +6,26% — participation normale, rebond légitimé
- Bonus **ANOMALIE_OPTIONS_RÉSOLUE** : valeurs opérationnelles max pain $100, put/call 0,44, call OI 69,7% — signal options fiable haussier
- Malus sectoriel (XLC bottom 3) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (`accounting_risk_latest.json` absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven
- **DRAFT_refresh classé faux positif** : les triggers PRICE_GAP et ATR_SPIKE reflètent le close 15/06 déjà intégré. Pas de mutation de données nouvelles

**Score Global Composite :** 47,2/100 → **39,2 ajusté** (−8,0 pts de malus additionnels). Seuil **SURVEILLER (35–49)**, en bas de fourchette.

> **Note :** le JSON `recommandations_2026-06-16.json` attribue à ASTS un score global ajusté de **39,2/100** avec action **SURVEILLER**, timing **Défavorable**, SL $61,97, TP $125,97, ratio R/R 1,5. Ces niveaux sont cohérents avec l'ATR $12,80 et le cours $87,57.

---

## Niveaux et Ratio R/R

- **Cours actuel :** $87,57
- **Stop-loss suggéré :** $61,97 (cours − 2×ATR = $87,57 − $25,60)
- **Take-profit suggéré :** $125,97 (cours + 3×ATR = $87,57 + $38,40)
- **Ratio R/R :** 1,5:1

**Révision :** SL et TP **inchangés** vs le snapshot 21h UTC 15/06. Aucun ajustement mécanique nécessaire (cours et ATR stables).
- Le SL à $61,97 correspond à la zone $60–$65 (support structurel historique)
- Le TP $125,97 correspond au **52W high ($133,86)** à −5,9% — probabilité d'atteinte faible sans catalyseur majeur
- Le consensus analystes ($94,54) est **+$6,97 au-dessus du cours** — upside consensus stable
- **Zone d'intérêt potentielle :** $82,50–$85,00 (test du previous close + support intermédiaire)
- **Résistance immédiate :** $89,13 (MM50) ; $89,76 (high 15/06) ; $92,06 (close 10/06)
- **Alerte options J+2 :** Max Pain opérationnel $100 au-dessus du spot (+14,2%). Pinning gamma haussier théorique
- **Alerte MM50 :** cours −1,8% sous MM50. Si break au-dessus de $89,13 sur volume >1,0× → confirmation haussière à court terme

---

## Conclusion

**Thèse confirmée sans modification : SURVEILLER — stabilité mécanique pré-ouverture à $87,57 sur volume consolidé 0,867×, RSI 36,00 stable proche survente, score global ajusté 39,2/100 (bas de zone SURVEILLER), anomalie options JSON récurrente traitée (max pain opérationnel $100 conservé).**

Le pré-ouverture du 16/06 ne présente **aucune mutation de données** vs le close 21h UTC 15/06. Le DRAFT_refresh déclenché automatiquement par `agents/detect_major_events` est classé **faux positif** : les triggers PRICE_GAP (+6,26%) et ATR_SPIKE (14,62%) sont des artefacts du close 15/06 déjà intégré dans l'analyse précédente. Aucun nouvel événement majeur n'est survenu entre le 15/06 21h UTC et le 16/06 10h UTC.

**Changements structurants depuis le snapshot 21h UTC 15/06 :**
1. **Stabilité totale des données brutes** : cours, RSI, ATR, MM50, consensus, short interest inchangés
2. **Volume légèrement révisé** : 23,57M → 23,92M (+1,5%) — correction du worker daemon, pas de changement qualitatif
3. **Anomalie options JSON récurrente** : max pain $28,0 aberrant, put/call 0,00, call OI 100% → traité comme faux positif. Valeurs opérationnelles $100 / 0,44 / 69,7% conservées
4. **EV/Revenue Yahoo mécanique** : 296,3× → 314,4× (+18×) — artefact de calcul Yahoo, préférer FMP 355,7× stable
5. **Score global ajusté inchangé** à 39,2/100 — bas de zone SURVEILLER
6. **Signal sectoriel inchangé** — NEUTRAL. XLC bottom 3 persistant
7. **Forward P/E stable** : −426,75

**Alertes actives :**
- **COURS_SOUS_MM50** : cours −1,8% sous MM50 $89,13 — résistance dynamique non conquise
- **RSI_SURVENTE_APPROCHÉE** : RSI 36,00 proche survente — faiblesse interne persistante
- **VOLUME_CONSOLIDÉ** : volume 0,867× = rebond consolidé et légitimé (alerte positive)
- **ATR_SPIKE (haut)** : ATR relatif 14,6% du cours ($12,80)
- **Profil non rentable** — EPS estimé négatif, multiples extrêmes (P/B 12,57× Yahoo / 10,10× FMP, EV/Revenue FMP 355,7×), aucune visibilité sur la rentabilité
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (RS20d −3,35%)
- **Options J+2** — Max Pain opérationnel $100 au-dessus du spot (+14,2%). Pinning gamma haussier théorique
- **Short Interest élevé** — 18,39%, pas de squeeze setup mais pression vendeuse présente
- **DRAFT_refresh Faux Positif** — les triggers PRICE_GAP et ATR_SPIKE reflètent le close 15/06, pas un nouvel événement

**Verdict opérationnel :** la configuration reste **techniquement fragile** avec le rebond consolidé à $87,57. Sans break au-dessus de la MM50 ($89,13) et sans catalyseur fondamental, la configuration reste en zone SURVEILLER. L'absence de nouvelles données au 16/06 matin ne modifie pas la thèse.

**Prochaines étapes :**
- Surveiller **impérativement** la tenue du niveau $85,00 en ouverture du 16/06
- Si break au-dessus de MM50 $89,13 sur volume >1,0× → réviser vers **ATTENDRE** avec objectif $92–$97
- Si repli sous $82,41 (previous close) sur volume maintenu (>0,8×) → réviser vers **ÉVITER** avec objectif $75–$80
- Si rebond au-dessus de $89,13 sur volume en retrait (<0,8×) → **ne pas suivre**, absence de conviction
- Monitoring comportement options J+2 (expiration 2026-06-18) autour du max pain opérationnel $100
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (breakout confirmé au-dessus de $100 sur volume >1,0×) avant toute entrée
- **Ne pas entrer long sans confirmation au-dessus de $92 sur volume >0,8×**

---

*Généré par le système Argus-IA — Pré-ouverture 2026-06-16 (cours $87,57, RSI 36,00, volume 0,867×, score global 39,2 SURVEILLER, divergence consensus +7,97%, cours −1,8% sous MM50 $89,13, anomalie options JSON traitée, DRAFT_refresh classé faux positif)*
