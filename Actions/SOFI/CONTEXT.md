# CONTEXT — SOFI — Dernière mise à jour : 2026-06-09

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
**Prix cible :** $19.41 (cours + 3×ATR)
**Stop-loss :** $14.56 (cours − 2×ATR)
**Upside/Downside :** +17.6% / −11.8%
**Dernière mise à jour :** 2026-06-09 (snapshot 13:00 UTC — close 08/06 final confirmé, données options corrigées)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le charter bancaire 2022 crée une barrière réglementaire modérée vs les fintechs non-banques. Le snapshot du **2026-06-09 à 13h UTC** reprend les données de close du 08/06 — **aucune nouvelle session de trading n'est intégrée**. Toutes les métriques de prix et de technique sont **stabiles** : cours **$16.50**, RSI **54.98**, ATR **$0.97**, MM50 **$16.76** (écart −1.55%). Le volume affiché à **79.06M (1.10×)** est stable. Le **DRAFT_refresh_2026-06-09** déclenché sur un prétendu ATR_SPIKE (5.88%) est un **faux positif** : l'ATR est stable à $0.97, sans expansion de volatilité. **[RÉSOLU]** Les données options dans `data/latest.json` sont corrigées : Max Pain **$17.00** confirmé cohérent, Put/Call **0.49** (vs 0.57 du 08/06), Call OI **67.2%** (vs 63.7% du 08/06) — repositionnement haussier marginal à très court terme. Le support immédiat est le low du 08/06 à **$15.955**, suivi de **$15.68** (low du 05/06) et **$15.00** (psychologique). La résistance immédiate est la MM50 à **$16.76**, puis **$17.00** (Max Pain) et **$17.46** (low du 02/06). La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro majeurs. Le Forward P/E **21.15** est mécaniquement attractif. Le Score Opportunité est de **6.1/10**, et le Score Global ajusté est de **53.1/100** (zone ATTENDRE) — inchangé. Le short interest à **13.68%** laisse un potentiel de squeeze si un reclaim de MM50 se matérialise avec volume. Le secteur financier (XLF) est dans le top3 sectoriel mais avec un momentum faible (4.0/10) — classement relatif par exclusion. Earnings Q2 dans **49j** (28 juillet, estimates EPS $0.10–$0.11, Rev $1.1B). ⚠️ Cours sous MM50 + échec reclaim en close + timing Défavorable = aucune entrée recommandée. Attendre reclaim MM50 $16.76 en close avec volume >1.0× ou breakout $17.00 pour réactiver la thèse haussière.
**Score 6.1/10. Score Global 61.1/100 (ajusté 53.1). ATTENDRE — Aucune entrée.**

**Données complètes** — Cours, RSI, ATR, P/E, beta disponibles dans `data/latest.json` (snapshot 2026-06-09T13:00 UTC). Options : Max Pain $17.00, Put/Call 0.49, Call OI 67.2%. Expiration prochaine 2026-06-12 (3 jours ouvrés).

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $19.41
- **Stop-loss :** $14.56
- **Statut thèse :** validée
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

- **RSI 14j :** 54.98
- **MM 50j :** 16.76
- **MM 200j :** —
- **ATR 14j :** 0.97
- **Volume moy. 20j :** 71627850

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-09
- **Type :** update
- **Fichier :** `SOFI_2026-06-09_update.md`
- **Conclusion :** Stabilité totale vs close 08/06. Données options corrigées (Max Pain $17.00, Put/Call 0.49, Call OI 67.2%). Repositionnement haussier marginal. Thèse ATTENDRE confirmée (53.1/100). DRAFT_refresh archivé (faux positif ATR_SPIKE).

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 5.88% (seuil 5.0%) — FAUX POSITIF ARCHIVÉ

---

*Généré automatiquement — ne pas éditer manuellement.*
