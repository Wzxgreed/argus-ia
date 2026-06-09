# CONTEXT — AST — Dernière mise à jour : 2026-06-09

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (AST placeholder 55.2/100) / ATTENDRE (ASTS proxy 51.0/100)
- **Score global :** 55.2/100 (AST placeholder) / 51.0/100 (ASTS proxy)
- **Prix cible :** $94.54 (consensus ASTS, 12 analysts)
- **Stop-loss :** $65.94 (ASTS proxy, SL = cours − 2×ATR 13.06)
- **Statut thèse :** ATTENDRE — stabilité totale, aucun nouveau catalyseur
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Anomalie structurelle AST :** >34 snapshots consécutifs sans données de cours (18/05 → 09/06). Doublon probable avec ASTS. Recommandation : supprimer AST de la watchlist ou marquer `excluded`.
- 🟡 **Anomalie options JSON ASTS :** dans `data/2026-06-09.json`, max pain affiché à $45.0 (aberrant, -62.5%), put/call et call OI null. Identifié comme faux positif de pipeline (3e occurrence cette semaine). Valeurs opérationnelles à retenir : max pain **$120.0**, put/call **0.7**, call OI **59.0%**.
- 🟡 **Earnings placeholder glissant AST :** FMP indique J=0 depuis le 25/05 (16+ jours de glissement), résultats non intégrés au pipeline.

---

## 📅 Prochains événements

- **2026-06-12** · Échéance options ASTS (dans 3 jours) — risque gamma actif, max pain $120.0 (+30.3%)
- **2026-08-10** · Earnings ASTS (yfinance, 63j) — estimations EPS $-0.29 à $-0.17, Revenues $0.0B

---

## 📊 Contexte technique (dernier snapshot)

- **Cours ASTS (proxy) :** $92.06 (stable vs close 08/06)
- **RSI 14j :** 52.33 (zone neutre favorable)
- **MM 50j :** $88.50 (support +4.0%)
- **MM 200j :** null
- **ATR 14j :** 13.06
- **Volume moy. 20j :** 27.06M
- **Volume séance :** 13.62M (0.50×)
- **52W high/low :** $133.86 / $34.21
- **Distance 52W high :** -31.2%

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-09
- **Type :** update (snapshot matinal 10h UTC, pré-ouverture US)
- **Fichier :** `AST_2026-06-09_update.md`
- **Conclusion :** Stabilité totale des données ASTS vs close 08/06. Aucune mutation technique ni fondamentale. Nouvelle anomalie options JSON (max pain $45.0 aberrant, P/C et call OI null) — faux positif de pipeline. Échéance options 06-12 dans 3 jours. Earnings placeholder glissant J=0 persistant (16+ jours). Thèse ASTS : ATTENDRE confirmée (51.0/100, timing Favorable). Support immédiat MM50j $88.50, résistance $97.00.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
