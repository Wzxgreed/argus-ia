# CONTEXT — SQ — Dernière mise à jour : 2026-06-03 · Snapshot 13h UTC

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100 (~59.0 ajusté)
- **Prix cible :** $85.67 (consensus, upside +2.6%)
- **Stop-loss :** — (bloqué, stale price)
- **Statut thèse :** ATTENDRE — stale price ≥32 snapshots / ≥14 jours, earnings placeholder glissant 14+ jours
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price** — cours figé ≥32 snapshots / ≥14 jours calendaires (2026-05-20 → 2026-06-03). SQ est le cas le plus ancien et le plus sévère de stale price dans le snapshot.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **14+ jours calendaires** (date initiale 20/05). `upcoming_events_2026-06-03.json` affiche `days_until: 0` avec date 03/06 (glissement depuis 20/05), mais champ details vide (placeholder FMP générique).
- 🔴 **Source FMP Fallback** — SQ est le **dernier ticker** du snapshot 03/06 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🔴 **Pipeline Degradation** — `validation_report.txt` (12:07 UTC) affiche **6 [ERROR]** (VRT schema + AST/AXA/SPCX/QTBS/ASTSPACE fetch) — seuil >2 franchi, stable vs 10h.
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) reste top3 sectoriel avec momentum score 10.0, mais le signal global est **`NEUTRAL`** (crossovers vides). Vent favorable growth/tech atténué.
- Aucune alerte de seuil de cours déclenchée

---

## 📅 Prochains événements

- **2026-06-03** · 🔴 **Earnings Q1 2026 placeholder** — `upcoming_events_2026-06-03.json` affiche `"date": "2026-06-03"` avec `"days_until": 0`, mais champ `"details": "Earnings "` vide. Pattern placeholder FMP générique partagé avec TEST, FUBO, AST, AXA, SPCX, QTBS, ASTSPACE.
- **Action opérationnelle urgente :** Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR. Forcer re-fetch isolé de SQ (`scripts/fetch_prices.py --tickers SQ`) pour diagnostiquer l'échec spécifique du worker daemon.
- Post-earnings : réviser le Filtre Qualité, le scoring, et le timing technique dès disponibilité des données RSI/ATR/MM **non stale**
- Vérifier résolution du stale price dans le prochain snapshot (risque de gap violent ±10–15% à réouverture)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc technical vide depuis 17/05)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A
- **Cours affiché :** $83.46 (⚠️ stale, source fmp_fallback)
- **Volume :** 1.14M

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-03 · Snapshot 13h UTC
- **Type :** update
- **Fichier :** `SQ_2026-06-03_update.md`
- **Conclusion :** Thèse confirmée ATTENDRE. Stabilité totale vs snapshot 10h. Stale price ≥32 snapshots / ≥14 jours. Earnings placeholder glissant 14+ jours. Zero mutation données brutes. Score Global Ajusté ~59.0 (fourchette ATTENDRE). Exclure SQ du périmètre long actif tant que le stale price persiste.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
