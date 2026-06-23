# IREN — Historique des Full Refreshes

---

## 2026-06-23 — Full Refresh Complété (snapshot 10:00 UTC)

**Triggers :**
- price_gap (medium) : Gap -5.15% overnight (seuil ±5.0%) — **faux positif**
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%) — **faux positif**

**Conclusion :** confirm — faux positif (triggers hérités du close 2026-06-22, données brutes strictement identiques)

Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-23T10:00:01 UTC). Les données brutes sont **strictement identiques** au snapshot 21h UTC du 2026-06-22 (cours $56.87, RSI 40.17, ATR $5.66, MM50 $54.37, volume 34.93 M, scores 4.9/10 et 54.3/100). Aucun nouvel événement majeur n'a eu lieu. **Anomalie options détectée** : Max Pain $20.00, put/call null, call OI 0.0% — structure incohérente qui remplace la structure fiable du 22/06 (Max Pain $40.00, put/call 4.99, call OI 16.7%). La structure du 22/06 est conservée comme référence opérationnelle. Thèse confirmée : **ATTENDRE** (Score Global 54.3/100). DRAFT_refresh complété et archivé (`IREN_2026-06-23_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-23_DRAFT_refresh_archived.md`). Fichier de référence : [IREN_2026-06-23_update.md](IREN_2026-06-23_update.md).

---

## 2026-06-17 — Full Refresh Déclenché (snapshot 17:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 9.62% (seuil 5.0%)

**Conclusion :** confirm — faux positif (même trigger ATR_SPIKE hérité, ATR en léger repli)

Le DRAFT_refresh a été déclenché automatiquement à 17:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T17:00:07 UTC). Les données brutes montrent une **stabilité mécanique totale** par rapport au snapshot 13h UTC : cours **$59.54** (+0.61%), ATR **$5.73** (−$0.08 vs 13h), MM50 **$53.54** (+$0.48), options stables (Max Pain $35.00, put/call 1.38, call OI 42.1%). Le seul mouvement significatif est l'**effondrement du volume** à **15.69 M** (33.1% de la moyenne 20j vs 65.9% à 13h), interprété comme un désengagement institutionnel ou une attitude d'attente pré-expiration du 18/06. Le RSI remonte à **44.32** (+4.36 pts), sortant de la zone 40. Les scores sont **strictement identiques** au snapshot 13h (Opportunité 5.2/10, Global 56.8/100). L'action reste **ATTENDRE**. Le trigger ATR_SPIKE est un **faux positif** (même configuration héritée du pipeline, ATR en repli). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_17h00.md`). Fichier de référence : [IREN_2026-06-17_update_17h00.md](IREN_2026-06-17_update_17h00.md).

---

## 2026-06-16 — Full Refresh Déclenché (snapshot 17:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 9.61% (seuil 5.0%)

**Conclusion :** modify — dégradation du momentum et révision des données brutes

Le DRAFT_refresh a été déclenché automatiquement à 17:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-16T17:00:07 UTC). Les données brutes ont été **révisées par Yahoo Finance** : open corrigé à **$59.99** (−$2.33 vs $62.32 à 13h), high à **$62.02** (−$1.15), low à **$59.05** (−$1.29), previous_close corrigé à **$60.85** (vs $59.77 erroné à 13h). Le cours à **$60.335** représente un repli de **−0.85%** vs le close corrigé du 15/06. Le RSI a chuté de **51.08 à 41.06** (−10.02 pts), signalant une accélération de la pression vendeuse intra-session. Le Score Momentum est dégradé de **7.3 à 5.5/10** (−1.8 pt), entraînant une baisse du Score Global ajusté de **57.5 à 53.0/100** (−4.5 pts). L'action reste **ATTENDRE**. La structure options reste inchangée et cohérente (Max Pain $35.00, put/call 1.44, call OI 41.0%). Volume très faible (16.82 M = 35.2% moyenne 20j à 17h UTC, session en cours). DRAFT_refresh complété et archivé (`IREN_2026-06-16_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-16_17h00.md`). Fichier de référence : [IREN_2026-06-16_update_17h00.md](IREN_2026-06-16_update_17h00.md).

