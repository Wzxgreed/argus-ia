# CONTEXT — SOFI — Dernière mise à jour : 2026-06-08

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER
- **Prix cible :** $19.00 (cours + 3×ATR)
- **Stop-loss :** $14.05 (cours − 2×ATR)
- **Upside/Downside :** +18.5% / −12.4%
- **Dernière mise à jour :** 2026-06-08 (gap −6.53% invalidant breakout MM50, reclassement ACHETER → SURVEILLER)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le snapshot du **2026-06-08** enregistre un **gap baissier de −6.53%** à **$16.03** sur un volume de **81.21M (1.15× moy. 20j)**, invalidant le breakout au-dessus de la MM50 du 01/06. Le RSI est retombé à **52.78** (−11.1 pts), l'ATR a gonflé à **$0.99** (+8.8%) et le cours est repassé **sous la MM50 à $16.75** (−0.43%). La thèse haussière du début juin est **invalidée**.

Le Forward P/E **20.54** s'améliore mécaniquement mais ne compense pas le momentum perdu. Le Score Opportunité est tombé à **5.8/10** et le Score Global ajusté à **49.8/100** (zone SURVEILLER). Le secteur financier (XLF) reste faible (momentum 4.0/10). Le short interest à **13.68%** laisse un potentiel de squeeze si un rebond technique se matérialise, mais le setup n'est pas actif sous MM50.

**Données options corrompues** dans `data/latest.json` du 08/06 (Max Pain $5.00 aberrant, Put/Call et Call OI null) — impossible d'évaluer le sentiment options. Dernières valeurs cohérentes : Max Pain **$20.00** (03/06).

**Conditions pour réactiver la thèse ACHETER :**
1. Reclaim MM50 $16.75 en close avec volume >1.0×
2. Rebond vif sur $15.68 (low du 05/06) avec RSI >55 et volume acheteur >1.2×
3. Catalyseur fondamental positif (guidance, contrat, M&A)

**Score 5.8/10. Score Global ajusté 49.8/100. SURVEILLER — Aucune entrée recommandée.**

**Données complètes** — Cours $16.03, RSI 52.78, ATR $0.99, MM50 $16.75, Forward P/E 20.54 dans `data/latest.json` (snapshot 2026-06-08T10:00 UTC). Options : données corrompues.

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $20.47
- **Stop-loss :** $15.92
- **Statut thèse :** invalide
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Baisse — $13.97 (SL 2×ATR) — 🟢 Active
- Hausse — $19.51 (prix cible) — 🟢 Active
- Volume — >2× moy. 20j (>XXM) — 🟢 Active

---

## 📅 Prochains événements

- Aucun événement à venir.

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
- **Type :** full refresh
- **Fichier :** `SOFI_2026-06-08_DRAFT_refresh.md`
- **Conclusion :** > **Date :** 2026-06-08

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap -6.53% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 6.18% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
