# FUBO — Mise à Jour (2026-06-02, snapshot 17h UTC)

> **Niveau d'impact :** 🔴 Élevé — Correction technique **−4.34%** à **$11.02** sur volume effondré **0.38×** (536k vs moy. 20j 1.40M), RSI sort de la zone proche-surachat (**62.22**, −5.26 pts), cours franchissant **sous la MM50** ($11.10). **Downgrade agent majeur** : **ACHETER Standard 78.5/100 → ATTENDRE 58.0/100**, Score Opportunité **7.3 → 6.6**, Score Momentum **7.0 → 4.0** (momentum baissier), timing **Favorable → Défavorable**. Structure options inchangée (max pain $12.00, put/call 0.20, call OI 83.2%) mais spot désormais **−8.2% sous le max pain** (vs −4.0% à 13h). Anomalie earnings persistante (`days_until: 0`, aucun résultat visible).
> **Référence précédente :** [FUBO_2026-06-02_update.md](FUBO_2026-06-02_update.md) (snapshot 13:00 UTC — close $11.52, RSI 67.48, volume 1.82M / 1.24×, agent ACHETER Standard 78.5/100, ajustement analyste ACHETER Réduit ~64.5/100)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-02 13:00 UTC)

| Métrique | 2026-06-02 13:00 UTC | **2026-06-02 17:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $11.52 | **$11.02** | **−4.34%** 🔴 |
| Previous close | $10.09 | **$11.52** | — |
| Volume séance | 1 822 500 | **536 103** | **−70.6% — collapse liquidité** 🔴 |
| Volume vs 20j | 1.24× | **0.38×** | **Effondré — sous-moyenne critique** 🔴 |
| RSI 14j | 67.48 | **62.22** | **−5.26 pts — sortie zone surachat** |
| ATR 14j | $0.62 | **$0.63** | Stable |
| MM 50j | $11.15 | **$11.10** | Stable |
| Spot vs MM50 | +3.3% | **−0.7%** | **Franchissement sous MM50** 🔴 |
| Market Cap (Yahoo) | $339.1M | **$324.4M** | −4.4% |
| Short Interest | 25.03% | **25.03%** | Stable — très élevé |
| **Max Pain (API)** | **$12.00** | **$12.00** | Inchangé |
| **Put/Call Ratio (API)** | **0.20** | **0.20** | Inchangé — biais haussier extrême |
| **Call OI % (API)** | **83.2%** | **83.2%** | Inchangé — domination calls |
| Spot vs Max Pain | −4.0% | **−8.2%** | **Aimant haussier renforcé mécaniquement** |
| **Score Global (agent)** | 73.5/100 | **66.0/100** | **−7.5 pts** 🔴 |
| **Score Global Ajusté (agent)** | 78.5/100 | **58.0/100** | **−20.5 pts — downgrade majeur** 🔴 |
| **Score Opportunité (agent)** | 7.3/10 | **6.6/10** | **−0.7 pt** 🔴 |
| **Score Momentum (agent)** | 7.0/10 | **4.0/10** | **−3.0 pts — momentum baissier** 🔴 |
| **Recommandation (agent)** | ACHETER Standard | **ATTENDRE** | **Downgrade** 🔴 |
| **Timing (agent)** | Favorable | **Défavorable** | **Sous MM50 + momentum négatif** 🔴 |

**Constats :**
1. **Correction technique −4.34% avec volume collapse alarmant** — Le cours recule de $11.52 à $11.02, franchissant sous la MM50 ($11.10). Le volume s'effondre à 536k (0.38× moyenne 20j), soit une chute de 70.6% vs le snapshot 13h. Cette configuration (baisse sur volume effondré) est techniquement ambiguë : elle peut refléter un manque d'acheteurs (bearish) OU une absence de vendeurs agressifs après le repositionnement options. Cependant, le franchissement sous MM50 est un signal technique clairement défavorable.
2. **Downgrade agent majeur** — L'agent quantitatif est passé de **ACHETER Standard (78.5/100)** à **ATTENDRE (58.0/100)**. Le Score Opportunité chute de 7.3 à 6.6 et le Score Momentum de 7.0 à 4.0. Le timing passe de Favorable à Défavorable. Ce downgrade est directement lié au franchissement sous MM50 et à la perte de momentum.
3. **Structure options inchangée mais spot plus éloigné du max pain** — Max pain $12.00, put/call 0.20, call OI 83.2% : aucun changement depuis 13h. Cependant, le spot à −8.2% sous le max pain (vs −4.0%) renforce mécaniquement l'aimant haussier vers $12.00 à l'échéance J+3 (2026-06-05). Cette divergence entre structure options haussière et prix en baisse crée une tension technique : les market makers ont un intérêt mécanique à rapprocher le cours vers $12.00, mais le momentum baissier du spot contrebalance cette force.
4. **Anomalie earnings persistante** — `data/upcoming_events_latest.json` (2026-06-02) place toujours l'earnings au **2026-06-02** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible. L'anomalie calendaire pèse sur le Score Catalyseur.
5. **Validation report** (`data/validation_report.txt`, 2026-06-02) : 24/29 tickers OK, 5 KO. FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 62.22 | **Neutre-haussier** — sortie de la zone proche-surachat (marge de 7.78 pts avant 70) |
| MM 50j | $11.10 | Cours **sous** MM50 — écart **−0.7%** (breakout infirmé) 🔴 |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.63 | Volatilité absolue stable (5.7% du spot) |
| Volume vs 20j | 0.38× | **Liquidité effondrée** — well below average |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+32.6%** |
| Short Interest | 25.03% | **Très élevé** — stable |

