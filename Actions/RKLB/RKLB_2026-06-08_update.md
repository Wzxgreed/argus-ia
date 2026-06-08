# RKLB — Mise à Jour Post-Gap (2026-06-08)

> Source : `data/latest.json` (fetched 2026-06-08T10:00:02 UTC) | `data/recommandations_2026-06-08.json` | Snapshot 10h UTC

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC (2026-06-03)

| Métrique | Snapshot 03/06 | Snapshot 08/06 | Variation |
|---|---|---|---|
| **Cours close** | $123,32 | **$110,08** | **−13,24 $ (−10,7 %)** |
| **RSI 14j** | 52,81 | **42,89** | **−9,92 pts** 🔴 |
| **ATR 14j** | $12,33 | **$12,49** | +$0,16 (+1,3 %) |
| **Volume séance** | 19,34 M (0,62×) | **21,34 M (0,67×)** | +2,0 M, participation légèrement meilleure |
| **Score Global Agent** | 44,5/100 (aj. 49,5) | **38,3/100 (aj. 43,3)** | **−6,2 pts** 🔴 |
| **Score Opportunité** | 4,5/10 | **3,8/10** | −0,7 pt |
| **Score Momentum** | 7,0/10 | **4,5/10** | **−2,5 pts** 🔴 |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Max Pain (JSON)** | $45,00 (anomalie) | **$45,00** | Anomalie persistante — [NON OPÉRATIONNEL] |
| **Forward P/E** | −11 191 | **−15 142** | Détérioration |
| **P/B Yahoo** | 31,36× | **27,99×** | −3,37 pts |
| **EV/Revenue** | 103,19× | **91,92×** | −11,3 % |
| **FMP Consensus PT** | $84,20 (15 analysts) | **$87,19 (16 analysts)** | **+$2,99 (+3,5 %)** 🟡 |
| **Divergence vs consensus** | +46,5 % | **+26,3 %** | Réduction significative |
| **Beta** | 2,313 | **2,499** | +0,186 |
| **MM 50j** | $93,38 | **$96,14** | +$2,76 |
| **52W High / Low** | $151,00 / $25,24 | **$151,00 / $25,24** | Inchangé |
| **Earnings Q2 2026** | 64 jours | **59 jours** | −5j |

**Verdict** : **Gap significatif −8,23 %** sur la séance du 8 juin porte le repli cumulé depuis le 3 juin à **−10,7 %**. Le RSI franchit la zone neutre (52,81 → 42,89) et le Score Momentum s'effondre (7,0 → 4,5). Le consensus sell-side a *haussé* son PT moyen à $87,19 (+3,5 %) malgré la baisse du cours — la divergence consensus se réduit mécaniquement de +46,5 % à +26,3 %. La valorisation reste extrême (Forward P/E négatif, EV/Rev 92×) et le Filtre Qualité 3/6 maintient le plafonnement à 5/10. **Aucun événement corporate détecté** (`events_latest.json` vide).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 42,89 | Neutre-bas. Sorti de la zone neutre haute (52,81) sans atteindre la survente (<30). Momentum dégradé. |
| **ATR 14j** | $12,49 | Volatilité élevée en légère expansion (+1,3 %). Le gap −8,23 % est contenu dans 0,66× ATR. |
| **MM 50j** | $96,14 | Écart haussier **+14,5 %** vs spot (était +32,1 %). Réduction mécanique du premium de tendance. |
| **Volume 20j** | 31 790 650 | Séance 08/06 : **21,34 M** — **0,67× moyenne**. Participation modérée, légèrement supérieure au 03/06 (0,62×). |
| **Beta** | 2,499 | Sensibilité systématique extrême en hausse (+8,0 %). Amplification des mouvements de marché. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−27,1 %** du 52W high (était −18,3 %). Éloignement des sommets. |
| **Range intraday** | $106,73 – $117,98 | Gap down suivi d'un repli intra jusqu'à −12,5 % avant rebond partiel à −8,2 %. |

