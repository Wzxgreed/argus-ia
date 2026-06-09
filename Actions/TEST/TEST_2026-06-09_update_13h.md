# TEST — Mise à jour quotidienne (snapshot 13h UTC)

> **Date :** 2026-06-09
> **Type :** Mise à jour post-session 13h UTC
> **Source :** data/latest.json (snapshot 13:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-09 10h UTC | 2026-06-09 13h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | $45.35 | $45.35 | **Stable** |
| Open | — | $44.03 | *Nouveau* |
| High | — | $45.35 | *Nouveau* |
| Low | — | $44.03 | *Nouveau* |
| Previous close | $43.527 | $43.527 | — |
| Variation vs previous | — | **+4.19%** | *Nouveau* |
| Variation open→close | — | **+3.00%** | *Nouveau* |
| RSI 14j | 54.61 | 54.61 | **Stable** |
| MM 50j | $43.61 | $43.61 | **Stable** |
| Volume session | 2,400 | 2,400 | **Stable** |
| Volume vs avg 20j | 0.94× | 0.94× | **Stable** |
| ATR 14j | $1.01 | $1.01 | **Stable** |
| Score Global | 61.5 (66.5 ajusté) | 61.5 (66.5 ajusté) | **Stable** |
| Score Opportunité | 6.2/10 | 6.2/10 | Stable |
| Score Momentum | 7.5/10 | 7.5/10 | Stable |
| Verdict | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| SL | $43.33 | $43.33 | Stable |
| TP | $48.38 | $48.38 | Stable |

**Stabilité technique confirmée avec nouvelle granularité intraday.** Le snapshot 13h UTC confirme la clôture à $45.35, inchangée vs le snapshot 10h UTC. Les données pré-session ont été enrichies : le titre a ouvert à $44.03, a grimpé en séance jusqu'à $45.35 (high = close), soit une performance intraday de +3.00% et une variation de +4.19% vs le previous close ($43.527). Le RSI, la MM50 et l'ATR restent strictement inchangés. Le volume persiste à 2,400 unités (0.94× moyenne 20j), dans la fourchette de faible conviction. L'earnings JOUR J (2026-06-09, source FMP) demeure non résolu.

---

## Mise à jour technique

- **Cours :** $45.35, stable vs snapshot 10h UTC. **Open :** $44.03, **High :** $45.35, **Low :** $44.03.
- **Performance intraday :** +$1.32 (+3.00%) depuis l'open. Le close égale le high de session — signe d'une clôture en haut de fourchette, mais sur un volume très faible.
- **Performance vs previous close :** +$1.823 (+4.19%). Ce rebond post-session du 8 juin est maintenant pleinement intégré dans le snapshot 13h.
- **Support clé :** MM50 à $43.61 — cushion maintenu à +$1.74 (+4.0%).
- **RSI 14j :** 54.61, inchangé. Zone neutre favorable.
- **Volume :** 2,400 (0.94× moyenne 20j). Le volume n'a pas suivi le mouvement haussier intraday : aucune accélération institutionnelle détectée. Sur un écart de +3.00%, un volume au moins égal à la moyenne 20j aurait validé la conviction.
- **ATR 14j :** $1.01, inchangé. Volatilité contenue.
- **Range 52 semaines :** $40.27–$57.74. Le cours se situe à 12.6% du low et 21.5% sous le high.

**Verdict timing :** Favorable. Cours au-dessus de MM50, RSI neutre-haussier, clôture en haut de fourchette, mais volume insuffisant pour confirmer un réel appétit institutionnel.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 13h UTC. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-09, source FMP) — résultats toujours non observables dans le snapshot 13h UTC. Le ticker n'a pas publié de résultats post-close à ce stade. Risque d'information asymétrique maintenu.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-09, snapshot 13h UTC) :

| Axe | Score | Évolution vs 10h 09/06 |
|-----|-------|---------------------|
| Catalyseur | 6.5/10 | Stable |
| Valorisation | 5.0/10 | Stable |
| Momentum | 7.5/10 | Stable |
| Opportunité | 6.2/10 | Stable |

**Modules agents (snapshot 13h UTC) :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-06-08) : aucun flag géopolitique pour TEST (score 2, exposé = false).
- `sector_rotation_latest.json` (2026-06-09) : signal NEUTRAL, régime UNKNOWN. TEST n'a pas de secteur assigné → pas d'alignement sectoriel à évaluer.
- `social_sentiment_latest.json` (2026-06-09) : 0 mention, sentiment "No data", pas de pump détecté.
- `fx_exposure_latest.json` (2026-06-09) : exposition FX 25%, impact score 0.0, divergence aligned. Aucun impact.
- `events_latest.json` (2026-06-09) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-09) : **earnings JOUR J** (2026-06-09, source FMP, days_until = 0). Résultats toujours non observables à 13h UTC.

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

Le Score Global Ajusté 66.5/100 se maintient dans la fourchette **ACHETER (Réduit)** (60–74). Aucune mutation détectée sur les 4 axes de scoring. Le mouvement intraday de +3.00% (open→close) est technique et non confirmé par le volume, ce qui justifie le maintien du sizing réduit.

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
1. **Stabilité technique globale** : close, RSI, MM50 et ATR strictement inchangés vs snapshot 10h UTC. Aucune cassure de support, aucun signal de retournement.
2. **Grille de prix enrichie** : le snapshot 13h révèle un open à $44.03 et une clôture en haut de fourchette ($45.35 = high). Le mouvement intraday de +3.00% est haussier, bien que non validé par le volume.
3. **RSI maintenu à 54.61** : dans la zone neutre favorable, sans surchauffe ni survente.
4. **MM50 confortablement au-dessus** : cushion de +$1.74 (+4.0%) au-dessus de la MM50 ($43.61). Le risque de cassure baissière immédiate reste faible.
5. **Seuil de décision maintenu** : Score Global Ajusté 66.5/100 stable dans la fourchette ACHETER (Réduit) 60–74.

**Points de vigilance :**
- **Volume faible persistant** : 2,400 unités (0.94× moyenne 20j). Le rebond intraday de +3.00% n'est pas accompagné d'une accélération volume, ce qui affaiblit la conviction institutionnelle. Si un tel mouvement se produit sur volume < moyenne, il peut refléter une micro-cap illiquide ou des ordres de faible taille.
- **Earnings JOUR J non résolu** (2026-06-09) — résultats toujours non observables à 13h UTC. Risque d'information asymétrique élevé. Tout résultat décevant post-close pourrait invalider le rebond à l'ouverture de la prochaine session.
- **Données fondamentales absentes** : impossible d'évaluer la qualité du rebond sur des fondamentaux. Le signal reste purement technique à sizing réduit.
- Si clôture sous MM50 ($43.61) + volume < 0.5× moyenne → retour immédiat en SURVEILLER.
- Si clôture sous $43.33 (SL) → invalidation complète, passage ÉVITER.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 13h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*
