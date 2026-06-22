# CONTEXT — FUBO — Dernière mise à jour : 2026-06-22

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l’historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — pas d’entrée en l’état. La récupération volumétrique est un signal positif marginal, mais le rejet intraday ($9.35 → $9.22), l’écart sous MM50 creusé (−15.0%) et l’absence de catalyseur confirment l’absence de momentum directionnel. L’échéance options 2026-06-26 (J+4) pourrait générer du pinning autour du max pain opérationnel ($11.00) si le spot remonte, mais la probabilité est faible avec un spot à −15.0% et une volatilité élevée (ATR_SPIKE 9.44%).

## Historique
- **Score global :** 52.8/100
- **Prix cible :** $11.83
- **Stop-loss :** $7.48
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **Anomalie Options JSON RÉCURRENTE** — snapshot 2026-06-22 : max pain $7.50 aberrant, put/call null, call OI 0.0% — valeurs opérationnelles conservées ($11.00 / 0.45 / 69.0%) — 2026-06-22
- **ATR_SPIKE** (medium) — ATR relatif 9.44% (seuil 5.0%) — persistant — 2026-06-22
- **Volume Récupération** — 1.71M (1.20× moy. 20j) vs 0.38× au 17/06 — regain d’intérêt mais sans close au-dessus de la résistance — 2026-06-22
- **Structure Options Haussière (opérationnelle)** — max pain $11.00, put/call 0.45, call OI 69.0%, spot à −15.0% sous max pain — 2026-06-22
- **Short Squeeze Setup (latent)** — short interest 24.32% + call OI dominant 69.0% + put/call 0.45 = risque de squeeze technique si catalyseur positif — 2026-06-22
- **Divergence Yahoo/FMP Market Cap** — ×12.0 d’écart entre sources ($271.4M Yahoo vs $3,268M FMP) — 2026-06-22
- **Sector Rotation XLC Bottom 3** — malus sectoriel confirmé (momentum score 0.0, `data/sector_rotation_latest.json`) — 2026-06-22
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif

---

## 📅 Prochains événements

- **Earnings Q2 2026** — `upcoming_events_latest.json` (2026-06-22) place l’earnings au **2026-08-06** (45 jours, Est EPS $-0.32-$0.07, Rev $1.5B).
- Échéance options : **2026-06-26** (J+4 — max pain opérationnel $11.00, put/call 0.45, call OI 69.0%)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 43.86
- **MM 50j :** 10.85
- **MM 200j :** —
- **ATR 14j :** 0.87
- **Volume moy. 20j :** 1,424,415

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-22
- **Type :** update
- **Fichier :** `FUBO_2026-06-22_update.md`
- **Conclusion :** ATTENDRE CONFIRMÉE — récupération volumétrique (1.20×) sans conviction de close (rejet $9.35 → $9.22). Anomalie options JSON récurrente détectée et traitée. ATR_SPIKE 9.44% actif. Pas d’entrée longue recommandée.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 9.44% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
