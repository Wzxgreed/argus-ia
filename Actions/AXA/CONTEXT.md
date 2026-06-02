# CONTEXT — AXA — Dernière mise à jour : 2026-06-02

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 2026-06-02 17h00 UTC) :** Le secteur Financials (XLF) affiche une **amélioration absolue marquée** par rapport au snapshot 13h00 : return 20j −0.17% (vs −0.94%) et return 60j +2.34% (vs +0.91%). Cependant, cette amélioration est portée par le rebond du broad market (SPY +5.81% sur 20j, +13.30% sur 60j) et non par une dynamique propre du secteur — le momentum score reste à 0.0/10. En termes relatifs, le RS 60j vs SPY se dégrade légèrement (−10.96% vs −10.73% à 13h00), confirmant la sous-performance structurelle. Le signal macro a été **neutralisé** (`ROTATION_TO_CYCLICAL` → `NEUTRAL`), indiquant un affaiblissement de la rotation sectorielle observée depuis le 1er juin. XLF reste classé 3e/11, en distribution relative vs le marché. Le snapshot confirme que les données de prix US sont bien récupérées (24 tickers OK sur 29), isolant AXA comme l'un des 4 tickers structurellement KO sur 29. Si les données AXA étaient disponibles, le headwind sectoriel persistant justifierait un ajustement à la baisse du placeholder Momentum (actuellement 5.0/10).

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
