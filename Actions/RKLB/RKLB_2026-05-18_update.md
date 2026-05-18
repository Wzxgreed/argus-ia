# RKLB — Mise à Jour Quotidienne (2026-05-18)

> Source : data/latest.json | Recommandations 2026-05-18 | Validation OK

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-17)

| Métrique | 2026-05-17 | 2026-05-18 | Variation |
|---|---|---|---|
| **Cours close** | $124,77 | $124,77 | **0,00 %** |
| **Change % séance** | –5,87 % | –5,87 % | — |
| **RSI 14j** | 73,28 | 73,28 | — |
| **ATR 14j** | $9,65 | $9,65 | — |
| **MM 50j** | $79,25 | $79,25 | — |
| **Volume** | 22,36 M | 22,36 M | — |
| **Max Pain** | $150,00 | **$45,00** | **–70,0 %** [ANOMALIE DATA] |
| **Put/Call ratio** | 0,84 | **None** | [DONNÉES MANQUANTES] |
| **Consensus PT (FMP)** | $84,20 | $84,20 | — |
| **Score Global Agent** | 27,0/100 | 27,0/100 | — |
| **Action Agent** | ÉVITER | ÉVITER | — |

**Verdict** : Aucune évolution de cours ni de technique entre les deux séances. Le titre reste figé dans sa configuration de surchauffe extrême (RSI 73,28, +57,3 % au-dessus de la MM50j). **Seul signal notable** : l'anomalie Max Pain à $45,00 (vs $150 précédemment), probablement un artefact de données options du 2026-05-22 à traiter avec prudence.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 73,28 | Zone de surachat inchangée. Risque de consolidation/correction intact. |
| **ATR 14j** | $9,65 | Volatilité quotidienne élevée stable. Le SL à –15,5 % reste franchissable en 1–2 séances. |
| **MM 50j** | $79,25 | Écart haussier +57,3 % vs spot. Tendance très étendue, aucun retest en vue. |
| **MM 200j** | None | [DONNÉES MANQUANTES] |
| **Volume 20j** | 26,37 M | Volume du jour 0,85× moyenne — absence d'accélération haussière, ni de liquidation panique. |
| **Beta** | 2,313 | Sensibilité systématique extrême inchangée. |

**Niveaux clés (inchangés)** :
- Support immédiat : $115,00 (basse du jour $121,80 → gap ouvert)
- Support technique majeur : **$105,47** (SL agent = spot – 2×ATR)
- Résistance / Objectif : **$153,72** (TP agent)

**Verdict timing : Défavorable** — Configuration overbought/extended non corrigée. Aucun signal de retournement ni de compression de volatilité.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|---|---|---|
| Market Cap | $72,2 Mds | Yahoo Finance |
| Forward P/E | **–14 644,37** | Yahoo Finance |
| EV/Revenue | 104,43× | Yahoo Finance |
| EV/EBITDA | –430,54× | Yahoo Finance |
| Price-to-Book | 39,38× | Yahoo Finance |
| Short Interest | **5,79 %** | Yahoo Finance |
| **FMP Consensus PT** | **$84,20** (15 analysts) | FMP Stable API |
| **FMP Gross Margin** | 34,4 % | FMP Stable API |
| **FMP EV/EBITDA** | –234,41× | FMP Stable API |

**Filtre Qualité (6 critères) — réévalué** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Croissance du segment spatial / lanceurs supérieure à 20 % historique. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif abyssal ; pertes persistantes anticipées. |
| 3. Assets/Liabilities > 1,0 | [DONNÉES MANQUANTES] | Bilan détaillé non disponible dans latest.json. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | EV/EBITDA négatif ; absence de génération de cash opérationnel rentable. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique (lanceurs réutilisables légers), mais concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion rapide (constellations, défense). |

**Score Qualité total : 2,5–3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $124,77 vs PT moyen $84,20 = **+48,2 % au-dessus du consensus sell-side**. Cet écart est anormalement large et traduit un premium spéculatif élevé non adossé aux fondamentaux actuels.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|---|---|---|
| **Consensus analystes** | $84,20 (15 analysts, 3 couvertures ce mois) | Inchangé |
| **Put/Call ratio** | None | [DONNÉES MANQUANTES] — précédent 0,84 |
| **Max Pain** | $45,00 | **Anomalie** (vs $150 précédent) |
| **Short Interest** | 5,79 % | Élevé ; potentiel squeeze si catalyseur majeur, mais absent. |
| **News du jour** | Aucune | `data/news_latest.json` vide pour RKLB. |
| **Social Sentiment** | 0 mentions | `data/social_sentiment_latest.json` — aucune activité retail détectée. |

