# IREN — Historique des Full Refreshes

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
- price_gap (high) : Gap -12.14% overnight (seuil ±5.0%)
- atr_spike (medium) : ATR relatif 10.36% (seuil 5.0%)

**Conclusion :** [À compléter après analyse LLM]

---
