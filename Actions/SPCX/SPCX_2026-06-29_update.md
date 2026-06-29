# SPCX — Mise à jour post-pipeline 2026-06-29 (snapshot 10h UTC)

**Date :** 2026-06-29
**Type :** Mise à jour post-pipeline — snapshot 10h UTC
**Analyse précédente :** snapshot 17h UTC 2026-06-23

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (17h UTC 23/06) | Actuel (10h UTC 29/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$163.24** | **$153.23** | 🔴 **−6.13%** |
| Previous close | $154.60 | **$153.00** | 🟡 Mécanique |
| Change % | +5.59% | **+0.15%** | 🟡 Normalisation mécanique |
| Open / High / Low | $151.03 / $165.50 / $147.11 | **$150.62 / $158.40 / $148.51** | 🟡 OHLC fictifs resserrés |
| Volume | 116,665,263 | **126,788,200** | 🔴 +8.7% (faux volume) |
| Volume vs moy. 20j | 0.47× (246.9M) | **0.62× (203.5M)** | 🟡 Faux volume vs moyenne 20j |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high / low | $225.64 / $147.11 | $225.64 / **$147.11** | = |
| Market cap (fundamentals) | $2,150.55B | **$2,018.68B** | 🔴 −6.13% (mécanique) |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | 🟢 **Stable (3e snapshot consécutif observé)** |
| Forward P/E | 830.02 | **779.12** | 🟡 −6.13% (mécanique) |
| Price-to-book (fundamentals) | 27.41 | **25.73** | 🟡 −6.13% (mécanique) |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | **281,190,750** | 🟢 **Stable (7e+ snapshot consécutif)** |
| Short interest | N/A | **0.0038%** | 🟢 Apparu (minime) |
| Options max_pain | 180.0 | **5.0** | 🔴 **Mutation majeure** |
| Options put/call ratio | 0.36 | **N/A** | 🔴 Retour à `null` |
| Options call OI % | 73.5% | **N/A** | 🔴 Retour à `null` |
| FMP consensus PT | $235.2 (5 analysts) | **$235.2 (5 analysts)** | 🟢 **Stable (3e+ snapshot consécutif)** |
| FMP consensus low/high | `null` / `null` | `null` / `null` | = |
| Recommandation agent | **ATTENDRE** | **ATTENDRE** | = |
| Score Opportunité | 6.0/10 | **5.8/10** | 🔴 −0.2 pt |
| Score Catalyseur | 8.0/10 | **8.0/10** | = |
| Score Valorisation | 4.5/10 | **4.5/10** | = |
| Score Momentum | 5.5/10 | **5.0/10** | 🔴 **−0.5 pt** (mécanique, lié au −6.13%) |
| **Score Global** | 59.8/100 | **58.5/100** | 🔴 **−1.3 pts** |
| **Score Global Ajusté** | 59.8/100 | **58.5/100** | 🔴 −1.3 pts |
| Timing | Neutre | **Neutre** | = |
| Validation report | Aucun warning SPCX | **Aucun warning SPCX** | = |
| Quality gate | ok | **ok** | = |

**Verdict :** Six jours après le dernier snapshot analysé, le cours fictif FMP a reculé de **$163.24 à $153.23 (−6.13%)**, entraînant mécaniquement une baisse du Score Global de **59.8 à 58.5/100** (−1.3 pt) et du Score Momentum de **5.5 à 5.0/10** (−0.5 pt). Le ticker reste en **ATTENDRE** et s'éloigne du seuil ACHETER Réduit (60). La principale évolution est la **régression des options FMP** : `max_pain` chute de 180.0 à **5.0**, et les ratios `put/call` et `call_oi_pct` retournent à `null`, interrompant la séquence de stabilisation observée sur deux snapshots.

---

## Mise à jour technique

**🔴 [CRITICAL] — Conflit de symbole persistant : faux prix en baisse à $153.23 (−6.13%)**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$153.23** | 🔴 Faux prix FMP — entité étrangère, en baisse vs 23/06 |
| Previous close | $153.00 | 🟡 Référence mécanique |
| Open | $150.62 | 🔴 Faux OHLC resserrés |
| High | $158.40 | 🔴 Faux high réduit vs $165.50 (23/06) |
| Low | $148.51 | 🟡 Proche du faux low $147.11 (23/06) |
| Change % | **+0.15%** | 🟡 Stable intraday, mais −6.13% vs 23/06 |
| RSI 14j | N/A | [DONNÉES MANQUANTES] — cinquantième+ snapshot consécutif |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **126.8M / 203.5M** | 🔴 Faux volume ~0.62× |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $147.11 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $153.23 reste ~7.0× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($147.11 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. Les métriques techniques (RSI, ATR, MM50) restent toutes nulles sur ce snapshot, confirmant l'absence totale de flux Yahoo. Le conflit de symbole FMP est **chronique** : plus de cinquante snapshots consécutifs sans données techniques fiables.

**Verdict timing :** Neutre → **Non-actionnable**.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes en baisse mécanique, cohérentes avec l'entité étrangère :**

| Métrique | Valeur actuelle (29/06) | Valeur historique (23/06) | Commentaire |
|----------|----------------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| Forward P/E | **779.12** | 830.02 | 🟡 −6.13% — mécanique, lié au faux prix |
| Market cap (fundamentals) | **$2,018.68B** | $2,150.55B | 🔴 −6.13% — mécanique |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | 🟢 **Stable (3e snapshot)** |
| Price-to-book (fundamentals) | **25.73** | 27.41 | 🟡 −6.13% — mécanique |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | 7,571,396,888 | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **281,190,750** | 281,190,750 | 🟢 **Stable (7e+ snapshot consécutif)** |
| Short interest | **0.0038%** | N/A | 🟢 Apparu — niveau minime |

**FMP Consensus (stabilisation approfondie) :**
- `price_target_avg`: **$235.2** (was $235.2) — 🟢 **Stable (3e+ snapshot consécutif)**
- `num_analysts`: **5** (was 5) — 🟢 Stable
- `num_analysts_last_month`: **5** (was 5) — 🟢 Stable
- `num_analysts_last_quarter`: **5** (was 5) — 🟢 Stable
- Source : TheFly

**FMP Ratios (globalement stables) :**
- `price_to_earnings`: −95.24 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 25.73 (fundamentals) — divergence interne persistante
- `price_to_sales`: 25.22 (stable)
- `price_to_fcf`: −33.75 (stable)
- `enterprise_value_multiple`: **369.23** (stable)
- `gross_margin`: 49.39% (stable)
- `operating_margin`: −13.86% (stable)
- `net_margin`: −26.44% (stable)

**FMP Key Metrics (stables mais faux) :**
- `market_cap`: $1,585.46B (stable — 3e snapshot)
- `enterprise_value`: $1,583.61B (stable)
- `ev_to_sales`: 84.80 (stable)
- `ev_to_ebitda`: 369.23 (stable)
- `net_debt_to_ebitda`: −0.43 (stable)
- `return_on_equity`: −11.95% (stable)

> **Note institutionnelle :** La divergence interne entre market cap fundamentals ($2.02T) et fmp_key_metrics ($1.59T) persiste mais le champ fmp_key_metrics est désormais stable sur trois snapshots observés. L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La **stabilisation du float** (281.2M) sur sept+ snapshots consécutifs est la séquence la plus longue observée. La **stabilisation du consensus** (PT $235.2, 5 analysts) sur trois+ snapshots consécutifs est maintenant confirmée. Cependant, la **régression des options** (`max_pain` 180.0 → **5.0**, retour à `null` sur put/call et call OI) interrompt la séquence de stabilité et signale que le mapping FMP reste actif et volatile.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-29.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-29.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🔴 **Régression majeure** | `max_pain` = **5.0** (was 180.0), `put_call_ratio` = **null** (was 0.36), `call_oi_pct` = **null** (was 73.5%) |
| Short interest | 🟢 Minime | 0.0038% — nouveau mais sans signification |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $235.2, 5 analysts), **stable 3e+ snapshot** |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-29.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_2026-06-29.json` : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_2026-06-29.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_2026-06-29.json` : n=0, insuffisant |

**Anomalie data quality — résolution maintenue :** Le `[WARNING] SPCX: volume is 0` reste absent du validation report 2026-06-29. Le quality gate marque SPCX comme `ok`. Cependant, le volume reste factice pour un ETF SPAC.

**Alerte social sentiment (artefact) :** `data/social_sentiment_2026-06-29.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL avec nette amélioration XLF :** `data/sector_rotation_2026-06-29.json` signale `NEUTRAL` avec 11/11 secteurs OK. **XLF (Financials)** : return_20d +4.85%, rs_20d +8.00%, momentum_score **8.40** (vs **6.23** au snapshot 23/06 — **+2.17 pts**). Le signal sectoriel financier est désormais le **#4 sector** avec un momentum solide, ce qui est théoriquement favorable à l'univers SPAC/ETF (Financial Services). Cependant, sans données fiables sur SPCX, cet alignement macro reste non exploitable.

**Anomalie upcoming events (artefact) :** `data/upcoming_events_2026-06-29.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-29 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. `data/events_2026-06-29.json` : 0 événement corporate réel pour SPCX.

---

## Scoring global (agents pipeline 2026-06-29, snapshot 10h UTC)

| Axe | Score | Changement vs 23/06 17h | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **8.0/10** | = | Stable — absence de catalyseur réel |
| Score Valorisation | **4.5/10** | = | Stable — proche seuil disqualification |
| Score Momentum | **5.0/10** | 🔴 −0.5 pt | **Mécanique** — lié au −6.13% du faux prix |
| **Score Opportunité** | **5.8/10** | 🔴 −0.2 pt | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **58.5/100** | 🔴 −1.3 pts | **ATTENDRE** (fourchette 50–59) — **s'éloigne du seuil ACHETER Réduit (60)** |
| **Score Global Ajusté** | **58.5/100** | 🔴 −1.3 pts | Aucun bonus/malus appliqué |
| Timing | **Neutre** | = | Non actionnable |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel — faux earnings FMP ignoré)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL avec XLF momentum 8.40 — +2.17 pts vs 23/06, mais sans impact direct sur SPCX faute de données fiables)

