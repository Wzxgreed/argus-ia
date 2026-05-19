# FUBO — Mise à Jour Post-Pipeline 10:00 UTC (2026-05-19)

> **Niveau d'impact :** 🟡 Modéré — Repositionnement options significatif (max pain ×2, call OI dominant), données fondamentales et techniques stables
> **Référence précédente :** [FUBO_2026-05-18_update.md](FUBO_2026-05-18_update.md) (post-pipeline 22:35 UTC) et [FUBO_2026-05-18_init.md](FUBO_2026-05-18_init.md) (FULL REFRESH 13h UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-18)

| Métrique | 2026-05-18 (close 22:35 UTC) | 2026-05-19 (10:00 UTC) | Variation |
|---|---|---|---|
| Cours close | $9,38 | **$9,38** | — |
| Volume séance | 964 675 | **965 500** | +0,09% |
| Volume vs 20j | 0,62× | **0,62×** | — |
| RSI 14j | 36,21 | **36,21** | — |
| ATR 14j | $0,80 | **$0,80** | — |
| MM 50j | $11,89 | **$11,89** | — |
| Market Cap (Yahoo) | $276,1M | **$276,1M** | — |
| P/E TTM (Yahoo) | 2,44x | **2,44x** | — |
| Forward P/E | 19,87x | **19,87x** | — |
| P/B (Yahoo) | 0,340x | **0,340x** | — |
| Short Interest | 22,84% | **22,84%** | — |
| **Max Pain** | $10,00 | **$21,00** | **+110,0%** |
| **Put/Call Ratio** | 0,90 | **0,65** | **−27,8%** |
| **Call OI %** | 52,5% | **60,6%** | **+8,1 pp** |
| FMP Market Cap | ~$3,27B | **~$3,27B** | — |

**Constat :** Le snapshot pipeline 10:00 UTC du 2026-05-19 confirme la **stabilité totale** du close final à **$9.38** et de l'ensemble des métriques fondamentales et techniques. Le volume reste inchangé à **965 500 actions** (0.62× moyenne 20j), le RSI **36.21**, l'ATR **$0.80**. **Aucune donnée de prix, volume, ratio technique ou consensus n'a varié** entre les deux sessions.

**Changement majeur : repositionnement options volatile autour de l'échéance 2026-05-22**
- Le max pain est remonté de **$10,00 à $21,00** (+110%), niveau proche du matin du 2026-05-18 ($21,00 à 10h UTC) avant de basculer à $10,00 en session close. Ce cycle suggère une volatilité de repositionnement quotidienne.
- Le put/call ratio est repassé de **0,90 à 0,65** (moins baissier), proche du niveau matinal du 2026-05-18.
- Les calls dominent désormais l'open interest à **60,6%** (+8,1 pp vs close 18/05), signalant un intérêt haussier renouvelé sur les dérivés à très court terme.
- **Lecture institutionnelle :** ce repositionnement call-dominant avec max pain à $21 peut refléter (a) des achats de calls spéculatifs en anticipation d'un catalyseur post-earnings, ou (b) une couverture de shorts massifs (short interest 22,84%). Le max pain à $21 reste à +123% du spot — le marché ne price pas un move de cette amplitude comme base, mais comme queue de distribution.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 36,21 | Zone neutre baissière, proximité survente (seuil 30) |
| MM 50j | $11,89 | Cours sous la moyenne — écart **−21,1%** |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,80 | Volatilité absolue élevée (8,5% du spot) |
| Volume vs 20j | 0,62× | Faiblesse persistante vs moyenne 20j (1,56M) |
| Beta | 2,508 | Volatilité systématique extrême |
| 52W High / Low | $56,64 / $8,31 | Distance au 52W low : +12,9% |

