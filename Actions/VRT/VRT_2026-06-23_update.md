# VRT — Mise à jour Snapshot Pré-Marché (10:00 UTC)

> **Date :** 2026-06-23
> **Cours de référence :** $357.96 (+7.48%)
> **Fichier précédent :** [VRT_2026-06-22_update.md](./VRT_2026-06-22_update.md) (close officiel 21:00 UTC, $357.96, RSI 60.41, volume 1.19×)
> **Statut thèse :** CONFIRMÉE — snapshot pré-marché sans nouvelle séance, données techniques inchangées, léger renforcement sectoriel

---

## 1. Résumé des changements depuis l'analyse précédente (22/06 21:00 UTC)

| Métrique | 2026-06-22 21:00 UTC | 2026-06-23 10:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| Cours close | **$357.96** | **$357.96** | **Stable** |
| RSI 14j | 60.41 | **60.41** | Stable |
| ATR 14j | $20.83 | $20.83 | Stable |
| MM 50j | $322.88 | $322.88 | Stable |
| Volume vs 20j | 1.19× (7.24M) | 1.19× (7.27M) | Stable |
| Change % séance | +7.48% | +7.48% | Stable |
| P/E TTM | 89.49 | 89.49 | Stable |
| Forward P/E | 40.44 | 40.44 | Stable |
| Put/Call ratio | 2.77 | 2.77 | Stable |
| Call OI % | 26.5% | 26.5% | Stable |
| Max pain | $245.0 | $245.0 | Stable |
| Consensus PT (FMP) | $267.57 | $267.57 | Stable — écart +33.8% |
| Sector rotation XLI | #2 / momentum 7.27 | **#2 / momentum 7.54** | **+0.27 pts** |
| FX exposure | 45% EUR/CNY, Score 0.0 | 45% EUR/CNY, Score 0.0 | Stable |
| Social sentiment | 0 mentions | 0 mentions | Stable |
| Events corporate | 0 | 0 | Stable |
| Prochain earnings | 2026-07-29 (37 jours) | 2026-07-29 (36 jours) | −1 jour |
| Score Global Ajusté | 50.0/100 (ATTENDRE) | **47.5/100 (SURVEILLER)** | −2.5 pts (moteur) |
| Recommandation moteur | SURVEILLER | **SURVEILLER** | Stable |

**Faits marquants :**
- **Snapshot pré-marché 10:00 UTC strictement identique au close officiel 22/06 21:00 UTC.** Aucune nouvelle séance US n'a eu lieu entre les deux snapshots. Les données techniques, fondamentales et options sont inchangées.
- **Sector rotation XLI momentum amélioré** : 7.54/10 (+0.27 pts vs 7.27/10 au snapshot 22/06). Le secteur Industriels confirme sa position #2 du ranking avec un momentum légèrement renforcé, soutenant la thèse haussière technique.
- **Options inchangées** : put/call 2.77, call OI 26.5%, max pain $245.0, expiration 26/06 (J+3). Sentiment options bearish mesuré stable.
- **Aucun événement corporate** détecté dans `data/events_latest.json`.
- **[DONNÉES MANQUANTES]** : `data/accounting_risk_latest.json` absent — pas de scan M-Score / Z-Score / F-Score / Sloan Ratio.
- **[DONNÉES MANQUANTES]** : `data/quant_report_latest.json` obsolète (2026-05-17) — pas de métriques de risque institutionnelles à jour.

---

## 2. Mise à jour technique

| Indicateur | Valeur | Signal |
|-------------|--------|--------|
| Cours | $357.96 | — |
| RSI 14j | 60.41 | Neutre haussier (zone 60, pas de surachat) |
| ATR 14j | $20.83 | Élevé (5.82% du cours) |
| MM 50j | $322.88 | Cours +10.9% au-dessus — tendance haussière court terme intacte |
| MM 200j | N/A | — |
| Golden Cross | N/A | — |
| Volume 20j moy. | 6,080,745 | — |
| Volume séance | 7,269,400 | **1.19× — accumulation confirmée** |
| 52-week high | $379.935 | Cours −5.8% du sommet |
| 52-week low | $110.06 | Cours +225% du plancher |

