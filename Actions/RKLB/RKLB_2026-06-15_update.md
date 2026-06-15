# RKLB — Mise à Jour Post-Gap 2026-06-15

> Source : `data/recommandations_latest.json` | `RKLB_2026-06-15_DRAFT_refresh.md` (triggers PRICE_GAP −10.79%, ATR_SPIKE 11.90%) | Pipeline officiel

---

## 1. Résumé des Changements depuis le Close 2026-06-09

| Métrique | Close 09/06 | Snapshot 15/06 | Variation |
|---|---|---|---|
| **Cours close** | $108,23 | **$102,39** | **−5,39 %** (−10,79 % intraday/gap) |
| **RSI 14j** | 42,93 | **33,52** | **−9,41 pts** — approche survente |
| **ATR 14j** | $12,15 | **$12,18** | +$0,03 — volatilité stable |
| **MM 50j** | $98,04 | **$100,74** | +$2,70 — spot reste +1,6 % au-dessus |
| **MM 200j** | null | **null** | [DONNÉES MANQUANTES] |
| **Volume séance** | 23,45 M (0,87×) | **62,99 M** (2,30×) | **+168 %** — distribution massive |
| **Score Global ajusté** | 45,8/100 | **37,0/100** | **−8,8 pts** — passage sous seuil ÉVITER |
| **Score Opportunité** | 4,6/10 | **3,7/10** | **−0,9 pt** |
| **Score Catalyseur** | 5,3/10 | **4,3/10** | **−1,0 pt** |
| **Score Valorisation** | 4,0/10 | **3,0/10** | **−1,0 pt** — plafonné FQ ≤3/6 |
| **Score Momentum** | 4,5/10 | **4,0/10** | **−0,5 pt** |
| **Forward P/E** | −14 887 | **−14 084** | Mécanique — inchangé |
| **Market Cap** | $67,62 Mds | **$63,98 Mds** | −5,4 % |
| **FMP Consensus PT** | $87,19 (16 analysts) | **$90,83 (18 analysts)** | **+$3,64 / +2 analysts** |
| **Divergence vs consensus** | +24,1 % | **+12,7 %** | Réduite mécaniquement |
| **Beta** | 2,499 | **2,499** | Inchangé |
| **Earnings Q2 2026** | 57 jours | **52 jours** | — |

**Verdict** : Gap baissier de **−10,79 %** sur volume 2,3× sans catalyseur fondamental identifiable. Le score global chute de **45,8 → 37,0/100**, franchissant le seuil inférieur de la zone SURVEILLER (35–49) et approchant le seuil **ÉVITER** (<35). Seule note positive : le consensus sell-side a révisé son PT à la hausse ($90,83, 18 analysts), réduisant la divergence cours/consensus de +24,1 % à +12,7 %.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 33,52 | Neutre-bas, en forte dégradation depuis 42,93. Zone <30 = survente proche. |
| **ATR 14j** | $12,18 | Volatilité élevée stable. ATR relatif 11,90 % — trigger actif. |
| **MM 50j** | $100,74 | Spot $102,39 = +1,6 % au-dessus. Support structurel **critique**. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 27,7 M | Séance : **62,99 M** — **2,30× moyenne**. Distribution confirmée. |
| **Beta** | 2,499 | Amplification extrême inchangée. Un gap S&P de −2 % = gap RKLB de −5 %. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−32,2 %** du 52W high. |

**Niveaux clés** (base ATR $12,18) :
- Support immédiat : **$100,74** (MM50 — test en cours)
- Support technique majeur : **$78,03** (spot − 2×ATR $12,18)
- Support psychologique : **$90,00**
- Résistance immédiate : **$108,23** (close 09/06)
- Résistance majeure : **$113,65** (close 08/06)
- Objectif haussier : **$138,93** (spot + 3×ATR $12,18)

**Verdict timing : Défavorable** — Gap baissier de −10,79 % sur volume 2,3× sans news. RSI en chute libre (33,52). La tendance haussière structurelle reste théoriquement intacte tant que le cours clôture au-dessus de la MM50 ($100,74), mais la marge de sécurité est réduite à +1,6 % seulement. Une cassure sous $100,74 avec volume >1,0× confirmerait un renversement de tendance haussière et justifierait un passage à **ÉVITER** strict.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_latest.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs 09/06 |
|---|---|---|
| Market Cap (Yahoo) | **$63,98 Mds** | −5,4 % |
| Forward P/E | **−14 084** | Mécanique — inchangé |
| EV/Revenue | ~86× | Mécanique — inchangée |
| P/B (Yahoo) | ~26× | Mécanique |
| FMP Gross Margin | **34,43 %** | Donnée fraîche FMP |
| FMP EV/EBITDA | **−234,4×** | Donnée fraîche FMP |
| FMP Consensus PT | **$90,83 (18 analysts)** | **+$3,64 / +2 analysts** |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($63,98 Mds) vs FMP sous-jacent historique ($37,02 Mds). Écart persistant.

**Filtre Qualité (6 critères) — inchangé** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Segment spatial / lanceurs en expansion. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif ; pertes persistantes. |
| 3. Assets/Liabilities > 1,0 | ✅ Oui | Current Ratio historique ~4,08. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | FCF yield négatif. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique, concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion. |

