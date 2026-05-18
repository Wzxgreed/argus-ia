# AST — Index

> **Symbole :** AST
> **Nom :** AST (non spécifié dans watchlist)
> **Secteur :** Non spécifié
> **Exchange :** NASDAQ
> **Priorité :** Medium
> **Dernière mise à jour :** 2026-05-18 (snapshot 22:36 UTC)

---

## Thèse courante

**Statut :** DONNÉES MANQUANTES — analyse initiale requise

- Aucune donnée de cours disponible dans les snapshots (`No price history`) — confirmé stable entre 21:23 UTC et 22:36 UTC
- Aucune analyse initiale (`_init.md`) n'a été produite
- Earnings programmés le 2026-05-18 (source FMP) mais résultats non intégrés au pipeline
- Scoring agent : placeholder 55.2/100 — action ATTENDRE par défaut

---

## Historique des fichiers

| Date | Fichier | Type | Résumé |
|------|---------|------|--------|
| 2026-05-18 | `AST_2026-05-18_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (21:23 UTC) | Données manquantes — non évaluable |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (22:36 UTC) | Confirmation stabilité snapshot — toujours non évaluable |

---

## Agenda

| Événement | Date | Statut |
|-----------|------|--------|
| Earnings | 2026-05-18 | Programmé (FMP) — résultats non disponibles dans les snapshots |

---

## Notes

- Symbole ajouté via dashboard API — validité du ticker à confirmer
- Pas de données FMP, pas de données Yahoo Finance dans les snapshots du jour (21:23 et 22:36 UTC)
- À traiter en priorité : fetch technique + fondamental pour débloquer l'analyse, OU correction du ticker si AST = ASTS
- Si confirmation que AST est illiquide / sans historique → marquer `excluded` dans `config/watchlist.json`
