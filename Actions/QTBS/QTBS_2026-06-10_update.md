# QTBS — Mise à jour Quotidienne

> **Date :** 2026-06-10 (snapshot 10h UTC)
> **Type :** `_update.md`
> **Source données :** `data/2026-06-10.json` (fetched_at 2026-06-10T10:00:01Z) + `data/recommandations_2026-06-10.json` + `data/quant_2026-06-10.json` + `data/geo_2026-06-10.json` + `data/sector_rotation_2026-06-10.json` + `data/social_sentiment_2026-06-10.json` + `data/fx_exposure_2026-06-10.json` + `data/upcoming_events_2026-06-10.json` + `data/events_2026-06-10.json` + `data/validation_report.txt`
> **Statut pipeline :** 25/29 tickers OK — 🔴 [ERROR] QTBS confirmé snapshot 10h UTC

---

## 1. Résumé des changements depuis l'analyse précédente

| Item | Close 21h UTC (09/06) | Snapshot 10h UTC (10/06) | Changement |
|------|-----------------------|------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | **[DONNÉES MANQUANTES]** | **Aucun changement** |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| Volume 20j | — | — | — |
| Data feed | `error: true` | `error: true` | **Bloquant confirmé** |
| Score global | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | **Stable** |
| Earnings | J0 placeholder (09/06) | **J0 placeholder (10/06)** | **Glissant d'un jour** |

**Verdict macro :** QTBS reste en **data blackout total** au snapshot 10h UTC du 10/06. Aucune mutation vs le close officiel 21h UTC du 09/06 — **44e snapshot consécutif sans changement** depuis au moins le 20 mai 2026. Le placeholder FMP s'est décalé au 10/06, confirmant son caractère **automatique et non une date d'earnings réelle**. Le rapport de validation du jour (`data/validation_report.txt`, 2026-06-10T09:07:21Z) liste explicitement `[ERROR] QTBS: fetch failed — No price history`.

---

## 2. Mise à jour technique

> **[DONNÉES MANQUANTES — FETCH KO CONFIRMÉ]**

- **Cours close :** [UNSOURCED] — `data/2026-06-10.json` retourne `"error": true`, `"reason": "No price history"` (timestamp 2026-06-10T10:00:18Z)
- **RSI 14j :** —
- **ATR 14j :** —
- **MM 50j / 200j :** —
- **Volume relatif vs 20j :** —
- **Max pain options :** —
- **Put/Call ratio :** —

**Impact :** Sans cours et sans ATR, les niveaux de stop-loss et take-profit restent **non calculables**. Le timing technique est indéterminable. L'erreur est stable sur 44 snapshots consécutifs, excluant toute hypothèse de latence temporaire.

---

## 3. Mise à jour fondamentale

> **[DONNÉES MANQUANTES — FMP ANNUAL ONLY / NO QUOTE]**

- **P/E LTM :** —
- **Forward P/E :** —
- **EV/EBITDA :** —
- **Consensus price target :** —
- **Nombre d'analystes :** —
- **Market cap :** —

**Événement du jour :** Earnings signalé par `upcoming_events_2026-06-10.json` (source FMP, date 2026-06-10, severity high, days_until=0). **Anomalie confirmée :** le placeholder J0 a glissé du 09/06 au 10/06, confirmant un **rafraîchissement automatique quotidien** du calendrier FMP et non une date d'earnings réelle. Aucun détail EPS/Revenue consensus n'a été récupéré. Le rapport accounting risk (`data/accounting_risk_2026-06-10.json`) est **totalement absent**. Le NLP transcript (`data/transcripts_NLP_latest.json`) est indisponible pour QTBS (plan FMP insuffisant).

---

## 4. Mise à jour sentiment / options / news

> **[DONNÉES MANQUANTES]**

- **Social sentiment (Reddit) :** No data — `mention_count: 0`, `sentiment_score: 0.0`, `pump_detected: false` (`data/social_sentiment_2026-06-10.json`, 2026-06-10)
- **News filtre Yahoo :** `[]` (liste vide, source Yahoo REST)
- **Upgrades / Downgrades :** —
- **Insider trades :** —
- **Unusual options activity :** —
- **Events corporate :** Aucun événement détecté (`data/events_2026-06-10.json`, 0 événements pour QTBS)

Aucune mention retail, aucune détection de pump/dump, aucune news Yahoo, aucun événement corporate. Le silence informationnel est total. L'alerte `EXTREME_BEARISH` du social sentiment est un artefact algorithmique (score 0.0 par défaut sur absence de données), non un signal réel.

