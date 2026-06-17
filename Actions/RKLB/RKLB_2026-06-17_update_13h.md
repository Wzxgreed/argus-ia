# RKLB — Mise à Jour Snapshot 13h UTC 2026-06-17

> Source : `data/latest.json` (snapshot 13h UTC) | `data/recommandations_latest.json` | `RKLB_2026-06-17_DRAFT_refresh.md` (trigger ATR_SPIKE duplicate 11,04 %) | Pipeline officiel

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC 17/06

| Métrique | Snapshot 10h UTC 17/06 | Snapshot 13h UTC 17/06 | Variation |
|---|---|---|---|
| **Cours close** | $104,63 | **$104,63** | **Inchangé** |
| **RSI 14j** | 26,80 | **26,80** | Inchangé — survente confirmée |
| **ATR 14j** | $11,55 | **$11,55** | Inchangé |
| **MM 50j** | $102,31 | **$102,31** | Inchangé — support structurel |
| **Spot vs MM50** | +2,3 % | **+2,3 %** | Inchangé — marge critique |
| **Volume séance** | 27,79 M (1,00×) | **27,79 M** (1,00×) | Inchangé |
| **Score Global ajusté** | 52,0/100 | **52,0/100** | Inchangé — zone ATTENDRE |
| **Score Opportunité** | 4,2/10 | **4,2/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé — plafonné FQ ≤3/6 |
| **Score Momentum** | 6,0/10 | **6,0/10** | Inchangé |
| **Max Pain (Yahoo)** | $35,00 [ANOMALIE] | **$115,00** | **RÉSOLU — valeur cohérente restaurée** |
| **Put/Call ratio (Yahoo)** | null [ANOMALIE] | **0,58** | **RÉSOLU — skew haussier modéré** |
| **Call OI % (Yahoo)** | null [ANOMALIE] | **63,3 %** | **RÉSOLU — positionnement haussier** |
| **Forward P/E** | −14 392 | **−14 392** | Inchangé |
| **Market Cap** | $65,37 Mds | **$65,37 Mds** | Inchangé |
| **FMP Consensus PT** | $90,83 (18 analysts) | **$90,83 (18 analysts)** | Inchangé |
| **Earnings Q2 2026** | 50 jours | **50 jours** | Inchangé |

**Verdict** : **Stabilité mécanique totale** — Seule évolution significative : la **résolution de l'anomalie options JSON** persistante depuis le 10/06. Les données opérationnelles sont rétablies (Max Pain $115,00, Put/Call 0,58, Call OI 63,3 %). Le DRAFT_refresh `RKLB_2026-06-17_DRAFT_refresh.md` (13h) porte le même trigger ATR_SPIKE 11,04 % que celui de 10h — il est archivé comme **artefact duplicate** (aucun nouvel événement technique).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 26,80 | **🔴 Survente technique confirmée** (<30). Asymétrie haussière inchangée. |
| **ATR 14j** | $11,55 | Volatilité stable. ATR relatif 11,0 % — élevée. |
| **MM 50j** | $102,31 | Spot $104,63 = **+2,3 %** au-dessus. Support structurel sous tension. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 27,8 M | Séance : **27,79 M** — **1,00× moyenne**. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $26,23 | Spot à **−30,7 %** du 52W high. |

**Niveaux clés** (base ATR $11,55) :
- Support immédiat : **$102,31** (MM50 — marge +2,3 %)
- Support technique majeur : **$81,53** (spot − 2×ATR)
- Support psychologique : **$90,00** puis **$100,00**
- Résistance immédiate : **$109,25** (previous close)
- Résistance structurante : **$113,65** (close 08/06)
- Objectif haussier : **$139,28** (spot + 3×ATR)

**Verdict timing : Neutre à favorable** — La structure technique est inchangée vs 10h. La proximité de la MM50 ($102,31) reste le facteur dominant. La survente RSI (26,80) continue d'offrir une asymétrie haussière latente. Le marché US n'étant pas encore ouvert (snapshot 13h UTC pré-ouverture), aucun nouveau signal intraday n'est à signaler.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 10h et 13h UTC. `data/news_latest.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs 10h UTC 17/06 |
|---|---|---|
| Market Cap (Yahoo) | **$65,37 Mds** | Inchangé |
| Forward P/E | **−14 392** | Inchangé |
| EV/Revenue | ~87× | Inchangée |
| P/B (Yahoo) | ~26,6× | Inchangé |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−234,4×** | Inchangé |
| FMP Consensus PT | **$90,83 (18 analysts)** | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($65,37 Mds) vs FMP sous-jacent ($37,02 Mds). Écart inchangé.

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

