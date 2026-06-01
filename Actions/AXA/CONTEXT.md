# CONTEXT — AXA — Dernière mise à jour : 2026-06-01

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 2026-06-01 UTC) :** Le secteur Financials (XLF) sous-performe le S&P 500 de −6.32% sur 20j et −10.05% sur 60j, avec un momentum score de 0.0/10. Le secteur affiche un return 20j de −1.06% et un return 60j de +0.67%. Le signal macro du jour est `ROTATION_TO_DEFENSIVE`, pénalisant les cycliques dont Financials. Le secteur financier reste en phase de distribution relative vs le marché (SPY surperforme de +6.32pp sur 20j), sous le coup de la rotation sectorielle vers la Tech (XLK return 20j +19.76%, momentum 10.0/10). Le snapshot confirme que les données de prix US sont bien récupérées (VRT 7.2M, IREN 50.2M, NOK 90.9M), isolant AXA comme l'un des 4 tickers structurellement KO sur 28. Si les données AXA étaient disponibles, le creusement du RS 60j à −10.05% pourrait justifier un ajustement à la marge du score Momentum (actuellement placeholder 5.0/10).

**Action immédiate :** corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`), mettre à jour le secteur (Financials / Insurance) et relancer le fetch.

---

## 📜 Historique des analyses
- **Score global :** 55.2/100
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** ATTENDRE
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **[CRITICAL]** Pas de données de prix pour AXA — ticker probablement incorrect
- **[WARNING]** Earnings J0 (2026-06-01) sans consensus ni résultats exploitables — 6e jour consécutif
- **[INFO]** Headwind sectoriel XLF persistant : RS 20j −6.32%, RS 60j −10.05%, return 20j −1.06%, return 60j +0.67%, momentum 0.0/10

---

## 📅 Prochains événements

- **2026-06-01** · earnings · Earnings J0 FMP sans détails exploitables

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-01
- **Type :** update
- **Fichier :** `AXA_2026-06-01_update.md`
- **Conclusion :** 19e snapshot consécutif sans mutation des données AXA. Thèse ATTENDRE confirmée. Données structurellement manquantes. Earnings J0 glissant sans détails. Headwind sectoriel XLF stable à 20j mais creusé à 60j. Action immédiate : corriger le symbole (`CS.PA` ou `AXAHY`) et relancer le fetch.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
