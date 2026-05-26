# CONTEXT — AXA — Dernière mise à jour : 2026-05-26

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale est impossible.

**Contexte sectoriel (snapshot 10h00 UTC) :** Le secteur Financials (XLF) sous-performe le S&P 500 de −3.43% sur 20j et −9.03% sur 60j, avec un momentum score de 0.0/10. Le secteur affiche un return 20j de +1.01% et un return 60j de −0.56%. Les métriques sectorielles sont stables vs le snapshot 21h00 UTC du 2026-05-25. Le secteur financier reste en phase de distribution relative vs le marché (SPY surperforme de +3.4pp sur 20j). Si les données AXA étaient disponibles, ce headwind sectoriel atténué pèserait encore sur le score Momentum et le timing d'entrée.

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
- **[WARNING]** Earnings J0 (2026-05-26) sans consensus ni résultats exploitables
- **[INFO]** Headwind sectoriel XLF atténué mais persistant (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10)

---

## 📅 Prochains événements

- **2026-05-26** · earnings · Earnings (J0, sans détails exploitables)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-26
- **Type :** update
- **Fichier :** `AXA_2026-05-26_update.md`
- **Conclusion :** 12e snapshot consécutif sans mutation des données AXA. Thèse non évaluable. Recommandation ATTENDRE confirmée. Marché rouvert post-Memorial Day sans résolution du blocage de sourcing.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
