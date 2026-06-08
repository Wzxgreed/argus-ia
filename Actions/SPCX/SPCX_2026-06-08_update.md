# SPCX — Mise à jour post-pipeline 2026-06-08 (snapshot 13h UTC)

**Date :** 2026-06-08
**Type :** Mise à jour post-pipeline — snapshot 13h UTC
**Analyse précédente :** snapshot 10h UTC 2026-06-08

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10h UTC 08/06) | Actuel (13h UTC 08/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Statut flux | `error: false` | `error: false` | = |
| Cours close | **$135.00** | **$135.00** | = |
| Open / High / Low | **$0.00 / $0.00 / $0.00** | **$0.00 / $0.00 / $0.00** | = |
| Volume | **0** | **0** | = |
| RSI 14j | N/A | N/A | = |
| ATR 14j | N/A | N/A | = |
| MM 50j | N/A | N/A | = |
| Recommandation agent | ATTENDRE | ATTENDRE | = |
| Score Opportunité | 5.5/10 | 5.5/10 | = |
| Score Catalyseur | 6.5/10 | 6.5/10 | = |
| Score Valorisation | 5.0/10 | 5.0/10 | = |
| Score Momentum | 5.0/10 | 5.0/10 | = |
| **Score Global Ajusté** | **55.2/100** | **55.2/100** | = |
| Timing | Neutre | Neutre | = |
| Signal sectoriel | `NEUTRAL` | `NEUTRAL` | = |

**Verdict :** Stabilité totale sur le snapshot 13h UTC. Le **conflit de symbole critique** persiste : `error: false` mais cours **$135.00** avec OHLC à **$0.00**, volume **0**, et secteur `Industrials` / `Aerospace & Defense` au lieu de `Financial Services` / `Asset Management`. Ce setup reste **non-actionnable**.

---

## Mise à jour technique

**🔴 [CRITICAL] — Anomalie data quality de type "conflit de symbole" persistante sur `data/latest.json` :**

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **$135.00** | 🔴 Conflit de symbole probable — ancien niveau ~$22, saut +513% non expliqué |
| Open | **$0.00** | 🔴 Incohérence absolue avec close $135.00 |
| High | **$0.00** | 🔴 Incohérence absolue avec close $135.00 |
| Low | **$0.00** | 🔴 Incohérence absolue avec close $135.00 |
| Previous close | $135.00 | 🔴 Aucun mouvement journalier (change_pct 0.00%) sur un gap théorique |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | **0 / 0** | 🔴 Liquidité nulle — pas un seul titre échangé |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w low / high | $0.00 / $0.00 | 🔴 Données erronées (anciens niveaux : $21.32 / $26.61) |
| Change % | 0.00% | 🔴 Plafonné mécaniquement malgré le "gap" |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le 27/05)
- Support secondaire : $21.32 (ancien 52w low)
- Résistance immédiate : $22.10 (high du 19/05 — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Défavorable → **Non-actionnable**. L'absence de données techniques fiables (RSI, ATR, MM50) sur treize snapshots consécutifs, combinée à un cours manifestement erroné ($135.00 avec OHLC à $0.00), rend toute analyse technique impossible. Le signal `error: false` reste trompeur — la qualité des données est dégradée.

---

## Mise à jour fondamentale

**🔴 [CRITICAL] — Changement de secteur dans `data/latest.json` persistant :**

| Métrique | Valeur actuelle | Valeur historique | Commentaire |
|----------|----------------|-------------------|-------------|
| Sector | `Industrials` | `Financial Services` | 🔴 Conflit de symbole confirmé — FMP renvoie les données d'une autre entité |
| Industry | `Aerospace & Defense` | `Asset Management` | 🔴 Conflit de symbole confirmé |
| P/E | N/A | N/A | ETF — non applicable |
| Forward P/E | N/A | N/A | ETF — non applicable |
| Market cap | N/A | N/A | 🔴 Non calculable |
| Price-to-book | 22.66622 | N/A | 🟡 Valeur FMP présente mais sector "Aerospace" → probablement d'une autre société |
| Beta | N/A | N/A | Non calculé |
| Dividend yield | N/A | N/A | Non distribué |

**FMP Ratios (données présentes mais non fiables) :**
- `market_cap`: 0
- `enterprise_value`: 0
- `price_to_book`: 0 (dans FMP ratios) vs 22.66622 (dans fundamentals) — incohérence interne
- `gross_margin`: 49.39%
- `operating_margin`: −13.86%
- `net_margin`: −26.44%

> **Note institutionnelle :** Les ratios FMP affichés (marges négatives, P/B 0, market cap 0) ne correspondent ni à un ETF SPAC ni aux données historiques de SPCX. Le symbole `SPCX` semble être mappé par FMP sur une entité du secteur `Aerospace & Defense` (probablement une small-cap industrielle) plutôt que sur l'ETF `SPAC & New Issue` de Tuttle Capital Management. **Toute donnée fondamentale sur ce snapshot doit être considérée comme non fiable.**

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/news_2026-06-08.json` : 0 item pour tous les tickers (source yahoo_rest) |
| Social sentiment | No data | `data/social_sentiment_2026-06-08.json` : 0 mentions Reddit, pump_detected = false |
| Options | 🟡 Anomalie | `max_pain` = $24.00 (incompatible avec cours $135.00), put/call ratio = 1.00, call_oi_pct = 50% — données probablement issues du même conflit de symbole |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable (ETF) |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-08.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-08.json` mentionne un faux événement `earnings` pour SPCX (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. Ce faux signal est récurrent depuis plusieurs snapshots et n'impacte pas le scoring.

---

## Scoring global (agents pipeline 2026-06-08, snapshot 13h UTC)

| Axe | Score | Changement vs 10h 08/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | 6.5/10 | = | Modéré-haussier — absence de catalyseur fondamental |
| Score Valorisation | 5.0/10 | = | Neutre |
| Score Momentum | 5.0/10 | = | ⚠️ Réajustement mécanique (placeholder), non fondé sur données de marché |
| **Score Opportunité** | **5.5/10** | = | Pondération régime Unknown : C×35% + V×40% + M×25% |
| **Score Global** | **55.2/100** | = | Avant ajustements |
| **Score Global Ajusté** | **55.2/100** | = | Aucun bonus/malus appliqué |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** 0 (données absentes, momentum non vérifiable)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé dans le rapport, mais hors fourchette ACHETER.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | ACHETER | Réduit | ❌ SPCX = 55.2 |
| 50–59 | **ATTENDRE** | — | ✅ SPCX = 55.2 (limite supérieure) |

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

**Verdict :** 🔴 Thèse **CONFIRMÉE** en état **ATTENDRE** — treize snapshots consécutifs sans données fiables, conflit de symbole FMP persistant, aucune mutation détectée entre 10h et 13h UTC.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix $135.00 erroné) |
| RSI | ❌ Non disponible |
| Volume | 🔴 0 unités — liquidité nulle |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes / corrompues = risque non quantifiable |
| Score Global | 🔴 55.2/100 → reclassement ATTENDRE maintenu |
| Source données | 🔴 **Conflit de symbole détecté** : SPCX mappé sur `Industrials` / `Aerospace & Defense` avec cours $135.00, OHLC $0.00 |
| Signal sectoriel | 🟡 `NEUTRAL` — XLF top3 avec momentum 4.0 (`return_20d` +1.45%), pas d'impact concret |
| Stabilité intra-journalière | 🟢 Aucune mutation entre 10h et 13h UTC |

- **Confirmation :** La recommandation **ATTENDRE** est maintenue. Aucun nouveau signal technique, fondamental ni de sentiment n'est apparu sur ce snapshot. Le setup technique du 27/05 (au-dessus MM50, RSI 59.07) reste suspendu. Le Score Global Ajusté de 55.2/100 est un artefact mécanique de l'Agent Recommandation en l'absence de données de marché fiables.
- **Nuances :** Le snapshot 13h UTC confirme la **stabilité totale** par rapport au snapshot 10h UTC : cours identique ($135.00), volume identique (0), scores identiques (55.2/100), secteur erroné identique (`Industrials` / `Aerospace & Defense`). Le signal sectoriel `NEUTRAL` persiste. XLF reste dans le top3 avec un momentum de 4.0 (`return_20d` +1.45%). Aucune news, événement corporate, flux options ni social n'est détecté sur ce snapshot. Le faux événement FMP `earnings` du 08/06 est un artefact récurrent et ignoré.
- **Rétablissement :** Un snapshot futur avec **données de prix fiables** (Yahoo ou FMP corrigé), volume > 1 000 unités, métriques techniques (RSI, ATR, MM50) et **sector correct** (`Financial Services`) justifierait une réévaluation. Un retour du Score Momentum à ≥ 6.0/10 relancerait le setup.
- **Invalidation définitive :** Si le flux de prix fiable ne revient pas sur les prochains snapshots → reclassement **ÉVITER** (ticker non surveillable). Si le prochain prix disponible confirmé est sous $21.32 (ancien 52w low) → **ÉVITER**.

**Recommandation :** **ATTENDRE**
**Prix cible :** N/A (données insuffisantes — cours $135.00 non fiable)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur treize snapshots consécutifs. Le flux Yahoo reste indisponible et FMP semble renvoyer les données d'un autre ticker (conflit de symbole). Attendre un snapshot avec prix confirmé, sector correct et volume > 0 avant toute réévaluation.

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
| Retour données Yahoo/FMP corrigées (prix, RSI, ATR, MM50, sector = Financial Services) | Prochain snapshot | Setup technique revalidable | Maintien en ATTENDRE / reclassement ÉVITER |
| Volume > 1 000 unités | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours confirmé sous $21.32 (ancien 52w low) | Immédiat | — | Reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ACHETER | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 10h UTC 08/06
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes — cours $135.00 non fiable)
- Recommandation précédente : ATTENDRE
- Recommandation révisée : **ATTENDRE**
- Raison principale : Snapshot 13h UTC 08/06 : stabilité totale vs 10h UTC, conflit de symbole FMP persistant (cours $135.00, OHLC $0.00, volume 0, sector Industrials/Aerospace au lieu de Financial Services/Asset Management). Score Global 55.2/100 (inchangé, artefact mécanique). Signal sectoriel NEUTRAL. Aucun catalyseur ni news. Faux earnings FMP ignoré.
- Thèse : 🟡 Confirmée (statu quo non-actionnable, dégradation data persistante avec conflit de symbole stable)
