# SPCX — Mise à jour post-pipeline 2026-06-09 (snapshot 13h UTC)

**Date :** 2026-06-09
**Type :** Mise à jour post-pipeline — snapshot 13h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-09

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 09/06) | Actuel (13h UTC 09/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$135.00** | **$135.00** | = |
| Open / High / Low | **$0.00 / $135.00 / $135.00** | **$0.00 / $135.00 / $135.00** | = |
| Volume | **0** | **0** | = |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM 50j | N/A | N/A | = |
| Recommandation agent | **SURVEILLER** | **SURVEILLER** | = |
| Score Opportunité | 4.7/10 | **4.7/10** | = |
| Score Catalyseur | 6.5/10 | 6.5/10 | = |
| Score Valorisation | 3.0/10 | **3.0/10** | = |
| Score Momentum | 5.0/10 | 5.0/10 | = |
| **Score Global Ajusté** | **47.2/100** | **47.2/100** | = |
| Timing | Neutre | Neutre | = |
| Signal sectoriel XLF | `NEUTRAL` (+1.42% 20j) | `NEUTRAL` (+1.42% 20j) | = |

**Verdict :** Seizième snapshot consécutif sans données fiables. **Stabilité totale** vs le snapshot 10h UTC : cours inchangé, volume inchangé, scores inchangés, conflit de symbole FMP persistant. Aucune mutation détectée sur aucun axe.

---

## Mise à jour technique

**🔴 [CRITICAL] — Anomalie data quality "conflit de symbole" persistante sur `data/latest.json` :**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$135.00** | 🔴 Conflit de symbole probable — ancien niveau ~$22, saut +513% non expliqué |
| Open | **$0.00** | 🔴 Incohérence absolue avec close $135.00 |
| High | **$135.00** | 🔴 Égal au close — plafonnage mécanique, pas de vrai high |
| Low | **$135.00** | 🔴 Égal au close — plafonnage mécanique, pas de vrai low |
| Previous close | $135.00 | 🔴 Aucun mouvement journalier (change_pct 0.00%) |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | **0 / 0** | 🔴 Liquidité nulle — pas un seul titre échangé |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w low / high | $135.00 / $135.00 | 🔴 Données erronées (anciens niveaux : $21.32 / $26.61) |
| Change % | 0.00% | 🔴 Plafonné mécaniquement |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Défavorable → **Non-actionnable**. L'absence de données techniques fiables (RSI, ATR, MM50) sur seize snapshots consécutifs, combinée à un cours manifestement erroné ($135.00 avec open $0.00), rend toute analyse technique impossible.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Changement de secteur dans `data/latest.json` persistant :**

| Métrique | Valeur actuelle | Valeur historique | Commentaire |
|----------|----------------|-------------------|-------------|
| Sector | `Industrials` | `Financial Services` | 🔴 Conflit de symbole confirmé — FMP renvoie les données d'une autre entité |
| Industry | `Aerospace & Defense` | `Asset Management` | 🔴 Conflit de symbole confirmé |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | N/A | N/A | ETF — non applicable |
| Market cap (fundamentals) | $1,765.2B | N/A | 🔴 Valeur absurde — correspond à une mega-cap industrielle, pas à un ETF SPAC |
| Market cap (fmp_key_metrics) | $395.0B | N/A | 🔴 Divergence interne flagrante vs $1,765.2B |
| Price-to-book (fundamentals) | 22.66622 | N/A | 🟡 Valeur FMP présente mais sector "Aerospace" → données d'une autre société |
| Price-to-book (fmp_ratios) | 9.56 | N/A | 🔴 Divergence interne vs 22.67 (fundamentals) |
| Beta | N/A | N/A | Non calculé |
| Dividend yield | N/A | N/A | Non distribué |

**FMP Ratios (données présentes mais non fiables) :**
- `market_cap`: $395.0B (fmp_key_metrics) vs $1,765.2B (fundamentals) — incohérence interne flagrante
- `enterprise_value`: $393.2B
- `price_to_book`: 9.56 (FMP ratios) vs 22.67 (fundamentals) — divergence interne
- `gross_margin`: 49.39%
- `operating_margin`: −13.86%
- `net_margin`: −26.44%
- `price_to_earnings`: −80.01
- `return_on_equity`: −11.95%
- `net_debt_to_ebitda`: −0.43

> **Note institutionnelle :** Les ratios FMP affichés (marges négatives, P/E −80, market cap $395B–$1,765B) ne correspondent ni à un ETF SPAC ni aux données historiques de SPCX. Le symbole `SPCX` est mappé par FMP sur une entité du secteur `Industrials` / `Aerospace & Defense` (probablement une mega-cap industrielle) plutôt que sur l'ETF `SPAC & New Issue` de Tuttle Capital Management. **Toute donnée fondamentale sur ce snapshot doit être considérée comme non fiable.**

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-09.json` : 0 item pour tous les tickers (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-09.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🟡 Anomalie | `max_pain` = $24.00 (incompatible avec cours $135.00), put/call ratio = 1.00, call_oi_pct = 50% — données probablement issues du même conflit de symbole |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-09.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-09.json` mentionne un faux événement `earnings` pour SPCX le 2026-06-09 (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. Ce faux signal est récurrent depuis plusieurs snapshots et n'impacte pas le scoring.

---

## Scoring global (agents pipeline 2026-06-09, snapshot 13h UTC)

| Axe | Score | Changement vs 10h 09/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | 6.5/10 | = | Modéré-haussier — absence de catalyseur fondamental |
| Score Valorisation | **3.0/10** | = | Détérioration mécanique — artefact de l'Agent Recommandation face aux données corrompues (P/B 22.7, P/E −80) |
| Score Momentum | 5.0/10 | = | ⚠️ Réajustement mécanique (placeholder), non fondé sur données de marché |
| **Score Opportunité** | **4.7/10** | = | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **47.2/100** | = | Avant ajustements |
| **Score Global Ajusté** | **47.2/100** | = | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)

**⚠️ Alerte de seuil :** Le Score Valorisation à 3.0/10 est proche du seuil de disqualification (≤ 2/10). Une baisse additionnelle de 1.0 pt exclurait SPCX du rapport d'opportunités.

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé dans le rapport, mais hors fourchette ACHENTER.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | ❌ |
| 50–59 | **ATTENDRE** | — | ❌ |
| 35–49 | **SURVEILLER** | — | ✅ **SPCX = 47.2** |
| < 35 | ÉVITER | — | — |

---

## Révision des niveaux SL / TP

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix fiable et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours $135.00 non fiable (conflit de symbole) |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valides sans confirmation technique ni prix fiable.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🔴 Thèse **CONFIRMÉE** en état **SURVEILLER** — seize snapshots consécutifs sans données fiables, conflit de symbole FMP persistant, **stabilité totale du scoring** (Score Global 47.2/100 inchangé). Le setup reste non-actionnable.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix $135.00 erroné) |
| RSI | ❌ Non disponible |
| Volume | 🔴 0 unités — liquidité nulle |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes / corrompues = risque non quantifiable |
| Score Global | 🔴 **47.2/100** → reclassement SURVEILLER (fourchette 35–49) |
| Source données | 🔴 **Conflit de symbole détecté** : SPCX mappé sur `Industrials` / `Aerospace & Defense` avec cours $135.00, OHLC $0.00/$135.00, volume 0, sector Industrials/Aerospace au lieu de Financial Services/Asset Management |
| Signal sectoriel | 🟡 `NEUTRAL` — XLF top3 avec momentum 4.0 (`return_20d` +1.42%, inchangé vs snapshot 10h). XLF reste dans le top3 sectoriel |
| Stabilité inter-snapshot | 🟢 Cours inchangé ($135.00), volume inchangé (0), scores inchangés |
| Seuil de vigilance | ⚠️ Score Valorisation 3.0/10 proche du seuil de disqualification (≤ 2/10) |

