# RKLB — Mise à Jour Snapshot 10h UTC (2026-06-10)

> Source : `data/latest.json` (fetched 2026-06-10T10:00:11 UTC) | `data/recommandations_latest.json` | Pipeline officiel — **données techniques partielles**

---

## 1. Résumé des Changements depuis le Close Officiel 21h UTC (2026-06-09)

| Métrique | Close 21h (09/06) | Snapshot 10h (10/06) | Variation |
|---|---|---|---|
| **Cours close** | $108,23 | **NaN** [DONNÉES PARTIELLES] | Close indisponible |
| **Previous close** | — | **$113,65** | [ANOMALIE STALE] probablement close 08/06 |
| **RSI 14j** | 40,65 | **42,93** | **+2,28 pts** |
| **ATR 14j** | $12,15 | **null** | [DONNÉES MANQUANTES] |
| **MM 50j** | $98,04 | **null** | [DONNÉES MANQUANTES] |
| **MM 200j** | — | **null** | [DONNÉES MANQUANTES] |
| **Volume séance** | 23,45 M (0,87×) | **23,45 M** (0,87×) | Inchangé |
| **Score Global ajusté** | 44,5/100 | **45,8/100** | **+1,3 pt** |
| **Score Opportunité** | 4,0/10 | **4,6/10** | **+0,6 pt** |
| **Score Catalyseur** | 4,3/10 | **5,3/10** | **+1,0 pt** |
| **Score Valorisation** | 3,0/10 | **4,0/10** | **+1,0 pt** |
| **Score Momentum** | 5,0/10 | **4,5/10** | **−0,5 pt** |
| **Max Pain (JSON)** | $65,00 | **$60,00** | [ANOMALIE JSON RÉCURRENTE] |
| **Put/Call ratio (JSON)** | 0,79 | **0,00** | [ANOMALIE JSON RÉCURRENTE] |
| **Call OI % (JSON)** | 55,8 % | **100,0 %** | [ANOMALIE JSON RÉCURRENTE] |
| **Short Interest** | 5,81 % | **5,51 %** | **−0,30 pt** |
| **Forward P/E** | −14 887 | **−14 887** | Inchangé |
| **EV/Revenue** | 94,96× | **90,34×** | −4,62× (mécanique) |
| **Market Cap Yahoo** | $67,62 Mds | **$67,62 Mds** | Inchangé |
| **FMP Consensus PT** | $87,19 (16 analysts) | **$87,19 (16 analysts)** | Inchangé |
| **Divergence vs consensus** | +24,1 % | **+30,3 %** | [MÉCANIQUE — previous_close stale élevé] |
| **Beta** | 2,499 | **2,499** | Inchangé |
| **Earnings Q2 2026** | 58 jours | **57 jours** | — |

**Verdict** : **Données techniques partielles** sur ce snapshot 10h UTC. Le close du jour est indisponible (NaN) et le `previous_close` à $113,65 correspond vraisemblablement au close du **08/06** ($113,65), non du 09/06 ($108,23) — anomalie stale Yahoo. Seul le RSI est fiable (42,93, +2,28 pts vs close 21h), signalant un léger rebond technique. L'ATR et les moyennes mobiles sont null, empêchant toute révision des niveaux SL/TP sur la base des données du jour. Le scoring global remonte mécaniquement de 44,5 à 45,8/100 (SURVEILLER) mais cette révision repose sur un `previous_close` potentiellement obsolète.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 42,93 | Neutre-bas, légère amélioration depuis 40,65. Reste sous 50, pas de survente. |
| **ATR 14j** | null | [DONNÉES MANQUANTES] — Impossible de calculer les niveaux SL/TP ATR-based. |
| **MM 50j** | null | [DONNÉES MANQUANTES] — Support structurel inconnu sur ce snapshot. |
| **MM 200j** | null | [DONNÉES MANQUANTES] |
| **Volume 20j** | 26 906 567 | Séance : **23,45 M** — **0,87× moyenne**. Participation stable vs hier. |
| **Beta** | 2,499 | Amplification systématique extrême inchangée. |
| **52W High / Low** | $151,00 / $25,24 | Spot indicatif $113,65 (previous_close stale) à **−24,7 %** du 52W high. |

