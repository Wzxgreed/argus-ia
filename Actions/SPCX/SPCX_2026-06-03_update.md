# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-06-03 (snapshot 10h UTC)

**Date :** 2026-06-03
**Type :** Mise à jour post-pipeline — snapshot 10h UTC
**Analyse précédente :** snapshot 21h UTC 2026-06-02

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (21h UTC 02/06) | Actuel (10h UTC 03/06) | Changement |
|--------|--------------------------|------------------------|------------|
| Cours close | N/A | N/A | = |
| Volume | N/A | N/A | = |
| Source | `error` | `error` | = |
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

**Verdict :** Aucun changement. Sept snapshots consécutifs (10h/17h/21h UTC 01/06, 13h/17h/21h UTC 02/06, 10h UTC 03/06) sans aucune donnée de prix, volume ou technique pour SPCX. Le setup reste **totalement non-actionnable**.

---

## Mise à jour technique

**🔴 [CRITICAL] — `data/latest.json` retourne une erreur brute pour SPCX :**
```json
{
  "ticker": "SPCX",
  "error": true,
  "reason": "No price history",
  "timestamp": "2026-06-03T10:00:18.529490+00:00"
}
```
Aucune métrique technique, prix, volume, ni historique n'est disponible sur ce snapshot.

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours close | **N/A** | 🔴 Perte totale du flux prix (FMP + Yahoo) — 7e snapshot consécutif |
| RSI 14j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM50j | N/A | [DONNÉES MANQUANTES] |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | N/A | Données absentes |
| ATR 14j | N/A | Volatilité non mesurable |
| 52w low / high | $21.32 / $26.61 | Derniers niveaux connus (non confirmés) |
| Change % | N/A | `change_pct` indisponible |
| Open / High / Low | N/A | Aucun tick |
| Volume journalier | N/A | 🔴 Plus aucune donnée de volume |

**Niveaux clés (anciens, obsolètes) :**
- Support immédiat : $22.00 (ancien MM50 — non vérifié depuis le snapshot 13h 02/06)
- Support secondaire : $21.32 (52w low)
- Résistance immédiate : $22.10 (high du jour précédent — non confirmé)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Défavorable → **Non-actionnable**. L'absence totale de données de prix sur sept snapshots consécutifs rend impossible toute analyse technique. Le ticker n'est plus surveillable en temps réel.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale. SPCX reste un ETF thématique SPAC/post-IPO sans métriques classiques applicables.

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| P/E | N/A | ETF — non applicable |
| Forward P/E | N/A | ETF — non applicable |
| Market cap | N/A | 🔴 Non calculable — prix indisponible |
| Beta | N/A | Non calculé |
| Dividend yield | N/A | Non distribué |
| Sector | Financial Services | Asset Management |

