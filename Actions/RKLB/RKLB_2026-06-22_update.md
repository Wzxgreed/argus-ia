# RKLB — Mise à Jour 2026-06-22 (Snapshot 13h UTC)

> Source : `data/latest.json` (snapshot 13h UTC) | `data/recommandations_latest.json` | `data/sector_rotation_latest.json` | `data/upcoming_events_latest.json` | `data/events_latest.json` | `data/geo_risk_latest.json` | `data/fx_exposure_latest.json` | `data/social_sentiment_latest.json`
> Date de référence précédente : 2026-06-22 10h UTC (RKLB_2026-06-22_update.md)

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC 22/06

| Métrique | Snapshot 10h UTC 22/06 | Snapshot 13h UTC 22/06 | Variation |
|---|---|---|---|
| **Cours close** | $107,24 | **$107,24** | **Inchangé** — aucun nouveau tick de prix |
| **RSI 14j** | 31,05 | **31,05** | Inchangé |
| **ATR 14j** | $11,08 | **$11,08** | Inchangé |
| **MM 50j** | $103,91 | **$103,91** | Inchangé |
| **Volume séance** | 70,33 M (2,34×) | **70,33 M (2,34×)** | Inchangé |
| **Score Global ajusté** | 39,5/100 (SURVEILLER) | **39,5/100 (SURVEILLER)** | Inchangé |
| **Score Opportunité** | 4,0/10 | **4,0/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé — plafonné FQ ≤3/6 |
| **Score Momentum** | 5,0/10 | **5,0/10** | Inchangé |
| **Max Pain (options)** | $45,00 [ANOMALIE] | **$69,00** | **🟢 CORRECTION — anomalie résolue** |
| **Put/Call ratio** | null [ANOMALIE] | **0,88** | **🟢 CORRECTION — anomalie résolue** |
| **Call OI %** | null [ANOMALIE] | **53,2 %** | **🟢 CORRECTION — anomalie résolue** |
| **Earnings Q2 2026** | 45 jours | **45 jours** | Inchangé |

**Verdict** : **Aucun changement de prix ni de métrique technique** entre les deux snapshots du 22/06. Le seul changement significatif est la **correction des données options Yahoo** : Max Pain passe de $45,00 (aberrant, signalé comme corrompu ce matin) à **$69,00** cohérent, Put/Call ratio rétabli à **0,88**, Call OI % à **53,2 %**. Cette restauration des données options modifie légèrement le verdict sentiment (voir section 4). Le scoring officiel (`recommandations_latest.json`) est inchangé à **SURVEILLER 39,5/100**. Le `DRAFT_refresh` du 22/06 (trigger ATR_SPIKE 10,33 %) est traité et archivé comme **faux positif** — volatilité structurelle connue, pas d'événement majeur.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 31,05 | Zone de **survente étendue** (<40) intacte. Aucun changement vs snapshot 10h. |
| **ATR 14j** | $11,08 | Volatilité stable. ATR relatif ~10,3 % — élevée mais inchangée. |
| **MM 50j** | $103,91 | Support dynamique remontant. Spot $107,24 = **+3,2 %** au-dessus. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 30,05 M | Séance : **70,33 M** — **2,34× moyenne**. Explosion volumétrique majeure sur mouvement prix quasi nul. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $28,44 | Spot à **−29,0 %** du 52W high. |

**Niveaux clés** (base ATR $11,08) :
- Support immédiat : **$103,91** (MM50 — marge +3,2 %)
- Support technique majeur : **$85,08** (spot − 2×ATR)
- Support psychologique : **$100,00** puis **$90,00**
- Résistance immédiate : **$109,55** (high du jour)
- Résistance structurante : **$113,65** (close 08/06)
- Objectif haussier : **$140,48** (spot + 3×ATR)

**Verdict timing : Neutre légèrement défavorable** — La compression de la marge au-dessus de la MM50 (+3,2 %) reste le signal technique dominant. L'explosion de volume sur stabilité prix est un pattern de distribution classique. Le RSI 31,05 confirme que la pression vendeuse reste forte malgré la latéralisation. Le support MM50 ($103,91) est le niveau critique absolu : une cassure avec volume >1,0× ouvrirait un target vers $90. À l'inverse, un dépassement de $113,65 avec volume >1,5× réactiverait la thèse haussière.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée entre le snapshot 10h UTC et le snapshot 13h UTC du 22/06. `data/events_latest.json` vide pour RKLB (0 événement corporate). `data/news_latest.json` sans mention significative.

