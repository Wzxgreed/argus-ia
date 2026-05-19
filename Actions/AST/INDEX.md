# AST — Index

> **Symbole :** AST
> **Nom :** AST (non spécifié dans watchlist)
> **Secteur :** Non spécifié
> **Exchange :** NASDAQ
> **Priorité :** Medium
> **Dernière mise à jour :** 2026-05-19 (snapshot 17:00 UTC)

---

## Thèse courante

**Statut :** DONNÉES MANQUANTES — analyse initiale requise

- Aucune donnée de cours disponible dans les snapshots (`No price history`) — confirmé stable sur 6 snapshots consécutifs (18/05 21:23, 22:36, 23:09 UTC ; 19/05 10:00, 13:00, 17:00 UTC)
- Aucune analyse initiale (`_init.md`) n'a été produite
- Earnings programmés le 2026-05-18 puis 2026-05-19 (source FMP) mais résultats non intégrés au pipeline
- Scoring agent : placeholder 55.2/100 — action ATTENDRE par défaut
- AST absent du `quality_gate_2026-05-19.json` (alors que ASTS y figure, statut `ok`)
- **Anomalie structurelle détectée :** doublon probable avec ASTS (AST SpaceMobile), ticker correct et liquide sur NASDAQ

---

## Historique des fichiers

| Date | Fichier | Type | Résumé |
|------|---------|------|--------|
| 2026-05-19 | `AST_2026-05-19_update.md` | Update (17:00 UTC) | Données manquantes confirmées — aucun changement vs snapshot 13:00, AST absent du quality gate, doublon ASTS confirmé |
| 2026-05-19 | `AST_2026-05-19_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (23:09 UTC) | Confirmation stabilité snapshot + détection doublon AST/ASTS |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (22:36 UTC) | Confirmation stabilité snapshot — toujours non évaluable |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (21:23 UTC) | Données manquantes — non évaluable |
| 2026-05-18 | `AST_2026-05-18_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |

---

## Agenda

| Événement | Date | Statut |
|-----------|------|--------|
| Earnings | 2026-05-19 | Programmé (FMP) — résultats non disponibles dans les snapshots |

---

## Notes

- Symbole ajouté via dashboard API — validité du ticker à confirmer
- Pas de données FMP, pas de données Yahoo Finance dans les snapshots du 18/05 et 19/05
- ASTS (AST SpaceMobile) présent dans la watchlist avec données complètes — probable doublon erroné
- AST absent du rapport `quality_gate_2026-05-19.json` (contrairement à ASTS, statut `ok`)
- **Action recommandée :** supprimer AST ou marquer `excluded` dans `config/watchlist.json` et privilégier ASTS
