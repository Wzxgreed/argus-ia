# FLY — Mise à Jour Quotidienne (2026-05-18) — Session 21:00 UTC

> Source : `data/latest.json` (2026-05-18 21:00 UTC) + `data/recommandations_latest.json` + agents quant / geo / sector / social / FX / events / upcoming.
> DRAFT_refresh actif (triggers PRICE_GAP +8.71%, ATR_SPIKE 9.99%) traité et intégré ci-dessous.

---

## Résumé des changements depuis l'analyse précédente (2026-05-18 20:12 UTC)

| Métrique | Session 20:12 UTC | Session 21:00 UTC | Variation | Seuil d'alerte |
|----------|-------------------|-------------------|-----------|----------------|
| Cours close | $43.95 | **$43.95** | **0.00%** | ≥ ±5% |
| Change vs prior close | +8.71% | **+8.71%** | stable | — |
| RSI 14j | 67.08 | **67.08** | stable | >70 / <30 |
| MM 50j | $32.72 | $32.72 | stable | — |
| MM 200j | N/A | N/A | — | — |
| ATR 14j | $4.39 | $4.39 | stable | >5% relatif |
| Volume 20j moy. | 6,239,757 | **6,239,757** | stable | — |
| Volume jour | 9,789,240 | **9,789,240** | stable | — |
| Volume relatif | 1.57× moy. | **1.57× moy.** | stable | >2.0× |
| Filtre Qualité | 2/6 | 2/6 | stable | — |
| Forward P/E | -38.50 | **-38.50** | stable | — |
| P/B (Yahoo) | 6.37 | **6.37** | stable | — |
| EV/Revenue (Yahoo) | 32.34x | **32.34x** | stable | — |
| Consensus PT | $42.45 | $42.45 | stable | — |
| Upside consensus | -3.4% | -3.4% | stable | — |
| Max Pain | $25.00 | $25.00 | stable | — |
| Put/Call Ratio | 0.86 | 0.86 | stable | — |
| Short Interest | 0.0866% | 0.0866% | stable | >5% |
| Score Opportunité | 5.3/10 | **5.3/10** | stable | — |
| Score Valorisation | 4.5/10 | 4.5/10 | stable | — |
| Score Catalyseur | 5.0/10 | 5.0/10 | stable | — |
| Score Momentum | 7.0/10 | 7.0/10 | stable | — |
| Score Global | 53.0 | **53.0** | stable | — |
| Score Global Ajusté | 58.0 | **58.0** | stable | — |

**Observations clés :**
- **Aucun changement de données** entre la session 20:12 UTC et le snapshot 21:00 UTC (`fetched_at` 21:00:02, timestamp ticker 21:00:09). Le cours, le volume, les indicateurs techniques et les fondamentaux sont strictement identiques.
- **DRAFT_refresh** (triggers PRICE_GAP +8.71%, ATR_SPIKE 9.99%) est le même événement déjà analysé en session 17:00 UTC et consolidé à 20:12 UTC. Pas de nouvel événement structurel post-session.
- **Agent Quant** : `data/quant_report_latest.json` du 2026-05-17 — pas assez de signaux historiques → [SIGNAUX NON SIGNIFICATIFS] (p-value 1.0).
- **Agent Accounting** : `data/accounting_risk_latest.json` absent → [DONNÉES MANQUANTES] pour M-Score / Z-Score / F-Score / Sloan.
- **Agent Géo** : FLY non flaggé — pas d'exposition politique spécifique.
- **Agent Event-Driven** : 0 événement corporate détecté dans `data/events_latest.json`.
- **Agent Social** : 0 mentions Reddit, 0.0 sentiment, pump non détecté.

---

## Mise à jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 67.08 | Haussier, proche du surachat (>70) — momentum stable en zone élevée |
| MM 50j | $32.72 | Cours supérieur de **+34.3%**, tendance haussière intacte |
| MM 200j | N/A | Donnée indisponible — impossible de valider le Golden/Death Cross |
| Volume | 9,789,240 | 1.57× moy. 20j — volume en accélération post-gap inchangé |
| ATR 14j | $4.39 | Relatif 10.0% — volatilité élevée, inchangée |
| Range jour | $42.34–$47.71 | Amplitude **12.3%** sans catalyst visible — comportement spéculatif |
| Support 1 | $32.72 (MM50) | Support dynamique — rupture = révision baissière |
| Support 2 | $16.00 (52W Low) | — |
| Résistance 1 | $47.71 (High du jour) | Testé en séance, non confirmé en close |
| Résistance 2 | $73.80 (52W High) | — |

