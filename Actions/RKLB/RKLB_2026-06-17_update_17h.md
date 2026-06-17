# RKLB — Mise à Jour Snapshot 17h UTC 2026-06-17

> Source : `data/latest.json` (snapshot 17h UTC) | `data/recommandations_latest.json` | `RKLB_2026-06-17_DRAFT_refresh.md` (trigger ATR_SPIKE 10,45 %) | Pipeline officiel

---

## 1. Résumé des Changements depuis le Snapshot 13h UTC 17/06

| Métrique | Snapshot 13h UTC 17/06 | Snapshot 17h UTC 17/06 | Variation |
|---|---|---|---|
| **Cours close** | $104,63 | **$109,07** | **+4,24 %** |
| **RSI 14j** | 26,80 | **30,62** | **+3,82 pts** — sortie de la survente stricte (<30) |
| **ATR 14j** | $11,55 | **$11,40** | −1,3 % — volatilité stable |
| **MM 50j** | $102,31 | **$103,16** | +0,83 % — support structurel remonte |
| **Spot vs MM50** | +2,3 % | **+5,7 %** | **Marge de sécurité élargie** |
| **Volume séance** | 27,79 M (1,00×) [pré-ouverture] | **13,60 M** (0,50×) | **Volume effondré** — faible conviction |
| **Score Global ajusté** | 52,0/100 (ATTENDRE) | **47,0/100** (SURVEILLER) | **−5,0 pts** — alignement sur scoring officiel `recommandations_latest.json` |
| **Score Opportunité** | 4,2/10 | **4,2/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé — plafonné FQ ≤3/6 |
| **Score Momentum** | 6,0/10 | **6,0/10** | Inchangé |
| **Max Pain (Yahoo)** | $115,00 | **$115,00** | Inchangé |
| **Put/Call ratio (Yahoo)** | 0,58 | **0,58** | Inchangé — skew haussier modéré |
| **Call OI % (Yahoo)** | 63,3 % | **63,3 %** | Inchangé — positionnement haussier |
| **Forward P/E** | −14 392 | **−15 003** | Inchangé (négatif) |
| **Market Cap** | $65,37 Mds | **$68,15 Mds** | +4,25 % (mécanique avec le cours) |
| **FMP Consensus PT** | $90,83 (18 analysts) | **$90,83 (18 analysts)** | Inchangé |
| **Earnings Q2 2026** | 50 jours | **50 jours** | Inchangé |

**Verdict** : **Rebound technique +4,24 % sur volume effondré 0,50×** — Le cours récupère une partie du repli des séances précédentes mais sur une participation très faible (moitié de la moyenne 20 jours). Le RSI quitte la zone de survente stricte (26,80 → 30,62) mais reste bas. La MM50 remonte lentement ($102,31 → $103,16). Le scoring officiel (`recommandations_latest.json`) maintient l'action **SURVEILLER** à 47,0/100. Le DRAFT_refresh `RKLB_2026-06-17_DRAFT_refresh.md` (17h) porte le même trigger ATR_SPIKE 10,45 % que celui de 13h — il est archivé comme **faux positif** (ATR stable $11,40, pas de spike). Aucun événement structurel détecté.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 30,62 | Sortie de la **🔴 survente stricte** (<30) mais reste en zone de survente étendue (<40). Asymétrie haussière latente intacte. |
| **ATR 14j** | $11,40 | Volatilité stable. ATR relatif 10,45 % — élevée mais inchangée. |
| **MM 50j** | $103,16 | Spot $109,07 = **+5,7 %** au-dessus. Support structurel désormais plus confortable que le snapshot 13h (+2,3 %). |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 27,0 M | Séance : **13,60 M** — **0,50× moyenne**. Faible conviction institutionnelle. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $26,23 | Spot à **−27,8 %** du 52W high (vs −30,7 % à 13h). |

