# AAL — Mise à Jour 2026-06-09 (Snapshot 10h UTC)

**Date :** 2026-06-09 (snapshot 10h UTC)  
**Ticker :** AAL (NASDAQ)  
**Type :** Update post-pipeline — Snapshot matinal, **stabilité totale vs clôture 08/06**, anomalie options récurrente, thèse **ACHETER (Sizing Réduit) CONFIRMÉE avec vigilance accrue J-3**
**Cours (close) :** $13.60  
**Previous close :** $13.50  
**Change session :** +0.74%  
**Volume :** 109.04M (vs moy. 20j 72.64M, **+50.1%**)

> **Note :** Ce snapshot 10h UTC (`data/latest.json` fetched_at 2026-06-09T10:00:11 UTC) reflète la **clôture officielle de la session 2026-06-08** (16h00 ET / 20h00 UTC) + after-hours. Les données de prix, RSI et volumes sont quasi identiques au snapshot 21h UTC du 08/06, confirmant la stabilité totale du ticker en l'absence de nouvelle session US depuis la dernière mise à jour. **Anomalie data quality majeure :** les données options sont à nouveau corrompues (Max Pain $5.00 aberrant, Put/Call null, Call OI null), répétant le pattern observé le 02/06 et le 20/05.

---

## Résumé des Changements depuis l'Update (2026-06-08 21:00 UTC)

| Indicateur | 2026-06-08 21:00 UTC | 2026-06-09 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $13.60 | **$13.60** | **Inchangé** |
| RSI 14j | 62.2 | **62.2** | **Inchangé** |
| ATR 14j | $0.63 | **$0.63** | **Inchangé** |
| MM 50j | $12.40 | **$12.40** | **Inchangé** |
| Forward P/E | 6.10 | **6.10** | **Inchangé** |
| Volume total | 108.46M vs 72.61M avg (+49.4%) | **109.04M vs 72.64M avg (+50.1%)** | **+0.58M (after-hours marginaux)** |
| Short Interest | 12.87% | **12.87%** | **Inchangé** |
| Consensus FMP PT | $16.60 (17 analystes) | **$16.60 (17 analystes, 2 màj mois, 5 trimestre)** | **Inchangé** |
| Upside vs PT | +22.1% | **+22.1%** | **Inchangé** |
| Options | Max Pain $13.00, Put/Call 1.92, Call OI 34.2% | **🔴 ANOMALIE : Max Pain $5.00 (.00), Put/Call null, Call OI null** | **🔴 Données corrompues — régression data quality** |
| Earnings Q2 (jours) | 45 | **44** | **−1j** |
| Score Opportunité agent | 6.0/10 | **6.0/10** | **Inchangé** |
| Score Global ajusté | 65.3/100 | **65.3/100** | **Inchangé** |
| Recommandation agent | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | **Confirmée** |

**Verdict institutionnel :** Stabilité totale des données fondamentales et techniques. Le snapshot 10h UTC du 09/06 ne capture pas une nouvelle session US mais la clôture consolidée du 08/06. L'**anomalie options récurrente** (Max Pain $5.00, Put/Call null) oblige à utiliser les dernières données valides connues (snapshot 21h 08/06 : Max Pain $13.00, Put/Call 1.92, Call OI 34.2%). La thèse **ACHETER (Sizing Réduit) est CONFIRMÉE**, mais la proximité de l'expiration (J-3, 12/06) sans données options fiables augmente l'incertitude gamma. La prudence est impérative.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $13.60 | +0.74% session (close 08/06) ; range intraday $13.41–$13.80 (close 08/06) |
| RSI 14j | 62.2 | 🟡 **Neutre-haussier** — inchangé, marge avant surachat intacte |
| ATR 14j | $0.63 | Volatilité stable |
| MM 50j | $12.40 | 🟢 Cours +9.7% au-dessus (trend haussier intact) |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 72.64M | 🟡 **+50.1% vs moyenne** — accumulation volumique confirmée, stable vs 108.46M close 08/06 |
| 52W Range | $10.09–$16.50 | Cours à 83.0% du 52W low, 17.6% sous le 52W high |
| Support clé | ~~$14.00~~ | 🔴 **CASSÉ depuis le 02/06** — non récupéré ($13.60 < $14.00) |
| Support secondaire | $13.20 | Low du 08/06 $13.41 — zone de confluence tenue |
| Support technique | $12.34 | Cours − 2×ATR = $13.60 − $1.26 (SL inchangé) |
| Résistance | $13.80 | High du 08/06 — rejet net en clôture |
| Résistance majeure | $16.50 | 52W high + consensus PT zone haute |
| Short Interest | 12.87% | 🟢 Stable — fuel squeeze intact |

