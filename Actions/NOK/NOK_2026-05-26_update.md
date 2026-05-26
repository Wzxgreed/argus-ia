# NOK — Mise à Jour Quotidienne (2026-05-26, Snapshot 13:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-26 | Données source : `data/latest.json` (snapshot 2026-05-26T13:00:08 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (2026-05-26 10:00 UTC)

| Indicateur | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Variation | Signal |
|-----------|-------------------|-------------------|-----------|--------|
| Cours close | $15.47 | **$15.47** | **0.00%** | 🟢 Stable |
| Change % vs previous close | +9.1% | **+9.1%** | — | Inchangé |
| RSI 14j | 64.29 | **64.29** | 0.00 | Stable |
| ATR 14j | $0.98 | **$0.98** | $0.00 | Stable |
| Volume relatif | 1.07× | **1.07×** | 0.00× | Stable |
| 52-week high | $15.78 | **$15.78** | — | Stable |
| P/E (TTM Yahoo) | 96.69 | **96.69** | 0.00 | Stable |
| Forward P/E | 31.72 | **31.72** | 0.00 | Stable |
| Premium vs consensus $9.26 | +66.8% | **+66.8%** | 0.0 pp | Stable |
| Consensus analystes (FMP) | $9.26 (6) | **$9.26 (6)** | Inchangé | Stable |
| Put/Call ratio | `null` (données partielles) | **0.51** | ✅ Restauré | Modération du bullish |
| Max pain options | $2.00 (incohérent) | **$15.00** | ✅ Restauré | Pin remonté |
| Call OI | `null` (données partielles) | **66.1%** | ✅ Restauré | Dominance calls maintenue |

**Changements significatifs détectés :**
- **🟢 Données options restaurées** dans le snapshot 13:00 UTC après un blackout partiel au snapshot 10:00 UTC (put/call `null`, max pain $2.00 placeholder, call OI `null`).
- **Max pain remonté à $15.00** (vs $14.00 au 25/05 et vs $2.00 placeholder ce matin). Le niveau de pin options est désormais à seulement $0.47 sous le close actuel, contre $1.47 auparavant. Cela réduit la probabilité d'un retour de moyenne violent vers $14.00 avant l'expiration du 29 mai.
- **Put/Call ratio 0.51** (vs 0.41 au 25/05) : la dominance call se modère mais reste nettement bullish. Ratio < 1.0 = plus d'OI calls que puts.
- **Call OI 66.1%** (vs 70.9% au 25/05) : léger désengagement des calls après le gap +9.1%, mais la structure reste haussière.
- **Aucune mutation fondamentale** : P/E, consensus, volumes, RSI, ATR strictement inchangés.
- **Aucun catalyseur fondamental** identifié dans `data/events_latest.json` (vide pour NOK) ni dans `data/news_2026-05-26.json` (0 article).

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $15.47 | Yahoo Finance | Inchangé vs 10:00 UTC. Gap +9.1% du 25/05 maintenu. |
| Open | $14.70 | Yahoo Finance | Gap haussier du 25/05 inchangé |
| High intraday | $15.78 | Yahoo Finance | **52-week high** |
| Low intraday | $14.58 | Yahoo Finance | Support intraday immédiat |
| Volume | 127,394,200 | Yahoo Finance | 1.07× moyenne 20j (118,870,420) |
| RSI 14j | 64.29 | Calcul agent | Zone neutre haute, proche surachat (>70) |
| ATR 14j | $0.98 | Calcul agent | 6.33% du cours — volatilité modérée |
| MM 50j | $10.80 | Calcul agent | Cours +43.2% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché |

**Niveaux clés (inchangés) :**
- **Support immédiat :** $14.58 (low du 25/05) / $15.00 (max pain options, renforcé)
- **Résistance :** $15.78 (52-week high)
- **Stop-loss ATR (2×) :** $13.51 ($15.47 − $1.96)
- **Take-profit ATR (3×) :** $18.41 ($15.47 + $2.94)
- **Ratio R/R :** 1.5

