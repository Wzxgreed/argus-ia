# SPCX — Mise à jour post-pipeline 2026-06-23 (snapshot 17h UTC)

**Date :** 2026-06-23
**Type :** Mise à jour post-pipeline — snapshot 17h UTC
**Analyse précédente :** snapshot 13h UTC 2026-06-23

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (13h UTC 23/06) | Actuel (17h UTC 23/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$154.60** | **$163.24** | 🔴 **+5.59% — mutation mécanique du faux prix** |
| Previous close | $185.00 | **$154.60** | 🔴 Référence mise à jour mécaniquement |
| Change % | −16.43% | **+5.59%** | 🔴 Inversion mécanique totale |
| Open / High / Low | $176.04 / $176.75 / $154.00 | **$151.03 / $165.50 / $147.11** | 🔴 Nouveaux faux OHLC |
| Volume | 167,066,800 | **116,665,263** | 🔴 **−30.1%** (faux volume en baisse) |
| Volume vs moy. 20j | 0.62× (268.6M) | **0.47× (246.9M)** | 🔴 Faux volume plus faible |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high / low | $225.64 / $149.34 | $225.64 / **$147.11** | 🟡 Nouveau faux 52w low |
| Market cap (fundamentals) | $2,036.73B | **$2,150.55B** | 🔴 +5.59% (mécanique) |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = **Stable (2e snapshot)** |
| Forward P/E | 786.09 | **830.02** | 🔴 +5.59% (mécanique) |
| Price-to-book (fundamentals) | 25.96 | **27.41** | 🔴 +5.59% (mécanique) |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = |
| Shares float | 281,190,750 | **281,190,750** | 🟢 **Stable (6e snapshot consécutif)** |
| Options max_pain | 180.0 | **180.0** | 🟢 **Stable (2e snapshot)** |
| Options put/call ratio | 0.36 | **0.36** | 🟢 **Stable (2e snapshot)** |
| Options call OI % | 73.5% | **73.5%** | 🟢 **Stable (2e snapshot)** |
| FMP consensus PT | $235.2 (5 analysts) | **$235.2 (5 analysts)** | 🟢 **Stable (2e snapshot)** |
| FMP consensus low/high | `null` / `null` | `null` / `null` | = |
| Recommandation agent | **ATTENDRE** | **ATTENDRE** | = |
| Score Opportunité | 5.6/10 | **6.0/10** | 🔴 **+0.4 pt** |
| Score Catalyseur | 8.0/10 | **8.0/10** | = |
| Score Valorisation | 4.5/10 | **4.5/10** | = |
| Score Momentum | 4.0/10 | **5.5/10** | 🟡 **+1.5 pt** (mécanique, lié au faux +5.59%) |
| **Score Global** | 56.0/100 | **59.8/100** | 🟡 **+3.8 pts** — proche seuil ACHETER Réduit (60) |
| **Score Global Ajusté** | 56.0/100 | **59.8/100** | 🟡 +3.8 pts |
| Timing | Neutre | **Neutre** | = |
| Validation report | Aucun warning SPCX | **Aucun warning SPCX** | = |
| Quality gate | ok | **ok** | = |

**Verdict :** Le snapshot 17h UTC du 23/06 montre une **mutation mécanique du faux prix** : le cours fictif passe de $154.60 à **$163.24 (+5.59%)**, entraînant mécaniquement une hausse du Score Global de 56.0 à **59.8/100** (+3.8 pts) et du Score Momentum de 4.0 à **5.5/10** (+1.5 pt). Le ticker reste à **0.2 pt du seuil ACHETER Réduit (60)**. Cependant, cette hausse est **strictement mécanique et non fondamentale** : le prix reste celui d'une entité étrangère mappée par erreur sur le symbole SPCX.

**Nouveauté majeure — stabilisation partielle se confirme :** Pour la **première fois depuis le début du conflit de symbole** (17/06), trois champs FMP clés sont **stables sur deux snapshots consécutifs** :
1. **Consensus FMP** : PT $235.2 et 5 analysts — stable sur 2 snapshots (13h → 17h)
2. **Options FMP** : max_pain 180.0, put/call 0.36, call OI 73.5% — stable sur 2 snapshots
3. **Float FMP** : 281.2M — stable sur **6 snapshots consécutifs** (record)

Cette stabilisation partielle est **contrebalancée** par la **mutation mécanique du prix** (+5.59%), qui révèle que le mapping FMP reste actif et volatile. Le `market_cap` (fmp_key_metrics) est également stable sur 2 snapshots ($1,585.46B).

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : faux prix muté à $163.24 (+5.59%)**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$163.24** | 🔴 Faux prix FMP — entité étrangère, muté vs 13h |
| Previous close | $154.60 | 🔴 Référence mise à jour mécaniquement |
| Open | $151.03 | 🔴 Faux OHLC muté |
| High | $165.50 | 🔴 Faux high réduit vs $176.75 (13h) |
| Low | $147.11 | 🔴 Nouveau faux low (anciennement $154.00) |
| Change % | **+5.59%** | 🔴 Totalement artificiel — inversion mécanique |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **116.7M / 246.9M** | 🔴 Faux volume en baisse ~0.47× |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $147.11 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $163.24 reste ~7.4× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($147.11 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. Les métriques techniques (RSI, ATR, MM50) restent toutes nulles sur ce snapshot 17h UTC, confirmant l'absence totale de flux Yahoo. Le conflit de symbole FMP est **chronique** : après quarante snapshots consécutifs sans données techniques fiables. La **seule nuance positive** est la **stabilisation partielle** de trois champs FMP (float, consensus, options) sur 2+ snapshots consécutifs.

**Verdict timing :** Neutre → **Non-actionnable**. Quarante snapshots consécutifs sans RSI, ATR, ni MM50 fiables.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes mutées mais cohérentes avec l'entité étrangère :**

| Métrique | Valeur actuelle (17h 23/06) | Valeur historique (13h 23/06) | Commentaire |
|----------|----------------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **830.02** | 786.09 | 🔴 +5.59% — mécanique, lié au faux prix |
| Market cap (fundamentals) | **$2,150.55B** | $2,036.73B | 🔴 +5.59% — mécanique |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = **Stable (2e snapshot)** |
| Price-to-book (fundamentals) | **27.41** | 25.96 | 🔴 +5.59% — mécanique |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | 281,190,750 | 🟢 **Stable (6e snapshot consécutif)** |

**FMP Consensus (stabilisation confirmée) :**
- `price_target_avg`: **$235.2** (was $235.2) — 🟢 **Stable (2e snapshot)**
- `num_analysts`: **5** (was 5) — 🟢 **Stable (2e snapshot)**
- `num_analysts_last_month`: **5** (was 5) — 🟢 Stable
- `num_analysts_last_quarter`: **5** (was 5) — 🟢 Stable
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.24 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 27.41 (fundamentals) — divergence interne persistante
- `price_to_sales`: 25.22 (stable)
- `price_to_fcf`: −33.75 (stable)
- `enterprise_value_multiple`: **369.23** (stable)
- `gross_margin`: 49.39% (stable)
- `operating_margin`: −13.86% (stable)
- `net_margin`: −26.44% (stable)

**FMP Key Metrics (stables mais faux) :**
- `market_cap`: $1,585.46B (stable — 2e snapshot)
- `enterprise_value`: $1,583.61B (stable)
- `ev_to_sales`: 84.80 (stable)
- `ev_to_ebitda`: 369.23 (stable)
- `net_debt_to_ebitda`: −0.43 (stable)
- `return_on_equity`: −11.95% (stable)

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.15T) et fmp_key_metrics ($1.59T) persiste mais les deux champs sont désormais stables sur 2 snapshots (fmp_key_metrics). L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La **stabilisation du float** (281.2M) sur six snapshots consécutifs est la séquence la plus longue observée. La **stabilisation du consensus** (PT $235.2, 5 analysts) et des **options** (max_pain 180.0, put/call 0.36, call OI 73.5%) sur deux snapshots consécutifs est une **première** depuis le début du conflit (17/06). Cependant, le prix a muté (+5.59%), ce qui signifie que le mapping reste actif et que l'entité étrangère est en mouvement.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-23.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-23.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🟢 **Stabilisation confirmée** | `max_pain` = **180.0** (stable), `put_call_ratio` = **0.36** (stable), `call_oi_pct` = **73.5%** (stable) |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $235.2, 5 analysts), **stable 2e snapshot** |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-23.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_2026-06-23.json` : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_2026-06-23.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_2026-06-23.json` : n=0, insuffisant |

**Anomalie data quality — résolution maintenue :** Le `[WARNING] SPCX: volume is 0` reste absent du validation report 2026-06-23. Le quality gate marque SPCX comme `ok`. Cependant, le volume reste factice pour un ETF SPAC.

**Alerte social sentiment (artefact) :** `data/social_sentiment_2026-06-23.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL avec amélioration XLF :** `data/sector_rotation_2026-06-23.json` signale `NEUTRAL` avec 11/11 secteurs OK. XLK (Technology) domine avec momentum_score 10.0. **XLF (Financials)** : return_20d +4.10%, rs_20d +4.96%, momentum_score **6.23** (vs 5.45 au snapshot 13h — **+0.78 pt**). Le signal sectoriel est lisible et légèrement amélioré mais n'impacte pas directement SPCX (absent du ranking sectoriel).

**Anomalie upcoming events (artefact) :** `data/upcoming_events_2026-06-23.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-23 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. `data/events_2026-06-23.json` : 0 événement corporate réel pour SPCX.

---

## Scoring global (agents pipeline 2026-06-23, snapshot 17h UTC)

| Axe | Score | Changement vs 13h 23/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **8.0/10** | = | Stable — absence de catalyseur réel |
| Score Valorisation | **4.5/10** | = | Stable — proche seuil disqualification |
| Score Momentum | **5.5/10** | 🟡 +1.5 pt | **Mécanique** — lié au faux +5.59% du prix |
| **Score Opportunité** | **6.0/10** | 🟡 +0.4 pt | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **59.8/100** | 🟡 +3.8 pts | **ATTENDRE** (fourchette 50–59) — **à 0.2 pt du seuil ACHETER Réduit (60)** |
| **Score Global Ajusté** | **59.8/100** | 🟡 +3.8 pts | Aucun bonus/malus appliqué |
| Timing | **Neutre** | = | Non actionnable |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel — faux earnings FMP ignoré)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL avec amélioration XLF 6.23 mais sans impact direct sur SPCX)

