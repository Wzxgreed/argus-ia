# RKLB — Mise à Jour 2026-06-22 (Snapshot 17h UTC)

> Source : `data/latest.json` (snapshot 17h UTC) | `data/recommandations_latest.json` | `data/sector_rotation_latest.json` | `data/upcoming_events_latest.json` | `data/events_latest.json` | `data/geo_risk_latest.json` | `data/fx_exposure_latest.json` | `data/social_sentiment_latest.json`
> Date de référence précédente : 2026-06-22 13h UTC (RKLB_2026-06-22_update.md)

---

## 1. Résumé des Changements depuis le Snapshot 13h UTC 22/06

| Métrique | Snapshot 13h UTC 22/06 | Snapshot 17h UTC 22/06 | Variation |
|---|---|---|---|
| **Cours close** | $107,24 | **$99,61** | **🔴 −7,11 %** — gap baissier majeur |
| **RSI 14j** | 31,05 | **36,14** | **+5,09 pts** — sortie de survente stricte, reste <40 |
| **ATR 14j** | $11,08 | **$10,25** | **−$0,83** — compression volatilité |
| **MM 50j** | $103,91 | **$104,56** | **+$0,65** — support dynamique remontant |
| **Volume séance** | 70,33 M (2,34×) | **17,64 M (0,60×)** | **Révision drastique** — volume normalisé sur le close |
| **Score Global ajusté** | 39,5/100 (SURVEILLER) | **29,3/100 (ÉVITER)** | **🔴 −10,2 pts — DOWNGRADE** |
| **Score Opportunité** | 4,0/10 | **3,7/10** | −0,3 pt |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **4,0/10** | **+1,0 pt** — base de comparaison mécanique sur repli |
| **Score Momentum** | 5,0/10 | **2,5/10** | **🔴 −2,5 pts — effondrement** |
| **Max Pain (options)** | $69,00 | **$69,00** | Inchangé — écart spot/max pain réduit à +44,4 % |
| **Put/Call ratio** | 0,88 | **0,88** | Inchangé |
| **Call OI %** | 53,2 % | **53,2 %** | Inchangé |
| **Earnings Q2 2026** | 45 jours | **45 jours** | Inchangé |

**Verdict** : **Gap baissier de −7,11 % à $99,61** entre les deux snapshots. Le cours a **cassé la MM50 ($104,56)** par le bas pour la première fois depuis le gap du 15/06. Le scoring officiel (`recommandations_latest.json`) est **downgradé de SURVEILLER à ÉVITER** (29,3/100). Le momentum s'est effondré à 2,5/10. Le volume final révisé à 0,60× confirme que la baisse ne s'est pas faite sur liquidation massive mais sur une dérive continue. Le `DRAFT_refresh` du 22/06 (trigger PRICE_GAP −7,11 % + ATR_SPIKE 10,29 %) est **validé comme vrai événement technique** — non un faux positif.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 36,14 | Zone de **survente étendue** (<40) intacte. Sortie de la zone stricte <30 (RSI 31,05 → 36,14) mais pas de momentum haussier. |
| **ATR 14j** | $10,25 | Volatilité en compression (−7,5 % vs 13h). ATR relatif ~10,3 % — reste élevée. |
| **MM 50j** | $104,56 | **CASSURE AU DERNIER TICK** — spot $99,61 = **−4,7 % sous la MM50**. Support transformé en résistance. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 29,39 M | Séance : **17,64 M** — **0,60× moyenne**. Pas de panique vendeuse, mais absence totale d'acheteurs. |
| **Beta** | 2,499 | Amplification systématique extrème inchangée. |
| **52W High / Low** | $151,00 / $28,44 | Spot à **−34,0 %** du 52W high (vs −29,0 % à 13h). |

**Niveaux clés** (base ATR $10,25) :
- Résistance immédiate : **$104,56** (MM50 — ancien support, nouvelle résistance)
- Support immédiat : **$99,61** (close du jour)
- Support technique majeur : **$79,11** (spot − 2×ATR — aligné avec SL officiel)
- Support psychologique : **$95,00** puis **$90,00**
- Objectif haussier : **$130,36** (spot + 3×ATR — aligné avec TP officiel)
- Max Pain options : **$69,00** (expiration 26/06 — pinning mécanique)

