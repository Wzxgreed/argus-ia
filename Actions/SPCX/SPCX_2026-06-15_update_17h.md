# SPCX — Mise à jour post-pipeline 2026-06-15 (snapshot 17h UTC)

**Date :** 2026-06-15
**Type :** Mise à jour post-pipeline — snapshot 17h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-15

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 15/06) | Actuel (17h UTC 15/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$160.95** | **$179.26** | 🔴 +11.4% (faux cours aggravé) |
| Open / High / Low | $150.00 / $176.52 / $149.34 | **$171.81 / $179.50 / $168.36** | 🔴 OHLC encore plus élevés |
| Volume | 519,234,800 | **144,177,048** | 🟡 Chute mais reste aberrant |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| Recommandation agent | **ATTENDRE** | **SURVEILLER** | 🔴 Reclassement mécanique à la baisse |
| Score Opportunité | 5.1/10 | **4.8/10** | −0.3 |
| Score Catalyseur | 7.0/10 | **6.5/10** | −0.5 |
| Score Valorisation | 3.5/10 | **3.0/10** | −0.5 |
| Score Momentum | 5.0/10 | **5.5/10** | +0.5 |
| **Score Global Ajusté** | **51.0/100** | **48.5/100** | −2.5 |
| Timing | Neutre | Neutre | = |

**Verdict :** Vingt-quatrième snapshot consécutif sans données fiables. Le conflit de symbole FMP s'est **encore aggravé** : le cours fictif a sauté de $160.95 à $179.26 (+11.4%), de nouvelles métriques fondamentales encore plus aberrantes sont apparues (market cap $2.35T, forward P/E −1,992), et l'Agent Recommandation a reclasse mécaniquement **ATTENDRE → SURVEILLER** avec un Score Global en baisse de 51.0 à 48.5. Cette dégradation du scoring mécanique reflète enfin partiellement la réalité : la qualité des données continue de s'effondrer.

---

## Mise à jour technique

**🔴 [CRITICAL] — Anomalie data quality "conflit de symbole" encore aggravée sur `data/latest.json` :**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$179.26** | 🔴 Conflit de symbole — ancien niveau réel ~$22, faux cours +714% vs réalité |
| Open | **$171.81** | 🔴 Issu du même ticker fantôme |
| High | **$179.50** | 🔴 52w high artificiel encore rehaussé |
| Low | **$168.36** | 🔴 52w low artificiel encore rehaussé |
| Previous close | $160.95 | 🔴 Basé sur le faux cours du snapshot 10h |
| Change % | **+11.37%** | 🔴 Calcul mécanique sur faux cours |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Volume vs moy. 20j | **144,177,048 / 331,705,924** | 🟡 Volume en chute mais reste astronomique pour un ETF SPAC |
| ATR 14j | N/A | Volatilité non mesurable |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Défavorable → **Non-actionnable**. Vingt-quatrième snapshot consécutif sans RSI, ATR, ni MM50 fiables. L'apparition d'un faux +11.37% sur le cours fictif est purement mécanique et issue du même ticker fantôme `Industrials` / `Aerospace & Defense`.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Aggravation des métriques aberrantes :**

| Métrique | Valeur actuelle | Valeur historique (10h 15/06) | Commentaire |
|----------|----------------|----------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **−1,991.69** | −1,788.33 | 🔴 **Aggravation** — encore plus absurde |
| Market cap (fundamentals) | **$2,346.56B** | $2,106.97B | 🔴 Augmentation mécanique sur faux cours |
| Market cap (fmp_key_metrics) | **$1,585.46B** | Absent | 🔴 Apparition d'une nouvelle valeur aberrante |
| Price-to-book (fundamentals) | **30.10** | 27.02 | 🔴 Augmentation mécanique sur faux cours |
| Beta | N/A | N/A | Non calculé |

**FMP Consensus (stable mais faux) :**
- `price_target_avg`: **$177.50** (stable vs 10h)
- `num_analysts`: **2** (stable vs 10h)
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.39 (stable)
- `price_to_book`: 11.40 (FMP ratios) vs 30.10 (fundamentals) — divergence interne aggravée
- `price_to_sales`: 25.22 (stable)
- `price_to_fcf`: −33.75 (stable)
- `enterprise_value_multiple`: **369.23** (vs 369.23 précédemment — stable)

> **Note institutionnelle :** Le forward P/E est passé de −1,788 à −1,992, et le market cap de $2.1T à $2.35T dans le bloc fundamentals (tandis qu'un $1.59T apparaît dans fmp_key_metrics). Ces écarts internes confirment que le symbole SPCX est mappé sur une entité totalement étrangère à l'ETF Tuttle SPAC & New Issue. La baisse du Score Valorisation de 3.5 à 3.0/10 et du Score Global de 51.0 à 48.5 sont des artefacts mécaniques — mais cette fois dans le bon sens : l'agent semble avoir pénalisé la valorisation face à des métriques encore plus délirantes.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-15.json` : 0 item pour tous les tickers (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-15.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🔴 Anomalie | `max_pain` = $24.00 (incompatible avec cours $179.26), put/call = 1.00, call_oi_pct = 50% — conflit de symbole |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $177.50, 2 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-15.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-15.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-15 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer.

**Alerte social sentiment (artefact) :** `data/social_sentiment_latest.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions. À ignorer.

---

## Scoring global (agents pipeline 2026-06-15, snapshot 17h UTC)

| Axe | Score | Changement vs 10h 15/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **6.5/10** | −0.5 | Modéré — absence de catalyseur réel |
| Score Valorisation | **3.0/10** | −0.5 | 🔴 Retour au niveau du 10/06 — artefact mécanique |
| Score Momentum | **5.5/10** | +0.5 | ⚠️ Placeholder mécanique, non fondé sur données de marché |
| **Score Opportunité** | **4.8/10** | −0.3 | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **48.5/100** | −2.5 | Avant ajustements — artefact mécanique |
| **Score Global Ajusté** | **48.5/100** | −2.5 | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL, XLF #3 momentum 5.12)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé dans le rapport, mais hors fourchette ACHETER.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | ATTENDRE | — | ❌ SPCX a quitté cette fourchette |
| 35–49 | **SURVEILLER** | — | ✅ **SPCX = 48.5** |
| < 35 | ÉVITER | — | — |

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours $179.26 non fiable (conflit de symbole aggravé) |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🔴 Thèse **CONFIRMÉE** en état **non-actionnable** — reclassement mécanique **ATTENDRE → SURVEILLER** (Score Global 48.5/100), le fondamental n'a pas changé : vingt-quatrième snapshot consécutif sans données fiables, conflit de symbole FMP aggravé avec de nouvelles métriques encore plus aberrantes.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix $179.26 erroné) |
| RSI | ❌ Non disponible |
| Volume | 🔴 144M unités — suspect (chute de 519M mais reste astronomique), probablement issu du ticker fantôme |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes / corrompues = risque non quantifiable |
| Score Global | 🔴 **48.5/100** → reclassement mécanique SURVEILLER (fourchette 35–49) |
| Source données | 🔴 **Conflit de symbole aggravé** : SPCX mappé sur `Industrials` / `Aerospace & Defense` avec cours $179.26, market cap $2.35T, forward P/E −1,992, consensus $177.50 |
| Signal sectoriel | 🟡 NEUTRAL — XLF #3 (momentum 5.12), XLK top3 (momentum 10.0), pas d'impact concret sur SPCX |
| Stabilité inter-snapshot | 🔴 Cours fictif passé de $160.95 à $179.26 (+11.4%), nouvelles métriques encore plus aberrantes |
| Seuil de vigilance | 🔴 Score Valorisation 3.0/10 proche du seuil de disqualification (≤ 2/10) — artefact mécanique |

- **Confirmation :** La recommandation **SURVEILLER** est un artefact mécanique — le fondamental (absence de données fiables) n'a pas changé. Le Score Global Ajusté de 48.5/100 reflète la dégradation perçue par l'Agent Recommandation face à des métriques FMP encore plus aberrantes (forward P/E −1,992 vs −1,788). En réalité, le setup reste totalement non-actionnable.
- **Nuances :** Le snapshot 17h UTC du 15/06 montre une **aggravation du conflit de symbole** par rapport au snapshot 10h : cours fictif +11.4% ($160.95 → $179.26), forward P/E passé de −1,788 à −1,992, market cap fundamentals passé de $2.1T à $2.35T, et apparition d'un market cap fmp_key_metrics à $1.59T. Le module sector rotation a légèrement évolué : XLF est désormais #3 (momentum 5.12) vs #2 (momentum 6.73) à 10h. Aucune news, événement corporate réel, ni flux options fiable n'est détecté. Le faux événement FMP `earnings` du 15/06 est un artefact récurrent et ignoré. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume > 1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHENTER.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **SURVEILLER** puis reclassement **ÉVITER**. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER**.

**Recommandation :** **SURVEILLER** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours $179.26 non fiable)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur vingt-quatre snapshots consécutifs. Le flux Yahoo reste indisponible et FMP semble renvoyer les données d'une autre entité (conflit de symbole aggravé). Attendre un snapshot avec prix confirmé, sector correct et volume > 0 avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **144,177,048** | 🔴 Extrême anomalie | Chute de 519M mais reste astronomique pour un ETF SPAC |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🔴 Anomalie | — | `max_pain` $24.00 incompatible avec cours $179.26 → conflit de symbole |
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
- Analyse précédente : snapshot 10h UTC 2026-06-15
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours $179.26 non fiable)
- Recommandation précédente : ATTENDRE (artefact mécanique)
- Recommandation révisée : **SURVEILLER** (artefact mécanique — fondamentalement non-actionnable)
- Raison principale : Snapshot 17h UTC 15/06 : conflit de symbole FMP aggravé vs 10h (cours fictif $160.95 → $179.26 +11.4%, forward P/E −1,788 → −1,992, market cap $2.1T → $2.35T, volume 519M → 144M). Scoring mécanique ajusté à la baisse : Score Global 51.0 → 48.5/100, Score Opportunité 5.1 → 4.8/10 (C:7.0→6.5 V:3.5→3.0 M:5.0→5.5). Reclassement ATTENDRE → SURVEILLER. Signal sectoriel NEUTRAL (XLF #3 momentum 5.12). Aucun catalyseur ni news. Faux earnings FMP du 15/06 ignoré. Alerte social EXTREME_BEARISH ignorée (artefact).
- Thèse : 🟡 Confirmée (statu quo non-actionnable, dégradation data aggravée avec conflit de symbole et nouvelles métriques aberrantes, reclassement mécanique ATTENDRE → SURVEILLER)
