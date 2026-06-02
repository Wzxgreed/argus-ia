# FUBO — Mise à Jour (2026-06-02, snapshot 13h UTC)

> **Niveau d'impact :** 🟡 Modéré — Cours stable **$11.52** (marché US non ouvert à 13h UTC ; dernier close identique au snapshot 21h UTC du 2026-06-01), RSI **67.48** inchangé. **Repositionnement options majeur haussier** : max pain **$12.00** (+9.1% vs $11.00), put/call **0.20** (−51.2% vs 0.41), call OI **83.2%** (+12.3 pts vs 70.9%). Spot désormais **−4.0% sous le max pain** (vs +4.7% au-dessus hier), réintroduisant un aimant haussier vers $12.00 à l'échéance J+3 (2026-06-05). Scoring agent inchangé **ACHETER Standard** (73.5/100 ajusté 78.5/100). Anomalie earnings persistante (`upcoming_events` place l'earnings au **2026-06-02**, `days_until: 0`, aucun résultat visible). Ajustement analyste maintenu **ACHETER Réduit (~64.5/100)**.
> **Référence précédente :** [FUBO_2026-06-01_update.md](FUBO_2026-06-01_update.md) (snapshot 21:00 UTC — close $11.52, RSI 67.48, volume 1.79M, max pain $11.00, put/call 0.41, call OI 70.9%, agent ACHETER Standard 78.5/100)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-01 21:00 UTC)

| Métrique | 2026-06-01 21:00 UTC | **2026-06-02 13:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $11.52 | **$11.52** | **Stable** — marché non ouvert |
| Previous close | $10.09 | **$10.09** | Stable |
| Change % vs previous | +14.17% | **+14.17%** | Stable |
| Volume séance | 1 787 953 | **1 822 500** | **+1.9%** |
| Volume vs 20j | 1.22× | **1.24×** | Stable — liquidité confirmée |
| RSI 14j | 67.48 | **67.48** | Stable |
| ATR 14j | $0.62 | **$0.62** | Stable |
| MM 50j | $11.15 | **$11.15** | Stable |
| Market Cap (Yahoo) | $339.1M | **$339.1M** | Stable |
| P/E TTM (Yahoo) | 3.00x | **3.00x** | Stable |
| Short Interest | 25.03% | **25.03%** | Stable |
| **Max Pain (API)** | **$11.00** | **$12.00** | **+9.1% — repositionné haussier** 🔴 |
| **Put/Call Ratio (API)** | **0.41** | **0.20** | **−51.2% — biais haussier renforcé** 🔴 |
| **Call OI % (API)** | **70.9%** | **83.2%** | **+12.3 pts — domination calls accrue** 🔴 |
| Échéance options | 2026-06-05 | **2026-06-05** | J+3 |
| Spot vs Max Pain | +4.7% | **−4.0%** | **Inversé — aimant haussier réactivé** 🔴 |
| Spot vs MM50 | +3.3% | **+3.3%** | Stable — au-dessus |
| **Score Global (agent)** | 73.5/100 | **73.5/100** | Stable |
| **Score Global Ajusté (agent)** | 78.5/100 | **78.5/100** | Stable |
| **Score Opportunité (agent)** | 7.3/10 | **7.3/10** | Stable |
| **Score Momentum (agent)** | 7.0/10 | **7.0/10** | Stable |
| **Recommandation (agent)** | ACHETER Standard | **ACHETER Standard** | Stable |
| **Timing (agent)** | Favorable | **Favorable** | Stable |

