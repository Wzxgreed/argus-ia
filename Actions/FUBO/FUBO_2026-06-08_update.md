# FUBO — Mise à Jour (2026-06-08, snapshot 10h UTC)

> **Niveau d'impact :** 🔴 Élevé — **Gap technique −6.10%** et **détérioration significative** vs snapshot 2026-06-03 10h UTC. Cours en chute libre inter-snapshot **$10.72 → $9.54 (−11.0%)**, volume de liquidation **1.28M (1.02× moy. 20j)** vs sous-moyenne précédente, RSI **49.4** (−9.2 pts), franchissement sous MM50 creusé de **−3.3% à −12.96%**. ATR en expansion **$0.72** (+10.8%). Scores agents **inchangés** : **ATTENDRE 58.0/100**, Score Opportunité **6.6/10**, Score Momentum **4.0/10** (momentum baissier), timing **Défavorable**. Anomalie options JSON persistante (max pain **$3.00** aberrant, échéance repoussée au **2026-06-12**). Earnings Q1 2026 toujours en anomalie jour J (`days_until: 0`).
> **Référence précédente :** [FUBO_2026-06-03_update.md](FUBO_2026-06-03_update.md) (snapshot 10:00 UTC — close $10.72, RSI 58.61, volume 1.10M / 0.77×, agent ATTENDRE 58.0/100)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-03 10:00 UTC)

| Métrique | 2026-06-03 10:00 UTC | **2026-06-08 10:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $10.72 | **$9.54** | **−11.0% inter-snapshot / −6.1% session** 🔴 |
| Previous close | $11.52 | **$10.16** | — |
| Volume séance | 1 103 400 | **1 281 500** | **+16.1%** |
| Volume vs 20j | 0.77× | **1.02×** | **Retour au-dessus moyenne — liquidation** |
| RSI 14j | 58.61 | **49.4** | **−9.2 pts — sortie zone neutre haute** |
| ATR 14j | $0.65 | **$0.72** | **+10.8% — volatilité en expansion** |
| MM 50j | $11.09 | **$10.96** | Recul de −1.2% |
| Spot vs MM50 | −3.3% | **−12.96%** | **Détérioration technique majeure** 🔴 |
| Market Cap (Yahoo) | $315.5M | **$280.8M** | −11.0% (aligné cours) |
| Short Interest | 25.03% | **25.03%** | Stable — très élevé |
| **Max Pain (API)** | **$3.00** | **$3.00** | **[ANOMALIE JSON PERSISTANTE] — aberrant** 🔴 |
| **Put/Call Ratio (API)** | **null** | **null** | **[ANOMALIE JSON] — données manquantes** |
| **Call OI % (API)** | **null** | **null** | **[ANOMALIE JSON] — données manquantes** |
| Échéance options | 2026-06-05 | **2026-06-12** | **Nouvelle échéance** |
| **Score Global (agent)** | 66.0/100 | **66.0/100** | Inchangé |
| **Score Global Ajusté (agent)** | 58.0/100 | **58.0/100** | Inchangé |
| **Score Opportunité (agent)** | 6.6/10 | **6.6/10** | Inchangé |
| **Score Momentum (agent)** | 4.0/10 | **4.0/10** | Inchangé — momentum baissier |
| **Recommandation (agent)** | ATTENDRE | **ATTENDRE** | Inchangée |
| **Timing (agent)** | Défavorable | **Défavorable** | Inchangé |

