# CONTEXT — SQ — Dernière mise à jour : 2026-05-27

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100
- **Prix cible :** —
- **Stop-loss :** —
- **Statut thèse :** Confirmée — aucune mutation détectée sur 18 snapshots consécutifs
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Quality Gate Exclusion** — stale price 18 snapshots / ≥8 jours calendaires (2026-05-20 → 2026-05-27). SQ seul ticker excluded.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après 8 jours calendaires (date initiale 20/05). Placeholder FMP générique glissant.
- 🔴 **Source FMP Fallback** — SQ est le seul ticker du snapshot 27/05 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Validation Divergence** — `validation_report.txt` indique `0 excluded by quality gate` alors que SQ est réellement excluded.
- 🟡 **Pipeline Degradation** — 4 [ERROR] dans validation (VRT schema, AST/AXA/QTBS fetch) — seuil >2 franchi.

---

## 📅 Prochains événements

- **2026-05-27** · earnings · Earnings placeholder J=0 (non résolu, glissant depuis 20/05)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc `technical` vide)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-27
- **Type :** update
- **Fichier :** `SQ_2026-05-27_update.md`
- **Conclusion :** Snapshot 13:00 UTC confirme intégralement la paralysie du snapshot 10:00 UTC. Cours $83.46 figé depuis 18 snapshots / 8 jours calendaires. Aucune mutation technique, fondamentale, sentiment ou macro. Score Opportunité 5.8/10, Global 58.0/100. Thèse ATTENDRE confirmée. Validation report dégrade à 4 [ERROR] (>2) — signal de fiabilité pipeline affaibli, sans impact direct sur SQ.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
