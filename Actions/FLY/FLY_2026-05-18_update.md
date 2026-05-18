# FLY — Mise à Jour Quotidienne (2026-05-18) — Session 20:12 UTC

> Source : `data/latest.json` (2026-05-18 20:12 UTC) + `data/recommandations_latest.json` + agents quant / geo / sector / social / FX / events / upcoming.
> FULL REFRESH triggers (PRICE_GAP +8.71%, ATR_SPIKE 9.99%) déjà traités dans la session 17:00 UTC — pas de nouvel événement majeur post-session.

---

## Résumé des changements depuis l'analyse précédente (2026-05-18 17:00 UTC)

| Métrique | Session 17:00 UTC | Session 20:12 UTC | Variation | Seuil d'alerte |
|----------|-------------------|-------------------|-----------|----------------|
| Cours close | $43.71 | **$43.95** | **+0.55%** | ≥ ±5% |
| Change vs prior close | +8.11% | **+8.71%** | +0.60 pt | — |
| RSI 14j | 66.80 | **67.08** | +0.28 pt | >70 / <30 |
| MM 50j | $32.72 | $32.72 | stable | — |
| MM 200j | N/A | N/A | — | — |
| ATR 14j | $4.39 | $4.39 | stable | >5% relatif |
| Volume 20j moy. | 6,107,093 | **6,239,757** | +2.2% | — |
| Volume jour | 7,135,963 | **9,789,240** | **+37.2%** | — |
| Volume relatif | 1.17× moy. | **1.57× moy.** | **+0.40×** | >2.0× |
| Filtre Qualité | 2/6 | 2/6 | stable | — |
| Forward P/E | -38.29 | **-38.50** | négatif accentué | — |
| P/B (Yahoo) | 6.33 | **6.37** | +0.6% | — |
| Consensus PT | $42.45 | $42.45 | stable | — |
| Upside consensus | -2.9% | -3.4% | **sous le spot** | — |
| Max Pain | $25.00 | $25.00 | stable | — |
| Put/Call Ratio | 0.86 | 0.86 | stable | — |
| Short Interest | 0.09% | **0.0866%** | stable | >5% |
| Score Opportunité | 5.3/10 | **5.3/10** | stable | — |
| Score Valorisation | 4.5/10 | 4.5/10 | stable | — |
| Score Catalyseur | 5.0/10 | 5.0/10 | stable | — |
| Score Momentum | 7.0/10 | 7.0/10 | stable | — |
| Score Global | 53.0 | **53.0** | stable | — |
| Score Global Ajusté | 58.0 | **58.0** | stable | — |

**Observations clés :**
- **Cours stable post-gap** (+0.55% vs 17:00 UTC) après le gap haussier de +8.71% overnight. Le titre consolide au-dessus de $43.
- **Volume en nette accélération** : 9.79M (1.57× moy. 20j) vs 7.14M en session 17:00 — signe que le gap a attiré des flux additionnels en fin de journée.
- **RSI 67.08** — inchangé de tendance, zone haussière proche du surachat (>70) sans l'atteindre.
- **Consensus PT $42.45 désormais 3.4% sous le spot** : le cours a dépassé la cible moyenne des 11 analystes. Pas de marge de sécurité de valorisation.
- **Agent Quant** : pas assez de signaux historiques → [SIGNAUX NON SIGNIFICATIFS] (p-value 1.0).
- **Agent Accounting** : `data/accounting_risk_latest.json` absent → [DONNÉES MANQUANTES] pour M-Score / Z-Score / F-Score / Sloan.
- **Agent Géo** : FLY non flaggé — pas d'exposition politique spécifique.
- **Agent Event-Driven** : 0 événement corporate détecté.
- Aucune news structurante détectée sur la session soir.

---

## Mise à jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 67.08 | Haussier, proche du surachat (>70) — momentum stable en zone élevée |
| MM 50j | $32.72 | Cours supérieur de **+34.3%**, tendance haussière intacte |
| MM 200j | N/A | Donnée indisponible — impossible de valider le Golden/Death Cross |
| Volume | 9,789,240 | 1.57× moy. 20j — volume en accélération post-gap |
| ATR 14j | $4.39 | Relatif 10.0% — volatilité élevée, inchangée de tendance |
| Range jour | $42.34–$47.71 | Amplitude **12.3%** sans catalyst visible — comportement spéculatif |
| Support 1 | $32.72 (MM50) | Support dynamique — rupture = révision baissière |
| Support 2 | $16.00 (52W Low) | — |
| Résistance 1 | $47.71 (High du jour) | Testé en séance, non confirmé en close |
| Résistance 2 | $73.80 (52W High) | — |

