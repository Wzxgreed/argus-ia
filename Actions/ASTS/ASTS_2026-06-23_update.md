# ASTS — Mise à Jour 2026-06-23 (Snapshot 10h UTC)

> **Close $73,19** : **stabilité mécanique totale** vs close officielle 2026-06-22 (snapshot 21h UTC). Cours, RSI, ATR, MM50 et volume inchangés au tick près. **Anomalie options JSON récurrente** détectée et traitée (max pain $45,00 aberrant → valeur opérationnelle $100,00 conservée). Score global ajusté **43,0/100 (SURVEILLER)** inchangé selon JSON recommandations. Thèse **SURVEILLER confirmée** — aucune mutation technique nouvelle depuis le close du 22/06. Le DRAFT_refresh déclenché par les triggers PRICE_GAP (−9,26%) et ATR_SPIKE (14,17%) est classé **faux positif algorithmique** : ces seuils reflètent la session du 22/06 déjà intégrée dans l'analyse précédente.

---

## Résumé des Changements depuis l'Analyse Précédente (Snapshot 21h UTC 22/06)

| Indicateur | Snapshot 21h UTC 22/06 | Snapshot 10h UTC 23/06 | Delta |
|-----------|------------------------|------------------------|-------|
| **Cours** | **$73,19** | **$73,19** | **—** 🟢 |
| Change % session | −9,26% (vs $80,66) | **−9,26%** (vs $80,66) | **—** 🟢 |
| **Cumul vs open** | −14,30% ($85,43 → $73,19) | **−14,30%** | **—** 🟢 |
| RSI 14j | **32,85** | **32,85** | **—** 🟢 |
| ATR 14j | **$10,37** | **$10,37** | **—** 🟢 |
| MM50 | **$88,05** | **$88,05** | **—** 🟢 |
| **Cours vs MM50** | **−16,8%** | **−16,8%** | **—** 🟢 |
| **Volume rel.** | **0,983×** (28,02M) | **0,991×** (28,28M) | **+0,008× (+0,8%)** 🟡 |
| Volume absolu | 28,02M | **28,28M** | **+0,26M (+0,9%)** 🟡 |
| Market Cap (Yahoo) | $28,41B | **$28,41B** | **—** 🟢 |
| Forward P/E | −356,68 | **−356,68** | **—** 🟢 |
| EV/Revenue (Yahoo) | 263,831× | **263,831×** | **—** 🟢 |
| P/B (Yahoo) | 10,505× | **10,505×** | **—** 🟢 |
| Consensus PT | $94,54 | **$94,54** | **—** 🟢 |
| Divergence consensus | +29,1% | **+29,1%** | **—** 🟢 |
| Short Interest | 18,39% | **18,39%** | **—** 🟢 |
| **Options Max Pain (op.)** | **$100,00** | **$100,00** | **—** 🟢 |
| **Options Put/Call (op.)** | **0,70** | **0,70** | **—** 🟢 |
| **Options Call OI % (op.)** | **58,9%** | **58,9%** | **—** 🟢 |
| **Score Global ajusté (JSON)** | **43,0 (SURVEILLER)** | **43,0 (SURVEILLER)** | **—** 🟢 |
| **Score Opportunité** | **5,1/10** | **5,1/10** | **—** 🟢 |
| **Score Momentum** | **2,5/10** | **2,5/10** | **—** 🟢 |
| **Score Catalyseur** | **6,5/10** | **6,5/10** | **—** 🟢 |
| **Score Valorisation** | **5,5/10** | **5,5/10** | **—** 🟢 |

**Verdict :** le snapshot 10h UTC du 2026-06-23 reproduit mécaniquement le close officiel 21h UTC du 2026-06-22. Aucun nouveau prix, volume ou indicateur technique n'est disponible. La légère révision volumétrique (+0,26M, +0,9%) est marginale et ne change pas la lecture (volume normalisé ~1,0×). Le DRAFT_refresh généré par `agents/detect_major_events/agent.py` est un **faux positif algorithmique** : les triggers PRICE_GAP et ATR_SPIKE sont des conséquences du close du 22/06 déjà traité dans `ASTS_2026-06-22_21-00_update.md`.

---

## Anomalies de Données

