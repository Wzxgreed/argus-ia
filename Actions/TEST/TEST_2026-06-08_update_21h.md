# TEST — Mise à jour quotidienne (snapshot 21h UTC)

> **Date :** 2026-06-08
> **Type :** Mise à jour post-session 21h UTC (close officiel)
> **Source :** data/latest.json (snapshot 21:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-08 17h UTC | 2026-06-08 21h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | $44.63 | $45.3501 | **+1.61%** |
| Previous close | $43.527 | $43.527 | — |
| RSI 14j | 51.62 | 54.61 | **+2.99 pts** |
| MM 50j | $43.59 | $43.61 | +$0.02 |
| Volume session | 2,251 | 2,294 | +1.9% |
| Volume vs avg 20j | 0.89× | 0.90× | +0.01× |
| ATR 14j | $0.97 | $1.01 | +$0.04 |
| Score Global | 61.0 (66.0 ajusté) | 61.5 (66.5 ajusté) | **+0.5 pt** |
| Score Opportunité | 6.1/10 | 6.2/10 | +0.1 pt |
| Score Momentum | 7.3/10 | 7.5/10 | +0.2 pt |
| Verdict | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| SL | $42.69 | $43.33 | Révisé |
| TP | $47.54 | $48.38 | Révisé |

**Grignotage haussier en fin de séance.** Le ticker TEST progresse de +1.61% entre le snapshot 17h UTC et la clôture officielle 21h UTC, portant le gain total de la séance à +4.19% vs la veille ($43.527). Le RSI franchit 54 et se rapproche de la zone neutre haussière (55). Le volume reste stable mais faible (0.90× moyenne 20j), confirmant l'absence de conviction institutionnelle sur ce rebond. La volatilité remonte légèrement (ATR +$0.04).

---

## Mise à jour technique

- **Cours :** $45.3501, progression de +1.61% vs close 17h ($44.63) et +4.19% vs previous close ($43.527). Le high de session atteint $45.3501, soit un test du niveau de résistance psychologique $45.35.
- **Support clé :** MM50 à $43.61 — le cours laisse un cushion de +$1.74 (+4.0%) au-dessus de la moyenne. La dynamique de support reste solide à court terme.
- **RSI 14j :** 54.61, en hausse de 2.99 pts. Entrée dans la zone neutre favorable, à 0.4 pt de la zone surachat modérée (55). Le momentum technique est confirmé mais reste mesuré.
- **Volume :** 2,294, stable vs snapshot 17h (+1.9%) et 10% sous la moyenne 20j (2,534). Sur un rebond total de +4.19% sur la séance, ce volume faible est qualifié de **rebond sans conviction institutionnelle**. Pas de confirmation par les gros blocs.
- **ATR 14j :** $1.01 (+$0.04 vs 17h). La volatilité remonte légèrement, reste contenue.
- **Range 52 semaines :** $40.27–$57.74. Le cours se situe à 12.6% du low et 21.5% sous le high.

**Verdict timing :** Favorable. Cours au-dessus de MM50, RSI neutre-haussier, mais volume faible limite la certitude du suivi.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 21h UTC. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-08, source FMP) — résultats toujours non observables dans le snapshot 21h UTC. L'absence de données consolidées maintient un risque d'information asymétrique élevé. Tout résultat décevant publié post-close pourrait invalider le rebond à l'ouverture de la prochaine session.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-08, snapshot 21h UTC) :

| Axe | Score | Évolution vs 17h |
|-----|-------|-----------------|
| Catalyseur | 6.5/10 | Stable |
| Valorisation | 5.0/10 | Stable |
| Momentum | 7.5/10 | +0.2 pt |
| Opportunité | 6.2/10 | +0.1 pt |

**Modules agents (snapshot 21h UTC) :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-06-08) : aucun flag géopolitique pour TEST (score 2, exposé = false).
- `sector_rotation_latest.json` (2026-06-08) : signal NEUTRAL, régime UNKNOWN. TEST n'a pas de secteur assigné → pas d'alignement sectoriel à évaluer.
- `social_sentiment_latest.json` (2026-06-08) : 0 mention, sentiment "No data", pas de pump détecté.
- `fx_exposure_latest.json` (2026-06-08) : exposition FX 25%, impact score 0.0, divergence aligned. Aucun impact.
- `events_latest.json` (2026-06-08) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-08) : **earnings JOUR J** (2026-06-08, source FMP, days_until = 0). Résultats toujours non observables à 21h UTC.

---

## Nouveau scoring global

| Métrique | Valeur |
|----------|--------|
| Score Opportunité | 6.2/10 |
| Score Catalyseur | 6.5/10 |
| Score Valorisation | 5.0/10 |
| Score Momentum | 7.5/10 |
| Score Global | 61.5/100 |
| Score Global Ajusté | **66.5/100** |
| Verdict | **ACHETER (Réduit)** |
| Timing | Favorable |
| Horizon | 1–3 mois |

Le Score Global Ajusté 66.5/100 se maintient dans la fourchette **ACHETER (Réduit)** (60–74). La progression de +0.5 pt vs le snapshot 17h est entièrement portée par le Momentum (+0.2 pt) et la légère révision du composite Opportunité (+0.1 pt). Les axes Catalyseur et Valorisation sont stables, reflétant l'absence de nouvelles données fondamentales ou de catalyseurs exogènes.

---

## Révision des niveaux SL / TP

Révision à la hausse du cours entraînant un ajustement des niveaux :

| Niveau | Formule | Valeur |
|--------|---------|--------|
| Stop-loss | Cours - 2×ATR | $43.33 |
| Take-profit | Cours + 3×ATR | $48.38 |
| Ratio R/R | 2.97 / 2.02 | **1.5** |

Le ratio R/R reste stable à 1.5 malgré la remontée du cours, légèrement soutenu par l'augmentation de l'ATR (+$0.04).

---

## Conclusion — Thèse confirmée

**La thèse est CONFIRMÉE : ACHETER (Réduit).**

**Raisons de la confirmation :**
1. **Rebond technique consolidé** : +4.19% sur la séance complète, avec un grignotage haussier de +1.61% en fin de journée (17h → 21h). Le cours clôture au high de session ($45.3501), signal de faiblesse vendeuse en fin de séance.
2. **RSI progresse à 54.61** : à 0.4 pt de la zone surachat modérée (55), confirmant la réparation du momentum amorcée à 17h.
3. **MM50 confortablement au-dessus** : cushion de +$1.74 (+4.0%) au-dessus de la MM50 ($43.61). Le risque de cassure baissière immédiate est faible.
4. **Seuil de décision maintenu** : Score Global Ajusté 66.5/100 reste dans la fourchette ACHETER (Réduit) 60–74.

**Points de vigilance :**
- **Volume faible persistant** : 0.90× moyenne 20j sur un rebond de +4.19% = pas de conviction institutionnelle. Si le volume ne suit pas à la prochaine session, le rebond reste fragile.
- **Earnings JOUR J non résolu** (2026-06-08) — résultats toujours non observables à 21h UTC. Risque d'information asymétrique élevé. Tout résultat décevant post-close pourrait invalider le rebond à l'ouverture.
- **Données fondamentales absentes** : impossible d'évaluer la qualité du rebond sur des fondamentaux. Le signal reste purement technique à sizing réduit.
- Si clôture sous MM50 ($43.61) + volume < 0.5× moyenne → retour immédiat en SURVEILLER.
- Si clôture sous $43.33 (SL) → invalidation complète, passage ÉVITER.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 21h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*
