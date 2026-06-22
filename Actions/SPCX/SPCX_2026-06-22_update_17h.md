# SPCX — Mise à jour post-pipeline 2026-06-22 (snapshot 17h UTC)

**Date :** 2026-06-22
**Type :** Mise à jour post-pipeline — snapshot 17h UTC
**Analyse précédente :** snapshot 13h UTC 2026-06-22

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (13h UTC 22/06) | Actuel (17h UTC 22/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$185.00** | **$165.845** | 🔴 **Faux prix −10.35%** |
| Previous close | $191.82 | **$185.00** | 🟡 Révisé mécaniquement (close 13h) |
| Change % | −3.56% | **−10.35%** | 🔴 Nouvelle chute fictine majeure |
| Open / High / Low | $188.39 / $190.00 / $172.11 | **$176.042 / $176.69 / $165.00** | 🔴 OHLC réduit, bande rétrécie |
| Volume | 272,126,800 | **88,013,714** | 🔴 **Faux volume collapse −67.7%** |
| Volume vs moy. 20j | 0.94× (288.9M) | **0.34× (255.5M)** | 🔴 Fausse moyenne révisée, ratio effondré |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high / low | $225.64 / $149.34 | $225.64 / $149.34 | = |
| Market cap (fundamentals) | $2,437.22B | **$2,184.94B** | 🔴 −10.35% du faux market cap (mécanique) |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = Stable |
| Forward P/E | 711.54 | **843.29** | 🔴 **Nouvelle mutation fondamentale +18.5%** |
| Price-to-book (fundamentals) | 31.06 | **27.85** | 🟡 Mécanique sur faux cours réduit |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = Stable |
| Shares float | 281,190,750 | 281,190,750 | 🟢 **Stabilisation confirmée** |
| Options max_pain | 180.0 | **180.0** | 🟢 **Première stabilité options depuis le 17/06** |
| Options put/call ratio | 0.83 | **0.83** | 🟢 **Stabilisation confirmée** |
| Options call OI % | 54.8% | **54.8%** | 🟢 **Stabilisation confirmée** |
| FMP consensus PT | $251.50 (4 analysts) | **$251.50 (4 analysts)** | 🟢 **Stabilisation confirmée** |
| Recommandation agent | **ATTENDRE** | **ATTENDRE** | = |
| Score Opportunité | 5.7/10 | **5.6/10** | 🟡 −0.1 pt |
| Score Catalyseur | 8.0/10 | **8.0/10** | = Stable |
| Score Valorisation | 4.5/10 | **4.5/10** | = Stable |
| Score Momentum | 4.5/10 | **4.0/10** | 🔴 **−0.5 pt** |
| **Score Global** | 57.2/100 | **56.0/100** | 🟡 **−1.2 pt** |
| **Score Global Ajusté** | 57.2/100 | **56.0/100** | 🟡 **−1.2 pt** |
| Timing | Neutre | **Neutre** | = |
| Validation report | Aucun warning SPCX | **Aucun warning SPCX** | = Cohérence maintenue |

**Verdict :** Trente-sixième snapshot consécutif sans données techniques fiables. Le conflit de symbole FMP persiste avec un **nouveau prix fictif $165.845** (−10.35% vs previous close $185.00), accompagné d'un faux market cap de **$2.18T** et d'un **forward P/E muté à 843.29** (was 711.54). Le **volume fictif s'est effondré de −67.7%** à 88.0M unités. L'**Agent Recommandation ajuste légèrement le ticker à la baisse : ATTENDRE 57.2/100 → ATTENDRE 56.0/100**, porté par une baisse du Score Momentum (−0.5 pt à 4.0/10). Le secteur reste `Industrials` / `Aerospace & Defense`, les métriques techniques (RSI, ATR, MM50) restent toutes nulles, et le prix reste ~7.5× supérieur aux derniers niveaux connus réels de l'ETF SPAC (~$22). Cependant, pour la **première fois depuis le 17/06**, les données options se sont **stabilisées** (max_pain 180.0, put/call 0.83, call OI 54.8% — tous inchangés vs 13h), et le float FMP (281.2M) ainsi que le consensus analystes (PT $251.50, 4 analysts) sont également stables. Le module sector rotation reste NEUTRAL avec 11/11 secteurs OK. Aucune news, social, ni catalyseur fondamental. Le gap −10.35% a déclenché un `PRICE_GAP` dans `agents/detect_major_events` (DRAFT_refresh.md généré) — **ce trigger est purement mécanique et lié au faux prix**.

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : nouveau prix fictif $165.845**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$165.845** | 🔴 Faux prix FMP — entité étrangère |
| Previous close | $185.00 | 🔴 Révisé (close 13h UTC) |
| Open | $176.042 | 🔴 Faux OHLC |
| High | $176.69 | 🔴 Faux OHLC, bande rétrécie vs 13h |
| Low | $165.00 | 🔴 Faux OHLC, bande rétrécie en dessous |
| Change % | **−10.35%** | 🔴 Totalement artificiel |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **88.0M / 255.5M** | 🔴 Volume fictif collapse −67.7% vs 13h |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $165.845 reste ~7.5× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. La **stabilité des options** (max_pain 180.0, put/call 0.83, call OI 54.8%) est la première pause dans la mutation depuis le 17/06, mais reste celle de l'entité étrangère. Les métriques techniques (RSI, ATR, MM50) restent toutes nulles sur ce snapshot 17h UTC, confirmant l'absence totale de flux Yahoo.

**Verdict timing :** Neutre → **Non-actionnable**. Trente-six snapshots consécutifs sans RSI, ATR, ni MM50 fiables. Le conflit de symbole FMP est **chronique** : prix oscillant entre $135.00 (08/06), $160.95 (15/06), $192.50–$216.94 (16/06), $201.80 (17/06), $185.00 (22/06 10h/13h), et désormais $165.845 (22/06 17h), toujours pour la même entité incorrecte. Le **gap −10.35% est fictif** et a déclenché un `PRICE_GAP` dans le module detect_major_events — à ignorer en l'absence de données fiables.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes mutantes mais toujours fausses :**

| Métrique | Valeur actuelle (17h) | Valeur historique (13h 22/06) | Commentaire |
|----------|----------------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **843.29** | 711.54 | 🔴 **Nouvelle mutation +18.5% — toujours impossible** |
| Market cap (fundamentals) | **$2,184.94B** | $2,437.22B | 🔴 −10.35% du faux market cap (mécanique) |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable — faux |
| Price-to-book (fundamentals) | **27.85** | 31.06 | 🟡 Mécanique sur faux cours réduit |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,571,396,888** | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | 281,190,750 | 🟢 **Stabilisation confirmée** |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$251.50** (was $251.50) — 🟢 Stable
- `num_analysts`: **4** (was 4) — 🟢 Stable
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.24 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 27.85 (fundamentals) — **divergence interne persistante**
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

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.18T) et fmp_key_metrics ($1.59T) persiste. Le P/B fundamentals a reculé de 31.06 à 27.85 suite au faux −10.35% de cours. Le **forward P/E a muté de 711.54 à 843.29** (+18.5%), nouvelle preuve d'instabilité du mapping symbole. L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La **stabilisation du float** (281.2M) et du **consensus analystes** ($251.50, 4 analysts) entre 13h et 17h est une pause dans la mutation, mais ne change pas la nature du conflit de symbole.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-22.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-22.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🟡 **Première stabilité depuis le 17/06** | `max_pain` = **180.0** (was 180.0 à 13h, was 162.5 à 10h, was 210.0 à 17/06), `put_call_ratio` = **0.83** (stable vs 13h), `call_oi_pct` = **54.8%** (stable vs 13h) |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $251.50, 4 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-22.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality — résolution maintenue :** Le `[WARNING] SPCX: volume is 0` reste absent du validation report 2026-06-22. La cohérence pipeline entre validation report et `latest.json` est maintenue. Cependant, le volume reste factice pour un ETF SPAC.

