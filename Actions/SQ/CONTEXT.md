# CONTEXT — SQ — Dernière mise à jour : 2026-05-25 · Snapshot 21:00 UTC

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 59/100 (Score Opportunité 5.4/10)
- **Prix cible :** $87.50 (consensus FMP, 2 analystes)
- **Stop-loss :** —
- **Statut thèse :** Bloquée — anomalie de données critique
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale price** — Cours $83.46 figé sur **12 snapshots consécutifs** (20/05 → 25/05). Source `"fmp_fallback"`, `change_pct: null`. **Seul ticker de la watchlist** avec cette anomalie.
- 🔴 **Earnings Q1 2026 non résolu** — J=0 dans `upcoming_events` depuis 5 jours calendaires. Résultats non intégrés dans le pipeline.
- 🟡 **Pipeline partial** — Phases C/D failed (validate + detect_major_events) le 25/05. Agent accounting skipped.
- 🟢 **Geo Risk** — Score 2/10, non flaggué.
- 🟢 **FX Exposure** — Score 0.0, direction neutral.
- 🟢 **Social Sentiment** — 0 mentions, 0/10, pump `false`.

---

## 📅 Prochains événements

- **2026-05-20** · earnings · Earnings Q1 2026 — **toujours non résolu** (J=0 depuis 5 jours)
- Marché US réouvert mardi 26/05 — vérifier si données fraîches injectées

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc `technical` vide)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A (volume brut 1.14M)
- **Cours :** $83.46 (figé depuis 12 snapshots)
- **High/Low :** $85.07 / $83.13 (figés)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-25 · Snapshot 21:00 UTC
- **Type :** update
- **Fichier :** `SQ_2026-05-25_update.md`
- **Conclusion :** Thèse **ATTENDRE** confirmée — stabilité totale vs snapshot 17:00 UTC. 12e snapshot consécutif identique ($83.46). Aucune mutation technique, fondamentale, sentiment ou macro. Memorial Day (marché fermé) n'explique pas le stale price depuis le 20/05. Earnings Q1 2026 J=0 toujours non résolu. Pipeline partial (phases C/D failed). Exclure SQ du périmètre long actif jusqu'à résolution de l'anomalie de données.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
