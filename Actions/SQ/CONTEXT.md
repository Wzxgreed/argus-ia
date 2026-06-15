# CONTEXT — SQ — Dernière mise à jour : 2026-06-15

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 54.0/100
- **Prix cible :** $85.67 (consensus, figé depuis 27/05)
- **Stop-loss :** $— (non définissable — cours stale)
- **Statut thèse :** Paralysé par stale price systémique
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale price record** — cours $83.46 figé ≥58 snapshots / ≥26 jours (20/05 → 15/06). Dernier ticker `fmp_fallback` du snapshot.
- 🔴 **Exclusion systémique** — `quality_gate_2026-06-15.json` : 25/25 tickers `excluded` (CRITICAL stale_price_history). SQ conserve le record de durée.
- 🔴 **Earnings placeholder glissant** — date J=0 au 15/06 (≥58ème snapshot consécutif), champ details vide — placeholder FMP générique.
- 🟡 **Consensus figé** — $85.67 (3 analystes) inchangé depuis 27/05 ; silence sell-side.
- 🟡 **Divergence market cap FMP** — ~4.8% ($51.73B vs $54.29B), réduite vs ~47% au 10/06.
- 🟡 **Divergence validation/gate** — validation_report "0 excluded" vs quality_gate 25 excluded.

---

## 📅 Prochains événements

- **2026-06-15** · earnings · Earnings Q1 2026 (placeholder glissant, J=0)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc `technical` vide depuis 17/05)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-15
- **Type :** update
- **Fichier :** `SQ_2026-06-15_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, stale price ≥58 snapshots / ≥26 jours, earnings placeholder glissant ≥58 snapshots (date 15/06), exclusion systémique quality_gate (25/25 tickers), divergence market cap réduite ~4.8%, zero mutation données brutes vs 10/06, Score Global 54.0/100, validation 5 [ERROR].

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