**Alerte social sentiment (artefact) :** `data/social_sentiment_latest.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL stable :** `data/sector_rotation_2026-06-22.json` signale `NEUTRAL` avec 11/11 secteurs OK. XLK (Technology) domine avec momentum_score 10.0. XLF (Financials) : return_20d +3.94%, rs_20d +3.40%, momentum_score **5.15** (was 4.25 à 10h UTC, +0.90 pt). Le signal sectoriel est lisible mais n'impacte pas SPCX (absent du ranking sectoriel).

**Anomalie upcoming events (artefact) :** `data/upcoming_events_2026-06-22.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-22 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. Aucun événement corporate réel détecté dans `data/events_2026-06-22.json` pour SPCX.

---

## Scoring global (agents pipeline 2026-06-22, snapshot 17h UTC)

| Axe | Score | Changement vs 13h 22/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **8.0/10** | = | Stable — absence de catalyseur réel |
| Score Valorisation | **4.5/10** | = | Stable — proche seuil disqualification |
| Score Momentum | **4.0/10** | −0.5 pt | Placeholder mécanique ajusté à la baisse sur faux mouvement −10.35% |
| **Score Opportunité** | **5.6/10** | −0.1 pt | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **56.0/100** | −1.2 pt | **ATTENDRE** (fourchette 50–59) |
| **Score Global Ajusté** | **56.0/100** | −1.2 pt | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel — faux earnings FMP ignoré)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL stable mais sans impact direct sur SPCX)