**Mise à jour options — impact technique :**
| Niveau | Valeur 25/05 | Valeur 26/05 13:00 | Interprétation |
|--------|-------------|-------------------|----------------|
| Max pain | $14.00 | **$15.00** | Le "pin" options remonte de $1.00. Le cours ($15.47) n'est plus que +3.1% au-dessus du max pain vs +10.5% précédemment. |
| Put/Call ratio | 0.41 | **0.51** | Plus d'équilibre entre calls et puts. Moins de skew call extrême, mais reste haussier. |
| Call OI % | 70.9% | **66.1%** | Désengagement partiel des calls après le gap. Structure moins unilatérale. |
| Expiration | 2026-05-29 | **2026-05-29** | 3 jours — risque de pin au max pain $15.00. |

**Verdict timing :** Favorable sur le momentum pur — inchangé. Le cours reste au-dessus de la MM50 (+43.2%) avec un volume normalisé. La restauration du max pain à $15.00 (vs $14.00 précédent) est un signal technique modérément positif : la probabilité d'un retour vers $14.00 avant vendredi diminue. Cependant, le RSI à 64.29 sans catalyseur fondamental fragilise la durabilité du mouvement au-delà du 52-week high.

**Score Momentum :** 7.0/10 — inchangé (gap +9.1% maintenu, new 52w high, volume normalisé, options bullish).

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

**Note fondamentale :** Aucune donnée fondamentale nouvelle entre le snapshot 10:00 UTC et le snapshot 13:00 UTC. L'expansion du multiple P/E à 96.69 sur un consensus inchangé à $9.26 maintient la divergence prix/valeur. Le forward P/E à 31.72 reste élevé pour une entreprise à croissance limitée et quality hors périmètre.

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 96.7 vs FMP 45.8 ; EV/EBITDA Yahoo 33.2 vs FMP 13.1. Cette divergence n'affecte pas le verdict consensus calibré sur l'ADR.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +66.8% vs consensus, P/E 96.7, forward P/E 31.7 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision détectée |
| Nombre analysts actifs (mois) | 1 | FMP Stable API | Faible couverture |
| Put/Call ratio | **0.51** | Yahoo Finance (restauré) | Dominance calls modérée (vs 0.41 au 25/05). Plus d'équilibre, moins de skew extrême. |
| Max pain | **$15.00** | Yahoo Finance (restauré) | Pin remonté de $14.00 → $15.00. Le cours ($15.47) est désormais proche du max pain. |
| Call OI % | **66.1%** | Yahoo Finance (restauré) | Dominance calls maintenue mais en recul (vs 70.9%). |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD, pas d'impact |
| News du jour | 0 article | `news_2026-05-26.json` | Aucune news NOK dans le flux Yahoo |

**Verdict Sentiment :** Bullish technique sur les options, mais neutre/bearish sur le consensus sell-side. La restauration des données options révèle une structure modérément moins bullish qu'au 25/05 (put/call 0.51 vs 0.41, call OI 66.1% vs 70.9%), ce qui peut s'interpréter comme un léger désengagement spéculatif après le gap +9.1%. Le max pain à $15.00 est désormais un niveau de support psychologique plus proche du cours. Aucun upgrade/downgrade massif détecté.

