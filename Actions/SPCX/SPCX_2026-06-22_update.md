# SPCX — Mise à jour post-pipeline 2026-06-22 (snapshot 10h UTC)

**Date :** 2026-06-22
**Type :** Mise à jour post-pipeline — snapshot 10h UTC
**Analyse précédente :** snapshot 13h UTC 2026-06-17

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (13h UTC 17/06) | Actuel (10h UTC 22/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$201.80** | **$185.00** | 🔴 Faux prix −8.3% vs précédent |
| Previous close | $192.50 | **$191.82** | 🟡 Révisé −0.35% |
| Change % | +4.83% | **−3.56%** | 🔴 Inversion mécanique |
| Open / High / Low | $200.51 / $225.64 / $195.13 | **$188.39 / $190.00 / $172.11** | 🔴 OHLC fictif réduit, bande élargie |
| Volume | 322,149,300 | **272,126,800** | 🟡 −15.5% — volume fictif en retrait |
| Volume vs moy. 20j | 0.88× (365.9M) | **0.94× (288.9M)** | 🟡 Fausse moyenne révisée à la baisse |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high | $225.64 | **$225.64** | = Stable (faux high artificiel) |
| 52w low | $149.34 | **$149.34** | = Stable (faux low incompatible ETF) |
| Market cap (fundamentals) | $2,658.55B | **$2,437.22B** | 🔴 −8.3% du faux market cap |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = Stable |
| Forward P/E | −2,242.2 | **711.54** | 🔴 **Nouvelle mutation fondamentale** |
| Price-to-book (fundamentals) | 33.88 | **31.06** | 🟡 Mécanique sur faux cours réduit |
| Shares outstanding | 7,571,396,888 | **7,571,396,888** | = Stable |
| Shares float | 2,919,745,600 | **281,190,750** | 🔴 **Mutation majeure −90.4%** |
| Options max_pain | 210.0 | **162.5** | 🔴 **Nouvelle mutation options** |
| Options put/call ratio | 0.66 | **null** | 🔴 Disparition mécanique |
| Options call OI % | 60.3% | **null** | 🔴 Disparition mécanique |
| FMP consensus PT | $177.50 (2 analysts) | **$251.50 (4 analysts)** | 🔴 **Mutation consensus majeure** |
| Recommandation agent | **ÉVITER** | **ATTENDRE** | 🔴 **Reclassement mécanique majeur** |
| Score Opportunité | 2.0/10 | **5.7/10** | 🔴 **+3.7 pt mécanique** |
| Score Catalyseur | 5.5/10 | **8.0/10** | 🔴 **+2.5 pt** |
| Score Valorisation | 2.0/10 | **4.5/10** | 🔴 **+2.5 pt** |
| Score Momentum | 5.5/10 | **4.5/10** | 🟡 −1.0 pt |
| **Score Global** | 20.0/100 | **57.2/100** | 🔴 **+37.2 pt — ÉVITER → ATTENDRE** |
| **Score Global Ajusté** | 20.0/100 | **57.2/100** | 🔴 **+37.2 pt** |
| Timing | Neutre | **Neutre** | = |
| Validation report | Aucun warning | **Aucun warning** | = Cohérence pipeline maintenue |

**Verdict :** Trente-quatrième snapshot consécutif sans données techniques fiables. Le conflit de symbole FMP persiste avec un **nouveau prix fictif $185.00** (−3.56% vs previous close $191.82), accompagné d'un faux market cap de **$2.44T** et d'un forward P/E muté à **711.54** (was −2,242). Le **volume fictif a reculé de −15.5%** à 272.1M unités. L'**Agent Recommandation effectue un reclassement mécanique majeur : ÉVITER 20.0/100 → ATTENDRE 57.2/100**, porté par un bond du Score Catalyseur (+2.5 pt à 8.0/10) et du Score Valorisation (+2.5 pt à 4.5/10). Cependant, le secteur reste `Industrials` / `Aerospace & Defense`, les métriques techniques (RSI, ATR, MM50) restent toutes nulles, et le prix reste ~8× supérieur aux derniers niveaux connus réels de l'ETF SPAC (~$22). Une **mutation majeure du float** (−90.4% à 281.2M) et du **consensus FMP** (PT $177.50 → $251.50, 2 → 4 analysts) confirment que FMP continue de mapper SPCX sur une entité étrangère en mutation. Les données options ont également muté : `max_pain` 210.0 → 162.5, avec disparition du `put_call_ratio` et du `call_oi_pct`. Le module sector rotation reste stable (NEUTRAL, 11/11 secteurs OK). Aucune news, social, ni catalyseur fondamental.

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : prix fictif $185.00**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$185.00** | 🔴 Faux prix FMP — entité étrangère |
| Previous close | $191.82 | 🔴 Révisé (close dernière séance) |
| Open | $188.39 | 🔴 Faux OHLC |
| High | $190.00 | 🔴 Faux OHLC, bande rétrécie vs 17/06 |
| Low | $172.11 | 🔴 Faux OHLC, bande élargie en dessous |
| Change % | **−3.56%** | 🔴 Totalement artificiel |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **272.1M / 288.9M** | 🔴 Volume fictif −15.5% vs 17/06 |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $185.00 reste ~8× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. La **mutation du float** de 2.92B à 281.2M (−90.4%) est une nouvelle preuve que les données FMP proviennent d'une entité incorrecte en mutation. Les options (`max_pain` 162.5) restent celles de cette entité étrangère.

**Verdict timing :** Neutre → **Non-actionnable**. Trente-quatre snapshots consécutifs sans RSI, ATR, ni MM50 fiables. Le conflit de symbole FMP est **chronique** : prix oscillant entre $135.00 (08/06), $160.95 (15/06), $192.50–$216.94 (16/06), $201.80 (17/06), et désormais $185.00 (22/06), toujours pour la même entité incorrecte.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes mutantes mais toujours fausses :**

| Métrique | Valeur actuelle | Valeur historique (13h 17/06) | Commentaire |
|----------|----------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **711.54** | −2,242.2 | 🔴 **Nouvelle mutation — toujours impossible** |
| Market cap (fundamentals) | **$2,437.22B** | $2,658.55B | 🔴 −8.3% du faux market cap |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable — faux |
| Price-to-book (fundamentals) | **31.06** | 33.88 | 🟡 Mécanique sur faux cours réduit |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,571,396,888** | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | 2,919,745,600 | 🔴 **Mutation majeure −90.4%** |

**FMP Consensus (mutant et faux) :**
- `price_target_avg`: **$251.50** (was $177.50) — 🔴 **+41.7%**
- `num_analysts`: **4** (was 2) — 🔴 **+2 analysts**
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.24 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 31.06 (fundamentals) — **divergence interne persistante**
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

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.44T) et fmp_key_metrics ($1.59T) persiste. Le P/B fundamentals a reculé de 33.88 à 31.06 suite au faux −8.3% de cours. L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La **mutation du float** (−90.4%) et du **consensus analystes** (PT +41.7%, 2 → 4 analysts) sont de nouvelles preuves que le mapping symbole est instable.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-22.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-22.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🔴 Anomalie mutante | `max_pain` = **162.5** (was 210.0), `put_call_ratio` = null (was 0.66), `call_oi_pct` = null (was 60.3%) — nouvelle mutation |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $251.50, 4 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-22.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality — résolution maintenue :** Le `[WARNING] SPCX: volume is 0` reste absent du validation report 2026-06-22. La cohérence pipeline entre validation report et `latest.json` est maintenue. Cependant, le volume reste factice pour un ETF SPAC.

