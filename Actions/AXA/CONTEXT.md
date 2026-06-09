# CONTEXT — AXA — Dernière mise à jour : 2026-06-09

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 2026-06-09 21h00 UTC) :** Le secteur Financials (XLF) affiche une **amélioration significative** vs le snapshot 13h : return 20j **+2.50%** (+1.08 pp), return 60j **+7.85%** (+0.87 pp), RS 20j **+2.81%** (+1.60 pp), RS 60j **−3.74%** (+0.57 pp), momentum score **5.19/10** (+1.19 pt). Le rang sectoriel progresse au **3e/11** (+1 place). Le signal macro `NEUTRAL` est inchangé. Le snapshot confirme que les données de prix US sont bien récupérées (25 tickers OK sur 29), isolant AXA comme l'un des **4 tickers structurellement KO** sur 29.

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

- **2026-06-09** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-09
- **Type :** update
- **Fichier :** `AXA_2026-06-09_update_21h.md`
- **Conclusion :** Thèse ATTENDRE confirmée (55.2/100). Données AXA toujours indisponibles. Mutation sectorielle XLF positive : RS 20j +2.81%, momentum 5.19/10, rang 3e/11. Earnings J0 sans détails. Action : corriger ticker dans config/watchlist.json.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