---

## 2026-06-16 — Full Refresh Complété

**Triggers :**
- atr_spike (medium) : ATR relatif 10.16% (seuil 5.0%)

**Conclusion :** confirm — faux positif (trigger hérité du 2026-06-15)

Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par ATR_SPIKE sur le snapshot `data/2026-06-16.json`. Les données brutes sont **strictement identiques** au snapshot 21h UTC du 2026-06-15 (cours $60.85, RSI 51.08, ATR $6.18, MM50 $52.58, volume 33.08 M, scores 5.3/10 et 57.5/100). Aucun nouvel événement majeur n'a eu lieu. Le marché est fermé ou les données pre-market n'ont pas évolué. **Anomalie options détectée** : Max Pain $100.00, put/call null, call OI 0.0% — structure incohérente qui remplace la structure fiable du 15/06 (Max Pain $40.00, put/call 1.62, call OI 38.1%). La structure du 15/06 est conservée comme référence opérationnelle. Thèse confirmée : **ATTENDRE** (Score Global 57.5/100). DRAFT_refresh complété et archivé (`IREN_2026-06-16_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-16.md`). Fichier de référence : [IREN_2026-06-16_update.md](IREN_2026-06-16_update.md).

---

## 2026-06-15 — Full Refresh Triggered (snapshot 10:00 UTC)

