# ASTS — Mise à Jour Snapshot 10:00 UTC (2026-05-20)

> Snapshot 10:00 UTC. Données quasi inchangées vs snapshot final 21:00 UTC du 2026-05-19. Cours stable à $88.10, RSI et ATR figés, volume soutenu. **Anomalie data quality détectée sur le Max Pain** ($40.0 vs $85.0 précédent). Thèse ATTENDRE confirmée.

---

## Résumé des Changements depuis l'Analyse Précédente

| Indicateur | Précédent (2026-05-19 21:00 UTC) | Actuel (2026-05-20 10:00 UTC) | Delta |
|-----------|----------------------------------|-------------------------------|-------|
| **Cours** | **$88.10** | **$88.10** | **0,00%** |
| RSI 14j | 63.39 | 63.39 | — |
| ATR 14j | $7.95 | $7.95 | — |
| MM50 | $83.62 | $83.62 | — |
| Volume rel. | 1.08x | **1.09x** | **+0.01x** |
| Market Cap | $34.19B | $34.19B | — |
| Forward P/E | −296.50 | −296.50 | — |
| P/B | 12.65 | 12.65 | — |
| Max Pain | $85.0 | **$40.0** | **[ANOMALIE]** |
| Put/Call Ratio | 0.59 | **null** | **[ANOMALIE]** |
| Call OI % | 63.0% | **null** | **[ANOMALIE]** |
| Score Opportunité | 5.0/10 | **5.0/10** | — |
| Score Global | 50.5 (ajusté 55.5) | **50.5 (ajusté 55.5)** | — |

**Verdict :** données quasi inchangées vs le snapshot final de la veille. Le cours $88.10 est inchangé, le RSI 63.39 et l'ATR $7.95 sont figés, confirmant que le snapshot 10:00 UTC reflète la clôture de la session précédente sans nouveau trading. Le volume relatif reste au-dessus de la moyenne 20j (1.09x). **Alerte data quality** : le Max Pain options est passé de $85.0 à $40.0, et les champs put/call ratio + call OI % sont désormais `null`. Ces valeurs sont aberrantes (Max Pain $40 avec le cours à $88.10 = écart de −54,6%) et probablement liées à un flux options interrompu ou corrompu. Les données options du snapshot précédent ($85.0, ratio 0.59, call OI 63%) restent la référence opérationnelle jusqu'à correction.

---

## Mise à Jour Technique

- **RSI 14j :** 63.39 — inchangé, zone neutre haussière, sous le seuil de surachat (70)
- **ATR 14j :** $7.95 (ATR relatif 9,02% du cours) — **[TRIGGER MEDIUM]** ATR_SPIKE persistant. Volatilité intraday extrême : le range de la session précédente était $78.66–$90.93 (~15,6%)
- **MM50 :** $83.62 — cours +5,3% au-dessus, support dynamique intact
- **MM200 :** N/A — croisement non confirmable
- **Volume :** 21,56M vs moy. 20j 19,86M (+8,6%) — volume soutenu au-dessus de la moyenne, stabilité du signal de liquidité
- **Supports clés :** MM50 $83.62 ; low intraday $78.66
- **Résistances clés :** High intraday $90.93 ; 52W high $129.89
- **Timing verdict :** Favorable (cours au-dessus MM50, RSI neutre haussier)
- **Score Momentum :** 6.8/10 — inchangé, momentum technique haussier court terme maintenu

---

## Mise à Jour Fondamentale

Aucune nouvelle donnée comptable ni révision d'estimations depuis le snapshot final 21:00 UTC du 2026-05-19.

- **Market Cap :** $34.19B
- **Forward P/E :** −296.50 (profil non rentable)
- **EV/EBITDA :** −84.90
- **EV/Revenue :** 316.28x — multiple spéculatif extrême
- **P/B :** 12.65x
- **Beta :** 2.60 — sensibilité au marché très supérieure à la moyenne
- **Short Interest :** 0.18% (très faible)
- **Consensus analystes :** Price target moyen $92.25 (10 analystes, 4 couverts le mois dernier) — upside +4,7% vs cours actuel $88.10
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, données comptables détaillées (M-Score, Z-Score, F-Score, Sloan) non disponibles dans le snapshot