**Timing verdict :** **Favorable mais risqué** — tendance haussière intacte (cours > MM50 +34.3%), RSI en zone haussière. La consolidation au-dessus de $43 après le gap de +8.71% est un signal technique positif. Proximité de l'expiration options (22/05) maintient le risque de microstructure élevé.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale qualitative depuis la session 20:12 UTC. Données croisées Yahoo / FMP (annual FY 2025) :

| Métrique | Yahoo | FMP | Commentaire |
|----------|-------|-----|-------------|
| Market Cap | $7.04B | $3.40B | Divergence matérielle — Yahoo utilise close actuel, FMP données historiques |
| Forward P/E | -38.50 | — | Pas de rentabilité nette attendue |
| EV/EBITDA | -26.61 | -13.12 | EBITDA négatif sur les deux sources |
| P/B | 6.37 | 2.86 | Divergence — Yahoo plus conservateur |
| EV/Revenue (Yahoo) | 32.34x | — | Multiple élevé |
| P/S (FMP) | — | 21.26x | — |
| Gross Margin | — | 15.6% | Faible |
| Operating Margin | — | -154.3% | Fortement négatif |
| EBITDA Margin | — | -138.9% | Fortement négatif |
| Net Margin | — | -186.6% | Fortement négatif |
| Debt/Equity | — | 0.26 | Levier modéré |
| Current Ratio | — | 4.51 | Liquidité solide |
| Short Interest | 0.0866% | — | Aucun pari baissier structuré |

**Filtre Qualité** : **2/6** (🔴 Hors périmètre)
| Critère | Verdict |
|---------|---------|
| Revenue CAGR 5 ans ≥ 20% | ❌ Données insuffisantes dans le snapshot |
| Profit CAGR 5 ans ≥ 20% | ❌ Forward P/E -38.50, marges négatives |
| Assets/Liabilities > 1.0 | ⚠️ Current Ratio 4.51 (solide) mais pas de visibilité complète sur le bilan |
| FCF positif et croissant 5 ans | ❌ FCF yield négatif (-7.0% environ, price_to_fcf -14.29) |
| Avantage compétitif (moat) | ❌ Non démontré dans les données |
| Industrie forte croissance (TAM ×5) | ❌ Données insuffisantes |

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10 avant calcul final. L'agent recommandation applique **4.5/10**.

---

