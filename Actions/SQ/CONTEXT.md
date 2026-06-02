# CONTEXT — SQ — Dernière mise à jour : 2026-06-02

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 59.0/100
- **Prix cible :** $85.67 (consensus)
- **Stop-loss :** —
- **Statut thèse :** Stable — aucune mutation données brutes vs snapshot 17h
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price** — cours figé ≥30 snapshots / ≥13 jours calendaires (2026-05-20 → 2026-06-02). SQ est le cas le plus ancien et le plus sévère de stale price dans le snapshot.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après 13+ jours calendaires (date initiale 20/05). `upcoming_events_2026-06-02.json` affiche `days_until: 0` avec date 02/06 (glissement depuis 20/05), mais champ details vide (placeholder FMP générique).
- 🔴 **Source FMP Fallback** — SQ est le dernier ticker du snapshot 02/06 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Consensus PT Figé** — Price target consensus $85.67 (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) reste top3 sectoriel avec momentum score 10.0, mais le signal global est `NEUTRAL` (crossovers vides). Vent favorable growth/tech atténué.

---

## 📅 Prochains événements

- **2026-06-02** · earnings · Earnings (placeholder glissant, non résolu)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (bloc `technical` vide)
- **MM 50j :** N/A
- **MM 200j :** N/A
- **ATR 14j :** N/A
- **Volume moy. 20j :** N/A

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-02
- **Type :** update
- **Fichier :** `SQ_2026-06-02_update.md`
- **Conclusion :** ATTENDRE — snapshot 21:00 UTC. Zero mutation données brutes SQ vs 17:00 UTC. Cours $83.46 figé ≥30 snapshots / ≥13 jours. Qualité 3/6 hors périmètre. Consensus figé $85.67 (3 analystes). Signal sectoriel NEUTRAL stable. Score Opportunité 5.4/10 institutionnel, Score Global Ajusté ~59.0.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
