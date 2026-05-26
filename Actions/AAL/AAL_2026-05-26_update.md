# AAL — Mise à Jour 2026-05-26

**Date :** 2026-05-26 (snapshot 13:00 UTC)  
**Ticker :** AAL (NASDAQ)  
**Type :** Update pre-market — Snapshot 13:00 UTC corrige l'anomalie data quality du snapshot 10:00 UTC  
**Cours (close) :** $13.85  
**Previous close :** $13.59  
**Change session :** +1.91%  
**Volume :** 99.26M (vs moy. 20j 57.88M, +71.5%)

> **Note :** Le snapshot 13:00 UTC est pre-market (ouverture US à 13:30 UTC). Les prix, volumes et indicateurs techniques sont strictement identiques au snapshot 10:00 UTC. La seule mutation concerne la correction des données options dans `data/latest.json`.

---

## Résumé des Changements depuis l'Update (2026-05-26 10:00 UTC)

| Indicateur | 2026-05-26 10:00 UTC | 2026-05-26 13:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $13.85 | **$13.85** | **0.00** |
| RSI 14j | 71.43 | **71.43** | **0.00** |
| ATR 14j | $0.55 | **$0.55** | **$0.00** |
| MM 50j | $11.71 | **$11.71** | **$0.00** |
| Forward P/E | 6.26 | **6.26** | **0.00** |
| Volume du jour | 99.26M vs 57.88M avg (+71.5%) | **99.26M vs 57.88M avg (+71.5%)** | **0.00** |
| Short Interest | 12.21% | **12.21%** | **0.00** |
| Consensus FMP PT | $16.02 (15 analystes) | **$16.02 (15 analystes, 0 màj mois)** | **Inchangé** |
| Upside vs PT | +15.7% | **+15.7%** | **0.00** |
| Put/Call Ratio | `null` [⚠️ DATA QUALITY] | **1.83** | ✅ **Corrigé** |
| Max Pain | $5.00 [⚠️ ABERRANT] | **$13.00** | ✅ **Corrigé** |
| Call OI % | `null` [⚠️ DATA QUALITY] | **35.3%** | ✅ **Corrigé** |
| Score Opportunité agent | 5.7/10 | **5.7/10** | **0.00** |
| Recommandation agent | SURVEILLER | **SURVEILLER** | **Inchangé** |
| Earnings Q2 (jours) | 58 | **58** | **0** |

**Pre-market, aucune mutation de prix.** Les données techniques, fondamentales et de consensus sont strictement identiques au snapshot 10:00 UTC. **Mutation positive : correction data quality options** — `put_call_ratio`, `max_pain` et `call_oi_pct` sont désormais cohérents et alignés sur les valeurs du 25/05 (Put/Call 1.83 vs 1.82, Max Pain $13.00, Call OI 35.3% vs 35.5%).

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $13.85 | +1.91% session (clôture 23/05) ; +14.8% vs close 20/05 |
| RSI 14j | 71.43 | 🔴 **Surachat** — inchangé |
| ATR 14j | $0.55 | Volatilité stable |
| MM 50j | $11.71 | 🟢 Cours +18.3% au-dessus (trend haussier intact) |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 57.88M | 🟡 **+71.5% vs moyenne** — inchangé, flux anormal confirmé |
| 52W Range | $10.09–$16.50 | Cours à 84% du 52W low, 16.1% sous le 52W high |
| Support clé | $13.50 | Ancienne résistance / gap janvier → support à valider |
| Support secondaire | $12.75 | Cours − 2×ATR = niveau technique de sortie |
| Résistance | $14.00–$14.18 | Gap janvier 2026 + high du 23/05 ($14.18) |
| Résistance majeure | $16.50 | 52W high |
| Short Interest | 12.21% | 🟡 Élevé — fuel squeeze partiellement consommé |

**Options — Data quality corrigée :**

| Métrique | Valeur JSON 13:00 UTC | Valeur 10:00 UTC | Δ | Interprétation |
|----------|------------------------|------------------|---|----------------|
| Put/Call Ratio | **1.83** | `null` | +1.83 | 🟡 Baissier atténué mais >1.50 — aligné sur 1.82 du 25/05 |
| Max Pain | **$13.00** | $5.00 (aberrant) | +$8.00 | 🟡 Réalignement complet avec le cours — cohérent avec 25/05 |
| Call OI % | **35.3%** | `null` | +35.3% | 🟡 Repositionnement call confirmé — proche de 35.5% du 25/05 |
| Expiration proche | 2026-05-29 | 2026-05-29 | — | Dans 3 jours — gamma risk concentré autour de $13.00 |

