# RKLB — Mise à Jour Snapshot Matin (2026-05-20, 10:00 UTC)

> Source : `data/latest.json` (2026-05-20T10:00:12 UTC) | `data/recommandations_latest.json` (2026-05-20) | Validation OK (22/25 tickers OK, RKLB non signalé)
> **Snapshot pre-market US** — Cours = close officiel du 19 mai 2026.

---

## 1. Résumé des Changements depuis l'Analyse Précédente

| Métrique | 2026-05-19 (21:00 UTC) | 2026-05-20 (10:00 UTC) | Variation |
|---|---|---|---|
| **Cours close** | $127,31 | **$127,31** | **0,00 %** — inchangé |
| **Change % vs veille** | –2,94 % | **–2,94 %** | **Inchangé** |
| **RSI 14j** | 76,14 | **76,14** | **Inchangé** |
| **ATR 14j** | $11,09 | **$11,09** | **Inchangé** |
| **MM 50j** | $81,58 | **$81,58** | **Inchangé** |
| **Volume séance** | 29,88 M (1,12×) | **29,996 M** (1,12×) | **Stable** |
| **Market Cap (Yahoo)** | $73,68 Mds | **$73,68 Mds** | **Inchangé** |
| **Forward P/E** | –14 942 | **–14 942** | **Inchangé** |
| **P/B (Yahoo)** | 40,19× | **40,19×** | **Inchangé** |
| **Consensus PT (FMP)** | $84,20 | **$84,20** | **Inchangé** |
| **Score Global Agent** | 39,5/100 (aj. 29,5) | **39,5/100** (aj. **29,5**) | **Inchangé** |
| **Action Agent** | ÉVITER | **ÉVITER** | **Inchangée** |
| **Max Pain** | $150,00 | **$45,00** | **[ANOMALIE DATA]** |
| **Put/Call ratio** | 0,83 | **null** | **[DONNÉES MANQUANTES]** |
| **Call OI %** | 54,6 % | **null** | **[DONNÉES MANQUANTES]** |

**Verdict** : Aucune variation de données entre le close du 19/05 21h UTC et le snapshot matinal du 20/05 10h UTC. Le ticker n'a pas été réévalué par le pipeline nocturne. **Configuration inchangée** : surchauffe technique persistante (RSI 76,14), valorisation déconnectée (spot +51,2 % vs consensus), absence de catalyseur. L'**anomalie data** sur le Max Pain ($45,00 vs $150,00 hier) et la disparition du Put/Call ratio indiquent une interruption du flux options pour RKLB ce matin — les métriques options du 19/05 restent la référence opérationnelle.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 76,14 | Surachat persistant (>70). Pas de refroidissement. |
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
- **Max Pain référence** (éch. 2026-05-22) : **$150,00** (valeur du 19/05) — spot $127,31 en dessous de **15,1 %**. La valeur $45,00 du snapshot matinal est rejetée comme aberrante.

**Verdict timing : Défavorable** — Pas de changement de configuration. RSI > 76, écart MM50 > 56 %, absence de signal de retournement. Attendre un retour sous RSI 70 ou un test de la zone $110–$115.

---

## 3. Mise à Jour Fondamentale

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

**[ANOMALIE DONNÉES]** — Divergence Market Cap Yahoo ($73,68 Mds) vs données FMP sous-jacentes maintenue. Les ratios FMP (P/B 21,50×, P/S 61,51×) restent indicatifs.

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
| **Put/Call ratio** | null | [DONNÉES MANQUANTES] — flux interrompu ce matin. Référence 19/05 : 0,83. |
| **Call OI %** | null | [DONNÉES MANQUANTES] — flux interrompu ce matin. Référence 19/05 : 54,6 %. |
| **Max Pain (snapshot)** | $45,00 | **[ANOMALIE DATA]** — aberrant vs spot $127,31. Référence 19/05 : $150,00. |
| **Short Interest** | 5,79 % | Inchangé |
| **News du jour** | Aucune | `data/news_2026-05-20.json` vide pour RKLB. |
| **Social Sentiment** | 0 mentions, score 0/10 | `data/social_sentiment_2026-05-20.json` — aucune activité retail. |
| **NLP Transcripts** | Indisponible | Plan FMP Starter — transcripts require Enterprise+. |

**Verdict Sentiment :** Neutre / Légèrement baissier — Flux options interrompus ce matin (données manquantes). En l'absence de nouvelle information, le sentiment reste dominé par la divergence consensus (spot +51 % vs PT) et le short interest élevé sans catalyseur de squeeze. Aucun upgrade/downgrade détecté.

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
| **Expiration options** | 2026-05-22 | **2 jours** | Max Pain référence $150,00 — spot en dessous de 15,1 % |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 22 mai approche dans 2 jours. La convergence vers $150 reste improbable. Surveillance si activité options inhabituelle en fin de semaine — **attention** : flux options interrompu ce matin, requiert vérification manuelle si rétabli d'ici vendredi.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER**

Le snapshot matinal du 20 mai 2026 ne fait que **confirmer l'analyse du 19 mai au soir** : aucune donnée n'a varié entre le close officiel et le fetch pre-market (10h UTC). Le ticker reste dans une configuration de **surchauffe technique persistante** (RSI 76,14) avec une **valorisation déconnectée du consensus sell-side** (+51,2 % vs PT $84,20).

**Éléments clés vs analyse précédente** :
1. **Cours stable à $127,31** — pas de mouvement post-séance ni pre-market significatif.
2. **Données techniques inchangées** — RSI, ATR, MM50, volume identiques.
3. **[ANOMALIE DATA] Max Pain $45,00** dans le snapshot matinal vs $150,00 hier. Valeur rejetée comme aberrante (écart 65 % sous le spot). Probable erreur de parsing ou données options corrompues.
4. **[DONNÉES MANQUANTES] Put/Call ratio et Call OI % passés à null** — flux options interrompu pour RKLB ce matin. Référence opérationnelle = données du 19/05 (Put/Call 0,83, Call OI 54,6 %).
5. **Aucune news** — `data/news_2026-05-20.json` vide. Mouvement purement technique/options-driven confirmé.
6. **Score agent inchangé** : 39,5/100 (aj. 29,5) — ÉVITER maintenu.
7. **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
8. **Sector rotation défavorable** — XLI sans momentum, sous-performe SPY.

**Recommandation** : Maintenir la posture **ÉVITER**. En l'absence de nouvelle information et avec des flux options partiellement interrompus, aucune réévaluation n'est justifiée. Le support $115 a tenu le 19/05 mais reste fragile sous RSI 76. Attendre :
- Un **retour vers la zone de confluence $80–$95** (proximité MM50j et compression technique), ou
- Une **inflexion matérielle des anticipations de résultats** (guidance positive, contrat majeur, etc.), ou
- Un **refroidissement technique** (RSI < 70 sur plusieurs séances) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de –17,4 % (SL) en 1–2 séances compte tenu de l'ATR $11,09 et du Beta 2,31.

---

*Rapport généré le 2026-05-20 — Données : `data/latest.json` (2026-05-20T10:00:12), `data/recommandations_latest.json` (2026-05-20), `data/upcoming_events_latest.json` (2026-05-20), `data/events_latest.json` (2026-05-20), `data/news_2026-05-20.json`, `data/social_sentiment_2026-05-20.json`, `data/geo_risk_latest.json` (2026-05-17), `data/sector_rotation_latest.json` (2026-05-20), `data/fx_exposure_latest.json` (2026-05-20), `data/quant_report_latest.json` (2026-05-17)*
