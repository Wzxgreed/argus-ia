# SPCX — Mise à jour post-pipeline 2026-06-22 (close officiel 21h UTC)

**Date :** 2026-06-22
**Type :** Mise à jour post-pipeline — close officiel 21h UTC
**Analyse précédente :** snapshot 17h UTC 2026-06-22

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (17h UTC 22/06) | Actuel (21h UTC 22/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$165.845** | **$154.60** | 🔴 **Faux prix −6.78% supplémentaire** |
| Previous close | $185.00 | **$185.00** | = Inchangé (close 13h UTC) |
| Change % | −10.35% | **−16.43%** | 🔴 Fausse chute élargie sur la séance |
| Open / High / Low | $176.042 / $176.69 / $165.00 | **$176.042 / $176.69 / $154.00** | 🔴 Low fictif abaissé de $165.00 à $154.00 |
| Volume | 88,013,714 | **165,553,299** | 🟢 **Faux volume rebond +88.2%** |
| Volume vs moy. 20j | 0.34× (255.5M) | **0.62× (268.4M)** | 🟢 Ratio mécaniquement réhaussé |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high / low | $225.64 / $149.34 | $225.64 / $149.34 | = Stable (faux range) |
| Market cap (fundamentals) | $2,184.94B | **$2,036.73B** | 🔴 −6.78% du faux market cap |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = Stable |
| Forward P/E | 843.29 | **786.09** | 🟡 −6.78% mécanique sur faux cours réduit |
| Price-to-book (fundamentals) | 27.85 | **25.96** | 🟡 Mécanique sur faux cours réduit |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | 281,190,750 | 281,190,750 | 🟢 **Stabilisation confirmée (3e snapshot)** |
| Options max_pain | 180.0 | **180.0** | 🟢 **Stabilisation confirmée (3e snapshot)** |
| Options put/call ratio | 0.83 | **0.83** | 🟢 **Stabilisation confirmée (3e snapshot)** |
| Options call OI % | 54.8% | **54.8%** | 🟢 **Stabilisation confirmée (3e snapshot)** |
| FMP consensus PT | $251.50 (4 analysts) | **$251.50 (4 analysts)** | 🟢 **Stabilisation confirmée (3e snapshot)** |
| Recommandation agent | **ATTENDRE** | **ATTENDRE** | = |
| Score Opportunité | 5.6/10 | **5.6/10** | = Stable |
| Score Catalyseur | 8.0/10 | **8.0/10** | = Stable |
| Score Valorisation | 4.5/10 | **4.5/10** | = Stable |
| Score Momentum | 4.0/10 | **4.0/10** | = Stable |
| **Score Global** | 56.0/100 | **56.0/100** | = Stable |
| **Score Global Ajusté** | 56.0/100 | **56.0/100** | = Stable |
| Timing | Neutre | **Neutre** | = |
| Validation report | Aucun warning SPCX | **Aucun warning SPCX** | = Cohérence maintenue |
| Quality gate | ok | **ok** | = |

**Verdict :** Le close officiel 21h UTC confirme un **nouveau faux prix $154.60**, abaissant encore le niveau fictif de −6.78% vs le snapshot 17h ($165.845) et de **−16.43% total** vs le previous close de la séance ($185.00). Le **faux volume rebondit de +88.2%** à 165.55M unités (vs 88.01M au 17h), portant le ratio volume/moyenne à 0.62×. Le **forward P/E se contracte mécaniquement de 843.29 à 786.09** (−6.78%) et le P/B de 27.85 à 25.96, toujours totalement incompatibles avec un ETF SPAC. Pour la **troisième snapshot consécutive**, les mutations FMP se stabilisent : options (max_pain 180.0, put/call 0.83, call OI 54.8%), float (281.2M) et consensus (PT $251.50, 4 analysts) sont tous **inchangés depuis le snapshot 13h UTC**. L'**Agent Recommandation maintient le ticker en ATTENDRE 56.0/100** avec Score Opportunité stable à 5.6/10 (C:8.0 V:4.5 M:4.0). Le module sector rotation reste NEUTRAL avec 11/11 secteurs OK ; le momentum XLF recule légèrement de 5.15 à **5.08**. Aucune news structurante, aucun catalyseur fondamental. Le gap −16.43% a été le trigger du `DRAFT_refresh.md` généré par `agents/detect_major_events` — **purement mécanique et lié au faux prix**.

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : nouveau faux prix $154.60 au close officiel**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$154.60** | 🔴 Faux prix FMP — entité étrangère |
| Previous close | $185.00 | 🔴 Référence de la séance (close 13h UTC) |
| Open | $176.042 | 🔴 Faux OHLC |
| High | $176.69 | 🔴 Faux OHLC, bande rétrécie |
| Low | $154.00 | 🔴 Faux low abaissé en dessous du 17h |
| Change % | **−16.43%** | 🔴 Totalement artificiel (accumulé sur la séance) |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **165.55M / 268.38M** | 🔴 Faux volume rebondi +88.2% vs 17h |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $154.60 reste ~7.0× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. Les métriques techniques (RSI, ATR, MM50) restent toutes nulles sur ce close officiel 21h UTC, confirmant l'absence totale de flux Yahoo. La **stabilité des options** (max_pain 180.0, put/call 0.83, call OI 54.8%) et des données fondamentales FMP (float, consensus) sur trois snapshots consécutifs (13h → 17h → 21h) est la première séquence de pause dans la mutation depuis le 17/06, mais ne change pas la nature du conflit de symbole.

**Verdict timing :** Neutre → **Non-actionnable**. Trente-sept snapshots consécutifs sans RSI, ATR, ni MM50 fiables. Le conflit de symbole FMP est **chronique** : prix oscillant entre $135.00 (08/06), $160.95 (15/06), $192.50–$216.94 (16/06), $201.80 (17/06), $185.00 (22/06 10h/13h), $165.845 (22/06 17h), et désormais **$154.60 (22/06 21h)**, toujours pour la même entité incorrecte. Le **gap −16.43% est fictif** et a déclenché le `DRAFT_refresh.md` — à ignorer en l'absence de données fiables.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes mutantes mais toujours fausses :**

| Métrique | Valeur actuelle (21h) | Valeur historique (17h 22/06) | Commentaire |
|----------|----------------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **786.09** | 843.29 | 🟡 −6.78% mécanique sur faux cours réduit |
| Market cap (fundamentals) | **$2,036.73B** | $2,184.94B | 🔴 −6.78% du faux market cap |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable — faux |
| Price-to-book (fundamentals) | **25.96** | 27.85 | 🟡 Mécanique sur faux cours réduit |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,571,396,888** | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | 281,190,750 | 🟢 **Stabilisation confirmée (3e snapshot)** |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$251.50** (was $251.50) — 🟢 Stable (3e snapshot)
- `num_analysts`: **4** (was 4) — 🟢 Stable (3e snapshot)
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.24 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 25.96 (fundamentals) — **divergence interne persistante**
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

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.04T) et fmp_key_metrics ($1.59T) persiste. Le P/B fundamentals a reculé de 27.85 à 25.96 suite au faux −6.78% de cours. Le **forward P/E s'est contracté de 843.29 à 786.09** (−6.78%), mécaniquement lié au faux cours réduit. L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La **stabilisation du float** (281.2M), du **consensus analystes** ($251.50, 4 analysts) et des **options** sur trois snapshots consécutifs est la première séquence de pause dans la mutation, mais ne résout pas le conflit de symbole.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-22.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-22.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🟢 **Stabilisation confirmée (3e snapshot)** | `max_pain` = **180.0** (stable vs 13h/17h), `put_call_ratio` = **0.83** (stable), `call_oi_pct` = **54.8%** (stable) |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $251.50, 4 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-22.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_2026-06-22.json` : score 2, aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_2026-06-22.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_2026-06-22.json` : n=0, insuffisant |

