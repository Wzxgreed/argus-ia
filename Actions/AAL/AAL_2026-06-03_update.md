# AAL — Mise à Jour 2026-06-03 (Snapshot 13:00 UTC)

**Date :** 2026-06-03 (snapshot 13:00 UTC)  
**Ticker :** AAL (NASDAQ)  
**Type :** Update post-pipeline — Snapshot reflétant la clôture de la session 2026-06-02, stabilité totale des données fondamentales, **correction anomalie options**, thèse SURVEILLER confirmée  
**Cours (close) :** $13.93  
**Previous close :** $14.34  
**Change session :** −2.86%  
**Volume :** 49.41M (vs moy. 20j 67.12M, **−26.4%**)

> **Note :** Ce snapshot 13:00 UTC (`data/latest.json` fetched_at 2026-06-03T13:00:01 UTC) reflète la **clôture officielle de la session 2026-06-02** (même close que le snapshot 10h). Les données techniques, fondamentales et de consensus sont **strictement identiques** au snapshot 10h et 21h du 02/06. **Seule évolution : les données options, corrompues dans le snapshot 10h, sont désormais valides.** Put/Call **1.42** (vs 1.46 au 02/06 21h), Call OI **41.3%** (vs 40.7%), Max Pain **$15.50** (inchangé). **Thèse SURVEILLER confirmée.**

---

## Résumé des Changements depuis l'Update (2026-06-02 21:00 UTC)

| Indicateur | 2026-06-02 21:00 UTC | 2026-06-03 13:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $13.93 | **$13.93** | **Inchangé** |
| RSI 14j | 63.42 | **63.42** | **Inchangé** |
| ATR 14j | $0.61 | **$0.61** | **Inchangé** |
| MM 50j | $12.18 | **$12.18** | **Inchangé** |
| Forward P/E | 6.25 | **6.25** | **Inchangé** |
| Volume total | 49.13M vs 67.11M avg (−26.8%) | **49.41M vs 67.12M avg (−26.4%)** | **+0.28M (+0.6%, arrondi)** |
| Short Interest | 12.87% | **12.87%** | **Inchangé** |
| Consensus FMP PT | $16.60 (17 analystes) | **$16.60 (17 analystes, 2 màj mois, 5 trimestre)** | **Inchangé** |
| Upside vs PT | +19.2% | **+19.2%** | **Inchangé** |
| Put/Call Ratio | 1.46 | **1.42** | **−0.04 (amélioration)** |
| Max Pain | $15.50 | **$15.50** | **Inchangé** |
| Call OI % | 40.7% | **41.3%** | **+0.6 pt (accumulation call)** |
| Earnings Q2 (jours) | 51 | **50** | **−1 (mécanique)** |
| Score Opportunité agent | 6.0/10 | **6.0/10** | **Inchangé** |
| Score Global ajusté | 65.3/100 | **65.3/100** | **Inchangé** |
| Recommandation agent | ACHETER (Sizing Reduit) | **ACHETER (Sizing Reduit)** | **Inchangée** |

**Snapshot 13:00 UTC 03/06 : stabilité totale des données fondamentales, correction options.** Aucune donnée technique ou fondamentale n'a changé par rapport au snapshot 10h et 21h du 02/06. Le cours reste à **$13.93**, le RSI à **63.42**, l'ATR à **$0.61**, et la MM50 à **$12.18**. Le consensus FMP reste à **$16.60** (17 analystes). Le short interest est stable à **12.87%**. Le score Opportunité (**6.0/10**) et le score global ajusté (**65.3/100**) sont inchangés. **Verdict institutionnel : SURVEILLER maintenu.**

> ✅ **Anomalie data quality options RÉSOLUE** : `data/latest.json` (snapshot 13h UTC) retourne désormais des données options valides pour AAL : **Put/Call 1.42, Max Pain $15.50, Call OI 41.3%** (expiration 2026-06-05). Ces valeurs remplacent les données corrompues du snapshot 10h (`max_pain` $5.00 aberrant, `put_call_ratio` null). Les données du snapshot 13h confirment une légère amélioration du setup options vs le snapshot 21h du 02/06 (Put/Call 1.46 → 1.42, Call OI 40.7% → 41.3%).

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $13.93 | −2.86% session 02/06 ; +15.5% vs close 20/05 ($12.06) |
| RSI 14j | 63.42 | 🟡 **Neutre-haussier** — stable, sous la zone proche surachat (70) |
| ATR 14j | $0.61 | Volatilité stable |
| MM 50j | $12.18 | 🟢 Cours +14.3% au-dessus (trend haussier intact) |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 67.12M | 🟡 **−26.4% vs moyenne** — volume after-hours compensateur intégré |
| 52W Range | $10.09–$16.50 | Cours à 84.6% du 52W low, 15.6% sous le 52W high |
| Support clé | ~~$14.00~~ | 🔴 **CASSÉ** — non récupéré à $13.93 |
| Support secondaire | $12.71 | Cours − 2×ATR = $13.93 − $1.22 (SL actuel) |
| Résistance | $15.50 | Max Pain + résistance psychologique |
| Résistance majeure | $16.50 | 52W high + consensus PT zone haute |
| Short Interest | 12.87% | 🟢 Stable — fuel squeeze intact |

