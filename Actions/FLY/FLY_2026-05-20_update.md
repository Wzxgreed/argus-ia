# FLY — Mise a Jour (2026-05-20 13:00 UTC)

> Source : `data/2026-05-20.json` (13:00 UTC, snapshot quotidien) + `data/recommandations_2026-05-20.json` + agents quant / geo / sector / social / FX / events / upcoming.
> **Validation data** : 4 erreurs globales (VRT schema, AST/AXA/CYTMOMX fetch failed) — aucune affectant FLY. Pas de [CRITICAL]. Donnees FLY considerees fiables.

---

## Resume des changements depuis l'analyse precedente (2026-05-20 10:00 UTC)

| Metrique | 2026-05-20 10:00 UTC | 2026-05-20 13:00 UTC | Variation |
|----------|----------------------|----------------------|-----------|
| Cours close | $42.57 | **$42.57** | stable |
| Previous close | $43.95 | **$43.95** | stable |
| Change % | -3.14% | **-3.14%** | stable |
| RSI 14j | 65.57 | **65.57** | stable |
| MM 50j | $33.16 | **$33.16** | stable |
| ATR 14j | $4.53 | **$4.53** | stable |
| Volume jour | 5,825,800 | **5,825,800** | stable (0.92× moy.) |
| Market Cap (Yahoo) | $6.82B | **$6.82B** | stable |
| Forward P/E | -37.29 | **-37.29** | stable |
| EV/Revenue (Yahoo) | 34.20× | **34.20×** | stable |
| P/B (Yahoo) | 6.17 | **6.17** | stable |
| Consensus PT (FMP) | $42.45 (11 analysts) | **$42.45 (11 analysts)** | stable |
| **Options — Max Pain** | $15.00 (anomalie) | **$65.00** | **+333% normalisation** |
| **Options — Put/Call** | null | **0.66** | **Donnees restaurees** |
| **Options — Call OI %** | null | **60.4%** | **Donnees restaurees** |
| Score Opportunite | 5.0/10 | **5.0/10** | stable |
| Score Valorisation | 4.5/10 | **4.5/10** | stable |
| Score Catalyseur | 5.0/10 | **5.0/10** | stable |
| Score Momentum | 6.0/10 | **6.0/10** | stable |
| Score Global | 50.5 | **50.5** | stable |
| Score Global Ajuste | 55.5 | **55.5** | stable |

**Verdict :** Le snapshot 13:00 UTC confirme la **stabilisation du cours a $42.57**. Aucune variation technique ou fondamentale. La seule evolution concerne la **correction d'anomalie options** : le max pain redevient **$65.00** (vs $15.00 artefact dans le snapshot 10:00 UTC), le put/call ratio redevient **0.66** et le call OI % **60.4%**. Cette normalisation confirme que l'anomalie observee a 10:00 UTC etait bien un **artefact de microstructure lie a l'expiration du 22/05** (2 jours) et a un epuisement transitoire de l'OI. Le social sentiment reste un signal artéfact `EXTREME_BEARISH` (0 mention) — a ignorer.

---

## Mise a jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $42.57 | Repli -3.14% vs prior close $43.95 — consolidation post-gap |
| Open | $42.945 | Gap down de -2.29% vs $43.95 |
| High | $43.56 | Test de la resistance intraday, rejet |
| Low | $39.11 | Support intraday a $39.11 — pas de rupture en close |
| RSI 14j | 65.57 | Zone haussiere, retrait du surachat — stable |
| MM 50j | $33.16 | Cours superieur de **+28.4%**, tendance haussiere intacte |
| MM 200j | N/A | Donnee indisponible |
| Volume | 5,825,800 | 0.92× moy. 20j — volume normal |
| ATR 14j | $4.53 | Relatif 10.6% — volatilite elevee persistante |
| Range jour | $39.11–$43.56 | Amplitude **10.1%** en seance |
| Support 1 | $33.16 (MM50) | Support dynamique — rupture = revision baissiere |
| Support 2 | $16.00 (52W Low) | — |
| Resistance 1 | $43.56 (High du jour) | Teste, non confirme en close |
| Resistance 2 | $47.71 (High 2026-05-18) | — |

