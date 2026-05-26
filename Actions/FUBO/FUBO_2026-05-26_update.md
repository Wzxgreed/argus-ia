# FUBO — Mise à Jour (2026-05-26, snapshot 21:00 UTC)

> **Niveau d'impact :** 🟢 Faible — Snapshot 21:00 UTC confirme la **stabilité globale** vs snapshot 17:00 UTC avec un léger repli du cours à $9.52 (−0.42% intraday, −2.36% vs previous close) et une **récupération partielle de la liquidité** (volume 987k, 0.69× moyenne 20j). RSI 21.08 inchangé en survente extrême, max pain $10.00 inchangé, scoring agent stable à 64.2/100 (ACHETER Réduit), ajustement analyste **SURVEILLER (~42/100)**. Earnings Q1 2026 toujours non résolu après 7 jours.
> **Référence précédente :** [FUBO_2026-05-26_update.md](FUBO_2026-05-26_update.md) (snapshot 17:00 UTC — close $9.56, RSI 21.26, volume 517k/0.37×, max pain $10.00, put/call 0.60, call OI 62.3%, scoring agent 64.2/100, thèse SURVEILLER)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (17:00 UTC)

| Métrique | 2026-05-26 17:00 UTC | **2026-05-26 21:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.56 | **$9.52** | **−0.42%** (−$0.04) |
| Change % vs previous | −1.95% | **−2.36%** | −0.41 pt vs previous close |
| Volume séance | 517 593 | **986 857** | **+90.6%** |
| Volume vs 20j | 0.37× | **0.69×** | **Récupération liquidité** |
| RSI 14j | 21.26 | **21.08** | −0.18 pt |
| ATR 14j | $0.62 | **$0.62** | — |
| MM 50j | $11.42 | **$11.42** | — |
| Market Cap (Yahoo) | $281.4M | **$280.2M** | −$1.2M |
| P/E TTM (Yahoo) | 2.49x | **2.48x** | −0.01x |
| Forward P/E | 20.25x | **20.17x** | −0.08x |
| Short Interest | 22.84% | **22.84%** | — |
| **Max Pain** | **$10.00** | **$10.00** | — |
| Put/Call Ratio | 0.60 | **0.60** | — |
| Call OI % | 62.3% | **62.3%** | — |
| Échéance options | 2026-05-29 | **2026-05-29** | J+3 |
| **Score Global (agent)** | 67.2/100 | **67.2/100** | — |
| **Score Global Ajusté (agent)** | 64.2/100 | **64.2/100** | — |
| **Score Opportunité (agent)** | 6.7/10 | **6.7/10** | — |
| **Score Momentum (agent)** | 4.5/10 | **4.5/10** | — |
| **Recommandation (agent)** | ACHETER (Réduit) | **ACHETER (Réduit)** | — |

**Constats :**
1. **Stabilité technique globale** — Le cours recule marginalement de $9.56 à $9.52 (−0.42% intraday, −2.36% vs previous close $9.75). Toutes les métriques techniques principales (RSI, ATR, MM50, options, scoring) sont **inchangées** entre 17:00 et 21:00 UTC.
2. **Récupération partielle de la liquidité** — Le volume passe de 517k à **987k actions** (+91%), remontant de 0.37× à **0.69× la moyenne 20j**. Cette amélioration est notable mais le titre reste sous sa moyenne de volume, signalant une liquidité encore réduite. Le cours −2.36% sur volume 0.69× n'est pas un signal de vente institutionnelle structurée, mais confirme l'absence d'appétit acheteur.
3. **RSI en survente extrême (21.08)** — stable en zone critique sous le seuil 30. Le titre reste techniquement survendu sans signe de reversal.
4. **ATR compressé à $0.62** (6.5% du spot) — volatilité absolue faible. La session −2.36% représente **3.8× l'ATR**, mouvement anormal mais moins extrême que le gap +6.67% du 25/05 (10.6× l'ATR).
5. **Max pain $10.00 inchangé** — Le spot $9.52 se situe à **−4.8%** sous le max pain (vs −4.4% à 17:00 UTC). La pression de pinning baissier vers $10.00 en échéance J+3 (2026-05-29) se maintient.
6. **Options stables** — Put/call 0.60 et call OI 62.3% inchangés. Le setup short squeeze latent (short interest 22.84% + call OI dominant) persiste, mais sans volume de suivi ni catalyseur.
7. **Earnings Q1 2026 non résolu après 7 jours** : `data/upcoming_events_latest.json` (2026-05-26) indique toujours l'événement au **2026-05-26** avec `days_until: 0`. Aucun résultat Q1 2026 (EPS, revenue, guidance) n'est visible dans `data/latest.json` au snapshot 21:00 UTC. [ANOMALIE CALENDRIER PERSISTANTE — J+7 NON RÉSOLU]
8. **Validation report** (`data/validation_report.txt`, 2026-05-26) : 23/26 tickers OK, 4 errors, 2 warnings. FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 21.08 | **Survente extrême** — sous le seuil 30, stable en zone critique |
| MM 50j | $11.42 | Cours sous la moyenne — écart **−16.6%** |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.62 | Volatilité absolue compressée (6.5% du spot) |
| Volume vs 20j | 0.69× | Réduit — liquidité partiellement récupérée mais sous moyenne |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+14.6%** |