| Métrique | Valeur | Variation vs 10h UTC 22/06 |
|---|---|---|
| Market Cap (Yahoo) | **$67,01 Mds** | Inchangé |
| Forward P/E | **−6 104** | Inchangé |
| EV/Revenue | ~89× | Inchangée |
| P/B (Yahoo) | ~27,3× | Inchangé |
| FMP Gross Margin | **34,43 %** | Inchangé |
| FMP EV/EBITDA | **−369×** | Inchangé |
| FMP Consensus PT | **$90,83 (18 analysts)** | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($67,01 Mds) vs FMP sous-jacent ($37,02 Mds). Écart inchangé.

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

**Divergence cours vs consensus** : Spot $107,24 vs PT $90,83 affiche une divergence de **+18,0 %**.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 10h UTC 22/06 |
|---|---|---|
| **Consensus analystes (FMP)** | $90,83 (18 analysts) | Inchangé |
| **Max Pain (Yahoo)** | **$69,00** | **🟢 CORRECTION — de $45,00 aberrant à $69,00 cohérent** |
| **Put/Call ratio (Yahoo)** | **0,88** | **🟢 CORRECTION — de null à 0,88** |
| **Call OI % (Yahoo)** | **53,2 %** | **🟢 CORRECTION — de null à 53,2 %** |
| **Expiration options** | 2026-06-26 | J+4 |
| **Short Interest** | 5,51 % | Pas de donnée fraîche — inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

**Analyse options rétablie** :
- **Max Pain $69,00** : Niveau de pinning cohérent avec le spot $107,24 (spot > max pain de +55,4 %). Cela signifie que le marché options anticipe une gravitation vers $69,00 à l'expiration du 26/06 — bien en dessous du spot actuel. C'est un signal **baissier latent** sur le très court terme (J+4).
- **Put/Call 0,88** : Légère prédominance puts (skew baissier modéré). Ratio <1 = plus d'appels que de puts en volume, mais le max pain $69,00 indique que les strikes puts dominent la structure OI.
- **Call OI 53,2 %** : Léger skew haussier sur l'open interest (53,2 % calls vs 46,8 % puts). Léger biais haussier des positionnements mais pas significatif.

**Verdict Sentiment : Neutre légèrement baissier sur le très court terme** — La restauration des données options révèle un **pin risk réel** : spot $107,24 vs max pain $69,00 = écart de +55,4 %. Cela crée une pression mécanique baissière vers l'expiration du 26/06 (J+4), surtout si le volume institutionnel reste élevé. Le consensus sell-side inchangé à $90,83 reste baissier vs spot. Aucune news, aucun insider trade, aucun upgrade/downgrade. Le volume explosion 2,34× sans news = mouvement institutionnel ou algorithmique (beta 2,499 amplifiant les flux sectoriels).

---

## 5. Nouveau Scoring Global

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 45 j. Consensus PT stable. Sector rotation Industrials #2 (momentum 6,25/10) — contexte sectoriel favorable. Options rétablies : max pain $69,00 crée un pin risk baissier J+4. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev ~89×, divergence consensus +18,0 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 5,0/10 | Repli −0,69 % à $107,24 sur volume explosion 2,34×, RSI 31,05 (survente étendue), MM50 sous tension à +3,2 %. Tendance haussière structurelle fragilisée. |
| **Score Opportunité** | **4,0/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −0 pt | Aucun malus additionnel. Geo/FX/Social/Event neutres. |
| **Score Global ajusté** | **39,5/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec le snapshot 10h UTC 22/06** : Le scoring officiel (`recommandations_latest.json`) est **strictement inchangé** à 39,5/100 (SURVEILLER). La seule évolution qualitative est la **correction des données options** qui révèle un pin risk baissier (max pain $69,00 vs spot $107,24) absent de l'analyse du matin (données corrompues). Ce pin risk est un facteur de très court terme (expiration 26/06) à surveiller mais ne modifie pas le scoring global.

**Sector rotation** : XLI (Industrials) #2 avec momentum score 6,25/10 → contexte sectoriel favorable pour RKLB (Aerospace & Defense).

