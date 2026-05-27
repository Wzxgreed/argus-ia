# FUBO — Mise à Jour (2026-05-27, snapshot 13:00 UTC)

> **Niveau d'impact :** 🟢 Faible — Snapshot 13:00 UTC confirme la **stabilité totale** vs snapshot 10:00 UTC (close $9.52 inchangé, RSI 21.08 inchangé, volume 1,004,300 inchangé). **Anomalie options JSON RÉSOLUE** : max pain $10.00 cohérent, put/call 0.51, call OI 66.3% (vs valeurs confirmées 10:00 UTC : 0.60 / 62.3%). Biais haussier options légèrement renforcé. Scoring agent stable à 64.2/100 (ACHETER Réduit), ajustement analyste **SURVEILLER (~42/100)**. Earnings Q1 2026 J=0 non résolu après 8 jours.
> **Référence précédente :** [FUBO_2026-05-27_update.md](FUBO_2026-05-27_update.md) (snapshot 10:00 UTC — close $9.52, RSI 21.08, volume 1,004,300 / 0.70×, anomalie options JSON traitée, scoring agent 64.2/100, thèse SURVEILLER)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-27 10:00 UTC)

| Métrique | 2026-05-27 10:00 UTC | **2026-05-27 13:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.52 | **$9.52** | **0.00%** |
| Change % vs previous | −2.36% | **−2.36%** | — |
| Volume séance | 1 004 300 | **1 004 300** | **0.00%** |
| Volume vs 20j | 0.70× | **0.70×** | **Stable** |
| RSI 14j | 21.08 | **21.08** | — |
| ATR 14j | $0.62 | **$0.62** | — |
| MM 50j | $11.42 | **$11.42** | — |
| Market Cap (Yahoo) | $280.2M | **$280.2M** | — |
| P/E TTM (Yahoo) | 2.48x | **2.48x** | — |
| Forward P/E | 20.17x | **20.17x** | — |
| Short Interest | 22.84% | **22.84%** | — |
| **Max Pain (API)** | $7.50 (anomalie) → confirmé **$10.00** | **$10.00** | **Anomalie résolue** |
| Put/Call Ratio (API) | 0.00 (anomalie) → confirmé **0.60** | **0.51** | **−0.09 (haussier)** |
| Call OI % (API) | 100.0% (anomalie) → confirmé **62.3%** | **66.3%** | **+4.0 pp (haussier)** |
| Échéance options | 2026-05-29 | **2026-05-29** | J+2 |
| **Score Global (agent)** | 67.2/100 | **67.2/100** | — |
| **Score Global Ajusté (agent)** | 64.2/100 | **64.2/100** | — |
| **Score Opportunité (agent)** | 6.7/10 | **6.7/10** | — |
| **Score Momentum (agent)** | 4.5/10 | **4.5/10** | — |
| **Recommandation (agent)** | ACHETER (Réduit) | **ACHETER (Réduit)** | — |

**Constats :**
1. **Stabilité absolue du cours et des métriques techniques** — Le close reste à **$9.52** (0.00% vs snapshot 10:00 UTC). Toutes les métriques techniques principales (RSI, ATR, MM50, market cap, P/E, short interest) sont **strictement inchangées**. Il s'agit du 14e snapshot consécutif avec un close quasi-identique (consolidation autour de $9.20–$9.75 depuis le 20/05).
2. **Anomalie options JSON RÉSOLUE** — Le snapshot 13:00 UTC retourne un max pain **$10.00** (cohérent avec la valeur confirmée du 10:00 UTC), un put/call **0.51** (vs 0.60 confirmé précédemment), et un call OI **66.3%** (vs 62.3% confirmé). L'anomalie JSON identifiée sur SOFI et SQ à 10:00 UTC est donc corrigée. Le put/call en légère baisse et le call OI en hausse de 4.0 pp signalent un **biais haussier options légèrement renforcé**.
3. **Liquidité stablement réduite** — Volume 1,004,300 (0.70× moyenne 20j), strictement inchangé vs 10:00 UTC. Le titre reste sous sa moyenne de volume depuis 8 jours.
4. **RSI en survente extrême (21.08)** — inchangé en zone critique sous le seuil 30. Aucun signe de reversal technique.
5. **Scoring agent stable** — 64.2/100 (ACHETER Réduit), Score Opportunité 6.7/10, Score Momentum 4.5/10. Aucun mouvement des algorithmes de scoring entre 10:00 et 13:00 UTC.
6. **Earnings Q1 2026 non résolu après 8 jours** : `data/upcoming_events_latest.json` (2026-05-27) place l'earnings au **2026-05-27** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible dans `data/latest.json` au snapshot 13:00 UTC. [ANOMALIE CALENDRIER PERSISTANTE — J+8 NON RÉSOLU]
7. **Validation report** (`data/validation_report.txt`, 2026-05-27) : 23/26 tickers OK, 4 errors (VRT schema, AST/AXA/QTBS fetch failed), 2 warnings (IREN, NOK). FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 21.08 | **Survente extrême** — sous le seuil 30, stable en zone critique |
| MM 50j | $11.42 | Cours sous la moyenne — écart **−16.6%** |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.62 | Volatilité absolue compressée (6.5% du spot) |
| Volume vs 20j | 0.70× | Réduit — liquidité inchangée, sous moyenne 20j |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+14.6%** |

