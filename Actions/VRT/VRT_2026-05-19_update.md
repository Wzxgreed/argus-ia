# VRT — Mise à Jour 2026-05-19

**Date :** 2026-05-19
**Snapshot :** 13:00 UTC (post-opening — données options corrigées)
**Cours :** $339.73 (inchangé vs clôture 2026-05-18)
**Market Cap :** $130.49B (Yahoo)
**Volume :** 8.07M (1.36× moy. 20j : 5.93M)
**52-Week Range :** $101.00 – $379.94
**Prochain Earnings :** 2026-07-29 (71 jours · Est EPS $1.39–$1.59 / Rev ~$3.4B)
**Sector :** Industrials / Electrical Equipment & Parts

---

## Résumé des changements depuis l'analyse précédente (2026-05-19 10:00 UTC)

| Indicateur | Snapshot 10:00 UTC (pre-market) | Snapshot 13:00 UTC (post-opening) | Δ |
|---|---|---|---|
| Cours | **$339.73** | **$339.73** | ✅ Inchangé |
| RSI 14j | **61.76** | **61.76** | ✅ Inchangé |
| ATR 14j | **$18.70** | **$18.70** | ✅ Inchangé |
| MM 50j | **$298.60** | **$298.60** | ✅ Inchangé |
| Volume relatif | **1.36×** | **1.36×** | ✅ Inchangé |
| Put/Call Ratio | **30.0** | **2.62** | 🟢 Corrigé — artefact pre-market résolu |
| Max Pain | **$185.00** | **$215.00** | 🟢 Corrigé — retour au niveau du 18 mai |
| Call OI % | **3.2%** | **27.7%** | 🟢 Corrigé — retour au niveau du 18 mai |
| P/E (Yahoo TTM) | **85.57** | **85.57** | ✅ Inchangé |
| Forward P/E | **38.59** | **38.59** | ✅ Inchangé |
| Score Opportunité | **3.9/10** | **3.9/10** | ✅ Inchangé |
| Score Global | **38.8/100** | **38.8/100** | ✅ Inchangé |
| Consensus PT | **$257.49 (43 analysts)** | **$257.49 (43 analysts)** | ✅ Inchangé |

> **Verdict :** Le snapshot 13:00 UTC confirme l'intégrité des données de prix du 18 mai et corrige l'artefact pre-market sur la chaîne options (put/call 30.0 → 2.62, max pain $185 → $215). Aucun écart sur les 11 métriques fondamentales et techniques. Le marché US n'a pas généré de nouveau prix pour VRT à ce stade — le cours reste figé à la clôture du 18 mai dans le snapshot JSON.

---

## Mise à jour technique

| Indicateur | Valeur JSON 13:00 UTC | Interprétation |
|---|---|---|
| RSI 14j | **61.76** | Sortie de surachat confirmée. Espace technique de consolidation inchangé |
| ATR 14j | **$18.70** | Volatilité élevée stable (beta 2.10). Expansion post-gap confirmée |
| MM 50j | **$298.60** | Cours +13.8% au-dessus — tendance haussière intacte malgré la correction |
| MM 200j | **null** | [DONNÉES MANQUANTES] |
| Support clé | $298.60 (MM50) | Si rupture → correction significative vers $280–$290 |
| Support secondaire | **$330.72** (low du 18 mai) | Zone de rejet intraday testée et tenue — première zone d'intérêt |
| Résistance clé | **$379.94** (52W high) | Ancien sommet, +11.8% au-dessus du cours |
| Résistance intermédiaire | **$370.94** (close 17 mai) | Gap à combler si rebond |
| Volume relatif | 1.36× | Distribution institutionnelle probable sur le gap −8.41% du 18 mai |

