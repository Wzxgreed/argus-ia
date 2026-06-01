# CONTEXT — SQ — Dernière mise à jour : 2026-06-01

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Score global :** 58.0/100 (agent reco) / ~59.0/100 (lecture institutionnelle avec plafonnement qualité)
- **Prix cible :** $85.67 (consensus, 3 analystes)
- **Stop-loss :** — (bloqué par stale price)
- **Statut thèse :** Confirmée inchangée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Stale Price CRITICAL** — cours $83.46 figé ≥25 snapshots / ≥12 jours calendaires (source fmp_fallback)
- 🔴 **Earnings Placeholder Glissant** — J=0 depuis 12+ jours (date initiale 20/05), champ details vide (placeholder FMP)
- 🔴 **Quality Gate Exclusion** — SQ excluded (stale_price_history CRITICAL 4j)
- 🔴 **Pipeline Degradation** — 5 [ERROR] validation (>2), divergence validation/gate persistante
- 🟡 **Consensus PT Figé** — $85.67 (3 analystes) inchangé depuis 27/05
- 🟡 **Rotation Défensive** — signal `ROTATION_TO_DEFENSIVE` sectoriel (crossover bearish XLE)

---

## 📅 Prochains événements

- **2026-06-01** · earnings · Earnings (placeholder glissant, date réelle non confirmée)
- **Action urgente :** Vérifier date réelle Q1 2026 via IR Block / SEC EDGAR

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** — (données manquantes, bloc technical vide)
- **MM 50j :** — (données manquantes)
- **MM 200j :** — (données manquantes)
- **ATR 14j :** — (données manquantes)
- **Volume moy. 20j :** — (données manquantes)
- **Volume snapshot :** 1.14M
- **Cours :** $83.46 (stale, figé depuis 20/05)

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-01
- **Type :** update
- **Fichier :** `SQ_2026-06-01_update.md` (snapshot 13:00 UTC)
- **Conclusion :** ATTENDRE — Qualité 3/6 hors périmètre, stale price ≥25 snapshots / 12+ jours, earnings placeholder glissant, consensus figé, zero changement données brutes vs snapshot 10:00 UTC, scoring agent reco révisé à 5.8/10 (non plafonné) mais lecture institutionnelle maintenue à 5.4/10 avec plafond qualité 5.0/10.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
