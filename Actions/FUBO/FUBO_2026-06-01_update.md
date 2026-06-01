# FUBO — Mise à Jour (2026-06-01, snapshot 17h UTC)

> **Niveau d'impact :** 🟡 Modéré — Cours **$10.90** (+8.03% vs previous close $10.09), RSI **62.27** (franchissement zone neutre, +15.1 pts vs 13h), volume **820 898** (0.58× moy. 20j, effondrement de liquidité), short interest stable **25.03%**. Agent upgrade **ACHETER Réduit** (68.5/100 ajusté 60.5/100) vs ATTENDRE (59.2/100) au snapshot 13h. Ajustement analyste inchangé **SURVEILLER (~48/100)**. Données options inchangées et cohérentes (max pain $11.00, put/call 0.41, call OI 70.9%). Anomalie earnings Q1 persistante (FMP jour J 2026-06-01, aucun résultat visible).
> **Référence précédente :** [FUBO_2026-06-01_update.md](FUBO_2026-06-01_update.md) (snapshot 13:00 UTC — close $10.09, RSI 47.2, volume 1.94M, agent ATTENDRE 59.2/100)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-01 13:00 UTC)

| Métrique | 2026-06-01 13:00 UTC | **2026-06-01 17:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $10.09 | **$10.90** | **+8.03%** 🔴 |
| Change % vs previous | −3.26% | **+8.03%** | **Inversion haussière** |
| Volume séance | 1 942 000 | **820 898** | **−57.7%** 🔴 |
| Volume vs 20j | 1.31× | **0.58×** | **Effondrement de liquidité** |
| RSI 14j | 47.2 | **62.27** | **+15.1 pts** — franchi zone neutre |
| ATR 14j | $0.54 | **$0.57** | +5.6% |
| MM 50j | $11.19 | **$11.13** | −0.5% |
| Market Cap (Yahoo) | $297.0M | **$320.8M** | +8.0% (mouvement cours) |
| P/E TTM (Yahoo) | 2.63x | **2.84x** | +8.0% |
| Short Interest | 25.03% | **25.03%** | Stable |
| Max Pain (API) | $11.00 | **$11.00** | Stable |
| Put/Call Ratio (API) | 0.41 | **0.41** | Stable |
| Call OI % (API) | 70.9% | **70.9%** | Stable |
| Échéance options | 2026-06-05 | **2026-06-05** | J+4 |
| **Score Global (agent)** | 67.2/100 | **68.5/100** | **+1.3 pt** |
| **Score Global Ajusté (agent)** | 59.2/100 | **60.5/100** | **+1.3 pt** |
| **Score Opportunité (agent)** | 6.7/10 | **6.8/10** | +0.1 pt |
| **Score Momentum (agent)** | 4.5/10 | **5.0/10** | **+0.5 pt** |
| **Recommandation (agent)** | ATTENDRE | **ACHETER** | **🔴 UPGRADE** |

**Constats :**
1. **Rally +8.03% sur volume effondré** — Le cours gagne $0.81 (+8.03%) pour clôturer à $10.90, mais le volume chute de 1.94M à 820k (−57.7%), soit 0.58× la moyenne 20j. Ce rally est interprété comme un **short-covering mécanique** (short interest 25.03%) ou un mouvement de convergence vers le max pain $11.00 (spot désormais à −0.9%), plutôt qu'une accumulation institutionnelle. Faible liquidité = faible conviction.
2. **RSI franchi 50 à 62.27** — Sortie de la zone neutre-baisse avec une accélération notable (+15.1 pts en 4h). Le RSI approche la zone de surachat (70). Cependant, le niveau 62.27 reste sous 70, laissant une marge technique avant surachat.
3. **Agent upgrade ATTENDRE → ACHETER** — Le modèle quantitatif passe en ACHETER Réduit (60.5/100 ajusté) sur base d'un Score Opportunité 6.8/10 (C:8.0 V:7.0 M:5.0). L'upgrade est porté par le Catalyseur 8.0/10 et la Valorisation 7.0/10, malgré un Momentum 5.0/10 et un timing Défavorable (cours sous MM50).
4. **Short interest stable à 25.03%** — Le niveau très élevé est inchangé. Le rally +8.03% pourrait refléter un début de couverture des shorts, mais l'absence d'explosion de volume suggère une couverture limitée ou un mouvement mécanique (max pain pinning).
5. **Anomalie calendrier earnings persistante** : `data/upcoming_events_latest.json` (2026-06-01) place l'earnings au **2026-06-01** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible dans `data/latest.json` au snapshot 17h UTC. [ANOMALIE PERSISTANTE — J+? NON RÉSOLU]
6. **Validation report** (`data/validation_report.txt`, 2026-06-01) : 24/28 tickers OK, 4 KO. FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 62.27 | **Neutre-haussier** — franchi 50 avec vigueur, progression continue depuis la survente extrême (RSI 21.08 le 26/05), proche surachat 70 |
| MM 50j | $11.13 | Cours sous la moyenne — écart **−2.1%** (vs −9.8% au snapshot 13h) |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.57 | Volatilité absolue stable (5.2% du spot) |
| Volume vs 20j | 0.58× | **Liquidité effondrée** — volume bien sous la moyenne, faible conviction |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+31.2%** (vs +21.4% au snapshot 13h) |
| Short Interest | 25.03% | **Très élevé** — stable |