**Niveaux clés (inchangés) :**
- **Support 1** : $350.00 (ancienne résistance → support)
- **Support 2** : $338.24 (low du 22/06)
- **Support 3** : $322.88 (MM 50j)
- **Résistance 1** : $358.54 (high intraday 22/06)
- **Résistance 2** : $379.935 (52-week high)
- **Résistance 3** : $400.00 (alerte hausse configurée)

**Verdict timing :** Favorable — cours au-dessus de MM50 avec RSI dans la zone neutre haussière. Le volume 1.19× confirme une accumulation réelle. Le dépassement de $350 en close du 22/06 reste le signal technique dominant. Cependant, le cours est à −5.8% du 52-week high — zone de profit-taking possible si retour de volatilité.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $137.5B | Yahoo Finance |
| P/E (TTM) | 89.49 | Yahoo Finance |
| Forward P/E | 40.44 | Yahoo Finance |
| EV/EBITDA | 54.00 | Yahoo Finance |
| EV/EBITDA (FMP) | 29.73 | FMP Stable API (FY2025) |
| EV/Revenue | 11.87 | Yahoo Finance |
| P/B | 34.74 | Yahoo Finance |
| P/B (FMP) | 15.69 | FMP Stable API |
| Beta | 2.037 | Yahoo Finance |
| Short Interest | 3.73% | Yahoo Finance |
| Gross Margin (FMP) | 34.36% | FMP Stable API |
| Operating Margin (FMP) | 18.54% | FMP Stable API |
| EBITDA Margin (FMP) | 20.89% | FMP Stable API |
| Net Margin (FMP) | 13.03% | FMP Stable API |
| ROIC (FMP) | 18.55% | FMP Stable API |
| ROCE (FMP) | 24.30% | FMP Stable API |
| Net Debt/EBITDA (FMP) | 0.78× | FMP Stable API |
| Interest Coverage (FMP) | 22.03× | FMP Stable API |
| Current Ratio (FMP) | 1.55× | FMP Stable API |
| FCF Yield (FMP) | 3.06% | FMP Stable API |

**Filtre Qualité (6 critères) :**
| Critère | Évaluation | Commentaire |
|---------|-----------|-------------|
| Revenue CAGR 5 ans ≥ 20% | ✅ Oui | Croissance data centers + IA |
| Profit CAGR 5 ans ≥ 20% | ✅ Oui | Marges en expansion |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.55× |
| FCF positif et croissant 5 ans | ✅ Oui | FCF yield 3.06% |
| Avantage compétitif (moat) | ✅ Oui | Leader refroidissement DC, parts dominantes |
| Industrie en forte croissance (TAM ×5) | ✅ Oui | TAM refroidissement IA en explosion |
| **Score Qualité total** | **6/6** | **Quality Compounder** |

**Observations :**
- Les fondamentaux sont **strictement inchangés**. Quality Compounder 6/6 maintenu.
- La valorisation reste extrême : P/E 89.5, Forward P/E 40.4, P/B 34.7. Le consensus PT $267.57 est **33.8% sous le cours**.
- Les marges et la rentabilité restent solides (ROIC 18.5%, ROCE 24.3%).
- La dette est maîtrisée (net debt/EBITDA 0.78×, interest coverage 22×).

---

## 4. Mise à jour sentiment / options / news

| Signal | Valeur | Commentaire |
|--------|--------|-------------|
| Consensus PT (FMP) | $267.57 (47 analysts) | 33.8% sous cours — divergence haussière extrême |
| Put/Call ratio | 2.77 | Bearish mesuré (73.5% puts) — stable |
| Call OI % | 26.5% | Puts dominent — stable |
| Max pain | $245.0 | Sous le cours de 31.6% — expiration J+3 à surveiller |
| Expiration prochaine | 2026-06-26 | J+3 — risque volatilité expiration |
| Social sentiment | 0 mentions | Aucune mention Reddit détectée |
| Pump detection | Non | — |
| Sector rotation (XLI) | #2 / momentum 7.54 | Industriels outperform — soutien sectoriel légèrement renforcé (+0.27 pts) |
| FX exposure | 45% EUR/CNY | Score FX Impact 0.0 (🟢) — pas d'impact change détecté |
| Events corporate | 0 événement | Aucun catalyseur externe |

