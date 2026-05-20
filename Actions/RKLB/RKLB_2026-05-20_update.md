# RKLB — Mise à Jour Snapshot 13:00 UTC (2026-05-20)

> Source : `data/latest.json` (2026-05-20T13:00:13 UTC) | `data/recommandations_latest.json` (2026-05-20) | Validation OK (22/25 tickers OK, RKLB non signalé)
> **Snapshot pré-market US** — Cours = close officiel du 19 mai 2026.

---

## 1. Résumé des Changements depuis l'Analyse Précédente

| Métrique | 2026-05-20 (10:00 UTC) | 2026-05-20 (13:00 UTC) | Variation |
|---|---|---|---|
| **Cours close** | $127,31 | **$127,31** | **0,00 %** — inchangé |
| **Change % vs veille** | –2,94 % | **–2,94 %** | **Inchangé** |
| **RSI 14j** | 76,14 | **76,14** | **Inchangé** |
| **ATR 14j** | $11,09 | **$11,09** | **Inchangé** |
| **MM 50j** | $81,58 | **$81,58** | **Inchangé** |
| **Volume séance** | 29,996 M (1,12×) | **29,996 M** (1,12×) | **Stable** |
| **Market Cap (Yahoo)** | $73,68 Mds | **$73,68 Mds** | **Inchangé** |
| **Forward P/E** | –14 942 | **–14 942** | **Inchangé** |
| **P/B (Yahoo)** | 40,19× | **40,19×** | **Inchangé** |
| **Consensus PT (FMP)** | $84,20 | **$84,20** | **Inchangé** |
| **Score Global Agent** | 39,5/100 (aj. 29,5) | **39,5/100** (aj. **29,5**) | **Inchangé** |
| **Action Agent** | ÉVITER | **ÉVITER** | **Inchangée** |
| **Max Pain** | $45,00 [ANOMALIE] | **$150,00** | **✅ RÉSOLU** |
| **Put/Call ratio** | null [DONNÉES MANQUANTES] | **0,85** | **✅ RÉSOLU** |
| **Call OI %** | null [DONNÉES MANQUANTES] | **54,0 %** | **✅ RÉSOLU** |

**Verdict** : Aucune variation de cours ni de données fondamentales/techniques entre le snapshot 10h UTC et 13h UTC. **Seule évolution : résolution de l'anomalie data options** détectée ce matin. Le flux Yahoo Finance options a été rétabli : Max Pain retourne à $150,00 (cohérent avec le close du 19/05), Put/Call à 0,85 et Call OI à 54,0 %. Ces valeurs restent la référence opérationnelle. Configuration globale inchangée.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 76,14 | Surachat persistant (>70). Aucun refroidissement. |
| **ATR 14j** | $11,09 | Volatilité stable. Range intraday du 19/05 = $115,23–$129,57 (12,4 %). |
| **MM 50j** | $81,58 | Écart haussier **+56,1 %** vs spot. Tendance étendue inchangée. |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume 20j** | 26 666 841 | Dernière séance 1,12× moyenne — pas de distribution massive. |
| **Beta** | 2,313 | Sensibilité systématique extrême. |
| **52W High / Low** | $138,38 / $23,92 | Spot à **–8,0 %** du 52W high. |
| **Short Interest** | 5,79 % | Élevé ; squeeze possible si catalyseur — absent pour l'instant. |

**Niveaux clés (inchangés)** :
- Support immédiat : **$115,23** (basse intraday 19/05) — tenu
- Support technique majeur : **$105,13** (spot – 2×ATR)
- Résistance immédiate : **$129,57** (haute intraday 19/05) / **$131,16** (close 18/05)
- Résistance / Objectif : **$160,58** (spot + 3×ATR)
- Confluence technique : $80–$95 (zone MM50j + compression historique)
- **Max Pain** (éch. 2026-05-22) : **$150,00** (restauré à 13h UTC) — spot $127,31 en dessous de **15,1 %**

**Verdict timing : Défavorable** — Pas de changement de configuration. RSI > 76, écart MM50 > 56 %, absence de signal de retournement. Attendre un retour sous RSI 70 ou un test de la zone $110–$115.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale depuis le snapshot 10h UTC.

