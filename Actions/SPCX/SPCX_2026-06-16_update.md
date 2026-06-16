# SPCX — Mise à jour post-pipeline 2026-06-16 (snapshot 10h UTC)

**Date :** 2026-06-16
**Type :** Mise à jour post-pipeline — snapshot 10h UTC
**Analyse précédente :** snapshot 21h UTC 2026-06-15

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (21h UTC 15/06) | Actuel (10h UTC 16/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$192.50** | **NaN** | 🔴 Perte totale du flux prix |
| Previous close | $160.95 | **$160.95** | = (rétrogradé — ancien previous_close devenu référence) |
| Volume | 144,177,048 | **243,783,175** | = (identique au snapshot 21h) |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| Recommandation agent | **SURVEILLER** | **SURVEILLER** | = |
| Score Opportunité | 4.5/10 | **4.7/10** | +0.2 (artefact) |
| Score Catalyseur | 5.5/10 | **6.5/10** | +1.0 (artefact) |
| Score Valorisation | 3.0/10 | **3.0/10** | = |
| Score Momentum | 5.5/10 | **5.0/10** | −0.5 |
| **Score Global Ajusté** | **45.0/100** | **47.2/100** | +2.2 (artefact) |
| Timing | Neutre | Neutre | = |

**Verdict :** Vingt-sixième snapshot consécutif sans données fiables. Le **cours fictif $192.50 a disparu au profit d'un NaN** dans le bloc `price.close`, confirmant la perte totale du flux de prix Yahoo pour SPCX. Le volume reste figé à **243,783,175** unités (identique au snapshot 21h UTC 15/06). Les métriques FMP aberrantes (forward P/E −2,139, market cap $2.52T, sector `Industrials` / `Aerospace & Defense`) restent inchangées. L'Agent Recommandation maintient **SURVEILLER** avec un Score Global Ajusté de **47.2/100** (vs 45.0 précédemment) — cette remontée mécanique de +2.2 pts est un **artefact algorithmique** sans fondement data, puisque la qualité des données s'est encore dégradée (perte du prix de clôture).

---

## Mise à jour technique

**🔴 [CRITICAL] — Anomalie data quality aggravée : perte totale du prix de clôture**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **NaN** | 🔴 Flux Yahoo totalement indisponible — plus aucun prix retourné |
| Previous close | $160.95 | 🔴 Rétrogradation mécanique (ancien previous_close du 15/06) |
| Open / High / Low | NaN / NaN / NaN | 🔴 OHLC totalement absent |
| Change % | NaN | 🔴 Non calculable |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **243,783,175 / 381,508,987** | 🔴 Volume figé à niveau astronomique, identique au snapshot 21h |
| ATR 14j | N/A | Volatilité non mesurable |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Défavorable → **Non-actionnable**. Vingt-sixième snapshot consécutif sans RSI, ATR, ni MM50 fiables. La disparition du cours fictif $192.50 au profit d'un NaN est une aggravation technique : le pipeline ne récupère plus aucun prix de clôture, même erroné. Le volume figé à 243M sur deux snapshots consécutifs confirme que ces données sont issues d'un ticker fantôme et non de l'ETF SPCX.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes figées :**

| Métrique | Valeur actuelle | Valeur historique (21h 15/06) | Commentaire |
|----------|----------------|----------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **−2,138.89** | −2,138.89 | = Stable — absurde |
| Market cap (fundamentals) | **$2,519.99B** | $2,519.99B | = Stable — divergence interne persistante |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable |
| Price-to-book (fundamentals) | **32.32** | 32.32 | = Stable — mécanique sur faux cours |
| Beta | N/A | N/A | Non calculé |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$177.50** (stable vs 21h)
- `num_analysts`: **2** (stable vs 21h)
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.39 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 32.32 (fundamentals) — divergence interne persistante
- `price_to_sales`: 25.22 (stable)
- `price_to_fcf`: −33.75 (stable)
- `enterprise_value_multiple`: **369.23** (stable)
- `gross_margin`: 49.39% (stable)
- `operating_margin`: −13.86% (stable)
- `net_margin`: −26.44% (stable)

> **Note institutionnelle :** Toutes les métriques FMP sont strictement identiques au snapshot 21h UTC 15/06. Le conflit de symbole n'a pas évolué — SPCX reste mappé sur une entité totalement étrangère à l'ETF Tuttle SPAC & New Issue. La remontée mécanique du Score Global de 45.0 à 47.2/100 est un artefact algorithmique sans corrélation avec une quelconque amélioration des données.

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

**Sector rotation — dégradation majeure :** `data/sector_rotation_2026-06-16.json` signale `NEUTRAL` mais avec **NaN massifs** : returns 20j/60j absents pour 9 des 11 secteurs (seuls XLRE et XLC ont des returns). Tous les `momentum_score` sont figés à 10.0 (artefact). Le signal sectoriel est donc totalement non fiable aujourd'hui.

---

## Scoring global (agents pipeline 2026-06-16, snapshot 10h UTC)

| Axe | Score | Changement vs 21h 15/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **6.5/10** | +1.0 | Modéré — absence de catalyseur réel, remontée mécanique non justifiée |
| Score Valorisation | **3.0/10** | = | 🔴 Proche seuil disqualification (≤ 2/10) — artefact mécanique |
| Score Momentum | **5.0/10** | −0.5 | Placeholder mécanique, non fondé sur données de marché |
| **Score Opportunité** | **4.7/10** | +0.2 | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **47.2/100** | +2.2 | Avant ajustements — artefact mécanique |
| **Score Global Ajusté** | **47.2/100** | +2.2 | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL corrompu — NaN massifs, momentum figé à 10.0)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé dans le rapport, mais hors fourchette ACHETER.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | ATTENDRE | — | ❌ |
| 35–49 | **SURVEILLER** | — | ✅ **SPCX = 47.2** |
| < 35 | ÉVITER | — | — |

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours NaN — aucune donnée de marché |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🔴 Thèse **CONFIRMÉE** en état **non-actionnable** — maintien mécanique **SURVEILLER** (Score Global 47.2/100), le fondamental n'a pas changé : vingt-sixième snapshot consécutif sans données fiables, conflit de symbole FMP persistant avec métriques aberrantes, et désormais **perte totale du flux prix** (close = NaN).

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix NaN) |
| RSI | ❌ Non disponible |
| Volume | 🔴 243M unités — figé sur deux snapshots, probablement issu du ticker fantôme |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes / corrompues = risque non quantifiable |
| Score Global | 🔴 **47.2/100** → maintien mécanique SURVEILLER (fourchette 35–49) |
| Source données | 🔴 **Conflit de symbole persistant** : SPCX mappé sur `Industrials` / `Aerospace & Defense` avec market cap $2.52T, forward P/E −2,139, consensus $177.50 — prix désormais totalement absent (NaN) |
| Signal sectoriel | 🔴 **NEUTRAL corrompu** — NaN massifs dans sector_rotation, momentum figé à 10.0 pour tous les secteurs |
| Stabilité inter-snapshot | 🔴 Prix fictif $192.50 → NaN (perte totale), volume figé 243M, métriques FMP identiques |
| Seuil de vigilance | 🔴 Score Valorisation 3.0/10 proche du seuil de disqualification (≤ 2/10) — artefact mécanique |

