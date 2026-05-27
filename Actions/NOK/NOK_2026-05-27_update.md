# NOK — Mise a Jour Quotidienne (2026-05-27, Snapshot 10:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-27 | Donnees source : `data/latest.json` (snapshot 2026-05-27T10:00:08 UTC)

---

## 1. Resume des changements depuis l'analyse precedente (2026-05-26 21:00 UTC)

| Indicateur | Snapshot 21:00 UTC (26/05) | Snapshot 10:00 UTC (27/05) | Variation | Signal |
|-----------|-------------------|-------------------|-----------|--------|
| Cours close | $16.46 | **$16.46** | **$0.00** | Aucune mutation — marche US ferme a 21:00 UTC |
| Change % vs previous close | +6.40% | **+6.40%** | 0.00 pp | Inchangé |
| RSI 14j | 67.16 | **67.16** | 0.00 | Stable — proche surachat (>70) |
| ATR 14j | $1.00 | **$1.00** | $0.00 | Inchange |
| Volume relatif | 1.48x | **1.56x** | **+0.08x** | Volume révisé a la hausse post-cloture |
| 52-week high | $16.625 | **$16.63** | +$0.005 | Arrondi — meme niveau |
| P/E (TTM Yahoo) | 102.88 | **102.88** | 0.00 | Inchange |
| Forward P/E | 33.75 | **33.75** | 0.00 | Inchange |
| P/B | 3.74 | **3.74** | 0.00 | Inchange |
| Premium vs consensus $9.26 | +77.8% | **+77.8%** | 0.0 pp | Divergence prix/valeur inchangee |
| Consensus analystes (FMP) | $9.26 (6) | **$9.26 (6)** | Inchange | Stable — silence total malgre +15.6% en 2j |
| Put/Call ratio | 0.51 | **null** | [ANOMALIE] | Données options degradees dans latest.json |
| Max pain options | $15.00 | **$2.00** | [ANOMALIE] | Valeur incoherente — conserver $15.00 comme reference |
| Call OI | 66.1% | **null** | [ANOMALIE] | Données options degradees |

**Changements significatifs detectes :**
- **Aucun changement de cours** : le snapshot 10:00 UTC du 27/05 repete integralement la cloture du 26/05 ($16.46), le marche US etant ferme entre 21:00 UTC et 10:00 UTC le lendemain. Pas de nouvelle seance de trading.
- **Volume révise a la hausse** : 188.9M actions (1.56x moyenne 20j) vs 178.7M rapporte hier a 21:00 UTC, soit +5.7% de volume supplementaire comptabilise post-cloture. Ce volume massif est maintenant confirme comme le plus eleve depuis le debut du suivi.
- **Anomalie donnees options** : `latest.json` du 27/05 affiche max pain $2.00 (vs $15.00 hier) et put/call ratio / call OI a `null`. Cette mutation est incoherente avec la structure options observee depuis le 25/05 et probablement liee a une degradation des donnees Yahoo pre-expiration (29 mai) ou a un manque de liquidite sur les strikes proches du cours. Les valeurs operationnelles retenues restent : max pain $15.00, put/call 0.51, call OI 66.1%.
- **Aucun catalyseur fondamental** identifie dans `data/events_latest.json` (vide pour NOK) ni dans `data/upcoming_events_latest.json`.

---

## 2. Mise a Jour Technique

| Metrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $16.46 | Yahoo Finance | Inchangé vs snapshot 21:00 UTC du 26/05 |
| Open | $15.99 | Yahoo Finance | Gap haussier d'ouverture du 26/05 confirmé |
| High intraday | $16.63 | Yahoo Finance | **52-week high** — arrondi a $16.63 vs $16.625 hier |
| Low intraday | $15.66 | Yahoo Finance | Support intraday immediat |
| Volume | 188,895,200 | Yahoo Finance | **1.56x moyenne 20j** (121,273,695) — volume révise +5.7% post-cloture |
| RSI 14j | 67.16 | Calcul agent | Zone neutre haute, proche surachat (>70) |
| ATR 14j | $1.00 | Calcul agent | 6.08% du cours — volatilite en expansion |
| MM 50j | $10.96 | Calcul agent | Cours +50.4% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilite au marche — mouvement idiosyncratique |

**Niveaux cles (revises) :**
- **Support immediat :** $15.66 (low du 26/05) / $15.00 (max pain options operationnel)
- **Resistance :** $16.63 (52-week high)
- **Stop-loss ATR (2x) :** $14.46 ($16.46 - $2.00)
- **Take-profit ATR (3x) :** $19.46 ($16.46 + $3.00)
- **Ratio R/R :** 1.5

