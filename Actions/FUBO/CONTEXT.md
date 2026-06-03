# CONTEXT — FUBO — Dernière mise à jour : 2026-06-03

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — pas d'entrée en l'état. Surveiller la convergence vers max pain $12.00 à échéance J+2 (2026-06-05).
- **Score global ajusté :** ~56.5 / 100
- **Prix cible (TP ATR) :** $12.67
- **Stop-loss :** $9.42
- **Statut thèse :** confirmée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **Anomalie Options JSON** — Max pain $3.00 aberrant détecté dans latest.json (valeur opérationnelle $12.00 conservée) — 2026-06-03
- **Anomalie Earnings Calendrier** — `upcoming_events_latest.json` place earnings au 2026-06-03 (jour J, `days_until: 0`), aucun résultat visible — persistant depuis 2026-05-18
- **Franchissement sous MM50** — Cours $10.72 sous MM50 $11.09 (−3.3%) — persistant
- **Structure Options Haussière Persistante** — Max pain $12.00 opérationnel, put/call 0.20, call OI 83.2%, spot à −10.7% sous max pain → aimant haussier mécanique vers $12.00 à échéance J+2 — 2026-06-03
- **Short Squeeze Setup (latent)** — short interest 25.03% + call OI dominant 83.2% + put/call 0.20 = risque de squeeze technique si catalyseur positif — persistant
- **Sector Rotation XLC Bottom 3** — malus sectoriel actif (snapshot 2026-06-03 : momentum score 0.0 / 10)
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif

---

## 📅 Prochains événements

- **2026-06-05** · options expiration · Échéance J+2 (max pain opérationnel $12.00)
- **2026-06-03** · earnings · Anomalie calendrier : jour J sans résultats visibles
- Prochaine échéance earnings Q2 : ~août 2026

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 58.61
- **MM 50j :** 11.09
- **MM 200j :** —
- **ATR 14j :** 0.65
- **Volume moy. 20j :** 1429910
- **Volume séance :** 1103400 (0.77×)
- **Close :** $10.72
- **Previous close :** $11.52
- **Change :** −6.94%
- **Beta :** 2.508
- **Short Interest :** 25.03%

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-03
- **Type :** update
- **Fichier :** `FUBO_2026-06-03_update.md`
- **Conclusion :** Stabilité totale vs close 02/06. Cours $10.72 inchangé, RSI 58.61, volume 1.10M / 0.77×. Anomalie options JSON détectée (max pain $3.00 aberrant → valeurs opérationnelles $12.00/0.20/83.2% conservées). Scores inchangés ATTENDRE 58.0/100. Thèse ATTENDRE confirmée (~56.5/100).

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap -6.94% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 6.06% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
