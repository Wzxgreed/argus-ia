# CONTEXT — AXA — Dernière mise à jour : 2026-05-28

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale est impossible.

**Contexte sectoriel (snapshot 17h00 UTC) :** Le secteur Financials (XLF) sous-performe le S&P 500 de −6.33% sur 20j et −8.93% sur 60j, avec un momentum score de 0.0/10. Le secteur affiche un return 20j de −0.96% et un return 60j de +0.61%. Après une stabilité totale entre 10h00 et 13h00 UTC, une mutation sectorielle a été détectée entre 13h00 et 17h00 UTC : le return 20j est repassé en territoire négatif (−0.96% vs +0.08% à 13h00) et le RS 20j vs SPY s'est creusé de −4.88% à −6.33%. C'est la première mutation sectorielle observée depuis le snapshot 17h00 UTC du 26/05. Le secteur financier reste en phase de distribution relative vs le marché (SPY surperforme de +6.32pp sur 20j), sous le coup de la rotation sectorielle vers la Tech (XLK return 20j +16.45%, momentum 10.0/10). Le snapshot 17h00 UTC confirme que les données de prix US sont bien récupérées (VRT 3.1M, IREN 46.0M, NOK 90.9M), isolant AXA comme l'un des 3 tickers structurellement KO sur 26. Si les données AXA étaient disponibles, cette dégradation sectorielle pourrait justifier un ajustement à la marge du score Momentum.

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

- **2026-05-28** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-28
- **Type :** preview
- **Fichier :** `AXA_2026-05-28_preview.md`
- **Conclusion :** > **Date :** 2026-05-28

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
