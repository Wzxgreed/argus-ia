# RKLB — Mise à Jour Snapshot 13h UTC (2026-06-09)

> Source : `data/latest.json` (fetched 2026-06-09T13:00:11 UTC) | `data/recommandations_latest.json` | Snapshot 13h UTC — pipeline officiel

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC (2026-06-09)

| Métrique | Snapshot 10h (09/06) | Snapshot 13h (09/06) | Variation |
|---|---|---|---|
| **Cours close** | $113,65 | **$113,65** | **Inchangé** |
| **RSI 14j** | 41,29 | **41,29** | Inchangé |
| **ATR 14j** | $11,96 | **$11,96** | Inchangé |
| **Volume séance** | 13,38 M (0,47×) | **13,38 M (0,47×)** | Inchangé |
| **Score Global ajusté** | 47,0/100 | **47,0/100** | Inchangé |
| **Score Opportunité** | 4,2/10 | **4,2/10** | Inchangé |
| **Score Momentum** | 6,0/10 | **6,0/10** | Inchangé |
| **Score Valorisation** | 3,0/10 | **3,0/10** | Inchangé |
| **Score Catalyseur** | 4,3/10 | **4,3/10** | Inchangé |
| **Max Pain (JSON)** | $60,00 | **$65,00** | **+8,3 % — résolution partielle** |
| **Put/Call ratio** | 0,0 | **0,79** | **RÉTABLI** |
| **Call OI %** | 100,0 % | **55,8 %** | **RÉTABLI** |
| **Forward P/E** | −15 633 | **−15 633** | Inchangé |
| **EV/Revenue** | 94,96× | **94,96×** | Inchangé |
| **FMP Consensus PT** | $87,19 (16 analysts) | **$87,19 (16 analysts)** | Inchangé |
| **Divergence vs consensus** | +30,3 % | **+30,3 %** | Inchangé |
| **Beta** | 2,499 | **2,499** | Inchangé |
| **MM 50j** | $97,09 | **$97,09** | Inchangé |
| **Earnings Q2 2026** | 58 jours | **58 jours** | Inchangé |

**Verdict** : **Stabilité totale** des cours et des métriques techniques entre le snapshot 10h et le snapshot 13h UTC. L'événement majeur du snapshot 13h est la **résolution partielle de l'anomalie options JSON** observée au snapshot 10h :
- Max Pain remonte de $60,00 à **$65,00** (+8,3 %)
- Put/Call ratio rétabli de 0,0 à **0,79**
- Call OI % rétabli de 100,0 % à **55,8 %**

Ces valeurs restent **aberrantes** vs le spot ($113,65) — Max Pain $65 représente toujours une divergence de −42,8 % — mais le rétablissement du Put/Call et du Call OI confirme le diagnostic d'artefact API Yahoo (snapshot intermédiaire corrompu) plutôt qu'un signal directionnel réel. Les valeurs opérationnelles à retenir restent celles du close 21h du 08/06 : **Max Pain ~$130–$150**, **Put/Call ~0,90**, **Call OI ~53 %**.

Aucune news fondamentale, aucun événement corporate (`events_latest.json` vide). Le DRAFT_refresh `_RKLB_2026-06-09_DRAFT_refresh.md` (trigger ATR_SPIKE 10,52 %) reste un **faux positif** : l'ATR est stable ($11,96), pas en expansion.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 41,29 | Neutre-bas. Inchangé vs snapshot 10h. Pas de survente (< 30). |
| **ATR 14j** | $11,96 | Volatilité élevée stable. Pas d'expansion. Faux positif DRAFT_refresh confirmé. |
| **MM 50j** | $97,09 | Écart haussier **+17,0 %** vs spot. Tendance haussière structurelle intacte. |
| **Volume 20j** | 28 470 205 | Séance : **13,38 M** — **0,47× moyenne**. Participation modérée, stable. |
| **Beta** | 2,499 | Sensibilité systématique extrême. Amplification des mouvements de marché. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−24,7 %** du 52W high. |
| **Range intraday (08/06)** | $111,00 – $116,25 | Amplitude 4,6 %, contenu dans 0,39× ATR. Aucun nouveau range 09/06 (marché fermé entre 10h et 13h UTC). |

