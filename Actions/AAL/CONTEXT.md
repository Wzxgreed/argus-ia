# CONTEXT — AAL — Dernière mise à jour : 2026-06-16

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE (downgrade de ACHETER Sizing Réduit)
**Prix cible :** Suspendu — attente récupération données de cours
**Stop-loss :** Suspendu — niveaux précédents ($14.16 / $17.41) obsolètes sans ATR confirmé
**Upside/Downside :** Indisponible — cours NaN
**Derniere mise a jour :** 2026-06-16 (snapshot 10h UTC)

American Airlines est une compagnie aerienne legacy fortement endettee (~$40B) avec aucun moat. Hors perimetre qualite (0-1/6). Le rally du 20–27/05 a matérialise **+24.3%** ($12.06 → $14.99). Après un repli post-rally jusqu'a **$13.50 (05/06)** et une période d'incertitude data quality (10/06), le cours avait rebondi de **$13.60 à $15.46 (+13.7%)** en 5 sessions. Le support **$14.00** avait été confirmé comme récupéré (3 closes consécutifs au-dessus).

La session du 15/06 s'est ouverte à **$15.54** (gap haussier vs close $14.98), a atteint **$15.895** (rejet institutionnel), et clôturé à **$15.46 (+3.20%)** sur un volume record de **178.76M (+78.9% vs moyenne 20j)**.

Au snapshot 10h UTC du 16/06, les données de cours sont **toutes NaN** dans `data/latest.json`. Seul `previous_close` ($14.98) est disponible, impliquant un repli de **−3.1%** vs le close officiel du 15/06 ($15.46). Le RSI est en détente à **51.38** (−4.5 pts). L'ATR 14j et la MM50 sont passés à **null**. Le volume affiché (178.76M) est **identique à celui du 15/06** — probablement stale. Les données options sont **corrompues** (Max Pain $1.00 aberrant vs $10.00 hier, Put/Call et Call OI nulls).

L'agent recommandation a **downgradé** la thèse en **ATTENDRE** avec un Score Opportunité de **5.2/10** (C:5.3 V:4.5 M:6.0) et un Score Global ajusté de **51.5/100** (vs 64.0/100 au snapshot 21h du 15/06). Le timing est jugé **Neutre**. Le consensus FMP reste inchangé à **$16.60** (17 analystes). Le short interest est stable à **11.39%**. Le Forward P/E est à **6.94**.

**Verdict institutionnel :** La thèse est **ATTENDRE — SUSPENDUE.** L'absence de données de cours fiables, la corruption des données options, et la disparition de l'ATR/MM50 rendent tout positionnement irrationnel. Le repli implied de −3.1% et la baisse du RSI indiquent une consolidation technique post-rally. Si les données sont récupérées et que le cours tient au-dessus de $14.50, une réactivation de la thèse ACHETER (Sizing Réduit) est possible. Si le cours est confirmé sous $14.50 : passage à **SURVEILLER**. Le bilan reste extrêmement fragile (current ratio 0.50, tangible asset value négatif, net debt/EBITDA 8.83x). AAdvantage (programme loyalty) reste le hidden asset (~$20-25B > market cap).

**⚠️ Données partielles** — Cours NaN (open/high/low/close), ATR null, MM50 null, MM200 indisponible. Options corrompues (Max Pain $1.00 aberrant, Put/Call et Call OI nulls). Volume suspect (identique au 15/06). Sector rotation NaN généralisé. Accounting risk indisponible. Quant report insuffisant. Social sentiment sans données Reddit.

---

## Actualites ayant impacte ce dossier
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** invalide
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- **2026-05-17** · earnings · Miss / Imprécis · Ligne:  | 2026-05-17 | AAL | `_init.md` | SURVEILLER | $14.00

---

## 🚨 Alertes actives

- Baisse — $11.41 (SL 2×ATR) — 🟢 Active
- Hausse — $14.00 (prix cible) — 🔴 Déclenchée (27/05)
- Volume — >2× moy. 20j (>XXM) — 🟢 Active

---

## 📅 Prochains événements

- Aucun événement à venir.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 59.18
- **MM 50j :** 12.8
- **MM 200j :** —
- **ATR 14j :** 0.67
- **Volume moy. 20j :** 93542059

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-16
- **Type :** update
- **Fichier :** `AAL_2026-06-16_update.md`
- **Conclusion :** **Date :** 2026-06-16 (snapshot 10h UTC, pré-ouverture NY)

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap +5.92% overnight (seuil ±5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
