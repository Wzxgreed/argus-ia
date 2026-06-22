# CONTEXT — AXA — Dernière mise à jour : 2026-06-22 (snapshot 17h UTC)

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 17h du 22/06 — fichier exploitable) :** Le fichier `data/sector_rotation_2026-06-22.json` est valide ce soir (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **3e/11** (stable vs 13h), momentum **5.15/10** (vs 4.25/10 à 13h), RS 20j **+3.40%** (vs +2.70%), RS 60j **−4.71%** (vs −5.91%). L'amélioration est **organique** (return 20j +3.94%) et portée par la performance propre du secteur. C'est un **vent arrière théorique marginalement positif** pour un assureur. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

**Action immédiate :** corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`), mettre à jour le secteur (Financials / Insurance) et relancer le fetch.

---

## 📜 Historique des analyses
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** —
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Aucune alerte active.

---

## 📅 Prochains événements

- **2026-06-22** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-22
- **Type :** update
- **Fichier :** `AXA_2026-06-22_update_17h.md`
- **Conclusion :** Thèse ATTENDRE confirmée — données AXA toujours manquantes (26e snapshot consécutif), contexte sectoriel XLF en amélioration organique (momentum +0.90 pt, RS 20j +0.70 pp, RS 60j +1.20 pp). Recommandation ATTENDRE stable (Score Global 55.2/100).

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
