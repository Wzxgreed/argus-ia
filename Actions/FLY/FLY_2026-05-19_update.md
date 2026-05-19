# FLY — Mise a Jour (2026-05-19 13:00 UTC)

> Source : `data/latest.json` (2026-05-19 13:00 UTC) + `data/recommandations_latest.json` + agents quant / geo / sector / social / FX / events / upcoming.

---

## Resume des changements depuis l'analyse precedente (2026-05-19 10:00 UTC)

| Metrique | 2026-05-19 10:00 UTC | 2026-05-19 13:00 UTC | Variation |
|----------|----------------------|----------------------|-----------|
| Cours close | $43.95 | **$43.95** | **0.00%** |
| RSI 14j | 67.08 | **67.08** | 0.00 |
| MM 50j | $32.72 | $32.72 | $0.00 |
| ATR 14j | $4.39 | **$4.39** | $0.00 |
| Volume jour | 9,827,800 | **9,827,800** | stable |
| Change % vs prior close | +8.71% | **+8.71%** | stable |
| Forward P/E | -38.50 | **-38.50** | stable |
| Consensus PT (FMP) | $42.45 (11 analysts) | $42.45 (11 analysts) | stable |
| **Options — Max Pain** | $15.00 (source Yahoo) | **$65.00** | **+333%** [CORRECTION] |
| **Options — Put/Call** | N/A | **0.64** | [CORRECTION] |
| **Options — Call OI %** | N/A | **61.1%** | [CORRECTION] |
| Score Opportunite | 5.3/10 | **5.3/10** | stable |
| Score Valorisation | 4.5/10 | **4.5/10** | stable |
| Score Catalyseur | 5.0/10 | 5.0/10 | stable |
| Score Momentum | 7.0/10 | **7.0/10** | stable |
| Score Global | 53.0 | **53.0** | stable |
| Score Global Ajuste | 58.0 | **58.0** | stable |

**Verdict : Donnees de cours, technique et fondamentale strictement inchangees vs snapshot 10:00 UTC.** Correction significative des donnees options : Max Pain remonte a $65.00 (vs $15.00 precedemment), put/call ratio 0.64, call OI 61.1%. Cette distorsion suggere un biais call tres prononce pour l'expiration du 22/05, avec une convexite haussiere plus marquee qu'initialement estimee.

---

## Mise a jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 67.08 | Haussier, proche surachat (>70) — inchangé |
| MM 50j | $32.72 | Cours superieur de **+34.3%**, tendance haussiere intacte |
| MM 200j | N/A | Donnee indisponible |
| Volume | 9,827,800 | 1.57x moy. 20j — acceleration post-gap confirmee, a surveiller |
| ATR 14j | $4.39 | Relatif 10.0% — volatilite elevee, comportement speculatif |
| Range jour | $42.34–$47.71 | Amplitude **12.3%** sans catalyst visible structurel |
| Support 1 | $32.72 (MM50) | Support dynamique — rupture = revision baissiere |
| Support 2 | $16.00 (52W Low) | — |
| Resistance 1 | $47.71 (High du jour) | Teste en seance, non confirme en close |
| Resistance 2 | $73.80 (52W High) | — |

**Timing verdict :** **Favorable mais risque** — tendance haussiere intacte (cours > MM50 +34.3%), RSI en zone haussiere elevee. La consolidation au-dessus de $43 apres le gap est un signal technique positif. La proximite de l'expiration options (22/05, soit dans 3 jours) maintient le risque de microstructure eleve.

---

## Mise a jour fondamentale

Donnees croisees Yahoo / FMP (annual FY 2025) — **inchangées vs snapshot 2026-05-19 10:00 UTC** :

| Metrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap | $7.04B (Yahoo) | Divergence FMP non renseignee |
| Forward P/E | -38.50 | Pas de rentabilite nette attendue |
| EV/EBITDA (Yahoo) | -29.12 | EBITDA negatif |
| EV/Revenue (Yahoo) | 35.40x | Multiple eleve |
| P/B (Yahoo) | 6.37 | Multiple eleve |
| Gross Margin (FMP) | 15.6% | Faible |
| Operating Margin (FMP) | -154.3% | Fortement negatif |
| Net Margin (FMP) | -186.6% | Fortement negatif |
| Debt/Equity (FMP) | 0.26 | Levier modere |
| Current Ratio (FMP) | 4.51 | Liquidite solide |
| Short Interest | 0.0866% | Aucun pari baissier structure |

**Filtre Qualite** : **2/6** (Hors perimetre) — stable.

**Regle** : Score <= 3/6 -> Score Valorisation plafonne a 5/10. L'agent recommandation applique **4.5/10**.

---

