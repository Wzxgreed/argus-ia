# ASTS — Mise à Jour Snapshot 10h UTC (2026-06-17)

> **Snapshot $82,25** : stabilité mécanique à la marge vs close 17h UTC 16/06 ($83,09). Cours **−1,01%** sous le close officiel, RSI **28,51** inchangé en survente, **volume recovery partiel** à **0,733×** (+73,7% vs le collapse 0,422× du 16/06). **Anomalies de données détectées** : `previous_close` JSON à $87,57 (close 13h 16/06, non 17h) ; open/high/low quasi identiques au 16/06 ; options JSON corrompues (max pain $18,00 aberrant, put/call et call OI `null`). Score global ajusté **43,0/100 (SURVEILLER)** inchangé. Thèse **SURVEILLER confirmée sans changement majeur** — le snapshot matinal (marché US fermé à 10h UTC) ne fournit pas de nouvelle information de cotation. Le pivot clé reste **$80,00**.

---

## Résumé des Changements depuis le Close 17h UTC 16/06

| Indicateur | Close 17h UTC 16/06 | Snapshot 10h UTC 17/06 | Delta |
|-----------|---------------------|------------------------|-------|
| **Cours** | **$83,09** | **$82,25** | **−$0,84 (−1,01%)** 🔴 |
| RSI 14j | **28,73** | **28,51** | **−0,22 pt** 🟢 |
| ATR 14j | **$12,40** | **$12,40** | **—** 🟢 |
| MM50 | **$88,90** | **$88,88** | **−$0,02** 🟢 |
| Cours vs MM50 | **−6,5%** | **−7,5%** | **−1,0 pt** 🔴 |
| **Volume rel.** | **0,422×** (11,35M) | **0,733×** (20,04M) | **+0,311× (+73,7%)** 🟡 |
| Volume absolu | 11,35M | **20,04M** | **+8,69M (+76,6%)** 🟡 |
| Market Cap | $32,25B | **$31,92B** | **−$0,33B (−1,0%)** 🔴 |
| Forward P/E | −404,92 | **−400,83** | **+4,09** 🟡 |
| EV/Revenue (Yahoo) | 314,41× | **295,70×** | **−18,71×** 🟡 |
| P/B (Yahoo) | 11,93× | **11,81×** | **−0,12×** 🟢 |
| Consensus PT | $94,54 | **$94,54** | **—** 🟢 |
| Divergence consensus | +13,8% | **+14,9%** | **+1,1 pt** 🟡 |
| Short Interest | 18,39% | **18,39%** | **—** 🟢 |
| **Score Global ajusté (JSON)** | **43,0 (SURVEILLER)** | **43,0 (SURVEILLER)** | **—** 🟢 |
| **Score Opportunité** | **4,6/10** | **4,6/10** | **—** 🟢 |
| **Score Momentum** | **3,5/10** | **3,5/10** | **—** 🟢 |

**Verdict :** le snapshot 10h UTC 17/06 n'apporte **pas de mutation significative** par rapport au close 17h UTC 16/06. Le cours recule marginalement de −1,01% sur un volume en recovery partiel (0,733×), ce qui contraste avec le volume collapse du 16/06. Cependant, ce snapshot est collecté avant l'ouverture du marché US (10h UTC = 6h EST) et présente des **anomalies de données** : le `previous_close` JSON ($87,57) ne correspond pas au close officiel du 16/06 ($83,09) mais au snapshot 13h UTC 16/06. Les valeurs open/high/low sont quasi identiques au 16/06, ce qui confirme que le snapshot matinal reflète des données pré-marché ou un carry-over. Le score global JSON reste inchangé à 43,0 (SURVEILLER). La divergence consensus se creuse mécaniquement à +14,9% (consensus inchangé, cours plus bas).

---

## Anomalies de Données Détectées

1. **`previous_close` erroné** : le JSON `latest.json` indique `previous_close: 87,57` pour ASTS. Or le close officiel 17h UTC 16/06 était **$83,09**. La valeur $87,57 correspond au snapshot 13h UTC 16/06. Le `change_pct` affiché (−6,08%) est donc calculé sur une base incorrecte. **Variation réelle vs close 17h : −1,01%**.
2. **Open/High/Low identiques** : open $85,70 / high $89,60 / low $82,11 sont quasi identiques au 16/06 (open $85,775 / high $89,60 / low $82,11). Le marché US étant fermé à 10h UTC, ces valeurs sont probablement des résidus de session précédente.
3. **Options JSON corrompues** : `max_pain: 18,0` (aberrant, valeur opérationnelle historique = $100,00), `put_call_ratio: null`, `call_oi_pct: null`. Anomalie récurrente de l'API options sur ASTS. **Valeurs opérationnelles conservées** : max pain $100,00, put/call 0,45, call OI 69,0% (dernières valeurs fiables du 16/06).

