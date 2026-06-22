# SPCX — Mise à jour post-pipeline 2026-06-22 (snapshot 13h UTC)

**Date :** 2026-06-22
**Type :** Mise à jour post-pipeline — snapshot 13h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-22

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 22/06) | Actuel (13h UTC 22/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$185.00** | **$185.00** | = Stable |
| Previous close | $191.82 | $191.82 | = |
| Change % | **−3.56%** | **−3.56%** | = Stable |
| Open / High / Low | $188.39 / $190.00 / $172.11 | $188.39 / $190.00 / $172.11 | = |
| Volume | 272,126,800 | 272,126,800 | = |
| Volume vs moy. 20j | 0.94× (288.9M) | 0.94× (288.9M) | = |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high / low | $225.64 / $149.34 | $225.64 / $149.34 | = |
| Market cap (fundamentals) | $2,437.22B | $2,437.22B | = |
| Market cap (fmp_key_metrics) | $1,585.46B | $1,585.46B | = |
| Forward P/E | 711.54 | 711.54 | = |
| Price-to-book (fundamentals) | 31.06 | 31.06 | = |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = |
| Shares float | 281,190,750 | 281,190,750 | = |
| Options max_pain | 162.5 | **180.0** | 🔴 **Nouvelle mutation +17.5** |
| Options put/call ratio | null | **0.83** | 🔴 **Réapparition mécanique** |
| Options call OI % | null | **54.8%** | 🔴 **Réapparition mécanique** |
| FMP consensus PT | $251.50 (4 analysts) | $251.50 (4 analysts) | = Stable |
| Recommandation agent | **ATTENDRE** | **ATTENDRE** | = |
| Score Opportunité | 5.7/10 | **5.7/10** | = |
| Score Catalyseur | 8.0/10 | **8.0/10** | = |
| Score Valorisation | 4.5/10 | **4.5/10** | = |
| Score Momentum | 4.5/10 | **4.5/10** | = |
| **Score Global** | 57.2/100 | **57.2/100** | = |
| **Score Global Ajusté** | 57.2/100 | **57.2/100** | = |
| Timing | Neutre | **Neutre** | = |
| Validation report | Aucun warning SPCX | Aucun warning SPCX | = |

**Verdict :** Trente-cinquième snapshot consécutif sans données techniques fiables. Le conflit de symbole FMP persiste avec un **prix fictif stable $185.00** (−3.56% vs previous close $191.82) et un faux market cap de **$2.44T**. Les métriques fondamentales (forward P/E 711.54, sector Industrials/Aerospace & Defense, float 281.2M, consensus $251.50) sont toutes stables vs 10h. **Seule anomalie détectée : les données options ont muté à nouveau** — `max_pain` 162.5 → 180.0 (+17.5), `put_call_ratio` réapparu à 0.83 (was null), `call_oi_pct` réapparu à 54.8% (was null). L'Agent Recommandation maintient le ticker en **ATTENDRE 57.2/100** avec un Score Opportunité stable à 5.7/10 (C:8.0 V:4.5 M:4.5). Le validation report 2026-06-22 compte 5 [ERROR] et 2 [WARNING] mais aucun ne concerne SPCX. Le module sector rotation reste stable (NEUTRAL, 11/11 secteurs OK). Aucune news, social, ni catalyseur fondamental.

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : prix fictif $185.00**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$185.00** | 🔴 Faux prix FMP — entité étrangère |
| Previous close | $191.82 | 🔴 Révisé (close dernière séance) |
| Open | $188.39 | 🔴 Faux OHLC |
| High | $190.00 | 🔴 Faux OHLC, bande rétrécie |
| Low | $172.11 | 🔴 Faux OHLC, bande élargie en dessous |
| Change % | **−3.56%** | 🔴 Totalement artificiel |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **272.1M / 288.9M** | 🔴 Volume fictif stable |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $185.00 reste ~8× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. Les métriques techniques (RSI, ATR, MM50) restent toutes nulles sur ce snapshot 13h UTC, confirmant l'absence totale de flux Yahoo.

**Verdict timing :** Neutre → **Non-actionnable**. Trente-cinq snapshots consécutifs sans RSI, ATR, ni MM50 fiables. Le conflit de symbole FMP est **chronique** : prix oscillant entre $135.00 (08/06), $160.95 (15/06), $192.50–$216.94 (16/06), $201.80 (17/06), $185.00 (22/06), toujours pour la même entité incorrecte.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes stables mais toujours fausses :**

| Métrique | Valeur actuelle (13h) | Valeur historique (10h 22/06) | Commentaire |
|----------|----------------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **711.54** | 711.54 | = Stable — toujours impossible |
| Market cap (fundamentals) | **$2,437.22B** | $2,437.22B | = Stable — faux |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable — faux |
| Price-to-book (fundamentals) | **31.06** | 31.06 | = Stable |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,571,396,888** | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | 281,190,750 | = Stable — mutation 10h fixée |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$251.50** (was $251.50) — = Stable
- `num_analysts`: **4** (was 4) — = Stable
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

> **Note institutionnelle :** L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La stabilisation du float (281.2M) et du consensus ($251.50, 4 analysts) entre 10h et 13h est une pause dans la mutation, mais ne change pas la nature du conflit de symbole.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-22.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-22.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🔴 **Anomalie mutante (2e mutation du jour)** | `max_pain` = **180.0** (was 162.5 à 10h, was 210.0 à 17/06), `put_call_ratio` = **0.83** (was null à 10h, was 0.66 à 17/06), `call_oi_pct` = **54.8%** (was null à 10h, was 60.3% à 17/06) |
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

## Scoring global (agents pipeline 2026-06-22, snapshot 13h UTC)

| Axe | Score | Changement vs 10h 22/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **8.0/10** | = | Stable — absence de catalyseur réel |
| Score Valorisation | **4.5/10** | = | Stable — proche seuil disqualification |
| Score Momentum | **4.5/10** | = | Placeholder mécanique, non fondé sur données de marché réelles |
| **Score Opportunité** | **5.7/10** | = | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **57.2/100** | = | **ATTENDRE** (fourchette 50–59) |
| **Score Global Ajusté** | **57.2/100** | = | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel — faux earnings FMP ignoré)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL stable mais sans impact direct sur SPCX)

