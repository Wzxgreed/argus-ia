# RKLB — Mise à Jour Close Officiel 21h UTC (2026-06-09)

> Source : `data/latest.json` (fetched 2026-06-09T21:00:11 UTC) | `data/recommandations_latest.json` | Close officiel 21h UTC — pipeline officiel

---

## 1. Résumé des Changements depuis le Snapshot 13h UTC (2026-06-09)

| Métrique | Snapshot 13h (09/06) | Close 21h (09/06) | Variation |
|---|---|---|---|
| **Cours close** | $113,65 | **$108,23** | **−4,77 %** 🔴 |
| **RSI 14j** | 41,29 | **40,65** | −0,64 pt |
| **ATR 14j** | $11,96 | **$12,15** | **+1,6 %** |
| **MM 50j** | $97,09 | **$98,04** | +$0,95 |
| **Volume séance** | 13,38 M (0,47×) | **23,45 M** | **+75,3 %** — **0,87× moy.** |
| **Score Global ajusté** | 47,0/100 | **44,5/100** | **−2,5 pts** 🔴 |
| **Score Opportunité** | 4,2/10 | **4,0/10** | −0,2 pt |
| **Score Momentum** | 6,0/10 | **5,0/10** | **−1,0 pt** 🔴 |
| **Score Valorisation** | 3,0/10 | 3,0/10 | Inchangé |
| **Score Catalyseur** | 4,3/10 | 4,3/10 | Inchangé |
| **Max Pain (JSON)** | $65,00 | $65,00 | Inchangé — toujours aberrant |
| **Put/Call ratio** | 0,79 | 0,79 | Inchangé |
| **Call OI %** | 55,8 % | 55,8 % | Inchangé |
| **Forward P/E** | −15 633 | **−14 887** | Mécanique (cours ↓) |
| **Market Cap Yahoo** | $71,01 Mds | **$67,62 Mds** | −4,8 % |
| **FMP Consensus PT** | $87,19 (16 analysts) | $87,19 (16 analysts) | Inchangé |
| **Divergence vs consensus** | +30,3 % | **+24,1 %** | Réduite mécaniquement |
| **Beta** | 2,499 | 2,499 | Inchangé |
| **Earnings Q2 2026** | 58 jours | 58 jours | Inchangé |

**Verdict** : **Distribution technique confirmée** en fin de séance. Le cours recule de −4,77 % sur une participation en nette hausse (volume 0,87× vs 0,47× au snapshot 13h), confirmant que le mouvement est soutenu par des flux réels et non un artefact de marché. L’ATR progresge légèrement ($12,15 vs $11,96), validant le trigger `ATR_SPIKE` du DRAFT_refresh 21h (**vrai trigger cette fois**, vs faux positif 13h). Aucune news fondamentale ni événement corporate (`data/events_latest.json` vide). Le repli s’inscrit dans la correction sectorielle : FLY −7,56 %, PLTR −3,22 %, secteur spatial / tech sous pression.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 40,65 | Neutre-bas. Pas de survente (< 30) mais dégradation continue depuis 70+ début juin. |
| **ATR 14j** | $12,15 | Volatilité en légère expansion (+1,6 %). Confirme le trigger ATR_SPIKE du DRAFT_refresh. |
| **MM 50j** | $98,04 | Écart haussier réduit à **+10,4 %** vs spot. Tendance haussière structurelle **intacte mais fragilisée**. |
| **Volume 20j** | 26 906 567 | Séance : **23,45 M** — **0,87× moyenne**. Participation quasi-normale, nette hausse vs 13h. |
| **Beta** | 2,499 | Amplification systématique extrême. Le −4,77 % de RKLB surpasse le repli du SPY (−0,3 % environ). |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−28,3 %** du 52W high (vs −24,7 % au snapshot 13h). |
| **Range intraday (09/06)** | $101,20 – $119,79 | Amplitude **17,2 %**, soit **1,41× ATR**. Volatilité intraday élevée, clôture proche du bas de range. |

**Niveaux clés révisés** (vs snapshot 13h) :
- Support immédiat : **$101,20** (basse intraday 09/06) — **testé et temporairement cassé en séance**
- Support technique majeur : **$83,93** (spot − 2×ATR)
- Support confluence critique : **$90,00–$98,04** (zone psychologique + MM50)
- Résistance immédiate : **$113,65** (close 13h / ancien support)
- Résistance majeure : **$119,79** (haute intraday 09/06)
- Objectif haussier : **$144,68** (spot + 3×ATR)

