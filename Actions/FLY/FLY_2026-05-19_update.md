# FLY — Mise a Jour (2026-05-19 21:00 UTC)

> Source : `data/2026-05-19.json` (21:00 UTC, close de seance) + `data/recommandations_2026-05-19.json` + agents quant / geo / sector / social / FX / events / upcoming.

---

## Resume des changements depuis l'analyse precedente (2026-05-19 17:00 UTC)

| Metrique | 2026-05-19 17:00 UTC | 2026-05-19 21:00 UTC (close) | Variation |
|----------|----------------------|------------------------------|-----------|
| Cours close | $42.32 | **$42.57** | **+0.59%** |
| Change % vs prior close | -3.71% | **-3.14%** | +0.57 pt |
| RSI 14j | 65.01 | **65.57** | +0.56 |
| MM 50j | $33.16 | **$33.16** | stable |
| ATR 14j | $4.53 | **$4.53** | stable |
| Volume jour | 2,903,276 | **5,818,313** | **+100.4%** |
| Volume vs moy. 20j | 0.47x | **0.92x** | **correction majeure** |
| Market Cap (Yahoo) | $6.78B | **$6.82B** | +0.6% |
| Forward P/E | -37.07 | **-37.29** | stable |
| P/B (Yahoo) | 6.13 | **6.17** | stable |
| P/B (FMP) | 2.86 | **2.86** | stable |
| Consensus PT (FMP) | $42.45 (11 analysts) | $42.45 (11 analysts) | stable |
| Options — Max Pain | $65.00 | **$65.00** | stable |
| Options — Put/Call | 0.64 | **0.64** | stable |
| Options — Call OI % | 61.1% | **61.1%** | stable |
| Score Opportunite | 5.0/10 | **5.0/10** | stable |
| Score Valorisation | 4.5/10 | **4.5/10** | stable |
| Score Catalyseur | 5.0/10 | **5.0/10** | stable |
| Score Momentum | 6.0/10 | **6.0/10** | stable |
| Score Global | 50.5 | **50.5** | stable |
| Score Global Ajuste | 55.5 | **55.5** | stable |

**Verdict : Le snapshot 21:00 UTC corrige l'interpretation du volume.** Le snapshot 17:00 UTC affichait un volume de 2.9M (0.47x moy. 20j) qui etait un **snapshot partiel** de milieu de seance. Le volume final de la seance est **5.8M** (0.92x moy. 20j), en ligne avec la normale. Le cours a legerement remonte en fin de seance de $42.32 a $42.57 (+0.59%). Le repli global de -3.14% sur la seance reste une **consolidation technique post-gap** (+8.71% veille) sans catalyst fondamental. Le scoring global reste en zone ATTENDRE (50.5 / 55.5 ajuste).

---

## Mise a jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 65.57 | Haussier, retrait du surachat — reste au-dessus de 60 |
| MM 50j | $33.16 | Cours superieur de **+28.4%**, tendance haussiere intacte |
| MM 200j | N/A | Donnee indisponible |
| Volume | 5,818,313 | 0.92x moy. 20j — **volume normal en fin de seance**, correction du snapshot partiel |
| ATR 14j | $4.53 | Relatif 10.6% — volatilite elevee, comportement speculatif |
| Range jour | $39.12–$43.56 | Amplitude **10.1%** en seance, consolidation apres gap |
| Support 1 | $33.16 (MM50) | Support dynamique — rupture = revision baissiere |
| Support 2 | $16.00 (52W Low) | — |
| Resistance 1 | $43.56 (High du jour) | Teste en seance, non confirme en close |
| Resistance 2 | $47.71 (High 2026-05-18) | — |

**Timing verdict :** **Favorable mais risque accru** — tendance haussiere intacte (cours > MM50 +28.4%), RSI en zone haussiere. Le repli de -3.14% sur la seance est une consolidation normale apres le gap de +8.71%. La proximite de l'expiration options (22/05, 3 jours) maintient le risque de microstructure eleve. La correction du volume (0.92x vs 0.47x errone) invalide le signal de "desertion post-gap" ; l'interet acheteur reste present.

---