**Niveaux clés révisés** :
- Support immédiat : **$106,73** (basse intraday 08/06)
- Support technique majeur : **$85,10** (spot − 2×ATR = $110,08 − $24,98) — aligné agent officiel
- Support confluence : **$90,00** (zone psychologique + ancien Max Pain opérationnel)
- Résistance immédiate : **$117,98** (haute intraday 08/06)
- Résistance majeure : **$123,32** (close 03/06 — ancien support devenu résistance)
- Objectif haussier : **$147,55** (spot + 3×ATR) — aligné agent officiel
- **[ANOMALIE OPTIONS PERSISTANTE]** : `latest.json` affiche Max Pain **$45,00** (vs spot $110,08). Divergence de −59,1 % sans fondement. **Valeur rejetée** — cause probable : corruption partielle du flux options JSON.

**Verdict timing : Défavorable** — Le gap −8,23 % avec volume modéré (0,67×) confirme une distribution active plutôt qu'une capitulation. Le RSI à 42,89 laisse encore de la marge avant la survente (<30). Le cours reste au-dessus de la MM50 ($96,14) donc la tendance haussière structurelle n'est pas rompue, mais le momentum s'est effondré (7,0 → 4,5). Le support $85,10 (2×ATR) est le pivot clé.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-08.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate). Le gap est purement technique/sentiment.

| Métrique | Valeur | Variation vs 03/06 |
|---|---|---|
| Market Cap (Yahoo) | **$68,78 Mds** | −$2,61 Mds (−3,7 %) |
| Forward P/E | **−15 142** | Détérioration (−36 %) |
| EV/Revenue | 91,92× | −11,3 % |
| P/B (Yahoo) | 27,99× | −10,7 % |
| P/S (FMP) | 61,51× | Inchangé |
| Short Interest | 5,81 % | Stable |
| **FMP Consensus PT** | **$87,19** (16 analysts) | **+$2,99 (+3,5 %)** 🟡 |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($68,78 Mds) vs FMP sous-jacent ($37,02 Mds) persiste. Écart de 85,7 %.

**Filtre Qualité (6 critères) — inchangé** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Segment spatial / lanceurs en expansion. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif ; pertes persistantes. |
| 3. Assets/Liabilities > 1,0 | ✅ Oui | Current Ratio 4,08. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | FCF yield négatif. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique, concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion. |

**Score Qualité total : 3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $110,08 vs PT moyen $87,19 = **+26,3 % au-dessus du consensus sell-side** (était +46,5 %). La réduction de divergence est mécanique (baisse du cours + hausse du PT) mais la prime reste significative.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 03/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $87,19 (16 analysts) | **+$2,99 (+3,5 %)** — hausse malgré baisse cours |
| **Max Pain (JSON)** | $45,00 | Anomalie persistante — [NON OPÉRATIONNEL] |
| **Put/Call ratio** | *Absent* | Données interrompues dans latest.json |
| **Call OI %** | *Absent* | Données interrompues dans latest.json |
| **Short Interest** | 5,81 % | Stable |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **[ANOMALIE OPTIONS PERSISTANTE]** : Max Pain $45,00 dans `latest.json` est aberrant. Les données Put/Call et Call OI sont absentes du snapshot du 08/06. La structure options du 03/06 (Put/Call 1,18, Call OI 45,9 %) est la dernière connue mais obsolète de 5 jours.
- **Consensus haussé** : Le PT moyen est passé de $84,20 à $87,19 avec un analyste supplémentaire (16 vs 15). Cela peut refléter une révision post-gap baissier ou un ajustement du modèle. Malgré cela, le spot reste +26,3 % au-dessus du consensus.

