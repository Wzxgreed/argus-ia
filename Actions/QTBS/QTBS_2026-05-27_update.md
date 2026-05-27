# QTBS — Mise à jour Quotidienne

> **Date :** 2026-05-27 (snapshot 13:00 UTC)
> **Type :** `_update.md`
> **Source données :** `data/latest.json` (fetched_at 2026-05-27T13:00:02Z) + `data/recommandations_latest.json` + `data/upcoming_events_latest.json` + `data/events_latest.json` + `data/social_sentiment_latest.json` + `data/fx_exposure_latest.json` + `data/sector_rotation_latest.json`
> **Statut pipeline :** 🔴 Fetch KO — No price history (confirmé snapshot 13:00)

---

## 1. Résumé des changements depuis l'analyse précédente

| Item | Snapshot 10:00 UTC (27/05) | Snapshot 13:00 UTC (27/05) | Changement |
|------|---------------------------|---------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | **[DONNÉES MANQUANTES]** | **Aucun changement** |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| Volume 20j | — | — | — |
| Data feed | `error: true` | `error: true` | **Bloquant confirmé** |
| Score global | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | **Stable** |
| Earnings | J0 (27/05) | **J0 (27/05)** | **Placeholder glissant inchangé** |

**Verdict macro :** QTBS reste en **data blackout complet** au snapshot 13:00 UTC du 27/05. Aucune mutation vs le snapshot 10:00 UTC — **16e snapshot consécutif sans changement** depuis au moins le 20 mai 2026. L'earnings signalé par FMP reste à J0 (27/05) : il s'agit d'un **placeholder glissant**, non d'un événement daté fiable.

---

## 2. Mise à jour technique

> **[DONNÉES MANQUANTES — FETCH KO CONFIRMÉ]**

- **Cours close :** [UNSOURCED] — `data/latest.json` retourne `"error": true`, `"reason": "No price history"` (timestamp 13:00:20 UTC)
- **RSI 14j :** —
- **ATR 14j :** —
- **MM 50j / 200j :** —
- **Volume relatif vs 20j :** —
- **Max pain options :** —
- **Put/Call ratio :** —

**Impact :** Sans cours et sans ATR, les niveaux de stop-loss et take-profit restent **non calculables**. Le timing technique est indéterminable. La quality gate du jour (`data/quality_report_latest.json`, date 2026-05-17) ne liste pas QTBS parmi les 7 tickers scannés, confirmant une exclusion totale du pipeline data.

---

## 3. Mise à jour fondamentale

> **[DONNÉES MANQUANTES — FMP ANNUAL ONLY / NO QUOTE]**

- **P/E LTM :** —
- **Forward P/E :** —
- **EV/EBITDA :** —
- **Consensus price target :** —
- **Nombre d'analystes :** —
- **Market cap :** —

**Événement du jour :** Earnings signalé par `upcoming_events_latest.json` (source FMP, date 2026-05-27, severity high, days_until=0). **Anomalie détectée :** la date J0 glisse de jour en jour sans résolution (26/05 → 27/05), ce qui confirme un **placeholder FMP** et non une date d'earnings réelle. Aucun détail EPS/Revenue consensus n'a été récupéré. L'event-driven scan (`data/events_latest.json`) ne retourne **aucun événement corporate détecté** pour QTBS. Le rapport accounting risk (`data/accounting_risk_latest.json`) est **totalement absent**. Le NLP transcript (`data/transcripts_NLP_latest.json`) est indisponible pour QTBS (plan FMP insuffisant).

---

## 4. Mise à jour sentiment / options / news

> **[DONNÉES MANQUANTES]**

- **Social sentiment (Reddit) :** No data — `mention_count: 0`, `sentiment_score: 0.0`, `pump_detected: false`
- **News filtre Yahoo :** `[]` (liste vide, source Yahoo REST)
- **Upgrades / Downgrades :** —
- **Insider trades :** —
- **Unusual options activity :** —

Aucune mention retail, aucune détection de pump/dump, aucune news Yahoo. Le silence informationnel est total. L'alerte `EXTREME_BEARISH` du social sentiment est un artefact algorithmique (score 0.0 par défaut sur absence de données), non un signal réel.

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

**Pondération régime :** Normal (35/40/25) — le régime macro est déclaré `Unknown` dans le snapshot du jour.

**Malus / Bonus détaillés :**
- Accounting : 0 (rapport absent — pas de données pour calculer M-Score, Z-Score, F-Score, Sloan)
- Geo : 0 (score politique 2/10, pas d'exposition détectée)
- FX : 0 (exposition 25% mais impact nul, DXY plat)
- Event : 0 (aucun événement corporate détecté — le placeholder earnings J0 n'est pas un événement vérifiable)
- Social : 0 (sentiment neutre par absence de données)
- Quant : 0 (insuffisance de signaux historiques, n=0)
- Timing technique : 0 (indéterminable)

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

1. **Data blackout persistant :** Le snapshot 13:00 UTC confirme l'erreur `[ERROR] QTBS: fetch failed — No price history`. Ce bloquant empêche toute analyse technique, fondamentale et quantitative. La stabilité de l'erreur sur 16 snapshots consécutifs confirme une panne structurelle du data feed, et non un effet de latence temporaire.

2. **Earnings J0 non analysable :** L'événement earnings du 2026-05-27 (source FMP, severity high, days_until=0) est un **placeholder glissant** (la date J0 avance de jour en jour sans résolution). Sans cours pré-event, sans consensus EPS/Revenue et sans métriques, il est impossible de mesurer un quelconque impact post-announcement.

3. **Score agent inchangé :** La recommandation `ATTENDRE` (55.2/100) reflète une absence de signal plutôt qu'une conviction neutre. Les scores Catalyseur 6.5/10 sont grevés par l'impossibilité de vérification. Le ticker n'apparaît pas dans le quality gate du jour (ni OK, ni warning, ni excluded), ce qui confirme une exclusion totale du pipeline.

4. **Action requise :** Attendre la résolution du fetch de données (vérifier le prochain snapshot). Si les données réapparaissent avec un gap significatif (>±5%), générer un `_update.md` flash pour qualifier l'impact. En l'absence de données, aucune position réelle ou paper trading ne peut être envisagée.

---

*Rapport généré le 2026-05-27. Données : latest.json (13:00 UTC), recommandations_latest.json, events_latest.json, social_sentiment_latest.json, fx_exposure_latest.json, upcoming_events_latest.json, quality_report_latest.json.*
*Avertissement : ce document est un outil d'analyse, pas un conseil en investissement.*
