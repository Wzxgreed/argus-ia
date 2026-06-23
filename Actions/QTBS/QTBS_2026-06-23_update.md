# QTBS — Mise à jour Quotidienne (Snapshot 10h UTC)

> **Date :** 2026-06-23
> **Type :** `_update.md` (snapshot close 22/06 + open 23/06)
> **Source données :** `data/2026-06-23.json` (fetched_at 2026-06-23T10:00:01Z) + `data/recommandations_latest.json` + `data/validation_report.txt` + `data/social_sentiment_latest.json` + `data/fx_exposure_latest.json` + `data/upcoming_events_latest.json` + `data/events_latest.json` + `data/sector_rotation_latest.json`
> **Statut pipeline :** 25/29 tickers OK — 🔴 [ERROR] QTBS confirmé

---

## 1. Résumé des changements depuis l'analyse précédente

| Item | Snapshot 21h UTC (22/06) | Snapshot 10h UTC (23/06) | Changement |
|------|--------------------------|--------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | **[DONNÉES MANQUANTES]** | **Aucun changement** |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| Volume 20j | — | — | — |
| Data feed | `error: true` | **`error: true`** | **Bloquant confirmé** |
| Score global | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | **Stable** |
| Earnings | J0 placeholder (22/06) | **J0 placeholder (23/06)** | **Glissement +1j (29e occurrence)** |
| Social sentiment | No data | **No data** | **Stable** |
| FX exposure | 25% export, impact neutre | **25% export, impact neutre** | **Stable** |
| News Yahoo | `[]` | **`[]`** | **Stable** |
| Events corporate | 0 | **0** | **Stable** |
| Contexte sectoriel XLF | Rang 3e/11, momentum 5.08/10 | **Rang 3e/11, momentum 5.45/10** | **Amélioration organique +0.37 pt** |

**Verdict macro :** QTBS reste en **data blackout total** au snapshot 10h UTC du 23/06. Aucune mutation des données brutes vs le snapshot 21h UTC du 22/06 — **59e snapshot consécutif sans changement** depuis au moins le 20 mai 2026. Le placeholder earnings FMP a glissé d'un jour (22/06 → 23/06), marquant la **29e occurrence glissante** de ce placeholder automatique. Aucune news Yahoo, aucun événement corporate, aucune mention retail. Le contexte sectoriel XLF affiche une **amélioration organique** de 5.08 à 5.45/10 (+0.37 pt), le rang 3e/11 est inchangé.

---

## 2. Mise à jour technique

> **[DONNÉES MANQUANTES — FETCH KO CONFIRMÉ]**

- **Cours close :** [UNSOURCED] — `data/2026-06-23.json` retourne `"error": true`, `"reason": "No price history"` pour QTBS (confirmé hors bloc `prices`, ticker absent des 25 tickers OK)
- **RSI 14j :** —
- **ATR 14j :** —
- **MM 50j / 200j :** —
- **Volume relatif vs 20j :** —
- **Max pain options :** —
- **Put/Call ratio :** —

**Impact :** Sans cours et sans ATR, les niveaux de stop-loss et take-profit restent **non calculables**. Le timing technique est indéterminable. L'erreur est stable sur **59 snapshots consécutifs**, excluant toute hypothèse de latence temporaire.

---

## 3. Mise à jour fondamentale

> **[DONNÉES MANQUANTES — FMP ANNUAL ONLY / NO QUOTE]**

- **P/E LTM :** —
- **Forward P/E :** —
- **EV/EBITDA :** —
- **Consensus price target :** —
- **Nombre d'analystes :** —
- **Market cap :** —

**Événement du jour :** Earnings signalé par `data/upcoming_events_latest.json` (source FMP, date 2026-06-23, severity high, days_until=0). **Anomalie confirmée :** ce placeholder J0 a glissé d'un jour vs le snapshot précédent (22/06 → 23/06). Aucun détail EPS/Revenue consensus n'a été récupéré. Le rapport accounting risk (`data/accounting_risk_latest.json`) reste **totalement absent**. Le NLP transcript (`data/transcripts_NLP_latest.json`) est indisponible pour QTBS (plan FMP insuffisant).

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

Aucune mention retail, aucune détection de pump/dump, aucune news Yahoo, aucun événement corporate. Le silence informationnel reste total. Le ticker n'apparaît dans aucun des rapports agents actifs (quant, geo, accounting, sector, events). L'entrée FX exposure est inchangée vs le snapshot 21h UTC du 22/06.

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

**Rotation sectorielle :** Pas de données sectorielles pour QTBS. Le ticker n'est pas classé dans les secteurs SPDR scannés. Contexte sectoriel XLF en amélioration organique : rang 3e/11, momentum 5.45/10 (+0.37 pt vs 5.08 au snapshot 21h UTC du 22/06). Aucun impact direct mesurable.

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

1. **Data blackout persistant :** Le snapshot 10h UTC du 23/06 confirme l'erreur `[ERROR] QTBS: fetch failed — No price history`. Ce bloquant empêche toute analyse technique, fondamentale et quantitative. La stabilité de l'erreur sur **59 snapshots consécutifs** confirme une panne structurelle du data feed, et non un effet de latence temporaire.

2. **Earnings J0 non analysable :** L'événement earnings du 2026-06-23 (source FMP, severity high, days_until=0) est un **placeholder glissant** ayant migré d'un jour vs le snapshot précédent (22/06 → 23/06). Sans cours pré-event, sans consensus EPS/Revenue et sans métriques, il est impossible de mesurer un quelconque impact post-announcement. Ce comportement glissant (29e occurrence) confirme le caractère automatique et non informatif de ce signal.

3. **Score agent inchangé :** La recommandation `ATTENDRE` (55.2/100) reflète une absence de signal plutôt qu'une conviction neutre. Les scores Catalyseur 6.5/10 sont grevés par l'impossibilité de vérification. Le ticker n'apparaît pas dans le quality gate du jour (0 excluded), ce qui confirme une exclusion totale du pipeline de données brutes.

4. **Aucun nouveau détail contextuel :** Le rapport FX exposure (25% export, impact neutre), le sentiment social (0 mentions), les news Yahoo (`[]`) et les événements corporate (aucun) sont tous inchangés vs le snapshot 21h UTC du 22/06. Aucun catalyseur externe n'est détecté. Le contexte sectoriel XLF (rang 3e/11, momentum 5.45/10) est en légère amélioration organique (+0.37 pt) mais sans impact direct mesurable sur QTBS.

5. **Action requise :** Attendre la résolution du fetch de données (vérifier le prochain snapshot). Si les données réapparaissent avec un gap significatif (>±5%), générer un `_update.md` flash pour qualifier l'impact. En l'absence de données, aucune position réelle ou paper trading ne peut être envisagée.

---

*Rapport généré le 2026-06-23. Données : 2026-06-23.json (10h UTC), recommandations_latest.json (QTBS score 55.2), validation_report.txt (4 erreurs dont QTBS), social_sentiment_latest.json (0 mentions), fx_exposure_latest.json (25% export, impact 0.0), upcoming_events_latest.json (J0 placeholder 23/06), events_latest.json (0 événements), sector_rotation_latest.json (XLF rang 3e/11, momentum 5.45/10).*
*Avertissement : ce document est un outil d'analyse, pas un conseil en investissement.*