**Timing verdict :** **Favorable mais risque accru** — tendance haussiere intacte (cours > MM50 +28.4%), RSI en zone haussiere. Le repli de -3.14% est une consolidation technique sans cassure de support majeur. La proximite de l'expiration options (22/05, 2 jours) maintient le risque de microstructure eleve, mais la normalisation des donnees OI (max pain $65.00, put/call 0.66) reduit l'incertitude par rapport au snapshot 10:00 UTC. Le range intraday extreme (10.1%) reflete un comportement speculatif accentue par l'epuisement du gamma.

---

## Mise a jour fondamentale

Donnees croisees Yahoo / FMP (annual FY 2025) — **strictement inchangees vs snapshot 2026-05-20 10:00 UTC** :

| Metrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $6.82B | Donnee de base |
| Market Cap (FMP) | $3.40B | [DIVERGENCE -50%] — persistante, a verifier |
| Forward P/E | -37.29 | Pas de rentabilite nette attendue |
| EV/EBITDA (Yahoo) | -28.13 | EBITDA negatif |
| EV/Revenue (Yahoo) | 34.20× | Multiple eleve |
| P/B (Yahoo) | 6.17 | Multiple eleve |
| P/B (FMP) | 2.86 | [DIVERGENCE] — si FMP est correct, multiple moins distordu |
| Gross Margin (FMP) | 15.6% | Faible |
| Operating Margin (FMP) | -154.3% | Fortement negatif |
| Net Margin (FMP) | -186.6% | Fortement negatif |
| Debt/Equity (FMP) | 0.26 | Levier modere |
| Current Ratio (FMP) | 4.51 | Liquidite solide |
| Short Interest | 8.66% | Aucun pari baissier structure |
| FMP Consensus PT | $42.45 (11 analysts) | Aligne sur le spot |

**Filtre Qualite** : **2/6** (Hors perimetre) — stable.

**Regle** : Score ≤ 3/6 → Score Valorisation plafonne a 5/10. L'agent recommandation applique **4.5/10**.

**Note sur la divergence Yahoo/FMP** : La divergence persistante (Market Cap -50%, P/B -54%) n'est pas resolue. Aucun nouvel element ne permet de trancher. Les donnees Yahoo restent la reference primaire pour le cours et la valorisation boursiere ; les donnees FMP sont citees comme donnees comptables. [DONNEES PARTIELLES — verification requise avant prochaine analyse.]

---

## Mise a jour sentiment / options / news

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-0.3%) — aligne, upside analytique nul |
| Max Pain | $65.00 | Yahoo Finance | **Normalisation** : retour a $65.00 apres artefact $15.00 a 10:00 UTC. Ecart +52.7% au-dessus du spot. Donnees credibles restaurees |
| Put/Call Ratio | 0.66 | Yahoo Finance | Restaure (null a 10:00 UTC). Preference call legerement elevee |
| Call OI % | 60.4% | Yahoo Finance | Restaure (null a 10:00 UTC). Biais call confirme |
| Short Interest | 8.66% | Yahoo Finance | Absence de squeeze setup |
| Social Sentiment | EXTREME_BEARISH (0.0) | `data/social_sentiment_2026-05-20.json` | Signal artéfact (0 mention, score 0.0) — pas d'activite retail detectee |
| Event-Driven | Aucun | `data/events_2026-05-20.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (76 jours) | `data/upcoming_events_2026-05-20.json` | Est EPS -$0.60 a -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_2026-05-20.json` | Aucune news specifique au ticker |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immediat. Le prochain catalyst structurel reste les earnings d'aout. L'anomalie options est resolue ; le max pain a $65.00 reflete une structure options normale pre-expiration. Pas d'impact sur le scoring.

---

## Scoring global (Agent Recommandation — 2026-05-20 13:00 UTC)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
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
- **Agent Quant** : Signaux non significatifs (insuffisant) → pas d'ajustement.
- **Agent Geo** : FLY non flagge → pas de malus.
- **Agent Sector Rotation** : XLI (Industrials) sous-performant SPY sur 20j (RS -5.79%) et 60j (RS -11.03%), momentum_score 0.0 → **headwind sectoriel persistant** (-0.5 pt implicite).
- **Agent Social** : Signal artéfact EXTREME_BEARISH (0 mention) → neutre, pas d'ajustement.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0, divergence aligned → pas d'ajustement.
- **Agent Event-Driven** : 0 evenement → neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible → pas d'ajustement.

---

