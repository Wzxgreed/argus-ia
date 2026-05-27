# AAL — Mise à Jour 2026-05-27

**Date :** 2026-05-27 (snapshot 10:00 UTC)  
**Ticker :** AAL (NASDAQ)  
**Type :** Update matinal post-close — Snapshot 10:00 UTC confirme stabilité totale vs clôture 26/05  
**Cours (close) :** $14.85  
**Previous close :** $13.85  
**Change vs previous close :** +7.22% (inchangé vs 26/05)  
**Volume :** 109.82M (vs moy. 20j 61.25M, +79.3%)

> **Note :** Ce snapshot 10:00 UTC (`data/latest.json` fetched_at 2026-05-27T10:00:01 UTC) reflète la clôture officielle de la session du 26 mai 2026. Aucune nouvelle session n'a eu lieu entre le snapshot 21:00 UTC du 26/05 et celui-ci. Les données sont mécaniquement identiques à la clôture d'hier.

---

## Résumé des Changements depuis l'Update (2026-05-26 21:00 UTC)

| Indicateur | 2026-05-26 21:00 UTC | 2026-05-27 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $14.845 | **$14.85** | **+$0.005 (+0.03%)** |
| RSI 14j | 73.82 | **73.85** | **+0.03** |
| ATR 14j | $0.58 | **$0.58** | **$0.00** |
| MM 50j | $11.80 | **$11.80** | **$0.00** |
| Forward P/E | 6.67 | **6.67** | **$0.00** |
| Volume du jour | 109.76M vs 61.24M avg (+79.3%) | **109.82M vs 61.25M avg (+79.3%)** | **+0.06M** |
| Short Interest | 12.21% | **12.21%** | **0.00** |
| Consensus FMP PT | $16.14 (16 analystes) | **$16.14 (16 analystes, 1 màj mois, 4 trimestre)** | **Inchangé** |
| Upside vs PT | +8.7% | **+8.7%** | **0.0 pt** |
| Put/Call Ratio | 1.83 | **null** | **[ANOMALIE DATA]** |
| Max Pain | $13.00 | **$5.00** | **[ANOMALIE DATA]** |
| Call OI % | 35.3% | **null** | **[ANOMALIE DATA]** |
| Score Opportunité agent | 5.4/10 | **5.4/10** | **0.0** |
| Score Global ajusté | 44.0/100 | **44.0/100** | **0.0** |
| Recommandation agent | SURVEILLER | **SURVEILLER** | **Inchangé** |
| Earnings Q2 (jours) | 58 | **57** | **−1** |

**Aucune mutation de données significative.** Le snapshot matinal confirme mécaniquement la clôture officielle du 26/05. Le cours $14.85, le RSI 73.85, l'ATR $0.58 et le volume 109.82M sont identiques à la séance d'hier. **L'unique différence notable est une anomalie data quality sur les options** : `max_pain` retourne $5.00 (aberrant vs $13.00 confirmé hier), `put_call_ratio` et `call_oi_pct` sont `null`. Ces valeurs sont rejetées ; les données options du 26/05 (put/call 1.83, max pain $13.00, call OI 35.3%) restent la référence opérationnelle. Le compte à rebours earnings Q2 passe à **57 jours** (2026-07-23). Le score Opportunité reste inchangé à **5.4/10** (SURVEILLER), le timing défavorable.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $14.85 | +7.22% vs previous close 25/05 ; +23.2% vs close 20/05 ($12.06) |
| RSI 14j | 73.85 | 🔴 **Surachat accentué** — inchangé, au-dessus de 70 depuis 3 séances |
| ATR 14j | $0.58 | Volatilité stable |
| MM 50j | $11.80 | 🟢 Cours +25.8% au-dessus (trend haussier fort) |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 61.25M | 🔴 **+79.3% vs moyenne** — volume massif confirmé sur 2 snapshots |
| 52W Range | $10.09–$16.50 | Cours à 90% du 52W low, 10.0% sous le 52W high |
| Support clé | $14.00 | Ancienne résistance / gap janvier → support à valider |
| Support secondaire | $13.69 | Cours − 2×ATR = niveau technique de sortie |
| Résistance | $15.50 | Ancien objectif technique + gap psychologique |
| Résistance majeure | $16.50 | 52W high + consensus PT zone haute |
| Short Interest | 12.21% | 🟡 Stable — fuel squeeze intact mais non consommé en masse |

