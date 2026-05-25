# AST — Index

> **Symbole :** AST
> **Nom :** AST (non spécifié dans watchlist)
> **Secteur :** Non spécifié
> **Exchange :** NASDAQ
> **Priorité :** Medium
> **Dernière mise à jour :** 2026-05-25 (snapshot 13:00 UTC)

---

## Thèse courante

**Statut :** DONNÉES MANQUANTES — analyse initiale requise

- Aucune donnée de cours disponible dans les snapshots (`No price history`) — confirmé stable sur 9 snapshots consécutifs (18/05 21:23, 22:36, 23:09 UTC ; 19/05 10:00, 13:00, 17:00, 21:00 UTC ; 20/05 10:00 UTC ; 25/05 10:00 UTC)
- Aucune analyse initiale (`_init.md`) n'a été produite
- Earnings programmés le 2026-05-25 (source FMP) — résultats non intégrés au pipeline (pas de données de cotation)
- Scoring agent : placeholder 55.2/100 — action ATTENDRE par défaut
- AST absent du quality gate (alors que ASTS y figure)
- **Anomalie structurelle détectée :** doublon probable avec ASTS (AST SpaceMobile), ticker correct et liquide sur NASDAQ

---

## Historique des fichiers

| Date | Fichier | Type | Résumé |
|------|---------|------|--------|
| 2026-05-25 | `AST_2026-05-25_update.md` | Update après-midi (13:00 UTC) | 10e snapshot consécutif sans mutation — `No price history` stable, earnings J=0 non résolu, ASTS $105.86 (+10.01%) confirme le doublon, recommandation maintenue : résoudre anomalie structurelle |
| 2026-05-25 | `AST_2026-05-25_update.md` | Update matin (10:00 UTC) | Données manquantes confirmées — aucun changement vs 20/05, earnings 25/05 non intégrés, doublon ASTS confirmé, recommandation : résoudre anomalie structurelle |
| 2026-05-25 | `AST_2026-05-25_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |
| 2026-05-24 | `AST_2026-05-24_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |
| 2026-05-23 | `AST_2026-05-23_update.md` | Update matin | Données manquantes confirmées — aucun changement vs 20/05 |
| 2026-05-22 | `AST_2026-05-22_update.md` | Update matin | Données manquantes confirmées — aucun changement vs 20/05 |
| 2026-05-21 | `AST_2026-05-21_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |
| 2026-05-20 | `AST_2026-05-20_update.md` | Update matin (10:00 UTC) | Données manquantes confirmées — aucun changement vs 19/05, AST absent du quality gate, doublon ASTS confirmé |
| 2026-05-20 | `AST_2026-05-20_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |
| 2026-05-19 | `AST_2026-05-19_update.md` | Update final (21:00 UTC) | Données manquantes confirmées — aucun changement vs snapshot 17:00, AST absent du quality gate, doublon ASTS confirmé |
| 2026-05-19 | `AST_2026-05-19_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (23:09 UTC) | Confirmation stabilité snapshot + détection doublon AST/ASTS |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (22:36 UTC) | Confirmation stabilité snapshot — toujours non évaluable |
| 2026-05-18 | `AST_2026-05-18_update.md` | Update (21:23 UTC) | Données manquantes — non évaluable |
| 2026-05-18 | `AST_2026-05-18_preview.md` | Preview earnings | Template vide — aucune prédiction renseignée |

---

## Agenda

| Événement | Date | Statut |
|-----------|------|--------|
| Earnings | 2026-05-25 | Programmé (FMP) — résultats non disponibles dans les snapshots (pas de données de cotation) |

---

## Notes

- Symbole ajouté via dashboard API — validité du ticker à confirmer
- Pas de données FMP, pas de données Yahoo Finance dans les snapshots du 18/05, 19/05, 20/05 et 25/05
- ASTS (AST SpaceMobile) présent dans la watchlist avec données complètes — probable doublon erroné
- AST absent du rapport quality gate (contrairement à ASTS)
- **Action recommandée :** supprimer AST ou marquer `excluded` dans `config/watchlist.json` et privilégier ASTS
