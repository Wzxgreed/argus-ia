# RKLB — Mise à Jour Post-Pipeline (2026-05-18, 21:23 UTC)

> Source : data/latest.json (2026-05-18T21:23:28 UTC) | Recommandations Agent | Validation OK
> **Triggers pipeline :** PRICE_GAP +5,12 % · ATR_SPIKE 7,84 % (confirmés)

---

## 1. Résumé des Changements depuis l'Analyse Précédente

| Métrique | 2026-05-18 20:34 | 2026-05-18 21:23 | Variation |
|---|---|---|---|
| **Cours close** | $131,16 | **$131,16** | **—** |
| **Change % vs veille** | +5,12 % | **+5,12 %** | **—** |
| **RSI 14j** | 77,99 | **77,99** | **—** |
| **ATR 14j** | $10,28 | **$10,28** | **—** |
| **MM 50j** | $80,47 | **$80,47** | **—** |
| **Volume séance** | 32,11 M | **32,15 M** | **+0,1 % (confirmation)** |
| **Volume vs 20j** | 1,21× | **1,21×** | **—** |
| **52W High** | $138,38 | **$138,38** | **—** |
| **Market Cap** | $75,9 Mds | **$75,9 Mds** | **—** |
| **Forward P/E** | –15 394 | **–15 394** | **—** |
| **Price-to-Book** | 41,40× | **41,40×** | **—** |
| **Consensus PT (FMP)** | $84,20 | **$84,20** | **—** |
| **Score Global Agent** | 40,8/100 (aj. 30,8) | **40,8/100** (aj. **30,8**) | **—** |
| **Action Agent** | ÉVITER | **ÉVITER** | **—** |

**Verdict** : Le snapshot final post-pipeline (21:23 UTC) confirme la **stabilisation** des données vs le snapshot 20:34 UTC. Aucune variation significative. Les triggers `PRICE_GAP` (+5,12 %) et `ATR_SPIKE` (7,84 %) détectés par l'agent de surveillance majeure sont désormais intégrés dans le contexte actif. Le scoring agent et la recommandation restent **inchangés** : **ÉVITER**.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 77,99 | Zone de surachat confirmée (>75). Risque de consolidation/correction accru. |
| **ATR 14j** | $10,28 | Volatilité quotidienne stable mais élevée. |
| **MM 50j** | $80,47 | Écart haussier **+62,9 %** vs spot. Tendance très étendue. |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume 20j** | 26 529 273 | Volume du jour **1,21×** moyenne — accélération confirmée. |
| **Beta** | 2,313 | Sensibilité systématique extrême inchangée. |
| **52W High / Low** | **$138,38** / $23,92 | Spot à –5,2 % du 52W high intraday. |
| **Intraday High** | $138,38 | Record historique atteint en séance. |
| **Intraday Low** | $125,68 | — |

**Niveaux clés (inchangés)** :
- Support immédiat : **$125,68** (basse du jour)
- Support technique majeur : **$110,60** (spot – 2×ATR)
- Résistance / Objectif : **$162,00** (spot + 3×ATR)
- Confluence technique : $80–$95 (zone MM50j + compression historique)
- **Max Pain** (éch. 2026-05-22) : **$150,00** — spot $131,16 en dessous de 12,6 % ; pression d'expiration possible si convergence vers $150 d'ici le 22 mai.

**Verdict timing : Défavorable** — Configuration overbought/extended confirmée. Le volume 1,21× en l'absence de news est interprété comme du momentum spéculatif / options flow plutôt que de l'accumulation institutionnelle structurée.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|---|---|---|
| Market Cap | **$75,9 Mds** | Yahoo Finance |
| Forward P/E | **–15 394** | Yahoo Finance |
| EV/Revenue | 104,43× | Yahoo Finance |
| EV/EBITDA | –430,54× | Yahoo Finance |
| Price-to-Book | **41,40×** | Yahoo Finance |
| Short Interest | 5,79 % | Yahoo Finance |
| **FMP Consensus PT** | **$84,20** (15 analysts, 3 couvertures ce mois) | FMP Stable API |
| **FMP Gross Margin** | 34,4 % | FMP Stable API |
| **FMP Debt/Equity** | 0,15 | FMP Stable API |
| **FMP Current Ratio** | 4,08 | FMP Stable API |

**Filtre Qualité (6 critères) — inchangé** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Croissance du segment spatial / lanceurs supérieure à 20 % historique. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif abyssal ; pertes persistantes anticipées. |
| 3. Assets/Liabilities > 1,0 | ✅ Oui | Current Ratio 4,08 ; liquidité solide. Debt/Equity 0,15. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | EV/EBITDA négatif ; absence de génération de cash opérationnel rentable. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique (lanceurs réutilisables légers), mais concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion rapide. |

