# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-03 (snapshot 13:00 UTC — close du 02/06 confirmé, pas de nouvelle session US)
**Type :** `_update.md` — Stabilité totale des prix, [RÉSOLU] données options corrompues corrigées
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-03_update.md` (10:00 UTC) | **Snapshot 2026-06-03 (13:00 UTC)** | **Δ** |
|----------|----------------------------------------|-------------------------------------|-------|
| Cours close | $17.74 | **$17.74** | **0.00** |
| RSI 14j | 63.90 | **63.90** | **0.00** |
| ATR 14j | $0.91 | **$0.91** | **0.00** |
| MM 50j | $16.76 | **$16.76** | **0.00** |
| Écart MM50 | +5.8% | **+5.8%** | **0.0 pt** |
| Volume | 76.76M (1.13×) | **76.76M (1.13×)** | **0.00** |
| P/E LTM (Yahoo) | 39.42 | **39.42** | **0.00** |
| Forward P/E | 22.74 | **22.74** | **0.00** |
| EV/Revenue (Yahoo) | 5.401 | **5.401** | **0.000** |
| P/B (Yahoo) | 2.103 | **2.103** | **0.000** |
| Short interest | 13.68% | **13.68%** | **0.00** |
| Consensus PT | $25.41 (27a) | **$25.41 (27a)** | **0.00** |
| Max Pain options | $20.00 [historique 02/06] | **$20.00** | **Confirmé par latest.json** |
| Put/Call ratio | 0.48 [historique 02/06] | **0.54** | **+0.06** |
| Call OI % | 67.4% [historique 02/06] | **65.0%** | **−2.4 pts** |
| Earnings J | 55 | **55** | **0** |
| **Score Opportunité** | **6.1/10** | **6.1/10** | **0.0** |
| **Score Global** | **60.8/100** | **60.8/100** | **0.0** |
| **Action** | **ACHETER** | **ACHETER** | **Confirmé** |
| **SL / TP** | **$15.92 / $20.47** | **$15.92 / $20.47** | **Inchangés** |

**Verdict :** Snapshot 13h UTC reprenant le close du 02/06 sans nouvelle session US intermédiaire. **Stabilité totale** des prix, RSI, ATR et MM50. La seule évolution est la **correction des données options** dans `data/latest.json` : les valeurs corrompues du snapshot 10h (Max Pain $5.00 aberrant, Put/Call `null`, Call OI `null`) sont remplacées par des données cohérentes.

**[RÉSOLU] Anomalie options JSON :**
- Max Pain confirmé à **$20.00** (cohérent avec historique 02/06 et niveau opérationnel)
- Put/Call ratio **0.54** (+0.06 vs historique 02/06) — légèrement moins bullish mais reste dans la zone bullish (< 1.0)
- Call OI **65.0%** (−2.4 pts vs historique 02/06) — légère prise de profit sur les calls après le gap du 01/06

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-06-03 (13:00 UTC) | Signal |
|------------|-------------------------------|--------|
| RSI 14j | 63.90 | 🟢 Zone neutre haute — stable, constructif |
| MM 50j | $16.76 | 🟢 Cours +5.8% au-dessus de MM50 — trend haussier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.91 | 🟡 Volatilité stable (ATR rel. 5.13%) |
| Support clé | $16.76 / $17.46 | 🟢 MM50 + low du 02/06 = supports immédiats |
| Résistance clé | $18.58 / $19.00 / $20.00 | 🟡 Close 01/06 = résistance immédiate, puis $19.00 psychologique et $20.00 (Max Pain confirmé) |
| Volume relatif | 1.13× | 🔴 **Supérieur à la moyenne 20j** — distribution partielle confirmée sur données révisées |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Analyse technique :** Aucun changement de prix depuis le close du 02/06. Le cours reste à **$17.74** avec le RSI à **63.90** et l'ATR à **$0.91**. La MM50 à **$16.76** est inchangée. Le volume de **76.76M (1.13× moy. 20j)** confirme la lecture distribution du snapshot 10h : le repli de −4.52% du 02/06 s'est effectué sur volume supérieur à la moyenne, signalant une distribution partielle active.

Le support immédiat reste le low du 02/06 à **$17.46**, suivi de la MM50 à **$16.76**. Une cassure sous $17.46 ouvrirait un test de **$17.00–$17.20** (zone du gap du 01/06). La résistance immédiate est le close du 01/06 à **$18.58**, suivi de **$19.00** (psychologique) puis **$20.00** (Max Pain options confirmé à $20.00, aimant statistique pour l'expiration prochaine).

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Évolution vs 10h | Commentaire |
|----------|--------|------------------|-------------|
| Market cap | $22.76B | 0.00 | Stable |
| P/E LTM (Yahoo) | 39.42 | 0.00 | Stable |
| Forward P/E | 22.74 | 0.00 | Stable |
| EV/Revenue | 5.401 | 0.000 | Stable |
| P/B (Yahoo) | 2.103 | 0.000 | Stable |
| Gross margin (FMP) | 75.1% | — | Stable, excellent |
| Operating margin | 11.0% | — | Stable |
| Net margin | 10.1% | — | Stable |
| Debt/Equity (FMP) | 0.173 | — | Très faible — bilan sain |
| FCF yield | −13.2% | — | FCF négatif — modèle en investissement |
| SBC/Revenue | 5.5% | — | Modéré, sous contrôle |
| ROE (FMP) | 4.6% | — | Faible — limite le Filtre Qualité à 4/6 |

**Aucune news structurante ni événement corporate détecté** (`data/events_latest.json` vide). Le mouvement reste purement technique : distribution post-gap sur volume supérieur à la moyenne, sans catalyseur fondamental négatif.

Le secteur financier (XLF) reste sous-performant SPY (RS20 −6.0%, momentum 0.0/10), ce qui rend la résilience relative de SOFI dans le pullback notable malgré le volume élevé. Le faible momentum sectoriel suggère un manque d'appétit général pour les financières qui amplifie les mouvements de SOFI.

**Short interest 13.68%** (inchangé) reste élevé. Les shorts n'ont pas couvert malgré le rallye puis le pullback, ce qui maintient le potentiel de squeeze si un rebond se matérialise au-dessus de $18.50.

---

## 4. Mise à jour sentiment / options / news

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Consensus PT | $25.41 (27 analystes) | 🟢 Upside consensus +43.2% vs cours $17.74 |
| Analystes actifs (1M) | 2 | 🟡 Couverture stable |
| Analystes actifs (1T) | 10 | 🟡 Couverture stable |
| Max Pain | $20.00 | 🟢 Révision haussière confirmée — strikes repositionnés à la hausse |
| Put/Call ratio | 0.54 | 🟢 Bullish — légèrement moins bullish vs 02/06 (+0.06) mais reste dans zone haussière |
| Call OI % | 65.0% | 🟢 Dominance call maintenue — légère prise de profit post-gap (−2.4 pts) |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit aujourd'hui |
| Pump detected | false | 🟢 Aucun signal pump |

**[RÉSOLU] Options JSON corrigé dans latest.json 13h UTC :**
- Max Pain : **$20.00** (cohérent — vs $5.00 aberrant à 10h UTC, 52W low $13.23)
- Put/Call ratio : **0.54** (vs `null` à 10h UTC) — repositionnement légèrement moins bullish vs 02/06 (0.48 → 0.54)
- Call OI % : **65.0%** (vs `null` à 10h UTC) — légère baisse vs 02/06 (67.4% → 65.0%), probable prise de profit partielle sur les calls après le gap haussier du 01/06
- **Expiration prochaine :** 2026-06-05 (2 jours ouvrés) — avec le cours sous le Max Pain $20.00, le pinning théorique favorise un rebond vers les strikes, mais la distance est significative (+12.7%) et le volume de distribution du 02/06 complique la donne

**News** — Aucune news structurante détectée via les flux automatiques. Le mouvement est non-news-driven.

---

## 5. Scoring global révisé

| Score | Snapshot 2026-06-03 10h (ACHETER) | **Snapshot 2026-06-03 13h (ACHETER)** | **Δ** |
|-------|-----------------------------------|----------------------------------------|-------|
| Score Opportunité | 6.1/10 | **6.1/10** | **0.0** |
| Score Catalyseur | 6.8/10 | **6.8/10** | 0.0 |
| Score Valorisation | 5.5/10 | **5.5/10** | 0.0 |
| Score Momentum | 6.0/10 | **6.0/10** | 0.0 |
| Score Global Composite | 60.8/100 | **60.8/100** | **0.0** |
| Score Global ajusté | 65.8/100 | **65.8/100** | 0.0 |
| Action | ACHETER | **ACHETER** | **Confirmé** |
| Timing | Favorable | **Favorable** | **Inchangé** |
| Sizing | Réduit | **Réduit** | **Inchangé** |
| Horizon | 1–3 mois | **1–3 mois** | **Inchangé** |

**Pondération régime :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime inconnu — pondération par défaut).

**Malus / Bonus appliqués :**
- Malus accounting : 0 (fichier absent)
- Malus geo : 0 (SOFI non flaggé dans geo_risk_latest.json)
- Malus FX : 0 (fx_impact_score 0.0, exposition 55% mais stable)
- Malus social : 0 (pas de données — EXTREME_BEARISH par absence, pas de malus appliqué)
- Malus quant : 0 (pas de signaux historiques)
- Bonus event : 0 (pas d'événement corporate)
- Timing technique : +10 (cours au-dessus de MM50 + breakout historique confirmé le 01/06)

**Note sur la stabilité du score :** Le Score Opportunité et le Score Global Composite restent stables à 6.1/10 et 60.8/100. Aucune nouvelle donnée de prix n'est disponible depuis le close du 02/06. La correction des options ne modifie pas l'interprétation fondamentale : le repositionnement haussier reste intact (Max Pain $20.00, Call OI 65.0%, Put/Call 0.54). Le secteur XLF reste sous-performant (momentum 0.0/10) — headwind sectoriel non résolu.

---

## 6. Niveaux révisés

| Niveau | Snapshot 2026-06-03 10h | Snapshot 2026-06-03 13h | Calcul |
|--------|-------------------------|-------------------------|--------|
| Prix d'entrée suggéré | $17.74 | **$17.74** | Cours actuel — acceptable en momentum avec SL ajusté |
| Stop-loss | $15.92 | **$15.92** | $17.74 − 2×ATR ($0.91) = $15.92 |
| Take-profit | $20.47 | **$20.47** | $17.74 + 3×ATR ($0.91) = $20.47 |
| Upside / Downside | +15.4% / −10.3% | **+15.4% / −10.3%** | — |
| Ratio R/R | 1.50 | **1.50** | Stable (~1.5×) |

**Note sur l'entrée :** Le pullback à $17.74 offre un upside +15.4% avec un ratio R/R ~1.5×. Cependant, la distribution sur volume 1.13× et la clôture proche du low du 02/06 ($17.46) restent des signaux tactiques défavorables à très court terme. Deux approches :
1. **Entrée immédiate (sizing réduit)** — Accepter le prix post-pullback, SL $15.92 strict.
2. **Entrée différée (préférée)** — Attendre un rebond au-dessus de $18.00 avec volume >1.0× pour confirmer que la distribution est terminée.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**🟢 THÈSE CONFIRMÉE — ACHETER maintenu (bord inférieur 60–74), stabilité overnight + correction options**

Aucune nouvelle session US n'a eu lieu entre le close du 02/06 et le snapshot 13h UTC du 03/06. Les données de prix sont **identiques** : cours $17.74, RSI 63.90, ATR $0.91, MM50 $16.76. Le volume final est stable à **76.76M (1.13× moy. 20j)**, confirmant la lecture distribution du snapshot 10h.

**[RÉSOLU] Anomalie options corrigée :** Les données options dans `data/latest.json` ont été corrigées entre le snapshot 10h et 13h UTC. Le Max Pain est confirmé à **$20.00** (cohérent avec l'historique), le Put/Call à **0.54** et le Call OI à **65.0%**. Ces valeurs indiquent un repositionnement légèrement moins bullish vs le 02/06 (Put/Call +0.06, Call OI −2.4 pts), probablement due à une prise de profit partielle sur les calls après le gap haussier du 01/06. L'orientation globale reste clairement haussière en options.

**Éléments confirmant la thèse :**
- Cours +5.8% au-dessus de MM50 — trend haussier court terme intact malgré le pullback
- RSI 63.90 = sortie progressive de la zone proche-surachat, constructif pour continuation
- Classification ACHETER (Score Global 60.8/100, ajusté 65.8) maintenue
- Forward P/E 22.74 attractif vs historique récent
- Short interest 13.68% (inchangé) = potentiel de squeeze intact
- Earnings Q2 dans 55j (28 juillet) avec EPS estimates $0.10–$0.11 — catalyseur forward
- Max Pain $20.00 confirmé = repositionnement haussier des strikes options validé
- Put/Call 0.54 et Call OI 65.0% = sentiment options reste bullish
- Aucune news négative — le mouvement est purement technique

**Risques à surveiller (inchangés vs 10h) :**
- Volume 1.13× = distribution partielle confirmée — vigilance à l'ouverture US du 03/06
- Clôture proche du low du 02/06 ($17.46) = signal tactique défavorable à très court terme
- P/E LTM 39.42 et Forward P/E 22.74 restent étirés pour un Filtre Qualité 4/6
- ATR $0.91 = volatilité persistante, sizing réduit obligatoire
- Secteur financier (XLF) sous-performant SPY (RS20 −6.0%, momentum 0.0/10) = headwind sectoriel
- Score Global au bord inférieur de la zone ACHETER (60.8) — une baisse de 0.9 pt ferait basculer en ATTENDRE
- Filtre Qualité 4/6 inchangé — Quality Partielle, FCF négatif, ROE faible
- Cassure sous $17.46 ouvrirait un test de $17.00–$17.20 (zone du gap)

**Action : ACHETER — Sizing réduit — SL $15.92 — TP $20.47 — Ratio R/R ~1.5×**

---

*Données sourcées : data/latest.json (2026-06-03T13:00:08+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json, data/quant_report_latest.json.*
