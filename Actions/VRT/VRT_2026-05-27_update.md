# VRT — Mise à Jour 2026-05-27 (Snapshot 10:00 UTC)

**Date :** 2026-05-27
**Snapshot :** 10:00 UTC (données pre-market / close 2026-05-26)
**Cours :** $323.91 (0.00% vs clôture précédente $323.91)
**Market Cap :** $124.42B (Yahoo)
**Volume :** 6.50M (1.13× moy. 20j : 5.77M)
**Open / High / Low :** $341.06 / $343.31 / $323.26 (données session 26/05)
**52-Week Range :** $104.71 – $379.935
**Prochain Earnings :** 2026-07-29 (63 jours · Est EPS $1.38–$1.59 / Rev ~$3.4B)
**Sector :** Industrials / Electrical Equipment & Parts

---

## Résumé des changements depuis l'analyse précédente (Snapshot 21:00 UTC 2026-05-26)

| Indicateur | Snapshot 21:00 UTC (26/05) | Snapshot 10:00 UTC (27/05) | Δ |
|---|---|---|---|
| Cours | **$323.91** | **$323.91** | ✅ **Inchangé** — stabilité post-rejet |
| RSI 14j | **44.32** | **44.32** | ✅ Inchangé — sous 45 |
| ATR 14j | **$20.34** | **$20.34** | ✅ Inchangé |
| MM 50j | **$304.33** | **$304.33** | ✅ Inchangé |
| Volume | **6.43M** (1.12×) | **6.50M** (1.13×) | 🟡 **+1.1%** — négligeable, toujours au-dessus moyenne |
| Put/Call Ratio | **2.39** | **null** | 🔴 **ANOMALIE JSON** — artefact détecté |
| Max Pain | **$225** | **$145** | 🔴 **ANOMALIE JSON** — $145 = artefact probable |
| Call OI % | **29.5%** | **null** | 🔴 **ANOMALIE JSON** — artefact détecté |
| P/E (Yahoo TTM) | **80.98** | **81.38** | 🟡 +0.40 pt (mise à jour données Yahoo) |
| Forward P/E | **36.65** | **36.65** | ✅ Inchangé |
| EV/EBITDA (Yahoo) | **53.10** | **52.53** | 🟢 −0.57 pt (mise à jour données Yahoo) |
| EV/Revenue | **11.67** | **11.54** | 🟢 −0.13 pt |
| Consensus PT | **$264.35 (46)** | **$264.35 (46)** | ✅ Inchangé — obsolète |
| Score Opportunité | **3.9/10** | **3.9/10** | ✅ Inchangé |
| Score Global | **38.8/100** | **38.8/100** | ✅ Inchangé |
| Score Global Ajusté | **43.8/100** | **43.8/100** | ✅ Inchangé |
| Timing moteur | Favorable | **Favorable** | ✅ Inchangé (divergence notée) |
| Jours jusqu'earnings | **64** | **63** | 🟡 −1 jour |

> **Verdict :** Le snapshot 10:00 UTC du 27 mai confirme une **stabilité totale** des données de cours et techniques vs le close du 26 mai. Le cours reste à $323.91, le RSI à 44.32, l'ATR à $20.34 et la MM50 à $304.33. Le volume est quasi-identique (6.50M vs 6.43M). Une **anomalie options est détectée** dans `data/latest.json` : max pain $145 (vs $225 confirmé), put/call `null`, call OI `null`. Ces valeurs sont traitées comme artefact et les valeurs confirmées du 26 mai (put/call 2.39, max pain $225, call OI 29.5%) sont maintenues. Les fondamentaux Yahoo subissent une légère mise à jour (P/E +0.40 pt à 81.38, EV/EBITDA −0.57 pt à 52.53). La thèse reste **SURVEILLER** avec la même nuance baissière — la consolidation $324–$335 reste sous pression, le support $324 n'a pas été retesté en séance ce matin (pre-market). À surveiller : ouverture du marché US ce jour (14:30 UTC) pour confirmer ou infirmer la tenue du support.

---

## Mise à jour technique