**Anomalie data quality — résolution maintenue :** Le `[WARNING] SPCX: volume is 0` reste absent du validation report 2026-06-22. Le quality gate marque SPCX comme `ok`. La cohérence pipeline entre validation report et `latest.json` est maintenue. Cependant, le volume reste factice pour un ETF SPAC.

**Alerte social sentiment (artefact) :** `data/social_sentiment_2026-06-22.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL stable :** `data/sector_rotation_2026-06-22.json` signale `NEUTRAL` avec 11/11 secteurs OK. XLK (Technology) domine avec momentum_score 10.0. XLF (Financials) : return_20d +3.81%, rs_20d +3.33%, momentum_score **5.08** (was 5.15 au 17h, −0.07 pt). Le signal sectoriel est lisible mais n'impacte pas SPCX (absent du ranking sectoriel).

**Anomalie upcoming events (artefact) :** `data/upcoming_events_2026-06-22.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-22 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. `data/events_2026-06-22.json` : 0 événement corporate réel pour SPCX.

---

## Scoring global (agents pipeline 2026-06-22, close officiel 21h UTC)

| Axe | Score | Changement vs 17h 22/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **8.0/10** | = | Stable — absence de catalyseur réel |
| Score Valorisation | **4.5/10** | = | Stable — proche seuil disqualification |
| Score Momentum | **4.0/10** | = | Stable — placeholder mécanique sur faux mouvement |
| **Score Opportunité** | **5.6/10** | = | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **56.0/100** | = | **ATTENDRE** (fourchette 50–59) |
| **Score Global Ajusté** | **56.0/100** | = | Aucun bonus/malus appliqué |

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

