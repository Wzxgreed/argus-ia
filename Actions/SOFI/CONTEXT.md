# CONTEXT — SOFI — Dernière mise à jour : 2026-06-23

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ACHETER (Réduit)
**Prix cible :** $20.10 (cours + 3×ATR)
**Stop-loss :** $15.10 (cours − 2×ATR)
**Upside/Downside :** +17.5% / −11.7%
**Dernière mise à jour :** 2026-06-23 (snapshot 13:00 UTC — stabilité mécanique totale, correction options, XLF amélioré)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le charter bancaire 2022 crée une barrière réglementaire modérée vs les fintechs non-banques. Le snapshot du **2026-06-23 à 13h00 UTC** (pré-ouverture US) reprend le close final du 22/06 : cours **$17.10**, RSI **40.98** (zone neutre-basse), ATR **$1.00** (stable), MM50 **$16.96** (+0.83% écart), volume **75.33M (0.90×)**. Le **Score Global ajusté est à 63.3/100**, dans la fourchette **ACHETER (60–74)** avec sizing **Réduit** — au bord inférieur. Le **Score Momentum est à 5.0/10**, le **Score Valorisation reste à 5.5/10**.

**Point de confirmation :** Le reclaim MM50 reste valide ($17.10 vs $16.96) avec un écart rétréci de +0.83%. Le RSI 40.98 est proche de la zone de survente — zone d'entrée technique favorable pour les investisseurs patient. L'ATR stable à $1.00 confirme une volatilité contenue. Aucun nouveau close depuis le 22/06.

**[LEVÉ] Point de vigilance majeur du 17h :** Le volume signalé à 0.52× (41.83M) à 17h00 du 22/06 était une sous-estimation due aux données préliminaires. Le volume final **75.33M (0.90×)** est normalisé. **La règle absolue interne (volume <0.7× = timing Défavorable) ne s'applique plus.**

**Amélioration marginale :** Le momentum sectoriel XLF est remonté de 5.08 à **5.45/10** (+0.37 pt), atténuant le vent de poupe modéré.

**[RÉSOLU] Données options :** L'anomalie JSON du snapshot 10h (Max Pain $5.00 aberrant, Put/Call et Call OI null) est corrigée à 13h. Valeurs restaurées : Max Pain **$18.00**, Put/Call **0.50**, Call OI **66.8%**. Le repositionnement est légèrement plus haussier que l'historique (−0.01 Put/Call, +0.4 pt Call OI), confirmant le sentiment options positif.

Le short interest reste élevé à **14.71%** — setup asymétrique squeeze/pression vendeuse intact. La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro structurels. Le Forward P/E **20.94** reste mécaniquement attractif. Le consensus PT **$25.41** (+48.6% upside vs $17.10) est inchangé. Le Filtre Qualité **4/6** (Quality Partielle) n'est pas remis en cause. Earnings Q2 dans **35j** (28 juillet, estimates EPS $0.10–$0.11, Rev $1.1B). XLF (Financials) momentum **5.45/10** (#3/11 sector rotation) — vent de poupe atténué. ⚠️ Reclaim MM50 très rétréci (+0.83%) — un close sous MM50 invaliderait le breakout. [ANOMALIE DATA] `previous_close` $17.91 et `change_pct` −4.52% dans `latest.json` incohérents avec le close final 22/06 — bug Yahoo, sans impact sur l'analyse. Entrée suggérée $17.10, SL $15.10, TP $20.10, Ratio R/R 1.5×.
**Score Opportunité 5.8/10. Score Global 63.3/100. ACHETER (Réduit) — Thèse confirmée.**

**Données complètes** — Cours, RSI, P/E, beta, ATR, MM50 disponibles dans `data/latest.json` (snapshot 2026-06-23T13:00 UTC). DRAFT_refresh 23/06 archivé faux positif ATR_SPIKE (même motif que 15–17/06 et 22/06).

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $20.10
- **Stop-loss :** $15.10
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

- **RSI 14j :** 40.98
- **MM 50j :** 16.96
- **MM 200j :** —
- **ATR 14j :** 1.0
- **Volume moy. 20j :** 82114745

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-23
- **Type :** update
- **Fichier :** `SOFI_2026-06-23_update_13h00.md`
- **Conclusion :** Snapshot 13h — stabilité mécanique totale, correction options JSON, thèse confirmée. Aucun nouveau close depuis 22/06.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 5.85% (seuil 5.0%) — **archivé faux positif** (ATR absolu stable à $1.00, même motif que 15–17/06 et 22/06)

---

*Généré automatiquement — ne pas éditer manuellement.*