**Règle de disqualification :** 🟡 **Score Valorisation = 4.5/10** — le seuil de disqualification (≤ 2/10) est dépassé mécaniquement. Le Score Opportunité est à **6.0/10**. L'Agent Recommandation maintient le ticker en **ATTENDRE** à **59.8/100**, soit **0.2 pt sous le seuil ACHETER Réduit (60)**.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | **ATTENDRE** | — | ✅ **SPCX = 59.8** (limite supérieure) |
| 35–49 | SURVEILLER | — | — |
| < 35 | ÉVITER | — | — |

> **Note institutionnelle :** Le maintien en ATTENDRE 59.8/100 est **purement mécanique** et non fondé sur une amélioration de la qualité data. Le Score Global a grimpé de 56.0 à **59.8** (+3.8 pts) uniquement parce que le **Score Momentum** est passé de 4.0 à **5.5/10** (+1.5 pt), mécaniquement lié à la mutation du faux prix (+5.59%). Les métriques techniques restent toutes nulles, le secteur reste incorrect, et le prix reste fictif. Le setup reste **non-actionnable** en pratique. La seule nuance positive est la **stabilisation partielle confirmée** sur trois fronts : **float** (6 snapshots), **consensus** (2 snapshots) et **options** (2 snapshots).

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours fictif $163.24 — aucune donnée de marché réelle |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable. Le faux cours $163.24 est ~7.4× supérieur à ces niveaux.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **CONFIRMÉE EN ATTENDRE AVEC NUANCE MIXTE** — **Score Global remonté mécaniquement à 59.8/100** (+3.8 pts), **proche du seuil ACHETER Réduit (60)**, mais **qualité data toujours dégradée**. Quarantième snapshot consécutif sans données techniques fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif muté +5.59%) |
| RSI | ❌ Non disponible |
| Volume | 🔴 116.7M unités — faux volume en baisse (~0.47×) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🟡 **59.8/100** → **ATTENDRE** (limite supérieure 50–59) — remontée mécanique |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $163.24, sector Industrials/Aerospace & Defense, market cap $2.15T, forward P/E 830.02 |
| Signal sectoriel | 🟡 **NEUTRAL avec amélioration XLF** — XLK momentum_score 10.0, XLF momentum_score **6.23** (+0.78 vs 13h) |
| Stabilité inter-snapshot | 🟡 Prix muté (+5.59%), mais **float stable sur 6 snapshots**, **consensus stable sur 2 snapshots**, **options stables sur 2 snapshots** |
| Seuil de vigilance | 🟡 Score Valorisation 4.5/10 — seuil de disqualification dépassé mécaniquement ; Score Global à 0.2 pt du seuil ACHETER Réduit |
| Qualité data pipeline | 🟢 Aucun warning SPCX — cohérence validation report / `latest.json` maintenue |
| Options | 🟢 **Stabilisation confirmée** : max_pain 180.0, put/call 0.36, call OI 73.5% — stables sur 2 snapshots |
| Consensus FMP | 🟢 **Stabilisation confirmée** : PT $235.2, 5 analysts — stables sur 2 snapshots |
| Float FMP | 🟢 **Stabilisation confirmée (6e snapshot)** : 281.2M inchangé |
| DRAFT_refresh | 🟡 Non déclenché — pas de trigger PRICE_GAP (−5% ≤ gap ≤ +5%) sur ce snapshot |

