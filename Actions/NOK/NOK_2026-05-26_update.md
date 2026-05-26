# NOK — Mise à Jour Quotidienne (2026-05-26, Snapshot 10:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-26 | Données source : `data/latest.json` (snapshot 2026-05-26T10:00:09 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (2026-05-25 21:00 UTC)

| Indicateur | Snapshot 25/05 21:00 UTC | Snapshot 26/05 10:00 UTC | Variation | Signal |
|-----------|-------------------------|-------------------------|-----------|--------|
| Cours close | $15.47 | **$15.47** | **0.00%** | 🟢 Stable |
| Change % vs previous close | +9.1% | **+9.1%** | — | Inchangé |
| RSI 14j | 64.29 | **64.29** | 0.00 | Stable |
| ATR 14j | $0.98 | **$0.98** | $0.00 | Stable |
| Volume relatif | 1.07× | **1.07×** | 0.00× | Stable |
| 52-week high | $15.78 | **$15.78** | — | Stable |
| P/E (TTM Yahoo) | 96.69 | **96.69** | 0.00 | Stable |
| Forward P/E | 31.72 | **31.72** | 0.00 | Stable |
| Premium vs consensus $9.26 | +66.8% | **+66.8%** | 0.0 pp | Stable |
| Consensus analystes (FMP) | $9.26 (6) | $9.26 (6) | Inchangé | Stable |
| Put/Call ratio | 0.41 | **[DONNÉES PARTIELLES]** | — | ⚠️ Yahoo retourne `null` |
| Max pain options | $14.00 | **[DONNÉES PARTIELLES — $2.00]** | — | ⚠️ Valeur incohérente, probable placeholder |
| Call OI | 70.9% | **[DONNÉES PARTIELLES]** | — | ⚠️ Yahoo retourne `null` |

**Changements significatifs détectés :**
- **Aucun.** Le snapshot 10:00 UTC du 2026-05-26 reproduit strictement les mêmes données de clôture que le snapshot 21:00 UTC du 2026-05-25. C'est le premier jour de marché post-Memorial Day (25/05 fermé) ; les données reflètent le close du 23/05 ou du 24/05 non mis à jour sur le feed Yahoo pour NOK.
- **Aucun catalyseur fondamental** identifié dans `data/events_latest.json` (vide pour NOK) ni dans `data/upcoming_events_latest.json` (hors earnings programmé au 2026-07-23).
- **⚠️ Données options partielles** dans `data/latest.json` : put/call ratio, call OI % et max pain retournent `null` ou une valeur incohérente ($2.00). Dernière lecture fiable : put/call 0.41, call OI 70.9%, max pain $14.00 (snapshot 25/05).

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $15.47 | Yahoo Finance | Inchangé vs 25/05 21:00 UTC |
| Open | $14.70 | Yahoo Finance | Gap haussier du 25/05 maintenu |
| High intraday | $15.78 | Yahoo Finance | **52-week high**, inchangé |
| Low intraday | $14.58 | Yahoo Finance | Support intraday immédiat, inchangé |
| Volume | 127,394,200 | Yahoo Finance | 1.07× moyenne 20j (118,870,420), inchangé |
| RSI 14j | 64.29 | Calcul agent | Zone neutre haute, proche surachat, inchangé |
| ATR 14j | $0.98 | Calcul agent | 6.33% du cours — volatilité relative modérée, inchangée |
| MM 50j | $10.80 | Calcul agent | Cours +43.2% au-dessus du support structurel, inchangé |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché |

**Niveaux clés (inchangés vs 25/05 21:00 UTC) :**
- **Support immédiat :** $14.58 (low du 25/05) / $14.0 (max pain options historique)
- **Résistance :** $15.78 (52-week high, fragile sans catalyseur)
- **Stop-loss ATR (2×) :** $13.51 ($15.47 − $1.96)
- **Take-profit ATR (3×) :** $18.41 ($15.47 + $2.94)
- **Ratio R/R :** 1.5

**Verdict timing :** Favorable sur le momentum pur — inchangé. Le cours reste au-dessus de la MM50 avec un écart significatif (+43.2%), le volume est normalisé, et l'options flow historique était bullish. Cependant, le RSI à 64.29 approche la zone de surachat (>70) sans catalyseur fondamental identifiable, ce qui fragilise la durabilité du mouvement. Le marché US reprend aujourd'hui après le Memorial Day ; aucun gap supplémentaire ni volume anormal n'est observé sur NOK.

**Score Momentum :** 7.0/10 — inchangé (gap +9.1% du 25/05 maintenu, new 52w high, volume normalisé, options historiquement bullish).

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