**Alerte social sentiment (artefact) :** `data/social_sentiment_latest.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL stable :** `data/sector_rotation_2026-06-22.json` signale `NEUTRAL` avec 11/11 secteurs OK. XLK (Technology) domine avec momentum_score 10.0. XLF (Financials) : return_20d +3.70%, rs_20d +2.70%, momentum_score 4.25. Le signal sectoriel est lisible mais n'impacte pas SPCX (absent du ranking sectoriel).

**Anomalie upcoming events (artefact) :** `data/upcoming_events_2026-06-22.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-22 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer.

---

## Scoring global (agents pipeline 2026-06-22, snapshot 10h UTC)

| Axe | Score | Changement vs 13h 17/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **8.0/10** | +2.5 pt | 🔴 **Saut mécanique** — absence de catalyseur réel |
| Score Valorisation | **4.5/10** | +2.5 pt | 🔴 **Proche seuil disqualification (≤ 2/10) dépassé** — artefact mécanique |
| Score Momentum | **4.5/10** | −1.0 pt | Placeholder mécanique, non fondé sur données de marché réelles |
| **Score Opportunité** | **5.7/10** | +3.7 pt | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **57.2/100** | +37.2 pt | 🔴 **Reclassement mécanique ÉVITER → ATTENDRE** |
| **Score Global Ajusté** | **57.2/100** | +37.2 pt | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel — faux earnings FMP ignoré)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL stable mais sans impact direct sur SPCX)