**Constats :**
1. **Repositionnement options majeur haussier** — Le max pain remonte de $11.00 à $12.00 (+9.1%), le put/cral chute de 0.41 à 0.20 (−51.2%) et le call OI grimpe de 70.9% à 83.2%. Cette recomposition du positionnement options est le signal le plus significatif du snapshot. Elle indique une anticipation haussière accrue des opérateurs sur l'échéance J+3 (2026-06-05). Le spot à −4.0% sous le max pain signifie que les market makers ont un intérêt mécanique à rapprocher le cours vers $12.00 à l'approche de l'échéance.
2. **Cours et indicateurs techniques inchangés** — Le snapshot 13h UTC précède l'ouverture du marché US (14h30 UTC). Tous les indicateurs de prix (close $11.52, RSI 67.48, ATR $0.62, MM50 $11.15) sont donce identiques au close du 2026-06-01. Le volume légèrement révisé à 1.82M (vs 1.79M) est une correction de données, sans impact matériel.
3. **Anomalie earnings persistante et décalée** — `data/upcoming_events_latest.json` (2026-06-02) place désormais l'earnings au **2026-06-02** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible dans `data/latest.json`. L'anomalie est passée de 2026-06-01 à 2026-06-02 sans résolution. [ANOMALIE PERSISTANTE — J+? NON RÉSOLU]
4. **Structure options et short squeeze** — Le short interest stable à 25.03% combiné au call OI 83.2% et au put/call 0.20 constitue un setup de short squeeze mécanique très favorable. Le max pain $12.00 agit comme un aimant haussier. Cependant, le RSI 67.48 reste proche du surachat (70), limitant la marge de progression technique avant consolidation.
5. **Validation report** (`data/validation_report.txt`, 2026-06-02) : 25/29 tickers OK, 4 KO. FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 67.48 | **Neutre-haussier proche surachat** — stable, marge de 2.52 pts avant 70 |
| MM 50j | $11.15 | Cours au-dessus — écart **+3.3%** (breakout confirmé) |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.62 | Volatilité absolue stable (5.4% du spot) |
| Volume vs 20j | 1.24× | Liquidité confirmée au-dessus de la moyenne |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+38.6%** |
| Short Interest | 25.03% | **Très élevé** — stable |

**Niveaux clés :**
- Support immédiat : **$10.25** (low 2026-06-01)
- Support psychologique : **$11.00** (ancien max pain / ancienne résistance → support)
- Support dynamique : **$11.15** (MM50)
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$11.68** (high 2026-06-01)
- Résistance majeure (max pain) : **$12.00** (échéance J+3 — spot à −4.0%)
- Résistance technique : **$12.00** (arrondi psychologique + max pain)
- Stop-loss ATR (2×) : **$10.28** (−10.8%)
- Take-profit ATR (3×) : **$13.38** (+16.2%)
- Ratio R/R : **1.5×**

**Verdict timing :** Favorable — cours au-dessus de MM50 (+3.3%), momentum haussier confirmé par volume 1.24×, structure options haussière renforcée (put/call 0.20, call OI 83.2%). Le max pain $12.00 agit comme un aimant haussier à l'échéance J+3. Risque : RSI 67.48 proche surachat (70) → consolidation ou pullback vers $11.15–$11.50 possible avant extension.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 2026-06-02 13h UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $339.1M | 3.00x | 0.42x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×9.6 sur la capitalisation (stable en structure).

### Ratios disponibles (Yahoo + FMP, snapshot 2026-06-02)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 3.00x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 24.41x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.444x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.42x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×7.6 avec Yahoo |
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

### Options — Repositionnement Majeur Haussier

| Signal | Valeur 21:00 UTC 01/06 | Valeur 13:00 UTC 02/06 | Lecture |
|---|---|---|---|
| Max Pain | $11.00 | **$12.00** | Repositionné haussier — spot à −4.0% |
| Put/Call Ratio | 0.41 | **0.20** | Biais haussier renforcé — extrêmement bas |
| Call OI % | 70.9% | **83.2%** | Domination calls accrue |
| Échéance options | 2026-06-05 | **2026-06-05** | J+3 |

**Lecture institutionnelle :** Le repositionnement options est le principal événement du snapshot. Le max pain remonté à $12.00 place le spot à −4.0% en dessous, réactivant l'hypothèse d'un aimant haussier mécanique à l'échéance J+3 (2026-06-05). Le put/call 0.20 est extrêmement faible, indiquant un positionnement net haussier très concentré. Le call OI 83.2% renforce cette lecture. Cette structure, combinée au short interest 25.03%, constitue un setup de short squeeze mécanique très favorable si un catalyseur positif survient (ex : résolution de l'anomalie earnings avec un beat).

