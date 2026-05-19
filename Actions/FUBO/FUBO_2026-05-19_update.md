# FUBO — Mise à Jour Post-Pipeline 17:00 UTC (2026-05-19)

> **Niveau d'impact :** 🟡 Modéré — Close reculé −1.92%, volume en effondrement à 0.39×, RSI proche survente, earnings Q1 JOUR J toujours non observables
> **Référence précédente :** [FUBO_2026-05-19_update.md](FUBO_2026-05-19_update.md) (post-pipeline 13:00 UTC — close $9,38) et [FUBO_2026-05-18_update.md](FUBO_2026-05-18_update.md) (close final $9,38)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (13:00 UTC)

| Métrique | 2026-05-19 13:00 UTC | 2026-05-19 17:00 UTC | Variation |
|---|---|---|---|
| Cours close | $9,38 | **$9,20** | **−1,92%** |
| Volume séance | 965 500 | **572 965** | **−40,7%** |
| Volume vs 20j | 0,62× | **0,39×** | **−0,23×** |
| RSI 14j | 36,21 | **32,26** | **−3,95 pts** |
| ATR 14j | $0,80 | **$0,78** | −$0,02 |
| MM 50j | $11,89 | **$11,79** | −$0,10 |
| Market Cap (Yahoo) | $276,1M | **$270,8M** | −$5,3M |
| P/E TTM (Yahoo) | 2,44x | **2,40x** | −0,04x |
| Forward P/E | 19,87x | **19,49x** | −0,38x |
| P/B (Yahoo) | 0,340x | **0,333x** | −0,007x |
| Short Interest | 22,84% | **22,84%** | — |
| Max Pain | $10,00 | **$10,00** | — |
| Put/Call Ratio | 0,67 | **0,67** | — |
| Call OI % | 60,0% | **60,0%** | — |
| FMP Market Cap | ~$3,27B | **~$3,27B** | — |

**Constat :** Le snapshot pipeline 17:00 UTC enregistre une **dégradation technique continue** par rapport au snapshot 13:00 UTC. Le close recule de **$9.38 à $9.20** (−1.92%) sur un volume en effondrement (**572 965 actions**, 0.39× moyenne 20j). Le RSI descend à **32.26**, à 2.3 pts du seuil de survente (30). La MM50 recule légèrement à **$11.79** (−$0.10). Aucune donnée fondamentale ou options n'a changé entre les deux snapshots. **Les résultats Q1 2026, attendus le 2026-05-19 (JOUR J), restent invisibles dans le snapshot 17:00 UTC.**

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 32,26 | Zone neutre baissière, proximité immédiate survente (seuil 30) |
| MM 50j | $11,79 | Cours sous la moyenne — écart **−22,0%** |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,78 | Volatilité absolue élevée (8,5% du spot) |
| Volume vs 20j | 0,39× | Effondrement du volume — liquidité réduite |
| Beta | 2,508 | Volatilité systématique extrême |
| 52W High / Low | $56,64 / $8,31 | Distance au 52W low : **+10,7%** |

**Niveaux clés (17:00 UTC) :**
- Support immédiat : **$9,11** (low du jour)
- Support secondaire : **$8,31** (52W low)
- Résistance : **$10,00** (niveau psychologique / max pain)
- Résistance majeure : **$11,79** (MM50)
- Stop-loss ATR (2×) : **$7,64** (−17,0%)
- Take-profit ATR (3×) : **$11,54** (+25,4%)

**Verdict timing :** Défavorable — sous MM50, RSI en descente vers la survente, volume en effondrement. Le cours a marqué un nouveau low intraday à $9.11, à 10% du 52W low ($8.31). L'absence de rebond technique malgré le RSI proche de 30 traduit une **faiblesse structurelle** et un manque d'achat dip. Le pinning options autour de $9.50–$10.00 (max pain $10, échéance 2026-05-22 J-3) reste le scénario de haute probabilité, mais le spot s'éloigne désormais du max pain vers le bas.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale dans le snapshot 17:00 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $270,8M | 2,40x | 0,333x | — |
| FMP Stable API | ~$3,27B | 5,65x | 3,19x | 16,10x |

