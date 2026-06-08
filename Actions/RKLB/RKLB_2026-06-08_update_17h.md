# RKLB — Mise à Jour Snapshot 17h UTC (2026-06-08)

> Source : `data/latest.json` (fetched 2026-06-08T17:00:02 UTC) | `data/recommandations_latest.json` | Snapshot 17h UTC

---

## 1. Résumé des Changements depuis le Snapshot 13h UTC (2026-06-08)

| Métrique | Snapshot 13h | Snapshot 17h | Variation |
|---|---|---|---|
| **Cours close** | $110,08 | **$114,19** | **+3,73 %** 🟡 |
| **RSI 14j** | 42,89 | **41,60** | −1,29 pt |
| **ATR 14j** | $12,49 | **$11,96** | −4,2 % |
| **Volume séance** | 21,34 M (0,67×) | **8,37 M (0,30×)** | **−60,8 %** 🔴 |
| **Score Global ajusté** | 43,3/100 | **47,0/100** | **+3,7 pts** |
| **Score Opportunité** | 3,8/10 | **4,2/10** | +0,4 pt |
| **Score Momentum** | 4,5/10 | **6,0/10** | **+1,5 pt** |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Max Pain (JSON)** | $65,00 | **$65,00** | Inchangé |
| **Put/Call ratio** | 0,90 | **0,90** | Inchangé |
| **Call OI %** | 52,7 % | **52,7 %** | Inchangé |
| **Forward P/E** | −15 142 | **−15 707** | Légèrement plus négatif |
| **P/B Yahoo** | 27,99× | **29,03×** | +3,7 % (mécanique cours) |
| **EV/Revenue** | 91,92× | **91,92×** | Inchangé |
| **FMP Consensus PT** | $87,19 (16 analysts) | **$87,19 (16 analysts)** | Inchangé |
| **Divergence vs consensus** | +26,3 % | **+31,0 %** | +4,7 pts |
| **Beta** | 2,499 | **2,499** | Inchangé |
| **MM 50j** | $96,14 | **$97,10** | +1,0 % |
| **Market Cap Yahoo** | $68,78 Mds | **$71,35 Mds** | +3,7 % (mécanique cours) |

**Verdict** : **Rebond technique +3,73 %** du close précédent ($110,08 → $114,19) sur un **volume effondré à 0,30×** la moyenne 20 jours (8,37 M vs 28,21 M). Ce rebond est **dépourvu de conviction institutionnelle** — la participation a chuté de 60,8 % par rapport au snapshot 13h (déjà faible à 0,67×). Le gap du 08/06 (−8,23 % en ouverture) n'est que partiellement comblé : le cours reste **−6,0 %** sous le close du 03/06 ($121,51). L'**ATR compresse légèrement** à $11,96 (−4,2 %), ce qui **résout le trigger ATR_SPIKE** (10,47 %) détecté ce matin et enregistré dans le `DRAFT_refresh.md`. Aucune news fondamentale, aucun événement corporate (`events_latest.json` vide). Le scoring global s'améliore mécaniquement (+3,7 pts) sous l'effet du rebond cours, mais reste dans la zone **SURVEILLER**.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 41,60 | Neutre-bas. Légère baisse (−1,29 pt) malgré le rebond cours, signe d'une pression vendeuse sous-jacente persistante. Pas de survente (< 30). |
| **ATR 14j** | $11,96 | Volatilité élevée mais en **compression** (−4,2 % vs 13h). Le trigger ATR_SPIKE du matin est résolu. |
| **MM 50j** | $97,10 | Écart haussier **+17,6 %** vs spot. Tendance haussière structurelle intacte. |
| **Volume 20j** | 28 213 029 | Séance : **8,37 M** — **0,30× moyenne**. Participation extrêmement faible, en décroissance vs 0,67× au snapshot 13h. |
| **Beta** | 2,499 | Sensibilité systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−24,4 %** du 52W high. |
| **Range intraday** | $111,00 – $116,25 | Amplitude 4,6 %, contenu dans 0,39× ATR. Rebond depuis le low sans volume. |

**Niveaux clés révisés** (recalculés avec ATR $11,96) :
- Support immédiat : **$111,00** (basse intraday 08/06)
- Support technique majeur : **$90,27** (spot − 2×ATR)
- Support confluence : **$90,00** (zone psychologique)
- Résistance immédiate : **$116,25** (haute intraday 08/06)
- Résistance majeure : **$123,32** (close 03/06)
- Objectif haussier : **$150,07** (spot + 3×ATR)

**Structure options — inchangée** :
- **Max Pain** : **$65,00** — divergence −43,1 % vs spot ($114,19). Éloignement persistant à interpréter avec prudence.
- **Put/Call ratio** : **0,90** — légère prédominance call dans l'OI.
- **Call OI %** : **52,7 %** — équilibre légèrement call-skewed.
- Expiration la plus proche : **2026-06-12** (4 jours).

**Verdict timing : Favorable** — L'agent recommandation bascule le timing de **Défavorable** (snapshot 13h) à **Favorable**, porté par le cours > MM50 ($97,10) et le rebond intraday. Cependant, ce verdict est **fortement tempéré** par le volume effondré (0,30×) qui traduit un manque de participation institutionnelle. Le RSI à 41,60 laisse de la marge avant la survente, mais la pression vendeuse n'est pas dissipée.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-08.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs snapshot 13h |
|---|---|---|
| Market Cap (Yahoo) | **$71,35 Mds** | +3,7 % (mécanique cours) |
| Forward P/E | **−15 707** | Légère dégradation vs −15 142 |
| EV/Revenue | 91,92× | Inchangé |
| P/B (Yahoo) | 29,03× | +3,7 % (mécanique cours) |
| P/S (FMP) | 61,51× | Inchangé |
| Short Interest | 5,81 % | Inchangé |
| **FMP Consensus PT** | **$87,19** (16 analysts) | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($71,35 Mds) vs FMP sous-jacent ($37,02 Mds). Écart de 92,7 % en expansion.

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