**Niveaux clés :**
- Support immédiat : **$9.50** (low du jour)
- Support secondaire : **$8.31** (52W low)
- Résistance : **$10.00** (niveau psychologique + **max pain**)
- Résistance majeure : **$11.42** (MM50)
- Stop-loss ATR (2×) : **$8.28** (−13.0%)
- Take-profit ATR (3×) : **$11.38** (+19.5%)

**Verdict timing :** Défavorable — sous MM50, RSI en survente extrême sans signe de reversal structurel, volume partiellement récupéré (0.69×) mais reste sous moyenne. Le cours −2.36% sur fond de volume faible n'est pas un signal directionnel fiable (carnet d'ordres vide), mais confirme l'absence d'achat institutionnel. Le gap +6.67% du 25/05 a été partiellement effacé ($9.52 vs previous close $9.75 = −2.36%). Tendance baissière primaire intacte.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale dans le snapshot 21:00 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $280.2M | 2.48x | 0.35x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×11.7 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-26)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.48x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 20.17x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.43x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.35x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×9.1 avec Yahoo |
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

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain (API) | $10.00 | Spot sous max pain — écart **−4.8%** (vs −4.4% à 17:00 UTC) |
| Put/Call Ratio | 0.60 | Légèrement put-biased — sentiment dérivés prudent |
| Call OI % | 62.3% | Dominance calls stable — setup squeeze latent |
| Échéance options | 2026-05-29 | J+3 — pinning vers $10.00 si pas de catalyseur |

**Lecture institutionnelle :** Le spot $9.52 s'éloigne légèrement du max pain $10.00. La pression de pinning baissier se maintient en échéance J+3. Cependant, le call OI dominant (62.3%) et le short interest massif (22.84%) maintiennent un **setup short squeeze latent** — si un catalyseur positif survient (ex : résolution earnings, surprise EPS), le squeeze technique pourrait propulser le cours au-dessus de $10.00 vers $11.00–$11.50. Sans catalyseur, la gravitation options vers $10.00 reste le scénario central.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +428%. Consensus figé.

### News & Événements Corporates

- `data/news_2026-05-26.json` : **non disponible** — [DONNÉES MANQUANTES]
- `data/events_2026-05-26.json` : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` place l'événement au **2026-05-26** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après 7 jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE — J+7 NON RÉSOLU]

### FX Exposure

- `data/fx_exposure_2026-05-26.json` : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_2026-05-26.json` : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

