# CONTEXT — SQ — Dernière mise à jour : 2026-05-25

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100
- **Prix cible :** $— (attendre résolution données)
- **Stop-loss :** $— (attendre résolution données)
- **Statut thèse :** Bloqué — anomalie de données critique
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale price 9 snapshots / 5 jours calendaires** — cours figé $83.46 depuis 20/05
- 🔴 **Earnings Q1 2026 J=0 non résolu** — 5 jours après date prévue dans `upcoming_events`
- 🔴 **Source FMP Fallback** — seul ticker du snapshot avec source fallback et change_pct null

---

## 📅 Prochains événements

- **2026-05-20 (non résolu)** · earnings · Earnings Q1 2026 — date prévue J=0, toujours non intégré

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc `technical` vide)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A
- **Cours affiché :** $83.46 (⚠️ stale — fiabilité non garantie)
- **Volume session :** 1.14M

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-25
- **Type :** update
- **Fichier :** `SQ_2026-05-25_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, stale price 9 snapshots consécutifs / 5 jours calendaires, earnings J=0 non résolu après 5 jours. Aucun changement vs snapshot 20/05 13:00 UTC. SQ est le seul ticker de la watchlist avec source `"fmp_fallback"` et `change_pct: null`. Priorité opérationnelle : vérifier cours live via broker et date réelle de publication des résultats Q1 2026. Exclure du périmètre long tant que l'anomalie persiste.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
