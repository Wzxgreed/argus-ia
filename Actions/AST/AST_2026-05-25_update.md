# AST — Mise à jour Quotidienne

> **Date :** 2026-05-25
> **Type :** Update après-midi (snapshot 13:00 UTC)
> **Source :** data/latest.json (13:00 UTC), data/recommandations_latest.json, data/quality_report_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-25_update.md` (snapshot 10:00 UTC)

| Élément | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Changement |
|---------|-------------------|-------------------|------------|
| Erreur Yahoo | `No price history` | `No price history` | **Confirmé stable** |
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| RSI 14j | Placeholder 50 | Placeholder 50 | Aucun changement |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| Earnings jour J | Programmé (FMP) | Programmé (FMP) | **Non résolu** |
| ASTS (doublon) | Cours $96.23 | Cours **$105.86** (+10.01%) | ASTS dynamique, AST statique |

**Constat :** Le snapshot 13:00 UTC confirme la stabilité absolue de l'absence de données de marché pour AST. C'est le **10e snapshot consécutif** (18/05 → 25/05) sans historique de prix. L'événement earnings programmé ce jour (2026-05-25, source FMP, `days_until: 0`) n'a toujours pas alimenté de données exploitables dans le pipeline.

---

## 2. Mise à jour technique

| Indicateur | Valeur snapshot 13:00 UTC | Valeur précédente (10:00 UTC) | Δ |
|-----------|--------------------------|-------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing :** [NON ÉVALUABLE] — absence totale de données techniques.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur snapshot 13:00 UTC | Valeur précédente | Δ |
|---------|--------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

---

## 4. Mise à jour sentiment / options / news

- **News :** aucune entrée Yahoo Finance ni FMP pour AST dans `data/latest.json`
- **Options :** pas de données (max pain, put/call ratio, OI absents)
- **Social sentiment :** 0 mention Reddit, score 0/10, pas de pump détecté
- **Upgrades/downgrades :** pas de consensus analystes disponible (aucun price target, 0 analystes)
- **Quant / Geo / Accounting / Sector / FX / Events :** aucune donnée spécifique pour AST dans les rapports agents

---

## 5. Scoring global

| Axe | Score 2026-05-25 (13:00 UTC) | Pondération | Note |
|-----|-------------------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35% | [NON FONDÉ] — aucun catalyseur vérifiable |
| Valorisation | 5.0/10 (placeholder) | 40% | [NON FONDÉ] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25% | [NON FONDÉ] — pas de cours, pas de momentum |
| **Score Opportunité** | **5.5/10** | — | Placeholder — **non utilisable pour décision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |
| **Score Global Ajusté** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)
**Timing :** Neutre
**Horizon :** —

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

---

## 6. Niveaux SL / TP / Ratio R/R

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

---

## 7. Conclusion — État de la thèse

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — CONFIRMÉE AU SNAPSHOT 13:00 UTC**

AST n'est pas évaluable en l'état. La situation est strictement inchangée depuis le snapshot 10:00 UTC :

1. **Anomalie structurelle confirmée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ, liquide, données complètes). ASTS affiche aujourd'hui un cours de **$105.86** (+10.01%, volume 30.6M, RSI 74.5) avec un forward P/E de −356, market cap $41B, et un earnings le 2026-08-10.
2. **Earnings du jour non exploitable :** FMP signale un earnings AST le 2026-05-25, mais sans historique de cours, le résultat ne peut être corrélé à un mouvement de marché ni intégré au scoring.
3. **Qualité des données :** AST fait partie des 4 tickers KO sur 26 requêtés (`tickers_ko: 4` dans `data/latest.json`), aux côtés d'AXA, CYTOMX, QTBS. AST est absent du quality gate (alors qu'ASTS y figure indirectement via les données de marché).

**Recommandation opérationnelle :**
- Résoudre l'anomalie structurelle : supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- Rediriger toute exposition space / telecom satellite vers **ASTS**, ticker validé avec data complètes
- Ne pas engager de capital sur AST tant que les données de cours ne sont pas disponibles

---

*Rapport généré à partir des fichiers data/latest.json (snapshot 13:00 UTC), data/recommandations_latest.json, data/quality_report_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json — aucune donnée hallucinée.*
