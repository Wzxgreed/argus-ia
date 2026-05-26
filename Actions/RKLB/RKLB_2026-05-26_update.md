# RKLB — Mise à Jour Snapshot 13:00 UTC (2026-05-26)

> Source : `data/latest.json` (fetched 2026-05-26T13:00:13 UTC) | `data/recommandations_latest.json` | Marché US non ouvert à 13:00 UTC (ouverture 13:30 UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente

| Métrique | Snapshot 10:00 UTC 26/05 | Snapshot 13:00 UTC 26/05 | Variation |
|---|---|---|---|
| **Cours close** | $135,76 | **$135,76** | **0,00 %** — stabilité totale |
| **Change % vs veille** | +8,22 % | **+8,22 %** | Inchangé |
| **RSI 14j** | 74,84 | **74,84** | Inchangé — surachat persistant |
| **ATR 14j** | $12,41 | **$12,41** | Inchangé |
| **MM 50j** | $85,31 | **$85,31** | Inchangé |
| **Volume séance** | 32,862 M (1,18×) | **32,862 M** (1,18×) | Inchangé |
| **Market Cap (Yahoo)** | $78,59 Mds | **$78,59 Mds** | Inchangé |
| **Forward P/E** | –12 319 | **–12 319** | Inchangé |
| **EV/Revenue** | 113,79× | **113,79×** | Inchangé |
| **P/B (Yahoo)** | 34,52× | **34,52×** | Inchangé |
| **Consensus PT (FMP)** | $84,20 | **$84,20** | Inchangé — divergence +61,3 % |
| **Score Global Agent** | 40,8/100 (aj. 30,8) | **40,8/100** (aj. **30,8**) | Inchangé — ÉVITER |
| **Max Pain** | $45,00 [ANOMALIE] | **$130,00** | 🟢 **ANOMALIE RÉSOLUE** |
| **Put/Call ratio** | null [ANOMALIE] | **1,08** | 🟢 **ANOMALIE RÉSOLUE** |
| **Call OI %** | null [ANOMALIE] | **48,1 %** | 🟢 **ANOMALIE RÉSOLUE** |

**Verdict** : Snapshot 13:00 UTC du 26 mai 2026 = stabilité totale des données de cours vs snapshot 10:00 UTC (marché US non ouvert à 13:00 UTC). **La résolution de l'anomalie options JSON est le seul événement significatif** : Max Pain rétabli à $130,00, Put/Call à 1,08, Call OI à 48,1 %. La thèse **ÉVITER** est confirmée sans modification.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 74,84 | Surachat persistant (>70). Aucun refroidissement. |
| **ATR 14j** | $12,41 | Volatilité stable. Range intraday 25/05 = $131,31–$139,76 (6,0 %). |
| **MM 50j** | $85,31 | Écart haussier **+59,2 %** vs spot. Tendance étendue au maximum. |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume 20j** | 27 765 260 | Dernière séance 1,18× moyenne. |
| **Beta** | 2,313 | Sensibilité systématique extrême. |
| **52W High / Low** | $139,76 / $25,24 | Spot à **–2,9 %** du 52W high. |
| **Short Interest** | 5,79 % | Stable. Élevé ; squeeze possible si catalyseur. |

**Niveaux clés révisés** (inchangés vs 10:00 UTC) :
- Support immédiat : **$131,31** (basse intraday 25/05)
- Support technique majeur : **$110,94** (spot – 2×ATR)
- Résistance immédiate : **$139,76** (haute intraday 25/05, 52W high)
- Résistance / Objectif : **$172,99** (spot + 3×ATR)
- Confluence technique : $80–$95 (zone MM50j — éloignée de –33 %)
- **Max Pain** (éch. 2026-05-29) : **$130,00** — rétabli, écart –4,2 % vs spot

**Verdict timing : Défavorable** — Configuration inchangée. RSI > 74, écart MM50 > 59 %, ATR stable en zone élevée. Aucun signal de retournement.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale. Snapshot pre-market 13:00 UTC.

| Métrique | Valeur | Source | Évolution vs 10:00 UTC |
|---|---|---|---|
| Market Cap (Yahoo) | **$78,59 Mds** | Yahoo Finance | Inchangé |
| Forward P/E | **–12 319** | Yahoo Finance | Inchangé |
| EV/Revenue | 113,79× | Yahoo Finance | Inchangé |
| EV/EBITDA | –469,13× | Yahoo Finance | Inchangé |
| P/B (Yahoo) | **34,52×** | Yahoo Finance | Inchangé |
| P/B (FMP) | 21,50× | FMP Stable API | Inchangé |
| P/S (FMP) | 61,51× | FMP Stable API | Inchangé |
| Short Interest | 5,79 % | Yahoo Finance | Inchangé |
| **FMP Consensus PT** | **$84,20** (15 analysts, 2 ce mois, 5 ce trimestre) | FMP Stable API | Inchangé |
| **FMP Gross Margin** | 34,4 % | FMP Stable API | Inchangé |
| **FMP Operating Margin** | –38,0 % | FMP Stable API | Inchangé |
| **FMP Net Margin** | –32,9 % | FMP Stable API | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($78,59 Mds) vs FMP sous-jacent ($37,02 Mds) maintenue. Les ratios FMP restent les références opérationnelles.

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

**Divergence cours vs consensus** : Spot $135,76 vs PT moyen $84,20 = **+61,3 % au-dessus du consensus sell-side**.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 10:00 UTC |
|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts) | Inchangé |
| **Put/Call ratio** | **1,08** | 🟢 **RÉSOLU** — flux restauré (était null) |
| **Call OI %** | **48,1 %** | 🟢 **RÉSOLU** — flux restauré (était null) |
| **Max Pain (snapshot)** | **$130,00** | 🟢 **RÉSOLU** — rétabli depuis $45,00 anomalie |
| **Short Interest** | 5,79 % | Inchangé |
| **News du jour** | Aucune | `data/news_2026-05-26.json` vide pour RKLB. |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail. |
| **NLP Transcripts** | Indisponible | Plan FMP Starter. |

