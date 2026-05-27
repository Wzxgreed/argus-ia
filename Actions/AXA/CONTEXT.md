# CONTEXT — AXA — Dernière mise à jour : 2026-05-27

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale est impossible.

**Contexte sectoriel (snapshot 13h00 UTC) :** Le secteur Financials (XLF) sous-performe le S&P 500 de −4.88% sur 20j et −8.38% sur 60j, avec un momentum score de 0.0/10. Le secteur affiche un return 20j de +0.08% et un return 60j de +1.33%. Les métriques sectorielles sont strictement identiques à celles du snapshot 10h00 UTC du 27/05 : aucune mutation technique sectorielle n'est survenue entre 10h00 et 13h00 UTC. Le secteur financier reste en phase de distribution relative vs le marché (SPY surperforme de +4.87pp sur 20j), sous le coup de la rotation sectorielle vers la Tech (XLK return 20j +15.3%, momentum 10.0/10). Le snapshot 13h00 UTC du 27/05 confirme que les données de prix US sont bien récupérées (AAPL 47.9M, NOK 188.9M, RKLB 32.8M), isolant AXA comme l'un des 3 tickers structurellement KO sur 26. Si les données AXA étaient disponibles, cette stabilité sectorielle laisserait le score Momentum inchangé.

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

- **2026-05-27** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-27
- **Type :** update
- **Fichier :** `AXA_2026-05-27_update.md`
- **Conclusion :** 17e snapshot consécutif sans mutation des données AXA. Stabilité totale sectorielle XLF. ATTENDRE.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
