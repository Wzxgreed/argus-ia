# CONTEXT — FLY — Derniere mise a jour : 2026-06-15 13h UTC

> Ce fichier est la **memoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise a jour automatique par `agents/update_context/agent.py` a chaque passage du pipeline.

---

## 🎯 These active

- **Recommandation :** SURVEILLER
- **Score global :** 45.0/100
- **Prix cible :** $43.77 (consensus 13 analysts)
- **Stop-loss :** $19.69
- **Statut these :** confirmee avec intensite negative inchangee
- **Horizon :** —

---

## 📉 Erreurs de prediction recentes

- Aucune erreur enregistree.

---

## 🚨 Alertes actives

- **SHORT INTEREST ELEVE ET EN HAUSSE** — 12.12% (+2.34 pts vs 09/06, +23.9% relative). Pression vendeuse accrue, pas de setup squeeze.
- **ANOMALIE OPTIONS MAX PAIN ABERRANT** — Max pain $65.00 vs spot $31.87. Valeur non operationnelle, probablement legacy strikes du rally $60+. Put/call 0.27 et call OI 78.5% restaures (skew haussier extreme).
- **GAP BAISSIER -19.05% SANS CATALYST** — Aucune news, aucun evenement corporate. Mouvement purement technique/speculatif.
- **QUALITY GATE FAUX POSITIF** — `data/quality_gate_2026-06-15.json` signale `stale_price_history` mais close varie ($31.87 vs $36.18). Donnees operationnelles valides.

---

## 📅 Prochains evenements

- Earnings Q2 2026 : **2026-08-04** (50 jours) — Est EPS -$0.61 a -$0.45, Rev $0.1B
- Expiration options : **2026-06-18** (J+3) — max pain aberrant $65.00, put/call 0.27, call OI 78.5%

---

## 📊 Contexte technique (dernier snapshot 13h UTC)

- **RSI 14j :** 32.85 (survente)
- **MM 50j :** 39.47 (cours -19.3% sous MM50)
- **MM 200j :** —
- **ATR 14j :** 6.09
- **Volume moy. 20j :** 9603470
- **Volume session :** 14538100 (1.51x moy. 20j)
- **Low 52W :** $16.00
- **High 52W :** $73.80
- **Previous close :** $39.37 (gap -19.05%)

---

## 📝 Resume derniere analyse

- **Date :** 2026-06-15
- **Type :** update_13h
- **Fichier :** `FLY_2026-06-15_update_13h.md`
- **Conclusion :** Snapshot 13h UTC — Donnees de cours stables vs 10h UTC. Anomalie options partiellement resolue (put/call 0.27, call OI 78.5% restaures) mais max pain $65.00 reste aberrant. These SURVEILLER (45.0) confirmee avec intensite negative inchangee, timing Defavorable.

---

## 🔄 Triggers detectes (full refresh)

- **PRICE_GAP** (high) — Gap -19.05% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 19.11% (seuil 5.0%)

---

*Genere automatiquement — ne pas editer manuellement.*
