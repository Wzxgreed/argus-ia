# FLY — Mise à Jour Quotidienne (2026-05-18)

> Source : `data/latest.json` (2026-05-18) + `data/recommandations_latest.json` + agents quant/geo/sector/social/FX/events/upcoming.

---

## Résumé des changements depuis l'analyse précédente (2026-05-17)

| Métrique | Précédent | Actuel | Variation |
|----------|-----------|--------|-----------|
| Cours close | $40.43 | $40.43 | 0.0% |
| Change vs prior close | — | -4.6% | — |
| RSI 14j | 61.71 | 61.71 | stable |
| MM 50j | $32.24 | $32.24 | stable |
| ATR 14j | $4.02 | $4.02 | stable |
| Volume | 8.2M | 8.2M | 1.37× moy. 20j |
| Filtre Qualité | 2/6 | 2/6 | stable |
| Consensus PT | [DONNÉES MANQUANTES] | $42.45 (11 analysts) | 🆕 |
| Score Opportunité | 5.2/10 | 5.0/10 | -0.2 pt |
| Score Valorisation | 5.0/10 | 4.5/10 | -0.5 pt |
| Score Global | — | 50.5 (55.5 ajusté) | 🆕 |

**Observations clés :**
- Cours et indicateurs techniques inchangés (même snapshot de marché).
- 🆕 **Consensus analystes** désormais disponible : PT moyen $42.45 (+5.0% upside), couvert par 11 analystes.
- Score Valorisation ajusté à la baisse par l'agent recommandation (4.5/10 vs 5.0/10), plafonné par le Filtre Qualité 2/6.
- ATR relatif élevé (9.94%) — volatilité intrajournalière marquée (range $37.65–$42.15, 11.5%).
- Aucune news structurante, événement corporate ou alerte macro/géo détectée.

---

## Mise à jour technique

- **RSI 14j** : 61.71 — zone neutre, loin de la survente (<30) et du surachat (>70).
- **MM 50j** : $32.24 — cours supérieur de +25.4%, tendance haussière intacte.
- **MM 200j** : N/A (donnée indisponible).
- **Volume** : 8,219,100 (1.37× moy. 20j de 5,994,630) — volume soutenu.
- **ATR 14j** : $4.02 (relatif 9.94%) — volatilité élevée.
- **Range jour** : $37.65–$42.15 (amplitude 11.5%) — forte volatilité intrajournalière sans clôture significative.
- **Supports** : MM50 $32.24 ; 52W Low $16.00.
- **Résistances** : High du jour $42.15 ; 52W High $73.80.
- **Timing verdict** : Favorable (tendance haussière, RSI neutre, mais volatilité élevée à surveiller).

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale depuis l'initiale. Rappel des métriques clés :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap | $6.48B | — |
| Forward P/E | -35.41 | Pas de rentabilité nette attendue |
| EV/EBITDA (Yahoo) | -26.61 | EBITDA négatif |
| EV/EBITDA (FMP) | -13.12 | Alternative FMP |
| P/B | 5.86 (Yahoo) / 2.86 (FMP) | Divergence de sources — préférer Yahoo 5.86x |
| EV/Revenue | 32.34x | Multiple élevé |
| Gross Margin | 15.6% | Faible |
| Operating Margin | -154% | Fortement négatif |
| Debt/Equity | 0.26 | Levier modéré |
| Current Ratio | 4.51 | Liquidité solide |
| Short Interest | 0.09% | Aucun pari baissier structuré |

**Filtre Qualité** : 2/6 (⚠️ Partielle)
- Rentabilité : ❌ (P/E négatif, marges négatives)
- Valorisation : ❌ (P/B 5.86x, EV/Revenue 32x)
- Bilan : ❌ (données insuffisantes pour validation complète)
- Moat/TAM : ❌ (données insuffisantes)
- FCF : ❌ (FCF yield négatif -7.0%)

**Règle** : Score ≤3/6 → Score Valorisation plafonné à 5/10 avant calcul final. L'agent recommandation applique 4.5/10.

