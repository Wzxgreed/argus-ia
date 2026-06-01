# FUBO — Mise à Jour (2026-06-01, snapshot 13:00 UTC)

> **Niveau d'impact :** 🟡 Modéré — **Données options restaurées** : max pain **$11.00**, put/call **0.41**, call OI **70.9%**. Cours stable **$10.09** (−3.26% vs previous close), RSI **47.2**, volume **1 942 000** (1.31× moy. 20j). Short interest stable **25.03%**. Scoring agent inchangé **ATTENDRE** (67.2/100, ajusté 59.2/100). Ajustement analyste inchangé **SURVEILLER (~46/100)**. Anomalie earnings Q1 persistante (FMP jour J 2026-06-01, aucun résultat visible). Anomalie options du snapshot 10h UTC **RÉSOLUE**.
> **Référence précédente :** [FUBO_2026-06-01_update.md](FUBO_2026-06-01_update.md) (snapshot 10:00 UTC — close $10.09, RSI 47.2, volume 1.94M, données options corrompues max pain aberrant $3.00, put/call et call OI null)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-01 10:00 UTC)

| Métrique | 2026-06-01 10:00 UTC | **2026-06-01 13:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $10.09 | **$10.09** | **Stable** (marché fermé 10h–13h UTC) |
| Change % vs previous | −3.26% | **−3.26%** | **Stable** |
| Volume séance | 1 942 000 | **1 942 000** | **Stable** |
| Volume vs 20j | 1.31× | **1.31×** | **Stable** |
| RSI 14j | 47.2 | **47.2** | **Stable** |
| ATR 14j | $0.54 | **$0.54** | **Stable** |
| MM 50j | $11.19 | **$11.19** | **Stable** |
| Market Cap (Yahoo) | $297.0M | **$297.0M** | **Stable** |
| P/E TTM (Yahoo) | 2.63x | **2.63x** | **Stable** |
| Short Interest | 25.03% | **25.03%** | **Stable** |
| **Max Pain (API)** | $3.00 (anomalie) | **$11.00** | **✅ RÉSOLU** |
| **Put/Call Ratio (API)** | null | **0.41** | **✅ RÉSOLU** |
| **Call OI % (API)** | null | **70.9%** | **✅ RÉSOLU** |
| Échéance options | 2026-06-05 | **2026-06-05** | **Stable** |
| **Score Global (agent)** | 67.2/100 | **67.2/100** | **Stable** |
| **Score Global Ajusté (agent)** | 59.2/100 | **59.2/100** | **Stable** |
| **Score Opportunité (agent)** | 6.7/10 | **6.7/10** | **Stable** |
| **Score Momentum (agent)** | 4.5/10 | **4.5/10** | **Stable** |
| **Recommandation (agent)** | ATTENDRE | **ATTENDRE** | **Stable** |

**Constats :**
1. **Données options RESTAURÉES** — L'anomalie majeure du snapshot 10:00 UTC (max pain aberrant $3.00, put/call et call OI null) est **résolue** au snapshot 13:00 UTC. Les valeurs sont maintenant cohérentes : max pain **$11.00**, put/call **0.41**, call OI **70.9%**. Ce reset coïncide avec le rollover d'échéance (2026-06-05, J+4) et la stabilisation du flux de données après le passage au nouveau cycle.
2. **Structure options haussière renforcée** — Put/call 0.41 est un niveau très faible (fort biais haussier du positionnement). Call OI 70.9% confirme la domination des calls. Le spot $10.09 se situe à **−8.3%** du max pain $11.00, signalant un potentiel de pinning haussier si le cours converge vers le max pain à l'approche de l'échéance J+4.
3. **Aucun changement de cours/RSI/volume** — Entre 10:00 et 13:00 UTC, le marché US est fermé (ouverture 14:30 UTC). Les métriques techniques sont donc inchangées.
4. **Short interest stable à 25.03%** — Niveau très élevé maintenu. Le setup short squeeze latent persiste avec 25% du float shorté + call OI dominant 70.9%.
5. **Anomalie calendrier earnings persistante** : `data/upcoming_events_latest.json` (2026-06-01) place l'earnings au **2026-06-01** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible dans `data/latest.json` au snapshot 13:00 UTC. [ANOMALIE PERSISTANTE — J+? NON RÉSOLU]
6. **Validation report** (`data/validation_report.txt`, 2026-06-01) : 24/28 tickers OK, 4 KO. FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 47.2 | **Neutre-baisse** — progression continue depuis la survente extrême (RSI 21.08 le 26/05), mais sous 50 |
| MM 50j | $11.19 | Cours sous la moyenne — écart **−9.8%** |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.54 | Volatilité absolue stable (5.4% du spot) |
| Volume vs 20j | 1.31× | **Retour de liquidité** — volume supérieur à la moyenne |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+21.4%** |
| Short Interest | 25.03% | **Très élevé** — stable vs snapshot 10h |