**Triggers :**
- price_gap (medium) : Gap +5.40% vs previous close $56.71 (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** modify favorablement — upgrade SURVEILLER → ACHETER (Sizing Réduit)

Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/2026-06-15.json`. Les données révèlent un upgrade algorithmique majeur : Score Global ajusté rehaussé de **44.3 à 61.8/100** (+17.5 pts), porté par une amélioration simultanée des trois axes (Catalyseur 6.3/10, Valorisation 4.0/10, Momentum 7.5/10). L'action passe de **SURVEILLER** à **ACHETER (Sizing Réduit)** avec timing **Favorable**. Les données techniques manquantes depuis le 2026-06-08 sont rétablies : ATR **$6.27**, MM50 **$52.06**. Le cours à **$59.77** se tient à +14.8% au-dessus de la MM50, confirmant la tendance haussière intermédiaire. Le RSI se normalise à **52.86** (neutre), favorable à l'entrée. Les multiples se dégradent mécaniquement (P/E 77.62×, EV/EBITDA 157.04×) sans nouvelle fondamentale. Les valeurs options du snapshot sont corrompues (Max Pain $100.00, put/call null) — les dernières valeurs fiables restent celles du 10/06. Aucune news Yahoo ni mention Reddit n'accompagne le mouvement, qui est purement technique/algorithmique. DRAFT_refresh archivé (`IREN_2026-06-15_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-15_DRAFT_refresh_archived.md`). Analyse complète sauvegardée dans `IREN_2026-06-15_update.md` (snapshot 10:00 UTC).

---

## 2026-06-09 — Full Refresh Triggered (snapshot 17:00 UTC)

**Triggers :**
- price_gap (high) : Gap −11.65% vs previous close $59.19 (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.59% (seuil 5.0%)

**Conclusion :** modify — vigilance accrue

Le DRAFT_refresh a été déclenché automatiquement à 17:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/2026-06-09.json`. Les données révèlent une correction sévère de −11.65% en séance : cours $52.295 (vs $59.19 à 13h), high $60.86, low $51.145, range intraday 18.6%. Le rejet massif du high $60.86 et le close faible dégradent le momentum technique (RSI 54.23, MM50 $50.67 testée à +3.2%). Cependant, la valorisation s'améliore mécaniquement (P/E 67.86×, P/B 6.69×, upside consensus +32.2%). Les options restent inchangées (put/call 2.22, puts 69.0%), signalant que le marché options n'a pas réagi à la chute. Le Score Opportunité reste inchangé à 5.7/10 (Catalyseur 6.8, Valorisation 4.5, Momentum 6.0), le Score Global reste 61.8/100. L'action ACHETER (Sizing Réduit) est maintenue mais la thèse est modifiée avec vigilance accrue. La MM50 ($50.67) est désormais le niveau critique : si cassure sans rebond → réviser en ATTENDRE. DRAFT_refresh archivé. Analyse complète sauvegardée dans `IREN_2026-06-09_update.md` (snapshot 17:00 UTC).

---

## 2026-06-09 — Full Refresh Triggered (faux positif)

**Triggers :**
- price_gap (medium) : Gap +8.91% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** confirm — faux positif

Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par PRICE_GAP et ATR_SPIKE, mais les triggers sont hérités du mouvement du 2026-06-08 (previous close $54.35 → open $56.60 → close $59.19). Les données du snapshot 10:00 UTC du 9 juin sont strictement identiques au close officiel du 8 juin (cours $59.19, RSI 58.78, ATR $5.68, MM50 $50.32, volume ~41.0 M). Aucun nouvel événement majeur n'a eu lieu. DRAFT_refresh archivé. Anomalie détectée : `data/latest.json` retourne Max Pain $20.00 (incohérent) et put/call null — valeurs fiables maintenues : Max Pain $33.00, put/call 3.95, call OI 20.2%. Thèse confirmée ACHETER (Sizing Réduit) — Score Opportunité 5.7/10, Global 61.8/100.

---

## 2026-06-03 — Full Refresh Triggered (faux positif)

**Triggers :**
- atr_spike (medium) : ATR relatif 7.67% (seuil 5.0%)

**Conclusion :** confirm — faux positif

Le DRAFT_refresh a ete declenche automatiquement a 10:00 UTC par ATR_SPIKE, mais les donnees brutes sont strictement identiques au close officiel du 2026-06-02 (cours $66.60, RSI 61.11, ATR $5.11, MM50 $48.75, volume 51.34 M). L'ATR n'a pas change — le trigger est mecanique sur une volatilite historique deja integree. Le marché US etant ferme jusqu'a 14:30 UTC, aucun nouveau flux de marche n'est disponible. DRAFT_refresh archive. Anomalie detectee : `data/latest.json` retourne Max Pain $20.00 (incohérent) et put/call null — valeurs fiables maintenues : Max Pain $52.00, put/call 2.09, call OI 32.4%. These confirmee ATTENDRE (Score Opportunite 4.8/10, Global 52.5/100).

---

## 2026-05-17 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -9.35% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.39% (seuil 5.0%)

**Conclusion :** confirm

Les triggers confirment la these ATTENDRE precedente. Le gap -9.35% coincidant avec les earnings illustre la volatilite extreme du titre (beta 4.18) sans apporter d'element nouveau modifiant le fondamental. Le Filtre Qualite reste a 4/6, le Forward P/E negatif et le FCF negatif maintiennent le Score Opportunite ajuste a ~4.2/10. Aucun changement de these requis.

---

## 2026-05-18 — Full Refresh Triggered (session matinale)

**Triggers :**
- price_gap (medium) : Gap -9.35% overnight (seuil ±5.0%) — **donnees inchanges vs 2026-05-17**
- atr_spike (medium) : ATR relatif 10.39% (seuil 5.0%)

**Conclusion :** confirm

Le cours est stable a $52.94 (meme niveau que le 2026-05-17). Les triggers sont des duplicatas de la session precedente — aucun nouveau gap ni spike ATR n'a ete detecte aujourd'hui. L'earnings Q1 2026 est attendu le 2026-05-18 mais les resultats ne sont pas encore integres dans les feeds. These inchangee : ACHETER sizing reduit (Score Opportunite 5.8/10, Score Global 63.3/100), en attente des resultats earnings pour revision eventuelle.

---

## 2026-05-18 — Full Refresh Triggered (pipeline 13:00 UTC)

**Triggers :**
- price_gap (medium) : Gap -9.35% overnight (seuil ±5.0%) — **duplicata, deja traite ce jour**
- atr_spike (medium) : ATR relatif 10.39% (seuil 5.0%) — **duplicata, deja traite ce jour**

**Conclusion :** confirm

Revue manuelle post-pipeline : les donnees brutes (cours $52.94, RSI 54.61, ATR 5.50, scores agents inchanges) sont identiques au snapshot 13:00 UTC. Aucun nouveau flux post-earnings n'a ete integre. DRAFT_refresh archives. These confirmee avec reserve earnings.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.44% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.98% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (20:07 UTC), aucun nouveau flux post-earnings intégré.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.89% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.12% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (20:07 UTC), aucun nouveau flux post-earnings intégré.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.85% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (20:07 UTC), aucun nouveau flux post-earnings intégré.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (20:07 UTC), aucun nouveau flux post-earnings intégré.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (20:07 UTC), aucun nouveau flux post-earnings intégré.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 20:39 UTC et 21:00 UTC, aucun nouveau flux post-earnings intégré. DRAFT_refresh complété et archivé.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 20:39 UTC et 21:00 UTC, aucun nouveau flux post-earnings intégré. DRAFT_refresh complété et archivé.

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 21:00 UTC et 22:35 UTC, aucun nouveau flux post-earnings intégré. DRAFT_refresh complété et archivé (_ARCHIVED_DRAFT_refresh_2026-05-18_5.md).

---

## 2026-05-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 21:00 UTC et 22:35 UTC du 2026-05-18, aucun nouveau flux post-earnings intégré. DRAFT_refresh complété et archivé.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 22:35 UTC du 2026-05-18, aucun nouveau flux post-earnings intégré. DRAFT_refresh complété et archivé.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 22:35 UTC du 2026-05-18, aucun nouveau flux post-earnings intégré. DRAFT_refresh complété et archivé.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (22:35 UTC du 2026-05-18), aucun nouveau flux post-earnings intégré.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.86% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (22:35 UTC du 2026-05-18), aucun nouveau flux post-earnings intégré.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.62% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.80% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot précédent, aucun nouveau flux post-earnings intégré.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.61% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot précédent, aucun nouveau flux post-earnings intégré.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.34% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.77% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot précédent, aucun nouveau flux post-earnings intégré.

---

## 2026-05-19 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.39% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.77% (seuil 5.0%)

**Conclusion :** confirm — données légèrement révisées vs snapshot 17:00 UTC (cours $47.74 vs $48.405, volume 36.45M vs 22.64M). Le volume en fin de session est plus actif (69% du moyen 20j) suggérant une distribution réelle sous $48.50. Aucun nouveau flux post-earnings intégré. Score Opportunité légèrement révisé à 6.2/10 (−0.1 pt), Score Global ajusté 67.0/100 (−1.3 pt). Thèse modifiée sous pression confirmée. DRAFT_refresh archivé.

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.39% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.77% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 21:00 UTC du 2026-05-19 (cours $47.74, RSI 54.95, ATR 5.62, MM50 45.17). Le Max Pain est révisé à $20.00 (expiration 2026-05-22), élèvant le tail risk à −58.1%. Aucun nouveau flux post-earnings intégré. Earnings Q1 2026 attendus aujourd'hui (J=0). Score Opportunité 6.2/10 inchangé, Score Global ajusté 67.0/100 inchangé. Thèse confirmée avec vigilance accrue. DRAFT_refresh complété et archivé.

---

## 2026-05-20 — Full Refresh Triggered (duplicata)

**Triggers :**
- price_gap (medium) : Gap -5.39% overnight (seuil ±5.0%) — duplicata
- atr_spike (medium) : ATR relatif 11.77% (seuil 5.0%) — duplicata

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent. DRAFT_refresh archivé.

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.39% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.77% (seuil 5.0%)

**Conclusion :** confirm — données strictement inchangées vs snapshot 10:00 UTC (cours $47.74, RSI 54.95, ATR 5.62, MM50 45.17). Le Max Pain est corrigé de $20.00 à $33.00 dans le snapshot 13:00 UTC (anomalie de données résolue). Put/call ratio (1.21) et call OI % (45.2%) sont de retour. Aucun nouveau flux post-earnings intégré. Earnings Q1 2026 attendus aujourd'hui (J=0). Score Opportunité 6.2/10 inchangé, Score Global ajusté 67.0/100 inchangé. Thèse confirmée, anomalie options résolue. DRAFT_refresh complété et archivé.

---

## 2026-05-20 — Full Refresh Triggered (duplicata)

**Triggers :**
- price_gap (medium) : Gap -5.39% overnight (seuil ±5.0%) — duplicata
- atr_spike (medium) : ATR relatif 11.77% (seuil 5.0%) — duplicata

**Conclusion :** confirm — duplicata de session, données inchangées vs snapshot précédent (13:00 UTC). DRAFT_refresh archivé.

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.26% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.03% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +9.38% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.99% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.39% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.01% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.00% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.00% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-20 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.00% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.00% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.00% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.00% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.00% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +6.77% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.52% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.00% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.11% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.37% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-21 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.37% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.37% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.37% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.37% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.37% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.15% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.14% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-23 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-24 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-25 — Full Refresh Complété (après analyse LLM)

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)
- price_gap (high) : Gap +10.41% overnight (seuil ±5.0%) — duplicatas multiples depuis 2026-05-20

