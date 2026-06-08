# CONTEXT — SQ — Dernière mise à jour : 2026-06-08

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 5.4/10 (institutionnel) / 58.0/100
- **Prix cible :** $— (aucun niveau suggéré — cours stale)
- **Stop-loss :** $—
- **Statut thèse :** Paralysie totale des données — cours figé ≥48 snapshots / ≥20 jours calendaires
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price** — Cours $83.46 figé ≥48 snapshots consécutifs couvrant ≥20 jours calendaires (20/05 → 08/06). Dernier ticker avec `source: fmp_fallback` et `change_pct: null`.
- 🔴 **Earnings placeholder glissant** — Q1 2026 non résolu après 22 jours calendaires (date initiale 20/05, glissée au 08/06). Champ details vide (placeholder FMP générique).
- 🟡 **Consensus figé** — PT $85.67 (3 analystes) inchangé depuis 27/05. Silence sell-side prolongé.
- 🟡 **Rotation sectorielle neutralisée** — XLK top3 mais signal global `NEUTRAL` (crossovers vides).
- 🔴 **Pipeline degradation** — 5 [ERROR] dans validation_report.txt (VRT schema + AST/AXA/ASTSPACE/QTBS fetch), 3 [WARNING].

---

## 📅 Prochains événements

- **2026-06-08 (glissant)** · 🔴 **Earnings Q1 2026 placeholder** — résultats **toujours non intégrés** dans le snapshot 08/06 (**22 jours après date initiale**). `upcoming_events_2026-06-08.json` affiche `"date": "2026-06-08"` avec `"days_until": 0`, mais le champ `"details": "Earnings "` est vide, et ce pattern est identique pour TEST, FUBO, AST, AXA, SPCX, QTBS, ASTSPACE (7 autres tickers), suggérant un placeholder FMP générique.
- **Action opérationnelle urgente :** Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR. Forcer re-fetch isolé de SQ (`scripts/fetch_prices.py --tickers SQ`) pour diagnostiquer l'échec spécifique du worker daemon.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** — (bloc technical vide)
- **MM 50j :** — (bloc technical vide)
- **MM 200j :** — (bloc technical vide)
- **ATR 14j :** — (bloc technical vide)
- **Volume moy. 20j :** — (non disponible)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-08
- **Type :** update
- **Fichier :** `SQ_2026-06-08_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, cours stale ≥48 snapshots / ≥20 jours, earnings placeholder glissant 22+ jours, consensus figé $85.67 (3 analystes), signal sectoriel NEUTRAL stable, zero mutation données brutes SQ vs snapshot 17h00 UTC, scoring inchangé 5.4/10 institutionnel, Score Global Ajusté ~59.0, validation 5 [ERROR] (identique 16:07 UTC).

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
