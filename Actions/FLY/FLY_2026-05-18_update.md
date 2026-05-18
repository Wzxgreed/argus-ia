# FLY — Mise a Jour Quotidienne (2026-05-18)

> Source : `data/latest.json` (2026-05-18 21:00 UTC) + `data/recommandations_latest.json` + agents quant / geo / sector / social / FX / events / upcoming.

---

## Resume des changements depuis l'analyse precedente (2026-05-17)

| Metrique | 2026-05-17 (init) | 2026-05-18 (snapshot 21:00 UTC) | Variation | Seuil d'alerte |
|----------|-------------------|-----------------------------------|-----------|----------------|
| Cours close | $40.43 | **$43.95** | **+8.71%** | >= +-5% |
| RSI 14j | 61.71 | **67.08** | +5.37 pts | >70 / <30 |
| MM 50j | $32.24 | $32.72 | +$0.48 (+1.5%) | — |
| MM 200j | N/A | N/A | — | — |
| ATR 14j | [DONNEES MANQUANTES] | **$4.39** | — | >5% relatif |
| Volume 20j moy. | [DONNEES MANQUANTES] | 6,239,757 | — | — |
| Volume jour | 1.37x moy. | **9,789,240** | **1.57x moy.** | >2.0x |
| Filtre Qualite | 2/6 | 2/6 | stable | — |
| Forward P/E | -35.41 | **-38.50** | degrade | — |
| P/B (Yahoo) | 5.86 | **6.37** | +8.7% | — |
| EV/Revenue (Yahoo) | 32.34x | 32.34x | stable | — |
| Consensus PT (FMP) | $42.45 (11 analysts) | $42.45 (11 analysts) | stable | — |
| Upside consensus | +5.0% | **-3.4%** | spot > PT | — |
| Max Pain | $25.00 | $25.00 | stable | — |
| Put/Call Ratio | 0.85 | 0.86 | stable | — |
| Short Interest | 0.09% | 0.0866% | stable | >5% |
| Score Opportunite | 5.2/10 | **5.3/10** | +0.1 pt | — |
| Score Valorisation | 5.0/10 | **4.5/10** | -0.5 pt | — |
| Score Catalyseur | 5.0/10 | 5.0/10 | stable | — |
| Score Momentum | 6.0/10 | **7.0/10** | +1.0 pt | — |
| Score Global | 52.0 | **53.0** | +1.0 pt | — |
| Score Global Ajuste | 57.0 | **58.0** | +1.0 pt | — |

**Observations cles :**
- **Gap +8.71%** vs prior close ($40.43 -> $43.95) — seuil +-5% franchi. Amplitude intraday 12.3% ($42.34-$47.71) sans catalyst visible structurel.
- **RSI 67.08** — zone haussiere elevee, proche du surachat (>70). Momentum renforce vs init (61.71).
- **Volume en acceleration** 1.57x moy. 20j (9.79M vs 6.24M) — comportement post-gap speculatif a surveiller pour signe de distribution institutionnelle.
- **Fondamentaux inchanges et defavorables** : Filtre Qualite 2/6 (hors perimetre), Forward P/E degrade (-38.50), marges fortement negatives (operating margin -154.3%, net margin -186.6%).
- **Consensus PT $42.45 sous le spot** (-3.4% upside) — la marge de securite analytique a disparu avec le gap.
- **Agent Quant** : `data/quant_report_latest.json` du 2026-05-17 — pas assez de signaux historiques -> [SIGNAUX NON SIGNIFICATIFS] (p-value 1.0).
- **Agent Accounting** : `data/accounting_risk_latest.json` absent -> [DONNEES MANQUANTES] pour M-Score / Z-Score / F-Score / Sloan.
- **Agent Geo** : FLY non flagge — pas d'exposition politique specifique.
- **Agent Event-Driven** : 0 evenement corporate detecte dans `data/events_latest.json`.
- **Agent Social** : 0 mentions Reddit, 0.0 sentiment, pump non detecte.

---

