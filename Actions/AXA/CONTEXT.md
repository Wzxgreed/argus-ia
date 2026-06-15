# CONTEXT — AXA — Dernière mise à jour : 2026-06-15

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (dernier snapshot fiable : 2026-06-15 10h00 UTC) :** Le secteur Financials (XLF) affiche une **amélioration continue** depuis le 09/06 : return 20j **+4.00%** (+1.50 pp vs 09/06), return 60j **+9.48%** (+1.63 pp), RS 20j **+4.85%** (+2.04 pp), RS 60j **−2.97%** (+0.77 pp), momentum score **6.73/10** (+1.54 pt). Le rang sectoriel est au **2e/11** (+1 place vs 09/06). Le signal macro reste `UNKNOWN` (stable depuis le 02/06). Le fichier `data/sector_rotation_2026-06-15.json` est validé et exploitable.

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

- **[CRITICAL]** Pas de données de prix pour AXA — ticker probablement incorrect
- **[WARNING]** Earnings J0 (2026-06-15) sans consensus ni résultats exploitables — pattern persistant depuis mi-mai (14e occurrence consécutive)

---

## 📅 Prochains événements

- Aucun événement à venir identifié (earnings J0 FMP glissant sans détails).

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-15
- **Type :** update
- **Fichier :** `AXA_2026-06-15_update.md`
- **Conclusion :** Données AXA toujours indisponibles. Récupération du fichier sectoriel : XLF en amélioration continue (RS 20j +4.85%, momentum 6.73/10, rang 2e/11). Thèse ATTENDRE confirmée à 55.2/100. Earnings J0 FMP glissant sans résolution (14e jour consécutif). Action immédiate : corriger le symbole dans config/watchlist.json.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