**Observations :**
- Le sentiment options est **bearish mesuré stable** (put/call 2.77, 73.5% puts). Le marché options continue de parier à la baisse malgré le rally de +19.5% depuis le low 17/06. Cette divergence contrarienne est à monitorer.
- Aucune news structurante détectée. Le mouvement reste purement technique / macro (soutien sectoriel XLI).
- Le short interest 3.73% est modéré — pas de setup short squeeze pur.
- Le momentum sectoriel XLI s'est légèrement amélioré (7.54/10 vs 7.27/10), renforçant le soutien technique au titre.

---

## 5. Scoring global révisé

**Données du moteur recommandations (Snapshot 10:00 UTC) :**
| Score | Valeur | Δ vs 22/06 21:00 UTC |
|-------|--------|----------------------|
| Score Opportunité | 4.3/10 | Stable |
| Score Catalyseur | 4.3/10 | Stable |
| Score Valorisation | 2.5/10 | Stable |
| Score Momentum | 7.0/10 | Stable |
| Score Global | 42.5/100 | Stable |
| Score Global Ajusté | 47.5/100 | Stable (moteur) |
| Recommandation moteur | **SURVEILLER** | Stable |

**Révision manuelle desk Argus-IA :**

Le moteur est resté SURVEILLER (47.5/100). Les conditions d'upgrade internes définies au close 22/06 restent **partiellement remplies** :

| Condition | Seuil | Statut 23/06 10:00 UTC | Verdict |
|-----------|-------|------------------------|---------|
| Clôture > $350 + volume >1.0× | $350 / 1.0× | **$357.96 / 1.19×** | ✅ **REMPLIE** |
| Catalyseur externe confirmé | Contrat/guidance/M&A | Aucun | 🔴 Non remplie |
| Forward P/E < 35 ou PT révisé | < 35 | 40.44 | 🔴 Non remplie |
| Sector rotation XLI maintenu | Top 3 | **#2 / 7.54** | ✅ **REMPLIE** |

**Verdict desk :** Le snapshot pré-marché du 23/06 n'apporte **aucune donnée nouvelle** par rapport au close 22/06. La thèse reste inchangée : le rally de +7.48% est confirmé sur volume standard (1.19×), le secteur Industriels (XLI) maintient sa position #2 avec un momentum légèrement amélioré (7.54/10), mais la **valorisation extrême** (P/E 89.5, Forward P/E 40.4, consensus 33.8% sous cours) et l'**absence de catalyseur externe** empêchent tout upgrade vers ACHETER. Le risque principal reste le profit-taking en approche du 52-week high ($379.94, −5.8%).

| Score révisé desk | Valeur |
|-------------------|--------|
| Score Opportunité | 4.6/10 (stable — volume confirmé, sectoriel renforcé) |
| Score Catalyseur | 4.3/10 (stable — pas de catalyseur nouveau) |
| Score Valorisation | 2.5/10 (stable — plafond) |
| Score Momentum | 7.0/10 (stable) |
| **Score Global Ajusté desk** | **50.0/100** |
| **Recommandation desk** | **ATTENDRE** (maintenu, nuance haussière stable) |

> ⚠️ **Note importante :** Le moteur est SURVEILLER (47.5) tandis que le desk maintient ATTENDRE (50.0). L'écart reflète la divergence d'interprétation sur le volume confirmé et le momentum sectoriel. Le desk maintient ATTENDRE car le franchissement de $350 avec volume >1.0× est un signal positif, mais la valorisation et l'absence de catalyseur externe justifient de ne pas passer à ACHETER.