**Options — 🔴 ANOMALIE DATA QUALITY RÉCURRENTE**

| Métrique | Valeur (snapshot 10h UTC 09/06) | Statut |
|----------|--------------------------------|--------|
| Max Pain | **$5.00** | 🔴 **Aberrant (.00)** — pattern de corruption récurrent |
| Put/Call Ratio | **null** | 🔴 **Donnée manquante** |
| Call OI % | **null** | 🔴 **Donnée manquante** |
| Expiration proche | **2026-06-12** | 🔴 **Dans 3 jours** — risque gamma élevé |

> **Règle de gestion de l'anomalie :** Les données options du snapshot 10h UTC sont corrompues (Max Pain $5.00 = pattern `.00` observé le 02/06 et le 20/05). L'agent utilise les **dernières données valides fiables** : snapshot 21h UTC 08/06 (Put/Call 1.92, Max Pain $13.00, Call OI 34.2%). Cependant, l'absence de données fraîches pour le 09/06 empêche de détecter un repositionnement overnight. L'incertitude gamma à J-3 est **maximale**.

**Interprétation technique — Stabilité totale, incertitude options :**
- **Cours $13.60 (+0.74%)** : inchangé vs close 08/06. Pas de nouvelle session US entre le snapshot 21h 08/06 et 10h 09/06.
- **Volume 109.04M (+50.1%)** : quasi identique au close 08/06 (108.46M). Les 0.58M supplémentaires correspondent aux after-hours — insignifiants.
- **RSI 62.2** : inchangé. La détente technique post-rally du 25–27/05 est stabilisée.
- **ATR $0.63** : inchangé. Volatilité historique stable.
- **Options — Anomalie critique :** Le pattern de corruption `.00` sur le Max Pain ($5.00) a été observé précédemment le 02/06 (max pain $5.00, corrigé à $15.50 en après-midi) et le 20/05 (max pain $5.00, corrigé le 25/05 à $13.00). Cela suggère une instabilité dans la source de données options (Yahoo Finance) en début de pipeline. À J-3 de l'expiration (12/06), l'incapacité à monitorer le repositionnement options est un **handicap majeur**.
- **Support $14.00** : toujours cassé et non récupéré depuis le 02/06. Aucun changement.
- **Support $13.20** : le low du 08/06 ($13.41) a tenu. Une cassure sous $13.20 en clôture = retour vers $12.75–$13.00.
- **Niveau critique $13.00 (Max Pain valide)** : avec les dernières données valides (Max Pain $13.00), le cours à $13.60 reste $0.60 au-dessus. À J-3, toute clôture sous $13.00 risque de déclencher un gamma squeeze baissier.
- **Niveau critique $12.34 (2×ATR)** : cassure = invalidation du trend haussier court terme.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $16.60** (17 analystes, **2 mises à jour le mois dernier**, 5 le trimestre dernier) — Inchangé vs 08/06
- **Upside implicite : +22.1%** vs cours $13.60
- **Couverture :** 17 analystes — coverage stable

### Ratios FMP — Inchangés
| Ratio | Valeur | Signal |
|-------|--------|--------|
| P/E (LTM, Yahoo) | 43.87 | 🔴 Élevé (charges récentes) |
| Forward P/E | **6.10** | 🟢 Asymétrie intacte |
| P/B (Yahoo) | -2.21 | 🔴 Equity négatif |
| P/B (FMP) | -2.72 | 🔴 Equity négatif |
| P/S (FMP) | 0.185 | 🟢 Très faible |
| EV/EBITDA (Yahoo) | 8.78 | 🟡 Élevé vs industrie |
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

**Évolution fondamentale :** Aucun changement structurel. Le Forward P/E 6.10 reste le niveau clé d'asymétrie. Le bilan reste extrêmement fragile et le Filtre Qualité à 0-1/6 intact.

### Événement Clé — Earnings Q2 FY2026
- **Date :** 2026-07-23 (**44 jours** — −1j vs 08/06)
- **Estimates EPS :** -$0.34 à $0.52 (source yfinance, fourchette large)
- **Estimates Revenue :** $16.6B
- **Implication :** Inchangée. Le binary event approche (J-44). Le setup options dégradé et l'anomalie data quality réduisent la visibilité sur le positioning pré-earnings.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Inchangé :** PT moyen $16.60 (17 analystes). Aucune nouvelle mise à jour depuis le 03/06. Le consensus institutionnel reste stable avant les earnings du 23/07.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** No data — absence de buzz = indifférence retail. Pas de signal contrarian.