**Conclusion :** modify

Le rally +19.0% en 5 sessions ($47.74 → $56.83) confirme le momentum technique mais modifie la thèse sur la dimension valuation. Le Score Valorisation est révisé de 4.5/10 à 4.0/10 (P/E 73.8×, EV/EBITDA 149.9×). Le put/call ratio à 2.35 et le call OI à 29.8% signalent une défiance massive des options traders avant l'earnings J=0. La thèse reste ACHETER sizing réduit (Score Global 65.8/100) avec vigilance accrue. DRAFT_refresh complété et archivé. Fichier de référence : [IREN_2026-05-25_update.md](IREN_2026-05-25_update.md).

---

## 2026-05-25 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm — duplicata du FULL REFRESH complété précédemment ce jour (voir entrée ci-dessus). Données strictement inchangées vs snapshot 13:00 UTC. DRAFT_refresh archivé (_ARCHIVED_DRAFT_refresh_2026-05-25_2.md).

---

## 2026-05-25 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm — duplicata du FULL REFRESH complété précédemment ce jour. Données strictement inchangées vs snapshot 13:00 UTC. Aucun nouveau flux post-earnings intégré. DRAFT_refresh archivé.

---

## 2026-05-25 — Full Refresh Complété (snapshot 21:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm

Données strictement inchangées vs snapshot 17:00 UTC (cours $56.83, RSI 56.77, ATR $5.85, MM50 $46.10, scores 6.1/10 et 65.8/100). Marché fermé Memorial Day après clôture. Aucun nouveau flux post-earnings intégré (J=0, résultats non publiés). Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh complété et archivé.

