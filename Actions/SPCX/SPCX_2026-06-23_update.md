# SPCX — Mise à jour post-pipeline 2026-06-23 (snapshot 13h UTC)

**Date :** 2026-06-23
**Type :** Mise à jour post-pipeline — snapshot 13h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-23

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 23/06) | Actuel (13h UTC 23/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$154.60** | **$154.60** | = **Stabilité mécanique totale** |
| Previous close | $185.00 | **$185.00** | = Inchangé |
| Change % | −16.43% | **−16.43%** | = Fausse chute figée |
| Open / High / Low | $176.04 / $176.75 / $154.00 | **$176.04 / $176.75 / $154.00** | = |
| Volume | 167,066,800 | **167,066,800** | = Faux volume stable |
| Volume vs moy. 20j | 0.62× (268.6M) | **0.62× (268.6M)** | = |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high / low | $225.64 / $149.34 | $225.64 / $149.34 | = |
| Market cap (fundamentals) | $2,036.73B | **$2,036.73B** | = |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = |
| Forward P/E | 786.09 | **786.09** | = |
| Price-to-book (fundamentals) | 25.96 | **25.96** | = |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = |
| Shares float | 281,190,750 | **281,190,750** | = **Stable (5e snapshot consécutif)** |
| Options max_pain | 162.5 | **180.0** | 🔴 **Mutation inverse de la mutation inverse** |
| Options put/call ratio | `null` | **0.36** | 🟡 **Réapparition** |
| Options call OI % | `null` | **73.5%** | 🟡 **Réapparition avec valeur supérieure** |
| FMP consensus PT | $251.50 (4 analysts) | **$235.2 (5 analysts)** | 🔴 **Mutation : PT −6.5%, analysts +1** |
| FMP consensus low/high | `null` / `null` | `null` / `null` | = |
| Recommandation agent | **ATTENDRE** | **ATTENDRE** | = |
| Score Opportunité | 5.6/10 | **5.6/10** | = Stable |
| Score Catalyseur | 8.0/10 | **8.0/10** | = |
| Score Valorisation | 4.5/10 | **4.5/10** | = |
| Score Momentum | 4.0/10 | **4.0/10** | = |
| **Score Global** | 56.0/100 | **56.0/100** | = Stable |
| **Score Global Ajusté** | 56.0/100 | **56.0/100** | = Stable |
| Timing | Neutre | **Neutre** | = |
| Validation report | Aucun warning SPCX | **Aucun warning SPCX** | = |
| Quality gate | ok | **ok** | = |

**Verdict :** Le snapshot 13h UTC du 23/06 confirme une **stabilité mécanique totale** du faux prix $154.60 (inchangé vs 10h UTC), avec le previous close figé à $185.00 et le faux volume stable. Cependant, la **séquence de stabilité des mutations FMP est rompue sur deux fronts :**

1. **Mutation consensus :** Après quatre snapshots consécutifs (13h → 17h → 21h 22/06 → 10h 23/06) où le consensus analystes était stable à $251.50 (4 analysts), le snapshot 13h UTC montre un **PT révisé à la baisse à $235.2** (−6.5%) et le **nombre d'analystes passe de 4 à 5**. Cette rupture invalide l'hypothèse de stabilisation du mapping symbole pour le consensus.

2. **Mutation inverse des options :** Après la disparition à 10h UTC (`max_pain` 162.5, `put_call_ratio` et `call_oi_pct` à `null`), les données options **réapparaissent** à 13h UTC avec `max_pain` = **180.0** (valeur du snapshot 13h 22/06), `put_call_ratio` = **0.36**, et `call_oi_pct` = **73.5%** (vs 54.8% au 21h 22/06). Cette volatilité des options confirme l'instabilité du mapping FMP.

Le **float** (281.2M) reste **inchangé pour un cinquième snapshot consécutif** (13h → 17h → 21h 22/06 → 10h → 13h 23/06), ce qui reste le seul champ FMP stable. Le module sector rotation émet un signal **NEUTRAL stable** avec 11/11 secteurs OK ; le momentum XLF reste à **5.45**. Aucune news structurante, aucun catalyseur fondamental.

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : faux prix $154.60 stable**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$154.60** | 🔴 Faux prix FMP — entité étrangère |
| Previous close | $185.00 | 🔴 Référence de la séance (close 22/06) |
| Open | $176.04 | 🔴 Faux OHLC |
| High | $176.75 | 🔴 Faux OHLC, bande rétrécie |
| Low | $154.00 | 🔴 Faux low inchangé |
| Change % | **−16.43%** | 🔴 Totalement artificiel (figé) |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **167.07M / 268.63M** | 🔴 Faux volume stable ~0.62× |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $154.60 reste ~7.0× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. Les métriques techniques (RSI, ATR, MM50) restent toutes nulles sur ce snapshot 13h UTC, confirmant l'absence totale de flux Yahoo. Le conflit de symbole FMP est **chronique** : après trente-neuf snapshots consécutifs sans données techniques fiables, le seul indicateur de la qualité du mapping est la **volatilité des champs FMP**. Le float reste stable (5e snapshot), mais le consensus et les options ont de nouveau muté, invalidant l'hypothèse de stabilisation partielle formulée au snapshot 10h.

**Verdict timing :** Neutre → **Non-actionnable**. Trente-neuf snapshots consécutifs sans RSI, ATR, ni MM50 fiables.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes stables mais toujours fausses :**

| Métrique | Valeur actuelle (13h 23/06) | Valeur historique (10h 23/06) | Commentaire |
|----------|----------------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **786.09** | 786.09 | = Stable — faux |
| Market cap (fundamentals) | **$2,036.73B** | $2,036.73B | = Stable — faux |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable — faux |
| Price-to-book (fundamentals) | **25.96** | 25.96 | = Stable — faux |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,571,396,888** | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | 281,190,750 | = **Stable (5e snapshot consécutif)** |

**FMP Consensus (mutation confirmée) :**
- `price_target_avg`: **$235.2** (was $251.50) — 🔴 **Baisse de −6.5%** ; rupture de la stabilité sur 4 snapshots
- `num_analysts`: **5** (was 4) — 🔴 **+1 analyste** ; rupture de la stabilité sur 4 snapshots
- `num_analysts_last_month`: **5** (was 4) — 🔴 Mutation
- `num_analysts_last_quarter`: **5** (was 4) — 🔴 Mutation
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.24 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 25.96 (fundamentals) — divergence interne persistante
- `price_to_sales`: 25.22 (stable)
- `price_to_fcf`: −33.75 (stable)
- `enterprise_value_multiple`: **369.23** (stable)
- `gross_margin`: 49.39% (stable)
- `operating_margin`: −13.86% (stable)
- `net_margin`: −26.44% (stable)

**FMP Key Metrics (stables mais faux) :**
- `market_cap`: $1,585.46B (stable)
- `enterprise_value`: $1,583.61B (stable)
- `ev_to_sales`: 84.80 (stable)
- `ev_to_ebitda`: 369.23 (stable)
- `net_debt_to_ebitda`: −0.43 (stable)
- `return_on_equity`: −11.95% (stable)

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.04T) et fmp_key_metrics ($1.59T) persiste. L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La **stabilité du float** (281.2M) sur cinq snapshots consécutifs est le seul signal de stabilité observé depuis le début du conflit de symbole (17/06). En revanche, la **mutation du consensus** (PT $251.50 → $235.2, analysts 4 → 5) et la **mutation inverse des options** (max_pain 162.5 → 180.0, put/call 0.36, call OI 73.5%) confirment que le mapping FMP reste **volatile et non résolu**. Le DRAFT_refresh.md du 23/06 (13h01) est déclenché par le gap −16.43% (`agents/detect_major_events`) — **purement mécanique et lié au faux prix figé** — mais les nouvelles mutations FMP justifient la mise à jour.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-23.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-23.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🟡 **Mutation inverse de la mutation inverse** | `max_pain` = **180.0** (was 162.5), `put_call_ratio` = **0.36** (was `null`), `call_oi_pct` = **73.5%** (was `null`) |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $235.2, 5 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-23.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_2026-06-23.json` : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_2026-06-23.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_2026-06-23.json` : n=0, insuffisant |