**Écart :** ×12,1 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-19)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2,40x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 19,49x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0,433x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0,333x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3,19x | Écart ×9,6 avec Yahoo |
| Beta | 2,508 | Extrême |
| Short Interest | 22,84% | Très élevé |
| Gross Margin (FMP) | 11,1% | Très faible |
| Operating Margin (FMP) | −2,6% | Perte opérationnelle |
| Current Ratio (FMP) | 0,84 | Illiquidité structurelle |
| Debt/Equity (FMP) | 2,43 | Levier élevé |
| Tangible Asset Value (FMP) | −$398,9M | Patrimoine net négatif |
| Net Debt/EBITDA (FMP) | 1,01x | Couverture faible |
| ROIC (FMP) | −2,1% | Destruction de valeur |

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à 5/10.

**Données Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — scan comptable non disponible pour cette session.

---

## 4. Mise à Jour Sentiment / Options / News

### Options (stable vs 13:00 UTC)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $10,00 | Pinning théorique autour de $10 — le spot à $9.20 s'en éloigne |
| Put/Call Ratio | 0,67 | Légèrement put-biased — sentiment dérivés baissier |
| Call OI % | 60,0% | Dominance calls — intérêt haussier near-term persistant |
| Échéance | 2026-05-22 | J-3 — volatilité de repositionnement attendue |

**Lecture institutionnelle :** Le max pain stable à $10 et le spot à $9.20 créent une **divergence options/cours** de 8.7%. Historiquement, le pinning vers le max pain augmente à J-1/J-0, ce qui implique un risque de **rebond technique vers $9.80–$10.00** si les market makers delta-hedgent. Cependant, le volume en effondrement (0.39×) et l'absence de catalyseur rendent ce scénario fragile. La dominance call OI (60%) combinée au short interest massif (22.84%) maintient un **setup latent de short squeeze**, mais sans fondement qualitatif. Le put/call 0.67 reste légèrement baissier.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +446%. Aucune révision récente.

### Social Sentiment

- Mention count Reddit : 0 (no data)
- Pump detected : false
- Alertes `EXTREME_BEARISH` : artefact d'absence de données

### News & Événements Corporates

- `data/news_2026-05-19.json` : **0 article** pour FUBO
- `data/events_2026-05-19.json` : **0 événement corporate** détecté
- `data/upcoming_events_2026-05-19.json` : **Earnings Q1 2026 — JOUR J** (2026-05-19) — résultats non visibles dans le snapshot 17:00 UTC

### FX Exposure

- Exposition FX : 25% (export USD)
- Impact revenus/EPS : 0,0%
- Divergence : aligned
- Score FX Impact : 0,0/10 — neutre

**Verdict Sentiment :** Neutre à légèrement baissier. Silence médiatique total, consensus figé, options stables, mais le cours qui recule vers $9.20 sans volume traduit un désintérêt généralisé. L'attente des résultats Q1 2026 (JOUR J non confirmé) domine le sentiment.

---

## 5. Scoring Global

| Composante | Valeur Moteur | Valeur Ajustée |
|---|---|---|
| Score Global | 64,8 / 100 | — |
| Score Global Ajusté | 56,8 / 100 | **~51 / 100** |
| Score Opportunité | 6,5 / 10 | **~5,1 / 10** |
| Score Catalyseur | 8,0 / 10 | **7,5 / 10** (malus options put-biased historique −0,5) |
| Score Valorisation | 7,0 / 10 | **5,0 / 10** (plafonné Qualité 1/6) |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation** | **ATTENDRE** | **ATTENDRE** |

