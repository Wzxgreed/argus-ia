# CONTEXT — FLY — Dernière mise à jour : 2026-06-23

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 52.5/100
- **Prix cible :** $43.77 (consensus 13 analysts) / TP $41.62
- **Stop-loss :** $20.52
- **Statut thèse :** confirmée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **[ANOMALIE DATA]** `data/latest.json` snapshot 10h UTC 23/06 : max pain $18.00 aberrant, put/call null, call OI null — valeurs opérationnelles du 22/06 conservées ($50.00/0.35/74.0%)
- **[ANOMALIE SCORING]** Score Valorisation 6.0/10 incohérent avec règle Filtre Qualité (≤3/6 → plafond 5/10). Score Opportunité ajusté manuel ~5.4/10, Global Ajusté ~50.0
- **[DRAFT_refresh archivé]** Faux trigger PRICE_GAP −6.43% / ATR_SPIKE (carry-over close 22/06) — traité dans `FLY_2026-06-23_update.md`

---

## 📅 Prochains événements

- **Earnings Q2 2026** — 2026-08-04 (42 jours) — Est EPS −$0.61 à −$0.45, Rev $0.1B
- **Expiration options** — 2026-06-26 (J-3) — max pain $50.00, spot −42.1%, calls OTM $35–$40 à risque d'expiration sans valeur

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 27.41
- **MM 50j :** 38.99
- **MM 200j :** —
- **ATR 14j :** 4.22
- **Volume moy. 20j :** 9918505

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-23
- **Type :** update
- **Fichier :** `FLY_2026-06-23_update.md`
- **Conclusion :** Thèse ATTENDRE confirmée — stabilité totale vs close officiel 22/06 (cours $28.96, volume 6.22M 0.63×, RSI 27.41, ATR 4.22, MM50 38.99 inchangés). [ANOMALIE DATA] Options corrompues dans `latest.json` (max pain $18.00 aberrant) — valeurs opérationnelles du 22/06 conservées. DRAFT_refresh déclenché par faux trigger (carry-over close 22/06) — archivé. Scores inchangés (Opp 5.6, Global 52.5), timing Défavorable. SL/TP $20.52/$41.62. Pas de position recommandée.

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap −6.43% vs prior close $30.95 (seuil ±5.0%) — **FAUX TRIGGER** : carry-over du close 22/06, pas de nouveau mouvement overnight
- **ATR_SPIKE** (medium) — ATR relatif 14.57% (seuil 5.0%) — **FAUX TRIGGER** : ATR stable à 4.22 vs close 22/06

---

*Généré automatiquement — ne pas éditer manuellement.*