**Interprétation technique :**
- **Aucune mutation technique** entre les snapshots 10:00 et 13:00 UTC. Les niveaux clés ($13.50 support, $14.00–$14.18 résistance, $12.75 SL) restent valides.
- **RSI 71.43 = surachat.** Historiquement, AAL corrige dans les 3–5 jours après franchissement de RSI 70. La probabilité de consolidation ou de repli technique reste élevée.
- **Max Pain $13.00 vs cours $13.85** : le cours reste au-dessus du max pain à 3 jours de l'expiration. Le risque de pinning vers $13.00 persiste si le momentum call faiblit avant le 29/05.
- **Niveau critique : $13.50.** Si cassure en clôture sous ce niveau = fin de l'impulsion haussière. Sous $12.75 = sortie technique obligatoire (2×ATR).
- **Correction data quality** : les valeurs options sont désormais fiables et confirment le setup technique du 25/05 (Put/Call 1.82→1.83, Max Pain $13.00, Call OI 35.5%→35.3%).

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable et figé
- **Price Target moyen FMP : $16.02** (15 analystes, **0 mise à jour le mois dernier**, 3 le trimestre dernier)
- **Upside implicite : +15.7%** vs cours $13.85
- **Couverture :** 15 analystes — coverage significatif mais dormante

### Ratios FMP — Bilan Stressé (inchangé)
| Ratio | Valeur | Seuil | Signal |
|-------|--------|-------|--------|
| P/E (LTM, Yahoo) | 44.68 | — | 🔴 Élevé (charges récentes) |
| Forward P/E | **6.26** | — | 🟡 Réévaluation mécanique — moins cheap |
| P/B (Yahoo) | -2.25 | — | 🔴 Equity négatif |
| P/B (FMP) | -2.72 | — | 🔴 Equity négatif |
| P/S (FMP) | 0.185 | — | 🟢 Très faible |
| EV/EBITDA (Yahoo) | 8.83 | — | 🟡 Élevé vs industrie |
| EV/EBITDA (FMP) | 11.44 | — | 🟡 Élevé vs Yahoo |
| EV/Revenue (Yahoo) | 0.65 | — | 🟢 Faible |
| EV/Revenue (FMP) | 0.81 | — | 🟢 Faible |
| Gross Margin | 19.2% | — | 🟡 Sector norm |
| Operating Margin | 2.7% | — | 🔴 Faible |
| Net Margin | 0.2% | — | 🔴 Quasi nul |
| Current Ratio | 0.50 | >1.0 | 🔴 Trésorerie insuffisante |
| Quick Ratio | 0.38 | >0.8 | 🔴 Liquidity stress |
| Net Debt / EBITDA | 8.83x | <3.0 | 🔴🔴 Extrême |
| Interest Coverage | 0.85x | >2.0 | 🔴 Service dette > EBIT |
| Tangible Asset Value | -$9.88B | >0 | 🔴 Patrimoine négatif |
| Working Capital | -$12.3B | >0 | 🔴 Capacité opérationnelle négative |
| ROE | -3.0% | >10% | 🔴 Destruction de valeur |
| ROIC | 2.0% | >8% | 🔴 Très faible |
| FCF Yield | -6.7% | >0 | 🔴 FCF négatif |
| Debt/Equity | -9.65 | — | 🔴 Equity négatif |
| Revenue per Share | $82.72 | — | 🟢 Élevé (revenue massive) |
| Book Value per Share | -$5.64 | >0 | 🔴 Equity négatif |

### Événement Clé — Earnings Q2 FY2026
- **Date :** 2026-07-23 (**58 jours**)
- **Estimates EPS :** -$0.34 à $0.17
- **Estimates Revenue :** $16.6B
- **Implication :** La fourchette EPS large reflète l'incertitude. Un beat au-dessus de $0.17 reste un catalyseur majeur compte tenu du short interest 12.2% et du put/call 1.83. Le timing d'entrée à $13.85 reste défavorable vs le niveau du 20/05 ($12.06).

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Figé :** 15 analystes FMP, PT $16.02. Aucune mise à jour le mois dernier. Le consensus institutionnel est en attente d'un catalyseur (earnings 23/07).

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz = indifférence retail. Pas de signal contrarian ici.

### Options — Correction Data Quality
- **Put/Call 1.83** : aligné sur la valeur du 25/05 (1.82). Le sentiment reste nettement baissier (>1.50) avec un repositionnement call atténué.
- **Max Pain $13.00** : réalignement complet avec le cours. À expiration 29/05, le pinning mécanique devrait se concentrer autour de $13.00.
- **Call OI 35.3%** : forte accumulation de calls — si le cours tient au-dessus de $13.50 jusqu'à expiration, le gamma squeeze pourrait continuer.
- **Note :** Les valeurs du snapshot 13:00 UTC confirment la fiabilité du setup options du 25/05. L'anomalie du snapshot 10:00 UTC (null/aberrant) est résolue.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🔴 Élevée | Inchangée — dette variable, +1% = +$400M/an |
| Pétrole (WTI) | 🔴🔴 Critique | Inchangée — jet fuel 25-30% coûts |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral, pas de headwind/tailwind) |
| Industriels (XLI) | 🔴 Défavorable | **XLI momentum 0.0, RS20 vs SPY −4.85%** — vent de secteur défavorable |

