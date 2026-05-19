# AST — Mise à jour 2026-05-19 (snapshot 13:00 UTC)

> **Date :** 2026-05-19
> **Type :** Update post-pipeline 13:00 UTC
> **Statut données :** [DONNÉES MANQUANTES] — aucun historique de prix disponible
> **Source :** data/latest.json (13:00 UTC), data/recommandations_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/geo_risk_latest.json, data/events_latest.json, data/quant_report_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-19_update.md` (snapshot 10:00 UTC)

| Élément | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Changement |
|---------|-------------------|-------------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Confirmé stable |
| RSI 14j | Placeholder 50 | Placeholder 50 | Confirmé stable |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Confirmé stable |
| Erreur Yahoo | `No price history` | `No price history` | Confirmé stable (timestamp 13:00:14 UTC) |
| Earnings J=0 | Programmé (19/05, FMP) | Programmé (19/05, FMP) | Résultats toujours non intégrés |
| Quality Gate | Non listé | Non listé | Confirmé |
| Scores agents | 55.2/100 (placeholder) | 55.2/100 (placeholder) | Aucun changement |

**Constat :** Le snapshot 13:00 UTC confirme la **stabilité totale de l'absence de données** pour AST. Aucun cours, volume, RSI, ATR, ni donnée FMP n'est disponible. L'événement earnings programmé à J=0 (source FMP) n'a pas alimenté de résultats exploitables dans le pipeline. AST n'est pas référencé dans le `quality_gate` (contrairement à ASTS, statut `ok`).

---

## 2. Mise à jour technique

| Métrique | Valeur précédente (10:00 UTC) | Valeur actuelle (13:00 UTC) | Variation |
|----------|------------------------------|----------------------------|-----------|
| Cours | — | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 | Placeholder 50 | — |
| ATR 14j | — | [DONNÉES MANQUANTES] | — |
| MM 50j | — | [DONNÉES MANQUANTES] | — |
| MM 200j | — | [DONNÉES MANQUANTES] | — |
| Volume relatif | — | [DONNÉES MANQUANTES] | — |

**Verdict timing :** NON ÉVALUABLE — aucune donnée de cours pour calculer les niveaux techniques ou le momentum.

---

## 3. Mise à jour fondamentale

Aucune donnée fondamentale (P/E, EV/EBITDA, FCF, margins, consensus) n'est présente dans `data/latest.json` pour AST. Le Filtre Qualité 6 critères ne peut pas être calculé.

---

## 4. Mise à jour sentiment / options / news

- **Sentiment retail :** 0 mentions Reddit, score 0/10 — `social_sentiment_latest.json`
- **News :** aucune news détectée pour AST dans `data/news_latest.json`
- **Options / Unusual activity :** [DONNÉES MANQUANTES] — pas de données de marché
- **Upgrades/downgrades :** [DONNÉES MANQUANTES]
- **Événements :** Earnings programmé le 2026-05-19 (FMP, `days_until: 0`) mais résultats non intégrés (`upcoming_events_latest.json`)
- **Geo / FX :** score géo non listé (geo_risk_latest.json), exposition FX 25% avec impact neutre (score 0.0) — pas de signal

---

## 5. Scoring global (données agents)

> ⚠️ Les scores ci-dessous sont issus de `data/recommandations_latest.json` et comportent des valeurs placeholders en l'absence de données réelles.

| Axe | Score | Note |
|-----|-------|------|
| Catalyseur | 6.5/10 | Placeholder (neutre) |
| Valorisation | 5.0/10 | Placeholder (neutre) |
| Momentum | 5.0/10 | Placeholder (neutre) |
| **Score Opportunité** | **5.5/10** | Placeholder |
| **Score Global** | **55.2/100** | Placeholder |
| **Score Global Ajusté** | **55.2/100** | Placeholder |

**Action suggérée :** ATTENDRE (données insuffisantes pour évaluation fiable)

| Niveau | Valeur |
|--------|--------|
| Prix actuel | [DONNÉES MANQUANTES] |
| Stop-loss | [DONNÉES MANQUANTES] |
| Take-profit | [DONNÉES MANQUANTES] |
| Ratio R/R | — |

---

## 6. Anomalie structurelle — AST vs ASTS

La watchlist (`config/watchlist.json`) contient **deux tickers** pour la même entité probable :
- `AST` — zéro données, erreur Yahoo `No price history`, non listé dans le quality gate
- `ASTS` (AST SpaceMobile) — données complètes : cours $86.83, RSI 60.85, ATR 7.39, MM50 83.66, volume 23.9M, score opportunité 5.5/10 dans `recommandations_latest.json`, statut `ok` dans le quality gate

**Conclusion :** AST est très probablement un **doublon erroné** d'ASTS. Le ticker correct sur NASDAQ pour AST SpaceMobile est **ASTS**.

---

## 7. Conclusion — Thèse

**Verdict : NON ÉVALUABLE / DONNÉES MANQUANTES — CONFIRMÉ AU SNAPSHOT 13:00 UTC (19/05)**

- Aucune analyse initiale n'a été produite pour AST (pas de `_init.md`)
- Le snapshot technique du jour reste vide (`No price history`) après cinq snapshots consécutifs (21:23, 22:36, 23:09 UTC le 18/05 ; 10:00 UTC, 13:00 UTC le 19/05)
- Les earnings programmés le 18/05 puis le 19/05 n'ont pas alimenté de données exploitables dans le pipeline
- Le scoring agent est entièrement basé sur des placeholders (RSI 50, scores neutres 5.0–6.5)
- **Aucun changement significatif** détecté entre les snapshots du 19/05
- AST n'est pas référencé dans le quality gate (alors que ASTS l'est, statut `ok`)
- Présence confirmée d'un doublon probable avec ASTS

**Recommandation immédiate :**
1. **Supprimer `AST` de `config/watchlist.json`** ou le marquer `excluded` — ASTS est le ticker valide et liquide
2. Si AST fait référence à un autre actif (non AST SpaceMobile), vérifier son symbole boursier sur Yahoo Finance / FMP
3. Relancer `make analyse TICKER=ASTS` pour débloquer l'analyse complète de l'entité sous son ticker correct

**Règle absolue :** Ne pas émettre de prix cible, de stop-loss ou de recommandation d'achat/vente sans données de marché sourcées.
