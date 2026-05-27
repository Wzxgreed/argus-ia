# RKLB — Mise à Jour Snapshot 13:00 UTC (2026-05-27)

> Source : `data/latest.json` (fetched 2026-05-27T13:00:02 UTC) | `data/recommandations_2026-05-27.json` | Snapshot 13:00 UTC

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-27 10:00 UTC)

| Métrique | Snapshot 10:00 UTC 27/05 | Snapshot 13:00 UTC 27/05 | Variation |
|---|---|---|---|
| **Cours close** | $143,20 | **$143,20** | **Inchangé** |
| **Change % vs veille** | +5,48 % | **+5,48 %** | Identique |
| **RSI 14j** | 77,42 | **77,42** | Inchangé — surachat extrême persistant |
| **ATR 14j** | $12,68 | **$12,68** | Inchangé |
| **MM 50j** | $86,80 | **$86,80** | Inchangé |
| **Volume séance** | 32,78 M (1,15×) | **32,78 M** (1,15×) | Inchangé |
| **Market Cap (Yahoo)** | $82,89 Mds | **$82,89 Mds** | Inchangé |
| **Forward P/E** | –12 995 | **–12 995** | Inchangé |
| **EV/Revenue** | 120,12× | **120,12×** | Inchangé |
| **P/B (Yahoo)** | 36,41× | **36,41×** | Inchangé |
| **52W High / Low** | $146,00 / $25,24 | **$146,00 / $25,24** | Inchangé |
| **Consensus PT (FMP)** | $84,20 | **$84,20** | Inchangé — divergence **+70,1 %** |
| **Score Global Agent** | 40,8/100 (aj. 30,8) | **40,8/100** (aj. **30,8**) | Inchangé — **ÉVITER** |
| **Max Pain** | $130,00 (confirmé 26/05) | **$123,00** | 🔴 **MUTATION** — abaissement de –5,4 % |
| **Put/Call ratio** | `null` (interrompu) → 1,08 (confirmé 26/05) | **1,47** | 🔴 **MUTATION** — hausse de +36 % |
| **Call OI %** | `null` (interrompu) → 48,1 % (confirmé 26/05) | **40,5 %** | 🔴 **MUTATION** — baisse de –7,6 pts |

**Verdict** : Le snapshot 13:00 UTC du 27 mai 2026 confirme la **stabilité totale** du cours à **$143,20** et de l'ensemble des métriques techniques (RSI, ATR, volume, MM). La donnée nouvelle et significative est la **restauration et mutation des données options** dans `latest.json` :
- Le Max Pain passe de **$130,00** (éch. 2026-05-29) à **$123,00** — écart vs spot élargi de –9,2 % à **–14,1 %**.
- Le Put/Call ratio passe de **1,08** à **1,47** — biais put renforcé de +36 %.
- Le Call OI % passe de **48,1 %** à **40,5 %** — confirmation d'un biais baissier dans l'open interest.

Cette mutation suggère qu'entre le close du 26/05 et le snapshot 13:00 UTC, les opérateurs options ont accru leur exposition put et révisé à la baisse le niveau de pin attendu pour l'échéance du 29 mai (2 jours ouvrés). La thèse **ÉVITER** est **confirmée et légèrement renforcée** par cette dégradation de la structure options.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 77,42 | 🔴 **Surachat extrême** (>70). Stable. Aucun refroidissement technique. |
| **ATR 14j** | $12,68 | Volatilité stable en zone élevée. Range intraday 26/05 = $138,56–$146,00 (5,1 %). |
| **MM 50j** | $86,80 | Écart haussier **+64,9 %** vs spot. Tendance parabolique étendue. |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume 20j** | 28 440 605 | Séance 26/05 : **32,78 M** — **1,15× moyenne**. |
| **Beta** | 2,313 | Sensibilité systématique extrême. |
| **52W High / Low** | $146,00 / $25,24 | Spot à **–1,9 %** du 52W high. Extension parabolique maintenue. |
| **Short Interest** | 5,79 % | Stable. Élevé ; squeeze possible si catalyseur, non déclenché. |

**Niveaux clés** (inchangés, ATR stable) :
- Support immédiat : **$138,56** (basse intraday 26/05)
- Support technique majeur : **$117,84** (spot – 2×ATR)
- Résistance immédiate : **$146,00** (haute intraday 26/05, 52W high)
- Résistance / Objectif : **$181,24** (spot + 3×ATR)
- Confluence technique : $80–$95 (zone MM50j — éloignée de –34 %)
- **Max Pain options** (éch. 2026-05-29) : **$123,00** — écart **–14,1 %** vs spot $143,20 (= 1,59×ATR)

**Verdict timing : Défavorable** — Configuration inchangée. RSI > 77, écart MM50 > 64 %, ATR stable en zone élevée. La mutation options (Max Pain $123, P/C 1,47) ajoute une pression baissière de très courte échéance qui coïncide avec la zone de support technique $117–$123.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. Snapshot 13:00 UTC sans nouveau catalyseur.

