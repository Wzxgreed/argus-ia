# AST — Mise à jour 2026-05-18 (snapshot 22:36 UTC)

> **Date :** 2026-05-18
> **Type :** Update post-snapshot confirmatoire
> **Statut données :** [DONNÉES MANQUANTES] — aucun historique de prix disponible
> **Source :** data/latest.json (22:36 UTC), data/recommandations_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json

---

## 1. Résumé des changements depuis l'analyse précédente

**Analyse précédente :** `AST_2026-05-18_update.md` (snapshot 21:23 UTC)

| Élément | Snapshot 21:23 UTC | Snapshot 22:36 UTC | Changement |
|---------|-------------------|-------------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| RSI 14j | Placeholder 50 | Placeholder 50 | Aucun changement |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | Aucun changement |
| Erreur Yahoo | `No price history` | `No price history` | Confirmé stable |
| Earnings jour J | Programmé (FMP) | Programmé (FMP) | Aucun résultat reçu |

**Constat :** Le snapshot 22:36 UTC confirme la stabilité de l'absence totale de données de marché pour AST. Aucun cours, volume, RSI, ATR, ni données FMP ne sont disponibles. L'événement earnings programmé ce jour (2026-05-18, source FMP, `days_until: 0`) n'a pas alimenté de données exploitables dans le pipeline.

---

## 2. Mise à jour technique

| Métrique | Valeur précédente | Valeur actuelle (22:36 UTC) | Variation |
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

- **Sentiment retail :** 0 mentions Reddit, score 0/10 — `social_sentiment_latest.json`
- **News :** aucune news détectée pour AST dans `data/news_2026-05-18.json` ni `data/news_latest.json`
- **Options / Unusual activity :** [DONNÉES MANQUANTES] — pas de données de marché
- **Upgrades/downgrades :** [DONNÉES MANQUANTES]
- **Événements :** Earnings programmé le 2026-05-18 (FMP) mais résultats non intégrés (`upcoming_events_latest.json`)

---

## 5. Scoring global (données agents)

> ⚠️ Les scores ci-dessous sont issus de `data/recommandations_latest.json` mais comportent des valeurs placeholders en l'absence de données réelles.

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

## 6. Conclusion — Thèse

**Verdict : NON ÉVALUABLE / DONNÉES MANQUANTES — CONFIRMÉ AU SNAPSHOT 22:36 UTC**

- Aucune analyse initiale n'a été produite pour AST (pas de `_init.md`)
- Le snapshot technique du jour reste vide (`No price history`) après deux snapshots (21:23 et 22:36 UTC)
- Les earnings du jour n'ont pas alimenté de données exploitables dans le pipeline
- Le scoring agent est entièrement basé sur des placeholders (RSI 50, scores neutres 5.0–6.5)
- **Aucun changement significatif** détecté entre les deux snapshots du jour

**Recommandation immédiate :**
1. Vérifier la validité du symbole boursier AST sur Yahoo Finance / FMP
2. Si AST est un symbole valide mais illiquide / OTC / récemment changé de ticker → le marquer comme `excluded` ou `low priority` dans `config/watchlist.json`
3. **Si AST fait référence à AST SpaceMobile** → corriger `config/watchlist.json` pour utiliser `ASTS` (données disponibles : $86.83, RSI réel, ATR, MM50/200)
4. Relancer `make analyse TICKER=AST` uniquement après confirmation du ticker et vérification de sa liquidité

**Règle absolue :** Ne pas émettre de prix cible, de stop-loss ou de recommandation d'achat/vente sans données de marché sourcées.