Le spot devrait converger mécaniquement vers $12.00 à l'approche de l'échéance, soit +4.2% de potentiel de gain intrinsèque lié à la structure options. Cependant, ce gain est bien inférieur au TP ATR ($13.38, +16.2%).

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +336%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-06-02) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` (2026-06-02) place l'événement au **2026-06-02** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plusieurs jours d'attente. L'anomalie a migré de 2026-06-01 à 2026-06-02 sans résolution. [ANOMALIE CALENDRIER PERSISTANTE]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-06-02) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-06-02) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

### Sector Rotation

- `data/sector_rotation_latest.json` (2026-06-02) : XLC classé **bottom 3** (momentum score 0.0 / 10). Signal système : **ROTATION_TO_CYCLICAL**. Malus sectoriel maintenu : −0.5 pt composite.

### Geo Risk

- `data/geo_risk_latest.json` (2026-05-17) : FUBO non flaggué. Score Politique non calculé.

### Quant Report

- `data/quant_report_latest.json` (2026-05-17) : n = 0, pas assez de signaux historiques FUBO. Win rate 0%, p-value 1.0 (insuffisant). Aucune calibration auto applicable.

**Verdict Sentiment :** Neutre à haussier. Le silence médiatique persiste, mais le repositionnement options est un signal technique fort. L'unique catalyseur observable reste la structure options (max pain $12.00, put/call 0.20, call OI 83.2%) et le short interest élevé (25.03%). L'anomalie earnings persistante continue de peser sur le Score Catalyseur.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 73.5 / 100 |
| Score Global Ajusté | **78.5 / 100** |
| Score Opportunité | **7.3 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | **7.0 / 10** |
| Recommandation agent | **ACHETER** |
| Timing agent | **Favorable** |
| Sizing agent | **Standard** |

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Catalyseur | 8.0 / 10 | **7.7 / 10** | Malus earnings anomalie persistante −0.3 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 7.0 / 10 | **7.4 / 10** | Bonus repositionnement options haussier (+0.5 pt), malus RSI proche surachat (−0.1 pt) |
| **Score Opportunité** | 7.3 / 10 | **~6.5 / 10** | Recalculé : (7.7×0.35) + (5.0×0.40) + (7.4×0.25) = 6.495 ≈ **6.5/10** |
| **Score Global** | — | **65.0 / 100** | 6.5 × 10 |
| Malus sectoriel XLC bottom 3 | — | **−0.5 pt** | Composite |
| **Score Global Ajusté** | 78.5 / 100 | **~64.5 / 100** | Zone 60–74 |
| **Recommandation analyste** | — | **ACHETER Réduit** | Score 60–74 ; Qualité 1/6 impose sizing réduit |

**Note sur la divergence agent/analyste :** L'agent quantitatif place FUBO en ACHETER Standard (78.5/100) avec un sizing standard. L'ajustement analyste applique le plafonnement Qualité 1/6 (Valorisation → 5.0/10) et le malus sectoriel XLC bottom 3. Le Score Opportunité ajusté tombe à **6.5/10**, donnant un Score Global **~64.5/100** — zone **ACHETER Réduit** (60–74). La Qualité 1/6 interdit tout sizing standard ; le sizing reste **réduit**.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $11.52 | — |
| Stop-Loss | **$10.28** | 2× ATR (−10.8%) — inchangé |
| Take-Profit | **$13.38** | 3× ATR (+16.2%) — inchangé |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$10.25** | Low 2026-06-01 |
| Support psychologique | **$11.00** | Ancien max pain / résistance → support |
| Support dynamique | **$11.15** | MM50 |
| Résistance immédiate | **$11.68** | High 2026-06-01 |
| Résistance technique | **$12.00** | Max pain (échéance J+3) + arrondi psychologique |

**Note sur le max pain vs TP :** Le max pain $12.00 se situe entre la résistance high du jour ($11.68) et le TP ATR ($13.38). Si le cours converge vers le max pain à l'échéance 2026-06-05, le gain serait de +4.2%, bien en-deçà du TP mais constituant un objectif technique intermédiaire réaliste. Le max pain agit comme un aimant haussier court terme.

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $14.00+ (extension breakout)
- Miss + guidance down → abaisser SL à $8.50 (support psychologique) voire $8.31 (52W low)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — ACHETER Réduit (~64.5/100). Repositionnement options haussier majeur (max pain $12.00, put/call 0.20, call OI 83.2%) sur cours stable. Fondamental inchangé (Qualité 1/6).**

La thèse **ACHETER Réduit** du snapshot 2026-06-01 21:00 UTC est **confirmée** avec une nuance technique renforcée par le repositionnement options. Quatre observations :

1. **Repositionnement options majeur haussier** — Le max pain remonte de $11.00 à $12.00 (+9.1%), le put/call chute de 0.41 à 0.20 et le call OI passe de 70.9% à 83.2%. Ce repositionnement est le signal le plus significatif du snapshot : il indique une anticipation haussière accrue des opérateurs sur l'échéance J+3. Le spot à −4.0% sous le max pain introduit un aimant haussier mécanique ($12.00 = +4.2%). Cependant, la probabilité de pinning vers $12.00 dépendra du comportement du marché à l'ouverture du 2026-06-02 (14h30 UTC).

2. **Cours et indicateurs techniques inchangés** — Le snapshot 13h UTC précède l'ouverture du marché US. Le close $11.52, le RSI 67.48, l'ATR $0.62 et la MM50 $11.15 sont identiques au snapshot précédent. Le volume confirmé à 1.24× maintient la liquidité au-dessus de la moyenne. Le cours reste au-dessus de la MM50 (+3.3%), confirmant l'inflexion technique de courte durée.

3. **Anomalie earnings persistante et migrée** — L'earnings Q1 reste placé au jour J (`days_until: 0`) mais la date a migré de 2026-06-01 à 2026-06-02 dans `upcoming_events_latest.json`. Cette anomalie calendaire persistante continue de peser sur le Score Catalyseur (−0.3 pt) et limite toute upgrade de la recommandation. La résolution de cette anomalie (publication effective des résultats Q1) serait le catalyseur fondamental clé à surveiller.

4. **Setup short squeeze intact et renforcé** — Le short interest stable à 25.03% combiné au call OI 83.2% et au put/call 0.20 constitue un setup de short squeeze mécanique très favorable. Si un catalyseur positif survient (beat earnings, guidance raise, ou même résolution de l'anomalie calendaire avec des résultats supérieurs aux attentes), la compression short pourrait provoquer un spike technique rapide. Cependant, sans catalyseur, le mouvement restera dicté par la structure options et le max pain $12.00.

**Recommandation finale :** **ACHETER Réduit — sizing minimal.** Le repositionnement options haussier renforce le setup technique (aimant $12.00, put/call 0.20, call OI 83.2%), mais le fondamental dégradé (Qualité 1/6, patrimoine net négatif, FCF négatif) et l'anomalie earnings persistante limitent strictement le sizing. Le timing est Favorable (cours > MM50, volume > moyenne, structure options haussière), mais le RSI 67.48 proche surachat (70) suggère d'attendre un pullback vers $11.15–$11.50 pour toute entrée optimale. Le comportement à l'ouverture du marché US (14h30 UTC) et à l'échéance options J+3 (2026-06-05) restent les deux catalyseurs techniques clés à surveiller.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-06-02 (snapshot 13:00 UTC)*
*Sources : data/latest.json (fetched 2026-06-02T13:00:01Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-06-02), data/social_sentiment_latest.json (2026-06-02), data/fx_exposure_latest.json (2026-06-02), data/upcoming_events_latest.json (2026-06-02), data/events_latest.json (2026-06-02), data/validation_report.txt (2026-06-02)*
