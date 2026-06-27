# CONTEXT — IREN — Dernière mise à jour : 2026-06-27

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** —
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- **2026-05-17** · earnings · Miss / Imprécis · Ligne:  | 2026-05-17 | IREN | `_init.md` | ATTENDRE | $65.86

---

## 🚨 Alertes actives

- Baisse — $45.00 — 🟢 Active
- Hausse — $65.86 — 🟢 Active
- Volume — >2× moy. 20j (>104.9M) — 🟢 Active
- IREN — Vérification — $61.20
- IREN — **⚠️ Volume DÉCLENCHÉ** — $55.15 (close)
- IREN — **⚠️ Baisse INTRADAY** — $52.36 (low)

---

## 📅 Prochains événements

- Aucun événement à venir.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 41.45
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** 44784134

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-26
- **Type :** full refresh
- **Fichier :** `IREN_2026-06-26_DRAFT_refresh.md`
- **Conclusion :** > **Date :** 2026-06-26

---

## 🔄 Triggers détectés (full refresh)

- Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-23T10:00:01 UTC). Les données brutes sont **strictement identiques** au snapshot 21h UTC du 2026-06-22 (cours $56.87, RSI 40.17, ATR $5.66, MM50 $54.37, volume 34.93 M, scores 4.9/10 et 54.3/100). Aucun nouvel événement majeur n'a eu lieu. **Anomalie options détectée** : Max Pain $20.00, put/call null, call OI 0.0% — structure incohérente qui remplace la structure fiable du 22/06 (Max Pain $40.00, put/call 4.99, call OI 16.7%). La structure du 22/06 est conservée comme référence opérationnelle. Thèse confirmée : **ATTENDRE** (Score Global 54.3/100). DRAFT_refresh complété et archivé (`IREN_2026-06-23_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-23_DRAFT_refresh_archived.md`). Fichier de référence : [IREN_2026-06-23_update.md](IREN_2026-06-23_update.md).
- Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-23T13:00:01 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-23 (cours $56.87, RSI 40.17, ATR $5.66, MM50 $54.37, volume 34.93 M, scores 4.9/10 et 54.3/100). **Correction options majeure** : Max Pain $40.00 (vs $20.00 anomalie 10h UTC), put/call 3.67 (vs null), call OI 21.4% (vs null) — structure cohérente rétablie avec détente marginale vs référence 22/06 (put/call 4.99 → 3.67, call OI 16.7% → 21.4%). Thèse confirmée : **ATTENDRE** (Score Global 54.3/100). DRAFT_refresh complété et archivé (`IREN_2026-06-23_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-23_13h00.md`). Fichier de référence : [IREN_2026-06-23_update_13h00.md](IREN_2026-06-23_update_13h00.md).
- Le DRAFT_refresh a été déclenché automatiquement à 17:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T17:00:07 UTC). Les données brutes montrent une **stabilité mécanique totale** par rapport au snapshot 13h UTC : cours **$59.54** (+0.61%), ATR **$5.73** (−$0.08 vs 13h), MM50 **$53.54** (+$0.48), options stables (Max Pain $35.00, put/call 1.38, call OI 42.1%). Le seul mouvement significatif est l'**effondrement du volume** à **15.69 M** (33.1% de la moyenne 20j vs 65.9% à 13h), interprété comme un désengagement institutionnel ou une attitude d'attente pré-expiration du 18/06. Le RSI remonte à **44.32** (+4.36 pts), sortant de la zone 40. Les scores sont **strictement identiques** au snapshot 13h (Opportunité 5.2/10, Global 56.8/100). L'action reste **ATTENDRE**. Le trigger ATR_SPIKE est un **faux positif** (même configuration héritée du pipeline, ATR en repli). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_17h00.md`). Fichier de référence : [IREN_2026-06-17_update_17h00.md](IREN_2026-06-17_update_17h00.md).
- Le DRAFT_refresh a été déclenché automatiquement à 17:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-16T17:00:07 UTC). Les données brutes ont été **révisées par Yahoo Finance** : open corrigé à **$59.99** (−$2.33 vs $62.32 à 13h), high à **$62.02** (−$1.15), low à **$59.05** (−$1.29), previous_close corrigé à **$60.85** (vs $59.77 erroné à 13h). Le cours à **$60.335** représente un repli de **−0.85%** vs le close corrigé du 15/06. Le RSI a chuté de **51.08 à 41.06** (−10.02 pts), signalant une accélération de la pression vendeuse intra-session. Le Score Momentum est dégradé de **7.3 à 5.5/10** (−1.8 pt), entraînant une baisse du Score Global ajusté de **57.5 à 53.0/100** (−4.5 pts). L'action reste **ATTENDRE**. La structure options reste inchangée et cohérente (Max Pain $35.00, put/call 1.44, call OI 41.0%). Volume très faible (16.82 M = 35.2% moyenne 20j à 17h UTC, session en cours). DRAFT_refresh complété et archivé (`IREN_2026-06-16_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-16_17h00.md`). Fichier de référence : [IREN_2026-06-16_update_17h00.md](IREN_2026-06-16_update_17h00.md).
- Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par ATR_SPIKE sur le snapshot `data/2026-06-16.json`. Les données brutes sont **strictement identiques** au snapshot 21h UTC du 2026-06-15 (cours $60.85, RSI 51.08, ATR $6.18, MM50 $52.58, volume 33.08 M, scores 5.3/10 et 57.5/100). Aucun nouvel événement majeur n'a eu lieu. Le marché est fermé ou les données pre-market n'ont pas évolué. **Anomalie options détectée** : Max Pain $100.00, put/call null, call OI 0.0% — structure incohérente qui remplace la structure fiable du 15/06 (Max Pain $40.00, put/call 1.62, call OI 38.1%). La structure du 15/06 est conservée comme référence opérationnelle. Thèse confirmée : **ATTENDRE** (Score Global 57.5/100). DRAFT_refresh complété et archivé (`IREN_2026-06-16_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-16.md`). Fichier de référence : [IREN_2026-06-16_update.md](IREN_2026-06-16_update.md).
- Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/2026-06-15.json`. Les données révèlent un upgrade algorithmique majeur : Score Global ajusté rehaussé de **44.3 à 61.8/100** (+17.5 pts), porté par une amélioration simultanée des trois axes (Catalyseur 6.3/10, Valorisation 4.0/10, Momentum 7.5/10). L'action passe de **SURVEILLER** à **ACHETER (Sizing Réduit)** avec timing **Favorable**. Les données techniques manquantes depuis le 2026-06-08 sont rétablies : ATR **$6.27**, MM50 **$52.06**. Le cours à **$59.77** se tient à +14.8% au-dessus de la MM50, confirmant la tendance haussière intermédiaire. Le RSI se normalise à **52.86** (neutre), favorable à l'entrée. Les multiples se dégradent mécaniquement (P/E 77.62×, EV/EBITDA 157.04×) sans nouvelle fondamentale. Les valeurs options du snapshot sont corrompues (Max Pain $100.00, put/call null) — les dernières valeurs fiables restent celles du 10/06. Aucune news Yahoo ni mention Reddit n'accompagne le mouvement, qui est purement technique/algorithmique. DRAFT_refresh archivé (`IREN_2026-06-15_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-15_DRAFT_refresh_archived.md`). Analyse complète sauvegardée dans `IREN_2026-06-15_update.md` (snapshot 10:00 UTC).
- Le DRAFT_refresh a été déclenché automatiquement à 17:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/2026-06-09.json`. Les données révèlent une correction sévère de −11.65% en séance : cours $52.295 (vs $59.19 à 13h), high $60.86, low $51.145, range intraday 18.6%. Le rejet massif du high $60.86 et le close faible dégradent le momentum technique (RSI 54.23, MM50 $50.67 testée à +3.2%). Cependant, la valorisation s'améliore mécaniquement (P/E 67.86×, P/B 6.69×, upside consensus +32.2%). Les options restent inchangées (put/call 2.22, puts 69.0%), signalant que le marché options n'a pas réagi à la chute. Le Score Opportunité reste inchangé à 5.7/10 (Catalyseur 6.8, Valorisation 4.5, Momentum 6.0), le Score Global reste 61.8/100. L'action ACHETER (Sizing Réduit) est maintenue mais la thèse est modifiée avec vigilance accrue. La MM50 ($50.67) est désormais le niveau critique : si cassure sans rebond → réviser en ATTENDRE. DRAFT_refresh archivé. Analyse complète sauvegardée dans `IREN_2026-06-09_update.md` (snapshot 17:00 UTC).
- Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par PRICE_GAP et ATR_SPIKE, mais les triggers sont hérités du mouvement du 2026-06-08 (previous close $54.35 → open $56.60 → close $59.19). Les données du snapshot 10:00 UTC du 9 juin sont strictement identiques au close officiel du 8 juin (cours $59.19, RSI 58.78, ATR $5.68, MM50 $50.32, volume ~41.0 M). Aucun nouvel événement majeur n'a eu lieu. DRAFT_refresh archivé. Anomalie détectée : `data/latest.json` retourne Max Pain $20.00 (incohérent) et put/call null — valeurs fiables maintenues : Max Pain $33.00, put/call 3.95, call OI 20.2%. Thèse confirmée ACHETER (Sizing Réduit) — Score Opportunité 5.7/10, Global 61.8/100.
- Le DRAFT_refresh a ete declenche automatiquement a 10:00 UTC par ATR_SPIKE, mais les donnees brutes sont strictement identiques au close officiel du 2026-06-02 (cours $66.60, RSI 61.11, ATR $5.11, MM50 $48.75, volume 51.34 M). L'ATR n'a pas change — le trigger est mecanique sur une volatilite historique deja integree. Le marché US etant ferme jusqu'a 14:30 UTC, aucun nouveau flux de marche n'est disponible. DRAFT_refresh archive. Anomalie detectee : `data/latest.json` retourne Max Pain $20.00 (incohérent) et put/call null — valeurs fiables maintenues : Max Pain $52.00, put/call 2.09, call OI 32.4%. These confirmee ATTENDRE (Score Opportunite 4.8/10, Global 52.5/100).
- Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).
- Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).
- Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).
- Le DRAFT_refresh a été déclenché automatiquement à 13:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-17T13:00:07 UTC). Les données brutes sont **strictement identiques** au snapshot 10h UTC du 2026-06-17 (cours $59.18, RSI 39.96, ATR $5.81, MM50 $53.06, volume 32.00 M, scores 5.2/10 et 56.8/100). Aucun nouvel événement majeur n'a eu lieu. **Correction anomalie options** : Max Pain rétabli à **$35.00** (vs $5.00 aberrant à 10h), put/call **1.38** (vs null), call OI **42.1%** (vs 0.0%). La structure options est désormais cohérente et fiable dans `latest.json`. Thèse confirmée : **ATTENDRE** (Score Global 56.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-17_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-17_13h00.md`). Fichier de référence : [IREN_2026-06-17_update_13h00.md](IREN_2026-06-17_update_13h00.md).
- Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par ATR_SPIKE sur le snapshot `data/latest.json` (fetched_at 2026-06-22T10:00:01 UTC). Les données brutes montrent un **retour massif du volume institutionnel** : 39.39 M (81.7% moyenne 20j) vs 15.69 M (33.1%) le 2026-06-17, soit +151%. Le cours à **$59.96** se tient à +11.1% au-dessus de la MM50 ($53.97). Le RSI est à **45.71** (zone neutre favorable). L'ATR est stable à **$5.75** (ATR relatif 9.59% vs 9.62% précédent) — le trigger est un faux positif sur une volatilité historique déjà intégrée. **Upgrade algorithmique majeur** : Score Global ajusté rehaussé de **56.8 à 61.8/100** (+5.0 pts), porté par le Score Momentum qui bondit de **5.5 à 7.5/10** (+2.0 pts). L'action passe de **ATTENDRE** à **ACHETER (Sizing Réduit)** avec timing **Favorable**. Anomalie options détectée : Max Pain $20.00, put/call null, call OI null — structure incohérente qui remplace la structure fiable du 17/06 (Max Pain $35.00, put/call 1.38, call OI 42.1%). La structure du 17/06 est conservée comme référence opérationnelle. Aucune news Yahoo ni mention Reddit n'accompagne le mouvement. Thèse modifiée favorablement : **ACHETER (Sizing Réduit)** (Score Global 61.8/100). DRAFT_refresh complété et archivé (`IREN_2026-06-22_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-22_DRAFT_refresh_archived.md`). Fichier de référence : [IREN_2026-06-22_update.md](IREN_2026-06-22_update.md).

---

*Généré automatiquement — ne pas éditer manuellement.*
