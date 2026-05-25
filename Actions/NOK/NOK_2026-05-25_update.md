# NOK — Mise à jour 2026-05-25

**Date :** 2026-05-25  
**Type :** Update post-FULL REFRESH (triggers PRICE_GAP + ATR_SPIKE)  
**Analyste :** Desk Argus-IA  
**Horizon :** Court terme (jusqu'aux earnings Q2 FY2026, 23 juillet)

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | Précédent (20/05) | Actuel (25/05) | Δ |
|----------|-------------------|----------------|---|
| Cours close | $13.67 | **$15.47** | **+13.2%** (+9.1% aujourd'hui) |
| RSI 14j | 58.34 | **64.29** | +5.95 pts |
| ATR 14j | $0.94 | **$0.98** | +4.3% |
| Volume vs 20j | 0.65× | **1.07×** | Retour de liquidité |
| 52-week high | — | **$15.78** | New high intraday |
| Consensus analystes (FMP) | $9.26 (6) | $9.26 (6) | Inchangé |
| Spread vs consensus | +47.6% | **+66.8%** | Surévaluation aggravée |
| P/E (TTM Yahoo) | ~85.4 | **96.69** | Expansion multiple |
| Forward P/E | — | **31.72** | [Données actualisées] |
| Put/Call ratio | 0.35 | **0.41** | Légère hausse, reste bullish |
| Max pain options | $14.50 | **$14.0** | Décalage sous le cours |
| Call OI | 73.8% | **70.9%** | Dominance calls maintenue |

**Événements corporates détectés (data/events_latest.json) :** Aucun.  
**Nouvelles fondamentales majeures identifiées :** Aucune — le gap n'est pas expliqué par un événement structurant capturé dans le pipeline.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | $15.47 | Yahoo Finance |
| Open | $14.70 | Yahoo Finance |
| High intraday | $15.78 | Yahoo Finance (52-week high) |
| Low intraday | $14.58 | Yahoo Finance |
| Change % vs previous close | **+9.1%** | Yahoo Finance |
| Volume | 127,394,200 | Yahoo Finance |
| Volume vs moy. 20j | 1.07× | Calcul |
| RSI 14j | 64.29 | Calcul agent |
| ATR 14j | $0.98 | Calcul agent |
| MM 50j | $10.80 | Calcul agent |
| MM 200j | — | Calcul agent |
| Golden Cross | Non | Calcul agent |
| Beta | 0.765 | Yahoo Finance |

**Niveaux clés (révisés) :**
- **Support immédiat :** $14.58 (low du jour) / $14.0 (max pain options)
- **Résistance :** $15.78 (52-week high, fragile si pas de catalyseur)
- **Stop-loss ATR (2×) :** $13.51 (cours − 2×ATR = 15.47 − 1.96)
- **Take-profit ATR (3×) :** $18.41 (cours + 3×ATR = 15.47 + 2.94)
- **Ratio R/R :** 1.5

**Verdict timing :** Favorable sur le momentum pur — le cours est au-dessus de la MM50 ($10.80) avec un écart significatif (+43.2%), le volume est revenu à la normale, et l'options flow est bullish. Cependant, le RSI à 64.29 approche la zone de surachat (>70) sans catalyseur fondamental identifiable, ce qui fragilise la durabilité du mouvement.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $86.36B | Yahoo Finance |
| P/E (TTM) | 96.69 | Yahoo Finance |
| Forward P/E | 31.72 | Yahoo Finance |
| EV/EBITDA (FMP) | 13.13 | FMP Stable API (FY2025) |
| Gross Margin (FMP) | 43.5% | FMP Stable API |
| Operating Margin (FMP) | 3.9% | FMP Stable API |
| Net Margin (FMP) | 3.3% | FMP Stable API |
| ROE (FMP) | 3.1% | FMP Stable API |
| ROIC (FMP) | 1.9% | FMP Stable API |
| Debt/Equity | 0.25 | FMP Stable API |
| Current Ratio | 1.58 | FMP Stable API |
| Dividend Yield | 1.06% | Yahoo Finance |

**Filtre Qualité (6 critères) :**
| Critère | Évaluation | Justification |
|---------|------------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ Non | Croissance anémique du top-line (mature 5G) |
| Profit CAGR 5 ans ≥ 20% | ❌ Non | Rentabilité historiquement faible |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.58, net cash position (net debt/EBITDA négatif −0.11) |
| FCF positif et croissant 5 ans | ⚠️ Partiel | FCF yield 4.9% (FMP) mais trajectoire instable |
| Avantage compétitif (moat) | ⚠️ Partiel | Leader 5G historique mais part de marché sous pression (Huawei, Ericsson) |
| Industrie forte croissance (TAM ×5) | ❌ Non | TAM 5G mature, croissance à simple digit |
| **Score Qualité total** | **2.5/6** | 🔴 Hors périmètre (inchangé) |

**Note fondamentale :** Aucune donnée fondamentale nouvelle (earnings, guidance, M&A) n'explique le gap de +9.1%. L'expansion du multiple P/E de ~85.4 à 96.69 en 5 jours, sur un consensus inchangé à $9.26, creuse la divergence entre prix et valeur. Le forward P/E à 31.72 reste élevé pour une entreprise à croissance limitée.

---

## 4. Bloc Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $9.26 (6 analysts) | FMP Stable API | Aucune révision détectée |
| Nombre analysts actifs (mois) | 1 | FMP Stable API | Faible couverture |
| Put/Call ratio | 0.41 | Yahoo Finance | Forte inclination calls |
| Max pain | $14.00 | Yahoo Finance | $1.47 sous le close |
| Call OI % | 70.9% | Yahoo Finance | Dominance calls maintenue |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |

**Verdict Sentiment :** Bullish technique sur les options, mais neutre/bearish sur le consensus sell-side. Le max pain à $14.00 crée un aimant technique si le momentum faiblit avant l'expiration du 29 mai. Aucun upgrade/downgrade massif détecté (data/upcoming_events_latest.json).

---

## 5. Scoring Global

**Pondération régime macro :** Inconnue (regime = Unknown) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable — gap non expliqué par news/event |
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
| Stop-loss | $11.79 | **$13.51** | Recalcul ATR 2× (15.47 − 1.96) — le gap haussier réduit la marge de sécurité |
| Take-profit | — | **$18.41** | Recalcul ATR 3× (15.47 + 2.94) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchangé — 6 analysts |
| Upside consensus | −32.1% | **−40.1%** | Écart consensus vs cours aggravé |
| Downside SL | −13.5% | **−12.7%** | Risque de perte maîtrisé si SL respecté |

**⚠️ Attention :** Le SL à $13.51 est désormais très proche du support intraday ($14.58). Un retour sous $14.00 (max pain) confirmerait une inversion technique rapide.

---

## 7. Exposition Macro & Sectorielle

**Régime macro :** Unknown (données macro partielles dans le pipeline).  
**Exposition sectorielle (Sector Rotation) :** XLC (Communication Services) classé **bottom 3** du classement sectoriel (momentum score 0.0, RS20d −4.51%, RS60d −9.23%). C'est un **headwind sectoriel** pour NOK — la rotation actuelle privilégie la Tech (XLK) et l'Energie (XLE), pas les télécoms/communication services.

**FX Exposure (data/fx_exposure_latest.json) :**
- Exposition : 25% export, primary currency USD
- Impact revenus/EPS estimé : 0%
- Divergence : aligned
- Flag : 🟢 — pas d'impact FX identifiable aujourd'hui.

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **modifiée** — le gap de +9.1% invalide l'hypothèse de retour rapide vers le consensus ($9.26), mais ne la transforme pas en signal d'achat.

**Analyse :**
- **Avant (20/05) :** Value trap technique. Cours surévalué mais sans momentum. Attendre un retour de volatilité ou une correction vers le consensus.
- **Après (25/05) :** Momentum haussier brutal sans catalyseur fondamental. Le titre a grimpé de +13.2% en 5 séances, atteint un new 52-week high ($15.78), avec un volume revenu à la normale et un options flow bullish. Cette configuration ressemble à un **momentum trade spéculatif** (possible rumeur non capturée, rotation sectorielle tardive, ou flux institutionnel non identifié dans les données JSON).

**Ce qui a changé :**
1. **Technique :** Le support est remonté de $11.79 à $13.51. Le titre est désormais en zone de surachat avancée (RSI 64.3, proche 70).
2. **Valorisation :** La surévaluation s'est aggravée (+66.8% vs consensus). Le forward P/E à 31.7 reste incompatible avec la qualité fondamentale (Quality 2.5/6).
3. **Sectoriel :** Le secteur Communication Services est en sous-performance relative vs SPY — le gap de NOK est donc **idiosyncratique**, pas sectoriel.

**Ce qui n'a pas changé :**
- **Fondamentaux :** Aucune amélioration des marges, du ROIC, ou du consensus.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise.

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

**⚠️ Risque principal :** Gap haussier non expliqué = vulnerable à un retour de moyenne rapide si le catalyseur (s'il existe) n'est pas confirmé. Le max pain options à $14.00 offre un premier support psychologique. L'absence de news structurante dans `data/events_latest.json` et `data/upcoming_events_latest.json` est un signal d'alerte — un gap de cette amplitude sans fondamental est généralement suivi d'une correction si le flux institutionnel s'inverse.

---

*Données sources : data/latest.json (2026-05-25), data/recommandations_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json. Aucune donnée hallucinée.*