| Indicateur | Valeur JSON 10:00 UTC | Interprétation |
|---|---|---|
| RSI 14j | **44.32** | Sous 45. Zone neutre-baissière. Pas de changement vs hier |
| ATR 14j | **$20.34** | Volatilité élevée stable. ATR relatif 6.28% > seuil 5.0% = trigger ATR_SPIKE actif |
| MM 50j | **$304.33** | Cours +6.4% au-dessus — tendance haussière structurelle intacte mais marge réduite |
| MM 200j | **null** | [DONNÉES MANQUANTES] |
| Open | **$341.06** | Données session 26/05 — gap up +4.1% rejeté |
| High | **$343.31** | Données session 26/05 — résistance intraday massive |
| Low | **$323.26** | Données session 26/05 — test support $324.00 |
| Support clé | **$303.02** (MM50) | Si rupture → correction vers $290–$295 (−10.5%) |
| Support immédiat | **$323.26** (low 26/05) | **Testé hier — non confirmé rompu sur clôture**. À surveiller aujourd'hui |
| Ancien support | **$324.00** (low 22/05) | Testé intraday 26/05 à $323.26. Clôture $323.91 = tenue marginale |
| Résistance clé | **$379.94** (52W high) | Éloigné de +17.3% |
| Résistance intermédiaire | **$335–$340** | Zone de congestion. Rejet massif 26/05 à $343.31 |
| Volume relatif | 1.13× | Au-dessus moyenne 20j. Stable vs hier (1.12×) |

**Options (expiration 2026-05-29 — vendredi, 2 jours)**
| Métrique | Valeur 26/05 21:00 | Valeur JSON 27/05 10:00 | Δ | Commentaire |
|---|---|---|---|---|
| Max Pain | **$225.00** | **$145.00** | 🔴 −$80 | **ANOMALIE JSON** — artefact probable. Maintenir $225 |
| Put/Call Ratio | **2.39** | **null** | 🔴 N/A | **ANOMALIE JSON** — artefact. Maintenir 2.39 |
| Call OI % | 29.5% | null | 🔴 N/A | **ANOMALIE JSON** — artefact. Maintenir 29.5% |

> **Verdict timing : Neutre → Défavorable** (inchangé)
- RSI sous 45 (44.32) = signal technique baissier stable
- Cours au-dessus de MM50 ($304.33) = tendance haussière structurelle intacte mais marge réduite à +6.4%
- **Rejet intraday du 26/05 non infirmé** : le pre-market du 27/05 n'a pas rebondi au-dessus de $335
- Volume stable (1.13×) = distribution potentiellement en cours
- Options bearish extrêmes maintenues (put/call 2.39, 70.5% puts) — risque volatilité à expiration vendredi (2 jours restants)
- **Support $324 tenu sur clôture** ($323.91) mais low $323.26 = quasi-rupture

---

## Mise à jour fondamentale

| Métrique | Source | Valeur JSON 10:00 UTC | Contexte |
|---|---|---|---|
| P/E (Yahoo TTM) | Yahoo | **81.38** | Légère hausse +0.40 pt vs 26/05 (mise à jour données Yahoo, pas effet cours) |
| Forward P/E | Yahoo | **36.65** | Inchangé. Réflète croissance >30% attendue |
| EV/EBITDA (Yahoo TTM) | Yahoo | **52.53** | Légère baisse −0.57 pt vs 26/05 (mise à jour données Yahoo) |
| EV/Revenue | Yahoo | **11.54** | Légère baisse −0.13 pt |
| P/B (Yahoo) | Yahoo | **31.44** | Stable |
| Beta | Yahoo | **2.099** | Très volatile. Sizing réduit obligatoire |
| Short Interest | Yahoo | **3.09%** | Modéré, inchangé |
| FMP ROE | FMP | **33.8%** | Excellente rentabilité — inchangée |
| FMP ROIC | FMP | **18.5%** | Forte création de valeur — inchangée |
| FMP ROCE | FMP | **24.3%** | Excellente utilisation du capital — inchangée |
| FMP Net Debt/EBITDA | FMP | **0.76×** | Très faible levier — inchangé |
| FMP FCF Yield | FMP | **3.06%** | Génération cash positive — inchangée |

