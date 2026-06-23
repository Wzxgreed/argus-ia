# RKLB — Mise à Jour 2026-06-23 (Snapshot 13h UTC)

> Source : `data/latest.json` (snapshot 13h UTC) | `data/recommandations_latest.json` | `data/sector_rotation_latest.json` | `data/upcoming_events_latest.json` | `data/events_latest.json` | `data/geo_risk_latest.json` | `data/fx_exposure_latest.json` | `data/social_sentiment_latest.json`
> Date de référence précédente : 2026-06-23 10h UTC (`RKLB_2026-06-23_update.md`)

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC 23/06

| Métrique | Snapshot 10h UTC 23/06 | Snapshot 13h UTC 23/06 | Variation |
|---|---|---|---|
| **Cours close** | $100,29 | **$100,29** | **Inchangé** — stabilité mécanique totale |
| **RSI 14j** | 36,44 | **36,44** | Inchangé — survente étendue stable |
| **ATR 14j** | $10,25 | **$10,25** | Inchangé |
| **MM 50j** | $104,58 | **$104,58** | Inchangé — support transformé en résistance |
| **Volume séance** | 27,65 M (0,92×) | **27,66 M (0,92×)** | Inchangé — distribution sur volume quasi-normal confirmée |
| **Score Global ajusté** | 29,3/100 (ÉVITER) | **29,3/100 (ÉVITER)** | Inchangé |
| **Score Opportunité** | 3,7/10 | **3,7/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 4,0/10 | **4,0/10** | Inchangé |
| **Score Momentum** | 2,5/10 | **2,5/10** | Inchangé |
| **Max Pain (options)** | $69,00 | **$69,00** | [ANOMALIE OPTIONS JSON RÉSOLUE] — `latest.json` retourne désormais $69,00 (cohérent) vs $45,00 aberrant précédent |
| **Put/Call ratio** | 0,88 | **0,91** | **+0,03 pt** — skew baissier légèrement renforcé |
| **Call OI %** | 53,2 % | **52,4 %** | **−0,8 pt** — skew haussier sur OI légèrement atténué |
| **Earnings Q2 2026** | 44 jours | **44 jours** | Inchangé |

**Verdict** : **Stabilité mécanique totale** — le snapshot 13h UTC du 23/06 reprend les données de close officiel du 22/06 sans mutation. L'absence de changement confirme la thèse **ÉVITER** inchangée. La principale évolution est la **résolution de l'anomalie options JSON récurrente** : `latest.json` retourne désormais un Max Pain $69,00 cohérent (vs $45,00 aberrant sur les snapshots précédents). Le Put/Call et le Call OI sont également restaurés à des valeurs exploitables (0,91 et 52,4 % vs `null` précédemment). Ces valeurs remplacent les données opérationnelles manuelles utilisées depuis le 22/06.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 36,44 | Zone de **survente étendue** (<40) intacte. |
| **ATR 14j** | $10,25 | Volatilité inchangée. ATR relatif ~10,2 %. |
| **MM 50j** | $104,58 | Spot **−4,1 % sous la MM50**. Support transformé en résistance inchangé. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 29,89 M | Séance : **27,66 M** — **0,92× moyenne**. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $31,78 | Spot à **−33,6 %** du 52W high. |

**Niveaux clés** (base ATR $10,25) :
- Résistance immédiate : **$104,58** (MM50)
- Support immédiat : **$100,29** (close du jour)
- Support technique majeur : **$79,79** (spot − 2×ATR — aligné avec SL officiel)
- Support psychologique : **$95,00** puis **$90,00**
- Objectif haussier : **$131,04** (spot + 3×ATR — aligné avec TP officiel)
- Max Pain options : **$69,00** (expiration 26/06 — pin risk baissier)

**Verdict timing : Défavorable** — La configuration technique est strictement inchangée depuis le snapshot 10h UTC. Cours sous MM50, RSI en survente étendue sans signal de retournement. Aucun nouveau niveau technique n'a été formé.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 10h UTC et le snapshot 13h UTC du 23/06. `data/events_latest.json` vide pour RKLB (0 événement corporate).

| Métrique | Valeur | Variation vs 10h UTC 23/06 |
|---|---|---|
| Market Cap (Yahoo) | **$62,66 Mds** | Inchangé |
| Market Cap (FMP) | **$37,02 Mds** | Inchangé — divergence Yahoo/FMP persistante |
| Forward P/E | **−5 708** | Inchangé — aberration data Yahoo |
| EV/Revenue (Yahoo) | ~83,6× | Inchangée |
| EV/Revenue (FMP) | ~60,6× | Inchangée |
| P/B (Yahoo) | ~25,5× | Inchangé |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−234×** | Inchangé — aberration structurelle |
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