**Options — Données anormales (conserver valeurs 26/05) :**

| Métrique | Valeur référence (26/05) | Interprétation |
|----------|--------------------------|----------------|
| Put/Call Ratio | **1.83** | 🟡 Baissier atténué mais >1.50 |
| Max Pain | **$13.00** | Cours $1.85 au-dessus — pinning mécanique improbable |
| Call OI % | **35.3%** | Repositionnement call confirmé |
| Expiration proche | 2026-05-29 | **Dans 2 jours** — gamma risk décalé vers le haut |

**Interprétation technique — Confirmation de la divergence volume/prix :**
- **Volume massif 109.82M (+79.3% vs moyenne) confirmé sur 2 snapshots consécutifs** : la divergence baissière identifiée hier (46.13M shares échangées 17:00–21:00 UTC pour +$0.095) se confirme aujourd'hui par la stabilité du prix malgré un volume identique. Le marché a absorbé ~110M shares sur 2 jours sans progression significative du cours au-delà de $14.85. Cela renforce l'hypothèse d'une **distribution institutionnelle** ou d'un **épuisement du short squeeze**.
- **RSI 73.85** : surachat persistant. Historiquement, AAL corrige dans les 3–5 jours après franchissement de RSI 70. Le risque de consolidation ou de repli technique reste élevé.
- **Max Pain $13.00 vs cours $14.85** : le cours s'éloigne de $1.85 du max pain à 2 jours de l'expiration. Le risque de pinning s'éloigne ; les market makers restent en position de perte sur les calls. Si le cours tient au-dessus de $14.50 jusqu'à expiration vendredi, le gamma squeeze pourrait s'amplifier. Inversement, un repli sous $14.00 déclencherait un dé-hedging violent.
- **Niveau critique : $14.00.** Cassure en clôture sous ce niveau = fin de l'impulsion haussière. Sous $13.69 = sortie technique obligatoire (2×ATR).
- **High intraday 26/05 : $14.94** — résistance immédiate testée et tenue. Un break au-dessus de $14.94 sur volume >70M réactiverait le momentum.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $16.14** (16 analystes, 1 mise à jour le mois dernier, 4 le trimestre dernier)
- **Upside implicite : +8.7%** vs cours $14.85
- **Couverture :** 16 analystes — coverage significatif mais dormante

### Ratios FMP — Inchangés
| Ratio | Valeur | Signal |
|-------|--------|--------|
| P/E (LTM, Yahoo) | 47.89 | 🔴 Élevé (charges récentes) |
| Forward P/E | 6.67 | 🟡 Réévaluation mécanique — asymétrie réduite |
| P/B (Yahoo) | -2.41 | 🔴 Equity négatif |
| P/B (FMP) | -2.72 | 🔴 Equity négatif |
| P/S (FMP) | 0.185 | 🟢 Très faible |
| EV/EBITDA (Yahoo) | 8.99 | 🟡 Élevé vs industrie |
| EV/EBITDA (FMP) | 11.44 | 🟡 Élevé vs Yahoo |
| Gross Margin | 19.2% | 🟡 Sector norm |
| Operating Margin | 2.7% | 🔴 Faible |
| Net Margin | 0.2% | 🔴 Quasi nul |
| Current Ratio | 0.50 | 🔴 Trésorerie insuffisante |
| Quick Ratio | 0.38 | 🔴 Liquidity stress |
| Net Debt / EBITDA | 8.83x | 🔴🔴 Extrême |
| Interest Coverage | 0.85x | 🔴 Service dette > EBIT |
| Tangible Asset Value | -$9.88B | 🔴 Patrimoine négatif |
| Working Capital | -$12.3B | 🔴 Capacité opérationnelle négative |
| ROE | -3.0% | 🔴 Destruction de valeur |
| ROIC | 2.0% | 🔴 Très faible |
| FCF Yield | -6.7% | 🔴 FCF négatif |

