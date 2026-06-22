# CONTEXT — SOFI — Dernière mise à jour : 2026-06-22

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ACHETER (Réduit)
**Prix cible :** $20.29 (cours + 3×ATR)
**Stop-loss :** $15.29 (cours − 2×ATR)
**Upside/Downside :** +17.3% / −11.6%
**Dernière mise à jour :** 2026-06-22 (snapshot 17:00 UTC — close final confirmé, retrait −3.46% sur volume effondré)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le charter bancaire 2022 crée une barrière réglementaire modérée vs les fintechs non-banques. Le snapshot du **2026-06-22 à 17h00 UTC** (close final confirmé) enregistre : cours **$17.29** (−3.46% vs snapshot 10h), RSI **41.95** (−6.05 pts, zone neutre-basse), ATR **$1.00** (stable), MM50 **$16.96** (+1.94% écart, rétréci), volume **41.83M (0.52×)**. Le **Score Global ajusté est à 63.3/100**, dans la fourchette **ACHETER (60–74)** avec sizing **Réduit** — au bord inférieur. Le **Score Momentum est à 5.0/10** (normalisation haussière), le **Score Valorisation reste à 5.5/10**.

**Point de confirmation :** Le reclaim MM50 reste valide ($17.29 vs $16.96) mais l'écart s'est rétréci à +1.94% (vs +5.72% ce matin). Le RSI 41.95 est proche de la zone de survente — ce n'est pas un signal baissier en soi mais une zone d'entrée technique favorable pour les investisseurs patient. L'ATR stable à $1.00 confirme une volatilité contenue.

**Point de vigilance majeur :** Le volume est effondré à 0.52× (41.83M vs moy. 80.44M), soit près de la moitié de la moyenne 20j. Ce n'est pas un signal de distribution massif (pas de gap baissier, pas de news négative), mais c'est un manque de conviction institutionnelle évident. **Règle absolue interne : si le volume reste <0.7× sur la prochaine session, le timing basculera en Défavorable.**

**[RÉSOLU] Anomalie options :** Les données options corrompues du snapshot 10h (Max Pain $5.00 aberrant, Put/Call et Call OI null) sont corrigées dans le snapshot 17h : Max Pain **$18.00** (pinning possible expiration 26/06), Put/Call **0.51**, Call OI **66.4%** — repositionnement haussier conservé mais moins extrême que les valeurs historiques de ce matin.

Le short interest reste élevé à **14.71%** — setup asymétrique squeeze/pression vendeuse intact. La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro structurels. Le Forward P/E **21.18** reste mécaniquement attractif. Le consensus PT **$25.41** (+46.9% upside vs $17.29) est inchangé. Le Filtre Qualité **4/6** (Quality Partielle) n'est pas remis en cause. Earnings Q2 dans **36j** (28 juillet, estimates EPS $0.10–$0.11, Rev $1.1B). XLF (Financials) momentum **5.15/10** (#3/11 sector rotation) — vent de poupe sectoriel modéré, légèrement amélioré vs ce matin. ⚠️ Reclaim MM50 rétréci (+1.94%) sur volume très faible. Entrée suggérée $17.29, SL $15.29, TP $20.29, Ratio R/R 1.5×. Un retour sous $17.10 (low du jour), sous MM50, ou un volume <0.7× sur la prochaine session justifierait une révision du timing → Défavorable.
**Score Opportunité 5.8/10. Score Global 63.3/100. ACHETER (Réduit) — Thèse confirmée avec vigilance accrue.**

**Données complètes** — Cours, RSI, P/E, beta, ATR, MM50 disponibles dans `data/latest.json` (snapshot 2026-06-22T17:00 UTC). DRAFT_refresh 22/06 archivé faux positif ATR_SPIKE (même motif que 15–17/06).

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $20.29
- **Stop-loss :** $15.29
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- **2026-05-17** · earnings · Miss / Imprécis · Ligne:  | 2026-05-17 | SOFI | `_init.md` | ATTENDRE | $19.51

---

## 🚨 Alertes actives

- Baisse — $13.78 (SL 2×ATR) — 🟢 Active
- Hausse — $18.88 (prix cible) — 🟢 Active
- Volume — >2× moy. 20j (>140.7M) — 🟢 Active

---

## 📅 Prochains événements

- Aucun événement à venir.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 40.9
- **MM 50j :** 16.96
- **MM 200j :** —
- **ATR 14j :** 1.0
- **Volume moy. 20j :** 81928467

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-22
- **Type :** full refresh
- **Fichier :** `SOFI_2026-06-22_DRAFT_refresh.md`
- **Conclusion :** > **Date :** 2026-06-22

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 5.85% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