- **Confirmation :** La recommandation **SURVEILLER** est un artefact mécanique — le fondamental (absence de données fiables) n'a pas changé. Le Score Global Ajusté de 47.2/100 reflète la détérioration du Score Valorisation, probablement déclenchée par les ratios FMP aberrants (P/B 22.7, P/E −80) que l'Agent Recommandation interprète comme une valorisation défavorable. En réalité, ces ratios appartiennent à une autre entité (conflit de symbole).
- **Nuances :** Le snapshot 13h UTC confirme la **stabilité totale** par rapport au snapshot 10h UTC du 09/06 : cours identique ($135.00), volume identique (0), secteur erroné identique (`Industrials` / `Aerospace & Defense`), scores identiques (Global 47.2, Opportunité 4.7, Catalyseur 6.5, Valorisation 3.0, Momentum 5.0). Le signal sectoriel `NEUTRAL` persiste avec XLF return_20d +1.42% (momentum_score 4.0). Aucune news, événement corporate, flux options ni social n'est détecté sur ce snapshot. Le faux événement FMP `earnings` du 09/06 est un artefact récurrent et ignoré.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume > 1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Global au-dessus de 50/100 relancerait le setup en ATTENDRE ; au-dessus de 60/100 en ACHENTER.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → maintien en **SURVEILLER** puis reclassement **ÉVITER**. Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER**. Si Score Valorisation passe ≤ 2/10 → exclusion automatique du rapport.

**Recommandation :** **SURVEILLER** (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours $135.00 non fiable)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur seize snapshots consécutifs. Le flux Yahoo reste indisponible et FMP semble renvoyer les données d'une autre ticker (conflit de symbole). Attendre un snapshot avec prix confirmé, sector correct et volume > 0 avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | **0** | 🔴 Extrême anomalie | Liquidité nulle — pas un seul titre échangé |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | 🟡 Anomalie | — | `max_pain` $24.00 incompatible avec cours $135.00 → conflit de symbole probable |
| Révisions consensus | N/A | — | Non applicable |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP corrigées (prix, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup revalidable en ATTENDRE | Maintien en SURVEILLER / reclassement ÉVITER |
| Volume > 1 000 unités | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Score Valorisation ≤ 2/10 | Immédiat | — | Exclusion automatique du rapport |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ACHENTER | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 10h UTC 2026-06-09
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours $135.00 non fiable)
- Recommandation précédente : SURVEILLER
- Recommandation révisée : **SURVEILLER** (artefact mécanique)
- Raison principale : Snapshot 13h UTC 09/06 : stabilité totale vs snapshot 10h UTC 09/06, seize snapshots consécutifs sans données fiables, conflit de symbole FMP persistant (cours $135.00, OHLC $0.00/$135.00, volume 0, sector Industrials/Aerospace au lieu de Financial Services/Asset Management). Scoring inchangé : Score Global 47.2/100, Score Opportunité 4.7/10 (C:6.5 V:3.0 M:5.0). Signal sectoriel NEUTRAL avec XLF return_20d +1.42% (momentum_score 4.0). Aucun catalyseur ni news. Faux earnings FMP du 09/06 ignoré (artefact récurrent). Alerte : Score Valorisation 3.0/10 proche du seuil de disqualification (≤ 2/10).
- Thèse : 🟡 Confirmée (statu quo non-actionnable, dégradation data persistante avec conflit de symbole stable, reclassement mécanique ATTENDRE → SURVEILLER maintenu)