**Options (expiration 2026-05-22 — vendredi)**
| Métrique | Valeur | Commentaire |
|---|---|---|
| Max Pain | **$215.00** | 🟢 Corrigé depuis $185 (artefact). Gap 36.7% vs cours $339.73 — hedging institutionnel probable |
| Put/Call Ratio | **2.62** | 🟢 Corrigé depuis 30.0 (artefact). Reste très élevé : 72.3% puts vs 27.7% calls |
| Call OI % | 27.7% | 🟢 Corrigé depuis 3.2% (artefact) |

> 🔴 **Alerte options persistante** — Put/Call 2.62 confirme une nervosité extrême autour de l'expiration vendredi 22 mai. La correction du ratio depuis 30.0 ne change pas la direction : le positionnement options reste massivement bearish. Risque de volatilité élevée jusqu'à vendredi.

**Verdict timing : Neutre à Défavorable**
- Pas de nouvelle donnée de prix depuis le 18 mai (cours figé à $339.73)
- La zone d'intérêt $330–$340 reste le premier support observable
- Put/call 2.62 (confirmé) = hedging institutionnel massif pré-expiration vendredi
- Volume supérieur à la moyenne sur gap baissier = distribution plus probable que simple profit-taking

---

## Mise à jour fondamentale

| Métrique | Source | Valeur JSON 13:00 UTC | Contexte |
|---|---|---|---|
| P/E (Yahoo TTM) | Yahoo | **85.57** | Inchangé. Prime de croissance IA massive |
| Forward P/E | Yahoo | **38.59** | Réflète croissance >30% attendue. Inchangé |
| EV/EBITDA (Yahoo TTM) | Yahoo | **55.08** | Premium massif, inchangé |
| EV/Revenue | Yahoo | **12.11** | Premium IA intact, inchangé |
| P/B (Yahoo) | Yahoo | **32.97** | Valorisation potentiel, inchangé |
| Beta | Yahoo | **2.099** | Très volatile. Sizing réduit obligatoire |
| Short Interest | Yahoo | **3.09%** | Modéré, inchangé |
| FCF Yield (FMP) | FMP | **3.06%** | Génération cash confirmée |
| ROIC (FMP) | FMP | **18.55%** | Création de valeur confirmée |
| Net Debt/EBITDA (FMP) | FMP | **0.76×** | Levier modéré, confortable |
| Interest Coverage (FMP) | FMP | **22.0×** | Très solide |
| Gross Margin (FMP) | FMP | **34.36%** | Bonne |
| Operating Margin (FMP) | FMP | **18.54%** | Excellente conversion |

> [DONNÉES PARTIELLES] — `data/validation_report.txt` signale une violation de schema sur `fmp_key_metrics.market_cap` pour VRT (type `number` au lieu de `integer`). Ce warning n'affecte pas les données utilisées (market cap Yahoo $130.49B préféré). FMP market cap $61.84B et ratios dérivés basés sur FY2025 annual (2025-12-31) avec share count obsolète. Préférer Yahoo pour capitalisation et P/E TTM.

> [DONNÉES MANQUANTES] — `data/accounting_risk_latest.json` absent ce jour. Pas de scan M-Score, Z-Score, F-Score, Sloan Ratio disponible pour VRT.

**Filtre Qualité :** 5–6/6 ✅ **Quality Compounder** — inchangé. La correction de −8.41% du 18 mai ne modifie aucun fondamental : ROIC 18.55%, marges en expansion, FCF positif, moat liquid cooling, TAM en explosion.

---

## Mise à jour sentiment / flux / news / agents

