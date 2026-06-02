# RKLB — Mise à Jour Snapshot 10:00 UTC (2026-06-02)

> Source : `data/2026-06-02.json` (fetched 2026-06-02T10:00:01 UTC) | `data/recommandations_2026-06-02.json` | Close officiel US du 2026-06-01

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-01)

| Métrique | Snapshot 01/06 | Snapshot 02/06 | Variation |
|---|---|---|---|
| **Cours close** | $122,39 | **$122,39** | ✅ **Stable** |
| **RSI 14j** | 52,48 | **52,48** | ✅ Stable |
| **ATR 14j** | $12,50 | **$12,55** | ✅ Stable (+$0,05) |
| **Volume séance** | 36,66 M (1,17×) | **37,13 M (1,19×)** | 🟡 Légère correction +1,3 % |
| **Market Cap (Yahoo)** | $70,85 Mds | **$70,85 Mds** | Stable |
| **P/B (Yahoo)** | 31,12× | **31,12×** | Stable |
| **Divergence consensus** | +45,4 % vs PT $84,20 | **+45,4 %** | Inchangé |
| **Score Global Agent** | 42,0/100 (aj. 47,0) SURVEILLER | **42,0/100 (aj. 47,0)** | Inchangé |
| **Max Pain** | $90,00 | **$45,00** | 🔴 **ANOMALIE DATA — voir §4** |
| **Put/Call ratio** | 1,25 | **null** | 🔴 **Données corrompues** |
| **Call OI %** | 44,4 % | **null** | 🔴 **Données corrompues** |

**Verdict** : **Stabilité totale** du cours, de la structure technique et du scoring global vs le snapshot 21h du 01/06. Le seul changement significatif concerne les **données options** dans `data/latest.json` : Max Pain passe de $90,00 à $45,00 et les ratios Put/Call / Call OI deviennent `null`. Il s'agit d'une anomalie data quality présumée — les valeurs du 01/06 ($90,00 / 1,25 / 44,4 %) restent plus cohérentes avec la structure observée. Le volume final est légèrement révisé à la hausse (37,13 M = 1,19× moyenne 20j), renforçant l'interprétation de distribution active post-repli.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 52,48 | ✅ Neutre. Sortie du surachat confirmée. |
| **ATR 14j** | $12,55 | Volatilité élevée stable. Range intraday 01/06 = $121,00–$135,63. |
| **MM 50j** | $92,26 | Écart haussier **+32,7 %** vs spot. Tendance haussière structurelle intacte. |
| **Volume 20j** | 31 224 555 | Séance 01/06 : **37,13 M** — **1,19× moyenne**. Distribution active confirmée. |
| **Beta** | 2,313 | Sensibilité systématique extrême. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−18,9 %** du 52W high. |

**Niveaux clés révisés** :
- Support immédiat : **$121,00** (basse intraday 01/06) — testé mais non cassé en clôture
- Support technique majeur : **$97,29** (spot – 2×ATR $12,55) — aligné agent officiel
- Support confluence : **$90,00** (zone Max Pain historique + test psychologique)
- Résistance immédiate : **$135,63** (haute intraday 01/06)
- Résistance / Objectif : **$160,04** (spot + 3×ATR $12,55) — aligné agent officiel
- **Max Pain** (éch. 2026-06-05, *valeur historique fiable*) : **$90,00** — spot $122,39 = +$32,39 (+26,5 %)

**Verdict timing : Défavorable** — Le repli −14,7 % sur volume 1,19× moyenne confirme une distribution active. Le RSI 52 est neutre mais la clôture proche du low ($122,39 vs low $121,00) indique une pression vendeuse soutenue. La probabilité d'un test de la zone $118–$121 (gap du 22/05) demeure élevée. Le support $97,29 (2×ATR) reste le pivot clé.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-02.json` vide pour RKLB. `data/events_2026-06-02.json` vide. Le mouvement −14,7 % reste **sans catalyseur fondamental identifiable**.