---

## 2026-05-25 — Full Refresh Complété (snapshot 21:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm

Données strictement inchangées vs snapshot 17:00 UTC (cours $56.83, RSI 56.77, ATR $5.85, MM50 $46.10, scores 6.1/10 et 65.8/100). Marché fermé Memorial Day après clôture. Aucun nouveau flux post-earnings intégré (J=0, résultats non publiés). Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh complété et archivé.

---

## 2026-05-25 — Full Refresh Complété (snapshot 21:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm

Données strictement inchangées vs snapshot 17:00 UTC (cours $56.83, RSI 56.77, ATR $5.85, MM50 $46.10, scores 6.1/10 et 65.8/100). Marché fermé Memorial Day après clôture. Aucun nouveau flux post-earnings intégré (J=0, résultats non publiés). Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh complété et archivé.

---

## 2026-05-25 — Full Refresh Complété (snapshot 21:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm

Données strictement inchangées vs snapshot 17:00 UTC (cours $56.83, RSI 56.77, ATR $5.85, MM50 $46.10, scores 6.1/10 et 65.8/100). Marché fermé Memorial Day après clôture. Aucun nouveau flux post-earnings intégré (J=0, résultats non publiés). Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh complété et archivé.

---

## 2026-05-26 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm — duplicata de session, données strictement inchangées vs snapshot 21:00 UTC du 2026-05-25 (cours $56.83, RSI 56.77, ATR $5.85, MM50 $46.10, scores 6.1/10 et 65.8/100). Marché fermé Memorial Day, reprise attendue ce jour. Aucun nouveau flux post-earnings intégré (J=0, résultats non publiés). Anomalie options : Max Pain $20.00 (probable erreur de données), put/call et call OI indisponibles. Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh complété et archivé.