**Niveaux clés :**
- Support immédiat : **$10.25** (low du jour)
- Support secondaire : **$10.09** (previous close / support technique)
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$10.99** (high du jour)
- Résistance majeure (max pain) : **$11.00** (échéance J+4 — spot à −0.9%)
- Résistance majeure (MM50) : **$11.13** (breakout requis pour inflexion de tendance)
- Stop-loss ATR (2×) : **$9.76** (−10.5%)
- Take-profit ATR (3×) : **$12.61** (+15.7%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — cours sous MM50 (−2.1%, mais nettement réduit vs −9.8% au snapshot 13h), RSI proche surachat (62.27), volume effondré (0.58×) signalant un rally sans conviction institutionnelle. La structure options haussière (put/call 0.41, call OI 70.9%, max pain $11.00) reste le principal support technique. Le spot à −0.9% du max pain suggère un pinning haussier probable à l'échéance J+4 (2026-06-05). Cependant, le faible volume et le manque de catalyseur fondamental limitent la directionnalité.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 2026-06-01 17h UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $320.8M | 2.84x | 0.40x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×10.2 sur la capitalisation (stable en structure).

### Ratios disponibles (Yahoo + FMP, close 2026-06-01 17h UTC)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.84x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 23.09x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.436x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.40x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×8.0 avec Yahoo |
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

### Options

| Signal | Valeur 13:00 UTC | Valeur 17:00 UTC | Lecture |
|---|---|---|---|
| Max Pain | $11.00 | **$11.00** | Stable — spot à −0.9% |
| Put/Call Ratio | 0.41 | **0.41** | Très faible — biais haussier fort |
| Call OI % | 70.9% | **70.9%** | Domination calls |
| Échéance options | 2026-06-05 | **2026-06-05** | J+4 |

**Lecture institutionnelle :** Les données options du snapshot 17h UTC sont **inchangées et cohérentes**. Le put/call **0.41** et le call OI **70.9%** confirment un positionnement net haussier. Le max pain **$11.00** place le spot à **−0.9%** en dessous — les market makers ont un intérêt mécanique à ce que le cours converge vers $11.00 à l'approche de l'échéance J+4. Le rally +8.03% a rapproché le spot du max pain, réduisant le gap de −8.3% (snapshot 13h) à −0.9%.

Le setup short squeeze latent persiste avec le short interest à **25.03%** combiné au call OI dominant **70.9%**. Cependant, le volume effondré (0.58×) suggère que le rally n'est pas porté par une accumulation institutionnelle massive, mais plutôt par un short-covering sélectif ou un mouvement mécanique (max pain pinning).

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +361%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-06-01) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` (2026-06-01) place l'événement au **2026-06-01** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plusieurs jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-06-01) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-06-01) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

### Sector Rotation

- `data/sector_rotation_latest.json` (2026-06-01) : XLC classé **bottom 3** (momentum score 0.0 / 10). Signal système : **ROTATION_TO_CYCLICAL** (note : signal a changé vs ROTATION_TO_DEFENSIVE mentionné au snapshot 13h — vérifier cohérence). Malus sectoriel maintenu : −0.5 pt composite.

### Geo Risk

- `data/geo_risk_latest.json` (2026-05-17) : FUBO non flaggué. Score Politique non calculé.

### Quant Report

- `data/quant_report_latest.json` (2026-05-17) : n = 0, pas assez de signaux historiques FUBO. Win rate 0%, p-value 1.0 (insuffisant). Aucune calibration auto applicable.

**Verdict Sentiment :** Neutre à prudent. Silence médiatique et institutionnel. L'unique signal observable est la structure options haussière (put/call 0.41, call OI 70.9%, max pain $11.00) et le short interest élevé (25.03%). Le rally +8.03% sur volume faible est interprété comme un mouvement technique (short-covering / max pain pinning) plutôt qu'un changement de fondamental.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 68.5 / 100 |
| Score Global Ajusté | **60.5 / 100** |
| Score Opportunité | **6.8 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | **5.0 / 10** |
| Recommandation agent | **ACHETER** |
| Timing agent | **Défavorable** |

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Opportunité | 6.8 / 10 | **~4.8 / 10** | Plafonnement Valorisation à 5/10 (Qualité 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus timing défavorable (−0.3 pt) ; malus données earnings Q1 manquantes (−0.5 pt) ; malus volume effondré 0.58× (−0.3 pt) ; bonus options haussières (+0.2 pt) ; bonus short squeeze latent (+0.1 pt) |
| Score Catalyseur | 8.0 / 10 | **7.7 / 10** | Malus earnings anomalie persistante −0.3 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 5.0 / 10 | **4.5 / 10** | Rally sur volume faible — malus conviction −0.5 pt |
| **Score Global Ajusté** | 60.5 / 100 | **~48 / 100** | Recalculé sur base 4.8/10 × 10 = 48 |
| **Recommandation analyste** | — | **SURVEILLER** | Score 35–49 ; Qualité 1/6 exclut tout sizing standard |

**Note sur la divergence agent/analyste :** L'agent quantitatif upgrade FUBO en ACHETER sur base d'un Score Opportunité 6.8/10 (Valorisation 7.0/10 non plafonnée). L'ajustement analyste applique le plafonnement Qualité 1/6 (Valorisation → 5.0/10), le malus volume effondré (0.58×, pas de confirmation institutionnelle) et le malus earnings anomalie persistante. Le Score Opportunité ajusté tombe à **4.8/10**, maintenant la recommandation en **SURVEILLER**.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $10.90 | — |
| Stop-Loss | **$9.76** | 2× ATR (−10.5%) — confirmé par recommandations agent |
| Take-Profit | **$12.61** | 3× ATR (+15.7%) — confirmé par recommandations agent |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$10.25** | Low du jour |
| Support technique | **$10.09** | Previous close |
| Résistance (max pain) | **$11.00** | Échéance J+4 — spot à −0.9% |
| Résistance majeure (MM50) | **$11.13** | Breakout requis pour inflexion de tendance |
| Résistance (high du jour) | **$10.99** | À franchir pour prolonger le rally |

**Note sur le max pain vs TP :** Le max pain $11.00 se situe entre la résistance high du jour ($10.99) et le TP ATR ($12.61). Si le cours converge vers le max pain à l'échéance 2026-06-05, le gain serait de +0.9%, bien en-deçà du TP. Le max pain agit comme un aimant technique court terme, pas comme un objectif de rendement.

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — SURVEILLER (~48/100). Rally technique +8.03% sur volume effondré sans changement fondamental. Agent upgrade mécanique non suivi par l'ajustement qualité.**

La thèse de **SURVEILLER** du snapshot 2026-06-01 13:00 UTC est **confirmée** avec une nuance technique haussière (RSI 62.27, rapprochement MM50) mais une conviction réduite (volume 0.58×). Cinq observations :

1. **Rally +8.03% sur volume effondré** — Le cours gagne $0.81 pour clôturer à $10.90, mais le volume chute de 57.7% à 820k (0.58× moy. 20j). Ce profil (rally sur volume décroissant) est caractéristique d'un **short-covering mécanique** ou d'un mouvement de pinning vers le max pain ($11.00), plutôt que d'une accumulation institutionnelle. Faible liquidité = faible conviction.

2. **RSI franchi 50 à 62.27** — Progression technique notable (+15.1 pts vs snapshot 13h) qui rapproche le titre de la zone de surachat (70). Le franchissement de 50 est un signal technique positif, mais le niveau 62.27 reste sous le seuil critique de 70. Le cours est désormais à seulement **−2.1%** de la MM50 ($11.13), contre **−9.8%** au snapshot 13h.

3. **Agent upgrade ATTENDRE → ACHETER** — Le modèle quantitatif réagit au rally en passant en ACHETER Réduit (60.5/100 ajusté). Cet upgrade est porté par le Catalyseur 8.0/10 et la Valorisation 7.0/10. Cependant, le timing reste Défavorable (cours sous MM50) et le Momentum 5.0/10 reste modéré. L'upgrade est interprété comme une réaction mécanique au prix, non comme une réévaluation fondamentale.

4. **Structure options inchangée et cohérente** — Max pain $11.00, put/call 0.41, call OI 70.9%. Le spot à −0.9% du max pain renforce l'hypothèse de pinning haussier à l'échéance J+4 (2026-06-05). Le rally +8.03% a réduit le gap spot/max pain, rendant la convergence mécanique plus probable.

5. **Anomalie earnings persistante** — L'earnings Q1 reste placé au 2026-06-01 (jour J) dans `upcoming_events_latest.json` sans résultats visibles. Cette incertitude continue de peser sur le Score Catalyseur (−0.3 pt) et justifie le maintien de la recommandation en SURVEILLER.

**Recommandation finale :** **SURVEILLER — pas de position.** Le rally +8.03% est un événement technique notable (RSI 62.27, rapprochement MM50, structure options favorable), mais il manque de conviction institutionnelle (volume 0.58×). La directionnalité reste incertaine : le cours sous MM50 (−2.1%), le fondamental dégradé (Qualité 1/6, patrimoine net négatif) et l'anomalie earnings persistante limitent tout sizing. La structure options haussière (max pain $11.00, put/call 0.41, call OI 70.9%) et le setup short squeeze mécanique (25.03% SI) sont des éléments de surveillance actifs, mais sans catalyseur fondamental, toute entrée reste un trade spéculatif avec sizing minimal. Le comportement à l'échéance options J+4 (2026-06-05) et la résolution de l'anomalie earnings sont les deux catalyseurs clés à surveiller.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-06-01 (snapshot 17:00 UTC)*
*Sources : data/latest.json (fetched 2026-06-01T17:00:01Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-06-01), data/social_sentiment_latest.json (2026-06-01), data/fx_exposure_latest.json (2026-06-01), data/upcoming_events_latest.json (2026-06-01), data/events_latest.json (2026-06-01), data/validation_report.txt (2026-06-01)*