**Règle de disqualification :** 🟡 **Score Valorisation = 4.5/10** — le seuil de disqualification (≤ 2/10) est dépassé mécaniquement. Le Score Opportunité est à **5.7/10**. L'Agent Recommandation maintient le ticker en **ATTENDRE**.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | **ATTENDRE** | — | ✅ **SPCX = 57.2** |
| 35–49 | SURVEILLER | — | — |
| < 35 | ÉVITER | — | — |

> **Note institutionnelle :** Le maintien en ATTENDRE 57.2/100 est **purement mécanique** et non fondé sur une amélioration de la qualité data. Les métriques techniques restent toutes nulles, le secteur reste incorrect, et le prix reste fictif. Le setup reste **non-actionnable** en pratique.

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

**Verdict :** 🟡 Thèse **CONFIRMÉE EN ATTENDRE** — **Score Global stable 57.2/100**, mais **qualité data toujours dégradée**. Trente-cinquième snapshot consécutif sans données techniques fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif) |
| RSI | ❌ Non disponible |
| Volume | 🔴 272.1M unités — volume fictif stable |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🟡 **57.2/100** → **ATTENDRE** (fourchette 50–59) — stable |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $185.00, sector Industrials/Aerospace & Defense, market cap $2.44T, forward P/E 711.54 |
| Signal sectoriel | 🟡 **NEUTRAL stable** — XLK momentum_score 10.0, XLF momentum_score 4.25, 11/11 secteurs OK |
| Stabilité inter-snapshot | 🟢 Prix stable $185.00 (10h → 13h) — pause dans la volatilité fictive |
| Seuil de vigilance | 🟡 Score Valorisation 4.5/10 — seuil de disqualification dépassé mécaniquement |
| Qualité data pipeline | 🟢 Aucun warning SPCX — cohérence validation report / `latest.json` maintenue |
| Options | 🔴 **2e mutation du jour** : max_pain 162.5 → **180.0**, put/call 0.83, call OI 54.8% (tous réapparus ou mutés vs 10h) |
| Consensus FMP | 🟢 Stabilisation : PT $251.50, 4 analysts (inchangé vs 10h) |
| Float FMP | 🟢 Stabilisation : 281.2M (inchangé vs 10h) |