---

## 2026-05-26 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm — duplicata du FULL REFRESH complété précédemment ce jour. Données strictement inchangées. DRAFT_refresh archivé.

---

## 2026-05-26 — Full Refresh Complété (snapshot 13:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm

Données strictement inchangées vs snapshot 10:00 UTC du 2026-05-26 (cours $56.83, RSI 56.77, ATR $5.85, MM50 $46.10, scores 6.1/10 et 65.8/100). Correction de l'anomalie options : Max Pain $20.00 → $45.00, put/call ratio null → 3.16, call OI % null → 24.0%. La défiance options s'aggrave (put/call 3.16 vs 2.35 précédent, puts à 76.0%). Aucun nouveau flux post-earnings intégré (J=0, résultats non publiés). Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh complété et archivé.

---

## 2026-05-26 — Full Refresh Complété (snapshot 13:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 10.29% (seuil 5.0%)

**Conclusion :** confirm — duplicata du FULL REFRESH complété précédemment ce jour. Données strictement inchangées vs snapshot 10:00 UTC. Correction anomalie options confirmée. Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh archivé.

---

## 2026-05-26 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.47% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-26 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.54% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-26 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.19% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.50% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-26 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.19% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.50% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-27 — Full Refresh Complété

**Triggers :**
- price_gap (medium) : Gap +5.19% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.50% (seuil 5.0%)

**Conclusion :** confirm — duplicata du FULL REFRESH complété le 2026-05-26 (snapshot 21:00 UTC). Données strictement inchangées vs close précédent (cours $59.78, RSI 54.85, ATR $5.68, MM50 $46.46, scores 5.8/10 et 63.3/100). Aucun nouveau flux post-earnings intégré (J=0, résultats non publiés). Thèse confirmée : ACHETER sizing réduit. DRAFT_refresh complété et archivé (_ARCHIVED_DRAFT_refresh_2026-05-27_1.md).

---

## 2026-05-27 — Full Refresh Triggered (duplicata)

**Triggers :**
- price_gap (medium) : Gap +5.19% overnight (seuil ±5.0%) — duplicata
- atr_spike (medium) : ATR relatif 9.50% (seuil 5.0%) — duplicata

**Conclusion :** confirm — duplicata du FULL REFRESH complété précédemment ce jour. Données strictement inchangées. DRAFT_refresh archivé.

---

## 2026-05-27 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.19% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.50% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-27 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.19% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.50% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-27 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +6.73% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-27 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.77% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.55% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-27 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +13.47% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.54% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-27 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +13.48% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.53% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +13.48% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.53% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +13.48% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.53% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +13.48% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.53% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +13.48% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.53% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.54% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.58% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.62% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.75% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-28 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.59% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.59% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.59% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.59% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.59% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.33% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.47% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.27% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-29 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-30 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-05-31 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-01 — Full Refresh Complété

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** confirm — trigger ATR_SPIKE persistant depuis le 2026-05-20 (artefact de volatilité historique), pas de nouvel événement majeur. Données : cours $63.54 (−4.05% vs 27/05), RSI 52.36, ATR $5.26, MM50 $47.77. Forward P/E détérioré −67.60×. Score Opportunité 4.8/10, Score Global ajusté 53.0/100. Action ATTENDRE maintenue. Upside consensus restauré +4.8% ($66.61). Short Interest −2.15 pts à 14.72%. Anomalie Max Pain $20.00 (probable erreur). Aucun flux post-earnings Q1 2026 intégré. DRAFT_refresh complété et archivé (_ARCHIVED_DRAFT_refresh_2026-06-01_1.md). Fichier de référence : [IREN_2026-06-01_update.md](IREN_2026-06-01_update.md).

---

## 2026-06-01 — Full Refresh Triggered (duplicata)

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%) — duplicata

**Conclusion :** confirm — duplicata du FULL REFRESH complété précédemment ce jour. Données strictement inchangées. DRAFT_refresh archivé.

---

## 2026-06-01 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-01 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.28% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-01 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.69% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-01 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.63% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-01 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.70% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-01 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.68% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-02 — Full Refresh Complété (close officiel)

