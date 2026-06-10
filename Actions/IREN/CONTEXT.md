# CONTEXT — IREN — Dernière mise à jour : 2026-06-10

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** SURVEILLER
- **Score global :** 44.3/100
- **Prix cible :** $69.12 (consensus FMP)
- **Stop-loss :** $41.90 (estimé, 2×ATR antérieur $6.06)
- **Statut thèse :** confirmée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

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

- **RSI 14j :** 62.18
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** 52267212
- **Max Pain :** $50.00 (exp 2026-06-12)
- **Put/Call :** 1.92
- **Call OI % :** 34.2%
- **Short Interest :** 16.05%

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-10 (snapshot 13h UTC — révision)
- **Type :** update
- **Fichier :** `IREN_2026-06-10_update.md`
- **Conclusion :** **Thèse : CONFIRMÉE — SURVEILLER** · Données brutes stables · Détente options majeure (Max Pain $50.00 vs $33.00, put/call 1.92 vs 2.22, call OI 34.2% vs 31.0%) · Score Global 44.3/100 inchangé · ATR/MM50/MM200 toujours indisponibles

---

## 🔄 Triggers détectés (full refresh)

- Le DRAFT_refresh a été déclenché automatiquement à 17:00 UTC par PRICE_GAP et ATR_SPIKE sur le snapshot `data/2026-06-09.json`. Les données révèlent une correction sévère de −11.65% en séance : cours $52.295 (vs $59.19 à 13h), high $60.86, low $51.145, range intraday 18.6%. Le rejet massif du high $60.86 et le close faible dégradent le momentum technique (RSI 54.23, MM50 $50.67 testée à +3.2%). Cependant, la valorisation s'améliore mécaniquement (P/E 67.86×, P/B 6.69×, upside consensus +32.2%). Les options restent inchangées (put/call 2.22, puts 69.0%), signalant que le marché options n'a pas réagi à la chute. Le Score Opportunité reste inchangé à 5.7/10 (Catalyseur 6.8, Valorisation 4.5, Momentum 6.0), le Score Global reste 61.8/100. L'action ACHETER (Sizing Réduit) est maintenue mais la thèse est modifiée avec vigilance accrue. La MM50 ($50.67) est désormais le niveau critique : si cassure sans rebond → réviser en ATTENDRE. DRAFT_refresh archivé. Analyse complète sauvegardée dans `IREN_2026-06-09_update.md` (snapshot 17:00 UTC).
- Le DRAFT_refresh a été déclenché automatiquement à 10:00 UTC par PRICE_GAP et ATR_SPIKE, mais les triggers sont hérités du mouvement du 2026-06-08 (previous close $54.35 → open $56.60 → close $59.19). Les données du snapshot 10:00 UTC du 9 juin sont strictement identiques au close officiel du 8 juin (cours $59.19, RSI 58.78, ATR $5.68, MM50 $50.32, volume ~41.0 M). Aucun nouvel événement majeur n'a eu lieu. DRAFT_refresh archivé. Anomalie détectée : `data/latest.json` retourne Max Pain $20.00 (incohérent) et put/call null — valeurs fiables maintenues : Max Pain $33.00, put/call 3.95, call OI 20.2%. Thèse confirmée ACHETER (Sizing Réduit) — Score Opportunité 5.7/10, Global 61.8/100.
- Le DRAFT_refresh a ete declenche automatiquement a 10:00 UTC par ATR_SPIKE, mais les donnees brutes sont strictement identiques au close officiel du 2026-06-02 (cours $66.60, RSI 61.11, ATR $5.11, MM50 $48.75, volume 51.34 M). L'ATR n'a pas change — le trigger est mecanique sur une volatilite historique deja integree. Le marché US etant ferme jusqu'a 14:30 UTC, aucun nouveau flux de marche n'est disponible. DRAFT_refresh archive. Anomalie detectee : `data/latest.json` retourne Max Pain $20.00 (incohérent) et put/call null — valeurs fiables maintenues : Max Pain $52.00, put/call 2.09, call OI 32.4%. These confirmee ATTENDRE (Score Opportunite 4.8/10, Global 52.5/100).

---

*Généré automatiquement — ne pas éditer manuellement.*