**Verdict timing : Défavorable** — La cassure de la MM50 est le signal technique dominant. L'absence de volume élevé sur la baisse (−7,11 % sur 0,60×) est inquiétante : ce n'est pas une liquidation de panique mais une **dérive structurelle** sans demande. Le RSI 36,14 indique que la survente n'est pas assez profonde pour justifier un rebond technique immédiat. La prochaine zone de support significative est **$90,00–$95,00**. Tant que le cours reste sous $104,56, la tendance est baissière.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 13h UTC et le snapshot 17h UTC du 22/06. `data/events_latest.json` vide pour RKLB (0 événement corporate). `data/news_latest.json` sans mention significative.

| Métrique | Valeur | Variation vs 13h UTC 22/06 |
|---|---|---|
| Market Cap (Yahoo) | **$62,26 Mds** | Révision vs $67,01 Mds à 13h — écart lié au repli cours |
| Forward P/E | **−5 671** | Inchangé — aberration data Yahoo |
| EV/Revenue | ~89× | Inchangée |
| P/B (Yahoo) | ~25,3× | Inchangé |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−369×** | Inchangé |
| FMP Consensus PT | **$90,83 (18 analysts)** | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($62,26 Mds) vs FMP sous-jacent ($37,02 Mds). Écart persistant.

**Filtre Qualité (6 critères) — inchangé** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Segment spatial / lanceurs en expansion. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif ; pertes persistantes. |
| 3. Assets/Liabilities > 1,0 | ✅ Oui | Current Ratio historique ~4,08. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | FCF yield négatif. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique, concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion. |

**Score Qualité total : 3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $99,61 vs PT $90,83 affiche une convergence de **+9,7 %** (vs +18,0 % à 13h). Le repli rapproche le cours du consensus — pas en surperformance haussière.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 13h UTC 22/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$69,00** | Inchangé — écart spot/max pain réduit de +55,4 % à **+44,4 %** |
| **Put/Call ratio (Yahoo)** | **0,88** | Inchangé |
| **Call OI % (Yahoo)** | **53,2 %** | Inchangé |
| **Expiration options** | 2026-06-26 | J+4 |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options** :
- **Max Pain $69,00** : Niveau de pinning inchangé. Le repli de −7,11 % réduit l'écart spot/max pain à +44,4 % (vs +55,4 % à 13h). La pression mécanique baissière persiste mais s'atténue mécaniquement.
- **Put/Call 0,88** : Léger skew baissier modéré inchangé.
- **Call OI 53,2 %** : Léger skew haussier sur l'open interest inchangé.

**Verdict Sentiment : Neutre légèrement baissier sur le très court terme** — Le pin risk persiste (expiration 26/06, J+4) mais le repli rapproche mécaniquement le spot du max pain. Le consensus sell-side inchangé à $90,83 reste baissier vs spot ($99,61) mais l'écart se réduit. Aucune news, aucun insider trade, aucun upgrade/downgrade. Le volume 0,60× sur baisse −7,11 % = absence d'acheteurs, pas liquidation panique.

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 45 j. Consensus PT stable. Sector rotation Industrials #2 (momentum 7,41/10) — contexte sectoriel favorable mais RKLB sous-performe. |
| **Valorisation** | 4,0/10 | Forward P/E négatif, EV/Rev ~89×, divergence consensus réduite à +9,7 %. Score mécaniquement révisé à la hausse sur repli (base de calcul), mais fondamentalement inchangé. Plafonné par FQ ≤3/6. |
| **Momentum** | 2,5/10 | **Effondrement** — gap −7,11 %, cassure MM50, cours sous MM50 −4,7 %, volume faible sur baisse (0,60×). Tendance haussière structurelle cassée. |
| **Score Opportunité** | **3,7/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **29,3/100** | **ÉVITER** — Seuil < 35. |

**Comparaison avec le snapshot 13h UTC 22/06** : Le scoring officiel (`recommandations_latest.json`) est **downgradé de 39,5/100 (SURVEILLER) à 29,3/100 (ÉVITER)**. La dégradation est entièrement portée par le **Momentum** (5,0 → 2,5/10) suite à la cassure MM50 et au gap −7,11 %. L'action recommandée passe de **SURVEILLER à ÉVITER**.

