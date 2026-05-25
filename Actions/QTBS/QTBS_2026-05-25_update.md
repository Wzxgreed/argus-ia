# QTBS — Mise à jour Quotidienne

> **Date :** 2026-05-25
> **Type :** `_update.md`
> **Source données :** `data/latest.json` + `data/recommandations_latest.json` + `data/validation_report.txt`
> **Statut pipeline :** ⚠️ Fetch failed — No price history

---

## 1. Résumé des changements depuis l’analyse précédente

| Item | Analyse précédente (2026-05-24) | Aujourd’hui (2026-05-25) | Changement |
|------|-------------------------------|--------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| Volume 20j | — | — | — |
| Earnings | Preview vide (0j) | **Earnings signalé le 2026-05-25** | Événement J0 |
| Data feed | Aucun historique prix | **Confirmé KO** (`validation_report.txt` ERROR) | Bloquant |
| Score global | — | **55.2/100 (ATTENDRE)** | Par défaut agents |

**Verdict macro :** Le ticker reste en **data blackout** complet. L’événement earnings prévu aujourd’hui ne peut pas être analysé faute de cours, de volumes, de consensus et de métriques techniques.

---

## 2. Mise à jour technique

> **[DONNÉES MANQUANTES — FETCH KO]**

- **Cours close :** [UNSOURCED] — `data/latest.json` retourne `"error": true`, `"reason": "No price history"`
- **RSI 14j :** —
- **ATR 14j :** —
- **MM 50j / 200j :** —
- **Volume relatif vs 20j :** —
- **Max pain options :** —
- **Put/Call ratio :** —

**Impact :** Sans cours et sans ATR, les niveaux de stop-loss et take-profit sont **non calculables**. Le timing technique est indéterminable.

---

## 3. Mise à jour fondamentale

> **[DONNÉES MANQUANTES — FMP ANNUAL ONLY / NO QUOTE]**

- **P/E LTM :** —
- **Forward P/E :** —
- **EV/EBITDA :** —
- **Consensus price target :** —
- **Nombre d’analystes :** —

**Événement du jour :** Earnings signalé par `upcoming_events_latest.json` (source FMP, severity high, 0j). Aucun détail EPS/Revenue consensus n’a été récupéré (template preview vide).

---

## 4. Mise à jour sentiment / options / news

> **[DONNÉES MANQUANTES]**

- **Social sentiment (Reddit) :** No data — `mention_count: 0`, `sentiment_score: 0.0`
- **News filtre Yahoo :** —
- **Upgrades / Downgrades :** —
- **Insider trades :** —
- **Unusual options activity :** —

Aucune mention retail, aucune détection de pump/dump. Le silence informationnel est total.

---

## 5. Scoring global (agents recommandation)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 6.5/10 | 35% | Earnings J0 = potentiel catalyseur, mais non vérifiable |
| Valorisation | 5.0/10 | 40% | [DONNÉES MANQUANTES] — score neutre par défaut |
| Momentum | 5.0/10 | 25% | [DONNÉES MANQUANTES] — score neutre par défaut |
| **Score Opportunité** | **5.5/10** | — | =(6.5×0.35)+(5.0×0.40)+(5.0×0.25) |
| **Score Global Composite** | **55.2/100** | — | Pas de malus/bonus spécifiques détectés |
| **Action** | **ATTENDRE** | — | Données insuffisantes pour toute recommandation active |

---

## 6. Niveaux SL / TP / Ratio R/R

> **Non calculables.** Absence de cours close et d’ATR 14j.

- **Prix d’entrée suggéré :** —
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

1. **Data blackout :** `validation_report.txt` confirme l’erreur `[ERROR] QTBS: fetch failed — No price history`. Ce bloquant empêche toute analyse technique, fondamentale et quantitative.
2. **Earnings J0 non analysable :** L’événement earnings du 2026-05-25 (source FMP) est le catalyseur naturel, mais sans cours pré-évent, sans consensus EPS/Revenue et sans métriques, il est impossible de mesurer l’impact post-announcement.
3. **Score agent par défaut :** La recommandation `ATTENDRE` (55.2/100) reflète une absence de signal plutôt qu’une conviction neutre. Les scores Catalyseur 6.5/10 sont grevés par l’impossibilité de vérification.
4. **Action requise :** Attendre la résolution du fetch de données (probablement post-earnings, vérifier le prochain snapshot demain matin). Si les données réapparaissent avec un gap significatif (>±5%), générer un `_update.md` flash pour qualifier l’impact.

---

*Rapport généré le 2026-05-25. Données : latest.json, recommandations_latest.json, validation_report.txt.*
*Avertissement : ce document est un outil d’analyse, pas un conseil en investissement.*
