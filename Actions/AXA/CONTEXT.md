# CONTEXT — AXA — Dernière mise à jour : 2026-06-23

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 10h du 23/06 — fichier exploitable) :** Le fichier `data/sector_rotation_2026-06-23.json` est valide ce matin (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **3e/11** (stable), momentum **5.45/10** (vs 5.08/10 hier soir), RS 20j **+3.69%** (vs +3.33%), RS 60j **−4.41%** (vs −4.79%), return 20j **+4.17%** (vs +3.81%). **Amélioration organique confirmée** sur les quatre métriques sectorielles (momentum +0.37 pt, RS 20j +0.36 pp, RS 60j +0.38 pp, return 20j +0.36 pp). Le secteur Financials confirme sa place dans le top 3 avec une dynamique positive, ce qui constitue un vent arrière théorique marginalement positif pour un assureur. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

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

- **2026-06-23** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-23
- **Type :** preview
- **Fichier :** `AXA_2026-06-23_preview.md`
- **Conclusion :** > **Date :** 2026-06-23

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
