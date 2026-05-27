# NOK — Mise a Jour Quotidienne (2026-05-27, Snapshot 13:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-27 | Donnees source : `data/latest.json` (snapshot 2026-05-27T13:00:02 UTC)

---

## 1. Resume des changements depuis l'analyse precedente (2026-05-27 10:00 UTC)

| Indicateur | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Variation | Signal |
|-----------|-------------------|-------------------|-----------|--------|
| Cours close | $16.46 | **$16.46** | **$0.00** | Aucune mutation — marche ferme |
| Change % vs previous close | +6.40% | **+6.40%** | 0.00 pp | Inchange |
| RSI 14j | 67.16 | **67.16** | 0.00 | Stable — proche surachat (>70) |
| ATR 14j | $1.00 | **$1.00** | $0.00 | Inchange |
| Volume | 188,895,200 | **188,895,200** | 0 | Inchange — 1.56x moyenne 20j |
| 52-week high | $16.63 | **$16.63** | — | Inchange |
| P/E (TTM Yahoo) | 102.88 | **102.88** | 0.00 | Inchange |
| Forward P/E | 33.75 | **33.75** | 0.00 | Inchange |
| P/B | 3.74 | **3.74** | 0.00 | Inchange |
| Premium vs consensus $9.26 | +77.8% | **+77.8%** | 0.0 pp | Divergence prix/valeur inchangee |
| Consensus analystes (FMP) | $9.26 (6) | **$9.26 (6)** | Inchange | Silence total malgre +15.6% en 2j |
| **Max pain options** | $2.00 [ANOMALIE] | **$16.00** | **+$14.00** | **Donnees restaurees — max pain aligne sur le cours** |
| **Put/Call ratio** | null [ANOMALIE] | **0.53** | — | **Restaure — dominance calls moderee** |
| **Call OI** | null [ANOMALIE] | **65.3%** | — | **Restaure — bullish mais leger recul** |

**Changements significatifs detectes :**
- **Restauration des donnees options** : le snapshot 13:00 UTC corrige l'anomalie du 10:00 UTC (max pain $2.00, put/call et call OI a `null`). Les valeurs sont desormais coherentes : max pain **$16.00**, put/call **0.53**, call OI **65.3%**. Cette mutation est l'evenement technique majeur du snapshot.
- **Max pain revalorise de $15.00 a $16.00** : le niveau de pin gamma a migre vers le haut, confirmant la nouvelle base de cours. Le cours ($16.46) n'est plus que **+2.9%** au-dessus du max pain (vs +9.7% hier) — le risque de mean-reversion vers le pin est **fortement attenue**.
- **Aucun changement de cours/volume/fondamentaux** : le marche US n'ayant pas ouvert de nouvelle seance entre 10:00 et 13:00 UTC, toutes les donnees de prix, volumes, RSI, ATR et fondamentaux sont strictement identiques au snapshot 10:00 UTC.
- **Aucun catalyseur fondamental** identifie dans `data/events_latest.json` (vide pour NOK).

---

## 2. Mise a Jour Technique

| Metrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $16.46 | Yahoo Finance | Inchange vs snapshots precedents |
| Open | $15.99 | Yahoo Finance | Gap haussier du 26/05 confirme |
| High intraday | $16.63 | Yahoo Finance | 52-week high — inchange |
| Low intraday | $15.66 | Yahoo Finance | Support intraday immediat |
| Volume | 188,895,200 | Yahoo Finance | 1.56x moyenne 20j (121,273,695) — volume massif confirme |
| RSI 14j | 67.16 | Calcul agent | Zone neutre haute, proche surachat (>70) |
| ATR 14j | $1.00 | Calcul agent | 6.08% du cours — volatilite en expansion |
| MM 50j | $10.96 | Calcul agent | Cours +50.4% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilite au marche — mouvement idiosyncratique |

**Niveaux cles (revises) :**
- **Support immediat :** $15.66 (low du 26/05) / $16.00 (max pain options, nouveau)
- **Resistance :** $16.63 (52-week high)
- **Stop-loss ATR (2x) :** $14.46 ($16.46 - $2.00)
- **Take-profit ATR (3x) :** $19.46 ($16.46 + $3.00)
- **Ratio R/R :** 1.5

