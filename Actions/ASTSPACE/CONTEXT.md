# CONTEXT — ASTSPACE — Dernière mise à jour : 2026-06-03

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** —
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** invalidée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **Anomalie structurelle :** ASTSPACE probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). Aucune donnée de marché depuis 33+ snapshots consécutifs (erreur Yahoo : *No price history*).
- **Placeholder glissant :** Earnings FMP signalé à J=0 depuis >6j (glissé du 29/05 au 03/06) — résultats non intégrés au pipeline.
- **Anomalie options JSON (proxy ASTS) :** Max Pain brut $40,00 aberrant (écart −66% vs cours) → valeur opérationnelle $120,00 conservée. Put/Call et Call OI passés à null → valeurs opérationnelles 1,09 et 47,9% conservées.

---

## 📅 Prochains événements

- **2026-06-03** · earnings · Earnings placeholder glissant (FMP, non résolu)
- **2026-06-05** · options expiry · ASTS nearest expiry — Max Pain $120,00 (opérationnel), put/call 1,09, call OI 47,9%
- **2026-08-10** · earnings · ASTS earnings (yfinance) — Est. EPS $−0,29 à $−0,17, Revenues $0,0B

---

## 📊 Contexte technique (dernier snapshot)

### ASTSPACE (données officielles)
- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

### ASTS (proxy — données du snapshot 10h UTC 2026-06-03)
- **Cours close :** $118,17 (inchangé vs close 02/06)
- **RSI 14j :** 72,58 (surachat persistant)
- **MM 50j :** $87,67
- **MM 200j :** —
- **ATR 14j :** $12,22
- **Volume relatif :** 0,78× moy. 20j (21,29M vs 27,47M)
- **Distance MM50j :** +34,7%
- **52W high :** $133,86 (−11,7%)
- **Max Pain (opérationnel) :** $120,00 (+1,5% vs cours)
- **Put/Call (opérationnel) :** 1,09
- **Call OI % (opérationnel) :** 47,9%

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-03
- **Type :** update
- **Fichier :** `ASTSPACE_2026-06-03_update.md`
- **Conclusion :** Stabilité totale du proxy ASTS à $118,17 sur volume 0,78× stable. RSI surachat 72,58 persistant. Anomalies options JSON détectées et traitées (max pain $40 aberrant → $120 conservé, put/call et call OI null → 1,09 et 47,9% conservés). EV/Revenue mécanique 422× (+44× vs veille). Score agent ASTS inchangé ÉVITER 29,8/100. Thèse confirmée : ASTSPACE indisponible, doublon probable d'ASTS.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
