# NOK — Mise à Jour Quotidienne (2026-06-01, Snapshot 13:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-06-01 | Données source : `data/latest.json` (snapshot 2026-06-01T13:00:08 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (2026-06-01 10:00 UTC)

| Indicateur | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Variation | Signal |
|-----------|--------------------|--------------------|-----------|--------|
| Cours close | $14.84 | **$14.84** | — | ✅ Confirmé |
| Change % vs previous close | −2.88% | **−2.88%** | — | ✅ Confirmé |
| RSI 14j | 61.3 | **61.3** | — | ✅ Confirmé |
| ATR 14j | $1.01 | **$1.01** | — | ✅ Confirmé |
| Volume | 112,624,800 | **112,624,800** | — | ✅ Confirmé |
| Volume relatif | 0.96× | **0.96×** | — | ✅ Confirmé |
| High intraday | $15.26 | **$15.26** | — | ✅ Confirmé |
| Low intraday | $14.53 | **$14.53** | — | ✅ Confirmé |
| P/E (TTM Yahoo) | 92.75 | **92.75** | — | ✅ Confirmé |
| Forward P/E | 30.43 | **30.43** | — | ✅ Confirmé |
| Premium vs consensus $9.26 | +60.2% | **+60.2%** | — | ✅ Confirmé |
| Consensus analystes (FMP) | $9.26 (6) | **$9.26 (6)** | — | ✅ Confirmé |
| MM 50j | $11.37 | **$11.37** | — | ✅ Confirmé |
| **Max pain options** | $2.00 (anomalie) | **$13.50** | **+$11.50** | 🟢 **Données restaurées** |
| **Put/Call ratio** | None | **0.46** | — | 🟢 **Données restaurées** |
| **Call OI** | None | **68.5%** | — | 🟢 **Données restaurées** |

**Changements significatifs détectés :**
- **🟢 Restauration des données options Yahoo** : le snapshot 13:00 UTC corrige l'anomalie détectée à 10:00 UTC (max pain $2.00 aberrant). Les options sont désormais exploitables : max pain $13.50, put/call 0.46, call OI 68.5%, expiration 2026-06-05 (dans 4 jours). C'est le **seul changement significatif** vs le snapshot 10:00 UTC.
- **🔴 Risque pin options inversé** : le cours ($14.84) est désormais **+9.9% au-dessus du max pain** ($13.50), alors qu'il était −1.9% sous le max pain opérationnel du 27/05 ($16.00). La structure a basculé d'un pin haussier à un pin baissier. Avec l'expiration dans 4 jours (vendredi 05/06), le risque de mean-reversion vers $13.50 est tangible.
- **Aucun catalyseur fondamental** identifié dans `data/events_latest.json` (vide pour NOK).
- Données prix, volume, technique et fondamentales **strictement inchangées** entre les deux snapshots du 01/06.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $14.84 | Yahoo Finance | −2.88% vs previous close ($15.28) |
| Open | $15.18 | Yahoo Finance | Gap baissier d'ouverture |
| High intraday | $15.26 | Yahoo Finance | Rejet net sous le 52w high ($16.63) |
| Low intraday | $14.53 | Yahoo Finance | **Casse du support $15.47** confirmée |
| Volume | 112,624,800 | Yahoo Finance | 0.96× moyenne 20j (117,493,570) — volume normal |
| RSI 14j | 61.3 | Calcul agent | Zone neutre haute, sortie de surachat confirmée |
| ATR 14j | $1.01 | Calcul agent | 6.81% du cours — trigger ATR_SPIKE actif (seuil 5.0%) |
| MM 50j | $11.37 | Calcul agent | Cours +30.5% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché — mouvement idiosyncratique |