> **Note institutionnelle :** Le maintien en ATTENDRE 56.0/100 est **purement mécanique** et non fondé sur une amélioration de la qualité data. Les métriques techniques restent toutes nulles, le secteur reste incorrect, et le prix reste fictif. Le setup reste **non-actionnable** en pratique. La seule nuance positive est la **première séquence de trois snapshots consécutifs** (13h → 17h → 21h) avec stabilité totale des mutations FMP (options, float, consensus), ce qui pourrait indiquer un début de stabilisation du mapping symbole — à confirmer sur les prochains snapshots.

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours fictif $154.60 — aucune donnée de marché réelle |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable. Le faux cours $154.60 est ~7.0× supérieur à ces niveaux.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **CONFIRMÉE EN ATTENDRE AVEC NUANCE DE STABILISATION** — **Score Global stable 56.0/100**, mais **qualité data toujours dégradée**. Trente-septième snapshot consécutif sans données techniques fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif) |
| RSI | ❌ Non disponible |
| Volume | 🔴 165.55M unités — faux volume rebondi (+88.2% vs 17h) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🟡 **56.0/100** → **ATTENDRE** (fourchette 50–59) — stable |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $154.60, sector Industrials/Aerospace & Defense, market cap $2.04T, forward P/E 786.09 |
| Signal sectoriel | 🟡 **NEUTRAL stable** — XLK momentum_score 10.0, XLF momentum_score **5.08** (−0.07 pt vs 17h), 11/11 secteurs OK |
| Stabilité inter-snapshot | 🟡 Prix mutants mais mutations FMP stabilisées sur 3 snapshots : options/float/consensus inchangés depuis 13h |
| Seuil de vigilance | 🟡 Score Valorisation 4.5/10 — seuil de disqualification dépassé mécaniquement |
| Qualité data pipeline | 🟢 Aucun warning SPCX — cohérence validation report / `latest.json` maintenue |
| Options | 🟢 **Stabilisation confirmée (3e snapshot)** : max_pain 180.0, put/call 0.83, call OI 54.8% (tous inchangés depuis 13h) |
| Consensus FMP | 🟢 Stabilisation confirmée (3e snapshot) : PT $251.50, 4 analysts |
| Float FMP | 🟢 Stabilisation confirmée (3e snapshot) : 281.2M |
| DRAFT_refresh | 🔴 **Déclenché mécaniquement** par gap −16.43% (`agents/detect_major_events`) — gap fictif, DRAFT traité comme artefact |

