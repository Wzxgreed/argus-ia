# RKLB — Mise à Jour Snapshot 10h UTC 2026-06-16

> Source : `data/latest.json` (snapshot 10h UTC) | `data/recommandations_latest.json` | `RKLB_2026-06-16_DRAFT_refresh.md` (triggers PRICE_GAP +6.70%, ATR_SPIKE 11.02%) | Pipeline officiel

---

## 1. Résumé des Changements depuis le Snapshot 21h UTC 15/06

| Métrique | Snapshot 21h UTC 15/06 | Snapshot 10h UTC 16/06 | Variation |
|---|---|---|---|
| **Cours close** | $109,25 | **$109,25** | **Inchangé** — données pré-ouverture US |
| **RSI 14j** | 33,14 | **33,14** | **Inchangé** |
| **ATR 14j** | $12,04 | **$12,04** | Inchangé — volatilité stable |
| **MM 50j** | $101,57 | **$101,57** | Inchangé — spot +7,6 % |
| **MM 200j** | null | **null** | [DONNÉES MANQUANTES] |
| **Volume séance** | 28,74 M (1,03×) | **28,81 M** (1,03×) | Inchangé — participation normale |
| **Score Global ajusté** | 47,0/100 | **47,0/100** | **Inchangé** — zone SURVEILLER |
| **Score Opportunité** | 4,2/10 | **4,2/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé — plafonné FQ ≤3/6 |
| **Score Momentum** | 6,0/10 | **6,0/10** | Inchangé |
| **Forward P/E** | −15 028 | **−15 028** | Mécanique — inchangé |
| **Market Cap** | $68,26 Mds | **$68,26 Mds** | Inchangé |
| **FMP Consensus PT** | $90,83 (18 analysts) | **$90,83 (18 analysts)** | Inchangé |
| **Divergence vs consensus** | +20,3 % | **+20,3 %** | Inchangée |
| **Beta** | 2,499 | **2,499** | Inchangé |
| **Earnings Q2 2026** | 52 jours | **51 jours** | −1 jour calendaire |

**Verdict** : **Stabilité totale** des données brutes et du scoring vs le snapshot 21h UTC du 15/06. Le snapshot 10h UTC du 16/06 est un snapshot pré-ouverture US (marché fermé à 10h UTC / 6h EDT). Aucune nouvelle séance n'a eu lieu. Le DRAFT_refresh détecté (`RKLB_2026-06-16_DRAFT_refresh.md`) est un **artefact de détection pré-ouverture** — ses triggers (PRICE_GAP +6,70 %, ATR_SPIKE 11,02 %) correspondent au gap du 15/06 matin déjà traité dans `RKLB_2026-06-15_update.md` et `RKLB_2026-06-15_update_17h.md`.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 33,14 | Zone basse stable. Pas de survente extrême (<30). |
| **ATR 14j** | $12,04 | Volatilité inchangée. ATR relatif 11,0 % — élevée mais stable. |
| **MM 50j** | $101,57 | Spot $109,25 = **+7,6 %** au-dessus. Support structurel intact. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 28,0 M | Séance : **28,81 M** — **1,03× moyenne**. Participation normale. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $25,71 | Spot à **−27,6 %** du 52W high. |

**Niveaux clés** (base ATR $12,04) :
- Support immédiat : **$101,57** (MM50 — marge +7,6 %)
- Support technique majeur : **$85,17** (spot − 2×ATR)
- Support psychologique : **$90,00**
- Résistance immédiate : **$110,78** (high 15/06)
- Résistance majeure : **$113,65** (close 08/06)
- Objectif haussier : **$145,37** (spot + 3×ATR)

**Verdict timing : Neutre à légèrement favorable** — La structure technique est inchangée vs le close 21h UTC du 15/06. La MM50 ($101,57) reste un support solide avec +7,6 % de marge. Le RSI à 33,14 laisse de la place à un rebond si le sentiment global s'améliore. Cependant, sans catalyseur fondamental, la dynamique reste technique. Le marché US n'étant pas encore ouvert (snapshot 10h UTC), aucun nouveau signal technique n'est à signaler.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le 21h UTC 15/06 et le 10h UTC 16/06. `data/news_latest.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs 21h UTC 15/06 |
|---|---|---|
| Market Cap (Yahoo) | **$68,26 Mds** | Inchangé |
| Forward P/E | **−15 028** | Mécanique — inchangé |
| EV/Revenue | ~85× | Mécanique — inchangée |
| P/B (Yahoo) | ~27,8× | Mécanique |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−234,4×** | Inchangé |
| FMP Consensus PT | **$90,83 (18 analysts)** | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($68,26 Mds) vs FMP sous-jacent ($37,02 Mds). Écart persistant. Source probable : différences de méthodologie de calcul (Yahoo = fully diluted, FMP = basic outstanding) ou données non synchronisées.

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