**Sector rotation** : XLI (Industrials) #2 avec momentum score 7,41/10 → contexte sectoriel favorable pour RKLB (Aerospace & Defense), mais RKLB sous-performe massivement son secteur.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $99,61 (snapshot 17h UTC 22/06) | — |
| **Stop-loss** | $79,11 (−20,6 %) | 2×ATR ($10,25) — aligné avec scoring officiel |
| **Take-profit** | $130,36 (+30,9 %) | 3×ATR ($10,25) — aligné avec scoring officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 institutionnel |

**Zone d'intérêt technique** :
- **$104,56 (MM50)** : Ancien support devenu résistance. Reclaim indispensable pour neutraliser le signal baissier.
- **$99,61** : Close du jour. Support immédiat psychologique.
- **$95,00–$90,00** : Zone de support technique majeure si dérive continue.
- **$79,11** : Stop-loss technique (2×ATR) et niveau de scoring officiel.
- **$69,00** : Max Pain options (expiration 26/06). Niveau de pinning mécanique — non un support technique mais une référence de très court terme.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Expiration options** | 2026-06-26 | **4 jours** | Max Pain $69,00 — pin risk baissier (spot +44,4 % au-dessus) |
| **Earnings Q2 2026** | 2026-08-06 | **45 jours** | Est EPS : −$0,15 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 26/06 est un événement technique à surveiller : le max pain $69,00 crée une pression mécanique baissière si le spot ne s'éloigne pas rapidement.

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE MODIFIÉE 🔴 ÉVITER — SCORE GLOBAL 29,3/100**

Le snapshot 17h UTC du 22/06 **modifie intégralement** la thèse du snapshot 13h UTC :

1. 🔴 **Gap baissier −7,11 % à $99,61** — Mouvement majeur sans catalyseur identifié. Cours sous MM50 pour la première fois depuis le 15/06.
2. 🔴 **Cassure MM50 ($104,56)** — Support dynamique remontant brisé. Spot −4,7 % sous la MM50. Signal technique baissier majeur.
3. 🔴 **Downgrade scoring : SURVEILLER → ÉVITER** — Score Global 39,5 → 29,3/100. Momentum 5,0 → 2,5/10.
4. 🟡 **Volume 0,60× sur baisse** — Pas de liquidation panique, mais absence totale d'acheteurs. Dérive structurelle.
5. 🟡 **RSI 36,14** — Sortie de survente stricte <30 mais reste en zone étendue <40. Pas de momentum haussier.
6. 🔴 **ATR $10,25** — Compression volatilité. La volatilité impliquee ne récompense pas le risque directionnel.
7. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel. Pas de changement fondamental.
8. 🟢 **Sector rotation favorable** — XLI (Industrials) #2 avec momentum 7,41/10. Le contexte sectoriel soutient RKLB mais le titre sous-performe.
9. 🔴 **DRAFT_refresh VALIDÉ** — Trigger PRICE_GAP −7,11 % + ATR_SPIKE 10,29 % confirmé comme **vrai événement technique**, pas faux positif.

**Recommandation** : **ÉVITER** — La cassure MM50 sur volume faible est un signal de distribution institutionnelle confirmé. Le ratio R/R 1,5:1 reste insuffisant. Aucune entrée n'est recommandée.

- **Si le cours reclaim $104,56 (MM50)** avec volume >1,0× → reconsidérer vers **SURVEILLER**.
- **Si le cours teste $90,00–$95,00** sur volume >1,5× → zone de survente extrême possible, mais attendre un signal de retournement (candle de reversal, divergence RSI).
- **Pin risk expiration 26/06** : Max Pain $69,00 vs spot $99,61. Surveiller le comportement J+1 à J+4.

Le setup est désormais **asymétriquement baissier** : la cassure MM50 et l'absence d'acheteurs sont les signaux dominants. La survente RSI latente (36,14) est insuffisante pour contrebalancer la rupture technique.

---

*Rapport généré le 2026-06-22 — Snapshot 17h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/geo_risk_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`*