---

## 5. Scoring global (agents recommandation)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|------------|
| Catalyseur | 6.5/10 | 35% | Placeholder earnings J0 = potentiel catalyseur non vérifiable |
| Valorisation | 5.0/10 | 40% | [DONNÉES MANQUANTES] — score neutre par défaut |
| Momentum | 5.0/10 | 25% | [DONNÉES MANQUANTES] — score neutre par défaut |
| **Score Opportunité** | **5.5/10** | — | =(6.5×0.35)+(5.0×0.40)+(5.0×0.25) |
| **Score Global Composite** | **55.2/100** | — | Pas de malus/bonus spécifiques détectés |
| **Action** | **ATTENDRE** | — | Données insuffisantes pour toute recommandation active |

**Pondération régime :** `Unknown` — régime macro non déterminé par l'agent Macro (`data/recommandations_2026-06-10.json` : `"regime_macro": "Unknown"`).

**Malus / Bonus détaillés :**
- Accounting : 0 (rapport absent)
- Geo : 0 (`data/geo_2026-06-10.json` : `"geo_risk_score": 2`, `"exposed": false`, flag 🟢)
- FX : 0 (`data/fx_exposure_2026-06-10.json` : `"fx_impact_score": 0.0`, `"flag": "🟢"`, secteur "Non spécifié", exposure 25% export)
- Event : 0 (placeholder earnings J0 non vérifiable)
- Social : 0 (neutre par absence de données)
- Quant : 0 (insuffisance de signaux historiques, n=0, p-value=null)
- Timing technique : 0 (indéterminable)

**Rotation sectorielle :** Signal `NEUTRAL` détecté (`data/sector_rotation_2026-06-10.json`, 2026-06-10). QTBS n'est pas classé dans les secteurs SPDR scannés. Aucun impact direct mesurable. Anomalie structurelle persistante : tous les momentum_score sectoriels sont à 10.0 avec return_20d/60d NaN et regime UNKNOWN, indiquant un dysfonctionnement du calcul RS vs SPY.

---

## 6. Niveaux SL / TP / Ratio R/R

> **Non calculables.** Absence de cours close et d'ATR 14j.

- **Prix d'entrée suggéré :** —
- **Stop-loss (2×ATR) :** —
- **Take-profit (3×ATR) :** —
- **Ratio R/R :** —

---

## 7. Conclusion — Statut de la thèse

| Question | Réponse |
|----------|---------|
| Thèse confirmée ? | N/A — pas de thèse initiale établie |
| Thèse modifiée ? | N/A |
| Thèse invalidée ? | N/A |
| **Statut** | **🔴 Bloqué data — ATTENDRE** |

**Argumentaire :**

1. **Data blackout persistant :** Le snapshot 10h UTC du 10/06 confirme l'erreur `[ERROR] QTBS: fetch failed — No price history`. Ce bloquant empêche toute analyse technique, fondamentale et quantitative. La stabilité de l'erreur sur **44 snapshots consécutifs** confirme une panne structurelle du data feed, et non un effet de latence temporaire.

2. **Earnings J0 non analysable :** L'événement earnings du 2026-06-10 (source FMP, severity high, days_until=0) est un **placeholder glissant** passé du 09/06 au 10/06. Sans cours pré-event, sans consensus EPS/Revenue et sans métriques, il est impossible de mesurer un quelconque impact post-announcement.

3. **Score agent inchangé :** La recommandation `ATTENDRE` (55.2/100) reflète une absence de signal plutôt qu'une conviction neutre. Les scores Catalyseur 6.5/10 sont grevés par l'impossibilité de vérification. Le ticker n'apparaît pas dans le quality gate du jour (ni OK, ni warning, ni excluded), ce qui confirme une exclusion totale du pipeline.

4. **Action requise :** Attendre la résolution du fetch de données (vérifier le prochain snapshot). Si les données réapparaissent avec un gap significatif (>±5%), générer un `_update.md` flash pour qualifier l'impact. En l'absence de données, aucune position réelle ou paper trading ne peut être envisagée.

---

*Rapport généré le 2026-06-10. Données : 2026-06-10.json (10h UTC), recommandations_2026-06-10.json, quant_2026-06-10.json, geo_2026-06-10.json, sector_rotation_2026-06-10.json, social_sentiment_2026-06-10.json, fx_exposure_2026-06-10.json, upcoming_events_2026-06-10.json, events_2026-06-10.json, validation_report.txt.*
*Avertissement : ce document est un outil d'analyse, pas un conseil en investissement.*
