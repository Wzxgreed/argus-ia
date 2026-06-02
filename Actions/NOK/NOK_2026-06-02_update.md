# NOK — Mise à Jour Quotidienne (2026-06-02, Snapshot 17:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-06-02 | Données source : `data/latest.json` (snapshot 2026-06-02T17:00:09 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (Snapshot 13:00 UTC 02/06)

| Indicateur | Snapshot 13:00 UTC (02/06) | Snapshot 17:00 UTC (02/06) | Variation | Signal |
|-----------|---------------------------|---------------------------|-----------|--------|
| Cours close | $16.25 | **$16.835** | **+3.60%** | → Rally intraday confirmé |
| RSI 14j | 62.59 | **70.17** | **+7.58** | → 🔴 Franchissement zone surachat (≥70) |
| ATR 14j | $1.04 | **$1.02** | −1.9% | → Stable |
| Volume | 171,815,100 | **98,881,235** | **−42.5%** | → Normalisation sous moyenne 20j (0.84×) |
| High intraday | $16.52 | **$17.11** | **+3.6%** | → 🔴 **New 52-week high** |
| Low intraday | $14.93 | **$16.45** | +10.2% | → Support remonté, range rétréci |
| P/E (TTM Yahoo) | 101.56 | **105.22** | +3.6% | → Valorisation encore étirée |
| Forward P/E | 33.32 | **34.52** | +3.6% | → Détérioration |
| Premium vs consensus $9.26 | +75.5% | **+81.8%** | +6.3 pp | → Divergence aggravée |
| MM 50j | $11.53 | **$11.70** | +1.5% | → Tendance haussière intacte |
| **Max pain options** | $13.50 | **$13.50** | — | → Inchangé |
| **Put/Call ratio** | 0.45 | **0.45** | — | → Structure call-dominated stable |
| **Call OI** | 69.1% | **69.1%** | — | → Forte activité call stable |
| Score Global ajusté (fichier JSON) | 50.5/100 (ATTENDRE) | **31.8/100 (ÉVITER)** | −18.7 pts | → 🔴 **Dégradation de catégorie** |
| Score Opportunité (fichier JSON) | 4.5/10 | **4.2/10** | −0.3 pt | → Dégradation marginale |
| Score Momentum (fichier JSON) | 7.0/10 | **5.5/10** | −1.5 pt | → Pénalisé par RSI surachat + volume en décroissance |

**Changements significatifs détectés :**
- **→ Cours +3.6% en séance**, portant le rally à **+9.6% vs previous close** ($15.37 implicite). Le cours a atteint un **nouveau 52-week high à $17.11**.
- **→ 🔴 RSI 70.17 : franchissement de la zone de surachat** (≥70) pour la première fois depuis le début du suivi. C'est un signal technique de vigilance.
- **→ Volume en chute libre −42.5%** : de 171.8M (1.45× moyenne 20j) à 98.9M (0.84× moyenne 20j). La participation s'effondre malgré le nouveau high — divergence baissière volume/prix classique.
- **→ Valorisation encore étirée** : P/E Yahoo 105.22, forward P/E 34.52, premium consensus +81.8% (vs +75.5% au snapshot 13h).
- **→ 🔴 Révision catégorielle dans `recommandations_latest.json`** : passage de **ATTENDRE** (50.5/100) à **ÉVITER** (31.8/100). La raison principale : le momentum a été révisé à la baisse (5.5/10 vs 7.0/10) en raison du franchissement RSI 70 et de la contraction volume, tandis que la valorisation reste défavorable (3.5/10) et le catalyseur absent (4.0/10). Le malus de valorisation s'est aggravé avec le nouveau high.
- **→ Options inchangées** : max pain $13.50, put/call 0.45, call OI 69.1%, expiration 2026-06-05 (**demain**). Le pin risk devient encore plus extrême : le cours +24.7% au-dessus du max pain (vs +20.4% au snapshot 13h).

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $16.835 | Yahoo Finance | +3.6% vs snapshot 13h, +9.6% vs previous close |
| Open | $16.56 | Yahoo Finance | Gap haussier d'ouverture confirmé |
| High intraday | $17.11 | Yahoo Finance | 🔴 **New 52-week high** — résistance historique cassée |
| Low intraday | $16.45 | Yahoo Finance | Support remonté, pas de retest des lows du 13h |
| Volume | 98,881,235 | Yahoo Finance | **0.84× moyenne 20j** — normalisation sous moyenne |
| RSI 14j | 70.17 | Calcul agent | 🔴 **Zone de surachat** franchie (≥70) |
| ATR 14j | $1.02 | Calcul agent | 6.06% du cours — trigger ATR_SPIKE actif |
| MM 50j | $11.70 | Calcul agent | Cours +43.9% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché |

**Niveaux clés (révisés) :**
- **Support immédiat :** $16.45 (low du jour) / $16.25 (close 13h, ancienne résistance devenue support)
- **Support structural :** $11.70 (MM 50j) / $15.47 (base du gap du 25/05)
- **Résistance :** $17.11 (52-week high) / $17.87 (take-profit ATR historique) / $19.89 (TP JSON)
- **Stop-loss ATR (2×) :** $14.80 ($16.835 − $2.04) — aligné avec `recommandations_latest.json`
- **Take-profit ATR (3×) :** $19.89 ($16.835 + $3.06) — aligné avec `recommandations_latest.json`
- **Ratio R/R :** 1.5

**Mise à jour options — données confirmées dans `latest.json` :**
| Niveau | Valeur 13:00 UTC (02/06) | Valeur 17:00 UTC (02/06) | Interprétation |
|--------|-------------------------|-------------------------|----------------|
| Max pain | $13.50 | **$13.50** | Inchangé — cohérent avec historique |
| Put/Call ratio | 0.45 | **0.45** | Structure bullish (dominance calls) |
| Call OI % | 69.1% | **69.1%** | Forte activité call — détenteurs ITM exposés au pin |
| Expiration | 2026-06-05 | **2026-06-05** | **Demain** |

> **🔴 Pin risk extrème à l'expiration 05/06 (demain).** Le cours ($16.835) est désormais **+24.7% au-dessus du max pain** ($13.50) vs +20.4% au snapshot 13h. La pression de mean-reversion vers $13.50 s'intensifie à chaque heure. Avec **1 jour restant** avant expiration vendredi, et en l'absence totale de catalyseur, la probabilité d'un ajustement baissier technique augmente. Le volume en décroissance (−42.5%) suggère que l'achat qui soutenait le cours à 13h s'est essoufflé.

**Verdict timing :** Défavorable. Le franchissement RSI 70 + new 52w high sur volume déclinant + pin risk à J-1 expiration crée une configuration technique de distribution potentielle. La tendance haussière structurelle reste intacte (cours > MM50), mais le timing d'entrée est désormais défavorable.

**Score Momentum :** 5.5/10 (source `recommandations_latest.json`) — révision à la baisse vs 7.0/10 au snapshot 13h, pénalisé par le franchissement de la zone surachat et l'effondrement du volume.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $93.98 B | Yahoo Finance |
| P/E (TTM Yahoo) | 105.22 | Yahoo Finance |
| Forward P/E (Yahoo) | 34.52 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 34.871 | Yahoo Finance |
| P/B (Yahoo) | 3.83 | Yahoo Finance |
| Dividend yield (Yahoo) | 1.01% | Yahoo Finance |

**Données opérationnelles FMP (FY 2025) — inchangées :**
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

**Filtre Qualité (6 critères) — inchangé :**
| Critère | Évaluation | Justification |
|---------|------------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ Non | Croissance anémique du top-line (mature 5G) |
| Profit CAGR 5 ans ≥ 20% | ❌ Non | Rentabilité historiquement faible |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.58, net cash position |
| FCF positif et croissant 5 ans | ⚠️ Partiel | FCF yield 4.9% mais trajectoire instable |
| Avantage compétitif (moat) | ⚠️ Partiel | Leader 5G historique mais part de marché sous pression |
| Industrie forte croissance (TAM ×5) | ❌ Non | TAM 5G mature, croissance à simple digit |
| **Score Qualité total** | **2.5/6** | 🔴 Hors périmètre (inchangé) |