**Structure options** (inchangée vs 13h) :
- **Max Pain** : **$65,00** — divergence −39,9 % vs spot ($108,23). Valeur toujours non opérationnelle ; valeur historique ~$130–$150 conservée.
- **Put/Call ratio** : **0,79** — inchangé, proche valeur opérationnelle historique (~0,90).
- **Call OI %** : **55,8 %** — inchangé, proche valeur historique (~53 %).
- Expiration la plus proche : **2026-06-12** (3 jours).

**Verdict timing : Favorable à tempérer** — Cours > MM50 ($98,04) mais l’écart s’est réduit à +10,4 %. Le RSI à 40,65 laisse de la marge avant la survente. La hausse de volume (0,87×) confirme que la distribution est active. La clôture proche du bas de range ($101,20–$119,79) est baissière à très court terme. Surveillance impérative du support $98,04 (MM50).

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-09.json` vide pour RKLB. `data/events_latest.json` vide (0 événement corporate).

| Métrique | Valeur | Variation vs snapshot 13h |
|---|---|---|
| Market Cap (Yahoo) | **$67,62 Mds** | −4,8 % (aligné baisse cours) |
| Forward P/E | **−14 887** | Mécanique (cours ↓) |
| EV/Revenue | 94,96× | Inchangé |
| P/B (Yahoo) | 27,52× | Inchangé |
| P/S (FMP) | 61,51× | Inchangé |
| Short Interest | 5,81 % | Inchangé |
| **FMP Consensus PT** | **$87,19** (16 analysts) | Inchangé |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($67,62 Mds) vs FMP sous-jacent ($37,02 Mds). Écart de 82,7 % (vs 91,8 % au snapshot 13h), réduit mécaniquement par la baisse du cours.

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

**Divergence cours vs consensus** : Spot $108,23 vs PT moyen $87,19 = **+24,1 % au-dessus du consensus sell-side** (vs +30,3 % au snapshot 13h). La baisse de cours réduit mécaniquement la divergence mais le surcroît reste significatif.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 13h |
|---|---|---|
| **Consensus analystes (FMP)** | $87,19 (16 analysts) | Inchangé |
| **Max Pain (JSON)** | $65,00 | Inchangé — aberration persistante |
| **Put/Call ratio** | 0,79 | Inchangé |
| **Call OI %** | 55,8 % | Inchangé |
| **Short Interest** | 5,81 % | Inchangé |
| **News du jour** | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |

- **Structure options stable** — Les valeurs corrigées au snapshot 13h (Put/Call 0,79, Call OI 55,8 %) se sont maintenues au close 21h, confirmant le diagnostic d’artefact API Yahoo sur le Max Pain uniquement. Les métriques directionnelles (Put/Call, Call OI) restent cohérentes.
- **Aucun upgrade/downgrade** détecté, absence totale d’activité retail.
- **Aucun insider trade** significatif signalé dans `data/upcoming_events_latest.json`.

**Verdict Sentiment :** Neutre-bas — L’absence totale de news et d’activité institutionnelle/retail confirme que le repli de −4,77 % est **purément technique / sectoriel**. La structure options stable ne modifie pas le verdict.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `1.0`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique RKLB dans `geo_risk_latest.json`. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) momentum score **3,52/10**, RS20 vs SPY **+0,62 %**. Signal **NEUTRAL** amélioré (vs 2,65/10, +0,03 % au snapshot 13h). | 🟡 Léger bonus sectoriel implicite, insuffisant contrebalancer la baisse. |
| **FX Exposure** | Score FX Impact 0,0. Flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**58 jours**). Est EPS : −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`. | Aucun malus. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **DRAFT_refresh 21h** | Trigger ATR_SPIKE 11,23 % — **VALIDÉ**. Cours −4,77 % + ATR expansion + volume hausse. | **Vrai trigger**, pas faux positif. Intégré dans cette analyse. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news. Earnings dans 58 j. Consensus PT stable. |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev ~95×, spot +24,1 % vs consensus. Plafonné par FQ ≤3/6. |
| **Momentum** | 5,0/10 | Repli −4,77 % confirmé par volume hausse, RSI 40,65, tendance haussière intacte mais fragilisée (écart MM50 réduit à +10,4 %). |
| **Score Opportunité** | **4,0/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (valorisation extrême + divergence consensus persistante). |
| **Score Global ajusté** | **44,5/100** | **SURVEILLER** — Seuil 35–49. |

