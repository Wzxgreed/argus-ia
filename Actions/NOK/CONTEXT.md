# CONTEXT — NOK — Dernière mise à jour : 2026-06-17

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER — Pas de position
**Prix cible :** $10.8 (consensus 7 analystes FMP)
**Stop-loss :** $11.80 (basé sur cours $13.98 et ATR $1.09 du snapshot actuel)
**Take-profit :** $17.25 (basé sur cours $13.98 et ATR $1.09 du snapshot actuel)
**Upside/Downside :** −22.7% / −15.6% (basés sur cours $13.98)
**Dernière mise à jour :** 2026-06-17 10:00 UTC

Snapshot 10h UTC : close **$13.98** (rebond +0.90% vs close 21h 16/06, gap baissier −5.67% vs previous close). RSI **40.53**, volume **123.7M** (0.98× moyenne 20j), ATR **$1.09**, MM50 **$12.99**. **Données options corrompues** dans `latest.json` — valeurs opérationnelles conservées : max pain **$14.00**, put/call **0.47**, call OI **68.1%**, expiration **2026-06-18** (**demain**). Cours quasi-aligné sur le max pain (−0.14%). Consensus FMP **$10.8** (7 analysts). Premium consensus **+28.7%**. Quality hors périmètre (2.5/6). Divergence Yahoo/FMP persistante. XLC bottom 3 (momentum score 0.0). `recommandations_2026-06-17.json` : scoring NOK indisponible — scores du 16/06 reportés (**44.2/100 — SURVEILLER**, C:4.0 V:3.5 M:4.5). Volume normalisé à la moyenne (0.98×) — invalidation du signal de désengagement du snapshot 21h. Pas de position.

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $10.8
- **Stop-loss :** $11.80
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- **2026-05-17** · earnings · Miss / Imprécis · Ligne:  | 2026-05-17 | NOK | `_init.md` | SURVEILLER | $9.26

---

## 🚨 Alertes actives

- Baisse — $11.80 (SL 2×ATR) — 🟢 Active
- Hausse — $10.8 (consensus) — 🔴 Déjà au-dessus
- Volume — >2× moy. 20j (>252M) — 🟢 Active

---

## 📅 Prochains événements

- 2026-07-23 · Earnings Q2 FY2026 (dans 36 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 40.53
- **MM 50j :** 12.99
- **MM 200j :** —
- **ATR 14j :** 1.09
- **Volume moy. 20j :** 126263065

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-17
- **Type :** update
- **Fichier :** `NOK_2026-06-17_update.md`
- **Conclusion :** Thèse SURVEILLER confirmée. Léger rebond technique (+0.90%) avec volume normalisé (0.98×) et RSI remonté à 40.53. Gap baissier −5.67% vs previous close persistant. Options corrompues, valeurs opérationnelles conservées. Expiration demain. Pas de position.

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap −5.67% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 7.80% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