**Triggers :**
- atr_spike (medium) : ATR relatif 7.67% (seuil 5.0%)

**Conclusion :** confirm

Données close officiel : cours $66.60 (−1.04% vs snapshot 17h), RSI 61.11, ATR $5.11, MM50 $48.75. Le breakout intraday à $69.57 est rejeté en clôture sous le consensus PT ($66.60 vs $66.61). Volume total de session 51.26 M (0.9× moyenne 20j), corrigeant l’impression de faible participation du snapshot 17h. Score Opportunité 4.8/10 inchangé, Score Global ajusté 52.5/100 (−0.5 pt). Forward P/E −70.85× (amélioration marginale vs −71.60×). Structure options inchangée (put/call 2.09, puts 67.6%). Thèse confirmée : ATTENDRE. DRAFT_refresh complété et archivé (_ARCHIVED_DRAFT_refresh_2026-06-02_close.md). Fichier de référence : [IREN_2026-06-02_update.md](IREN_2026-06-02_update.md).

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.67% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.67% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.67% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.67% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.71% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 7.92% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.03% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-03 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.03% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.06% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.06% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.06% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 8.06% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.48% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.57% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -6.61% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.54% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-04 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.53% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 8.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.42% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.06% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.88% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.22% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.33% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.38% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-05 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-06 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-07 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** modifiée — DRAFT_refresh traité le 2026-06-08 (pipeline différé). Correction −12.14% confirmée.

---

## 2026-06-08 — Full Refresh Completed

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** MODIFIÉE favorablement

Le DRAFT_refresh a été complété par l'agent LLM. Correction majeure −18.4% vs close 03/06 ($66.60→$54.35). Consensus PT révisé à la hausse $69.12 (+27.2% upside, +3 analysts). RSI retourne zone neutre (51.49). MM50 respectée ($49.89, cours +8.9%). Multiples mécaniquement réduits (P/E 70.6×, EV/EBITDA 143.9×, P/B 7.0×). Action passée de ATTENDRE à ACHETER (Sizing Réduit). Score Global 61.8/100. Risques : corrélation BTC (beta 2.1), volatilité extrême (beta 4.232), FCF négatif. Fichier généré : `IREN_2026-06-08_init.md`. DRAFT_refresh archivé.

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +6.97% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.68% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.68% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.62% (seuil 5.0%)

**Conclusion :** confirm

Snapshot 17:00 UTC — Rebond +7.68% ($54.35 → $58.525) sur volume faible (0.41× moyenne). RSI 58.22, MM50 $50.31. Défiance options record persistante (put/call 3.95, puts 79.8%). Scores révisés (C 6.3, V 4.0, M 7.5). Score Global 61.8/100. Action ACHETER (Sizing Réduit) maintenue. Thèse confirmée. DRAFT_refresh complété et archivé (_ARCHIVED_DRAFT_refresh_IREN_2026-06-08_17h00.md). Fichier de référence : [IREN_2026-06-08_update.md](IREN_2026-06-08_update.md).

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.91% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-08 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.91% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.91% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.91% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.91% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +8.91% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -9.71% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.04% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-09 — Full Refresh Triggered (snapshot 17:00 UTC)

**Triggers :**
- price_gap (high) : Gap -11.65% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.59% (seuil 5.0%)

**Conclusion :** modify — traité dans l'update 17h00. Close $52.295, volume 33.21 M (0.65×), RSI 54.23, MM50 $50.67 testée (+3.2%). Thèse modifiée avec vigilance accrue. Voir entrée REFRESH_LOG du 2026-06-09 ligne 5.

---

## 2026-06-09 — Full Refresh Triggered (close officiel 21:00 UTC)

**Triggers :**
- price_gap (medium) : Gap -8.73% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 11.22% (seuil 5.0%)