**Niveaux clés :**
- Support immédiat : **$9.92** (low du jour)
- Support secondaire : **$9.53** (low du 27/05)
- Support majeur : **$8.31** (52W low)
- Résistance : **$10.49** (high du jour — rejet net en séance)
- Résistance majeure : **$11.19** (MM50 — breakout requis pour inflexion de tendance)
- Max pain options : **$11.00** (résistance technique supplémentaire, échéance J+4)
- Stop-loss ATR (2×) : **$9.01** (−10.7%)
- Take-profit ATR (3×) : **$11.71** (+16.1%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — sous MM50 (−9.8%), RSI neutre-baisse malgré la progression, recul de −3.26% sur volume en hausse (distribution potentielle). Le rejet du high $10.49 et la mèche haute de la séance confirment la présence de vendeurs au-dessus de $10.40. Cependant, la **restauration des données options** apporte un élément haussier : put/call 0.41 et call OI 70.9% signalent un positionnement options clairement bullish. Le max pain $11.00 place un aimant technique haussier à J+4. Conflit entre structure technique baissière (cours sous MM50, distribution en séance) et structure options haussière (call OI dominant, max pain au-dessus du spot).

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 2026-06-01. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $297.0M | 2.63x | 0.37x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×11.0 sur la capitalisation (stable).

### Ratios disponibles (Yahoo + FMP, close 2026-06-01)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.63x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 21.38x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.436x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.37x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×8.6 avec Yahoo |
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

| Signal | Valeur 10:00 UTC | Valeur 13:00 UTC | Lecture |
|---|---|---|---|
| Max Pain | $3.00 (anomalie) | **$11.00** | **✅ Cohérent** — au-dessus du spot |
| Put/Call Ratio | null | **0.41** | **✅ Très faible — biais haussier fort** |
| Call OI % | null | **70.9%** | **✅ Domination calls** |
| Échéance options | 2026-06-05 | **2026-06-05** | J+4 |

**Lecture institutionnelle :** Les données options du snapshot 13:00 UTC sont **entièrement restaurées et cohérentes**. Le put/call **0.41** est un niveau très faible signalant un positionnement net haussier sur les options. Le call OI **70.9%** confirme cette dominance. Le max pain **$11.00** place le spot à **−8.3%** en dessous — les vendeurs d'options (market makers) ont un intérêt mécanique à ce que le cours converge vers $11.00 à l'approche de l'échéance J+4.

Le setup short squeeze latent s'intensifie avec le short interest à **25.03%** combiné au call OI dominant **70.9%**. Cependant, le recul séance de −3.26% sur volume en hausse (1.31×) et le rejet du high $10.49 suggèrent que les shorts utilisent les rallyes pour renforcer leurs positions plutôt que de couvrir.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +398%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-06-01) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` (2026-06-01) place l'événement au **2026-06-01** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plusieurs jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-06-01) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-06-01) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

### Sector Rotation

- `data/sector_rotation_latest.json` (2026-06-01) : XLC classé **bottom 3** (momentum score 0.0 / 10). Signal système : **ROTATION_TO_DEFENSIVE**.
- Malus sectoriel maintenu : −0.5 pt composite.

### Geo Risk

- `data/geo_risk_latest.json` (2026-05-17) : FUBO non flaggué. Score Politique non calculé.

### Quant Report

- `data/quant_report_latest.json` (2026-05-17) : n = 0, pas assez de signaux historiques FUBO. Win rate 0%, p-value 1.0 (insuffisant). Aucune calibration auto applicable.