**Niveaux clés** (base ATR $11,40) :
- Support immédiat : **$103,16** (MM50 — marge +5,7 %)
- Support technique majeur : **$86,27** (spot − 2×ATR)
- Support psychologique : **$100,00** puis **$90,00**
- Résistance immédiate : **$113,65** (close 08/06)
- Résistance structurante : **$115,00** (Max Pain options)
- Objectif haussier : **$143,27** (spot + 3×ATR)

**Verdict timing : Neutre** — Le rebond de +4,24 % améliore la posture technique (sortie de survente stricte, allongement de la marge au-dessus de la MM50). Cependant, le volume effondré (0,50×) indique une faible conviction acheteuse. Le setup reste un rebond technique dans une tendance baissière de consolidation. Pas de signal d'achat institutionnel.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 13h et 17h UTC. `data/news_latest.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs 13h UTC 17/06 |
|---|---|---|
| Market Cap (Yahoo) | **$68,15 Mds** | +4,25 % (mécanique cours) |
| Forward P/E | **−15 003** | Inchangé (négatif) |
| EV/Revenue | ~87× | Inchangée |
| P/B (Yahoo) | ~27,7× | Inchangé |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−234,4×** | Inchangé |
| FMP Consensus PT | **$90,83 (18 analysts)** | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($68,15 Mds) vs FMP sous-jacent ($37,02 Mds). Écart inchangé en proportion mais élargi en valeur absolue.

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