| Signal | Valeur | Évolution vs 10h UTC 23/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$69,00** | [ANOMALIE JSON RÉSOLUE] — `latest.json` retourne $69,00 (cohérent) |
| **Put/Call ratio (Yahoo)** | **0,91** | Restauré depuis `null` — skew baissier modéré légèrement renforcé vs 0,88 |
| **Call OI % (Yahoo)** | **52,4 %** | Restauré depuis `null` — skew haussier sur OI légèrement atténué vs 53,2 % |
| **Expiration options** | 2026-06-26 | **J+3** |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options** :
- **Max Pain $69,00** : Niveau de pinning inchangé. Écart spot/max pain = **+45,3 %**. La pression mécanique baissière persiste. L'anomalie JSON est résolue : la valeur $69,00 est désormais native dans `latest.json`.
- **Put/Call 0,91** : Skew baissier modéré, légèrement renforcé vs 0,88. Indique une couverture put accrue.
- **Call OI 52,4 %** : Skew haussier sur l'open interest, légèrement atténué vs 53,2 %.
- **Résolution anomalie** : Contrairement aux snapshots 10h UTC 23/06 et 21h UTC 22/06, `data/latest.json` ne retourne plus de valeurs aberrantes ($45,00 / `null`). Les métriques options sont désormais exploitables nativement.

**Verdict Sentiment : Neutre légèrement baissier sur le très court terme** — Pin risk persiste (expiration 26/06, J+3). Consensus sell-side inchangé à $90,83, baissier vs spot. Aucune news, aucun insider trade, aucun upgrade/downgrade. Le léger rehaussement du Put/Call à 0,91 confirme une couverture baissière modérée.

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 44 j. Consensus PT stable. Sector rotation Industrials #2 (momentum 7,54/10) — contexte sectoriel favorable mais RKLB sous-performe massivement. |
| **Valorisation** | 4,0/10 | Forward P/E négatif, EV/Rev ~83,6×, divergence consensus +10,4 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 2,5/10 | **Effondrement confirmé** — cassure MM50, cours sous MM50 −4,1 %, volume quasi-normal sur baisse (0,92×). Tendance baissière structurelle inchangée. |
| **Score Opportunité** | **3,7/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **29,3/100** | **ÉVITER** — Seuil < 35. |

**Comparaison avec le snapshot 10h UTC 23/06** : Le scoring officiel (`recommandations_latest.json`) est **stable à 29,3/100 (ÉVITER)**. Aucune mutation des données brutes ni des scores quantitatifs.

**Sector rotation** : XLI (Industrials) #2 avec momentum score 7,54/10 → contexte sectoriel favorable pour RKLB (Aerospace & Defense), mais le titre sous-performe massivement son secteur. Aucun bonus sectoriel n'est appliqué étant donné le momentum individuel à 2,5/10.

**FX Exposure** : Exposition 25 %, flag 🟢, FX Impact Score 0,0 — aucun impact. Direction export, divergence aligned. Aucun malus FX.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $100,29 (snapshot 13h UTC 23/06) | — |
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

Le snapshot 13h UTC du 23/06 **confirme intégralement** la thèse ÉVITER du snapshot 10h UTC avec une stabilité mécanique totale :

1. 🔴 **Stabilité mécanique totale** — Cours, RSI, ATR, MM50, volume et scores strictement identiques au snapshot 10h UTC. Aucune mutation des données brutes.
2. 🟢 **[ANOMALIE OPTIONS JSON RÉSOLUE]** — `latest.json` retourne désormais Max Pain $69,00 (cohérent), Put/Call 0,91 et Call OI 52,4 %. Les valeurs aberrantes ($45,00 / `null`) des snapshots précédents ne se reproduisent plus. Cette résolution retire une incertitude data mais ne modifie pas la thèse.
3. 🔴 **Cassure MM50 ($104,58) inchangée** — Spot −4,1 % sous la MM50. Support transformé en résistance persistant.
4. 🟡 **Put/Call 0,91** — Léger rehaussement du skew baissier (+0,03 pt), cohérent avec la couverture protectrice avant expiration J+3.
5. 🔴 **Score Global 29,3/100 (ÉVITER)** — Stable. Aucun signal de retournement.
6. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel.
7. 🟢 **Sector rotation favorable** — XLI (Industrials) #2 avec momentum 7,54/10. Le contexte sectoriel soutient RKLB mais le titre sous-performe massivement.
8. 🟡 **RSI 36,44** — Survente étendue stable. Pas de momentum haussier.

**Recommandation** : **ÉVITER** — Aucun changement depuis le snapshot 10h UTC. La configuration reste asymétriquement baissière avec cassure MM50 confirmée et distribution sur volume quasi-normal. Le ratio R/R 1,5:1 reste insuffisant. Aucune entrée n'est recommandée.

- **Si le cours reclaim $104,58 (MM50)** avec volume >1,0× → reconsidérer vers **SURVEILLER**.
- **Si le cours teste $90,00–$95,00** sur volume >1,5× → zone de survente extrême possible, mais attendre un signal de retournement (candle de reversal, divergence RSI).
- **Pin risk expiration 26/06** : Max Pain $69,00 vs spot $100,29. Surveiller le comportement J+1 à J+3.

Le setup reste **asymétriquement baissier** : la cassure MM50 et la distribution sur volume quasi-normal sont les signaux dominants.

---

*Rapport généré le 2026-06-23 — Snapshot 13h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/geo_risk_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`*