**Niveaux clés (confirmés 10:00 UTC) :**
- Support immédiat : **$9,31** (low du 2026-05-18)
- Support secondaire : **$8,31** (52W low)
- Résistance : **$10,00** (niveau psychologique)
- Résistance majeure : **$11,89** (MM50)
- Stop-loss ATR (2×) : **$7,78** (−17,1%)
- Take-profit ATR (3×) : **$11,78** (+25,5%)

**Verdict timing :** Défavorable — sous MM50, RSI proche survente mais non confirmé, volume inférieur à la normale. Le pinning autour de $9,40 reste le scénario de haute probabilité à J-3 de l'échéance options (2026-05-22), malgré le max pain théorique à $21. Ce dernier est trop éloigné du spot pour constituer un aimant de prix réaliste à court terme.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale dans le snapshot 10:00 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $276,1M | 2,44x | 0,340x | — |
| FMP Stable API | ~$3,27B | 5,65x | 3,19x | 16,10x |

**Écart :** ×11,8 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-19)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2,44x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 19,87x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0,433x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0,340x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3,19x | Écart ×9,4 avec Yahoo |
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

### Options (repositionnement majeur)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $21,00 | Niveau théorique très éloigné du spot (+123%) — aimant peu crédible à J-3 |
| Put/Call Ratio | 0,65 | Moins baissier qu'hier (0,90) — repositionnement vers calls |
| Call OI % | 60,6% | Dominance calls — intérêt haussier sur dérivés near-term |
| Échéance | 2026-05-22 | J-2 — volatilité de repositionnement attendue |

**Lecture institutionnelle :** Le cycle max pain $21 → $10 → $21 en 24h traduit une incertitude extrême sur le payoff post-earnings. La dominance call OI (60,6%) combinée au short interest massif (22,84%) dessine un **setup potentiel de short squeeze** si un catalyseur positif survient (beat earnings, guidance raise, annonce stratégique). Toutefois, la probabilité reste faible au vu de la qualité dégradée (1/6) et de l'absence de news. Le max pain à $21 est un artefact de la structure OI — le véritable aimant de prix reste $9,50–$10,00.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +435%. Aucune révision récente.

### Social Sentiment

- Mention count Reddit : 0 (no data)
- Pump detected : false
- Alertes `EXTREME_BEARISH` : artefact d'absence de données

### News & Événements Corporates

- `data/news_2026-05-19.json` : **0 article** pour FUBO
- `data/events_2026-05-19.json` : **0 événement corporate** détecté
- `data/upcoming_events_2026-05-19.json` : **Earnings Q1 2026 — JOUR J** (2026-05-19) — résultats non visibles dans le snapshot 10:00 UTC

### FX Exposure

- Exposition FX : 25% (export USD)
- Impact revenus/EPS : 0,0%
- Divergence : aligned
- Score FX Impact : 0,0/10 — neutre

**Verdict Sentiment :** Neutre à légèrement spéculatif haussier sur options. Silence médiatique total, consensus figé, mais repositionnement call-dominant et max pain volatile signalent une attente de catalyseur. Aucune news fondamentale détectée.

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

**Ajustements qualitatifs (inchangés vs 2026-05-18) :**
- Malus Qualité (1/6) : Valorisation plafonnée à 5/10
- Malus Sectoriel : XLC bottom 3 (momentum 0,0) → −0,5 pt composite
- Signal de prudence Liquidité : volume 0,62× — risque de slippage persistant
- Options : malus historique −0,5 pt Catalyseur maintenu malgré le repositionnement call-dominant, car le max pain à $21 est un artefact de structure et non un signal de conviction

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
| Close | $9,38 | — |
| Stop-Loss | **$7,78** | 2× ATR (−17,1%) |
| Take-Profit | **$11,78** | 3× ATR (+25,5%) |
| Ratio R/R | **1,5×** | Stable |
| Max Pain (théorique) | $21,00 | Niveau non crédible à J-3 — artefact OI |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13,00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7,50 (support psychologique) voire $6,80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — ATTENDRE (vigilance accrue sur options)**

