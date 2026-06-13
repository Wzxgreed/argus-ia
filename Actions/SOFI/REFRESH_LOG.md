# SOFI — Historique des Full Refreshes

## 2026-06-09 — Full Refresh Trigger Detected (DRAFT 21h UTC, archivé)

**Triggers :**
- atr_spike (medium) : ATR relatif 6.19% (seuil 5.0%)

**Conclusion :** CONFIRME — Faux positif. Le trigger ATR_SPIKE ne modifie pas la structure fondamentale. Pas de réécriture de `_init.md` requise.
- L'ATR relatif 6.19% est un faux positif : l'ATR est resté stable à **$1.02** entre le close 08/06 et le snapshot 09/06 21h. Aucune expansion de volatilité réelle n'est survenue.
- Aucun nouvel événement structurant ne modifie le moat, le TAM ou la qualité bénéfice. Le Filtre Qualité reste 4/6 (Quality Partielle).
- Cours $16.47, RSI 58.29, MM50 $16.78, écart MM50 −1.85%. Volume 79.33M (1.10×) — stable.
- Score Opportunité 6.0/10, Score Global ajusté 52.3/100 (ATTENDRE) — bord inférieur.
- Options : Max Pain $17.00, Put/Call 0.49, Call OI 67.2%.
- **Action :** DRAFT_refresh archivé (`SOFI_2026-06-09_DRAFT_refresh_ARCHIVED_4.md`). La mise à jour quotidienne `SOFI_2026-06-09_update.md` (snapshot 21h UTC) intègre le trigger et confirme la thèse ATTENDRE.

---

## 2026-06-09 — Full Refresh Trigger Detected (DRAFT, archivé)

**Triggers :**
- atr_spike (medium) : ATR relatif 6.45% (seuil 5.0%)

**Conclusion :** CONFIRME — Le trigger ATR_SPIKE est justifié mais ne modifie pas la structure fondamentale. Pas de réécriture de `_init.md` requise.
- L'ATR relatif 6.45% reflète l'expansion de volatilité lors de la session du 09/06 (close $15.817, −4.14%) après la consolidation post-gap du 05/06. L'ATR passe de $0.97 à $1.02 (+5.15%).
- Aucun nouvel événement structurant ne modifie le moat, le TAM ou la qualité bénéfice. Le Filtre Qualité reste 4/6 (Quality Partielle).
- Cours $15.817, RSI 53.61, MM50 $16.77, écart MM50 −5.68% (vs −1.55% à 13h). Volume 45.37M (0.65×) — baisse sans conviction institutionnelle.
- Score Opportunité 5.9/10, Score Global ajusté 51.1/100 (ATTENDRE, bord inférieur) — recul de 2.0 pts vs snapshot 13h.
- Options inchangées : Max Pain $17.00, Put/Call 0.49, Call OI 67.2%.
- **Action :** DRAFT_refresh archivé (`SOFI_2026-06-09_DRAFT_refresh_ARCHIVED_3.md`). La mise à jour quotidienne `SOFI_2026-06-09_update.md` (snapshot 17h UTC) intègre le trigger et confirme la thèse ATTENDRE affaiblie.

---