**Constats :**
1. **Gap technique −6.10% overnight** — Le cours a ouvert en gap baissier à $9.87 (vs previous close $10.16) et a poursuivi sa dégringolade jusqu'à $9.44 (low du jour), pour clôturer à $9.54. Cette baisse de −11.0% inter-snapshot (5 jours de trading écoulés depuis le 03/06) confirme la rupture technique initiée le 02/06 sous MM50.
2. **Volume de liquidation au-dessus de la moyenne** — Le volume est passé de 0.77× à 1.02× la moyenne 20j, soit 1.28M actions échangées. C'est le premier volume supérieur à la moyenne depuis le rally du 01/06. La liquidité accrue sur une baisse de −6.1% suggère une distribution / prise de profits / stop-losss déclenchés plutôt qu'une accumulation.
3. **RSI en retour médian, momentum perdu** — Le RSI est passé de 58.61 (zone neutre haute) à 49.4 (neutre médian), perdant 9.2 pts. Il n'y a pas de survente (RSI > 30), ce qui laisse théoriquement de la marge pour une poursuite baissière.
4. **Franchissement sous MM50 creusé de −3.3% à −12.96%** — La MM50 a reculé à $10.96 (vs $11.09), mais le spot a chuté bien plus vite, creusant l'écart à près de −13%. Ce franchissement est désormais profond et structurellement baissier à court terme.
5. **ATR en expansion +10.8%** — L'ATR est remonté à $0.72, confirmant une augmentation de la volatilité. Le trigger `ATR_SPIKE` du pipeline a détecté un ATR relatif de 7.55% (seuil 5.0%).
6. **Anomalie options JSON persistante** — `data/latest.json` (2026-06-08) retourne toujours un max pain **$3.00** (aberrant), put/call `null`, call OI `null`. L'échéance a été repoussée au **2026-06-12** (vs 2026-06-05). Les valeurs opérationnelles historiques ($12.00 / 0.20 / 83.2%) ne sont plus applicables suite au changement d'échéance. [ANOMALIE DATA QUALITY]
7. **Anomalie earnings persistante** — `data/upcoming_events_latest.json` (2026-06-08) place toujours l'earnings au **2026-06-08** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plus de 2 semaines d'attente.
8. **Validation report** (`data/validation_report.txt`, 2026-06-08) : 24/29 tickers OK, 5 KO. FUBO **non flaggué** — données considérées fiables (hors anomalie options JSON).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 49.4 | **Neutre médian** — marge de 20.6 pts avant surachat (70), marge de 19.4 pts avant survente (30) |
| MM 50j | $10.96 | Cours **sous** MM50 — écart **−12.96%** (franchissement profondément creusé) 🔴 |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.72 | Volatilité en expansion (7.55% du spot) — ATR_SPIKE détecté |
| Volume vs 20j | 1.02× | **Liquidation** — volume au-dessus moyenne sur baisse |
| Beta | 2.392 | Volatilité systématique extrême (en retrait vs 2.508) |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+14.8%** (rétrécissement) |
| Short Interest | 25.03% | **Très élevé** — stable |

