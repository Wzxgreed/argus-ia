# TEST — Mise à jour quotidienne (snapshot 21h UTC)

> **Date :** 2026-06-09
> **Type :** Mise à jour post-session 21h UTC
> **Source :** data/latest.json (snapshot 21:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-09 17h UTC | 2026-06-09 21h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | $42.97 | **$43.87** | **+$0.90 (+2.10%)** 🟢 |
| Open | $43.31 | $43.31 | — |
| Previous close | $45.35 | $45.35 | — |
| Variation vs previous | −5.25% | **−3.25%** | **+2.00 pts** 🟢 |
| RSI 14j | 47.10 | **50.48** | **+3.38 pts** 🟢 |
| MM 50j | $43.65 | $43.67 | +$0.02 |
| Écart cours / MM50 | −$0.68 (−1.6%) | **+$0.20 (+0.5%)** | **Reclaim** 🟢 |
| Volume session | 1,217 | **1,570** | **+29.0%** 🟢 |
| Volume vs avg 20j | 0.50× | **0.64×** | +0.14× |
| ATR 14j | $1.07 | $1.07 | Stable |
| Score Global | 52.8 (44.8 ajusté) | **59.0 (64.0 ajusté)** | **+6.2 pts (+19.2 pts ajusté)** 🟢 |
| Score Opportunité | 5.3/10 | **5.9/10** | **+0.6 pt** 🟢 |
| Score Momentum | 4.0/10 | **6.5/10** | **+2.5 pts** 🟢 |
| Verdict | SURVEILLER | **ACHETER (Réduit)** | **Regradation** 🟢 |
| SL | $40.83 | **$41.73** | +$0.90 |
| TP | $46.18 | **$47.08** | +$0.90 |

**Mutation technique favorable.** Le snapshot 21h UTC enregistre une clôture à $43.8744, en rebond de +2.10% vs le snapshot 17h UTC ($42.97) et réduction du repli vs previous close à −3.25% (vs −5.25% à 17h). Le titre a ouvert à $43.31, testé le low à $42.97 (niveau du close 17h) puis rebondi pour clôturer au high de la fourchette intraday ($43.8744 = high), suggérant un regain d'appétit acheteur en fin de session. Le RSI remonte de 3.38 pts à 50.48, **franchissant à nouveau le seuil de 50** et repassant en territoire neutre légèrement haussier. La MM50 ($43.67) est désormais sous le cours, avec un écart positif de +$0.20 (+0.5%) — **reclaim technique du support mobile 50j confirmé**. Le volume reste contraint à 1,570 unités (0.64× moyenne 20j), en légère hausse vs 17h (+29.0%) mais toujours indiquant une faible participation institutionnelle.

---

## Mise à jour technique

- **Cours :** $43.87, en rebond de +$0.90 (+2.10%) vs snapshot 17h UTC. **Open :** $43.31, **Low :** $42.97, **High :** $43.8744 = close.
- **Performance intraday :** clôture au high de fourchette — pattern de rebond en « hammer » inversé confirmé par le close au sommet.
- **Support clé :** MM50 à $43.67 — **reclaim confirmé** avec écart positif de +$0.20 (+0.5%).
- **Support suivant :** low 52 semaines à $40.27 (écart de −8.3%). Le SL de l'agent reco ($41.73) se situe à $1.46 au-dessus de ce niveau critique.
- **RSI 14j :** 50.48, en hausse de 3.38 pts. Repassage au-dessus de 50 : momentum neutre-haussier réactivé.
- **Volume :** 1,570 (0.64× moyenne 20j). Léger regain de volume sur la session de rebond (+29% vs 17h), mais toujours très en dessous de la moyenne. Risque de faux signal amplifié par la microstructure illiquide persistante.
- **ATR 14j :** $1.07 (inchangé vs 17h). Volatilité stabilisée.
- **Range 52 semaines :** $40.27–$57.74. Le cours se situe à 8.3% du low et 24.0% sous le high.

**Verdict timing :** Favorable. Reclaim de MM50, RSI au-dessus de 50, clôture au high de fourchette. Signal technique de rebond confirmé, bien que sur volume faible.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 21h UTC. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-09, source FMP) — résultats toujours non observables dans le snapshot 21h UTC. Après plus de 9 jours de flag « JOUR J » sans publication, l'hypothèse d'un artefact de calendrier FMP se renforce. Toutefois, le risque d'information asymétrique persiste tant qu'aucune résolution n'est confirmée.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-09, snapshot 21h UTC) :

