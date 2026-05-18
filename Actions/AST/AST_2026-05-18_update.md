# AST — Mise à jour 2026-05-18 (snapshot 23:09 UTC)

> **Date :** 2026-05-18
> **Type :** Update post-pipeline 23:09 UTC
> **Statut données :** [DONNÉES MANQUANTES] — aucun historique de prix disponible
> **Source :** data/latest.json (23:09 UTC), data/recommandations_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/geo_risk_latest.json, data/events_latest.json, data/quant_report_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-18_update.md` (snapshot 22:36 UTC)

| Élément | Snapshot 22:36 UTC | Snapshot 23:09 UTC | Changement |
|---------|-------------------|-------------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| RSI 14j | Placeholder 50 | Placeholder 50 | Aucun changement |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| Erreur Yahoo | `No price history` | `No price history` | Confirmé stable |
| Earnings jour J | Programmé (FMP) | Programmé (FMP) | Aucun résultat reçu |

**Constat :** Le snapshot 23:09 UTC confirme la stabilité de l'absence totale de données de marché pour AST. Aucun cours, volume, RSI, ATR, ni données FMP ne sont disponibles. L'événement earnings programmé ce jour (2026-05-18, source FMP, `days_until: 0`) n'a pas alimenté de données exploitables dans le pipeline. Les données restent strictement identiques au snapshot 22:36 UTC.

---

## 2. Mise à jour technique

| Métrique | Valeur précédente | Valeur actuelle (23:09 UTC) | Variation |
|----------|-------------------|---------------------------|-----------|
| Cours | — | [DONNÉES MANQUANTES] | — |
| RSI 14j | — | Placeholder 50 (agent) | — |
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

- **Sentiment retail :** 0 mentions Reddit, score 0/10 — `social_sentiment_2026-05-18.json`
- **News :** aucune news détectée pour AST dans `data/news_2026-05-18.json`
- **Options / Unusual activity :** [DONNÉES MANQUANTES] — pas de données de marché
- **Upgrades/downgrades :** [DONNÉES MANQUANTES]
- **Événements :** Earnings programmé le 2026-05-18 (FMP) mais résultats non intégrés (`upcoming_events_latest.json`)
- **Geo / Accounting / Sector / Events :** aucune donnée spécifique pour AST dans les rapports agents

---

## 5. Scoring global (données agents)

> ⚠️ Les scores ci-dessous sont issus de `data/recommandations_2026-05-18.json` mais comportent des valeurs placeholders en l'absence de données réelles.

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
- `AST` — zéro données, erreur Yahoo `No price history`
- `ASTS` (AST SpaceMobile) — données complètes : cours $86.83, RSI 60.85, ATR 7.39, MM50 83.66, volume 23.9M, score opportunité 5.5/10 dans `recommandations_2026-05-18.json`

**Conclusion :** AST est très probablement un **doublon erroné** d'ASTS. Le ticker correct sur NASDAQ pour AST SpaceMobile est **ASTS**.

---

## 7. Conclusion — Thèse

**Verdict : NON ÉVALUABLE / DONNÉES MANQUANTES — CONFIRMÉ AU SNAPSHOT 23:09 UTC**

- Aucune analyse initiale n'a été produite pour AST (pas de `_init.md`)
- Le snapshot technique du jour reste vide (`No price history`) après trois snapshots (21:23, 22:36 et 23:09 UTC)
- Les earnings du jour n'ont pas alimenté de données exploitables dans le pipeline
- Le scoring agent est entièrement basé sur des placeholders (RSI 50, scores neutres 5.0–6.5)
- **Aucun changement significatif** détecté entre les trois snapshots du jour
- Présence confirmée d'un doublon probable avec ASTS

**Recommandation immédiate :**
1. **Supprimer `AST` de `config/watchlist.json`** ou le marquer `excluded` — ASTS est le ticker valide et liquide
2. Si AST fait référence à un autre actif (non AST SpaceMobile), vérifier son symbole boursier sur Yahoo Finance / FMP
3. Relancer `make analyse TICKER=ASTS` pour débloquer l'analyse complète de l'entité sous son ticker correct

**Règle absolue :** Ne pas émettre de prix cible, de stop-loss ou de recommandation d'achat/vente sans données de marché sourcées.