**Verdict Sentiment :** Neutre-bas — Aucun upgrade/downgrade détecté, absence totale d'activité retail. La dégradation du Score Momentum (7,0 → 4,5) et le gap −8,23 % traduisent un retrait des acheteurs. La hausse du consensus PT est un signal positif marginal mais insuffisant face à la chute de cours.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique RKLB. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum score 2,05/10, RS20 vs SPY −0,71 %. Signal NEUTRAL. | 🟡 Malus sectoriel implicite. |
| **FX Exposure** | Score FX Impact 0,0. Flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**59 jours**). Est EPS : −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`. | Aucun malus. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 59j. Consensus PT révisé à la hausse (+3,5 %) — signal positif marginal. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 92×, spot +26,3 % vs consensus. Plafonné par FQ ≤3/6. |
| **Momentum** | 4,5/10 | **Effondrement** (était 7,0). Gap −8,23 %, RSI 42,89, volume modéré 0,67×. Tendance haussière intacte (prix > MM50) mais fragilisée. |
| **Score Opportunité** | **3,8/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (valorisation extrême + divergence consensus persistante). |
| **Score Global ajusté** | **43,3/100** | **SURVEILLER** — Seuil 35–49. L'agent officiel classe SURVEILLER. |

**Comparaison avec snapshot 03/06** : Le score global ajusté chute de **49,5 à 43,3 (−6,2 pts)**. La quasi-totalité de la dégradation vient du Momentum (7,0 → 4,5) sous l'effet du gap −8,23 %. Le Catalyseur et la Valorisation sont stables. Le Consensus PT s'est amélioré (+3,5 %) mais cela ne compense pas la chute technique.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $110,08 | — |
| **Stop-loss** | $85,10 (−22,7 %) | 2×ATR ($12,49) — aligné agent officiel |
| **Take-profit** | $147,55 (+34,0 %) | 3×ATR ($12,49) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Révision vs 03/06** : Les niveaux sont révisés à la baisse mécaniquement (SL $98,66 → $85,10, TP $160,31 → $147,55) en raison du gap −8,23 %. Le ratio R/R reste à 1,5:1. Le SL élargi à −22,7 % reflète la volatilité extrême (Beta 2,50, ATR $12,49).

**Zone d'intérêt potentielle** : Un retour vers **$90–$97** (test support psychologique + confluence 2×ATR) constituerait une zone d'accumulation technique intéressante pour les spéculateurs, sous réserve de confirmation de volume.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **59 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août).

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE MODIFIÉE 🟡 SURVEILLER — DÉGRADATION TECHNIQUE SIGNIFICATIVE**

Le snapshot du 8 juin 2026 modifie la thèse du 3 juin sur le plan technique tout en maintenant le verdict global SURVEILLER :

1. 🔴 **Gap −8,23 %** — mouvement significatif (>5 %) sans news fondamentale. Distribution active confirmée.
2. 🔴 **RSI dégradé** — 52,81 → 42,89. Sortie de la zone neutre haute vers le bas.
3. 🔴 **Score Momentum effondré** — 7,0 → 4,5. La tendance haussière structurelle (prix > MM50) n'est pas rompue mais fragilisée.
4. 🔴 **Score Global ajusté** — 49,5 → 43,3 (−6,2 pts). Passage de la limite supérieure vers le milieu de la fourchette SURVEILLER.
5. 🟡 **Consensus PT haussé** — $87,19 (+3,5 %) avec 16 analysts. Signal positif marginal mais spot reste +26,3 % au-dessus.
6. 🟡 **Divergence consensus réduite** — +46,5 % → +26,3 %. Mécanique (baisse cours + hausse PT).
7. 🟡 **Volume légèrement meilleur** — 0,67× (vs 0,62×). Participation modérée mais pas de capitulation.
8. 🟡 **Options corrompues** — Max Pain JSON $45,00 persistant (anomalie), données Put/Call absentes.
9. ✅ **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
10. ✅ **Earnings** inchangé — 59 jours.

**Recommandation** : Maintenir la posture **SURVEILLER**. Le gap −8,23 % ne justifie pas un passage à ÉVITER (le cours reste > MM50, le consensus s'est amélioré), mais la dégradation technique est réelle et le risque d'un test du support $85–$90 est élevé compte tenu du Beta 2,50 et de l'ATR $12,49.

Attendre :
- Un **retour vers la zone $90–$97** avec **volume supérieur à la moyenne** (confirmation de capitulation), ou
- Une **stabilisation au-dessus de $117,98** (haute du 08/06) avec volume croissant pour confirmer un rebond.

Toute position longue actuelle expose à un drawdown de −22,7 % (SL) en 1–2 séances. Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel.

---

*Rapport généré le 2026-06-08 — Données : `data/latest.json` (10:00 UTC), `data/recommandations_2026-06-08.json`, `data/upcoming_events_2026-06-08.json`, `data/events_2026-06-08.json`, `data/sector_rotation_2026-06-08.json`, `data/quant_report_2026-05-17.json`, `data/social_sentiment_2026-06-08.json`, `data/fx_exposure_2026-06-08.json`*
