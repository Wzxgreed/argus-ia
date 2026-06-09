# TEST — Mise à jour quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-09
> **Type :** Mise à jour pré-session 10h UTC
> **Source :** data/latest.json (snapshot 10:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-08 21h UTC | 2026-06-09 10h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | $45.3501 | $45.35 | **Stable** |
| Previous close | $43.527 | $43.527 | — |
| RSI 14j | 54.61 | 54.61 | **Stable** |
| MM 50j | $43.61 | $43.61 | **Stable** |
| Volume session | 2,294 | 2,400 | +4.6% |
| Volume vs avg 20j | 0.89× | 0.94× | +0.04× |
| ATR 14j | $1.01 | $1.01 | **Stable** |
| Score Global | 61.5 (66.5 ajusté) | 61.5 (66.5 ajusté) | **Stable** |
| Score Opportunité | 6.2/10 | 6.2/10 | Stable |
| Score Momentum | 7.5/10 | 7.5/10 | Stable |
| Verdict | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| SL | $43.33 | $43.33 | Stable |
| TP | $48.38 | $48.38 | Stable |

**Stabilité totale du snapshot matinal.** Le ticker TEST affiche une parfaite stabilité vs la clôture officielle du 8 juin ($45.3501 → $45.35, écart négligeable). Le RSI, la MM50 et l'ATR sont strictement inchangés. Le volume légèrement supérieur (+106 unités, 0.94× moyenne 20j) reste dans la fourchette de faible conviction institutionnelle. L'earnings JOUR J (2026-06-09) n'est toujours pas résolu dans le snapshot 10h UTC.

---

## Mise à jour technique

- **Cours :** $45.35, stable vs close 21h UTC du 8 juin ($45.3501). Le high/low du snapshot n'est pas renseigné (données pré-session).
- **Support clé :** MM50 à $43.61 — le cours laisse un cushion de +$1.74 (+4.0%) au-dessus de la moyenne. La dynamique de support reste inchangée et solide à court terme.
- **RSI 14j :** 54.61, inchangé. Positionnement dans la zone neutre favorable, à 0.4 pt de la zone surachat modérée (55). Le momentum technique est maintenu.
- **Volume :** 2,400, en légère hausse vs close 21h (+4.6%) mais toujours 5.5% sous la moyenne 20j (2,540). Sur un cours stable, ce volume modéré traduit une attente du marché avant l'événement earnings JOUR J.
- **ATR 14j :** $1.01, inchangé. Volatilité contenue.
- **Range 52 semaines :** $40.27–$57.74. Le cours se situe à 12.6% du low et 21.5% sous le high.

**Verdict timing :** Favorable. Cours au-dessus de MM50, RSI neutre-haussier, mais volume faible et attente pré-événement limitent la certitude du suivi.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 10h UTC. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-09, source FMP) — résultats toujours non observables dans le snapshot 10h UTC. L'absence de données consolidées maintient un risque d'information asymétrique élevé. Tout résultat décevant publié post-close pourrait invalider la thèse à l'ouverture de la prochaine session.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-09, snapshot 10h UTC) :

| Axe | Score | Évolution vs 21h 08/06 |
|-----|-------|---------------------|
| Catalyseur | 6.5/10 | Stable |
| Valorisation | 5.0/10 | Stable |
| Momentum | 7.5/10 | Stable |
| Opportunité | 6.2/10 | Stable |

**Modules agents (snapshot 10h UTC) :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-06-08) : aucun flag géopolitique pour TEST (score 2, exposé = false).
- `sector_rotation_latest.json` (2026-06-08) : signal NEUTRAL, régime UNKNOWN. TEST n'a pas de secteur assigné → pas d'alignement sectoriel à évaluer.
- `social_sentiment_latest.json` (2026-06-08) : 0 mention, sentiment "No data", pas de pump détecté.
- `fx_exposure_latest.json` (2026-06-08) : exposition FX 25%, impact score 0.0, divergence aligned. Aucun impact.
- `events_latest.json` (2026-06-08) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-09) : **earnings JOUR J** (2026-06-09, source FMP, days_until = 0). Résultats toujours non observables à 10h UTC.

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

Le Score Global Ajusté 66.5/100 se maintient dans la fourchette **ACHETER (Réduit)** (60–74). Aucune mutation détectée sur les 4 axes de scoring. L'absence de volatilité pré-session traduit une attente du marché face à l'événement earnings JOUR J.

---

## Révision des niveaux SL / TP

Aucune révision nécessaire — stabilité totale des niveaux :

| Niveau | Formule | Valeur |
|--------|---------|--------|
| Stop-loss | Cours - 2×ATR | $43.33 |
| Take-profit | Cours + 3×ATR | $48.38 |
| Ratio R/R | 2.97 / 2.02 | **1.5** |

---

## Conclusion — Thèse confirmée

**La thèse est CONFIRMÉE : ACHETER (Réduit).**

**Raisons de la confirmation :**
1. **Stabilité totale technique** : cours, RSI, MM50 et ATR strictement inchangés vs close 21h UTC du 8 juin. Aucune cassure de support, aucun signal de retournement.
2. **RSI maintenu à 54.61** : dans la zone neutre favorable, sans surchauffe ni survente.
3. **MM50 confortablement au-dessus** : cushion de +$1.74 (+4.0%) au-dessus de la MM50 ($43.61). Le risque de cassure baissière immédiate reste faible.
4. **Seuil de décision maintenu** : Score Global Ajusté 66.5/100 stable dans la fourchette ACHETER (Réduit) 60–74.

**Points de vigilance :**
- **Volume faible persistant** : 0.94× moyenne 20j, traduisant une attente pré-événement sans conviction institutionnelle. Si le volume ne suit pas post-earnings, le rebond reste fragile.
- **Earnings JOUR J non résolu** (2026-06-09) — résultats toujours non observables à 10h UTC. Risque d'information asymétrique élevé. Tout résultat décevant post-close pourrait invalider le rebond à l'ouverture.
- **Données fondamentales absentes** : impossible d'évaluer la qualité du rebond sur des fondamentaux. Le signal reste purement technique à sizing réduit.
- Si clôture sous MM50 ($43.61) + volume < 0.5× moyenne → retour immédiat en SURVEILLER.
- Si clôture sous $43.33 (SL) → invalidation complète, passage ÉVITER.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 10h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*