### Options — 🔴 ANOMALIE DATA QUALITY RÉCURRENTE (J-3 CRITIQUE)
- **Données snapshot 10h 09/06 : CORROMPUES** — Max Pain $5.00 (pattern `.00`), Put/Call null, Call OI null.
- **Dernières données valides :** snapshot 21h 08/06 — Put/Call 1.92, Max Pain $13.00, Call OI 34.2%.
- **Interprétation :** L'anomalie empêche de monitorer un repositionnement overnight à J-3. Le risque gamma reste élevé mais non quantifiable. La prudence recommande d'assumer que le setup (Put/Call 1.92, Max Pain $13.00) est inchangé sauf preuve du contraire.
- **Risque gamma baissier persistant** : avec les dernières données valides (Max Pain $13.00 vs cours $13.60) et Put/Call 1.92, le setup gamma reste défavorable. Une clôture sous $13.00 avant le 12/06 = risque de cascade baissière.

### Sector Rotation — Signal NEUTRAL stable
- **Industrials (XLI)** : return 20d **+0.25%**, RS20 vs SPY **+0.03%**. Momentum score **2.65**.
- **Signal global : NEUTRAL** — inchangé vs 08/06.
- **Impact AAL :** XLI parfaitement aligné avec le S&P 500. Le secteur Industriels n'est pas dans le bottom3 (bottom3 = XLY, XLB, XLC).
- **Bonus sectoriel :** 0 (signal NEUTRAL), headwind sectoriel disparu.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🔴 Élevée | Inchangée — dette variable, +1% = +$400M/an |
| Pétrole (WTI) | 🔴🔴 Critique | Inchangée — jet fuel 25-30% coûts |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Industriels (XLI) | 🟡 Amélioration | RS20 vs SPY +0.03% — convergence sectorielle complète |

### Géopolitique
- **Score Politique :** AAL non exposé aux événements géopolitiques actuels.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible** (fichier absent depuis le 17/05). Le Filtre Qualité (0-1/6) et les ratios FMP suggèrent une santé financière très faible. Pas de nouvelle alerte comptable.
- **Quant report :** Données insuffisantes — 0 signaux historiques, calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-06-08 21h UTC /10 | 2026-06-09 10h UTC /10 | Δ | Justification |
|-----|------------------------|------------------------|---|---------------|
| Catalyseur | 6.1 | **6.1** | **0.0** | Consensus PT stable $16.60. Earnings 23/07 dans 44 jours. RS20 XLI stable +0.03%. Volume 109.04M (+50.1%) confirmé. **Anomalie options = incertitude accrue** — pas de bonus/malus faute de données fiables. |
| Valorisation | 5.5 | **5.5** | **0.0** | Forward P/E 6.10 inchangé. Asymétrie intacte. Filtre qualité 0-1/6 intact, plafond valorisation inchangé. |
| Momentum | 6.3 | **6.3** | **0.0** | RSI 62.2 inchangé. Cours au-dessus MM50 ($12.40) +9.7%. **Anomalie options empêche d'évaluer le momentum options** — maintien du score précédent. |
| **Score Opportunité** | **5.9** | **5.9** | **0.0** | Pondération 35/40/25 (régime inconnu = default). Stabilité totale des inputs. L'anomalie options n'est pas suffisante pour réviser le score à la baisse, mais elle supprime toute marge d'upside. |

> **Note :** L'agent recommandation du pipeline a calculé un score officiel de **6.0/10** (C:6.3 V:5.5 M:6.5) et un Score Global ajusté de **65.3/100** sur la base du snapshot 10h. Après ajustement institutionnel Argus-IA pour l'**anomalie options** (données corrompues à J-3), le score ajusté institutionnel reste **~6.0/10** — l'anomalie est un facteur de risque, pas de scoring.

**Score Global Composite agent :** 60.3/100 → **Ajusté 65.3/100** (officiel pipeline) / **~65.0/100** (ajustement institutionnel anomalie options)
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Bonus : sectoriel 0 (signal NEUTRAL)
- Timing : **Favorable** (volume élevé + au-dessus MM50) mais **Incertitude gamma élevée à J-3**
- **Recommandation agent : ACHETER (Sizing Réduit)**
- **Recommandation institutionnelle Argus-IA : ACHETER (Sizing Réduit) — CONFIRMÉE, vigilance accrue J-3**

