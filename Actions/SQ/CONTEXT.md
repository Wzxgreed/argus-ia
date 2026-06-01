# CONTEXT — SQ — Dernière mise à jour : 2026-06-01

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100 (agent) / ~61.0 institutionnel
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** Bloqué par stale price + earnings non résolu
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale price** — cours $83.46 figé ≥26 snapshots / ≥12 jours calendaires (source `fmp_fallback`, `change_pct: null`)
- 🔴 **Earnings placeholder glissant** — J=0 depuis 12+ jours (date initiale 20/05), details vide
- 🔴 **Quality Gate Exclusion** — SQ parmi 23 tickers excluded (CRITICAL stale 4j)
- 🔴 **Validation divergence** — `validation_report` signale `0 excluded` alors que 23 tickers excluded réellement
- 🟡 **Consensus figé** — $85.67 (3 analystes), inchangé depuis 27/05
- 🟢 **Rotation sectorielle favorable** — signal `ROTATION_TO_CYCLICAL` (was défensive), XLK top3

---

## 📅 Prochains événements

- **2026-06-01** · earnings · Earnings Q1 2026 — **placeholder glissant, non résolu**

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc `technical` vide)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A
- **Volume snapshot :** 1.14M
- **Cours :** $83.46 (stale)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-01
- **Type :** update (snapshot 17:00 UTC)
- **Fichier :** `SQ_2026-06-01_update.md`
- **Conclusion :** **ATTENDRE** — Qualité 3/6 hors périmètre, stale price ≥12 jours, earnings non résolu, consensus figé. Seul changement significatif : signal sectoriel basculé de `ROTATION_TO_DEFENSIVE` à `ROTATION_TO_CYCLICAL` (vent favorable growth/tech). Maintenir exclusion du périmètre long actif jusqu'à résolution données live.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