**Analyse options post-résolution** :
- **Max Pain $130,00** (éch. 2026-05-29, **3 jours**) : écart –4,2 % vs spot $135,76. Le marché options price un pin proche de $130, légèrement sous le spot actuel. Avec 3 jours avant expiration, la pression de pin risque de tirer le cours vers $130.
- **Put/Call 1,08** : léger biais put (ratio > 1,0). Les détenteurs d'options privilégient légèrement la protection à la hausse.
- **Call OI 48,1 %** : < 50 %, confirmant un léger biais baissier dans l'open interest.
- **Synthèse options** : configuration légèrement baissière à très courte échéance (3 jours). Le pin $130 est un niveau de support psychologique actif.

**Verdict Sentiment :** Neutre / Légèrement baissier — La résolution des données options révèle un biais put modéré et un pin $130 proche du spot. Aucun support call massif n'est détecté. Aucun upgrade/downgrade. Aucune news. Le mouvement du 25 mai reste purement technique/momentum sans support informationnel.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `null`, n=0, date 2026-05-17). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Non flaggé dans `geo_risk_latest.json` (2026-05-17). | Aucun malus. |
| **Comptable (Accounting)** | `data/accounting_risk_latest.json` non disponible. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum 0,0, sous-performe SPY 20j/60j (RS –4,85 % / –10,99 %). | Malus sectoriel implicite. |
| **FX Exposure** | Score FX Impact 0,0. Exposition 25 % export, divergence aligned. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate dans `events_2026-05-26.json`. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**72 jours**). Est EPS –$0,06 à –$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 72j — trop loin. Gap haussier non expliqué fondamentalement. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 114×, spot +61 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 5,5/10 | Tendance haussière structurelle intacte (prix > MM50), nouveau 52W high, mais RSI surachat 74,84. |
| **Score Opportunité** | **4,1/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | –10 pts | Malus structurel (surchauffe technique + divergence consensus + absence de catalyseur). |
| **Score Global ajusté** | **30,8/100** | **ÉVITER** — Seuil < 35 |

