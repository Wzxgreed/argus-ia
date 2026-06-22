# ASTS — Mise à Jour 2026-06-22 (Snapshot 13h UTC — Options Résolues)

> **Close $80,66** : gap down **−5,58%** vs previous close $85,43, test du pivot **$80,00** (low $77,12), RSI **32,75** en survente atténuée (+4,24 pt vs 28,51 du 17/06), volume en expansion **1,117×** (31,68M vs moy. 20j 28,35M). **Anomalie options JSON RÉSOLUE** : max pain **$100,00**, put/call **0,70**, call OI **58,9%** (vs valeurs corrompues du snapshot matinal). Score global ajusté **39,2/100 (SURVEILLER)** vs 43,0 précédent. Score Momentum dégradé à **2,5/10**. Thèse **SURVEILLER aggravée** — le pivot $80 a été testé et violé intraday. La configuration est désormais plus fragile.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-17)

| Indicateur | Snapshot 13h UTC 17/06 | Close 2026-06-22 | Delta |
|-----------|------------------------|------------------|-------|
| **Cours** | **$82,25** | **$80,66** | **−$1,59 (−1,93%)** 🔴 |
| Change % session | — | **−5,58%** (vs prev. $85,43) | **Gap down significatif** 🔴 |
| RSI 14j | **28,51** | **32,75** | **+4,24 pt** 🟡 |
| ATR 14j | **$12,40** | **$10,66** | **−$1,74 (−14,0%)** 🟢 |
| MM50 | **$88,88** | **$88,42** | **−$0,46** 🟢 |
| Cours vs MM50 | **−7,5%** | **−8,8%** | **−1,3 pt** 🔴 |
| **Volume rel.** | **0,733×** (20,04M) | **1,117×** (31,68M) | **+0,384× (+52,4%)** 🔴 |
| Volume absolu | 20,04M | **31,68M** | **+11,64M (+58,1%)** 🔴 |
| Market Cap (Yahoo) | $31,92B | **$31,31B** | **−$0,61B (−1,9%)** 🔴 |
| Forward P/E | −400,83 | **−393,08** | **+7,75** 🟡 |
| EV/Revenue (Yahoo) | 295,70× | **290,11×** | **−5,59×** 🟢 |
| P/B (Yahoo) | 11,81× | **11,58×** | **−0,23×** 🟢 |
| Consensus PT | $94,54 | **$94,54** | **—** 🟢 |
| Divergence consensus | +14,9% | **+17,2%** | **+2,3 pt** 🟡 |
| Short Interest | 18,39% | **18,39%** | **—** 🟢 |
| **Options Max Pain** | **$100,00** (résolu 17/06) | **$100,00** (résolu 22/06) | **—** 🟢 |
| **Options Put/Call** | **0,46** | **0,70** | **+0,24 pt** 🔴 |
| **Options Call OI %** | **68,3%** | **58,9%** | **−9,4 pt** 🔴 |
| **Score Global ajusté (JSON)** | **43,0 (SURVEILLER)** | **39,2 (SURVEILLER)** | **−3,8 pts** 🔴 |
| **Score Opportunité** | **4,6/10** | **4,7/10** | **+0,1 pt** 🟡 |
| **Score Momentum** | **3,5/10** | **2,5/10** | **−1,0 pt** 🔴 |
| **Score Catalyseur** | **5,5/10** | **6,0/10** | **+0,5 pt** 🟡 |
| **Score Valorisation** | **4,5/10** | **5,0/10** | **+0,5 pt** 🟡 |

**Verdict :** la session du 2026-06-22 apporte une **mutation technique significative** : gap down −5,58% à l'ouverture ($85,30 → open, $77,12 low), volume en expansion 1,117×, et test du pivot clé **$80,00** avec violation intraday ($77,12). Le close à $80,66 (+4,6% du low) est un **rejet partiel** de la cassure, mais la configuration est désormais plus fragile. Le score global ajusté recule de 43,0 à 39,2 (SURVEILLER, bas de fourchette). Le score Momentum s'est dégradé de 3,5 à 2,5/10, confirmant la faiblesse structurelle. RSI en survente atténuée (32,75 vs 28,51) — léger répit mais pas de signal de retournement.