**Règle de disqualification :** 🟡 **Score Valorisation = 4.5/10** — le seuil de disqualification (≤ 2/10) est dépassé mécaniquement. Le Score Opportunité est à **5.6/10**. L'Agent Recommandation maintient le ticker en **ATTENDRE**.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | **ATTENDRE** | — | ✅ **SPCX = 56.0** |
| 35–49 | SURVEILLER | — | — |
| < 35 | ÉVITER | — | — |

> **Note institutionnelle :** Le maintien en ATTENDRE 56.0/100 est **purement mécanique** et non fondé sur une amélioration de la qualité data. Les métriques techniques restent toutes nulles, le secteur reste incorrect, et le prix reste fictif. Le léger ajustement à la baisse (−1.2 pt) est porté par le Score Momentum (−0.5 pt), réagissant mécaniquement au faux mouvement −10.35% du cours. Le setup reste **non-actionnable** en pratique.

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours fictif $165.845 — aucune donnée de marché réelle |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable. Le faux cours $165.845 est ~7.5× supérieur à ces niveaux.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **CONFIRMÉE EN ATTENDRE AVEC NUANCE DE DÉGRADATION** — **Score Global ajusté à la baisse 57.2 → 56.0/100**, mais **qualité data toujours dégradée**. Trente-sixième snapshot consécutif sans données techniques fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif) |
| RSI | ❌ Non disponible |
| Volume | 🔴 88.0M unités — faux volume collapse majeur (−67.7% vs 13h) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🟡 **56.0/100** → **ATTENDRE** (fourchette 50–59) — ajustement mécanique à la baisse |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $165.845, sector Industrials/Aerospace & Defense, market cap $2.18T, forward P/E 843.29 |
| Signal sectoriel | 🟡 **NEUTRAL stable** — XLK momentum_score 10.0, XLF momentum_score 5.15 (+0.90 pt vs 10h), 11/11 secteurs OK |
| Stabilité inter-snapshot | 🔴 Prix mutants : $185.00 (13h) → $165.845 (17h) — faux gap −10.35% |
| Seuil de vigilance | 🟡 Score Valorisation 4.5/10 — seuil de disqualification dépassé mécaniquement |
| Qualité data pipeline | 🟢 Aucun warning SPCX — cohérence validation report / `latest.json` maintenue |
| Options | 🟡 **Première stabilité depuis le 17/06** : max_pain 180.0, put/call 0.83, call OI 54.8% (tous inchangés vs 13h) |
| Consensus FMP | 🟢 Stabilisation confirmée : PT $251.50, 4 analysts (inchangé vs 13h) |
| Float FMP | 🟢 Stabilisation confirmée : 281.2M (inchangé vs 13h) |
| DRAFT_refresh | 🔴 **Déclenché mécaniquement** par gap −10.35% (`agents/detect_major_events`) — gap fictif, DRAFT à ignorer ou traiter comme artefact |

