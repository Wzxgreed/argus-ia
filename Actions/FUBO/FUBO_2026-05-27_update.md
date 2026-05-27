# FUBO — Mise à Jour (2026-05-27, snapshot 17:00 UTC)

> **Niveau d'impact :** 🟡 Modéré — Mutation technique significative : cours **$9.97 (+4.73%)**, RSI **43.35** (+22.27 pts vs 13:00 UTC, sortie de la survente extrême), volume **920 203** (0.64× moy. 20j, en retrait supplémentaire). Scoring agent dégradé **ACHETER (Réduit) → ATTENDRE** (66.0/100, ajusté 58.0/100). Ajustement analyste inchangé **SURVEILLER (~42/100)**. Earnings Q1 2026 J=0 non résolu après 8 jours. Spot désormais à **−0.3%** du max pain $10.00 (vs −4.8% à 13:00 UTC).
> **Référence précédente :** [FUBO_2026-05-27_update.md](FUBO_2026-05-27_update.md) (snapshot 13:00 UTC — close $9.52, RSI 21.08, volume 1 004 300 / 0.70×, scoring agent 64.2/100 ACHETER Réduit, thèse SURVEILLER)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-27 13:00 UTC)

| Métrique | 2026-05-27 13:00 UTC | **2026-05-27 17:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.52 | **$9.97** | **+4.73%** |
| Change % vs previous | −2.36% | **+4.73%** | **+7.09 pp** |
| Volume séance | 1 004 300 | **920 203** | **−8.4%** |
| Volume vs 20j | 0.70× | **0.64×** | **Liqui. en retrait** |
| RSI 14j | 21.08 | **43.35** | **+22.27 pts** |
| ATR 14j | $0.62 | **$0.55** | **−11.3%** |
| MM 50j | $11.42 | **$11.34** | **−0.7%** |
| Market Cap (Yahoo) | $280.2M | **$293.5M** | **+4.7%** |
| P/E TTM (Yahoo) | 2.48x | **2.60x** | **+4.8%** |
| Forward P/E | 20.17x | **21.12x** | **+4.7%** |
| Short Interest | 22.84% | **22.84%** | **Stable** |
| Max Pain (API) | $10.00 | **$10.00** | **Stable** |
| Put/Call Ratio (API) | 0.51 | **0.51** | **Stable** |
| Call OI % (API) | 66.3% | **66.3%** | **Stable** |
| Échéance options | 2026-05-29 | **2026-05-29** | **J+2** |
| **Score Global (agent)** | 67.2/100 | **66.0/100** | **−1.2 pt** |
| **Score Global Ajusté (agent)** | 64.2/100 | **58.0/100** | **−6.2 pts** |
| **Score Opportunité (agent)** | 6.7/10 | **6.6/10** | **−0.1 pt** |
| **Score Momentum (agent)** | 4.5/10 | **4.0/10** | **−0.5 pt** |
| **Recommandation (agent)** | ACHETER (Réduit) | **ATTENDRE** | **Downgrade** |

**Constats :**
1. **Rebond technique significatif (+4.73%)** — Le close passe de $9.52 à **$9.97**, soit le plus haut niveau depuis le 26/05 au matin. Le rebond intervient après 8 jours de consolidation autour de $9.20–$9.75.
2. **RSI sort de la survente extrême** — De **21.08 à 43.35** (+22.27 pts), franchissant le seuil 30 pour la première fois depuis le 20/05. La zone de survente extrême est quittée, mais le RSI reste en zone neutre-baisse (sous 50).
3. **Liquidité en retrait supplémentaire** — Volume 920 203 (0.64× moyenne 20j), en baisse de 8.4% vs le snapshot 13:00 UTC et de 36% vs la moyenne 20j. Le rebond s'effectue sur des volumes décroissants, signalant un **manque de conviction institutionnelle**.
4. **Agent downgrade en ATTENDRE** — Malgré le rebond cours et la sortie de survente, l'algorithme de scoring abaisse la recommandation de **ACHETER (Réduit) à ATTENDRE** et le Score Global Ajusté de 64.2 à **58.0/100**. Le Score Momentum recule de 4.5 à **4.0/10**, suggérant que le rebond n'est pas interprété comme un signal de momentum haussier durable par le modèle.
5. **Spot désormais collé au max pain** — À $9.97, le spot n'est plus qu'à **−0.3%** du max pain $10.00 (vs −4.8% à 13:00 UTC). La pression de pinning options s'est considérablement atténuée ; le titre est désormais en équilibre techniques options en échéance J+2.
6. **ATR compressé à $0.55** — La volatilité absolue atteint 5.5% du spot, son plus bas niveau observé. Cela réduit la latitude du trade (SL/TP resserrés) mais confirme la compression de volatilité pré-échéance.
7. **Anomalie calendrier earnings persistante (J+8)** : `data/upcoming_events_latest.json` (2026-05-27) place l'earnings au **2026-05-27** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible dans `data/latest.json` au snapshot 17:00 UTC. [ANOMALIE CALENDRIER PERSISTANTE — J+8 NON RÉSOLU]
8. **Validation report** (`data/validation_report.txt`, 2026-05-27) : 23/26 tickers OK, 4 errors (VRT schema, AST/AXA/QTBS fetch failed), 2 warnings (IREN, NOK). FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 43.35 | **Neutre-baisse** — sortie de survente extrême (21.08), mais sous 50 |
| MM 50j | $11.34 | Cours sous la moyenne — écart **−12.1%** (vs −16.6% à 13:00 UTC) |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.55 | Volatilité absolue compressée (5.5% du spot) |
| Volume vs 20j | 0.64× | Réduit — liquidité en retrait, risque de slippage élevé |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+20.0%** (vs +14.6% à 13:00 UTC) |

