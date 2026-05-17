# CONTEXT — [TICKER] — Dernière mise à jour : YYYY-MM-DD

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `scripts/update_context.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** [ACHETER / ATTENDRE / ÉVITER / SURVEILLER]
- **Score global :** X.X/10
- **Prix cible :** $XXX
- **Stop-loss :** $XX
- **Statut thèse :** [validée / modifiée / invalide]
- **Horizon :** X–X mois

---

## 📉 Erreurs de prédiction récentes

| Date · Type · Erreur · Leçon |

- *(Rempli automatiquement depuis SUIVI_PRIX_CIBLES.md et SUIVI_EARNINGS_PREDICTIONS.md)*

---

## 🚨 Alertes actives

| Alerte · Seuil · État |

- *(Rempli automatiquement depuis Alertes/ALERTES.md)*

---

## 📅 Prochains événements

| Date · Événement · Impact |

- *(Rempli automatiquement depuis Alertes/UPCOMING_EVENTS.md)*

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** XX
- **MM 50j :** $XX
- **MM 200j :** $XX
- **ATR 14j :** $X.XX
- **Volume moy. 20j :** XX M

---

## 📝 Résumé dernière analyse

- **Date :** YYYY-MM-DD
- **Type :** [init / update / earnings / preview / full refresh]
- **Fichier :** `[TICKER]_YYYY-MM-DD_type.md`
- **Conclusion :** *(1 phrase synthétique)*

---

## 🔄 Triggers détectés (full refresh)

- *(Rempli par detect_major_events.py lors d'un refresh)*

---

*Généré automatiquement — ne pas éditer manuellement.*
