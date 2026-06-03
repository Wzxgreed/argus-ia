# FUBO — Mise à Jour (2026-06-03, snapshot 10h UTC)

> **Niveau d'impact :** 🟢 Faible — **Stabilité totale** vs snapshot 21h UTC 02/06. Cours inchangé **$10.72**, volume stable **1.10M** (0.77× moy. 20j), RSI **58.61** inchangé, franchissement sous MM50 ($11.09) maintenu à **−3.3%**. Scores agents **inchangés** : **ATTENDRE 58.0/100**, Score Opportunité **6.6/10**, Score Momentum **4.0/10** (momentum baissier), timing **Défavorable**. **Anomalie options JSON détectée** (max pain **$3.00** aberrant vs $12.00 opérationnel) — valeurs opérationnelles conservées. Anomalie earnings persistante (`days_until: 0`, jour J).
> **Référence précédente :** [FUBO_2026-06-02_update.md](FUBO_2026-06-02_update.md) (snapshot 21:00 UTC — close $10.72, RSI 58.61, volume 1.07M / 0.75×, agent ATTENDRE 58.0/100)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-02 21:00 UTC)

| Métrique | 2026-06-02 21:00 UTC | **2026-06-03 10:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $10.72 | **$10.72** | **Inchangé** |
| Previous close | $11.52 | **$11.52** | — |
| Volume séance | 1 072 880 | **1 103 400** | **+2.8% — stable** |
| Volume vs 20j | 0.75× | **0.77×** | **Stable, reste sous-moyenne** |
| RSI 14j | 58.61 | **58.61** | **Inchangé** |
| ATR 14j | $0.65 | **$0.65** | Stable |
| MM 50j | $11.09 | **$11.09** | Stable |
| Spot vs MM50 | −3.3% | **−3.3%** | **Inchangé** |
| Market Cap (Yahoo) | $315.5M | **$315.5M** | Inchangé |
| Short Interest | 25.03% | **25.03%** | Stable — très élevé |
| **Max Pain (API)** | **$12.00** | **$3.00** | **[ANOMALIE JSON] — valeur opérationnelle $12.00 conservée** 🔴 |
| **Put/Call Ratio (API)** | **0.20** | **null** | **[ANOMALIE JSON] — valeur opérationnelle 0.20 conservée** |
| **Call OI % (API)** | **83.2%** | **null** | **[ANOMALIE JSON] — valeur opérationnelle 83.2% conservée** |
| Échéance options | 2026-06-05 | **2026-06-05** | J+2 |
| Spot vs Max Pain (op.) | −10.7% | **−10.7%** | Inchangé |
| **Score Global (agent)** | 66.0/100 | **66.0/100** | Inchangé |
| **Score Global Ajusté (agent)** | 58.0/100 | **58.0/100** | Inchangé |
| **Score Opportunité (agent)** | 6.6/10 | **6.6/10** | Inchangé |
| **Score Momentum (agent)** | 4.0/10 | **4.0/10** | Inchangé — momentum baissier |
| **Recommandation (agent)** | ATTENDRE | **ATTENDRE** | Inchangée |
| **Timing (agent)** | Défavorable | **Défavorable** | Inchangé |

**Constats :**
1. **Stabilité totale des données marché** — Aucune variation de cours, RSI, ATR, MM50 ou volume significative entre le close 02/06 et l'ouverture 03/06. Le cours reste ancré à $10.72, en dessous de la MM50 ($11.09) avec un écart de −3.3%. Le volume à 0.77× confirme un intérêt modéré mais insuffisant pour un rebond technique.
2. **Scores agents inchangés — downgrade stabilisé** — L'agent quantitatif maintient **ATTENDRE (58.0/100)** avec Score Momentum 4.0/10 et timing Défavorable. La stabilité des scores sur 2 snapshots consécutifs confirme que le franchissement sous MM50 et le momentum négatif sont intégrés dans le modèle.
3. **Anomalie options JSON détectée et traitée** — `data/latest.json` (2026-06-03) retourne un max pain **$3.00** (vs $12.00 à 21h UTC 02/06), put/call `null`, call OI `null`. Cette valeur est aberrante (le spot à $10.72 est +257% au-dessus du max pain $3.00, ce qui invalide mécaniquement le concept de max pain). Il s'agit d'une corruption JSON récurrente (même anomalie observée le 2026-06-01 10h UTC, résolue à 13h UTC). Les valeurs opérationnelles **$12.00 / 0.20 / 83.2%** sont conservées. L'échéance reste **2026-06-05 (J+2)**.
4. **Anomalie earnings persistante** — `data/upcoming_events_latest.json` (2026-06-03) place toujours l'earnings au **2026-06-03** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible. L'anomalie calendaire continue de peser sur le Score Catalyseur.
5. **Validation report** (`data/validation_report.txt`, 2026-06-03) : 24/29 tickers OK, 5 KO. FUBO **non flaggué** — données considérées fiables (hors anomalie options JSON gérée).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 58.61 | **Neutre** — marge de 11.39 pts avant surachat (70), marge de 8.61 pts avant survente (50) |
| MM 50j | $11.09 | Cours **sous** MM50 — écart **−3.3%** (breakout infirmé) 🔴 |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.65 | Volatilité absolue stable (6.1% du spot) |
| Volume vs 20j | 0.77× | **Stable sous-moyenne** — liquidité insuffisante pour un rebond confirmé |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+29.0%** |
| Short Interest | 25.03% | **Très élevé** — stable |

