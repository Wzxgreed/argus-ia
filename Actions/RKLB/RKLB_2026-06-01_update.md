# RKLB — Mise à Jour Snapshot 13:00 UTC (2026-06-01)

> Source : `data/2026-06-01.json` (fetched 2026-06-01T13:00:15 UTC) | `data/recommandations_2026-06-01.json` | Close officiel US du 2026-05-30

---

## 1. Résumé des Changements depuis l'Analyse Précédente (Snapshot 10:00 UTC)

| Métrique | Snapshot 10h (01/06) | Snapshot 13h (01/06) | Variation |
|---|---|---|---|
| **Cours close** | $143,48 | **$143,48** | Inchangé |
| **Change % vs veille** | -3,07 % | **-3,07 %** | Inchangé |
| **RSI 14j** | 70,56 | **70,56** | Inchangé |
| **ATR 14j** | $12,37 | **$12,37** | Inchangé |
| **Volume séance** | 34,82 M (1,15×) | **34,82 M (1,15×)** | Inchangé |
| **Market Cap (Yahoo)** | $83,06 Mds | **$83,06 Mds** | Inchangé |
| **Forward P/E** | –13 020 | **–13 020** | Inchangé |
| **EV/Revenue** | 120,36× | **120,36×** | Inchangé |
| **P/B (Yahoo)** | 36,48× | **36,48×** | Inchangé |
| **52W High** | $151,00 | **$151,00** | Inchangé |
| **Consensus PT (FMP)** | $84,20 | **$84,20** | Inchangé |
| **Score Global Agent** | 38,3/100 (aj. 28,3) | **38,3/100** (aj. **28,3**) | ÉVITER maintenu |
| **Max Pain** | $45,00 (anomalie) | **$90,00** | ✅ **DONNÉES OPTIONS RÉTABLIES** |
| **Put/Call ratio** | null | **1,25** | ✅ **FLUX RÉTABLI** |
| **Call OI %** | null | **44,4 %** | ✅ **FLUX RÉTABLI** |
| **Short Interest** | 5,81 % | **5,81 %** | Stable |

**Verdict** : Le snapshot 13:00 UTC confirme l'ensemble des données de cours et de technique du snapshot 10:00 UTC. L'évolution majeure concerne la **correction des données options** dans `data/2026-06-01.json` : le Max Pain passe d'une valeur aberrante ($45,00) à **$90,00**, le Put/Call ratio est rétabli à **1,25** et le Call OI à **44,4 %**. Ces valeurs sont cohérentes avec le contexte du cours ($143,48) et valident la structure baissière à très court terme détectée précédemment (Max Pain $90,00 << spot $143,48 = forte pression baissière vers le strike de plus grande pain). La thèse **ÉVITER** est **confirmée et renforcée** par cette résolution d'anomalie.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 70,56 | 🔴 **Surachat** (>70). Refroidissement de -6,91 pts vs 27/05. Persistance dans la zone de surachat. |
| **ATR 14j** | $12,37 | Volatilité en contraction (-6,1 % vs 27/05). Range intraday 01/06 = $134,05–$144,00 (6,9 %). |
| **MM 50j** | $91,25 | Écart haussier **+57,2 %** vs spot. Tendance haussière structurelle intacte mais éloignement excessif. |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume 20j** | 30 184 210 | Séance 01/06 : **34,82 M** — **1,15× moyenne**. Repli sur volume élevé = distribution. |
| **Beta** | 2,313 | Sensibilité systématique extrême. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **-5,0 %** du 52W high. Extension parabolique intacte malgré le repli. |
| **Short Interest** | 5,81 % | Stable. Élevé ; squeeze possible si catalyseur, non déclenché. |

**Niveaux clés révisés** (ATR contracté) :
- Support immédiat : **$134,05** (basse intraday 01/06)
- Support technique majeur : **$118,74** (spot – 2×ATR) — aligné agent officiel
- Résistance immédiate : **$144,00** (haute intraday 01/06)
- Résistance / Objectif : **$180,59** (spot + 3×ATR) — aligné agent officiel
- Confluence technique : $80–$95 (zone MM50j — éloignée de –36 %)
- **Max Pain** (éch. 2026-06-05) : **$90,00** — ✅ corrigé, cohérent vs spot

