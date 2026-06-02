# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-06-02 (snapshot 13h UTC)

**Date :** 2026-06-02
**Type :** Mise à jour post-pipeline — snapshot 13h UTC
**Analyse précédente :** snapshot 21h UTC 2026-06-01

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (21h UTC 01/06) | Actuel (13h UTC 02/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Cours close | $22.0801 | $22.0801 | = |
| RSI 14j | N/A | N/A | = [DONNÉES MANQUANTES] |
| ATR 14j | N/A | N/A | = [DONNÉES MANQUANTES] |
| MM 50j | N/A | N/A | = [DONNÉES MANQUANTES] |
| Volume | 196 | 196 | = |
| Source | `fmp_fallback` | `fmp_fallback` | = |
| Recommandation agent | ATTENDRE | ATTENDRE | = |
| Score Opportunité | 5.4/10 | 5.4/10 | = |
| Score Catalyseur | 6.5/10 | 6.5/10 | = |
| Score Valorisation | 5.0/10 | 5.0/10 | = |
| Score Momentum | 4.5/10 | 4.5/10 | = |
| Score Global Ajusté | 54.0/100 | 54.0/100 | = |
| Timing | Neutre | Neutre | = |
| Signal sectoriel | `ROTATION_TO_CYCLICAL` | `ROTATION_TO_CYCLICAL` | = |

**Verdict :** Stabilité totale sur quatre snapshots consécutifs (10h/17h/21h UTC 01/06 et 13h UTC 02/06). Le cours est figé à **$22.0801**, le volume figé à **196 unités**, et la source `fmp_fallback` persiste sans retour des données Yahoo. Le setup reste **non-actionnable**.

---

## Mise à jour technique

**[DONNÉES PARTIELLES]** — Le bloc `technical` de `data/latest.json` pour SPCX reste vide (source : `fmp_fallback`). Aucune métrique technique Yahoo n'est disponible sur ce snapshot 13h.

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | N/A | Données absentes |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w low / high | $21.32 / $26.61 | −17.0% vs 52w high, +3.6% vs 52w low |
| Change % | N/A | `change_pct` null (source FMP) |
| Open / High / Low | $22.07 / $22.10 / $22.07 | Range intraday $0.03 (0.14%) |
| Volume journalier | 196 | 🔴 Quasi-illiquide — inchangé sur 4 snapshots |
| Previous close | $21.95 | Micro-hausse $0.13 (+0.59%) vs clôture veille |

**Niveaux clés (anciens, non confirmés) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié)
- Support secondaire : $21.32 (52w low)
- Résistance immédiate : $22.10 (high du jour)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Neutre → Défavorable. L'absence totale de données Yahoo sur quatre snapshots consécutifs et le volume figé à 196 unités rendent tout setup technique non vérifiable. Le range intraday de $0.03 confirme un marché totalement figé.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale. SPCX reste un ETF thématique SPAC/post-IPO sans métriques classiques applicables.

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| P/E | N/A | ETF — non applicable |
| Forward P/E | N/A | ETF — non applicable |
| Market cap | $7.17M (FMP) | 🔴 Très faible — artefact FMP sur ETF thématique |
| Beta | N/A | Non calculé |
| Dividend yield | N/A | Non distribué |
| Sector | Financial Services | Asset Management |

**Sector rotation :** `data/sector_rotation_2026-06-02.json` enregistre un signal stable `ROTATION_TO_CYCLICAL`. XLF (Financials) figure dans le `top3` avec un `return_20d` de −0.94% et un `momentum_score` de 0.0 — pas de bonus/malus sectoriel pour SPCX. XLK (Technology) domine avec `momentum_score` 10.0 et `return_20d` +20.94%. Le secteur Financials reste sous-performant vs SPY sur 20j (`rs_20d` −6.20%).

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_2026-06-02.json` : 0 événement corporate |
| Social sentiment | No data | `data/social_sentiment_2026-06-02.json` : 0 mentions Reddit, pump_detected = false |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-02.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant pour SPCX |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-02.json` mentionne un faux événement `earnings` pour SPCX (source FMP, days_until = 0) — artefact connu, à ignorer pour un ETF.

---

## Scoring global (agents pipeline 2026-06-02, snapshot 13h UTC)

