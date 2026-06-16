# CONTEXT — SQ — Dernière mise à jour : 2026-06-16

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 54.0/100
- **Prix cible :** $85.67 (consensus)
- **Stop-loss :** —
- **Statut thèse :** ATTENDRE
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price aggravé** — cours figé ≥62 snapshots / ≥27 jours calendaires (2026-05-20 → 2026-06-16). SQ est le cas le plus ancien et le plus sévère de stale price dans le snapshot.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **27 jours calendaires** (date initiale 20/05). `upcoming_events_2026-06-16.json` affiche `days_until: 0` avec date 16/06 (placeholder FMP générique).
- 🔴 **Source FMP Fallback** — SQ est le **dernier ticker** du snapshot 16/06 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé.
- 🟡 **Pipeline Degradation** — `validation_report.txt` (16/06) affiche **5 [ERROR]** — seuil >2 franchi, stable vs 10h00.

---

## 📅 Prochains événements

- **2026-06-16** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc technical vide depuis 17/05)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-16
- **Type :** update
- **Fichier :** `SQ_2026-06-16_update_17h00.md`
- **Conclusion :** > **Trigger :** Snapshot pipeline 17:00 UTC — post-session US. Zero mutation données brutes SQ vs snapshot 10h00.

---

## 🔄 Triggers détectés (full refresh)

- **Stale price ≥62 snapshots** — record historique du ticker, persistant depuis 20/05.
- **Earnings placeholder glissant** — date initiale 20/05, glissée au 16/06, ≥62 snapshots sans résolution.

---

*Généré automatiquement — ne pas éditer manuellement.*