| Axe | Score 17h | Score 21h | Δ |
|-----|-----------|-----------|---|
| Catalyseur | 6.5/10 | 6.5/10 | Stable |
| Valorisation | 5.0/10 | 5.0/10 | Stable |
| Momentum | 4.0/10 | **6.5/10** | **+2.5 pts** 🟢 |
| Opportunité | 5.3/10 | **5.9/10** | **+0.6 pt** 🟢 |

**Modules agents (snapshot 21h UTC) :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-05-17) : aucun flag géopolitique pour TEST.
- `sector_rotation_latest.json` (2026-06-09) : régime UNKNOWN, signal NEUTRAL. TEST sans secteur assigné.
- `social_sentiment_latest.json` (2026-06-09) : 0 mention, sentiment « No data », pas de pump.
- `fx_exposure_latest.json` (2026-06-09) : exposition FX 25%, impact score 0.0, divergence aligned.
- `events_latest.json` (2026-06-09) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-09) : earnings JOUR J (2026-06-09, source FMP, days_until = 0) — toujours non résolu.

---

## Nouveau scoring global

| Métrique | Valeur |
|----------|--------|
| Score Opportunité | 5.9/10 |
| Score Catalyseur | 6.5/10 |
| Score Valorisation | 5.0/10 |
| Score Momentum | **6.5/10** 🟢 |
| Score Global | 59.0/100 |
| Score Global Ajusté | **64.0/100** 🟢 |
| Verdict | **ACHETER (Réduit)** |
| Timing | Favorable |
| Horizon | 1–3 mois |

Le Score Global Ajusté est passé de 44.8/100 à **64.0/100**, réintégrant la fourchette **ACHETER (Réduit)** (60–74). L'amélioration est entièrement portée par la remontée du Score Momentum (+2.5 pts, de 4.0 à 6.5) consécutive au reclaim de MM50 et au passage du RSI au-dessus de 50. Les axes Catalyseur et Valorisation sont stables. La règle de disqualification n'est pas activée (aucun score ≤ 2/10).

---

## Révision des niveaux SL / TP

Révision obligatoire suite au nouveau cours et au rebascullement de verdict :

| Niveau | Ancien (17h) | Nouveau (21h) | Formule agent reco |
|--------|--------------|---------------|--------------------|
| Stop-loss | $40.83 | **$41.73** | Cours − 2×ATR |
| Take-profit | $46.18 | **$47.08** | Cours + 3×ATR |
| Ratio R/R | 1.5 | **1.5** | 3.21 / 2.14 |

**Alerte :** le nouveau SL ($41.73) se sitve à $1.46 au-dessus du low 52 semaines ($40.27). Une cassure sous $40.27 invaliderait structurellement la configuration et justifierait un passage à **ÉVITER**.

---

## Conclusion — Thèse modifiée

**La thèse est MODIFIÉE : passage SURVEILLER → ACHETER (Réduit).**

**Raisons de la modification :**
1. **Reclaim de MM50** : le cours a rebondi pour clôturer au-dessus de la moyenne mobile 50j ($43.67) avec un close de $43.87. C'est le premier signal de récupération du support mobile depuis la cassure de 17h UTC.
2. **RSI au-dessus de 50** : à 50.48, le momentum est repassé en territoire neutre-haussier. Le regain de 3.38 pts en quelques heures confirme la présence d'acheteurs en fin de session.
3. **Clôture au high de fourchette** : le titre a clôturé à son high intraday ($43.8744), formant un pattern de rebond technique favorable.
4. **Score Global Ajusté regradé** : de 44.8 à 64.0, réintégration de la fourchette d'achat. L'agent reco a ajusté automatiquement le verdict en ACHETER (Réduit).

**Points de vigilance :**
- **Earnings JOUR J non résolu** (2026-06-09) — plus de 9 jours de flag sans publication. Risque d'artefact de calendrier FMP élevé, mais impossible à écarter définitivement.
- **Volume toujours faible** (0.64× moyenne 20j) : le rebond de +2.10% s'est effectué sur un volume très contraint. Sans confirmation sur volume > 1.0× moyenne, le signal reste fragile.
- **Illiquidité extrême** : sur un ticker avec volume moyen 20j de 2,463 unités, tout ordre de taille modeste peut déplacer le cours de plusieurs pourcents. Les signaux techniques doivent être interprétés avec une marge d'erreur élevée.
- **Proximity avec le low 52 semaines ($40.27)** : le cours est à 8.3% du plus bas annuel. Toute accélération baissière casserait ce support psychologique.
- Si clôture sous $41.73 (SL) → passage **ÉVITER**.
- Si clôture sous MM50 ($43.67) sur volume > moyenne → regradation **SURVEILLER**.
- Si volume > 1.5× moyenne et maintien au-dessus de MM50 → confirmation **ACHETER (Réduit)**.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 21h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*