**Niveaux clés :**
- Support immédiat : **$10.645** (low 02/06)
- Support psychologique : **$10.50** (arrondi)
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$11.09** (MM50)
- Résistance : **$11.28** (high 02/06)
- Résistance majeure : **$12.00** (max pain opérationnel, échéance J+2)
- Stop-loss ATR (2×) : **$9.42** (−12.1%)
- Take-profit ATR (3×) : **$12.67** (+18.2%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — cours sous MM50 (−3.3%), momentum baissier confirmé (Score Momentum 4.0/10), timing Défavorable. Le volume stable (0.77×) ne montre ni accumulation ni distribution marquée. La structure options haussière (max pain $12.00 opérationnel, put/call 0.20, call OI 83.2%) et le short interest 25.03% constituent un support technique sous-jacent, mais le momentum immédiat reste négatif. Attendre un retour au-dessus de MM50 ($11.09) avec volume confirmé (>0.8× moyenne) pour toute réactivation haussière. L'échéance options J+2 (2026-06-05) reste un catalyseur technique à surveiller.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 2026-06-03 10h UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $315.5M | 2.79x | 0.39x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×10.4 sur la capitalisation (stable en structure).

### Ratios disponibles (Yahoo + FMP, snapshot 2026-06-03)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.79x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 22.71x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.439x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.39x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×8.2 avec Yahoo |
| Beta | 2.508 | Extrême |
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

### Options — Anomalie JSON Détectée, Valeurs Opérationnelles Conservées

| Signal | Valeur 21:00 UTC 02/06 | Valeur 10:00 UTC 03/06 | Lecture |
|---|---|---|---|
| Max Pain (API) | $12.00 | **$3.00** | **[ANOMALIE JSON] — aberrant, valeur op. $12.00 conservée** |
| Put/Call Ratio (API) | 0.20 | **null** | **[ANOMALIE JSON] — valeur op. 0.20 conservée** |
| Call OI % (API) | 83.2% | **null** | **[ANOMALIE JSON] — valeur op. 83.2% conservée** |
| Échéance options | 2026-06-05 | **2026-06-05** | J+2 |

**Lecture institutionnelle :** La structure options opérationnelle n'a pas changé. Le spot à −10.7% sous le max pain $12.00 renforce mécaniquement l'aimant haussier vers $12.00 à l'échéance J+2. Cependant, le volume stable (0.77×) et le cours inchangé suggèrent un marché en attente. Le setup de short squeeze reste théoriquement intact (short interest 25.03% + call OI 83.2% + put/call 0.20), mais le timing immédiat reste défavorable. Si le cours converge vers $12.00 à échéance, le gain serait de +11.9% depuis le close actuel.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +368.8%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-06-03) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` (2026-06-03) place l'événement au **2026-06-03** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plusieurs jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-06-03) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-06-03) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

### Sector Rotation

- `data/sector_rotation_latest.json` (2026-06-03) : XLC classé **bottom 3** (momentum score 0.0 / 10). Signal système : **NEUTRAL**. Malus sectoriel maintenu : −0.5 pt composite.

### Geo Risk

- `data/geo_risk_latest.json` (2026-05-17) : FUBO non flaggué. Score Politique non calculé.

### Quant Report

- `data/quant_report_latest.json` (2026-05-17) : n = 0, pas assez de signaux historiques FUBO. Win rate 0%, p-value 1.0 (insuffisant). Aucune calibration auto applicable.

**Verdict Sentiment :** Neutre à légèrement baissier. Le silence médiatique persiste. Le repositionnement options haussier (inchangé) contrebalance la stagnation du spot, mais le momentum négatif et le franchissement sous MM50 pèsent sur le sentiment technique. L'unique catalyseur observable reste la structure options et le short interest élevé. L'absence de volume et de mouvement de cours suggère un marché en attente de la résolution de l'anomalie earnings.

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