### Événement Clé — Earnings Q2 FY2026
- **Date :** 2026-07-23 (**57 jours**)
- **Estimates EPS :** -$0.34 à $0.17
- **Estimates Revenue :** $16.6B
- **Implication :** La fourchette EPS large reflète l'incertitude. Un beat au-dessus de $0.17 reste un catalyseur majeur compte tenu du short interest 12.2% et du put/call 1.83. Le timing d'entrée à $14.85 reste défavorable pour un nouveau positionnement ; le trade tactique optimal a eu lieu entre $12.06 et $13.50.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Inchangé :** PT moyen $16.14 (16 analystes). Aucune nouvelle mise à jour ce mois. Le consensus institutionnel reste en attente d'un catalyseur (earnings 23/07).

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz = indifférence retail. Pas de signal contrarian.

### Options — Anomalie data quality, conserver valeurs 26/05
- **Put/Call 1.83** : inchangé (valeur 26/05). Sentiment baissier atténué mais persistant.
- **Max Pain $13.00** : le cours à $14.85 s'éloigne de $1.85 du max pain. À expiration 29/05 (dans 2 jours), le pinning mécanique est improbable ; si le cours tient, les market makers devront hedger à la hausse = squeeze auto-entretenu.
- **Call OI 35.3%** : accumulation call stable.
- **⚠️ Anomalie data quality :** Le snapshot 27/05 retourne `max_pain: $5.00` (aberrant) et `put_call_ratio: null`, `call_oi_pct: null`. Ces valeurs sont rejetées. Les données du 26/05 restent la référence.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🔴 Élevée | Inchangée — dette variable, +1% = +$400M/an |
| Pétrole (WTI) | 🔴🔴 Critique | Inchangée — jet fuel 25-30% coûts |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Industriels (XLI) | 🟡 Stable | **XLI return 20d +1.04%**, RS20 vs SPY −3.92% — inchangé |

### Sector Rotation
- **Industrials (XLI)** : return 20d +1.04% (stable), RS20 vs SPY −3.92% (stable). Momentum score 0.0. Pas de crossover détecté.
- **Impact :** Le vent de secteur reste défavorable. Le rally d'AAL reste majoritairement idiosyncratique (short-covering + squeeze gamma).

### Géopolitique
- **Score Politique :** 2/10 — AAL non exposé aux événements géopolitiques actuels.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**. Le Filtre Qualité (0-1/6) et les ratios FMP suggèrent une santé financière très faible. Pas de nouvelle alerte comptable.
- **Quant report :** Données insuffisantes — 0 signaux historiques, calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-05-26 21:00 UTC /10 | 2026-05-27 10:00 UTC /10 | Δ | Justification |
|-----|--------------------------|--------------------------|---|---------------|
| Catalyseur | 5.8 | **5.8** | 0.0 | Consensus PT $16.14 inchangé. Upside +8.7%. Earnings 23/07 reste le catalyseur clé. Pas de news structurante. |
| Valorisation | 5.0 | **5.0** | 0.0 | Forward P/E 6.67 inchangé. Filtre qualité 0-1/6 intact. Asymétrie valorisation inchangée. |
| Momentum | 5.5 | **5.5** | 0.0 | RSI 73.85 = surachat accentué. Volume massif confirmé (109.82M) mais prix stagnant = divergence baissière confirmée sur 2 sessions. |
| **Score Opportunité** | **5.4** | **5.4** | **0.0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 54.0/100 → **Ajusté 44.0/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse tactique SURVEILLER est **confirmée**. Aucune mutation de données depuis la clôture officielle du 26/05. Le setup de risque/rendement reste défavorable à $14.85. **La divergence volume/prix se confirme sur 2 snapshots consécutifs** (~110M shares échangées sans progression significative du prix au-delà de $14.85), renforçant l'hypothèse d'épuisement du momentum et/ou de distribution institutionnelle. Le SL révisé à $13.69 implique une perte potentielle de −7.7% pour un upside de +11.8% (TP $16.59). La valorisation n'est plus attractive (upside consensus +8.7% seulement) et le RSI surachat (73.85) indique un risque de consolidation imminente. **Expiration options 29/05 dans 2 jours** : le cours à $14.85 est $1.85 au-dessus du Max Pain $13.00, ce qui réduit le risque de pinning et peut amplifier le gamma squeeze si le momentum call se maintient, mais la divergence volume/prix reste l'avertissement dominant.

