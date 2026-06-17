# SPCX — Mise à jour post-pipeline 2026-06-17 (snapshot 10h UTC)

**Date :** 2026-06-17
**Type :** Mise à jour post-pipeline — snapshot 10h UTC
**Analyse précédente :** snapshot 17h UTC 2026-06-16

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (17h UTC 16/06) | Actuel (10h UTC 17/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$216.94** | **$201.80** | 🔴 Faux prix −7.0% |
| Previous close | $160.95 | **$192.50** | 🔴 Révisé — aligné sur close 21h 16/06 |
| Change % | +34.78% | **+4.83%** | 🟡 Faux mouvement réduit mais persistant |
| Open / High / Low | $200.42 / $225.64 / $200.00 | **$200.51 / $225.64 / $195.13** | 🔴 OHLC fictif stable, low élargi |
| Volume | 224,216,788 | **322,149,300** | 🔴 +43.6% — volume fictif en expansion |
| Volume vs moy. 20j | 0.60× (371.7M) | **0.88× (365.9M)** | 🟡 Approche fausse moyenne |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high | $225.64 | **$225.64** | = Stable (faux high artificiel) |
| 52w low | $149.34 | **$149.34** | = Stable (faux low incompatible ETF) |
| Market cap (fundamentals) | $2,841.76B | **$2,658.55B** | 🔴 −6.4% du faux market cap |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = Stable |
| Forward P/E | −2,412.0 | **−2,242.2** | 🟡 Moins aberrant, toujours impossible |
| Price-to-book (fundamentals) | 36.45 | **33.88** | 🟡 Mécanique sur faux cours |
| Shares outstanding | 7,488,063,555 | **7,571,396,888** | 🔴 +1.1% quantité fictive |
| Options max_pain | null | **25.0** | 🔴 **Nouvelle anomalie options** |
| Recommandation agent | **ÉVITER** | **ÉVITER** | = **Maintien** |
| Score Opportunité | 2.0/10 | **2.0/10** | = |
| Score Catalyseur | 5.5/10 | **5.5/10** | = |
| Score Valorisation | 2.0/10 | **2.0/10** | = — proche seuil disqualification |
| Score Momentum | 5.5/10 | **5.5/10** | = |
| **Score Global** | 20.0/100 | **20.0/100** | = 🔴 **ÉVITER maintenu** |
| **Score Global Ajusté** | 20.0/100 | **20.0/100** | = |
| Timing | Neutre | **Neutre** | = |

**Verdict :** Vingt-neuvième snapshot consécutif sans données fiables. Le conflit de symbole FMP persiste avec un **nouveau prix fictif $201.80** (+4.83% vs previous close révisé $192.50), accompagné d'un faux market cap de **$2.66T** et d'un forward P/E de **−2,242**. Le **volume fictif a gonflé de +43.6%** à 322.1M unités. L'Agent Recommandation maintient le verdict **ÉVITER 20.0/100** (Score Opportunité 2.0/10). Une **nouvelle anomalie options** apparaît : `max_pain` passe de `null` à `25.0` (aberrant pour un ETF SPAC). Le secteur reste `Industrials` / `Aerospace & Defense`. La divergence interne P/B (fundamentals 33.88 vs fmp_ratios 11.40) persiste. Le validation report du jour émet par ailleurs un `[WARNING] SPCX: volume is 0` qui **contradict directement** le champ `volume: 322149300` de `latest.json` — signal d'une dégradation transversale de la qualité data.

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : prix fictif $201.80**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$201.80** | 🔴 Faux prix FMP — entité étrangère |
| Previous close | $192.50 | 🔴 Révisé (close 21h 16/06) |
| Open | $200.51 | 🔴 Faux OHLC |
| High | $225.64 | 🔴 Correspond au faux 52w high artificiel |
| Low | $195.13 | 🔴 Faux OHLC, bande élargie |
| Change % | **+4.83%** | 🔴 Totalement artificiel |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **322.1M / 365.9M** | 🔴 Volume fictif +43.6% vs 17h 16/06 |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $201.80 reste ~9× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. L'apparition d'un `max_pain` à 25.0 (vs null hier) est une nouvelle mutation de l'anomalie options.

**Verdict timing :** Défavorable → **Non-actionnable**. Vingt-neuf snapshots consécutifs sans RSI, ATR, ni MM50 fiables. Le conflit de symbole FMP est **chronique** : prix oscillant entre $135.00 (08/06), $160.95 (15/06), $192.50–$216.94 (16/06), et désormais $201.80 (17/06), toujours pour la même entité incorrecte.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes mutantes mais toujours fausses :**

| Métrique | Valeur actuelle | Valeur historique (17h 16/06) | Commentaire |
|----------|----------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **−2,242.2** | −2,412.0 | 🟡 Légèrement moins aberrant, toujours impossible |
| Market cap (fundamentals) | **$2,658.55B** | $2,841.76B | 🔴 −6.4% du faux market cap |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable |
| Price-to-book (fundamentals) | **33.88** | 36.45 | 🟡 Mécanique sur faux cours réduit |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,571,396,888** | 7,488,063,555 | 🔴 +1.1% quantité fictive |
| Shares float | **2,919,745,600** | 2,919,745,600 | = Stable |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$177.50** (stable vs 17h 16/06)
- `num_analysts`: **2** (stable)
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.39 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 33.88 (fundamentals) — **divergence interne persistante**
- `price_to_sales`: 25.22 (stable)
- `price_to_fcf`: −33.75 (stable)
- `enterprise_value_multiple`: **369.23** (stable)
- `gross_margin`: 49.39% (stable)
- `operating_margin`: −13.86% (stable)
- `net_margin`: −26.44% (stable)

**FMP Key Metrics (stables mais faux) :**
- `market_cap`: $1,585.46B (stable)
- `enterprise_value`: $1,583.61B
- `ev_to_sales`: 84.80
- `ev_to_ebitda`: 369.23
- `net_debt_to_ebitda`: −0.43
- `return_on_equity`: −11.95%

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.66T) et fmp_key_metrics ($1.59T) persiste. Le P/B fundamentals a reculé de 36.45 à 33.88 suite au faux −7.0% de cours. L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. Le `[WARNING]` du validation report (`volume is 0`) est une erreur interne du pipeline qui contradict le `volume: 322149300` de `latest.json` — signe d'une dégradation de la fiabilité des contrôles qualité eux-mêmes.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-17.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-17.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🔴 Anomalie mutante | `max_pain` = **25.0** (was null), `put_call_ratio` = null, `call_oi_pct` = null — nouvelle mutation |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $177.50, 2 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-17.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-17.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-17 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer.

