# RKLB — Mise à Jour Close Officiel 21h UTC (2026-06-08)

> Source : `data/latest.json` (fetched 2026-06-08T21:00:01 UTC) | `data/recommandations_latest.json` | Close officiel

---

## 1. Résumé des Changements depuis le Snapshot 17h UTC (2026-06-08)

| Métrique | Snapshot 17h | Close 21h | Variation |
|---|---|---|---|
| **Cours close** | $114,19 | **$113,65** | **−0,47 %** |
| **RSI 14j** | 41,60 | **41,29** | −0,31 pt |
| **ATR 14j** | $11,96 | **$11,96** | Inchangé |
| **Volume séance** | 8,37 M (0,30×) | **13,36 M (0,47×)** | **+59,6 %** 🔴 |
| **Score Global ajusté** | 47,0/100 | **47,0/100** | Inchangé |
| **Score Opportunité** | 4,2/10 | **4,2/10** | Inchangé |
| **Score Momentum** | 6,0/10 | **6,0/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Max Pain (JSON)** | $65,00 | **$65,00** | Inchangé |
| **Put/Call ratio** | 0,90 | **0,90** | Inchangé |
| **Call OI %** | 52,7 % | **52,7 %** | Inchangé |
| **Forward P/E** | −15 707 | **−15 633** | Légèrement moins négatif |
| **P/B Yahoo** | 29,03× | **28,90×** | −0,4 % |
| **EV/Revenue** | 91,92× | **91,92×** | Inchangé |
| **FMP Consensus PT** | $87,19 (16 analysts) | **$87,19 (16 analysts)** | Inchangé |
| **Divergence vs consensus** | +31,0 % | **+30,3 %** | −0,7 pt |
| **Beta** | 2,499 | **2,499** | Inchangé |
| **MM 50j** | $97,10 | **$97,09** | −0,01 % |
| **Market Cap Yahoo** | $71,35 Mds | **$71,01 Mds** | −0,5 % (mécanique cours) |
| **Market Cap FMP** | $37,02 Mds | **$37,02 Mds** | Inchangé |

**Verdict** : **Correction de données positive sur le volume** — le close officiel révise le volume à la hausse de 8,37 M (0,30×) à **13,36 M (0,47×)**. Cette révision atténue l'interprétation « effondrement de la participation » du snapshot 17h : la participation reste **sous la moyenne** mais n'est pas catastrophique. Le cours a légèrement reculé depuis le snapshot 17h (−0,47 %) pour clôturer à **$113,65**, en hausse de **+3,24 %** vs le close du 07/06 ($110,08). Le gap baissier du 08/06 (−8,23 % en ouverture) n'est que partiellement comblé : le spot reste **−6,5 %** sous le close du 03/06 ($121,51). L'**ATR est stable** à $11,96 (trigger ATR_SPIKE du matin résolu). Aucune news fondamentale, aucun événement corporate (`data/events_latest.json` vide). Le scoring global est **inchangé** à 47,0/100 (**SURVEILLER**).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 41,29 | Neutre-bas. Stable vs 17h (−0,31 pt). Pas de survente (< 30). |
| **ATR 14j** | $11,96 | Volatilité élevée mais stable. Trigger ATR_SPIKE du matin résolu. |
| **MM 50j** | $97,09 | Écart haussier **+17,0 %** vs spot. Tendance haussière structurelle intacte. |
| **Volume 20j** | 28 462 266 | Séance : **13,36 M** — **0,47× moyenne**. Révision à la hausse vs 17h, mais participation modérée. |
| **Beta** | 2,499 | Sensibilité systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−24,7 %** du 52W high. |
| **Range intraday** | $111,00 – $116,25 | Amplitude 4,6 %, contenu dans 0,39× ATR. |

**Niveaux clés révisés** (recalculés avec ATR $11,96) :
- Support immédiat : **$111,00** (basse intraday 08/06)
- Support technique majeur : **$89,73** (spot − 2×ATR)
- Support confluence : **$90,00** (zone psychologique)
- Résistance immédiate : **$116,25** (haute intraday 08/06)
- Résistance majeure : **$121,51** (close 03/06)
- Objectif haussier : **$149,53** (spot + 3×ATR)

**Structure options — inchangée** :
- **Max Pain** : **$65,00** — divergence −42,8 % vs spot ($113,65). Éloignement persistant à interpréter avec prudence.
- **Put/Call ratio** : **0,90** — légère prédominance call dans l'OI.
- **Call OI %** : **52,7 %** — équilibre légèrement call-skewed.
- Expiration la plus proche : **2026-06-12** (4 jours).

**Verdict timing : Favorable** — Cours > MM50 ($97,09) et rebond intraday maintenu. Le volume révisé à 0,47× atténue le verdict « sans conviction » du 17h mais ne confirme pas non plus une accumulation institutionnelle. Le RSI à 41,29 laisse de la marge avant la survente.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs snapshot 17h |
|---|---|---|
| Market Cap (Yahoo) | **$71,01 Mds** | −0,5 % (mécanique cours) |
| Forward P/E | **−15 633** | Légère amélioration vs −15 707 |
| EV/Revenue | 91,92× | Inchangé |
| P/B (Yahoo) | 28,90× | −0,4 % (mécanique cours) |
| P/S (FMP) | 61,51× | Inchangé |
| Short Interest | 5,81 % | Inchangé |
| **FMP Consensus PT** | **$87,19** (16 analysts) | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($71,01 Mds) vs FMP sous-jacent ($37,02 Mds). Écart de 91,8 % stable.

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