**Niveaux clés (inchangés) :**
- **Support immédiat :** $14.53 (low du jour) / $14.18 (close estimé du 24/05, base d'avant-gap)
- **Support structural :** $11.37 (MM 50j)
- **Résistance :** $15.26 (high du jour) / $15.47 (ancien support, désormais résistance) / $16.63 (52-week high)
- **Stop-loss ATR (2×) :** $12.82 ($14.84 − $2.02)
- **Take-profit ATR (3×) :** $17.87 ($14.84 + $3.03)
- **Ratio R/R :** 1.5

**Mise à jour options — restauration complète :**
| Niveau | Valeur 10:00 UTC | Valeur 13:00 UTC | Interprétation |
|--------|------------------|------------------|----------------|
| Max pain | $2.00 (anomalie) | **$13.50** | ✅ Valeur réaliste restaurée |
| Put/Call ratio | None | **0.46** | ✅ Structure bullish (plus de calls que de puts) |
| Call OI % | None | **68.5%** | ✅ Dominance call claire |
| Expiration | 2026-06-05 | **2026-06-05** | 4 jours restants |

> **⚠️ Risque pin inversé à l'expiration 05/06.** Le cours ($14.84) est +9.9% au-dessus du max pain ($13.50). Historiquement, au 27/05, le cours était −1.9% sous le max pain ($16.00). La structure a basculé : les détenteurs de calls (OI 68.5%) sont ITM mais le max pain attire le cours vers $13.50. Avec seulement 4 jours avant expiration, le risque de retour vers $13.50 est élevé si le cours ne trouve pas de catalyseur. Le put/call 0.46 indique une forte activité call, ce qui peut amplifier la pression vendeuse post-expiration (déclenchement de profits sur calls).

**Verdict timing :** Neutre à défavorable. La cassure du support $15.47 est confirmée sans révision. La correction se déroule sur volume normal (0.96×), sans panique, et le RSI à 61.3 n'est pas en zone de survente. Le cours reste +30.5% au-dessus de la MM 50j, ce qui maintient une tendance haussière structurelle à moyen terme. Cependant, le **risque pin options ($13.50)** ajoute une pression baissière à court terme (jusqu'au 05/06). Le verdict est **défavorable à court terme** (pin risk + cassure support) mais **neutre à moyen terme** (tendance MM50 intacte).

**Score Momentum :** 6.5/10 — inchangé dans `recommandations_latest.json`. Le maintien au-dessus de la MM 50j et la normalisation du volume soutiennent le momentum structurel, malgré la cassure du support $15.47.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $82.84 B | Yahoo Finance |
| P/E (TTM Yahoo) | 92.75 | Yahoo Finance |
| Forward P/E (Yahoo) | 30.43 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 31.76 | Yahoo Finance |
| P/B (Yahoo) | 3.37 | Yahoo Finance |
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

**Note fondamentale :** Aucune donnée fondamentale nouvelle depuis le snapshot 10:00 UTC. Le consensus inchangé à $9.26 sur 6 analystes maintient la divergence à +60.2%. Aucun upgrade, downgrade ou révision d'estimations n'a été détecté.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +60.2% vs consensus, P/E 92.75, forward P/E 30.43 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision détectée — silence total malgré la volatilité |
| Nombre analysts actifs (mois) | 0 | FMP Stable API | Faible couverture, aucun upgrade massif |
| Put/Call ratio | **0.46** | Yahoo Finance | ✅ **Restauré** — structure bullish (dominance calls) |
| Max pain | **$13.50** | Yahoo Finance | ✅ **Restauré** — risque pin baissier à l'expiration 05/06 |
| Call OI % | **68.5%** | Yahoo Finance | ✅ **Restauré** — forte activité call |
| Short Interest | 1.08% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiée dans le flux |

**Verdict Sentiment :** Neutre à légèrement bearish à court terme. La restauration des données options révèle une structure **bullish historiquement** (put/call 0.46, call OI 68.5%) mais avec un **pin risk baissier** ($13.50 vs cours $14.84). Les détenteurs de calls sont ITM mais le max pain attire le cours vers le bas à l'expiration (05/06). Le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement reste sans explication fondamentale. L'absence de news et d'événements corporate maintient le sentiment neutre.

**Score Catalyseur :** 4.0/10 — inchangé dans `recommandations_latest.json`. Aucun catalyseur identifiable ; double gap suivi d'une correction non expliquée par news/event ; earnings éloignés (52 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Unknown (régime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable |
| Valorisation | 3.5/10 | → | P/E 92.75, cours +60.2% vs consensus |
| Momentum | 6.5/10 | → | Maintien au-dessus MM50, volume normalisé |
| **Score Opportunité** | **4.4/10** | → | (4.0×0.35) + (3.5×0.40) + (6.5×0.25) = 4.4 |
| **Score Global** | **44.2/100** | → | Malus : Valorisation faible + momentum érodé mais structurel |
| **Score Global ajusté** | **49.2/100** | → | — |

**Action recommandée :** **SURVEILLER** (seuil 35–49)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

**Note de scoring :** Le Score Global ajusté reste **49.2/100** dans `recommandations_latest.json`. Le ticker reste fermement dans la zone SURVEILLER. L'entrée reste exclue.

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (10:00 UTC) | Nouveau (13:00 UTC) | Justification |
|--------|--------------------|---------------------|---------------|
| Stop-loss | $12.82 | **$12.82** | Inchange — ATR 2× ($14.84 − $2.02) |
| Take-profit | $17.87 | **$17.87** | Inchange — ATR 3× ($14.84 + $3.03) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | −37.6% | **−37.6%** | Inchange |
| Downside SL | −13.6% | **−13.6%** | Inchange |