- **Confirmation :** L'Agent Recommandation maintient le ticker en **ATTENDRE 57.2/100** avec un Score Opportunité stable à 5.7/10 (C:8.0 V:4.5 M:4.5). Aucun changement de scoring entre 10h et 13h. Le timing reste Neutre.
- **Nuances :** Le snapshot 13h UTC du 22/06 montre une **stabilisation partielle** du conflit de symbole : prix fictif $185.00 inchangé vs 10h, métriques fondamentales stables (forward P/E 711.54, market cap $2.44T, float 281.2M, consensus $251.50). Cependant, les **données options ont muté à nouveau** : `max_pain` 162.5 → 180.0 (+17.5), `put_call_ratio` réapparu à 0.83 (was null), `call_oi_pct` réapparu à 54.8% (was null). Cette instabilité des options confirme que le mapping symbole reste volatile sous la surface. Les métriques techniques (RSI, ATR, MM50) restent toutes nulles. Le module sector rotation est stable (NEUTRAL, 11/11 OK). L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 22/06 est un artefact récurrent et ignoré. Le validation report reste cohérent (aucun warning SPCX).
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation fiable. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHETER (Réduit). Tant que le prix oscille entre des valeurs fictives volatiles ($135–$225), aucune action n'est justifiable en pratique.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** (artefact mécanique) ou retour en **ÉVITER** si le scoring re-chute. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER** fondé sur données réelles. Si le faux prix reprend sa volatilité mutante ou si les métriques FMP continuent de diverger → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable malgré le reclassement agent)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur trente-cinq snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère (prix fictif $185.00, sector Industrials/Aerospace & Defense, market cap $2.44T, forward P/E 711.54, float 281.2M, consensus $251.50). Le maintien en ATTENDRE 57.2/100 n'est pas fondé sur une amélioration tangible de la qualité data. Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et métriques stables avant toute réévaluation opérationnelle.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **272,126,800** | 🔴 Extrême anomalie | Faux volume stable vs 10h, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 Anomalie mutante (2e mutation du jour) | — | `max_pain` = 180.0 (was 162.5 à 10h, was 210.0 à 17/06), `put_call_ratio` = 0.83 (was null à 10h), `call_oi_pct` = 54.8% (was null à 10h) |
| Révisions consensus | 🟢 Stabilisation | — | PT $251.50 et 4 analysts — inchangé vs 10h |
| Float FMP | 281,190,750 | 🟢 Stabilisation | Inchangé vs 10h — mutation fixée |
| Faux −3.56% | −3.56% | 🔴 Mouvement fictif stable | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | Aucun warning SPCX | 🟢 Cohérent | Cohérence maintenue entre validation report et `latest.json` |

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
| Consensus FMP stable (PT et nb analysts constants) | 1–3j | Mapping symbole stabilisé | Si consensus mute à nouveau → méfiance |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 10h UTC 2026-06-22
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ATTENDRE (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — maintien agent non fondé sur amélioration data quality)
- Raison principale : Snapshot 13h UTC 22/06 : conflit de symbole FMP chronique persistant — prix fictif stable $185.00 (−3.56% vs previous close $191.82), faux OHLC $172.11–$190.00, faux market cap $2.44T, forward P/E 711.54, sector Industrials/Aerospace & Defense, volume fictif 272.1M. Stabilisation partielle du float FMP (281.2M, inchangé vs 10h) et du consensus (PT $251.50, 4 analysts). Nouvelle mutation options (`max_pain` 162.5 → 180.0, put/call 0.83, call OI 54.8%). Scoring agent stable ATTENDRE 57.2/100 : Score Opportunité 5.7/10 (C:8.0 V:4.5 M:4.5), Score Valorisation 4.5/10, Score Catalyseur 8.0/10. Sector rotation stable (NEUTRAL, 11/11 secteurs OK, XLK momentum 10.0, XLF momentum 4.25). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 22/06 ignoré. Validation report cohérent (aucun warning SPCX).
- Thèse : 🟡 **Confirmée en ATTENDRE** — maintien agent Score Global 57.2/100, conflit de symbole chronique persistant, données totalement non fiables, mutation options 2e du jour (max_pain 180.0, was 162.5), setup non-actionnable en pratique