**Niveaux clés :**
- Support immédiat : **$9.50** (low du jour)
- Support secondaire : **$8.31** (52W low)
- Résistance : **$10.00** (niveau psychologique + **max pain**)
- Résistance majeure : **$11.42** (MM50)
- Stop-loss ATR (2×) : **$8.28** (−13.0%)
- Take-profit ATR (3×) : **$11.38** (+19.5%)

**Verdict timing :** Défavorable — sous MM50, RSI en survente extrême sans signe de reversal structurel, volume stablement réduit (0.70×). Le cours consolidé autour de $9.50–$9.75 depuis 8 jours n'est pas un signal directionnel fiable, mais confirme l'absence d'achat institutionnel. La tendance baissière primaire reste intacte.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale dans le snapshot 13:00 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $280.2M | 2.48x | 0.35x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×11.7 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-27)

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

| Signal | Valeur 10:00 UTC | Valeur 13:00 UTC | Lecture |
|---|---|---|---|
| Max Pain | $10.00 (confirmé) | **$10.00** | Cohérent — anomalie résolue |
| Put/Call Ratio | 0.60 (confirmé) | **0.51** | **Biais haussier légèrement renforcé** |
| Call OI % | 62.3% (confirmé) | **66.3%** | **+4.0 pp — domination call accrue** |
| Échéance options | 2026-05-29 | **2026-05-29** | J+2 — pinning vers $10.00 si pas de catalyseur |

**Lecture institutionnelle :** Le spot $9.52 se situe à **−4.8%** sous le max pain $10.00. La pression de pinning baissier vers $10.00 se maintient en échéance J+2 (2026-05-29). Le call OI dominant (66.3%) et le short interest massif (22.84%) maintiennent un **setup short squeeze latent** — si un catalyseur positif survient (ex : résolution earnings, surprise EPS), le squeeze technique pourrait propulser le cours au-dessus de $10.00 vers $11.00–$11.50. Sans catalyseur, la gravitation options vers $10.00 reste le scénario central. La résolution de l'anomalie JSON et le renforcement du biais call (66.3% vs 62.3%) sont des signaux marginalement positifs, mais sans impact sur la thèse globale.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +428%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-05-27) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` place l'événement au **2026-05-27** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après 8 jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE — J+8 NON RÉSOLU]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-05-27) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-05-27) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

