# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-03 (snapshot 10:00 UTC — close du 02/06 confirmé, pas de nouvelle session US)
**Type :** `_update.md` — Stabilité overnight, données options corrompues dans latest.json
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-02_update.md` (21:00 UTC) | **Snapshot 2026-06-03 (10:00 UTC)** | **Δ** |
|----------|------------------------------------------|-------------------------------------|-------|
| Cours close | $17.74 | **$17.74** | **0.00** |
| RSI 14j | 63.90 | **63.90** | **0.00** |
| ATR 14j | $0.91 | **$0.91** | **0.00** |
| MM 50j | $16.76 | **$16.76** | **0.00** |
| Écart MM50 | +5.8% | **+5.8%** | **0.0 pt** |
| Volume | 73.21M (1.10×) | **76.76M (1.13×)** | **+3.55M (+0.03×)** |
| P/E LTM (Yahoo) | 39.42 | **39.42** | **0.00** |
| Forward P/E | 22.74 | **22.74** | **0.00** |
| EV/Revenue (Yahoo) | 5.401 | **5.401** | **0.000** |
| P/B (Yahoo) | 2.103 | **2.103** | **0.000** |
| Short interest | 13.68% | **13.68%** | **0.00** |
| Consensus PT | $25.41 (27a) | **$25.41 (27a)** | **0.00** |
| Max Pain options | $20.00 | **$5.00 [ABERRANT]** | **Données corrompues** |
| Put/Call ratio | 0.48 | **null [CORROMPU]** | **Données corrompues** |
| Call OI % | 67.4% | **null [CORROMPU]** | **Données corrompues** |
| Earnings J | 56 | **55** | **−1j** |
| **Score Opportunité** | **6.1/10** | **6.1/10** | **0.0** |
| **Score Global** | **60.8/100** | **60.8/100** | **0.0** |
| **Action** | **ACHETER** | **ACHETER** | **Confirmé** |
| **SL / TP** | **$15.92 / $20.47** | **$15.92 / $20.47** | **Inchangés** |

**Verdict :** Snapshot matinal 10h UTC reprenant le close du 02/06 sans nouvelle session US intermédiaire. **Stabilité totale** des prix, RSI, ATR et MM50. Seule révision : le volume final est ajusté à **76.76M (1.13× moy. 20j)** vs 73.21M (1.10×) dans le snapshot 21h du 02/06 — confirmation que le repli s'est effectué sur volume supérieur à la moyenne.

**[ALERTE DATA QUALITY]** Les données options dans `data/latest.json` sont corrompues ce matin : Max Pain $5.00 (aberrant vs historique $20.00), Put/Call ratio `null`, Call OI % `null`. Les valeurs opérationnelles du snapshot 02/06 sont conservées : **Max Pain $20.00, Put/Call 0.48, Call OI 67.4%**.

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-06-03 (10:00 UTC) | Signal |
|------------|-------------------------------|--------|
| RSI 14j | 63.90 | 🟢 Zone neutre haute — stable, constructif |
| MM 50j | $16.76 | 🟢 Cours +5.8% au-dessus de MM50 — trend haussier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.91 | 🟡 Volatilité stable (ATR rel. 5.13%) |
| Support clé | $16.76 / $17.46 | 🟢 MM50 + low du 02/06 = supports immédiats |
| Résistance clé | $18.58 / $19.00 / $20.00 | 🟡 Close 01/06 = résistance immédiate, puis $19.00 psychologique et $20.00 (Max Pain) |
| Volume relatif | 1.13× | 🔴 **Supérieur à la moyenne 20j** — distribution partielle confirmée sur données révisées |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Analyse technique :** Aucun changement de prix depuis le close du 02/06. Le cours reste à **$17.74** avec le RSI à **63.90** et l'ATR à **$0.91**. La MM50 à **$16.76** est inchangée. Le volume révisé à **76.76M (1.13× moy. 20j)** confirme la lecture du snapshot 21h : le repli de −4.52% du 02/06 s'est effectué sur volume supérieur à la moyenne, signalant une distribution partielle active.

Le support immédiat reste le low du 02/06 à **$17.46**, suivi de la MM50 à **$16.76**. Une cassure sous $17.46 ouvrirait un test de **$17.00–$17.20** (zone du gap du 01/06). La résistance immédiate est le close du 01/06 à **$18.58**, suivi de **$19.00** (psychologique) puis **$20.00** (Max Pain options historique).

⚠️ **Données options corrompues** — `latest.json` retourne Max Pain $5.00 (aberrant, le 52W low est $13.23), Put/Call `null`, Call OI `null`. Ces valeurs sont ignorées. Les dernières valeurs fiables (02/06) sont : Max Pain **$20.00**, Put/Call **0.48**, Call OI **67.4%**.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Évolution vs 02/06 | Commentaire |
|----------|--------|--------------------|-------------|
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
| Max Pain | $20.00 (historique 02/06) | 🟢 Révision haussière confirmée — strikes repositionnés à la hausse |
| Put/Call ratio | 0.48 (historique 02/06) | 🟢 Bullish — repositionnement haussier intact |
| Call OI % | 67.4% (historique 02/06) | 🟢 Dominance call maintenue |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit aujourd'hui |
| Pump detected | false | 🟢 Aucun signal pump |

**[ALERTE DATA QUALITY] Options JSON corrompu dans latest.json :**
- Max Pain retourné : $5.00 (aberrant — 52W low $13.23, impossible)
- Put/Call ratio : `null`
- Call OI % : `null`
- **Action :** Valeurs historiques du 02/06 conservées (Max Pain $20.00, Put/Call 0.48, Call OI 67.4%). L'expiration prochaine reste le 2026-06-05 (2 jours ouvrés).

**News** — Aucune news structurante détectée via les flux automatiques. Le mouvement est non-news-driven.

---

## 5. Scoring global révisé

| Score | Snapshot 2026-06-02 21h (ACHETER) | **Snapshot 2026-06-03 10h (ACHETER)** | **Δ** |
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

**Note sur la stabilité du score :** Le Score Opportunité et le Score Global Composite restent stables à 6.1/10 et 60.8/100. Aucune nouvelle donnée de prix n'est disponible depuis le close du 02/06. Le volume révisé à 1.13× (vs 1.10×) ne modifie pas l'interprétation : distribution partielle confirmée. Le secteur XLF reste sous-performant (momentum 0.0/10) — headwind sectoriel non résolu.

---

## 6. Niveaux révisés

| Niveau | Snapshot 2026-06-02 21h | Snapshot 2026-06-03 10h | Calcul |
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

**🟢 THÈSE CONFIRMÉE — ACHETER maintenu (bord inférieur 60–74), stabilité overnight**

Aucune nouvelle session US n'a eu lieu entre le close du 02/06 et le snapshot 10h UTC du 03/06. Les données sont **identiques** : cours $17.74, RSI 63.90, ATR $0.91, MM50 $16.76. Le volume final est légèrement révisé à la hausse (**76.76M, 1.13× moy. 20j** vs 73.21M, 1.10×), confirmant la lecture distribution du snapshot 21h.

**[ALERTE DATA QUALITY]** Les données options dans `data/latest.json` sont corrompues (Max Pain $5.00 aberrant, Put/Call et Call OI `null`). Les valeurs opérationnelles du 02/06 sont conservées.

**Éléments confirmant la thèse :**
- Cours +5.8% au-dessus de MM50 — trend haussier court terme intact malgré le pullback
- RSI 63.90 = sortie progressive de la zone proche-surachat, constructif pour continuation
- Classification ACHETER (Score Global 60.8/100, ajusté 65.8) maintenue
- Forward P/E 22.74 attractif vs historique récent
- Short interest 13.68% (inchangé) = potentiel de squeeze intact
- Earnings Q2 dans 55j (28 juillet) avec EPS estimates $0.10–$0.11 — catalyseur forward
- Max Pain $20.00 (historique) = repositionnement haussier des strikes options confirmé
- Put/Call 0.48 et Call OI 67.4% (historique) = sentiment options reste bullish
- Aucune news négative — le mouvement est purement technique

**Risques à surveiller (inchangés vs 02/06) :**
- Volume 1.13× = distribution partielle confirmée — vigilance à l'ouverture US du 03/06
- Clôture proche du low du 02/06 ($17.46) = signal tactique défavorable à très court terme
- P/E LTM 39.42 et Forward P/E 22.74 restent étirés pour un Filtre Qualité 4/6
- ATR $0.91 = volatilité persistante, sizing réduit obligatoire
- Secteur financier (XLF) sous-performant SPY (RS20 −6.0%, momentum 0.0/10) = headwind sectoriel
- Score Global au bord inférieur de la zone ACHETER (60.8) — une baisse de 0.9 pt ferait basculer en ATTENDRE
- Filtre Qualité 4/6 inchangé — Quality Partielle, FCF négatif, ROE faible
- Cassure sous $17.46 ouvrirait un test de $17.00–$17.20 (zone du gap)
- Données options corrompues dans latest.json — surveillance nécessaire à la prochaine snapshot

**Action : ACHETER — Sizing réduit — SL $15.92 — TP $20.47 — Ratio R/R ~1.5×**

---

*Données sourcées : data/latest.json (2026-06-03T10:00:08+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json, data/quant_report_latest.json.*