## Revision des niveaux SL / TP

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $42.57 | Close 2026-05-20 13:00 UTC | -3.14% vs prior close $43.95 |
| Stop-loss | $33.51 | Cours - 2×ATR ($4.53) | Inchange — support MM50 $33.16 en ligne de mire |
| Take-profit | $56.16 | Cours + 3×ATR ($4.53) | Inchange |
| Ratio R/R | 1.5:1 | Gain $13.59 / Perte $9.06 | Limite pour profil sans rentabilite |

Les niveaux sont inchanges car le cours de cloture est stable a $42.57. Le ratio 1.5:1 reste limite pour une action sans rentabilite demontree et Filtre Qualite faible (2/6).

---

## Conclusion — These confirmee, modifiee ou invalidee ?

**Verdict : These CONFIRMEE — consolidation technique stable, anomalie options RESOLUE.**

Le snapshot 13:00 UTC confirme que le cours se stabilise a **$42.57** apres le repli de -3.14%. Aucune cassure de support majeur (MM50 $33.16 intacte, low intraday $39.11 > MM50). Les fondamentaux sont strictement inchanges et defavorables. Le scoring global reste en zone **ATTENDRE** (50.5 / 55.5 ajuste).

**Ce qui confirme la these :**
- **Normalisation des donnees options** : le max pain redevient $65.00, le put/call 0.66 et le call OI 60.4% confirment que l'anomalie observee a 10:00 UTC etait un artefact transitoire. La microstructure redevient interpretable.
- Aucune news structurante, guidance cut, guidance raise, ou evenement corporate detecte dans les agents events / geo / social / FX.
- Cours $42.57 reste bien au-dessus de la MM50 ($33.16, +28.4%) — tendance haussiere technique intacte.
- RSI 65.57 en zone haussiere, retrait du surachat sans inversion.
- Short interest 8.66% — absence de pari baissier structure.
- Consensus PT $42.45 aligne sur le spot — pas de signal de downgrade massif.
- Volume stable (0.92× moy.) — l'interet acheteur n'a pas deserte.
- Scoring global en zone ATTENDRE (50.5 / 55.5 ajuste) — pas de bascule vers ACHETER ou EVITER.

**Ce qui maintient la prudence :**
- Filtre Qualite 2/6 (hors perimetre) — pas de quality compounding.
- Forward P/E -37.29, marges negatives, EV/Revenue 34.2× — valorisation incompatible avec les fondamentaux.
- Headwind sectoriel : XLI sous-performe le SPY (RS 20j -5.79%, momentum_score 0.0).
- Volatilite elevee sans couverture fondamentale (ATR 10.6%, range intraday 10.1%).
- Proximite expiration options 22/05 (2 jours) — risque de microstructure persistant malgre la normalisation des donnees.
- Divergence Yahoo/FMP sur Market Cap ($6.82B vs $3.40B) et P/B (6.17 vs 2.86) — [DONNEES PARTIELLES] a clarifier.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 76 jours) : Est EPS -$0.45 a -$0.60, Rev $0.1B. Toute surprise positive vs consensus negatif serait un catalyseur majeur.
2. **Expiration options 22/05** (2 jours) : surveillance post-expiration pour confirmation de la normalisation de la volatilite.

**Risques :**
1. Rentabilite non demontree — operating margin -154%, net margin -187%.
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 34×, P/B 6.17×).
3. Cours au-dessus du consensus analystes — risque de retournement si les resultats ne suivent pas.
4. Comportement speculatif intraday (range 10.1%) sans catalyst — risque de correction rapide post-expiration options.
5. Divergence Yahoo/FMP sur capitalisation et P/B — risque d'erreur de donnees dans le scoring de valorisation.

**Prochaine etape :**
- Maintenir **ATTENDRE**. Aucune position recommandee.
- Surveiller l'expiration options du 22/05 pour confirmation de la normalisation de la volatilite.
- Surveiller le volume demain : si le volume casse sous 4M (0.6× moy.) et le cours casse $39 (low du jour), reviser le timing a "Defavorable".
- Si le cours casse la MM50 ($33.16) → reviser la these a la baisse.
- Si un catalyst fondamental emerge (contrat, partnership, guidance raise) → reevaluer le Score Catalyseur et le Filtre Qualite.
- **Verifier la divergence Yahoo/FMP** sur Market Cap et P/B avant la prochaine analyse.
