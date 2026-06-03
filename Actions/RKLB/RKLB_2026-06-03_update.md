# RKLB — Mise à Jour Snapshot 10h UTC (2026-06-03)

> Source : `data/2026-06-03.json` (fetched 2026-06-03T10:00:13 UTC) | `data/recommandations_2026-06-03.json` | Snapshot pre-market US du 2026-06-03

---

## 1. Résumé des Changements depuis le Snapshot 21h UTC (2026-06-02)

| Métrique | Snapshot 21h 02/06 | Snapshot 10h 03/06 | Variation |
|---|---|---|---|
| **Cours close** | $123,32 | **$123,32** | Stable |
| **RSI 14j** | 52,81 | **52,81** | Stable |
| **ATR 14j** | $12,33 | **$12,33** | Stable |
| **Volume séance** | 19,25 M (0,61×) | **19,34 M (0,62×)** | Stable |
| **Score Global Agent** | 44,5/100 (aj. 49,5) | **44,5/100 (aj. 49,5)** | Inchangé |
| **Max Pain (opérationnel)** | $145,00 | **$145,00** | Stable |
| **Put/Call ratio** | 1,18 | **1,18** | Stable |
| **Call OI %** | 45,9 % | **45,9 %** | Stable |
| **Signal sectoriel** | NEUTRAL | **NEUTRAL** | Stable |
| **Forward P/E** | −11 191 | **−11 191** | Stable (négatif) |
| **P/B Yahoo** | 31,36× | **31,36×** | Stable |
| **FMP Consensus PT** | $84,20 (15 analysts) | **$84,20 (15 analysts)** | Stable |
| **Earnings Q2 2026** | 65 jours | **64 jours** | −1j |

**Verdict** : **Stabilité totale** du snapshot 10h UTC du 3 juin vs le close officiel du 2 juin. Aucune variation significative sur les prix, volumes, indicateurs techniques ou scores agents. L'unique événement est le **décompte earnings qui passe de 65 à 64 jours** (échéance 2026-08-06). Une **anomalie Max Pain** est détectée dans `latest.json` ($45,00 vs $145,00 opérationnel) — la valeur opérationnelle est conservée.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 52,81 | Neutre. Aucun changement depuis le snapshot 21h du 02/06. |
| **ATR 14j** | $12,33 | Volatilité élevée stable. |
| **MM 50j** | $93,38 | Écart haussier **+32,1 %** vs spot. Tendance haussière structurelle intacte. |
| **Volume 20j** | 31 387 921 | Séance 02/06 close : **19,34 M** — **0,62× moyenne**. Participation modérée. |
| **Beta** | 2,313 | Sensibilité systématique extrême. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−18,3 %** du 52W high. |

**Niveaux clés inchangés** :
- Support immédiat : **$122,56** (basse intraday 02/06)
- Support technique majeur : **$98,66** (spot − 2×ATR) — aligné agent officiel
- Support confluence : **$90,00** (zone test psychologique + ancien Max Pain)
- Résistance immédiate : **$128,28** (haute intraday 02/06)
- Résistance / Objectif : **$160,31** (spot + 3×ATR) — aligné agent officiel
- **Max Pain** (éch. 2026-06-05, valeur opérationnelle) : **$145,00** — spot $123,32 = −$21,68 (−15,0 %)

**[ANOMALIE OPTIONS DÉTECTÉE]** — `data/latest.json` affiche Max Pain **$45,00** pour RKLB (vs $145,00 au snapshot précédent). Cette valeur est **aberrante** (spot $123,32, un max pain à $45 implique une divergence de −63,5 % sans fondement). Cause probable : corruption partielle du flux options JSON. **Valeur opérationnelle $145,00 conservée** pour l'analyse.

**Verdict timing : Défavorable** — La stabilité des données confirme l'absence de momentum directionnel. Le cours reste sous la résistance $128,28 et le volume sous-moyen (0,62×) invalide toute lecture haussière. Le support $98,66 (2×ATR) reste le pivot clé.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-03.json` vide pour RKLB. `data/events_2026-06-03.json` vide (0 événement corporate). Le marché est en attente.

| Métrique | Valeur | Source |
|---|---|---|
| Market Cap (Yahoo) | **$71,39 Mds** | Yahoo Finance |
| Forward P/E | **−11 191** | Yahoo Finance |
| EV/Revenue | 103,19× | Yahoo Finance |
| EV/EBITDA | −425,45× | Yahoo Finance |
| P/B (Yahoo) | **31,36×** | Yahoo Finance |
| P/B (FMP) | 21,50× | FMP Stable API |
| P/S (FMP) | 61,51× | FMP Stable API |
| Short Interest | 5,81 % | Yahoo Finance |
| **FMP Consensus PT** | **$84,20** (15 analysts) | FMP Stable API |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($71,39 Mds) vs FMP sous-jacent ($37,02 Mds) persiste.

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

**Divergence cours vs consensus** : Spot $123,32 vs PT moyen $84,20 = **+46,5 % au-dessus du consensus sell-side**.

---

## 4. Mise à Jour Sentiment / Options / News

Structure options inchangée vs snapshot 21h du 02/06 :

