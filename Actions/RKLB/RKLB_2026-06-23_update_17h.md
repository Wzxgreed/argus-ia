# RKLB — Mise à Jour 2026-06-23 (Snapshot 17h UTC)

> Source : `data/latest.json` (snapshot 17h UTC) | `data/recommandations_latest.json` | `data/sector_rotation_latest.json` | `data/upcoming_events_latest.json` | `data/events_latest.json` | `data/geo_risk_latest.json` | `data/fx_exposure_latest.json` | `data/social_sentiment_latest.json`
> Date de référence précédente : 2026-06-23 13h UTC (`RKLB_2026-06-23_update.md`)

---

## 1. Résumé des Changements depuis le Snapshot 13h UTC 23/06

| Métrique | Snapshot 13h UTC 23/06 | Snapshot 17h UTC 23/06 | Variation |
|---|---|---|---|
| **Cours close** | $100,29 | **$97,51** | **−2,77 %** — repli confirmé, nouveau low du jour $96,025 |
| **RSI 14j** | 36,44 | **34,51** | **−0,93 pt** — survente étendue, approche zone stricte <30 |
| **ATR 14j** | $10,25 | **$10,23** | −$0,02 — volatilité stable |
| **MM 50j** | $104,58 | **$105,17** | **+$0,59** — support dynamique remontant, spot s'éloigne |
| **Volume séance** | 27,66 M (0,92×) | **11,92 M (0,41×)** | **🔴 EFFONDREMENT** — volume coupé de moitié, dérive sans acheteurs |
| **Score Global ajusté** | 29,3/100 (ÉVITER) | **31,8/100 (ÉVITER)** | **+2,5 pts** — toujours sous seuil ÉVITER (< 35) |
| **Score Opportunité** | 3,7/10 | **4,0/10** | **+0,3 pt** |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 4,0/10 | **4,0/10** | Inchangé |
| **Score Momentum** | 2,5/10 | **3,5/10** | **+1,0 pt** — rebond mécanique du score malgré la baisse |
| **Max Pain (options)** | $69,00 | **$69,00** | Inchangé |
| **Put/Call ratio** | 0,91 | **0,91** | Inchangé — skew baissier modéré stable |
| **Call OI %** | 52,4 % | **52,4 %** | Inchangé |
| **Earnings Q2 2026** | 44 jours | **44 jours** | Inchangé |

**Verdict** : **Repli −2,77 % sur volume effondré (0,41×)** — la baisse de ce jour s'est faite sur une participation extrêmement faible (11,92 M vs moyenne 20j 28,84 M). Cette configuration **invalide l'hypothèse « distribution institutionnelle active »** du snapshot 13h UTC (0,92×) et réintroduit la thèse **« dérive sans acheteurs »**. Le spot teste $96,025 (low du jour) et se rapproche de la zone de survente stricte (RSI 34,51). La cassure sous la MM50 s'aggrave : spot −7,3 % sous MM50 $105,17. Le scoring officiel reste **ÉVITER** malgré une légère remontée à 31,8/100.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 34,51 | Zone de **survente étendue** (< 40), proche seuil stricte < 30. |
| **ATR 14j** | $10,23 | Volatilité stable. ATR relatif ~10,5 %. |
| **MM 50j** | $105,17 | **CASSURE AGGRAVÉE** — spot $97,51 = **−7,3 % sous la MM50** (vs −4,1 % à 13h). Support transformé en résistance, écart qui se creuse. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 28 841 909 | Séance : **11 919 783** — **0,41× moyenne**. Effondrement de la participation. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $31,78 | Spot à **−35,4 %** du 52W high (vs −33,6 % à 13h). |
| **Previous Close** | $100,29 | Gap baissier mécanique confirmé sur la séance. |
| **Low du jour** | $96,025 | Test du support psychologique $95,00–$96,00. |

**Niveaux clés** (base ATR $10,23) :
- Résistance immédiate : **$105,17** (MM50 — ancien support, nouvelle résistance, écart aggravé)
- Résistance intermédiaire : **$100,29** (previous close du 22/06)
- Support immédiat : **$97,51** (close du jour)
- Support technique majeur : **$77,05** (spot − 2×ATR — aligné avec SL officiel recommandations)
- Support psychologique : **$95,00** puis **$90,00**
- Objectif haussier : **$128,20** (spot + 3×ATR — aligné avec TP officiel)
- Max Pain options : **$69,00** (expiration 26/06 — pinning mécanique)