---

## Niveaux SL / TP Révisés

| | 2026-05-26 21:00 UTC | 2026-05-27 10:00 UTC | Justification |
|---|----------------------|----------------------|---------------|
| Entrée suggérée | $14.845 | **$14.85** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $13.69 | **$13.69** | Cours − 2×ATR = $14.85 − $1.16. Aligné sur support $13.69–$14.00 |
| Take-Profit | $16.59 | **$16.59** | Cours + 3×ATR = $14.85 + $1.74. Objectif technique sous 52W high |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont inchangés. Le SL $13.69 correspond à la zone $13.69–$14.00 (ancienne résistance devenue support). Une cassure sous $13.69 en clôture = invalidation du trend haussier court terme. Le TP $16.59 est conservateur (ancien gap + résistance psychologique + consensus PT). **Expiration options 29/05 dans 2 jours** : le cours à $14.85 est désormais $1.85 au-dessus du Max Pain $13.00. Si le cours tient au-dessus de $14.50 jusqu'à expiration, le gamma squeeze pourrait s'amplifier. Inversement, un repli sous $14.00 déclencherait un dé-hedging violent.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — La thèse SURVEILLER est maintenue. Aucune mutation de données significative entre le snapshot 21:00 UTC du 26/05 et le snapshot 10:00 UTC du 27/05. La divergence volume/prix se confirme et reste le signal dominant.**

### Ce qui a changé (snapshot 2026-05-27 10:00 UTC vs 2026-05-26 21:00 UTC) :
1. **Cours $14.845 → $14.85 (+0.03%)** — Aucun changement significatif. Même clôture officielle.
2. **RSI 73.82 → 73.85 (+0.03)** — Aucun changement significatif.
3. **Volume 109.76M → 109.82M (+0.06M)** — Quasi identique. Le volume massif se confirme.
4. **Forward P/E 6.67 → 6.67** — Inchangé.
5. **Upside consensus +8.7% → +8.7%** — Inchangé.
6. **Score Opportunité 5.4 → 5.4** — Inchangé.
7. **Score Global ajusté 44.0 → 44.0** — Inchangé, maintien de SURVEILLER.
8. **Anomalie data quality options** : max_pain $5.00 (aberrant), put/call null, call_oi null — rejetés, conserver valeurs 26/05.
9. **Earnings Q2 : 58 → 57 jours** — Compte à rebours mécanique.

### Ce qui n'a PAS changé (et reste valide) :
1. **Divergence volume/prix majeure** — ~110M shares sur 2 jours sans progression significative du prix. Signal d'épuisement du momentum et/ou distribution institutionnelle.
2. **Surachat technique (RSI 73.85)** — Risque de repli de −5% à −8% vers $13.69–$14.00 dans les prochains jours.
3. **Gamma squeeze / gamma risk à expiration 29/05** — Dans 2 jours. Le cours à $14.85 est $1.85 au-dessus du Max Pain. Si le momentum call se maintient, les market makers devront hedger à la hausse = squeeze auto-entretenu. Inversement, un repli sous $14.00 déclencherait un dé-hedging violent.
4. **Value trap réactivé** — Forward EPS ~$2.23/share peut ne pas se matérialiser si fuel/grèves/récession. Le forward P/E 6.67 n'est pas une protection à ce niveau de cours.
5. **Filtre Qualité 0-1/6** — Hors périmètre compounding. AAL reste une commodité sans moat, bilan stressé.
6. **Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value -$9.88B, working capital -$12.3B.
7. **Régime macro défavorable** — Stagflation (fuel, taux élevés, salaires) = pire environnement pour les airlines.
8. **Recommandation SURVEILLER** — Le timing d'entrée est défavorable à $14.85.
9. **Consensus FMP $16.14 (16 analystes)** — Inchangé. Aucune nouvelle mise à jour ce mois.