**Mise a jour options — impact technique :**
| Niveau | Valeur 10:00 UTC (27/05) | Valeur 13:00 UTC (27/05) | Interpretation |
|--------|-------------|-------------------|----------------|
| Max pain | $2.00 [ANOMALIE] | **$16.00** | **Restaure et revalorise** — pin aligne sur le cours |
| Put/Call ratio | null [ANOMALIE] | **0.53** | **Restaure** — dominance calls moderee, legerement superieure a 0.51 |
| Call OI % | null [ANOMALIE] | **65.3%** | **Restaure** — bullish, legere baisse vs 66.1% du 26/05 |
| Cours vs max pain | +9.7% (vs $15.00 op.) | **+2.9%** | **Risque mean-reversion fortement reduit** |
| Expiration | 2026-05-29 | **2026-05-29** | **2 jours** — risque de pin desormais faible |

**Verdict timing :** Favorable sur le momentum pur. La restauration du max pain a **$16.00** est un element technique positif majeur : le marché options a valide la nouvelle base de cours a $16.00, eliminant le risque de reversion violent vers $15.00. Le cours n'est plus que +2.9% au-dessus du pin, ce qui est dans la marge normale d'une expiration. Cependant, le timing reste **defavorable sur la durabilite** car le double gap (+15.6% en 2j) reste sans catalyseur fondamental.

**Score Momentum :** 7.0/10 — inchange dans `recommandations_latest.json`.

---

## 3. Mise a Jour Fondamentale

| Metrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $91.89 B | Yahoo Finance |
| P/E (TTM Yahoo) | 102.88 | Yahoo Finance |
| Forward P/E (Yahoo) | 33.75 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 35.33 | Yahoo Finance |
| P/B (Yahoo) | 3.74 | Yahoo Finance |
| Dividend yield (Yahoo) | 1.00% | Yahoo Finance |

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

**Note fondamentale :** Aucune donnee fondamentale nouvelle entre le snapshot 10:00 UTC et 13:00 UTC du 27/05. Le P/E, forward P/E, P/B et consensus sont strictement inchanges. La divergence prix/valeur a +77.8% vs consensus $9.26 persiste.

**Score Valorisation :** 3.5/10 — plafonne par regle Filtre Qualite <= 3/6 (max 5/10). Premium +77.8% vs consensus, P/E 102.9, forward P/E 33.8 sur stock mature.

---

## 4. Mise a Jour Sentiment & Options

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune revision detectee — silence total malgre le +15.6% en 2j |
| Nombre analysts actifs (mois) | 1 | FMP Stable API | Faible couverture, aucun upgrade massif |
| Put/Call ratio | 0.53 | Yahoo Finance (restaure) | Dominance calls moderee, legerement superieure a 0.51 |
| Max pain | $16.00 | Yahoo Finance (restaure) | **Pin revalorise** — aligne sur le cours, risque mean-reversion attenue |
| Call OI % | 65.3% | Yahoo Finance (restaure) | Bullish, legere baisse vs 66.1% du 26/05 |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun evenement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignee. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiee dans le flux |

**Verdict Sentiment :** La restauration des donnees options est le signal cle du snapshot. Le max pain a $16.00 (vs $15.00 hier) indique que le marché options a valide la nouvelle base de cours. Le cours n'est plus que +2.9% au-dessus du pin avec expiration dans 2 jours — le risque de mean-reversion vers $15.00 est elimine. Cependant, le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement reste sans explication fondamentale.

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

**Note de scoring :** Le Score Global ajuste (50.5) reste a la limite inferieure du seuil ATTENDRE. La restauration des options et le max pain a $16.00 ameliorent le profil technique, mais le malus Valorisation (P/E 103, premium +78%) et l'absence de catalyseur fondamental empechent tout passage en zone ACHETER.

---

## 6. Revision des niveaux SL/TP

| Niveau | Ancien (10:00 UTC) | Nouveau (13:00 UTC) | Justification |
|--------|---------------------|---------------------|---------------|
| Stop-loss | $14.46 | **$14.46** | Inchange — ATR 2x stable |
| Take-profit | $19.46 | **$19.46** | Inchange — ATR 3x stable |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | -43.7% | **-43.7%** | Inchange |
| Downside SL | -12.2% | **-12.2%** | Inchange |
| Max pain options | $15.00 (operationnel) | **$16.00** | **Restaure et revalorise** — pin aligne sur le cours |