**Options — Données corrigées dans latest.json (snapshot 13h UTC) :**

| Métrique | Valeur (snapshot 13h UTC) | Interprétation |
|----------|--------------------------|----------------|
| Put/Call Ratio | **1.42** | 🟡 Baissier atténué — amélioration vs 1.46 (21h 02/06), sentiment neutre-biaisé à la baisse |
| Max Pain | **$15.50** | 🟡 Cours **$1.57 sous le max pain** — pinning mécanique vers le haut à J-2 expiration |
| Call OI % | **41.3%** | 🟢 Accumulation call légèrement renforcée (+0.6 pt vs 40.7%) — paris haussiers maintenus |
| Expiration proche | 2026-06-05 | **Dans 2 jours** — gamma risk centré sur $15.50 |

**Interprétation technique — Stabilité pré-session, support $14.00 toujours cassé, setup options légèrement amélioré :**
- **Cours $13.93 (inchangé)** : la cassure du support clé **$14.00** n'a pas été récupérée. Le cours est en dessous du niveau critique depuis la session du 02/06. En l'absence de nouvelle session dans ce snapshot, aucun élément technique nouveau ne modifie l'interprétation.
- **RSI 63.42 (inchangé)** : stable dans la zone neutre-haussière 50–70. La marge avant surachat reste confortable, mais la stabilité du RSI sans rebond de prix confirme l'absence de momentum acheteur immédiat.
- **Volume 49.41M (−26.4% vs moyenne)** : identique au volume total rapporté à 21h du 02/06 (49.13M). Ce niveau intègre le volume after-hours compensateur. Il reste sous la moyenne 20j mais n'est plus un collapse extrême.
- **Max Pain $15.50 vs cours $13.93** : le cours est $1.57 sous le max pain à J-2 de l'expiration (05/06). Le potentiel mécanique de pinning reste de **+11.3%**. Cependant, la probabilité de réalisation dépendra entièrement du comportement en session régulière aujourd'hui (03/06).
- **Put/Call 1.42 vs 1.46 (21h 02/06)** : légère amélioration du sentiment options. Le ratio put/call continue de se détendre depuis le pic à 4.07 (18/05), confirmant un repositionnement progressif vers les calls. Call OI 41.3% (+0.6 pt) = accumulation call marginale.
- **Niveau critique : $14.00.** La non-récupération de ce support dans le snapshot 13:00 UTC confirme la cassure. Un retour au-dessus de $14.00 en session régulière sur volume > 40M reste nécessaire pour réactiver la thèse ACHETER.
- **Niveau critique : $12.71 (2×ATR).** Une cassure en clôture sous ce niveau = invalidation complète du trend haussier court terme.
- **Niveau critique : $15.50.** Franchissement confirmé au-dessus = réactivation du momentum avec objectif $16.00–$16.50.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $16.60** (17 analystes, **2 mises à jour le mois dernier**, 5 le trimestre dernier) — Inchangé vs 21h 02/06
- **Upside implicite : +19.2%** vs cours $13.93
- **Couverture :** 17 analystes — coverage stable