**Sector rotation :** `data/sector_rotation_2026-06-03.json` enregistre un signal **`NEUTRAL`**. XLF (Financials) reste dans le `top3` mais avec un `return_20d` de **−0.23%** et un `momentum_score` de **0.0** — pas de catalyseur sectoriel exploitable. XLK (Technology) domine toujours avec `momentum_score` 10.0. Le secteur Financials affiche un `rs_20d` de **−6.02%** (sous-performant vs SPY). Aucun crossover détecté.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_2026-06-03.json` : 0 événement corporate |
| Social sentiment | No data | `data/social_sentiment_2026-06-03.json` : 0 mentions Reddit, pump_detected = false |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies |
| Analyst consensus | N/A | Non applicable |
| FX Exposure | 🟢 | `data/fx_exposure_2026-06-03.json` : fx_impact_score 0.0, flag 🟢, neutral |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : aucun flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : n=0, insuffisant |

**Anomalie data quality persistante :** `data/upcoming_events_2026-06-03.json` mentionne un faux événement `earnings` pour SPCX (source FMP, days_until = 0) — artefact connu pour un ETF, à ignorer. Ce faux signal est récurrent depuis plusieurs snapshots et n'impacte pas le scoring.

---

## Scoring global (agents pipeline 2026-06-03, snapshot 10h UTC)

| Axe | Score | Changement vs 21h 02/06 | Commentaire |
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

**Niveaux totalement obsolètes — recalcul impossible en l'absence totale de prix et d'ATR.**

| Niveau | Valeur | Statut |
|--------|--------|--------|
| Prix entrée suggéré | **N/A** | Cours indisponible |
| Stop-loss | **N/A** | ATR absent — recalcul impossible |
| Take-profit | **N/A** | ATR absent — recalcul impossible |
| Ratio R/R | **N/A** | Données insuffisantes |

**Derniers niveaux connus (27/05) à titre purement indicatif :** SL $21.78, TP $23.18, ratio R/R 1.5×. Ces niveaux ne sont plus valides sans confirmation technique ni prix.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **CONFIRMÉE** en état **ATTENDRE** — sept snapshots consécutifs sans données, setup totalement non-actionnable.

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ Non vérifiable (prix indisponible) |
| RSI | ❌ Non disponible |
| Volume | 🔴 Indisponible — liquidité non mesurable |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique, suspendu |
| Risque technique | 🔴 Données absentes = risque non quantifiable |
| Score Global | 🔴 55.2/100 → reclassement ATTENDRE maintenu |
| Source données | 🔴 **Erreur totale persistante** : Yahoo et FMP indisponibles sur 7 snapshots |
| Signal sectoriel | 🟡 `NEUTRAL` — pas d'impact concret |

- **Confirmation :** La recommandation **ATTENDRE** est maintenue. Aucun nouveau signal technique, fondamental ni de sentiment n'est apparu sur ce snapshot. Le setup technique du 27/05 (au-dessus MM50, RSI 59.07) reste suspendu. Le Score Global Ajusté de 55.2/100 est un artefact mécanique de l'Agent Recommandation en l'absence de données de marché.
- **Nuances :** Le signal sectoriel `NEUTRAL` persiste. XLF reste dans le top3 mais sans momentum (0.0). Aucune news, événement corporate, flux options ni social n'est détecté sur ce snapshot. Le faux événement FMP `earnings` du 03/06 est un artefact récurrent et ignoré.
- **Rétablissement :** Un snapshot futur avec **données de prix complètes** (Yahoo ou FMP), volume > 1 000 unités, et métriques techniques (RSI, ATR, MM50) justifierait une réévaluation. Un retour du Score Momentum à ≥ 6.0/10 relancerait le setup.
- **Invalidation définitive :** Si le flux de prix ne revient pas sur les prochains snapshots → reclassement **ÉVITER** (ticker non surveillable). Si le prochain prix disponible confirme une clôture sous $21.32 (52w low) → **ÉVITER**.

**Recommandation :** **ATTENDRE**
**Prix cible :** N/A (données insuffisantes)
**Stop-loss :** N/A (prix et ATR absents)
**Horizon :** —
**Conviction :** Très faible — setup technique suspendu par absence totale de données fiables sur sept snapshots consécutifs. Le flux Yahoo et FMP restent indisponibles. Attendre un snapshot avec prix confirmé avant toute réévaluation.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | N/A | 🔴 Extrême anomalie | Données totalement indisponibles sur snapshot 10h |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | N/A | — | Données non disponibles |
| Révisions consensus | N/A | — | Non applicable |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|-------------------|
| Retour données Yahoo/FMP (prix, RSI, ATR, MM50) | Prochain snapshot | Setup technique revalidable | Maintien en ATTENDRE / reclassement ÉVITER |
| Volume > 1 000 unités | 1–3j | Signe de réactivation de la liquidité | Confirmation de l'illiquide si persistant |
| Cours sous $21.32 (52w low) | Immédiat | — | Reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |
| Cassure $23.00 avec volume | Variable | Rehaussement en ACHETER | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 21h UTC 02/06
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : **N/A** (données insuffisantes)
- Recommandation précédente : ATTENDRE
- Recommandation révisée : **ATTENDRE**
- Raison principale : Snapshot 10h UTC 03/06 : erreur totale data/latest.json (`No price history`) persistante — 7e snapshot consécutif sans prix, Score Global 55.2/100 (inchangé, artefact mécanique), signal sectoriel NEUTRAL, aucun catalyseur ni news, faux earnings FMP ignoré
- Thèse : 🟡 Confirmée (statu quo non-actionnable, dégradation data persistante)