**Note sur la divergence agent/analyste :** L'agent quantitatif maintient FUBO en ATTENDRE (58.0/100) suite au franchissement sous MM50 et à la perte de momentum. L'ajustement analyste applique le plafonnement Qualité 1/6 (Valorisation → 5.0/10) et le malus sectoriel XLC bottom 3. Le Score Opportunité ajusté reste à **5.7/10**, donnant un Score Global **~56.5/100** — zone **ATTENDRE** (50–59). La thèse reste **ATTENDRE**.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $10.72 | — |
| Stop-Loss | **$9.42** | 2× ATR (−12.1%) — inchangé |
| Take-Profit | **$12.67** | 3× ATR (+18.2%) — inchangé |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$10.645** | Low 02/06 |
| Support psychologique | **$10.50** | Arrondi |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$11.09** | MM50 |
| Résistance | **$11.28** | High 02/06 |
| Résistance majeure (max pain op.) | **$12.00** | Max pain opérationnel (échéance J+2) |

**Note sur le max pain vs TP :** Le max pain $12.00 se situe entre la résistance immédiate ($11.09) et le TP ATR ($12.67). Si le cours converge vers le max pain à l'échéance 2026-06-05, le gain serait de +11.9% (vs +8.9% à 17h 02/06), bien en-deçà du TP mais constituant un objectif technique intermédiaire réaliste.

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE ATTENDRE CONFIRMÉE (~56.5/100). Stabilité totale vs snapshot 21h UTC 02/06 (cours $10.72 inchangé, RSI 58.61, volume 1.10M / 0.77×), franchissement sous MM50 maintenu (−3.3%), scores agents inchangés. Anomalie options JSON détectée (max pain $3.00 aberrant → valeurs opérationnelles $12.00/0.20/83.2% conservées).**

La thèse **ATTENDRE** du snapshot 2026-06-02 21:00 UTC est **confirmée** sur base des quatre observations suivantes :

1. **Stabilité totale des données marché** — Aucune variation de cours, RSI, ATR, MM50 ou volume significative entre le close 02/06 et l'ouverture 03/06. Le cours reste ancré à $10.72, en dessous de la MM50 ($11.09) avec un écart de −3.3%. Le volume stable à 0.77× suggère un marché en attente, sans accumulation ni distribution marquée.

2. **Scores agents inchangés — downgrade stabilisé** — L'agent quantitatif maintient **ATTENDRE (58.0/100)** avec Score Momentum 4.0/10 et timing Défavorable. La stabilité des scores sur 2 snapshots consécutifs confirme que le franchissement sous MM50 et le momentum négatif sont intégrés dans le modèle. L'ajustement analyste confirme ATTENDRE (~56.5/100) avec le plafonnement Qualité 1/6 et le malus sectoriel.

3. **Structure options opérationnelle inchangée** — Max pain $12.00, put/call 0.20, call OI 83.2% : aucun changement opérationnel. L'anomalie JSON (max pain $3.00) est identifiée comme corruption récurrente et les valeurs opérationnelles sont conservées. Le spot à −10.7% sous le max pain renforce mécaniquement l'aimant haussier vers $12.00 à l'échéance J+2. Cependant, le volume stable et le cours inchangé limitent la probabilité d'une convergence rapide. Le setup de short squeeze reste latent (short interest 25.03% + call OI dominant), mais sans catalyseur positif (résolution de l'anomalie earnings, beat, guidance raise), le mouvement restera contraint par le momentum baissier.

4. **Anomalie earnings persistante** — L'earnings Q1 reste placé au jour J (`days_until: 0`) sans résultat visible. Cette anomalie continue de peser sur le Score Catalyseur (−0.3 pt) et de justifier le statut ATTENDRE. La résolution de cette anomalie serait le catalyseur fondamental clé à surveiller.

**Recommandation finale :** **ATTENDRE.** Le franchissement sous MM50 ($11.09) reste creusé à −3.3% et le momentum baissier (Score Momentum 4.0/10) persiste. Le volume stable (0.77×) indique un marché en attente. La structure options haussière (max pain $12.00 opérationnel, put/call 0.20, call OI 83.2%) et le short interest 25.03% constituent un support technique sous-jacent, mais le timing Défavorable impose d'attendre un retour au-dessus de MM50 avec volume confirmé (>0.8× moyenne) avant toute réactivation. L'échéance options J+2 (2026-06-05) reste un catalyseur technique à surveiller : si le spot converge vers $12.00, cela constituerait un +11.9% depuis le close actuel.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-06-03 (snapshot 10:00 UTC)*
*Sources : data/latest.json (fetched 2026-06-03T10:00:01Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-06-03), data/social_sentiment_latest.json (2026-06-03), data/fx_exposure_latest.json (2026-06-03), data/upcoming_events_latest.json (2026-06-03), data/events_latest.json (2026-06-03)*
