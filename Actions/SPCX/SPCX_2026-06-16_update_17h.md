# SPCX — Mise à jour post-pipeline 2026-06-16 (snapshot 17h UTC)

**Date :** 2026-06-16
**Type :** Mise à jour post-pipeline — snapshot 17h UTC
**Analyse précédente :** snapshot 13h UTC 2026-06-16

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (13h UTC 16/06) | Actuel (17h UTC 16/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **NaN** | **$216.94** | 🔴 **Nouveau prix fictif** |
| Previous close | $160.95 | **$160.95** | = |
| Change % | NaN | **+34.78%** | 🔴 Artefact mécanique |
| Open / High / Low | NaN / NaN / NaN | $200.42 / $225.64 / $200.00 | 🔴 OHLC fictif fourni |
| Volume | 243,783,175 | **224,216,788** | 🟡 −8.0% — toujours astronomique |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high | N/A | **$225.64** | 🔴 Nouveau — correspond au high du jour |
| 52w low | N/A | **$149.34** | 🔴 Nouveau — incompatible ETF SPAC |
| Market cap (fundamentals) | $2,519.99B | **$2,841.76B** | 🔴 +13.2% du faux market cap |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = Stable |
| Forward P/E | −2,138.89 | **−2,412.0** | 🔴 Plus aberrant |
| Recommandation agent | **SURVEILLER** | **ÉVITER** | 🔴 **Reclassement majeur** |
| Score Opportunité | 4.7/10 | **2.0/10** | 🔴 −2.7 pts |
| Score Catalyseur | 6.5/10 | **5.5/10** | 🟡 −1.0 pt |
| Score Valorisation | 3.0/10 | **2.0/10** | 🔴 −1.0 pt — proche seuil disqualification |
| Score Momentum | 5.0/10 | **5.5/10** | 🟢 +0.5 pt (artefact mécanique) |
| **Score Global** | 47.2/100 | **20.0/100** | 🔴 **−27.2 pts** |
| **Score Global Ajusté** | 47.2/100 | **20.0/100** | 🔴 **−27.2 pts** |
| Timing | Neutre | **Neutre** | = |

**Verdict :** Vingt-huitième snapshot consécutif sans données fiables, mais avec une **mutation majeure du conflit de symbole** : après deux snapshots de prix NaN (10h et 13h UTC), FMP a renvoyé un **nouveau cours fictif $216.94** (+34.78% vs previous close $160.95), accompagné d'un faux market cap de **$2.84T** et d'un forward P/E de **−2,412**. L'Agent Recommandation a **basculé en ÉVITER 20.0/100** (Score Opportunité 2.0/10, Score Valorisation 2.0/10) — le ticker est désormais à la limite de la règle de disqualification (score individuel ≤ 2/10 → action exclue). Cette hausse de 34.78% est purement algorithmique et non corrélée à l'ETF Tuttle SPAC & New Issue.

---

## Mise à jour technique

**🔴 [CRITICAL] — Aggravation du conflit de symbole : nouveau prix fictif $216.94**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$216.94** | 🔴 Faux prix FMP — entité étrangère |
| Previous close | $160.95 | 🔴 Stable depuis 10h — base du faux +34.78% |
| Open | $200.42 | 🔴 Faux OHLC |
| High | $225.64 | 🔴 Correspond au nouveau 52w high artificiel |
| Low | $200.00 | 🔴 Faux OHLC |
| Change % | **+34.78%** | 🔴 Totalement artificiel |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **224.2M / 371.7M** | 🔴 Volume fictif −8% vs 13h, toujours astronomique |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $216.94 est 10× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité totalement étrangère (probablement un large-cap Industrials/Aerospace). Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC.

**Verdict timing :** Défavorable → **Non-actionnable**. Vingt-huit snapshots consécutifs sans RSI, ATR, ni MM50 fiables. Le conflit de symbole a muté : après une phase NaN, FMP fournit désormais un prix fictif volatil (+34.78%) pour une entité incorrecte.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes mutantes mais toujours fausses :**

| Métrique | Valeur actuelle | Valeur historique (13h 16/06) | Commentaire |
|----------|----------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **−2,412.0** | −2,138.89 | 🔴 Aggravation — plus aberrant |
| Market cap (fundamentals) | **$2,841.76B** | $2,519.99B | 🔴 +13.2% du faux market cap |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable |
| Price-to-book (fundamentals) | **36.45** | 32.32 | 🔴 Faux — mécanique sur faux cours |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,488,063,555** | — | 🔴 Nouveau — quantité fictive |
| Shares float | **2,919,745,600** | — | 🔴 Nouveau — quantité fictue |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$177.50** (stable vs 13h)
- `num_analysts`: **2** (stable vs 13h)
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.39 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 36.45 (fundamentals) — **divergence interne aggravée**
- `price_to_sales`: 25.22 (stable)
- `price_to_fcf`: −33.75 (stable)
- `enterprise_value_multiple`: **369.23** (stable)
- `gross_margin`: 49.39% (stable)
- `operating_margin`: −13.86% (stable)
- `net_margin`: −26.44% (stable)

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.84T) et fmp_key_metrics ($1.59T) s'est aggravée. Le P/B fundamentals est passé de 32.32 à 36.45 suite au faux +34.78% de cours. L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-16.json` : 0 item pour tous les tickers (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-16.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🔴 Anomalie persistante | `max_pain` = null, `put_call_ratio` = null, `call_oi_pct` = null — perte totale du flux options |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $177.50, 2 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-16.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-16.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-16 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer.

