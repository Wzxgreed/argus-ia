# CONTEXT — AXA — Dernière mise à jour : 2026-06-22

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 10h du 22/06 — fichier exploitable) :** Le fichier `data/sector_rotation_2026-06-22.json` est valide ce matin (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **3e/11** (vs 4e/11 le 17/06) par effet mécanique, momentum **4.25/10** (vs 5.32/10), RS 20j **+2.70%** (vs +3.46%), RS 60j **−5.91%** (vs −4.38%). Le rang remonte car d'autres secteurs ont sous-performé davantage, mais le momentum propre de XLF se dégrade. C'est une **dégradation sous-jacente** marginalement négative pour un assureur. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

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
- **Fichier :** `AXA_2026-06-22_update.md`
- **Conclusion :** Thèse ATTENDRE confirmée. Données AXA toujours manquantes (24e snapshot consécutif). Contexte sectoriel XLF en dégradation sous-jacente (momentum 4.25/10 vs 5.32/10, RS 60j −5.91% vs −4.38%). Earnings J0 FMP glissant sans détails (24e occurrence consécutive). Action immédiate : corriger le symbole (`CS.PA` ou `AXAHY`).

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