**Verdict institutionnel Argus-IA :** La thèse tactique **ACHETER (Sizing Réduit) est CONFIRMÉE.** Le Forward P/E 6.10 est attractif. Le volume 109.04M (+50.1%) confirme l'intérêt institutionnel. Cependant, l'**anomalie options récurrente** à J-3 de l'expiration (12/06) empêche de monitorer le repositionnement gamma. Sans données options fiables, le risque de pinning vers $13.00 ou de cascade sous $13.00 ne peut être quantifié. Le support **$14.00 reste cassé**. Le sizing réduit est impératif. **Aucune nouvelle entrée ne devrait être initiée avant récupération de données options valides ou clôture au-dessus de $14.00.**

---

## Niveaux SL / TP

| | 2026-06-08 21:00 UTC | 2026-06-09 10:00 UTC | Justification |
|---|----------------------|----------------------|---------------|
| Entrée suggérée | $13.60 | **$13.60** | Inchangé — close officiel stable |
| Stop-Loss | $12.34 | **$12.34** | Cours − 2×ATR = $13.60 − $1.26. Aligné sur MM50 $12.40 |
| Take-Profit | $15.49 | **$15.49** | Cours + 3×ATR = $13.60 + $1.89. Objectif technique sous 52W high |
| Ratio R/R | 1.5 | **1.5** | Inchangé — Gain $1.89 / Perte $1.26 |

**Note institutionnelle :** Les niveaux sont inchangés car le cours est stable à $13.60. Le SL $12.34 correspond à la zone MM50 — une cassure sous ce niveau en clôture = invalidation complète du trend haussier court terme. Le TP $15.49 reste conservateur. La zone de **$13.00 (dernier Max Pain valide)** devient un niveau de vigilance intermédiaire critique. À J-3 sans données options fiables, une clôture sous $13.00 = risque gamma inconnu — sortie anticipée partielle (50%) recommandée. **Si données options récupérées et Put/Call < 1.50 avec Max Pain > $14.00 :** réévaluer le momentum. Si cours > $14.00 sur volume > 80M : TP révisable à $15.80–$16.00.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — La thèse reste ACHETER (Sizing Réduit) avec VIGILANCE ACCRUE J-3. Aucun changement de fondamental ou technique, mais anomalie options récurrente = incertitude gamma non quantifiable.**

### Ce qui a changé (snapshot 10h UTC 09/06 vs 21h00 UTC 08/06) :
1. **🟢 Volume après consolidation :** 109.04M vs 108.46M — stabilité totale, +0.58M after-hours marginaux.
2. **🔴 ANOMALIE OPTIONS RÉCURRENTE** — Max Pain $5.00 (pattern `.00`), Put/Call null, Call OI null. Pattern observé le 02/06 et le 20/05. Source Yahoo Finance instable en début de pipeline.
3. **🟡 Earnings dans 44 jours** — −1j vs hier, inchangé en substance.
4. **🟢 Validation report AAL non concerné** — 5 errors globales (VRT schema, AST, AXA, ASTSPACE, QTBS), 3 warnings (SPCX, IREN, NOK). AAL = données complètes.

### Ce qui n'a PAS changé (et reste valide) :
1. **Cours $13.60 (+0.74%)** — stable vs close 08/06.
2. **RSI 62.2** — inchangé, neutre-haussier.
3. **ATR $0.63** — stable.
4. **Forward P/E 6.10** — asymétrie intacte.
5. **Support $14.00 cassé** — toujours non récupéré depuis le 02/06.
6. **Consensus FMP $16.60 (17 analystes)** — inchangé.
7. **Short Interest 12.87%** — stable, fuel squeeze intact.
8. **XLI RS20 vs SPY +0.03%** — convergence sectorielle complète.
9. **Filtre Qualité 0-1/6** — hors périmètre compounding.
10. **Bilan extrêmement fragile** — current ratio 0.50, interest coverage 0.85x, tangible asset value négatif.
11. **Score agent 6.0/10** — dans la zone ACHETER.
12. **Geo risk 2/10** — non exposé.
13. **FX exposure 0.0** — neutral.

