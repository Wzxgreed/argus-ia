# NOK — Mise a Jour Quotidienne (2026-05-26, Snapshot 21:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-26 | Donnees source : `data/latest.json` (snapshot 2026-05-26T21:00:09 UTC)

---

## 1. Resume des changements depuis l'analyse precedente (2026-05-26 17:00 UTC)

| Indicateur | Snapshot 17:00 UTC | Snapshot 21:00 UTC | Variation | Signal |
|-----------|-------------------|-------------------|-----------|--------|
| Cours close | $16.52 | **$16.46** | **-0.36%** | Consolidation legere post-high |
| Change % vs previous close | +6.79% | **+6.40%** | -0.39 pp | Deuxieme gap confirme mais legerement attenue |
| RSI 14j | 67.38 | **67.16** | -0.22 | Stable — proche surachat (>70) |
| ATR 14j | $1.00 | **$1.00** | $0.00 | Inchange |
| Volume relatif | 1.17x | **1.48x** | **+0.31x** | Volume de cloture massif |
| 52-week high | $16.625 | **$16.625** | — | Inchange — close sous le high |
| P/E (TTM Yahoo) | 103.25 | **102.88** | -0.37 | Legere contraction multiple |
| Forward P/E | 33.87 | **33.75** | -0.12 | Inchange |
| P/B | 3.76 | **3.74** | -0.02 | Inchange |
| Premium vs consensus $9.26 | +78.4% | **+77.8%** | -0.6 pp | Divergence prix/valeur legerement attenue |
| Consensus analystes (FMP) | $9.26 (6) | **$9.26 (6)** | Inchange | Stable — silence total malgre +15.6% en 2j |
| Put/Call ratio | 0.51 | **0.51** | 0.00 | Inchange |
| Max pain options | $15.00 | **$15.00** | $0.00 | Inchange — aimant gamma a 3 jours |
| Call OI | 66.1% | **66.1%** | 0.0 pp | Inchange |