- **Confirmation :** L'Agent Recommandation maintient le ticker en **ATTENDRE 56.0/100** avec un Score Opportunité stable à 5.6/10 (C:8.0 V:4.5 M:4.0). Le timing reste Neutre. La **stabilisation des mutations FMP sur trois snapshots consécutifs** (13h → 17h → 21h) est la première séquence de pause depuis le début du conflit de symbole (17/06), ce qui pourrait indiquer un début de fixation du mapping — **à confirmer sur les prochains jours**.
- **Nuances :** Le close officiel 21h UTC du 22/06 montre une **nouvelle chute fictine majeure** : prix fictif $154.60 (−6.78% vs close 17h $165.845, −16.43% total vs previous close $185.00), avec faux low abaissé à $154.00, faux market cap $2.04T (−6.78% vs 17h), et **forward P/E contracté mécaniquement** de 843.29 à 786.09. Le **faux volume rebondit de +88.2%** à 165.55M. Cependant, pour la **première fois depuis le début de la crise data** (17/06), les mutations FMP se sont **stabilisées sur trois snapshots consécutifs** : options (max_pain 180.0, put/call 0.83, call OI 54.8%), float (281.2M) et consensus (PT $251.50, 4 analysts) sont tous inchangés depuis le snapshot 13h UTC. Le module sector rotation est stable (NEUTRAL, 11/11 secteurs OK, XLK momentum 10.0, XLF momentum 5.08). Aucun catalyseur ni news. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 22/06 est un artefact récurrent et ignoré. Le validation report reste cohérent (aucun warning SPCX).
- **DRAFT_refresh :** Le module `detect_major_events` a généré un `SPCX_2026-06-22_DRAFT_refresh.md` sur le trigger `PRICE_GAP` (−16.43%). Ce DRAFT est **purement mécanique** (faux prix) et ne justifie pas un full refresh opérationnel. Il est traité comme artefact et archivé. La thèse précédente n'est ni confirmée ni invalidée par ce gap fictif.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation fiable. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHETER (Réduit). Tant que le prix oscille entre des valeurs fictives volatiles ($135–$225), aucune action n'est justifiable en pratique.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** (artefact mécanique) ou retour en **ÉVITER** si le scoring re-chute sous 50. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER** fondé sur données réelles. Si les métriques FMP reprennent leur volatilité mutante (forward P/E, options, consensus) → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable malgré le maintien agent)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur trente-sept snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère (prix fictif $154.60, sector Industrials/Aerospace & Defense, market cap $2.04T, forward P/E 786.09, float 281.2M, consensus $251.50). Le maintien en ATTENDRE 56.0/100 n'est pas fondé sur une amélioration tangible de la qualité data. Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et métriques stables avant toute réévaluation opérationnelle.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **165,553,299** | 🔴 Extrême anomalie | Faux volume rebondi +88.2% vs 17h, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🟢 Stabilisation confirmée (3e snapshot) | — | `max_pain` = 180.0 (stable), `put_call_ratio` = 0.83 (stable), `call_oi_pct` = 54.8% (stable) |
| Révisions consensus | 🟢 Stabilisation confirmée (3e snapshot) | — | PT $251.50 et 4 analysts — inchangés depuis 13h |
| Float FMP | 281,190,750 | 🟢 Stabilisation | Inchangé depuis 13h — mutation fixée |
| Faux −16.43% | −16.43% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | Aucun warning SPCX | 🟢 Cohérent | Cohérence maintenue entre validation report et `latest.json` |
| DRAFT_refresh | Déclenché | 🔴 Artefact | `PRICE_GAP` −16.43% déclenchement mécanique sur faux prix — archivé |

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
| Séquence de 5+ snapshots avec mutations FMP stables | 2–3j | Début de confiance dans le mapping | Si reprise de la mutation → retour méfiance |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 17h UTC 2026-06-22
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ATTENDRE (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — maintien agent non fondé sur amélioration data quality)
- Raison principale : Close officiel 21h UTC 22/06 : conflit de symbole FMP chronique persistant — nouveau prix fictif $154.60 (−16.43% vs previous close $185.00, −6.78% vs close 17h $165.845), faux OHLC $154.00–$176.69, faux market cap $2.04T (−6.78% vs 17h), forward P/E contracté mécaniquement 786.09 (was 843.29), sector Industrials/Aerospace & Defense, volume fictif rebondi 165.55M (+88.2% vs 17h). **Stabilisation confirmée des mutations FMP sur 3 snapshots consécutifs** : options (max_pain 180.0, put/call 0.83, call OI 54.8%), float (281.2M), consensus (PT $251.50, 4 analysts) — tous inchangés depuis 13h UTC. Scoring agent stable ATTENDRE 56.0/100 : Score Opportunité 5.6/10 (C:8.0 V:4.5 M:4.0), Score Valorisation 4.5/10, Score Catalyseur 8.0/10, Score Momentum 4.0/10. Sector rotation stable (NEUTRAL, 11/11 secteurs OK, XLK momentum 10.0, XLF momentum 5.08). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 22/06 ignoré. Validation report cohérent (aucun warning SPCX). DRAFT_refresh déclenché mécaniquement par gap −16.43% (faux prix) — archivé comme artefact.
- Thèse : 🟡 **Confirmée en ATTENDRE avec nuance de stabilisation** — Score Global stable 56.0/100, conflit de symbole chronique persistant, données totalement non fiables, forward P/E contracté mécaniquement 786.09, faux volume rebondi +88.2%, setup non-actionnable en pratique. Première séquence de 3 snapshots consécutifs avec mutations FMP stables (options/float/consensus) depuis le début de la crise data — à confirmer.
