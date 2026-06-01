# NOK — Mise à Jour Quotidienne (2026-06-01, Snapshot 17:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-06-01 | Données source : `data/latest.json` (snapshot 2026-06-01T17:00:01 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (2026-06-01 13:00 UTC)

| Indicateur | Snapshot 13:00 UTC | Snapshot 17:00 UTC | Variation | Signal |
|-----------|--------------------|--------------------|-----------|--------|
| Cours close | $14.84 | **$16.175** | **+9.0%** | 🔴 **Explosion haussière** |
| Change % vs previous close | −2.88% | **+9.0%** | **+11.88pp** | 🔴 **Inversion massive** |
| RSI 14j | 61.3 | **62.29** | +0.99 | → |
| ATR 14j | $1.01 | **$1.02** | +1.0% | → |
| Volume | 112,624,800 | **118,976,466** | +5.6% | → |
| Volume relatif | 0.96× | **1.03×** | +0.07× | 🟢 Au-dessus de la moyenne 20j |
| High intraday | $15.26 | **$16.25** | +6.5% | 🔴 Approche du 52w high |
| Low intraday | $14.53 | **$14.93** | +2.7% | 🟢 Support élevé, pas de retest |
| P/E (TTM Yahoo) | 92.75 | **101.09** | +9.0% | 🔴 Valorisation extrême |
| Forward P/E | 30.43 | **33.17** | +9.0% | 🔴 |
| Premium vs consensus $9.26 | +60.2% | **+74.7%** | +14.5pp | 🔴 Divergence maximale |
| MM 50j | $11.37 | **$11.52** | +1.3% | → |
| **Max pain options** | $13.50 | **$13.50** | — | → |
| **Put/Call ratio** | 0.46 | **0.46** | — | → |
| **Call OI** | 68.5% | **68.5%** | — | → |

**Changements significatifs détectés :**
- **🔴 Explosion haussière de +9.0%** en une séance, sans catalyseur identifiable dans `data/events_latest.json`, `data/upcoming_events_latest.json`, ni dans le flux news Yahoo. Le mouvement est totalement idiosyncratique.
- **🔴 Récupération technique totale** du support $15.47 (cassé ce matin à $14.53). Le cours a non seulement réintégré $15.47 mais a clôturé à $16.175, à 2.3% du 52-week high ($16.63). Le double gap haussier du 25–26/05 est désormais quasi-intégralement défendu.
- **🔴 Valorisation hors normes** : P/E Yahoo 101.09, forward P/E 33.17, cours +74.7% vs consensus $9.26. Chaque dollar de hausse creuse la divergence fondamentale.
- **🔴 Pin risk options extrême** : le cours ($16.175) est désormais **+19.9% au-dessus du max pain** ($13.50), contre +9.9% au snapshot 13:00 UTC. À 4 jours de l'expiration (vendredi 05/06), la pression de mean-reversion vers $13.50 s'intensifie mécaniquement.
- **🟢 Volume confirmé** : 119.0M (1.03× moyenne 20j), signalant une participation réelle et non un gap sur vide.
- **🟢 Low du jour $14.93** : aucun retest du plus bas matinal ($14.53). La structure de la bougie est haussière (open $15.07, close $16.175, proche du high).

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $16.175 | Yahoo Finance | +9.0% vs previous close ($14.84) |
| Open | $15.07 | Yahoo Finance | Gap haussier d'ouverture +1.55% |
| High intraday | $16.25 | Yahoo Finance | À 2.3% du 52w high ($16.63) |
| Low intraday | $14.93 | Yahoo Finance | Support supérieur au low du matin |
| Volume | 118,976,466 | Yahoo Finance | 1.03× moyenne 20j (116,012,413) |
| RSI 14j | 62.29 | Calcul agent | Zone neutre haute, pas de surachat |
| ATR 14j | $1.02 | Calcul agent | 6.31% du cours — trigger ATR_SPIKE actif |
| MM 50j | $11.52 | Calcul agent | Cours +40.5% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché — mouvement idiosyncratique |