**Score Qualité total : 3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $102,39 vs PT $90,83 affiche une divergence de **+12,7 %** (vs +24,1 % le 09/06). La révision haussière du consensus (+$3,64) et la baisse du cours ont réduit significativement la survalorisation apparente, mais RKLB reste au-dessus du consensus sell-side.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 09/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | **+$3,64 / +2 analysts** |
| **Max Pain (Yahoo)** | $35,00 | Nouvelle donnée — divergence −65,8 % vs spot, probablement non opérationnelle |
| **Put/Call ratio (Yahoo)** | null | [DONNÉES MANQUANTES] |
| **Call OI % (Yahoo)** | null | [DONNÉES MANQUANTES] |
| **Short Interest** | — | Pas de donnée fraîche — dernier connu 5,51 % |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Consensus révisé à la hausse** — $90,83 avec 18 couvertures (+2) est le seul signal positif du jour. Cela suggère que le sell-side ne voit pas le gap baissier comme un changement de fondamentaux.
- **Aucune news**, aucun insider trade, aucun événement corporate détecté.
- **Social sentiment mort** — 0 mentions, pas de pump/dump.

**Verdict Sentiment : Neutre à légèrement positif institutionnel** — Le consensus a révisé son PT à la hausse malgré le gap, ce qui atténue la lecture la plus négative. Cependant, l'absence totale de news expliquant le gap de −10,79 % renforce l'hypothèse d'une distribution technique / prise de profit agressive plutôt qu'un changement de fondamentaux.

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 52 j. Consensus PT révisé à la hausse — léger support. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev ~86×, divergence consensus +12,7 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 4,0/10 | RSI 33,52 (chute libre), gap −10,79 %, volume 2,3×. Tendance haussière structurelle très fragilisée (MM50 $100,74, spot +1,6 %). |
| **Score Opportunité** | **3,7/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel détecté dans `recommandations_latest.json`. |
| **Score Global ajusté** | **37,0/100** | **SURVEILLER / ÉVITER** — Seuil 35–49, proche du plancher. |

**Comparaison avec le 09/06** : Le scoring s'est dégradé de **45,8 → 37,0/100** (−8,8 pts), entraîné par la chute du Catalyseur (−1,0 pt), de la Valorisation (−1,0 pt) et du Momentum (−0,5 pt). Le score global franchit le seuil inférieur de la zone SURVEILLER et approche le seuil ÉVITER (<35). Une nouvelle séance de −3 % ferait basculer le score sous 35.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $102,39 (close 15/06) | — |
| **Stop-loss** | $78,03 (−23,8 %) | 2×ATR ($12,18) — révisé à la baisse |
| **Take-profit** | $138,93 (+35,7 %) | 3×ATR ($12,18) — révisé à la baisse |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Zone d'intérêt technique** :
- **$100,74 (MM50)** : Support structurel immédiat. Une cassure avec volume >1,0× = signal de renversement haussier → passage à **ÉVITER**.
- **$90,00** : Support psychologique + zone d'accumulation si test.
- **$108,23** : Résistance immédiate (close 09/06). Rebond au-dessus = neutralisation du gap.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **52 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). Le gap du 15/06 n'a pas de catalyseur identifié.

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE MODIFIÉE 🔴 ÉVITER — SCORE GLOBAL 37,0/100**

Le gap baissier de **−10,79 %** sur volume 2,3× modifie la thèse de **SURVEILLER** (45,8/100) vers **SURVEILLER / ÉVITER** (37,0/100). Les réserves suivantes s'appliquent :

1. 🔴 **Gap baissier majeur sans news** — −10,79 % sur 62,99 M de volume (2,3×) sans catalyseur identifiable. Hypothèse privilégiée : distribution technique / prise de profit agressive.
2. 🔴 **RSI en chute libre** — 33,52 (−9,41 pts en 5 jours). Approche la zone de survente (<30), ce qui pourrait générer un rebond technique à court terme, mais la dynamique est clairement baissière.
3. 🟡 **MM50 intacte mais fragilisée** — Spot $102,39 = +1,6 % au-dessus de la MM50 ($100,74). La tendance haussière structurelle n'est pas encore cassée, mais la marge est extrêmement faible.
4. ✅ **Consensus sell-side révisé à la hausse** — PT $90,83 (+$3,64) avec 18 analysts (+2). Le sell-side ne semble pas interpréter ce gap comme un changement de fondamentaux majeur.
5. 🔴 **Score Global sous seuil critique** — 37,0/100 est à 2 pts du seuil ÉVITER (<35). Une cassure de la MM50 suffirait à basculer la recommandation.
6. 🟡 **Aucune anomalie options** — Max Pain $35,00 reste aberrant. Pas de données Put/Call fraîches.
7. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel. Pas d'amélioration fondamentale.

**Recommandation** : Passer de **SURVEILLER** à **ÉVITER** avec nuance technique :
- Si le cours **casse la MM50 ($100,74)** avec volume >1,0× → **ÉVITER** strict.
- Si le cours **rebondit et clôture au-dessus de $108,23** (close 09/06) avec volume croissant → revenir à **SURVEILLER**.
- La zone **$90–$100** reste le support critique à surveiller.

Toute position longue actuelle expose à un drawdown de −23,8 % (SL $78,03) en 1–2 séances compte tenu du Beta 2,50 et de l'ATR $12,18. Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel.

---

*Rapport généré le 2026-06-15 — Données : `data/recommandations_latest.json`, `RKLB_2026-06-15_DRAFT_refresh.md`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