| Métrique | Valeur | Source |
|---|---|---|
| Market Cap (Yahoo) | **$73,68 Mds** | Yahoo Finance |
| Forward P/E | **–14 942** | Yahoo Finance |
| EV/Revenue | 104,43× | Yahoo Finance |
| EV/EBITDA | –430,54× | Yahoo Finance |
| P/B (Yahoo) | **40,19×** | Yahoo Finance |
| P/B (FMP) | 21,50× | FMP Stable API |
| P/S (FMP) | 61,51× | FMP Stable API |
| Short Interest | 5,79 % | Yahoo Finance |
| **FMP Consensus PT** | **$84,20** (15 analysts) | FMP Stable API |
| **FMP Gross Margin** | 34,4 % | FMP Stable API |
| **FMP Operating Margin** | –38,0 % | FMP Stable API |
| **FMP EBITDA Margin** | –25,8 % | FMP Stable API |
| **FMP Net Margin** | –32,9 % | FMP Stable API |
| **FMP Debt/Equity** | 0,15 | FMP Stable API |
| **FMP Current Ratio** | 4,08 | FMP Stable API |
| **FMP Interest Coverage** | –8,64× | FMP Stable API (négatif) |

**[ANOMALIE DONNÉES PERSISTANTE]** — Divergence Market Cap Yahoo ($73,68 Mds) vs FMP sous-jacent ($37,02 Mds) maintenue. Les ratios FMP (P/B 21,50×, P/S 61,51×) restent indicatifs.

**Filtre Qualité (6 critères) — inchangé** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Croissance du segment spatial / lanceurs. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif abyssal ; pertes persistantes. |
| 3. Assets/Liabilities > 1,0 | ✅ Oui | Current Ratio 4,08 ; liquidité solide. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | FCF yield négatif ; pas de génération de cash rentable. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique (lanceurs réutilisables légers), concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion rapide. |

**Score Qualité total : 3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $127,31 vs PT moyen $84,20 = **+51,2 % au-dessus du consensus sell-side**. Écart inchangé.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts, 3 ce mois, 5 ce trimestre) | Inchangé |
| **Put/Call ratio** | **0,85** | ✅ **RÉSOLU** — restauré depuis null (10h UTC) |
| **Call OI %** | **54,0 %** | ✅ **RÉSOLU** — restauré depuis null (10h UTC) |
| **Max Pain (snapshot)** | **$150,00** | ✅ **RÉSOLU** — restauré depuis $45,00 aberrant (10h UTC) |
| **Short Interest** | 5,79 % | Inchangé |
| **News du jour** | Aucune | `data/news_2026-05-20.json` vide pour RKLB. |
| **Social Sentiment** | 0 mentions, score 0/10 | `data/social_sentiment_2026-05-20.json` — aucune activité retail. |
| **NLP Transcripts** | Indisponible | Plan FMP Starter — transcripts require Enterprise+. |

**Verdict Sentiment :** Neutre / Légèrement baissier — Les flux options étant désormais rétablis, les métriques de référence sont : Max Pain $150,00 (éch. 22/05), Put/Call 0,85, Call OI 54,0 %. Le Put/Call < 1 indique une légère inclination call-biased (54 % Call OI), ce qui est cohérent avec la surchauffe technique observée. Spot $127,31 reste sous le Max Pain de 15,1 %, ce qui est favorable aux détenteurs de puts mais ne constitue pas un catalyseur directionnel en l'absence de volume options anormal. Aucun upgrade/downgrade détecté.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `null`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Non flaggé dans `geo_risk_latest.json`. | Aucun malus. |
| **Comptable (Accounting)** | `data/accounting_risk_latest.json` non disponible. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum 0,0, sous-performe SPY 20j/60j. | Malus sectoriel implicite — RKLB dans un secteur sans momentum. |
| **FX Exposure** | Score FX Impact 0,0. Exposition 25 % export, divergence aligned. | Aucun malus/bonus FX. |
| **Event-Driven** | Aucun événement corporate détecté dans `events_latest.json`. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le 2026-08-06 (**78 jours**). Est EPS –$0,06 à –$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 78j — trop loin. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 104×, spot +51 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 5,0/10 | Tendance haussière structurelle intacte (prix > MM50), mais RSI surachat 76,14 persistant. |
| **Score Opportunité** | **4,0/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | –10 pts | Malus structurel (surchauffe technique + divergence consensus + absence de catalyseur). |
| **Score Global ajusté** | **29,5/100** | **ÉVITER** — Seuil < 35 |