**⚠️ Attention :** Le max pain est desormais a **$16.00** (restauration des donnees options), tres proche du cours ($16.46, +2.9%). Le risque de pin gamma a l'expiration du 29 mai est **fortement reduit** par rapport au scenario du 10:00 UTC (max pain $15.00, cours +9.7% au-dessus). Le SL a $14.46 reste la barriere de sortie principale, mais la probabilite de l'atteindre avant expiration est desormais jugee plus faible.

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

**Verdict :** La these est **modifiee confirme** — la restauration des donnees options et le max pain revalorise a $16.00 ameliorent le profil technique, mais l'absence de catalyseur fondamental et la degradation de la valorisation (P/E 103, premium +78%) maintiennent la recommandation en **ATTENDRE**.

**Analyse :**
- **Technique :** Double gap haussier confirme (+9.1% le 25/05, +6.4% le 26/05), 52-week high $16.63, RSI 67.16 proche du surachat, volume massif confirme (1.56x). Le cours est stable a $16.46, +50.4% au-dessus de la MM50.
- **Options (mutation majeure) :** Max pain restaure et revalorise a **$16.00** (vs $2.00 anomalie a 10:00 UTC, vs $15.00 operationnel du 26/05). Put/call 0.53, call OI 65.3%. Le marché options a valide la nouvelle base de cours — le risque de mean-reversion vers $15.00 est elimine. Le cours n'est plus que +2.9% au-dessus du pin (vs +9.7% hier).
- **Volume :** 188.9M actions (1.56x moyenne 20j) — volume le plus eleve depuis le debut du suivi, confirme. Sans catalyseur, ce volume reste ambigu (accumulation ou distribution ?).
- **Fondamentaux :** Aucune amelioration. P/E Yahoo 102.9, forward P/E 33.8. Consensus inchange $9.26. Divergence prix/valeur a +77.8%.
- **Qualite :** Toujours hors perimetre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d -5.18%). Le mouvement de NOK reste totalement idiosyncratique.

**Ce qui a change :**
- **Options — max pain :** $15.00 (operationnel) → **$16.00** (restaure) — revalorisation majeure, risque mean-reversion attenue
- **Options — put/call :** 0.51 → **0.53** — legere augmentation de la dominance calls
- **Options — call OI :** 66.1% → **65.3%** — legere baisse mais reste bullish
- **Options — cours vs max pain :** +9.7% → **+2.9%** — pin gamma desormais aligne

**Ce qui n'a pas change :**
- **Cours :** $16.46 — stable
- **RSI :** 67.16 — stable
- **ATR :** $1.00 — stable
- **Volume :** 188.9M — stable
- **Consensus :** $9.26 (6 analysts) — silence total malgre le +15.6% en 2j
- **Qualite :** 2.5/6 hors perimetre
- **Catalyseur :** 4.0/10 — aucun identifie
- **Scores agents :** Opportunite 4.5/10, Global ajuste 50.5/100 — inchanges
- **Action :** ATTENDRE — inchangee (seuil 50–59)
- **SL/TP :** $14.46/$19.46 — inchanges

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
| Optimiste | 20% | Catalyseur non capture (M&A, contrat majeur) se confirme | $17.50–$19.50 |
| Central | 50% | Consolidation autour de $16.00–$16.50 avec pin au max pain $16.00 | Range |
| Pessimiste | 30% | Aucun catalyseur → legere correction vers $15.50–$16.00 | $15.50–$16.00 |

**⚠️ Risque principal :** Double gap haussier non explique + volume massif = mouvement parabolique vulnerable. Cependant, le max pain revalorise a $16.00 reduit le risque de mean-reversion brutale. Le SL a $14.46 reste la barriere de sortie principale. L'expiration du 29 mai est desormais vue comme un evenement neutre (pin a $16.00 aligne sur le cours) plutot que bearish.

**Prochains points de controle :**
- Expiration options **2026-05-29** (dans **2 jours**) — max pain $16.00, risque pin desormais limite
- Earnings Q2 FY2026 au **2026-07-23** (dans **57 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Franchissement technique du SL a $14.46
- Catalyseur eventuel expliquant le double gap (M&A, contrat, upgrade)

---

*Donnees sources : `data/latest.json` (2026-05-27T13:00:02 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnee hallucinee.*