**Niveaux clés :**
- Support immédiat : **$9.44** (low 08/06)
- Support psychologique : **$9.00** (arrondi)
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$10.16** (previous close)
- Résistance : **$10.96** (MM50)
- Résistance majeure : **$11.00–$12.00** (zone historique / ancien max pain)
- Stop-loss ATR (2×) : **$8.10** (−15.1%)
- Take-profit ATR (3×) : **$11.70** (+22.6%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — cours sous MM50 (−12.96%), momentum baissier confirmé (Score Momentum 4.0/10), gap technique −6.1% non comblé, volume de liquidation. Le setup de short squeeze (short interest 25.03%) reste latémaent présent mais sans structure options observable fiable (anomalie JSON) et sans catalyseur positif (earnings jour J non résolu). Le retour au-dessus de MM50 ($10.96) nécessiterait un rebond de +14.9%, ce qui est ambitieux sans catalyseur. Attendre une stabilisation et un retour test de MM50 avec volume confirmé (>1.0× moyenne) avant toute réactivation.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 2026-06-08. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/Revenue |
|---|---|---|---|---|
| Yahoo Finance | $280.8M | 2.48x | 0.35x | 0.433x |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | — |

**Écart :** ×11.6 sur la capitalisation (stable en structure).

### Ratios disponibles (Yahoo + FMP, snapshot 2026-06-08)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.48x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 20.21x | En retrait vs 22.71x — anticipation légèrement moins pessimiste NTM |
| EV/Revenue | 0.433x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.35x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×9.1 avec Yahoo |
| Beta | 2.392 | Extrême |
| Short Interest | 25.03% | Très élevé — stable |
| Gross Margin (FMP) | 11.1% | Très faible |
| Operating Margin (FMP) | −2.6% | Perte opérationnelle |
| Current Ratio (FMP) | 0.84 | Illiquidité structurelle |
| Debt/Equity (FMP) | 2.43 | Levier élevé |
| Tangible Asset Value (FMP) | −$398.9M | Patrimoine net négatif |
| Net Debt/EBITDA (FMP) | 1.01x | Couverture faible |
| ROIC (FMP) | −2.1% | Destruction de valeur |
| ROE (FMP) | 56.5% | Élevé — structure de capital très levée |

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à **5/10** (règle absolue Argus-IA).

**Données Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — scan comptable non disponible pour cette session.

---

## 4. Mise à Jour Sentiment / Options / News

### Options — Anomalie JSON Persistante, Nouvelle Échéance

| Signal | Valeur 03/06 | Valeur 08/06 | Lecture |
|---|---|---|---|
| Max Pain (API) | $3.00 | **$3.00** | **[ANOMALIE JSON PERSISTANTE] — aberrant** |
| Put/Call Ratio (API) | null | **null** | **[ANOMALIE JSON] — données manquantes** |
| Call OI % (API) | null | **null** | **[ANOMALIE JSON] — données manquantes** |
| Échéance options | 2026-06-05 | **2026-06-12** | **Nouvelle échéance** |

**Lecture institutionnelle :** L'anomalie options JSON persiste depuis le 01/06 sans résolution. Le max pain $3.00 est mécaniquement invalide (spot à +218% au-dessus). L'échéance a été repoussée au 2026-06-12. Les valeurs opérationnelles historiques ($12.00, put/call 0.20, call OI 83.2%) du 02/06 ne sont plus applicables à cette nouvelle échéance. En l'absence de données options fiables, le setup de short squeeze ne peut être quantifié. Le short interest 25.03% reste le seul signal technique haussier latent observable.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +426.7%. Consensus totalement figé et déconnecté du cours.

### News & Événements Corporates

- `data/events_latest.json` (2026-06-08) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` (2026-06-08) place toujours l'événement au **2026-06-08** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plus de 2 semaines d'attente. [ANOMALIE CALENDRIER PERSISTANTE]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-06-08) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-06-08) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

### Sector Rotation

- `data/sector_rotation_latest.json` (2026-06-08) : XLC classé **bottom 3** (momentum score 0.0 / 10). Signal système : **NEUTRAL**. Malus sectoriel maintenu : −0.5 pt composite.

### Geo Risk

- `data/geo_risk_latest.json` (2026-05-17) : FUBO non flaggué. Score Politique non calculé.

### Quant Report

- `data/quant_report_latest.json` (2026-05-17) : n = 0, pas assez de signaux historiques FUBO. Win rate 0%, p-value 1.0 (insuffisant). Aucune calibration auto applicable.

**Verdict Sentiment :** Neutre à baissier. Le silence médiatique persiste. L'absence de données options fiables prive le titre de son principal support technique quantifiable. Le short interest élevé (25.03%) constitue un support latent mais sans catalyseur déclencheur (earnings anomalie, guidance, upgrade). Le volume de liquidation sur le gap baissier confirme une pression vendeuse active.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 66.0 / 100 |
| Score Global Ajusté | **58.0 / 100** |
| Score Opportunité | **6.6 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | **4.0 / 10** |
| Recommandation agent | **ATTENDRE** |
| Timing agent | **Défavorable** |
| Sizing agent | **—** |

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Catalyseur | 8.0 / 10 | **7.7 / 10** | Malus earnings anomalie persistante −0.3 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 4.0 / 10 | **4.0 / 10** | Inchangé — momentum baissier confirmé |
| **Score Opportunité** | 6.6 / 10 | **~5.7 / 10** | Recalculé : (7.7×0.35) + (5.0×0.40) + (4.0×0.25) = 5.695 ≈ **5.7/10** |
| **Score Global** | — | **57.0 / 100** | 5.7 × 10 |
| Malus sectoriel XLC bottom 3 | — | **−0.5 pt** | Composite |
| **Score Global Ajusté** | 58.0 / 100 | **~56.5 / 100** | Zone 50–59 |
| **Recommandation analyste** | — | **ATTENDRE** | Score 50–59 ; Qualité 1/6 limite le risque |

**Note sur la divergence agent/analyste :** L'agent quantitatif maintient FUBO en ATTENDRE (58.0/100) sans réagir au gap −6.1% du jour, probablement car le Score Momentum était déjà à 4.0/10 et le timing Défavorable. L'ajustement analyste applique le plafonnement Qualité 1/6 (Valorisation → 5.0/10) et le malus sectoriel XLC bottom 3. Le Score Opportunité ajusté reste à **5.7/10**, donnant un Score Global **~56.5/100** — zone **ATTENDRE** (50–59). La thèse reste **ATTENDRE**.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.54 | — |
| Stop-Loss | **$8.10** | 2× ATR (−15.1%) — révisé à la hausse (ATR expansion) |
| Take-Profit | **$11.70** | 3× ATR (+22.6%) — révisé à la baisse |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$9.44** | Low 08/06 |
| Support psychologique | **$9.00** | Arrondi |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$10.16** | Previous close (comble gap partiel) |
| Résistance | **$10.96** | MM50 |
| Résistance majeure | **$11.00–$12.00** | Zone historique |

**Note sur le gap :** Le gap overnight −6.1% ($10.16 → $9.54) est partiellement comblable vers $10.16 (previous close). Un retour à $10.16 constituerait un rebond de +6.5% depuis le close actuel, bien en-deçà du TP ATR mais formant un objectif technique intermédiaire réaliste si une absorption du gap se produit.

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE ATTENDRE CONFIRMÉE ET RENFORCÉE (~56.5/100). Détérioration technique majeure vs snapshot 2026-06-03 : gap −6.10% overnight, cours $9.54 (−11.0% inter-snapshot), RSI 49.4 (−9.2 pts), franchissement sous MM50 creusé à −12.96%, volume de liquidation 1.02×, ATR expansion $0.72. Scores agents inchangés ATTENDRE 58.0/100.**

La thèse **ATTENDRE** du snapshot 2026-06-03 est **confirmée et renforcée** sur base des quatre observations suivantes :

1. **Détérioration technique majeure** — Le cours a chuté de −11.0% en 5 jours de trading (close $10.72 → $9.54) avec un gap overnight de −6.1% le 08/06. Le franchissement sous MM50 est passé de −3.3% à −12.96%, ce qui est désormais une rupture technique profonde. Le RSI est retombé à 49.4 (neutre médian) avec 9.2 pts de perte, sans atteindre la zone de survente (30), laissant une marge technique à la baisse.

2. **Volume de liquidation au-dessus de la moyenne** — Le volume à 1.02× (1.28M) est le premier volume supérieur à la moyenne 20j depuis le rally du 01/06. Cette liquidité sur une baisse de −6.1% suggère une distribution active (prises de profits, stops déclenchés) plutôt qu'une accumulation. C'est un signal technique baissier.

3. **ATR en expansion +10.8%** — L'ATR est passé de $0.65 à $0.72, confirmant une volatilité croissante. Le pipeline a détecté un `ATR_SPIKE` à 7.55% (seuil 5.0%). Cette expansion de la volatilité sur une baisse est caractéristique d'une phase de distribution ou de panique contrôlée.

4. **Absence totale de catalyseur positif** — L'anomalie earnings persiste (jour J sans résultats), les données options sont corrompues (max pain $3.00 aberrant), le consensus analyste est figé (4 analysts, PT $50.25), et aucun événement corporate n'est détecté. Le silence médiatique et le sentiment retail à zéro renforcent l'absence d'intérêt acheteur.

**Recommandation finale :** **ATTENDRE.** Le gap −6.1% et la chute de −11.0% inter-snapshot confirment le momentum baissier. Le cours est désormais à −12.96% sous la MM50 ($10.96), ce qui représente une barrière technique élevée pour tout retournement. Le volume de liquidation au-dessus de la moyenne est un signal baissier. Le setup de short squeeze (short interest 25.03%) reste latémaent présent mais n'est pas quantifiable en l'absence de données options fiables. Attendre une stabilisation du cours (base au-dessus de $9.44), un comblement partiel du gap vers $10.16 avec volume confirmé, et surtout un retour au-dessus de MM50 ($10.96) avant toute réactivation haussière. L'échéance options du 2026-06-12 reste un catalyseur technique distant à surveiller si les données options redeviennent cohérentes.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-06-08 (snapshot 10:00 UTC)*
*Sources : data/latest.json (fetched 2026-06-08T10:00:13Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-06-08), data/social_sentiment_latest.json (2026-06-08), data/fx_exposure_latest.json (2026-06-08), data/upcoming_events_latest.json (2026-06-08), data/events_latest.json (2026-06-08)*