**Timing verdict :** **Favorable mais risqué** — tendance haussière intacte (cours > MM50 +34.3%), RSI en zone haussière. La consolidation au-dessus de $43 après le gap est un signal technique positif. Cependant, la volatilité intrajournalière (12.3%) sans catalyst apparent et la proximité de l'expiration options (22/05) maintiennent le risque de microstructure élevé. Le consensus PT sous le spot élimine la marge de sécurité de valorisation.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale qualitative depuis la session 17:00 UTC. Rappel des métriques clés avec sources croisées Yahoo / FMP :

| Métrique | Yahoo | FMP | Commentaire |
|----------|-------|-----|-------------|
| Market Cap | $7.04B | — | — |
| Forward P/E | -38.50 | — | Pas de rentabilité nette attendue |
| EV/EBITDA | -26.61 | -13.12 | EBITDA négatif sur les deux sources |
| P/B | 6.37 | 2.86 | Divergence matérielle — Yahoo plus conservateur |
| EV/Revenue | 32.34x | — | Multiple élevé |
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
| Revenue CAGR 5 ans ≥ 20% | ❌ Données insuffisantes |
| Profit CAGR 5 ans ≥ 20% | ❌ Forward P/E -38.50, marges négatives |
| Assets/Liabilities > 1.0 | ⚠️ Current Ratio 4.51 (solide) mais pas de visibilité complète sur le bilan |
| FCF positif et croissant 5 ans | ❌ FCF yield négatif (-7.0% environ) |
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

## Scoring global (Agent Recommandation — 2026-05-18 20:12 UTC)

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
- **Agent Sector Rotation** : XLI (Industrials) sous-performant le SPY sur 20j (-1.82%) et 60j (-3.40%), momentum_score 0.0 → **headwind sectoriel** (-0.5 pt implicite sur le catalyseur sectoriel).
- **Agent Social** : Pas d'activité retail → neutre.
- **Agent FX** : Exposition 25%, currency USD, fx_impact_score 0.0 → pas d'ajustement.
- **Agent Event-Driven** : 0 événement → neutre.

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $43.95 | Close 2026-05-18 20:12 UTC | +0.55% vs session 17:00 UTC, +8.71% vs prior close |
| Stop-loss | $35.17 | Cours − 2×ATR ($4.39) | Inchangé — ATR stable |
| Take-profit | $57.12 | Cours + 3×ATR ($4.39) | Inchangé — ATR stable |
| Ratio R/R | 1.5:1 | Gain $13.17 / Perte $8.78 | Inchangé malgré la légère hausse du cours |

Les niveaux sont inchangés car l'ATR est stable à $4.39. Le ratio 1.5:1 reste limité pour une action sans rentabilité démontrée et avec un Filtre Qualité faible.

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : Thèse CONFIRMÉE — pas de changement matériel vs session 17:00 UTC.**

L'analyse de la session 17:00 UTC concluait à un profil **ATTENDRE** avec momentum technique favorable mais fondamentaux insuffisants. Le snapshot 20:12 UTC confirme cette lecture : le cours a légèrement grignoté +0.55% ($43.71 → $43.95) sur un volume en accélération (+37.2%), mais **aucun fondamental n'a changé** et aucun catalyst structurel n'est apparu.

**Ce qui confirme la thèse :**
- Cours stable post-gap, consolidant au-dessus de $43 — momentum intact.
- RSI 67.08, MM50 $32.72 — tendance haussière technique confirmée.
- Aucune news structurante, guidance raise, ou événement corporate détecté.
- Scoring global inchangé (53.0 / 58.0 ajusté) — pas de bascule de zone.

**Ce qui maintient la prudence :**
- Filtre Qualité inchangé à 2/6 (🔴 Hors périmètre) — pas de quality compounding.
- Marges négatives, forward P/E -38.50, EV/Revenue 32x — valorisation incompatible avec les fondamentaux.
- Consensus PT $42.45 sous le spot (-3.4% upside) — plus de marge de sécurité selon les analystes.
- Headwind sectoriel : XLI sous-performe le SPY (momentum_score 0.0).
- Volatilité élevée sans couverture fondamentale (ATR 10%) — risque de correction rapide si le momentum casse.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 78 jours) : Est EPS -$0.45 à -$0.60, Rev $0.1B. Toute surprise positive vs consensus négatif serait un catalyseur majeur.
2. **Expiration options 22/05** : surveillance post-expiration pour voir si la volatilité se normalise et si le Max Pain redevient cohérent.

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
