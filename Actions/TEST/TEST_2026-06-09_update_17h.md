# TEST — Mise à jour quotidienne (snapshot 17h UTC)

> **Date :** 2026-06-09
> **Type :** Mise à jour post-session 17h UTC
> **Source :** data/latest.json (snapshot 17:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-09 13h UTC | 2026-06-09 17h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | $45.35 | $42.97 | **−$2.38 (−5.25%)** 🔴 |
| Open | $44.03 | $43.31 | — |
| Previous close | $43.527 | $45.35 | — |
| Variation vs previous | +4.19% | **−5.25%** | **−9.44 pts** |
| RSI 14j | 54.61 | 47.10 | **−7.51 pts** 🔴 |
| MM 50j | $43.61 | $43.65 | +$0.04 |
| Écart cours / MM50 | +$1.74 (+4.0%) | **−$0.68 (−1.6%)** | **Cassure** 🔴 |
| Volume session | 2,400 | 1,217 | **−49.3%** 🔴 |
| Volume vs avg 20j | 0.94× | **0.50×** | **Effondrement** 🔴 |
| ATR 14j | $1.01 | $1.07 | +$0.06 |
| Score Global | 61.5 (66.5 ajusté) | 52.8 (44.8 ajusté) | **−8.7 pts (−21.7 pts ajusté)** 🔴 |
| Score Opportunité | 6.2/10 | 5.3/10 | **−0.9 pt** |
| Score Momentum | 7.5/10 | 4.0/10 | **−3.5 pts** 🔴 |
| Verdict | ACHETER (Réduit) | **SURVEILLER** | **Regradation** 🔴 |
| SL | $43.33 | $40.83 | −$2.50 |
| TP | $48.38 | $46.18 | −$2.20 |

**Mutation technique majeure.** Le snapshot 17h UTC enregistre une clôture à $42.97, en repli de −5.25% vs le previous close ($45.35) et de −5.25% vs le snapshot 13h UTC. Le titre a ouvert à $43.31 puis a clôturé au plus bas de la fourchette intraday ($42.97 = low), suggérant une pression vendeuse soutenue sur la session. Le RSI chute de 7.51 pts à 47.10, franchissant le seuil de 50 et passant en territoire légèrement baissier. La MM50 ($43.65) est désormais au-dessus du cours, avec un écart négatif de −$0.68 (−1.6%) — **cassure technique du support mobile 50j confirmée**. Le volume s'est effondré à 1,217 unités (0.50× moyenne 20j), ce qui amplifie le risque de microstructure : sur un ticker illiquide, un tel mouvement de −5.25% sur la moitié du volume moyen peut refléter des ordres de faible taille déplaçant le cours de manière disproportionnée, sans conviction institutionnelle identifiable.

---

## Mise à jour technique

- **Cours :** $42.97, en repli de −$2.38 (−5.25%) vs snapshot 13h UTC. **Open :** $43.31, **Low :** $42.97 = close.
- **Performance intraday :** clôture au plus bas de fourchette — aucun rebond en fin de session.
- **Support clé :** MM50 à $43.65 — **cassure confirmée** avec écart négatif de −$0.68 (−1.6%).
- **Support suivant :** low 52 semaines à $40.27 (écart de −6.3%). Le SL de l'agent reco ($40.83) se situe juste au-dessus de ce niveau critique.
- **RSI 14j :** 47.10, en chute de 7.51 pts. Passage sous 50 : momentum baissier activé.
- **Volume :** 1,217 (0.50× moyenne 20j). Effondrement volume sur une session baissière de −5.25% : aucune participation institutionnelle observable. Risque de faux signal amplifié par la microstructure illiquide.
- **ATR 14j :** $1.07 (+$0.06 vs 13h). Volatilité en légère expansion, cohérente avec le mouvement de cassure.
- **Range 52 semaines :** $40.27–$57.74. Le cours se situe à 6.7% du low et 25.6% sous le high.

**Verdict timing :** Défavorable. Cassure de MM50, RSI sous 50, clôture au plus bas de fourchette sur volume effondré. Aucun signal de soutien technique détecté.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 17h UTC. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-09, source FMP) — résultats toujours non observables dans le snapshot 17h UTC. Après plus de 9 jours de flag "JOUR J" sans publication, l'hypothèse d'un artefact de calendrier FMP se renforce. Toutefois, le risque d'information asymétrique persiste tant qu'aucune résolution n'est confirmée.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-09, snapshot 17h UTC) :

