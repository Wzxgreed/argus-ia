# CONTEXT — FUBO — Dernière mise à jour : 2026-05-26

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER
- **Score global :** ~4.2/10 (~42/100)
- **Prix cible :** $—
- **Stop-loss :** $8.32
- **Statut thèse :** Confirmée — pas de position
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **PRICE_GAP** (medium) — Gap +6.67% overnight (seuil ±5.0%) — 2026-05-25, partiellement effacé par −1.95% le 2026-05-26
- **ATR_SPIKE** (medium) — ATR relatif 6.49% (seuil 5.0%) — persistant depuis 2026-05-17
- **RSI SURVENTE EXTRÊME** — RSI 21.26 (seuil 30) — 2026-05-26
- **Earnings Q1 2026 en attente** — anomalie calendrier : `upcoming_events_latest.json` place l'earnings au **2026-05-26** (jour J), mais aucun résultat visible dans `data/latest.json` au snapshot 17:00 UTC — J+7 non résolu
- **Divergence Yahoo/FMP Market Cap** — ×11.6 d'écart entre sources ($281.4M vs ~$3.27B)
- **Sector Rotation XLC Bottom 3** — malus sectoriel actif (snapshot 2026-05-26 : momentum score 0.0 / 10)
- **Options Spot/Max Pain Divergence** — spot $9.56 vs max pain $10.00 (écart −4.4%) ; call OI dominant 62.3%
- **Liquidité critique** — volume 0.37× moyenne 20j (517k vs 1.41M) — risque de slippage majeur
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif
- **Short Squeeze Setup (latent)** — short interest 22.84% + call OI dominant 62.3% = risque de squeeze technique si catalyseur positif

---

## 📅 Prochains événements

- **2026-05-26** · earnings · Earnings Q1 2026 (anomalie calendrier — J=0 non résolu après 7 jours)
- **2026-05-29** · options expiration · Échéance options (max pain $10.00, put/call 0.60, call OI 62.3%)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 21.26
- **MM 50j :** 11.42
- **MM 200j :** —
- **ATR 14j :** 0.62
- **Volume moy. 20j :** 1413924
- **Volume session :** 517593 (0.37×)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-26 (snapshot 17:00 UTC)
- **Type :** update
- **Fichier :** `FUBO_2026-05-26_update.md`
- **Conclusion :** THÈSE CONFIRMÉE — SURVEILLER. Cours $9.56 (−1.95%), volume effondré à 0.37× (liquidité critique), RSI 21.26 survente extrême, max pain $10.00 pinning baissier intensifié (−4.4%), momentum agent retrait à 4.5/10. Score Global ajusté agent 64.2/100, ajustement analyste ~42/100 sur base liquidité critique + earnings Q1 J=0 non résolu après 7 jours. Pas de position.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 6.49% (seuil 5.0%) — couvert par update.md du 2026-05-26

---

*Généré automatiquement — ne pas éditer manuellement.*
