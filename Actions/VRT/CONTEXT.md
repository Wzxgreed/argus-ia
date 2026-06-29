# CONTEXT — VRT — Dernière mise à jour : 2026-06-29

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ÉVITER (data blackout, cassure MM50 confirmée, score historique bas 20.8/100)
- **Prix cible :** $340–$360 (technique, consensus $267.57) — **non actif**
- **Upside/Downside :** +12.0% / −14.3% (SL engine) / −4.6% (desk SL $290)
- **Dernière mise à jour :** 2026-06-29 (Data blackout — dernier close connu **$303.95** [STALE, 28/06], −6.54% vs 23/06, −15.1% cumulé depuis 22/06, RSI **50.9**, volume **21.97M (3.0×)** [distribution, 26/06], ATR **$21.71** [ATR_SPIKE 7.14%], MM50 **$324.04** [**−6.20% sous MM50, cassure confirmée**], options **put/call 1.74** [bearish atténué, max pain $235], sector rotation XLI **Données manquantes** [BLACKOUT], FX exposure **45% EUR/CNY** [Score FX Impact 0.0, 🟢], social sentiment **0 mentions**, consensus PT **$267.57** [47 analysts, +13.6% sous cours], Score Global Ajusté **20.8/100** [ÉVITER, plus bas historique] — thèse **INVALIDÉE**, downgrade SURVEILLER → ÉVITER)

Vertiv est le leader mondial du refroidissement data centers, bénéficiant directement de l'explosion de l'IA. Quality Compounder 6/6 avec marges en expansion, ROIC 18.5%, ROCE 24.3%, net debt/EBITDA 0.78×. La configuration technique s'est structurellement dégradée entre le 23/06 et le 26/06 : **gap down cumulé de −15.1%** depuis le high du 22/06, **cassure de la MM50** ($324.04) sur **volume explosion 3.0×** = distribution institutionnelle confirmée. Le `quality_gate_2026-06-29.json` signale un **data blackout** (`stale_price_history` — close identique sur 3 jours). Aucune news, aucun événement corporate, aucun social sentiment détecté. Le Score Global Ajusté à **20.8/100** est le plus bas historique. Timing Défavorable. Aucune position longue recommandée. Si clôture au-dessus de MM50 ($324.04) avec volume >1.2× + catalyseur externe → upgrade conditionnel vers SURVEILLER. Si perte de $300 avec volume >1.0× → support $280–$290 exposé. Prochain earnings 2026-07-29 (30 jours).

---

## Actualités ayant impacté ce dossier
- **Score global :** 20.8/10
- **Prix cible :** $340
- **Stop-loss :** $290.00
- **Statut thèse :** invalidée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- **2026-05-17** · earnings · Miss / Imprécis · Ligne:  | 2026-05-17 | VRT | `_init.md` | SURVEILLER | $400.00
- **2026-06-22** · timing · Miss — rally +19.5% suivi de gap down −9.14% (23/06) puis −6.64% (26/06), invalidant l'upgrade ATTENDRE

---

## 🚨 Alertes actives

- Baisse — $335.22 — 🟢 Active
- Hausse — $400.00 — 🟢 Active
- Volume — >2× moy. 20j (>11.5M) — 🔴 **DÉCLENCHÉE** (21.97M le 26/06)

---

## 📅 Prochains événements

- **2026-07-29** · earnings · Earnings date — Est EPS $1.38-$1.59, Rev $3.4B (30 jours)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 50.9
- **MM 50j :** 324.04
- **MM 200j :** —
- **ATR 14j :** 21.71
- **Volume moy. 20j :** 7214525

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-29
- **Type :** update
- **Fichier :** `VRT_2026-06-29_update.md`
- **Conclusion :** Thèse INVALIDÉE — data blackout, cassure MM50 confirmée, score historique bas 20.8/100 ÉVITER

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap -6.64% overnight (seuil ±5.0%) [STALE, 26/06]
- **VOLUME_SURGE** (medium) — Volume 3.0× moyenne 20j (21,974,500 vs 7,214,525) [STALE, 26/06]
- **ATR_SPIKE** (medium) — ATR relatif 7.14% (seuil 5.0%) [STALE, 26/06]
- **Note :** Triggers du 29/06 identiques au 28/06 — artefact algorithmique (stale_price_history confirmée par quality_gate)

---

*Généré automatiquement — ne pas éditer manuellement.*
