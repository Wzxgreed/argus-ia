# CONTEXT — AXA — Dernière mise à jour : 2026-06-08

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 2026-06-08 10h00 UTC) :** Le secteur Financials (XLF) affiche une **amélioration significative** vs le snapshot du 03/06 : return 20j **+1.45%** (vs SPY +0.82%), return 60j **+5.90%** (vs SPY +9.35%), RS 20j **+0.64%** (vs −6.02% le 03/06), RS 60j **−3.45%** (vs −10.99% le 03/06). Le momentum score a bondi à **4.0/10** (vs 0.0/10). Le signal macro `NEUTRAL` est inchangé. XLF reste classé 3e/11. Le snapshot confirme que les données de prix US sont bien récupérées (25 tickers OK sur 29), isolant AXA comme l'un des **4 tickers structurellement KO** sur 29 (SPCX résolu depuis le 03/06). Si les données AXA étaient disponibles, le contexte sectoriel aurait justifié un relèvement du placeholder Momentum.

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

- **2026-06-08** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-08
- **Type :** update
- **Fichier :** `AXA_2026-06-08_update.md`
- **Conclusion :** > **Date :** 2026-06-08

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