## Mise a jour sentiment / options / news

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-3.4%) — plus d'upside selon consensus |
| **Max Pain** | **$65.00** | Yahoo Finance | Ecart de **+47.9% au-dessus du spot** [CORRECTION]. Distorsion majeure liee expiration 22/05 (3 jours). Anomalie probable : strikes calls OTM concentres sur niveaux eleves |
| **Put/Call Ratio** | **0.64** | Yahoo Finance | Call-biased — biais haussier options |
| **Call OI %** | **61.1%** | Yahoo Finance | Fort biais haussier |
| Short Interest | 0.0866% | Yahoo Finance | Absence de squeeze setup |
| Social Sentiment | 0 mentions, 0.0 score | `data/social_sentiment_latest.json` | Aucune activite retail detectee |
| Event-Driven | Aucun | `data/events_latest.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (77 jours) | `data/upcoming_events_latest.json` | Est EPS -$0.60 a -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_latest.json` | Aucune news specifique au ticker |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immediat. Prochain catalyst structurel : earnings d'aout. La correction des donnees options (max pain $65, call OI 61%) revele un biais haussier latent non detecte au snapshot 10:00 UTC, mais sans catalyst fondamental sous-jacent cette distorsion est interpretee comme speculative liee a l'expiration 22/05.

---

## Scoring global (Agent Recommandation — 2026-05-19 13:00 UTC)

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
- **Agent Geo** : FLY non flagge -> pas de malus.
- **Agent Sector Rotation** : XLI (Industrials) sous-performant SPY sur 20j (-1.81%) et 60j (-3.39%), momentum_score 0.0 -> **headwind sectoriel** (-0.5 pt implicite).
- **Agent Social** : Pas d'activite retail -> neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0, divergence aligned -> pas d'ajustement.
- **Agent Event-Driven** : 0 evenement -> neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible -> pas d'ajustement.

---

## Revision des niveaux SL / TP

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $43.95 | Close 2026-05-19 13:00 UTC | +8.71% vs prior close |
| Stop-loss | $35.17 | Cours - 2xATR ($4.39) | ATR stable |
| Take-profit | $57.12 | Cours + 3xATR ($4.39) | ATR stable |
| Ratio R/R | 1.5:1 | Gain $13.17 / Perte $8.78 | Limite pour profil sans rentabilite |

Les niveaux sont inchanges. Le ratio 1.5:1 reste limite pour une action sans rentabilite demontree et Filtre Qualite faible (2/6).

---

## Conclusion — These confirmee, modifiee ou invalidee ?

**Verdict : These CONFIRMEE — consolidation du snapshot 13:00 UTC (2026-05-19).**

Le snapshot 13:00 UTC confirme que les donnees de cours, technique et fondamentale sont **strictement identiques** au snapshot 10:00 UTC. La seule variation significative est la **correction des donnees options** : Max Pain passe de $15.00 a $65.00 (+333%), put/call ratio a 0.64, call OI a 61.1%. Cette distorsion revele un biais call tres prononce pour l'expiration du 22/05, probablement lie a des positions speculatives sur strikes OTM eleves. Sans catalyst fondamental sous-jacent, cette anomalie options ne modifie pas le scoring global.

**Ce qui confirme la these :**
- Donnees cours, technique, fondamentale et scores strictement inchangées vs snapshot 10:00 UTC.
- Cours $43.95 stable post-gap, consolidant au-dessus de $43 — momentum intact.
- RSI 67.08, MM50 $32.72 — tendance haussiere technique confirmee.
- Aucune news structurante, guidance raise, ou evenement corporate detecte dans les agents events / geo / social.
- Scoring global en zone ATTENDRE (53.0 / 58.0 ajuste) — pas de bascule vers ACHETER ou EVITER.

**Ce qui maintient la prudence :**
- Filtre Qualite 2/6 (hors perimetre) — pas de quality compounding.
- Forward P/E -38.50, marges negatives, EV/Revenue 35x — valorisation incompatible avec les fondamentaux.
- Consensus PT $42.45 sous le spot (-3.4% upside) — plus de marge de securite analytique.
- Headwind sectoriel : XLI sous-performe le SPY (momentum_score 0.0).
- Volatilite elevee sans couverture fondamentale (ATR 10%, range intraday 12.3%).
- Volume accelere post-gap (1.57x moy.) — a surveiller pour signe de distribution.
- **Max Pain distordu a $65.00** (+47.9% au-dessus du spot) — anomalie options expiration 22/05, risque de microstructure eleve.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 77 jours) : Est EPS -$0.45 a -$0.60, Rev $0.1B. Toute surprise positive vs consensus negatif serait un catalyseur majeur.
2. **Expiration options 22/05** (3 jours) : surveillance post-expiration pour normalisation de la volatilite et du max pain.

**Risques :**
1. Rentabilite non demontree — operating margin -154%, net margin -187%.
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 35x, P/B 6.37x).
3. Cours au-dessus du consensus analystes — risque de retournement si les resultats ne suivent pas.
4. Comportement speculatif intraday (range 12.3%) sans catalyst — risque de correction rapide post-expiration options.
5. Anomalie Max Pain $65.00 — si les donnees sont confirmees, indique une convexite haussiere speculative extreme sans fondamental.

**Prochaine etape :**
- Maintenir **ATTENDRE**. Aucune position recommandee.
- Surveiller l'approche des earnings (aout) et toute amelioration des marges ou du FCF.
- Surveiller l'expiration options du 22/05 pour normalisation de la volatilite et du max pain.
- Si le cours casse la MM50 ($32.72) -> reviser la these a la baisse.
- Si un catalyst fondamental emerge (contrat, partnership, guidance raise) -> reevaluer le Score Catalyseur et le Filtre Qualite.