**Divergence cours vs consensus** : Spot $113,65 vs PT moyen $87,19 = **+30,3 % au-dessus du consensus sell-side** (−0,7 pt vs 17h).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 17h |
|---|---|---|
| **Consensus analystes (FMP)** | $87,19 (16 analysts) | Inchangé |
| **Max Pain (JSON)** | $65,00 | Inchangé |
| **Put/Call ratio** | 0,90 | Inchangé |
| **Call OI %** | 52,7 % | Inchangé |
| **Short Interest** | 5,81 % | Inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Structure options stable** : Max Pain, Put/Call et Call OI inchangés depuis le snapshot 17h.
- **Max Pain $65,00** : Divergence −42,8 % vs spot. L'expiration du 12 juin (4 jours) pourrait amplifier la volatilité si le spot reste éloigné du strike de concentration.
- **Put/Call 0,90 + Call OI 52,7 %** : Coloration haussière marginale dans l'OI, insuffisante pour contrebalancer le manque de participation au cash.

**Verdict Sentiment :** Neutre-bas — Inchangé. Aucun upgrade/downgrade détecté, absence totale d'activité retail. La structure options stable n'apporte pas de signal directionnel net.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique RKLB dans `geo_risk_latest.json`. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum score 2,65/10, RS20 vs SPY 0,03 %. Signal **NEUTRAL**. | 🟡 Malus sectoriel implicite. |
| **FX Exposure** | Score FX Impact 0,0. Flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**59 jours**). Est EPS : −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`. | Aucun malus. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 59 j. Consensus PT stable. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 92×, spot +30,3 % vs consensus. Plafonné par FQ ≤3/6. |
| **Momentum** | 6,0/10 | Rebond +3,24 % vs veille, RSI 41,29, volume révisé 0,47×. Tendance haussière intacte (prix > MM50) mais fragilisée par la participation modérée. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (valorisation extrême + divergence consensus persistante). |
| **Score Global ajusté** | **47,0/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec snapshot 17h** :
- **Score Opportunité** : 4,2 → 4,2 (inchangé)
- **Score Momentum** : 6,0 → 6,0 (inchangé)
- **Score Global ajusté** : 47,0 → 47,0 (inchangé)
- **Timing** : Favorable (inchangé)
- **Volume** : 0,30× → 0,47× (révision à la hausse, interprétation atténuée)

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $113,65 | — |
| **Stop-loss** | $89,73 (−21,0 %) | 2×ATR ($11,96) — aligné agent officiel |
| **Take-profit** | $149,53 (+31,6 %) | 3×ATR ($11,96) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Révision vs snapshot 17h** : SL/TP inchangés (ATR stable $11,96, spot quasi-stable). Le ratio R/R reste à 1,5:1, toujours insuffisant pour un trade directionnel institutionnel.

**Zone d'intérêt potentielle** : Un retour vers **$90–$97** (test support psychologique + confluence 2×ATR / MM50) constituerait une zone d'accumulation technique intéressante pour les spéculateurs, sous réserve de **confirmation de volume > 1,0× moyenne**.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **59 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-12 | **4 jours** | Max Pain JSON $65,00 (à interpréter avec prudence) |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 12 juin pourrait amplifier la volatilité à court terme compte tenu du Max Pain éloigné du spot.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — REBOND TECHNIQUE SUR VOLUME RÉVISÉ, PARTICIPATION MODÉRÉE**

Le close officiel du 21h UTC confirme la thèse du snapshot 17h UTC avec les ajustements suivants :

1. ✅ **Volume révisé à la hausse** — 8,37 M → 13,36 M (0,47× moyenne). Cette correction atténue l'interprétation « sans conviction institutionnelle » du 17h, mais la participation reste sous la moyenne. Pas d'accumulation détectée.
2. ✅ **Cours quasi-stable** — $114,19 → $113,65 (−0,47 %). Le rebond vs veille (+3,24 %) est maintenu. Pas de distribution active en after-hours.
3. ✅ **Anomalie options stabilisée** — Max Pain $65,00, Put/Call 0,90, Call OI 52,7 % inchangés. Données fiables.
4. ✅ **Trigger ATR_SPIKE résolu** — ATR stable à $11,96. Le DRAFT_refresh matinal (trigger 10,52 %) est obsolète.
5. ✅ **Métriques fondamentales inchangées** — Forward P/E −15 633, EV/Rev 92×, Filtre Qualité 3/6, consensus PT $87,19 stable.
6. ✅ **Scoring inchangé** — Score Global ajusté 47,0/100 (SURVEILLER).
7. ✅ **Timing maintenu Favorable** — Cours > MM50 ($97,09), mais à tempérer par le volume modéré.
8. ✅ **Niveaux SL/TP inchangés** — SL $89,73, TP $149,53, R/R 1,5:1.
9. 🟡 **Divergence consensus +30,3 %** — stable. Le spot s'éloigne du consensus sell-side malgré le repli cumulé depuis le 03/06.

**Recommandation** : Maintenir la posture **SURVEILLER**. Le close officiel à $113,65 (+3,24 % vs veille) confirme le rebond technique du 08/06 sans toutefois apporter la preuve d'une conviction institutionnelle (volume 0,47×). La vigilance reste de mise sur le support $90–$97 (2×ATR / MM50) en cas de poursuite de la distribution.

Attendre :
- Un **retour vers la zone $90–$97** avec **volume supérieur à la moyenne** (confirmation de capitulation), ou
- Une **stabilisation au-dessus de $116,25** (haute du 08/06) avec volume croissant vers 1,0×+ pour confirmer un rebond durable.

Toute position longue actuelle expose à un drawdown de −21,0 % (SL) en 1–2 séances compte tenu du Beta 2,50 et de l'ATR $11,96. Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel.

---

*Rapport généré le 2026-06-08 — Données : `data/latest.json` (21:00 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/quant_report_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