> [DONNÉES PARTIELLES] — FMP ratios dérivés basés sur des données FY2025 annual (2025-12-31) avec share count obsolète. Les ratios Yahoo reflètent la capitalisation actuelle $124.42B.
> [DONNÉES MANQUANTES] — `data/accounting_risk_latest.json` absent. Pas de M-Score, Z-Score, F-Score, Sloan Ratio pour VRT.
> [DONNÉES MANQUANTES] — MM200, MACD, IV Rank, earnings whisper, insider trades, job postings, 13F, ETF flows, dark pool, transcripts NLP.
> [ANOMALIE OPTIONS] — `data/latest.json` retourne max pain $145, put/call `null`, call OI `null` pour VRT. Ces valeurs sont incohérentes avec l'historique récent ($225, 2.39, 29.5%) et traitées comme artefact. Les valeurs confirmées du 26/05 sont maintenues.

**Filtre Qualité :** 5–6/6 ✅ **Quality Compounder** — inchangé. Les fondamentaux ne sont pas affectés : marges en expansion, FCF positif (yield 3.06%), moat liquid cooling, TAM en explosion. ROIC 18.5% et ROCE 24.3% confirment la création de valeur. L'absence de mouvement de cours entre les deux snapshots ne change pas la qualité fondamentale.

---

## Mise à jour sentiment / flux / news / agents

| Signal | État | Impact |
|---|---|---|
| News VRT | Aucune news détectée (`data/news_latest.json`) | 🟢 Pas de catalyseur externe négatif |
| Consensus analystes | 46 analysts · PT $264.35 | ⚠️ **OBSOLÈTE** — cours $323.91 = +18.3% au-dessus. 7 analysts actifs le mois dernier |
| Put/Call Ratio | **2.39** (confirmé 26/05) | 🔴 Sentiment options extrêmement bearish. 70.5% puts — maintenu |
| Max Pain | **$225.00** (confirmé 26/05) | Gap 30.5% vs cours — maintenu |
| Call OI % | 29.5% (confirmé 26/05) | Puts dominent massivement — maintenu |
| Social Sentiment | 0 mentions / No data | 🟢 Pas de pump/dump (`data/social_sentiment_latest.json`) |
| Event-Driven | 0 événement corporate (`data/events_latest.json`) | 🟢 Pas de M&A, buyback, guidance change |
| FX Exposure | 45% EUR/CNY · Score 0.0 | 🟢 Aligné — pas d'impact FX (`data/fx_exposure_latest.json`) |
| Sector Rotation | XLI Industrials · Momentum 0.0 | 🔴 Sous-performant. XLI return 20j +1.04% vs XLK Tech +15.3%. VRT dans un secteur faible |
| Geo Risk | Aucun flag pour VRT | 🟢 Pas de risque géopolitique identifié (`data/geo_risk_latest.json`) |
| Quant Report | Insuffisant | ⚪ Pas assez de signaux historiques pour calibration (p-value = 1.0) |
| Upcoming Events | Earnings 2026-07-29 (63j) | 🟡 Prochain catalyseur binaire dans 63 jours |

---

## Scoring global (source : `data/recommandations_latest.json`)

| Axe | Score | Pondération (Unknown) | Pondéré |
|---|---|---|---|
| Catalyseur | **4.3/10** | 35% | 1.51 |
| Valorisation | **2.5/10** | 40% | 1.00 |
| Momentum | **5.5/10** | 25% | 1.38 |
| **Score Opportunité** | | | **3.9/10** |
| **Score Global Composite** | | | **38.8/100** |
| **Score Global Ajusté** | | | **43.8/100** |
| Timing moteur | **Favorable** | | Divergence notée vs interprétation manuelle Défavorable |

> **Règle absolue :** Score Valorisation ≤ 2.5/10 + catalyseur faible = **SURVEILLER STRICT**. Le score Opportunité reste à **3.9/10** (inchangé vs 26/05 21:00 UTC). Verdict **SURVEILLER** maintenu avec nuance baissière.
> **Note timing :** Le moteur recalcule Favorable en raison de la position au-dessus de MM50, mais l'interprétation manuelle reste **Neutre → Défavorable** compte tenu du rejet intraday du 26/05 (−5.2% depuis l'open), du volume de distribution (1.13×) et du test du support $324.

---

## Révision des niveaux SL/TP (source : moteur recommandation)

