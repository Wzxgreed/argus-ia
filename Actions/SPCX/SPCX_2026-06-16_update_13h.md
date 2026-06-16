# SPCX — Mise à jour post-pipeline 2026-06-16 (snapshot 13h UTC)

**Date :** 2026-06-16
**Type :** Mise à jour post-pipeline — snapshot 13h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-16

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 16/06) | Actuel (13h UTC 16/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **NaN** | **NaN** | = |
| Previous close | $160.95 | **$160.95** | = |
| Volume | 243,783,175 | **243,783,175** | = |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| Recommandation agent | **SURVEILLER** | **SURVEILLER** | = |
| Score Opportunité | 4.7/10 | **4.7/10** | = |
| Score Catalyseur | 6.5/10 | **6.5/10** | = |
| Score Valorisation | 3.0/10 | **3.0/10** | = |
| Score Momentum | 5.0/10 | **5.0/10** | = |
| **Score Global Ajusté** | **47.2/100** | **47.2/100** | = |
| Timing | Neutre | Neutre | = |

**Verdict :** Vingt-septième snapshot consécutif sans données fiables. Stabilité mécanique totale entre 10h et 13h UTC : le cours reste **NaN**, le volume figé à **243,783,175**, les métriques FMP aberrantes inchangées, et le scoring agent identique (**SURVEILLER 47.2/100**). Aucune mutation technique, fondamentale ni sentimentale sur ce snapshot.

---

## Mise à jour technique

**🔴 [CRITICAL] — Anomalie data quality stable : perte totale du flux prix persistante**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **NaN** | 🔴 Flux Yahoo totalement indisponible |
| Previous close | $160.95 | 🔴 Rétrogradation mécanique stable |
| Open / High / Low | NaN / NaN / NaN | 🔴 OHLC totalement absent |
| Change % | NaN | 🔴 Non calculable |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **243,783,175 / 381,508,987** | 🔴 Volume figé à niveau astronomique |
| ATR 14j | N/A | Volatilité non mesurable |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Défavorable → **Non-actionnable**. Vingt-septième snapshot consécutif sans RSI, ATR, ni MM50 fiables. La stabilité mécanique totale (NaN persistant, volume identique, métriques FMP figées) confirme que le pipeline n'a accès à aucune source de prix fiable pour SPCX depuis le 1er juin 2026.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Métriques aberrantes strictement identiques au snapshot 10h :**

| Métrique | Valeur actuelle | Valeur historique (10h 16/06) | Commentaire |
|----------|----------------|------------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **−2,138.89** | −2,138.89 | = Stable — absurde |
| Market cap (fundamentals) | **$2,519.99B** | $2,519.99B | = Stable — divergence interne persistante |
| Market cap (fmp_key_metrics) | **$1,585.46B** | $1,585.46B | = Stable |
| Price-to-book (fundamentals) | **32.32** | 32.32 | = Stable — mécanique sur faux cours |
| Beta | N/A | N/A | Non calculé |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$177.50** (stable vs 10h)
- `num_analysts`: **2** (stable vs 10h)
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

> **Note institutionnelle :** Toutes les métriques FMP sont strictement identiques au snapshot 10h UTC 16/06. Le conflit de symbole n'a pas évolué — SPCX reste mappé sur une entité totalement étrangère à l'ETF Tuttle SPAC & New Issue. Le Score Global 47.2/100 est inchangé et demeure un artefact algorithmique sans corrélation avec une quelconque amélioration des données.

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

**Sector rotation — dégradation majeure stable :** `data/sector_rotation_2026-06-16.json` signale `NEUTRAL` mais avec **NaN massifs** : returns 20j/60j absents pour 9 des 11 secteurs (seuls XLRE et XLC ont des returns). Tous les `momentum_score` sont figés à 10.0 (artefact). Le signal sectoriel est totalement non fiable aujourd'hui.

---

## Scoring global (agents pipeline 2026-06-16, snapshot 13h UTC)

| Axe | Score | Changement vs 10h 16/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **6.5/10** | = | Modéré — absence de catalyseur réel, score mécanique |
| Score Valorisation | **3.0/10** | = | 🔴 Proche seuil disqualification (≤ 2/10) — artefact mécanique |
| Score Momentum | **5.0/10** | = | Placeholder mécanique, non fondé sur données de marché |
| **Score Opportunité** | **4.7/10** | = | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **47.2/100** | = | Avant ajustements — artefact mécanique |
| **Score Global Ajusté** | **47.2/100** | = | Aucun bonus/malus appliqué |

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

**Verdict :** 🔴 Thèse **CONFIRMÉE** en état **non-actionnable** — maintien mécanique **SURVEILLER** (Score Global 47.2/100), le fondamental n'a pas changé : vingt-septième snapshot consécutif sans données fiables, conflit de symbole FMP persistant avec métriques aberrantes, et **perte totale du flux prix** (close = NaN).

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix NaN) |
| RSI | ❌ Non disponible |
| Volume | 🔴 243M unités — figé sur trois snapshots consécutifs, probablement issu du ticker fantôme |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes / corrompues = risque non quantifiable |
| Score Global | 🔴 **47.2/100** → maintien mécanique SURVEILLER (fourchette 35–49) |
| Source données | 🔴 **Conflit de symbole persistant** : SPCX mappé sur `Industrials` / `Aerospace & Defense` avec market cap $2.52T, forward P/E −2,139, consensus $177.50 — prix totalement absent (NaN) |
| Signal sectoriel | 🔴 **NEUTRAL corrompu** — NaN massifs dans sector_rotation, momentum figé à 10.0 pour tous les secteurs |
| Stabilité inter-snapshot | 🟡 Prix NaN stable, volume figé 243M, métriques FMP identiques sur 10h→13h |
| Seuil de vigilance | 🔴 Score Valorisation 3.0/10 proche du seuil de disqualification (≤ 2/10) — artefact mécanique |