## Mise a jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 67.08 | Haussier, proche du surachat (>70) — momentum renforce vs init |
| MM 50j | $32.72 | Cours superieur de **+34.3%**, tendance haussiere intacte |
| MM 200j | N/A | Donnee indisponible — impossible de valider le Golden/Death Cross |
| Volume | 9,789,240 | 1.57x moy. 20j — volume post-gap en acceleration |
| ATR 14j | $4.39 | Relatif 10.0% — volatilite elevee, comportement speculatif |
| Range jour | $42.34–$47.71 | Amplitude **12.3%** sans catalyst visible |
| Support 1 | $32.72 (MM50) | Support dynamique — rupture = revision baissiere |
| Support 2 | $16.00 (52W Low) | — |
| Resistance 1 | $47.71 (High du jour) | Teste en seance, non confirme en close |
| Resistance 2 | $73.80 (52W High) | — |

**Timing verdict :** **Favorable mais risque** — tendance haussiere intacte (cours > MM50 +34.3%), RSI en zone haussiere elevee. La consolidation au-dessus de $43 apres le gap est un signal technique positif, mais la proximite de l'expiration options (22/05) maintient le risque de microstructure eleve. Volume accelere post-gap peut indiquer du profit-taking ou de la distribution.

---

## Mise a jour fondamentale

Donnees croisees Yahoo / FMP (annual FY 2025) :

| Metrique | Yahoo | FMP | Commentaire |
|----------|-------|-----|-------------|
| Market Cap | $7.04B | $3.40B | Divergence materielle — Yahoo utilise close actuel, FMP donnees historiques |
| Forward P/E | -38.50 | — | Pas de rentabilite nette attendue |
| EV/EBITDA | -26.61 | -13.12 | EBITDA negatif sur les deux sources |
| P/B | 6.37 | 2.86 | Divergence — Yahoo plus conservateur |
| EV/Revenue (Yahoo) | 32.34x | — | Multiple eleve |
| P/S (FMP) | — | 21.26x | — |
| Gross Margin | — | 15.6% | Faible |
| Operating Margin | — | -154.3% | Fortement negatif |
| EBITDA Margin | — | -138.9% | Fortement negatif |
| Net Margin | — | -186.6% | Fortement negatif |
| Debt/Equity | — | 0.26 | Levier modere |
| Current Ratio | — | 4.51 | Liquidite solide |
| Short Interest | 0.0866% | — | Aucun pari baissier structure |

**Filtre Qualite** : **2/6** (Hors perimetre)
| Critere | Verdict |
|---------|---------|
| Revenue CAGR 5 ans >= 20% | Donnees insuffisantes dans le snapshot |
| Profit CAGR 5 ans >= 20% | Forward P/E -38.50, marges negatives |
| Assets/Liabilities > 1.0 | Current Ratio 4.51 (solide) mais pas de visibilite complete sur le bilan |
| FCF positif et croissant 5 ans | FCF yield negatif (-7.0% environ, price_to_fcf -14.29) |
| Avantage competitif (moat) | Non demontre dans les donnees |
| Industrie forte croissance (TAM x5) | Donnees insuffisantes |

**Regle** : Score <= 3/6 -> Score Valorisation plafonne a 5/10 avant calcul final. L'agent recommandation applique **4.5/10**.

---

