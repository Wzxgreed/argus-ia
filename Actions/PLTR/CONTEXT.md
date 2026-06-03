# CONTEXT — PLTR — Dernière mise à jour : 2026-06-03

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 56.8/100
- **Prix cible :** $186.15 (consensus FMP, 34 analystes)
- **Stop-loss :** $138.79 (cours − 2×ATR)
- **Statut thèse :** Confirmée
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 FY2026 le 2026-08-03)

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **Anomalie options JSON** (2026-06-03) — `data/latest.json` retourne Max Pain $50.00 aberrant, Put/Call et Call OI null pour PLTR. Valeurs opérationnelles conservées du snapshot 21h 02/06 : Max Pain $160.00, Put/Call 0.50, Call OI 66.8%.
- Warning : `data/accounting_risk_latest.json` absent — Filtre Qualité non alimenté
- Alerte technique RÉSOLUE : RSI 35.66 < 40 — retour en zone de survente depuis le 25/05 (résolu le 26/05 17:00 UTC, RSI 52.85)
- Alerte technique RÉSOLUE : volume collapse 30.21M (0.68× moyenne) au snapshot 17h 02/06 — résolu au snapshot 21h (42.49M, 0.95×)
- Anomalie options JSON RÉSOLUE snapshot 26/05 13:00 UTC — Put/Call 0.55, Max Pain $140.00, Call OI 64.4% valides et cohérents
- Anomalie options JSON RÉSOLUE snapshot 27/05 13:00 UTC — valeurs validées (Put/Call 0.49, Max Pain $140.00, Call OI 67.0%)
- Anomalie options JSON RÉSOLUE snapshot 01/06 13:00 UTC — Max Pain $160.00, Put/Call 0.52, Call OI 65.8% validés

---

## 📅 Prochains événements

- **Earnings Q2 FY2026 :** 2026-08-03 (Est. EPS $0.32–$0.40, Rev $1.8B) — dans 61 jours
- **Expiration options :** 2026-06-05 (2 jours) — Max Pain $160.00, écart −4.9% vs cours

---

## 📊 Contexte technique (dernier snapshot)

- **Cours :** $152.17
- **RSI 14j :** 64.74
- **MM 50j :** 141.92
- **MM 200j :** —
- **ATR 14j :** 6.69
- **Volume moy. 20j :** 44891555
- **Volume jour :** 42732600
- **Max Pain (opérationnel) :** $160.00
- **Put/Call (opérationnel) :** 0.50
- **Call OI % (opérationnel) :** 66.8%

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-03
- **Type :** update
- **Fichier :** `PLTR_2026-06-03_update.md`
- **Conclusion :** Stabilité totale vs close 02/06. Cours $152.17 inchangé, RSI 64.74 stable, volume 42.73M (0.95× moyenne) confirmé. Anomalie options JSON détectée (Max Pain $50.00 aberrant) — valeurs opérationnelles conservées. Thèse ATTENDRE confirmée sans modification (Score Global 56.8/100).

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium, résolu) — Gap -5.28% overnight entre close 01/06 ($160.65) et open 02/06 ($156.69). Traité dans les updates du 02/06. Cours stabilisé à $152.17 depuis. Pas de nouveau trigger le 03/06.

---

*Généré automatiquement — ne pas éditer manuellement.*
