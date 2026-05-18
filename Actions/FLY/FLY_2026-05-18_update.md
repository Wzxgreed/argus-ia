# FLY — Mise à Jour Quotidienne (2026-05-18) — Session 17:00 UTC

> Source : `data/latest.json` (2026-05-18 17:00 UTC) + `data/recommandations_latest.json` + agents quant / geo / sector / social / FX / events / upcoming.
> FULL REFRESH déclenché par PRICE_GAP +8.11% et ATR_SPIKE 10.04% — traité ci-dessous.

---

## Résumé des changements depuis l'analyse précédente (2026-05-18 13:00 UTC)

| Métrique | Session 13:00 UTC | Session 17:00 UTC | Variation | Seuil d'alerte |
|----------|-------------------|-------------------|-----------|----------------|
| Cours close | $40.43 | **$43.71** | **+8.11%** | ≥ ±5% |
| Change vs prior close | -4.6% | **+8.11%** | inversion | — |
| RSI 14j | 61.71 | **66.80** | **+5.1 pts** | >70 / <30 |
| MM 50j | $32.24 | **$32.72** | +$0.48 | — |
| MM 200j | N/A | N/A | — | — |
| ATR 14j | $4.02 | **$4.39** | **+9.2%** | >5% relatif |
| Volume 20j moy. | 5,994,630 | 6,107,093 | +2.1% | — |
| Volume jour | 8,219,100 | 7,135,963 | -13.2% | — |
| Volume relatif | 1.37× moy. | **1.17× moy.** | -0.20× | >2.0× |
| Filtre Qualité | 2/6 | 2/6 | stable | — |
| Forward P/E | -35.41 | **-38.29** | négatif accentué | — |
| EV/Revenue (Yahoo) | 32.34x | 32.34x | stable | — |
| P/B (Yahoo) | 5.86 | **6.33** | +8.0% | — |
| Consensus PT | $42.45 | $42.45 | stable | — |
| Upside consensus | +5.0% | **-2.9%** | **sous le spot** | — |
| Max Pain | $25.00 | $25.00 | stable | — |
| Put/Call Ratio | 0.86 | 0.86 | stable | — |
| Short Interest | 0.09% | 0.09% | stable | >5% |
| Score Opportunité | 5.0/10 | **5.3/10** | +0.3 pt | — |
| Score Valorisation | 4.5/10 | 4.5/10 | stable | — |
| Score Catalyseur | 5.0/10 | 5.0/10 | stable | — |
| Score Momentum | 6.0/10 | **7.0/10** | **+1.0 pt** | — |
| Score Global | 50.5 | **53.0** | +2.5 pts | — |
| Score Global Ajusté | 55.5 | **58.0** | +2.5 pts | — |

**Observations clés :**
- **Cours +8.11%** sur la session, franchissant le seuil d'alerte ±5% — gap haussier overnight puis consolidation autour de $43.71.
- **RSI 66.8** — zone haussière, se rapprochant du seuil de surachat (>70).
- **Consensus PT $42.45 désormais sous le spot** (-2.9% upside) : le cours a dépassé la cible moyenne des 11 analystes couvrant le titre. Il n'y a plus de marge de sécurité de valorisation selon le consensus.
- **ATR $4.39 (10.0% relatif)** — volatilité persistante et élevée, sans catalyst structurel identifié.
- **Range intraday $42.34–$47.71** (amplitude 12.8%) — comportement spéculatif ou lié à la microstructure options (expiration 22/05 proche).
- **Agent Quant** : pas assez de signaux historiques → [SIGNAUX NON SIGNIFICATIFS] (p-value 1.0).
- **Agent Accounting** : `data/accounting_risk_latest.json` absent → [DONNÉES MANQUANTES] pour M-Score / Z-Score / F-Score / Sloan.
- **Agent Géo** : FLY non flaggé — pas d'exposition politique spécifique.
- **Agent Event-Driven** : 0 événement corporate détecté.
- Aucune news structurante détectée sur la session.

---