**Verdict timing : Défavorable** — La cassure de la MM50 s'aggrave (−7,3 % vs −4,1 %). L'effondrement du volume à 0,41× est le signal dominant : la baisse n'est pas alimentée par des vendeurs agressifs mais par un désert acheteur. C'est une configuration de survente mécanique. Le RSI 34,51 est proche de la zone stricte < 30. La prochaine zone de support significative reste **$90,00–$95,00**. Tant que le cours reste sous $105,17, la tendance est baissière.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 13h UTC et le snapshot 17h UTC du 23/06. `data/events_latest.json` vide pour RKLB (0 événement corporate). `data/news_latest.json` sans mention significative.

| Métrique | Valeur | Variation vs 13h UTC 23/06 |
|---|---|---|
| Market Cap (Yahoo) | **$60,93 Mds** | −$1,73 Mds (lié au repli cours) |
| Market Cap (FMP) | **$37,02 Mds** | Inchangé — divergence Yahoo/FMP persistante |
| Forward P/E | **−5 549,8** | Inchangé — aberration data Yahoo |
| EV/Revenue (Yahoo) | ~83,6× | Inchangée |
| EV/Revenue (FMP) | ~60,6× | Inchangée |
| P/B (Yahoo) | ~24,8× | Inchangé |
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

**Divergence cours vs consensus** : Spot $97,51 vs PT $90,83 affiche un écart de **+7,3 %** (réduit vs +10,4 % à 13h). Le repli mécanique réduit légèrement la divergence mais le consensus reste baissier vs spot.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 13h UTC 23/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$69,00** | Inchangé — écart spot/max pain = **+41,3 %** (vs +45,3 % à 13h) |
| **Put/Call ratio (Yahoo)** | **0,91** | Inchangé — skew baissier modéré stable |
| **Call OI % (Yahoo)** | **52,4 %** | Inchangé — skew haussier sur OI stable |
| **Expiration options** | 2026-06-26 | **J+3** |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options** :
- **Max Pain $69,00** : Niveau de pinning inchangé. Le repli à $97,51 réduit légèrement l'écart spot/max pain à +41,3 % (vs +45,3 %). La pression mécanique baissière persiste mais s'atténue marginalement.
- **Put/Call 0,91** : Skew baissier modéré stable. Aucune mutation de la couverture options.
- **Call OI 52,4 %** : Skew haussier sur l'open interest stable.

**Verdict Sentiment : Neutre légèrement baissier sur le très court terme** — Le pin risk persiste (expiration 26/06, J+3). Le consensus sell-side inchangé à $90,83 reste baissier vs spot. Aucune news, aucun insider trade, aucun upgrade/downgrade. L'effondrement du volume à 0,41× suggère un repli mécanique par absence de demande plutôt que par pression vendeuse agressive.

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 44 j. Consensus PT stable. Sector rotation Industrials #2 (momentum 7,13/10) — contexte sectoriel favorable mais RKLB sous-performe massivement. |
| **Valorisation** | 4,0/10 | Forward P/E négatif, EV/Rev ~83,6×, divergence consensus +7,3 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 3,5/10 | **Effondrement confirmé** — cassure MM50 aggravée (spot −7,3 %), volume effondré 0,41×, RSI 34,51 proche survente stricte. Score officiel remonté à 3,5/10 malgré la dégradation technique brute. |
| **Score Opportunité** | **4,0/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **31,8/100** | **ÉVITER** — Seuil < 35. |

**Comparaison avec le snapshot 13h UTC 23/06** : Le scoring officiel (`recommandations_latest.json`) est remonté à **31,8/100 (ÉVITER)** vs 29,3/100 précédemment. Cette remontée (+2,5 pts) est principalement portée par le Score Opportunité (+0,3 pt → 4,0/10) et le Score Momentum (+1,0 pt → 3,5/10), malgré la dégradation technique brute (cours −2,77 %, MM50 écart aggravé). Cette divergence souligne que le modèle de scoring intègre la faiblesse volumétrique comme un facteur de non-confirmation de la pression vendeuse.

**Sector rotation** : XLI (Industrials) #2 avec momentum score 7,13/10 (vs 7,54/10 à 13h) → contexte sectoriel toujours favorable mais légèrement atténué. RKLB sous-performe massivement son secteur. Aucun bonus sectoriel n'est appliqué.