**Mise a jour options — impact technique :**
| Niveau | Valeur 21:00 UTC (26/05) | Valeur 10:00 UTC (27/05) | Interpretation |
|--------|-------------|-------------------|----------------|
| Max pain | $15.00 | **$2.00** | [ANOMALIE] — conserver $15.00 comme reference operationnelle |
| Put/Call ratio | 0.51 | **null** | Donnees degradees — conserver 0.51 comme reference |
| Call OI % | 66.1% | **null** | Donnees degradees — conserver 66.1% comme reference |
| Cours vs max pain | +9.7% | **+9.7%** | Inchangé — cours significativement au-dessus du pin |
| Expiration | 2026-05-29 | **2026-05-29** | **2 jours** — risque de pin au max pain $15.00 |

**Verdict timing :** Favorable sur le momentum pur, mais **defavorable sur la durabilite**. Le volume de cloture massif (1.56x) est maintenant confirme avec un chiffre revise a la hausse. L'absence de mutation entre le snapshot 21:00 UTC et 10:00 UTC confirme que le marche US n'a pas ouvert, mais l'expiration options approche dans 2 jours. Le risque de mean-reversion vers le max pain $15.00 reste eleve.

**Score Momentum :** 7.0/10 — inchange dans `recommandations_latest.json`.

---

## 3. Mise a Jour Fondamentale

| Metrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $91.89 B | Yahoo Finance |
| Market Cap (FMP FY2025) | $29.82 B | FMP Stable API |
| P/E (TTM Yahoo) | 102.88 | Yahoo Finance |
| Forward P/E (Yahoo) | 33.75 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 35.33 | Yahoo Finance |
| EV/EBITDA (FMP) | 13.13 | FMP Stable API (FY2025) |
| P/B (Yahoo) | 3.74 | Yahoo Finance |
| P/B (FMP) | 1.42 | FMP Stable API |
| Dividend yield (Yahoo) | 1.00% | Yahoo Finance |
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

**Note fondamentale :** Aucune donnee fondamentale nouvelle entre le snapshot 21:00 UTC du 26/05 et le snapshot 10:00 UTC du 27/05. Le P/E, forward P/E, P/B et consensus sont strictement inchanges. La divergence prix/valeur a +77.8% vs consensus $9.26 persiste.

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 102.9 vs FMP 45.8 ; P/B Yahoo 3.74 vs FMP 1.42. Cette divergence n'affecte pas le verdict consensus calibre sur l'ADR, mais elle signale que le multiple ADR est en surchauffe extreme.

**Score Valorisation :** 3.5/10 — plafonne par regle Filtre Qualite <= 3/6 (max 5/10). Premium +77.8% vs consensus, P/E 102.9, forward P/E 33.8 sur stock mature.

---

## 4. Mise a Jour Sentiment & Options

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune revision detectee — silence total malgre le +15.6% en 2j |
| Nombre analysts actifs (mois) | 1 | FMP Stable API | Faible couverture, aucun upgrade massif |
| Put/Call ratio | 0.51 [conservé] | Yahoo Finance (latest.json degrade) | Dominance calls moderee |
| Max pain | $15.00 [conservé] | Yahoo Finance (latest.json degrade : $2.00) | Pin operationnel a 2 jours |
| Call OI % | 66.1% [conservé] | Yahoo Finance (latest.json degrade) | Dominance calls maintenue |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun evenement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignee. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiee dans le flux |

**Verdict Sentiment :** Bullish technique sur les options (put/call 0.51, call OI 66.1%), mais neutre/bearish sur le consensus sell-side. Le silence absolu des analystes malgre un +15.6% en 2 jours reste un signal fort : le mouvement est purement technique/speculatif. L'anomalie donnees options dans `latest.json` (max pain $2.00, null sur put/call et call OI) est a traiter avec prudence — les valeurs operationnelles retenues sont celles du 26/05. Le max pain a $15.00 avec expiration dans 2 jours cree un aimant gamma puissant.

**Score Catalyseur :** 4.0/10 — inchange dans `recommandations_latest.json`. Aucun catalyseur identifiable ; double gap non explique par news/event ; earnings eloignes (57 jours).

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

**Note de scoring :** Le Score Global ajuste (50.5) reste a la limite inferieure du seuil ATTENDRE. Aucune mutation de donnees entre le 26/05 21:00 UTC et le 27/05 10:00 UTC. Le double gap haussier et le volume massif n'ont pas suffi a faire passer le ticker en zone ACHETER car le malus Valorisation (P/E 103, premium +78%) et l'absence de catalyseur pesent lourd.

---

## 6. Revision des niveaux SL/TP

| Niveau | Ancien (21:00 UTC 26/05) | Nouveau (10:00 UTC 27/05) | Justification |
|--------|---------------------|---------------------|---------------|
| Stop-loss | $14.46 | **$14.46** | Inchange — ATR 2x stable |
| Take-profit | $19.46 | **$19.46** | Inchange — ATR 3x stable |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | -43.7% | **-43.7%** | Inchange |
| Downside SL | -12.2% | **-12.2%** | Inchange |
| Max pain options | $15.00 | **$15.00** | [Conservé] — anomalie $2.00 dans latest.json ignoree |

