# FLY — Mise a Jour (2026-05-19 17:00 UTC)

> Source : `data/latest.json` (2026-05-19 17:00 UTC) + `data/recommandations_latest.json` + agents quant / geo / sector / social / FX / events / upcoming.

---

## Resume des changements depuis l'analyse precedente (2026-05-19 13:00 UTC)

| Metrique | 2026-05-19 13:00 UTC | 2026-05-19 17:00 UTC | Variation |
|----------|----------------------|----------------------|-----------|
| Cours close | $43.95 | **$42.32** | **-3.71%** |
| RSI 14j | 67.08 | **65.01** | -2.07 |
| MM 50j | $32.72 | **$33.16** | +$0.44 |
| ATR 14j | $4.39 | **$4.53** | +$0.14 |
| Volume jour | 9,827,800 | **2,903,276** | **-70.5%** (0.47x moy. 20j) |
| Change % vs prior close | +8.71% | **-3.71%** | — |
| Forward P/E | -38.50 | **-37.07** | stable |
| Market Cap (Yahoo) | $7.04B | **$6.78B** | -3.7% |
| Market Cap (FMP) | Non renseigne | **$3.40B** | [DIVERGENCE] |
| P/B (Yahoo) | 6.37 | **6.13** | stable |
| P/B (FMP) | Non renseigne | **2.86** | [DIVERGENCE] |
| Consensus PT (FMP) | $42.45 (11 analysts) | $42.45 (11 analysts) | stable |
| Options — Max Pain | $65.00 | **$65.00** | stable |
| Options — Put/Call | 0.64 | **0.64** | stable |
| Options — Call OI % | 61.1% | **61.1%** | stable |
| Score Opportunite | 5.3/10 | **5.0/10** | -0.3 pt |
| Score Valorisation | 4.5/10 | **4.5/10** | stable |
| Score Catalyseur | 5.0/10 | **5.0/10** | stable |
| Score Momentum | 7.0/10 | **6.0/10** | -1.0 pt |
| Score Global | 53.0 | **50.5** | -2.5 pts |
| Score Global Ajuste | 58.0 | **55.5** | -2.5 pts |

**Verdict : Le cours recule de -3.71% sur volume en effondrement (-70.5% vs snapshot 13:00 UTC, 0.47x moyenne 20j).** Aucune news structurante ni catalyseur fondamental. Le repli est interprete comme une consolidation technique post-gap (+8.71% veille) dans un contexte de biais call speculatif (expiration 22/05 dans 3 jours). Le scoring global reste en zone ATTENDRE (50.5 / 55.5 ajuste).

---

## Mise a jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 65.01 | Haussier, retrait du surachat — reste au-dessus de 60 |
| MM 50j | $33.16 | Cours superieur de **+27.6%**, tendance haussiere intacte |
| MM 200j | N/A | Donnee indisponible |
| Volume | 2,903,276 | 0.47x moy. 20j — **desertion post-gap**, retrait de l'interet acheteur |
| ATR 14j | $4.53 | Relatif 10.7% — volatilite elevee, comportement speculatif |
| Range jour | $39.12–$42.945 | Amplitude **9.1%** en seance, consolidation sous le high 13:00 UTC ($47.71) |
| Support 1 | $33.16 (MM50) | Support dynamique — rupture = revision baissiere |
| Support 2 | $16.00 (52W Low) | — |
| Resistance 1 | $42.945 (High du jour) | Non confirme en close |
| Resistance 2 | $47.71 (High 13:00 UTC) | — |

**Timing verdict :** **Favorable mais risque accru** — tendance haussiere intacte (cours > MM50 +27.6%), RSI en zone haussiere. Cependant, le repli de -3.71% sur volume en effondrement (0.47x moy.) est un signal de retrait de l'interet acheteur apres le gap. La proximite de l'expiration options (22/05, 3 jours) maintient le risque de microstructure eleve. La consolidation au-dessus de $42 apres le gap est un support technique a court terme.

---

## Mise a jour fondamentale

Donnees croisees Yahoo / FMP (annual FY 2025) — **stable vs snapshot 2026-05-19 13:00 UTC**, avec divergence Yahoo/FMP significative sur la capitalisation :

| Metrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $6.78B | Donnee de base |
| Market Cap (FMP) | $3.40B | [DIVERGENCE -50%] — a verifier, possible data lag FMP |
| Forward P/E | -37.07 | Pas de rentabilite nette attendue |
| EV/EBITDA (Yahoo) | -29.12 | EBITDA negatif |
| EV/Revenue (Yahoo) | 35.40x | Multiple eleve |
| P/B (Yahoo) | 6.13 | Multiple eleve |
| P/B (FMP) | 2.86 | [DIVERGENCE] — si FMP est correct, le multiple est moins distordu |
| Gross Margin (FMP) | 15.6% | Faible |
| Operating Margin (FMP) | -154.3% | Fortement negatif |
| Net Margin (FMP) | -186.6% | Fortement negatif |
| Debt/Equity (FMP) | 0.26 | Levier modere |
| Current Ratio (FMP) | 4.51 | Liquidite solide |
| Short Interest | 0.0866% | Aucun pari baissier structure |

**Filtre Qualite** : **2/6** (Hors perimetre) — stable.

**Regle** : Score <= 3/6 -> Score Valorisation plafonne a 5/10. L'agent recommandation applique **4.5/10**.

**Note sur la divergence Yahoo/FMP :** Le snapshot 17:00 UTC fait apparaitre un Market Cap FMP de $3.40B contre $6.78B Yahoo (-50%) et un P/B FMP de 2.86 contre 6.13 Yahoo. Cette divergence est significative et non expliquee. En l'absence de verification, les donnees Yahoo sont utilisees comme reference primaire pour le cours et la valorisation boursiere ; les donnees FMP sont citees comme donnees comptables. [DONNEES PARTIELLES — verification requise]

---

## Mise a jour sentiment / options / news

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-0.2%) — presque aligne, upside analytique nul |
| Max Pain | $65.00 | Yahoo Finance | Ecart de **+53.6% au-dessus du spot**. Distorsion majeure liee expiration 22/05 (3 jours). Anomalie : strikes calls OTM concentres sur niveaux eleves |
| Put/Call Ratio | 0.64 | Yahoo Finance | Call-biased — biais haussier options |
| Call OI % | 61.1% | Yahoo Finance | Fort biais haussier |
| Short Interest | 0.0866% | Yahoo Finance | Absence de squeeze setup |
| Social Sentiment | 0 mentions, 0.0 score | `data/social_sentiment_latest.json` | Aucune activite retail detectee |
| Event-Driven | Aucun | `data/events_latest.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (77 jours) | `data/upcoming_events_latest.json` | Est EPS -$0.60 a -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_latest.json` | Aucune news specifique au ticker |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immediat. Le prochain catalyst structurel reste les earnings d'aout. La distorsion options (max pain $65, call OI 61%) n'a pas evolue depuis 13:00 UTC ; elle revele un biais haussier latent speculative sans fondamental sous-jacent, amplifie par l'expiration imminente.

---

## Scoring global (Agent Recommandation — 2026-05-19 17:00 UTC)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 6.0/10 | 25% | 1.50 |
| **Score Opportunite** | **5.0/10** | | |
| Malus/Bonus | +5.5 pts | | (pas de malus accounting/geo/FX majeur) |
| **Score Global** | **50.5** | | |
| **Score Global Ajuste** | **55.5** | | |

**Action** : **ATTENDRE**
**Direction** : Neutre
**Timing** : Favorable mais risque accru
**Horizon** : —

**Ajustements agents complementaires :**
- **Agent Quant** : Signaux non significatifs (insuffisant) -> pas d'ajustement.
- **Agent Geo** : FLY non flagge -> pas de malus.
- **Agent Sector Rotation** : XLI (Industrials) sous-performant SPY sur 20j et 60j, momentum_score faible -> **headwind sectoriel** (-0.5 pt implicite).
- **Agent Social** : Pas d'activite retail -> neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0, divergence aligned -> pas d'ajustement.
- **Agent Event-Driven** : 0 evenement -> neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible -> pas d'ajustement.

---