---

## Mise à jour sentiment / options / news

- **Consensus analystes (FMP)** : PT moyen $42.45 (+5.0% upside), 11 analystes actifs. 2 analystes actifs le mois dernier, 4 le trimestre dernier. Couverture stable mais modérée.
- **Max Pain** : $15.00 (significativement sous le spot de $40.43) — écart de 63%. La proximité de l'expiration du 22/05 pourrait expliquer la distortion, mais la convexité de baisse reste théoriquement élevée si le spot converge vers le Max Pain.
- **Put/Call Ratio** : N/A (données manquantes).
- **Short Interest** : 0.09% — absence de squeeze setup.
- **Social Sentiment** : [DONNÉES MANQUANTES] — Reddit sans mention, pump non détecté.
- **Event-Driven** : Aucun événement corporate détecté (M&A, buyback, guidance, activism).
- **Upcoming Events** : Earnings Q2 2026 le 2026-08-04 (78 jours). Est EPS -$0.60 à -$0.45, Rev $0.1B.

---

## Scoring global (Agent Recommandation — 2026-05-18)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 6.0/10 | 25% | 1.50 |
| **Score Opportunité** | **5.0/10** | | |
| Malus/Bonus | +5.5 pts | | |
| **Score Global** | **50.5** (55.5 ajusté) | | |

**Action** : **ATTENDRE**
**Direction** : Neutre
**Timing** : Favorable
**Horizon** : —

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Cours actuel | $40.43 | Close 2026-05-18 |
| Stop-loss | $32.39 | Cours − 2×ATR ($4.02) |
| Take-profit | $52.49 | Cours + 3×ATR ($4.02) |
| Ratio R/R | 1.5:1 | Gain $12.06 / Perte $8.04 |

Aucun changement de niveau — les données techniques (cours, ATR) sont identiques à l'initiale. Le ratio 1.5:1 reste limité pour une action sans rentabilité et avec un Filtre Qualité faible.

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : Thèse CONFIRMÉE avec nuance.**

L'analyse initiale du 2026-05-17 concluait à un profil **ATTENDRE** en raison d'un momentum technique favorable (cours > MM50, RSI neutre) mais de fondamentaux insuffisants (Filtre Qualité 2/6, absence de rentabilité, multiples élevés). Cette conclusion reste valide à ce stade.

**Ce qui confirme la thèse :**
- Cours stable au-dessus de la MM50 (+25% de marge), tendance haussière intacte.
- Aucune news structurante n'a altéré le narrative.
- Consensus analystes ($42.45 PT) cohérent avec une valorisation haute mais pas irrationnelle.

**Ce qui ajoute une nuance :**
- Volatilité intrajournalière élevée (range 11.5%) sans catalyst visible — comportement spéculatif ou microstructure options (expiration 22/05 proche).
- Score Valorisation ajusté à 4.5/10 par l'agent recommandation, renforçant la prudence.
- Secteur Industriels (XLI) sous-performant le SPY sur 20j/60j (momentum sectoriel nul, momentum_score 0.0) — headwind sectoriel.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 78 jours) : Est EPS -$0.45 à -$0.60. Toute surprise positive vs consensus négatif serait un catalyseur majeur.
2. **Activité options 22/05** : expiration proche avec Max Pain à $15.00. Surveillance post-expiration pour voir si la volatilité se normalise.

**Risques :**
1. Rentabilité non démontrée — la société brûle du cash avec des marges négatives.
2. Multiple de valorisation incompatible avec un profil de quality compounding.
3. Volatilité élevée sans couverture fondamentale = risque de correction rapide si le momentum technique casse.

**Prochaine étape :**
- Maintenir **ATTENDRE**. Aucune position recommandée.
- Surveiller l'approche des earnings (août) et toute amélioration des marges ou du FCF dans les prochains filings.
- Si le cours casse la MM50 ($32.24) → réviser la thèse à la baisse.