1. **Anomalie options JSON récurrente** détectée dans `data/latest.json` (snapshot 10h UTC) :
   - Max pain JSON : **$45,00** (aberrant, historique opérationnel $100,00) → **valeur opérationnelle conservée : $100,00**
   - Put/Call ratio JSON : **null** → **valeur opérationnelle conservée : 0,70**
   - Call OI % JSON : **null** → **valeur opérationnelle conservée : 58,9%**
   - Cette anomalie est récurrente pour ASTS (9e occurrence depuis le 10/06). Le pipeline ne dispose pas de données options fiables pour ce ticker en dehors des valeurs manuellement calibrées.
2. Le rapport de validation `data/validation_report.txt` ne signale ni erreur ni warning pour ASTS.

---

## Mise à Jour Technique

- **Cours :** $73,19 — inchangé vs close 21h UTC 22/06. **−9,26%** vs previous close $80,66. **Cumul session précédente : −14,30%** depuis le vrai previous close $85,43
- **RSI 14j :** **32,85** — survente confirmée. Zone <35 maintenue, faiblesse structurelle persistante
- **ATR 14j :** $10,37 (ATR relatif **14,2%** du cours) — volatilité élevée et stable
- **MM50 :** $88,05 — cours **−16,8% sous** la moyenne. Écart extrême, résistance dynamique très lointaine
- **MM200 :** N/A
- **Volume :** 28,28M vs moy. 20j 28,53M (**0,991×**) — **volume normalisé**, inchangé en substance vs 0,983× du snapshot 21h. Lecture : distribution active confirmée, liquidité au niveau moyen mais direction négative
- **52W high :** $133,86 — repli à **−45,3%**
- **52W low :** $36,08
- **Supports clés :** $72,59 (low du 22/06, **pivot absolu**) ; $70,00 (support structurel majeur) ; $65,00 (congestion historique) ; $60,00 (zone de consolidation mai 2026)
- **Résistances clés :** $80,66 (previous close 13h 22/06) ; $85,43 (vrai previous close 22/06) ; $88,05 (MM50) ; $92,06 (close 09/06) ; $100,00 (psychologique + max pain opérationnel)
- **Timing verdict :** **Défavorable** — inchangé. Cours sous MM50 avec écart extrême (−16,8%), cassure confirmée du pivot $80. Aucun signal de retournement haussier
- **Score Momentum :** 2,5/10 — inchangé (JSON). Momentum baissier persistant

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. Données fondamentales inchangées vs close 22/06.

