# CONTEXT — NOK — Dernière mise à jour : 2026-05-26

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — Pas de position
- **Prix cible :** $9.26 (consensus 6 analystes)
- **Stop-loss :** $14.52 (cours − 2×ATR)
- **Take-profit :** $19.52 (cours + 3×ATR)
- **Upside/Downside :** −43.9% / −12.1%
- **Dernière mise à jour :** 2026-05-26 17:00 UTC

Double gap haussier consécutif : +9.1% (25/05) puis +6.79% (26/05), soit +18.3% en deux séances sans catalyseur fondamental identifiable. Cours $16.52, nouveau 52-week high $16.625, RSI 67.38 proche surachat. P/E Yahoo 103.3, premium consensus +78.4%. Options : max pain $15.00 (expiration 29/05, dans 2j), put/call 0.51, call OI 66.1%. Risque de mean-reversion vers le max pain élevé. Quality hors périmètre (2.5/6). Secteur XLC bottom 3. Pas d'entrée.

**✅ Données complètes** — Cours, RSI, ATR, P/E, consensus, options disponibles dans `data/latest.json`.

---

## Actualités ayant impacté ce dossier
- **Score global :** 50.5/100
- **Prix cible :** $9.26
- **Stop-loss :** $14.52
- **Statut thèse :** modifiée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Baisse — $14.52 (SL 2×ATR) — 🟢 Active
- Hausse — $9.26 (consensus) — 🔴 Déjà au-dessus (+78.4%)
- Volume — >2× moy. 20j (>237M) — 🟢 Active

---

## 📅 Prochains événements

- 2026-05-29 — Expiration options (max pain $15.00, dans 2 jours)
- 2026-07-23 — Earnings Q2 FY2026 (dans 58 jours)

---

## 📊 Contexte technique (dernier snapshot)

- **Cours close :** $16.52
- **RSI 14j :** 67.38
- **MM 50j :** $10.96
- **MM 200j :** —
- **ATR 14j :** $1.00
- **Volume moy. 20j :** 118,756,294
- **Volume relatif :** 1.17×
- **52-week high :** $16.625
- **52-week low :** $4.00

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-26
- **Type :** update
- **Fichier :** `NOK_2026-05-26_update.md`
- **Conclusion :** Deuxième gap consécutif (+6.79%, close $16.52). New 52w high $16.625. RSI 67.38. P/E 103.3, premium consensus +78.4%. Aucun catalyseur identifié. Thèse modifiée : ATTENDRE maintenu, SL/TP révisés $14.52/$19.52. Risque mean-reversion élevé vers max pain $15.00 (expiration 29/05).

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (high) — Deuxième gap consécutif : +6.79% overnight (seuil ±5.0%)
- **RSI_OVERBOUGHT** (medium) — RSI 67.38 approche zone surachat (>70)
- **ATR_SPIKE** (medium) — ATR relatif 6.05% (seuil 5.0%)
- **VOLUME_SPIKE** (medium) — Volume 1.17× moy. 20j (seuil 1.0×)
- **MAX_PAIN_DIVERGENCE** (high) — Cours $16.52 vs max pain $15.00 : écart +10.1%, expiration dans 2 jours

---

*Généré automatiquement — ne pas éditer manuellement.*