**Verdict timing : Défavorable** — Configuration inchangée vs 10h. RSI > 70, écart MM50 > 57 %, repli sur volume 1,15× = distribution. La probabilité d'un retour de manivelle vers la zone $120–$130 s'accroît avec ce signal de vente sur volume.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-01.json` vide pour RKLB. `data/events_2026-06-01.json` vide.

| Métrique | Valeur | Source | Évolution vs 27/05 |
|---|---|---|---|
| Market Cap (Yahoo) | **$83,06 Mds** | Yahoo Finance | -3,9 % |
| Forward P/E | **–13 020** | Yahoo Finance | Négatif, magnitude réduite |
| EV/Revenue | 120,36× | Yahoo Finance | Stable |
| EV/EBITDA | –496,23× | Yahoo Finance | Stable en magnitude |
| P/B (Yahoo) | **36,48×** | Yahoo Finance | -3,9 % |
| P/B (FMP) | 21,50× | FMP Stable API | Inchangé |
| P/S (FMP) | 61,51× | FMP Stable API | Inchangé |
| Short Interest | 5,81 % | Yahoo Finance | +0,02 pts |
| **FMP Consensus PT** | **$84,20** (15 analysts, 2 ce mois, 5 ce trimestre) | FMP Stable API | Inchangé |
| **FMP Gross Margin** | 34,4 % | FMP Stable API | Inchangé |
| **FMP Operating Margin** | –38,0 % | FMP Stable API | Inchangé |
| **FMP Net Margin** | –32,9 % | FMP Stable API | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($83,06 Mds) vs FMP sous-jacent ($37,02 Mds) maintenue. Les ratios FMP restent les références opérationnelles.

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

**Divergence cours vs consensus** : Spot $143,48 vs PT moyen $84,20 = **+70,4 % au-dessus du consensus sell-side** (vs +77,4 % au 27/05).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 10h |
|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts) | Inchangé |
| **Put/Call ratio** | **1,25** | ✅ **RÉTABLI** — structure baissière à CT (put > call) |
| **Call OI %** | **44,4 %** | ✅ **RÉTABLI** — légère dominance calls |
| **Max Pain** | **$90,00** | ✅ **CORRIGÉ** — cohérent vs spot $143,48 |
| **Short Interest** | 5,81 % | Stable |
| **News du jour** | Aucune | `data/news_2026-06-01.json` vide pour RKLB. |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail. |
| **NLP Transcripts** | Indisponible | Plan FMP Starter. |

**Analyse options (données corrigées)** :
- **Max Pain $90,00** (éch. 2026-06-05) : valeur désormais cohérente avec le cours $143,48. Le spread spot vs Max Pain est de **+$53,48 (+59,4 %)**. Cette divergence extrême entre le cours et le niveau de maximum pain indique une **forte pression baissière** des options pour l'expiration du 5 juin : le marché options anticipe un retour vers la zone $90,00 d'ici vendredi.
- **Put/Call 1,25** : les puts dominent légèrement les calls. Structure baissière à très court terme confirmée.
- **Call OI 44,4 %** : les détenteurs de calls sont minoritaires en OI. Peu de conviction haussière institutionnelle à CT.
- **Synthèse options** : La correction des données confirme une structure options **baissière à très court terme** (Max Pain $90,00 << spot, Put/Call > 1). L'expiration du 5 juin est dans 4 jours ouvrés et constitue un catalyseur technique de potentielle volatilité.

**Verdict Sentiment :** Légèrement baissier — Aucun upgrade/downgrade. Aucune news. Absence totale d'activité retail. La structure options corrigée renforce le signal baissier à CT. Le repli de -3,07 % sur volume 1,15× reste le signal informationnel dominant de la séance.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0, date 2026-06-01). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Non flaggé dans `geo_risk_2026-06-01.json`. Score Politique 2/10. | Aucun malus. |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) return 20j -0,83 %, sous-performe SPY (RS -6,09 % / -12,05 %). Momentum score 0,0. | Malus sectoriel implicite. |
| **FX Exposure** | Score FX Impact 0,0. Exposition 25 % export, divergence aligned. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate dans `events_2026-06-01.json`. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**66 jours**). Est EPS –$0,06 à –$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 66j — trop loin. Structure options baissière à CT (Max Pain $90). |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 120×, spot +70,4 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 4,5/10 | Tendance haussière structurelle intacte (prix > MM50), nouveau 52W high $151,00, mais RSI surachat 70,56 et repli -3,07 % sur volume élevé = distribution. |
| **Score Opportunité** | **3,8/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | –10 pts | Malus structurel (surchauffe technique + divergence consensus + absence de catalyseur + signal distribution + pression options CT). |
| **Score Global ajusté** | **28,3/100** | **ÉVITER** — Seuil < 35 |

**Règle de disqualification** : Score Valorisation ≤ 2/10 → action exclue du rapport long. Ici Val = 3,0/10 — le titre reste dans le rapport mais avec recommandation ÉVITER.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $143,48 | — |
| **Stop-loss** | $118,74 (–17,2 %) | 2×ATR ($12,37) — aligné agent officiel |
| **Take-profit** | $180,59 (+25,9 %) | 3×ATR ($12,37) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | **Inférieur au seuil minimum 2:1** pour un trade directionnel à haut beta |

> **Révision** : Niveaux inchangés vs snapshot 10h. Le SL expose à un drawdown de –17,2 % en 1–2 séances compte tenu du Beta 2,31 et de l'ATR $12,37.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **66 jours** | Est EPS : –$0,06 à –$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-05 | **4 jours ouvrés** | Max Pain **$90,00** — pression baissière majeure vs spot $143,48 |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 5 juin approche dans 4 jours avec un Max Pain $90,00, soit **$53,48 sous le spot**. Cette divergence constitue un risque technique de volatilité à la baisse d'ici vendredi.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER — SIGNAL DE DISTRIBUTION + PRESSION OPTIONS CT**

Le snapshot 13:00 UTC du 1er juin 2026 confirme l'ensemble de la configuration du snapshot 10:00 UTC et l'enrichit par la **correction des données options**. Le Max Pain est désormais établi à **$90,00** (vs spot $143,48), le Put/Call à **1,25** et le Call OI à **44,4 %**.

**Éléments clés vs analyse précédente (snapshot 10h)** :
1. **Cours, RSI, ATR, volume inchangés** — repli -3,07 % à $143,48 confirmé.
2. **✅ DONNÉES OPTIONS RÉTABLIES** : Max Pain $90,00 (vs $45,00 aberrant), Put/Call 1,25 (vs null), Call OI 44,4 % (vs null).
3. **Structure options baissière à CT** : Max Pain $90,00 << spot = forte pression vers la baisse avant expiration vendredi.
4. **RSI 70,56** — refroidissement mais persistance en surachat.
5. **Volume 34,82 M (1,15×)** — distribution confirmée.
6. **52W high $151,00** — nouveau record suivi de repli immédiat.
7. **Divergence consensus +70,4 %** (spot vs PT $84,20) — valorisation massivement déconnectée.
8. **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
9. **Score global 38,3/100 (aj. 28,3)** — ÉVITER maintenu.
10. **Sector rotation défavorable** — XLI sans momentum, sous-performe SPY 20j/60j.
11. **Aucune news** — mouvement purement technique/options.

**Recommandation** : Maintenir la posture **ÉVITER**. La résolution de l'anomalie options renforce l'hypothèse d'une pression baissière à très court terme. Le Max Pain $90,00 pour l'expiration du 5 juin constitue un catalyseur technique de volatilité négative.

Attendre :
- Un **retour vers la zone de confluence $118–$130** (test de support + zone proche du Max Pain historique), ou
- Un **refroidissement technique complet** (RSI < 60 sur plusieurs séances + volume décroissant), ou
- Une **inflexion matérielle des anticipations** (guidance positive, contrat majeur, etc.) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de –17,2 % (SL) en 1–2 séances compte tenu de l'ATR $12,37 et du Beta 2,31. Le risque options CT (Max Pain $90,00) aggrave ce profil.

---

*Rapport généré le 2026-06-01 — Données : `data/2026-06-01.json` (13:00 UTC), `data/recommandations_2026-06-01.json`, `data/upcoming_events_2026-06-01.json`, `data/events_2026-06-01.json`, `data/news_2026-06-01.json`, `data/social_sentiment_2026-06-01.json`, `data/geo_risk_2026-06-01.json`, `data/sector_rotation_2026-06-01.json`, `data/fx_exposure_2026-06-01.json`, `data/quant_2026-06-01.json`*