**Anomalie data quality — résolution maintenue :** Le `[WARNING] SPCX: volume is 0` reste absent du validation report 2026-06-23. Le quality gate marque SPCX comme `ok`. Cependant, le volume reste factice pour un ETF SPAC.

**Alerte social sentiment (artefact) :** `data/social_sentiment_2026-06-23.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL stable :** `data/sector_rotation_2026-06-23.json` signale `NEUTRAL` avec 11/11 secteurs OK. XLK (Technology) domine avec momentum_score 10.0. XLF (Financials) : return_20d +4.17%, rs_20d +3.69%, momentum_score **5.45** (stable vs 10h 23/06). Le signal sectoriel est lisible mais n'impacte pas SPCX (absent du ranking sectoriel).

**Anomalie upcoming events (artefact) :** `data/upcoming_events_2026-06-23.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-23 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. `data/events_2026-06-23.json` : 0 événement corporate réel pour SPCX.

---

## Scoring global (agents pipeline 2026-06-23, snapshot 13h UTC)

| Axe | Score | Changement vs 10h 23/06 | Commentaire |
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

> **Note institutionnelle :** Le maintien en ATTENDRE 56.0/100 est **purement mécanique** et non fondé sur une amélioration de la qualité data. Les métriques techniques restent toutes nulles, le secteur reste incorrect, et le prix reste fictif. Le setup reste **non-actionnable** en pratique. La seule nuance positive est que le **float** (281.2M) est **stable sur cinq snapshots consécutifs** (13h → 17h → 21h 22/06 → 10h → 13h 23/06), ce qui est la séquence de stabilité la plus longue observée. Cependant, cette stabilité partielle est **contrebalancée** par la rupture de stabilité du consensus (PT $235.2 vs $251.50, analysts 5 vs 4) et la mutation inverse des options (max_pain 180.0, put/call 0.36, call OI 73.5%). Le mapping FMP reste globalement instable.

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