### Risques identifiés (révisés)
1. **🔴 Anomalie options à J-3 (12/06)** — Données corrompues empêchent de quantifier le risque gamma. Max Pain valide $13.00 (dernière donnée fiable). À J-3, toute clôture sous $13.00 = risque inconnu. Sortie anticipée partielle (50%) si cours < $13.00.
2. **🔴 Setup options dégradé (dernières données valides)** — Put/Call 1.92, Max Pain $13.00, Call OI 34.2% = repositionnement baissier persistant vs 03/06.
3. **🔴 Cassure du support $14.00 non récupérée** — Le niveau clé reste tombé depuis 6 séances. Sans récupération, la voie est ouverte vers $13.20 puis $12.34.
4. **🔴 Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value négatif. Risque structurel permanent.
5. **🔴 Value trap** — Forward EPS ~$2.23/share peut ne pas se matérialiser si fuel/grèves/récession.
6. **🟡 Earnings binaire dans 44 jours** — Fourchette EPS -$0.34 à $0.52 = forte volatilité attendue.
7. **🟡 Max Pain $13.00 vs cours $13.60** — Le pinning mécanique n'offre pas d'upside significatif. Le cours est $0.60 au-dessus du max pain valide, ce qui est raisonnable mais instable à J-3.

### Positionnement Argus-IA
- **Action : ACHETER (Sizing Réduit) — CONFIRMÉE, vigilance accrue J-3**
- **Sizing max :** 5% du portefeuille (vs 10% standard) compte tenu du bilan fragile, du risque earnings et de l'incertitude gamma options.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 + réaction post-announcement).
- **Catalyseur clé court terme :** Récupération du support $14.00 sur volume > 80M + données options valides avec Put/Call < 1.50.
- **Catalyseur clé moyen terme :** Earnings 2026-07-23.
- **Si cours < $12.34 (SL) :** Sortie technique complète — trend haussier invalidé.
- **Si cours < $13.00 avant expiration 12/06 :** Sortie anticipée partielle (50%) — risque gamma inconnu élevé.
- **Si cours > $14.00 sur volume > 80M avec données options valides Put/Call < 1.50 :** Réévaluer le momentum. TP révisable à $15.80–$16.00.
- **Si volume en prochaine session < 60M avec cours sous $13.20 :** Distribution confirmée — réduire de 50% ou sortir.
- **Si volume en prochaine session > 90M avec cours au-dessus de $14.00 :** Accumulation confirmée — maintenir voire augmenter le sizing.

---

## [ANOMALIE]
- **🔴 ACTIVE (10h 09/06)** — Données options corrompues dans `data/latest.json` (snapshot 10h UTC) : `max_pain` = $5.00 (aberrant, `.00`), `put_call_ratio` = null, `call_oi_pct` = null. **Pattern récurrent** (observé le 02/06 et le 20/05). Corrigé dans les snapshots ultérieurs les jours précédents. L'agent utilise les dernières données valides connues : snapshot 21h UTC 08/06 (Put/Call 1.92, Max Pain $13.00, Call OI 34.2%).

## [DONNÉES PARTIELLES]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `accounting_risk_latest.json` indisponible depuis le 17/05.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.
- Validation report 2026-06-09 : 5 errors globales (VRT schema, AST, AXA, ASTSPACE, QTBS fetch failed), 3 warnings (SPCX volume 0, IREN qualité partielle, NOK hors périmètre). **AAL non concerné — données complètes.**

---

## Références
- `data/2026-06-09.json` (snapshot 10h UTC) — Cours $13.60, RSI 62.2, ATR $0.63, MM50 $12.40, volume 109.04M, short interest 12.87%, consensus FMP $16.60 (17 analysts), Forward P/E 6.10, options CORROMPUES (Max Pain $5.00, Put/Call null, Call OI null)
- `data/recommandations_2026-06-09.json` — Score Opportunité 6.0/10 (C:6.3 V:5.5 M:6.5), Score Global 60.3/100 (ajusté 65.3), Recommandation ACHETER sizing réduit, SL $12.34, TP $15.49, ratio R/R 1.5
- `data/validation_report.txt` (2026-06-09) — 5 errors (VRT schema, AST, AXA, ASTSPACE, QTBS), 3 warnings (SPCX, IREN, NOK). AAL non concerné.
- `data/sector_rotation_2026-06-09.json` — XLI return 20d +0.25%, RS20 vs SPY +0.03%, momentum score 2.65, signal NEUTRAL
- `data/fx_exposure_2026-06-09.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-09.json` — Sentiment retail 0 mentions (No data)
- `data/upcoming_events_2026-06-09.json` — Earnings 2026-07-23, 44 jours, Est EPS -$0.34 à $0.52, Rev $16.6B
- `data/events_2026-06-09.json` — Aucun événement corporate détecté
- `data/geo_risk_latest.json` — Score Politique 2/10 (IREN), AAL non exposé
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
- Données options valides de référence : snapshot 21h UTC 2026-06-08 (Max Pain $13.00, Put/Call 1.92, Call OI 34.2%)
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