**FX Exposure** : Exposition 25 %, flag 🟢, FX Impact Score 0,0 — aucun impact. Direction export, divergence aligned. Aucun malus FX.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $97,51 (snapshot 17h UTC 23/06) | — |
| **Stop-loss** | $77,05 (−21,0 %) | 2×ATR ($10,23) — aligné avec scoring officiel |
| **Take-profit** | $128,20 (+31,5 %) | 3×ATR ($10,23) — aligné avec scoring officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 institutionnel |

**Zone d'intérêt technique** :
- **$105,17 (MM50)** : Ancien support devenu résistance. Reclaim indispensable pour neutraliser le signal baissier. Écart aggravé.
- **$100,29** : Previous close (22/06). Resistance intermédiaire.
- **$97,51** : Close du jour. Support immédiat.
- **$95,00–$90,00** : Zone de support technique majeure si dérive continue.
- **$77,05** : Stop-loss technique (2×ATR) et niveau de scoring officiel.
- **$69,00** : Max Pain options (expiration 26/06). Niveau de pinning mécanique — non un support technique mais une référence de très court terme.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Expiration options** | 2026-06-26 | **3 jours** | Max Pain $69,00 — pin risk baissier (spot +41,3 % au-dessus) |
| **Earnings Q2 2026** | 2026-08-06 | **44 jours** | Est EPS : −$0,15 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 26/06 est un événement technique à surveiller : le max pain $69,00 crée une pression mécanique baissière si le spot ne s'éloigne pas rapidement.

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🔴 ÉVITER — SCORE GLOBAL 31,8/100**

Le snapshot 17h UTC du 23/06 **confirme la thèse ÉVITER** avec une nuance technique modifiée :

1. 🔴 **Repli −2,77 % à $97,51** — Cours sous MM50 aggravé (−7,3 % vs −4,1 % à 13h). Low du jour $96,025 teste le support psychologique $95,00.
2. 🟡 **[EFFONDREMENT VOLUMÉTRIQUE]** — Volume 11,92 M (0,41×) vs 27,66 M (0,92×) à 13h. Cette chute drastique invalide l'hypothèse « distribution institutionnelle active » du snapshot 13h et réintroduit la thèse **« dérive sans acheteurs »**. La baisse n'est pas alimentée par des vendeurs agressifs mais par un désert de demande.
3. 🟡 **RSI 34,51** — Survente étendue, proche du seuil stricte < 30. Zone de survente mécanique, sans signal de retournement.
4. 🔴 **Score Global 31,8/100 (ÉVITER)** — Remontée de 2,5 pts vs 29,3/100 mais toujours sous le seuil ÉVITER (< 35). La remontée du Score Momentum (+1,0 pt à 3,5/10) malgré la baisse du cours est une divergence à surveiller.
5. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel. Pas de changement fondamental.
6. 🟢 **Sector rotation favorable** — XLI (Industrials) #2 avec momentum 7,13/10. Le contexte sectoriel soutient RKLB mais le titre sous-performe massivement.
7. 🟡 **Divergence consensus réduite** — Spot vs PT $90,83 : écart +7,3 % (vs +10,4 % à 13h). La décote se réduit mais le consensus reste baissier.
8. 🟡 **Pin risk expiration 26/06** — Max Pain $69,00 vs spot $97,51 (écart +41,3 %, réduit vs +45,3 %). La pression mécanique persiste mais s'atténue.

**Recommandation** : **ÉVITER** — La configuration reste asymétriquement baissière avec cassure MM50 aggravée et dérive sur volume effondré. Le ratio R/R 1,5:1 reste insuffisant. Aucune entrée n'est recommandée. La nuance principale vs le snapshot 13h est le passage de « distribution active » à « dérive sans acheteurs », ce qui ne change pas la direction mais modifie la nature du repli.

- **Si le cours reclaim $105,17 (MM50)** avec volume >1,0× → reconsidérer vers **SURVEILLER**.
- **Si le cours teste $90,00–$95,00** sur volume >1,5× → zone de survente extrême possible, mais attendre un signal de retournement (candle de reversal, divergence RSI).
- **Si le cours casse $90,00** sur volume >1,0× → support technique majeur brisé, risque de poursuite baissière vers $77,05 (SL).
- **Pin risk expiration 26/06** : Max Pain $69,00 vs spot $97,51. Surveiller le comportement J+1 à J+3.

Le setup reste **asymétriquement baissier** : la cassure MM50 aggravée et la dérive sur volume effondré sont les signaux dominants.

---

*Rapport généré le 2026-06-23 — Snapshot 17h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/geo_risk_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`*
