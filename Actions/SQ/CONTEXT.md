# CONTEXT — SQ — Dernière mise à jour : 2026-06-09 · Snapshot 21h00 UTC

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** ~59.0/100
- **Prix cible :** $85.67 (consensus, 3 analystes)
- **Stop-loss :** — (attendre résolution stale price)
- **Statut thèse :** Bloqué — stale price ≥52 snapshots / ≥21 jours calendaires
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée (absence totale de données live depuis 20/05).

---

## 🚨 Alertes actives

- 🔴 **Stale Price aggravé** — cours figé ≥52 snapshots / ≥21 jours calendaires (2026-05-20 → 2026-06-09). SQ est le cas le plus ancien et le plus sévère de stale price dans le snapshot.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **≥52 snapshots consécutifs** (date initiale 20/05, glissée au 09/06). Placeholder FMP générique partagé avec 7 autres tickers.
- 🔴 **Source FMP Fallback** — SQ est le **dernier ticker** du snapshot 09/06 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) reste top3 sectoriel avec momentum score 10.0, mais le signal global reste **`NEUTRAL`** (crossovers vides). Vent favorable growth/tech atténué.
- Aucune alerte de seuil de cours déclenchée.

---

## 📅 Prochains événements

- **2026-06-09** · 🔴 **Earnings Q1 2026 (placeholder glissant)** — résultats **toujours non intégrés** dans le snapshot 09/06 (**≥52 snapshots après date initiale 20/05**). `upcoming_events_2026-06-09.json` affiche `"date": "2026-06-09"` avec `"days_until": 0`, mais le champ `"details": "Earnings "` est vide (placeholder FMP générique).
- **Action opérationnelle urgente :** Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR. Forcer re-fetch isolé de SQ (`scripts/fetch_prices.py --tickers SQ`) pour diagnostiquer l'échec spécifique du worker daemon.
- Post-earnings : réviser le Filtre Qualité, le scoring, et le timing technique dès disponibilité des données RSI/ATR/MM **non stale**.
- Vérifier résolution du stale price dans le prochain snapshot (risque de gap violent ±10–15% à réouverture).

---

## 📊 Contexte technique (dernier snapshot 21h00 UTC)

- **RSI 14j :** N/A (bloc `technical` vide depuis 17/05)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A
- **Volume du jour :** 1,142,032 (figé)
- **High/Low du jour :** $85.07 / $83.13 (figés)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-09
- **Type :** update
- **Fichier :** `SQ_2026-06-09_update_21h00.md`
- **Conclusion :** **ATTENDRE** — Qualité 3/6 (hors périmètre), stale price ≥52 snapshots / ≥21 jours, earnings placeholder glissant ≥52 snapshots, consensus figé $85.67 (3 analystes), signal sectoriel NEUTRAL stable, zero mutation données brutes vs snapshot 17h00 UTC, Score Global Ajusté ~59.0, validation 5 [ERROR] (identique 16:07 UTC).

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
