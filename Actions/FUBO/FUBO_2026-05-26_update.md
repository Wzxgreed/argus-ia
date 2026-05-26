# FUBO — Mise a Jour (2026-05-26, snapshot 10:00 UTC)

> **Niveau d'impact :** 🟢 Faible — Snapshot 10:00 UTC post-Memorial Day **stable** vs snapshot 21:00 UTC 25/05. Close $9.75 inchangé, RSI 20.19 inchangé, ATR $0.63 inchangé, scoring agent stable a 65.5/100 (ACHETER Reduit). **Anomalie options JSON detectee** (max_pain 7.50 aberrant, put/call 0.00, call OI 100.0%) — valeurs confirmées 25/05 maintenues. Earnings Q1 2026 J=0 non resolu apres 6 jours d'attente.
> **Reference precedente :** [FUBO_2026-05-25_update.md](FUBO_2026-05-25_update.md) (snapshot 21:00 UTC — close $9.75, RSI 20.19, max pain $9.00, put/call 0.65, call OI 60.6%, scoring agent 65.5/100, these SURVEILLER)

---

## 1. Resume des Changements depuis l'Analyse Precedente (21:00 UTC 25/05)

| Metrique | 2026-05-25 21:00 UTC | **2026-05-26 10:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.75 | **$9.75** | — |
| Change % vs previous | +6.67% | **+6.67%** | — |
| Volume seance | 1 101 200 | **1 101 200** | — |
| Volume vs 20j | 0.75× | **0.75×** | — |
| RSI 14j | 20.19 | **20.19** | — |
| ATR 14j | $0.63 | **$0.63** | — |
| MM 50j | $11.52 | **$11.52** | — |
| Market Cap (Yahoo) | $287.0M | **$287.0M** | — |
| P/E TTM (Yahoo) | 2.54x | **2.54x** | — |
| Forward P/E | 20.66x | **20.66x** | — |
| Short Interest | 22.84% | **22.84%** | — |
| **Max Pain (brut API)** | **$9.00** | **$7.50** | −16.7% |
| Put/Call Ratio (brut API) | 0.65 | **0.00** | −0.65 |
| Call OI % (brut API) | 60.6% | **100.0%** | +39.4 pp |
| Echeance options | 2026-05-29 | **2026-05-29** | — |
| **Score Global Ajuste (agent)** | 65.5/100 | **65.5/100** | — |
| **Recommandation (agent)** | ACHETER (Reduit) | **ACHETER (Reduit)** | — |

**Constats :**
1. **Stabilite totale snapshot 21:00 25/05 → 10:00 26/05** — 13e snapshot consecutif identique pour les metriques principales (cours, RSI, ATR, volume, fondamentaux). Le snapshot 10:00 UTC est capture peu apres la reouverture post-Memorial Day (6h00 ET) ; les donnees de session sont probablement incompletes ou stale.
2. **Anomalie options JSON detectee et preservee** : `data/latest.json` (2026-05-26) retourne un bloc options FUBO avec `max_pain: 7.50`, `put_call_ratio: 0.00`, `call_oi_pct: 100.0`. Ces valeurs sont incoherentes avec l'historique (max pain $9.00–$10.00, put/call 0.59–0.90, call OI 60–63%) et probablement liees a un artefact de parsing JSON ou a l'absence de donnees options pre-ouverture. **Les valeurs confirmées du 25/05 ($9.00 / 0.65 / 60.6%) sont conservees pour l'analyse.**
3. **Earnings Q1 2026 non resolu apres 6 jours** : `data/upcoming_events_latest.json` (date 2026-05-26) indique toujours un evenement earnings FUBO au **2026-05-26** avec `days_until: 0`. Aucun resultat Q1 2026 (EPS, revenue, guidance) n'est visible dans `data/latest.json` ni dans les donnees FMP enrichies au snapshot 10:00 UTC. L'earnings, initialement attendu le 2026-05-20, a ete deplace au 2026-05-25 puis au 2026-05-26 par FMP, mais aucune donnee n'a ete publiee. **Hypothese** : la publication est probablement postposee ou le ticker n'a pas encore publie ses resultats pour le trimestre. Verification imperative au prochain snapshot.
4. **RSI en survente extreme (20.19)** — inchangé depuis le snapshot 13:00 UTC 25/05. Le titre reste techniquement survendu.
5. **ATR comprime a $0.63** (6.5% du spot) — volatilite absolue faible. Le gap +6.67% represente toujours **10.6× l'ATR**, anomalie de volatilite relative persistante depuis le 2026-05-17.
6. **Scoring agent stable** : Score Global 65.5/100, action ACHETER (Reduit, timing Defavorable), porte par Catalyseur 8.0/10 et Valorisation 7.0/10, malgre Momentum faible 5.0/10.
7. **Validation report** (`data/validation_report.txt`, 2026-05-26) : 22/26 tickers OK, 5 errors (AST/AXA/CYTOMX/QTBS : no price history ; VRT : schema violation), 2 warnings (IREN, NOK). FUBO non flagge. [DONNEES PARTIELLES] sur le pipeline global mais pas sur FUBO.

