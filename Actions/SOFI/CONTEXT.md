# CONTEXT — SOFI — Dernière mise à jour : 2026-06-08

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER
**Prix cible :** $19.00 (cours + 3×ATR)
**Stop-loss :** $14.05 (cours − 2×ATR)
**Upside/Downside :** +18.5% / −12.4%
**Dernière mise à jour :** 2026-06-08 (snapshot 13:00 UTC — close du 05/06 confirmé, anomalie options JSON corrigée)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le snapshot du **2026-06-08 13h UTC** reprend le close du 05/06 à **$16.03** (gap baissier −6.53%), RSI **52.78**, ATR **$0.99**, MM50 **$16.75** (−0.43%). Le volume de **81.21M (1.15× moy. 20j)** confirme la distribution institutionnelle active. **[RÉSOLU]** L'anomalie options JSON du snapshot 10h UTC (Max Pain $5.00 aberrant, Put/Call et Call OI `null`) est corrigée : Max Pain **$17.00**, Put/Call **0.57**, Call OI **63.7%** — repositionnement options modérément haussier mais s'affaiblissant vs le 01/06. Le support immédiat est le low du 05/06 à **$15.68**, suivi de **$15.00** (psychologique) et **$14.05** (SL 2×ATR). La résistance immédiate est la MM50 à **$16.75**, puis **$17.46** (low du 02/06) et **$17.00** (Max Pain). La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro majeurs. Le Forward P/E **20.54** est mécaniquement attractif. Le Score Opportunité est révisé à **5.8/10**, et le Score Global ajusté est en zone **SURVEILLER (49.8/100)** — reclassement depuis ACHETER (65.8) suite à l'invalidation du breakout MM50 du 01/06. Le short interest à **13.68%** laisse un potentiel de squeeze si un rebond technique se matérialise. Le secteur financier (XLF) est dans le top3 sectoriel mais avec un momentum faible (4.0/10) — classement relatif par exclusion, pas force absolue. Earnings Q2 dans **50j** (28 juillet, estimates EPS $0.10–$0.11, Rev $1.1B). ⚠️ Cours sous MM50 + RSI en zone neutre + momentum baissier (4.0/10) = timing défavorable. Aucune entrée recommandée. Attendre reclaim MM50 $16.75 avec volume >1.0× ou rebond vif sur $15.68 avec RSI >55 pour réactiver la thèse haussière.
**Score 5.8/10. Score Global 57.8/100 (ajusté 49.8). SURVEILLER — Aucune entrée.**

**Données complètes** — Cours, RSI, ATR, P/E, beta disponibles dans `data/latest.json` (snapshot 2026-06-08T13:00:08+00:00). Options corrigées : Max Pain $17.00, Put/Call 0.57, Call OI 63.7%. Expiration prochaine 2026-06-12 (4 jours ouvrés).

---

## Actualités ayant impacté ce dossier
- **Score global :** 49.8/100
- **Prix cible :** $19.00
- **Stop-loss :** $14.05
- **Statut thèse :** invalidée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Baisse — $13.97 (SL historique) — 🟢 Active (obsolète, nouveau SL $14.05)
- Hausse — $19.51 (prix cible historique) — 🟢 Active (obsolète, nouveau TP $19.00)
- Volume — >2× moy. 20j (>XXM) — 🟢 Active

---

## 📅 Prochains événements

- Earnings Q2 : 2026-07-28 (50j) — Est EPS $0.10–$0.11, Rev $1.1B

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 52.78
- **MM 50j :** 16.75
- **MM 200j :** —
- **ATR 14j :** 0.99
- **Volume moy. 20j :** 70441210

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-08
- **Type :** update
- **Fichier :** `SOFI_2026-06-08_update.md`
- **Conclusion :** Snapshot 13:00 UTC — close du 05/06 $16.03 (gap −6.53%) confirmé. Anomalie options JSON corrigée (Max Pain $17.00, Put/Call 0.57, Call OI 63.7%). Thèse invalidée — breakout MM50 du 01/06 rompu. Reclassement ACHETER → SURVEILLER confirmé. Score Global ajusté 49.8/100. SL $14.05, TP $19.00.

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap -6.53% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 6.18% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