## Mise a jour fondamentale

Donnees croisees Yahoo / FMP (annual FY 2025) — **strictement inchangees vs snapshot 17:00 UTC**, avec divergence Yahoo/FMP persistante :

| Metrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $6.82B | Donnee de base |
| Market Cap (FMP) | $3.40B | [DIVERGENCE -50%] — persistante, a verifier |
| Forward P/E | -37.29 | Pas de rentabilite nette attendue |
| EV/EBITDA (Yahoo) | -29.12 | EBITDA negatif |
| EV/Revenue (Yahoo) | 35.40x | Multiple eleve |
| P/B (Yahoo) | 6.17 | Multiple eleve |
| P/B (FMP) | 2.86 | [DIVERGENCE] — si FMP est correct, le multiple est moins distordu |
| Gross Margin (FMP) | 15.6% | Faible |
| Operating Margin (FMP) | -154.3% | Fortement negatif |
| Net Margin (FMP) | -186.6% | Fortement negatif |
| Debt/Equity (FMP) | 0.26 | Levier modere |
| Current Ratio (FMP) | 4.51 | Liquidite solide |
| Short Interest | 0.0866% | Aucun pari baissier structure |

**Filtre Qualite** : **2/6** (Hors perimetre) — stable.

**Regle** : Score <= 3/6 -> Score Valorisation plafonne a 5/10. L'agent recommandation applique **4.5/10**.

**Note sur la divergence Yahoo/FMP :** Le snapshot 21:00 UTC confirme la divergence persistante : Market Cap FMP $3.40B contre $6.82B Yahoo (-50%) et P/B FMP 2.86 contre 6.17 Yahoo. En l'absence de verification, les donnees Yahoo sont utilisees comme reference primaire pour le cours et la valorisation boursiere ; les donnees FMP sont citees comme donnees comptables. [DONNEES PARTIELLES — verification requise avant prochaine analyse.]

---

## Mise a jour sentiment / options / news

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-0.3%) — presque aligne, upside analytique nul |
| Max Pain | $65.00 | Yahoo Finance | Ecart de **+52.7% au-dessus du spot**. Distorsion majeure liee expiration 22/05 (3 jours). Anomalie : strikes calls OTM concentres sur niveaux eleves |
| Put/Call Ratio | 0.64 | Yahoo Finance | Call-biased — biais haussier options |
| Call OI % | 61.1% | Yahoo Finance | Fort biais haussier |
| Short Interest | 0.0866% | Yahoo Finance | Absence de squeeze setup |
| Social Sentiment | Non trouve | `data/social_sentiment_2026-05-19.json` | Aucune activite retail detectee |
| Event-Driven | Aucun | `data/events_2026-05-19.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (77 jours) | `data/upcoming_events_2026-05-19.json` | Est EPS -$0.60 a -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_2026-05-19.json` | Aucune news specifique au ticker |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immediat. Le prochain catalyst structurel reste les earnings d'aout. La distorsion options (max pain $65, call OI 61%) n'a pas evolue ; elle revele un biais haussier latent speculatif sans fondamental sous-jacent, amplifie par l'expiration imminente (3 jours).

---

## Scoring global (Agent Recommandation — 2026-05-19 21:00 UTC)

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
- **Agent Sector Rotation** : XLI (Industrials) sous-performant SPY sur 20j (RS -5.79%) et 60j (RS -11.03%), momentum_score 0.0 -> **headwind sectoriel persistant** (-0.5 pt implicite).
- **Agent Social** : Pas d'activite retail -> neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0, divergence aligned -> pas d'ajustement.
- **Agent Event-Driven** : 0 evenement -> neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible -> pas d'ajustement.

---

## Revision des niveaux SL / TP

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $42.57 | Close 2026-05-19 21:00 UTC | -3.14% vs prior close |
| Stop-loss | $33.51 | Cours - 2xATR ($4.53) | Ajuste a la hausse (+$0.25) vs 17:00 UTC |
| Take-profit | $56.16 | Cours + 3xATR ($4.53) | Ajuste a la hausse (+$0.37) vs 17:00 UTC |
| Ratio R/R | 1.5:1 | Gain $13.59 / Perte $9.06 | Limite pour profil sans rentabilite |