**Divergence cours vs consensus** : Spot $114,19 vs PT moyen $87,19 = **+31,0 % au-dessus du consensus sell-side** (+4,7 pts vs snapshot 13h).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 13h |
|---|---|---|
| **Consensus analystes (FMP)** | $87,19 (16 analysts) | Inchangé |
| **Max Pain (JSON)** | $65,00 | Inchangé |
| **Put/Call ratio** | 0,90 | Inchangé |
| **Call OI %** | 52,7 % | Inchangé |
| **Short Interest** | 5,81 % | Inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Structure options stable** : Max Pain, Put/Call et Call OI inchangés depuis le snapshot 13h. La résolution de l'anomalie matinale est confirmée.
- **Max Pain $65,00** : Divergence −43,1 % vs spot. L'expiration du 12 juin (4 jours) pourrait amplifier la volatilité si le spot reste éloigné du strike de concentration.
- **Put/Call 0,90 + Call OI 52,7 %** : Coloration haussière marginale dans l'OI, insuffisante pour contrebalancer le manque de participation au cash.

**Verdict Sentiment :** Neutre-bas — Inchangé. Aucun upgrade/downgrade détecté, absence totale d'activité retail. La structure options stable n'apporte pas de signal directionnel net.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique RKLB dans `geo_risk_latest.json`. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum score 2,50/10, RS20 vs SPY −0,11 %. Signal **NEUTRAL**. | 🟡 Malus sectoriel implicite. |
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
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 92×, spot +31,0 % vs consensus. Plafonné par FQ ≤3/6. |
| **Momentum** | 6,0/10 | Rebond +3,73 %, RSI 41,60, volume effondré 0,30×. Tendance haussière intacte (prix > MM50) mais fragilisée par l'absence de participation. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (valorisation extrême + divergence consensus persistante). |
| **Score Global ajusté** | **47,0/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec snapshot 13h** :
- **Score Opportunité** : 3,8 → 4,2 (+0,4 pt) — hausse mécanique du Momentum.
- **Score Momentum** : 4,5 → 6,0 (+1,5 pt) — rebond cours, mais volume déplorable.
- **Score Global ajusté** : 43,3 → 47,0 (+3,7 pts) — reste dans la fourchette SURVEILLER.
- **Timing** : Défavorable → **Favorable** (bascule agent recommandation, à tempérer par le volume).

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $114,19 | — |
| **Stop-loss** | $90,27 (−20,9 %) | 2×ATR ($11,96) — aligné agent officiel |
| **Take-profit** | $150,07 (+31,4 %) | 3×ATR ($11,96) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Révision vs snapshot 13h** : SL remonté de $85,10 à $90,27 (compression ATR + rebond cours). TP remonté de $147,55 à $150,07. Le ratio R/R reste à 1,5:1, toujours insuffisant pour un trade directionnel institutionnel.

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

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — REBOND TECHNIQUE SANS CONVICTION, VOLUME EFFONDRE**

Le snapshot du 17h UTC confirme la thèse du snapshot 13h UTC avec les ajustements mécaniques suivants :

1. ✅ **Rebond technique +3,73 %** — $110,08 → $114,19. Pas de gap haussier : progression linéaire intraday depuis $111,00.
2. ✅ **Volume effondré 0,30×** — 8,37 M vs 28,21 M moy. Participation en chute libre (−60,8 % vs snapshot 13h). **Pas de conviction institutionnelle**.
3. ✅ **Anomalie options stabilisée** — Max Pain $65,00, Put/Call 0,90, Call OI 52,7 % inchangés depuis 13h. Données fiables.
4. ✅ **Trigger ATR_SPIKE résolu** — ATR compresse à $11,96 (−4,2 %). Le DRAFT_refresh matinal (trigger 10,47 %) est obsolète.
5. ✅ **Métriques fondamentales inchangées** — Forward P/E −15 707, EV/Rev 92×, Filtre Qualité 3/6, consensus PT $87,19 stable.
6. ✅ **Scoring légèrement amélioré** — Score Global ajusté 47,0/100 (SURVEILLER), +3,7 pts vs 13h. Reste dans la zone SURVEILLER.
7. ✅ **Timing basculé Favorable** — Selon l'agent recommandation (cours > MM50), mais à tempérer par le volume.
8. ✅ **Niveaux SL/TP révisés** — SL $90,27, TP $150,07, R/R 1,5:1.
9. 🟡 **Divergence consensus +31,0 %** — en expansion (+4,7 pts). Le spot s'éloigne du consensus sell-side malgré le repli cumulé depuis le 03/06.

**Recommandation** : Maintenir la posture **SURVEILLER**. Le rebond +3,73 % n'est pas un signal d'achat : il s'accompagne d'un volume effondré qui dénote l'absence de participation institutionnelle. La vigilance reste de mise sur le support $90–$97 (2×ATR / MM50) en cas de poursuite de la distribution.

Attendre :
- Un **retour vers la zone $90–$97** avec **volume supérieur à la moyenne** (confirmation de capitulation), ou
- Une **stabilisation au-dessus de $116,25** (haute du 08/06) avec volume croissant vers 1,0×+ pour confirmer un rebond durable.

Toute position longue actuelle expose à un drawdown de −20,9 % (SL) en 1–2 séances compte tenu du Beta 2,50 et de l'ATR $11,96. Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel.

---

*Rapport généré le 2026-06-08 — Données : `data/latest.json` (17:00 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/quant_report_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