| Signal | État | Impact |
|---|---|---|
| News VRT | Aucune news détectée (`data/news_latest.json`) | 🟢 Pas de catalyseur externe aujourd'hui |
| Consensus analystes | 43 analysts · PT $257.49 | ⚠️ OBSOLÈTE — cours $339.73 reste +31.8% au-dessus du consensus. 10 analysts actifs le mois dernier, 12 le trimestre dernier |
| Put/Call Ratio | **2.62** (vs 30.0 artefact, vs 3.08 le 18 mai) | 🔴 Bearish extrême confirmé — hedging institutionnel massif. La correction de −8.41% est cohérente avec ce positionnement |
| Max Pain | **$215.00** (vs $185 artefact) | 🟢 Corrigé. Gap 36.7% vs cours = niveau de hedging institutionnel |
| Social Sentiment | 0 mentions / No data | 🟢 Pas de pump/dump détecté (`data/social_sentiment_latest.json`) |
| Event-Driven | 0 événement corporate | 🟢 Pas de M&A, buyback, guidance change (`data/events_latest.json`) |
| FX Exposure | 45% EUR/CNY · Score 0.0 | 🟢 Aligné — pas d'impact FX aujourd'hui (`data/fx_exposure_latest.json`) |
| Sector Rotation | XLI Industrials · Momentum 0.0 | 🔴 Sous-performant vs XLK Tech (10.0) et XLE Energy (9.94). VRT corrige dans un secteur déjà faible (`data/sector_rotation_latest.json`) |
| Geo Risk | Aucun flag | 🟢 Pas de risque géopolitique identifié (`data/geo_risk_latest.json`) |
| Quant Report | Insuffisant | ⚪ Pas assez de signaux historiques pour calibration (p-value = 1.0) |
| Upcoming Events | Earnings 2026-07-29 (71j) | 🟡 Prochain catalyseur binaire dans 71 jours |

---

## Scoring global (source : `data/recommandations_latest.json`)

| Axe | Score | Pondération (Stagflation) | Pondéré |
|---|---|---|---|
| Catalyseur | **4.3/10** | 35% | 1.51 |
| Valorisation | **2.5/10** | 40% | 1.00 |
| Momentum | **5.5/10** | 25% | 1.38 |
| **Score Opportunité** | | | **3.9/10** |
| **Score Global Composite** | | | **38.8/100** |
| **Score Global Ajusté** | | | **43.8/100** |

> Règle absolue : Score Valorisation ≤ 2.5/10 + catalyseur faible = **SURVEILLER STRICT**. Pas de changement de scoring depuis le 18 mai.

---

## Révision des niveaux SL/TP

| | Valeur | Note |
|---|---|---|
| **Prix cible (consensus)** | $257.49 | OBSOLÈTE — à ignorer jusqu'à révisions |
| **Prix cible technique (optimiste)** | $380 (+11.8%) / $400 (+17.7%) | Résistance gap / rerating massif |
| **Zone d'entrée attractive** | **$330–$340** | Low du 18 mai $330.72 testé et tenu. Si retest → opportunité d'accumulation pour les believers de la thèse IA |
| **Stop-Loss (engine 2×ATR)** | **$302.33** (−11.0%) | Sous MM50. Conforme engine |
| **Take-Profit (engine 3×ATR)** | **$395.83** (+16.5%) | Calcul engine : cours + 3×ATR |
| **Ratio R/R (engine)** | **1.5** | Acceptable mais timing défavorable |
| **Sizing recommandé** | Réduit (beta 2.10) | Inchangé. Volatilité extrême |
| **Horizon** | 1–3 mois | Earnings 29 juillet = catalyseur binaire |

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — CORRECTION ARTEFACT OPTIONS RÉSOLUE**