**Verdict Sentiment :** Neutre à prudent. Silence médiatique et institutionnel. L'unique signal observable est la hausse du short interest (25.03%) et la structure options haussière restaurée (put/call 0.41, call OI 70.9%). Le positionnement options est clairement bullish, mais le comportement du cours (recul sur volume de distribution) et l'absence de catalyseur fondamental limitent la traduction en momentum positif.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 67.2 / 100 |
| Score Global Ajusté | **59.2 / 100** |
| Score Opportunité | **6.7 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | **4.5 / 10** |
| Recommandation agent | **ATTENDRE** |
| Timing agent | **Défavorable** |

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Opportunité | 6.7 / 10 | **~4.6 / 10** | Plafonnement Valorisation à 5/10 (Qualité 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus timing défavorable (−0.3 pt) ; malus données earnings Q1 manquantes (−0.5 pt) ; bonus données options restaurées (+0.2 pt) |
| Score Catalyseur | 8.0 / 10 | **7.7 / 10** | Malus earnings anomalie persistante −0.3 pt ; bonus options restaurées +0.0 pt (déjà intégré) |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 4.5 / 10 | **4.5 / 10** | = |
| **Score Global Ajusté** | 59.2 / 100 | **~46 / 100** | Recalculé sur base 4.6/10 × 10 = 46 |
| **Recommandation analyste** | — | **SURVEILLER** | Score 35–49 ; Qualité 1/6 exclut tout sizing standard |

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $10.09 | — |
| Stop-Loss | **$9.01** | 2× ATR (−10.7%) — confirmé par recommandations agent |
| Take-Profit | **$11.71** | 3× ATR (+16.1%) — confirmé par recommandations agent |
| Ratio R/R | **1.5×** | Stable |
| Résistance intermédiaire | **$10.49** | High du jour — rejet net, à surveiller |
| Résistance majeure (MM50) | **$11.19** | Breakout requis pour inflexion de tendance |
| Max pain options | **$11.00** | Aimant technique J+4 — proche du TP ATR |

**Note sur le max pain vs TP :** Le max pain $11.00 se situe entre la résistance MM50 ($11.19) et le TP ATR ($11.71). Si le cours converge vers le max pain à l'échéance 2026-06-05, il atteindrait approximativement $11.00 (+9.0%), ce qui est en-deçà du TP ATR mais constituerait un premier objectif réaliste technique.

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — SURVEILLER (~46/100). Amélioration mineure : données options restaurées (structure haussière), mais fondamental dégradé et technique baissier inchangés.**

La thèse de **SURVEILLER** du snapshot 2026-06-01 10:00 UTC est **confirmée** avec une nuance positive liée à la restauration des données options. Cinq observations :

1. **Données options RÉSOLUES** — Le passage du snapshot 10:00 au snapshot 13:00 UTC a vu la correction complète de l'anomalie options : max pain $11.00 (cohérent), put/call 0.41 (très faible, biais haussier), call OI 70.9% (domination calls). Cette structure options est **haussière** et place un aimant technique à $11.00 pour l'échéance J+4 (2026-06-05).

2. **Aucun changement de cours/RSI/volume** — Entre 10:00 et 13:00 UTC, les données de marché sont inchangées (marché US fermé). Le close reste $10.09, le RSI 47.2, le volume 1.94M. La séance US du jour a donc déjà été entièrement analysée dans le snapshot 10:00 UTC.

3. **Short interest stable à 25.03%** — Le niveau très élevé est maintenu. Le setup short squeeze latent persiste mécaniquement (25% du float shorté + call OI 70.9% = combustible élevé), mais le timing de déclenchement reste incertain sans catalyseur fondamental.

4. **Agent stable ATTENDRE (59.2/100)** — Le modèle quantitatif ne change pas de recommandation entre les deux snapshots, ce qui est cohérent avec la stabilité des données de marché.

5. **Anomalie earnings persistante** — L'earnings Q1 reste placé au 2026-06-01 (jour J) dans `upcoming_events_latest.json` sans résultats visibles. Cette incertitude continue de peser sur le Score Catalyseur (−0.3 pt).

**Recommandation finale :** **SURVEILLER — pas de position.** La restauration des données options est une amélioration analytique notable qui renforce le setup haussier latent (max pain $11.00, put/call 0.41, call OI 70.9%). Cependant, la directionnalité reste incertaine : le cours sous MM50 (−9.8%), le recul séance sur volume de distribution (−3.26% sur 1.31×) et l'empilement des shorts (25.03%) suggèrent une distribution plutôt qu'une accumulation. La structure options haussière et le setup short squeeze mécanique sont des éléments de surveillance actifs, mais sans catalyseur fondamental (earnings, guidance, M&A), toute entrée reste un trade spéculatif avec sizing minimal. La résolution de l'anomalie earnings et le comportement à l'échéance options J+4 sont les deux catalyseurs clés à surveiller.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-06-01 (snapshot 13:00 UTC)*
*Sources : data/latest.json (fetched 2026-06-01T13:00:16Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-06-01), data/social_sentiment_latest.json (2026-06-01), data/fx_exposure_latest.json (2026-06-01), data/upcoming_events_latest.json (2026-06-01), data/events_latest.json (2026-06-01), data/validation_report.txt (2026-06-01)*