| Axe | Score | Changement vs 21h 01/06 | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | 6.5/10 | = | Modéré-haussier — absence de catalyseur fondamental |
| Score Valorisation | 5.0/10 | = | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 4.5/10 | = | 🔴 Dégradation — données techniques absentes, volume quasi nul |
| **Score Opportunité** | **5.4/10** | = | Pondération régime Unknown : C×35% + V×40% + M×25% = 5.38 |
| **Score Global** | **54.0/100** | = | Avant ajustements |
| **Score Global Ajusté** | **54.0/100** | = | Aucun bonus/malus appliqué |

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
| 60–74 | ACHETER | Réduit | ❌ SPCX = 54.0 |
| 50–59 | **ATTENDRE** | — | ✅ SPCX = 54.0 (limite supérieure) |

---

## Révision des niveaux SL / TP

**Niveaux obsolètes — recalcul impossible en l'absence d'ATR valide dans `data/latest.json`.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | $22.08 | Close du jour (source `data/latest.json`) |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Anciens niveaux (27/05) à titre indicatif uniquement :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valides sans confirmation technique.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **CONFIRMÉE** en état ATTENDRE — stabilité totale sur quatre snapshots consécutifs (10h/17h/21h UTC 01/06 et 13h UTC 02/06). Aucune amélioration ni dégradation.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (MM50 absent du snapshot) |
| RSI | ❌ Non disponible |
| Volume | 🔴 Quasi-illiquide persistant (196 unités, inchangé sur 4 snapshots) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes = risque non quantifiable |
| Score Global | 🔴 54.0/100 → reclassement ATTENDRE maintenu |
| Source données | ⚠️ `fmp_fallback` persistant sur 4 snapshots — Yahoo indisponible |
| Signal sectoriel | 🟡 `ROTATION_TO_CYCLICAL` inchangé — XLF dans top3 mais momentum 0.0 |

- **Confirmation :** La recommandation **ATTENDRE** du snapshot 21h UTC 01/06 est confirmée sur le snapshot 13h UTC 02/06. Aucun nouveau signal technique, fondamental ni de sentiment n'est apparu. Le cours ($22.0801) est statique, le volume (196) figé, et les données Yahoo toujours absentes. Le setup technique du 27/05 (au-dessus MM50, RSI 59.07) reste suspendu.
- **Nuances :** Le secteur Financials (XLF) est classé dans le `top3` du `sector_rotation` avec un signal `ROTATION_TO_CYCLICAL`, mais son `momentum_score` reste à 0.0 et son `return_20d` à −0.94% — pas de catalyseur sectoriel exploitable pour SPCX. Aucune news, aucun événement corporate, aucun flux options ni social n'est détecté.
- **Rétablissement :** Un snapshot futur avec données Yahoo complètes (RSI, ATR, MM50), volume > 1 000 unités, et cours stable au-dessus de $22.00 justifierait une réévaluation. Un retour du Score Momentum à ≥ 6.0/10 relancerait le setup.
- **Invalidation définitive :** Si le prochain snapshot Yahoo confirme une clôture sous $21.32 (52w low) avec volume persistant faible → reclassement **ÉVITER**.

**Recommandation :** **ATTENDRE**
**Prix cible :** N/A (données insuffisantes)
**Stop-loss :** N/A (ATR absent)
**Horizon :** —
**Conviction :** Faible — setup technique suspendu par absence de données fiables et quasi-illiquide persistante sur quatre snapshots consécutifs. Attendre un snapshot Yahoo complet avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 196 | 🔴 Extrême anomalie | Inchangé sur 4 snapshots — quasi-illiquide persistant, marché figé |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | N/A | — | Données non disponibles |
| Révisions consensus | N/A | — | Non applicable |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo (RSI, ATR, MM50) | Prochain snapshot | Setup technique revalidable | Maintien en ATTENDRE |
| Volume > 1 000 unités | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours sous $21.32 (52w low) | Immédiat | — | Reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ACHETER | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 21h UTC 01/06
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes)
- Recommandation précédente : ATTENDRE
- Recommandation révisée : **ATTENDRE**
- Raison principale : Snapshot 13h UTC 02/06 : stabilité totale vs 21h 01/06 — données Yahoo absentes (RSI/ATR/MM50), volume figé à 196 unités, source fmp_fallback persistante sur 4 snapshots, Score Global 54.0 maintenu, signal sectoriel ROTATION_TO_CYCLICAL sans impact concret
- Thèse : 🟡 Confirmée (statu quo)
