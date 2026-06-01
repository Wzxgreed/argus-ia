# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-06-01 (snapshot 10:00 UTC)

**Date :** 2026-06-01
**Type :** Mise à jour post-pipeline — snapshot 10:00 UTC
**Analyse précédente :** snapshot 17:00 UTC 2026-05-27

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (17:00 UTC 27/05) | Actuel (10:00 UTC 01/06) | Changement |
|--------|----------------------------|--------------------------|------------|
| Cours close | $22.339 | $22.08 | −$0.26 (−1.16%) |
| RSI 14j | 59.07 | **N/A** | 🔴 [DONNÉES MANQUANTES] |
| ATR 14j | $0.28 | **N/A** | 🔴 [DONNÉES MANQUANTES] |
| MM 50j | $22.00 | **N/A** | 🔴 [DONNÉES MANQUANTES] |
| Volume | 3 845 | **196** | −94.9% — quasi-illiquide |
| Volume vs moy. 20j | 1.02× | **N/A** | Données absentes |
| Recommandation agent | **ACHETER (Réduit)** | **ATTENDRE** | 🔴 Reclassement |
| Score Opportunité | 6.0/10 | **5.4/10** | −0.6 pt |
| Score Catalyseur | 6.5/10 | **6.5/10** | = |
| Score Valorisation | 5.0/10 | **5.0/10** | = |
| Score Momentum | 7.0/10 | **4.5/10** | −2.5 pts 🔴 |
| Score Global Ajusté | 65.2/100 | **54.0/100** | −11.2 pts |
| Timing | Favorable | **Neutre** | Dégradation |

**Verdict :** Dégradation majeure du setup technique. Yahoo n'a fourni aucune donnée technique (RSI, ATR, MM) pour SPCX sur le snapshot du 01/06 — source basculée sur `fmp_fallback`. Le volume a chuté de 95% à 196 unités, signalant une quasi-illiquide. L'Agent Recommandation a reclassé SPCX en **ATTENDRE** (Score Global 54.0), hors de la fourchette ACHETER. Le momentum a perdu 2.5 pts suite à l'absence de confirmation technique.

---

## Mise à jour technique

**[DONNÉES PARTIELLES]** — Le bloc `technical` de `data/latest.json` pour SPCX est vide (source : `fmp_fallback`). Aucune métrique technique n'est disponible sur ce snapshot.

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | N/A | [DONNÉES MANQUANTES] — impossible de valider la zone |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] — tendance non vérifiable |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | N/A | Données absentes |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w low / high | $21.32 / $26.61 | −17.0% vs 52w high, +3.6% vs 52w low |
| Change % | N/A | `change_pct` null (source FMP) |
| Open / High / Low | $22.07 / $22.10 / $22.07 | Range intraday $0.03 (0.14%) — extrêmement serré |
| Volume journalier | 196 | 🔴 Quasi-illiquide — 95% sous le volume du 27/05 |