## 2026-06-08 — Full Refresh Conclu (snapshot 10:00 UTC)

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** INVALIDE — Le breakout MM50 du 01/06 est rompu. Thèse précédente (ACHETER) invalidée.
- Le gap baissier de −6.53% à $16.03 sur volume 1.15× a cassé le support MM50 ($16.75) et invalidé le breakout haussier de 4 séances.
- Le RSI est retombé de 63.90 à 52.78, le Score Momentum de 6.0 à 4.0/10 (baissier), et le Score Global ajusté de 65.8 à 49.8/100 (zone SURVEILLER).
- Aucun événement corporate ni news négative — la rupture est technique/macro-correlée (beta 2.152, secteur XLF faible).
- La valorisation s'améliore mécaniquement (Forward P/E 20.54) mais ne compense pas le momentum perdu.
- Données options corrompues dans `data/latest.json` (Max Pain $5.00 aberrant, Put/Call et Call OI null) — impossible d'évaluer le sentiment options.
- Recommandation : **ACHETER → SURVEILLER**. Aucune entrée recommandée. SL $14.05, TP $19.00, Ratio R/R 1.5×.
- Conditions pour réactiver ACHETER : (1) reclaim MM50 $16.75 avec volume >1.0×, (2) rebond vif sur $15.68 avec RSI >55, ou (3) catalyseur fondamental positif.
- **Action :** DRAFT_refresh archivés (`SOFI_2026-06-03_DRAFT_refresh_ARCHIVED.md` à `SOFI_2026-06-08_DRAFT_refresh_ARCHIVED.md`). Pas de réécriture de `_init.md` requise — la structure fondamentale du 2026-05-17 reste inchangée, mais la thèse technique est invalidée. La mise à jour `SOFI_2026-06-08_update.md` capture la nouvelle posture.

---

## 2026-05-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.25% (seuil 5.0%)

**Conclusion :** CONFIRME — La thèse précédente est confirmée et légèrement renforcée.
- Le full refresh confirme la thèse d'attente : trend baissier sous MM50 intact, RSI 30.21 = survente sans capitulation (volume 0.7×).
- Le consensus FMP renforcé (27 analystes, PT $25.41) et le Forward P/E 19.95 raisonnable justifient une légère révision à la hausse du Score Opportunité (5.1/10 vs 4.85/10) et du Score Global (43/100 vs ~39/100).
- Aucun élément fondamental nouveau ne modifie la structure du moat, du TAM ou de la qualité bénéfice. Le Filtre Qualité reste 4/6 (Quality Partielle).
- Les risques macro dominants (taux + prêts étudiants) restent inchangés et non pricés comme catalyseurs immédiats.
- Recommandation inchangée : ATTENDRE. Pas de position. Attendre retour au-dessus de MM50 ($17.05) ou test support $14.50.

**Fichier généré :** `SOFI_2026-05-17_init.md`

---

## 2026-06-03 — Full Refresh Trigger Detected (DRAFT)

**Triggers :**
- ATR_SPIKE (medium) : ATR relatif 5.13% (seuil 5.0%)

**Conclusion :** CONFIRME — Trigger déjà intégré dans l'analyse courante. Pas de réécriture de `_init.md` requise.
- L'ATR relatif 5.13% reflète la volatilité post-gap du 01/06 ($18.58, +7.37%) et le pullback du 02/06 ($17.74, −4.52%), déjà analysés en détail dans les `_update.md` des 2026-06-01 et 2026-06-02.
- Aucun nouvel événement structurant ne modifie le moat, le TAM ou la qualité bénéfice. Le Filtre Qualité reste 4/6 (Quality Partielle).
- Cours stable $17.74, RSI 63.90, MM50 $16.76, volume 76.76M (1.13×). Score Opportunité 6.1/10, Score Global 60.8/100 (ajusté 65.8) — ACHETER maintenu.
- [RÉSOLU] Anomalie options JSON corrigée dans `data/latest.json` 13h UTC : Max Pain $20.00 confirmé, Put/Call 0.54, Call OI 65.0%.
- **Action :** DRAFT_refresh archivé (`SOFI_2026-06-03_DRAFT_refresh_ARCHIVED.md`). La mise à jour quotidienne `SOFI_2026-06-03_update.md` intègre la correction options et confirme la thèse.

---

## 2026-05-18 — Full Refresh Trigger Detected (DRAFT)

**Triggers :**
- atr_spike (medium) : ATR relatif 5.25% (seuil 5.0%)