### Ratios FMP — Inchangés
| Ratio | Valeur | Signal |
|-------|--------|--------|
| P/E (LTM, Yahoo) | 44.94 | 🔴 Élevé (charges récentes) |
| Forward P/E | **6.25** | 🟢 Asymétrie intacte |
| P/B (Yahoo) | -2.26 | 🔴 Equity négatif |
| P/B (FMP) | -2.72 | 🔴 Equity négatif |
| P/S (FMP) | 0.185 | 🟢 Très faible |
| EV/EBITDA (Yahoo) | 8.85 | 🟡 Élevé vs industrie |
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
- **Date :** 2026-07-23 (**50 jours** — vs 51 jours hier)
- **Estimates EPS :** -$0.34 à $0.52 (source yfinance, fourchette large)
- **Estimates Revenue :** $16.6B
- **Implication :** La fourchette EPS large reflète l'incertitude. Un beat au-dessus de $0.52 reste un catalyseur majeur compte tenu du short interest 12.9% et du setup options favorable. La non-récupération du support $14.00 réduit la probabilité d'un rally pré-earnings immédiat. Le timing d'entrée à $13.93 reste acceptable pour un trade tactique mais la prudence est de mise.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Inchangé :** PT moyen $16.60 (17 analystes). Aucune nouvelle mise à jour depuis le 02/06 21h. Le consensus institutionnel reste stable avant les earnings du 23/07.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz = indifférence retail. Pas de signal contrarian.

### Options — Données corrigées dans latest.json (snapshot 13h UTC)
- **Put/Call 1.42** : amélioration vs 1.46 (21h 02/06). Sentiment baissier atténué mais persistant (>1.00). Le ratio continue de se détendre depuis le pic à 4.07 (18/05).
- **Max Pain $15.50** : le cours $13.93 est **$1.57 sous le max pain**. À expiration 05/06 (dans 2 jours), le pinning mécanique pourrait exercer une pression à la hausse de +11.3%.
- **Call OI 41.3%** : accumulation call légèrement renforcée (+0.6 pt vs 40.7%) — paris haussiers stables avant expiration.
- **Risque gamma baissier** : si le cours recule sous $13.50 avant expiration, le dé-hedging des market makers pourrait accélérer la baisse.

### Sector Rotation — Signal stable
- **Industrials (XLI)** : return 20d **+1.88%**, RS20 vs SPY **−3.91%**. Momentum score 0.0.
- **Signal global : NEUTRAL** (inchangé vs 02/06) — la rotation vers les cycliques ne s'est pas réactivée. Le secteur Technologie (XLK) domine toujours avec un momentum score 10.0.
- **Impact AAL :** La perte du signal ROTATION_TO_CYCLICAL continue de retirer un soutien technique au trade.
- **Bonus sectoriel :** Réduit à 0 (signal NEUTRAL).

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🔴 Élevée | Inchangée — dette variable, +1% = +$400M/an |
| Pétrole (WTI) | 🔴🔴 Critique | Inchangée — jet fuel 25-30% coûts |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Industriels (XLI) | 🟡 Stable | RS20 vs SPY −3.91%, signal NEUTRAL |

### Géopolitique
- **Score Politique :** 2/10 — AAL non exposé aux événements géopolitiques actuels.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible** (fichier absent). Le Filtre Qualité (0-1/6) et les ratios FMP suggèrent une santé financière très faible. Pas de nouvelle alerte comptable.
- **Quant report :** Données insuffisantes — 0 signaux historiques, calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-06-02 21:00 UTC /10 | 2026-06-03 13:00 UTC /10 | Δ | Justification |
|-----|--------------------------|--------------------------|---|---------------|
| Catalyseur | 5.8 | **5.8** | **0.0** | Consensus PT stable $16.60. Upside mécanique +19.2%. Earnings 23/07 reste le catalyseur clé. Cassure support $14.00 non récupérée. Options légèrement améliorées (Put/Call 1.42 vs 1.46, Call OI 41.3% vs 40.7%). |
| Valorisation | 5.7 | **5.7** | **0.0** | Forward P/E 6.25 (inchangé). Asymétrie intacte. Filtre qualité 0-1/6 intact mais plafond valorisation inchangé. |
| Momentum | 5.3 | **5.3** | **0.0** | RSI 63.42 (inchangé). Volume 49.41M (−26.4% vs moyenne) — identique au 21h 02/06. Cours stable sous support cassé = pas de momentum acheteur. Signal sectoriel NEUTRAL persistant. |
| **Score Opportunité** | **5.6** | **5.6** | **0.0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 60.3/100 → **Ajusté 62.3/100** (estimation institutionnelle Argus-IA)
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Bonus : sectoriel 0 (signal NEUTRAL)
- Timing : **Neutre** (support cassé, volume partiellement compensé)
- **Recommandation institutionnelle Argus-IA : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse tactique **SURVEILLER est CONFIRMÉE.** Le snapshot 13:00 UTC du 03/06 ne rapporte aucune nouvelle donnée fondamentale par rapport au snapshot 21h du 02/06. Le support **$14.00** reste cassé et non récupéré. Le setup options (Max Pain $15.50, Call OI 41.3%) reste théoriquement favorable avec l'expiration dans 2 jours. **Verdict : maintenir SURVEILLER. Attendre la session régulière du 03/06 pour évaluer le comportement du cours autour de $14.00.**

