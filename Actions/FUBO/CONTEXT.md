# CONTEXT — FUBO — Dernière mise à jour : 2026-06-09

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — pas d'entrée en l'état. Surveiller la résolution de l'anomalie earnings (22 sessions persistantes) et l'échéance options du 2026-06-12. L'upgrade agent à ACHETER Réduit (61.2/100) est noté comme signal positif mais non suivi en l'absence de confirmation volume (>1.0×) et de franchissement MM50 ($10.96).

## Historique
- **Score global :** 58.5/100 (analyste ajusté)
- **Prix cible :** $11.92 (TP ATR 3×)
- **Stop-loss :** $8.22 (SL ATR 2×)
- **Statut thèse :** confirmée
- **Horizon :** 1–3 mois

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **Anomalie earnings Q1 persistante** — 22 sessions avec `days_until: 0`, aucun résultat visible. Risque opérationnel majeur sur la qualité des données.
- **Anomalie options JSON récurrente** — `max_pain: $3.00` aberrant dans latest.json (vs $13.00 opérationnel). Traité comme artefact technique.
- **Sector Rotation XLC Bottom 3** — malus sectoriel −0.5 pt actif.
- **Short Squeeze Setup latent** — short interest 25.03% + call OI 79.7% + put/call 0.25.

---

## 📅 Prochains événements

- **2026-06-12** · options · Échéance options (max pain $13.00, put/call 0.25, call OI 79.7%) — J+3
- **2026-06-09** · earnings · Earnings Q1 2026 anomalie persistante (`days_until: 0` — 22 sessions)

---

## 📊 Contexte technique (dernier snapshot)

- **Close :** $9.70
- **RSI 14j :** 52.43
- **MM 50j :** 10.96
- **MM 200j :** —
- **ATR 14j :** 0.74
- **Volume moy. 20j :** 1212770
- **Volume séance :** 904000 (0.75×)
- **Spot vs MM50 :** −11.5%
- **52W High/Low :** $56.64 / $8.31

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-09
- **Type :** update
- **Fichier :** `FUBO_2026-06-09_update.md`
- **Conclusion :** Stabilité totale vs close 08/06. Cours $9.70 inchangé, RSI 52.43 stable, volume 904k (0.75×). Agent ACHETER Réduit maintenu (61.2/100). Analyste ATTENDRE confirmé (~58.5/100). Anomalie options JSON récurrente ($3.00 aberrant). Anomalie earnings Q1 persistante (22 sessions). Attendre retour au-dessus MM50 avec volume confirmé.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 7.63% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