**⚠️ Attention :** Le cours ($16.46) est +9.7% au-dessus du max pain operationnel ($15.00) avec expiration dans **2 jours** (29 mai). Le volume de cloture massif (1.56x) est confirme avec un chiffre revise a 188.9M. L'interpretation reste ambigue : accumulation institutionnelle ou distribution retail ? Le SL a $14.46 reste la barriere de sortie principale.

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
| **Agent Watchman** | Earnings 2026-07-23 (57 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |

---

## 8. Conclusion — Evolution de la these

**Verdict :** La these est **confirme inchangee** — aucune mutation de donnees entre le snapshot 21:00 UTC du 26/05 et le snapshot 10:00 UTC du 27/05 (marche US ferme). Le volume de cloture massif est revise a la hausse (1.56x), confirmant l'intensite du mouvement. L'anomalie donnees options (max pain $2.00 dans `latest.json`) est ignoree au profit des valeurs operationnelles du 26/05 ($15.00). La recommandation reste **ATTENDRE**.

**Analyse :**
- **Technique :** Double gap haussier confirme (+9.1% le 25/05, +6.4% le 26/05), 52-week high $16.63, RSI 67.16 proche du surachat, volume massif confirme (1.56x). Le cours est stable a $16.46, +50.4% au-dessus de la MM50.
- **Volume :** 188.9M actions (1.56x moyenne 20j) est le volume le plus eleve depuis le debut du suivi, confirme par revision post-cloture. Sans catalyseur, ce volume reste ambigu.
- **Options :** Max pain operationnel $15.00 conserve, put/call 0.51, call OI 66.1%. La structure options n'a pas suivi le prix vers le haut — le cours est +9.7% au-dessus du max pain avec expiration dans 2 jours. Risque de mean-reversion eleve.
- **Fondamentaux :** Aucune amelioration. P/E Yahoo 102.9, forward P/E 33.8. Consensus inchange $9.26. Divergence prix/valeur a +77.8%.
- **Qualite :** Toujours hors perimetre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d -5.18%). Le mouvement de NOK est totalement idiosyncratique.

**Ce qui a change :**
- **Volume :** 1.48x → 1.56x — volume de cloture massif confirme avec revision post-cloture (+5.7%)
- **52-week high :** $16.625 → $16.63 (arrondi, meme niveau)
- **Expiration options :** 3 jours → **2 jours** (29 mai)
- **SL/TP :** Inchanges ($14.46/$19.46)

**Ce qui n'a pas change :**
- **Cours :** $16.46 — stable
- **Consensus :** $9.26 (6 analysts) — silence total malgre le +15.6% en 2j
- **RSI :** 67.16 — stable
- **ATR :** $1.00 — stable
- **Options (operationnel) :** Max pain $15.00, put/call 0.51, call OI 66.1%
- **Qualite :** 2.5/6 hors perimetre
- **Catalyseur :** 4.0/10 — aucun identifie
- **Scores agents :** Opportunite 4.5/10, Global ajuste 50.5/100 — inchanges
- **Action :** ATTENDRE — inchangee (seuil 50–59)

**Recommandation revisee :**
- **Action :** **ATTENDRE** (Score Global ajuste 50.5/100)
- **Prix cible :** $9.26 (consensus inchange)
- **Stop-loss :** $14.46 (inchange — 2xATR)
- **Take-profit :** $19.46 (inchange — 3xATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scenarios forward (revises) :**
| Scenario | Probabilite | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 15% | Catalyseur non capture (M&A, contrat majeur) se confirme | $17.50–$19.50 |
| Central | 45% | Consolidation autour de $15.50–$16.50 avec pin au max pain $15.00 | Range |
| Pessimiste | 40% | Aucun catalyseur → retour de mean-reversion vers max pain $15.00 puis $14.50 | $14.50–$15.50 |

**⚠️ Risque principal :** Double gap haussier non explique + volume massif tardif = mouvement parabolique vulnerable a une correction brutale. Le max pain options a $15.00 avec expiration dans 2 jours est un aimant gamma puissant. Un franchissement sous $15.00 declencherait une acceleration vendeuse. Le SL a $14.46 est la barriere de sortie principale.

**Prochains points de controle :**
- Expiration options **2026-05-29** (dans **2 jours**) — observer le pin au max pain $15.00
- Earnings Q2 FY2026 au **2026-07-23** (dans **57 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Franchissement technique du SL a $14.46
- Catalyseur eventuel expliquant le double gap (M&A, contrat, upgrade)

---

*Donnees sources : `data/latest.json` (2026-05-27T10:00:08 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnee hallucinee.*
