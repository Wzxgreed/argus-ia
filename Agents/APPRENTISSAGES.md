# APPRENTISSAGES.md — Mémoire institutionnelle + Calibration automatique

Ce fichier contient les **règles actives** issues des erreurs passées. Elles surpassent les règles par défaut de tous les agents.

---

## Règles actives issues des erreurs
### Règle auto — 2026-06-16
- **Règle :** Si prix cible rate avec une erreur > 20% → revérifier le Filtre Qualité et les hypothèses de DCF avant prochaine émission de PT sur ce ticker.
- **Source :** Post-mortem prix cible IREN 2026-05-17
- **Confiance :** moyenne
- **Commentaire :** Extrait automatiquement par `learn_from_errors.py`. À réévaluer après 3 mois ou 10 signaux supplémentaires.


> Les règles ci-dessous sont extraites automatiquement par `learn_from_errors.py` lors de chaque post-mortem. Elles s'appliquent à TOUTES les analyses futures.

*(Aucune règle active pour le moment — les premières seront générées après les premiers signaux et post-mortems.)*

---

## Journal des post-mortems

| Date | Ticker | Horizon | Cause racine | Règle extraite | Confiance |
|------|--------|---------|-------------|----------------|-----------|
| — | — | — | — | — | — |

---

## Statistiques d'apprentissage

- **Post-mortems générés :** 0
- **Règles actives :** 0
- **Règles révoquées :** 0
- **Dernière mise à jour :** —

---

### Ajustements de calibration actifs

| Ajustement | Motif | Depuis | Sur quel agent | Fin prévue |
|-----------|-------|--------|---------------|-----------|
| — | — | — | — | — |

---

## Règles révoquées

*(Règles qui ont été retirées car non efficaces après 3 mois / 10 signaux)*

---

*Ce fichier est mis à jour automatiquement par `agents/learn_from_errors/agent.py` à chaque passage du pipeline.*
