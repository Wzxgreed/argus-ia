# CONTEXT — SQ — Dernière mise à jour : 2026-06-15

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 54.0/100
- **Prix cible :** $85.67
- **Stop-loss :** — (attendre résolution données)
- **Statut thèse :** ATTENDRE — Qualité 3/6 hors périmètre, stale price ≥58 snapshots / ≥26 jours, earnings placeholder glissant
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Exclusion Quality Gate Systémique** — SQ `excluded` (CRITICAL stale_price_history, 25/25 tickers)
- 🔴 **Stale Price aggravé** — cours figé ≥58 snapshots / ≥26 jours calendaires (2026-05-20 → 2026-06-15)
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après 26 jours calendaires
- 🔴 **Source FMP Fallback** — dernier ticker avec `source: fmp_fallback` et `change_pct: null`
- 🟡 **Consensus PT Figé** — $85.67 (3 analystes) inchangé depuis 27/05
- 🟡 **Divergence Validation / Quality Gate** — 0 excluded par validation_report vs 25/25 dans quality_gate
- 🟡 **Divergence Market Cap FMP** — $51.73B vs $54.29B (~4.8%)
- 🟡 **Rotation Sectorielle Neutralisée** — XLK top3 mais signal global `NEUTRAL`

---

## 📅 Prochains événements

- **2026-06-15 (glissement)** · 🔴 **Earnings Q1 2026** — résultats **toujours non intégrés** dans le snapshot 15/06 (**26 jours après date prévue**). `upcoming_events_2026-06-15.json` affiche `"date": "2026-06-15"` avec `"days_until": 0`, mais champ `"details"` vide (placeholder FMP générique).

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** — (données manquantes, bloc technical vide depuis 17/05)
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-15
- **Type :** update (snapshot 13h00 UTC)
- **Fichier :** `SQ_2026-06-15_update_13h00.md`
- **Conclusion :** > **Trigger :** Snapshot pipeline 13:00 UTC — aucune mutation détectée vs snapshot 10:00 UTC. Qualité 3/6, stale price ≥58 snapshots / ≥26 jours, earnings placeholder glissant, consensus figé, exclusion systémique quality gate, signal sectoriel NEUTRAL stable. Score Global Ajusté ~54.0 (fourchette ATTENDRE). Tout positionnement avant résolution du stale price déconseillé.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
