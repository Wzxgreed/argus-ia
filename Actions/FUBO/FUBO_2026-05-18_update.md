# FUBO — Mise à Jour Quotidienne (2026-05-18)

> **Niveau d'impact :** 🟡 Modéré — Données techniques stables, earnings jour J en attente, malus sectoriel additionnel détecté

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-18 matinale)

| Métrique | Session matinale | Session actuelle | Variation |
|----------|-----------------|------------------|-----------|
| Cours close | $9,62 | $9,62 | 0,00% |
| Change % | −1,64% | −1,64% | — |
| Volume | 944 400 | 944 400 | 0% |
| RSI 14j | 36,84 | 36,84 | — |
| MM 50j | $11,98 | $11,98 | — |
| ATR 14j | $0,79 | $0,79 | — |
| Max Pain | $21,00 | $21,00 | — |
| Put/Call Ratio | 0,65 | 0,65 | — |
| Short Interest | 22,84% | 22,84% | — |
| Score Global Argus-IA | 56,8/100 | 56,8/100 | — |
| Score Opportunité | 6,5/10 | 6,5/10 | — |

**Constat clé :** Les données de cotation, techniques, fondamentales et options sont strictement identiques à la session matinale (snapshot `data/latest.json` timestamp 09:00:15 UTC inchangé). Aucun nouveau flux de prix ni de consensus n'est disponible depuis. L'earnings Q1 2026 reste jour J sans résultat publié à ce stade.

**Nouveauté d'analyse :** Intégration des modules **Sector Rotation** (XLC en bottom 3) et **Quant Report** (calibration insuffisante) — voir sections 3 et 5.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 36,84 | Zone de neutralité baissière, proche survente |
| MM 50j | $11,98 | Cours sous la moyenne — tendance baissière intacte |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,79 | Volatilité absolue élevée (8,2% du spot) |
| Volume vs 20j | 0,6× | Activité inférieure à la moyenne |
| Beta | 2,508 | Volatilité systématique très élevée |

**Niveaux clés :**
- Support immédiat : $9,58 (low du jour)
- Résistance : $10,00 (high du jour) / $11,98 (MM50)
- Stop-loss ATR (2×) : $8,04
- Take-profit (3× ATR) : $11,99

**Verdict timing :** Défavorable — sous MM50, RSI non confirmé en survente, absence de volume. Attendre un pivot technique ou le verdict de l'earnings du jour.

---

## 3. Mise à Jour Fondamentale

### Divergence Yahoo / FMP — Anomalie Persistante

| Source | Market Cap | P/B | EV/EBITDA |
|---|---|---|---|
| Yahoo Finance | $283,2M | 0,35x | — |
| FMP Stable API | **$3,27B** | **3,19x** | 16,10x |

**Écart :** ×11,5 sur la capitalisation. Ce hiatus massif entre les deux sources empêche toute valorisation fiable. Dans le doute, privilégier la source institutionnelle (FMP) tout en notant que les multiples FMP (EV/EBITDA 16,1x, P/B 3,2x) ne correspondent pas à un profil value. La valorisation apparente (P/E Yahoo 2,5x) reste suspecte.

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

### Filtre Qualité (6 critères) — réévalué avec prudence

| Critère | Verdict | Justification |
|---------|---------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ⚪ Inconnu | Séries historiques `statements` absentes de `data/latest.json` — impossible à vérifier depuis les JSON |
| Profit CAGR 5 ans ≥ 20% | ⚪ Inconnu | Idem — pas de données EPS historiques dans les snapshots |
| Assets/Liabilities > 1,0 | 🔴 Non | Current ratio 0,84 ; tangible asset value négatif ; patrimoine net négatif |
| FCF positif et croissant | 🔴 Non | Price/FCF négatif (−5,29x) ; FCF yield −18,9% ; EV/FCF −20,96x |
| Moat structurel | 🟡 Partiel | Niche du streaming sportif live, mais concurrence intensifiée (YouTube TV, ESPN+) |
| Industrie forte croissance | 🟡 Partiel | TAM streaming global en croissance, mais FUBO perd des parts ; XLC bottom 3 rotation sectorielle |

**Score Qualité : 1/6** — 🔴 **Hors périmètre Quality Compounder.**

> **Règle absolue :** Score ≤ 3/6 → Score Valorisation plafonné à 5/10. L'anomalie de scoring persiste dans `recommandations_latest.json` (Valorisation affichée 7,0/10) ; le malus qualité n'est pas appliqué par le moteur de recommandation. En ajustement manuel, le score Valorisation effectif ne dépasse pas 5/10.

### Sector Rotation — Malus Additionnel

