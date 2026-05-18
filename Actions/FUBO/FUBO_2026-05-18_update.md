# FUBO — Mise à Jour Quotidienne (2026-05-18 révisée)

> **Niveau d'impact :** 🟡 Modéré — Données de cours inchangées, mais repositionnement options majeur post-séance, max pain corrigé à 10 $

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-18 10h UTC)

| Métrique | 10h UTC | 13h UTC (révision) | Variation |
|---|---|---|---|
| Cours close | $9,62 | $9,62 | 0,00% |
| Volume | 944 400 | 944 400 | 0% |
| RSI 14j | 36,84 | 36,84 | — |
| ATR 14j | $0,79 | $0,79 | — |
| MM 50j | $11,98 | $11,98 | — |
| **Max Pain** | **$21,00** | **$10,00** | **−52,4%** 🔴 |
| **Put/Call Ratio** | **0,65** | **0,90** | **+38,5%** 🔴 |
| **Call OI %** | **60,6%** | **52,5%** | **−13,4%** 🔴 |
| Short Interest | 22,84% | 22,84% | — |

**Constat :** Le snapshot `data/latest.json` a été rafraîchi à 13h UTC. Les données de prix et de technique restent inchangées (aucune nouvelle séance). En revanche, le flux options a été mis à jour avec un repositionnement significatif :
- Le **max pain** est corrigé à **$10** (vs $21 précédemment) — désormais à seulement 4,1% du spot, rendant le pinning très probable à l'échéance 2026-05-22.
- Le **put/call ratio** passe de 0,65 à **0,90**, inversant le skew de call-biased à **put-biased**.
- La part des calls dans l'open interest recule de 60,6% à **52,5%**.

Ces ajustements traduisent une dégradation du sentiment options entre 10h et 13h UTC, probablement en anticipation des résultats Q1 2026 (jour J).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 36,84 | Zone neutre baissière, proche survente |
| MM 50j | $11,98 | Cours sous la moyenne — tendance baissière intacte |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,79 | Volatilité absolue élevée (8,2% du spot) |
| Volume vs 20j | 0,6× | Activité inférieure à la moyenne |
| Beta | 2,508 | Volatilité systématique très élevée |

**Niveaux clés :**
- Support immédiat : $9,58 (low du jour)
- Résistance : $10,00 (high du jour / max pain / niveau psychologique)
- Stop-loss ATR (2×) : $8,04
- Take-profit (3× ATR) : $11,99

**Verdict timing :** Défavorable — sous MM50, RSI non confirmé en survente, absence de volume. Le max pain à $10 renforce la résistance psychologique. Attendre un pivot technique ou le verdict de l'earnings du jour.

---

## 3. Mise à Jour Fondamentale

### Divergence Yahoo / FMP — Anomalie Persistante

| Source | Market Cap | P/B | EV/EBITDA |
|---|---|---|---|
| Yahoo Finance | $283M | 0,35x | — |
| FMP Stable API | **$3,27B** (implicite) | **3,19x** | 16,10x |

**Écart :** ×11,5 sur la capitalisation. Ce hiatus empêche toute valorisation fiable. Dans le doute, privilégier la source institutionnelle (FMP) tout en notant que les multiples FMP (EV/EBITDA 16,1x, P/B 3,2x) correspondent à un profil small-cap spéculative, pas à un value trap profond.

### Ratios FMP (FY 2025)

| Métrique | Valeur | Lecture |
|---|---|---|
| Gross Margin | 11,1% | Très faible |
| Operating Margin | −2,6% | Perte opérationnelle |
| Net Margin | 5,7% | Rentabilité nette positive (effet exceptionnel ?) |
| Debt/Equity | 2,43 | Levier élevé |
| Interest Coverage | −4,70x | Insuffisance de couverture |
| Current Ratio | 0,84 | Illiquidité structurelle |
| ROIC | N/A (null dans snapshot) | Destruction de valeur probable |
| Price/FCF | −5,29x | FCF négatif |

### Filtre Qualité (6 critères)

| Critère | Verdict | Justification |
|---------|---------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ⚪ Inconnu | Séries historiques absentes du snapshot |
| Profit CAGR 5 ans ≥ 20% | ⚪ Inconnu | Idem |
| Assets/Liabilities > 1,0 | 🔴 Non | Current ratio 0,84 ; dette/équité 2,43 |
| FCF positif et croissant | 🔴 Non | Price/FCF négatif (−5,29x) ; FCF yield −18,9% |
| Moat structurel | 🟡 Partiel | Niche streaming sportif live, concurrence YouTube TV / ESPN+ |
| Industrie forte croissance | 🟡 Partiel | TAM streaming en croissance, mais FUBO perd des parts ; XLC bottom 3 |

**Score Qualité : 1/6** — 🔴 Hors périmètre Quality Compounder.

> **Règle absolue :** Score ≤ 3/6 → Score Valorisation plafonné à 5/10. Le moteur de recommandations affiche Valorisation 7,0/10 ; en ajustement manuel qualité, le score effectif ne dépasse pas 5/10.

### Sector Rotation — Malus Actif

- **XLC (Communication Services)** classé **bottom 3** (momentum score 0,0)
- RS 20j vs SPY : −6,62% ; RS 60j : −7,15%
- Crossover détecté : **BULLISH_CROSSOVER** sur XLC (signal contradictoire non confirmé par momentum)