### Sector Rotation
- **Industrials (XLI)** : return 20d −0.41%, RS20 vs SPY −4.85%. Momentum score 0.0. Pas de crossover détecté.
- **Impact :** Vent de secteur défavorable. Le rally d'AAL reste idiosyncratique (short-covering) et non soutenu par la rotation sectorielle.

### Géopolitique
- **Score Politique :** 2/10 — AAL non exposé aux événements géopolitiques actuels.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**. Le Filtre Qualité (0-1/6) et les ratios FMP (interest coverage <1x, tangible asset value négative) suggèrent une santé financière très faible. Pas de nouvelle alerte comptable.
- **Quant report :** Données insuffisantes — 0 signaux historiques, calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-05-26 10:00 UTC /10 | 2026-05-26 13:00 UTC /10 | Δ | Justification |
|-----|--------------------------|--------------------------|---|---------------|
| Catalyseur | 6.3 | **6.3** | 0.0 | Consensus PT $16.02 inchangé. Upside +15.7%. Earnings 23/07 reste le catalyseur clé. Pas de news structurante. |
| Valorisation | 5.5 | **5.5** | 0.0 | Forward P/E 6.26. Filtre qualité 0-1/6 intact. Pas de mutation de données. |
| Momentum | 5.3 | **5.3** | 0.0 | RSI 71.43 = surachat. Rally +14.8% en 5j. Volume extrême = avertissement distribution. |
| **Score Opportunité** | **5.7** | **5.7** | **0.0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 57.3/100 → **Ajusté 47.3/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse tactique SURVEILLER est **confirmée et stable** entre les snapshots 10:00 et 13:00 UTC. La correction data quality des options renforce la confiance dans les niveaux techniques déjà identifiés sans modifier la conclusion opérationnelle. Le ratio risque/rendement reste dégradé à ce niveau de cours : le SL à $12.75 implique une perte potentielle de −7.9% pour un upside de +11.9% (TP $15.50). La valorisation n'est plus attractive et le RSI surachat indique un risque de repli technique élevé. Le secteur Industriels est en sous-performance. **Maintien de SURVEILLER / ATTENDRE une consolidation.**

---

## Niveaux SL / TP Révisés

| | 2026-05-26 10:00 UTC | 2026-05-26 13:00 UTC | Justification |
|---|----------------------|----------------------|---------------|
| Entrée suggérée | $13.85 | **$13.85** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $12.75 | **$12.75** | Cours − 2×ATR = $13.85 − $1.10. Aligné sur support $12.75–$13.00 |
| Take-Profit | $15.50 | **$15.50** | Cours + 3×ATR = $13.85 + $1.65. Objectif technique sous 52W high |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont inchangés car les données techniques (cours, ATR, MM50) sont strictement identiques au snapshot 10:00 UTC. Le SL $12.75 correspond à la zone $12.75–$13.00 (support technique post-rally). Une cassure sous $12.75 en clôture = invalidation du trend haussier court terme. Le TP $15.50 est conservateur (ancien gap + résistance psychologique). **Expiration options 29/05 dans 3 jours** : le Max Pain $13.00 vs cours $13.85 indique un risque de repli mécanique de $0.85 si le momentum call faiblit. La correction data quality confirme que ce risque est bien réel.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — La thèse SURVEILLER est stable. Mutation mineure : correction data quality options.**

### Ce qui a changé (snapshot 2026-05-26 13:00 UTC vs 10:00 UTC) :
**Correction data quality uniquement.** Les données options dans `data/latest.json` ont été corrigées entre les snapshots 10:00 et 13:00 UTC :
- `put_call_ratio` : `null` → **1.83** (aligné sur 1.82 du 25/05)
- `max_pain` : $5.00 (aberrant) → **$13.00** (cohérent avec le cours)
- `call_oi_pct` : `null` → **35.3%** (proche de 35.5% du 25/05)

Cette correction valide le setup technique et options du 25/05 sans en modifier l'interprétation.