---

## 6. Révision des niveaux SL / TP

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix actuel | $357.96 | — |
| Stop-loss | $316.30 | Cours − 2× ATR ($357.96 − $41.66) |
| Take-profit | $420.45 | Cours + 3× ATR ($357.96 + $62.49) |
| Ratio R/R | 1.50 | Engine standard |

**Notes :**
- Le SL $316.30 correspond au support critique $316–$320 + marge ATR.
- Le TP $420.45 est cohérent avec la zone de résistance long terme $400–$420.
- ATR élevé ($20.83) élargit les niveaux — sizing réduit recommandé si position.
- **Alerte :** Si clôture sous $350 avec volume >0.8× → révision SL vers $322.88 (MM50).

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — snapshot pré-marché sans nouvelle séance, données techniques inchangées, léger renforcement sectoriel**

La thèse de fond reste inchangée : VRT est un **Quality Compounder 6/6** bénéficiant du boom de l'IA infrastructure, avec des fondamentaux solides (ROIC 18.5%, net debt/EBITDA 0.78×) mais une **valorisation extrême** qui plafonne le score.

**Ce qui n'a pas changé depuis le close 22/06 21:00 UTC :**
1. **Toutes les données techniques** : cours $357.96, RSI 60.41, ATR $20.83, MM50 $322.88, volume 1.19×.
2. **Toutes les données fondamentales** : P/E 89.5, Forward P/E 40.4, marges, ROIC, dette — inchangés.
3. **Options** : put/call 2.77, call OI 26.5%, max pain $245 — inchangés.
4. **Consensus** : PT $267.57, écart +33.8% — inchangé.
5. **FX exposure** : Score 0.0 (🟢) — inchangé.
6. **Social sentiment** : 0 mentions — inchangé.
7. **Events corporate** : 0 événement — inchangé.
8. **Score Global Ajusté desk** : 50.0/100 (ATTENDRE) — inchangé.

**Ce qui a légèrement changé :**
1. **Sector rotation XLI** : momentum amélioré de 7.27 à **7.54/10** (+0.27 pts) — renforcement du soutien sectoriel.
2. **Prochain earnings** : 36 jours (vs 37 jours) — compte à rebours.

**Scénarios forward (inchangés) :**

| Scénario | Déclencheur | Probabilité | Impact cours |
|----------|-------------|-------------|--------------|
| **Optimiste** | Clôture > $360 avec volume >1.0× + catalyseur externe | 15% | +6–10% vers $380–$395 |
| **Central** | Consolidation $350–$360 en attendant earnings 29/07 | 55% | ±3–5% |
| **Pessimiste** | Retombe sous $350 avec volume >0.8× (profit-taking vers 52W high) | 30% | −8–12% vers $320–$330 |

**Conditions de maintenance du grade ATTENDRE :**
- Cours > $350 en close
- RSI maintenu entre 50 et 65
- Pas de gap down >−3% sans reprise
- XLI reste dans le top 3 sectoriel

**Conditions de downgrade vers SURVEILLER :**
- Clôture sous $350 avec volume >0.8×
- RSI retombe sous 55
- Volume >1.3× sur séance baissière
- XLI sort du top 3

**Conditions d'upgrade vers ACHETER (réduit) :**
- Clôture > $360 avec volume >1.0×
- Catalyseur externe confirmé (contrat, guidance raise, M&A)
- Forward P/E < 35 ou consensus PT révisé à la hausse

**Prochain événement :** Earnings Q2 FY2026 le **2026-07-29** (36 jours) — Est EPS $1.38–$1.59, Rev $3.4B. Ce sera le catalyseur décisif.

---

*Rapport généré par le desk Argus-IA — données source : `data/latest.json` (2026-06-23 10:00 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/geo_risk_latest.json`. [DONNÉES MANQUANTES] : `data/accounting_risk_latest.json` absent, `data/quant_report_latest.json` obsolète (2026-05-17).*
