# CONTEXT — AXA — Dernière mise à jour : 2026-06-29

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 10h du 29/06) :** Le fichier `data/sector_rotation_2026-06-29.json` est valide (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **4e/11** (vs 3e/11), momentum **8.40/10** (vs 6.23/10 à 17h du 23/06), RS 20j **+8.00%** (vs +4.96%), RS 60j **−3.50%** (vs −4.36%), return 20j **+4.85%** (vs +4.10%), return 60j **+8.89%**. **Mutation positive nette** : toutes les métriques sectorielles ont progressé. L'amélioration est organique et signale une accélération de la rotation vers les Financials. Le rang 4e (vs 3e) est une descente mécanique (XLK et XLV plus forts), pas organique. Le secteur Financials constitue un vent arrière théorique **fortement renforcé** pour un assureur. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

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

- **[CRITICAL]** Pas de données de prix pour AXA — ticker probablement incorrect (30e snapshot consécutif)
- **[WARNING]** Earnings J0 (2026-06-29) sans consensus ni résultats exploitables — pattern persistant depuis mi-mai (30e occurrence consécutive)
- **[INFO]** **Fichier sectoriel exploitable** : `data/sector_rotation_2026-06-29.json` valide — XLF rang 4e/11 (momentum 8.40/10, RS 20j +8.00%, RS 60j −3.50%, return 20j +4.85%, return 60j +8.89%). **Mutation positive nette** détectée vs 23/06, portée par le momentum et le RS 20j. Vent arrière théorique **fortement renforcé** pour un assureur. Signal macro `UNKNOWN` stable

---

## 📅 Prochains événements

- **2026-06-29** · earnings · Earnings J0 FMP (sans détails exploitables)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** —

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-29
- **Type :** update
- **Fichier :** `AXA_2026-06-29_update.md`
- **Conclusion :** Thèse inchangée ATTENDRE (55.2/100). Données AXA toujours manquantes (30e snapshot). Vent arrière sectoriel XLF fortement renforcé (momentum 8.40/10, RS 20j +8.00%). Earnings J0 FMP sans détails exploitables. Action prioritaire : corriger le symbole ticker.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