### Ce qui n'a PAS changé (et reste valide) :
1. **Cours $13.85** — Rally +14.8% en 5 séances maintenu. Le trade virtuel du 20/05 aurait généré +11.7%–14.8%.
2. **RSI 71.43** — Franchissement de la zone surachat (70). Probabilité de consolidation/repli technique élevée dans les 3–5 jours.
3. **Volume 99.26M (+71.5%)** — Explosion volumétrique confirmée. Probable short-covering massif ou flux institutionnel.
4. **Forward P/E 6.26** — Réévaluation mécanique. L'asymétrie valorisation s'est réduite.
5. **Put/Call 1.83** — Atténuation du sentiment extrême baissier. Repositionnement call confirmé (Call OI 35.3%).
6. **Max Pain $13.00** — Réalignement complet avec le cours. Gamma risk concentré à expiration 29/05.
7. **Score agent 5.7/10** — Maintien de SURVEILLER, timing défavorable.
8. **Sector rotation défavorable** — Industriels (XLI) en sous-performance. Le rally n'est pas soutenu par le secteur.
9. **Filtre Qualité 0-1/6** — Hors périmètre compounding. AAL reste une commodité sans moat, bilan stressé.
10. **Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value -$9.88B, working capital -$12.3B.
11. **Short Interest 12.21%** — stable. Le fuel de squeeze n'a pas été consommé en masse.
12. **Régime macro défavorable** — Stagflation (fuel, taux élevés, salaires) = pire environnement pour les airlines.
13. **Earnings Q2 = binary event** — 58 jours. Estimates EPS large = forte volatilité post-announcement.

### Risques identifiés (inchangés)
1. **Surachat technique (RSI 71.43)** — Risque de repli de −5% à −8% vers $12.75–$13.00 dans les prochains jours.
2. **Volume extrême sur rally = distribution possible** — Si la prochaine session affiche volume > 80M avec un cours sous $13.50, signal de distribution institutionnelle.
3. **Gamma risk à expiration 29/05** — Dans 3 jours. Max Pain $13.00 vs cours $13.85 = repli mécanique de $0.85 plausible.
4. **Value trap réactivé** — Forward EPS ~$2.21/share peut ne pas se matérialiser si fuel/grèves/récession. Le forward P/E 6.26 n'est pas une protection.
5. **Accounting risk non quantifié** — Absence de scan comptable (M-Score, Z-Score, F-Score, Sloan).
6. **Vent de secteur défavorable** — XLI sous-performe. Un rally sectoriel est nécessaire pour soutenir une continuation au-dessus de $14.00.

### Positionnement Argus-IA
- **Action : SURVEILLER / ATTENDRE** — Ne pas entrer à $13.85. Le trade tactique a eu lieu entre $12.06 et $13.47.
- **Si position virtuelle ouverte depuis le 20/05 :** Réduire de 50% ou placer un stop trailing à $12.75. Le gain +11.7%–14.8% doit être protégé.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 + réaction post-announcement) mais l'entrée est désormais défavorable.
- **Catalyseur clé :** Earnings 2026-07-23. Préparer un nouvel entry si repli vers $12.50–$12.75 sur volume normalisé.
- **Si cours < $12.75 (SL) :** Sortie technique complète — trend haussier invalidé.
- **Si cours > $14.18 (high du 23/05) sur volume > 80M :** Réévaluer le momentum. TP révisable à $15.50–$16.00.
- **Si cours < $13.50 avant expiration 29/05 :** Sortie anticipée — fin de l'impulsion + risque gamma baissier.
- **Si put/call repasse sous 1.50 avec volume calls > 40% OI :** Setup contrarian transformé en setup haussier pur — réévaluer la thèse.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/2026-05-26.json` (snapshot 13:00 UTC) — Cours $13.85, RSI 71.43, ATR $0.55, MM50 $11.71, volume 99.26M, short interest 12.21%, consensus FMP $16.02, options (put/call 1.83, max pain $13.00, call OI 35.3%), Forward P/E 6.26
- `data/recommandations_2026-05-26.json` — Score Opportunité 5.7/10, Score Global 57.3/100 (ajusté 47.3), Recommandation SURVEILLER, SL $12.75, TP $15.50
- `data/validation_report.txt` (2026-05-26) — 5 errors globales (AST/AXA/CYTOMX/QTBS fetch failed ; VRT schema), 2 warnings (IREN, NOK). AAL non concerné.
- `data/sector_rotation_2026-05-26.json` — XLI momentum 0.0, RS20 vs SPY −4.85%
- `data/fx_exposure_2026-05-26.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-05-26.json` — Sentiment retail 0 mentions (EXTREME_BEARISH)
- `data/upcoming_events_2026-05-26.json` — Earnings 2026-07-23, 58 jours
- `data/events_2026-05-26.json` — Aucun événement corporate détecté
- `data/quant_2026-05-17.json` — Données quantitatives insuffisantes
- `data/geo_risk_2026-05-17.json` — Score Politique 2/10, non exposé
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
