# CONTEXT — AXA — Dernière mise à jour : 2026-06-15 (snapshot 17h00 UTC)

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (dernier snapshot fiable : 2026-06-15 17h00 UTC) :** Le secteur Financials (XLF) affiche une **divergence** entre le snapshot 10h et le JSON 17h : rang **3e/11** (vs 2e/11 à 10h), momentum score **5.12/10** (vs 6.73/10 à 10h), RS 20j **+3.13%** (vs +4.85% à 10h), RS 60j **−4.38%** (vs −2.97% à 10h). Le signal macro reste `UNKNOWN` (stable depuis le 02/06). Cette divergence modère l'interprétation du vent de queue sectoriel sans invalider la thèse.

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

- **2026-06-15** · earnings · Earnings ...

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
- **Fichier :** `AXA_2026-06-15_update_17h.md`
- **Conclusion :** Thèse ATTENDRE confirmée — données AXA toujours manquantes (4 tickers KO sur 29). Divergence sectorielle XLF détectée entre snapshot 10h et JSON 17h (rang 3e/11 vs 2e/11, momentum 5.12 vs 6.73, RS 20j +3.13% vs +4.85%). Signal macro `UNKNOWN` stable. Earnings J0 FMP glissant sans détails — 14e jour consécutif.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
