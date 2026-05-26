# CONTEXT — FUBO — Dernière mise à jour : 2026-05-26

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER
- **Score global :** ~5.2/10 (ajusté analyste) / 65.5/100 (brut agent)
- **Prix cible :** $11.64 (TP ATR 3×)
- **Stop-loss :** $8.49 (2× ATR)
- **Statut thèse :** Confirmée — pas de position
- **Horizon :** 1–3 mois (si entrée technique confirmée)

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **PRICE_GAP** (medium) — Gap +6.67% overnight (seuil ±5.0%) — 2026-05-25
- **ATR_SPIKE** (medium) — ATR relatif 6.46% (seuil 5.0%) — persistant depuis 2026-05-17
- **RSI SURVENTE EXTRÊME** — RSI 20.19 (seuil 30) — 2026-05-25
- **Earnings Q1 2026 en attente** — anomalie calendrier : `upcoming_events_latest.json` place l'earnings au **2026-05-26** (jour J), mais aucun résultat visible — vérification impérative au prochain snapshot
- **Divergence Yahoo/FMP Market Cap** — ×11.4 d'écart entre sources ($287.0M vs ~$3.27B)
- **Sector Rotation XLC Bottom 3** — malus sectoriel actif (snapshot 2026-05-26 : momentum score 0.0 / 10)
- **Options Spot/Max Pain Divergence** — spot $9.75 vs max pain confirmé $9.00 (écart +8.3%) ; call OI dominant 60.6%
- **Anomalie Options JSON** — snapshot 2026-05-26 brut API retourne max_pain 7.50, put/call 0.00, call OI 100.0% (valeurs aberrantes vs historique) — valeurs confirmées 25/05 conservées
- **Liquidité réduite** — volume 0.75× moyenne 20j (1.10M vs 1.46M) — risque de slippage majeur
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif
- **Short Squeeze Setup (latent)** — short interest 22.84% + call OI dominant 60.6% = risque de squeeze technique si catalyseur positif

---

## 📅 Prochains événements

- **2026-05-26** · earnings · Earnings Q1 2026 (jour J, non résolu après 6 jours)
- **2026-05-29** · options expiration · Échéance options (max pain confirmé $9.00)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 20.19
- **MM 50j :** 11.52
- **MM 200j :** —
- **ATR 14j :** 0.63
- **Volume moy. 20j :** 1462240
- **Volume dernière séance :** 1101200 (0.75×)
- **Beta :** 2.508
- **52W Low :** 8.31
- **52W High :** 56.64

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-26
- **Type :** update
- **Fichier :** `FUBO_2026-05-26_update.md`
- **Conclusion :** Snapshot 10:00 UTC post-Memorial Day stable vs 25/05. Cours $9.75, RSI 20.19, ATR $0.63 inchangés. Anomalie options JSON détectée (max_pain 7.50 aberrant, put/call 0.00, call OI 100%) — valeurs confirmées 25/05 conservées. Earnings Q1 J=0 non résolu après 6 jours. Thèse SURVEILLER confirmée (~52/100 ajusté analyste). Pas de position.

---

## 🔄 Triggers détectés (update)

- **PRICE_GAP** (medium) — Gap +6.67% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 6.46% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