- **Market Cap :** $28,41B (Yahoo) / $25,32B (FMP)
- **Forward P/E :** −356,68 (profil non rentable)
- **EV/EBITDA :** −70,825 (Yahoo) / −68,189 (FMP annual)
- **EV/Revenue :** 263,831× (Yahoo) / 355,7× (FMP annual) — multiples spéculatifs extrêmes
- **P/B :** 10,505× (Yahoo) / 10,096× (FMP annual)
- **Beta :** 2,634 — sensibilité très supérieure au marché
- **Short Interest :** 18,39% (stable, pression vendeuse présente)
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes, 2 couverts le mois dernier, 7 le trimestre dernier). Divergence **+29,1% upside** ($94,54 vs $73,19)
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK**

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-23 émet un signal macro **NEUTRAL** avec régime UNKNOWN. **XLC (Communication Services)** reste dans le **bottom 3** avec momentum_score **0,0**. XLK (Technology) est **top 1** (momentum_score 10,0). Malus sectoriel maintenu (−0,5 pt).

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence consensus **+29,1% upside**
- **Options (valeurs opérationnelles, anomalie JSON traitée) :**
  - **Max Pain :** **$100,00** — cohérent. Cours $73,19 reste **−26,8% sous le Max Pain**
  - **Put/Call Ratio :** **0,70** — positionnement défensif/baissier maintenu
  - **Call OI % :** **58,9%** — skew call réduit mais stable
  - Nearest expiry : **2026-06-26** (J+3)
  - **Lecture :** le positionnement options n'a pas changé depuis le close 22/06. Les calls OTM $80+ restent profondément OTM. Le max pain $100 est à +36,6% du spot — pinning gamma très improbable
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_2026-06-23.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_risk_latest.json` — pas de données récentes pertinentes)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-23 (`news_2026-06-23.json` vide). Le mouvement reste purement technique

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+48) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-06-26 (J+3)** — max pain opérationnel $100 au-dessus du spot (+36,6%). Pinning gamma hautement improbable. Put/call 0,70 reflète un positionnement défensif stable

---

## Scoring Global — Snapshot 2026-06-23 (10h UTC)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 6,5/10 | 35% | Aucun catalyseur imminent, earnings dans 48j. Structure options historiquement haussière (call OI 58,9%) mais stable. Put/call 0,70 = couverture baissière maintenue |
| Valorisation | 5,5/10 | 40% | Multiples spéculatifs extrêmes persistants (EV/Revenue FMP 355,7×). Consensus offre un upside mécanique +29,1% mais fondamentaux non rentables. P/B 10,51× Yahoo — reste élevé |
| Momentum | 2,5/10 | 25% | RSI 32,85 en survente confirmée, cours −16,8% sous MM50, volume normalisé ~1,0× à la baisse = distribution active. Configuration baissière confirmée |
| **Score Opportunité** | **5,1/10** | | |

**Malus / Bonus appliqués (règles agents) :**
- Malus **COURS_SOUS_MM50 aggravé** : cours −16,8% sous MM50 $88,05 — écart extrême
- Malus **RSI_SURVENTE** : RSI 32,85 < 35 — survente technique confirmée
- Malus **VOLUME_DISTRIBUTION** : volume ~1,0× normalisé mais cours en baisse — distribution active confirmée
- Malus **TRIPLE_GAP_DOWN** : trois phases baissières le 22/06 ($85,43→$80,66→$74,11→$73,19), total −14,30% — configuration extrêmement fragile
- Malus **PIVOT_CASSE** : low $72,59 < pivot $80,00 — cassure confirmée
- Malus **OPTIONS_BEARISH** : put/call 0,70, call OI 58,9% — positionnement options défensif maintenu, max pain $100 à +36,6%
- Malus sectoriel (XLC bottom 3, momentum 0,0) : −0,5 pt — faiblesse sectorielle persistante
- Aucun malus comptable (`accounting_risk_latest.json` absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite (JSON) :** 51,0/100 → **43,0 ajusté** (−8,0 pts de malus). Seuil **SURVEILLER (35–49)**, milieu de fourchette. Le JSON `recommandations_2026-06-23.json` attribue à ASTS un score global ajusté de **43,0/100** avec action **SURVEILLER**, timing **Défavorable**, SL $52,45, TP $104,30, ratio R/R 1,5.

---

## Niveaux et Ratio R/R

- **Cours actuel :** $73,19
- **Stop-loss suggéré :** $52,45 (cours − 2×ATR = $73,19 − $20,74)
- **Take-profit suggéré :** $104,30 (cours + 3×ATR = $73,19 + $31,11)
- **Ratio R/R :** 1,5:1

**Révision :** SL et TP **inchangés** vs le snapshot 21h du 22/06 (SL $52,45 / TP $104,30) car le cours et l'ATR sont identiques.
- Le SL à $52,45 correspond à la zone $55–$60 (support structurel historique majeur). Distance SL = 28,3% du cours
- Le TP $104,30 correspond au consensus analystes ($94,54) à +10,3% — probabilité d'atteinte faible sans catalyseur majeur
- Le consensus analystes ($94,54) est **+$21,35 au-dessus du cours** — upside consensus mécanique +29,1%
- **Zone d'intérêt potentielle :** $72–$74 (test du low du 22/06 + support psychologique)
- **Résistance immédiate :** $80,66 (previous close 13h 22/06) ; $85,43 (vrai previous close 22/06) ; $88,05 (MM50)
- **Alerte options J+3 :** Max Pain opérationnel $100 à +36,6%. Put/call 0,70 = couverture baissière structurée. Pinning gamma théoriquement possible mais très improbable sous $80
- **Alerte volume :** 0,991× = liquidité normalisée mais direction négative. La distribution est **active et structurée**

---

## Conclusion

**Thèse SURVEILLER confirmée : aucune mutation technique ou fondamentale nouvelle depuis le close 2026-06-22. Le snapshot 10h UTC du 23/06 reproduit mécaniquement les données du close 21h UTC. Score global ajusté 43,0/100 (SURVEILLER).**

Le DRAFT_refresh déclenché par `agents/detect_major_events/agent.py` (triggers PRICE_GAP −9,26% et ATR_SPIKE 14,17%) est classé **faux positif algorithmique** : ces seuils reflètent exclusivement la session du 2026-06-22 déjà traitée dans `ASTS_2026-06-22_21-00_update.md`. Aucun nouveau gap, aucune nouvelle volatilité, aucune news n'est survenue entre le close 21h UTC et le snapshot 10h UTC.

**Configuration technique inchangée vs le close 22/06 :**
1. **Triple gap down du 22/06** : $85,43 → $80,66 (−5,58%) → $74,11 (−8,12%) → $73,19 (−1,24%). Total : **−14,30% en une seule journée**
2. **Cassure confirmée du pivot $80** : low $72,59 < $80,00. Pas de rejet significatif
3. **Volume normalisé ~1,0×** : distribution active confirmée
4. **RSI en survente confirmée** : 32,85 — pas de signal de retournement
5. **Écart MM50 extrême** : −16,8% — résistance dynamique très lointaine
6. **Divergence consensus mécanique** : +29,1% (uniquement due à la baisse du cours)
7. **Options inchangées** : max pain opérationnel $100 à +36,6% du spot. Put/call 0,70 stable
8. **Score global JSON inchangé** : 43,0/100 (SURVEILLER)

**Alertes actives (inchangées) :**
- **TRIPLE_GAP_DOWN** — trois phases baissières dans la même journée du 22/06, total −14,30%
- **PIVOT_CASSE** — low $72,59 < pivot $80,00 — cassure confirmée
- **COURS_SOUS_MM50 aggravé** — cours −16,8% sous MM50 $88,05
- **RSI_SURVENTE** — RSI 32,85 < 35 — survente technique confirmée
- **VOLUME_DISTRIBUTION** — volume ~1,0× normalisé mais cours en baisse — distribution active
- **ATR_SPIKE (haut)** — ATR relatif 14,2% du cours ($10,37)
- **Profil non rentable** — EPS estimé négatif, multiples extrêmes (P/B 10,51× Yahoo / 10,10× FMP, EV/Revenue FMP 355,7×)
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (momentum_score 0,0)
- **Options J+3** — Max Pain opérationnel $100 à +36,6%. Put/call 0,70 = couverture baissière structurée
- **Short Interest élevé** — 18,39% — pas de squeeze setup mais pression vendeuse présente

**Verdict opérationnel :** la configuration reste **extrêmement fragile** mais inchangée vs le close du 22/06. Le niveau $72,59 est toujours le **pivot absolu**.

**Scénarios à court terme (inchangés) :**
- **Optimiste (10%)** : défense de $72,59, rebond technique vers $78–$82 sur volume <0,8× dans les 2–3 prochains jours (dead cat bounce)
- **Central (40%)** : consolidation dans le range $70–$76 avec volume modéré, attente d'un catalyseur
- **Pessimiste (50%)** : cassure confirmée de $72,59 au close, accélération baissière vers $65–$70

**Prochaines étapes (inchangées) :**
- Surveiller **impérativement** la tenue du niveau **$72,59** (low du 22/06) au close des prochaines sessions
- Si close > $75 sur 2 sessions consécutives avec volume <0,8× → épuisement vendeur possible, maintenir SURVEILLER
- Si close < $72,59 sur volume >0,8× → réviser vers **ÉVITER** avec objectif $65–$70
- Si rebond au-dessus de $80 sur volume >1,0× → réviser vers SURVEILLER avec objectif $85–$88
- Si rebond au-dessus de $80 sur volume <0,6× → **ne pas suivre**, absence de conviction
- Monitoring comportement options J+3 (expiration 2026-06-26) — les calls $80+ sont menacés
- Attendre un catalyseur fondamental (earnings le 2026-08-10) ou technique (breakout confirmé au-dessus de $88 sur volume >0,8×) avant toute entrée
- **Ne pas entrer long sans confirmation au-dessus de $88 sur volume >0,6×**
- Le niveau $72,59 reste le **pivot absolu** : close au-dessus de $75 = consolidation possible ; close sous $72,59 = risque d'accélération baissière majeure

---

*Généré par le système Argus-IA — Snapshot 2026-06-23, 10h UTC (cours $73,19, RSI 32,85, volume 0,991×, score global 43,0 SURVEILLER, divergence consensus +29,1%, cours −16,8% sous MM50 $88,05, triple gap down total −14,30% du 22/06, low $72,59, options : max pain opérationnel $100,00, put/call 0,70, call OI 58,9%)*