## Mise à jour sentiment / options / news

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-3.4%) — plus de upside selon le consensus. Couverture stable. |
| Max Pain | $25.00 | Yahoo Finance | Écart de **43%** sous le spot. Distorsion probable liée à l'expiration du 22/05. |
| Put/Call Ratio | 0.86 | Yahoo Finance | Légèrement call-biased (53.8% call OI). |
| Call OI % | 53.8% | Yahoo Finance | Biais call modéré. |
| Short Interest | 0.0866% | Yahoo Finance | Absence de squeeze setup. |
| Social Sentiment | 0 mentions, 0.0 score | `data/social_sentiment_latest.json` | Aucune activité retail détectée sur Reddit. Pump non détecté. |
| Event-Driven | Aucun | `data/events_latest.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (78 jours) | `data/upcoming_events_latest.json` | Est EPS -$0.60 à -$0.45, Rev $0.1B. |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immédiat. Le prochain catalyst structurel est l'earnings d'août.

---

## Scoring global (Agent Recommandation — 2026-05-18 21:00 UTC)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 7.0/10 | 25% | 1.75 |
| **Score Opportunité** | **5.3/10** | | |
| Malus/Bonus | +4.5 pts | | (pas de malus accounting/geo/FX majeur) |
| **Score Global** | **53.0** | | |
| **Score Global Ajusté** | **58.0** | | |

**Action** : **ATTENDRE**
**Direction** : Neutre
**Timing** : Favorable (technique) mais risqué
**Horizon** : —

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant) → pas d'ajustement.
- **Agent Géo** : FLY non flaggé (pas d'exposition politique spécifique détectée) → pas de malus.
- **Agent Sector Rotation** : XLI (Industrials) sous-performant le SPY sur 20j (-1.81%) et 60j (-3.40%), momentum_score 0.0 → **headwind sectoriel** (-0.5 pt implicite sur le catalyseur sectoriel).
- **Agent Social** : Pas d'activité retail → neutre.
- **Agent FX** : Exposition 25%, currency USD, fx_impact_score 0.0, divergence aligned → pas d'ajustement.
- **Agent Event-Driven** : 0 événement → neutre.

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $43.95 | Close 2026-05-18 21:00 UTC | Inchangé vs session 20:12 UTC, +8.71% vs prior close |
| Stop-loss | $35.17 | Cours − 2×ATR ($4.39) | Inchangé — ATR stable |
| Take-profit | $57.12 | Cours + 3×ATR ($4.39) | Inchangé — ATR stable |
| Ratio R/R | 1.5:1 | Gain $13.17 / Perte $8.78 | Inchangé |

Les niveaux sont inchangés car l'ATR est stable à $4.39. Le ratio 1.5:1 reste limité pour une action sans rentabilité démontrée et avec un Filtre Qualité faible (2/6).

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : Thèse CONFIRMÉE — aucun changement matériel entre la session 20:12 UTC et le snapshot 21:00 UTC.**

Le snapshot 21:00 UTC est issu du même batch de données que la session 20:12 UTC (`timestamp` 21:00:09 vs données identiques). **Aucun nouveau cours, volume, ni indicateur technique n'a été enregistré.** Le DRAFT_refresh actif (PRICE_GAP +8.71%, ATR_SPIKE 9.99%) reflète le même événement déjà traité et consolidé dans `FLY_2026-05-18_update.md` (session 20:12 UTC).

**Ce qui confirme la thèse :**
- Cours stable post-gap, consolidant au-dessus de $43 — momentum intact.
- RSI 67.08, MM50 $32.72 — tendance haussière technique confirmée.
- Aucune news structurante, guidance raise, ou événement corporate détecté dans les agents events / geo / social.
- Scoring global inchangé (53.0 / 58.0 ajusté) — pas de bascule de zone.

**Ce qui maintient la prudence :**
- Filtre Qualité inchangé à 2/6 (🔴 Hors périmètre) — pas de quality compounding.
- Marges négatives, forward P/E -38.50, EV/Revenue 32x — valorisation incompatible avec les fondamentaux.
- Consensus PT $42.45 sous le spot (-3.4% upside) — plus de marge de sécurité selon les analystes.
- Headwind sectoriel : XLI sous-performe le SPY (momentum_score 0.0).
- Volatilité élevée sans couverture fondamentale (ATR 10%) — risque de correction rapide si le momentum casse.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 78 jours) : Est EPS -$0.45 à -$0.60, Rev $0.1B. Toute surprise positive vs consensus négatif serait un catalyseur majeur.
2. **Expiration options 22/05** (4 jours) : surveillance post-expiration pour voir si la volatilité se normalise et si le Max Pain redevient cohérent avec le spot.

**Risques :**
1. Rentabilité non démontrée — la société brûle du cash avec des marges fortement négatives (operating margin -154%, net margin -187%).
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 32x, P/B 6.37x).
3. Cours au-dessus du consensus analystes — si les résultats ne suivent pas, le gap de valorisation se resserrera brutalement.
4. Volume en accélération post-gap peut indiquer du profit-taking ou de la distribution institutionnelle ; à surveiller sur les prochaines sessions.

**Prochaine étape :**
- Maintenir **ATTENDRE**. Aucune position recommandée.
- Surveiller l'approche des earnings (août) et toute amélioration des marges ou du FCF dans les prochains filings.
- Si le cours casse la MM50 ($32.72) → réviser la thèse à la baisse.
- Si un catalyst fondamental émerge (contrat, partnership, guidance raise) → réévaluer le Score Catalyseur et le Filtre Qualité.
