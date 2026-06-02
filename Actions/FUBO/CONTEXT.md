# CONTEXT — FUBO — Dernière mise à jour : 2026-06-02

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — pas d'entrée en l'état. Surveiller la convergence vers max pain $12.00 à échéance J+3 (2026-06-05).
- **Score global :** ~56.5/100
- **Prix cible :** $12.91 (TP ATR 3×)
- **Stop-loss :** $9.76 (2× ATR)
- **Statut thèse :** MODIFIÉE (was ACHETER Réduit ~64.5/100)
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **CORRECTION TECHNIQUE + VOLUME COLLAPSE** — Cours −4.34% à $11.02, volume 0.38× (536k), franchissement sous MM50
- **Downgrade Agent Majeur** — ACHETER Standard 78.5/100 → ATTENDRE 58.0/100, Score Momentum 7.0 → 4.0
- **Structure Options Haussière Persistante** — Max pain $12.00, put/call 0.20, call OI 83.2%, spot à −8.2% sous max pain
- **Short Squeeze Setup (latent)** — short interest 25.03% + call OI 83.2% + put/call 0.20
- **Earnings Q1 2026 en attente** — anomalie calendrier persistante (jour J, `days_until: 0`, aucun résultat visible)

---

## 📅 Prochains événements

- **2026-06-05** · options · Échéance options (J+3) — max pain $12.00, put/call 0.20, call OI 83.2%
- **2026-06-02** · earnings · Earnings Q1 anomalie persistante (jour J, aucun résultat visible)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 62.22
- **MM 50j :** 11.1
- **MM 200j :** —
- **ATR 14j :** 0.63
- **Volume moy. 20j :** 1400995
- **Volume session :** 536103 (0.38×)
- **Cours close :** 11.02
- **Spot vs MM50 :** −0.7% (sous MM50)
- **Spot vs Max Pain :** −8.2%

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-02
- **Type :** update
- **Fichier :** `FUBO_2026-06-02_update.md`
- **Conclusion :** Correction technique −4.34% à $11.02 sur volume collapse 0.38×, RSI sort de la zone proche-surachat (62.22), cours franchissant sous MM50 ($11.10). Downgrade agent majeur (ACHETER Standard 78.5/100 → ATTENDRE 58.0/100). Score Momentum 7.0 → 4.0 (momentum baissier). Structure options haussière inchangée (max pain $12.00, put/call 0.20, call OI 83.2%) mais spot à −8.2% sous max pain. Thèse MODIFIÉE en ATTENDRE (~56.5/100).

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif persistant depuis 2026-05-17
- **Franchissement sous MM50** — cours $11.02 vs MM50 $11.10
- **Volume collapse** — 0.38× moyenne 20j
- **Downgrade agent** — ACHETER → ATTENDRE

---

*Généré automatiquement — ne pas éditer manuellement.*