## Mise a jour sentiment / options / news

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-3.4%) — plus d'upside selon le consensus. Couverture stable. |
| Max Pain | $25.00 | Yahoo Finance | Ecart de **43%** sous le spot. Distorsion probable liee a l'expiration du 22/05. |
| Put/Call Ratio | 0.86 | Yahoo Finance | Legerement call-biased (53.8% call OI). |
| Call OI % | 53.8% | Yahoo Finance | Biais call modere. |
| Short Interest | 0.0866% | Yahoo Finance | Absence de squeeze setup. |
| Social Sentiment | 0 mentions, 0.0 score | `data/social_sentiment_latest.json` | Aucune activite retail detectee sur Reddit. |
| Event-Driven | Aucun | `data/events_latest.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (78 jours) | `data/upcoming_events_latest.json` | Est EPS -$0.60 a -$0.45, Rev $0.1B. |
| News FLY | Aucune | `data/news_latest.json` | Aucune news specifique au ticker dans le snapshot. |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immediat. Le prochain catalyst structurel est l'earnings d'aout.

---

## Scoring global (Agent Recommandation — 2026-05-18 21:00 UTC)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 7.0/10 | 25% | 1.75 |
| **Score Opportunite** | **5.3/10** | | |
| Malus/Bonus | +4.5 pts | | (pas de malus accounting/geo/FX majeur) |
| **Score Global** | **53.0** | | |
| **Score Global Ajuste** | **58.0** | | |

**Action** : **ATTENDRE**
**Direction** : Neutre
**Timing** : Favorable (technique) mais risque
**Horizon** : —

**Ajustements agents complementaires :**
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant) -> pas d'ajustement.
- **Agent Geo** : FLY non flagge (pas d'exposition politique specifique detectee) -> pas de malus.
- **Agent Sector Rotation** : XLI (Industrials) sous-performant le SPY sur 20j (-1.81%) et 60j (-3.40%), momentum_score 0.0 -> **headwind sectoriel** (-0.5 pt implicite sur le catalyseur sectoriel).
- **Agent Social** : Pas d'activite retail -> neutre.
- **Agent FX** : Exposition 25%, currency USD, fx_impact_score 0.0, divergence aligned -> pas d'ajustement.
- **Agent Event-Driven** : 0 evenement -> neutre.

---

## Revision des niveaux SL / TP

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $43.95 | Close 2026-05-18 21:00 UTC | +8.71% vs prior close |
| Stop-loss | $35.17 | Cours - 2xATR ($4.39) | ATR stable |
| Take-profit | $57.12 | Cours + 3xATR ($4.39) | ATR stable |
| Ratio R/R | 1.5:1 | Gain $13.17 / Perte $8.78 | Limite pour un profil sans rentabilite |

Les niveaux sont calcules sur l'ATR actuel a $4.39. Le ratio 1.5:1 reste limite pour une action sans rentabilite demontree et avec un Filtre Qualite faible (2/6).

---

## Conclusion — These confirmee, modifiee ou invalidee ?

**Verdict : These CONFIRMEE avec nuance haussiere technique.**

Le gap de +8.71% et la consolidation au-dessus de $43 confirment le momentum technique identifie dans l'analyse initiale. Cependant, **aucun fondamental ne justifie ce rehaussement de cours**. Le Filtre Qualite reste a 2/6 (hors perimetre), les marges sont fortement negatives, et le consensus analystes ($42.45) est desormais sous le spot.

**Ce qui confirme la these :**
- Cours stable post-gap, consolidant au-dessus de $43 — momentum intact.
- RSI 67.08, MM50 $32.72 — tendance haussiere technique confirmee et renforcee vs init.
- Aucune news structurante, guidance raise, ou evenement corporate detecte dans les agents events / geo / social.
- Scoring global en zone ATTENDRE (53.0 / 58.0 ajuste) — pas de bascule vers ACHETER ou EVITER.

**Ce qui maintient la prudence :**
- Filtre Qualite 2/6 (hors perimetre) — pas de quality compounding.
- Forward P/E degrade (-38.50), marges negatives, EV/Revenue 32x — valorisation incompatible avec les fondamentaux.
- Consensus PT $42.45 sous le spot (-3.4% upside) — plus de marge de securite selon les analystes.
- Headwind sectoriel : XLI sous-performe le SPY (momentum_score 0.0).
- Volatilite elevee sans couverture fondamentale (ATR 10%, range intraday 12.3%) — risque de correction rapide si le momentum casse.
- Volume accelere post-gap peut indiquer du profit-taking ou de la distribution institutionnelle.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 78 jours) : Est EPS -$0.45 a -$0.60, Rev $0.1B. Toute surprise positive vs consensus negatif serait un catalyseur majeur.
2. **Expiration options 22/05** (4 jours) : surveillance post-expiration pour voir si la volatilite se normalise et si le Max Pain redevient coherent avec le spot.

**Risques :**
1. Rentabilite non demontree — la societe brule du cash avec des marges fortement negatives (operating margin -154%, net margin -187%).
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 32x, P/B 6.37x).
3. Cours au-dessus du consensus analystes — si les resultats ne suivent pas, le gap de valorisation se resserrera brutalement.
4. Comportement speculatif intraday (range 12.3%) sans catalyst — risque de retournement rapide.

**Prochaine etape :**
- Maintenir **ATTENDRE**. Aucune position recommandee.
- Surveiller l'approche des earnings (aout) et toute amelioration des marges ou du FCF dans les prochains filings.
- Si le cours casse la MM50 ($32.72) -> reviser la these a la baisse.
- Si un catalyst fondamental emerge (contrat, partnership, guidance raise) -> reevaluer le Score Catalyseur et le Filtre Qualite.