---

## 2. Mise a Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 20.19 | **Survente extreme** — sous le seuil 30, en baisse de 12 pts depuis le 20-05 |
| MM 50j | $11.52 | Cours sous la moyenne — ecart **−15.4%** |
| MM 200j | N/A | [DONNEES MANQUANTES] |
| ATR 14j | $0.63 | Volatilite absolue comprimee (6.5% du spot) |
| Volume vs 20j | 0.75× | Faible — liquidite reduite persistante |
| Beta | 2.508 | Volatilite systematique extreme |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+17.3%** |

**Niveaux cles :**
- Support immediat : **$9.26** (low du 2026-05-25)
- Support secondaire : **$8.31** (52W low)
- Resistance : **$10.00** (niveau psychologique / ancien max pain)
- Resistance majeure : **$11.52** (MM50)
- Stop-loss ATR (2×) : **$8.49** (−12.9%)
- Take-profit ATR (3×) : **$11.64** (+19.4%)

**Verdict timing :** Defavorable — sous MM50, RSI en survente extreme sans signe de reversal structurel, volume faible. Le gap +6.67% sur ATR comprime ($0.63) reste anomal (10.6× l'ATR). L'absence de volume de suivi (0.75×) et le put/call a 0.65 (valeur confirmée) indiquent que le marche options ne valide pas le gap. Tendance baissiere primaire intacte.

---

## 3. Mise a Jour Fondamentale

Aucune nouvelle donnee fondamentale ni resultat Q1 2026 dans le snapshot 10:00 UTC. La divergence Yahoo/FMP persiste integralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $287.0M | 2.54x | 0.35x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Ecart :** ×11.4 sur la capitalisation. Ce hiatus empeche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-26)

| Metrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.54x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 20.66x | Eleve — anticipation benefices faibles NTM |
| EV/Revenue | 0.43x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.35x | < 1x — patrimoine net suspect ou negatif |
| P/B (FMP) | 3.19x | Ecart ×9.1 avec Yahoo |
| Beta | 2.508 | Extreme |
| Short Interest | 22.84% | Tres eleve — inchangé |
| Gross Margin (FMP) | 11.1% | Tres faible |
| Operating Margin (FMP) | −2.6% | Perte operationnelle |
| Current Ratio (FMP) | 0.84 | Illiquidite structurelle |
| Debt/Equity (FMP) | 2.43 | Levier eleve |
| Tangible Asset Value (FMP) | −$398.9M | Patrimoine net negatif |
| Net Debt/EBITDA (FMP) | 1.01x | Couverture faible |
| ROIC (FMP) | −2.1% | Destruction de valeur |
| ROE (FMP) | 56.5% | Eleve — structure de capital tres levee |

**Filtre Qualite :** Score **1/6** confirmé. Hors perimetre Quality Compounder. Score Valorisation plafonne a **5/10** (regle absolue Argus-IA).