**Niveaux clés** (conservés sur base ATR $12,15 du 09/06, faute de données fraîches) :
- Support immédiat : **$101,20** (basse intraday 09/06)
- Support technique majeur : **$83,93** (spot − 2×ATR $12,15)
- Support confluence critique : **$90,00–$98,04** (zone psychologique + MM50 du 09/06)
- Résistance immédiate : **$113,65** (previous_close stale / close 08/06)
- Résistance majeure : **$119,79** (haute intraday 09/06)
- Objectif haussier : **$144,68** (spot + 3×ATR $12,15)

**Structure options** (anomalie JSON récurrente) :
- **Max Pain** : **$60,00** — divergence −47,2 % vs previous_close. Valeur non opérationnelle ; valeur historique ~$130–$150 conservée.
- **Put/Call ratio** : **0,00** — [ANOMALIE JSON]. Valeur opérationnelle historique ~0,79 conservée.
- **Call OI %** : **100,0 %** — [ANOMALIE JSON]. Valeur opérationnelle historique ~55,8 % conservée.
- Expiration la plus proche : **2026-06-12** (2 jours).

**Verdict timing : Neutre à tempérer** — RSI en légère remontée (42,93) mais absence totale de données ATR et MM50. La tendance haussière structurelle (MM50 $98,04 du 09/06) reste théoriquement intacte tant que le cours ne casse pas cette zone, mais la confirmation nécessite un close fiable. Volume stable (0,87×) sans signal d'accumulation ni de distribution particulière sur ce snapshot.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-10.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs close 21h (09/06) |
|---|---|---|
| Market Cap (Yahoo) | **$67,62 Mds** | Inchangé |
| Forward P/E | **−14 887** | Inchangé |
| EV/Revenue | **90,34×** | −4,62× (mécanique — base cours différente) |
| P/B (Yahoo) | **27,52×** | Inchangé |
| P/S (FMP) | **61,51×** | Inchangé |
| Short Interest | **5,51 %** | −0,30 pt |
| **FMP Consensus PT** | **$87,19** (16 analysts) | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($67,62 Mds) vs FMP sous-jacent ($37,02 Mds). Écart de **82,7 %** inchangé.

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

**Divergence cours vs consensus** : Le `previous_close` stale à $113,65 vs PT moyen $87,19 affiche une divergence mécanique de **+30,3 %**. Sur la base du close confirmé du 09/06 ($108,23), la divergence réelle reste **+24,1 %** — toujours élevée.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs close 21h (09/06) |
|---|---|---|
| **Consensus analystes (FMP)** | $87,19 (16 analysts) | Inchangé |
| **Max Pain (JSON)** | $60,00 | [ANOMALIE JSON RÉCURRENTE] |
| **Put/Call ratio (JSON)** | 0,00 | [ANOMALIE JSON RÉCURRENTE] |
| **Call OI % (JSON)** | 100,0 % | [ANOMALIE JSON RÉCURRENTE] |
| **Short Interest** | 5,51 % | −0,30 pt — léger désengagement des shorts |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Structure options corrompues à nouveau** — Les valeurs JSON (Put/Call 0,00, Call OI 100 %) sont identifiées comme une anomalie récurrente du pipeline. Les métriques directionnelles opérationnelles historiques (~0,79 et ~55,8 %) restent la référence jusqu'à résolution.
- **Short interest en légère baisse** (5,51 % vs 5,81 %) — pas de squeeze setup, mais léger désengagement.
- **Aucun upgrade/downgrade**, absence totale d'activité retail.
- **Aucun insider trade** significatif signalé dans `data/upcoming_events_latest.json`.