**Verdict Sentiment :** Neutre à prudent. Silence médiatique et institutionnel total. Le repositionnement options call-biased (66.3%) est le seul signal haussier technique ; le max pain à $10.00 au-dessus du spot est le contre-signal baissier dominant.

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
| Score Opportunité | 6.7 / 10 | **~4.2 / 10** | Plafonnement Valorisation à 5/10 (Qualité 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus liquidité 0.70× (−0.3 pt) ; malus timing défavorable (−0.3 pt) ; malus données earnings Q1 manquantes (−0.5 pt) |
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
- Date 2026-05-27 : XLC classé **bottom 3** (momentum score 0.0 / 10).
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
| Max Pain | **$10.00** | Spot sous max pain (−4.8%) — pinning baissier J+2 |
| Résistance intermédiaire | **$10.00** | Niveau psychologique + max pain — à surveiller en échéance |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — SURVEILLER (snapshot 13:00 UTC, stabilité totale, anomalie options JSON résolue, biais call légèrement renforcé, earnings J+8 non résolu)**

La thèse de **SURVEILLER** du snapshot 10:00 UTC du 27/05 est **confirmée** par le snapshot 13:00 UTC. Six observations :

1. **Stabilité absolue des métriques de prix et technique** — Le close reste à **$9.52** (0.00% vs précédent). Toutes les métriques techniques (RSI, ATR, MM50, options confirmées, scoring agent) sont **strictement inchangées**. Il s'agit du 14e snapshot consécutif avec des données quasi-identiques, signalant une absence totale de volatilité directionnelle.

2. **Anomalie options JSON RÉSOLUE** — Le snapshot 13:00 UTC retourne des valeurs cohérentes : max pain **$10.00**, put/call **0.51**, call OI **66.3%**. L'anomalie observée à 10:00 UTC (max pain $7.50, put/call 0.00, call OI 100.0%) est un artefact corrigé. Le biais call est légèrement renforcé (+4.0 pp) et le put/call en légère baisse, mais cela ne modifie pas la lecture institutionnelle : pinning baissier vers $10.00 en échéance J+2.

3. **Liquidité stablement réduite** — Volume 1,004,300 (0.70× moyenne 20j), strictement inchangé vs 10:00 UTC. Aucune amélioration. Le risque de slippage persiste.

4. **Scoring agent stable en ACHETER (Réduit)**, mais ajustement analyste maintenant **SURVEILLER (~42/100)** — inchangé vs précédent. Le plafonnement Qualité 1/6, le malus sectoriel XLC bottom 3, la liquidité réduite (0.70×) et le timing défavorable maintiennent le titre hors de la zone d'achat institutionnelle.

5. **Anomalie calendrier earnings persistante (J+8)** : `upcoming_events_latest.json` place l'earnings FUBO au **2026-05-27** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après 8 jours d'attente. Cette incohérence alimente l'incertitude fondamentale majeure.

6. **Setup short squeeze latent inchangé** — short interest 22.84% + call OI 66.3% + spot sous max pain = configuration explosive si catalyseur positif. Mais sans volume (> 1.5× moyenne 20j) et sans confirmation de résultats, ce setup reste théorique.

**Arguments confirmant la prudence :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Divergence Yahoo/FMP persistante** — market cap $280.2M vs ~$3.3B (×11.7).
3. **Timing défavorable** — sous MM50 (−16.6%), RSI en survente extrême sans signe de reversal, volume réduit.
4. **Liquidité réduite** — volume 0.70×, risque de slippage sur toute taille de position.
5. **Données manquantes** — pas de résultats Q1 après 8 jours, pas de news, pas de accounting risk, pas de social sentiment.
6. **Quant report non significatif** — pas assez d'historique.
7. **Earnings Q1 non résolu** — incertitude sur le calendrier de publication et les résultats attendus.
8. **Max pain $10.00 au-dessus du spot** — pinning baissier en échéance J+2 si pas de catalyseur.
9. **Momentum agent en retrait** — 4.5/10, confirmant la faiblesse du mouvement de prix.

**Recommandation finale :** **SURVEILLER — pas de position.** Le titre reste dans une configuration de survente extrême (RSI 21.08) avec un setup short squeeze latent (short interest 22.84% + call OI 66.3%), mais l'absence de liquidité (0.70×) et l'incertitude earnings (J+8 non résolu) rendent tout trade de très court terme extrêmement risqué. Le scoring agent ACHETER (Réduit) ne doit pas être suivi sans confirmation technique (volume > 1.5× moyenne 20j + breakout MM50) et résolution des données fondamentales (earnings Q1 + divergence Yahoo/FMP). Toute entrée eventuelle resterait un trade spéculatif avec sizing minimal et stop-loss strict à $8.28.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-05-27 (snapshot 13:00 UTC)*
*Sources : data/latest.json (fetched 2026-05-27T13:00:02Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-05-27), data/social_sentiment_latest.json (2026-05-27), data/fx_exposure_latest.json (2026-05-27), data/upcoming_events_latest.json (2026-05-27), data/events_latest.json (2026-05-27), data/validation_report.txt (2026-05-27)*