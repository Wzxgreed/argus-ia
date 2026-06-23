# RKLB — Mise à Jour 2026-06-23 (Snapshot 10h UTC)

> Source : `data/latest.json` (snapshot 10h UTC) | `data/recommandations_latest.json` | `data/sector_rotation_latest.json` | `data/upcoming_events_latest.json` | `data/events_latest.json` | `data/geo_risk_latest.json` | `data/fx_exposure_latest.json` | `data/social_sentiment_latest.json`
> Date de référence précédente : 2026-06-22 21h UTC (`RKLB_2026-06-22_update_21h.md`)

---

## 1. Résumé des Changements depuis le Snapshot 21h UTC 22/06

| Métrique | Snapshot 21h UTC 22/06 | Snapshot 10h UTC 23/06 | Variation |
|---|---|---|---|
| **Cours close** | $100,29 | **$100,29** | **Inchangé** — stabilité mécanique totale |
| **RSI 14j** | 36,44 | **36,44** | Inchangé — survente étendue stable |
| **ATR 14j** | $10,25 | **$10,25** | Inchangé |
| **MM 50j** | $104,58 | **$104,58** | Inchangé — support transformé en résistance |
| **Volume séance** | 27,54 M (0,92×) | **27,65 M (0,92×)** | Inchangé — distribution sur volume quasi-normal confirmée |
| **Score Global ajusté** | 29,3/100 (ÉVITER) | **29,3/100 (ÉVITER)** | Inchangé |
| **Score Opportunité** | 3,7/10 | **3,7/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 4,0/10 | **4,0/10** | Inchangé |
| **Score Momentum** | 2,5/10 | **2,5/10** | Inchangé |
| **Max Pain (options)** | $69,00 | **$69,00** | [ANOMALIE OPTIONS JSON] — max_pain $45,00 aberrant dans `latest.json`, valeur opérationnelle $69,00 conservée |
| **Put/Call ratio** | 0,88 | **0,88** | [ANOMALIE JSON] — `null` dans `latest.json`, valeur opérationnelle 0,88 conservée |
| **Call OI %** | 53,2 % | **53,2 %** | [ANOMALIE JSON] — `null` dans `latest.json`, valeur opérationnelle 53,2 % conservée |
| **Earnings Q2 2026** | 45 jours | **44 jours** | −1 jour |

**Verdict** : **Stabilité mécanique totale** — le snapshot 10h UTC du 23/06 reprend les données de close officiel du 22/06 sans mutation. L'absence de changement confirme la thèse **ÉVITER** inchangée. La seule variation est la détection d'une **anomalie options JSON récurrente** (max_pain $45,00 aberrant vs $69,00 opérationnel, Put/Call et Call OI corrompus en `null`). Les valeurs opérationnelles du snapshot 21h UTC 22/06 sont conservées.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 36,44 | Zone de **survente étendue** (<40) intacte. |
| **ATR 14j** | $10,25 | Volatilité inchangée. ATR relatif ~10,2 %. |
| **MM 50j** | $104,58 | Spot **−4,1 % sous la MM50**. Support transformé en résistance inchangé. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 29,89 M | Séance : **27,65 M** — **0,92× moyenne**. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $31,78 | Spot à **−33,6 %** du 52W high. |

**Niveaux clés** (base ATR $10,25) :
- Résistance immédiate : **$104,58** (MM50)
- Support immédiat : **$100,29** (close du jour)
- Support technique majeur : **$79,79** (spot − 2×ATR — aligné avec SL officiel)
- Support psychologique : **$95,00** puis **$90,00**
- Objectif haussier : **$131,04** (spot + 3×ATR — aligné avec TP officiel)
- Max Pain options : **$69,00** (expiration 26/06 — pin risk baissier)

**Verdict timing : Défavorable** — La configuration technique est inchangée depuis le close 22/06. Cours sous MM50, RSI en survente étendue sans signal de retournement. Aucun nouveau niveau technique n'a été formé.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 21h UTC 22/06 et le snapshot 10h UTC 23/06. `data/events_latest.json` vide pour RKLB (0 événement corporate). `data/news_latest.json` sans mention significative.

| Métrique | Valeur | Variation vs 21h UTC 22/06 |
|---|---|---|
| Market Cap (Yahoo) | **$62,66 Mds** | Inchangé |
| Forward P/E | **−5 708** | Inchangé — aberration data Yahoo |
| EV/Revenue | ~84× (FMP ~60,6×) | Inchangée |
| P/B (Yahoo) | ~25,5× | Inchangé |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−369×** | Inchangé — aberration structurelle |
| FMP Consensus PT | **$90,83 (18 analysts)** | Inchangé |

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

**Divergence cours vs consensus** : Spot $100,29 vs PT $90,83 affiche un écart de **+10,4 %** (stable).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 21h UTC 22/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$69,00** | [ANOMALIE JSON] — $45,00 aberrant dans `latest.json`, valeur opérationnelle $69,00 conservée |
| **Put/Call ratio (Yahoo)** | **0,88** | [ANOMALIE JSON] — `null` dans `latest.json`, valeur opérationnelle 0,88 conservée |
| **Call OI % (Yahoo)** | **53,2 %** | [ANOMALIE JSON] — `null` dans `latest.json`, valeur opérationnelle 53,2 % conservée |
| **Expiration options** | 2026-06-26 | **J+3** |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options** :
- **Max Pain $69,00** : Niveau de pinning inchangé. Écart spot/max pain = **+45,3 %**. La pression mécanique baissière persiste.
- **Put/Call 0,88** : Léger skew baissier modéré inchangé.
- **Call OI 53,2 %** : Léger skew haussier sur l'open interest inchangé.
- **Anomalie JSON détectée** : `data/latest.json` retourne max_pain $45,00 (aberrant, écart de −34,8 % vs valeur opérationnelle), Put/Call `null` et Call OI `null`. Ces valeurs sont ignorées au profit des données opérationnelles du snapshot 21h UTC 22/06.