**Verdict :** 🟡 Thèse **CONFIRMÉE EN ATTENDRE AVEC NUANCE NÉGATIVE** — **Score Global stable 56.0/100**, mais **qualité data toujours dégradée** et **hypothèse de stabilisation partielle invalidée**. Trente-neuvième snapshot consécutif sans données techniques fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif) |
| RSI | ❌ Non disponible |
| Volume | 🔴 167.07M unités — faux volume stable (~0.62×) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🟡 **56.0/100** → **ATTENDRE** (fourchette 50–59) — stable |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $154.60, sector Industrials/Aerospace & Defense, market cap $2.04T, forward P/E 786.09 |
| Signal sectoriel | 🟡 **NEUTRAL stable** — XLK momentum_score 10.0, XLF momentum_score **5.45** |
| Stabilité inter-snapshot | 🟡 Prix stable ($154.60), float stable sur 5 snapshots, mais **consensus et options mutés à nouveau** |
| Seuil de vigilance | 🟡 Score Valorisation 4.5/10 — seuil de disqualification dépassé mécaniquement |
| Qualité data pipeline | 🟢 Aucun warning SPCX — cohérence validation report / `latest.json` maintenue |
| Options | 🟡 **Mutation inverse de la mutation inverse** : max_pain 180.0 (was 162.5), put/call 0.36 (was `null`), call OI 73.5% (was `null`) |
| Consensus FMP | 🔴 **Stabilité rompue** : PT $235.2 (was $251.50), 5 analysts (was 4) |
| Float FMP | 🟢 **Stabilisation confirmée (5e snapshot)** : 281.2M inchangé |
| DRAFT_refresh | 🔴 **Déclenché mécaniquement** par gap −16.43% (`agents/detect_major_events`) — gap fictif, mais mutations FMP nouvelles justifient la mise à jour |

