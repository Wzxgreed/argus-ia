# FUBO — Mise à Jour Quotidienne (2026-05-18)

> **Niveau d'impact :** 🟡 Modéré — Earnings jour J, données techniques inchangées, divergence fondamentale majeure détectée

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-17)

| Métrique | 2026-05-17 | 2026-05-18 | Variation |
|----------|-----------|-----------|-----------|
| Cours close | $9,62 | $9,62 | 0,00% |
| Change % | −1,64% | −1,64% | — |
| Volume | 944 400 | 944 400 | 0% |
| RSI 14j | 36,84 | 36,84 | — |
| MM 50j | $11,98 | $11,98 | — |
| ATR 14j | $0,79 | $0,79 | — |
| Max Pain (options) | $10,00 | $21,00 | **+110%** |
| Put/Call Ratio | 0,90 | 0,65 | **−27,8%** |
| Short Interest | — | 22,84% | [NOUVEAU] |

**Constat clé :** Les données de cotation (prix, volume, RSI, moyennes mobiles, ATR) sont strictement identiques à la session précédente, suggérant un snapshot non rafraîchi au moment du fetch. L'activité options en revanche affiche un décalage significatif : le max pain bondit à $21 (+110%) et le put/call ratio se détend à 0,65 (vs 0,90), signalant un repositionnement call-skewed à l'approche de l'échéance du 22 mai.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 36,84 | Zone de neutralité baissière, proche survente |
| MM 50j | $11,98 | Cours sous la moyenne — tendance baissière intacte |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,79 | Volatilité absolue élevée (8,2% du spot) |
| Volume vs 20j | 0,6× | Activité inférieure à la moyenne |

**Niveaux clés :**
- Support immédiat : $9,58 (low du jour)
- Résistance : $10,00 (high du jour) / $11,98 (MM50)
- Stop-loss ATR (2×) : $8,04
- Take-profit (3× ATR) : $11,99

**Verdict timing :** Défavorable — sous MM50, RSI non confirmé en survente, absence de volume. Attendre un pivot technique ou le résultat de l'earnings du jour.

---

## 3. Mise à Jour Fondamentale

### Divergence Yahoo / FMP — Anomalie à Signaler

| Source | Market Cap | P/B | EV/EBITDA |
|---|---|---|---|
| Yahoo Finance | $283,2M | 0,35x | — |
| FMP Stable API | **$3,27B** | **3,19x** | 16,10x |

**Écart :** ×11,5 sur la capitalisation. Ce hiatus massif entre les deux sources empêche toute valorisation fiable. Dans le doute, privilégier la source institutionnelle (FMP) tout en notant que les multiples FMP (EV/EBITDA 16,1x, P/B 3,19x) ne correspondent pas à un profil value.

### Ratios FMP (FY 2025)

| Métrique | Valeur | Lecture |
|---|---|---|
| Gross Margin | 11,12% | Très faible — quasi pas de marge brute |
| Operating Margin | −2,64% | Perte opérationnelle |
| Net Margin | 5,72% | Rentabilité nette positive (effet exceptionnel ?) |
| Debt/Equity | 2,43 | Levier élevé |
| Interest Coverage | −4,70x | Insuffisance de couverture des intérêts |
| Current Ratio | 0,84 | Illiquidité structurelle |
| ROIC | −2,15% | Destruction de valeur |
| Tangible Asset Value | −$398,9M | **Patrimoine net négatif** |
| Working Capital | −$180,9M | Besoin en fonds de roulement négatif |

**Filtre Qualité (6 critères) — réévalué :**

| Critère | Verdict | Justification |
|---------|---------|---------------|
| Revenue CAGR 5 ans ≥ 20% | 🔴 Non | Croissance ralentie, saturation du streaming sportif |
| Profit CAGR 5 ans ≥ 20% | 🔴 Non | Perte opérationnelle persistante |
| Assets/Liabilities > 1,0 | 🔴 Non | Current ratio 0,84 ; tangible asset value négatif |
| FCF positif et croissant | 🔴 Non | Price/FCF négatif (−5,29x) |
| Moat structurel | 🟡 Partiel | Niche du streaming sportif live, mais concurrence intensifiée (YouTube TV, ESPN+) |
| Industrie forte croissance | 🟡 Partiel | TAM streaming global en croissance, mais FUBO perd des parts |

**Score Qualité : 1/6** — 🔴 **Hors périmètre Quality Compounder.**