---

## Niveaux SL / TP Révisés

| | 2026-06-02 21:00 UTC | 2026-06-03 13:00 UTC | Justification |
|---|----------------------|----------------------|---------------|
| Entrée suggérée | $13.93 | **$13.93** | Close actuel — inchangé |
| Stop-Loss | $12.71 | **$12.71** | Cours − 2×ATR = $13.93 − $1.22. Aligné sur support technique $12.75–$13.00 |
| Take-Profit | $15.76 | **$15.76** | Cours + 3×ATR = $13.93 + $1.83. Objectif technique sous 52W high |
| Ratio R/R | 1.5 | **1.5** | Inchangé — Gain $1.83 / Perte $1.22 |

**Note institutionnelle :** Les niveaux sont inchangés car le cours et l'ATR n'ont pas varié. Le SL $12.71 correspond à la zone $12.75–$13.00 (confluence ancien gap + MM50 ascendante). Une cassure sous $12.71 en clôture = invalidation complète du trend haussier court terme. Le TP $15.76 est conservateur. Le Max Pain $15.50 constitue une résistance intermédiaire critique. **Expiration options 05/06 dans 2 jours** : le cours à $13.93 est $1.57 sous le Max Pain. Si le cours tient au-dessus de $13.50 jusqu'à expiration, le pinning vers $15.50 pourrait matérialiser +11.3%. **Setup options légèrement amélioré** : Put/Call 1.42 (vs 1.46), Call OI 41.3% (vs 40.7%) — repositionnement call confirmé.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — La thèse reste SURVEILLER. Le snapshot 13:00 UTC du 03/06 confirme la stabilité totale des données fondamentales par rapport au 02/06 21h. Seule évolution : correction de l'anomalie options dans `data/latest.json`.**

### Ce qui a changé (snapshot 13:00 UTC 03/06 vs 21:00 UTC 02/06) :
1. **✅ Anomalie data quality options RÉSOLUE** — `data/latest.json` (snapshot 13h UTC) retourne désormais des données options valides : Put/Call **1.42** (vs 1.46), Max Pain **$15.50** (inchangé), Call OI **41.3%** (vs 40.7%). Le snapshot 10h retournait des valeurs corrompues (`max_pain` $5.00 aberrant, `put_call_ratio` null).
2. **Earnings 51 → 50 jours** — Décompte mécanique, pas de nouvelle information.
3. **Volume 49.13M → 49.41M** — Différence d'arrondi/precision entre snapshots, pas de nouvelle activité.

### Ce qui n'a PAS changé (et reste valide) :
1. **Support $14.00 cassé** — Non récupéré = niveau technique clé toujours perdu.
2. **Cours $13.93** — Stable sous le support cassé.
3. **RSI 63.42** — Neutre-haussier stable.
4. **Put/Call 1.42** — Atténuation du sentiment extrême baissier. Repositionnement call confirmé (Call OI 41.3%).
5. **Short Interest 12.87%** — Stable. Le fuel de squeeze n'a pas été consommé.
6. **Filtre Qualité 0-1/6** — Hors périmètre compounding. AAL reste une commodité sans moat, bilan stressé.
7. **Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value négatif, working capital négatif.
8. **Régime macro défavorable** — Stagflation (fuel, taux élevés, salaires) = pire environnement pour les airlines.
9. **Earnings Q2 = binary event** — 50 jours. Estimates EPS large = forte volatilité attendue.
10. **Social sentiment extrême baissier** — 0 mentions, absence de buzz retail.
11. **Geo risk 2/10** — Non exposé.
12. **FX exposure 0.0** — Neutral.
13. **Options Max Pain $15.50** — Pinning mécanique vers le haut théoriquement intact.
14. **Consensus FMP $16.60 (17 analystes)** — Inchangé.
15. **Sector signal NEUTRAL** — Pas de vent de secteur favorable.