- **Confirmation :** L'Agent Recommandation maintient le ticker en **ATTENDRE 56.0/100** avec un Score Opportunité stable à 5.6/10 (C:8.0 V:4.5 M:4.0). Le timing reste Neutre. Le **float** (281.2M) est **inchangé pour un cinquième snapshot consécutif** (13h → 17h → 21h 22/06 → 10h → 13h 23/06), ce qui est la séquence de stabilité la plus longue observée depuis le début du conflit de symbole.
- **Nuances négatives :** La **stabilité du consensus sur quatre snapshots est rompue** : le `price_target_avg` baisse de $251.50 à **$235.2** (−6.5%) et le `num_analysts` passe de 4 à **5**. Les **options** ont également muté à l'inverse : `max_pain` remonte de 162.5 à **180.0** (valeur du snapshot 13h 22/06), `put_call_ratio` réapparaît à **0.36**, et `call_oi_pct` réapparaît à **73.5%** (vs 54.8% au snapshot 21h 22/06). Ces mutations confirment que le mapping symbole FMP reste **volatile et non résolu**. Le secteur persiste `Industrials` / `Aerospace & Defense`, le market cap faux $2.04T, et le forward P/E 786.09 sont tous inchangés. Aucun catalyseur ni news. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 23/06 est un artefact récurrent et ignoré.
- **DRAFT_refresh :** Le module `detect_major_events` a généré un `SPCX_2026-06-23_DRAFT_refresh.md` (13h01) sur le trigger `PRICE_GAP` (−16.43%). Ce DRAFT est **purement mécanique** (faux prix figé), mais les **nouvelles mutations FMP à 13h UTC** (consensus et options) justifient la présente mise à jour. Le DRAFT est classé **faux positif algorithmique avec mutations secondaires** et archivé.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation fiable. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHETER (Réduit). Tant que le prix oscille entre des valeurs fictives volatiles ($135–$225) ou reste figé sur un faux niveau, aucune action n'est justifiable en pratique.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** (artefact mécanique) ou retour en **ÉVITER** si le scoring re-chute sous 50. Si les mutations FMP reprennent sur le float (dernier champ stable) → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable malgré le maintien agent)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur trente-neuf snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère (prix fictif $154.60, sector Industrials/Aerospace & Defense, market cap $2.04T, forward P/E 786.09, float 281.2M). Le seul signal positif est la **stabilité du float sur cinq snapshots consécutifs**. Cependant, la **rupture de stabilité du consensus** (PT $235.2 vs $251.50, 5 analysts vs 4) et la **mutation inverse des options** (max_pain 180.0, put/call 0.36, call OI 73.5%) rappellent que le mapping FMP reste instable. Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et métriques stables avant toute réévaluation opérationnelle.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **167,066,800** | 🔴 Extrême anomalie | Faux volume stable ~167M, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🟡 Mutation inverse | — | `max_pain` = 180.0 (was 162.5), `put_call_ratio` = 0.36 (was `null`), `call_oi_pct` = 73.5% (was `null`) |
| Révisions consensus | 🔴 Stabilité rompue | — | PT $235.2 (was $251.50), 5 analysts (was 4) |
| Float FMP | 281,190,750 | 🟢 Stabilisation confirmée (5e snapshot) | Inchangé depuis 13h 22/06 |
| Faux −16.43% | −16.43% | 🔴 Mouvement fictif figé | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | Aucun warning SPCX | 🟢 Cohérent | Cohérence maintenue entre validation report et `latest.json` |
| DRAFT_refresh | Déclenché | 🔴 Faux positif | `PRICE_GAP` −16.43% déclenchement mécanique sur faux prix — archivé avec mutations secondaires notées |

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
| Consensus FMP stable (PT et nb analysts constants sur 3+ snapshots) | 1–3j | Mapping symbole stabilisé | Si consensus mute → méfiance |
| Forward P/E FMP stable (arrêt des mutations > ±10%) | 1–3j | Métrique fondamentale stabilisée | Si forward P/E mute → data quality irréparable |
| Séquence de 5+ snapshots avec mutations FMP stables | 2–3j | Début de confiance dans le mapping | Si reprise de la mutation → retour méfiance |
| Float FMP stable sur 7+ snapshots | 2–3j | Seul champ fiable potentiel | Si float mute → ÉVITER |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 10h UTC 2026-06-23
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ATTENDRE (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — maintien agent non fondé sur amélioration data quality)
- Raison principale : Snapshot 13h UTC 23/06 : conflit de symbole FMP chronique persistant — faux prix $154.60 stable (−16.43% vs previous close $185.00), faux OHLC $154.00–$176.75, faux market cap $2.04T, forward P/E 786.09 stable, sector Industrials/Aerospace & Defense, volume fictif stable 167.07M (0.62×). **Mutation consensus FMP** : PT $251.50 → $235.2 (−6.5%), num analysts 4 → 5 (rupture stabilité 4 snapshots). **Mutation inverse des options** : max_pain 162.5 → 180.0, put/call ratio `null` → 0.36, call OI `null` → 73.5%. **Float FMP stable sur 5 snapshots consécutifs** : 281.2M (inchangé depuis 13h UTC 22/06). Scoring agent stable ATTENDRE 56.0/100 : Score Opportunité 5.6/10 (C:8.0 V:4.5 M:4.0), Score Valorisation 4.5/10, Score Catalyseur 8.0/10, Score Momentum 4.0/10. Sector rotation stable (NEUTRAL, 11/11 secteurs OK, XLK momentum 10.0, XLF momentum 5.45). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 23/06 ignoré. Validation report cohérent (aucun warning SPCX). DRAFT_refresh déclenché mécaniquement par gap −16.43% (faux prix) — classé faux positif algorithmique avec mutations secondaires notées.
- Thèse : 🟡 **Confirmée en ATTENDRE avec nuance négative** — Score Global stable 56.0/100, conflit de symbole chronique persistant, données totalement non fiables, forward P/E 786.09 stable, faux volume stable 167.07M, setup non-actionnable en pratique. Float stable sur 5 snapshots consécutifs (seule stabilité), mais rupture de stabilité du consensus (PT et nb analysts mutés) et mutation inverse des options (max_pain 180.0, put/call 0.36, call OI 73.5%) rappellent l'instabilité du mapping FMP.
