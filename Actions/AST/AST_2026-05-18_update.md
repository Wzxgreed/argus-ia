# AST — Mise à jour 2026-05-18

> **Date :** 2026-05-18
> **Type :** Update post-événement (earnings)
> **Statut données :** [DONNÉES MANQUANTES] — aucun historique de prix disponible
> **Source :** data/latest.json, data/recommandations_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-18_preview.md` — fichier template vide, aucune donnée technique ni fondamentale renseignée. Aucune analyse initiale (`_init.md`) n'existe pour ce ticker.

**État actuel :**
- `data/latest.json` (snapshot 21:23 UTC) retourne **erreur** pour AST : `No price history`
- Aucun cours, volume, RSI, ATR, MM50/200, ni données FMP ne sont disponibles
- Événement earnings programmé ce jour (2026-05-18, source FMP) mais résultats non présents dans le snapshot
- Aucune news détectée pour AST dans `data/news_2026-05-18.json`

**Changement significatif :** Impossible à évaluer — absence totale de données de marché.

---

## 2. Mise à jour technique

| Métrique | Valeur précédente | Valeur actuelle | Variation |
|----------|-------------------|-----------------|-----------|
| Cours | — | [DONNÉES MANQUANTES] | — |
| RSI 14j | — | 50 (placeholder) | — |
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
- **News :** aucune news détectée pour AST dans le snapshot du jour
- **Options / Unusual activity :** [DONNÉES MANQUANTES] — pas de données de marché
- **Upgrades/downgrades :** [DONNÉES MANQUANTES]

---

## 5. Scoring global (données agents)

> ⚠️ Les scores ci-dessous sont issus de `data/recommandations_latest.json` mais comportent des valeurs placeholders en l'absence de données réelles.

| Axe | Score |
|-----|-------|
| Catalyseur | 6.5/10 |
| Valorisation | 5.0/10 |
| Momentum | 5.0/10 |
| **Score Opportunité** | **5.5/10** |
| **Score Global** | **55.2/100** |
| **Score Global Ajusté** | **55.2/100** |

**Action suggérée :** ATTENDRE (données insuffisantes pour évaluation fiable)

| Niveau | Valeur |
|--------|--------|
| Prix actuel | [DONNÉES MANQUANTES] |
| Stop-loss | [DONNÉES MANQUANTES] |
| Take-profit | [DONNÉES MANQUANTES] |
| Ratio R/R | — |

---

## 6. Conclusion — Thèse

**Verdict : NON ÉVALUABLE / DONNÉES MANQUANTES**

- Aucune analyse initiale n'a été produite pour AST (pas de `_init.md`)
- Le snapshot technique du jour est vide (`No price history`)
- Les earnings du jour n'ont pas alimenté de données exploitables dans le pipeline
- Le scoring agent est entièrement basé sur des placeholders (RSI 50, scores neutres 5.0–6.5)

**Recommandation immédiate :**
1. Vérifier la validité du symbole boursier AST sur Yahoo Finance / FMP
2. Si AST est un symbole valide mais illiquide / OTC / récemment changé de ticker → le marquer comme `excluded` ou `low priority`
3. Si AST est un symbole erroné (ex: AST SpaceMobile = ASTS) → corriger `config/watchlist.json`
4. Relancer `make analyse TICKER=AST` après correction

**Règle absolue :** Ne pas émettre de prix cible, de stop-loss ou de recommandation d'achat/vente sans données de marché sourcées.