**Donnees Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — scan comptable non disponible pour cette session.

---

## 4. Mise a Jour Sentiment / Options / News

### Options

| Signal | Valeur Brut API | Valeur Confirmée | Lecture |
|---|---|---|---|
| Max Pain | $7.50 | **$9.00** | Valeur API aberrante — conservee $9.00 (historique 25/05) |
| Put/Call Ratio | 0.00 | **0.65** | Valeur API aberrante — conservee 0.65 (historique 25/05) |
| Call OI % | 100.0% | **60.6%** | Valeur API aberrante — conservee 60.6% (historique 25/05) |
| Echeance | 2026-05-29 | **2026-05-29** | J+3 — repositionnement possible |

**Lecture institutionnelle :** Setup short squeeze latent (short interest 22.84% + call OI dominant) persiste, mais sans fondement qualitatif. Le marche options n'a pas amplifie son positionnement haussier. L'anomalie JSON du snapshot 10:00 UTC (put/call 0.00, call OI 100%) est ignoree en l'absence de confirmation.

### Consensus Analystes (FMP)

| Metrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise a jour recente | 0 (dernier mois) |

**Lecture :** Ecart PT / spot de +415%. Consensus fige.

### News & Evenements Corporates

- `data/news_2026-05-26.json` : **vide** (0 article) pour FUBO — silence mediatique total.
- `data/events_2026-05-26.json` : **vide** (0 evenement) — aucun M&A, buyback, guidance change ou activism detecte.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` place l'evenement au **2026-05-26** (jour J, `days_until: 0`), mais aucun resultat n'est visible dans `data/latest.json` au snapshot 10:00 UTC. [ANOMALIE CALENDRIER PERSISTANTE — J+6 non resolu]

### FX Exposure

- `data/fx_exposure_2026-05-26.json` : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_2026-05-26.json` : 0 mentions Reddit, sentiment 0.0/10, pas de pump detecte. Silence retail total.

**Verdict Sentiment :** Neutre a prudent. Silence mediatique et institutionnel total. Le repositionnement options legerement defensif persiste (put/call 0.65 confirmé).

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 68.5 / 100 |
| Score Global Ajuste | **65.5 / 100** |
| Score Opportunite | **6.8 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | 5.0 / 10 |
| Recommandation agent | **ACHETER (Reduit)** |
| Timing agent | **Defavorable** |