**Niveaux clés (anciens, non confirmés) :**
- Support immédiat : $22.00 (MM50 — ancienne valeur, non vérifiée)
- Support secondaire : $21.32 (52w low)
- Résistance immédiate : $22.10 (high du jour)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Neutre → Défavorable. L'absence de données Yahoo et le volume quasi nul (196) rendent tout setup technique non vérifiable. Le range intraday de $0.03 confirme un marché figé, sans participation. Aucun signal d'accumulation ou de distribution n'est lisible.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale. SPCX reste un ETF thématique SPAC/post-IPO sans métriques classiques (P/E, EPS, consensus analystes non applicables).

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| P/E | N/A | ETF — non applicable |
| Forward P/E | N/A | ETF — non applicable |
| Market cap | $7.17M (FMP) | 🔴 Très faible — possible artefact FMP (capitalisation d'ETF thématique) |
| Beta | N/A | Non calculé |
| Dividend yield | N/A | Non distribué |
| Sector | Financial Services | Asset Management |

**Sector rotation :** Le secteur Financials (XLF) n'apparaît pas dans le top3 du `sector_rotation_2026-06-01.json`. XLF enregistre un return_20d de −1.06% et un momentum_score de 0.0 — pas de bonus/malus sectoriel pour SPCX. Seul XLK (Technology) domine avec un momentum_score de 10.0. Signal macro : `ROTATION_TO_DEFENSIVE` détecté, sans impact direct sur l'ETF SPAC.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_latest.json` : 0 événement corporate pour SPCX |
| Social sentiment | No data | `data/social_sentiment_latest.json` : 0 mentions Reddit, pump_detected = false |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable |
| FX Exposure | 🟢 | `data/fx_exposure_latest.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : pas de flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : pas assez de signaux historiques pour SPCX |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-01.json` mentionne un faux événement `earnings` pour SPCX (source FMP, days_until = 0) — artefact connu, à ignorer pour un ETF.

---

## Scoring global (agents pipeline 2026-06-01, snapshot 10:00 UTC)

| Axe | Score | Changement vs 27/05 | Commentaire |
|-----|-------|---------------------|-------------|
| Score Catalyseur | 6.5/10 | = | Modéré-haussier — absence de catalyseur fondamental |
| Score Valorisation | 5.0/10 | = | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 4.5/10 | −2.5 pts | 🔴 Dégradation — données techniques absentes, volume quasi nul |
| **Score Opportunité** | **5.4/10** | −0.6 pt | Pondération régime Normal : C×35% + V×40% + M×25% = 5.38 |
| **Score Global** | **54.0/100** | −11.2 pts | Avant ajustements |
| **Score Global Ajusté** | **54.0/100** | −11.2 pts | Aucun bonus/malus appliqué |

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

**Verdict :** 🔴 Thèse **INVALIDÉE** — suspension du signal technique par manque de données fiables et volume quasi nul.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (MM50 absent du snapshot) |
| RSI | ❌ Non disponible |
| Volume | 🔴 Quasi-illiquide (196 unités, −95% vs 27/05) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, désormais suspendu |
| Risque technique | 🔴 Données absentes = risque non quantifiable |
| Score Global | 🔴 54.0/100 → reclassement ATTENDRE |
| Source données | ⚠️ `fmp_fallback` — Yahoo a échoué, métriques techniques manquantes |

- **Invalidation :** La recommandation **ACHETER (Réduit)** du 27/05 reposait sur un setup technique validé (RSI 59.07, au-dessus MM50 $22.00, volume normalisé 1.02×). À la date du 01/06, Yahoo n'a fourni aucune donnée technique pour SPCX ; le snapshot se contente d'un cours FMP ($22.08) avec un volume de 196 unités. L'Agent Recommandation a logiquement abaissé le Score Momentum de 7.0 à 4.5 (−2.5 pts), entraînant le Score Global Ajusté à 54.0, hors de la fourchette d'achat.
- **Nuances :** Le cours $22.08 reste proche du niveau précédent ($22.34), mais la fiabilité de ce cours est entamée par le volume quasi nul et l'absence de données Yahoo. Il est impossible de confirmer que le support $22.00 (ancien MM50) tient. Le secteur Financials (XLF) reste hors de la rotation haussière (momentum_score 0.0, return_20d −1.06%). Aucun catalyseur sectoriel (reprise SPAC/IPO, baisse des taux) n'est apparu.
- **Rétablissement :** Un snapshot futur avec données Yahoo complètes (RSI, ATR, MM50), volume >1 000 unités, et cours stable au-dessus de $22.00 justifierait une réévaluation. Un retour du Score Momentum à ≥ 6.0/10 relancerait le setup.
- **Invalidation définitive :** Si le prochain snapshot Yahoo confirme une clôture sous $21.32 (52w low) avec volume persistant faible → reclassement **ÉVITER**.

**Recommandation :** **ATTENDRE**
**Prix cible :** N/A (données insuffisantes)
**Stop-loss :** N/A (ATR absent)
**Horizon :** —
**Conviction :** Faible — setup technique suspendu par absence de données fiables et quasi-illiquide. Attendre un snapshot Yahoo complet avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 196 | 🔴 Extrême anomalie | −95% vs snapshot 27/05 (3 845) — quasi-illiquide, marché figé |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | N/A | — | Données non disponibles |
| Révisions consensus | N/A | — | Non applicable |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|------------------|
| Retour données Yahoo (RSI, ATR, MM50) | Prochain snapshot | Setup technique revalidable | Maintien en ATTENDRE |
| Volume > 1 000 unités | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours sous $21.32 (52w low) | Immédiat | — | Reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ACHETER | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 17:00 UTC 27/05
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : $23.18
- Prix cible révisé : **N/A** (données insuffisantes)
- Recommandation précédente : ACHETER (Réduit)
- Recommandation révisée : **ATTENDRE**
- Raison principale : Snapshot 10:00 UTC 01/06 : données Yahoo absentes (RSI/ATR/MM50), volume chute de 95% à 196 unités, Agent Recommandation reclassifie SPCX en ATTENDRE avec Score Global 54.0
- Thèse : 🔴 Invalidée