**Note fondamentale :** Aucune donnée fondamentale nouvelle depuis le snapshot 13h. Le consensus inchangé à $9.26 sur 6 analystes maintient la divergence à **+81.8%** (vs +75.5% au snapshot 13h). Aucun upgrade, downgrade ou révision d'estimations n'a été détecté. Le quality report du pipeline matinal confirme le warning « Quality hors périmètre 2–2.5/6 ; P/E 105.22 très élevé ; Cours +81.8% vs consensus ».

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +81.8% vs consensus, P/E 105.22, forward P/E 34.52 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision — silence total malgré la volatilité |
| Nombre analysts actifs (mois) | 0 | FMP Stable API | Faible couverture |
| Put/Call ratio | 0.45 | Yahoo Finance | Structure bullish (dominance calls) — stable |
| Max pain | $13.50 | Yahoo Finance | 🔴 Risque pin baissier extrême à l'expiration demain |
| Call OI % | 69.1% | Yahoo Finance | Forte activité call — stable |
| Short Interest | 1.08% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiée dans le flux |

**Verdict Sentiment :** Neutre à légèrement bearish à court terme. La structure options est stable (put/call 0.45, call OI 69.1%) mais le max pain $13.50 crée une pression technique réelle à J-1 expiration. Le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement reste sans explication fondamentale. L'absence de volume à 17h sur le new high suggère un manque de conviction institutionnelle.

