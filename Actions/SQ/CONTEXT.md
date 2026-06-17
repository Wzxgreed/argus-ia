# CONTEXT — SQ — Dernière mise à jour : 2026-06-17

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 54.0/100
- **Prix cible :** $85.67 (consensus figé, 3 analystes)
- **Stop-loss :** $— (indisponible — cours stale)
- **Statut thèse :** Bloqué par anomalie de données
- **Horizon :** Jusqu'à résolution stale price + earnings

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price aggravé** — cours figé ≥63 snapshots / ≥28 jours calendaires (2026-05-20 → 2026-06-17)
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **28 jours calendaires** (date initiale 20/05, glissée au 17/06). Placeholder FMP vide.
- 🔴 **Source FMP Fallback** — SQ est le dernier ticker du snapshot avec `"fmp_fallback"` et `change_pct: null`
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) top3 mais signal global **`NEUTRAL`**
- 🟡 **Divergence Market Cap FMP** — `fundamentals` ($51.73B) vs `fmp_key_metrics` ($54.29B) ~4.8%
- 🟢 **Pipeline stable** — Agents reco/social/fx/events/sector exécutés ce 17/06

---

## 📅 Prochains événements

- **2026-06-17 (glissement)** · 🔴 **Earnings Q1 2026** — placeholder FMP J=0, champ details vide

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** — (bloc `technical` vide depuis 17/05)
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-17
- **Type :** update
- **Fichier :** `SQ_2026-06-17_update.md`
- **Conclusion :** ATTENDRE — Qualité 3/6 (hors périmètre), cours stale $83.46 figé ≥63 snapshots / ≥28 jours, earnings placeholder glissant ≥63 snapshots, consensus figé, pipeline stable mais zero mutation données brutes détectée entre 16/06 17h00 et 17/06 10h00.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
