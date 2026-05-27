# CONTEXT — FUBO — Dernière mise à jour : 2026-05-27

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER
- **Score global :** ~42/100
- **Prix cible :** $—
- **Stop-loss :** $8.28
- **Statut thèse :** Confirmée (stabilité totale vs précédent)
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **RSI SURVENTE EXTRÊME** — RSI 21.08 (seuil 30) — persistant
- **Earnings Q1 2026 en attente** — `upcoming_events_latest.json` place l'earnings au **2026-05-27** (jour J), aucun résultat visible après 8 jours — [ANOMALIE J+8 NON RÉSOLU]
- **Anomalie Options JSON TRAITÉE** — snapshot 2026-05-27 retourne max_pain $7.50 / put/call 0.00 / call OI 100% (artefact) ; valeurs confirmées $10.00 / 0.60 / 62.3% maintenues
- **Liquidité réduite** — volume 0.70× moyenne 20j
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif
- **Short Squeeze Setup (latent)** — short interest 22.84% + call OI 62.3%
- **Divergence Yahoo/FMP Market Cap** — ×11.7 ($280.2M vs ~$3.27B)
- **Sector Rotation XLC Bottom 3** — malus sectoriel actif

---

## 📅 Prochains événements

- **2026-05-27** · earnings · Earnings Q1 2026 (J=0, non résolu)
- **2026-05-29** · options · Échéance options (max pain $10.00, J+2)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 21.08
- **MM 50j :** 11.42
- **MM 200j :** —
- **ATR 14j :** 0.62
- **Volume moy. 20j :** 1,438,260
- **Close :** $9.52
- **Volume vs 20j :** 0.70×

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-27
- **Type :** update
- **Fichier :** `FUBO_2026-05-27_update.md`
- **Conclusion :** Stabilité totale vs snapshot précédent (close $9.52 inchangé, RSI 21.08, volume 1,004,300 / 0.70×). Anomalie options JSON détectée et traitée (valeurs aberrantes remplacées par historique confirmé $10.00 / 0.60 / 62.3%). Earnings Q1 J=0 non résolu après 8 jours. Thèse SURVEILLER (~42/100) confirmée sans modification.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 6.51% (seuil 5.0%) — persistant depuis 2026-05-17

---

*Généré automatiquement — ne pas éditer manuellement.*