**Signal important :** l'anomalie options JSON est **résolue** dans le snapshot 13h UTC 2026-06-22. Les valeurs opérationnelles sont désormais directement issues du JSON : max pain $100,00, put/call 0,70, call OI 58,9%. Le put/call ratio a grimpé de 0,46 à 0,70 (+52%) et le call OI a reculé de 68,3% à 58,9% (−9,4 pt), signalant un **virage plus bearish du positionnement options** par rapport au 17/06. Cette évolution cohère avec le gap down et le test du pivot $80.

---

## Anomalies de Données — Résolution Options

1. **Options JSON RÉSOLUES** : le snapshot 13h UTC 2026-06-22 restaure des données options cohérentes pour ASTS :
   - Max Pain : **$100,00** (coherent avec l'historique récent)
   - Put/Call Ratio : **0,70** (vs `null` corrompu au snapshot matinal)
   - Call OI % : **58,9%** (vs `null` corrompu au snapshot matinal)
   - Nearest expiry : **2026-06-26** (J+4)
   
   **Lecture :** le positionnement options s'est dégradé par rapport au 17/06. Le put/call 0,70 est supérieur au 0,46 précédent (plus de puts relativement aux calls), et le call OI 58,9% est inférieur au 68,3% précédent. Cela traduit une **couverture baissière accrue** par les opérateurs options, cohérente avec le gap down −5,58% et le test du pivot $80.

2. Aucune autre anomalie de données détectée dans `data/latest.json` pour ASTS.

---

## Mise à Jour Technique

- **Cours :** $80,66 — **−5,58%** vs previous close $85,43. Open $85,30, high $85,70, low **$77,12** (**amplitude intraday 11,1%**)
- **RSI 14j :** **32,75** — survente atténuée (+4,24 pt vs 28,51 du 17/06). Sortie mécanique de la zone <30 due à la réduction de l'ATR et au rebond du low, mais reste faible
- **ATR 14j :** $10,66 (ATR relatif **13,2%** du cours) — **en retrait** vs $12,40 (15,1%) du 17/06. Volatilité élevée mais en décroissance
- **MM50 :** $88,42 — cours **−8,8% sous** la moyenne (vs −7,5% au 17/06). Écart mécaniquement creusé par la baisse du cours
- **MM200 :** N/A
- **Volume :** 31,68M vs moy. 20j 28,35M (**1,117×**) — **expansion volumétrique significative** (+52,4% relatif vs le 17/06). C'est le premier volume >1× depuis le 15/06 (2,00×). La liquidité est de retour, mais à la baisse
- **52W high :** $133,86 — repli à **−39,7%** (vs −38,6% au 17/06)
- **52W low :** $36,08
- **Range intraday :** $77,12–$85,70 (**amplitude 11,1%**) — séance volatile avec test du pivot $80
- **Supports clés :** $80,00 (psychologique, **pivot clé**, close juste au-dessus) ; $77,12 (low du 22/06, **support immédiat**) ; $75,00 (support structurel majeur) ; $70,00 (zone de congestion avril 2026)
- **Résistances clés :** $85,43 (previous close) ; $85,70 (high du 22/06) ; $88,42 (MM50) ; $92,06 (close 09/06) ; $100,00 (psychologique + max pain)
- **Timing verdict :** **Défavorable** — cours sous MM50 avec écart accru (−8,8%), gap down sur volume expansion, test et rejet partiel du pivot $80. Aucun signal de retournement haussier
- **Score Momentum :** 2,5/10 — **dégradation** (JSON recommandations). Momentum baissier renforcé

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. Mutation **exclusivement technique** (gap down + test pivot).

- **Market Cap :** $31,31B (Yahoo) / $25,32B (FMP) — divergence significative entre sources. La valorisation Yahoo fait foi pour le cours actuel
- **Forward P/E :** −393,08 (profil non rentable, légère amélioration mécanique vs −400,83)
- **EV/EBITDA :** −77,88
- **EV/Revenue :** **290,11× (Yahoo)** / **355,70× (FMP annual)** — mécaniquement réduit par la baisse du cours (Yahoo), inchangé FMP
- **P/B :** 11,58× (Yahoo) / 10,10× (FMP annual) — mécaniquement réduit
- **Beta :** 2,634 — sensibilité très supérieure au marché (inchangée)
- **Short Interest :** 18,39% (stable, pression vendeuse présente mais pas de squeeze setup)
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes, 2 couverts le mois dernier, 7 le trimestre dernier) — inchangé. Divergence **+17,2% upside** (mécanique, due à la baisse du cours)
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK**

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-22 émet un signal macro **NEUTRAL** avec régime UNKNOWN. **XLC (Communication Services)** reste dans le **bottom 3** avec momentum_score **0,0**. XLK (Technology) est **top 1** (momentum_score 10,0). ASTS, en tant que Communication Equipment, est à la croisée des deux secteurs mais le signal XLC domine. Malus sectoriel maintenu (−0,5 pt).

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence consensus **+17,2% upside** (mécanique)
- **Options (JSON résolu 13h UTC) :**
  - **Max Pain :** **$100,00** — cohérent avec l'historique récent. Cours $80,66 reste **−19,3% sous le Max Pain**
  - **Put/Call Ratio :** **0,70** — **dégradation vs 0,46 du 17/06** (+52% relatif). Plus de puts relativement aux calls, signalant une couverture baissière accrue
  - **Call OI % :** **58,9%** — **recul vs 68,3% du 17/06** (−9,4 pt). Le skew call se réduit, cohérent avec la pression vendeuse du jour
  - Nearest expiry : **2026-06-26** (J+4)
  - **Lecture :** le positionnement options s'est viré plus défensif/baissier par rapport au 17/06. Le décrochage du cours sous $85 renforce l'écart au max pain. Les calls OTM $85+ subiront une dépréciation rapide si le cours reste sous $85 à l'expiration. Le pinning vers $100 est hautement improbable à court terme
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_2026-06-22.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_risk_latest.json` — pas de données récentes pertinentes)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-22 (`news_2026-06-22.json` vide). Le mouvement reste purement technique

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+49) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-06-26 (J+4)** — max pain $100 au-dessus du spot (+23,9%). La probabilité de pinning gamma s'éloigne avec le cours sous $85. Le put/call 0,70 et le call OI 58,9% reflètent un positionnement plus défensif que la semaine dernière

---

## Scoring Global — Close 2026-06-22 (Snapshot 13h UTC, Options Résolues)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 6,0/10 | 35% | Aucun catalyseur imminent, earnings dans 49j. Structure options historiquement haussière (call OI 58,9%) mais en dégradation vs 68,3% du 17/06. Put/call 0,70 = couverture baissière accrue |
| Valorisation | 5,0/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue FMP 355,7×). Consensus offre un upside mécanique +17,2% mais fondamentaux non rentables |
| Momentum | 2,5/10 | 25% | RSI 32,75 en survente atténuée, cours −8,8% sous MM50, volume expansion 1,117× à la baisse. Configuration baissière renforcée |
| **Score Opportunité** | **4,7/10** | | |

**Malus / Bonus appliqués (règles agents) :**
- Malus **COURS_SOUS_MM50** : cours −8,8% sous MM50 $88,42 — résistance dynamique non reconquise, écart mécaniquement creusé
- Malus **RSI_SURVENTE** : RSI 32,75 < 35 — survente technique atténuée mais faiblesse interne persistante
- Malus **VOLUME_BAISSE** : volume 1,117× en expansion à la baisse — liquidité de retour mais direction négative
- Malus **GAP_DOWN** : gap −5,58% overnight — ouverture sous le previous close, pression vendeuse agressive
- Malus **PIVOT_TEST** : low $77,12 < pivot $80,00 — cassure intraday du niveau clé, rejet partiel au close
- Malus **OPTIONS_BEARISH_SHIFT** : put/call 0,70 (+52% vs 0,46 du 17/06), call OI 58,9% (−9,4 pt vs 68,3%) — positionnement options viré plus défensif/baissier
- Malus sectoriel (XLC bottom 3, momentum 0,0) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (`accounting_risk_latest.json` absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite (JSON) :** 47,2/100 → **39,2 ajusté** (−8,0 pts de malus). Seuil **SURVEILLER (35–49)**, proche du bas de fourchette.

> **Note :** le JSON `recommandations_2026-06-22.json` attribue à ASTS un score global ajusté de **39,2/100** avec action **SURVEILLER**, timing **Défavorable**, SL $59,34, TP $112,64, ratio R/R 1,5. Ces niveaux sont cohérents avec l'ATR $10,66 et le cours $80,66.

---

## Niveaux et Ratio R/R

- **Cours actuel :** $80,66
- **Stop-loss suggéré :** $59,34 (cours − 2×ATR = $80,66 − $21,32)
- **Take-profit suggéré :** $112,64 (cours + 3×ATR = $80,66 + $31,98)
- **Ratio R/R :** 1,5:1

**Révision :** SL et TP **révisés à la baisse** vs le close 17/06 (SL $57,45 / TP $119,45) en raison de la baisse du cours et de l'ATR.
- Le SL à $59,34 correspond à la zone $55–$60 (support structurel historique majeur). Distance SL = 26,4% du cours
- Le TP $112,64 correspond au **52W high ($133,86)** à −15,8% — probabilité d'atteinte très faible sans catalyseur majeur
- Le consensus analystes ($94,54) est **+$13,88 au-dessus du cours** — upside consensus mécanique +17,2%
- **Zone d'intérêt potentielle :** $77–$80 (test du low du 22/06 + support psychologique $80)
- **Résistance immédiate :** $85,43 (previous close) ; $85,70 (high 22/06) ; $88,42 (MM50)
- **Alerte options J+4 :** Max Pain $100 au-dessus du spot (+23,9%). Put/call 0,70 et call OI 58,9% = positionnement plus défensif. Pinning gamma théoriquement possible mais très improbable sous $85
- **Alerte volume :** 1,117× = liquidité de retour mais à la baisse. Tout rebond sera contesté si le volume reste directionnellement vendeur

---

## Conclusion

**Thèse SURVEILLER aggravée : le pivot $80,00 a été testé et violé intraday ($77,12). Le close à $80,66 est un rejet partiel mais la configuration est désormais plus fragile. Score global ajusté 39,2/100 (SURVEILLER, bas de fourchette).**

La session du 2026-06-22 apporte une **mutation technique significative** par rapport au snapshot du 17/06 :

1. **Gap down −5,58%** : $85,43 → $80,66. Ouverture agressive sous le previous close, pression vendeuse structurée
2. **Test et violation du pivot $80** : low $77,12 < $80,00. Cassure intraday du niveau clé identifié depuis le 16/06
3. **Rejet partiel au close** : $80,66 (+4,6% du low) — les acheteurs ont défendu $80 en fin de séance, mais le close est juste au-dessus du pivot
4. **RSI en survente atténuée** : 28,51 → 32,75 — léger répit mécanique, pas de signal de retournement
5. **Volume en expansion à la baisse** : 0,733× → 1,117× (+52,4%) — liquidité de retour mais direction négative
6. **Score global ajusté dégradé** : 43,0 → 39,2 (−3,8 pts) — proche du seuil inférieur de la fourchette SURVEILLER
7. **Score Momentum dégradé** : 3,5 → 2,5/10 — momentum baissier renforcé
8. **Divergence consensus mécanique** : +14,9% → +17,2% (uniquement due à la baisse du cours)
9. **Options JSON résolues** : max pain $100,00, put/call 0,70, call OI 58,9% — mais le positionnement s'est viré plus bearish vs le 17/06 (put/call +52%, call OI −9,4 pt)
10. **MM50 s'éloigne** : cours désormais −8,8% sous MM50 $88,42 (vs −7,5%)

**Alertes actives :**
- **GAP_DOWN** : gap −5,58% overnight — ouverture agressive sous le previous close
- **PIVOT_TEST** : low $77,12 < pivot $80,00 — cassure intraday du niveau clé, rejet partiel au close
- **COURS_SOUS_MM50 aggravé** : cours −8,8% sous MM50 $88,42 — résistance dynamique très lointaine
- **RSI_SURVENTE atténuée** : RSI 32,75 < 35 — survente technique atténuée mais faiblesse persistante
- **VOLUME_BAISSE** : 1,117× en expansion à la baisse — liquidité de retour mais direction négative
- **ATR_SPIKE (haut)** : ATR relatif 13,2% du cours ($10,66)
- **Profil non rentable** — EPS estimé négatif, multiples extrêmes (P/B 11,58× Yahoo / 10,10× FMP, EV/Revenue FMP 355,7×)
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (momentum_score 0,0)
- **Options J+4** — Max Pain $100 à +23,9%, put/call 0,70 = couverture baissière accrue, pinning gamma improbable sous $85
- **Short Interest élevé** — 18,39%, pas de squeeze setup mais pression vendeuse présente
- **OPTIONS_BEARISH_SHIFT** — put/call 0,70 (+52% vs 17/06), call OI 58,9% (−9,4 pt) = positionnement options plus défensif

**Verdict opérationnel :** la configuration s'est **aggravée** vs le 17/06. Le pivot $80 a été testé et violé intraday. Le rejet au close ($80,66) est un signal mitigé : soit les acheteurs défendent $80, soit c'est un "dead cat bounce" avant une cassure confirmée. Le volume en expansion à la baisse (1,117×) est le signal le plus inquiétant — il indique une participation vendeuse structurée. L'évolution du positionnement options (put/call 0,70, call OI 58,9%) confirme que les opérateurs se couvrent à la baisse, ce qui renforce la fragilité technique.

**Scénarios à court terme :**
- **Optimiste (15%)** : défense de $80 confirmée, rebond technique vers $85–$88 sur volume >1,0× dans les 2–3 prochains jours
- **Central (50%)** : consolidation dans le range $77–$83 avec volume modéré, attente d'un catalyseur
- **Pessimiste (35%)** : cassure confirmée de $80 au close, accélération baissière vers $72–$75

**Prochaines étapes :**
- Surveiller **impérativement** la tenue du niveau **$80,00** au close des prochaines sessions
- Si close > $80 sur 2 sessions consécutives avec volume <1,0× → consolidation probable, maintenir SURVEILLER
- Si close < $80 sur volume >0,8× → réviser vers **ÉVITER** avec objectif $72–$75
- Si rebond au-dessus de $85 sur volume >1,0× → réviser vers ATTENDRE avec objectif $88–$92
- Si rebond au-dessus de $85 sur volume <0,8× → **ne pas suivre**, absence de conviction
- Monitoring comportement options J+4 (expiration 2026-06-26) — les calls $85+ sont menacés ; le put/call 0,70 indique une couverture baissière structurée
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (breakout confirmé au-dessus de $92 sur volume >0,8×) avant toute entrée
- **Ne pas entrer long sans confirmation au-dessus de $88 sur volume >0,6×**
- Le niveau $80 reste le **pivot absolu** : close au-dessus = consolidation possible ; close sous = risque d'accélération baissière majeure

---

*Généré par le système Argus-IA — Close 2026-06-22, snapshot 13h UTC (cours $80,66, RSI 32,75, volume 1,117×, score global 39,2 SURVEILLER, divergence consensus +17,2%, cours −8,8% sous MM50 $88,42, gap down −5,58%, low $77,12 < pivot $80, options résolues : max pain $100,00, put/call 0,70, call OI 58,9%)*
