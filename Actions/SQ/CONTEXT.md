# CONTEXT — SQ — Dernière mise à jour : 2026-05-25

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100
- **Prix cible :** $87.50 (consensus 2 analystes)
- **Stop-loss :** $— (non défini — attendre résolution stale price)
- **Statut thèse :** Bloqué par anomalie de données (stale price 10 snapshots / earnings J=0 non résolu)
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price** — Cours $83.46 figé sur 10 snapshots consécutifs (20/05 → 25/05), source `fmp_fallback`, `change_pct: null`
- 🔴 **Earnings J=0 non résolu** — Q1 2026 non intégré dans le pipeline après 5 jours calendaires
- 🔴 **Quality Gate Exclusion** — Filtre Qualité 3/6 (hors périmètre), bilan négatif, ROIC −12.8%
- 🟡 **Consensus réduit** — 2 analystes couvrant, 0 révision mois/trimestre dernier

---

## 📅 Prochains événements

- **2026-05-25** · 🔴 Earnings Q1 2026 — J=0, résultats **toujours non intégrés** dans le snapshot 13:00 UTC
- Action opérationnelle urgente : Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR

---

## 📊 Contexte technique (dernier snapshot 13:00 UTC)

- **RSI 14j :** N/A (bloc `technical` vide)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A
- **Volume session :** 1.14M

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-25
- **Type :** update
- **Fichier :** `SQ_2026-05-25_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, earnings J=0 **non résolu après 5 jours**, **stale price 10 snapshots / 5 jours calendaires (quality gate excluded)**, zero changement vs snapshot matinal 10:00 UTC. Seul ticker watchlist avec `fmp_fallback` et cours figé. Exclure du périmètre long actif jusqu'à résolution.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
