# AST — Mise à jour 2026-05-20 (snapshot 10:00 UTC)

> **Date :** 2026-05-20
> **Type :** Update post-pipeline matin
> **Statut données :** [DONNÉES MANQUANTES] — aucun historique de prix disponible
> **Source :** data/latest.json (10:00 UTC), data/recommandations_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/geo_risk_latest.json, data/events_latest.json, data/quant_report_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-19_update.md` (snapshot final 21:00 UTC)

| Élément | 2026-05-19 (21:00 UTC) | 2026-05-20 (10:00 UTC) | Changement |
|---------|------------------------|------------------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Confirmé stable (8ᵉ snapshot consécutif) |
| RSI 14j | Placeholder 50 | Placeholder 50 | Confirmé stable |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Confirmé stable |
| Erreur Yahoo | `No price history` | `No price history` | Confirmé stable (timestamp 10:00:15 UTC) |
| Earnings J=0 | Programmé (19/05, FMP) | Programmé (20/05, FMP) | Reporté d'un jour dans upcoming_events |
| Quality Gate | Non listé | Non listé | Confirmé |
| Scores agents | 55.2/100 (placeholder) | 55.2/100 (placeholder) | Aucun changement |
| ASTS (doublon) | $84.82 / RSI 60.87 | $88.10 / RSI 63.39 / +1.46% session | Hausse continue, volume 21.56M (1.09× moy. 20j), ATR 7.95 |

**Constat :** Le snapshot du 20/05 confirme la **stabilité totale de l'absence de données** pour AST. Huit snapshots consécutifs sans cours, volume, RSI, ATR ni donnée FMP (21:23, 22:36, 23:09 UTC le 18/05 ; 10:00, 13:00, 17:00, 21:00 UTC le 19/05 ; 10:00 UTC le 20/05). L'événement earnings source FMP bascule de J=0 le 19/05 à J=0 le 20/05 sans alimenter de résultats exploitables. AST reste absent du quality gate ; ASTS est le seul ticker référencé avec données complètes.

---

## 2. Mise à jour technique

| Métrique | Valeur précédente (19/05) | Valeur actuelle (20/05) | Variation |
|----------|---------------------------|-------------------------|-----------|
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
- **Événements :** Earnings programmé le 2026-05-20 (FMP, `days_until: 0`) mais résultats non intégrés (`upcoming_events_latest.json`)
- **Geo :** score géo 2/10, pas d'exposition — `geo_risk_latest.json`
- **FX :** exposition 25%, impact neutre (score 0.0) — pas de signal

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
- `ASTS` (AST SpaceMobile) — données complètes : cours $88.10, RSI 63.39, ATR 7.95, MM50 83.62, volume 21.56M (1.09× moy. 20j), consensus $92.25 (10 analystes), score opportunité 5.0/10 dans `recommandations_latest.json`

**Conclusion :** AST est très probablement un **doublon erroné** d'ASTS. Le ticker correct sur NASDAQ pour AST SpaceMobile est **ASTS**.

---

## 7. Conclusion — Thèse

**Verdict : NON ÉVALUABLE / DONNÉES MANQUANTES — CONFIRMÉ AU SNAPSHOT 10:00 UTC (20/05)**

- Aucune analyse initiale n'a été produite pour AST (pas de `_init.md`)
- Le snapshot technique du jour reste vide (`No price history`) après huit snapshots consécutifs (21:23, 22:36, 23:09 UTC le 18/05 ; 10:00, 13:00, 17:00, 21:00 UTC le 19/05 ; 10:00 UTC le 20/05)
- Les earnings programmés le 18/05, 19/05 puis 20/05 n'ont pas alimenté de données exploitables dans le pipeline
- Le scoring agent est entièrement basé sur des placeholders (RSI 50, scores neutres 5.0–6.5)
- **Aucun changement significatif** détecté entre les snapshots du 19/05 et du 20/05
- AST n'est pas référencé dans le quality gate (alors que ASTS l'est)
- Présence confirmée d'un doublon probable avec ASTS

**Recommandation immédiate :**
1. **Supprimer `AST` de `config/watchlist.json`** ou le marquer `excluded` — ASTS est le ticker valide et liquide
2. Si AST fait référence à un autre actif (non AST SpaceMobile), vérifier son symbole boursier sur Yahoo Finance / FMP
3. Relancer `make analyse TICKER=ASTS` pour débloquer l'analyse complète de l'entité sous son ticker correct

**Règle absolue :** Ne pas émettre de prix cible, de stop-loss ou de recommandation d'achat/vente sans données de marché sourcées.
