# CONTEXT — AXA — Dernière mise à jour : 2026-06-23

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 13h du 23/06 — fichier exploitable) :** Le fichier `data/sector_rotation_2026-06-23.json` est valide cet après-midi (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **3e/11** (stable vs 10h), momentum **5.45/10** (stable), RS 20j **+3.69%** (stable), RS 60j **−4.41%** (stable), return 20j **+4.17%** (stable). **Stabilité mécanique totale** inter-snapshot — aucune mutation détectée entre 10h et 13h. Le secteur Financials confirme sa place dans le top 3 avec une dynamique positive, ce qui constitue un vent arrière théorique marginalement positif pour un assureur. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

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
- **Type :** update
- **Fichier :** `AXA_2026-06-23_update_13h.md`
- **Conclusion :** Thèse ATTENDRE confirmée — stabilité totale inter-snapshot, aucune mutation détectée entre 10h et 13h UTC.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
