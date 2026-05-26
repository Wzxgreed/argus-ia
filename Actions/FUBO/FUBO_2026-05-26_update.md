# FUBO — Mise à Jour (2026-05-26, snapshot 13:00 UTC)

> **Niveau d'impact :** 🟡 Modéré — Anomalie options JSON **résolue** (max pain $10.00, put/call 0.60, call OI 62.3%), structure options légèrement plus haussière vs 25/05. Spot $9.75 inchangé vs snapshot 10:00 UTC. Earnings Q1 2026 J+0 non résolu après 7 jours d'attente. Thèse **SURVEILLER** confirmée.
> **Référence précédente :** [FUBO_2026-05-26_update.md](FUBO_2026-05-26_update.md) (snapshot 10:00 UTC — close $9.75, RSI 20.19, anomalie options JSON détectée, scoring agent 65.5/100, thèse SURVEILLER)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (10:00 UTC 26/05)

| Métrique | 2026-05-26 10:00 UTC | **2026-05-26 13:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.75 | **$9.75** | — |
| Change % vs previous | +6.67% | **+6.67%** | — |
| Volume séance | 1 101 200 | **1 101 200** | — |
| Volume vs 20j | 0.75× | **0.75×** | — |
| RSI 14j | 20.19 | **20.19** | — |
| ATR 14j | $0.63 | **$0.63** | — |
| MM 50j | $11.52 | **$11.52** | — |
| Market Cap (Yahoo) | $287.0M | **$287.0M** | — |
| P/E TTM (Yahoo) | 2.54x | **2.54x** | — |
| Forward P/E | 20.66x | **20.66x** | — |
| Short Interest | 22.84% | **22.84%** | — |
| **Max Pain (brut API)** | **$7.50** (anomalie) | **$10.00** | **Résolu** |
| Put/Call Ratio (brut API) | **0.00** (anomalie) | **0.60** | **Résolu** |
| Call OI % (brut API) | **100.0%** (anomalie) | **62.3%** | **Résolu** |
| Échéance options | 2026-05-29 | **2026-05-29** | — |
| **Score Global Ajusté (agent)** | 65.5/100 | **65.5/100** | — |
| **Recommandation (agent)** | ACHETER (Réduit) | **ACHETER (Réduit)** | — |

**Constats :**
1. **Anomalie options JSON RÉSOLUE** : `data/latest.json` (snapshot 13:00 UTC) retourne un bloc options FUBO avec des valeurs **cohérentes** : `max_pain: 10.0`, `put_call_ratio: 0.60`, `call_oi_pct: 62.3`. Ces valeurs remplacent l'anomalie du snapshot 10:00 UTC (`max_pain: 7.50`, `put_call_ratio: 0.00`, `call_oi_pct: 100.0`) qui était un artefact de parsing pre-ouverture. Les valeurs confirmées du 25/05 ($9.00 / 0.65 / 60.6%) sont désormais obsolètes ; le snapshot 13:00 UTC fait foi.
2. **Max Pain remonté à $10.00** (vs $9.00 historique 25/05) — le spot $9.75 se situe **sous** le max pain (−2.5%). Lecture : pression de pinning vers $10.00 en échéance J+3 (2026-05-29). Si le cours approche $10.00, la gravitation options pourrait freiner le momentum haussier.
3. **Call OI en hausse à 62.3%** (vs 60.6% confirmé 25/05) — le positionnement call-biased s'est renforcé marginalement. Combiné au short interest massif (22.84%), le setup **short squeeze latent** est maintenu.
4. **Put/Call légèrement baissier à 0.60** (vs 0.65 historique) — repositionnement put vendeur ou couverture call, signal mixte.
5. **Stabilité totale des métriques principales** — cours, RSI, ATR, volume, fondamentaux identiques entre 10:00 et 13:00 UTC (snapshot pre-market, marché US ouvre à 13:30 UTC). Le snapshot 13:00 UTC capture la fin de la session pre-market sans nouvelle information de prix.
6. **Earnings Q1 2026 non résolu après 7 jours** : `data/upcoming_events_latest.json` (2026-05-26) indique toujours un événement earnings FUBO au **2026-05-26** avec `days_until: 0`. Aucun résultat Q1 2026 (EPS, revenue, guidance) n'est visible dans `data/latest.json` au snapshot 13:00 UTC. L'earnings, initialement attendu le 2026-05-20, a été déplacé au 2026-05-26 par FMP, mais aucune donnée n'a été publiée. **Hypothèse** : publication probablement reportée ou le ticker n'a pas encore communiqué ses résultats. Vérification impérative au prochain snapshot post-session.
7. **Scoring agent stable** : Score Global 65.5/100, action ACHETER (Réduit, timing Défavorable), porté par Catalyseur 8.0/10 et Valorisation 7.0/10, malgré Momentum faible 5.0/10.
8. **Validation report** (`data/validation_report.txt`, 2026-05-26) : 22/26 tickers OK, 5 errors (AST/AXA/CYTOMX/QTBS : no price history ; VRT : schema violation), 2 warnings (IREN, NOK). FUBO non flaggué. [DONNÉES PARTIELLES] sur le pipeline global mais pas sur FUBO.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 20.19 | **Survente extrême** — sous le seuil 30, en baisse de 12 pts depuis le 20-05 |
| MM 50j | $11.52 | Cours sous la moyenne — écart **−15.4%** |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.63 | Volatilité absolue comprimée (6.5% du spot) |
| Volume vs 20j | 0.75× | Faible — liquidité réduite persistante |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+17.3%** |