- **Fondamentaux :** ✅ Confirmés — Quality Compounder 5–6/6, ROIC 18.55%, FCF positif, moat intact. La baisse ne change rien à la thèse fondamentale.
- **Valorisation :** 🟡 **Stable** — Forward P/E 38.6, P/E TTM 85.6. Toujours extrême mais inchangé.
- **Catalyseur :** 🔴 Stable — Score C 4.3/10. Pas de nouveau catalyseur. Earnings 29 juillet reste le prochain catalyseur binaire.
- **Momentum :** 🔴 Stable — Score M 5.5/10. Gap −8.41% du 18 mai intact. Pas de rebond ni de continuation observée.
- **Options :** 🔴 **Alerte persistante (corrigée)** — Put/Call 2.62 / max pain $215 confirmés post-opening. Le ratio extrême de 30.0 était un artefact pre-market. Néanmoins, 2.62 reste très bearish (72.3% puts). Risque de volatilité élevée jusqu'à expiration vendredi 22 mai.
- **Timing :** 🟡 **Stable** — Zone $330–$340 reste la première zone d'intérêt technique. Pas de changement de timing.
- **Sector Rotation :** 🔴 **Stable** — XLI Industrials momentum 0.0, sous-performant vs XLK (10.0) et XLE (9.94).
- **Données Pipeline :** ✅ **Intégrité confirmée** — 11/11 métriques clés identiques entre snapshot 18 mai et snapshot 19 mai 13:00 UTC. Le seul changement est la correction de l'artefact options pre-market.
- **Validation :** ⚠️ `validation_report.txt` signale une violation JSON schema sur `fmp_key_metrics.market_cap` pour VRT. Warning mineur sans impact sur l'analyse.

**Recommandation : SURVEILLER** (Score Global 43.8/100)
- Pas de position longue significative à $339.73. Attendre consolidation ou retest $330–$333
- Si le cours repasse sous $330 avec volume → risque de test MM50 ($298.60) = −12.1% supplémentaires
- Si rebond sur $330–$340 avec volume faible → possible squeeze technique post-expiration vendredi
- Earnings 29 juillet (71 jours) reste binaire : valider la croissance ou correction vers MM50 ($299)

---

## Alertes actives

- 🔴 **Put/Call 2.62** — Sentiment options extrêmement bearish (confirmé post-opening). Max pain $215 = gap 36.7%
- 🔴 **Valorisation extrême** — P/E 85.6, EV/EBITDA 55.1. Aucune marge d'erreur
- 🔴 **Sector rotation défavorable** — XLI Industrials momentum 0.0, sous-performant vs XLK/XLE
- 🟡 **RSI 61.76** — Sortie de surachat, mais toujours élevé. Espace de baisse technique
- 🟡 **Consensus obsolète** — PT $257 vs cours $339.73 (+31.8%). Révisions attendues
- 🟡 **Correction en cours** — Gap −8.41% du 18 mai. Low $330.72 testé et tenu
- 🟡 **Volume élevé** — 1.36× moyenne 20j sur gap baissier = distribution possible
- 🟡 **Données comptables manquantes** — `data/accounting_risk_latest.json` absent ce jour

---

## Notes et limitations

- [DONNÉES PARTIELLES] — `validation_report.txt` : violation schema JSON sur `prices -> VRT -> fmp_key_metrics -> market_cap` (type `number` au lieu de `integer`). Warning mineur, préférer Yahoo market cap $130.49B
- [DONNÉES PARTIELLES] — FMP market cap $61.84B et ratios dérivés obsolètes (FY2025, share count dépassé). Préférer Yahoo pour capitalisation et P/E TTM
- [DONNÉES MANQUANTES] — `data/accounting_risk_latest.json` absent ce jour. Pas de M-Score, Z-Score, F-Score, Sloan Ratio pour VRT
- [DONNÉES MANQUANTES] — MM200, MACD, IV Rank, earnings whisper, insider trades, job postings, 13F, ETF flows, dark pool, transcripts NLP
- [SIGNAUX NON SIGNIFICATIFS] — Quant report : pas assez de signaux historiques pour calibration (p-value = 1.0)
- [SECTOR ROTATION] — XLI Industrials sous-performant (momentum 0.0), risque relatif accru pour VRT
- [PIPELINE STABLE] — Snapshot 13:00 UTC confirmé identique au snapshot 18 mai sur les prix. Artefact options pre-market (30.0 / $185) corrigé à 2.62 / $215.

---

*Analyse générée le 2026-05-19 avec snapshot 13:00 UTC. Ne pas modifier — créer un nouvel `_update.md` pour toute révision.*