| Métrique | Valeur | Source |
|---|---|---|
| Market Cap (Yahoo) | **$70,85 Mds** | Yahoo Finance |
| Forward P/E | **−11 106,17** | Yahoo Finance |
| EV/Revenue | 102,40× | Yahoo Finance |
| EV/EBITDA | −422,18× | Yahoo Finance |
| P/B (Yahoo) | **31,12×** | Yahoo Finance |
| P/B (FMP) | 21,50× | FMP Stable API |
| P/S (FMP) | 61,51× | FMP Stable API |
| Short Interest | 5,81 % | Yahoo Finance |
| **FMP Consensus PT** | **$84,20** (15 analysts) | FMP Stable API |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($70,85 Mds) vs FMP sous-jacent ($37,02 Mds) persiste.

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

**Divergence cours vs consensus** : Spot $122,39 vs PT moyen $84,20 = **+45,4 % au-dessus du consensus sell-side**.

---

## 4. Mise à Jour Sentiment / Options / News

**🔴 ANOMALIE DATA QUALITY — Options RKLB dans `data/2026-06-02.json`**

| Signal | Valeur 01/06 (fiable) | Valeur 02/06 (snapshot) | Diagnostic |
|---|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts) | $84,20 (15 analysts) | ✅ Stable |
| **Put/Call ratio** | **1,25** | **null** | 🔴 **Données corrompues** |
| **Call OI %** | **44,4 %** | **null** | 🔴 **Données corrompues** |
| **Max Pain** | **$90,00** | **$45,00** | 🔴 **Incohérent vs historique** |
| **Short Interest** | 5,81 % | 5,81 % | Stable |
| **News du jour** | Aucune | Aucune | `data/news_2026-06-02.json` vide. |
| **Social Sentiment** | 0 mentions, score 0/10 | 0 mentions, score 0/10 | Aucune activité retail. |

- **Max Pain $90,00** (valeur historique confirmée, éch. 2026-06-05) : spot $122,39 = spread **+$32,39 (+26,5 %)**. La divergence reste extrême.
- **Put/Call 1,25** (valeur historique) : puts dominent légèrement les calls. Structure baissière à très court terme maintenue.
- **Call OI 44,4 %** (valeur historique) : faible conviction haussière institutionnelle à CT.
- **⚠️ Données options du 02/06** : Max Pain $45,00 est incohérent avec la structure historique ($90,00–$130,00 sur les 2 dernières semaines) et les ratios `null` indiquent un flux interrompu. **Recommandation : utiliser les valeurs du 01/06 jusqu'à correction.**

