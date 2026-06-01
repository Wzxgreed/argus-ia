# CONTEXT — SPCX — Dernière mise à jour : 2026-06-01

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
- **Prix cible :** N/A (données insuffisantes)
- **Stop-loss :** N/A
- **Upside :** —
- **Dernière mise à jour :** 2026-06-01 (snapshot 10:00 UTC)

> SPCX est un ETF thématique SPAC/post-IPO. Le snapshot du 01/06 n'a fourni aucune donnée technique Yahoo (RSI, ATR, MM50 absents) — source basculée sur `fmp_fallback`. Le volume a chuté de 95% à **196 unités** (quasi-illiquide). L'Agent Recommandation a reclassé SPCX en **ATTENDRE** avec un Score Global Ajusté de **54.0/100** (Score Opportunité 5.4/10 : C:6.5 V:5.0 M:4.5), timing Neutre. Le setup technique du 27/05 (au-dessus MM50, RSI 59.07) est suspendu par manque de données fiables. Le secteur Financials (XLF) reste hors rotation haussière (momentum_score 0.0, return_20d −1.06%). Aucun catalyseur fondamental. SL/TP non calculables (ATR absent). Rétablissement possible si retour données Yahoo complètes + volume >1 000 + Score Momentum ≥ 6.0.

---

## Actualités ayant impacté ce dossier
- **Score global :** 54.0/100
- **Prix cible :** N/A
- **Stop-loss :** N/A
- **Statut thèse :** invalidée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- 🔴 **Volume extrême anomalie** : 196 unités (−95% vs 27/05) — quasi-illiquide, marché figé.
- 🔴 **Données techniques manquantes** : RSI, ATR, MM50 absents du snapshot 01/06 (source FMP fallback).

---

## 📅 Prochains événements

- Aucun — ETF thématique, pas de calendrier earnings au sens classique. (Note : artefact FMP `earnings` days_until=0 à ignorer.)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** N/A (données manquantes)
- **MM 50j :** N/A (données manquantes)
- **MM 200j :** N/A
- **ATR 14j :** N/A (données manquantes)
- **Volume moy. 20j :** N/A (données manquantes)
- **Cours close :** $22.08 (source FMP)
- **Volume journalier :** 196
- **52w range :** $21.32 / $26.61

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-01
- **Type :** update
- **Fichier :** `SPCX_2026-06-01_update.md`
- **Conclusion :** Thèse INVALIDÉE — setup technique suspendu par absence de données Yahoo, volume quasi nul (196), reclassement ATTENDRE (Score Global 54.0). Attendre snapshot complet pour réévaluation.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manueluellement.*