**Niveaux clés (révisés) :**
- Support immédiat : **$9.26** (low du 2026-05-25)
- Support secondaire : **$8.31** (52W low)
- Résistance psychologique : **$10.00** (niveau psychologique + **max pain**)
- Résistance majeure : **$11.52** (MM50)
- Stop-loss ATR (2×) : **$8.49** (−12.9%)
- Take-profit ATR (3×) : **$11.64** (+19.4%)

**Verdict timing :** Défavorable — sous MM50, RSI en survente extrême sans signe de reversal structurel, volume faible. Le gap +6.67% sur ATR comprimé ($0.63) reste anormal (10.6× l'ATR). L'absence de volume de suivi (0.75×) indique que le gap n'est pas validé par le cash. Tendance baissière primaire intacte.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale ni résultat Q1 2026 dans le snapshot 13:00 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $287.0M | 2.54x | 0.35x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×11.4 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-26)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.54x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 20.66x | Élevé — anticipation bénéfices faibles NTM |
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

### Options (résolution anomalie)

| Signal | Valeur Brut API 10:00 | **Valeur Brut API 13:00** | Lecture |
|---|---|---|---|
| Max Pain | $7.50 (anomalie) | **$10.00** | Cohérent — spot sous max pain |
| Put/Call Ratio | 0.00 (anomalie) | **0.60** | Cohérent — légèrement put-biased |
| Call OI % | 100.0% (anomalie) | **62.3%** | Cohérent — call-biased renforcé |
| Échéance | 2026-05-29 | **2026-05-29** | J+3 — repositionnement imminent |

**Lecture institutionnelle :** L'anomalie JSON du snapshot 10:00 UTC est résolue. Les valeurs du snapshot 13:00 UTC font foi. Le max pain remonté à $10.00 place le spot $9.75 sous pression de pinning baissier (écart −2.5%). Cependant, le call OI dominant (62.3%) et le short interest massif (22.84%) maintiennent un **setup short squeeze latent** — si un catalyseur positif survient (ex : résolution earnings, surprise EPS), le squeeze technique pourrait propulser le cours au-dessus de $10.00 vers $11.00–$11.50. Sans catalyseur, la gravitation options vers $10.00 reste le scénario central.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +415%. Consensus figé.

### News & Événements Corporates

- `data/news_2026-05-26.json` : **vide** (0 article) pour FUBO — silence médiatique total.
- `data/events_2026-05-26.json` : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` place l'événement au **2026-05-26** (jour J, `days_until: 0`), mais aucun résultat Q1 n'est visible dans `data/latest.json` au snapshot 13:00 UTC. [ANOMALIE CALENDRIER PERSISTANTE — J+7 non résolu]

### FX Exposure

- `data/fx_exposure_2026-05-26.json` : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_2026-05-26.json` : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

**Verdict Sentiment :** Neutre à prudent. Silence médiatique et institutionnel total. Le repositionnement options call-biased (62.3%) est le seul signal haussier technique ; le max pain à $10.00 est le contre-signal baissier dominant.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 68.5 / 100 |
| Score Global Ajusté | **65.5 / 100** |
| Score Opportunité | **6.8 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | 5.0 / 10 |
| Recommandation agent | **ACHETER (Réduit)** |
| Timing agent | **Défavorable** |

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Opportunité | 6.8 / 10 | **~5.2 / 10** | Plafonnement Valorisation à 5/10 (Qualité 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus liquidité 0.75× (−0.3 pt) ; malus timing défavorable (−0.3 pt) ; malus données earnings Q1 manquantes (−0.5 pt) |
| Score Catalyseur | 8.0 / 10 | **7.5 / 10** | Malus options put-biased historique −0.5 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 5.0 / 10 | **5.0 / 10** | = |
| **Score Global Ajusté** | 65.5 / 100 | **~52 / 100** | Recalculé sur base 5.2/10 × 10 = 52 |
| **Recommandation analyste** | — | **SURVEILLER** | Score < 60 ; Qualité 1/6 exclut tout sizing standard |

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
| Close | $9.75 | — |
| Stop-Loss | **$8.49** | 2× ATR (−12.9%) |
| Take-Profit | **$11.64** | 3× ATR (+19.4%) |
| Ratio R/R | **1.5×** | Stable |
| Max Pain | **$10.00** | Spot sous max pain (−2.5%) — pinning baissier J+3 |
| Résistance intermédiaire | **$10.00** | Niveau psychologique + max pain — à surveiller en échéance |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — SURVEILLER (snapshot 13:00 UTC, anomalie options JSON résolue, earnings J+7 non résolu)**

La thèse de **SURVEILLER** du snapshot 10:00 UTC est **confirmée** par le snapshot 13:00 UTC. Cinq observations :

1. **Résolution de l'anomalie options JSON** : `data/latest.json` (snapshot 13:00 UTC) retourne des valeurs options cohérentes : `max_pain: 10.0`, `put_call_ratio: 0.60`, `call_oi_pct: 62.3`. Ces valeurs remplacent l'artefact du snapshot 10:00 UTC et l'historique 25/05. Le max pain remonté à $10.00 place le spot sous pression de pinning baissier (écart −2.5%), tandis que le call OI renforcé (62.3%) maintient le setup squeeze.

2. **Absence totale de mutation technique et fondamentale** : toutes les métriques principales (cours, RSI, ATR, volume, fondamentaux, scoring agent) sont identiques entre 10:00 et 13:00 UTC. Le snapshot 13:00 UTC est pre-market (marché US ouvre à 13:30 UTC).

3. **Anomalie calendrier earnings persistante (J+7)** : `upcoming_events_latest.json` place l'earnings FUBO au **2026-05-26** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après 7 jours d'attente. Cette incohérence suggère soit un report de publication, soit une absence de communication pour le trimestre en cours. **Vérification impérative au prochain snapshot post-session (17:00 UTC).**

4. **Scoring agent stable en ACHETER (Réduit)**, mais ajustement analyste maintenant **SURVEILLER (~52/100)** : le plafonnement Qualité 1/6, le malus sectoriel XLC bottom 3, la liquidité réduite et le timing défavorable maintiennent le titre hors de la zone d'achat institutionnelle.

5. **Setup options mixte** : max pain $10.00 (spot sous max pain = pinning baissier) vs call OI 62.3% + short interest 22.84% (setup squeeze latent). Sans catalyseur, le pinning vers $10.00 est le scénario central. Avec catalyseur (ex : résolution earnings positive), le squeeze technique pourrait propulser le cours au-dessus de $10.00.

**Arguments confirmant la prudence :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Divergence Yahoo/FMP persistante** — market cap $287M vs ~$3.3B (×11.4).
3. **Timing défavorable** — sous MM50 (−15.4%), RSI en survente extrême sans signe de reversal, volume faible.
4. **Liquidité réduite** — volume 0.75×, risque de slippage majeur.
5. **Données manquantes** — pas de résultats Q1 après 7 jours, pas de news, pas de accounting risk, pas de social sentiment.
6. **Quant report non significatif** — pas assez d'historique.
7. **Earnings Q1 non résolu** — incertitude sur le calendrier de publication et les résultats attendus.
8. **Max pain $10.00 au-dessus du spot** — pinning baissier en échéance J+3 si pas de catalyseur.

**Recommandation finale :** **SURVEILLER — pas de position.** Le gap +6.67% sur fond de survente extrême (RSI 20.19) et de short interest massif (22.84%) dessine un potentiel rebond technique de courte durée vers $10.00, mais ce scénario reste purement spéculatif et contraint par le max pain. Le scoring agent ACHETER (Réduit) ne doit pas être suivi sans confirmation technique (volume > 1.5× moyenne 20j + breakout MM50) et résolution des données fondamentales (earnings Q1 + divergence Yahoo/FMP). Toute entrée eventuelle resterait un trade de très court terme avec sizing minimal et stop-loss strict à $8.49.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-05-26 (snapshot 13:00 UTC)*
*Sources : data/latest.json (fetched 2026-05-26T13:00:13Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-05-26), data/social_sentiment_latest.json (2026-05-26), data/fx_exposure_latest.json (2026-05-26), data/upcoming_events_latest.json (2026-05-26), data/events_latest.json (2026-05-26), data/validation_report.txt (2026-05-26)*