---

## 6. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $107,24 (snapshot 13h UTC 22/06) | — |
| **Stop-loss** | $85,08 (−20,7 %) | 2×ATR ($11,08) — inchangé |
| **Take-profit** | $140,48 (+31,0 %) | 3×ATR ($11,08) — inchangé |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 institutionnel |

**Zone d'intérêt technique** :
- **$103,91 (MM50)** : Support structurel. Marge de +3,2 % — réduite et critique. Cassure avec volume >1,0× = signal baissier majeur vers $90.
- **$100,00** : Support psychologique + zone d'accumulation si test.
- **$109,55** : Résistance immédiate (high du jour).
- **$113,65** : Résistance structurante (close 08/06). Dépassement = neutralisation du repli.
- **$69,00** : Max Pain options (expiration 26/06). Niveau de pinning mécanique — non un support technique mais une référence de très court terme.

---

## 7. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Expiration options** | 2026-06-26 | **4 jours** | Max Pain $69,00 — pin risk baissier (spot +55,4 % au-dessus) |
| **Earnings Q2 2026** | 2026-08-06 | **45 jours** | Est EPS : −$0,15 à −$0,02 ; Rev : $0,2 B |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 26/06 est un événement technique à surveiller : le max pain $69,00 crée une pression mécanique baissière si le spot ne s'éloigne pas rapidement.

---

## 8. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — SCORE GLOBAL 39,5/100**

Le snapshot 13h UTC du 22/06 **confirme intégralement** la thèse du snapshot 10h UTC avec un ajustement technique mineur :

1. 🟢 **Correction des données options** — Max Pain $69,00, Put/Call 0,88, Call OI 53,2 % rétablis. L'anomalie JSON récurrente du matin est résolue. Cela révèle un **pin risk baissier** (spot $107,24 vs max pain $69,00) à l'expiration du 26/06.
2. 🔴 **Explosion volumétrique 2,34× sur stabilité prix** — Pattern de distribution institutionnelle classique inchangé.
3. 🟡 **RSI stabilisé en survente étendue** — 31,05. L'asymétrie technique haussière latente persiste mais ne s'active pas.
4. 🔴 **Marge au-dessus de la MM50 compressée** — +3,2 %. Le support dynamique remonte ($103,91) mais le cours ne suit pas aussi vite.
5. 🔴 **Momentum 5,0/10** — Inchangé. Reflet mécanique du repli et du pattern volume-price divergence.
6. 🔴 **Valorisation inchangée** — Forward P/E −6 104, EV/Rev ~89×, divergence consensus +18,0 %. RKLB reste une action de croissance chère et non rentable.
7. 🔴 **Filtre Qualité 3/6 inchangé** — Hors périmètre institutionnel.
8. 🟢 **Sector rotation favorable** — XLI (Industrials) #2 avec momentum 6,25/10. Le contexte sectoriel soutient RKLB.
9. 🟢 **DRAFT_refresh ATR_SPIKE archivé** — Trigger 10,33 % traité comme faux positif / volatilité structurelle. Pas d'événement majeur. Full refresh complété et archivé.

**Recommandation** : Maintenir **SURVEILLER** avec vigilance accrue :
- **Pin risk expiration 26/06** : Max Pain $69,00 vs spot $107,24. Surveiller le comportement du cours J+1 à J+4. Une convergence vers $69,00 serait un mouvement mécanique de −35,6 % — extrême mais théoriquement possible si le volume institutionnel se retourne.
- **Volume explosion 2,34×** : Surveiller les 2–3 prochaines séances. Si le volume reste élevé (>1,5×) avec un break sous $103,91 → **ÉVITER** vers $90.
- Si le cours **rebondit et clôture au-dessus de $113,65** avec volume croissant → upgrade possible vers **ATTENDRE** avec nuance positive.
- La zone **$100–$103,91** reste le support critique absolu à surveiller en temps réel.

Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel. Aucune nouvelle entrée n'est recommandée à ce stade. Le setup reste **asymétrique technique** (survente RSI proche + MM50 remontante) mais le **pattern de distribution volumétrique** et le **pin risk baissier** sont des signaux d'alerte qui l'emportent sur l'asymétrie haussière.

---

*Rapport généré le 2026-06-22 — Snapshot 13h UTC — Données : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/geo_risk_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`*