**Changements significatifs detectes :**
- **Volume de cloture massif** : 178.7M actions echangees (1.48x moyenne 20j), soit +28.6% vs le snapshot 17:00 UTC (138.9M). Ce volume tardif suggere soit une accumulation institutionnelle en fin de seance, soit une distribution vers des acheteurs retail. Sans catalyseur identifiable, l'interpretation reste ambigue.
- **Consolidation du cours** : le close $16.46 est legerement sous le high intraday $16.625 et le snapshot 17:00 UTC ($16.52). Le double gap haussier (+9.1% hier, +6.4% aujourd'hui) reste intact mais le titre ne parvient pas a clore sur ses sommets.
- **Aucun catalyseur fondamental** identifie dans `data/events_latest.json` (vide pour NOK) ni dans `data/upcoming_events_latest.json` (hors earnings programme au 2026-07-23).

---

## 2. Mise a Jour Technique

| Metrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $16.46 | Yahoo Finance | +6.40% vs previous close ($15.47) |
| Open | $15.99 | Yahoo Finance | Gap haussier d'ouverture confirme |
| High intraday | $16.625 | Yahoo Finance | **Nouveau 52-week high** — non franchi en cloture |
| Low intraday | $15.66 | Yahoo Finance | Support intraday immediat |
| Volume | 178,662,437 | Yahoo Finance | 1.48x moyenne 20j (120,745,546) — volume de cloture massif |
| RSI 14j | 67.16 | Calcul agent | Zone neutre haute, proche surachat (>70) |
| ATR 14j | $1.00 | Calcul agent | 6.08% du cours — volatilite en expansion |
| MM 50j | $10.96 | Calcul agent | Cours +50.4% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilite au marche — le mouvement est idiosyncratique |

**Niveaux cles (revises) :**
- **Support immediat :** $15.66 (low du jour) / $15.00 (max pain options)
- **Resistance :** $16.625 (52-week high, non valide en cloture)
- **Stop-loss ATR (2x) :** $14.46 ($16.46 - $2.00)
- **Take-profit ATR (3x) :** $19.46 ($16.46 + $3.00)
- **Ratio R/R :** 1.5

**Mise a jour options — impact technique :**
| Niveau | Valeur 17:00 UTC | Valeur 21:00 UTC | Interpretation |
|--------|-------------|-------------------|----------------|
| Max pain | $15.00 | **$15.00** | Inchange — aimant gamma a 3 jours |
| Put/Call ratio | 0.51 | **0.51** | Stable — dominance calls moderee |
| Call OI % | 66.1% | **66.1%** | Stable — dominance calls maintenue |
| Cours vs max pain | +10.1% | **+9.7%** | Le cours reste significativement au-dessus du pin |
| Expiration | 2026-05-29 | **2026-05-29** | **3 jours** — risque de pin au max pain $15.00 |

**Verdict timing :** Favorable sur le momentum pur, mais **defavorable sur la durabilite**. Le volume de cloture massif (1.48x) est le nouvel element cle : il peut indiquer un interet institutionnel tardif ou une distribution retail. Historiquement, un tel volume sans news sur un gap de +6.4% se resout par consolidation dans les 2-3 seances suivantes. Le RSI a 67.16 approche le surachat sans catalyseur.

**Score Momentum :** 7.0/10 — inchange dans `recommandations_latest.json` (double gap, new 52w high, volume massif, options bullish).

---

## 3. Mise a Jour Fondamentale

| Metrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $91.89 B | Yahoo Finance |
| Market Cap (FMP FY2025) | $29.82 B | FMP Stable API |
| P/E (TTM Yahoo) | 102.88 | Yahoo Finance |
| Forward P/E (Yahoo) | 33.75 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 33.15 | Yahoo Finance |
| EV/EBITDA (FMP) | 13.13 | FMP Stable API (FY2025) |
| P/B (Yahoo) | 3.74 | Yahoo Finance |
| P/B (FMP) | 1.42 | FMP Stable API |
| Dividend yield (Yahoo) | 1.06% | Yahoo Finance |
| Dividend yield (FMP) | 2.55% | FMP Stable API |

**Donnees operationnelles FMP (FY 2025) :**
| Ratio | Valeur |
|-------|--------|
| Gross margin | 43.5% |
| Operating margin | 3.9% |
| Net margin | 3.3% |
| ROE | 3.1% |
| ROIC | 1.9% |
| Debt/Equity | 0.25 |
| Current ratio | 1.58 |
| Net debt/EBITDA | -0.11 (net cash) |

**Filtre Qualite (6 criteres) :**
| Critere | Evaluation | Justification |
|---------|------------|---------------|
| Revenue CAGR 5 ans >= 20% | ❌ Non | Croissance anemique du top-line (mature 5G) |
| Profit CAGR 5 ans >= 20% | ❌ Non | Rentabilite historiquement faible |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.58, net cash position |
| FCF positif et croissant 5 ans | ⚠️ Partiel | FCF yield 4.9% mais trajectoire instable |
| Avantage competitif (moat) | ⚠️ Partiel | Leader 5G historique mais part de marche sous pression |
| Industrie forte croissance (TAM x5) | ❌ Non | TAM 5G mature, croissance a simple digit |
| **Score Qualite total** | **2.5/6** | 🔴 Hors perimetre (inchange) |

**Note fondamentale :** Aucune donnee fondamentale nouvelle entre le snapshot 17:00 UTC et le snapshot 21:00 UTC. La legere contraction du P/E (102.88 vs 103.25) reflete la baisse de -$0.06 du close, pas une amelioration des fondamentaux. Le consensus inchangé a $9.26 sur 6 analystes maintient la divergence a +77.8%.

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 102.9 vs FMP 45.8 ; P/B Yahoo 3.74 vs FMP 1.42. Cette divergence n'affecte pas le verdict consensus calibre sur l'ADR, mais elle signale que le multiple ADR est en surchauffe extreme.

**Score Valorisation :** 3.5/10 — plafonne par regle Filtre Qualite <= 3/6 (max 5/10). Premium +77.8% vs consensus, P/E 102.9, forward P/E 33.8 sur stock mature.

---

## 4. Mise a Jour Sentiment & Options

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune revision detectee — silence total malgre le +15.6% en 2j |
| Nombre analysts actifs (mois) | 1 | FMP Stable API | Faible couverture, aucun upgrade massif |
| Put/Call ratio | 0.51 | Yahoo Finance | Dominance calls moderee, inchange vs 17:00 UTC |
| Max pain | $15.00 | Yahoo Finance | Inchange — aimant gamma a 3 jours de l'expiration |
| Call OI % | 66.1% | Yahoo Finance | Stable — dominance calls maintenue |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun evenement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignee. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiee dans le flux |

**Verdict Sentiment :** Bullish technique sur les options (put/call 0.51, call OI 66.1%), mais neutre/bearish sur le consensus sell-side. Le silence absolu des analystes malgre un +15.6% en 2 jours reste un signal fort : le mouvement est purement technique/speculatif. Le max pain a $15.00 avec expiration dans 3 jours cree un aimant gamma puissant.

**Score Catalyseur :** 4.0/10 — inchange dans `recommandations_latest.json`. Aucun catalyseur identifiable ; double gap non explique par news/event ; earnings eloignes (58 jours).

---

## 5. Scoring Global

**Ponderation regime macro :** Inconnu (regime = Unknown dans `recommandations_latest.json`) — appliquee par defaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Evolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable — double gap non explique |
| Valorisation | 3.5/10 | → | P/E 102.9, cours +77.8% vs consensus, forward P/E 33.8 |
| Momentum | 7.0/10 | → | Double gap +15.6% en 2j, new 52w high, volume massif, options bullish |
| **Score Opportunite** | **4.5/10** | → | (4.0x0.35) + (3.5x0.40) + (7.0x0.25) = 4.5 |
| **Score Global** | **45.5/100** | → | Malus : Valorisation faible plombe le score |
| **Score Global ajuste** | **50.5/100** | → | — |

**Action recommandee :** **ATTENDRE** (seuil 50–59)

> Regle de disqualification : aucun score individuel <= 2/10 → ticker non exclu.
> Regle Filtre Qualite : score 2.5/6 <= 3/6 → Score Valorisation plafonne a 5/10 (applique).

**Note de scoring :** Le Score Global ajuste (50.5) reste a la limite inferieure du seuil ATTENDRE. Le double gap haussier et le volume massif n'ont pas suffi a faire passer le ticker en zone ACHETER car le malus Valorisation (P/E 103, premium +78%) et l'absence de catalyseur pesent lourd.

---

## 6. Revision des niveaux SL/TP

| Niveau | Ancien (17:00 UTC) | Nouveau (21:00 UTC) | Justification |
|--------|---------------------|---------------------|---------------|
| Stop-loss | $14.52 | **$14.46** | Revise — recalcul ATR 2x ($16.46 - $2.00) |
| Take-profit | $19.52 | **$19.46** | Revise — recalcul ATR 3x ($16.46 + $3.00) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | -43.9% | **-43.7%** | Legere amelioration (close legerement plus bas) |
| Downside SL | -12.1% | **-12.2%** | Inchange |
| Max pain options | $15.00 | **$15.00** | Inchange — aimant gamma a 3 jours |

**⚠️ Attention :** Le cours ($16.46) est desormais +9.7% au-dessus du max pain ($15.00) avec expiration dans 3 jours (29 mai). Le volume de cloture massif (1.48x) est l'element nouveau a surveiller : s'il s'agit d'achats institutionnels, le support $15.66 pourrait tenir ; s'il s'agit de distribution, un retour vers $15.00 est probable avant vendredi. Le SL a $14.46 reste la barriere de sortie principale.

---

## 7. Modules Agents — Recapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Regime Unknown | Ponderation standard 35/40/25 appliquee |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Geopolitique** | Score 3, flag 🟢 (IREN seul flagge) | NOK non flagge. Aucun risque politique detecte. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualite reste la seule barriere. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d -5.18%, RS60d -11.52%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignee. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun evenement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (58 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |

---

## 8. Conclusion — Evolution de la these

**Verdict :** La these est **modifiee confirme** — le momentum technique s'est amplifie avec un volume de cloture massif (1.48x) sur le deuxieme gap haussier. Cependant, l'absence de catalyseur fondamental et la degradation de la valorisation (P/E 103, premium +78%) maintiennent la recommandation en **ATTENDRE**.

**Analyse :**
- **Technique :** Double gap haussier confirme (+9.1% hier, +6.4% aujourd'hui), nouveau 52-week high $16.625, RSI 67.16 proche du surachat, volume de cloture massif (1.48x). Le cours a legerement recule du high ($16.46 vs $16.625) mais reste +50.4% au-dessus de la MM50.
- **Volume :** 178.7M actions (1.48x moyenne 20j) est le volume le plus eleve depuis le debut du suivi. Ce volume tardif sans catalyseur est ambigu : accumulation institutionnelle ou distribution retail ?
- **Options :** Max pain $15.00 inchange, put/call 0.51, call OI 66.1%. La structure options n'a pas suivi le prix vers le haut — le cours est +9.7% au-dessus du max pain avec expiration dans 3 jours. Risque de mean-reversion eleve.
- **Fondamentaux :** Aucune amelioration. P/E Yahoo 102.9, forward P/E 33.8. Consensus inchange $9.26. Divergence prix/valeur a +77.8%.
- **Qualite :** Toujours hors perimetre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d -5.18%). Le mouvement de NOK est totalement idiosyncratique.

**Ce qui a change :**
- **Prix :** $16.52 → $16.46 (-0.36% vs 17:00 UTC, mais +6.40% vs previous close) — consolidation legere sous le high
- **Volume :** 1.17x → 1.48x — volume de cloture massif, +28.6% vs snapshot 17:00 UTC
- **RSI :** 67.38 → 67.16 — stable
- **P/E Yahoo :** 103.25 → 102.88 — legere contraction avec le close
- **Premium consensus :** +78.4% → +77.8% — legere attenuation
- **SL/TP :** $14.52/$19.52 → $14.46/$19.46 — recalculs sur nouveau close/ATR

**Ce qui n'a pas change :**
- **Consensus :** $9.26 (6 analysts) — silence total malgre le +15.6% en 2j
- **Options :** Max pain $15.00, put/call 0.51, call OI 66.1% — structure stable
- **Qualite :** 2.5/6 hors perimetre
- **Catalyseur :** 4.0/10 — aucun identifie
- **Scores agents :** Opportunite 4.5/10, Global ajuste 50.5/100 — inchanges
- **Action :** ATTENDRE — inchangee (seuil 50–59)

**Recommandation revisee :**
- **Action :** **ATTENDRE** (Score Global ajuste 50.5/100)
- **Prix cible :** $9.26 (consensus inchange)
- **Stop-loss :** $14.46 (revise — 2xATR)
- **Take-profit :** $19.46 (revise — 3xATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scenarios forward (revises) :**
| Scenario | Probabilite | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 15% | Catalyseur non capture (M&A, contrat majeur) se confirme | $17.50–$19.50 |
| Central | 45% | Consolidation autour de $15.50–$16.50 avec pin au max pain $15.00 | Range |
| Pessimiste | 40% | Aucun catalyseur → retour de mean-reversion vers max pain $15.00 puis $14.50 | $14.50–$15.50 |

**⚠️ Risque principal :** Double gap haussier non explique + volume massif tardif = mouvement parabolique vulnerable a une correction brutale. Le max pain options a $15.00 avec expiration dans 3 jours est un aimant gamma puissant. Un franchissement sous $15.00 declencherait une acceleration vendeuse. Le SL a $14.46 est la barriere de sortie principale.

**Prochains points de controle :**
- Expiration options **2026-05-29** (dans **3 jours**) — observer le pin au max pain $15.00
- Earnings Q2 FY2026 au **2026-07-23** (dans **58 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Franchissement technique du SL a $14.46
- Catalyseur eventuel expliquant le double gap (M&A, contrat, upgrade)

---

*Donnees sources : `data/latest.json` (2026-05-26T21:00:09 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnee hallucinee.*