## Revision des niveaux SL / TP

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $42.32 | Close 2026-05-19 17:00 UTC | -3.71% vs prior close |
| Stop-loss | $33.26 | Cours - 2xATR ($4.53) | Ajuste a la hausse (+$0.14) vs 13:00 UTC |
| Take-profit | $55.91 | Cours + 3xATR ($4.53) | Ajuste a la baisse (-$1.21) vs 13:00 UTC |
| Ratio R/R | 1.5:1 | Gain $13.59 / Perte $9.06 | Limite pour profil sans rentabilite |

Les niveaux sont revises a la marge du fait de la baisse du cours et de la hausse de l'ATR. Le ratio 1.5:1 reste limite pour une action sans rentabilite demontree et Filtre Qualite faible (2/6).

---

## Conclusion — These confirmee, modifiee ou invalidee ?

**Verdict : These CONFIRMEE avec legere degradation du momentum — consolidation technique post-gap.**

Le snapshot 17:00 UTC confirme un repli de -3.71% sur volume en effondrement (0.47x moy. 20j). Ce repli est interprete comme une **consolidation technique normale** apres le gap de +8.71% de la veille, sans catalyst fondamental negatif. Les donnees fondamentales sont strictement inchangées. Le scoring global reste en zone ATTENDRE (50.5 / 55.5 ajuste), avec une legere degradation du momentum (6.0/10 vs 7.0/10) due au repli du cours et a la desertion du volume.

**Ce qui confirme la these :**
- Aucune news structurante, guidance cut, guidance raise, ou evenement corporate detecte dans les agents events / geo / social / FX.
- Cours $42.32 reste bien au-dessus de la MM50 ($33.16, +27.6%) — tendance haussiere technique intacte.
- RSI 65.01 en zone haussiere, retrait du surachat sans inversion.
- Short interest 0.0866% — absence de pari baissier structure.
- Consensus PT $42.45 aligne sur le spot — pas de signal de downgrade massif.
- Scoring global en zone ATTENDRE (50.5 / 55.5 ajuste) — pas de bascule vers ACHETER ou EVITER.

**Ce qui maintient la prudence :**
- Filtre Qualite 2/6 (hors perimetre) — pas de quality compounding.
- Forward P/E -37.07, marges negatives, EV/Revenue 35x — valorisation incompatible avec les fondamentaux.
- Volume en effondrement (0.47x moy. 20j) — retrait de l'interet acheteur, a surveiller pour signe de distribution.
- Headwind sectoriel : XLI sous-performe le SPY (momentum_score faible).
- Volatilite elevee sans couverture fondamentale (ATR 10.7%, range intraday 9.1%).
- Max Pain distordu a $65.00 (+53.6% au-dessus du spot) — anomalie options expiration 22/05, risque de microstructure eleve.
- Divergence Yahoo/FMP sur Market Cap ($6.78B vs $3.40B) et P/B (6.13 vs 2.86) — [DONNEES PARTIELLES] a clarifier.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 77 jours) : Est EPS -$0.45 a -$0.60, Rev $0.1B. Toute surprise positive vs consensus negatif serait un catalyseur majeur.
2. **Expiration options 22/05** (3 jours) : surveillance post-expiration pour normalisation de la volatilite, du max pain et du volume.

**Risques :**
1. Rentabilite non demontree — operating margin -154%, net margin -187%.
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 35x, P/B 6.13x).
3. Cours au-dessus du consensus analystes — risque de retournement si les resultats ne suivent pas.
4. Comportement speculatif intraday (range 9.1%) sans catalyst — risque de correction rapide post-expiration options.
5. Anomalie Max Pain $65.00 — convexite haussiere speculative extreme sans fondamental.
6. Divergence Yahoo/FMP sur capitalisation et P/B — risque d'erreur de donnees dans le scoring de valorisation.

**Prochaine etape :**
- Maintenir **ATTENDRE**. Aucune position recommandee.
- Surveiller le volume demain : si le volume reste faible sous 3M et le cours casse $39 (low du jour), reviser le timing a "Defavorable".
- Surveiller l'expiration options du 22/05 pour normalisation de la volatilite et du max pain.
- Si le cours casse la MM50 ($33.16) -> reviser la these a la baisse.
- Si un catalyst fondamental emerge (contrat, partnership, guidance raise) -> reevaluer le Score Catalyseur et le Filtre Qualite.
- **Verifier la divergence Yahoo/FMP** sur Market Cap et P/B avant la prochaine analyse.
