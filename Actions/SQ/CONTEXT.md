# CONTEXT — SQ — Dernière mise à jour : 2026-06-01

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 5.4/10
- **Prix cible :** $85.67 (consensus 3 analystes)
- **Stop-loss :** $— (attendre résolution stale price)
- **Statut thèse :** Confirmée inchangée
- **Horizon :** — (bloqué par anomalie de données)

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale price ≥23 snapshots / ≥12 jours calendaires** — cours figé $83.46 depuis 20/05, source `fmp_fallback`, `change_pct: null`
- 🔴 **Earnings placeholder glissant 12+ jours** — `upcoming_events` affiche J=0 avec date glissante (20/05 → 01/06), champ details vide
- 🔴 **Quality gate eruption** — `quality_gate_2026-06-01.json` exclut 23/24 tickers (CRITICAL stale 4j) ; SQ reste le cas le plus ancien
- 🔴 **Pipeline dégradation** — 5 [ERROR] dans validation (>2), divergence gate/validation persistante
- 🟡 **Rotation défensive** — Signal `ROTATION_TO_DEFENSIVE` sectoriel (crossover bearish XLE) ; vent contraire growth multiples
- 🟡 **Consensus figé** — $85.67 (3 analystes) inchangé depuis 27/05 ; silence sell-side

---

## 📅 Prochains événements

- **2026-06-01** · earnings · Earnings (placeholder FMP glissant — 12+ jours de retard)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc `technical` vide)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-01
- **Type :** update
- **Fichier :** `SQ_2026-06-01_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, stale price ≥12 jours, earnings placeholder glissant, consensus figé $85.67, rotation défensive signalée, quality gate eruption systémique. Aucune mutation détectée sur les données SQ vs 27/05. Risque de gap violent maximal. Exclure du périmètre long actif tant que l'anomalie persiste.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
