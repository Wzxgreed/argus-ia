# QTBS — Mise à jour Quotidienne (Snapshot 13h UTC)

> **Date :** 2026-06-17 (snapshot 13h UTC)
> **Type :** `_update_13h.md`
> **Source données :** `data/2026-06-17.json` (fetched_at 2026-06-17T13:00:01Z) + `data/recommandations_latest.json` + `data/validation_report.txt` + `data/social_sentiment_latest.json` + `data/fx_exposure_latest.json` + `data/upcoming_events_latest.json` + `data/events_latest.json`
> **Statut pipeline :** 25/29 tickers OK — 🔴 [ERROR] QTBS confirmé snapshot 13h UTC

---

## 1. Résumé des changements depuis l'analyse précédente

| Item | Snapshot 10h UTC (17/06) | Snapshot 13h UTC (17/06) | Changement |
|------|--------------------------|--------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | **[DONNÉES MANQUANTES]** | **Aucun changement** |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| Volume 20j | — | — | — |
| Data feed | `error: true` | `error: true` | **Bloquant confirmé** |
| Score global | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | **Stable** |
| Earnings | J0 placeholder (17/06) | **J0 placeholder (17/06)** | **Stable** |
| Social sentiment | No data | **No data** | **Stable** |
| FX exposure | 25% export, impact neutre | **25% export, impact neutre** | **Stable** |
| News Yahoo | `[]` | **`[]`** | **Stable** |
| Timestamp erreur | 10:00:19Z | **13:00:19Z** | **Fetch ré-échoué** |
| Snapshots sans mutation | 54 | **55** | **+1 snapshot** |

**Verdict macro :** QTBS reste en **data blackout total** au snapshot 13h UTC du 17/06. Aucune mutation des données brutes vs le snapshot 10h UTC du 17/06 — **55e snapshot consécutif sans changement** depuis au moins le 20 mai 2026. Le placeholder earnings J0 est figé au 17/06 entre les deux snapshots (pas de glissement mécanique cette fois, car déjà à J0). Aucune news Yahoo, aucun événement corporate, aucune mention retail.

---

## 2. Mise à jour technique

> **[DONNÉES MANQUANTES — FETCH KO CONFIRMÉ]**

- **Cours close :** [UNSOURCED] — `data/2026-06-17.json` (13h UTC) retourne `"error": true`, `"reason": "No price history"` (timestamp 2026-06-17T13:00:19Z)
- **RSI 14j :** —
- **ATR 14j :** —
- **MM 50j / 200j :** —
- **Volume relatif vs 20j :** —
- **Max pain options :** —
- **Put/Call ratio :** —

**Impact :** Sans cours et sans ATR, les niveaux de stop-loss et take-profit restent **non calculables**. Le timing technique est indéterminable. L'erreur est stable sur 55 snapshots consécutifs, excluant toute hypothèse de latence temporaire.

---

## 3. Mise à jour fondamentale

> **[DONNÉES MANQUANTES — FMP ANNUAL ONLY / NO QUOTE]**

- **P/E LTM :** —
- **Forward P/E :** —
- **EV/EBITDA :** —
- **Consensus price target :** —
- **Nombre d'analystes :** —
- **Market cap :** —

**Événement du jour :** Earnings signalé par `data/upcoming_events_latest.json` (source FMP, date 2026-06-17, severity high, days_until=0). **Anomalie confirmée :** ce placeholder J0 est figé au 17/06 entre le snapshot 10h et 13h (pas de glissement mécanique cette fois, car le calendrier FMP a déjà atteint la date glissante). Aucun détail EPS/Revenue consensus n'a été récupéré. Le rapport accounting risk (`data/accounting_risk_latest.json`) reste **totalement absent**. Le NLP transcript (`data/transcripts_NLP_latest.json`) est indisponible pour QTBS (plan FMP insuffisant).

---

## 4. Mise à jour sentiment / options / news

> **[DONNÉES MANQUANTES — AUCUN SIGNAL NOUVEAU]**

