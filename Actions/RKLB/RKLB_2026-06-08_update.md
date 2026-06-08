# RKLB — Mise à Jour Snapshot 13h UTC (2026-06-08)

> Source : `data/latest.json` (fetched 2026-06-08T13:00:01 UTC) | `data/recommandations_latest.json` | Snapshot 13h UTC

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC (2026-06-08)

| Métrique | Snapshot 10h | Snapshot 13h | Variation |
|---|---|---|---|
| **Cours close** | $110,08 | **$110,08** | **Inchangé** |
| **RSI 14j** | 42,89 | **42,89** | Inchangé |
| **ATR 14j** | $12,49 | **$12,49** | Inchangé |
| **Volume séance** | 21,34 M (0,67×) | **21,34 M (0,67×)** | Inchangé |
| **Score Global ajusté** | 43,3/100 | **43,3/100** | Inchangé |
| **Score Opportunité** | 3,8/10 | **3,8/10** | Inchangé |
| **Score Momentum** | 4,5/10 | **4,5/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Max Pain (JSON)** | $45,00 (anomalie) | **$65,00** | **Corrigé** 🟡 |
| **Put/Call ratio** | *Absent* | **0,90** | **Rétabli** ✅ |
| **Call OI %** | *Absent* | **52,7 %** | **Rétabli** ✅ |
| **Forward P/E** | −15 142 | **−15 142** | Inchangé |
| **P/B Yahoo** | 27,99× | **27,99×** | Inchangé |
| **EV/Revenue** | 91,92× | **91,92×** | Inchangé |
| **FMP Consensus PT** | $87,19 (16 analysts) | **$87,19 (16 analysts)** | Inchangé |
| **Divergence vs consensus** | +26,3 % | **+26,3 %** | Inchangé |
| **Beta** | 2,499 | **2,499** | Inchangé |
| **MM 50j** | $96,14 | **$96,14** | Inchangé |
| **Earnings Q2 2026** | 59 jours | **59 jours** | Inchangé |

**Verdict** : **Stabilité totale** des cours et des métriques techniques entre les deux snapshots du 8 juin. Le gap −8,23 % séance et le repli cumulé −10,7 % depuis le 03/06 sont confirmés sans amplification. La principale évolution concerne la **résolution partielle de l'anomalie options** : les données Put/Call (0,90) et Call OI (52,7 %) sont rétablies dans `latest.json`. Le Max Pain passe de $45,00 aberrant à $65,00 — moins incohérent mais toujours éloigné du spot ($110,08). Aucune news fondamentale, aucun événement corporate (`events_latest.json` vide).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 42,89 | Neutre-bas. Inchangé vs snapshot 10h. Sorti de la zone neutre haute sans survente (<30). |
| **ATR 14j** | $12,49 | Volatilité élevée stable. Gap −8,23 % contenu dans 0,66× ATR. |
| **MM 50j** | $96,14 | Écart haussier **+14,5 %** vs spot. Tendance haussière structurelle intacte. |
| **Volume 20j** | 31 790 650 | Séance : **21,34 M** — **0,67× moyenne**. Participation modérée, stable. |
| **Beta** | 2,499 | Sensibilité systématique extrême. Amplification des mouvements de marché. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−27,1 %** du 52W high. Éloignement des sommets confirmé. |
| **Range intraday** | $106,73 – $117,98 | Identique au snapshot 10h. Gap down suivi d'un repli intra jusqu'à −12,5 % avant rebond partiel à −8,2 %. |

**Niveaux clés révisés** (inchangés vs snapshot 10h) :
- Support immédiat : **$106,73** (basse intraday 08/06)
- Support technique majeur : **$85,10** (spot − 2×ATR)
- Support confluence : **$90,00** (zone psychologique)
- Résistance immédiate : **$117,98** (haute intraday 08/06)
- Résistance majeure : **$123,32** (close 03/06)
- Objectif haussier : **$147,55** (spot + 3×ATR)

**Structure options — anomalie partiellement résolue** :
- **Max Pain** : **$65,00** (vs $45,00 aberrant au snapshot 10h). Divergence −40,9 % vs spot. Moins incohérent mais reste éloigné ; à interpréter avec prudence.
- **Put/Call ratio** : **0,90** — légère prédominance call dans l'OI.
- **Call OI %** : **52,7 %** — équilibre légèrement call-skewed.
- Expiration la plus proche : **2026-06-12** (4 jours).

**Verdict timing : Défavorable** — Inchangé. Le gap −8,23 % avec volume modéré confirme une distribution active. Le RSI à 42,89 laisse de la marge avant la survente. Le cours > MM50 ($96,14) maintient la tendance haussière structurelle, mais le momentum est fragilisé (Score Momentum 4,5/10).

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-08.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs snapshot 10h |
|---|---|---|
| Market Cap (Yahoo) | **$68,78 Mds** | Inchangé |
| Forward P/E | **−15 142** | Inchangé |
| EV/Revenue | 91,92× | Inchangé |
| P/B (Yahoo) | 27,99× | Inchangé |
| P/S (FMP) | 61,51× | Inchangé |
| Short Interest | 5,81 % | Inchangé |
| **FMP Consensus PT** | **$87,19** (16 analysts) | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($68,78 Mds) vs FMP sous-jacent ($37,02 Mds). Écart de 85,7 % inchangé.

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

