# CONTEXT — AXA — Dernière mise à jour : 2026-05-26 (snapshot 17h00 UTC)

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale est impossible.

**Contexte sectoriel (snapshot 17h00 UTC) :** Le secteur Financials (XLF) sous-performe le S&P 500 de −4.74% sur 20j et −8.24% sur 60j, avec un momentum score de 0.0/10. Le secteur affiche un return 20j de 0.00% et un return 60j de +1.26%. Les métriques sectorielles ont muté entre 13h00 et 17h00 UTC : dégradation du RS 20j (−3.43% → −4.74%) et amélioration du RS 60j (−9.03% → −8.24%). Le secteur financier reste en phase de distribution relative vs le marché (SPY surperforme de +4.74pp sur 20j), sous le coup de la rotation sectorielle vers la Tech (XLK return 20j +14.93%, momentum 10.0/10). La session US est ouverte et liquide (volumes élevés sur AAPL 20.5M, NOK 138.9M) mais cela n'a pas permis la récupération de données pour AXA. Si les données AXA étaient disponibles, cette dégradation relative courte terme peserait légèrement sur le score Momentum et le timing d'entrée.

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

- **2026-05-26** · earnings · Earnings ...

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
- **Conclusion :** Données manquantes persistantes — 14e snapshot consécutif sans mutation ; mutation sectorielle XLF détectée entre 13h00 et 17h00 (RS 20j −3.43% → −4.74%) ; thèse ATTENDRE confirmée

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