**Conclusion :** confirm — close officiel corrige le snapshot 17h. Cours $54.02 (vs $52.295), volume 56.48 M (1.08× moyenne), RSI 56.02, MM50 $50.70 (+6.6%). Le rebond du low $51.145 vers $54.02 et le volume supérieur à la moyenne invalident la lecture "distribution silencieuse" du snapshot 17h. Structure options inchangée (put/call 2.22). Scores inchangés 5.7/10, Global 61.8/100. Action ACHETER (Sizing Réduit) confirmée. Thèse confirmée — vigilance accrue maintenue sur rejet high $60.86. DRAFT_refresh complété et archivé. Fichier de référence : [IREN_2026-06-09_update_21h00.md](IREN_2026-06-09_update_21h00.md).

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.33% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.45% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.75% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-10 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.74% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.98% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 11.09% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.11% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.77% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-11 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.07% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.77% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.07% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.77% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.07% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.77% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.07% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.77% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (high) : Gap +10.07% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.77% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.63% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +7.23% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.31% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.46% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-12 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-13 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-14 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap +5.40% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.49% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.05% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.97% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.16% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-15 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.16% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.16% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.16% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.16% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 10.16% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.60% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.61% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.83% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-16 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.82% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.82% (seuil 5.0%)

**Conclusion :** confirm — faux positif (trigger hérité du snapshot 10h UTC, données brutes strictement identiques)

Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).

> **Note :** Si cette entrée apparaît en duplicata, il s'agit de ré-exécutions du pipeline sur le même trigger.

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.82% (seuil 5.0%)

**Conclusion :** confirm — faux positif (trigger hérité du snapshot 10h UTC, données brutes strictement identiques)

Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).

> **Note :** Si cette entrée apparaît en duplicata, il s'agit de ré-exécutions du pipeline sur le même trigger.

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.82% (seuil 5.0%)

**Conclusion :** confirm — faux positif (trigger hérité du snapshot 10h UTC, données brutes strictement identiques)

Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).

> **Note :** Si cette entrée apparaît en duplicata, il s'agit de ré-exécutions du pipeline sur le même trigger.

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.82% (seuil 5.0%)

**Conclusion :** confirm — faux positif (trigger hérité du snapshot 10h UTC, données brutes strictement identiques)

Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).

> **Note :** Si cette entrée apparaît en duplicata, il s'agit de ré-exécutions du pipeline sur le même trigger.

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.82% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.62% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-17 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.48% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.54% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.58% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-18 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-19 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-20 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-21 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

---

## 2026-06-22 — Full Refresh Complété (snapshot 10:00 UTC)

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** confirm — faux positif (ATR stable vs 9.62% du 2026-06-17, volume institutionnel de retour massif)

Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-22T10:00:01 UTC). Les données brutes montrent un **retour massif du volume institutionnel** : 39.39 M (81.7% moyenne 20j) vs 15.69 M (33.1%) le 2026-06-17, soit +151%. Le cours à **$59.96** se tient à +11.1% au-dessus de la MM50 ($53.97). Le RSI est à **45.71** (zone neutre favorable). L'ATR est stable à **$5.75** (ATR relatif 9.59% vs 9.62% précédent) — le trigger est un faux positif sur une volatilité historique déjà intégrée. **Upgrade algorithmique majeur** : Score Global ajusté rehaussé de **56.8 à 61.8/100** (+5.0 pts), porté par le Score Momentum qui bondit de **5.5 à 7.5/10** (+2.0 pts). L'action passe de **ATTENDRE** à **ACHETER (Sizing Réduit)** avec timing **Favorable**. Anomalie options détectée : Max Pain $20.00, put/call null, call OI null — structure incohérente qui remplace la structure fiable du 17/06 (Max Pain $35.00, put/call 1.38, call OI 42.1%). La structure du 17/06 est conservée comme référence opérationnelle. Aucune news Yahoo ni mention Reddit n'accompagne le mouvement. Thèse modifiée favorablement : **ACHETER (Sizing Réduit)** (Score Global 61.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-22_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-22_DRAFT_refresh_archived.md`). Fichier de référence : [IREN_2026-06-22_update.md](IREN_2026-06-22_update.md).

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.59% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- atr_spike (medium) : ATR relatif 9.53% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.04% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.89% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.16% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-22 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-23 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---

## 2026-06-23 — Full Refresh Triggered

**Triggers :**
- price_gap (medium) : Gap -5.15% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 9.95% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---