**Verdict Sentiment :** Neutre — L'absence de news et d'activité institutionnelle/retail persiste. La baisse du short interest est marginale. La structure options reste inutilisable sur ce snapshot.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique RKLB dans `geo_risk_latest.json`. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum score **10,0/10** (NaN mécanique), signal **NEUTRAL**. | [DONNÉES PARTIELLES] — returns NaN. |
| **FX Exposure** | Score FX Impact **0,0**, flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**57 jours**). Est EPS : −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`. | Aucun malus. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 5,3/10 | Aucune news. Earnings dans 57 j. Consensus PT stable. |
| **Valorisation** | 4,0/10 | Forward P/E négatif, EV/Rev ~90×, divergence consensus +24–30 %. Plafonné par FQ ≤3/6. |
| **Momentum** | 4,5/10 | RSI 42,93 (légère remontée), mais données ATR/MM50 manquantes. Tendance haussière structurelle théoriquement intacte (MM50 $98,04 du 09/06). |
| **Score Opportunité** | **4,6/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (valorisation extrême + divergence consensus persistante). |
| **Score Global ajusté** | **45,8/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec close 21h du 09/06** : Le scoring remonte de **44,5 → 45,8/100** (+1,3 pt), entraîné par la hausse mécanique du Catalyseur (+1,0 pt) et de la Valorisation (+1,0 pt) dans `recommandations_latest.json`, partiellement contrebalancée par la dégradation du Momentum (5,0 → 4,5/10). Cette révision repose sur un `previous_close` stale ($113,65) et des données techniques partielles (ATR/MM50 null) ; elle doit être interprétée avec prudence.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $108,23 (close 09/06) | [DONNÉES PARTIELLES] — close 10/06 indisponible |
| **Stop-loss** | $83,93 (−22,4 %) | 2×ATR ($12,15 du 09/06) — **non révisé**, ATR 10/06 manquant |
| **Take-profit** | $144,68 (+33,7 %) | 3×ATR ($12,15 du 09/06) — **non révisé**, ATR 10/06 manquant |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Zone d’intérêt potentielle** : Un retour vers **$90–$98** (test support psychologique + confluence MM50 du 09/06 / zone critique) constituerait la zone d’accumulation technique à surveiller. Une **cassure sous $98,04 (MM50 du 09/06)** avec volume > 1,0× confirmerait un renversement de tendance haussière et justifierait un passage de SURVEILLER à ÉVITER.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **57 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-12 | **2 jours** | Max Pain JSON $60,00 — [NON OPÉRATIONNEL] |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L’expiration options du 12 juin (2 jours) pourrait amplifier la volatilité à court terme.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE AVEC RÉSERVES 🟡 SURVEILLER — DONNÉES TECHNIQUES PARTIELLES, SCORE GLOBAL 45,8/100**

Le snapshot 10h UTC du 10/06 confirme la posture **SURVEILLER** avec les réserves suivantes :

1. 🟡 **Données techniques partielles** — Close NaN, previous_close stale ($113,65 = probablement close 08/06), ATR null, MM50 null. Seul le RSI (42,93) est fiable et affiche une légère remontée.
2. 🟡 **Options JSON corrompues à nouveau** — Put/Call 0,00 et Call OI 100 % sont une anomalie récurrente. Valeurs opérationnelles historiques (~0,79 / ~55,8 %) conservées.
3. ✅ **Fondamentaux inchangés** — Forward P/E −14 887, EV/Rev ~90×, Filtre Qualité 3/6, consensus PT $87,19 stable.
4. 🟡 **Short interest en légère baisse** — 5,51 % vs 5,81 %, signalant un léger désengagement des shorts sans setup squeeze.
5. 🟡 **Scoring mécaniquement amélioré** — Score Global 45,8/100 (+1,3 pt) mais sur la base d'un `previous_close` potentiellement obsolète et de données techniques incomplètes.
6. 🔴 **Divergence consensus persistante** — +24 à +30 % au-dessus du consensus sell-side selon le cours de référence utilisé.
7. ✅ **Aucune news fondamentale** ni événement corporate — le contexte reste purement technique.

**Recommandation** : Maintenir la posture **SURVEILLER** avec vigilance accrue. En l'absence de données ATR et MM50 fraîches, aucune révision technique significative n'est possible sur ce snapshot :
- La zone **$90–$98** reste le support critique à surveiller (confluence MM50 du 09/06 + psychologique).
- Une **cassure sous $98,04 (MM50)** avec volume > 1,0× confirmerait un renversement de tendance et justifierait un passage à **ÉVITER**.
- Un **rebond confirmé au-dessus de $113,65** (close 08/06) avec volume croissant vers 1,0×+ rétablirait la neutralité technique.

Toute position longue actuelle expose à un drawdown de −22,4 % (SL $83,93) en 1–2 séances compte tenu du Beta 2,50 et de l’ATR $12,15 (dernière valeur connue). Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel.

---

*Rapport généré le 2026-06-10 — Données : `data/latest.json` (10:00 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/quant_report_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
