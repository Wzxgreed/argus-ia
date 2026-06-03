# CONTEXT — SQ — Dernière mise à jour : 2026-06-03

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100 (~59.0 institutionnel)
- **Prix cible :** $85.67 (consensus 3 analystes)
- **Stop-loss :** $— (non défini — stale price)
- **Statut thèse :** Confirmée — qualité hors périmètre 3/6, stale price ≥14 jours, earnings placeholder glissant
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price aggravé** — cours figé ≥31 snapshots / ≥14 jours calendaires (2026-05-20 → 2026-06-03). SQ est le cas le plus ancien et le plus sévère de stale price dans le snapshot.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **14+ jours calendaires** (date initiale 20/05). `upcoming_events_2026-06-03.json` affiche `days_until: 0` avec date 03/06 (glissement depuis 20/05), mais champ details vide (placeholder FMP générique).
- 🔴 **Source FMP Fallback** — SQ est le **dernier ticker** du snapshot 03/06 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🔴 **Pipeline Degradation** — `validation_report.txt` (09:07 UTC) affiche **6 [ERROR]** (VRT schema + AST/AXA/SPCX/QTBS/ASTSPACE fetch) — seuil >2 franchi, stable vs 02/06.
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) reste top3 sectoriel avec momentum score 10.0, mais le signal global est **`NEUTRAL`** (crossovers vides). Vent favorable growth/tech atténué.
- Aucune alerte de seuil de cours déclenchée

---

## 📅 Prochains événements

- **2026-06-03** · earnings · Earnings (placeholder FMP, date glissante, 14ème jour)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (données manquantes — bloc technical vide)
- **MM 50j :** N/A (données manquantes)
- **MM 200j :** N/A (données manquantes)
- **ATR 14j :** N/A (données manquantes)
- **Volume moy. 20j :** N/A (données manquantes)
- **Cours affiché :** $83.46 (⚠️ stale ≥14 jours)
- **Volume :** 1.14M

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-03
- **Type :** update
- **Fichier :** `SQ_2026-06-03_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, stale price ≥31 snapshots / ≥14 jours, earnings placeholder glissant 14+ jours (date 03/06), consensus figé $85.67 (3 analystes), signal sectoriel NEUTRAL stable, zero mutation données brutes vs 02/06, scoring institutionnel 5.4/10, Score Global Ajusté ~59.0, validation 6 [ERROR].

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