**Divergence cours vs consensus** : Spot $109,07 vs PT $90,83 affiche une divergence de **+20,1 %** (élargie par le rebond).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 13h UTC 17/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$115,00** | Inchangé |
| **Put/Call ratio (Yahoo)** | **0,58** | Inchangé — skew haussier modéré |
| **Call OI % (Yahoo)** | **63,3 %** | Inchangé — positionnement haussier |
| **Expiration options** | 2026-06-18 | J+1 (demain) |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options stable** :
- **Max Pain $115,00** : Valeur cohérente et proche des résistances structurantes ($113,65). Spot $109,07 vs Max Pain $115,00 = **écart de +5,4 %** (rétréci par le rebond).
- **Put/Call 0,58** : Ratio inférieur à 1, indiquant un **skew haussier modéré** (plus d'OI calls que puts).
- **Call OI 63,3 %** : Confirme le **positionnement haussier** des détenteurs d'options.
- **Pin risk J+1 (expiration 18/06)** : Le Max Pain ($115,00) est supérieur au spot (+5,4 %). L'écart a diminué grâce au rebond. Un close demain au-dessus de $109 avec momentum vers $113–115 reste plausible si le beta 2,499 amplifie un sentiment macro positif.

**Verdict Sentiment : Neutre légèrement haussier sur les options** — La structure options reste inchangée et favorable (skew haussier). Aucune news, aucun insider trade. Le consensus inchangé à $90,83 suggère que le sell-side maintient sa vue. Le rebond de +4,24 % sans news = mouvement technique / macro (beta 2,499 amplifiant le sentiment global).

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 50 j. Consensus PT stable. Sector rotation Industrials top3 (momentum 7,32/10) — contexte sectoriel légèrement favorable. Options stables (skew haussier). |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev ~87×, divergence consensus +20,1 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 6,0/10 | Rebound +4,24 % à $109,07, RSI 30,62 (proche survente), MM50 sous tension à +5,7 %. Tendance haussière structurelle intacte mais fragile. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel détecté dans `recommandations_latest.json`. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **47,0/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec le snapshot 13h UTC 17/06** : Le scoring officiel (`recommandations_latest.json`) maintient **SURVEILLER** à 47,0/100 ajusté. L'update 13h indiquait 52,0/100 (ATTENDRE) — il s'agissait d'un calcul manuel préliminaire. Le scoring officiel de l'agent Recommandation prévaut : **SURVEILLER**. L'unique évolution mécanique est le rebond +4,24 % qui élargit la marge au-dessus de la MM50 et réduit l'écart avec le Max Pain options.

**Sector rotation** : XLI (Industrials) top3 avec momentum score 7,32/10 → contexte sectoriel légèrement favorable, inchangé.

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $109,07 (snapshot 17h UTC 17/06) | — |
| **Stop-loss** | $86,27 (−20,9 %) | 2×ATR ($11,40) — révisé mécaniquement |
| **Take-profit** | $143,27 (+31,4 %) | 3×ATR ($11,40) — révisé mécaniquement |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 institutionnel |

**Zone d'intérêt technique** :
- **$103,16 (MM50)** : Support structurel. Marge de +5,7 % — plus confortable qu'à 13h (+2,3 %). Cassure = signal baissier majeur.
- **$100,00** : Support psychologique + zone d'accumulation si test.
- **$113,65** : Résistance immédiate (close 08/06). Dépassement = neutralisation du repli.
- **$115,00** : Résistance structurante (Max Pain options). Reclaim = reprise tendance haussière.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Expiration options** | 2026-06-18 | **1 jour** | Max Pain $115,00 — pinning haussier potentiel |
| **Earnings Q2 2026** | 2026-08-06 | **50 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options demain (18/06) est un événement technique à surveiller en raison du Max Pain $115,00 (+5,4 % vs spot).

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — SCORE GLOBAL 47,0/100**

Le snapshot 17h UTC du 17/06 confirme la thèse du snapshot 13h, avec un **rebond technique de +4,24 % qui améliore la posture mais pas la conviction** :

1. 🟢 **Rebond technique +4,24 %** — Cours remonte à $109,07. La proximité critique avec la MM50 est dissipée (+5,7 % vs +2,3 % à 13h).
2. 🔴 **Volume effondré 0,50×** — Le rebond s'effectue sur la moitié de la moyenne 20 jours. Faible conviction institutionnelle. Suspicion de short-covering ou de mouvement beta-driven (2,499) sans catalyst propre.
3. 🟢 **RSI sort de la survente stricte** — 30,62 (>26,80). Asymétrie technique haussière latente renforcée mais toujours en zone de survente étendue.
4. 🟢 **Options stables et cohérentes** — Max Pain $115,00, Put/Call 0,58, Call OI 63,3 %. Skew haussier modéré inchangé. Pin risk J+1 : écart réduit à +5,4 %.
5. 🟢 **MM50 remonte** — $103,16 (+0,83 %), renforçant le support dynamique.
6. 🔴 **Valorisation inchangée** — Forward P/E −15 003, EV/Rev ~87×, divergence consensus +20,1 %. RKLB reste une action de croissance chère et non rentable.
7. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel. Pas d'amélioration fondamentale.
8. 🟡 **DRAFT_refresh 17h archivé** — Trigger ATR_SPIKE 10,45 % identique au snapshot 13h. Aucun nouveau spike ATR (valeur stable $11,40). Faux positif du système de détection. Aucun événement structurel.

**Recommandation** : Maintenir **SURVEILLER** avec vigilance accrue :
- **Expiration options 18/06** : Surveiller le comportement vers $113–115 (Max Pain + résistance structurante). Un close au-dessus de $115 avec volume >1,0× renforcerait la thèse haussière à court terme.
- Si le cours **casse la MM50 ($103,16)** avec volume >1,0× → **ÉVITER** vers $90.
- Si le cours **rebondit et clôture au-dessus de $115,00** avec volume croissant → upgrade possible vers **ATTENDRE** avec nuance positive.
- La zone **$100–$103** reste le support critique absolu à surveiller en temps réel.

Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel. Aucune nouvelle entrée n'est recommandée à ce stade. Le setup reste **asymétrique technique** (survente RSI proche + skew options haussier + rebond sur volume faible) sans catalyseur fondamental.

---

*Rapport généré le 2026-06-17 — Snapshot 17h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`*