La thèse d'**ATTENDRE** du 2026-05-18 reste intégralement valide. Le snapshot pipeline 10:00 UTC du 2026-05-19 **ne modifie aucune donnée de prix, volume ou ratio fondamental** par rapport au close final précédent. Trois observations :

1. **Stabilité totale des données closes :** entre le snapshot 2026-05-18 22:35 UTC et le snapshot 2026-05-19 10:00 UTC, le close reste à **$9.38**, le volume quasi identique, et toutes les métriques techniques (RSI, ATR, MM) inchangées. Le fichier `data/2026-05-19.json` (fetched 2026-05-19T10:00:01Z) confirme la stabilité.

2. **Repositionnement options volatile autour de l'échéance 2026-05-22 :** le cycle max pain $21 → $10 → $21 en 24h traduit une incertitude extrême sur le payoff post-earnings. La dominance call OI (60,6%) et le put/call 0,65 signalent un intérêt spéculatif haussier, mais le max pain à $21 est trop éloigné du spot pour constituer un aimant crédible. Ce setup combine un **potentiel short squeeze** (short interest 22,84% + calls dominants) avec une **qualité dégradée 1/6** qui exclut toute conviction structurelle.

3. **Earnings toujours en attente :** les résultats Q1 2026 étaient attendus le 2026-05-19 selon `data/upcoming_events_2026-05-19.json`. Aucune donnée earnings (EPS, revenue, guidance) n'est visible dans le snapshot 10:00 UTC. Hypothèses : (a) publication post-close avec délai de récupération API, (b) report de publication, (c) données non remontées par Yahoo/FMP. → **À vérifier à la prochaine session impérativement.**

**Arguments confirmant la patience (inchangés) :**
1. **Qualité dégradée 1/6** — patrimoine net négatif (−$398,9M FMP), FCF négatif, current ratio 0,84, debt/equity 2,43, ROIC −2,1%.
2. **Données techniques baissières** — sous MM50 (−21,1%), RSI 36,21 proche survente, aucun signe de reversal.
3. **Divergence Yahoo/FMP persistante** — P/E 2,44x et market cap $276M restent suspects vs les données FMP (~$3,3B).
4. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 (momentum 0,0).
5. **Quant report non significatif** — pas assez d'historique.
6. **Absence totale de news et de social sentiment** — 0 article, 0 mention Reddit.
7. **Accounting risk non disponible** — pas de données M-Score / Z-Score / F-Score / Sloan pour cette session.

**Seul élément modifié vs 2026-05-18 :**
- **Repositionnement options :** max pain $21,00 (+110%), put/call 0,65 (−27,8%), call OI 60,6% (+8,1 pp). Signal de volatilité imminente à J-2 de l'échéance, mais sans direction fondamentale claire.

**Scénarios post-earnings (dès disponibilité des résultats) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 15% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 45% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 40% | −10–20% | Confirmer l'évitement |

> **Note de probabilité :** Inchangée vs 2026-05-18. Le repositionnement options call-dominant maintient la probabilité d'un squeeze technique à 15%, mais sans fondement qualitatif.

**Recommandation finale :** **ATTENDRE — pas de position.** Le titre reste une spéculation pure sans fondement qualitatif. Le close confirmé à $9.38, le volume sous-moyenne et l'absence de données earnings justifient de rester à l'écart. Le repositionnement options volatile à J-2 de l'échéance 2026-05-22 augmente le risque de gap, mais dans les deux directions. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle. Si résultats positifs demain, le titre reste une spéculation court terme et non un investissement long terme.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-19 (post-pipeline 10:00 UTC)*  
*Sources : data/2026-05-19.json (fetched 2026-05-19T10:00:01Z), data/recommandations_2026-05-19.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_2026-05-19.json, data/social_sentiment_2026-05-19.json, data/fx_exposure_2026-05-19.json, data/upcoming_events_2026-05-19.json, data/events_2026-05-19.json, data/news_2026-05-19.json*