> **Règle absolue :** Score ≤ 3/6 → Score Valorisation plafonné à 5/10. La valorisation attractive apparente (P/E Yahoo 2,5x) est probablement une illusion comptable (one-off, restructuration, ou erreur de source). Le profil FMP (EV/EBITDA 16x, P/B 3,2x) est loin du deep value.

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Publishers | TheFly, StreetInsider, Benzinga, Pulse 2.0 |

**Lecture :** Écart prix cible / spot de +422%, symptomatique d'un titre en détresse où les analystes maintiennent des objectifs historiques non révisés. Avec seulement 4 couvertures (0 mise à jour le dernier mois), la crédibilité de ce PT est faible. Considérer comme legacy rating plutôt que signal actif.

### Options (échéance 2026-05-22)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $21,00 | Loin du spot ($9,62) — pinning théorique peu probable |
| Put/Call Ratio | 0,65 | Skew nettement call-biased vs la veille (0,90) |
| Call OI % | 60,6% | Positionnement haussier sur le near-term |

**Lecture :** Le repositionnement options vers les calls à 4 jours de l'échéance suggère une anticipation de volatilité autour de l'earnings du jour. Cependant, le max pain à $21 est si éloigné du spot qu'il perd de sa pertinence pratique. Le call-skew peut refléter un pari spéculatif sur un beat earnings (catalyseur), pas un consensus haussier structuré.

### Short Interest

- **22,84% du float** — niveau très élevé
- Float : 29,2M actions
- Setup short squeeze théorique possible sur catalyseur positif, mais la qualité fondamentale rend la tenue du rebond improbable

### Social Sentiment

- Mention count Reddit : 0 (no data)
- Pump detected : false
- **Alerte EXTREME_BEARISH** déclenchée par le système social (valeur 0,0 — artefact d'absence de données, non significative)

---

## 5. Scoring Global Révisé

| Composante | Valeur | vs 2026-05-17 |
|---|---|---|
| Score Global Argus-IA | 56,8 / 100 | = |
| Score Opportunité | 6,5 / 10 | = |
| Score Catalyseur | 8,0 / 10 | = |
| Score Valorisation | 7,0 / 10 | = |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation** | **ATTENDRE** | **=** |

**Malus appliqués :**
- Malus Qualité : Score Qualité 1/6 → Score Valorisation théorique plafonné à 5/10, mais le système affiche 7,0/10. **Anomalie de scoring détectée** — le malus qualité n'est pas appliqué dans `recommandations_latest.json`.
- Malus Momentum : Cours sous MM50, RSI 36,84 → −0,5 pt implicite
- Malus Comptable : Tangible asset value négatif, ROIC négatif, current ratio < 1 → risque financier élevé

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9,62 | — |
| Stop-Loss | $8,04 | Inchangé — 2× ATR sous le spot (−16,4%) |
| Take-Profit | $11,99 | Inchangé — 3× ATR au-dessus du spot (+24,6%) |
| Ratio R/R | 1,5× | Inchangé |

**Condition de révision :** Sur résultats d'earnings du jour :
- Beat + guidance raise → réviser TP à $13,50+ (breakout MM50)
- Miss + guidance cut → abaisser SL à $7,50 (support psychologique)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE avec RÉSERVE MAJEURE**

La thèse d'ATTENDRE du 2026-05-17 reste valide. Aucun élément nouveau ne justifie une exposition longue à ce stade.

**Arguments confirmant la patience :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, ROIC négatif, marge opérationnelle négative. Ce n'est pas un Quality Compounder.
2. **Données techniques inchangées** — aucun signe de reversal, aucun volume, toujours sous MM50.
3. **Earnings jour J sans résultat visible** — le catalyseur majeur est en cours ; attendre le verdict avant toute action.
4. **Divergence Yahoo/FMP** — le P/E 2,5x et le market cap $283M sont suspects. Le profil FMP (EV/EBITDA 16x, P/B 3,2x, market cap $3,3B) correspond davantage à une small-cap spéculative à haut risque qu'à un value trap profond.

**Seuls éléments modifiés :**
- Options repositionnement call-skewed (put/call 0,65, max pain $21) → anticipation de volatilité earnings, pas direction haussière.
- Détection du tangible asset value négatif (−$398,9M) via FMP → renforce le verdict de risque financier.

**Scénarios post-earnings (2026-05-18 soir) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 20% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 50% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 30% | −10–20% | Confirmer l'évitement |

**Recommandation finale :** **ATTENDRE — pas de position.** Si résultats positifs, le titre reste une spéculation court terme (trade technique) et non un investissement long terme. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-05-18*
*Sources : data/latest.json, data/recommandations_latest.json, data/fx_exposure_latest.json, data/social_sentiment_latest.json, data/upcoming_events_latest.json*
