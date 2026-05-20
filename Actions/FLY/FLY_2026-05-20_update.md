# FLY — Mise à Jour (2026-05-20 10:00 UTC)

> Source : `data/2026-05-20.json` (10:00 UTC, snapshot quotidien) + `data/recommandations_2026-05-20.json` + agents quant / geo / sector / social / FX / events / upcoming.
> **Validation data** : 4 erreurs globales (VRT schema, AST/AXA/CYTMOMX fetch failed) — aucune affectant FLY. Pas de [CRITICAL]. Données FLY considérées fiables.

---

## Résumé des changements depuis l'analyse précédente (2026-05-19 21:00 UTC)

| Métrique | 2026-05-19 21:00 UTC | 2026-05-20 10:00 UTC | Variation |
|----------|----------------------|----------------------|-----------|
| Cours close | $42.57 (snapshot) | **$42.57** | stable en close |
| Previous close réel | — | **$43.95** | révélation données |
| Change % vs prior close | -3.14% | **-3.14%** | stable |
| RSI 14j | 65.57 | **65.57** | stable |
| MM 50j | $33.16 | **$33.16** | stable |
| ATR 14j | $4.53 | **$4.53** | stable |
| Volume jour | 5,818,313 | **5,825,800** | stable (0.92× moy.) |
| Market Cap (Yahoo) | $6.82B | **$6.82B** | stable |
| Forward P/E | -37.29 | **-37.29** | stable |
| EV/Revenue (Yahoo) | 35.40× | **34.20×** | -1.2 pt |
| P/B (Yahoo) | 6.17 | **6.17** | stable |
| Consensus PT (FMP) | $42.45 (11 analysts) | **$42.45 (11 analysts)** | stable |
| Options — Max Pain | $65.00 | **$15.00** | **-76.9%** |
| Options — Put/Call | 0.64 | **null** | données manquantes |
| Options — Call OI % | 61.1% | **null** | données manquantes |
| Score Opportunité | 5.0/10 | **5.0/10** | stable |
| Score Valorisation | 4.5/10 | **4.5/10** | stable |
| Score Catalyseur | 5.0/10 | **5.0/10** | stable |
| Score Momentum | 6.0/10 | **6.0/10** | stable |
| Score Global | 50.5 | **50.5** | stable |
| Score Global Ajusté | 55.5 | **55.5** | stable |

**Verdict :** Le snapshot du 2026-05-20 confirme la **stabilisation du cours à $42.57** après le repli de -3.14% observé hier. Les fondamentaux sont strictement inchangés. La seule variation notable concerne les **données options** : le max pain est passé de $65.00 à $15.00, et le put/call ratio ainsi que le call OI % sont désormais `null`. Cette discontinuité est probablement liée à la **proximité de l'expiration du 22/05** (2 jours) et à un épuisement des données OI en fin de cycle. [DONNÉES PARTIELLES — à traiter avec prudence]. Le social sentiment émet un signal `EXTREME_BEARISH` (valeur 0.0) sans mention réelle — artefact de données.

---

## Mise à jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $42.57 | Repli -3.14% vs prior close $43.95 — consolidation post-gap |
| Open | $42.945 | Gap down de -2.29% vs $43.95 |
| High | $43.56 | Test de la résistance intraday, rejet |
| Low | $39.11 | Support intraday à $39.11 — pas de rupture en close |
| RSI 14j | 65.57 | Zone haussière, retrait du surachat — stable |
| MM 50j | $33.16 | Cours supérieur de **+28.4%**, tendance haussière intacte |
| MM 200j | N/A | Donnée indisponible |
| Volume | 5,825,800 | 0.92× moy. 20j — volume normal |
| ATR 14j | $4.53 | Relatif 10.6% — volatilité élevée persistante |
| Range jour | $39.11–$43.56 | Amplitude **10.1%** en séance, identique à hier |
| Support 1 | $33.16 (MM50) | Support dynamique — rupture = révision baissière |
| Support 2 | $16.00 (52W Low) | — |
| Résistance 1 | $43.56 (High du jour) | Testé, non confirmé en close |
| Résistance 2 | $47.71 (High 2026-05-18) | — |