**Divergence cours vs consensus** : Spot $110,08 vs PT moyen $87,19 = **+26,3 % au-dessus du consensus sell-side**.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 10h |
|---|---|---|
| **Consensus analystes (FMP)** | $87,19 (16 analysts) | Inchangé |
| **Max Pain (JSON)** | $65,00 | Corrigé depuis $45,00 (anomalie) 🟡 |
| **Put/Call ratio** | 0,90 | **Rétabli** (était absent) ✅ |
| **Call OI %** | 52,7 % | **Rétabli** (était absent) ✅ |
| **Short Interest** | 5,81 % | Inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Structure options rétablie** : Le flux options JSON est désormais complet (Max Pain, Put/Call, Call OI) contrairement au snapshot 10h où les champs étaient partiellement absents/corrompus.
- **Max Pain $65,00** : Bien que moins aberrant que $45,00, cette valeur reste éloignée du spot ($110,08). La proximité de l'expiration (2026-06-12, 4 jours) avec un Max Pain aussi bas suggère soit une concentration d'OI héritée des niveaux antérieurs à la chute, soit une incertitude persistante sur le support à court terme.
- **Put/Call 0,90 + Call OI 52,7 %** : Légère coloration haussière dans l'open interest, insuffisante cependant pour contrebalancer la dégradation technique du Momentum.

**Verdict Sentiment :** Neutre-bas — Inchangé. Aucun upgrade/downgrade détecté, absence totale d'activité retail. La structure options rétablie n'apporte pas de signal directionnel net.

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
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 59j. Consensus PT stable. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 92×, spot +26,3 % vs consensus. Plafonné par FQ ≤3/6. |
| **Momentum** | 4,5/10 | Gap −8,23 % confirmé, RSI 42,89, volume modéré 0,67×. Tendance haussière intacte (prix > MM50) mais fragilisée. |
| **Score Opportunité** | **3,8/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (valorisation extrême + divergence consensus persistante). |
| **Score Global ajusté** | **43,3/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec snapshot 10h** : Le scoring est **intégralement inchangé** (43,3/100). Les seules évolutions concernent la qualité des données options (résolution partielle de l'anomalie), sans impact sur les scores agrégés.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $110,08 | — |
| **Stop-loss** | $85,10 (−22,7 %) | 2×ATR ($12,49) — aligné agent officiel |
| **Take-profit** | $147,55 (+34,0 %) | 3×ATR ($12,49) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Révision vs snapshot 10h** : Inchangés. Les niveaux reflètent la volatilité extrême (Beta 2,50, ATR $12,49).

**Zone d'intérêt potentielle** : Un retour vers **$90–$97** (test support psychologique + confluence 2×ATR) constituerait une zone d'accumulation technique intéressante pour les spéculateurs, sous réserve de confirmation de volume.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **59 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-12 | **4 jours** | Max Pain JSON $65,00 (à interpréter avec prudence) |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 12 juin pourrait amplifier la volatilité à court terme compte tenu du Max Pain éloigné du spot.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — STABILITÉ TOTALE, ANOMALIE OPTIONS PARTIELLEMENT RÉSOLUE**

Le snapshot du 13h UTC confirme intégralement la thèse du snapshot 10h UTC :

1. ✅ **Cours stable** — $110,08 inchangé. Aucun nouveau gap ni mouvement significatif entre 10h et 13h UTC.
2. ✅ **Anomalie options partiellement résolue** — Put/Call (0,90) et Call OI (52,7 %) rétablis. Le Max Pain passe de $45,00 aberrant à $65,00 (moins incohérent mais toujours éloigné du spot).
3. ✅ **Métriques techniques stables** — RSI 42,89, ATR $12,49, MM50 $96,14, volume 0,67× inchangés.
4. ✅ **Fondamentaux inchangés** — Forward P/E −15 142, EV/Rev 92×, Filtre Qualité 3/6, consensus PT $87,19 stable.
5. ✅ **Scoring inchangé** — Score Global ajusté 43,3/100 (SURVEILLER).
6. ✅ **Niveaux SL/TP inchangés** — SL $85,10, TP $147,55, R/R 1,5:1.
7. ✅ **Aucune news fondamentale** ni événement corporate détecté.
8. 🟡 **Max Pain $65,00** — reste distant du spot ($110,08). À traiter avec prudence jusqu'à validation avec source tierce.

**Recommandation** : Maintenir la posture **SURVEILLER**. Le setup technique reste identique. La résolution de l'anomalie options renforce légèrement la fiabilité des données sans modifier la thèse. La vigilance reste de mise sur le support $85–$90 (2×ATR) en cas de poursuite de la distribution.

Attendre :
- Un **retour vers la zone $90–$97** avec **volume supérieur à la moyenne** (confirmation de capitulation), ou
- Une **stabilisation au-dessus de $117,98** (haute du 08/06) avec volume croissant pour confirmer un rebond.

Toute position longue actuelle expose à un drawdown de −22,7 % (SL) en 1–2 séances compte tenu du Beta 2,50 et de l'ATR $12,49. Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel.

---

*Rapport généré le 2026-06-08 — Données : `data/latest.json` (13:00 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/quant_report_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