**Verdict Sentiment :** Neutre à prudent. Silence médiatique et institutionnel total. Le repositionnement options call-biased (62.3%) est le seul signal haussier technique ; le max pain à $10.00 au-dessus du spot est le contre-signal baissier dominant.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 67.2 / 100 |
| Score Global Ajusté | **64.2 / 100** |
| Score Opportunité | **6.7 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | **4.5 / 10** |
| Recommandation agent | **ACHETER (Réduit)** |
| Timing agent | **Défavorable** |

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Opportunité | 6.7 / 10 | **~4.2 / 10** | Plafonnement Valorisation à 5/10 (Qualité 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus liquidité 0.69× (−0.3 pt) ; malus timing défavorable (−0.3 pt) ; malus données earnings Q1 manquantes (−0.5 pt) |
| Score Catalyseur | 8.0 / 10 | **7.5 / 10** | Malus options put-biased historique −0.5 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 4.5 / 10 | **4.5 / 10** | = |
| **Score Global Ajusté** | 64.2 / 100 | **~42 / 100** | Recalculé sur base 4.2/10 × 10 = 42 |
| **Recommandation analyste** | — | **SURVEILLER** | Score < 50 ; Qualité 1/6 exclut tout sizing standard ; liquidité réduite |

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — n = 0, pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1.0 (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

**Sector Rotation (`data/sector_rotation_latest.json`) :**
- Date 2026-05-26 : XLC classé **bottom 3** (momentum score 0.0 / 10).
- Malus sectoriel maintenu : −0.5 pt composite.

**Geo Risk (`data/geo_risk_latest.json`) :**
- Date 2026-05-17 — FUBO non flaggué. Score Politique non calculé.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.52 | — |
| Stop-Loss | **$8.28** | 2× ATR (−13.0%) |
| Take-Profit | **$11.38** | 3× ATR (+19.5%) |
| Ratio R/R | **1.5×** | Stable |
| Max Pain | **$10.00** | Spot sous max pain (−4.8%) — pinning baissier J+3 |
| Résistance intermédiaire | **$10.00** | Niveau psychologique + max pain — à surveiller en échéance |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — SURVEILLER (snapshot 21:00 UTC, liquidité partiellement récupérée, earnings J+7 non résolu)**

La thèse de **SURVEILLER** du snapshot 17:00 UTC est **confirmée** par le snapshot 21:00 UTC. Cinq observations :

1. **Stabilité quasi totale des métriques** — Le cours recule marginalement de $9.56 à $9.52 (−0.42% intraday), tandis que toutes les autres métriques techniques (RSI, ATR, MM50, options, max pain, put/call, call OI, scoring agent) sont **inchangées** entre 17:00 et 21:00 UTC. Cette stabilité confirme l'absence de mouvement directionnel structuré.

2. **Récupération partielle de la liquidité** — Le volume remonte de 517k à **987k actions** (+91%), passant de 0.37× à **0.69× la moyenne 20j**. Cette amélioration est notable mais le titre reste sous sa moyenne de volume. Le cours −2.36% sur ce volume n'est pas un signal de vente institutionnelle, mais confirme l'absence d'appétit acheteur. Le risque de slippage persiste.

3. **Scoring agent stable en ACHETER (Réduit)**, mais ajustement analyste maintenant **SURVEILLER (~42/100)** — inchangé vs 17:00 UTC. Le plafonnement Qualité 1/6, le malus sectoriel XLC bottom 3, la liquidité réduite (0.69×) et le timing défavorable maintiennent le titre hors de la zone d'achat institutionnelle.

4. **Pression de pinning options stable** — Le max pain $10.00 est à **+4.8%** au-dessus du spot (vs +4.4% à 17:00 UTC). En échéance J+3 (2026-05-29), la gravitation options vers $10.00 reste le scénario central si aucun catalyseur ne survient.

5. **Anomalie calendrier earnings persistante (J+7)** : `upcoming_events_latest.json` place l'earnings FUBO au **2026-05-26** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après 7 jours d'attente. Cette incohérence alimente l'incertitude fondamentale majeure.

**Arguments confirmant la prudence :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Divergence Yahoo/FMP persistante** — market cap $280.2M vs ~$3.3B (×11.7).
3. **Timing défavorable** — sous MM50 (−16.6%), RSI en survente extrême sans signe de reversal, volume réduit.
4. **Liquidité réduite** — volume 0.69×, risque de slippage sur toute taille de position.
5. **Données manquantes** — pas de résultats Q1 après 7 jours, pas de news, pas de accounting risk, pas de social sentiment.
6. **Quant report non significatif** — pas assez d'historique.
7. **Earnings Q1 non résolu** — incertitude sur le calendrier de publication et les résultats attendus.
8. **Max pain $10.00 au-dessus du spot** — pinning baissier en échéance J+3 si pas de catalyseur.
9. **Momentum agent en retrait** — 4.5/10, confirmant la faiblesse du mouvement de prix.

**Recommandation finale :** **SURVEILLER — pas de position.** Le gap +6.67% du 25/05 a été partiellement effacé par la baisse −2.36% du jour sur volume réduit. Le titre reste dans une configuration de survente extrême (RSI 21.08) avec un setup short squeeze latent (short interest 22.84% + call OI 62.3%), mais l'absence de liquidité (0.69×) et l'incertitude earnings (J+7 non résolu) rendent tout trade de très court terme extrêmement risqué. Le scoring agent ACHETER (Réduit) ne doit pas être suivi sans confirmation technique (volume > 1.5× moyenne 20j + breakout MM50) et résolution des données fondamentales (earnings Q1 + divergence Yahoo/FMP). Toute entrée eventuelle resterait un trade spéculatif avec sizing minimal et stop-loss strict à $8.28.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-05-26 (snapshot 21:00 UTC)*
*Sources : data/latest.json (fetched 2026-05-26T21:00:15Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-05-26), data/social_sentiment_latest.json (2026-05-26), data/fx_exposure_latest.json (2026-05-26), data/upcoming_events_latest.json (2026-05-26), data/events_latest.json (2026-05-26), data/validation_report.txt (2026-05-26)*