**Niveaux clés :**
- Support immédiat : **$9.53** (low du jour)
- Support secondaire : **$8.31** (52W low)
- Résistance : **$10.00** (niveau psychologique + **max pain**)
- Résistance majeure : **$11.34** (MM50)
- Stop-loss ATR (2×) : **$8.87** (−11.0%)
- Take-profit ATR (3×) : **$11.62** (+16.5%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — sous MM50, RSI neutre-baisse malgré la sortie de survente, volume en retrait (0.64×). Le rebond de +4.73% sur volume décroissant n'est pas un signal de reversal structurel. La tendance baissière primaire reste intacte (sous MM50). La compression de l'écart au max pain (−0.3%) suggère un équilibre techniques options sans directionnalité claire en échéance J+2.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale dans le snapshot 17:00 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $293.5M | 2.60x | 0.36x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×11.2 sur la capitalisation (légère réduction vs ×11.7 à 13:00 UTC du fait de la hausse du cours Yahoo).

### Ratios disponibles (Yahoo + FMP, close 2026-05-27)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.60x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 21.12x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.43x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.36x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×8.9 avec Yahoo |
| Beta | 2.508 | Extrême |
| Short Interest | 22.84% | Très élevé — inchangé |
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
| Max Pain | $10.00 | **$10.00** | Stable |
| Put/Call Ratio | 0.51 | **0.51** | Stable — biais haussier modéré |
| Call OI % | 66.3% | **66.3%** | Stable — domination call |
| Échéance options | 2026-05-29 | **2026-05-29** | J+2 — pinning neutre (spot à −0.3%) |

**Lecture institutionnelle :** Le spot $9.97 se situe à **−0.3%** sous le max pain $10.00, contre −4.8% à 13:00 UTC. La pression de pinning baissier s'est considérablement atténuée. En échéance J+2 (2026-05-29), le titre est désormais en zone d'équilibre techniques options. Le call OI dominant (66.3%) et le short interest massif (22.84%) maintiennent un **setup short squeeze latent**, mais la compression de l'écart au max pain réduit la probabilité d'un mouvement explosif sans catalyseur externe. Si un catalyseur positif survient (ex : résolution earnings, surprise EPS), le squeeze technique pourrait propulser le cours au-dessus de $10.50–$11.00. Sans catalyseur, la consolidation autour de $10.00 reste le scénario central.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +404%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-05-27) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` place l'événement au **2026-05-27** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après 8 jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE — J+8 NON RÉSOLU]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-05-27) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-05-27) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

**Verdict Sentiment :** Neutre à prudent. Silence médiatique et institutionnel total. Le repositionnement options call-biased (66.3%) et la compression de l'écart au max pain sont les seuls signaux techniques observables ; aucun catalyseur fondamental n'est détecté.

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

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Opportunité | 6.6 / 10 | **~4.2 / 10** | Plafonnement Valorisation à 5/10 (Qualité 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus liquidité 0.64× (−0.3 pt) ; malus timing défavorable (−0.3 pt) ; malus données earnings Q1 manquantes (−0.5 pt) |
| Score Catalyseur | 8.0 / 10 | **7.5 / 10** | Malus options put-biased historique −0.5 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 4.0 / 10 | **4.0 / 10** | = |
| **Score Global Ajusté** | 58.0 / 100 | **~42 / 100** | Recalculé sur base 4.2/10 × 10 = 42 |
| **Recommandation analyste** | — | **SURVEILLER** | Score < 50 ; Qualité 1/6 exclut tout sizing standard ; liquidité réduite |

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — n = 0, pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1.0 (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

**Sector Rotation (`data/sector_rotation_latest.json`) :**
- Date 2026-05-27 : XLC classé **bottom 3** (momentum score 0.0 / 10).
- Malus sectoriel maintenu : −0.5 pt composite.

**Geo Risk (`data/geo_risk_latest.json`) :**
- Date 2026-05-17 — FUBO non flaggué. Score Politique non calculé.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.97 | — |
| Stop-Loss | **$8.87** | 2× ATR (−11.0%) — resserré par compression ATR |
| Take-Profit | **$11.62** | 3× ATR (+16.5%) |
| Ratio R/R | **1.5×** | Stable |
| Max Pain | **$10.00** | Spot à −0.3% — équilibre techniques options J+2 |
| Résistance intermédiaire | **$10.00** | Niveau psychologique + max pain — à surveiller en échéance |
| Résistance majeure | **$11.34** | MM50 — breakout requis pour inflexion de tendance |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE MODIFIÉE — SURVEILLER avec nuance technique améliorée (snapshot 17:00 UTC, rebond +4.73%, RSI sort de survente extrême, agent downgrade ATTENDRE, earnings J+8 non résolu)**

La thèse de **SURVEILLER** du snapshot 13:00 UTC du 27/05 est **modifiée** par l'arrivée d'un rebond technique significatif, mais le verdict final reste inchangé. Sept observations :

1. **Rebond technique significatif (+4.73%) avec sortie de survente extrême** — Le close remonte à **$9.97** et le RSI bondit de 21.08 à **43.35** (+22.27 pts), franchissant le seuil 30 pour la première fois depuis le 20/05. C'est une amélioration technique objective. Cependant, le RSI reste sous 50 (zone neutre-baisse) et le cours demeure largement sous la MM50 (−12.1%).

2. **Volume en retrait supplémentaire (0.64×)** — Le rebond s'effectue sur un volume de 920 203, inférieur au snapshot 13:00 UTC (1 004 300) et à 36% de la moyenne 20j. C'est le **signal le plus inquiétant** : un rebond de près de +5% sans volume de suivi est caractéristique d'un mouvement technique de consolidation ou d'un short covering limité, et non d'un retour d'acheteurs institutionnels.

3. **Agent downgrade en ATTENDRE (58.0/100 ajusté)** — Malgré le rebond cours et la sortie de survente, l'algorithme de scoring abaisse la recommandation de ACHETER (Réduit) à **ATTENDRE** et le Score Momentum de 4.5 à **4.0/10**. Cette divergence (cours qui monte, momentum qui baisse aux yeux du modèle) confirme le caractère non-convictionnel du rebond.

4. **Compression de l'écart au max pain** — Le spot à $9.97 n'est plus qu'à **−0.3%** du max pain $10.00. La pression de pinning baissier s'est atténuée, mais cela signifie aussi que le potentiel de mean-reversion haussier vers le max pain s'est réduit. Le titre est désormais en équilibre techniques options.

5. **Anomalie calendrier earnings persistante (J+8)** : `upcoming_events_latest.json` place l'earnings FUBO au **2026-05-27** (jour J) — aucun résultat Q1 n'est visible après 8 jours d'attente. Cette incohérence demeure le risque fondamental majeur.

6. **Setup short squeeze latent affaibli mais présent** — short interest 22.84% + call OI 66.3% + spot proche max pain = configuration explosive si catalyseur positif. Mais le volume en retrait (0.64×) et l'absence de news réduisent la probabilité de déclenchement immédiat.

7. **Fondamental inchangé — profil dégradé** : Score Qualité 1/6, patrimoine net négatif, FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%. La divergence Yahoo/FMP persiste (market cap $293.5M vs ~$3.3B, écart ×11.2).

**Arguments confirmant la prudence :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Divergence Yahoo/FMP persistante** — market cap $293.5M vs ~$3.3B (×11.2).
3. **Timing défavorable** — sous MM50 (−12.1%), RSI neutre-baisse malgré la sortie de survente, volume réduit.
4. **Liquidité réduite** — volume 0.64×, risque de slippage sur toute taille de position.
5. **Données manquantes** — pas de résultats Q1 après 8 jours, pas de news, pas de accounting risk, pas de social sentiment.
6. **Quant report non significatif** — pas assez d'historique.
7. **Earnings Q1 non résolu** — incertitude sur le calendrier de publication et les résultats attendus.
8. **Agent downgrade** — le modèle quantitatif ne valide pas le rebond comme un signal d'achat.
9. **Max pain $10.00 au-dessus du spot** — bien que l'écart se soit compressé, le pinning reste un contre-signal.
10. **Momentum agent en retrait** — 4.0/10, confirmant la faiblesse du mouvement de prix aux yeux du modèle.

**Recommandation finale :** **SURVEILLER — pas de position.** Le rebond de +4.73% et la sortie de survente extrême (RSI 43.35) sont des évolutions techniques positives, mais le volume en retrait (0.64×) et le downgrade de l'agent quantitatif (ATTENDRE, Score Momentum 4.0/10) invalident toute interprétation haussière. Le setup short squeeze latent (short interest 22.84% + call OI 66.3%) persiste, mais sans fondement qualitatif ni volume de suivi. Toute entrée eventuelle resterait un trade spéculatif avec sizing minimal et stop-loss strict à $8.87. La résolution de l'anomalie earnings Q1 est le catalyseur clé à surveiller.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-05-27 (snapshot 17:00 UTC)*
*Sources : data/latest.json (fetched 2026-05-27T17:00:02Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-05-27), data/social_sentiment_latest.json (2026-05-27), data/fx_exposure_latest.json (2026-05-27), data/upcoming_events_latest.json (2026-05-27), data/events_latest.json (2026-05-27), data/validation_report.txt (2026-05-27)*