**Comparaison avec snapshot 13h du 09/06** : Le scoring baisse de **47,0 → 44,5/100** (−2,5 pts), entraîné principalement par la dégradation du Momentum (6,0 → 5,0/10) et de la dynamique de cours. La baisse du Score Opportunité (4,2 → 4,0) reflète le repli technique. Le ticker reste dans la fourchette SURVEILLER.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d’entrée (spot)** | $108,23 | — |
| **Stop-loss** | $83,93 (−22,4 %) | 2×ATR ($12,15) — aligné agent officiel |
| **Take-profit** | $144,68 (+33,7 %) | 3×ATR ($12,15) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Révision vs snapshot 13h du 09/06** : SL/TP révisés à la baisse en raison de la chute du spot (−4,77 %) et de l’expansion ATR (+$0,19). Le ratio R/R reste insuffisant.

**Zone d’intérêt potentielle** : Un retour vers **$90–$98** (test support psychologique + confluence MM50 / zone critique) constituerait la zone d’accumulation technique à surveiller. Une **cassure sous $98,04 (MM50)** avec volume > 1,0× confirmerait un renversement de tendance haussière et justifierait un passage de SURVEILLER à ÉVITER.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **58 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-12 | **3 jours** | Max Pain JSON $65,00 — valeur opérationnelle à privilégier (~$130–$150) |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L’expiration options du 12 juin (3 jours) pourrait amplifier la volatilité à court terme, surtout avec un Max Pain aberrant JSON.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE MODIFIÉE 🔴 SURVEILLER — DISTRIBUTION TECHNIQUE CONFIRMÉE, SCORE GLOBAL RÉDUIT À 44,5/100**

Le close officiel 21h UTC du 09/06 modifie la thèse du snapshot 13h :

1. 🔴 **Cours en repli significatif** — $108,23 (−4,77 % vs 13h). Distribution active confirmée par la hausse de volume (0,87× vs 0,47×) et la clôture proche du bas de range ($101,20).
2. 🔴 **ATR_SPIKE validé** — Le trigger ATR_SPIKE 11,23 % du DRAFT_refresh 21h est **un vrai événement technique** (vs faux positif 13h). L’ATR progresge à $12,15 et le cours chute.
3. 🟡 **Métriques techniques dégradées** — RSI 40,65 (bas), écart MM50 réduit à +10,4 %, 52W high désormais à −28,3 %.
4. ✅ **Fondamentaux inchangés** — Forward P/E −14 887, EV/Rev ~95×, Filtre Qualité 3/6, consensus PT $87,19 stable. La baisse est purement technique.
5. 🔴 **Scoring réduit** — Score Global ajusté 44,5/100 (SURVEILLER, −2,5 pts). Score Opportunité 4,0/10, Momentum 5,0/10.
6. 🔴 **Niveaux SL/TP révisés** — SL $83,93, TP $144,68, R/R 1,5:1.
7. ✅ **Aucune news fondamentale** ni événement corporate — le repli s’inscrit dans la correction sectorielle (FLY −7,56 %, PLTR −3,22 %).
8. ✅ **Anomalie options inchangée** — Max Pain JSON $65,00 aberrant ; valeurs opérationnelles conservées.

**Recommandation** : Maintenir la posture **SURVEILLER** avec vigilance accrue. Le setup technique se dégrade :
- La zone **$90–$98** est désormais le support critique à surveiller (confluence MM50 + psychologique).
- Une **cassure sous $98,04 (MM50)** avec volume > 1,0× confirmerait un renversement de tendance et justifierait un passage à **ÉVITER**.
- Un **rebond au-dessus de $113,65** (close 13h) avec volume croissant vers 1,0×+ rétablirait la neutralité technique.

Toute position longue actuelle expose à un drawdown de −22,4 % (SL) en 1–2 séances compte tenu du Beta 2,50 et de l’ATR $12,15. Le ratio R/R 1,5:1 reste insuffisant pour un trade directionnel institutionnel.

---

*Rapport généré le 2026-06-09 — Données : `data/latest.json` (21:00 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/quant_report_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`*
