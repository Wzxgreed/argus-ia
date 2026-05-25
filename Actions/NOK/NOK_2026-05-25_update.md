# NOK — Mise à Jour Quotidienne (2026-05-25, Snapshot 17:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-25 | Données source : `data/latest.json` (snapshot 2026-05-25T17:00:07 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (2026-05-20)

| Indicateur | Snapshot 20/05 | Snapshot 25/05 (17:00 UTC) | Variation | Signal |
|-----------|---------------|----------------------------|-----------|--------|
| Cours close | $13.67 | **$15.47** | **+$1.80 (+13.2%)** | 🔴 Gap haussier majeur |
| Change % vs previous close | −0.51% | **+9.1%** | — | Nouveau 52w high intraday |
| RSI 14j | 58.34 | **64.29** | +5.95 pts | Approche surachat (>70) |
| ATR 14j | $0.94 | **$0.98** | +$0.04 (+4.3%) | Volatilité en légère hausse |
| Volume relatif | 0.65× | **1.07×** | +0.42× | Retour de liquidité au-dessus de la moyenne |
| 52-week high | $15.19 | **$15.78** | New high | Record annuel cassé |
| P/E (TTM Yahoo) | ~85.4 | **96.69** | +11.3 pts | Expansion multiple aggravée |
| Forward P/E | 28.18 | **31.72** | +3.54 pts | Multiple forward réévalué |
| Premium vs consensus $9.26 | +47.6% | **+66.8%** | +19.2 pp | Surévaluation massive |
| Consensus analystes (FMP) | $9.26 (6) | $9.26 (6) | Inchangé | Aucune révision détectée |
| Put/Call ratio | 0.35 | **0.41** | +0.06 | Reste bullish |
| Max pain options | $14.50 | **$14.00** | −$0.50 | Sous le cours |
| Call OI | 73.8% | **70.9%** | −2.9 pp | Dominance calls maintenue |

**Changements significatifs détectés :**
- **Cours +9.1% aujourd'hui** et +13.2% depuis le 20/05, avec un nouveau 52-week high à $15.78 (intraday).
- **Aucun catalyseur fondamental** identifié dans `data/events_latest.json` (vide pour NOK) ni dans `data/upcoming_events_latest.json` (hors earnings programmé au 2026-07-23).
- **Volume revenu à la normale** (1.07× moyenne 20j) après une période de liquidité réduite.
- **Options bullish** : put/call 0.41, call OI 70.9%, max pain $14.00 (sous le close), expiration 2026-05-29.

**Confirmation snapshot 17:00 UTC vs 13:00 UTC :** Données strictement inchangées. Le snapshot 17:00 UTC reproduit la clôture US unique du jour. Aucune mutation technique, fondamentale ou options entre les deux timestamps.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $15.47 | Yahoo Finance | +9.1% vs previous close ($14.18) |
| Open | $14.70 | Yahoo Finance | Gap haussier d'ouverture |
| High intraday | $15.78 | Yahoo Finance | **Nouveau 52-week high** |
| Low intraday | $14.58 | Yahoo Finance | Support intraday immédiat |
| Volume | 127,394,200 | Yahoo Finance | 1.07× moyenne 20j (118,870,420) |
| RSI 14j | 64.29 | Calcul agent | Zone neutre haute, proche surachat |
| ATR 14j | $0.98 | Calcul agent | 6.33% du cours — volatilité relative modérée |
| MM 50j | $10.80 | Calcul agent | Cours +43.2% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché |

**Niveaux clés (révisés) :**
- **Support immédiat :** $14.58 (low du jour) / $14.0 (max pain options)
- **Résistance :** $15.78 (52-week high, fragile sans catalyseur)
- **Stop-loss ATR (2×) :** $13.51 ($15.47 − $1.96)
- **Take-profit ATR (3×) :** $18.41 ($15.47 + $2.94)
- **Ratio R/R :** 1.5

**Verdict timing :** Favorable sur le momentum pur — le cours est au-dessus de la MM50 avec un écart significatif (+43.2%), le volume est revenu à la normale, et l'options flow est bullish. Cependant, le RSI à 64.29 approche la zone de surachat (>70) sans catalyseur fondamental identifiable, ce qui fragilise la durabilité du mouvement.

**Score Momentum :** 7.0/10 — inchangé (gap +9.1%, new 52w high, volume normalisé, options bullish).

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $86.36 B | Yahoo Finance |
| P/E (TTM) | 96.69 | Yahoo Finance |
| Forward P/E | 31.72 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 33.15 | Yahoo Finance |
| EV/EBITDA (FMP) | 13.13 | FMP Stable API (FY2025) |
| P/B | 3.52 | Yahoo Finance |
| Dividend yield | 1.06% | Yahoo Finance |

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

**Note fondamentale :** Aucune donnée fondamentale nouvelle (earnings, guidance, M&A) n'explique le gap de +9.1%. L'expansion du multiple P/E de ~85.4 à 96.69 en 5 jours, sur un consensus inchangé à $9.26, creuse la divergence entre prix et valeur. Le forward P/E à 31.72 reste élevé pour une entreprise à croissance limitée et quality hors périmètre.

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 96.7 vs FMP 45.8 ; EV/EBITDA Yahoo 33.2 vs FMP 13.1. Cette divergence n'affecte pas le verdict consensus calibré sur l'ADR.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +66.8% vs consensus, P/E 96.7, forward P/E 31.7 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision détectée |
| Nombre analysts actifs (mois) | 1 | FMP Stable API | Faible couverture |
| Put/Call ratio | 0.41 | Yahoo Finance | Forte inclination calls |
| Max pain | $14.00 | Yahoo Finance | $1.47 sous le close |
| Call OI % | 70.9% | Yahoo Finance | Dominance calls maintenue |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD, pas d'impact |