### Risques identifiés (révisés)
1. **🔴 Cassure du support $14.00 non récupérée** — Le niveau clé est toujours tombé. Sans récupération rapide en session régulière du 03/06, la voie est ouverte vers $13.50 puis $12.75.
2. **🔴 Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value négatif. Risque structurel permanent.
3. **🔴 Régime macro défavorable** — Stagflation = double poids sur les airlines. Le vent de secteur reste NEUTRAL.
4. **🔴 Value trap réactivé** — Forward EPS ~$2.23/share peut ne pas se matérialiser si fuel/grèves/récession.
5. **🔴 Gamma risk inversé** — Si le cours recule sous $13.50 avant expiration 05/06, le dé-hedging des market makers pourrait accélérer la baisse.
6. **🔴 Accounting risk non quantifié** — Absence de scan comptable (M-Score, Z-Score, F-Score, Sloan) sur AAL.
7. **🟡 Pinning vers Max Pain $15.50** — Le potentiel mécanique est de +11.3%. La probabilité dépendra du comportement en session régulière du 03/06.
8. **🟡 Earnings binaire dans 50 jours** — Fourchette EPS -$0.34 à $0.52 = forte volatilité attendue.

### Positionnement Argus-IA
- **Action : SURVEILLER** — La cassure du support $14.00 et l'absence de récupération imposent la prudence. Ne pas entrer de nouvelle position à ce stade.
- **Si position virtuelle ouverte depuis le 20/05 :** Le gain non réalisé se réduit à +15.5% ($12.06 → $13.93). Maintenir la position avec SL ajusté à $12.71. Si le cours ne repasse pas au-dessus de $14.00 en session régulière du 03/06, réduire de 50%.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 + réaction post-announcement).
- **Catalyseur clé court terme :** Expiration options 2026-06-05 (dans 2 jours). Le Max Pain $15.50 reste un aimant mécanique théorique de +11.3%.
- **Catalyseur clé moyen terme :** Earnings 2026-07-23.
- **Si cours < $12.71 (SL) :** Sortie technique complète — trend haussier invalidé.
- **Si cours > $15.50 sur volume > 50M :** Réévaluer le momentum. TP révisable à $16.00–$16.50.
- **Si cours < $13.50 avant expiration 05/06 :** Sortie anticipée — fin de l'impulsion + risque gamma baissier.
- **Si volume en session régulière du 03/06 > 60M avec cours au-dessus de $14.00 :** Réactivation de la thèse ACHETER — récupération du support = signal haussier.
- **Si volume en session régulière du 03/06 < 30M avec cours sous $14.00 :** Distribution confirmée — sortie immédiate si position ouverte.
- **Si put/call repasse sous 1.30 avec volume calls > 45% OI :** Setup contrarian transformé en setup haussier pur — réévaluer la thèse.
- **Si RSI > 70 sur prochain snapshot avec volume > 60M :** Surachat technique — ne pas entrer.

---

## [ANOMALIE]
- **RÉSOLUE** — Données options corrompues dans `data/latest.json` (snapshot 10h UTC) : `max_pain` = $5.00 (aberrant, .00), `put_call_ratio` = null, `call_oi_pct` = null. **Corrigées dans le snapshot 13h UTC** : Put/Call 1.42, Max Pain $15.50, Call OI 41.3%.

## [DONNÉES PARTIELLES]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.
- Validation report 2026-06-03 : 6 errors globales (VRT schema, AST, AXA, SPCX, QTBS, ASTSPACE fetch failed), 2 warnings (IREN, NOK). AAL non concerné.

---

## Références
- `data/2026-06-03.json` (snapshot 13:00 UTC) — Cours $13.93, RSI 63.42, ATR $0.61, MM50 $12.18, volume 49.41M, short interest 12.87%, consensus FMP $16.60 (17 analysts), Forward P/E 6.25, **options corrigées** (Put/Call 1.42, Max Pain $15.50, Call OI 41.3%, expiration 2026-06-05)
- `data/recommandations_2026-06-03.json` — Score Opportunité 6.0/10, Score Global 60.3/100 (ajusté 65.3), Recommandation ACHETER sizing réduit, SL $12.71, TP $15.76, ratio R/R 1.5
- `data/validation_report.txt` (2026-06-03) — 6 errors (VRT schema, AST, AXA, SPCX, QTBS, ASTSPACE fetch failed), 2 warnings (IREN, NOK). AAL non concerné.
- `data/sector_rotation_2026-06-03.json` — XLI return 20d +1.88%, RS20 vs SPY −3.91%, momentum score 0.0, signal NEUTRAL
- `data/fx_exposure_2026-06-03.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-03.json` — Sentiment retail 0 mentions (EXTREME_BEARISH)
- `data/upcoming_events_2026-06-03.json` — Earnings 2026-07-23, 50 jours, Est EPS -$0.34 à $0.52, Rev $16.6B
- `data/events_2026-06-03.json` — Aucun événement corporate détecté
- `data/geo_risk_latest.json` — Score Politique 2/10, non exposé
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