- **Confirmation :** La recommandation **SURVEILLER** est un artefact mécanique — le fondamental (absence totale de données fiables) s'est légèrement aggravé avec la perte du prix de clôture. La remontée du Score Global de 45.0 à 47.2/100 est purement algorithmique et non fondée sur une amélioration des données. Le setup reste totalement non-actionnable.
- **Nuances :** Le snapshot 10h UTC du 16/06 montre une **stabilisation du conflit de symbole dans sa forme la plus dégradée** : plus aucun prix n'est retourné (NaN), les métriques FMP restent figées aux niveaux aberrants du 21h 15/06, et le volume est identique (243M). Le module sector rotation est devenu inutilisable (NaN massifs). Le faux événement FMP `earnings` du 16/06 est un artefact récurrent et ignoré. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHENTER.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **SURVEILLER** puis reclassement **ÉVITER**. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER**.

**Recommandation :** **SURVEILLER** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours NaN)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur vingt-six snapshots consécutifs. Le flux Yahoo est totalement indisponible (NaN) et FMP continue de renvoyer les données d'une entité étrangère (conflit de symbole persistant). Attendre un snapshot avec prix confirmé, sector correct et volume > 0 avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **243,783,175** | 🔴 Extrême anomalie | Figé sur deux snapshots consécutifs, astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 Anomalie persistante | — | `max_pain` null, `put_call_ratio` null, `call_oi_pct` null — perte totale du flux options |
| Révisions consensus | 🔴 Anomalie | — | PT $177.50 et 2 analysts — non applicable à un ETF, artefact FMP |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP corrigées (prix ~$22, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup revalidable en ATTENDRE | Maintien en SURVEILLER / reclassement ÉVITER |
| Volume > 1 000 unités confirmé | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ACHENTER | — |
| XLF momentum_score > 6.0 + données fiables | 5–10j | Contexte sectoriel favorable | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 21h UTC 2026-06-15
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours NaN)
- Recommandation précédente : SURVEILLER (artefact mécanique)
- Recommandation révisée : **SURVEILLER** (artefact mécanique — fondamentalement non-actionnable)
- Raison principale : Snapshot 10h UTC 16/06 : conflit de symbole FMP persistant (sector Industrials/Aerospace & Defense, forward P/E −2,138, market cap $2.52T), prix passé de $192.50 fictif à NaN (perte totale du flux Yahoo), volume figé 243M sur deux snapshots, métriques FMP identiques au 21h 15/06. Scoring mécanique remonté 45.0→47.2/100 (artefact : Score Catalyseur 5.5→6.5, Score Momentum 5.5→5.0). Sector rotation corrompu (NaN massifs, momentum figé 10.0). Aucun catalyseur ni news. Faux earnings FMP du 16/06 ignoré. Alerte social EXTREME_BEARISH ignorée (artefact).
- Thèse : 🟡 Confirmée (statu quo non-actionnable, aggravation data avec perte totale du prix, maintien mécanique SURVEILLER)