- **Social sentiment (Reddit) :** No data — `mention_count: 0`, `sentiment_score: 0.0`, `pump_detected: false`
- **News filtre Yahoo (`data/news_latest.json`) :** `[]` (liste vide, source Yahoo REST)
- **Upgrades / Downgrades :** —
- **Insider trades :** —
- **Unusual options activity :** —
- **Events corporate (`data/events_latest.json`) :** Aucun événement détecté (0 events, 0 tickers_with_events)
- **FX exposure (`data/fx_exposure_latest.json`) :**
  - Exposition : 25% (export)
  - Primary currency : USD
  - FX impact score : **0.0/10** (neutre)
  - Direction : neutral
  - Flag : 🟢

Aucune mention retail, aucune détection de pump/dump, aucune news Yahoo, aucun événement corporate. Le silence informationnel reste total. Le ticker n'apparaît dans aucun des rapports agents actifs (quant, geo, accounting, sector, events). L'entrée FX exposure est inchangée vs le snapshot 10h UTC du 17/06.

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

**Pondération régime :** `Unknown` — régime macro non déterminé par l'agent Macro.

**Malus / Bonus détaillés :**
- Accounting : 0 (rapport absent)
- Geo : 0 (pas de données geo pour QTBS)
- FX : 0 (exposition 25% export mais impact score 0.0)
- Event : 0 (placeholder earnings J0 non vérifiable)
- Social : 0 (neutre par absence de données)
- Quant : 0 (insuffisance de signaux historiques, n=0, p-value=1.0)
- Timing technique : 0 (indéterminable)

**Rotation sectorielle :** Pas de données sectorielles pour QTBS. Le ticker n'est pas classé dans les secteurs SPDR scannés. Contexte sectoriel XLF inchangé : rang 4e/11, momentum 5.32/10. Aucun impact direct mesurable.

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

1. **Data blackout persistant :** Le snapshot 13h UTC du 17/06 confirme l'erreur `[ERROR] QTBS: fetch failed — No price history`. Ce bloquant empêche toute analyse technique, fondamentale et quantitative. La stabilité de l'erreur sur **55 snapshots consécutifs** confirme une panne structurelle du data feed, et non un effet de latence temporaire.

2. **Earnings J0 non analysable :** L'événement earnings du 2026-06-17 (source FMP, severity high, days_until=0) est un **placeholder glissant** figé à la date du jour. Sans cours pré-event, sans consensus EPS/Revenue et sans métriques, il est impossible de mesurer un quelconque impact post-announcement.

3. **Score agent inchangé :** La recommandation `ATTENDRE` (55.2/100) reflète une absence de signal plutôt qu'une conviction neutre. Les scores Catalyseur 6.5/10 sont grevés par l'impossibilité de vérification. Le ticker n'apparaît pas dans le quality gate du jour (0 excluded), ce qui confirme une exclusion totale du pipeline de données brutes.

4. **Aucun nouveau détail contextuel :** Le rapport FX exposure (25% export, impact neutre), le sentiment social (0 mentions), les news Yahoo (`[]`) et les événements corporate (aucun) sont tous inchangés vs le snapshot 10h UTC du 17/06. Aucun catalyseur externe n'est détecté. Le contexte sectoriel XLF (rang 4e/11, momentum 5.32/10) reste inchangé.

5. **Action requise :** Attendre la résolution du fetch de données (vérifier le prochain snapshot). Si les données réapparaissent avec un gap significatif (>±5%), générer un `_update.md` flash pour qualifier l'impact. En l'absence de données, aucune position réelle ou paper trading ne peut être envisagée.

---

*Rapport généré le 2026-06-17. Données : 2026-06-17.json (13h UTC), recommandations_latest.json (QTBS score 55.2), validation_report.txt (5 erreurs dont QTBS), social_sentiment_latest.json (0 mentions), fx_exposure_latest.json (25% export, impact 0.0), upcoming_events_latest.json (J0 placeholder 17/06), events_latest.json (0 événements).*
*Avertissement : ce document est un outil d'analyse, pas un conseil en investissement.*