**Alerte validation report (artefact) :** `validation_report.txt` émet `[WARNING] SPCX: volume is 0 — market closed or delisted?` alors que `data/latest.json` indique clairement `volume: 322149300`. Cette incohérence interne indique une défaillance du module de validation sur ce ticker.

**Alerte social sentiment (artefact) :** `data/social_sentiment_latest.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL stable :** `data/sector_rotation_2026-06-17.json` signale `NEUTRAL` avec 11/11 secteurs OK. XLF (Financials) : return_20d +5.04%, rs_20d +3.46%, momentum_score 5.32. XLK (Technology) domine avec momentum_score 10.0. Le signal sectoriel est lisible mais n'impacte pas SPCX (absent du ranking sectoriel).

---

## Scoring global (agents pipeline 2026-06-17, snapshot 10h UTC)

| Axe | Score | Changement vs 17h 16/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **5.5/10** | = | Modéré — absence de catalyseur réel |
| Score Valorisation | **2.0/10** | = | 🔴 **Proche seuil disqualification (≤ 2/10)** — artefact mécanique |
| Score Momentum | **5.5/10** | = | Placeholder mécanique, non fondé sur données de marché réelles |
| **Score Opportunité** | **2.0/10** | = | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **20.0/100** | = | 🔴 **ÉVITER maintenu** |
| **Score Global Ajusté** | **20.0/100** | = | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL stable mais sans impact direct sur SPCX)

**Règle de disqualification :** 🔴 **Score Valorisation = 2.0/10** — exactement sur le seuil de disqualification (≤ 2/10). Le Score Opportunité est également à **2.0/10**. L'Agent Recommandation maintient l'exclusion du rapport.

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
| Prix entrée suggéré | **N/A** | Cours fictif $201.80 — aucune donnée de marché réelle |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable. Le faux cours $201.80 est ~9× supérieur à ces niveaux.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🔴 Thèse **INVALIDÉE** — **maintien ÉVITER** (Score Global 20.0/100), vingt-neuvième snapshot consécutif sans données fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif) |
| RSI | ❌ Non disponible |
| Volume | 🔴 322.1M unités — volume fictif en expansion (+43.6%) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🔴 **20.0/100** → **ÉVITER** (fourchette < 35) |
| Source données | 🔴 **Conflit de symbole chronique** : prix oscillant $135→$216→$201, sector Industrials/Aerospace & Defense, market cap $2.66T, forward P/E −2,242 |
| Signal sectoriel | 🟡 **NEUTRAL stable** — XLF momentum_score 5.32, 11/11 secteurs OK |
| Stabilité inter-snapshot | 🔴 Prix mutants : $216.94 (17h 16/06) → $201.80 (10h 17/06) — volatilité fictive |
| Seuil de vigilance | 🔴 Score Valorisation 2.0/10 = **seuil de disqualification atteint** — Score Opportunité également à 2.0/10 |
| Qualité data pipeline | 🔴 `[WARNING] volume is 0` dans validation report contradict `volume: 322149300` dans latest.json |

- **Invalidation :** La recommandation **ÉVITER** reste un artefact mécanique — le fondamental (absence totale de données fiables) est identique. Le scoring est **inchangé à 20.0/100**. Aucune donnée réelle n'a changé. Le setup reste totalement non-actionnable.
- **Nuances :** Le snapshot 10h UTC du 17/06 montre une **mutation du conflit de symbole dans sa forme volatile** : prix fictif $201.80 (+4.83% vs previous $192.50), avec faux OHLC étendu ($195.13–$225.64), faux market cap $2.66T (−6.4%), et **nouvelle anomalie options** (`max_pain` = 25.0). Le volume fictif a gonflé de 224M à 322M (+43.6%). Le module sector rotation est stable (NEUTRAL, 11/11 OK). L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 17/06 est un artefact récurrent et ignoré. Le validation report contient une **incohérence critique** (`volume is 0`) qui undermine la confiance dans les contrôles qualité.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 50/100 relancerait le setup en ATTENDRE. Tant que le prix oscille entre des valeurs fictives volatiles ($135–$225), aucune action n'est justifiable.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ÉVITER** (artefact). Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER** fondé sur données réelles. Si le faux prix continue de muter (valeurs fictives volatiles) → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ÉVITER** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur vingt-neuf snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère en mutation (prix fictif $201.80, sector Industrials/Aerospace & Defense, market cap $2.66T). Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`) et volume > 0 avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **322,149,300** | 🔴 Extrême anomalie | Faux volume +43.6% vs 17h 16/06, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 Anomalie mutante | — | `max_pain` = 25.0 (was null), `put_call_ratio` null, `call_oi_pct` null — nouvelle mutation |
| Révisions consensus | 🔴 Anomalie | — | PT $177.50 et 2 analysts — non applicable à un ETF, artefact FMP |
| Faux +4.83% | +4.83% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | `[WARNING] volume is 0` | 🔴 Incohérence interne | Contradict `latest.json` (322M) — défaillance qualité data |

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
| Validation report cohérent avec latest.json | 1j | Confiance pipeline restaurée | Méfiance sur tous les contrôles qualité |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 17h UTC 2026-06-16
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ÉVITER (artefact mécanique)
- Recommandation révisée : **ÉVITER** (artefact mécanique — fondamentalement non-actionnable)
- Raison principale : Snapshot 10h UTC 17/06 : conflit de symbole FMP chronique — prix fictif $201.80 (+4.83% vs previous close $192.50), faux OHLC $195.13–$225.64, faux market cap $2.66T (−6.4% vs 16/06), forward P/E −2,242, sector Industrials/Aerospace & Defense, volume fictif 322.1M (+43.6%). Scoring agent inchangé ÉVITER 20.0/100 : Score Opportunité 2.0/10, Score Valorisation 2.0/10 (seuil disqualification atteint), Score Catalyseur 5.5/10. Nouvelle anomalie options (`max_pain` 25.0). Sector rotation stable (NEUTRAL, 11/11 secteurs OK, XLF momentum 5.32). Aucun catalyseur ni news. Faux earnings FMP du 17/06 ignoré. Alerte social EXTREME_BEARISH ignorée (artefact). Validation report incohérent (`volume is 0` vs 322M dans latest.json).
- Thèse : 🔴 **Invalidée** — maintien ÉVITER (Score Global 20.0/100), conflit de symbole chronique, données totalement non fiables, dégradation data quality pipeline détectée