**Niveaux clés révisés** (inchangés vs snapshot 10h) :
- Support immédiat : **$111,00** (basse intraday 08/06)
- Support technique majeur : **$89,73** (spot − 2×ATR)
- Support confluence : **$90,00** (zone psychologique)
- Résistance immédiate : **$116,25** (haute intraday 08/06)
- Résistance majeure : **$121,51** (close 03/06)
- Objectif haussier : **$149,53** (spot + 3×ATR)

**Structure options — anomalie JSON partiellement résolue** :
- **Max Pain** : **$65,00** (vs $60,00 au snapshot 10h). Divergence −42,8 % vs spot ($113,65). Amélioration mécanique mais valeur toujours non opérationnelle.
- **Put/Call ratio** : **0,79** — rétabli (vs 0,0 corrompu au snapshot 10h). Proche de la valeur opérationnelle historique (~0,90 au close 21h 08/06).
- **Call OI %** : **55,8 %** — rétabli (vs 100,0 % corrompu au snapshot 10h). Proche de la valeur opérationnelle historique (~52,7 % au close 21h 08/06).
- Expiration la plus proche : **2026-06-12** (3 jours).

**Verdict timing : Favorable** — Cours > MM50 ($97,09). Le RSI à 41,29 laisse de la marge avant la survente. La participation reste modérée (0,47×) sans signe d'accumulation institutionnelle ni de distribution active. La résolution partielle des données options renforce la confiance dans l'absence de signal directionnel extrême à CT.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-09.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs snapshot 10h |
|---|---|---|
| Market Cap (Yahoo) | **$71,01 Mds** | Inchangé |
| Forward P/E | **−15 633** | Inchangé |
| EV/Revenue | 94,96× | Inchangé |
| P/B (Yahoo) | 28,90× | Inchangé |
| P/S (FMP) | 61,51× | Inchangé |
| Short Interest | 5,81 % | Inchangé |
| **FMP Consensus PT** | **$87,19** (16 analysts) | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($71,01 Mds) vs FMP sous-jacent ($37,02 Mds). Écart de 91,8 % inchangé.

**Filtre Qualité (6 critères) — inchangé** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Segment spatial / lanceurs en expansion. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif ; pertes persistantes. |
| 3. Assets/Liabilities > 1,0 | ✅ Oui | Current Ratio 4,08. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | FCF yield négatif. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique, concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion. |

**Score Qualité total : 3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $113,65 vs PT moyen $87,19 = **+30,3 % au-dessus du consensus sell-side**.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 10h |
|---|---|---|
| **Consensus analystes (FMP)** | $87,19 (16 analysts) | Inchangé |
| **Max Pain (JSON)** | $65,00 | Partiellement rétabli (was $60,00) 🟡 |
| **Put/Call ratio** | 0,79 | RÉTABLI (was 0,00) 🟢 |
| **Call OI %** | 55,8 % | RÉTABLI (was 100,0 %) 🟢 |
| **Short Interest** | 5,81 % | Inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Anomalie options JSON partiellement résolue** : Le flux options Yahoo a corrigé entre le snapshot 10h et le snapshot 13h UTC. Put/Call et Call OI sont revenus à des valeurs cohérentes (0,79 et 55,8 %), proches des valeurs opérationnelles du close 21h du 08/06 (0,90 et 52,7 %). Seul le Max Pain reste dégradé ($65,00 vs ~$130–$150 opérationnel), confirmant qu'il s'agit d'un artefact persistant sur cette métrique spécifique de l'API Yahoo. **Diagnostic confirmé : artefact API, pas signal directionnel.**
- **Aucun upgrade/downgrade** détecté, absence totale d'activité retail.