**⚠️ Attention :** Le cours ($14.84) reste sous le support $15.47 (base du gap du 25/05) avec un low à $14.53. Si le cours franchit $14.50 en clôture, le risque d'accélération vendeuse vers $14.00 puis $13.00 (zone du max pain $13.50) augmente significativement. Le SL à $12.82 reste la barrière de sortie principale. Le **pin risk options ($13.50, expiration 05/06)** ajoute une pression baissière à court terme.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −5.97%, RS60d −13.01%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (52 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **confirmée** — le snapshot 13:00 UTC confirme intégralement les données du snapshot 10:00 UTC avec **restauration des données options** comme seule mutation. La recommandation reste **SURVEILLER** (Score Global ajusté 49.2/100).

**Analyse :**
- **Technique :** Données strictement inchangées (close $14.84, RSI 61.3, ATR $1.01, volume 112.6M, 0.96×). La cassure du support $15.47 est confirmée. Le double gap haussier du 25–26/05 reste quasi-intégralement invalidé. Le cours reste +30.5% au-dessus de la MM50 ($11.37), maintenant la tendance haussière structurelle.
- **Options (restaurées) :** Max pain $13.50, put/call 0.46, call OI 68.5%, expiration 2026-06-05 (dans 4 jours). La structure call-dominated est bullish historiquement mais le cours +9.9% au-dessus du max pain crée un **pin risk baissier** à l'expiration. Le risque de retour vers $13.50 est tangible si le cours ne trouve pas de catalyseur d'ici vendredi.
- **Volume :** 112.6M (0.96×) — correction ordonnée sans panique ni distribution massive.
- **Fondamentaux :** Aucune amélioration. P/E Yahoo 92.75, forward P/E 30.43. Consensus inchangé $9.26. Divergence prix/valeur à +60.2%.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d −5.97%, RS60d −13.01%). Le mouvement de NOK reste totalement idiosyncratique et fragile.

**Ce qui a changé (10:00 UTC → 13:00 UTC) :**
- **Options data :** Max pain $2.00 (anomalie) → **$13.50** — ✅ données restaurées
- **Put/Call ratio :** None → **0.46** — ✅ données restaurées
- **Call OI :** None → **68.5%** — ✅ données restaurées
- **Risque pin :** Basculé de "anomalie" à **pin baissier $13.50** (cours +9.9% au-dessus)

**Ce qui n'a pas changé :**
- **Toutes les données prix/volume/technique/fondamentales** — strictement identiques entre les deux snapshots
- **Consensus :** $9.26 (6 analysts) — silence total
- **Qualité :** 2.5/6 hors périmètre
- **Catalyseur :** 4.0/10 — aucun identifié
- **Score Global ajusté :** 49.2/100 — SURVEILLER maintenu
- **SL/TP :** $12.82/$17.87 — inchangés
- **Event-Driven :** Aucun événement corporate

**Recommandation révisée :**
- **Action :** **SURVEILLER** (Score Global ajusté 49.2/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $12.82 (2×ATR)
- **Take-profit :** $17.87 (3×ATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scénarios forward (inchangés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 15% | Catalyseur non capturé + rebond technique sur MM50 | $16.00–$17.00 |
| Central | 50% | Consolidation $14.50–$15.50 sans catalyseur | Range |
| Pessimiste | 35% | Cassure $14.50 en clôture + pin options $13.50 → retour MM50 $11.37 | $12.00–$14.00 |

**⚠️ Risque principal :** Pin options à $13.50 avec expiration dans 4 jours (05/06). Le cours +9.9% au-dessus du max pain crée une pression baissière technique à court terme. Si le cours clôture sous $14.50, l'accélération vendeuse vers $13.50 puis $12.82 (SL) devient probable. Le double gap haussier est quasi-comblé. Aucun catalyseur ne soutient le niveau.

**Prochains points de contrôle :**
- Franchissement technique du SL à $12.82
- Franchissement sous $14.50 en clôture (risque d'accélération)
- **Expiration options 2026-06-05** (vendredi) — comportement autour du max pain $13.50
- Earnings Q2 FY2026 au **2026-07-23** (dans **52 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Catalyseur éventuel expliquant le double gap (M&A, contrat, upgrade)

---

*Données sources : `data/latest.json` (2026-06-01T13:00:08 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