| Métrique | Valeur | Source | Évolution vs 10:00 |
|---|---|---|---|
| Market Cap (Yahoo) | **$82,89 Mds** | Yahoo Finance | Inchangé |
| Forward P/E | **–12 995** | Yahoo Finance | Inchangé |
| EV/Revenue | 120,12× | Yahoo Finance | Inchangé |
| EV/EBITDA | –495,25× | Yahoo Finance | Inchangé en magnitude |
| P/B (Yahoo) | **36,41×** | Yahoo Finance | Inchangé |
| P/B (FMP) | 21,50× | FMP Stable API | Inchangé |
| P/S (FMP) | 61,51× | FMP Stable API | Inchangé |
| Short Interest | 5,79 % | Yahoo Finance | Inchangé |
| **FMP Consensus PT** | **$84,20** (15 analysts, 2 ce mois, 5 ce trimestre) | FMP Stable API | Inchangé |
| **FMP Gross Margin** | 34,4 % | FMP Stable API | Inchangé |
| **FMP Operating Margin** | –38,0 % | FMP Stable API | Inchangé |
| **FMP Net Margin** | –32,9 % | FMP Stable API | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($82,89 Mds) vs FMP sous-jacent ($37,02 Mds) maintenue. Les ratios FMP restent les références opérationnelles.

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

**Divergence cours vs consensus** : Spot $143,20 vs PT moyen $84,20 = **+70,1 % au-dessus du consensus sell-side**.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 10:00 |
|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts) | Inchangé |
| **Put/Call ratio** | **1,47** | 🔴 **MUTATION** — hausse de +36 % vs 1,08 (26/05) |
| **Call OI %** | **40,5 %** | 🔴 **MUTATION** — baisse de –7,6 pts vs 48,1 % (26/05) |
| **Max Pain** | **$123,00** | 🔴 **MUTATION** — abaissement de –$7 vs $130,00 (26/05) |
| **Short Interest** | 5,79 % | Inchangé |
| **News du jour** | Aucune | `data/news_2026-05-27.json` vide pour RKLB. |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail. |
| **NLP Transcripts** | Indisponible | Plan FMP Starter. |

**Analyse options** (données restaurées et révisées dans `latest.json` 13:00 UTC) :
- **Max Pain $123,00** (éch. 2026-05-29, **2 jours ouvrés**) : écart de **–14,1 %** vs spot $143,20 (= 1,59×ATR). Le marché options a abaissé le niveau de pin attendu de $130 à $123 entre le 26/05 et le 27/05 13:00 UTC. Cette révision à la baisse indique que les opérateurs ne price pas de consolidation vers le spot actuel, mais anticipent un repli significatif avant vendredi.
- **Put/Call 1,47** (vs 1,08) : hausse de +36 %. Biais put nettement renforcé. À ratio > 1,4, la protection domine largement la spéculation haussière à très courte échéance.
- **Call OI 40,5 %** (vs 48,1 %) : désormais < 50 %, confirmant que l'open interest est majoritairement put-oriented.
- **Synthèse options** : configuration **baissière renforcée** à très courte échéance (2 jours). Le spot $143,20 est significativement au-dessus du nouveau Max Pain $123,00. La probabilité d'un repli vers la zone $123–$130 d'ici vendredi est évaluée comme élevée compte tenu du Beta 2,31 et de l'ATR $12,68 (1,59×ATR = $20,20, soit un mouvement plausible en 2 séances).

**Verdict Sentiment :** Légèrement baissier — Aucun upgrade/downgrade. Aucune news. La mutation options est le seul signal nouveau et il est négatif : hausse de l'exposition put, abaissement du Max Pain, baisse du Call OI. Cela coïncide avec la thèse ÉVITER et renforce la prudence à très court terme.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `null`, n=0, date 2026-05-17). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Non flaggé dans `geo_risk_latest.json` (2026-05-17). | Aucun malus. |
| **Comptable (Accounting)** | `data/accounting_risk_latest.json` non disponible. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) return 20j +1,04 %, sous-performe SPY (RS –3,92 % / –11,04 %). Momentum score 0,0. | Malus sectoriel implicite. |
| **FX Exposure** | Score FX Impact 0,0. Exposition 25 % export, divergence aligned. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate dans `events_2026-05-27.json`. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**71 jours**). Est EPS –$0,06 à –$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 71j — trop loin. Mutation options baissière à très CT. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 120×, spot +70,1 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 5,5/10 | Tendance haussière structurelle intacte (prix > MM50), 52W high maintenu, mais RSI surachat extrême 77,42. |
| **Score Opportunité** | **4,1/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | –10 pts | Malus structurel (surchauffe technique + divergence consensus + absence de catalyseur). |
| **Score Global ajusté** | **30,8/100** | **ÉVITER** — Seuil < 35 |