- **Confirmation :** L'Agent Recommandation maintient le ticker en **ATTENDRE 56.0/100** avec un Score Opportunité légèrement réduit à 5.6/10 (C:8.0 V:4.5 M:4.0). Le timing reste Neutre. La **stabilisation des options**, du float et du consensus entre 13h et 17h est une pause notable dans la mutation, mais ne résout pas le conflit de symbole.
- **Nuances :** Le snapshot 17h UTC du 22/06 montre une **nouvelle chute fictine majeure** : prix fictif $165.845 (−10.35% vs previous close $185.00), avec faux OHLC rétréci ($165.00–$176.69), faux market cap $2.18T (−10.35% vs 13h), et **forward P/E muté** de 711.54 à 843.29 (+18.5%, toujours impossible). Le **volume fictif s'est effondré de 67.7%** (272.1M → 88.0M). Cependant, pour la **première fois depuis le 17/06**, les données options se sont **stabilisées** (max_pain 180.0, put/call 0.83, call OI 54.8% — tous inchangés vs 13h). Le float FMP (281.2M) et le consensus analystes ($251.50, 4 analysts) sont également stables. Le module sector rotation est stable (NEUTRAL, 11/11 OK) avec une **amélioration du momentum XLF** (+0.90 pt à 5.15). L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 22/06 est un artefact récurrent et ignoré. Le validation report reste cohérent (aucun warning SPCX).
- **DRAFT_refresh :** Le module `detect_major_events` a généré un `SPCX_2026-06-22_DRAFT_refresh.md` sur le trigger `PRICE_GAP` (−10.35%). Ce DRAFT est **purement mécanique** (faux prix) et ne justifie pas un full refresh opérationnel. La thèse précédente n'est ni confirmée ni invalidée par ce gap fictif. Si l'utilisateur souhaite néanmoins forcer un full refresh, le DRAFT est disponible dans le dossier.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation fiable. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHETER (Réduit). Tant que le prix oscille entre des valeurs fictives volatiles ($135–$225), aucune action n'est justifiable en pratique.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** (artefact mécanique) ou retour en **ÉVITER** si le scoring re-chute sous 50. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER** fondé sur données réelles. Si les métriques FMP reprennent leur volatilité mutante (forward P/E, options, consensus) → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable malgré le reclassement agent)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur trente-six snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère (prix fictif $165.845, sector Industrials/Aerospace & Defense, market cap $2.18T, forward P/E 843.29, float 281.2M, consensus $251.50). Le maintien en ATTENDRE 56.0/100 n'est pas fondé sur une amélioration tangible de la qualité data. Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et métriques stables avant toute réévaluation opérationnelle.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **88,013,714** | 🔴 Extrême anomalie | Faux volume collapse −67.7% vs 13h, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🟡 Première stabilité depuis le 17/06 | — | `max_pain` = 180.0 (stable vs 13h), `put_call_ratio` = 0.83 (stable), `call_oi_pct` = 54.8% (stable) |
| Révisions consensus | 🟢 Stabilisation confirmée | — | PT $251.50 et 4 analysts — inchangé vs 13h |
| Float FMP | 281,190,750 | 🟢 Stabilisation | Inchangé vs 13h — mutation fixée |
| Faux −10.35% | −10.35% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | Aucun warning SPCX | 🟢 Cohérent | Cohérence maintenue entre validation report et `latest.json` |
| DRAFT_refresh | Déclenché | 🔴 Artefact | `PRICE_GAP` −10.35% déclenchement mécanique sur faux prix |

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
| Options stables et cohérentes (max_pain proche du vrai cours ~$22) | 1–3j | Confiance data restaurée | Si max_pain reprend sa mutation → méfiance |
| Consensus FMP stable (PT et nb analysts constants) | 1–3j | Mapping symbole stabilisé | Si consensus mute à nouveau → méfiance |
| Forward P/E FMP stable (arrêt des mutations > ±10%) | 1–3j | Métrique fondamentale stabilisée | Si forward P/E continue de muter → data quality irréparable |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 13h UTC 2026-06-22
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ATTENDRE (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — maintien agent non fondé sur amélioration data quality)
- Raison principale : Snapshot 17h UTC 22/06 : conflit de symbole FMP chronique persistant — nouveau prix fictif $165.845 (−10.35% vs previous close $185.00), faux OHLC $165.00–$176.69, faux market cap $2.18T (−10.35% vs 13h), forward P/E muté 843.29 (was 711.54, +18.5%), sector Industrials/Aerospace & Defense, volume fictif collapse 88.0M (−67.7%). Stabilisation confirmée du float FMP (281.2M, inchangé vs 13h), du consensus (PT $251.50, 4 analysts) et des options (max_pain 180.0, put/call 0.83, call OI 54.8%). Scoring agent ajustement mécanique à la baisse ATTENDRE 56.0/100 : Score Opportunité 5.6/10 (C:8.0 V:4.5 M:4.0), Score Valorisation 4.5/10, Score Catalyseur 8.0/10, Score Momentum 4.0/10 (−0.5 pt). Sector rotation stable (NEUTRAL, 11/11 secteurs OK, XLK momentum 10.0, XLF momentum 5.15). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 22/06 ignoré. Validation report cohérent (aucun warning SPCX). DRAFT_refresh déclenché mécaniquement par gap −10.35% (faux prix) — à ignorer.
- Thèse : 🟡 **Confirmée en ATTENDRE avec nuance de dégradation** — ajustement mécanique Score Global 57.2 → 56.0/100, conflit de symbole chronique persistant, données totalement non fiables, mutation forward P/E majeure (+18.5%), faux volume collapse −67.7%, setup non-actionnable en pratique. Première stabilisation des options/float/consensus depuis le 17/06.