## Mise à jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 66.80 | Haussier, proche du surachat (>70) — momentum en accélération |
| MM 50j | $32.72 | Cours supérieur de **+33.6%**, tendance haussière renforcée |
| MM 200j | N/A | Donnée indisponible — impossible de valider le Golden/Death Cross |
| Volume | 7,135,963 | 1.17× moy. 20j — volume soutenu mais en retrait vs session matinale |
| ATR 14j | $4.39 | Relatif 10.0% — volatilité élevée, inchangée de tendance |
| Range jour | $42.34–$47.71 | Amplitude **12.8%** sans catalyst visible — comportement spéculatif |
| Support 1 | $32.72 (MM50) | Support dynamique — rupture = révision baissière |
| Support 2 | $16.00 (52W Low) | — |
| Résistance 1 | $47.71 (High du jour) | Testé en séance, non confirmé en close |
| Résistance 2 | $73.80 (52W High) | — |

**Timing verdict :** **Favorable mais risqué** — tendance haussière intacte et renforcée (cours > MM50 +33.6%), RSI en zone haussière. Cependant, la volatilité intrajournalière (12.8%) sans catalyst apparent et la proximité de l'expiration options (22/05) augmentent le risque de microstructure. Le consensus PT sous le spot élimine la marge de sécurité de valorisation.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale qualitative depuis l'initiale. Rappel des métriques clés avec sources croisées Yahoo / FMP :

| Métrique | Yahoo | FMP | Commentaire |
|----------|-------|-----|-------------|
| Market Cap | $7.00B | $3.40B | Divergence majeure — préférer Yahoo (close × shares out.) |
| Forward P/E | -38.29 | — | Pas de rentabilité nette attendue |
| EV/EBITDA | -26.61 | -13.12 | EBITDA négatif sur les deux sources |
| P/B | 6.33 | 2.86 | Divergence matérielle — Yahoo plus conservateur |
| EV/Revenue | 32.34x | — | Multiple élevé |
| P/S (FMP) | — | 21.26x | — |
| Gross Margin | — | 15.6% | Faible |
| Operating Margin | — | -154.3% | Fortement négatif |
| EBITDA Margin | — | -138.9% | Fortement négatif |
| Net Margin | — | -186.6% | Fortement négatif |
| Debt/Equity | — | 0.26 | Levier modéré |
| Current Ratio | — | 4.51 | Liquidité solide |
| Short Interest | 0.09% | — | Aucun pari baissier structuré |

**Filtre Qualité** : **2/6** (🔴 Hors périmètre)
| Critère | Verdict |
|---------|---------|
| Revenue CAGR 5 ans ≥ 20% | ❌ Données insuffisantes |
| Profit CAGR 5 ans ≥ 20% | ❌ Forward P/E -38.29, marges négatives |
| Assets/Liabilities > 1.0 | ⚠️ Current Ratio 4.51 (solide) mais pas de visibilité complète sur le bilan |
| FCF positif et croissant 5 ans | ❌ FCF yield négatif (-7.0% environ) |
| Avantage compétitif (moat) | ❌ Non démontré dans les données |
| Industrie forte croissance (TAM ×5) | ❌ Données insuffisantes |

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10 avant calcul final. L'agent recommandation applique **4.5/10**.

---