**Score Catalyseur :** 4.0/10 — inchangé dans `recommandations_latest.json`. Aucun catalyseur identifiable ; earnings éloignés (51 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Unknown (régime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score (JSON 17h) | Évolution (vs 13h) | Justification |
|-----|-----------------|-------------------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable |
| Valorisation | 3.5/10 | → | P/E 105.22, cours +81.8% vs consensus |
| Momentum | 5.5/10 | ↓ −1.5 | RSI 70.17 (surachat), volume −42.5% sous moyenne |
| **Score Opportunité** | **4.2/10** | ↓ −0.3 | (4.0×0.35) + (3.5×0.40) + (5.5×0.25) = 4.2 |
| **Score Global** | **41.8/100** | ↓ −8.7 | Malus : Valorisation faible + pin risk extrême + RSI surachat |
| **Score Global ajusté** | **31.8/100** | ↓ −18.7 | Seuil **ÉVITER** (<35) |

**Action recommandée :** **ÉVITER** (source `recommandations_latest.json`, Score Global ajusté 31.8/100)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

**⚠️ Divergence de scoring interne :** L'update 13h UTC indiquait un Score Global ajusté de 50.5/100 (ATTENDRE), tandis que le fichier `recommandations_latest.json` (snapshot 17h) porte le score à 31.8/100 (ÉVITER). Cette révision est justifiée par la dégradation du momentum (RSI surachat + volume en chute libre) et l'aggravation du premium de valorisation (+81.8% vs +75.5%). **Le fichier JSON prime.**

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (13:00 UTC 02/06) | Nouveau (17:00 UTC 02/06) | Justification |
|--------|--------------------------|--------------------------|---------------|
| Stop-loss | $14.17 | **$14.80** | Révisé — ATR 2× ($16.835 − $2.04), aligné JSON |
| Take-profit | $19.37 | **$19.89** | Révisé — ATR 3× ($16.835 + $3.06), aligné JSON |
| Prix cible (consensus) | $9.26 | $9.26 | Inchangé — 6 analysts, silence total |
| Upside consensus | −43.0% | **−45.0%** | Détérioré (cours +3.6%) |
| Downside SL | −12.8% | **−12.1%** | Stable |

**⚠️ Attention :** Le cours ($16.835) a atteint un nouveau 52w high ($17.11) sur volume déclinant (0.84× moyenne 20j). C'est une divergence baissière classique. Si le cours casse sous $16.25 (close 13h) en clôture, le rejet du new high sera confirmé et le retour vers $15.47 (support gap) puis $14.80 (SL) devient probable. Le **pin risk options ($13.50, expiration demain 05/06)** reste la menace principale : le cours est désormais +24.7% au-dessus du max pain. Sans catalyseur, la probabilité d'un ajustement baissier technique avant ou à l'expiration est élevée.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −7.39%, RS60d −15.71%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (51 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |
| **Quality Report** | Warning | Quality hors périmètre 2–2.5/6 ; P/E 105.22 ; cours +81.8% vs consensus. Pas d'exclusion. |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **modifiée** — le snapshot 17:00 UTC du 02/06 révèle une mutation technique significative qui pénalise le scoring global. La recommandation passe de **ATTENDRE** (50.5/100) à **ÉVITER** (31.8/100) selon le fichier `recommandations_latest.json`.

**Analyse :**
- **Technique :** Cours +3.6% à $16.835, nouveau 52w high $17.11. Cependant, le **RSI franchit 70** (70.17), entrant en zone de surachat. Le **volume s'effondre de 42.5%** (0.84× moyenne 20j), signalant une divergence baissière volume/prix classique sur new high. Le cours reste +43.9% au-dessus de la MM50 ($11.70) — tendance haussière structurelle intacte mais surchauffée.
- **Options :** Données stables (max pain $13.50, put/call 0.45, call OI 69.1%). Le pin risk devient encore plus extrême : cours +24.7% au-dessus du max pain, expiration **demain** (05/06). La structure call-dominated intacte signifie que les détenteurs de calls ITM sont de plus en plus exposés au pin.
- **Volume :** 98.9M (0.84×) — normalisation complète sous la moyenne 20j. La participation élevée du snapshot 13h (1.45×) n'a pas été maintenue. Cela fragilise le soutien du nouveau high.
- **Fondamentaux :** Aucune amélioration. P/E Yahoo 105.22, forward P/E 34.52. Consensus inchangé $9.26. Divergence prix/valeur à +81.8% (vs +75.5% au snapshot 13h).
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news. Le rally de +9.6% depuis la veille reste non justifié fondamentalement.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d −7.39%, RS60d −15.71%). Le mouvement de NOK reste totalement idiosyncratique.

**Ce qui a changé (13:00 UTC 02/06 → 17:00 UTC 02/06) :**
- **Cours :** $16.25 → **$16.835** (+3.6%)
- **RSI :** 62.59 → **70.17** (surachat)
- **Volume :** 1.45× → **0.84×** (normalisation)
- **52w high :** $16.63 → **$17.11** (new high)
- **P/E Yahoo :** 101.56 → **105.22**
- **Premium consensus :** +75.5% → **+81.8%**
- **Score Global ajusté :** 50.5/100 (ATTENDRE) → **31.8/100 (ÉVITER)**
- **Score Momentum :** 7.0/10 → **5.5/10**

**Ce qui n'a pas changé :**
- **Options :** max pain $13.50, put/call 0.45, call OI 69.1%
- **Consensus :** $9.26 (6 analysts) — silence total
- **Qualité :** 2.5/6 hors périmètre
- **Catalyseur :** 4.0/10 — aucun identifié
- **Event-Driven :** Aucun événement corporate
- **Sectoriel :** XLC bottom 3
- **FX :** Score 0.0/10, aligned

**Recommandation révisée :**
- **Action :** **ÉVITER** (Score Global ajusté 31.8/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $14.80 (2×ATR)
- **Take-profit :** $19.89 (3×ATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scénarios forward (révisés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 10% | Breakout $17.11 avec volume >1.5× + catalyseur | $18.50–$19.50 |
| Central | 35% | Consolidation $16.00–$17.00 sans catalyseur | Range |
| Pessimiste | 55% | Pin options $13.50 + retour MM50 $11.70 | $13.00–$15.00 |

**⚠️ Risque principal :** Pin options à $13.50 avec expiration **demain** (05/06). Le cours +24.7% au-dessus du max pain crée une pression baissière technique extrême à court terme. Le volume en chute libre sur new high suggère que l'achat institutionnel s'est retiré. Si le cours clôture sous $16.25, le rejet du new high sera confirmé et l'accélération vendeuse vers $14.80 (SL) puis $13.50 devient probable. Le rally de +9.6% est non justifié fondamentalement et donc fragile. Aucun catalyseur ne soutient le niveau au-delà du momentum technique désormais surchauffé.

**Prochains points de contrôle :**
- Franchissement du 52w high à $17.11 avec volume (ou rejet)
- Franchissement sous $16.25 en clôture (confirmation rejet new high)
- **Expiration options 2026-06-05** (demain) — comportement autour du max pain $13.50
- Earnings Q2 FY2026 au **2026-07-23** (dans **51 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Catalyseur éventuel expliquant le rally de +9.6% (M&A, contrat, upgrade)

---

*Données sources : `data/latest.json` (2026-06-02T17:00:09 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