**Score Qualité total : 3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $131,16 vs PT moyen $84,20 = **+55,8 % au-dessus du consensus sell-side**. Écart anormalement large traduisant un premium spéculatif élevé non adossé aux fondamentaux actuels.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts, 3 couvertures ce mois) | Inchangé |
| **Put/Call ratio** | 0,81 | Inchangé — légèrement baissier (puts > calls en volume). |
| **Call OI %** | 55,2 % | Inchangé — léger biais haussier en open interest. |
| **Max Pain** | $150,00 | Inchangé (échéance 2026-05-22). Spot $131,16 en dessous du max pain. |
| **Short Interest** | 5,79 % | Élevé ; potentiel squeeze si catalyseur majeur, mais absent. |
| **News du jour** | Aucune | `data/news_2026-05-18.json` vide pour RKLB. |
| **Social Sentiment** | 0 mentions, score 0/10 | `data/social_sentiment_2026-05-18.json` — aucune activité retail détectée. |
| **NLP Transcripts** | Indisponible | Plan FMP Starter — transcripts require Enterprise+. |

**Verdict Sentiment :** Neutre / Légèrement baissier — Put/Call 0,81 et absence de momentum retail compensés partiellement par un Call OI à 55,2 %. Consensus sell-side à –35,8 % du spot. Short interest élevé sans catalyseur de squeeze. La hausse de +5,12 % et le volume confirmé ne sont adossés à aucune nouvelle publique.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value 1,0, calibration en cours). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Score 2/10, non exposé. Aucun événement politique détecté. | Aucun malus. |
| **Comptable (Accounting)** | `data/accounting_risk_latest.json` non disponible. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum nul, sous-performe SPY 20j/60j. Top3 = XLK, XLE, XLP. | Malus sectoriel implicite — RKLB dans un secteur sans momentum. |
| **FX Exposure** | Score FX Impact 0,0. Exposition 25 % export, divergence aligned. | Aucun malus/bonus FX. |
| **Event-Driven** | Aucun événement corporate détecté. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le 2026-08-06 (80 jours). Est EPS –$0,06 à –$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 80j — trop loin pour pricer. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 104×, spot +55,8 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 5,5/10 | Tendance haussière structurelle (prix > MM50, 52W high), mais RSI surachat et écart excessif. Volume confirmé 1,21×. |
| **Score Opportunité** | **4,1/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | –10 pts | Malus structurel (surchauffe technique + divergence consensus + absence de catalyseur). |
| **Score Global ajusté** | **30,8/100** | **ÉVITER** — Seuil < 35 |

**Rappel de la règle de disqualification** : Score Valorisation ≤ 2/10 → action exclue du rapport long. Ici Val = 3,0/10 — le titre reste dans le rapport mais avec recommandation ÉVITER.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $131,16 | — |
| **Stop-loss** | $110,60 (–15,7 %) | 2×ATR — inchangé |
| **Take-profit** | $162,00 (+23,5 %) | 3×ATR — inchangé |
| **Ratio R/R** | **1,5 : 1** | **Inférieur au seuil minimum 2:1** pour un trade directionnel à haut beta |

> **Révision** : Les niveaux sont inchangés car le spot et l'ATR sont stables ($131,16 / $10,28). Le ratio R/R reste défavorable compte tenu du Beta 2,31. Toute position longue expose à un drawdown de –15,7 % en 1–2 séances.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **80 jours** | Est EPS : –$0,06 à –$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-05-22 | **4 jours** | Max Pain $150,00 — spot en dessous de 12,6 % |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 22 mai pourrait créer une pression de convergence vers $150 si le volume/options activity s'intensifie, mais absence de signal actuel.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER**

Le snapshot final post-pipeline 21:23 UTC confirme l'**absence de nouveauté fondamentale** malgré la hausse de **+5,12 %** et le 52W high intraday à $138,38. Le titre clôture à **$131,16** dans une configuration de surchauffe technique **confirmée** (RSI 77,99, +62,9 % vs MM50) et de valorisation encore plus déconnectée des fondamentaux (Forward P/E –15 394, EV/Rev 104×, spot **+55,8 %** vs consensus analystes).

**Éléments confirmés vs 20:34** :
1. **Stabilisation volumétrique** : 32,15 M confirmé (vs 32,11 M), soit 1,21× la moyenne 20j. Mouvement non adossé à des news — momentum spéculatif / flow options.
2. **Triggers pipeline intégrés** : `PRICE_GAP` +5,12 % et `ATR_SPIKE` 7,84 % reflètent la volatilité intrinsèque d'un titre à Beta 2,31 en surchauffe. Aucun événement structurant ne modifie la thèse.
3. **RSI 77,99** — surachat technique confirmé. Zone critique (>75).
4. **Écart consensus élargi** — $131,16 vs PT $84,20 = 55,8 % de premium. Ce niveau ne résiste à aucun benchmark fondamental.
5. **Expiration options 2026-05-22** — Max Pain $150, spot en dessous de 12,6 %. Surveillance si convergence imminente.

**Recommandation** : Maintenir la posture **ÉVITER**. Attendre un retour vers la zone de confluence **$80–$95** (proximité MM50j et compression technique) ou une inflexion matérielle des anticipations de résultats avant toute réévaluation. Toute position longue actuelle expose à un drawdown de –15,7 % (SL) en 1–2 séances compte tenu de l'ATR élevé. La hausse de +5,12 % et le volume confirmé ne sont pas des signaux d'achat — ils confirment la déconnexion cours/fondamentaux.

---

*Rapport généré le 2026-05-18 — Données : data/latest.json (2026-05-18T21:23:28), data/recommandations_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/quant_report_latest.json*