**Règle de disqualification :** 🟡 **Score Valorisation = 4.5/10** — le seuil de disqualification (≤ 2/10) est dépassé mécaniquement. Le Score Opportunité est à **5.8/10**. L'Agent Recommandation maintient le ticker en **ATTENDRE 58.5/100**.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | **ATTENDRE** | — | ✅ **SPCX = 58.5** |
| 35–49 | SURVEILLER | — | — |
| < 35 | ÉVITER | — | — |

> **Note institutionnelle :** Le maintien en ATTENDRE 58.5/100 est **purement mécanique** et non fondé sur une amélioration de la qualité data. Le Score Global a reculé de 59.8 à **58.5** (−1.3 pt) parce que le **Score Momentum** est passé de 5.5 à **5.0/10** (−0.5 pt), mécaniquement lié à la baisse du faux prix (−6.13%). Les métriques techniques restent toutes nulles, le secteur reste incorrect, et le prix reste fictif. Le setup reste **non-actionnable** en pratique. La seule nuance positive est la **stabilisation approfondie** du **float** (7+ snapshots) et du **consensus** (3+ snapshots), contrecarrée par la **régression des options** (max_pain 5.0, retour à `null`).

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours fictif $153.23 — aucune donnée de marché réelle |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable. Le faux cours $153.23 est ~7.0× supérieur à ces niveaux.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **CONFIRMÉE EN ATTENDRE AVEC NUANCE MIXTE** — **Score Global reculé mécaniquement à 58.5/100** (−1.3 pt), **s'éloignant du seuil ACHETER Réduit (60)**, et **qualité data toujours dégradée**. Cinquantième+ snapshot consécutif sans données techniques fiables, conflit de symbole FMP **chronique**.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix fictif $153.23) |
| RSI | ❌ Non disponible |
| Volume | 🔴 126.8M unités — faux volume stable à très élevé |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🟡 **58.5/100** → **ATTENDRE** (limite supérieure 50–59) — recul mécanique |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $153.23, sector Industrials/Aerospace & Defense, market cap $2.02T, forward P/E 779.12 |
| Signal sectoriel | 🟡 **NEUTRAL avec nette amélioration XLF** — XLK momentum_score 10.0, XLF momentum_score **8.40** (+2.17 vs 23/06) |
| Stabilité inter-snapshot | 🟡 Prix muté (−6.13%), mais **float stable sur 7+ snapshots**, **consensus stable sur 3+ snapshots** ; **options régressées** (max_pain 5.0, retour `null`) |
| Seuil de vigilance | 🟡 Score Valorisation 4.5/10 — seuil de disqualification dépassé mécaniquement ; Score Global à 1.5 pt du seuil ACHETER Réduit |
| Qualité data pipeline | 🟢 Aucun warning SPCX — cohérence validation report / `latest.json` maintenue |
| Options | 🔴 **Régression** : max_pain 5.0 (was 180.0), put/call `null`, call OI `null` |
| Consensus FMP | 🟢 **Stabilisation approfondie** : PT $235.2, 5 analysts — stables sur 3+ snapshots |
| Float FMP | 🟢 **Stabilisation confirmée (7e+ snapshot)** : 281.2M inchangé |
| DRAFT_refresh | 🟢 Non déclenché — pas de trigger PRICE_GAP (−6.13% hors fourchette ±5%, mais DRAFT non présent) |