**Règle de disqualification** : Score Valorisation ≤ 2/10 → action exclue du rapport long. Ici Val = 3,0/10 — le titre reste dans le rapport mais avec recommandation ÉVITER.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $135,76 | — |
| **Stop-loss** | $110,94 (–18,3 %) | 2×ATR ($12,41) — aligné agent officiel |
| **Take-profit** | $172,99 (+27,4 %) | 3×ATR ($12,41) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | **Inférieur au seuil minimum 2:1** pour un trade directionnel à haut beta |

> **Révision** : Niveaux inchangés vs snapshot 10:00 UTC (données identiques). Le SL expose à un drawdown de –18,3 % en 1–2 séances compte tenu du Beta 2,31 et de l'ATR $12,41.

**Niveau de pin options** : Max Pain $130,00 (éch. 2026-05-29) constitue un support psychologique très proche du spot (–4,2 %). Si le cours casse sous $130 avant expiration, la pression gamma put pourrait amplifier le mouvement baissier.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **72 jours** | Est EPS : –$0,06 à –$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-05-29 | **3 jours** | Max Pain $130,00 — pin actif, biais put léger |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 29 mai approche dans 3 jours avec un pin $130 légèrement sous le spot.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER**

Le snapshot 13:00 UTC du 26 mai 2026 confirme la **stabilité totale** des données de cours vs le snapshot 10:00 UTC. Le marché US n'avait pas encore ouvert à 13:00 UTC — aucune nouvelle cotation, aucune news, aucun mouvement.

**La seule évolution significative est la résolution de l'anomalie options JSON** :
- **Max Pain rétabli à $130,00** (vs $45,00 anomalie précédente) — cohérent avec le spot $135,76.
- **Put/Call 1,08** — léger biais put, flux restauré.
- **Call OI 48,1 %** — biais call neutralisé, flux restauré.

**Éléments clés vs analyse précédente (10:00 UTC)** :
1. **Cours stable à $135,76** — identique au snapshot 10:00 UTC.
2. **Données techniques inchangées** — RSI 74,84, ATR $12,41, MM50 $85,31.
3. **Données fondamentales inchangées** — aucun nouvel événement structurant.
4. **Score agent inchangé** : 40,8/100 (aj. 30,8) — ÉVITER maintenu.
5. **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
6. **🟢 [ANOMALIE RÉSOLUE]** Données options JSON corrigées : Max Pain $130,00, Put/Call 1,08, Call OI 48,1 %.
7. **Sector rotation défavorable** — XLI sans momentum, sous-performe SPY 20j/60j.
8. **Aucune news** — mouvement purement technique confirmé.
9. **Pin options** : Max Pain $130,00 dans 3 jours — légèrement sous le spot, pression de rappel possible.

**Recommandation** : Maintenir la posture **ÉVITER**. La stabilité des données renforce la confiance dans la thèse opérationnelle : aucun catalyseur fondamental, valorisation déconnectée, surchauffe technique extrême. La résolution des données options révèle en outre un léger biais put et un pin $130 proche du spot, ce qui ne constitue pas un signal haussier.

Attendre :
- Un **retour vers la zone de confluence $110–$120** (gap fill + test de support), ou
- Une **inflexion matérielle des anticipations de résultats** (guidance positive, contrat majeur, etc.), ou
- Un **refroidissement technique** (RSI < 70 sur plusieurs séances + volume décroissant) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de –18,3 % (SL) en 1–2 séances compte tenu de l'ATR $12,41 et du Beta 2,31.

---

*Rapport généré le 2026-05-26 — Données : `data/latest.json` (13:00 UTC), `data/recommandations_2026-05-26.json`, `data/upcoming_events_2026-05-26.json`, `data/events_2026-05-26.json`, `data/news_2026-05-26.json`, `data/social_sentiment_2026-05-26.json`, `data/geo_risk_latest.json` (2026-05-17), `data/sector_rotation_2026-05-26.json`, `data/fx_exposure_2026-05-26.json`, `data/quant_report_latest.json` (2026-05-17)*
