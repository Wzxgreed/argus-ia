# CONTEXT — AXA — Dernière mise à jour : 2026-06-16

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (dernier snapshot fiable : 2026-06-15 21h00 UTC) :** Le secteur Financials (XLF) affichait une **mutation mécanique** entre 17h et 21h du 15/06. Le fichier `data/sector_rotation_2026-06-15.json` réécrit à 21h plaçait XLF au rang **2e/11** (vs 3e/11 à 17h), mais avec un momentum score de **4.69/10** (vs 5.12/10 à 17h), RS 20j **+2.70%** (vs +3.13% à 17h) et RS 60j **−4.82%** (vs −4.38% à 17h). Le retour au rang 2e était mécanique (dégradation relative d'autres secteurs), pas organique. Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

**Anomalie JSON sectorielle récurrente (16/06) :** Le fichier `data/sector_rotation_2026-06-16.json` présente la même anomalie technique que le 10/06 (NaN + momentum 10.0 uniforme pour tous les secteurs) et est classé inexploitable. Le dernier contexte sectoriel fiable reste le snapshot 21h du 15/06.

**Action immédiate :** corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`), mettre à jour le secteur (Financials / Insurance) et relancer le fetch.

---

## 📜 Historique des analyses
- **Score global :** 55.2/100
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** invalide (données manquantes)
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- **[CRITICAL]** Pas de données de prix pour AXA — ticker probablement incorrect
- **[WARNING]** Earnings J0 (2026-06-16) sans consensus ni résultats exploitables — pattern persistant depuis mi-mai (16e occurrence consécutive)
- **[INFO]** **Anomalie JSON sectorielle récurrente** dans `data/sector_rotation_2026-06-16.json` (NaN + momentum 10.0 uniforme pour tous les secteurs) — fichier classé inexploitable, déjà observé le 10/06. Dernier contexte sectoriel fiable : 15/06 21h (XLF rang 2e/11 mécanique, momentum 4.69/10, RS 20j +2.70%, RS 60j −4.82%) ; signal macro `UNKNOWN` stable

---

## 📅 Prochains événements

- **2026-06-16** · earnings · Earnings J0 FMP glissant sans détails exploitables

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
- **Type :** update
- **Fichier :** `AXA_2026-06-16_update.md`
- **Conclusion :** 🟡 Thèse ATTENDRE confirmée (55.2/100). Données AXA toujours manquantes (No price history — 16e snapshot consécutif). Anomalie JSON sectorielle récurrente détectée (NaN + momentum 10.0 uniforme) — fichier 16/06 classé inexploitable. Dernier contexte sectoriel fiable : 15/06 21h (XLF rang 2e/11 mécanique, momentum 4.69/10). Earnings J0 glissant reculé d'un jour (16/06) sans résolution. Action : corriger symbole (`CS.PA` ou `AXAHY`) et relancer fetch.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