---

## Mise à Jour Technique

- **Cours :** $82,25 — **−1,01%** vs close 17h 16/06. Open $85,70, high $89,60, low $82,11 (données pré-marché, voir anomalie § ci-dessus)
- **RSI 14j :** **28,51** — **stable en survente** (<30). Écart de −0,22 pt vs 28,73 (16/06). Signal de survente intact
- **ATR 14j :** $12,40 (ATR relatif **15,1%** du cours) — inchangé, volatilité élevée persistante
- **MM50 :** $88,88 — cours **−7,5% sous** la moyenne (vs −6,5% au 16/06). Écart mécaniquement creusé par la baisse du cours
- **MM200 :** N/A
- **Volume :** 20,04M vs moy. 20j 27,33M (**0,733×**) — **recovery partiel** vs le collapse 0,422× du 16/06. C'est le premier signe de retour de liquidité depuis le 15/06 (0,855×). Toutefois, ce volume est enregistré avant l'ouverture US et peut inclure des transactions pre-market / after-hours consolidées
- **52W high :** $133,86 — repli à **−38,6%** (vs −37,9% au 16/06)
- **52W low :** $36,08
- **Range intraday (session précédente) :** $82,11–$89,60 (**amplitude 9,1%**) — séance du 16/06
- **Supports clés :** $82,11 (low du 16/06) ; $80,00 (psychologique, **pivot clé**) ; $75,00 (support structurel majeur) ; $70,00 (zone de congestion avril 2026)
- **Résistances clés :** $85,00 (previous close 13h 16/06) ; $88,88 (MM50) ; $89,60 (high 16/06) ; $92,06 (close 10/06) ; $100,00 (psychologique + max pain opérationnel)
- **Timing verdict :** **Défavorable** — cours sous MM50 avec écart accru (−7,5%), RSI en survente. Aucun signal de retournement
- **Score Momentum :** 3,5/10 — **inchangé** (JSON recommandations). Momentum baissier confirmé

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. Mutation **exclusivement technique/liquide**.

