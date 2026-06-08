# CONTEXT — SQ — Dernière mise à jour : 2026-06-08

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 59.0/100
- **Prix cible :** $85.67 (consensus)
- **Stop-loss :** — (attendre résolution stale price)
- **Statut thèse :** Confirmée — ATTENDRE
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price aggravé** — cours figé ≥47 snapshots / ≥20 jours calendaires (2026-05-20 → 2026-06-08). SQ est le cas le plus ancien et le plus sévère de stale price dans le snapshot.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **21 jours calendaires** (date initiale 20/05). `upcoming_events_2026-06-08.json` affiche `days_until: 0` avec date 08/06 (glissement depuis 20/05), mais champ details vide (placeholder FMP générique).
- 🔴 **Source FMP Fallback** — SQ est le **dernier ticker** du snapshot 08/06 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🔴 **Pipeline Degradation** — `validation_report.txt` (16:07 UTC) affiche **5 [ERROR]** (VRT schema + AST/AXA/ASTSPACE/QTBS fetch) — seuil >2 franchi, stable vs 12:07 UTC.
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) reste top3 sectoriel avec momentum score 10.0, mais le signal global reste **`NEUTRAL`** (crossovers vides). Vent favorable growth/tech atténué.
- Aucune alerte de seuil de cours déclenchée

---

## 📅 Prochains événements

- **2026-06-08** · earnings · Earnings (placeholder glissant depuis 20/05)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** — (bloc technical vide)
- **MM 50j :** — (données manquantes)
- **MM 200j :** — (données manquantes)
- **ATR 14j :** — (données manquantes)
- **Volume moy. 20j :** — (données manquantes)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-08
- **Type :** update
- **Fichier :** `SQ_2026-06-08_update.md` (snapshot 17h00 UTC)
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, stale price ≥47 snapshots / ≥20 jours, earnings placeholder glissant 21+ jours, consensus figé $85.67, signal sectoriel NEUTRAL stable, zero mutation données brutes vs snapshot 13h00 UTC, scoring 5.4/10 institutionnel, Score Global Ajusté ~59.0.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
