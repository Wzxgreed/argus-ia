# SPCX — Mise à jour post-pipeline 2026-06-17 (snapshot 13h UTC)

**Date :** 2026-06-17
**Type :** Mise à jour post-pipeline — snapshot 13h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-17

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 17/06) | Actuel (13h UTC 17/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$201.80** | **$201.80** | = |
| Previous close | $192.50 | $192.50 | = |
| Change % | +4.83% | **+4.83%** | = |
| Open / High / Low | $200.51 / $225.64 / $195.13 | **$200.51 / $225.64 / $195.13** | = |
| Volume | 322,149,300 | **322,149,300** | = |
| Volume vs moy. 20j | 0.88× (365.9M) | **0.88× (365.9M)** | = |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM50j | N/A | N/A | = |
| 52w high | $225.64 | **$225.64** | = |
| 52w low | $149.34 | **$149.34** | = |
| Market cap (fundamentals) | $2,658.55B | **$2,658.55B** | = |
| Market cap (fmp_key_metrics) | $1,585.46B | **$1,585.46B** | = |
| Forward P/E | −2,242.2 | **−2,242.2** | = |
| Price-to-book (fundamentals) | 33.88 | **33.88** | = |
| Shares outstanding | 7,571,396,888 | **7,571,396,888** | = |
| Options max_pain | 25.0 | **210.0** | 🔴 **Mutation options majeure** |
| Options put/call ratio | null | **0.66** | 🔴 Nouvelle anomalie |
| Options call OI % | null | **60.3%** | 🔴 Nouvelle anomalie |
| Recommandation agent | **ÉVITER** | **ÉVITER** | = **Maintien** |
| Score Opportunité | 2.0/10 | **2.0/10** | = |
| Score Catalyseur | 5.5/10 | **5.5/10** | = |
| Score Valorisation | 2.0/10 | **2.0/10** | = — seuil disqualification atteint |
| Score Momentum | 5.5/10 | **5.5/10** | = |
| **Score Global** | 20.0/100 | **20.0/100** | = 🔴 **ÉVITER maintenu** |
| **Score Global Ajusté** | 20.0/100 | **20.0/100** | = |
| Timing | Neutre | **Neutre** | = |
| Validation report | `[WARNING] volume is 0` | **Aucun warning** | 🟢 **Résolue** |

**Verdict :** Stabilité mécanique totale entre les snapshots 10h et 13h UTC sur le cours, le volume et les métriques fondamentales. Le conflit de symbole FMP persiste avec le **faux prix $201.80** (+4.83% vs previous close $192.50), le faux market cap **$2.66T** et le forward P/E **−2,242**. Deux évolutions significatives : (1) **résolution de l'anomalie validation report** — le `[WARNING] SPCX: volume is 0` du snapshot 10h a disparu dans le rapport 13h, confirmant que le volume 322.1M est désormais cohérent entre `latest.json` et le module de validation ; (2) **mutation majeure des données options** — `max_pain` est passé de `25.0` (10h) à **210.0** (13h), avec apparition d'un `put_call_ratio` à **0.66** et d'un `call_oi_pct` à **60.3%**. Le niveau 210.0 est désormais proche du faux cours 201.80, suggérant que ces options mutantes sont celles de l'entité étrangère mappée par FMP. L'Agent Recommandation maintient le verdict **ÉVITER 20.0/100** (Score Opportunité 2.0/10). Le secteur reste `Industrials` / `Aerospace & Defense`.

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
| Volume vs moy. 20j | **322.1M / 365.9M** | 🔴 Volume fictif stable, ~0.88× moyenne |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w range | $149.34 – $225.64 | 🔴 Totalement incompatible avec un ETF SPAC |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

> **Note institutionnelle :** Le faux prix $201.80 reste ~9× supérieur aux derniers niveaux connus de SPCX (~$22). Le faux 52w range ($149.34 – $225.64) confirme que FMP mappe SPCX sur une entité large-cap Industrials/Aerospace. Aucun de ces niveaux n'a de pertinence pour l'ETF SPAC. La **mutation options** est particulièrement révélatrice : `max_pain` à 210.0 (vs 25.0 à 10h) est quasi-aligné sur le faux cours 201.80, ce qui confirme que le module options récupère les données de l'**entité étrangère** et non de l'ETF SPAC. Le `put_call_ratio` 0.66 et le `call_oi_pct` 60.3% sont eux aussi ceux de cette entité incorrecte.

**Verdict timing :** Défavorable → **Non-actionnable**. Vingt-neuf snapshots consécutifs sans RSI, ATR, ni MM50 fiables. Le conflit de symbole FMP est **chronique** : prix oscillant entre $135.00 (08/06), $160.95 (15/06), $192.50–$216.94 (16/06), et désormais $201.80 (17/06), toujours pour la même entité incorrecte.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes stables mais toujours fausses :**

| Métrique | Valeur actuelle | Valeur historique (10h 17/06) | Commentaire |
|----------|----------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **−2,242.2** | −2,242.2 | 🔴 Aberrant, impossible |
| Market cap (fundamentals) | **$2,658.55B** | $2,658.55B | = Stable — faux |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable — faux |
| Price-to-book (fundamentals) | **33.88** | 33.88 | = Stable — mécanique sur faux cours |
| Beta | N/A | N/A | Non calculé |
| Shares outstanding | **7,571,396,888** | 7,571,396,888 | = Stable — quantité fictive |
| Shares float | **2,919,745,600** | 2,919,745,600 | = Stable |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$177.50** (stable)
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

> **Note institutionnelle :** L'ensemble des métriques FMP reste strictement celles d'une entité étrangère à l'ETF SPAC. L'absence totale de données sur l'AUM, le NAV premium/discount et le tracking error rend toute analyse fondamentale impossible. La résolution du WARNING validation report (`volume is 0`) est une amélioration mécanique du pipeline, mais ne change pas la nature fictive des données de marché.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-17.json` : 0 item pour SPCX (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-17.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🔴 Anomalie mutante majeure | `max_pain` = **210.0** (was 25.0), `put_call_ratio` = **0.66** (was null), `call_oi_pct` = **60.3%** (was null) — alignement sur entité étrangère |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $177.50, 2 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-17.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-06-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-06-17) : n=0, insuffisant |

**Anomalie data quality — résolution partielle :** Le `[WARNING] SPCX: volume is 0` du snapshot 10h a **disparu** dans le validation report 13h. Cette incohérence interne est résolue : le module de validation confirme désormais le `volume: 322149300` de `latest.json`. Cependant, le volume reste factice pour un ETF SPAC.

**Alerte social sentiment (artefact) :** `data/social_sentiment_latest.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

**Sector rotation — signal NEUTRAL stable :** `data/sector_rotation_2026-06-17.json` signale `NEUTRAL` avec 11/11 secteurs OK. XLK (Technology) domine avec momentum_score 10.0. XLF (Financials) : return_20d +5.04%, rs_20d +3.46%, momentum_score 5.32. Le signal sectoriel est lisible mais n'impacte pas SPCX (absent du ranking sectoriel).

---

## Scoring global (agents pipeline 2026-06-17, snapshot 13h UTC)

| Axe | Score | Changement vs 10h 17/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **5.5/10** | = | Modéré — absence de catalyseur réel |
| Score Valorisation | **2.0/10** | = | 🔴 **Sur le seuil de disqualification (≤ 2/10)** — artefact mécanique |
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
| Volume | 🔴 322.1M unités — volume fictif stable |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données corrompues/mutantes = risque non quantifiable |
| Score Global | 🔴 **20.0/100** → **ÉVITER** (fourchette < 35) |
| Source données | 🔴 **Conflit de symbole chronique** : prix fictif $201.80, sector Industrials/Aerospace & Defense, market cap $2.66T, forward P/E −2,242 |
| Signal sectoriel | 🟡 **NEUTRAL stable** — XLK momentum_score 10.0, XLF momentum_score 5.32, 11/11 secteurs OK |
| Stabilité inter-snapshot | 🟢 Prix stable : $201.80 (10h) → $201.80 (13h) — première stabilité de cours fictif depuis 6 jours |
| Seuil de vigilance | 🔴 Score Valorisation 2.0/10 = **seuil de disqualification atteint** — Score Opportunité également à 2.0/10 |
| Qualité data pipeline | 🟢 `[WARNING] volume is 0` résolu — validation report 13h cohérent avec `latest.json` |
| Options | 🔴 Mutation majeure : max_pain 25.0 → **210.0**, put/call 0.66, call OI 60.3% — alignement sur entité étrangère |

- **Invalidation :** La recommandation **ÉVITER** reste un artefact mécanique — le fondamental (absence totale de données fiables) est identique. Le scoring est **inchangé à 20.0/100**. Aucune donnée réelle n'a changé. Le setup reste totalement non-actionnable.
- **Nuances :** Le snapshot 13h UTC du 17/06 montre une **stabilité mécanique totale** du faux cours ($201.80 inchangé), du volume (322.1M) et du market cap ($2.66T). Après plusieurs jours de mutation volatile ($160.95 → $179.26 → $192.50 → $216.94 → $201.80), le prix fictif s'est stabilisé sur deux snapshots consécutifs (10h et 13h). Cependant, la **mutation options est plus inquiétante** : `max_pain` est passé de `null` (15/06) à `25.0` (10h 17/06) puis **210.0** (13h 17/06). Le niveau 210.0 est quasi-aligné sur le faux cours 201.80, ce qui confirme que les flux options proviennent de l'**entité étrangère mappée par FMP** et non de l'ETF SPAC. Le `put_call_ratio` 0.66 et le `call_oi_pct` 60.3% sont eux aussi ceux de cette entité. Le module sector rotation est stable (NEUTRAL, 11/11 OK). L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée. Le faux événement FMP `earnings` du 17/06 est un artefact récurrent et ignoré. Le validation report est désormais **cohérent** (WARNING volume résolu).
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 50/100 relancerait le setup en ATTENDRE. Tant que le prix oscille entre des valeurs fictives ($135–$225) ou que les options mutent de manière erratique, aucune action n'est justifiable.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ÉVITER** (artefact). Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER** fondé sur données réelles. Si le faux prix reprend sa volatilité mutante ou si les options continuent de diverger → **ÉVITER** pour cause de data quality irréparable.

**Recommandation :** **ÉVITER** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur vingt-neuf snapshots consécutifs. Le flux Yahoo est totalement indisponible (RSI/ATR/MM50 null) et FMP continue de renvoyer les données d'une entité étrangère en mutation (prix fictif $201.80, sector Industrials/Aerospace & Defense, market cap $2.66T, options mutantes max_pain 210.0). Attendre un snapshot avec prix confirmé, sector correct (`Financial Services`), volume > 0 et options cohérentes avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **322,149,300** | 🔴 Extrême anomalie | Faux volume stable vs 10h, toujours astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 Anomalie mutante majeure | — | `max_pain` = 210.0 (was 25.0 à 10h), `put_call_ratio` 0.66, `call_oi_pct` 60.3% — alignement sur entité étrangère |
| Révisions consensus | 🔴 Anomalie | — | PT $177.50 et 2 analysts — non applicable à un ETF, artefact FMP |
| Faux +4.83% | +4.83% | 🔴 Mouvement fictif | Correspond à l'entité étrangère mappée par FMP, pas à SPCX |
| Validation report | **Aucun warning** | 🟢 Résolu | Cohérence restaurée entre validation report et `latest.json` |

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
| Options stables et cohérentes (max_pain proche du vrai cours ~$22) | 1–3j | Confiance data restaurée | Si max_pain continue de muter → méfiance |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 10h UTC 2026-06-17
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours fictif)
- Recommandation précédente : ÉVITER (artefact mécanique)
- Recommandation révisée : **ÉVITER** (artefact mécanique — fondamentalement non-actionnable)
- Raison principale : Snapshot 13h UTC 17/06 : stabilité mécanique totale vs 10h (prix $201.80, volume 322.1M, market cap $2.66T inchangés). Conflit de symbole FMP chronique persistant. Résolution de l'anomalie validation report (`WARNING volume is 0` disparu). Mutation majeure des données options : max_pain 25.0 → 210.0 (alignement sur entité étrangère), put/call ratio 0.66, call OI 60.3%. Scoring agent inchangé ÉVITER 20.0/100 : Score Opportunité 2.0/10, Score Valorisation 2.0/10 (seuil disqualification atteint), Score Catalyseur 5.5/10. Sector rotation stable (NEUTRAL, 11/11 secteurs OK, XLK momentum 10.0, XLF momentum 5.32). Aucun catalyseur ni news. Alerte social EXTREME_BEARISH ignorée (artefact). Faux earnings FMP du 17/06 ignoré.
- Thèse : 🔴 **Invalidée** — maintien ÉVITER (Score Global 20.0/100), conflit de symbole chronique, données totalement non fiables, mutation options majeure détectée, cohérence validation report restaurée