| | Valeur | Note |
|---|---|---|
| **Prix cible (consensus)** | $264.35 | Toujours obsolète — à ignorer jusqu'à révisions significatives |
| **Prix cible technique (optimiste)** | $380 (+17.4%) / $400 (+23.5%) | Résistance gap / rerating massif |
| **Zone d'entrée attractive** | **$314–$324** | Support $324 tenu sur clôture. Zone d'accumulation si tenue confirmée aujourd'hui |
| **Stop-Loss (engine 2×ATR)** | **$283.23** (−12.6%) | Sous MM50. Conforme engine |
| **Take-Profit (engine 3×ATR)** | **$384.93** (+18.8%) | Calcul engine : cours + 3×ATR |
| **Ratio R/R (engine)** | **1.5** | Acceptable, timing Défavorable |
| **Sizing recommandé** | Réduit (beta 2.10) | Inchangé. Volatilité extrême |
| **Horizon** | 1–3 mois | Earnings 29 juillet = catalyseur binaire |

> **Révision :** Inchangée. Le SL engine ($283.23) reste éloigné (−12.6%) compte tenu du beta 2.10. Pour un positionnement swing, le SL engine reste valide. Une approche plus conservatrice reste un SL sous le low du 26/05 ($323.26) soit ~$318 (−1.8%) pour un trade intraday/swing, mais cela ne respecte pas la méthode ATR.

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — STABILITÉ POST-REJET, FONDAMENTAUX INTACTS, PRESSION TECHNIQUE BAISSIÈRE MAINTENUE**

- **Fondamentaux :** ✅ Confirmés — Quality Compounder 5–6/6, ROIC 18.5%, ROCE 24.3%, FCF yield 3.06%, net debt/EBITDA 0.76×. Marges en expansion, moat intact. Légère mise à jour Yahoo (P/E +0.40 pt, EV/EBITDA −0.57 pt) sans impact sur la thèse.
- **Valorisation :** 🟡 **Stable** — Forward P/E 36.7, P/E TTM 81.4. Toujours extrême mais inchangée en essence.
- **Catalyseur :** 🟡 Stable — Score C 4.3/10. Pas de nouveau catalyseur. Earnings 29 juillet reste le prochain catalyseur binaire (63 jours).
- **Momentum :** 🟡 **Stable** — Score M 5.5/10 (inchangé). Pas de nouvelle séance pour évaluer un rebond ou une poursuite de la baisse.
- **Options :** 🔴 **Stable** — Put/Call 2.39 (70.5% puts). Max pain $225 confirmé. **Anomalie JSON détectée** ($145, null) — valeurs confirmées 26/05 maintenues. Risque de volatilité à expiration vendredi inchangé (2 jours restants).
- **Volume :** 🟡 **Stable** — 6.50M (1.13× moyenne). Stable vs hier, toujours au-dessus de la moyenne 20j.
- **Timing :** 🟡 **Neutre → Défavorable** (inchangé) — RSI sous 45, rejet intraday 26/05 non infirmé, options bearish extrêmes.
- **Sector Rotation :** 🔴 **Stable** — XLI Industrials momentum 0.0, sous-performant vs XLK (10.0).
- **Niveaux techniques :** 🟡 **Pression maintenue** — Support $324.00 **tenu sur clôture** ($323.91) mais low $323.26 = test quasi-rompu. La consolidation $324–$335 reste sous pression. Prochain support structurel MM50 ($304.33) = −6.1%.
- **Données Pipeline :** ⚠️ Anomalie options JSON — valeurs confirmées 26/05 maintenues. 23/26 tickers OK, VRT sans erreur [CRITICAL].

**Recommandation : SURVEILLER** (Score Global Ajusté 43.8/100)
- **Pas de position longue significative à $323.91.** Attendre la session US du 27/05 pour confirmer la tenue du support $324.
- **Si le cours clôture sous $324 aujourd'hui** avec volume → risque élevé de test MM50 ($304.33) = −6.1% supplémentaires.
- **Si rebond et consolidation au-dessus de $335** → possible squeeze technique post-expiration vendredi, mais le momentum reste dégradé.
- **Urgence :** Expiration options vendredi 29 mai avec max pain $225 (gap 30.5%) et put/call 2.39 — risque de volatilité élevée. 70.5% puts = potentiel de short squeeze si catalyst inattendu, mais le rejet du 26/05 affaiblit cette probabilité.
- Earnings 29 juillet (63 jours) reste binaire : valider la croissance ou correction vers MM50 ($304).

---

## Alertes actives