**Niveaux clés :**
- Support immédiat : **$10.91** (low du jour)
- Support psychologique : **$11.00** (arrondi)
- Support dynamique : **$11.10** (MM50) — cours sous!
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$11.28** (high du jour)
- Résistance majeure : **$11.52** (close 13h UTC / previous close)
- Résistance technique (max pain) : **$12.00** (échéance J+3 — spot à −8.2%)
- Stop-loss ATR (2×) : **$9.76** (−11.4%)
- Take-profit ATR (3×) : **$12.91** (+17.2%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — cours sous MM50 (−0.7%), momentum baissier confirmé par le downgrade agent (Score Momentum 4.0/10), volume collapse 0.38×. La structure options haussière (max pain $12.00, put/call 0.20, call OI 83.2%) et le short interest 25.03% constituent un setup de short squeeze latent, mais le momentum immédiat est négatif. Attendre un retour au-dessus de MM50 ($11.10) avec volume confirmé (>0.8× moyenne) pour toute réactivation haussière.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 2026-06-02 17h UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $324.4M | 2.87x | 0.40x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×10.1 sur la capitalisation (stable en structure).

### Ratios disponibles (Yahoo + FMP, snapshot 2026-06-02)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.87x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 23.35x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.444x | Bas — valorisation type turnaround/distressed |
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

### Options — Structure Haussière Inchangée, Spot Plus Éloigné

| Signal | Valeur 13:00 UTC 02/06 | Valeur 17:00 UTC 02/06 | Lecture |
|---|---|---|---|
| Max Pain | $12.00 | **$12.00** | Inchangé — spot à −8.2% |
| Put/Call Ratio | 0.20 | **0.20** | Biais haussier extrême — inchangé |
| Call OI % | 83.2% | **83.2%** | Domination calls — inchangée |
| Échéance options | 2026-06-05 | **2026-06-05** | J+3 |

**Lecture institutionnelle :** La structure options n'a pas bougé depuis 13h, mais le spot a glissé de −4.0% à −8.2% sous le max pain. Cette divergence renforce mécaniquement l'aimant haussier vers $12.00 à l'échéance J+3 : les market makers ont un intérêt croissant à rapprocher le cours du max pain. Cependant, le volume collapse (0.38×) et le franchissement sous MM50 indiquent un manque de participation acheteuse qui pourrait limiter la force de ce mécanisme. Le setup de short squeeze reste théoriquement intact (short interest 25.03% + call OI 83.2% + put/call 0.20), mais le timing immédiat s'est dégradé.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +356%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-06-02) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` (2026-06-02) place l'événement au **2026-06-02** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plusieurs jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-06-02) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-06-02) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

### Sector Rotation

- `data/sector_rotation_latest.json` (2026-06-02) : XLC classé **bottom 3** (momentum score 0.0 / 10). Signal système : **NEUTRAL** (was ROTATION_TO_CYCLICAL). Malus sectoriel maintenu : −0.5 pt composite.

### Geo Risk

- `data/geo_risk_latest.json` (2026-05-17) : FUBO non flaggué. Score Politique non calculé.

### Quant Report

- `data/quant_report_latest.json` (2026-05-17) : n = 0, pas assez de signaux historiques FUBO. Win rate 0%, p-value 1.0 (insuffisant). Aucune calibration auto applicable.

**Verdict Sentiment :** Neutre à légèrement baissier. Le silence médiatique persiste. Le repositionnement options haussier (inchangé) contrebalance la baisse du spot, mais le volume collapse et le franchissement sous MM50 pèsent sur le sentiment technique. L'unique catalyseur observable reste la structure options et le short interest élevé.

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

**Note sur la divergence agent/analyste :** L'agent quantitatif place FUBO en ATTENDRE (58.0/100) suite au franchissement sous MM50 et à la perte de momentum. L'ajustement analyste applique le plafonnement Qualité 1/6 (Valorisation → 5.0/10) et le malus sectoriel XLC bottom 3. Le Score Opportunité ajusté tombe à **5.7/10**, donnant un Score Global **~56.5/100** — zone **ATTENDRE** (50–59). La thèse passe de **ACHETER Réduit** à **ATTENDRE**.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $11.02 | — |
| Stop-Loss | **$9.76** | 2× ATR (−11.4%) — révisé à la baisse (was $10.28) |
| Take-Profit | **$12.91** | 3× ATR (+17.2%) — révisé à la baisse (was $13.38) |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$10.91** | Low du jour |
| Support psychologique | **$11.00** | Arrondi |
| Support dynamique | **$11.10** | MM50 — cours sous |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$11.28** | High du jour |
| Résistance technique | **$11.52** | Close 13h UTC / previous close |
| Résistance majeure (max pain) | **$12.00** | Max pain (échéance J+3) |

**Note sur le max pain vs TP :** Le max pain $12.00 se situe entre la résistance immédiate ($11.28) et le TP ATR ($12.91). Si le cours converge vers le max pain à l'échéance 2026-06-05, le gain serait de +8.9% (vs +4.2% à 13h), bien en-deçà du TP mais constituant un objectif technique intermédiaire réaliste.

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE MODIFIÉE — ATTENDRE (~56.5/100). Correction technique −4.34% sur volume collapse, franchissement sous MM50, downgrade agent majeur (ACHETER → ATTENDRE). Structure options haussière intacte mais contrebalancée par momentum négatif.**

La thèse **ACHETER Réduit** du snapshot 2026-06-02 13:00 UTC est **modifiée** en **ATTENDRE** sur base des quatre observations suivantes :

1. **Correction technique −4.34% avec volume collapse** — Le cours chute de $11.52 à $11.02, franchissant sous la MM50 ($11.10). Le volume s'effondre à 536k (0.38× moyenne), soit une chute de 70.6% en 4 heures. Cette configuration rompt la dynamique haussière du matin. Le manque de liquidité suggère que le rally +8.03% du 2026-06-01 n'a pas trouvé de suivi institutionnel durable.

2. **Downgrade agent majeur** — L'agent quantitatif est passé de ACHETER Standard (78.5/100) à ATTENDRE (58.0/100). Le Score Momentum est tombé de 7.0 à 4.0 (momentum baissier) et le timing de Favorable à Défavorable. Ce downgrade est directement corrélé au franchissement sous MM50 et à la perte de momentum. L'ajustement analyste confirme ATTENDRE (~56.5/100) avec le plafonnement Qualité 1/6 et le malus sectoriel.

3. **Structure options inchangée mais tension technique accrue** — Max pain $12.00, put/call 0.20, call OI 83.2% : aucun changement. Le spot à −8.2% sous le max pain renforce mécaniquement l'aimant haussier vers $12.00 à l'échéance J+3. Cependant, le volume collapse limite la probabilité d'une convergence rapide. Le setup de short squeeze reste latent (short interest 25.03% + call OI dominant), mais sans catalyseur positif (résolution de l'anomalie earnings, beat, guidance raise), le mouvement restera contraint par le momentum baissier.

4. **Anomalie earnings persistante** — L'earnings Q1 reste placé au jour J (`days_until: 0`) sans résultat visible. Cette anomalie continue de peser sur le Score Catalyseur (−0.3 pt) et de justifier le statut ATTENDRE. La résolution de cette anomalie serait le catalyseur fondamental clé à surveiller.

**Recommandation finale :** **ATTENDRE.** Le franchissement sous MM50 ($11.10) et le momentum baissier (Score Momentum 4.0/10) imposent une pause. La structure options haussière (max pain $12.00, put/call 0.20, call OI 83.2%) et le short interest 25.03% constituent un support technique sous-jacent, mais le volume collapse (0.38×) et le timing Défavorable suggèrent d'attendre un retour au-dessus de MM50 avec volume confirmé (>0.8× moyenne) avant toute réactivation. L'échéance options J+3 (2026-06-05) reste un catalyseur technique à surveiller : si le spot converge vers $12.00, cela constituerait un +8.9% depuis le close actuel.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-06-02 (snapshot 17:00 UTC)*
*Sources : data/latest.json (fetched 2026-06-02T17:00:02Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-06-02), data/social_sentiment_latest.json (2026-06-02), data/fx_exposure_latest.json (2026-06-02), data/upcoming_events_latest.json (2026-06-02), data/events_latest.json (2026-06-02)*