- **Confirmation :** L'Agent Recommandation maintient le ticker en **ATTENDRE 58.5/100** avec un Score Opportunité à 5.8/10 (C:8.0 V:4.5 M:5.0). Le timing reste Neutre. Le **float** (281.2M) est **inchangé pour un septième snapshot consécutif** (ou plus), ce qui est la séquence de stabilité la plus longue observée. Le **consensus FMP** (PT $235.2, 5 analysts) est **stable pour un troisième snapshot consécutif** — confirmation de la tendance de stabilisation.
- **Nuances négatives :** Le **prix fictif a reculé** de $163.24 à **$153.23 (−6.13%)**, entraînant mécaniquement une baisse du Score Global (−1.3 pt) et du Score Momentum (−0.5 pt). Le `forward P/E` de 779.12 et le `market_cap` (fundamentals) de $2.02T ont tous deux reculé mécaniquement avec le prix. Le secteur persiste `Industrials` / `Aerospace & Defense`, les métriques techniques restent nulles. Aucun catalyseur ni news. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 29/06 est un artefact récurrent et ignoré. La **principale dégradation** est la **régression des options FMP** : le `max_pain` est passé de 180.0 à **5.0**, et les champs `put_call_ratio` / `call_oi_pct` sont retournés à `null` — interruption de la séquence de stabilité observée sur deux snapshots.
- **Nuances positives :** La **stabilisation approfondie** du **float** et du **consensus** sur 3+ snapshots consécutifs est la bonne nouvelle la plus significative. Le `market_cap` (fmp_key_metrics) est également stable sur 3 snapshots ($1,585.46B). L'amélioration sectorielle XLF (momentum_score 8.40, +2.17 pts) est théoriquement favorable à l'univers SPAC/Financial Services, bien que non exploitable sans données fiables sur SPCX.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation fiable. Un retour du Score Global au-dessus de 60/100 (seuil ACHETER Réduit) est mécaniquement possible si le faux prix remonte, mais **ne doit pas être interprété comme un signal d'achat** tant que le prix reste fictif. Si le mapping FMP se stabilise complètement (prix + sector + toutes métriques stables sur 3+ snapshots) et que les options redeviennent cohérentes → réévaluation possible.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** (artefact mécanique) ou retour en **SURVEILLER/ÉVITER** si le scoring re-chute sous 50. Si les mutations FMP reprennent sur les champs précédemment stabilisés (consensus, float) ou si les options continuent de muter → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable malgré la stabilisation partielle)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur cinquante+ snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère (prix fictif $153.23, sector Industrials/Aerospace & Defense, market cap $2.02T, forward P/E 779.12, float 281.2M). La **stabilisation du float et du consensus** (3+ snapshots) est confirmée, mais la **régression des options** (max_pain 5.0, retour `null`) interrompt la progression. L'amélioration sectorielle XLF (8.40) est non exploitable. Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et métriques stables avant toute réévaluation opérationnelle.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **126,788,200** | 🔴 Extrême anomalie | Faux volume stable ~126.8M, toujours astronomique pour un ETF SPAC |
| Short interest | **0.0038%** | 🟢 Minime | Données apparues mais sans signification opérationnelle |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 **Régression** | — | `max_pain` = 5.0 (was 180.0), `put_call_ratio` = `null`, `call_oi_pct` = `null` |
| Révisions consensus | 🟢 Stabilisation | — | PT $235.2 (stable), 5 analysts (stable) |
| Float FMP | 281,190,750 | 🟢 Stabilisation confirmée (7e+ snapshot) | Inchangé depuis le snapshot 13h UTC 22/06 |
| Faux −6.13% | −6.13% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | Aucun warning SPCX | 🟢 Cohérent | Cohérence maintenue entre validation report et `latest.json` |
| DRAFT_refresh | Non déclenché | 🟢 | Pas de trigger PRICE_GAP actif sur ce snapshot |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP corrigées (prix ~$22, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup revalidable en ATTENDRE / ACHETER | Maintien en ATTENDRE / reclassement ÉVITER |
| Volume > 1 000 unités confirmé | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER fondé sur données réelles |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ATTENDRE | — |
| XLF momentum_score > 8.0 + données fiables | 5–10j | Contexte sectoriel favorable | — |
| FMP corrige le mapping symbole (sector = Financial Services, market cap < $1B, float stable) | Variable | Rétablissement data quality | Maintien ATTENDRE / ÉVITER |
| Options redeviennent stables (max_pain cohérent, put/call et call OI non-null) | 1–3j | Confiance data restaurée | Si options continuent de muter → méfiance |
| Consensus FMP stable (PT et nb analysts constants sur 5+ snapshots) | 1–3j | Mapping symbole stabilisé | Si consensus mute → méfiance |
| Float FMP stable sur 10+ snapshots | 2–3j | Seul champ fiable potentiel | Si float mute → ÉVITER |
| Séquence de 5+ snapshots avec consensus + float stables | 2–3j | Début de confiance dans le mapping | Si reprise de la mutation → retour méfiance |
| Forward P/E FMP stable (arrêt des mutations > ±10%) | 1–3j | Métrique fondamentale stabilisée | Si forward P/E mute → data quality irréparable |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 17h UTC 2026-06-23
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ATTENDRE (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — recul mécanique à 58.5/100 non fondé sur dégradation data quality)
- Raison principale : Snapshot 10h UTC 29/06 : conflit de symbole FMP chronique persistant — faux prix muté $163.24 → $153.23 (−6.13%), faux OHLC $148.51–$158.40, faux market cap $2.02T, forward P/E 779.12 (muté −6.13%), sector Industrials/Aerospace & Defense, volume fictif 126.8M (0.62×). **Stabilisation approfondie** : float 281.2M stable sur 7+ snapshots consécutifs, consensus PT $235.2 et 5 analysts stables sur 3+ snapshots. **Régression options** : max_pain 180.0 → 5.0, put/call et call OI retournés à `null`. Scoring agent reculé mécaniquement ATTENDRE 58.5/100 : Score Opportunité 5.8/10 (C:8.0 V:4.5 M:5.0), Score Momentum 5.0/10 (−0.5 pt mécanique lié au faux −6.13%), Score Valorisation 4.5/10, Score Catalyseur 8.0/10. Sector rotation NEUTRAL avec nette amélioration XLF momentum 8.40 (+2.17 vs 23/06). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 29/06 ignoré. Validation report cohérent (aucun warning SPCX). DRAFT_refresh non déclenché.
- Thèse : 🟡 **Confirmée en ATTENDRE avec nuance mixte** — Score Global reculé mécaniquement à 58.5/100 (−1.3 pt, s'éloignant du seuil ACHETER Réduit 60), conflit de symbole chronique persistant, données totalement non fiables, forward P/E 779.12 muté −6.13%, faux volume stable 126.8M, setup non-actionnable en pratique. Stabilisation approfondie float/consensus (7+/3+ snapshots) mais régression options majeure (max_pain 5.0, retour `null`). Amélioration sectorielle XLF non exploitable.
