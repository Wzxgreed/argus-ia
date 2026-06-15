# CONTEXT — SQ — Dernière mise à jour : 2026-06-15 · Snapshot 21h00 UTC

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** ~54.0/100 (dernier connu, agent reco échoué au snapshot 21h00)
- **Prix cible :** $85.67 (consensus, 3 analystes)
- **Stop-loss :** N/A (attendre résolution stale price)
- **Statut thèse :** Bloquée — stale price + dégradation pipeline
- **Horizon :** Jusqu'à résolution données live + earnings Q1 2026

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price aggravé** — cours figé $83.46 sur ≥60 snapshots / ≥26 jours calendaires (20/05 → 15/06). Source `fmp_fallback` persistante.
- 🔴 **Dégradation Pipeline Systémique** — `recommandations_2026-06-15.json` 0 recommandation (agent reco échoué). Agents quant, geo, social, fx, events, accounting skipped/vides pour SQ.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après 26 jours calendaires. `upcoming_events_2026-06-15.json` affiche `days_until: 0` avec date 15/06 (glissement depuis 20/05), champ details vide (placeholder FMP).
- 🔴 **Exclusion Quality Gate** — SQ `excluded` dans `quality_gate_2026-06-15.json` (CRITICAL stale_price_history : "close identique sur 4 jours consécutifs").
- 🟡 **Divergence Validation / Quality Gate** — `validation_report.txt` (20:07 UTC) indique "0 excluded" alors que quality_gate exclut SQ. Divergence persistante.
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🟡 **Divergence Market Cap FMP** — `fundamentals.market_cap` ($51.73B) vs `fmp_key_metrics.market_cap` ($54.29B) : écart **~4.8%** (stable).
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) top3 sectoriel avec momentum score 10.0, mais le signal global reste **`NEUTRAL`** (crossovers null, regime UNKNOWN).
- Aucune alerte de seuil de cours déclenchée

---

## 📅 Prochains événements

- **2026-06-15 (glissement)** · 🔴 **Earnings Q1 2026** — résultats **toujours non intégrés** dans le snapshot 15/06 (**26 jours après date prévue**). `upcoming_events_2026-06-15.json` affiche `"date": "2026-06-15"` avec `"days_until": 0`, mais le champ `"details": "Earnings "` est vide (placeholder FMP générique).
- **Action opérationnelle urgente :**
  1. Diagnostiquer l'échec de l'agent recommandation (phase D pipeline) — vérifier logs orchestrateur.
  2. Diagnostiquer la panne du worker daemon Yahoo pour SQ — vérifier logs `yahoo_worker_daemon.py`.
  3. Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR.
  4. Forcer re-fetch isolé de SQ (`scripts/fetch_prices.py --tickers SQ`) après résolution daemon.
  5. Relancer manuellement agents skipped (quant, geo, social, fx, events, accounting) une fois données brutes résolues.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (données manquantes depuis 17/05)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A
- **Cours affiché :** $83.46 (⚠️ stale ≥60 snapshots)
- **Volume jour :** 1,142,032
- **High/Low jour :** $85.07 / $83.13
- **Previous close :** $82.99 (divergence vs close $83.46)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-15
- **Type :** update
- **Fichier :** `SQ_2026-06-15_update_21h00.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, stale price ≥60 snapshots / ≥26 jours, earnings placeholder glissant ≥60 snapshots, consensus figé, dégradation pipeline systémique (0 reco, agents skipped). Aucune mutation données brutes entre 17h00 et 21h00. Exclure SQ du périmètre long actif jusqu'à résolution.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