D'après `data/sector_rotation_latest.json` (2026-05-18) :
- **XLC (Communication Services)** classé dans le **bottom 3** sectors (momentum score 0,0)
- RS 20j vs SPY : −6,62% ; RS 60j : −7,15%
- Crossover détecté : **BULLISH_CROSSOVER** sur XLC (signal contradictoire avec le ranking faible)

**Impact FUBO :** FUBO appartient au secteur Communication Services (Yahoo Finance). Le classement bottom 3 sectoriel implique un **malus sectoriel −0,5 pt** sur le Score Opportunité. Le crossover bullish est un signal de potentiel reversal, mais non confirmé par le momentum effectif.

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart prix cible / spot de +422%, symptomatique d'un titre en détresse où les analystes maintiennent des objectifs historiques non révisés. Avec 0 mise à jour le dernier mois, la crédibilité de ce PT est faible. Considérer comme legacy rating plutôt que signal actif.

### Options (échéance 2026-05-22)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $21,00 | Loin du spot ($9,62) — pinning théorique peu probable |
| Put/Call Ratio | 0,65 | Skew nettement call-biased |
| Call OI % | 60,6% | Positionnement haussier sur le near-term |

**Lecture :** Le repositionnement options vers les calls à 4 jours de l'échéance suggère une anticipation de volatilité autour de l'earnings du jour. Le max pain à $21 est si éloigné du spot qu'il perd de sa pertinence pratique. Le call-skew reflète un pari spéculatif sur un beat earnings, pas un consensus haussier structuré.

### Short Interest

- **22,84% du float** — niveau très élevé
- Float : 29,2M actions
- Setup short squeeze théorique possible sur catalyseur positif, mais la qualité fondamentale rend la tenue du rebond improbable

### Social Sentiment

- Mention count Reddit : 0 (no data)
- Pump detected : false
- Alertes `EXTREME_BEARISH` déclenchées sur l'ensemble de la watchlist (artefact d'absence de données, non significative)

---

## 5. Scoring Global Révisé

| Composante | Valeur | vs Session Matinale |
|---|---|---|
| Score Global Argus-IA | 56,8 / 100 | = |
| Score Opportunité | 6,5 / 10 | = |
| Score Catalyseur | 8,0 / 10 | = |
| Score Valorisation | 7,0 / 10 | = (moteur) / **5,0 / 10** (ajusté manuel Qualité) |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation moteur** | **ATTENDRE** | **=** |

**Ajustements qualitatifs :**
- Malus Qualité : Score Qualité 1/6 → Score Valorisation théorique plafonné à 5/10 (non reflété dans `recommandations_latest.json`)
- Malus Momentum : Cours sous MM50, RSI 36,84 → −0,5 pt implicite
- Malus Sectoriel : XLC bottom 3 sector rotation → −0,5 pt additionnel sur le composite
- Malus Comptable : Tangible asset value négatif, ROIC négatif, current ratio < 1 → risque financier élevé

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — pas assez de signaux historiques FUBO pour établir une calibration fiable
- Win rate observé : 0% (insuffisant) ; p-value : 1,0 (non significatif)
- **Conclusion :** Aucune calibration auto applicable ; les scores reposent sur les agents fondamental/sentiment/technique sans correction empirique.

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

La thèse d'**ATTENDRE** du 2026-05-18 reste valide. Aucun élément nouveau ne justifie une exposition longue à ce stade.

**Arguments confirmant la patience :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, ROIC négatif, marge opérationnelle négative, FCF yield négatif. Ce n'est pas un Quality Compounder.
2. **Données techniques inchangées** — aucun signe de reversal, aucun volume, toujours sous MM50.
3. **Earnings jour J sans résultat visible** — le catalyseur majeur est en cours ; attendre le verdict avant toute action.
4. **Divergence Yahoo/FMP persistante** — le P/E 2,5x et le market cap $283M sont suspects. Le profil FMP (EV/EBITDA 16x, P/B 3,2x, market cap $3,3B) correspond davantage à une small-cap spéculative à haut risque qu'à un value trap profond.
5. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 sectoriel, malus additionnel.
6. **Quant report non significatif** — pas assez de signaux historiques pour calibrer le scoring.

**Seuls éléments modifiés :**
- Intégration du malus sectoriel XLC bottom 3 → renforce l'évitement structurel.
- Confirmation de l'artefact social sentiment (0 mentions) → absence de signal retail.

**Scénarios post-earnings (2026-05-18 soir) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 20% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 50% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 30% | −10–20% | Confirmer l'évitement |

**Recommandation finale :** **ATTENDRE — pas de position.** Si résultats positifs, le titre reste une spéculation court terme (trade technique) et non un investissement long terme. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle. Le malus sectoriel XLC renforce ce verdict.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-18*  
*Sources : data/latest.json, data/recommandations_latest.json, data/quant_report_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/validation_report.txt*
