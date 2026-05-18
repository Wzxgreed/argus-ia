# AST — Contexte actif

> **Dernière mise à jour :** 2026-05-18 (snapshot 23:09 UTC)
> **Fichier source :** `AST_2026-05-18_update.md`

---

## Thèse active

**Statut :** DONNÉES MANQUANTES — analyse initiale requise

- Aucune donnée de cours disponible (`No price history` dans latest.json, confirmé stable 21:23 → 22:36 → 23:09 UTC)
- Pas de Filtre Qualité calculable
- Pas de niveaux techniques (RSI, ATR, MM)
- Aucune news détectée dans le snapshot du jour
- **Doublon probable avec ASTS** (AST SpaceMobile) — ticker correct avec données complètes

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
- [ ] **Doublon ticker :** AST vs ASTS — à résoudre dans `config/watchlist.json`

---

## Erreurs de prédiction passées

Aucune — pas d'historique de prédictions.

---

## Prochaines étapes

1. **Résoudre le doublon AST / ASTS** dans `config/watchlist.json`
2. Si AST est confirmé comme illiquide / sans historique → supprimer ou marquer `excluded`
3. Privilégier l'analyse sous le ticker `ASTS` (données complètes disponibles : $86.83, RSI 60.85, ATR 7.39)
4. Lancer `make analyse TICKER=ASTS` pour débloquer l'analyse complète de l'entité