- 🔴 **Rejet intraday massif (26/05)** — Open $341.06 → Low $323.26 (−5.2%). Pattern bearish engulfing/shooting star. Non infirmé ce matin
- 🔴 **Support $324 testé et tenu marginalement** — Low $323.26 = rupture intraday non confirmée sur clôture. À confirmer aujourd'hui
- 🔴 **Volume distribution** — 6.50M (1.13× moyenne). Stable au-dessus moyenne 20j. Pas d'accumulation
- 🔴 **Put/Call 2.39** — Sentiment options extrêmement bearish. 70.5% puts vs 29.5% calls. Max pain $225 = gap 30.5%
- 🔴 **Valorisation extrême** — P/E 81.4, EV/EBITDA 52.5. Aucune marge d'erreur
- 🔴 **Sector rotation défavorable** — XLI Industrials momentum 0.0, sous-performant vs XLK/XLE
- 🔴 **Options expiration 29 mai** — Risque volatilité élevée à 2 jours. 70.5% puts = potentiel squeeze affaibli par rejet
- 🟡 **RSI 44.32** — Sous 45. Approche zone survente (40). Espace de baisse technique vers 40 ouvert
- 🟡 **Consensus obsolète** — PT $264 vs cours $323.91 (+18.3%). Révisions attendues
- 🟡 **Correction cumulée** — Cumul −14.8% depuis le 52W high ($379.94). Low $323.26 nouveau plus bas récent
- 🟡 **Données comptables manquantes** — `data/accounting_risk_latest.json` absent
- 🟡 **Anomalie options JSON** — Max pain $145 / put/call null dans `data/latest.json`. Valeurs confirmées 26/05 ($225, 2.39) maintenues
- 🟡 **Divergence timing moteur** — Recalculé Favorable vs Neutre/Défavorable manuel. À surveiller si confirmation par flux

---

## Notes et limitations

- [SNAPSHOT PRE-MARKET] — Le snapshot 10:00 UTC du 27 mai reflète le pre-market US (ouverture 14:30 UTC). Les données de cours ($323.91) sont identiques au close du 26 mai. La session US du 27 mai n'a pas encore eu lieu au moment du snapshot.
- [ANOMALIE OPTIONS JSON] — `data/latest.json` retourne max pain $145.00, put/call `null`, call OI `null` pour VRT. Ces valeurs sont incohérentes avec l'historique récent (max pain $225 depuis le 18/05, put/call 2.39). L'anomalie est traitée comme artefact et les valeurs confirmées du 26 mai sont maintenues. L'historique VRT montre des anomalies options récurrentes (18/05 : put/call 3.08, 19/05 : put/call 2.62, 20/05 : anomalie 0.0/$190/100%, 25/05 : put/call 2.59, 26/05 : put/call 2.39). La stabilité relative de ces valeurs (2.39–3.08) vs les artefacts extrêmes confirme la méthode de maintien des valeurs confirmées.
- [DONNÉES PARTIELLES] — FMP ratios dérivés obsolètes (FY2025, share count dépassé). Préférer Yahoo pour capitalisation et P/E TTM.
- [DONNÉES MANQUANTES] — `data/accounting_risk_latest.json` absent. Pas de M-Score, Z-Score, F-Score, Sloan Ratio pour VRT.
- [DONNÉES MANQUANTES] — MM200, MACD, IV Rank, earnings whisper, insider trades, job postings, 13F, ETF flows, dark pool, transcripts NLP.
- [SIGNAUX NON SIGNIFICATIFS] — Quant report : pas assez de signaux historiques pour calibration (p-value = 1.0).
- [SECTOR ROTATION] — XLI Industrials sous-performant (momentum 0.0, return 20j +1.04% — amélioration mécanique due au rebase post-Memorial Day mais toujours faible vs XLK 10.0).
- [TIMING MOTEUR] — Divergence Favorable vs Neutre/Défavorable manuel. Pas d'impact opérationnel en l'absence de flux de marché confirmés.

---

*Analyse générée le 2026-05-27 avec snapshot 10:00 UTC. Stabilité confirmée post-rejet intraday du 26/05. Anomalie options JSON détectée et traitée. Thèse confirmée avec pression baissière maintenue. Ne pas modifier — créer un nouvel `_update.md` pour toute révision.*
