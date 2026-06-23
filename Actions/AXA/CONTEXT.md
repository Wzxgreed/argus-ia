# CONTEXT — AXA — Dernière mise à jour : 2026-06-23

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 17h du 23/06 — fichier exploitable) :** Le fichier `data/sector_rotation_2026-06-23.json` est valide ce soir (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **3e/11** (stable), momentum **6.23/10** (vs 5.45/10 à 13h), RS 20j **+4.96%** (vs +3.69%), RS 60j **−4.36%** (vs −4.41%), return 20j **+4.10%** (vs +4.17%). **Mutation positive nette** entre 13h et 17h : momentum +0.78 pt, RS 20j +1.27 pp, RS 60j +0.05 pp. L'amélioration est concentrée sur le momentum et le RS 20j, signalant une accélération de la rotation vers les Financials en fin de séance. Le secteur Financials confirme sa place dans le top 3 avec une dynamique **nettement plus positive**, ce qui constitue un vent arrière théorique **renforcé** pour un assureur. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

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

- **2026-06-23** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-23
- **Type :** init
- **Fichier :** `AXA_2026-06-23_update_13h.md`
- **Conclusion :** > **Date :** 2026-06-23

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