- **Confirmation :** L'Agent Recommandation maintient le ticker en **ATTENDRE 59.8/100** avec un Score Opportunité remonté à 6.0/10 (C:8.0 V:4.5 M:5.5). Le timing reste Neutre. Le **float** (281.2M) est **inchangé pour un sixième snapshot consécutif** (13h → 17h → 21h 22/06 → 10h → 13h → 17h 23/06), ce qui est la séquence de stabilité la plus longue observée. Le **consensus FMP** (PT $235.2, 5 analysts) et les **options FMP** (max_pain 180.0, put/call 0.36, call OI 73.5%) sont **stables pour un deuxième snapshot consécutif** — première depuis le début du conflit de symbole (17/06).
- **Nuances négatives :** Le **prix fictif a muté** de $154.60 à **$163.24 (+5.59%)**, entraînant mécaniquement une hausse du Score Global (+3.8 pts) et du Score Momentum (+1.5 pt). Le `previous_close` est passé de $185.00 à **$154.60** (mise à jour mécanique), le `forward P/E` de 786.09 à **830.02**, et le `market_cap` (fundamentals) de $2.04T à **$2.15T** — toutes mutations mécaniques liées au faux prix. Le secteur persiste `Industrials` / `Aerospace & Defense`, les métriques techniques restent nulles. Aucun catalyseur ni news. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 23/06 est un artefact récurrent et ignoré.
- **Nuances positives :** La **stabilisation partielle** est la nouvelle la plus significative depuis des semaines. Le fait que le **consensus**, les **options** et le **float** soient stables sur 2+ snapshots consécutifs suggère que le mapping symbole FMP pourrait être en phase de stabilisation — même si le prix reste celui d'une entité étrangère. Le `market_cap` (fmp_key_metrics) est également stable sur 2 snapshots ($1,585.46B).
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation fiable. Un retour du Score Global au-dessus de 60/100 (seuil ACHETER Réduit) est désormais mécaniquement proche mais **ne doit pas être interprété comme un signal d'achat** tant que le prix reste fictif. Si le mapping FMP se stabilise complètement (prix + sector + toutes métriques stables sur 3+ snapshots) → réévaluation possible.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** (artefact mécanique) ou retour en **SURVEILLER/ÉVITER** si le scoring re-chute sous 50. Si les mutations FMP reprennent sur les champs précédemment stabilisés (consensus, options, float) → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable malgré la remontée mécanique à 59.8/100)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur quarante snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère (prix fictif $163.24, sector Industrials/Aerospace & Defense, market cap $2.15T, forward P/E 830.02, float 281.2M). La **stabilisation partielle** (float 6 snapshots, consensus 2 snapshots, options 2 snapshots) est la première bonne nouvelle depuis le début du conflit, mais le prix a muté (+5.59%), confirmant que le mapping reste actif et volatile. Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et métriques stables avant toute réévaluation opérationnelle.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **116,665,263** | 🔴 Extrême anomalie | Faux volume en baisse ~116.7M, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🟢 Stabilisation | — | `max_pain` = 180.0 (stable), `put_call_ratio` = 0.36 (stable), `call_oi_pct` = 73.5% (stable) |
| Révisions consensus | 🟢 Stabilisation | — | PT $235.2 (stable), 5 analysts (stable) |
| Float FMP | 281,190,750 | 🟢 Stabilisation confirmée (6e snapshot) | Inchangé depuis 13h UTC 22/06 |
| Faux +5.59% | +5.59% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | Aucun warning SPCX | 🟢 Cohérent | Cohérence maintenue entre validation report et `latest.json` |
| DRAFT_refresh | Non déclenché | 🟢 | Pas de trigger PRICE_GAP sur ce snapshot (gap +5.59% dans la fourchette ±5% → non déclenché, ou trigger non actif) |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP corrigées (prix ~$22, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup revalidable en ATTENDRE / ACHETER | Maintien en ATTENDRE / reclassement ÉVITER |
| Volume > 1 000 unités confirmé | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER fondé sur données réelles |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ATTENDRE | — |
| XLF momentum_score > 7.0 + données fiables | 5–10j | Contexte sectoriel favorable | — |
| FMP corrige le mapping symbole (sector = Financial Services, market cap < $1B, float stable) | Variable | Rétablissement data quality | Maintien ATTENDRE / ÉVITER |
| Options stables et cohérentes (max_pain proche du vrai cours ~$22) | 1–3j | Confiance data restaurée | Si max_pain continue de muter → méfiance |
| Consensus FMP stable (PT et nb analysts constants sur 3+ snapshots) | 1–3j | Mapping symbole stabilisé | Si consensus mute → méfiance |
| Float FMP stable sur 8+ snapshots | 2–3j | Seul champ fiable potentiel | Si float mute → ÉVITER |
| Séquence de 3+ snapshots avec consensus + options + float stables | 2–3j | Début de confiance dans le mapping | Si reprise de la mutation → retour méfiance |
| Forward P/E FMP stable (arrêt des mutations > ±10%) | 1–3j | Métrique fondamentale stabilisée | Si forward P/E mute → data quality irréparable |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 13h UTC 2026-06-23
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ATTENDRE (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — remontée mécanique à 59.8/100 non fondée sur amélioration data quality)
- Raison principale : Snapshot 17h UTC 23/06 : conflit de symbole FMP chronique persistant — faux prix muté $154.60 → $163.24 (+5.59%), faux OHLC $147.11–$165.50, faux market cap $2.15T, forward P/E 830.02 (muté +5.59%), sector Industrials/Aerospace & Defense, volume fictif en baisse 116.7M (0.47×). **Stabilisation partielle confirmée** : float 281.2M stable sur 6 snapshots consécutifs, consensus PT $235.2 et 5 analysts stables sur 2 snapshots, options max_pain 180.0 / put_call 0.36 / call OI 73.5% stables sur 2 snapshots. Scoring agent remonté mécaniquement ATTENDRE 59.8/100 : Score Opportunité 6.0/10 (C:8.0 V:4.5 M:5.5), Score Momentum 5.5/10 (+1.5 pt mécanique lié au faux +5.59%), Score Valorisation 4.5/10, Score Catalyseur 8.0/10. Sector rotation NEUTRAL avec amélioration XLF momentum 6.23 (+0.78). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 23/06 ignoré. Validation report cohérent (aucun warning SPCX). DRAFT_refresh non déclenché (pas de trigger PRICE_GAP).
- Thèse : 🟡 **Confirmée en ATTENDRE avec nuance mixte** — Score Global remonté mécaniquement à 59.8/100 (+3.8 pts, à 0.2 pt du seuil ACHETER Réduit 60), conflit de symbole chronique persistant, données totalement non fiables, forward P/E 830.02 muté +5.59%, faux volume en baisse 116.7M, setup non-actionnable en pratique. Stabilisation partielle sans précédent (float 6 snapshots, consensus 2 snapshots, options 2 snapshots) mais prix muté (+5.59%), invalidant toute confiance opérationnelle.