Les niveaux sont revises a la marge du fait de la remontee du cours en fin de seance. Le ratio 1.5:1 reste limite pour une action sans rentabilite demontree et Filtre Qualite faible (2/6).

---

## Conclusion — These confirmee, modifiee ou invalidee ?

**Verdict : These CONFIRMEE — consolidation technique post-gap, correction du volume.**

Le snapshot 21:00 UTC confirme que le repli de -3.14% sur la seance est une **consolidation technique normale** apres le gap de +8.71% de la veille. La donnee majeure corrigee est le volume : le snapshot 17:00 UTC affichait un volume partiel de 2.9M (0.47x moy.) qui creat l'illusion d'une desertion acheteur. Le volume final de 5.8M (0.92x moy. 20j) montre que l'interet est reste present en fin de seance. Les donnees fondamentales sont strictement inchangées. Le scoring global reste en zone ATTENDRE (50.5 / 55.5 ajuste).

**Ce qui confirme la these :**
- Aucune news structurante, guidance cut, guidance raise, ou evenement corporate detecte dans les agents events / geo / social / FX.
- Cours $42.57 reste bien au-dessus de la MM50 ($33.16, +28.4%) — tendance haussiere technique intacte.
- RSI 65.57 en zone haussiere, retrait du surachat sans inversion.
- Short interest 0.0866% — absence de pari baissier structure.
- Consensus PT $42.45 aligne sur le spot — pas de signal de downgrade massif.
- Volume final corrige (0.92x moy.) — l'interet acheteur n'a pas deserte.
- Scoring global en zone ATTENDRE (50.5 / 55.5 ajuste) — pas de bascule vers ACHETER ou EVITER.

**Ce qui maintient la prudence :**
- Filtre Qualite 2/6 (hors perimetre) — pas de quality compounding.
- Forward P/E -37.29, marges negatives, EV/Revenue 35x — valorisation incompatible avec les fondamentaux.
- Headwind sectoriel : XLI sous-performe le SPY (RS 20j -5.79%, momentum_score 0.0).
- Volatilite elevee sans couverture fondamentale (ATR 10.6%, range intraday 10.1%).
- Max Pain distordu a $65.00 (+52.7% au-dessus du spot) — anomalie options expiration 22/05, risque de microstructure eleve.
- Divergence Yahoo/FMP sur Market Cap ($6.82B vs $3.40B) et P/B (6.17 vs 2.86) — [DONNEES PARTIELLES] a clarifier.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 77 jours) : Est EPS -$0.45 a -$0.60, Rev $0.1B. Toute surprise positive vs consensus negatif serait un catalyseur majeur.
2. **Expiration options 22/05** (3 jours) : surveillance post-expiration pour normalisation de la volatilite, du max pain et du volume.

**Risques :**
1. Rentabilite non demontree — operating margin -154%, net margin -187%.
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 35x, P/B 6.17x).
3. Cours au-dessus du consensus analystes — risque de retournement si les resultats ne suivent pas.
4. Comportement speculatif intraday (range 10.1%) sans catalyst — risque de correction rapide post-expiration options.
5. Anomalie Max Pain $65.00 — convexite haussiere speculative extreme sans fondamental.
6. Divergence Yahoo/FMP sur capitalisation et P/B — risque d'erreur de donnees dans le scoring de valorisation.

**Prochaine etape :**
- Maintenir **ATTENDRE**. Aucune position recommandee.
- Surveiller l'expiration options du 22/05 pour normalisation de la volatilite et du max pain.
- Surveiller le volume demain : si le volume casse sous 4M (0.6x moy.) et le cours casse $39 (low du jour), reviser le timing a "Defavorable".
- Si le cours casse la MM50 ($33.16) -> reviser la these a la baisse.
- Si un catalyst fondamental emerge (contrat, partnership, guidance raise) -> reevaluer le Score Catalyseur et le Filtre Qualite.
- **Verifier la divergence Yahoo/FMP** sur Market Cap et P/B avant la prochaine analyse.
