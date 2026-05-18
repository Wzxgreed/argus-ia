# AST — Contexte actif

> **Dernière mise à jour :** 2026-05-18 (snapshot 22:36 UTC)
> **Fichier source :** `AST_2026-05-18_update.md`

---

## Thèse active

**Statut :** DONNÉES MANQUANTES — analyse initiale requise

- Aucune donnée de cours disponible (`No price history` dans latest.json, confirmé stable 21:23 → 22:36 UTC)
- Pas de Filtre Qualité calculable
- Pas de niveaux techniques (RSI, ATR, MM)
- Aucune news détectée dans le snapshot du jour

---

## Scores

| Score | Valeur | Source |
|-------|--------|--------|
| Opportunité | 5.5/10 | Placeholder (données manquantes) |
| Catalyseur | 6.5/10 | Placeholder |
| Valorisation | 5.0/10 | Placeholder |
| Momentum | 5.0/10 | Placeholder |
| Global | 55.2/100 | Placeholder |
| Global ajusté | 55.2/100 | Placeholder |

---

## Niveaux

| Niveau | Valeur | Note |
|--------|--------|------|
| Prix actuel | — | [DONNÉES MANQUANTES] |
| Stop-loss | — | [DONNÉES MANQUANTES] |
| Take-profit | — | [DONNÉES MANQUANTES] |

---

## Alertes actives

- [ ] Aucune alerte définie (pas de données pour calculer les seuils)

---

## Erreurs de prédiction passées

Aucune — pas d'historique de prédictions.

---

## Prochaines étapes

1. Vérifier la validité du symbole AST sur Yahoo Finance / FMP
2. Corriger `config/watchlist.json` si nécessaire (AST vs ASTS ?)
3. Si AST est confirmé comme illiquide / sans historique → marquer `excluded` dans la watchlist
4. Lancer `make analyse TICKER=AST` uniquement après confirmation du ticker et de sa liquidité
