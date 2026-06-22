# RKLB — Mise à Jour 2026-06-22 (Snapshot 21h UTC)

> Source : `data/latest.json` (snapshot 21h UTC) | `data/recommandations_latest.json` | `data/sector_rotation_latest.json` | `data/upcoming_events_latest.json` | `data/events_latest.json` | `data/geo_risk_latest.json` | `data/fx_exposure_latest.json` | `data/social_sentiment_latest.json`
> Date de référence précédente : 2026-06-22 17h UTC (`RKLB_2026-06-22_update_17h.md`)

---

## 1. Résumé des Changements depuis le Snapshot 17h UTC 22/06

| Métrique | Snapshot 17h UTC 22/06 | Snapshot 21h UTC 22/06 | Variation |
|---|---|---|---|
| **Cours close** | $99,61 | **$100,29** | **+0,68 %** — rebond technique post-close |
| **RSI 14j** | 36,14 | **36,44** | **+0,30 pt** — survente étendue stable |
| **ATR 14j** | $10,25 | **$10,25** | Inchangé |
| **MM 50j** | $104,56 | **$104,58** | **+$0,02** — support dynamique remontant |
| **Volume séance** | 17,64 M (0,60×) | **27,54 M (0,92×)** | **🔴 RÉVISION MAJEURE** — volume quasi-normal, pas effondré |
| **Score Global ajusté** | 29,3/100 (ÉVITER) | **29,3/100 (ÉVITER)** | Inchangé |
| **Score Opportunité** | 3,7/10 | **3,7/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 4,0/10 | **4,0/10** | Inchangé |
| **Score Momentum** | 2,5/10 | **2,5/10** | Inchangé |
| **Max Pain (options)** | $69,00 | **$69,00** | Inchangé |
| **Put/Call ratio** | 0,88 | **0,88** | Inchangé |
| **Call OI %** | 53,2 % | **53,2 %** | Inchangé |
| **Earnings Q2 2026** | 45 jours | **45 jours** | Inchangé |

**Verdict** : **Révision volumétrique majeure** — le volume final passe de 0,60× à **0,92× moyenne 20j**. Cette correction invalide l'hypothèse « dérive sans acheteurs » du snapshot 17h UTC. La baisse de −6,48 % s'est faite sur un volume **quasi-normal**, signe de **distribution réelle et active** (vendeurs présents, pas simple absence de demande). Le cours a légèrement rebondi à $100,29 (+0,68 % vs 17h) mais reste **−4,1 % sous la MM50** ($104,58). La thèse **ÉVITER** est confirmée et légèrement renforcée par la révision volumétrique.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 36,44 | Zone de **survente étendue** (<40) intacte. Stable vs 17h. |
| **ATR 14j** | $10,25 | Volatilité inchangée. ATR relatif ~10,2 % — reste élevée. |
| **MM 50j** | $104,58 | **CASSURE CONFIRMÉE** — spot $100,29 = **−4,1 % sous la MM50**. Support transformé en résistance. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 29,89 M | Séance : **27,54 M** — **0,92× moyenne**. Révision drastique : la baisse s'est faite avec participation réelle. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $28,44 | Spot à **−33,6 %** du 52W high (vs −34,0 % à 17h). |

**Niveaux clés** (base ATR $10,25) :
- Résistance immédiate : **$104,58** (MM50 — ancien support, nouvelle résistance)
- Support immédiat : **$100,29** (close du jour)
- Support technique majeur : **$79,79** (spot − 2×ATR — aligné avec SL officiel)
- Support psychologique : **$95,00** puis **$90,00**
- Objectif haussier : **$131,04** (spot + 3×ATR — aligné avec TP officiel)
- Max Pain options : **$69,00** (expiration 26/06 — pinning mécanique)

**Verdict timing : Défavorable** — La cassure de la MM50 est confirmée sur le close officiel. La révision volumétrique à 0,92× invalide l'hypothèse « dérive structurelle sans acheteurs » : les vendeurs étaient bien présents. Le RSI 36,44 reste en zone de survente étendue sans signal de retournement. La prochaine zone de support significative est **$90,00–$95,00**. Tant que le cours reste sous $104,58, la tendance est baissière.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 17h UTC et le snapshot 21h UTC du 22/06. `data/events_latest.json` vide pour RKLB (0 événement corporate). `data/news_latest.json` sans mention significative.

| Métrique | Valeur | Variation vs 17h UTC 22/06 |
|---|---|---|
| Market Cap (Yahoo) | **$62,66 Mds** | Révision vs $61,86 Mds à 17h — écart lié au rebond cours |
| Forward P/E | **−5 708** | Inchangé — aberration data Yahoo |
| EV/Revenue | ~89× | Inchangée |
| P/B (Yahoo) | ~25,5× | Inchangé |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−369×** | Inchangé |
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