**Verdict Sentiment : Neutre légèrement baissier sur le très court terme** — Pin risk persiste (expiration 26/06, J+3). Consensus sell-side inchangé à $90,83, baissier vs spot. Aucune news, aucun insider trade, aucun upgrade/downgrade.

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 44 j. Consensus PT stable. Sector rotation Industrials #2 (momentum 7,54/10) — contexte sectoriel favorable mais RKLB sous-performe massivement. |
| **Valorisation** | 4,0/10 | Forward P/E négatif, EV/Rev ~84×, divergence consensus +10,4 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 2,5/10 | **Effondrement confirmé** — cassure MM50, cours sous MM50 −4,1 %, volume quasi-normal sur baisse (0,92×). Tendance baissière structurelle inchangée. |
| **Score Opportunité** | **3,7/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **29,3/100** | **ÉVITER** — Seuil < 35. |

**Comparaison avec le snapshot 21h UTC 22/06** : Le scoring officiel (`recommandations_latest.json`) est **stable à 29,3/100 (ÉVITER)**. Aucune mutation des données brutes ni des scores quantitatifs.

**Sector rotation** : XLI (Industrials) #2 avec momentum score 7,54/10 → contexte sectoriel favorable pour RKLB (Aerospace & Defense), mais le titre sous-performe massivement son secteur. Aucun bonus sectoriel n'est appliqué étant donné le momentum individuel à 2,5/10.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $100,29 (snapshot 10h UTC 23/06) | — |
| **Stop-loss** | $79,79 (−20,4 %) | 2×ATR ($10,25) — aligné avec scoring officiel |
| **Take-profit** | $131,04 (+30,7 %) | 3×ATR ($10,25) — aligné avec scoring officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 institutionnel |

**Zone d'intérêt technique** :
- **$104,58 (MM50)** : Ancien support devenu résistance. Reclaim indispensable pour neutraliser le signal baissier.
- **$100,29** : Close du jour. Support immédiat psychologique.
- **$95,00–$90,00** : Zone de support technique majeure si dérive continue.
- **$79,79** : Stop-loss technique (2×ATR) et niveau de scoring officiel.
- **$69,00** : Max Pain options (expiration 26/06). Niveau de pinning mécanique — non un support technique mais une référence de très court terme.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Expiration options** | 2026-06-26 | **3 jours** | Max Pain $69,00 — pin risk baissier (spot +45,3 % au-dessus) |
| **Earnings Q2 2026** | 2026-08-06 | **44 jours** | Est EPS : −$0,15 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 26/06 est un événement technique à surveiller : le max pain $69,00 crée une pression mécanique baissière si le spot ne s'éloigne pas rapidement.

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER — SCORE GLOBAL 29,3/100**

Le snapshot 10h UTC du 23/06 **confirme intégralement** la thèse ÉVITER du snapshot 21h UTC 22/06 avec une stabilité mécanique totale :

1. 🔴 **Stabilité mécanique totale** — Cours, RSI, ATR, MM50, volume et scores strictement identiques au close 22/06. Aucune mutation des données brutes.
2. 🔴 **Cassure MM50 ($104,58) inchangée** — Spot −4,1 % sous la MM50. Support transformé en résistance persistant.
3. 🟡 **[ANOMALIE OPTIONS JSON RÉCURRENTRE]** — `latest.json` retourne max_pain $45,00 (aberrant), Put/Call `null`, Call OI `null`. Valeurs opérationnelles du 21h UTC 22/06 conservées ($69,00 / 0,88 / 53,2 %). Cette anomalie récurrente sur RKLB doit être monitorée.
4. 🔴 **Score Global 29,3/100 (ÉVITER)** — Stable. Aucun signal de retournement.
5. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel.
6. 🟢 **Sector rotation favorable** — XLI (Industrials) #2 avec momentum 7,54/10. Le contexte sectoriel soutient RKLB mais le titre sous-performe massivement.
7. 🟡 **RSI 36,44** — Survente étendue stable. Pas de momentum haussier.

**Recommandation** : **ÉVITER** — Aucun changement depuis le close 22/06. La configuration reste asymétriquement baissière avec cassure MM50 confirmée et distribution sur volume quasi-normal. Le ratio R/R 1,5:1 reste insuffisant. Aucune entrée n'est recommandée.

- **Si le cours reclaim $104,58 (MM50)** avec volume >1,0× → reconsidérer vers **SURVEILLER**.
- **Si le cours teste $90,00–$95,00** sur volume >1,5× → zone de survente extrême possible, mais attendre un signal de retournement (candle de reversal, divergence RSI).
- **Pin risk expiration 26/06** : Max Pain $69,00 vs spot $100,29. Surveiller le comportement J+1 à J+3.

Le setup reste **asymétriquement baissier** : la cassure MM50 et la distribution sur volume quasi-normal sont les signaux dominants.

---

*Rapport généré le 2026-06-23 — Snapshot 10h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/geo_risk_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`*
