# CONTEXT — FUBO — Dernière mise à jour : 2026-05-27

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER
- **Score global :** ~42/100 (ajusté analyste) / 64.2/100 (agent)
- **Prix cible :** $11.38 (TP ATR 3×)
- **Stop-loss :** $8.28 (2× ATR)
- **Statut thèse :** Confirmée — stabilité totale, anomalie options JSON résolue, biais call légèrement renforcé
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **RSI SURVENTE EXTRÊME** — RSI 21.08 (seuil 30) — persistant
- **Earnings Q1 2026 en attente** — anomalie calendrier : `upcoming_events_latest.json` place l'earnings au **2026-05-27** (jour J), mais aucun résultat visible — [ANOMALIE J+8 NON RÉSOLU]
- **Divergence Yahoo/FMP Market Cap** — ×11.7 d'écart entre sources ($280.2M vs ~$3.27B)
- **Sector Rotation XLC Bottom 3** — malus sectoriel actif (snapshot 2026-05-27 : momentum score 0.0 / 10)
- **Options Spot/Max Pain Divergence** — spot $9.52 vs max pain $10.00 (écart −4.8%) ; call OI dominant 66.3%
- **Liquidité réduite** — volume 0.70× moyenne 20j (1,004,300 vs 1,438,260) — risque de slippage majeur
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif
- **Short Squeeze Setup (latent)** — short interest 22.84% + call OI dominant 66.3% = risque de squeeze technique si catalyseur positif
- **Anomalie Options JSON RÉSOLUE** — snapshot 13:00 UTC : max pain $10.00, put/call 0.51, call OI 66.3% (cohérent)

---

## 📅 Prochains événements

- **2026-05-27** · earnings · Earnings Q1 2026 (jour J, non résolu après 8 jours)
- **2026-05-29** · options expiration · Échéance options (max pain $10.00, put/call 0.51, call OI 66.3%)
- **~août 2026** · earnings · Prochain earnings Q2 (estimation)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 21.08
- **MM 50j :** 11.42
- **MM 200j :** —
- **ATR 14j :** 0.62
- **Volume moy. 20j :** 1,438,260
- **Volume séance :** 1,004,300 (0.70×)
- **Max pain :** $10.00
- **Put/Call :** 0.51
- **Call OI % :** 66.3%

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-27
- **Type :** update
- **Fichier :** `FUBO_2026-05-27_update.md` (snapshot 13:00 UTC)
- **Conclusion :** THÈSE CONFIRMÉE — SURVEILLER. Stabilité totale vs 10:00 UTC. Anomalie options JSON résolue (max pain $10.00 cohérent, put/call 0.51, call OI 66.3%). Biais haussier options légèrement renforcé. Scoring agent stable 64.2/100. Ajustement analyste ~42/100. Earnings Q1 J=0 non résolu après 8 jours. Pas de position.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 6.51% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