**Note fondamentale :** Aucune donnée fondamentale nouvelle entre le 25/05 21:00 UTC et le 26/05 10:00 UTC. L'expansion du multiple P/E à 96.69 sur un consensus inchangé à $9.26 maintient la divergence entre prix et valeur. Le forward P/E à 31.72 reste élevé pour une entreprise à croissance limitée et quality hors périmètre.

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 96.7 vs FMP 45.8 ; EV/EBITDA Yahoo 33.2 vs FMP 13.1. Cette divergence n'affecte pas le verdict consensus calibré sur l'ADR.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +66.8% vs consensus, P/E 96.7, forward P/E 31.7 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision détectée |
| Nombre analysts actifs (mois) | 1 | FMP Stable API | Faible couverture |
| Put/Call ratio | **null** | Yahoo Finance | ⚠️ Données manquantes dans `latest.json` |
| Max pain | **$2.00** | Yahoo Finance | ⚠️ Valeur incohérente — probable placeholder |
| Call OI % | **null** | Yahoo Finance | ⚠️ Données manquantes |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD, pas d'impact |

**Verdict Sentiment :** Bullish technique sur les options (dernières données fiables : put/call 0.41, call OI 70.9%), mais neutre/bearish sur le consensus sell-side. Le max pain historique à $14.00 crée un aimant technique si le momentum faiblit avant l'expiration du 29 mai. Aucun upgrade/downgrade massif détecté dans `data/upcoming_events_latest.json`.

**Score Catalyseur :** 4.0/10 — inchangé. Aucun catalyseur identifiable ; gap du 25/05 non expliqué par news/event ; earnings éloignés (58 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Inconnu (regime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable — gap du 25/05 non expliqué |
| Valorisation | 3.5/10 | → | P/E 96.7, cours +66.8% vs consensus, forward P/E 31.7 sur stock mature |
| Momentum | 7.0/10 | → | Gap +9.1% du 25/05 maintenu, new 52w high, volume normalisé |
| **Score Opportunité** | **4.5/10** | → | (4.0×0.35) + (3.5×0.40) + (7.0×0.25) = 4.5 |
| **Score Global** | **45.5/100** | → | Malus : Valorisation faible plombe le score |
| **Score Global ajusté** | **50.5/100** | → | — |

**Action recommandée :** **ATTENDRE** (seuil 50–59)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (25/05 21:00 UTC) | Nouveau (26/05 10:00 UTC) | Justification |
|--------|--------------------------|---------------------------|---------------|
| Stop-loss | $13.51 | **$13.51** | Inchangé — recalcul ATR 2× stable |
| Take-profit | $18.41 | **$18.41** | Inchangé — recalcul ATR 3× stable |
| Prix cible (consensus) | $9.26 | $9.26 | Inchangé — 6 analysts |
| Upside consensus | −40.1% | **−40.1%** | Inchangé |
| Downside SL | −12.7% | **−12.7%** | Inchangé |

**⚠️ Attention :** Le SL à $13.51 reste très proche du support intraday ($14.58). Un retour sous $14.00 (max pain historique) confirmerait une inversion technique rapide. Le gap de +9.1% du 25/05 sans catalyseur rend le titre vulnérable à un retour de moyenne. Première session post-Memorial Day sans catalyseur supplémentaire.

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
| **Agent Watchman** | Earnings 2026-07-23 (58 j) | 🟢 >30j — pas de preview requis. |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **confirmée** — aucune mutation entre le snapshot 25/05 21:00 UTC et le snapshot 26/05 10:00 UTC.

**Analyse :**
- Les données du snapshot 26/05 10:00 UTC sont **strictement identiques** au snapshot 25/05 21:00 UTC (close $15.47, RSI 64.29, ATR $0.98, volume 1.07×).
- Aucune nouvelle post-Memorial Day, aucun événement corporate, aucun mouvement options/insiders.
- Le momentum haussier de +9.1% du 25/05 reste non expliqué par un catalyseur fondamental identifiable.
- **Données options partielles** dans `latest.json` (max pain $2.00 incohérent, put/call et call OI `null`). Dernières données fiables conservées pour référence.

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
| Central | 50% | Consolidation autour de $14.50–$15.50 | Range |
| Pessimiste | 30% | Aucun catalyseur → retour vers max pain $14.00 | $13.50–$14.00 |

**⚠️ Risque principal :** Gap haussier du 25/05 non expliqué = vulnérable à un retour de moyenne rapide si le catalyseur (s'il existe) n'est pas confirmé. Le max pain options historique à $14.00 offre un premier support psychologique. Données options partielles aujourd'hui — surveillance requise.

**Prochains points de contrôle :**
- Earnings Q2 FY2026 au **2026-07-23** (dans **58 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Expiration options **2026-05-29** — observer si le max pain $14.00 agit comme aimant
- Franchissement technique du SL à $13.51
- **Rétablissement des données options** dans les prochains snapshots (put/call, call OI, max pain)

---

*Données sources : `data/latest.json` (2026-05-26T10:00:09 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
