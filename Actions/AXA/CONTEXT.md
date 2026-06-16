# CONTEXT — AXA — Dernière mise à jour : 2026-06-16

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (dernier snapshot fiable : 2026-06-15 21h00 UTC) :** Le secteur Financials (XLF) affiche une **mutation mécanique** entre 17h et 21h. Le fichier `data/sector_rotation_2026-06-15.json` réécrit à 21h place XLF au rang **2e/11** (vs 3e/11 à 17h), mais avec un momentum score de **4.69/10** (vs 5.12/10 à 17h), RS 20j **+2.70%** (vs +3.13% à 17h) et RS 60j **−4.82%** (vs −4.38% à 17h). Le retour au rang 2e est mécanique (dégradation relative d'autres secteurs), pas organique. Le signal macro reste `UNKNOWN` (stable depuis le 02/06). Cette divergence modère l'interprétation du vent de queue sectoriel sans invalider la thèse.

**Action immédiate :** corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`), mettre à jour le secteur (Financials / Insurance) et relancer le fetch.

---

## 📜 Historique des analyses
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** invalide
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Aucune alerte active.

---

## 📅 Prochains événements

- **2026-06-16** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-16
- **Type :** preview
- **Fichier :** `AXA_2026-06-16_preview.md`
- **Conclusion :** > **Date :** 2026-06-16

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