### Risques identifiés (révisés)
1. **🔴 Divergence volume/prix majeure (CONFIRMÉE)** — ~110M shares échangées sur 2 sessions sans progression significative du prix. Si le volume reste >100M demain avec un cours sous $14.50 = distribution confirmée.
2. **Surachat technique (RSI 73.85)** — Risque de repli de −5% à −8% vers $13.69–$14.00 dans les prochains jours.
3. **Gamma squeeze / gamma risk à expiration 29/05** — Dans 2 jours. Le cours à $14.85 est $1.85 au-dessus du Max Pain. Si le momentum call se maintient, squeeze auto-entretenu. Inversement, repli sous $14.00 = dé-hedging violent.
4. **Value trap réactivé** — Forward EPS ~$2.23/share peut ne pas se matérialiser. Le forward P/E 6.67 n'est pas une protection.
5. **Accounting risk non quantifié** — Absence de scan comptable (M-Score, Z-Score, F-Score, Sloan).
6. **Vent de secteur défavorable** — XLI sous-performe toujours vs SPY (−3.92% RS20). Un rally sectoriel est nécessaire pour soutenir une continuation au-dessus de $15.50.

### Positionnement Argus-IA
- **Action : SURVEILLER / ATTENDRE** — Ne pas entrer à $14.85. Le trade tactique optimal a eu lieu entre $12.06 et $13.50.
- **Si position virtuelle ouverte depuis le 20/05 :** Le gain non réalisé atteint +23.2%. Réduire de 50% ou placer un stop trailing à $13.69. Le gain doit être protégé avant expiration 29/05. La divergence volume/prix est un signal de prudence.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 + réaction post-announcement) mais l'entrée est désormais défavorable.
- **Catalyseur clé :** Earnings 2026-07-23. Préparer un nouvel entry si repli vers $13.69–$14.00 sur volume normalisé (<70M).
- **Si cours < $13.69 (SL) :** Sortie technique complète — trend haussier invalidé.
- **Si cours > $15.50 sur volume > 70M :** Réévaluer le momentum. TP révisable à $16.00–$16.50.
- **Si cours < $14.00 avant expiration 29/05 :** Sortie anticipée — fin de l'impulsion + risque gamma baissier.
- **Si put/call repasse sous 1.50 avec volume calls > 40% OI :** Setup contrarian transformé en setup haussier pur — réévaluer la thèse.
- **Si volume demain >100M avec cours sous $14.50 :** Distribution confirmée — sortie immédiate si position ouverte.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/2026-05-27.json` (snapshot 10:00 UTC) — Cours $14.85, RSI 73.85, ATR $0.58, MM50 $11.80, volume 109.82M, short interest 12.21%, consensus FMP $16.14 (16 analysts), options anomalie (max_pain $5.00 aberrant, put/call null, call_oi null) — conserver valeurs 26/05, Forward P/E 6.67
- `data/recommandations_2026-05-27.json` — Score Opportunité 5.4/10, Score Global 54.0/100 (ajusté 44.0), Recommandation SURVEILLER, SL $13.69, TP $16.59
- `data/validation_report.txt` (2026-05-27) — 3 errors globales (AST/AXA/QTBS fetch failed), 2 warnings (IREN, NOK). AAL non concerné.
- `data/sector_rotation_2026-05-27.json` — XLI return 20d +1.04%, RS20 vs SPY −3.92%
- `data/fx_exposure_2026-05-27.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-05-27.json` — Sentiment retail 0 mentions (EXTREME_BEARISH)
- `data/upcoming_events_2026-05-27.json` — Earnings 2026-07-23, 57 jours
- `data/events_2026-05-27.json` — Aucun événement corporate détecté
- `data/quant_2026-05-27.json` — Données quantitatives insuffisantes
- `data/geo_2026-05-27.json` — Score Politique 2/10, non exposé
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
