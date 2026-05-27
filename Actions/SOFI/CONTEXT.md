# CONTEXT — SOFI — Dernière mise à jour : 2026-05-27

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — Pas de position
**Prix cible :** $18.11 (cours + 3×ATR)
**Stop-loss :** $14.56 (cours − 2×ATR)
**Upside/Downside :** +13.3% / −8.9%
**Dernière mise à jour :** 2026-05-27 (snapshot 10:00 UTC — pré-marché, stabilité totale confirmée, anomalie options JSON signalée)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le charter bancaire 2022 crée une barrière réglementaire modérée vs les fintechs non-banques. Le snapshot du 2026-05-27 à 10:00 UTC (pré-marché) confirme la **stabilité totale** vs le close final 2026-05-26 21:00 UTC : cours **$15.98**, RSI 14j **49.59** (zone neutre médiane), ATR 14j **$0.71**, MM50 **$16.73**. Le volume est légèrement révisé à **80.29M (1.14× moy. 20j)** (+1.2% vs 79.35M) — correction mécanique post-close sans signification technique. Le cours reste sous la MM50 **$16.73** (−4.5% sous la moyenne). Le support psychologique **$15.00** est intact (52W low $12.86). La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro majeurs. Le Forward P/E **20.60** est raisonnable pour une fintech en croissance mais le P/E LTM **35.51** reste élevé. Le Score Opportunité est stable à **6.1/10**, et le Score Global Composite reste en zone **ATTENDRE (53.1/100)** (bord inférieur). **[ALERTE DATA QUALITY]** Le snapshot 2026-05-27 présente une anomalie systémique sur les options SOFI dans `data/latest.json` (Max Pain $5.00 aberrant, Put/Call `null`, Call OI `null`). Les valeurs confirmées du 2026-05-26 sont maintenues : Max Pain **$16.00** (parité avec cours $15.98), Put/Call **0.70**, Call OI **58.8%**. Le pinning vers $16.00 à l'expiration 29/05 (2 jours ouvrés) reste le risque dominant. Le secteur financier (XLF) reste sans direction (momentum 0.0/10). Attendre un retour au-dessus de MM50 avec volume confirmatoire, ou un test du support $15.00 pour éventuelle entrée spéculative.
**Score 6.1/10. Score Global 53.1/100. ATTENDRE.**

**Données complètes** — Cours, RSI, ATR, P/E, beta disponibles dans `data/latest.json` (snapshot 2026-05-27T10:00 UTC). Options : Max Pain $16.00 (parité avec cours), Put/Call 0.70, Call OI 58.8%. Expiration prochaine 2026-05-29 (2 jours ouvrés).

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $18.11
- **Stop-loss :** $14.56
- **Statut thèse :** —
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

- 2026-07-28 — Earnings Q2 FY2026 (62j)

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 49.59
- **MM 50j :** 16.73
- **MM 200j :** —
- **ATR 14j :** 0.71
- **Volume moy. 20j :** 70423610

---

## 📝 Résumé dernière analyse

- **Date :** 2026-05-27
- **Type :** update
- **Fichier :** `SOFI_2026-05-27_update.md`
- **Conclusion :** Snapshot 10:00 UTC (pré-marché) confirme stabilité totale vs close 2026-05-26 21:00 UTC. Cours $15.98, RSI 49.59, ATR $0.71, MM50 $16.73. Volume 80.29M (1.14×) — stable. Score Opportunité 6.1/10, Score Global 53.1/100 (ATTENDRE). SL $14.56, TP $18.11, R/R 1.50. [ALERTE DATA QUALITY] Anomalie JSON 2026-05-27 sur options (max pain $5.00 aberrant, put/call null) — valeurs historiques confirmées maintenues. Pinning 29/05 probable. Earnings dans 62j. Thèse confirmée.

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
