# CONTEXT — FUBO — Dernière mise à jour : 2026-06-23

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — pas d’entrée en l’état. La configuration technique, fondamentale et sectorielle est **strictement inchangée** vs le close officiel du 22/06. La survente technique (RSI 27.72) est un élément d’intérêt mais le **cours à $0.51 du 52W low ($8.31)** et l'**absence de volume** éliminent toute crédibilité à un rebond durable. Le titre reste un spéculatif fondamental dégradé (Qualité 1/6) sans catalyseur observable, sous exposition gamma vendeuse à J+3. Aucune position longue recommandée. Surveillance renforcée si rupture du 52W low.

## Historique
- **Score global :** 57.8/100
- **Prix cible :** $11.25
- **Stop-loss :** $7.20
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **52W Low sous Pression** — cours à $0.51 du 52W low ($8.31) — rupture = signal baissier majeur, gap risk — 2026-06-23
- **Spot sous Max Pain à J+3** — $8.82 < $9.00 — exposition gamma vendeuse, pinning baissier — 2026-06-23
- **Anomalie Options JSON RÉSOLUE** — snapshot 10h UTC retourne max_pain $7.50 aberrant → valeurs opérationnelles $9.00/0.66/60.3% conservées — 2026-06-23
- **ATR_SPIKE** (medium) — ATR relatif 9.19% (seuil 5.0%), persistant — 2026-06-23
- **Short Squeeze Setup (latent, atténué)** — short interest 24.32% + call OI 60.3% + put/call 0.66 = risque de squeeze réduit vs configuration précédente (69.0% / 0.45) — 2026-06-23
- **Divergence Yahoo/FMP Market Cap** — ×12.6 d'écart entre sources ($259.6M Yahoo vs $3,268.5M FMP) — anomalie data persistante — 2026-06-23
- **Sector Rotation XLC Bottom 3** — malus sectoriel confirmé (momentum score 0.0, `data/sector_rotation_latest.json`) — 2026-06-23
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif

---

## 📅 Prochains événements

- **Earnings Q2 2026** — `upcoming_events_latest.json` (2026-06-23) place l'earnings au **2026-08-06** (44 jours, Est EPS $-0.32-$0.07, Rev $1.5B).
- Échéance options : **2026-06-26** (J+3 — max pain $9.00, put/call 0.66, call OI 60.3%)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 27.72
- **MM 50j :** 10.78
- **MM 200j :** —
- **ATR 14j :** 0.81
- **Volume moy. 20j :** 1435365

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-23
- **Type :** update
- **Fichier :** `FUBO_2026-06-23_update.md`
- **Conclusion :** Stabilité mécanique totale vs close 22/06. Anomalie options JSON traitée. Thèse ATTENDRE confirmée (57.8/100). DRAFT_refresh traité (ATR_SPIKE déjà intégré).

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 9.19% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