**Verdict Sentiment :** Bullish technique sur les options, mais neutre/bearish sur le consensus sell-side. Le max pain à $14.00 crée un aimant technique si le momentum faiblit avant l'expiration du 29 mai. Aucun upgrade/downgrade massif détecté dans `data/upcoming_events_latest.json`.

**Score Catalyseur :** 4.0/10 — inchangé. Aucun catalyseur identifiable ; gap non expliqué par news/event ; earnings éloignés (59 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Inconnu (regime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable — gap non expliqué |
| Valorisation | 3.5/10 | → | P/E 96.7, cours +66.8% vs consensus, forward P/E 31.7 sur stock mature |
| Momentum | 7.0/10 | → | Gap +9.1%, new 52w high, volume normalisé, options bullish |
| **Score Opportunité** | **4.5/10** | → | (4.0×0.35) + (3.5×0.40) + (7.0×0.25) = 4.5 |
| **Score Global** | **45.5/100** | → | Malus : Valorisation faible plombe le score |
| **Score Global ajusté** | **50.5/100** | → | — |

**Action recommandée :** **ATTENDRE** (seuil 50–59)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (20/05) | Nouveau (25/05) | Justification |
|--------|----------------|-----------------|---------------|
| Stop-loss | $11.79 | **$13.51** | Recalcul ATR 2× ($15.47 − $1.96) — le gap haussier réduit la marge de sécurité |
| Take-profit | $16.49 | **$18.41** | Recalcul ATR 3× ($15.47 + $2.94) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchangé — 6 analysts |
| Upside consensus | −32.1% | **−40.1%** | Écart consensus vs cours aggravé |
| Downside SL | −13.5% | **−12.7%** | Risque de perte maîtrisé si SL respecté |

**⚠️ Attention :** Le SL à $13.51 est désormais très proche du support intraday ($14.58). Un retour sous $14.00 (max pain) confirmerait une inversion technique rapide. Le gap de +9.1% sans catalyseur rend le titre vulnérable à un retour de moyenne.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 2, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −4.51%, RS60d −9.23%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **modifiée** — le gap de +9.1% invalide l'hypothèse de retour rapide vers le consensus ($9.26), mais ne la transforme pas en signal d'achat.

**Analyse :**
- **Avant (20/05) :** Value trap technique. Cours surévalué mais sans momentum. Attendre un retour de volatilité ou une correction vers le consensus.
- **Après (25/05) :** Momentum haussier brutal sans catalyseur fondamental. Le titre a grimpé de +13.2% en 5 séances, atteint un nouveau 52-week high ($15.78), avec un volume revenu à la normale et un options flow bullish. Cette configuration ressemble à un **momentum trade spéculatif** (possible rumeur non capturée, rotation sectorielle tardive, ou flux institutionnel non identifié).

**Ce qui a changé :**
1. **Technique :** Le support est remonté de $11.79 à $13.51. Le titre est désormais en zone de surachat avancée (RSI 64.3, proche 70).
2. **Valorisation :** La surévaluation s'est aggravée (+66.8% vs consensus). Le forward P/E à 31.7 reste incompatible avec la qualité fondamentale (Quality 2.5/6).
3. **Sectoriel :** Le secteur Communication Services (XLC) est en sous-performance relative vs SPY — le gap de NOK est donc **idiosyncratique**, pas sectoriel.

**Ce qui n'a pas changé :**
- **Fondamentaux :** Aucune amélioration des marges, du ROIC, ou du consensus.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise.
- **Données 17:00 UTC :** Confirmation intégrale du snapshot 13:00 UTC. Aucune mutation post-clôture.

**Recommandation révisée :**
- **Action :** **ATTENDRE** (Score Global ajusté 50.5/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $13.51 (nouveau)
- **Take-profit :** $18.41 (momentum pur, sans conviction fondamentale)
- **Sizing :** — (pas de position)

**Scénarios forward :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 20% | Rumeur/upgrade non capturé se confirme | $16.50–$18.00 |
| Central | 50% | Consolidation autour de $14.50–$15.50 | Range |
| Pessimiste | 30% | Aucun catalyseur → retour vers max pain $14.00 | $13.50–$14.00 |

**⚠️ Risque principal :** Gap haussier non expliqué = vulnérable à un retour de moyenne rapide si le catalyseur (s'il existe) n'est pas confirmé. Le max pain options à $14.00 offre un premier support psychologique. L'absence de news structurante dans `data/events_latest.json` et `data/upcoming_events_latest.json` est un signal d'alerte — un gap de cette amplitude sans fondamental est généralement suivi d'une correction si le flux institutionnel s'inverse.

**Prochains points de contrôle :**
- Earnings Q2 FY2026 au **2026-07-23** (dans **59 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Expiration options **2026-05-29** — observer si le max pain $14.00 agit comme aimant
- Franchissement technique du SL à $13.51

---

*Données sources : `data/latest.json` (2026-05-25T17:00:07 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