## Mise à jour sentiment / options / news

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **sous le spot** (-2.9%) — plus de upside selon le consensus. Couverture stable. |
| Max Pain | $25.00 | Yahoo Finance | Écart de **43%** sous le spot. Distorsion probable liée à l'expiration du 22/05. |
| Put/Call Ratio | 0.86 | Yahoo Finance | Légèrement call-biased (53.8% call OI). |
| Call OI % | 53.8% | Yahoo Finance | Biais call modéré. |
| Short Interest | 0.09% | Yahoo Finance | Absence de squeeze setup. |
| Social Sentiment | 0 mentions, 0.0 score | `data/social_sentiment_latest.json` | Aucune activité retail détectée sur Reddit. Pump non détecté. |
| Event-Driven | Aucun | `data/events_latest.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (78 jours) | `data/upcoming_events_latest.json` | Est EPS -$0.60 à -$0.45, Rev $0.1B. |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immédiat. Le prochain catalyst structurel est l'earnings d'août.

---

## Scoring global (Agent Recommandation — 2026-05-18 17:00 UTC)

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
- **Agent Sector Rotation** : XLI (Industrials) sous-performant le SPY sur 20j (-2.17%) et 60j (-3.74%), momentum_score 0.0 → **headwind sectoriel** (-0.5 pt implicite sur le catalyseur sectoriel).
- **Agent Social** : Pas d'activité retail → neutre.
- **Agent FX** : Exposition 25%, currency USD, fx_impact_score 0.0 → pas d'ajustement.
- **Agent Event-Driven** : 0 événement → neutre.

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $43.71 | Close 2026-05-18 17:00 UTC | +8.11% vs session matinale |
| Stop-loss | $34.93 | Cours − 2×ATR ($4.39) | Recalculé avec ATR actualisé |
| Take-profit | $56.88 | Cours + 3×ATR ($4.39) | Recalculé avec ATR actualisé |
| Ratio R/R | 1.5:1 | Gain $13.17 / Perte $8.78 | Inchangé malgré la hausse du cours |

Les niveaux ont été révisés à la hausse en raison du nouveau close ($43.71) et de l'ATR plus élevé ($4.39). Le ratio 1.5:1 reste limité pour une action sans rentabilité démontrée et avec un Filtre Qualité faible.

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : Thèse MODIFIÉE avec nuance haussière technique.**

L'analyse initiale du 2026-05-17 concluait à un profil **ATTENDRE** en raison d'un momentum technique favorable mais de fondamentaux insuffisants. Le FULL REFRESH du 2026-05-18 (triggers PRICE_GAP +8.11% et ATR_SPIKE 10.04%) révèle une accélération technique significative : le cours a gagné +8.11% sur la session, testé un intraday à $47.71 (+18% vs close précédent), et le RSI est monté à 66.8. Cependant, **aucun fondamental n'a changé** pour justifier ce mouvement.

**Ce qui modifie la thèse :**
- Cours a dépassé le consensus analystes ($42.45 → upside négatif de -2.9%), éliminant la marge de sécurité de valorisation.
- RSI proche du surachat (66.8) et range intraday de 12.8% — le risque de correction technique augmente.
- Volatilité persistante (ATR 10%) sans catalyst visible — comportement probablement lié à la microstructure options (expiration 22/05).

**Ce qui confirme la prudence :**
- Filtre Qualité inchangé à 2/6 (🔴 Hors périmètre) — pas de quality compounding.
- Marges négatives, forward P/E -38.29, EV/Revenue 32x — valorisation incompatible avec les fondamentaux.
- Aucune news structurante, guidance raise, ou événement corporate n'a été détecté.
- Headwind sectoriel : XLI sous-performe le SPY (momentum_score 0.0).

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 78 jours) : Est EPS -$0.45 à -$0.60, Rev $0.1B. Toute surprise positive vs consensus négatif serait un catalyseur majeur.
2. **Expiration options 22/05** : surveillance post-expiration pour voir si la volatilité se normalise et si le Max Pain redevient cohérent.

**Risques :**
1. Rentabilité non démontrée — la société brûle du cash avec des marges fortement négatives (operating margin -154%, net margin -187%).
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 32x, P/B 6.33x).
3. Cours au-dessus du consensus analystes — si les résultats ne suivent pas, le gap de valorisation se resserrera brutalement.
4. Volatilité élevée sans couverture fondamentale = risque de correction rapide si le momentum technique casse (rupture MM50 $32.72).

**Prochaine étape :**
- Maintenir **ATTENDRE**. Aucune position recommandée.
- Surveiller l'approche des earnings (août) et toute amélioration des marges ou du FCF dans les prochains filings.
- Si le cours casse la MM50 ($32.72) → réviser la thèse à la baisse.
- Si un catalyst fondamental émerge (contrat, partnership, guidance raise) → réévaluer le Score Catalyseur et le Filtre Qualité.