**Niveaux clés (révisés) :**
- **Support immédiat :** $15.47 (ancien support cassé ce matin, désormais testé comme support/résistance) / $14.93 (low du jour)
- **Support structural :** $11.52 (MM 50j)
- **Résistance :** $16.25 (high du jour) / $16.63 (52-week high) / $17.87 (take-profit ATR)
- **Stop-loss ATR (2×) :** $14.14 ($16.175 − $2.04)
- **Take-profit ATR (3×) :** $19.23 ($16.175 + $3.06)
- **Ratio R/R :** 1.5

**Mise à jour options — inchangées mais risque aggravé :**
| Niveau | Valeur 13:00 UTC | Valeur 17:00 UTC | Interprétation |
|--------|------------------|------------------|----------------|
| Max pain | $13.50 | **$13.50** | → Valeur inchangée |
| Put/Call ratio | 0.46 | **0.46** | → Structure bullish (dominance calls) |
| Call OI % | 68.5% | **68.5%** | → Dominance call intacte |
| Expiration | 2026-06-05 | **2026-06-05** | 4 jours restants |

> **🔴 Pin risk extrême à l'expiration 05/06.** Le cours ($16.175) est désormais **+19.9% au-dessus du max pain** ($13.50), soit +10.0pp de plus qu'au snapshot 13:00 UTC (+9.9%). Historiquement, le max pain attire le cours à l'expiration. Avec 4 jours restants, les détenteurs de calls ITM (OI 68.5%) verront une forte pression vendeuse si le cours ne trouve pas de catalyseur pour justifier un settlement au-dessus de $16.00. La probabilité d'un retour vers $14.00–$13.50 d'ici vendredi est élevée en l'absence de news.

**Verdict timing :** Favorable structurellement (cours au-dessus de MM50, tendance haussière intacte), mais **défavorable à court terme** (pin risk extrême + proximité du 52w high + absence de catalyseur). Le mouvement de +9.0% en 4 heures sans explication est suspect et fragile. Le verdict est **favorable pour le momentum** mais **défavorable pour le timing d'entrée** (achat au sommet).

**Score Momentum :** 7.0/10 — inchangé dans `recommandations_latest.json`. Le momentum structurel est soutenu par le maintien au-dessus de la MM50 et le volume supérieur à la moyenne.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $90.30 B | Yahoo Finance |
| P/E (TTM Yahoo) | 101.09 | Yahoo Finance |
| Forward P/E (Yahoo) | 33.17 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 31.76 | Yahoo Finance |
| P/B (Yahoo) | 3.68 | Yahoo Finance |
| Dividend yield (Yahoo) | 1.10% | Yahoo Finance |

**Données opérationnelles FMP (FY 2025) :**
| Ratio | Valeur |
|-------|--------|
| Gross margin | 43.5% |
| Operating margin | 3.9% |
| Net margin | 3.3% |
| ROE | 3.1% |
| ROIC | 1.9% |
| Debt/Equity | 0.25 |
| Current ratio | 1.58 |
| Net debt/EBITDA | −0.11 (net cash) |

**Filtre Qualité (6 critères) :**
| Critère | Évaluation | Justification |
|---------|------------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ Non | Croissance anémique du top-line (mature 5G) |
| Profit CAGR 5 ans ≥ 20% | ❌ Non | Rentabilité historiquement faible |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.58, net cash position |
| FCF positif et croissant 5 ans | ⚠️ Partiel | FCF yield 4.9% mais trajectoire instable |
| Avantage compétitif (moat) | ⚠️ Partiel | Leader 5G historique mais part de marché sous pression |
| Industrie forte croissance (TAM ×5) | ❌ Non | TAM 5G mature, croissance à simple digit |
| **Score Qualité total** | **2.5/6** | 🔴 Hors périmètre (inchangé) |

