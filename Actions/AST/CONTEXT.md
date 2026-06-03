# CONTEXT — AST — Dernière mise à jour : 2026-06-03

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** —
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** 🔴 INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>26 SNAPSHOTS)
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **Anomalie structurelle :** AST (ticker NASDAQ) sans données de cours depuis >26 snapshots consécutifs (18/05 → 03/06) — probable doublon erroné d'ASTS (AST SpaceMobile)
- **Anomalie options ASTS (proxy) :** max pain JSON $40.0 aberrant (vs cours $118.17) → valeur opérationnelle $120.0 conservée ; put/call ratio et call OI passés à null (données dégradées)
- **Earnings placeholder glissant :** FMP signale earnings AST le 2026-06-03 (days_until: 0) — 11 jours de glissement consécutifs non résolus

---

## 📅 Prochains événements

- **2026-06-03** · earnings · Earnings (FMP placeholder glissant J=0, 11 jours de glissement)
- **2026-08-10** · earnings · ASTS earnings (proxy) — Est EPS $−0.29 à $−0.17, Rev $0.0B
- **2026-06-05** · options expiration · Échéance options ASTS (proxy) — max pain opérationnel $120.0

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

### ASTS (proxy, données du 2026-06-03 10:00 UTC)
- **Cours :** $118.17 (stable vs close 02/06, pre-market)
- **RSI 14j :** 72.58 (surachat consolidé)
- **MM 50j :** 87.67
- **ATR 14j :** 12.22
- **Volume :** 21.29M (0.78× moy. 20j)
- **Support immédiat :** $108.80 (low intra-day 02/06)
- **Résistance immédiate :** $118.74–120.00 (high intra-day + max pain opérationnel)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-03
- **Type :** update
- **Fichier :** `AST_2026-06-03_update.md`
- **Conclusion :** >26e snapshot consécutif sans mutation pour AST — stabilité totale confirmée. ASTS (proxy) stable à $118.17 (pre-market) sur volume 0.78×, RSI 72.58 surachat consolidé. Agent maintient ASTS ÉVITER (29.8/100). Anomalie options JSON détectée et traitée (max pain $40.0 aberrant → $120.0 conservé). Earnings placeholder glissant J=0 à 11 jours. Recommandation : résoudre anomalie structurelle (supprimer AST ou marquer excluded), rediriger exposition vers ASTS.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