**Règle de disqualification** : Score Valorisation ≤ 2/10 → action exclue du rapport long. Ici Val = 3,0/10 — le titre reste dans le rapport mais avec recommandation ÉVITER.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $143,20 | — |
| **Stop-loss** | $117,84 (–17,7 %) | 2×ATR ($12,68) — aligné agent officiel |
| **Take-profit** | $181,24 (+26,6 %) | 3×ATR ($12,68) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | **Inférieur au seuil minimum 2:1** pour un trade directionnel à haut beta |

> **Révision** : Niveaux inchangés vs 10:00 UTC. Le Max Pain révisé à $123,00 (écart –14,1 %) se situe entre le support immédiat $138,56 et le support majeur $117,84. Il constitue un **niveau intermédiaire de consolidation probable** d'ici l'expiration du 29 mai. Une position longue actuelle expose toujours à un drawdown de –17,7 % (SL) en 1–2 séances compte tenu du Beta 2,31 et de l'ATR $12,68.

**Niveau de pin options** : Max Pain $123,00 (éch. 2026-05-29, **2 jours ouvrés**) — écart **–14,1 %** vs spot. Le rapprochement du Max Pain vers la zone $120–$123 renforce l'hypothèse d'un test de cette zone avant vendredi, compte tenu du biais put renforcé (P/C 1,47).

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **71 jours** | Est EPS : –$0,06 à –$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-05-29 | **2 jours ouvrés** | Max Pain $123,00 — écart –14,1 % vs spot |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 29 mai approche dans 2 jours avec un Max Pain révisé à la baisse ($123), ce qui augmente la probabilité d'une consolidation technique vers cette zone.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER — MUTATION OPTIONS RENFORCE LA PRUDENCE**

Le snapshot 13:00 UTC du 27 mai 2026 confirme la **stabilité totale** du cours à **$143,20** et de l'ensemble des métriques techniques/fondamentales. La seule variation significative est la **restauration et mutation des données options** dans `latest.json` :

1. **Cours stable à $143,20** — inchangé vs 10:00 UTC et vs close officiel 26/05.
2. **RSI 77,42** — surachat extrême persistant, proche de la zone >80.
3. **ATR $12,68** — inchangé, volatilité stable en zone élevée.
4. **Volume 32,78 M (1,15×)** — inchangé, gap haussier du 26/05 confirmé sur volume supérieur à la moyenne.
5. **🔴 MUTATION OPTIONS** :
   - Max Pain **$123,00** (vs $130,00 au 26/05, vs $45,00 anomalie matin) — écart **–14,1 %** vs spot.
   - Put/Call **1,47** (vs 1,08 au 26/05) — hausse de +36 %, biais put renforcé.
   - Call OI **40,5 %** (vs 48,1 % au 26/05) — biais baissier de l'open interest confirmé.
6. **52W high $146,00** maintenu — extension parabolique intacte.
7. **Divergence consensus +70,1 %** (spot vs PT $84,20) — valorisation de plus en plus déconnectée.
8. **P/B Yahoo 36,41×** — valorisation stable en zone extrême.
9. **Score agent inchangé** : 40,8/100 (aj. 30,8) — ÉVITER maintenu.
10. **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
11. **Sector rotation défavorable** — XLI sans momentum, sous-performe SPY 20j/60j.
12. **Aucune news** — mouvement purement technique/momentum confirmé.

**Recommandation** : Maintenir la posture **ÉVITER**. La mutation options renforce la prudence à très court terme : le marché options a accru son exposition put et abaissé le Max Pain de $130 à $123, ce qui indique que les opérateurs anticipent une consolidation vers la zone $123–$130 d'ici l'expiration de vendredi. Cette évolution est cohérente avec la thèse ÉVITER et n'appelle pas de révision à la hausse.

Attendre :
- Un **retour vers la zone de confluence $110–$123** (gap fill + test de support + zone Max Pain), ou
- Une **inflexion matérielle des anticipations de résultats** (guidance positive, contrat majeur, etc.), ou
- Un **refroidissement technique** (RSI < 70 sur plusieurs séances + volume décroissant) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de –17,7 % (SL) en 1–2 séances compte tenu de l'ATR $12,68 et du Beta 2,31.

---

*Rapport généré le 2026-05-27 — Données : `data/latest.json` (13:00 UTC), `data/recommandations_2026-05-27.json`, `data/upcoming_events_2026-05-27.json`, `data/events_2026-05-27.json`, `data/news_2026-05-27.json`, `data/social_sentiment_2026-05-27.json`, `data/geo_risk_latest.json` (2026-05-17), `data/sector_rotation_2026-05-27.json`, `data/fx_exposure_2026-05-27.json`, `data/quant_report_latest.json` (2026-05-17)*