### Scoring ajuste analyste (regles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustee | Regle appliquee |
|---|---|---|---|
| Score Opportunite | 6.8 / 10 | **~5.2 / 10** | Plafonnement Valorisation a 5/10 (Qualite 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus liquidite 0.75× (−0.3 pt) ; malus timing defavorable (−0.3 pt) ; malus donnees manquantes earnings Q1 (−0.5 pt) |
| Score Catalyseur | 8.0 / 10 | **7.5 / 10** | Malus options put-biased historique −0.5 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualite ≤ 3/6 |
| Score Momentum | 5.0 / 10 | **5.0 / 10** | = |
| **Score Global Ajuste** | 65.5 / 100 | **~52 / 100** | Recalculé sur base 5.2/10 × 10 = 52 |
| **Recommandation analyste** | — | **SURVEILLER** | Score < 60 ; Qualite 1/6 exclut tout sizing standard |

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — n = 0, pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1.0 (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

**Sector Rotation (`data/sector_rotation_latest.json`) :**
- Date 2026-05-26 : XLC classé **bottom 3** (momentum score 0.0 / 10).
- Malus sectoriel maintenu : −0.5 pt composite.

**Geo Risk (`data/geo_risk_latest.json`) :**
- Date 2026-05-17 — FUBO non flagge. Score Politique non calcule.

---

## 6. Revision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.75 | — |
| Stop-Loss | **$8.49** | 2× ATR (−12.9%) |
| Take-Profit | **$11.64** | 3× ATR (+19.4%) |
| Ratio R/R | **1.5×** | Stable |
| Max Pain (confirmé) | $9.00 | Aligné — pinning theorique reduit |

**Condition de revision post-earnings (si resultats disponibles) :**
- Beat + guidance raise → reviser TP a $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL a $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — These Confirmee, Modifiee ou Invalidee ?

### **Verdict : THESE CONFIRMEE — SURVEILLER (snapshot 10:00 UTC stable vs 21:00 UTC 25/05, anomalie options JSON preservee, earnings J+6 non resolu)**

La these de **SURVEILLER** du snapshot 21:00 UTC 25/05 est **confirmee** par le snapshot 10:00 UTC 26/05. Quatre observations :

1. **Absence totale de mutation technique et fondamentale** : toutes les metriques principales (cours, RSI, ATR, volume, options confirmées, scoring agent) sont identiques entre 21:00 UTC 25/05 et 10:00 UTC 26/05. Le snapshot post-Memorial Day a 10:00 UTC (6h00 ET) est precoce ; les donnees de session sont potentiellement incompletes.

2. **Anomalie options JSON detectee et traitee** : `data/latest.json` retourne `max_pain: 7.50`, `put_call_ratio: 0.00`, `call_oi_pct: 100.0` pour FUBO — valeurs incoherentes avec l'historique et probablement liees a un artefact de parsing pre-ouverture. **Les valeurs confirmées du 25/05 ($9.00 / 0.65 / 60.6%) sont conservees.**

3. **Anomalie calendrier earnings persistante (J+6)** : `upcoming_events_latest.json` place l'earnings FUBO au **2026-05-26** (jour J, `days_until: 0`) depuis le snapshot du 25 mai. Aucun resultat Q1 n'est visible apres 6 jours d'attente (initialement attendu le 2026-05-20). Cette incoherence suggere soit un report de publication, soit une absence de resultats pour le trimestre en cours. **Verification imperative au prochain snapshot.**

4. **Scoring agent stable en ACHETER (Reduit)**, mais ajustement analyste maintenant **SURVEILLER (~52/100)** : le plafonnement Qualite 1/6, le malus sectoriel XLC bottom 3, la liquidite reduite et le timing defavorable maintiennent le titre hors de la zone d'achat institutionnelle.

**Arguments confirmant la prudence :**
1. **Qualite degradee 1/6** — patrimoine net negatif, FCF negatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Divergence Yahoo/FMP persistante** — market cap $287M vs ~$3.3B (×11.4).
3. **Timing defavorable** — sous MM50 (−15.4%), RSI en survente extreme sans signe de reversal, volume faible.
4. **Liquidite reduite** — volume 0.75×, risque de slippage majeur.
5. **Donnees manquantes** — pas de resultats Q1 apres 6 jours, pas de news, pas de accounting risk, pas de social sentiment.
6. **Quant report non significatif** — pas assez d'historique.
7. **Earnings Q1 non resolu** — incertitude sur le calendrier de publication et les resultats attendus.

**Recommandation finale :** **SURVEILLER — pas de position.** Le gap +6.67% sur fond de survente extreme (RSI 20.19) et de short interest massif (22.84%) dessine un potentiel rebond technique de courte duree vers $10.00–$10.50, mais ce scenario reste purement speculatif. Le scoring agent ACHETER (Reduit) ne doit pas etre suivi sans confirmation technique (volume > 1.5× moyenne 20j + breakout MM50) et resolution des donnees fondamentales (earnings Q1 + divergence Yahoo/FMP). Toute entree eventuelle resterait un trade de tres court terme avec sizing minimal et stop-loss strict a $8.49.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-05-26 (snapshot 10:00 UTC)*
*Sources : data/latest.json (fetched 2026-05-26T10:00:13Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-05-26), data/social_sentiment_latest.json (2026-05-26), data/fx_exposure_latest.json (2026-05-26), data/upcoming_events_latest.json (2026-05-26), data/events_latest.json (2026-05-26), data/validation_report.txt (2026-05-26)*