**Note fondamentale :** Aucune donnée fondamentale nouvelle (pas de résultats, pas de guidance, pas de M&A). Le consensus inchangé à $9.26 sur 6 analystes maintient la divergence à **+74.7%** (vs +60.2% ce matin). Chaque point de hausse du cours creuse le déficit de valorisation. Aucun upgrade, downgrade ou révision d'estimations n'a été détecté.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +74.7% vs consensus, P/E 101.09, forward P/E 33.17 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision — silence total malgré la volatilité extrême |
| Nombre analysts actifs (mois) | 0 | FMP Stable API | Faible couverture, aucun upgrade massif |
| Put/Call ratio | 0.46 | Yahoo Finance | Structure bullish (dominance calls) |
| Max pain | $13.50 | Yahoo Finance | 🔴 Risque pin baissier extrême à l'expiration 05/06 |
| Call OI % | 68.5% | Yahoo Finance | Forte activité call — détenteurs ITM exposés au pin |
| Short Interest | 1.08% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiée dans le flux |

**Verdict Sentiment :** Neutre à légèrement bearish à court terme. La structure options reste **bullish historiquement** (put/call 0.46, call OI 68.5%) mais avec un **pin risk baissier extrême** ($13.50 vs cours $16.175, soit +19.9% de divergence). Les détenteurs de calls sont fortement ITM mais le max pain exerce une pression mécanique à la baisse à l'expiration (05/06). Le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement de +9.0% reste sans explication fondamentale. L'absence de news et d'événements corporate maintient le sentiment neutre, voire suspicieux face à un rally non justifié.