**Verdict Sentiment :** Neutre-bas — Inchangé. La structure options partiellement rétablie ne modifie pas le verdict : aucun signal directionnel net. Prudence requise jusqu'à validation d'une source tierce (CBOE, OPRA) pour le Max Pain.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique RKLB dans `geo_risk_latest.json`. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum score 2,65/10, RS20 vs SPY +0,03 %. Signal **NEUTRAL**. | 🟡 Malus sectoriel implicite. |
| **FX Exposure** | Score FX Impact 0,0. Flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**58 jours**). Est EPS : −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`. | Aucun malus. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **DRAFT_refresh** | Trigger ATR_SPIKE 10,52 % — **FAUX POSITIF**. L'ATR est stable ($11,96). | Archivé, aucun impact thèse. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 58 j. Consensus PT stable. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev ~95×, spot +30,3 % vs consensus. Plafonné par FQ ≤3/6. |
| **Momentum** | 6,0/10 | Rebond +3,24 % vs veille maintenu, RSI 41,29, volume 0,47×. Tendance haussière intacte (prix > MM50) mais fragilisée par la participation modérée. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (valorisation extrême + divergence consensus persistante). |
| **Score Global ajusté** | **47,0/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec snapshot 10h du 09/06** : Le scoring est **intégralement inchangé** (47,0/100). La résolution partielle des données options JSON n'a pas d'impact sur les scores agrégés car les valeurs corrigées (Put/Call 0,79, Call OI 55,8 %) restent dans la fourchette historique et ne modifient pas le verdict Sentiment.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $113,65 | — |
| **Stop-loss** | $89,73 (−21,0 %) | 2×ATR ($11,96) — aligné agent officiel |
| **Take-profit** | $149,53 (+31,6 %) | 3×ATR ($11,96) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Révision vs snapshot 10h du 09/06** : Inchangés. L'ATR est stable ($11,96) et le spot inchangé.

**Zone d'intérêt potentielle** : Un retour vers **$90–$97** (test support psychologique + confluence 2×ATR / MM50) constituerait une zone d'accumulation technique intéressante pour les spéculateurs, sous réserve de **confirmation de volume > 1,0× moyenne**.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **58 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-12 | **3 jours** | Max Pain JSON $65,00 — valeur opérationnelle à privilégier (~$130–$150) |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 12 juin (3 jours) pourrait amplifier la volatilité à court terme. La structure options opérationnelle (Put/Call ~0,90, Call OI ~53 %) ne suggère pas de pinning immédiat autour du Max Pain aberrant JSON.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE 🟡 SURVEILLER — STABILITÉ TOTALE, ANOMALIE OPTIONS PARTIELLEMENT RÉSOLUE, DRAFT_refresh FAUX POSITIF ARCHIVÉ**

Le snapshot du 13h UTC du 09/06 confirme intégralement la thèse du snapshot 10h et du close officiel du 08/06 :

1. ✅ **Cours stable** — $113,65 inchangé. Aucun nouveau gap ni mouvement significatif.
2. ✅ **Anomalie options JSON partiellement résolue** — Put/Call rétabli à 0,79 (vs 0,0), Call OI rétabli à 55,8 % (vs 100,0 %). Max Pain remonte à $65,00 (vs $60,00) mais reste aberrant. Diagnostic confirmé : artefact API Yahoo. Valeurs opérationnelles (close 21h) conservées : Max Pain ~$130–$150, Put/Call ~0,90, Call OI ~53 %.
3. ✅ **Métriques techniques stables** — RSI 41,29, ATR $11,96, MM50 $97,09, volume 0,47× inchangés.
4. ✅ **Fondamentaux inchangés** — Forward P/E −15 633, EV/Rev ~95×, Filtre Qualité 3/6, consensus PT $87,19 stable.
5. ✅ **Scoring inchangé** — Score Global ajusté 47,0/100 (SURVEILLER).
6. ✅ **Niveaux SL/TP inchangés** — SL $89,73, TP $149,53, R/R 1,5:1.
7. ✅ **Aucune news fondamentale** ni événement corporate détecté.
8. ✅ **DRAFT_refresh archivé** — Le trigger ATR_SPIKE 10,52 % est un faux positif (ATR stable $11,96). Pas d'événement majeur justifiant un full refresh.

**Recommandation** : Maintenir la posture **SURVEILLER**. Le setup technique reste identique. L'anomalie options JSON est désormais documentée comme un artefact récurrent de l'API Yahoo et ne modifie pas la thèse. La vigilance reste de mise sur le support $90–$97 (2×ATR / MM50) en cas de poursuite de la distribution.

Attendre :
- Un **retour vers la zone $90–$97** avec **volume supérieur à la moyenne** (confirmation de capitulation), ou
- Une **stabilisation au-dessus de $116,25** (haute du 08/06) avec volume croissant vers 1,0×+ pour confirmer un rebond durable.

Toute position longue actuelle expose à un drawdown de −21,0 % (SL) en 1–2 séances compte tenu du Beta 2,50 et de l'ATR $11,96. Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel.

---

*Rapport généré le 2026-06-09 — Données : `data/latest.json` (13:00 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/quant_report_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