- **Confirmation :** La recommandation **SURVEILLER** est un artefact mécanique — le fondamental (absence totale de données fiables) est strictement identique au snapshot 10h. Le setup reste totalement non-actionnable. La stabilité mécanique sur trois snapshots consécutifs (21h 15/06, 10h 16/06, 13h 16/06) avec les mêmes valeurs figées (volume 243M, NaN prix, métriques FMP inchangées) confirme l'absence totale de flux de marché réel pour SPCX.
- **Nuances :** Le snapshot 13h UTC du 16/06 montre une **stabilisation du conflit de symbole dans sa forme la plus dégradée** : plus aucun prix n'est retourné (NaN), les métriques FMP restent figées aux niveaux aberrants, et le volume est identique (243M). Le module sector rotation est inutilisable (NaN massifs). Le faux événement FMP `earnings` du 16/06 est un artefact récurrent et ignoré. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume >1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ATTENDRE.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **SURVEILLER** puis reclassement **ÉVITER**. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER**.

**Recommandation :** **SURVEILLER** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours NaN)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur vingt-sept snapshots consécutifs. Le flux Yahoo est totalement indisponible (NaN) et FMP continue de renvoyer les données d'une entité étrangère (conflit de symbole persistant). Attendre un snapshot avec prix confirmé, sector correct et volume > 0 avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **243,783,175** | 🔴 Extrême anomalie | Figé sur trois snapshots consécutifs, astronomique pour un ETF SPAC |
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
- Analyse précédente : snapshot 10h UTC 2026-06-16
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours NaN)
- Recommandation précédente : SURVEILLER (artefact mécanique)
- Recommandation révisée : **SURVEILLER** (artefact mécanique — fondamentalement non-actionnable)
- Raison principale : Snapshot 13h UTC 16/06 : stabilité mécanique totale vs 10h — conflit de symbole FMP persistant (sector Industrials/Aerospace & Defense, forward P/E −2,138, market cap $2.52T), prix NaN stable (perte totale du flux Yahoo), volume figé 243M sur trois snapshots, métriques FMP identiques au 10h. Scoring mécanique inchangé 47.2/100. Sector rotation corrompu (NaN massifs, momentum figé 10.0). Aucun catalyseur ni news. Faux earnings FMP du 16/06 ignoré. Alerte social EXTREME_BEARISH ignorée (artefact).
- Thèse : 🟡 Confirmée (statu quo non-actionnable, stabilité mécanique totale, maintien SURVEILLER)