| Signal | Valeur | Évolution vs 21h 02/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts) | Inchangé |
| **Max Pain (opérationnel)** | **$145,00** | Inchangé |
| **Put/Call ratio** | **1,18** | Inchangé |
| **Call OI %** | **45,9 %** | Inchangé |
| **Short Interest** | 5,81 % | Stable |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Max Pain $145,00** (éch. 2026-06-05) : spot $123,32 = **−$21,68 (−15,0 %)**. La divergence reste significative.
- **Put/Call 1,18** : puts dominent légèrement les calls.
- **Call OI 45,9 %** : faible conviction haussière institutionnelle à CT.

**Verdict Sentiment :** Neutre — Aucun upgrade/downgrade, aucune news, absence totale d'activité retail. La structure options confirme un **pin haussier technique** (spot sous Max Pain $145). L'expiration du 5 juin dans 2 jours ouvrables constitue un catalyseur technique de volatilité CT.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique RKLB (score 3 sur IREN uniquement). | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) return 20j +1,88 %, sous-performe SPY (RS −3,91 %). Signal **NEUTRAL**. Momentum score 0,0. | 🟡 Malus sectoriel implicite. |
| **FX Exposure** | Score FX Impact 0,0. Flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**64 jours**). Est EPS : −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`. | Aucun malus. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 64j. Pin haussier technique CT (Max Pain $145). |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 103×, spot +46,5 % vs consensus. Plafonné par FQ ≤3/6. |
| **Momentum** | 7,0/10 | Tendance haussière structurelle intacte (prix > MM50), mais volume sous-moyen 0,62×. RSI 53 neutre. |
| **Score Opportunité** | **4,5/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (surchauffe partiellement dégonflée + divergence consensus). |
| **Score Global ajusté** | **49,5/100** | **SURVEILLER** — Seuil 35–49 (juste au-dessus, l'agent officiel classe SURVEILLER). |

**Comparaison avec snapshot 21h 02/06** : Le score global est **inchangé** (49,5). Toutes les métriques de prix, volume, technique et fondamentale sont stables. L'unique variation est le décompte earnings (64j vs 65j) et l'anomalie Max Pain JSON ($45,00 aberrant) qui n'affecte pas le scoring opérationnel.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $123,32 | — |
| **Stop-loss** | $98,66 (−20,0 %) | 2×ATR ($12,33) — aligné agent officiel |
| **Take-profit** | $160,31 (+30,0 %) | 3×ATR ($12,33) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inférieur au seuil minimum 2:1 pour un trade directionnel à haut beta |

**Note options CT** : L'expiration du 5 juin avec Max Pain $145 implique un chemin de moindre résistance technique vers $135–$145. Le volume sous-moyen (0,62×) réduit la probabilité d'un rallye violent. L'anomalie Max Pain JSON ($45,00) est signalée mais la valeur opérationnelle $145,00 reste le pivot de référence.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **64 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-05 | **2 jours ouvrables** | Max Pain **$145,00** — spot $123,32 = **−$21,68 sous le Max Pain**. Risque de pin haussier CT. |

**Prochain catalyseur majeur** : Aucun avant earnings (août).

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — STABILITÉ TOTALE**

Le snapshot 10h UTC du 3 juin 2026 confirme intégralement l'analyse du close officiel du 2 juin :

1. ✅ **Cours stable** : $123,32 inchangé. Aucun mouvement directionnel.
2. ✅ **Volume stable** : 19,34 M (0,62×) vs 19,25 M (0,61×). Participation modérée confirmée.
3. ✅ **RSI stable neutre** : 52,81. Risque de correction technique immédiate réduit.
4. ✅ **ATR stable** : $12,33. Volatilité élevée mais contrôlée.
5. ✅ **Divergence consensus stable** : +46,5 % vs PT $84,20. Prime toujours élevée.
6. 🔴 **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
7. 🟡 **Options inchangées** : Max Pain $145,00 opérationnel conservé (anomalie JSON $45,00 signalée), Put/Call 1,18, Call OI 45,9 %. Pin haussier CT persistant.
8. 🟡 **Sectoriel défavorable** — XLI sous-performe SPY 20j/60j, signal NEUTRAL.
9. 🟡 **Aucune news** — le marché est en attente.

**Recommandation** : Maintenir la posture **SURVEILLER**. La stabilité totale des données ne modifie en rien le verdict global. La valorisation reste extrême (Forward P/E négatif, EV/Rev 103×, spot +46,5 % vs consensus) et le Filtre Qualité 3/6 exclut tout positionnement institutionnel long.

Attendre :
- Un **retour vers la zone de confluence $97–$105** (test support 2×ATR + test psychologique), ou
- Une **inflexion matérielle des anticipations** (guidance positive, contrat majeur, etc.) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de −20,0 % (SL) en 1–2 séances compte tenu de l'ATR $12,33 et du Beta 2,31. Le risque options CT (Max Pain $145,00) persiste avec expiration dans 2 jours ouvrables.

---

*Rapport généré le 2026-06-03 — Données : `data/2026-06-03.json` (10:00 UTC), `data/recommandations_2026-06-03.json`, `data/upcoming_events_2026-06-03.json`, `data/events_2026-06-03.json`, `data/sector_rotation_2026-06-03.json`, `data/quant_report_2026-05-17.json`, `data/social_sentiment_2026-06-03.json`, `data/fx_exposure_2026-06-03.json`*