**Conclusion :** CONFIRME — Même trigger que le 2026-05-17. Pas de nouveau full refresh nécessaire.
- L'ATR relatif 5.25% est identique à celui du full refresh du 2026-05-17. Aucune nouvelle volatilité anormale n'est apparue.
- La mise à jour quotidienne du 2026-05-18 (`SOFI_2026-05-18_update.md`) intègre déjà ce niveau de volatilité et confirme la thèse.
- Cours stable $15.61, RSI 30.21 inchangé, volume faible. Support $15.38 testé sans cassure.
- Score Opportunité révisé 5.7/10 (+0.6 pt). Score Global 48.6/100 (SURVEILLER). TP $18.07, SL $13.97.
- **Action :** DRAFT_refresh archivé (`_DRAFT_refresh_2026-05-18.md`). Pas de réécriture de `_init.md` requise.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.25% (seuil 5.0%)

**Conclusion :** CONFIRME — Le DRAFT_refresh `SOFI_2026-05-18_DRAFT_refresh.md` a été traité et archivé.
- L'ATR relatif 5.25% est identique à celui du full refresh du 2026-05-17 et de la mise à jour matinale du 2026-05-18 (08:46). Aucune nouvelle volatilité anormale n'est apparue.
- Le snapshot `data/latest.json` (timestamp 2026-05-18T10:00:08+00:00) confirme l'absence de changement de données : cours $15.61, RSI 30.21, ATR $0.82, MM50 $17.05, volume 0.74×.
- Score Opportunité stable à 5.7/10. Score Global 48.6/100 (SURVEILLER). TP $18.07, SL $13.97.
- **Action :** DRAFT_refresh supprimé (`SOFI_2026-05-18_DRAFT_refresh.md`). Pas de réécriture de `_init.md` requise — la thèse du 2026-05-17 reste valide.

---

## 2026-05-18 — Full Refresh Triggered (ancien DRAFT résiduel)

**Triggers :**
- atr_spike (medium) : ATR relatif 5.25% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — Ce DRAFT était un résidu du pipeline matinal. Même conclusion que ci-dessus : CONFIRME. Aucune modification de thèse.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.25% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (révisée 13:00 UTC). CONFIRME. Aucune modification de thèse.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.25% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (révisée 13:00 UTC). CONFIRME. Aucune modification de thèse.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.40% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (snapshot 20:56 UTC). CONFIRME. Aucune modification de thèse. Données identiques au snapshot 20:12 UTC.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.41% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (snapshot 20:56 UTC). CONFIRME. Aucune modification de thèse. Données identiques au snapshot 20:12 UTC.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (snapshot 20:56 UTC). CONFIRME. Aucune modification de thèse. Données identiques au snapshot 20:12 UTC.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (snapshot 20:56 UTC). CONFIRME. Aucune modification de thèse. Données identiques au snapshot 20:12 UTC.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (snapshot 20:56 UTC). CONFIRME. Aucune modification de thèse. Données identiques au snapshot 20:12 UTC.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT résiduel traité par l'update du 2026-05-18 (snapshot 20:56 UTC). CONFIRME. Aucune modification de thèse. Données identiques au snapshot 20:12 UTC.

---