| Axe | Score 13h | Score 17h | Δ |
|-----|-----------|-----------|---|
| Catalyseur | 6.5/10 | 6.5/10 | Stable |
| Valorisation | 5.0/10 | 5.0/10 | Stable |
| Momentum | 7.5/10 | **4.0/10** | **−3.5 pts** 🔴 |
| Opportunité | 6.2/10 | **5.3/10** | **−0.9 pt** |

**Modules agents (snapshot 17h UTC) :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-05-17) : aucun flag géopolitique pour TEST.
- `sector_rotation_latest.json` (2026-06-09) : régime UNKNOWN, signal NEUTRAL. TEST sans secteur assigné.
- `social_sentiment_latest.json` (2026-06-09) : 0 mention, sentiment "No data", pas de pump.
- `fx_exposure_latest.json` (2026-06-09) : exposition FX 25%, impact score 0.0, divergence aligned.
- `events_latest.json` (2026-06-09) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-09) : earnings JOUR J (2026-06-09, source FMP, days_until = 0) — toujours non résolu.

---

## Nouveau scoring global

| Métrique | Valeur |
|----------|--------|
| Score Opportunité | 5.3/10 |
| Score Catalyseur | 6.5/10 |
| Score Valorisation | 5.0/10 |
| Score Momentum | **4.0/10** 🔴 |
| Score Global | 52.8/100 |
| Score Global Ajusté | **44.8/100** 🔴 |
| Verdict | **SURVEILLER** |
| Timing | Défavorable |
| Horizon | — |

Le Score Global Ajusté est passé de 66.5/100 à **44.8/100**, sortant de la fourchette ACHETER (Réduit) (60–74) pour entrer dans la fourchette **SURVEILLER** (35–49). La dégradation est entièrement portée par l'effondrement du Score Momentum (−3.5 pts, de 7.5 à 4.0) consécutif à la cassure de MM50 et au passage du RSI sous 50. Les axes Catalyseur et Valorisation sont stables, mais la règle de disqualification n'est pas activée (aucun score ≤ 2/10).

---

## Révision des niveaux SL / TP

Révision obligatoire suite au nouveau cours et au basculement de verdict :

| Niveau | Ancien (13h) | Nouveau (17h) | Formule agent reco |
|--------|--------------|---------------|--------------------|
| Stop-loss | $43.33 | **$40.83** | Cours − 2×ATR |
| Take-profit | $48.38 | **$46.18** | Cours + 3×ATR |
| Ratio R/R | 1.5 | **1.5** | 3.21 / 2.14 |

**Alerte :** le nouveau SL ($40.83) se sitve à seulement $0.56 au-dessus du low 52 semaines ($40.27). Une cassure sous $40.27 invaliderait structurellement la configuration et justifierait un passage à **ÉVITER**.

---

## Conclusion — Thèse invalidée

**La thèse est INVALIDÉE : passage ACHETER (Réduit) → SURVEILLER.**

**Raisons de l'invalidation :**
1. **Cassure de MM50** : le cours a franchi à la baisse la moyenne mobile 50j ($43.65) avec un close de $42.97. C'est le premier signal de retournement de tendance moyen terme depuis le rebond du 8 juin.
2. **RSI sous 50** : à 47.10, le momentum est passé en territoire baissier. La perte de 7.51 pts en une session est un mouvement rapide qui confirme l'absence de soutien acheteur.
3. **Volume effondré sur baisse** : 1,217 unités (0.50× moyenne) sur une session de −5.25%. En conditions normales, une baisse de cette ampleur s'accompagnerait d'un volume supérieur à la moyenne si elle reflétait une conviction vendeuse. Ici, le volume diminue, ce qui suggère davantage un déséquilibre de liquidité sur micro-cap qu'un signal institutionnel directionnel — mais l'effet sur le prix est réel.
4. **Score Global Ajusté en chute libre** : de 66.5 à 44.8, sortie de la fourchette d'achat. L'agent reco a ajusté automatiquement le verdict en SURVEILLER.

**Points de vigilance :**
- **Earnings JOUR J non résolu** (2026-06-09) — plus de 9 jours de flag sans publication. Risque d'artefact de calendrier FMP élevé, mais impossible à écarter définitivement.
- **Proximity avec le low 52 semaines ($40.27)** : le cours est à seulement 6.7% du plus bas annuel. Toute accélération baissière casserait ce support psychologique.
- **Illiquidité extrême** : sur un ticker avec volume moyen 20j de 2,445 unités, tout ordre de taille modeste peut déplacer le cours de plusieurs pourcents. Les signaux techniques doivent être interprétés avec une marge d'erreur élevée.
- Si clôture sous $40.83 (SL) → passage **ÉVITER**.
- Si retour au-dessus de MM50 ($43.65) sur volume > 1.5× moyenne → réévaluation possible vers **ACHETER (Réduit)**.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 17h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*
