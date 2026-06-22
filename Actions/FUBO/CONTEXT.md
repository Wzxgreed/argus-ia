# CONTEXT — FUBO — Dernière mise à jour : 2026-06-22

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — pas d'entrée en l'état. La résolution de l'anomalie options JSON (snapshot 13h UTC) est une avancée data quality, mais les valeurs corrigées révèlent une **structure options moins favorable** qu'antérieurement estimée. Le max pain révisé à **$9.00** (vs $11.00 réf. opérationnelle), le put/call à **0.66** (vs 0.45) et le call OI à **60.3%** (vs 69.0%) éliminent le catalyseur technique latent lié au pinning haussier vers $11.00. Le spot ($9.22) est désormais +2.4% au-dessus du max pain (configuration « pinning neutre »). Les données de marché (cours, volume, RSI, ATR, MM50) sont strictement identiques au snapshot 10h. Aucune position longue recommandée.

## Historique
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **Anomalie Options JSON RÉSOLUE — PIVOT STRUCTUREL** — snapshot 13h UTC corrige l'incohérence 10h avec des valeurs cohérentes mais moins favorables : max pain $9.00 (vs $11.00), put/call 0.66 (vs 0.45), call OI 60.3% (vs 69.0%). Spot passe de −16.2% sous max pain à +2.4% au-dessus — pinning neutre / légèrement baissier — 2026-06-22
- **Structure Options Neutre / Légèrement Baissière** — max pain $9.00, put/call 0.66, call OI 60.3%, spot +2.4% au-dessus du max pain — élimination du catalyseur technique latent — 2026-06-22
- **ATR_SPIKE** (medium) — ATR relatif 9.44% (seuil 5.0%) — 2026-06-22
- **Short Squeeze Setup (latent, atténué)** — short interest 24.32% + call OI 60.3% + put/call 0.66 = risque de squeeze réduit vs configuration précédente — 2026-06-22
- **Divergence Yahoo/FMP Market Cap** — ×12.0 d'écart entre sources ($271.4M Yahoo vs $3,268.5M FMP) — 2026-06-22
- **Sector Rotation XLC Bottom 3** — malus sectoriel confirmé (momentum score 0.0) — 2026-06-22
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif

---

## 📅 Prochains événements

- **Earnings Q2 2026** — 2026-08-06 (45 jours, Est EPS $-0.32-$0.07, Rev $1.5B)
- **Échéance options** — 2026-06-26 (J+4, max pain $9.00, put/call 0.66, call OI 60.3%)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 43.86
- **MM 50j :** 10.85
- **MM 200j :** —
- **ATR 14j :** 0.87
- **Volume moy. 20j :** 1424415
- **Volume session :** 1712500 (1.20×)
- **Close :** 9.22
- **High :** 9.35
- **Low :** 8.48
- **52W Low :** 8.31
- **52W High :** 56.64

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-22
- **Type :** update
- **Fichier :** `FUBO_2026-06-22_update.md`
- **Conclusion :** Thèse ATTENDRE CONFIRMÉE — options landscape révisé à la baisse. Snapshot 13h UTC : stabilité totale données marché (close $9.22, volume 1.20×, RSI 43.86, écart MM50 −15.0% inchangés vs 10h). Anomalie options JSON résolue avec valeurs corrigées moins favorables (max pain $9.00 vs $11.00, put/call 0.66 vs 0.45, call OI 60.3% vs 69.0%). Structure options moins haussière, spot désormais +2.4% au-dessus du max pain (pinning neutre). Scoring agent ATTENDRE 52.8/100 inchangé. ATR_SPIKE 9.44% actif. Timing Défavorable. Aucune position longue recommandée.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 9.44% (seuil 5.0%)
- **OPTIONS_PIVOT** — max pain révisé de $11.00 à $9.00, put/call de 0.45 à 0.66, call OI de 69.0% à 60.3%

---

*Généré automatiquement — ne pas éditer manuellement.*