## 2026-05-18 — Nettoyage DRAFT_refresh résiduels (snapshot 21:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — Les fichiers `_DRAFT_refresh_2026-05-18.md` et `SOFI_2026-05-18_DRAFT_refresh.md` ont été supprimés. Le `data/latest.json` (timestamp 2026-05-18T21:00:08+00:00) confirme l'absence de changement de données vs le snapshot 20:56 UTC : cours $15.71, RSI 32.70, ATR $0.84, MM50 $16.98, volume 0.97×. L'analyse `SOFI_2026-05-18_update.md` est à jour et ne nécessite pas de réécriture. Thèse SURVEILLER confirmée (Score Opportunité 5.7/10, Score Global 48.6/100). Pas de nouveau `_init.md` requis.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT_refresh résiduel traité par l'update du 2026-05-19 (snapshot 10:00 UTC). CONFIRME. Aucune modification de thèse.
- Le snapshot `data/latest.json` (timestamp 2026-05-19T10:00:07+00:00) confirme l'absence de changement de données vs le close 2026-05-18 20:56 UTC : cours $15.71, RSI 32.70, ATR $0.84, MM50 $16.98, volume 0.98×.
- Données options partiellement manquantes (anomalie Max Pain $1.00, Put/Call null) — pas d'impact sur la thèse, dernières valeurs fiables conservées.
- Score Opportunité stable à 5.7/10. Score Global 48.6/100 (SURVEILLER). TP $18.23, SL $14.03.
- **Action :** DRAFT_refresh archivé (`SOFI_2026-05-19_DRAFT_refresh_ARCHIVED.md`). Pas de réécriture de `_init.md` requise — la thèse du 2026-05-17 reste valide.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-19 — Full Refresh Triggered (snapshot 13:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 5.35% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT_refresh résiduel traité par l'update du 2026-05-19 (snapshot 13:00 UTC). CONFIRME. Aucune modification de thèse.
- Le snapshot `data/latest.json` (timestamp 2026-05-19T13:00:07+00:00) confirme l'absence de changement de données vs le snapshot 10:00 UTC : cours $15.71, RSI 32.70, ATR $0.84, MM50 $16.98, volume 0.98×.
- Données options revenues à 13:00 UTC (Max Pain $16.00, Put/Call 0.59, Call OI 62.7%) — légère hausse du sentiment options à très court terme, mais pas de modification structurelle de la thèse.
- Score Opportunité stable à 5.7/10. Score Global 48.6/100 (SURVEILLER). TP $18.23, SL $14.03.
- **Action :** DRAFT_refresh supprimé (`SOFI_2026-05-19_DRAFT_refresh.md`). Pas de réécriture de `_init.md` requise — la thèse du 2026-05-17 reste valide.

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +9.19% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.47% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-01 — Full Refresh Conclu (snapshot 13:00 UTC)

**Triggers :**
- price_gap (medium) : Gap +7.37% overnight (seuil ±5.0%)

**Conclusion :** MODIFIE — La thèse est confirmée mais renforcée avec un reclassement majeur.
- Le gap +7.37% à $18.22 valide le rebond technique attendu depuis le 25/05. Breakout MM50 ($16.71) avec écart +9.0% et volume 2.25× = signal technique fort.
- Les fondamentaux n'ont pas changé structurellement : Forward P/E 23.35 raisonnable, Quality Partielle 4/6 inchangée, Filtre Qualité non affecté par le gap (événement technique).
- Le repositionnement options haussier (Call OI 69.6%, Put/Call 0.44, Max Pain $17.00) confirme le sentiment positif à très court terme.
- Recommandation : **ATTENDRE → ACHETER** (Score Opportunité 6.3/10, Score Global 72.5/100).
- SL $16.52, TP $20.77, Ratio R/R 1.5×, sizing réduit (beta 2.126).
- RSI 69.63 = proche surachat, pullback vers $17.20–$17.50 probable à court terme avant continuation.
- **Action :** DRAFT_refresh archivés (`_DRAFT_refresh_2026-05-31_ARCHIVED.md`, `_DRAFT_refresh_2026-06-01_ARCHIVED.md`). Pas de réécriture de `_init.md` requise — la structure fondamentale du 2026-05-17 reste valide, le gap est un événement technique capturé par `SOFI_2026-06-01_update.md`.

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.13% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.13% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.13% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.13% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.13% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.13% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.79% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.62% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.29% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.00% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.70% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.98% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.70% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.98% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.70% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.98% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.70% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.98% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.70% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.98% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 5.70% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.42% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.42% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.47% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.05% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -7.00% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.14% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.50% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.17% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Conclu (snapshot 13:00 UTC, DRAFT résiduel traité)

**Triggers :**
- price_gap (medium) : Gap -6.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.18% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT_refresh résiduel traité par l'update du 2026-06-08 (snapshot 13:00 UTC). Même conclusion que le full refresh du 2026-06-08 10:00 UTC : **INVALIDE**.
- Le snapshot 13:00 UTC confirme l'absence de changement de données vs le snapshot 10:00 UTC : cours $16.03, RSI 52.78, ATR $0.99, MM50 $16.75, volume 81.21M (1.15×). Les données de clôture sont identiques car il s'agit du même close du 05/06 (pré-ouverture lundi matin avant 9:30 ET).
- **[RÉSOLU]** Anomalie options JSON corrigée dans `data/latest.json` (snapshot 13:00 UTC) : Max Pain $17.00 (vs $5.00 aberrant à 10:00 UTC), Put/Call 0.57 (vs `null`), Call OI 63.7% (vs `null`).
- Thèse précédente (ACHETER) reste invalidée : breakout MM50 du 01/06 rompu, Score Global ajusté 49.8/100 (SURVEILLER), SL $14.05, TP $19.00.
- **Action :** DRAFT_refresh archivé (`_DRAFT_refresh_2026-06-08_ARCHIVED.md`). La mise à jour `SOFI_2026-06-08_update.md` est à jour et intègre la correction options.

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.82% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.84% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.87% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.88% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.88% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT_refresh faux positif traité par l'update du 2026-06-09 (snapshot 10:00 UTC).
- Le trigger ATR_SPIKE 5.88% est un **faux positif** : l'ATR est resté stable à **$0.97** entre le close 08/06 et le snapshot 09/06. Aucune expansion de volatilité n'est survenue.
- Le snapshot `data/latest.json` (timestamp 2026-06-09T10:00:09+00:00) confirme la **stabilité totale** des données vs le close 08/06 : cours $16.50, RSI 54.98, ATR $0.97, MM50 $16.76, volume 79.06M (1.10×) — ajustement mécanique mineur vs 77.12M (1.08×).
- Les données options dans `data/latest.json` sont partielles (Max Pain aberrant $5.00, Put/Call et Call OI null) — valeurs du 08/06 conservées : Max Pain $17.00, Put/Call 0.57, Call OI 63.7%.
- Thèse **ATTENDRE** confirmée sans changement : Score Opportunité 6.1/10, Score Global ajusté 53.1/100. SL $14.56, TP $19.41, R/R 1.50.
- **Action :** DRAFT_refresh archivé (`SOFI_2026-06-09_DRAFT_refresh_ARCHIVED.md`). Pas de réécriture de `_init.md` requise — la structure fondamentale du 2026-05-17 reste valide, et la mise à jour `SOFI_2026-06-09_update.md` capture la stabilité.

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.88% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — Même DRAFT_refresh résiduel que ci-dessus. Faux positif ATR_SPIKE. Aucune modification de thèse.

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.88% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — DRAFT_refresh résiduel traité par l'update du 2026-06-09 (snapshot 13:00 UTC). Même conclusion que ci-dessus : **FAUX POSITIF**.
- Le snapshot `data/latest.json` (timestamp 2026-06-09T13:00:07+00:00) confirme la **stabilité totale** des données vs le snapshot 10:00 UTC : cours $16.50, RSI 54.98, ATR $0.97, MM50 $16.76, volume 79.06M (1.10×).
- **[RÉSOLU]** Données options JSON corrigées : Max Pain $17.00 (cohérent), Put/Call 0.49, Call OI 67.2% — repositionnement haussier marginal.
- Thèse **ATTENDRE** confirmée sans changement : Score Opportunité 6.1/10, Score Global ajusté 53.1/100. SL $14.56, TP $19.41, R/R 1.50.
- **Action :** DRAFT_refresh archivé (`SOFI_2026-06-09_DRAFT_refresh_ARCHIVED_2.md`). Pas de réécriture de `_init.md` requise.

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 5.88% (seuil 5.0%)

**Conclusion :** ARCHIVÉ — Même DRAFT_refresh résiduel que ci-dessus. Faux positif ATR_SPIKE. Aucune modification de thèse.

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.37% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.45% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.19% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.19% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.33% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.50% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.04% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.04% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.04% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.04% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.04% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.04% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 6.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.62% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.56% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 6.51% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---
