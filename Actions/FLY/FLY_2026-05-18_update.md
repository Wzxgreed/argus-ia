# FLY — Mise à Jour Quotidienne (2026-05-18)

> Source : `data/latest.json` (2026-05-18) + `data/recommandations_latest.json` + agents quant / geo / sector / social / FX / events / upcoming.

---

## Résumé des changements depuis l'analyse précédente (2026-05-17)

| Métrique | 2026-05-17 (init) | 2026-05-18 (update) | Variation | Seuil d'alerte |
|----------|-------------------|---------------------|-----------|----------------|
| Cours close | $40.43 | $40.43 | 0.0% | — |
| Change vs prior close | — | -4.6% | — | ≥ ±5% |
| RSI 14j | 61.71 | 61.71 | stable | >70 / <30 |
| MM 50j | $32.24 | $32.24 | stable | — |
| MM 200j | N/A | N/A | — | — |
| ATR 14j | $4.02 | $4.02 | stable | >5% relatif |
| Volume 20j moy. | 5,994,630 | 5,994,630 | stable | — |
| Volume jour | 8,219,100 | 8,219,100 | 1.37× moy. | >2.0× |
| Filtre Qualité | 2/6 | 2/6 | stable | — |
| Forward P/E | -35.41 | -35.41 | stable | — |
| EV/EBITDA (Yahoo) | -26.61 | -26.61 | stable | — |
| P/B (Yahoo) | 5.86 | 5.86 | stable | — |
| Consensus PT | [MANQUANT] | **$42.45 (11 analysts)** | 🆕 | — |
| Max Pain | **$25.00** | **$15.00** | **-40.0%** | 🚨 |
| Put/Call Ratio | 0.85 | N/A | [MANQUANT] | — |
| Short Interest | 0.09% | 0.09% | stable | >5% |
| Score Opportunité | 5.2/10 | 5.0/10 | -0.2 pt | — |
| Score Valorisation | 5.0/10 | 4.5/10 | -0.5 pt | — |
| Score Catalyseur | 5.0/10 | 5.0/10 | stable | — |
| Score Momentum | 6.0/10 | 6.0/10 | stable | — |
| Score Global | — | 50.5 (55.5 ajusté) | 🆕 | — |

**Observations clés :**
- Cours inchangé en clôture ($40.43) mais ouverture à $42.38 → -4.6% sur la séance. Amplitude intrajournalière élevée : $37.65–$42.15 (11.5%).
- 🆕 **Consensus analystes FMP** désormais disponible : PT moyen $42.45 (+5.0% upside), 11 analystes actifs (2 le mois dernier, 4 le trimestre dernier). Couverture stable mais modérée.
- 🚨 **Max Pain options replongé à $15.00** (vs $25.00 hier) — écart de 63% sous le spot. Distorsion liée à l'expiration du 22/05 proche ; surveillance post-expiration recommandée.
- **Score Valorisation ajusté à la baisse** par l'agent recommandation (4.5/10 vs 5.0/10), plafonné par le Filtre Qualité 2/6.
- **Agent Quant** : pas assez de signaux historiques → [SIGNAUX NON SIGNIFICATIFS] (p-value 1.0).
- **Agent Accounting** : `data/accounting_risk_latest.json` absent → [DONNÉES MANQUANTES] pour M-Score / Z-Score / F-Score / Sloan.
- Aucune news structurante, événement corporate ou alerte macro/géo détectée.

---

## Mise à jour technique

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| RSI 14j | 61.71 | Neutre, loin de la survente (<30) et du surachat (>70) |
| MM 50j | $32.24 | Cours supérieur de +25.4%, tendance haussière intacte |
| MM 200j | N/A | Donnée indisponible — impossible de valider le Golden/Death Cross |
| Volume | 8,219,100 | 1.37× moy. 20j — volume soutenu |
| ATR 14j | $4.02 | Relatif 9.94% — volatilité élevée à surveiller |
| Range jour | $37.65–$42.15 | Amplitude 11.5% sans catalyst visible |
| Support 1 | $32.24 (MM50) | Support dynamique — rupture = révision baissière |
| Support 2 | $16.00 (52W Low) | — |
| Résistance 1 | $42.15 (High du jour) | — |
| Résistance 2 | $73.80 (52W High) | — |

**Timing verdict** : **Favorable** — tendance haussière intacte (cours > MM50), RSI neutre. Cependant, la volatilité intrajournalière (11.5%) sans catalyst apparent et la proximité de l'expiration options (22/05) augmentent le risque de microstructure.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale qualitative depuis l'initiale. Rappel des métriques clés avec sources croisées Yahoo / FMP :

| Métrique | Yahoo | FMP | Commentaire |
|----------|-------|-----|-------------|
| Market Cap | $6.48B | — | — |
| Forward P/E | -35.41 | — | Pas de rentabilité nette attendue |
| EV/EBITDA | -26.61 | -13.12 | EBITDA négatif sur les deux sources |
| P/B | 5.86 | 2.86 | Divergence matérielle — préférer Yahoo 5.86x (plus conservateur pour un profil non rentable) |
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
| Profit CAGR 5 ans ≥ 20% | ❌ Forward P/E -35.41, marges négatives |
| Assets/Liabilities > 1.0 | ⚠️ Current Ratio 4.51 (solide) mais pas de visibilité complète sur le bilan |
| FCF positif et croissant 5 ans | ❌ FCF yield négatif (-7.0% environ) |
| Avantage compétitif (moat) | ❌ Non démontré dans les données |
| Industrie forte croissance (TAM ×5) | ❌ Données insuffisantes |

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10 avant calcul final. L'agent recommandation applique **4.5/10**.

