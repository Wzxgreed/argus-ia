# QTBS — Mise à jour Quotidienne

> **Date :** 2026-05-26 (snapshot 10:00 UTC, post-Memorial Day)
> **Type :** `_update.md`
> **Source données :** `data/latest.json` (fetched_at 2026-05-26T10:00:02Z) + `data/recommandations_latest.json`
> **Statut pipeline :** 🔴 Fetch KO — No price history (confirmé snapshot 10:00)

---

## 1. Résumé des changements depuis l'analyse précédente

| Item | Snapshot 21:00 UTC (25/05) | Snapshot 10:00 UTC (26/05) | Changement |
|------|---------------------------|---------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | **[DONNÉES MANQUANTES]** | **Aucun changement** |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| Volume 20j | — | — | — |
| Earnings (FMP) | J0 (2026-05-25) | **J0 (2026-05-26)** | Décalage source confirmé |
| Data feed | `error: true` | `error: true` | **Bloquant confirmé** |
| Score global | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | **Stable** |

**Verdict macro :** QTBS reste en **data blackout complet** au snapshot 10:00 UTC post-Memorial Day. Aucune mutation vs le snapshot 21:00 UTC du 25/05 — **12e snapshot consécutif sans changement** depuis au moins le 20 mai 2026.

---

## 2. Mise à jour technique

> **[DONNÉES MANQUANTES — FETCH KO CONFIRMÉ]**

- **Cours close :** [UNSOURCED] — `data/latest.json` retourne `"error": true`, `"reason": "No price history"` (timestamp 10:00:21 UTC)
- **RSI 14j :** —
- **ATR 14j :** —
- **MM 50j / 200j :** —
- **Volume relatif vs 20j :** —
- **Max pain options :** —
- **Put/Call ratio :** —

**Impact :** Sans cours et sans ATR, les niveaux de stop-loss et take-profit restent **non calculables**. Le timing technique est indéterminable.

---

## 3. Mise à jour fondamentale

> **[DONNÉES MANQUANTES — FMP ANNUAL ONLY / NO QUOTE]**

- **P/E LTM :** —
- **Forward P/E :** —
- **EV/EBITDA :** —
- **Consensus price target :** —
- **Nombre d'analystes :** —
- **Market cap :** —

**Événement du jour :** Earnings signalé par `upcoming_events_latest.json` (source FMP, severity high, 0j, date 2026-05-26). Aucun détail EPS/Revenue consensus n'a été récupéré. L'event-driven scan (`data/events_latest.json`) ne retourne **aucun événement corporate détecté** pour QTBS.

---

## 4. Mise à jour sentiment / options / news

> **[DONNÉES MANQUANTES]**

- **Social sentiment (Reddit) :** No data — `mention_count: 0`, `sentiment_score: 0.0`, `pump_detected: false`
- **News filtre Yahoo :** —
- **Upgrades / Downgrades :** —
- **Insider trades :** —
- **Unusual options activity :** —

Aucune mention retail, aucune détection de pump/dump. Le silence informationnel est total.

---

## 5. Scoring global (agents recommandation)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|------------|
| Catalyseur | 6.5/10 | 35% | Earnings J0 = potentiel catalyseur, mais non vérifiable |
| Valorisation | 5.0/10 | 40% | [DONNÉES MANQUANTES] — score neutre par défaut |
| Momentum | 5.0/10 | 25% | [DONNÉES MANQUANTES] — score neutre par défaut |
| **Score Opportunité** | **5.5/10** | — | =(6.5×0.35)+(5.0×0.40)+(5.0×0.25) |
| **Score Global Composite** | **55.2/100** | — | Pas de malus/bonus spécifiques détectés |
| **Action** | **ATTENDRE** | — | Données insuffisantes pour toute recommandation active |

**Pondération régime :** Normal (35/40/25) — le régime macro n'est pas déterminé dans le snapshot.

**Malus / Bonus détaillés :**
- Accounting : 0 (rapport absent)
- Geo : 0 (score politique non calculé)
- FX : 0 (exposition non calculable)
- Event : 0 (aucun événement détecté)
- Social : 0 (sentiment neutre)
- Quant : 0 (insuffisance de signaux historiques)
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

1. **Data blackout persistant :** Le snapshot 10:00 UTC confirme l'erreur `[ERROR] QTBS: fetch failed — No price history`. Ce bloquant empêche toute analyse technique, fondamentale et quantitative. La stabilité de l'erreur entre 21:00 UTC (25/05) et 10:00 UTC (26/05) exclut un effet de latence temporaire lié au week-end.
2. **Earnings J0 non analysable :** L'événement earnings du 2026-05-26 (source FMP) est le catalyseur naturel, mais sans cours pré-event, sans consensus EPS/Revenue et sans métriques, il est impossible de mesurer l'impact post-announcement.
3. **Score agent inchangé :** La recommandation `ATTENDRE` (55.2/100) reflète une absence de signal plutôt qu'une conviction neutre. Les scores Catalyseur 6.5/10 sont grevés par l'impossibilité de vérification.
4. **Action requise :** Attendre la résolution du fetch de données (probablement post-earnings, vérifier le prochain snapshot demain matin). Si les données réapparaissent avec un gap significatif (>±5%), générer un `_update.md` flash pour qualifier l'impact.

---

*Rapport généré le 2026-05-26. Données : latest.json (10:00 UTC), recommandations_latest.json, events_latest.json, social_sentiment_latest.json, fx_exposure_latest.json.*
*Avertissement : ce document est un outil d'analyse, pas un conseil en investissement.*
