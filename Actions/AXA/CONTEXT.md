# CONTEXT — AXA — Dernière mise à jour : 2026-06-22

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 13h du 17/06 — fichier exploitable) :** Le fichier `data/sector_rotation_2026-06-17.json` est valide ce matin et strictement inchangé entre 10h et 13h (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **4e/11**, momentum **5.32/10**, RS 20j **+3.46%**, RS 60j **−4.38%**. C'est une **légère dégradation** vs le close du 16/06 (momentum −1.36 pt, RS 20j −1.18 pp, RS 60j −1.62 pp) mais **stabilité totale mécanique** en séance. XLF reste hors du top 3 (XLK, XLB, XLI). Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

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

- **2026-06-22** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-22
- **Type :** preview
- **Fichier :** `AXA_2026-06-22_preview.md`
- **Conclusion :** > **Date :** 2026-06-22

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