**Alerte social sentiment (artefact) :** `data/social_sentiment_latest.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL rétabli partiellement :** `data/sector_rotation_2026-06-16.json` signale `NEUTRAL` avec 11/11 secteurs OK (vs NaN massifs à 13h). XLF (Financials) : return_20d +6.43%, rs_20d +4.64%, momentum_score 6.68. XLK (Technology) domine avec momentum_score 10.0. Le signal sectoriel est désormais lisible mais n'impacte pas SPCX (absent du ranking sectoriel).

---

## Scoring global (agents pipeline 2026-06-16, snapshot 17h UTC)

| Axe | Score | Changement vs 13h 16/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **5.5/10** | −1.0 | Modéré — absence de catalyseur réel, dégradation mécanique |
| Score Valorisation | **2.0/10** | −1.0 | 🔴 **Proche seuil disqualification (≤ 2/10)** — artefact mécanique |
| Score Momentum | **5.5/10** | +0.5 | Placeholder mécanique, non fondé sur données de marché réelles |
| **Score Opportunité** | **2.0/10** | −2.7 | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **20.0/100** | −27.2 | 🔴 **Bascule mécanique ÉVITER** |
| **Score Global Ajusté** | **20.0/100** | −27.2 | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL rétabli mais sans impact direct sur SPCX)

**Règle de disqualification :** 🔴 **Score Valorisation = 2.0/10** — exactement sur le seuil de disqualification (≤ 2/10). Le Score Opportunité est également à **2.0/10**. Si l'Agent Recommandation applique strictement la règle, SPCX devrait être **exclue du rapport**.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | ATTENDRE | — | — |
| 35–49 | SURVEILLER | — | — |
| < 35 | **ÉVITER** | — | ✅ **SPCX = 20.0** |

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours fictif $216.94 — aucune donnée de marché réelle |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable. Le faux cours $216.94 est 10× supérieur à ces niveaux.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🔴 Thèse **INVALIDÉE** — **reclassement mécanique SURVEILLER → ÉVITER** (Score Global 20.0/100), vingt-huitième snapshot consécutif sans données fiables, avec une **aggravation structurelle majeure** du conflit de symbole FMP.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif) |
| RSI | ❌ Non disponible |
| Volume | 🔴 224M unités — volume fictif, toujours astronomique |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🔴 **20.0/100** → **ÉVITER** (fourchette < 35) |
| Source données | 🔴 **Conflit de symbole mutagène** : après NaN (10h/13h), FMP renvoie un nouveau prix fictif $216.94 (+34.78%) avec market cap $2.84T, forward P/E −2,412, sector Industrials/Aerospace & Defense |
| Signal sectoriel | 🟡 **NEUTRAL rétabli** — XLF momentum_score 6.68, pas de NaN massifs |
| Stabilité inter-snapshot | 🔴 Prix mutants : $192.50 (21h 15/06) → NaN (10h/13h 16/06) → $216.94 (17h 16/06) |
| Seuil de vigilance | 🔴 Score Valorisation 2.0/10 = **seuil de disqualification atteint** — Score Opportunité également à 2.0/10 |

- **Invalidation :** La recommandation **ÉVITER** est un artefact mécanique — le fondamental (absence totale de données fiables) est identique, mais la **mutation du conflit de symbole** (passage de NaN à un prix fictif +34.78%) a fait basculer l'algorithme de scoring en dessous du seuil de tolérance. Le Score Global est passé de 47.2 à 20.0/100 (−27.2 pts) en un seul snapshot, sans qu'aucune donnée réelle n'ait changé. Le setup reste totalement non-actionnable.
- **Nuances :** Le snapshot 17h UTC du 16/06 montre une **réactivation du conflit de symbole dans sa forme la plus volatile** : après deux snapshots de prix NaN, FMP fournit un prix fictif $216.94 avec un faux +34.78%, un faux 52w range ($149.34 – $225.64) et un faux market cap $2.84T. La divergence interne P/B (11.40 vs 36.45) s'est aggravée. Le module sector rotation est rétabli (11/11 secteurs OK, signal NEUTRAL). L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 16/06 est un artefact récurrent et ignoré.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 50/100 relancerait le setup en ATTENDRE. Tant que le prix oscille entre NaN et des valeurs fictives volatiles, aucune action n'est justifiable.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ÉVITER** (artefact). Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER** fondé sur données réelles. Si le faux prix continue de muter (NaN ↔ valeurs fictives volatiles) → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ÉVITER** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur vingt-huit snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère en mutation (prix NaN ↔ fictif $216.94, sector Industrials/Aerospace & Defense, market cap $2.84T). Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`) et volume > 0 avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **224,216,788** | 🔴 Extrême anomalie | Faux volume −8% vs 13h, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 Anomalie persistante | — | `max_pain` null, `put_call_ratio` null, `call_oi_pct` null — perte totale du flux options |
| Révisions consensus | 🔴 Anomalie | — | PT $177.50 et 2 analysts — non applicable à un ETF, artefact FMP |
| Faux +34.78% | +34.78% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP corrigées (prix ~$22, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup revalidable en ATTENDRE | Maintien en ÉVITER / reclassement ÉVITER |
| Volume > 1 000 unités confirmé | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER fondé sur données réelles |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ATTENDRE | — |
| XLF momentum_score > 6.0 + données fiables | 5–10j | Contexte sectoriel favorable | — |
| FMP corrige le mapping symbole (sector = Financial Services, market cap < $1B) | Variable | Rétablissement data quality | Maintien ÉVITER |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 13h UTC 2026-06-16
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : SURVEILLER (artefact mécanique)
- Recommandation révisée : **ÉVITER** (artefact mécanique — fondamentalement non-actionnable)
- Raison principale : Snapshot 17h UTC 16/06 : mutation majeure du conflit de symbole FMP — après NaN (10h/13h), nouveau prix fictif $216.94 (+34.78%) avec faux market cap $2.84T (+13.2%), forward P/E −2,412, sector Industrials/Aerospace & Defense, 52w range fictif $149.34–$225.64, volume fictif 224M. Scoring agent basculé ÉVITER 20.0/100 (−27.2 pts vs 13h) : Score Opportunité 2.0/10, Score Valorisation 2.0/10 (seuil disqualification atteint), Score Catalyseur 5.5/10. Sector rotation rétabli (NEUTRAL, 11/11 secteurs OK). Aucun catalyseur ni news. Faux earnings FMP du 16/06 ignoré. Alerte social EXTREME_BEARISH ignorée (artefact).
- Thèse : 🔴 **Invalidée** — reclassement mécanique SURVEILLER → ÉVITER (Score Global 20.0/100), conflit de symbole mutagène, données totalement non fiables
