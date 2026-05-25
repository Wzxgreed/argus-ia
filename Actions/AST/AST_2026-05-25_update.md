# AST — Mise à jour Quotidienne

> **Date :** 2026-05-25
> **Type :** Update matin (10:00 UTC)
> **Source :** data/latest.json, data/recommandations_latest.json, data/upcoming_events_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Aucun changement significatif.** AST reste dans l'impasse data :
- Snapshot 2026-05-25 10:00 UTC : `error: true`, `reason: "No price history"` — confirmé stable sur 9 snapshots consécutifs (18/05 → 25/05)
- Aucun cours, volume, RSI, ATR, MM, fondamental, ni options disponibles
- Earnings programmé le 2026-05-25 (source FMP, severity high, 0j) — résultats non intégrés au pipeline faute de données de cotation
- AST absent du quality gate et du rapport accounting
- Doublon structurel avec ASTS (AST SpaceMobile) toujours actif

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-05-25 | Valeur précédente (20/05) | Δ |
|-----------|-------------------|---------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | — | — | — |
| ATR 14j | — | — | — |
| MM 50j | — | — | — |
| MM 200j | — | — | — |

**Verdict timing :** [NON ÉVALUABLE] — absence totale de données techniques.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur 2026-05-25 | Valeur précédente | Δ |
|---------|-------------------|-------------------|---|
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
- **Social sentiment :** 0 mention Reddit, score 0/10, pas de pump detecté (`data/social_sentiment_latest.json`)
- **Upgrades/downgrades :** pas de consensus analystes disponible (aucun price target, 0 analystes)

---

## 5. Scoring global

| Axe | Score 2026-05-25 | Pondération | Note |
|-----|------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35% | [NON FONDÉ] — aucun catalyseur vérifiable |
| Valorisation | 5.0/10 (placeholder) | 40% | [NON FONDÉ] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25% | [NON FONDÉ] — pas de cours, pas de momentum |
| **Score Opportunité** | **5.5/10** | — | Placeholder — **non utilisable pour décision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |

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

**Thèse :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES**

AST n'est pas évaluable en l'état. La situation est inchangée depuis le 18/05 :

1. **Anomalie structurelle confirmée :** AST est probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ, liquide, données complètes). ASTS affiche aujourd'hui un cours de $105.86 (+10.01%, volume 30.6M, RSI 74.5) avec un forward P/E de −356, market cap $41B, et un earnings le 2026-08-10.
2. **Earnings du jour non exploitable :** FMP signale un earnings AST le 2026-05-25, mais sans historique de cours, le résultat ne peut être corrélé à un mouvement de marché ni intégré au scoring.
3. **Qualité des données :** AST fait partie des 4 tickers KO sur 26 requêtés (`tickers_ko: 4` dans `data/latest.json`), aux côtés d'AXA, CYTOMX, QTBS.

**Recommandation opérationnelle :**
- Résoudre l'anomalie structurelle : supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- Rediriger toute exposition space / telecom satellite vers **ASTS**, ticker validé avec data complètes
- Ne pas engager de capital sur AST tant que les données de cours ne sont pas disponibles

---

*Rapport généré à partir des fichiers data/latest.json, data/recommandations_latest.json, data/upcoming_events_latest.json — aucune donnée hallucinée.*