---

## Mise à jour sentiment / options / news

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT cohérent avec +5.0% upside. Couverture stable. |
| Max Pain | $15.00 | Yahoo Finance | Écart de **63%** sous le spot. Distorsion probable liée à l'expiration du 22/05. |
| Put/Call Ratio | N/A | Yahoo Finance | Donnée indisponible aujourd'hui. |
| Call OI % | N/A | Yahoo Finance | Donnée indisponible. |
| Short Interest | 0.09% | Yahoo Finance | Absence de squeeze setup. |
| Social Sentiment | 0 mentions, 0.0 score | `data/social_sentiment_latest.json` | Aucune activité retail détectée sur Reddit. Pump non détecté. |
| Event-Driven | Aucun | `data/events_latest.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (78 jours) | `data/upcoming_events_latest.json` | Est EPS -$0.60 à -$0.45, Rev $0.1B. |

**Score Catalyseur** : **5.0/10** — absence de catalyseur immédiat. Le prochain catalyst structurel est l'earnings d'août.

---

## Scoring global (Agent Recommandation — 2026-05-18)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 6.0/10 | 25% | 1.50 |
| **Score Opportunité** | **5.0/10** | | |
| Malus/Bonus | +5.5 pts | | (pas de malus accounting/geo/FX majeur) |
| **Score Global** | **50.5** | | |
| **Score Global Ajusté** | **55.5** | | |

**Action** : **ATTENDRE**  
**Direction** : Neutre  
**Timing** : Favorable (technique)  
**Horizon** : —

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant) → pas d'ajustement.
- **Agent Géo** : FLY non flaggé (pas d'exposition politique spécifique détectée) → pas de malus.
- **Agent Sector Rotation** : XLI (Industrials) sous-performant le SPY sur 20j (-1.22%) et 60j (-2.53%), momentum_score 0.0 → **headwind sectoriel** (-0.5 pt implicite sur le catalyseur sectoriel).
- **Agent Social** : Pas d'activité retail → neutre.
- **Agent FX** : Exposition 25%, currency USD, fx_impact_score 0.0 → pas d'ajustement.
- **Agent Event-Driven** : 0 événement → neutre.

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $40.43 | Close 2026-05-18 | Inchangé vs initiale |
| Stop-loss | $32.39 | Cours − 2×ATR ($4.02) | À ajuster si ATR évolue |
| Take-profit | $52.49 | Cours + 3×ATR ($4.02) | À ajuster si ATR évolue |
| Ratio R/R | 1.5:1 | Gain $12.06 / Perte $8.04 | Limité pour un profil non rentable |

Aucun changement de niveau — cours et ATR identiques à l'initiale. Le ratio 1.5:1 reste limité pour une action sans rentabilité démontrée et avec un Filtre Qualité faible.

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : Thèse CONFIRMÉE avec nuance.**

L'analyse initiale du 2026-05-17 concluait à un profil **ATTENDRE** en raison d'un momentum technique favorable (cours > MM50 $32.24, RSI 61.71 neutre) mais de fondamentaux insuffisants (Filtre Qualité 2/6, absence de rentabilité, multiples élevés). Cette conclusion reste valide.

**Ce qui confirme la thèse :**
- Cours stable au-dessus de la MM50 (+25% de marge), tendance haussière intacte.
- Aucune news structurante, guidance cut, ou événement corporate n'a altéré le narrative.
- Consensus analystes ($42.45 PT) cohérent avec une valorisation haute mais pas irrationnelle.

**Ce qui ajoute une nuance :**
- Volatilité intrajournalière élevée (range 11.5%) sans catalyst visible — comportement spéculatif ou microstructure options (expiration 22/05 proche).
- Max Pain à $15.00 (écart de 63% sous le spot) — distorsion options majeure à surveiller post-expiration.
- Score Valorisation ajusté à 4.5/10 par l'agent recommandation, renforçant la prudence.
- Headwind sectoriel : XLI (Industrials) sous-performe le SPY sur 20j et 60j (momentum_score 0.0) — pas de vent favorable sectoriel.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 78 jours) : Est EPS -$0.45 à -$0.60, Rev $0.1B. Toute surprise positive vs consensus négatif serait un catalyseur majeur.
2. **Expiration options 22/05** : surveillance post-expiration pour voir si la volatilité se normalise et si le Max Pain redevient cohérent.

**Risques :**
1. Rentabilité non démontrée — la société brûle du cash avec des marges fortement négatives (operating margin -154%, net margin -187%).
2. Multiple de valorisation incompatible avec un profil de quality compounding (EV/Revenue 32x, P/B 5.86x).
3. Volatilité élevée sans couverture fondamentale = risque de correction rapide si le momentum technique casse (rupture MM50 $32.24).

**Prochaine étape :**
- Maintenir **ATTENDRE**. Aucune position recommandée.
- Surveiller l'approche des earnings (août) et toute amélioration des marges ou du FCF dans les prochains filings.
- Si le cours casse la MM50 ($32.24) → réviser la thèse à la baisse.