**Timing verdict :** **Favorable mais risque accru** — tendance haussière intacte (cours > MM50 +28.4%), RSI en zone haussière. Le repli de -3.14% est une consolidation technique sans cassure de support majeur. La proximité de l'expiration options (22/05, 2 jours) maintient le risque de microstructure élevé. Le range intraday extrême (10.1%) reflète un comportement spéculatif accentué par l'épuisement du gamma.

---

## Mise à jour fondamentale

Données croisées Yahoo / FMP (annual FY 2025) — **strictement inchangées vs snapshot 2026-05-19** :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $6.82B | Donnée de base |
| Market Cap (FMP) | $3.40B | [DIVERGENCE -50%] — persistante, à vérifier |
| Forward P/E | -37.29 | Pas de rentabilité nette attendue |
| EV/EBITDA (Yahoo) | -28.13 | EBITDA négatif |
| EV/Revenue (Yahoo) | 34.20× | Multiple élevé, en légère baisse de 35.40× |
| P/B (Yahoo) | 6.17 | Multiple élevé |
| P/B (FMP) | 2.86 | [DIVERGENCE] — si FMP est correct, multiple moins distordu |
| Gross Margin (FMP) | 15.6% | Faible |
| Operating Margin (FMP) | -154.3% | Fortement négatif |
| Net Margin (FMP) | -186.6% | Fortement négatif |
| Debt/Equity (FMP) | 0.26 | Levier modéré |
| Current Ratio (FMP) | 4.51 | Liquidité solide |
| Short Interest | 8.66% | Aucun pari baissier structuré |

**Filtre Qualité** : **2/6** (Hors périmètre) — stable.

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10. L'agent recommandation applique **4.5/10**.

**Note sur la divergence Yahoo/FMP** : La divergence persistante (Market Cap -50%, P/B -54%) n'est pas résolue. Aucun nouvel élément ne permet de trancher. Les données Yahoo restent la référence primaire pour le cours et la valorisation boursière ; les données FMP sont citées comme données comptables. [DONNÉES PARTIELLES — vérification requise avant prochaine analyse.]

---

## Mise à jour sentiment / options / news

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-0.3%) — aligné, upside analytique nul |
| Max Pain | $15.00 | Yahoo Finance | **Anomalie majeure** : écart de -64.8% sous le spot. Passage de $65.00 à $15.00 en 24h. Probablement artefact lié à l'expiration 22/05 (2 jours) et à un épuisement de l'OI concentrée. [DONNÉES PARTIELLES] |
| Put/Call Ratio | null | Yahoo Finance | Données manquantes — expiration imminente |
| Call OI % | null | Yahoo Finance | Données manquantes — expiration imminente |
| Short Interest | 8.66% | Yahoo Finance | Absence de squeeze setup |
| Social Sentiment | EXTREME_BEARISH (0.0) | `data/social_sentiment_2026-05-20.json` | Signal artéfact (0 mention, score 0.0) — pas d'activité retail détectée |
| Event-Driven | Aucun | `data/events_2026-05-20.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (76 jours) | `data/upcoming_events_2026-05-20.json` | Est EPS -$0.60 à -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_2026-05-20.json` | Aucune news spécifique au ticker |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immédiat. Le prochain catalyst structurel reste les earnings d'août. L'anomalie options (max pain $15.00, données OI manquantes) est considérée comme un artefact de données lié à l'expiration imminente (2 jours) et ne modifie pas le scoring.

---

## Scoring global (Agent Recommandation — 2026-05-20 10:00 UTC)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 6.0/10 | 25% | 1.50 |
| **Score Opportunité** | **5.0/10** | | |
| Malus/Bonus | +5.5 pts | | (pas de malus accounting/geo/FX majeur) |
| **Score Global** | **50.5** | | |
| **Score Global Ajusté** | **55.5** | | |

**Action** : **ATTENDRE**
**Direction** : Neutre
**Timing** : Favorable mais risque accru
**Horizon** : —

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (insuffisant) → pas d'ajustement.
- **Agent Geo** : FLY non flaggué → pas de malus.
- **Agent Sector Rotation** : XLI (Industrials) sous-performant SPY sur 20j (RS -5.79%) et 60j (RS -11.03%), momentum_score 0.0 → **headwind sectoriel persistant** (-0.5 pt implicite).
- **Agent Social** : Signal artéfact EXTREME_BEARISH (0 mention) → neutre, pas d'ajustement.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0, divergence aligned → pas d'ajustement.
- **Agent Event-Driven** : 0 événement → neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible → pas d'ajustement.

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $42.57 | Close 2026-05-20 10:00 UTC | -3.14% vs prior close $43.95 |
| Stop-loss | $33.51 | Cours - 2×ATR ($4.53) | Inchangé — support MM50 $33.16 en ligne de mire |
| Take-profit | $56.16 | Cours + 3×ATR ($4.53) | Inchangé |
| Ratio R/R | 1.5:1 | Gain $13.59 / Perte $9.06 | Limite pour profil sans rentabilité |