**Règle de disqualification :** 🟡 **Score Valorisation = 4.5/10** — le seuil de disqualification (≤ 2/10) est désormais dépassé mécaniquement. Le Score Opportunité est à **5.7/10**. L'Agent Recommandation reclasse le ticker en **ATTENDRE**.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | **ATTENDRE** | — | ✅ **SPCX = 57.2** |
| 35–49 | SURVEILLER | — | — |
| < 35 | ÉVITER | — | — |

> **Note institutionnelle :** Le reclassement ÉVITER → ATTENDRE est **purement mécanique** et non fondé sur une amélioration de la qualité data. Les métriques techniques restent toutes nulles, le secteur reste incorrect, et le prix reste fictif. Ce saut de +37.2 pt en 5 jours sans nouvelle donnée fiable est un artefact du scoring agent face à des données mutantes (notamment la mutation du consensus FMP et du forward P/E). Le setup reste **non-actionnable** en pratique.

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours fictif $185.00 — aucune donnée de marché réelle |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable. Le faux cours $185.00 est ~8× supérieur à ces niveaux.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **MODIFIÉE MÉCANIQUEMENT** — **reclassement agent ÉVITER → ATTENDRE** (Score Global 20.0 → 57.2/100), mais **qualité data toujours dégradée**. Trente-quatrième snapshot consécutif sans données techniques fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif) |
| RSI | ❌ Non disponible |
| Volume | 🔴 272.1M unités — volume fictif en retrait (−15.5%) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🟡 **57.2/100** → **ATTENDRE** (fourchette 50–59) — reclassement mécanique |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $185.00, sector Industrials/Aerospace & Defense, market cap $2.44T, forward P/E 711.54 |
| Signal sectoriel | 🟡 **NEUTRAL stable** — XLK momentum_score 10.0, XLF momentum_score 4.25, 11/11 secteurs OK |
| Stabilité inter-snapshot | 🔴 Prix mutants : $201.80 (17/06) → $185.00 (22/06) — volatilité fictive −8.3% |
| Seuil de vigilance | 🟡 Score Valorisation 4.5/10 — seuil de disqualification dépassé mécaniquement |
| Qualité data pipeline | 🟢 Aucun warning — cohérence validation report / `latest.json` maintenue |
| Options | 🔴 Mutation : max_pain 210.0 → **162.5**, put/call et call OI disparus |
| Consensus FMP | 🔴 Mutation majeure : PT $177.50 → **$251.50** (+41.7%), 2 → **4 analysts** |
| Float FMP | 🔴 Mutation majeure : 2.92B → **281.2M** (−90.4%) |