**Score Catalyseur :** 4.0/10 — inchangé. Aucun catalyseur fondamental identifiable ; gap du 25/05 non expliqué par news/event ; earnings éloignés (57 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Inconnu (regime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable — gap du 25/05 non expliqué |
| Valorisation | 3.5/10 | → | P/E 96.7, cours +66.8% vs consensus, forward P/E 31.7 sur stock mature |
| Momentum | 7.0/10 | → | Gap +9.1% maintenu, new 52w high, options bullish (restaurés) |
| **Score Opportunité** | **4.5/10** | → | (4.0×0.35) + (3.5×0.40) + (7.0×0.25) = 4.5 |
| **Score Global** | **45.5/100** | → | Malus : Valorisation faible plombe le score |
| **Score Global ajusté** | **50.5/100** | → | — |

**Action recommandée :** **ATTENDRE** (seuil 50–59)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (10:00 UTC) | Nouveau (13:00 UTC) | Justification |
|--------|---------------------|---------------------|---------------|
| Stop-loss | $13.51 | **$13.51** | Inchangé — recalcul ATR 2× stable |
| Take-profit | $18.41 | **$18.41** | Inchangé — recalcul ATR 3× stable |
| Prix cible (consensus) | $9.26 | $9.26 | Inchangé — 6 analysts |
| Upside consensus | −40.1% | **−40.1%** | Inchangé |
| Downside SL | −12.7% | **−12.7%** | Inchangé |
| Max pain options | $2.00 (incohérent) | **$15.00** | ✅ Restauré — nouveau support psychologique |

**⚠️ Attention :** Le max pain options à $15.00 est désormais très proche du cours ($15.47, écart +3.1%). À 3 jours de l'expiration (29 mai), ce niveau agira comme un aimant gamma. Un franchissement sous $15.00 pourrait déclencher une accélération vendeuse vers le support intraday $14.58. Au-dessus de $15.00, la structure options est un soutien technique. Le SL à $13.51 reste la barrière de sortie principale.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −4.51%, RS60d −9.23%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (57 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B. |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **confirmée** — aucune mutation fondamentale entre le snapshot 10:00 UTC et le snapshot 13:00 UTC. Seules les données options ont été restaurées.

**Analyse :**
- Les données de clôture, technique et fondamentale sont **strictement identiques** au snapshot 10:00 UTC (close $15.47, RSI 64.29, ATR $0.98, volume 1.07×, consensus $9.26).
- **Restauration des données options** : le snapshot 13:00 UTC corrige le blackout partiel du 10:00 UTC. Le max pain remonte à $15.00 (vs $14.00 au 25/05), le put/call ratio à 0.51 (vs 0.41), et le call OI à 66.1% (vs 70.9%).
- **Implications options** : le max pain plus proche du cours réduit le risque d'un retour de moyenne violent vers $14.00 avant l'expiration du 29 mai. Cependant, la modération du skew call (put/call +0.10, call OI −4.8 pp) suggère un léger désengagement spéculatif post-gap.
- **Aucun catalyseur fondamental** n'est apparu entre les deux snapshots. Aucune news, aucun événement corporate, aucun upgrade/downgrade.

**Ce qui n'a pas changé :**
- **Technique :** RSI 64.29, ATR $0.98, volume 1.07×, cours inchangé.
- **Fondamentaux :** Aucune amélioration des marges, du ROIC, ou du consensus. P/E 96.7, forward P/E 31.7.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3).

**Recommandation révisée :**
- **Action :** **ATTENDRE** (Score Global ajusté 50.5/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $13.51 (inchangé)
- **Take-profit :** $18.41 (inchangé)
- **Sizing :** — (pas de position)

**Scénarios forward (inchangés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 20% | Rumeur/upgrade non capturé se confirme | $16.50–$18.00 |
| Central | 50% | Consolidation autour de $14.80–$15.50 avec pin au max pain $15.00 | Range |
| Pessimiste | 30% | Aucun catalyseur → retour vers $14.50–$14.80 | $13.50–$14.80 |

**⚠️ Risque principal :** Gap haussier du 25/05 non expliqué = vulnérable à un retour de moyenne si le catalyseur (s'il existe) n'est pas confirmé. Le max pain options à $15.00 offre un premier support gamma, mais un franchissement sous ce niveau avant vendredi pourrait accélérer la correction. Données options restaurées mais modérées vs le 25/05.

**Prochains points de contrôle :**
- Earnings Q2 FY2026 au **2026-07-23** (dans **57 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Expiration options **2026-05-29** (dans **3 jours**) — observer le pin au max pain $15.00
- Franchissement technique du SL à $13.51
- Rétablissement complet et cohérent des données options dans les prochains snapshots

---

*Données sources : `data/latest.json` (2026-05-26T13:00:08 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/news_2026-05-26.json`. Aucune donnée hallucinée.*