Les niveaux sont inchangés car le cours de clôture est stable à $42.57. Le ratio 1.5:1 reste limité pour une action sans rentabilité démontrée et Filtre Qualité faible (2/6).

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : Thèse CONFIRMÉE — consolidation technique stable, données options anormales à ignorer.**

Le snapshot du 2026-05-20 confirme que le cours se stabilise à **$42.57** après le repli de -3.14%. Aucune cassure de support majeur (MM50 $33.16 intacte, low intraday $39.11 > MM50). Les fondamentaux sont strictement inchangés et défavorables. Le scoring global reste en zone **ATTENDRE** (50.5 / 55.5 ajusté).

**Ce qui confirme la thèse :**
- Aucune news structurante, guidance cut, guidance raise, ou événement corporate détecté dans les agents events / geo / social / FX.
- Cours $42.57 reste bien au-dessus de la MM50 ($33.16, +28.4%) — tendance haussière technique intacte.
- RSI 65.57 en zone haussière, retrait du surachat sans inversion.
- Short interest 8.66% — absence de pari baissier structuré.
- Consensus PT $42.45 aligné sur le spot — pas de signal de downgrade massif.
- Volume stable (0.92× moy.) — l'intérêt acheteur n'a pas déserté.
- Scoring global en zone ATTENDRE (50.5 / 55.5 ajusté) — pas de bascule vers ACHETER ou ÉVITER.

**Ce qui maintient la prudence :**
- Filtre Qualité 2/6 (hors périmètre) — pas de quality compounding.
- Forward P/E -37.29, marges négatives, EV/Revenue 34.2× — valorisation incompatible avec les fondamentaux.
- Headwind sectoriel : XLI sous-performe le SPY (RS 20j -5.79%, momentum_score 0.0).
- Volatilité élevée sans couverture fondamentale (ATR 10.6%, range intraday 10.1%).
- Anomalie options : max pain $15.00 (données suspectes, expiration 22/05), put/call et call OI % manquants — risque de microstructure élevé.
- Divergence Yahoo/FMP sur Market Cap ($6.82B vs $3.40B) et P/B (6.17 vs 2.86) — [DONNÉES PARTIELLES] à clarifier.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 76 jours) : Est EPS -$0.45 à -$0.60, Rev $0.1B. Toute surprise positive vs consensus négatif serait un catalyseur majeur.
2. **Expiration options 22/05** (2 jours) : surveillance post-expiration pour normalisation de la volatilité et des données options (max pain, OI).

**Risques :**
1. Rentabilité non démontrée — operating margin -154%, net margin -187%.
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 34×, P/B 6.17×).
3. Cours au-dessus du consensus analystes — risque de retournement si les résultats ne suivent pas.
4. Comportement spéculatif intraday (range 10.1%) sans catalyst — risque de correction rapide post-expiration options.
5. Anomalie Max Pain $15.00 — probable artefact données lié expiration, à vérifier post-22/05.
6. Divergence Yahoo/FMP sur capitalisation et P/B — risque d'erreur de données dans le scoring de valorisation.

**Prochaine étape :**
- Maintenir **ATTENDRE**. Aucune position recommandée.
- Surveiller l'expiration options du 22/05 pour normalisation des données et de la volatilité.
- Surveiller le volume demain : si le volume casse sous 4M (0.6× moy.) et le cours casse $39 (low du jour), réviser le timing à "Défavorable".
- Si le cours casse la MM50 ($33.16) → réviser la thèse à la baisse.
- Si un catalyst fondamental émerge (contrat, partnership, guidance raise) → réévaluer le Score Catalyseur et le Filtre Qualité.
- **Vérifier la divergence Yahoo/FMP** sur Market Cap et P/B avant la prochaine analyse.