- **Modification :** L'Agent Recommandation effectue un **reclassement mécanique majeur** : ÉVITER 20.0/100 → ATTENDRE 57.2/100. Ce saut de +37.2 pt est porté par une hausse du Score Catalyseur (+2.5 pt à 8.0/10) et du Score Valorisation (+2.5 pt à 4.5/10), sans fondamental nouveau ni amélioration de la qualité data. Le Score Momentum recule légèrement (−1.0 pt à 4.5/10). Le timing reste Neutre.
- **Nuances :** Le snapshot 10h UTC du 22/06 montre une **nouvelle mutation du conflit de symbole** : prix fictif $185.00 (−3.56% vs previous close $191.82), avec faux OHLC étendu ($172.11–$190.00), faux market cap $2.44T (−8.3% vs 17/06), et **forward P/E muté** de −2,242.2 à 711.54 (toujours impossible). Le volume fictif a reculé de 322M à 272M (−15.5%). Le **float FMP** a chuté de 90.4% (2.92B → 281.2M), et le **consensus analystes** a muté (PT +41.7%, 2 → 4 analysts). Les données options ont également muté (`max_pain` 210.0 → 162.5, disparition du put/call ratio et du call OI). Le module sector rotation est stable (NEUTRAL, 11/11 OK). L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 22/06 est un artefact récurrent et ignoré. Le validation report reste cohérent (aucun warning).
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation fiable. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHETER (Réduit). Tant que le prix oscille entre des valeurs fictives volatiles ($135–$225), aucune action n'est justifiable en pratique.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** (artefact mécanique) ou retour en **ÉVITER** si le scoring re-chute. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER** fondé sur données réelles. Si le faux prix reprend sa volatilité mutante ou si les métriques FMP continuent de diverger → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable malgré le reclassement agent)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur trente-quatre snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère en mutation (prix fictif $185.00, sector Industrials/Aerospace & Defense, market cap $2.44T, forward P/E 711.54, float mutant 281.2M, consensus mutant $251.50). Le reclassement mécanique en ATTENDRE 57.2/100 n'est pas fondé sur une amélioration tangible de la qualité data. Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et métriques stables avant toute réévaluation opérationnelle.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **272,126,800** | 🔴 Extrême anomalie | Faux volume −15.5% vs 17/06, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 Anomalie mutante | — | `max_pain` = 162.5 (was 210.0), `put_call_ratio` null, `call_oi_pct` null — nouvelle mutation |
| Révisions consensus | 🔴 Anomalie majeure | — | PT $251.50 (+41.7%) et 4 analysts — non applicable à un ETF, artefact FMP mutant |
| Float FMP | 281,190,750 | 🔴 Mutation −90.4% | Preuve de mapping symbole instable |
| Faux −3.56% | −3.56% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | Aucun warning | 🟢 Cohérent | Cohérence maintenue entre validation report et `latest.json` |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP corrigées (prix ~$22, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup revalidable en ATTENDRE / ACHETER | Maintien en ATTENDRE / reclassement ÉVITER |
| Volume > 1 000 unités confirmé | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER fondé sur données réelles |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ATTENDRE | — |
| XLF momentum_score > 6.0 + données fiables | 5–10j | Contexte sectoriel favorable | — |
| FMP corrige le mapping symbole (sector = Financial Services, market cap < $1B, float stable) | Variable | Rétablissement data quality | Maintien ATTENDRE / ÉVITER |
| Options stables et cohérentes (max_pain proche du vrai cours ~$22) | 1–3j | Confiance data restaurée | Si max_pain continue de muter → méfiance |
| Consensus FMP stable (PT et nb analysts constants) | 1–3j | Mapping symbole stabilisé | Si consensus continue de muter → méfiance |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 13h UTC 2026-06-17
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ÉVITER (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — reclassement agent non fondé sur amélioration data quality)
- Raison principale : Snapshot 10h UTC 22/06 : conflit de symbole FMP chronique persistant — prix fictif $185.00 (−3.56% vs previous close $191.82), faux OHLC $172.11–$190.00, faux market cap $2.44T (−8.3% vs 17/06), forward P/E muté 711.54 (was −2,242), sector Industrials/Aerospace & Defense, volume fictif 272.1M (−15.5%). Mutation majeure du float FMP (2.92B → 281.2M, −90.4%) et du consensus (PT $177.50 → $251.50, 2 → 4 analysts). Scoring agent reclassement mécanique ÉVITER 20.0/100 → ATTENDRE 57.2/100 : Score Opportunité 5.7/10 (C:8.0 V:4.5 M:4.5), Score Valorisation 4.5/10 (seuil disqualification dépassé mécaniquement), Score Catalyseur 8.0/10. Options mutantes (max_pain 162.5, was 210.0). Sector rotation stable (NEUTRAL, 11/11 secteurs OK, XLK momentum 10.0, XLF momentum 4.25). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 22/06 ignoré. Validation report cohérent (aucun warning).
- Thèse : 🟡 **Modifiée mécaniquement** — reclassement agent ÉVITER → ATTENDRE (Score Global 57.2/100), mais conflit de symbole chronique persistant, données totalement non fiables, mutations fondamentales majeures (float, consensus, forward P/E), setup non-actionnable en pratique