**Score Catalyseur :** 4.0/10 — inchangé dans `recommandations_latest.json`. Aucun catalyseur identifiable ; rally de +9.0% sans news/event ; earnings éloignés (52 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Unknown (régime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable |
| Valorisation | 3.5/10 | → | P/E 101.09, cours +74.7% vs consensus |
| Momentum | 7.0/10 | → | Maintien au-dessus MM50, volume confirmé, rally +9% |
| **Score Opportunité** | **4.5/10** | ↑ | (4.0×0.35) + (3.5×0.40) + (7.0×0.25) = 4.5 |
| **Score Global** | **45.5/100** | ↑ | Malus : Valorisation faible + pin risk extrême |
| **Score Global ajusté** | **50.5/100** | ↑ | Seuil ATTENDRE (50–59) franchi |

**Action recommandée :** **ATTENDRE** (seuil 50–59)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

**Note de scoring :** Le Score Global ajusté progresse de **49.2/100** (SURVEILLER, snapshot 13:00 UTC) à **50.5/100** (ATTENDRE, snapshot 17:00 UTC) dans `recommandations_latest.json`. Le franchissement du seuil 50 est entièrement dû au mouvement de cours (+9.0%) qui a mécaniquement rehaussé le Score Momentum et le Score Global. Cependant, l'action reste **ATTENDRE** — l'entrée est toujours exclue (seuil ACHETER = ≥60).

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (13:00 UTC) | Nouveau (17:00 UTC) | Justification |
|--------|--------------------|---------------------|---------------|
| Stop-loss | $12.82 | **$14.14** | Révisé — ATR 2× ($16.175 − $2.04) |
| Take-profit | $17.87 | **$19.23** | Révisé — ATR 3× ($16.175 + $3.06) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | −37.6% | **−42.7%** | Dégradé mécanique (cours plus haut) |
| Downside SL | −13.6% | **−12.6%** | Amélioré mécaniquement |

**⚠️ Attention :** Le cours ($16.175) est revenu au-dessus du support $15.47 et approche le 52w high ($16.63). Si le cours casse $16.25 en clôture avec volume, le test du 52w high ($16.63) devient probable à court terme. Inversement, si le cours clôture sous $15.47, le faux breakout haussier du jour sera confirmé et le risque de retour vers $14.14 (SL) puis $13.50 (max pain) augmente. Le **pin risk options ($13.50, expiration 05/06)** reste la menace principale à court terme.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −6.14%, RS60d −13.65%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (52 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **modifiée** — le snapshot 17:00 UTC révèle une explosion haussière de +9.0% qui inverse totalement la cassure du support $15.47 observée ce matin. La recommandation passe de **SURVEILLER** (Score Global ajusté 49.2/100) à **ATTENDRE** (Score Global ajusté 50.5/100). L'entrée reste exclue.

**Analyse :**
- **Technique :** Rally massif de +9.0% en 4 heures, portant le cours de $14.84 à $16.175. Le support $15.47 est non seulement récupéré mais le cours clôture à +4.5% au-dessus. Le high du jour ($16.25) est à 2.3% du 52w high ($16.63). RSI 62.29 (pas de surachat). ATR $1.02 (trigger ATR_SPIKE actif à 6.31%). Volume 119.0M (1.03×) — participation réelle. Le cours reste +40.5% au-dessus de la MM50 ($11.52) — tendance haussière structurelle renforcée.
- **Options :** Max pain $13.50, put/call 0.46, call OI 68.5%, expiration 2026-06-05 (dans 4 jours). Le cours +19.9% au-dessus du max pain crée un **pin risk baissier extrême** à l'expiration. La structure call-dominated est bullish historiquement mais la divergence cours/max pain est dangereuse.
- **Volume :** 119.0M (1.03×) — rally confirmé par le volume, signalant une participation institutionnelle ou algorithmique réelle.
- **Fondamentaux :** Aucune amélioration. P/E Yahoo 101.09, forward P/E 33.17. Consensus inchangé $9.26. Divergence prix/valeur à +74.7%.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news. Le rally de +9.0% est non justifié fondamentalement.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d −6.14%). Le mouvement de NOK reste totalement idiosyncratique.

**Ce qui a changé (13:00 UTC → 17:00 UTC) :**
- **Cours :** $14.84 → **$16.175** — 🔴 +9.0% en 4 heures
- **Change % :** −2.88% → **+9.0%** — 🔴 Inversion de +11.88pp
- **P/E Yahoo :** 92.75 → **101.09** — 🔴 Dépassé 100×
- **Premium consensus :** +60.2% → **+74.7%** — 🔴 Divergence maximale
- **Volume relatif :** 0.96× → **1.03×** — 🟢 Confirmé
- **High intraday :** $15.26 → **$16.25** — 🔴 Approche 52w high
- **Pin risk :** +9.9% au-dessus du max pain → **+19.9%** — 🔴 Extrême
- **Score Global ajusté :** 49.2/100 → **50.5/100** — → Passage SURVEILLER → ATTENDRE
- **SL/TP :** $12.82/$17.87 → **$14.14/$19.23** — Révisés mécaniquement

**Ce qui n'a pas changé :**
- **Consensus :** $9.26 (6 analysts) — silence total
- **Qualité :** 2.5/6 hors périmètre
- **Catalyseur :** 4.0/10 — aucun identifié
- **Options :** Max pain $13.50, put/call 0.46, call OI 68.5%
- **Event-Driven :** Aucun événement corporate
- **Sectoriel :** XLC bottom 3

**Recommandation révisée :**
- **Action :** **ATTENDRE** (Score Global ajusté 50.5/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $14.14 (2×ATR)
- **Take-profit :** $19.23 (3×ATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scénarios forward (révisés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 15% | Breakout $16.63 + catalyseur non capturé | $18.00–$19.00 |
| Central | 45% | Consolidation $15.50–$16.50 sans catalyseur | Range |
| Pessimiste | 40% | Pin options $13.50 + retour MM50 $11.52 | $12.00–$14.00 |

**⚠️ Risque principal :** Pin options à $13.50 avec expiration dans 4 jours (05/06). Le cours +19.9% au-dessus du max pain crée une pression baissière technique extrême à court terme. Si le cours clôture sous $15.47, le faux breakout haussier sera confirmé et l'accélération vendeuse vers $14.14 (SL) puis $13.50 devient probable. Le rally de +9.0% est non justifié fondamentalement et donc fragile. Aucun catalyseur ne soutient le niveau au-delà du momentum technique.

**Prochains points de contrôle :**
- Franchissement du 52w high à $16.63 (ou rejet)
- Franchissement sous $15.47 en clôture (confirmation faux breakout)
- **Expiration options 2026-06-05** (vendredi) — comportement autour du max pain $13.50
- Earnings Q2 FY2026 au **2026-07-23** (dans **52 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Catalyseur éventuel expliquant le rally de +9% (M&A, contrat, upgrade)

---

*Données sources : `data/latest.json` (2026-06-01T17:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
