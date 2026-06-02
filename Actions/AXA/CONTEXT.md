# CONTEXT — AXA — Dernière mise à jour : 2026-06-02

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 2026-06-02 10h00 UTC) :** Le secteur Financials (XLF) sous-performe le S&P 500 de −6.20% sur 20j et −10.73% sur 60j, avec un momentum score de 0.0/10. Le secteur affiche un return 20j de −0.94% et un return 60j de +0.91%. Ces chiffres sont **strictement inchangés** vs close 01/06. Le signal macro reste **`ROTATION_TO_CYCLICAL`**, porté par la domination de XLK (Technology, return 20j +20.94%, momentum 10.0/10) et le crossover haussier de XLE (Energy). XLF reste classé 3e/11 mais sans momentum propre (0.0/10), en distribution relative structurelle vs le marché. Le snapshot confirme que les données de prix US sont bien récupérées (25 tickers OK sur 29), isolant AXA comme l'un des 4 tickers structurellement KO sur 29. Si les données AXA étaient disponibles, le headwind sectoriel pourrait justifier un ajustement à la marge du score Momentum (actuellement placeholder 5.0/10).

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

- **2026-06-02** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-02
- **Type :** update
- **Fichier :** `AXA_2026-06-02_update.md`
- **Conclusion :** > **Date :** 2026-06-02

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