**Divergence cours vs consensus** : Spot $104,63 vs PT $90,83 affiche une divergence de **+15,2 %** (inchangée).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 10h UTC 17/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$115,00** | **RÉSOLU** (was $35,00 aberrant) |
| **Put/Call ratio (Yahoo)** | **0,58** | **RÉSOLU** (was null) |
| **Call OI % (Yahoo)** | **63,3 %** | **RÉSOLU** (was null) |
| **Expiration options** | 2026-06-18 | J+1 (demain) |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options rétablie** :
- **Max Pain $115,00** : Valeur désormais cohérente et proche des résistances structurantes ($113,65). Spot $104,63 vs Max Pain $115,00 = **écart de +9,9 %**.
- **Put/Call 0,58** : Ratio inférieur à 1, indiquant un **skew haussier modéré** (plus d'OI calls que puts).
- **Call OI 63,3 %** : Confirme le **positionnement haussier** des détenteurs d'options.
- **Pin risk J+1 (expiration 18/06)** : Le Max Pain ($115,00) est supérieur au spot (+9,9 %). Cela suggère un **setup de pinning haussier** pour l'expiration de demain. Toutefois, l'écart de +9,9 % en une seule séance est conséquent et dépendra du momentum macro/sectoriel (beta 2,499).

**Verdict Sentiment : Neutre légèrement haussier sur les options** — La résolution de l'anomalie révèle un positionnement options haussier (Put/Call 0,58, Call OI 63,3 %) avec un Max Pain $115,00 qui aligne les intérêts des market makers vers la résistance structurante $113–115. Aucune news, aucun insider trade. Le consensus inchangé à $90,83 suggère que le sell-side maintient sa vue. Le repli de −4,23 % sans news = mouvement technique / macro (beta 2,499 amplifiant le sentiment global).

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 50 j. Consensus PT stable. Sector rotation Industrials top3 (momentum 5,6/10) — légèrement favorable. Options rétablies (skew haussier) — léger bonus latent. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev ~87×, divergence consensus +15,2 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 6,0/10 | Repli consolidé à $104,63, RSI 26,80 (survente), MM50 sous tension à +2,3 %. Tendance haussière structurelle intacte mais fragile. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel détecté dans `recommandations_latest.json`. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **52,0/100** | **ATTENDRE** — Seuil 50–59, stable. |

**Comparaison avec le snapshot 10h UTC 17/06** : Le scoring est **strictement inchangé** à 52,0/100 ajusté (ATTENDRE). L'unique évolution est la **qualité du signal options** : la résolution de l'anomalie JSON confirme un positionnement haussier en OI (Call 63,3 %, Put/Call 0,58) avec un Max Pain $115,00. Cela n'est pas suffisant pour modifier le Score Catalyseur (pas de news fondamentale), mais renforce l'asymétrie technique déjà identifiée.

**Sector rotation** : XLI (Industrials) top3 avec momentum score 5,6/10 → contexte sectoriel légèrement favorable, inchangé.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $104,63 (close 13h UTC 17/06) | — |
| **Stop-loss** | $81,53 (−22,1 %) | 2×ATR ($11,55) — inchangé mécaniquement |
| **Take-profit** | $139,28 (+33,1 %) | 3×ATR ($11,55) — inchangé mécaniquement |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 institutionnel |

**Zone d'intérêt technique** :
- **$102,31 (MM50)** : Support structurel sous tension. Marge de +2,3 % — cassure = signal baissier majeur.
- **$90,00** : Support psychologique + zone d'accumulation si test.
- **$109,25** : Résistance immédiate (previous close). Dépassement = neutralisation du repli.
- **$113,65–$115,00** : Résistance structurante (close 08/06 + Max Pain options). Reclaim = reprise tendance haussière.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Expiration options** | 2026-06-18 | **1 jour** | Max Pain $115,00 — pinning haussier potentiel |
| **Earnings Q2 2026** | 2026-08-06 | **50 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options demain (18/06) est un événement technique à surveiller en raison du Max Pain $115,00 (+9,9 % vs spot).

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 ATTENDRE — SCORE GLOBAL 52,0/100**

Le snapshot 13h UTC du 17/06 confirme intégralement la thèse du snapshot 10h, avec une **amélioration sur la qualité des données options** :

1. 🟢 **Stabilité mécanique totale** — Cours, RSI, ATR, MM50, volume, scores : tous inchangés. Le repli de −4,23 % est consolidé.
2. 🟢 **[ANOMALIE OPTIONS JSON RÉSOLUE]** — Max Pain rétabli à $115,00 (coherent), Put/Call 0,58, Call OI 63,3 %. Le positionnement options est désormais lisible : **skew haussier modéré**.
3. 🟢 **Pin risk J+1 identifié** — Max Pain $115,00 vs spot $104,63 = +9,9 %. L'expiration du 18/06 pourrait générer un pinning vers la résistance $113–115 si le momentum macro/sectoriel (beta 2,499) est favorable.
4. 🔴 **Proximité critique MM50 inchangée** — Spot $104,63 vs MM50 $102,31 = +2,3 %. Le support structurel reste sous tension directe. Une cassure ouvrirait la voie vers $90.
5. 🟢 **RSI en survente confirmée** — 26,80 (<30). Asymétrie technique haussière latente inchangée.
6. 🔴 **Valorisation inchangée** — Forward P/E −14 392, EV/Rev ~87×, divergence consensus +15,2 %. RKLB reste une action de croissance chère et non rentable.
7. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel. Pas d'amélioration fondamentale.
8. 🟡 **DRAFT_refresh 13h archivé** — Artefact duplicate du trigger ATR_SPIKE 11,04 % (déjà validé à 10h). Aucun nouvel événement technique.

**Recommandation** : Maintenir **ATTENDRE** avec vigilance accrue :
- **Expiration options 18/06** : Surveiller le comportement vers $113–115 (Max Pain + résistance structurante). Un close au-dessus de $115 avec volume >1,0× renforcerait la thèse haussière à court terme.
- Si le cours **casse la MM50 ($102,31)** avec volume >1,0× → **SURVEILLER** penchant **ÉVITER** vers $90.
- Si le cours **rebondit et clôture au-dessus de $109,25** avec volume croissant → maintien **ATTENDRE** avec nuance positive.
- La zone **$100–$102** reste le support critique absolu à surveiller en temps réel.

Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel. Aucune nouvelle entrée n'est recommandée à ce stade. Le setup reste **asymétrique technique** (survente RSI + proximité MM50 + skew options haussier rétabli) sans catalyseur fondamental.

---

*Rapport généré le 2026-06-17 — Snapshot 13h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`*
