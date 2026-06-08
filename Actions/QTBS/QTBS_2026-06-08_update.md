# QTBS — Mise à jour Quotidienne

> **Date :** 2026-06-08 (snapshot 13h UTC)
> **Type :** `_update.md`
> **Source données :** `data/latest.json` (fetched_at 2026-06-08T13:00:01Z) + `data/recommandations_latest.json` + `data/upcoming_events_latest.json` + `data/events_latest.json` + `data/social_sentiment_latest.json` + `data/fx_exposure_latest.json` + `data/sector_rotation_latest.json` + `data/validation_report.txt`
> **Statut pipeline :** 🔴 Fetch KO confirmé snapshot 13h UTC

---

## 1. Résumé des changements depuis l'analyse précédente

| Item | Snapshot 10h UTC (08/06) | Snapshot 13h UTC (08/06) | Changement |
|------|--------------------------|--------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | **[DONNÉES MANQUANTES]** | **Aucun changement** |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| Volume 20j | — | — | — |
| Data feed | `error: true` | `error: true` | **Bloquant confirmé** |
| Score global | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | **Stable** |
| Earnings | J0 (08/06) placeholder | **J0 (08/06) placeholder** | **Stable** |

**Verdict macro :** QTBS reste en **data blackout complet** au snapshot 13h UTC du 08/06. Aucune mutation vs le snapshot 10h UTC — **39e snapshot consécutif sans changement** depuis au moins le 20 mai 2026. Le placeholder FMP a été maintenu au 2026-06-08, confirmant son caractère automatique et non une date d'earnings réelle.

---

## 2. Mise à jour technique

> **[DONNÉES MANQUANTES — FETCH KO CONFIRMÉ]**

- **Cours close :** [UNSOURCED] — `data/latest.json` retourne `"error": true`, `"reason": "No price history"` (timestamp 2026-06-08T13:00:19Z)
- **RSI 14j :** —
- **ATR 14j :** —
- **MM 50j / 200j :** —
- **Volume relatif vs 20j :** —
- **Max pain options :** —
- **Put/Call ratio :** —

**Impact :** Sans cours et sans ATR, les niveaux de stop-loss et take-profit restent **non calculables**. Le timing technique est indéterminable. Le rapport de validation du jour (`data/validation_report.txt`, 2026-06-08T12:07:19Z) liste explicitement `[ERROR] QTBS: fetch failed — No price history`, confirmant l'exclusion totale du pipeline data.

---

## 3. Mise à jour fondamentale

> **[DONNÉES MANQUANTES — FMP ANNUAL ONLY / NO QUOTE]**

- **P/E LTM :** —
- **Forward P/E :** —
- **EV/EBITDA :** —
- **Consensus price target :** —
- **Nombre d'analystes :** —
- **Market cap :** —

**Événement du jour :** Earnings signalé par `upcoming_events_latest.json` (source FMP, date 2026-06-08, severity high, days_until=0). **Anomalie confirmée :** la date J0 est restée figée au 2026-06-08, confirmant un **placeholder FMP automatique** et non une date d'earnings réelle. Aucun détail EPS/Revenue consensus n'a été récupéré. Le rapport accounting risk (`data/accounting_risk_latest.json`) reste **totalement absent**. Le NLP transcript (`data/transcripts_NLP_latest.json`) est indisponible pour QTBS (plan FMP insuffisant).

---

## 4. Mise à jour sentiment / options / news

> **[DONNÉES MANQUANTES]**

- **Social sentiment (Reddit) :** No data — `mention_count: 0`, `sentiment_score: 0.0`, `pump_detected: false` (`data/social_sentiment_latest.json`, 2026-06-08)
- **News filtre Yahoo :** `[]` (liste vide, source Yahoo REST)
- **Upgrades / Downgrades :** —
- **Insider trades :** —
- **Unusual options activity :** —
- **Events corporate :** Aucun événement détecté (`data/events_latest.json`, 0 événements pour QTBS)

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

**Pondération régime :** `Unknown` — régime macro non déterminé par l'agent Macro (`data/recommandations_latest.json` : `"regime_macro": "Unknown"`).

**Malus / Bonus détaillés :**
- Accounting : 0 (rapport absent)
- Geo : 0 (QTBS absent du geo_risk scan)
- FX : 0 (`fx_exposure_latest.json` : `fx_impact_score: 0.0`, `flag: 🟢`, `divergence_flag: aligned`)
- Event : 0 (placeholder earnings J0 non vérifiable)
- Social : 0 (neutre par absence de données)
- Quant : 0 (insuffisance de signaux historiques, n=0, p-value=1.0)
- Timing technique : 0 (indéterminable)

**Rotation sectorielle :** Signal `NEUTRAL` détecté (`data/sector_rotation_latest.json`, 2026-06-08). QTBS n'est pas classé dans les secteurs SPDR scannés. Aucun impact direct mesurable.

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

1. **Data blackout persistant :** Le snapshot 13h UTC du 08/06 confirme l'erreur `[ERROR] QTBS: fetch failed — No price history`. Ce bloquant empêche toute analyse technique, fondamentale et quantitative. La stabilité de l'erreur sur **39 snapshots consécutifs** confirme une panne structurelle du data feed, et non un effet de latence temporaire.

2. **Earnings J0 non analysable :** L'événement earnings du 2026-06-08 (source FMP, severity high, days_until=0) est un **placeholder glissant** resté figé au 08/06. Sans cours pré-event, sans consensus EPS/Revenue et sans métriques, il est impossible de mesurer un quelconque impact post-announcement.

3. **Score agent inchangé :** La recommandation `ATTENDRE` (55.2/100) reflète une absence de signal plutôt qu'une conviction neutre. Les scores Catalyseur 6.5/10 sont grevés par l'impossibilité de vérification. Le ticker n'apparaît pas dans le quality gate du jour (ni OK, ni warning, ni excluded), ce qui confirme une exclusion totale du pipeline.

4. **Action requise :** Attendre la résolution du fetch de données (vérifier le prochain snapshot). Si les données réapparaissent avec un gap significatif (>±5%), générer un `_update.md` flash pour qualifier l'impact. En l'absence de données, aucune position réelle ou paper trading ne peut être envisagée.

---

*Rapport généré le 2026-06-08. Données : latest.json (13h UTC), recommandations_latest.json, events_latest.json, social_sentiment_latest.json, fx_exposure_latest.json, upcoming_events_latest.json, validation_report.txt.*
*Avertissement : ce document est un outil d'analyse, pas un conseil en investissement.*
