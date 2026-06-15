# SPCX — Mise à jour post-pipeline 2026-06-15 (snapshot 10h UTC)

**Date :** 2026-06-15
**Type :** Mise à jour post-pipeline — snapshot 10h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-10

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 10/06) | Actuel (10h UTC 15/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$135.00** | **$160.95** | 🔴 +19.2% (faux cours aggravé) |
| Open / High / Low | **$0.00 / $135.00 / $135.00** | **$150.00 / $176.52 / $149.34** | 🔴 OHLC renseignés mais suspects |
| Volume | **0** | **519,234,800** | 🔴 Saut artificiel — égal à volume_avg_20d |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM 50j | N/A | N/A | = |
| Recommandation agent | **SURVEILLER** | **ATTENDRE** | 🟡 Reclassement mécanique |
| Score Opportunité | 4.7/10 | **5.1/10** | +0.4 (artefact) |
| Score Catalyseur | 6.5/10 | **7.0/10** | +0.5 (artefact) |
| Score Valorisation | 3.0/10 | **3.5/10** | +0.5 (artefact) |
| Score Momentum | 5.0/10 | 5.0/10 | = |
| **Score Global Ajusté** | **47.2/100** | **51.0/100** | +3.8 (artefact mécanique) |
| Timing | Neutre | Neutre | = |
| Signal sectoriel | NEUTRAL (données corrompues) | NEUTRAL | = |

**Verdict :** Vingt-troisième snapshot consécutif sans données fiables. Le conflit de symbole FMP s'est **aggravé** : le cours fictif a sauté de $135.00 à $160.95 (+19.2%), le volume est passé de 0 à 519M (identique à la moyenne 20j), et de nouvelles métriques fondamentales aberrantes sont apparues (market cap $2.1T, forward P/E −1,788). Le reclassement mécanique **SURVEILLER → ATTENDRE** et la remontée du Score Global de 47.2 à 51.0 sont des artefacts algorithmiques — en réalité la qualité des données s'est dégradée.

---

## Mise à jour technique

**🔴 [CRITICAL] — Anomalie data quality "conflit de symbole" aggravée sur `data/latest.json` :**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$160.95** | 🔴 Conflit de symbole — ancien niveau réel ~$22, faux cours +631% vs réalité |
| Open | **$150.00** | 🔴 Renseigné mais probablement issu d'une autre entité |
| High | **$176.52** | 🔴 52w high artificiel — non représentatif de SPCX |
| Low | **$149.34** | 🔴 52w low artificiel — non représentatif de SPCX |
| Previous close | $160.95 | 🔴 Égal au close — change_pct mécaniquement figé à 0.00% |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | **519,234,800 / 519,234,800** | 🔴 Volume identique à la moyenne — probable artefact |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w low / high (snapshot) | $149.34 / $176.52 | 🔴 Données erronées (anciens niveaux réels : $21.32 / $26.61) |
| Change % | 0.00% | 🔴 Figé mécaniquement malgré le "saut" de $135 à $160.95 |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Défavorable → **Non-actionnable**. Vingt-troisième snapshot consécutif sans RSI, ATR, ni MM50 fiables. L'apparition d'OHLC renseignés ($150/$176.52/$149.34) ne constitue pas une amélioration : elles proviennent très probablement du même ticker fantôme `Industrials` / `Aerospace & Defense` que FMP continue de mapper sur le symbole SPCX.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Changement de secteur persistant + aggravation des métriques aberrantes :**

| Métrique | Valeur actuelle | Valeur historique (10/06) | Commentaire |
|----------|----------------|--------------------------|-------------|
| Sector | `Industrials` | `Industrials` | 🔴 Conflit de symbole persistant |
| Industry | `Aerospace & Defense` | `Aerospace & Defense` | 🔴 Conflit de symbole persistant |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | **−1,788.33** | N/A | 🔴 **Nouvelle anomalie** — absurde pour tout instrument |
| Market cap (fundamentals) | **$2,106.97B** | $1,765.2B | 🔴 Aggravation — correspond à une mega-cap industrielle |
| Market cap (fmp_key_metrics) | **Absente** | $395.0B | 🔴 Disparue du bloc FMP, remplacée par $2.1T dans fundamentals |
| Price-to-book (fundamentals) | **27.02** | 22.67 | 🔴 Augmentation mécanique sur faux cours |
| Beta | N/A | N/A | Non calculé |
| Dividend yield | N/A | N/A | Non distribué |

**FMP Consensus (nouvelle anomalie) :**
- `price_target_avg`: **$177.50** (nouveau — incompatible avec un ETF SPAC)
- `num_analysts`: **2** (nouveau — non applicable pour un ETF)
- Source : TheFly

**FMP Ratios (données présentes mais non fiables) :**
- `price_to_earnings`: −95.39 (vs −80.01 le 10/06)
- `price_to_book`: 11.40 (FMP ratios) vs 27.02 (fundamentals) — divergence interne aggravée
- `price_to_sales`: 25.22
- `price_to_fcf`: −33.75
- `gross_margin`: 49.39%
- `operating_margin`: −13.86%
- `net_margin`: −26.44%
- `enterprise_value_multiple`: 369.23 (vs 234.41 précédemment)

> **Note institutionnelle :** Les nouvelles données FMP (forward P/E −1,788, market cap $2.1T, consensus $177.50 avec 2 analysts) confirment que le symbole SPCX est mappé sur une entité totalement étrangère à l'ETF Tuttle SPAC & New Issue. L'augmentation du Score Global de 47.2 à 51.0 et du Score Valorisation de 3.0 à 3.5 sont des artefacts mécaniques : l'Agent Recommandation interprète la présence de nouvelles métriques (même aberrantes) comme une "richesse de données" et ajuste ses scores en conséquence. **En réalité, la qualité des données s'est dégradée.**

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-15.json` : 0 item pour tous les tickers (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-15.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🟡 Anomalie | `max_pain` = $24.00 (incompatible avec cours $160.95), put/call = 1.00, call_oi_pct = 50% — conflit de symbole |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) — `fmp_consensus` présent mais faux (PT $177.50, 2 analysts) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-15.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-15.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-15 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer.

**Alerte social sentiment (artefact) :** `data/social_sentiment_latest.json` émet une alerte `EXTREME_BEARISH` sur SPCX (value 0.0) — purement mécanique due à l'absence totale de mentions (sentiment_score = 0.0). À ignorer en l'absence de volume réel de discussion.

---

## Scoring global (agents pipeline 2026-06-15, snapshot 10h UTC)

| Axe | Score | Changement vs 10h 10/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | **7.0/10** | +0.5 | Modéré-haussier — absence de catalyseur réel, artefact de richesse de données |
| Score Valorisation | **3.5/10** | +0.5 | 🔴 Artefact mécanique — nouvelles données FMP aberrantes (P/B 27, P/E −1,788) interprétées comme "richesse" |
| Score Momentum | 5.0/10 | = | ⚠️ Placeholder mécanique, non fondé sur données de marché |
| **Score Opportunité** | **5.1/10** | +0.4 | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **51.0/100** | +3.8 | Avant ajustements — artefact mécanique |
| **Score Global Ajusté** | **51.0/100** | +3.8 | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données — alerte EXTREME_BEARISH ignorée)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)
- **Sector rotation :** +0 (signal NEUTRAL, XLF #2 momentum 6.73)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé dans le rapport, mais hors fourchette ACHETER.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | — |
| 50–59 | **ATTENDRE** | — | ✅ **SPCX = 51.0** (limite basse) |
| 35–49 | SURVEILLER | — | ❌ |
| < 35 | ÉVITER | — | — |

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours $160.95 non fiable (conflit de symbole aggravé) |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valables sans confirmation technique ni prix fiable.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🔴 Thèse **CONFIRMÉE** en état **non-actionnable** — reclassement mécanique **SURVEILLER → ATTENDRE** (Score Global 51.0/100), mais le fondamental n'a pas changé : vingt-troisième snapshot consécutif sans données fiables, conflit de symbole FMP aggravé avec de nouvelles métriques encore plus aberrantes.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix $160.95 erroné) |
| RSI | ❌ Non disponible |
| Volume | 🔴 519M unités — suspect (identique à moyenne 20j), probablement issu du ticker fantôme |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes / corrompues = risque non quantifiable |
| Score Global | 🟡 **51.0/100** → reclassement mécanique ATTENDRE (fourchette 50–59) |
| Source données | 🔴 **Conflit de symbole aggravé** : SPCX mappé sur `Industrials` / `Aerospace & Defense` avec cours $160.95, market cap $2.1T, forward P/E −1,788, consensus $177.50 |
| Signal sectoriel | 🟡 NEUTRAL — XLF #2 (momentum 6.73), XLK top3 (momentum 10.0), pas d'impact concret sur SPCX |
| Stabilité inter-snapshot | 🔴 Cours fictif passé de $135.00 à $160.95 (+19.2%), nouvelles métriques aberrantes |
| Seuil de vigilance | 🟢 Score Valorisation 3.5/10 s'est éloigné du seuil de disqualification (≤ 2/10) — mais c'est un artefact |

- **Confirmation :** La recommandation **ATTENDRE** est un artefact mécanique — le fondamental (absence de données fiables) n'a pas changé. Le Score Global Ajusté de 51.0/100 reflète la présence de nouvelles métriques FMP (même aberrantes) que l'Agent Recommandation interprète comme une richesse de données. En réalité, le setup reste totalement non-actionnable.
- **Nuances :** Le snapshot 10h UTC du 15/06 montre une **aggravation du conflit de symbole** par rapport au 10/06 : cours fictif +19.2% ($135 → $160.95), apparition d'un forward P/E −1,788, market cap $2.1T, consensus $177.50 avec 2 analysts, et volume de 519M (identique à la moyenne 20j). Le module sector rotation semble avoir récupéré des données exploitables (pas de NaN cette fois), avec XLF #2 (momentum 6.73) et XLK top3 (momentum 10.0). Aucune news, événement corporate réel, ni flux options fiable n'est détecté. Le faux événement FMP `earnings` du 15/06 est un artefact récurrent et ignoré. L'alerte `EXTREME_BEARISH` du module social est un artefact mécanique (0 mention) et ignorée.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume > 1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 60/100 relancerait le setup en ACHENTER.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **ATTENDRE** puis reclassement **ÉVITER**. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER**.

**Recommandation :** **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours $160.95 non fiable)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur vingt-trois snapshots consécutifs. Le flux Yahoo reste indisponible et FMP semble renvoyer les données d'une autre entité (conflit de symbole aggravé). Attendre un snapshot avec prix confirmé, sector correct et volume > 0 avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **519,234,800** | 🔴 Extrême anomalie | Identique à volume_avg_20d — probable artefact du ticker fantôme |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🟡 Anomalie | — | `max_pain` $24.00 incompatible avec cours $160.95 → conflit de symbole |
| Révisions consensus | 🔴 Anomalie | — | PT $177.50 et 2 analysts — non applicable à un ETF, artefact FMP |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP corrigées (prix ~$22, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup revalidable en ATTENDRE | Maintien en ATTENDRE / reclassement ÉVITER |
| Volume > 1 000 unités confirmé | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ACHENTER | — |
| XLF momentum_score > 6.0 + données fiables | 5–10j | Contexte sectoriel favorable | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 10h UTC 2026-06-10
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours $160.95 non fiable)
- Recommandation précédente : SURVEILLER (artefact mécanique)
- Recommandation révisée : **ATTENDRE** (artefact mécanique — fondamentalement non-actionnable)
- Raison principale : Snapshot 10h UTC 15/06 : conflit de symbole FMP aggravé vs 10/06 (cours fictif $135.00 → $160.95 +19.2%, market cap $2.1T, forward P/E −1,788, consensus $177.50 avec 2 analysts, volume suspect 519M égal à moyenne 20j, OHLC renseignés mais suspects). Scoring mécanique remonté : Score Global 47.2 → 51.0/100, Score Opportunité 4.7 → 5.1/10 (C:6.5→7.0 V:3.0→3.5 M:5.0=). Signal sectoriel NEUTRAL (XLF #2 momentum 6.73). Aucun catalyseur ni news. Faux earnings FMP du 15/06 ignoré. Alerte social EXTREME_BEARISH ignorée (artefact).
- Thèse : 🟡 Confirmée (statu quo non-actionnable, dégradation data aggravée avec conflit de symbole et nouvelles métriques aberrantes, reclassement mécanique SURVEILLER → ATTENDRE)