**Divergence cours vs consensus** : Spot $109,25 vs PT $90,83 affiche une divergence de **+20,3 %**. RKLB reste significativement au-dessus du consensus sell-side.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 21h UTC 15/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | $35,00 | **[ANOMALIE JSON RÉCURRENTRE]** — retour à la valeur aberrante ($35,00) vs $120,00 cohérent du 21h UTC 15/06 |
| **Put/Call ratio (Yahoo)** | null | **[ANOMALIE JSON RÉCURRENTRE]** — données corrompues (null) vs 0,74 cohérent du 21h UTC 15/06 |
| **Call OI % (Yahoo)** | null | **[ANOMALIE JSON RÉCURRENTRE]** — données corrompues (null) vs 57,6 % cohérent du 21h UTC 15/06 |
| **Short Interest** | — | Pas de donnée fraîche — dernier connu 5,51 % |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **[ANOMALIE OPTIONS JSON RÉCURRENTRE]** — Le snapshot 10h UTC du 16/06 présente à nouveau une anomalie sur les données options : Max Pain $35,00 (aberrant), Put/Call null, Call OI null. Ces valeurs sont incohérentes avec le snapshot 21h UTC du 15/06 (Max Pain $120,00, Put/Call 0,74, Call OI 57,6 %) qui étaient stables et cohérentes. **Les données opérationnelles du 21h UTC 15/06 sont conservées comme référence.**
- **Aucune news**, aucun insider trade, aucun événement corporate détecté.
- **Social sentiment mort** — 0 mentions, pas de pump/dump.

**Verdict Sentiment : Neutre** — L'absence de news continue de dominer. L'anomalie options ne permet pas de nouvelle lecture du sentiment. Le consensus inchangé à $90,83 suggère que le sell-side maintient sa vue malgré la volatilité.

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 51 j. Consensus PT stable. Sector rotation Industrials middling. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev ~85×, divergence consensus +20,3 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 6,0/10 | Rebond consolidé à $109,25, RSI 33,14 (zone basse), MM50 réaffirmée à +7,6 %. Tendance haussière structurelle intacte. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel détecté dans `recommandations_latest.json`. |
| **Score Global ajusté** | **47,0/100** | **SURVEILLER** — Seuil 35–49, stable. |

**Comparaison avec le snapshot 21h UTC 15/06** : Le scoring est **inchangé** à 47,0/100. Tous les piliers (Catalyseur, Valorisation, Momentum) sont stables. La seule évolution est la réapparition de l'**anomalie options JSON** dans `data/latest.json` (snapshot 10h UTC), qui est documentée mais ne modifie pas les scores agents.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $109,25 (close 10h UTC 16/06) | — |
| **Stop-loss** | $85,17 (−22,0 %) | 2×ATR ($12,04) — inchangé |
| **Take-profit** | $145,37 (+33,0 %) | 3×ATR ($12,04) — inchangé |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 institutionnel |

**Zone d'intérêt technique** :
- **$101,57 (MM50)** : Support structurel intact. Marge de +7,6 % — cassure improbable sauf choc systémique.
- **$90,00** : Support psychologique + zone d'accumulation si test.
- **$110,78** : Résistance immédiate (high 15/06). Dépassement = confirmation de la neutralisation du gap.
- **$113,65** : Résistance majeure (close 08/06). Rebond au-dessus = retour à la tendance haussière pré-gap.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **51 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). Le rebond du 15/06 est de nature technique, non fondamentale.

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — SCORE GLOBAL 47,0/100**

Le snapshot 10h UTC du 16/06 confirme la thèse de **SURVEILLER** établie au close 21h UTC du 15/06, avec **stabilité totale** des données brutes et du scoring :

1. ✅ **Stabilité totale des données brutes** — Cours $109,25, RSI 33,14, ATR $12,04, MM50 $101,57, scores 47,0/100 inchangés vs 21h UTC 15/06.
2. 🟢 **DRAFT_refresh archivé comme artefact** — Les triggers PRICE_GAP +6,70 % et ATR_SPIKE 11,02 % du `RKLB_2026-06-16_DRAFT_refresh.md` correspondent au gap du 15/06 matin déjà traité. Aucun nouvel événement structurant à signaler.
3. 🔴 **[ANOMALIE OPTIONS JSON RÉCURRENTRE]** — Max Pain $35,00 / Put/Call null / Call OI null dans le snapshot 10h UTC. Valeurs aberrantes. Les données opérationnelles du 21h UTC 15/06 (Max Pain $120,00, Put/Call 0,74, Call OI 57,6 %) restent la référence.
4. 🟢 **MM50 intacte** — Spot $109,25 = +7,6 % au-dessus de la MM50 ($101,57). La tendance haussière structurelle n'est pas menacée.
5. 🟡 **RSI bas mais stable** — 33,14. La zone <30 = survente n'a pas été atteinte. Cela limite l'asymétrie haussière à court terme.
6. 🔴 **Valorisation inchangée** — Forward P/E −15 028, EV/Rev ~85×, divergence consensus +20,3 %. RKLB reste une action de croissance chère et non rentable.
7. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel. Pas d'amélioration fondamentale.

**Recommandation** : Maintenir **SURVEILLER** :
- Si le cours **casse la MM50 ($101,57)** avec volume >1,0× → **ÉVITER**.
- Si le cours **rebondit et clôture au-dessus de $113,65** (close 08/06) avec volume croissant → maintien **SURVEILLER** avec nuance positive.
- La zone **$100–$105** reste le support critique à surveiller.

Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel. Aucune nouvelle entrée n'est recommandée à ce stade. Le DRAFT_refresh est archivé comme artefact de détection pré-ouverture.

---

*Rapport généré le 2026-06-16 — Snapshot 10h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