- **Market Cap :** $31,92B — **−$0,33B** vs close 16/06
- **Forward P/E :** −400,83 (profil non rentable, légère amélioration mécanique vs −404,92)
- **EV/EBITDA :** −79,38
- **EV/Revenue :** **295,70× (Yahoo)** / **355,70× (FMP annual)** — mécaniquement réduit par la baisse du cours (Yahoo), inchangé FMP
- **P/B :** 11,81× (Yahoo) / 10,10× (FMP annual) — mécaniquement réduit
- **Beta :** 2,634 — sensibilité très supérieure au marché (inchangée)
- **Short Interest :** 18,39% (stable, pression vendeuse présente mais pas de squeeze setup)
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes, 2 couverts le mois dernier, 7 le trimestre dernier) — inchangé. Divergence **+14,9% upside** (mécanique, due à la baisse du cours uniquement)
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK**

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-17 émet un signal macro **NEUTRAL** avec régime UNKNOWN. **XLC (Communication Services)** reste dans le **bottom 3** avec return_20d **−3,98%** et momentum_score **0,0** (vs return_20d −4,62% au 16/06 — légère amélioration mais toujours faible). XLK (Technology) est cependant **top 1** (momentum_score 10,0). ASTS, en tant que Communication Equipment, est à la croisée des deux secteurs mais le signal XLC domine. Malus sectoriel maintenu (−0,5 pt).

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence consensus **+14,9% upside** (mécanique)
- **Options :**
  - **Max Pain :** **$18,00** (JSON) — **anomalie aberrante récurrente**. Valeur opérationnelle conservée : **$100,00** (dernière donnée fiable 16/06). Cours $82,25 reste **−17,8% sous le Max Pain opérationnel**
  - **Put/Call Ratio :** **`null`** (JSON corrompu). Valeur opérationnelle conservée : **0,45**
  - **Call OI % :** **`null`** (JSON corrompu). Valeur opérationnelle conservée : **69,0%**
  - Nearest expiry : **2026-06-18** (J+1)
  - **Lecture :** le décrochage du cours sous $85 renforce l'écart au max pain. Les calls OTM $85+ subiront une dépréciation rapide si le cours reste sous $85 à l'expiration demain. Le pinning vers $100 est hautement improbable à court terme
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_2026-06-17.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_risk_latest.json` — pas de données récentes pertinentes)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-17. Le mouvement reste purement technique

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+54) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-06-18 (J+1)** — max pain opérationnel $100 au-dessus du spot (+21,6%). La probabilité de pinning gamma s'éloigne avec le cours sous $85

---

## Scoring Global — Snapshot 10h UTC (2026-06-17)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 5,5/10 | 35% | Aucun catalyseur imminent, earnings dans 54j. Structure options historiquement haussière (call OI 69,0%, put/call 0,45) mais données corrompues aujourd'hui |
| Valorisation | 4,5/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue FMP 355,7×). Consensus offre un upside mécanique +14,9% mais fondamentaux non rentables |
| Momentum | 3,5/10 | 25% | RSI 28,51 en survente, cours −7,5% sous MM50, volume recovery partiel 0,733×. Configuration baissière confirmée |
| **Score Opportunité** | **4,6/10** | | |

**Malus / Bonus appliqués (règles agents) :**
- Malus **COURS_SOUS_MM50** : cours −7,5% sous MM50 $88,88 — résistance dynamique non reconquise, écart mécaniquement creusé
- Malus **RSI_SURVENTE** : RSI 28,51 < 30 — survente technique confirmée, faiblesse interne
- Malus **VOLUME_FAIBLE** : volume 0,733× — en recovery mais toujours sous la moyenne 20j
- Bonus **ANOMALIE_OPTIONS_STABLE** (historique) : max pain $100 cohérent, put/call 0,45, call OI 69,0% — signal options fiable mais de moins en moins pertinent avec le cours sous $85
- Malus sectoriel (XLC bottom 3, momentum 0,0) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (`accounting_risk_latest.json` absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite (JSON) :** 46,0/100 → **43,0 ajusté** (−3,0 pts de malus). Seuil **SURVEILLER (35–49)**, au milieu de la fourchette.

> **Note :** le JSON `recommandations_2026-06-17.json` attribue à ASTS un score global ajusté de **43,0/100** avec action **SURVEILLER**, timing **Défavorable**, SL $57,45, TP $119,45, ratio R/R 1,5. Ces niveaux sont cohérents avec l'ATR $12,40 et le cours $82,25.

---

## Niveaux et Ratio R/R

- **Cours actuel :** $82,25
- **Stop-loss suggéré :** $57,45 (cours − 2×ATR = $82,25 − $24,80)
- **Take-profit suggéré :** $119,45 (cours + 3×ATR = $82,25 + $37,20)
- **Ratio R/R :** 1,5:1

**Révision :** SL et TP **révisés à la baisse** vs le close 17h UTC 16/06 (SL $58,29 / TP $120,29) en raison de la baisse du cours.
- Le SL à $57,45 correspond à la zone $55–$60 (support structurel historique majeur). Distance SL = 30,1% du cours
- Le TP $119,45 correspond au **52W high ($133,86)** à −10,8% — probabilité d'atteinte très faible sans catalyseur majeur
- Le consensus analystes ($94,54) est **+$12,29 au-dessus du cours** — upside consensus mécanique
- **Zone d'intérêt potentielle :** $80,00–$82,50 (test du low du 16/06 + support psychologique $80)
- **Résistance immédiate :** $85,00 (previous close 13h 16/06) ; $88,88 (MM50) ; $89,60 (high 16/06)
- **Alerte options J+1 :** Max Pain opérationnel $100 au-dessus du spot (+21,6%). Pinning gamma théoriquement possible mais très improbable sous $85
- **Alerte volume :** 0,733× = liquidité en recovery mais pas encore normale. Tout ordre de taille peut provoquer un gap significatif

---

## Conclusion

**Thèse confirmée sans changement majeur : SURVEILLER — snapshot matinal $82,25 sur données pré-marché, RSI stable en survente 28,51, score global ajusté 43,0/100 (SURVEILLER), anomalies de données détectées (previous_close erroné, options JSON corrompues).**

Le snapshot 10h UTC 17/06 n'apporte **pas de nouvelle information de marché** : le marché US est fermé à cette heure (ouverture 13h30 UTC). Les données techniques (open/high/low identiques au 16/06) et le `previous_close` erroné ($87,57 au lieu de $83,09) indiquent que le snapshot est un carry-over de la session précédente avec une légère révision du close à $82,25. Le volume en recovery partiel (0,733×) est le seul signal potentiellement significatif, mais il inclut probablement des transactions after-hours et pre-market consolidées.

**Changements observés depuis le close 17h UTC 16/06 :**
1. **Cours −1,01%** : $83,09 → $82,25. Baisse marginale, pas de mutation
2. **RSI stable** : 28,73 → 28,51 — survente intacte, pas de rebond
3. **Volume recovery partiel** : 0,422× → 0,733× (+73,7%). Liquidité en retour mais toujours sous moyenne
4. **MM50 s'éloigne mécaniquement** : cours désormais −7,5% sous MM50 (vs −6,5%)
5. **Score global inchangé** : 43,0 SURVEILLER
6. **Scores agents inchangés** : Opportunité 4,6, Catalyseur 5,5, Valorisation 4,5, Momentum 3,5
7. **Divergence consensus mécanique** : +13,8% → +14,9% (uniquement due à la baisse du cours)
8. **Anomalies options** : max pain JSON $18,00 aberrant, put/call et call OI `null` — valeurs opérationnelles conservées
9. **Anomalie previous_close** : $87,57 dans le JSON = close 13h 16/06, pas 17h. Le `change_pct` officiel (−6,08%) est faux

**Alertes actives :**
- **COURS_SOUS_MM50** : cours −7,5% sous MM50 $88,88 — résistance dynamique très lointaine
- **RSI_SURVENTE** : RSI 28,51 < 30 — survente technique
- **VOLUME_RECOVERY** : 0,733× — liquidité en retour mais pas encore normale
- **ATR_SPIKE (haut)** : ATR relatif 15,1% du cours ($12,40)
- **Profil non rentable** — EPS estimé négatif, multiples extrêmes (P/B 11,81× Yahoo / 10,10× FMP, EV/Revenue FMP 355,7×)
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (return_20d −3,98%, momentum 0,0)
- **Options J+1** — Max Pain opérationnel $100 à +21,6%, pinning gamma improbable sous $85
- **Short Interest élevé** — 18,39%, pas de squeeze setup mais pression vendeuse présente
- **Anomalies données** — previous_close erroné, options JSON corrompues

**Verdict opérationnel :** la configuration est **stable vs le close 16/06**. Le marché n'ayant pas encore ouvert au moment du snapshot, aucune conclusion nouvelle ne peut être tirée. Le niveau clé à surveiller à l'ouverture US du 17/06 est le **pivot $80,00** : une cassure sous ce niveau sur volume >0,5× confirmerait la poursuite de la baisse vers $75–$78. Un rebond au-dessus de $85 sur volume >0,8× ouvrirait la porte à une consolidation $85–$92. Le RSI en survente laisse la possibilité d'un rebond technique, mais le contexte sectoriel faible (XLC bottom 3) et l'absence de catalyseur fondamental limitent l'amplitude d'un tel rebond.

**Scénarios à court terme (post-ouverture US 17/06) :**
- **Optimiste (20%)** : rebond technique depuis la survente (RSI 28,51) vers $85–$88 sur volume >0,8× à l'ouverture
- **Central (55%)** : consolidation dans le range $80–$85 avec volume modéré, attente d'un catalyseur
- **Pessimiste (25%)** : continuation de la baisse vers $75–$80 si le support $80 cède sur volume >0,5× à l'ouverture

**Prochaines étapes :**
- Surveiller **impérativement** la tenue du niveau **$80,00** à l'ouverture US du 17/06
- Si rebond au-dessus de $85 sur volume >0,8× → réviser vers ATTENDRE avec objectif $88–$92
- Si cassure de $80 sur volume >0,5× → réviser vers **ÉVITER** avec objectif $75–$78
- Si rebond au-dessus de $85 sur volume <0,5× → **ne pas suivre**, absence de conviction
- Monitoring comportement options J+1 (expiration 2026-06-18) — les calls $85+ sont menacés
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (breakout confirmé au-dessus de $92 sur volume >0,8×) avant toute entrée
- **Ne pas entrer long sans confirmation au-dessus de $88 sur volume >0,6×**
- Le niveau $80 reste le **pivot clé** : au-dessus = consolidation ; sous = risque d'accélération baissière

---

*Généré par le système Argus-IA — Snapshot 10h UTC 2026-06-17 (cours $82,25, RSI 28,51, volume 0,733×, score global 43,0 SURVEILLER, divergence consensus +14,9%, cours −7,5% sous MM50 $88,88, anomalies données : previous_close erroné $87,57, options JSON corrompues)*