**Risque sectoriel :** ASTS est classé dans Communication Equipment. L'Agent Sector Rotation place XLC (Communication Services) dans le **bottom 3** des secteurs (momentum score 0,0). Cette faiblesse sectorielle persiste et pèse sur le positionnement relatif.

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** aucun upgrade/downgrade signalé dans le pipeline du jour
- **Options :** **[ANOMALIE DATA QUALITY]** Max Pain affiché **$40.0** (vs $85.0 au snapshot précédent). Put/Call Ratio et Call OI % désormais `null`. Ces valeurs sont incohérentes avec le cours $88.10 et le contexte options du 19/05 (Max Pain $85.0, ratio 0.59, call OI 63%). **Hypothèse : flux options interrompu ou corruption de données.** Référence opérationnelle conservée : Max Pain $85.0, ratio 0.59, call OI 63% jusqu'à correction. Nearest expiry : **2026-05-22 (J+2)**
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False
- **Event-Driven :** aucun événement corporate (M&A, buyback, activism, guidance change) détecté pour ASTS
- **Géopolitique :** ASTS non flaggé dans geo_risk_latest.json
- **FX Exposure :** Exposition 25%, direction export, devise principale USD. FX Impact Score 0,0/10 — impact neutre

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+82) — Est. EPS $-0.29 à $-0.17, Revenus $0.0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-05-22** (J+2) — avec données options corrompues, le risque de pinning autour de $85 (données précédentes) reste à surveiller

---

## Scoring Global — Snapshot 10:00 UTC

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 5.0/10 | 35% | Aucun catalyseur imminent, earnings dans 82j |
| Valorisation | 4.0/10 | 40% | Multiples spéculatifs extrêmes, profil non rentable |
| Momentum | 6.8/10 | 25% | Cours > MM50, RSI neutre haussier, volume soutenu |
| **Score Opportunité** | **5.0/10** | | |

**Malus / Bonus appliqués :**
- Malus sectoriel (XLC bottom 3) : contexte défavorable pour le sous-secteur communication
- Malus ATR_SPIKE : volatilité intraday extrême (9,02% du cours), risque de whipsaw
- Malus range intraday extrême : $78.66–$90.93 (~15,6%) persistant
- Aucun malus comptable (données indisponibles)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite :** 50.5/100 (ajusté 55.5)

---

## Niveaux et Ratio R/R

- **Cours actuel :** $88.10
- **Stop-loss :** $72.20 (cours − 2×ATR = $88.10 − $15.90)
- **Take-profit :** $111.95 (cours + 3×ATR = $88.10 + $23.85)
- **Ratio R/R :** 1.5:1

**Révision :** niveaux inchangés — pas de mouvement de cours ni d'expansion de l'ATR depuis le snapshot précédent. Le SL à $72.20 reste sous le low intraday de la session précédente ($78.66) et la MM50 ($83.62).

---

## Conclusion

**Thèse confirmée : ATTENDRE — données stables, fondamentaux inchangés, anomalie options à surveiller**

Le snapshot 10:00 UTC du 2026-05-20 confirme le verdict **ATTENDRE** avec un Score Global ajusté stable à 55,5. Aucun changement significatif de cours, de momentum technique ou de fondamental depuis le snapshot final de la veille. Les données sont quasi identiques, indiquant que le marché n'a pas encore ouvert de nouvelle session au moment du fetch (ou que le cours de clôture du 19/05 a été répété).

**Alerte opérationnelle majeure :** le flux options a généré une anomalie flagrante (Max Pain $40.0, put/call et call OI `null`). Cette valeur est à ignorer en l'état. La référence reste le Max Pain $85.0 du 19/05 avec 2 jours avant expiration le 22 mai.

**Points de vigilance :**
1. **Anomalie data quality options** — Max Pain $40.0 aberrant (écart −54,6% vs cours), put/call et call OI null. Flux options probablement interrompu
2. **Expiration options 2026-05-22 (J+2)** — avec Max Pain $85.0 (données précédentes), le cours $88.10 reste au-dessus. Risque de pinning vers $85 si les market makers gèrent l'expiration
3. **ATR_SPIKE persistant** — ATR relatif 9,02% (seuil 5,0%). Volatilité intraday très élevée
4. **Secteur Communication Services** — bottom 3 du classement sectoriel (momentum 0,0)
5. **Profil non rentable** — EPS estimé négatif, multiples extrêmes, aucune visibilité sur la rentabilité

**Prochaines étapes :**
- Surveiller la correction de l'anomalie options au prochain snapshot
- Monitoring du comportement autour de $85 à l'approche de l'expiration du 22 mai
- Revoir le scoring si earnings preview à générer (dans ~80j)
- Attendre un repli vers MM50 ($83.62) ou mieux pour améliorer le ratio R/R avant toute entrée

---

*Généré par le système Argus-IA — Snapshot 2026-05-20 10:00 UTC*