**Verdict Sentiment :** Légèrement baissier — Aucun upgrade/downgrade, aucune news, absence totale d'activité retail. La structure options historique confirme la pression baissière à CT. L'expiration du 5 juin dans 3 jours ouvrés constitue un catalyseur technique de potentielle volatilité.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `null`, n=0, date 2026-06-02). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Score Politique 2/10, non exposé. | Aucun malus. |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) return 20j −0,32 %, sous-performe SPY (RS −5,58 %). Momentum score 0,0. Signal ROTATION_TO_CYCLICAL. | Malus sectoriel implicite. RKLB dans Aerospace & Defense (XLI) — pas de momentum sectoriel. |
| **FX Exposure** | Score FX Impact 0,0. Exposition 25 % export, divergence aligned. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate dans `events_2026-06-02.json`. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**65 jours**). Est EPS −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`, pas d'anomalie détectée sur le prix. | Aucun malus. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 65j. Structure options baissière à CT (Max Pain historique $90). |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 102×, spot +45,4 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 6,0/10 | Tendance haussière structurelle intacte (prix > MM50), mais distribution −14,7 % sur volume 1,19×. RSI 52 neutre. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (surchauffe partiellement dégonflée + divergence consensus). |
| **Score Global ajusté** | **47,0/100** | **SURVEILLER** — Seuil 35–49 |

**Comparaison avec snapshot 01/06** : Le score global est **inchangé** (47,0). Aucun nouvel input fondamental, technique ou sentiment n'altère la thèse. L'unique variation notable est l'**anomalie data quality options** (Max Pain $45,00 / ratios `null`), jugée non fiable et écartée au profit des valeurs historiques.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $122,39 | — |
| **Stop-loss** | $97,29 (−20,4 %) | 2×ATR ($12,55) — aligné agent officiel |
| **Take-profit** | $160,04 (+30,7 %) | 3×ATR ($12,55) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inférieur au seuil minimum 2:1 pour un trade directionnel à haut beta |

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **65 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-05 | **3 jours ouvrés** | Max Pain historique **$90,00** — pression baissière persistante vs spot $122,39 |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 5 juin approche dans 3 jours avec un Max Pain historique $90,00, soit **$32,39 sous le spot**. La baisse de −14,7 % a réduit mais pas éliminé le risque technique de volatilité négative d'ici vendredi.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — STABILITÉ TOTALE**

Le snapshot 10:00 UTC du 2 juin 2026 confirme l'intégralité de l'analyse du 1er juin : **aucun changement significatif** sur le cours ($122,39 stable), la structure technique (RSI 52, ATR $12,55), la valorisation (extrême), ou le scoring global (47,0 — SURVEILLER).

**Éléments clés vs analyse précédente (2026-06-01)** :
1. ✅ **Cours stable** : $122,39 inchangé. Aucun suivi du repli ni rebond.
2. ✅ **RSI stable neutre** : 52,48. Risque de correction technique immédiate réduit.
3. ✅ **Volume stable** : 37,13 M (1,19×) vs 36,66 M (1,17×). Distribution active confirmée.
4. ✅ **ATR stable** : $12,55. Volatilité inchangée.
5. ✅ **Divergence consensus stable** : +45,4 % vs PT $84,20. Prime toujours élevée.
6. 🔴 **ANOMALIE DATA QUALITY OPTIONS** : Max Pain $90,00 → $45,00 (incohérent), Put/Call et Call OI passent à `null`. Valeurs historiques conservées.
7. 🔴 **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
8. 🔴 **Sectoriel défavorable** — XLI sans momentum, sous-performe SPY 20j/60j.
9. ✅ **Score global inchangé** : 42,0/100 ajusté 47,0 — SURVEILLER.

**Recommandation** : Maintenir la posture **SURVEILLER**. La stabilité totale du snapshot du 02/06 confirme que le repli du 01/06 n'a pas déclenché de panique additionnelle overnight, mais n'a pas non plus généré de rebond technique. La valorisation reste extrême (Forward P/E négatif, EV/Rev 102×, spot +45 % vs consensus) et le Filtre Qualité 3/6 exclut tout positionnement institutionnel long.

Attendre :
- Un **retour vers la zone de confluence $97–$105** (test support 2×ATR + test psychologique), ou
- Une **inflexion matérielle des anticipations** (guidance positive, contrat majeur, etc.) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de −20,4 % (SL) en 1–2 séances compte tenu de l'ATR $12,55 et du Beta 2,31. Le risque options CT (Max Pain historique $90,00) persiste. L'anomalie data quality options du snapshot 02/06 doit être corrigée par le pipeline avant le prochain bulletin.

---

*Rapport généré le 2026-06-02 — Données : `data/2026-06-02.json` (10:00 UTC), `data/recommandations_2026-06-02.json`, `data/upcoming_events_2026-06-02.json`, `data/events_2026-06-02.json`, `data/news_2026-06-02.json`, `data/social_sentiment_2026-06-02.json`, `data/geo_2026-06-02.json`, `data/sector_rotation_2026-06-02.json`, `data/fx_exposure_2026-06-02.json`, `data/quant_2026-06-02.json`, `data/quality_gate_2026-06-02.json`*