**Anomalie Max Pain** : Le niveau $45,00 pour l'échéance du 2026-05-22 est incohérent avec un spot à $124,77. Cette valeur est probablement un artefact de données (options très OTM, faible open interest, ou erreur de parsing Yahoo). **À ignorer pour le positionnement** jusqu'à confirmation manuelle.

---

## 5. Mise à Jour Macro & Secteur

| Signal | Valeur | Impact RKLB |
|---|---|---|
| **Régime macro** | Unknown | Pas d'ajustement automatique. |
| **Rotation sectorielle** | XLK #1, XLE bullish crossover | XLI (Industrials) : momentum 0, aucun crossover. Secteur sous-performant le SPY sur 20j/60j. |
| **Exposition FX** | 25 % export, direction USD | Score FX Impact 0,0 — pas de headwind/tailwind détecté. |
| **Score Politique / Géo** | Non flaggué | `data/geo_risk_latest.json` — aucun événement politique détecté pour RKLB. |

**Alignement secteur** : RKLB (Aerospace & Defense) est classé dans Industrials (XLI). Le secteur affiche un momentum nul et sous-performe le SPY sur 20j et 60j. La rotation en cours privilégie la Tech (XLK) et l'Énergie (XLE) — pas favorable à RKLB.

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 80j (2026-08-06) — trop loin pour pricer. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 104×, spot +48 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 4,0/10 | Tendance haussière structurelle (prix > MM50), mais RSI surachat et écart excessif. |
| **Score Opportunité** | **3,7/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | –10 pts | Aucun malus supplémentaire détecté (Accounting, Geo, FX nuls). |
| **Score Global ajusté** | **27,0/100** | **ÉVITER** — Seuil < 35 |

**Rappel de la règle de disqualification** : Score Valorisation ≤ 2/10 → action exclue du rapport long. Ici Val = 3,0/10, donc le titre reste dans le rapport mais avec recommandation ÉVITER.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $124,77 | — |
| **Stop-loss** | $105,47 (–15,5 %) | 2×ATR — inchangé, cohérent avec la volatilité |
| **Take-profit** | $153,72 (+23,2 %) | 3×ATR — inchangé |
| **Ratio R/R** | **1,5 : 1** | **Inférieur au seuil minimum 2:1** pour un trade directionnel à haut beta |

> **Aucune révision nécessaire** — les niveaux techniques et le ratio R/R inchangés ne justifient pas de modification. Le ratio reste défavorable compte tenu du Beta 2,31.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **80 jours** | Est EPS : –$0,06 à –$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). Pas de preview à générer (seuil ≤ 5j).

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER**

Aucun élément nouveau depuis l'analyse du 2026-05-17 ne modifie la thèse. Le titre reste figé à $124,77 dans une configuration de surchauffe technique extrême (RSI 73,28, +57,3 % vs MM50) et de valorisation déconnectée des fondamentaux (Forward P/E –14 644, EV/Rev 104×, spot +48 % vs consensus analystes).

**Points de vigilance** :
1. **Anomalie Max Pain $45** — probable artefact data, à ignorer jusqu'à confirmation.
2. **Écart consensus** — $124,77 vs PT $84,20 = 48 % de premium. Ce niveau ne résiste à aucun benchmark fondamental.
3. **Absence de catalyseur** — 80 jours sans earnings, aucune news structurante, volume en dessous de la moyenne.

**Recommandation** : Maintenir la posture **ÉVITER**. Attendre un retour vers la zone de confluence **$80–$95** (proximité MM50j et compression technique) ou une inflexion matérielle des anticipations de résultats avant toute réévaluation. Toute position longue actuelle expose à un drawdown de –15,5 % (SL) en 1–2 séances compte tenu de l'ATR.

---

*Rapport généré le 2026-05-18 — Données : data/latest.json, data/recommandations_latest.json, data/upcoming_events_latest.json*