**Impact FUBO :** Malus sectoriel **−0,5 pt** sur le Score Opportunité.

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +422%, symptomatique d'un titre en détresse avec objectifs historiques non révisés. Crédibilité faible — legacy rating.

### Options (échéance 2026-05-22) — Repositionnement Majeur

| Signal | 10h UTC | 13h UTC | Lecture |
|---|---|---|---|
| **Max Pain** | $21,00 | **$10,00** | Désormais proche du spot — pinning très probable |
| **Put/Call Ratio** | 0,65 | **0,90** | Skew inversé : de call-biased à **put-biased** |
| **Call OI %** | 60,6% | **52,5%** | Déclin du positionnement haussier near-term |

**Lecture :** Le repositionnement options entre 10h et 13h UTC révèle un virage bearish du marché des dérivés à J-4 de l'échéance. Le max pain à $10 (vs $21) rend le pinning autour du niveau actuel un scénario de haute probabilité. L'inversion du put/call ratio à 0,90 suggère que les opérateurs anticipent une déception sur l'earnings Q1 2026 ou une guidance保守. Ce repositionnement contraste avec le call-skew observé ce matin et constitue un signal baissier dérivés majeur.

### Short Interest

- **22,84% du float** — niveau très élevé
- Float : 29,2M actions
- Setup short squeeze théorique possible sur catalyseur positif, mais la qualité fondamentale rend la tenue du rebond improbable

### Social Sentiment

- Mention count Reddit : 0 (no data)
- Pump detected : false
- Alertes `EXTREME_BEARISH` déclenchées sur l'ensemble de la watchlist (artefact d'absence de données)

---

## 5. Scoring Global Révisé

| Composante | Valeur Moteur | Valeur Ajustée Manuelle |
|---|---|---|
| Score Global | 56,8 / 100 | **~51 / 100** |
| Score Opportunité | 6,5 / 10 | **5,1 / 10** |
| Score Catalyseur | 8,0 / 10 | **7,5 / 10** (malus options put-biased −0,5) |
| Score Valorisation | 7,0 / 10 | **5,0 / 10** (plafonné Qualité) |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation** | **ATTENDRE** | **ATTENDRE** |

**Ajustements qualitatifs :**
- Malus Qualité (1/6) : Valorisation plafonnée à 5/10
- Malus Sectoriel : XLC bottom 3 → −0,5 pt composite
- **Malus Options (nouveau)** : put/call ratio 0,90 + max pain à $10 → −0,5 pt Catalyseur
- Malus Comptable : Current ratio 0,84, debt/equity 2,43, FCF négatif → risque financier élevé

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — pas assez de signaux historiques FUBO pour calibration fiable
- Win rate observé : 0% (insuffisant) ; p-value : 1,0 (non significatif)
- **Conclusion :** Aucune calibration auto applicable.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9,62 | — |
| Stop-Loss | $8,04 | Inchangé — 2× ATR (−16,4%) |
| Take-Profit | $11,99 | Inchangé — 3× ATR (+24,6%) |
| Ratio R/R | 1,5× | Inchangé |
| Max Pain | $10,00 | Niveau de pinning probable à J-4 options |

**Condition de révision post-earnings :**
- Beat + guidance raise → réviser TP à $13,50+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7,50 (support psychologique)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE avec RÉSERVE MAJEURE**

La thèse d'**ATTENDRE** du 2026-05-18 reste valide. Le repositionnement options vers un profil put-biased renforce la prudence, sans invalider la thèse.

**Arguments confirmant la patience :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, FCF négatif, current ratio 0,84, debt/equity 2,43. Ce n'est pas un Quality Compounder.
2. **Données techniques inchangées** — aucun signe de reversal, aucun volume, toujours sous MM50.
3. **Repositionnement options baissier** — max pain à $10, put/call 0,90. Le marché des dérivés a viré nettement plus bearish entre 10h et 13h UTC.
4. **Earnings jour J sans résultat visible** — le catalyseur majeur est en cours ; attendre le verdict avant toute action.
5. **Divergence Yahoo/FMP persistante** — le P/E 2,5x et le market cap $283M sont suspects. Le profil FMP (EV/EBITDA 16x, P/B 3,2x) correspond davantage à une small-cap spéculative à haut risque.
6. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 sectoriel.
7. **Quant report non significatif** — pas assez de signaux historiques pour calibrer le scoring.

**Seuls éléments modifiés :**
- Intégration du malus options put-biased → renforce l'évitement structurel.
- Max pain corrigé à $10 → niveau de pinning proche du spot à surveiller.

**Scénarios post-earnings (2026-05-18 soir) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 15% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 45% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 40% | −10–20% | Confirmer l'évitement |

> **Note de probabilité :** La probabilité du scénario bearish a été relevée de 30% à 40% suite au repositionnement options put-biased. Le scénario beat a été abaissé de 20% à 15%.

**Recommandation finale :** **ATTENDRE — pas de position.** Si résultats positifs, le titre reste une spéculation court terme et non un investissement long terme. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle. Le repositionnement options vers put-biased suggère que le marché s'attend à une déception.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-18 (révision 13h UTC)*  
*Sources : data/latest.json (fetched 2026-05-18T13:00:01Z), data/recommandations_2026-05-18.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_2026-05-18.json, data/social_sentiment_2026-05-18.json, data/fx_exposure_2026-05-18.json, data/upcoming_events_2026-05-18.json, data/events_2026-05-18.json, data/validation_report.txt*
