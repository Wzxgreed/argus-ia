# TEST — Mise à jour quotidienne (snapshot 17h UTC)

> **Date :** 2026-06-08
> **Type :** Mise à jour post-session 17h UTC
> **Source :** data/2026-06-08.json (snapshot 17:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-08 13h UTC | 2026-06-08 17h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | $43.527 | $44.63 | **+2.53%** |
| Previous close | $45.468 | $43.527 | — |
| RSI 14j | 41.19 | 51.62 | **+10.43 pts** |
| MM 50j | $43.54 | $43.59 | +$0.05 |
| Volume session | 5,000 | 2,251 | **−55%** |
| Volume vs avg 20j | 2.06× | 0.89× | **−1.17×** |
| ATR 14j | $0.97 | $0.97 | $0.00 |
| Score Global | 49.0 (36.0 ajusté) | 61.0 (66.0 ajusté) | **+12.0 pts** |
| Score Opportunité | 4.9/10 | 6.1/10 | +1.2 pt |
| Score Momentum | 2.5/10 | 7.3/10 | **+4.8 pts** |
| Verdict | SURVEILLER | **ACHETER (Réduit)** | — |
| SL | $41.59 | $42.69 | — |
| TP | $46.44 | $47.54 | — |

**Mutation technique majeure détectée.** Le ticker TEST rebondit de +2.53% à la clôture du snapshot 17h UTC, avec un RSI remonté de 10.4 pts à 51.62 — franchissement du seuil neutre 50 après avoir flirté avec la survente. Le cours repasse nettement au-dessus de la MM50 ($43.59 vs $44.63, écart +$1.04). Cependant, le volume s'effondre à 2,251 (0.89× moyenne 20j), signalant une absence de conviction institutionnelle sur ce rebond.

---

## Mise à jour technique

- **Cours :** $44.63, rebond de +2.53% vs close 13h ($43.527). Le low de session est resté à $44.04, sans retour sur le niveau précédent.
- **Support clé :** MM50 à $43.59 — le cours laisse désormais un cushion de +$1.04 (+2.4%) au-dessus de la moyenne. Le risque de franchissement à la baisse est atténué à court terme.
- **RSI 14j :** 51.62, en hausse de 10.4 pts. Sortie de la zone de survente (< 40) et retour dans le territoire neutre légèrement haussier. Le momentum technique est réparé mais reste sans élan fort (RSI < 55).
- **Volume :** 2,251, en effondrement de 55% vs snapshot 13h et 11% sous la moyenne 20j (2,532). Sur un rebond de +2.5%, ce volume faible est qualifié de **rebond sans conviction**. Pas de confirmation institutionnelle.
- **ATR 14j :** $0.97 (stable). La volatilité reste contenue.
- **Range 52 semaines :** $40.27–$57.74. Le cours se situe à 15.6% du low et 22.7% sous le high.

**Verdict timing :** Favorable. Cours au-dessus de MM50, RSI neutre, mais volume faible limite la certitude du suivi haussier.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 17h UTC. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-08, snapshot 17h UTC) :

| Axe | Score | Évolution vs 13h |
|-----|-------|-----------------|
| Catalyseur | 6.5/10 | Stable |
| Valorisation | 5.0/10 | Stable |
| Momentum | 7.3/10 | **+4.8 pts** |
| Opportunité | 6.1/10 | **+1.2 pt** |

**Modules agents (snapshot 17h UTC) :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-06-08) : aucun flag géopolitique pour TEST (score 2, exposé = false).
- `sector_rotation_latest.json` (2026-06-08) : signal NEUTRAL, régime UNKNOWN. TEST n'a pas de secteur assigné → pas d'alignement sectoriel à évaluer.
- `social_sentiment_latest.json` (2026-06-08) : 0 mention, sentiment "No data", pas de pump détecté.
- `fx_exposure_latest.json` (2026-06-08) : exposition FX 25%, impact score 0.0, divergence aligned. Aucun impact.
- `events_latest.json` (2026-06-08) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-08) : **earnings JOUR J** (2026-06-08, source fmp, days_until = 0). Résultats toujours non observables dans le snapshot 17h UTC.

---

## Révision des niveaux SL / TP

Révision à la hausse du cours entraînant un ajustement des niveaux :

| Niveau | Formule | Valeur |
|--------|---------|--------|
| Stop-loss | Cours - 2×ATR | $42.69 |
| Take-profit | Cours + 3×ATR | $47.54 |
| Ratio R/R | 2.91 / 1.94 | **1.5** |

Le ratio R/R reste stable à 1.5 malgré la remontée du cours, grâce à l'ATR inchangé.

---

## Conclusion — Thèse modifiée

**La thèse est MODIFIÉE : SURVEILLER → ACHETER (Réduit).**

**Raisons du réclassement :**
1. **Rebond technique confirmé** : +2.53% à la clôture 17h, avec un RSI remonté à 51.62 — sortie de la zone de survente et retour au-dessus du seuil neutre 50.
2. **MM50 récupérée** : le cours s'établit à $44.63, soit +$1.04 au-dessus de la MM50 ($43.59). Le risque de cassure baissière est temporairement levé.
3. **Momentum réparé** : Score Momentum bondit de 2.5 à 7.3/10, tirant le Score Opportunité de 4.9 à 6.1/10 et le Score Global de 49.0 à 61.0/100.
4. **Seuil de décision franchi** : Score Global ajusté 66.0 ≥ 60 → conformité avec la règle ACHETER (Réduit).

**Points de vigilance :**
- **Volume faible** : 0.89× moyenne 20j sur le rebond = pas de conviction institutionnelle. Si le volume ne suit pas à la prochaine session, le rebond est fragile.
- **Earnings JOUR J** (2026-06-08) — résultats toujours non observables. L'absence de données consolidées à 17h UTC maintient un risque d'information asymétrique élevé. Tout résultat décevant pourrait invalider le rebond immédiatement.
- **Données fondamentales absentes** : impossible d'évaluer la qualité du rebond sur des fondamentaux. Le signal reste purement technique.
- Si clôture sous MM50 ($43.59) + volume < 0.5× moyenne → retour immédiat en SURVEILLER.
- Si clôture sous $42.69 (SL) → invalidation complète, passage ÉVITER.

---

*Format institutionnel JPM/GS/MS — Données : data/2026-06-08.json (snapshot 17h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*
