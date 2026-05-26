# CONTEXT — SQ — Dernière mise à jour : 2026-05-26

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100
- **Prix cible :** $87.50 (consensus 2 analystes)
- **Stop-loss :** $— (aucun — cours stale, pas de positionnement)
- **Statut thèse :** Bloquée par anomalie de données
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Quality Gate Exclusion** — stale price 13 snapshots / ≥6 jours calendaires (2026-05-20 → 2026-05-26). SQ officiellement excluded dans `quality_gate_2026-05-26.json`.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après 6 jours calendaires (date initiale 20/05). Placeholder FMP générique détecté (`"details": "Earnings "` vide).
- 🔴 **Source FMP Fallback** — SQ est le seul ticker du snapshot 26/05 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Pipeline Partial** — Phases C/D failed (validate + detect_major_events) le 26/05 ; agent accounting skipped.
- 🟡 **Quality Gate Bug** — 22/22 tickers marqués excluded avec motif identique, y compris ceux à cours frais. Incohérence avec `validation_report.txt`.

---

## 📅 Prochains événements

- **2026-05-20 (initialement prévu)** · earnings · Earnings Q1 2026 — résultats toujours non intégrés après 6 jours

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** — (bloc technical vide)
- **MM 50j :** — (bloc technical vide)
- **MM 200j :** — (bloc technical vide)
- **ATR 14j :** — (bloc technical vide)
- **Volume moy. 20j :** — (indisponible)
- **Cours affiché :** $83.46 (⚠️ stale — 13 snapshots identiques)
- **Source :** fmp_fallback (seul ticker watchlist)
- **change_pct :** null

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-26
- **Type :** update
- **Fichier :** `SQ_2026-05-26_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, earnings non résolu après 6 jours, stale price 13 snapshots / 6 jours, quality gate exclusion officielle, SQ seul ticker fmp_fallback post-Memorial Day, pipeline partial, zero changement vs 25/05.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
