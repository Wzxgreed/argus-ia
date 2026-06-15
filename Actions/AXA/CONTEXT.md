# CONTEXT — AXA — Dernière mise à jour : 2026-06-15

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (dernier snapshot fiable : 2026-06-09 21h00 UTC) :** Le secteur Financials (XLF) affichait une **amélioration significative** vs le snapshot 13h du 09/06 : return 20j **+2.50%** (+1.08 pp), return 60j **+7.85%** (+0.87 pp), RS 20j **+2.81%** (+1.60 pp), RS 60j **−3.74%** (+0.57 pp), momentum score **5.19/10** (+1.19 pt). Le rang sectoriel était au **3e/11** (+1 place). Le signal macro `NEUTRAL` était inchangé. **Attention :** le fichier `data/sector_rotation_2026-06-10.json` est corrompu (NaN + momentum 10.0 uniforme pour tous les secteurs) et ne peut pas être utilisé pour évaluer la rotation du jour.

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
- **Type :** preview
- **Fichier :** `AXA_2026-06-15_preview.md`
- **Conclusion :** > **Date :** 2026-06-15

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