**Ajustements qualitatifs (inchangés vs 13:00 UTC, contexte technique dégradé) :**
- Malus Qualité (1/6) : Valorisation plafonnée à 5/10
- Malus Sectoriel : XLC bottom 3 (momentum 0,0) → −0,5 pt composite
- Signal de prudence Liquidité : volume 0,39× (effondrement) — risque de slippage majeur
- Options : malus historique −0,5 pt Catalyseur maintenu ; divergence spot/max pain $9.20 vs $10.00 = −0,3 pt additionnel implicite

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — n = 0, pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1,0 (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

**Sector Rotation (`data/sector_rotation_2026-05-19.json`) :**
- XLC classé **bottom 3** (momentum score 0,0 / 10)
- Malus sectoriel actif : −0,5 pt composite

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9,20 | — |
| Stop-Loss | **$7,64** | 2× ATR (−17,0%) |
| Take-Profit | **$11,54** | 3× ATR (+25,4%) |
| Ratio R/R | **1,5×** | Stable |
| Max Pain | $10,00 | Niveau de pinning probable à J-3 |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13,00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7,50 (support psychologique) voire $6,80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — ATTENDRE (dégradation technique, vigilance earnings)**

La thèse d'**ATTENDRE** du 2026-05-19 13:00 UTC reste intégralement valide et est **légèrement renforcée par la dégradation technique** observée au snapshot 17:00 UTC. Trois observations :

1. **Dégradation technique continue :** le close recule de **$9.38 à $9.20** (−1.92%) sur un volume en **effondrement à 572 965 actions** (0.39× moyenne 20j). Le RSI descend à **32.26** (à 2.3 pts de la survente), confirmant l'absence de momentum haussier. Le low intraday à **$9.11** est le plus bas depuis le 2026-05-18. La MM50 recule à **$11.79**, creusant l'écart à −22.0%. Aucun signe de reversal technique n'est détectable.

2. **Options stables mais divergence spot/max pain :** le max pain reste à **$10.00**, le put/call à **0.67**, le call OI à **60.0%**. La stabilité des métriques options entre 13:00 et 17:00 UTC indique un marché dérivés figé en attente du catalyseur. Le spot à $9.20 s'écarte désormais de 8.7% sous le max pain, ce qui augmente la probabilité d'un **rebond technique de repositionnement vers $9.80–$10.00** à J-1/J-0 (2026-05-21/22) si les market makers ajustent leur delta hedge. Ce potentiel rebond reste purement technique et non fondamental.

3. **Earnings toujours en attente :** les résultats Q1 2026 étaient attendus le 2026-05-19 selon `data/upcoming_events_2026-05-19.json`. Aucune donnée earnings (EPS, revenue, guidance) n'est visible dans le snapshot 17:00 UTC. Hypothèses : (a) publication post-close avec délai de récupération API, (b) report de publication, (c) données non remontées par Yahoo/FMP. → **À vérifier à la prochaine session impérativement.**

**Arguments confirmant la patience (renforcés) :**
1. **Qualité dégradée 1/6** — patrimoine net négatif (−$398,9M FMP), FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Données techniques baissières** — sous MM50 (−22.0%), RSI 32.26 en descente, volume en effondrement, aucun signe de reversal.
3. **Divergence Yahoo/FMP persistante** — P/E 2.40x et market cap $270.8M restent suspects vs les données FMP (~$3.3B).
4. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 (momentum 0.0).
5. **Quant report non significatif** — pas assez d'historique.
6. **Absence totale de news et de social sentiment** — 0 article, 0 mention Reddit.
7. **Accounting risk non disponible** — pas de données M-Score / Z-Score / F-Score / Sloan pour cette session.
8. **Liquidité réduite** — volume 0.39×, risque de slippage majeur sur toute position.

**Seuls éléments modifiés vs 13:00 UTC :**
- **Cours :** $9.38 → **$9.20** (−1.92%)
- **Volume :** 965 500 → **572 965** (−40.7%, 0.39×)
- **RSI :** 36.21 → **32.26** (−3.95 pts)
- **MM50 :** $11.89 → **$11.79** (−$0.10)
- **Market Cap Yahoo :** $276.1M → **$270.8M**

**Scénarios post-earnings (dès disponibilité des résultats) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 15% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 45% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 40% | −10–20% | Confirmer l'évitement |

> **Note de probabilité :** Inchangée vs 13:00 UTC. Le repositionnement options normalisé (max pain $10) et le spot qui s'en éloigne vers $9.20 augmentent marginalement la probabilité d'un rebond technique de pinning (15% → 20%) à J-1/J-0, mais sans changement de fond.

**Recommandation finale :** **ATTENDRE — pas de position.** Le titre reste une spéculation pure sans fondement qualitatif. Le close à $9.20, le volume en effondrement et l'absence de données earnings justifient de rester à l'écart. La proximité du RSI avec la survente (30) et l'écart spot/max pain ($9.20 vs $10.00) laissent entrevoir un **rebond technique de courte durée** à J-1/J-0 de l'échéance options, mais ce scénario est spéculatif et non investissable. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle. Si résultats positifs demain, le titre reste une spéculation court terme et non un investissement long terme.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-19 (post-pipeline 17:00 UTC)*  
*Sources : data/2026-05-19.json (fetched 2026-05-19T17:00:01Z), data/recommandations_2026-05-19.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_2026-05-19.json, data/social_sentiment_2026-05-19.json, data/fx_exposure_2026-05-19.json, data/upcoming_events_2026-05-19.json, data/events_2026-05-19.json, data/news_2026-05-19.json*
