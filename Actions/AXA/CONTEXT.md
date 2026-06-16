# CONTEXT — AXA — Dernière mise à jour : 2026-06-16

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 17h du 16/06 — fichier réparé) :** Le fichier `data/sector_rotation_2026-06-16.json` est récupéré et exploitable à 17h. XLF (Financials) au rang **2e/11**, momentum **6.68/10**, RS 20j **+4.64%**, RS 60j **−2.76%**. C'est une **amélioration nette** vs le close du 15/06 (momentum +1.99 pt, RS 20j +1.94 pp, RS 60j +2.06 pp), qualitativement organique. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

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

- **[INFO]** Fichier sectoriel réparé à 17h : `data/sector_rotation_2026-06-16.json` exploitable — XLF rang 2e/11, momentum 6.68/10, RS 20j +4.64%, RS 60j −2.76%.

---

## 📅 Prochains événements

- **2026-06-16** · earnings · Earnings J0 FMP sans détails exploitables (18e jour consécutif)

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
- **Type :** _update.md
- **Fichier :** `AXA_2026-06-16_update_17h.md`
- **Conclusion :** Données AXA toujours KO (18e snapshot consécutif). Fichier sectoriel XLF réparé à 17h avec amélioration nette du momentum (+1.99 pt) et de la force relative (+1.94 pp à 20j, +2.06 pp à 60j). Thèse ATTENDRE confirmée, scoring stable 55.2/100. Action : corriger le symbole.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