**Rappel de la règle de disqualification** : Score Valorisation ≤ 2/10 → action exclue du rapport long. Ici Val = 3,0/10 — le titre reste dans le rapport mais avec recommandation ÉVITER.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $127,31 | — |
| **Stop-loss** | $105,13 (–17,4 %) | 2×ATR ($11,09) — aligné avec l'agent officiel |
| **Take-profit** | $160,58 (+26,1 %) | 3×ATR ($11,09) — aligné avec l'agent officiel |
| **Ratio R/R** | **1,5 : 1** | **Inférieur au seuil minimum 2:1** pour un trade directionnel à haut beta |

> **Révision** : Les niveaux sont inchangés car le spot et l'ATR n'ont pas varié. Le ratio R/R reste figé à 1,5:1, toujours défavorable compte tenu du Beta 2,31. Toute position longue expose à un drawdown de –17,4 % en 1–2 séances.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **78 jours** | Est EPS : –$0,06 à –$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-05-22 | **2 jours** | Max Pain $150,00 — spot en dessous de 15,1 % |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 22 mai approche dans 2 jours. La convergence vers $150 reste improbable. Surveillance si activité options inhabituelle en fin de semaine — **flux options désormais rétabli**, données opérationnelles à suivre.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER**

Le snapshot 13h UTC du 20 mai 2026 ne fait que **confirmer l'analyse du matin** : aucune donnée de cours ni fondamentale n'a varié. Le seul changement est la **résolution de l'anomalie data options** (Max Pain, Put/Call, Call OI restaurés). Cette correction ne modifie en rien la thèse opérationnelle.

**Éléments clés vs analyse précédente (10h UTC)** :
1. **Cours stable à $127,31** — pas de mouvement post-séance ni pre-market significatif.
2. **Données techniques inchangées** — RSI, ATR, MM50, volume identiques.
3. **✅ Anomalie options RÉSOLUE** — Max Pain $150,00 (vs $45,00 aberrant ce matin), Put/Call 0,85, Call OI 54,0 %. Flux Yahoo Finance rétabli.
4. **Aucune news** — `data/news_2026-05-20.json` vide. Mouvement purement technique/options-driven confirmé.
5. **Score agent inchangé** : 39,5/100 (aj. 29,5) — ÉVITER maintenu.
6. **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
7. **Sector rotation défavorable** — XLI sans momentum, sous-performe SPY.

**Recommandation** : Maintenir la posture **ÉVITER**. La correction des données options n'apporte aucun élément nouveau susceptible de modifier la thèse. Le support $115 a tenu le 19/05 mais reste fragile sous RSI 76. Attendre :
- Un **retour vers la zone de confluence $80–$95** (proximité MM50j et compression technique), ou
- Une **inflexion matérielle des anticipations de résultats** (guidance positive, contrat majeur, etc.), ou
- Un **refroidissement technique** (RSI < 70 sur plusieurs séances) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de –17,4 % (SL) en 1–2 séances compte tenu de l'ATR $11,09 et du Beta 2,31.

---

*Rapport généré le 2026-05-20 — Données : `data/latest.json` (2026-05-20T13:00:13), `data/recommandations_latest.json` (2026-05-20), `data/upcoming_events_latest.json` (2026-05-20), `data/events_latest.json` (2026-05-20), `data/news_2026-05-20.json`, `data/social_sentiment_2026-05-20.json`, `data/geo_risk_latest.json` (2026-05-17), `data/sector_rotation_latest.json` (2026-05-20), `data/fx_exposure_latest.json` (2026-05-20), `data/quant_report_latest.json` (2026-05-17)*