**Divergence cours vs consensus** : Spot $100,29 vs PT $90,83 affiche un écart de **+10,4 %** (vs +9,7 % à 17h). Le rebond mécanique post-close élargit légèrement l'écart.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 17h UTC 22/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$69,00** | Inchangé — écart spot/max pain = **+45,3 %** |
| **Put/Call ratio (Yahoo)** | **0,88** | Inchangé |
| **Call OI % (Yahoo)** | **53,2 %** | Inchangé |
| **Expiration options** | 2026-06-26 | J+4 |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options** :
- **Max Pain $69,00** : Niveau de pinning inchangé. Le rebond à $100,29 élargit légèrement l'écart spot/max pain à +45,3 % (vs +44,4 % à 17h). La pression mécanique baissière persiste.
- **Put/Call 0,88** : Léger skew baissier modéré inchangé.
- **Call OI 53,2 %** : Léger skew haussier sur l'open interest inchangé.

**Verdict Sentiment : Neutre légèrement baissier sur le très court terme** — Le pin risk persiste (expiration 26/06, J+4). Le consensus sell-side inchangé à $90,83 reste baissier vs spot. Aucune news, aucun insider trade, aucun upgrade/downgrade. La révision volumétrique à 0,92× confirme que la pression vendeuse était réelle, pas un artefact de liquidité.

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 45 j. Consensus PT stable. Sector rotation Industrials #2 (momentum 7,27/10) — contexte sectoriel favorable mais RKLB sous-performe. |
| **Valorisation** | 4,0/10 | Forward P/E négatif, EV/Rev ~89×, divergence consensus réduite à +10,4 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 2,5/10 | **Effondrement confirmé** — gap −6,48 %, cassure MM50, cours sous MM50 −4,1 %, volume quasi-normal sur baisse (0,92×). Tendance haussière structurelle cassée. |
| **Score Opportunité** | **3,7/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **29,3/100** | **ÉVITER** — Seuil < 35. |

**Comparaison avec le snapshot 17h UTC 22/06** : Le scoring officiel (`recommandations_latest.json`) est **stable à 29,3/100 (ÉVITER)**. La révision volumétrique à 0,92× ne modifie pas les scores quantitatifs mais renforce qualitativement la thèse de distribution institutionnelle active.

**Sector rotation** : XLI (Industrials) #2 avec momentum score 7,27/10 → contexte sectoriel favorable pour RKLB (Aerospace & Defense), mais RKLB sous-performe massivement son secteur.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $100,29 (snapshot 21h UTC 22/06) | — |
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
| **Expiration options** | 2026-06-26 | **4 jours** | Max Pain $69,00 — pin risk baissier (spot +45,3 % au-dessus) |
| **Earnings Q2 2026** | 2026-08-06 | **45 jours** | Est EPS : −$0,15 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 26/06 est un événement technique à surveiller : le max pain $69,00 crée une pression mécanique baissière si le spot ne s'éloigne pas rapidement.

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER — SCORE GLOBAL 29,3/100**

Le snapshot 21h UTC du 22/06 **confirme intégralement** la thèse ÉVITER du snapshot 17h UTC avec une nuance renforcée :

1. 🔴 **Révision volumétrique majeure** — Volume final 27,54 M (0,92×) vs 17,64 M (0,60×) à 17h. La baisse de −6,48 % s'est faite sur volume quasi-normal, invalide l'hypothèse « dérive sans acheteurs ». = **Distribution institutionnelle active confirmée**.
2. 🔴 **Cassure MM50 ($104,58) confirmée** — Spot −4,1 % sous la MM50. Support dynamique brisé.
3. 🟡 **Rebond technique +0,68 % à $100,29** — Mécanique post-close, sans volume supplémentaire. Non significatif.
4. 🟡 **RSI 36,44** — Survente étendue stable. Pas de momentum haussier.
5. 🔴 **Score Global 29,3/100 (ÉVITER)** — Stable. Aucun signal de retournement.
6. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel. Pas de changement fondamental.
7. 🟢 **Sector rotation favorable** — XLI (Industrials) #2 avec momentum 7,27/10. Le contexte sectoriel soutient RKLB mais le titre sous-performe massivement.
8. 🔴 **DRAFT_refresh du 21h UTC confirmé comme vrai événement technique** — Trigger PRICE_GAP −6,48 % + ATR_SPIKE 10,22 % validé.

**Recommandation** : **ÉVITER** — La cassure MM50 sur volume quasi-normal (0,92×) est un signal de distribution institutionnelle confirmé et renforcé. Le ratio R/R 1,5:1 reste insuffisant. Aucune entrée n'est recommandée.

- **Si le cours reclaim $104,58 (MM50)** avec volume >1,0× → reconsidérer vers **SURVEILLER**.
- **Si le cours teste $90,00–$95,00** sur volume >1,5× → zone de survente extrême possible, mais attendre un signal de retournement (candle de reversal, divergence RSI).
- **Pin risk expiration 26/06** : Max Pain $69,00 vs spot $100,29. Surveiller le comportement J+1 à J+4.

Le setup reste **asymétriquement baissier** : la cassure MM50 et la distribution sur volume quasi-normal sont les signaux dominants.

---

*Rapport généré le 2026-06-22 — Snapshot 21h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/geo_risk_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`*
