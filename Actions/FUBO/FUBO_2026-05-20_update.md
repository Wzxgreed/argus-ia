# FUBO — Mise à Jour Snapshot 10:00 UTC (2026-05-20)

> **Niveau d'impact :** 🟡 Modéré — Close stable $9.20 (0.00% session), volume légèrement supérieur à 1,035,600 (0.69× moyenne 20j), RSI 32.26 inchangé proche survente, earnings Q1 JOUR J (2026-05-20) toujours non résolus, anomalie data quality majeure sur max pain ($21.00 vs $10.00 précédent)
> **Référence précédente :** [FUBO_2026-05-19_update.md](FUBO_2026-05-19_update.md) (snapshot final 21:00 UTC — close $9.20, volume 945 778, max pain $10.00)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-19 21:00 UTC)

| Métrique | 2026-05-19 (final) | 2026-05-20 10:00 UTC | Variation |
|---|---|---|---|
| Cours close | $9,20 | **$9,20** | — |
| Volume séance | 945 778 | **1 035 600** | **+89 822 (+9,5%)** |
| Volume vs 20j | 0,63× | **0,69×** | **+0,06×** |
| RSI 14j | 32,26 | **32,26** | — |
| ATR 14j | $0,78 | **$0,78** | — |
| MM 50j | $11,79 | **$11,79** | — |
| Market Cap (Yahoo) | $270,8M | **$270,8M** | — |
| P/E TTM (Yahoo) | 2,40x | **2,40x** | — |
| Forward P/E | 19,49x | **19,49x** | — |
| P/B (Yahoo) | 0,333x | **0,333x** | — |
| Short Interest | 22,84% | **22,84%** | — |
| **Max Pain** | **$10,00** | **$21,00** | **🔴 +$11,00 (+110%)** |
| Put/Call Ratio | 0,67 | **0,65** | −0,02 |
| Call OI % | 60,0% | **60,6%** | +0,6 pp |
| Échéance options | 2026-05-22 | **2026-05-22** | — (J−2) |

**Constats :**
1. **Cours et technique inchangés** : le close reste à **$9.20** pour la deuxième session consécutive. Le RSI (32.26), l'ATR ($0.78) et la MM50 ($11.79) sont strictement identiques au snapshot précédent. Aucun signal technique nouveau n'est détectable.
2. **Volume légèrement supérieur** : 1,035,600 actions (0.69× moyenne 20j) vs 945,778 hier. La progression de +9.5% reste marginale et le titre continue de négocier sur des volumes très inférieurs à la moyenne — liquidité réduite persistante.
3. **Anomalie data quality — Max Pain $21.00** : le max pain est passé de **$10.00 à $21.00** entre les deux sessions, soit un écart de +110% et +128% vs le spot ($9.20). Cette valeur est irréaliste pour une échéance dans 2 jours (2026-05-22) et traduit très probablement une **erreur de calcul API Yahoo** liée à l'illiquidité extrême des options FUBO ou à un changement d'échéance de référence dans la chaîne options. **Le max pain précédent ($10.00) reste le niveau de référence crédible.**
4. **Earnings Q1 2026 — JOUR J non résolu** : `data/upcoming_events_2026-05-20.json` indique un earnings FUBO au **2026-05-20** (JOUR J, days_until = 0). Aucun résultat (EPS, revenue, guidance) n'est visible dans le snapshot 10:00 UTC. Hypothèses : publication post-close ce soir, retard de remontée API, ou report de publication.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 32,26 | Zone neutre baissière, proximité immédiate survente (seuil 30) — inchangé |
| MM 50j | $11,79 | Cours sous la moyenne — écart **−22,0%** — inchangé |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,78 | Volatilité absolue élevée (8,5% du spot) — inchangée |
| Volume vs 20j | 0,69× | Faible — liquidité réduite persistante, légère amélioration vs 0.63× hier |
| Beta | 2,508 | Volatilité systématique extrême — inchangé |
| 52W High / Low | $56,64 / $8,31 | Distance au 52W low : **+10,7%** — inchangé |

**Niveaux clés (10:00 UTC) :**
- Support immédiat : **$9,09** (low du 2026-05-19)
- Support secondaire : **$8,31** (52W low)
- Résistance : **$10,00** (niveau psychologique — max pain historique crédible)
- Résistance majeure : **$11,79** (MM50)
- Stop-loss ATR (2×) : **$7,64** (−17,0%)
- Take-profit ATR (3×) : **$11,54** (+25,4%)

**Verdict timing :** Défavorable — sous MM50, RSI en descente vers la survente, volume faible. Le cours a clôturé à $9.20 pour deux sessions consécutives, marquant une phase de consolidation/congestion au-dessus du low intraday $9.09. L'absence de rebond technique malgré le RSI proche de 30 et le silence médiatique total traduit un **désintérêt institutionnel profond**. L'anomalie max pain $21.00 est à ignorer pour le positionnement ; le niveau crédible reste $10.00. Le put/call en légère baisse (0.65 vs 0.67) et le call OI en hausse (60.6%) signalent un intérêt spéculatif haussier persistant, mais sans volume pour le valider.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale dans le snapshot 10:00 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $270,8M | 2,40x | 0,333x | — |
| FMP Stable API | ~$3,27B (implicite) | 5,65x | 3,19x | 16,10x |

**Écart :** ×12,1 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-20)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2,40x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 19,49x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0,431x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0,333x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3,19x | Écart ×9,6 avec Yahoo |
| Beta | 2,508 | Extrême |
| Short Interest | 22,84% | Très élevé — inchangé |
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

### Options (stable avec anomalie data quality)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain (brut API) | $21,00 | 🔴 ANOMALIE DATA QUALITY — écart +128% vs spot, incohérent à J−2 |
| Max Pain (crédible, historique) | $10,00 | Niveau psychologique / pinning théorique réaliste |
| Put/Call Ratio | 0,65 | Légèrement put-biased — sentiment dérivés baissier, en amélioration vs 0.67 |
| Call OI % | 60,6% | Dominance calls — intérêt haussier near-term persistant (+0.6 pp) |
| Échéance | 2026-05-22 | J−2 — repositionnement imminent |

**Lecture institutionnelle :** Le max pain brut à $21.00 est une **anomalie data quality** à ignorer. Le niveau crédible reste $10.00 (historique cohérent sur les 3 derniers snapshots). Avec le spot à $9.20 et le max pain crédible à $10.00, l'écart de 8.7% laisse entrevoir un potentiel de **pinning vers $9.80–$10.00** à J−1/J−0 (2026-05-21/22) si les market makers ajustent leur delta hedge. Cependant, le volume faible (0.69×) et l'absence de catalyseur rendent ce scénario fragile. La dominance call OI (60.6%) combinée au short interest massif (22.84%) maintient un **setup latent de short squeeze**, mais sans fondement qualitatif. Le put/call 0.65 reste légèrement baissier.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +446%. Aucune révision récente.

### Social Sentiment (`data/social_sentiment_2026-05-20.json`)

- Mention count Reddit : 0 (no data)
- Pump detected : false
- Sentiment label : No data

### News & Événements Corporates

- `data/news_2026-05-20.json` : **0 article** pour FUBO (silence médiatique total)
- `data/events_2026-05-20.json` : **0 événement corporate** détecté
- `data/upcoming_events_2026-05-20.json` : **Earnings Q1 2026 — JOUR J** (2026-05-20) — résultats non visibles dans le snapshot 10:00 UTC

### FX Exposure (`data/fx_exposure_2026-05-20.json`)

- Exposition FX : 25% (export USD)
- Impact revenus/EPS : 0,0%
- Divergence : aligned
- Score FX Impact : 0,0/10 — neutre

**Verdict Sentiment :** Neutre à légèrement baissier. Silence médiatique total, consensus figé, options marquées par une anomalie data quality, mais le cours qui tient $9.20 pour deux sessions consécutives sans volume traduit une **consolidation latérale avant catalyseur**. L'attente des résultats Q1 2026 (JOUR J non confirmé) domine le sentiment.

---

## 5. Scoring Global

| Composante | Valeur Moteur | Valeur Ajustée (règles Argus-IA) |
|---|---|---|
| Score Global | 64,8 / 100 | — |
| Score Global Ajusté | 56,8 / 100 | **~51 / 100** |
| Score Opportunité | 6,5 / 10 | **~5,1 / 10** |
| Score Catalyseur | 8,0 / 10 | **7,5 / 10** (malus options put-biased historique −0,5) |
| Score Valorisation | 7,0 / 10 | **5,0 / 10** (plafonné Qualité 1/6) |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation** | **ATTENDRE** | **ATTENDRE** |

**Ajustements qualitatifs (inchangés vs 2026-05-19) :**
- Malus Qualité (1/6) : Valorisation plafonnée à 5/10 (règle absolue Filtre Qualité)
- Malus Sectoriel : XLC bottom 3 (momentum 0,0) → −0,5 pt composite
- Signal de prudence Liquidité : volume 0,69× (faible) — risque de slippage modéré
- Options : malus historique −0,5 pt Catalyseur maintenu ; anomalie max pain $21.00 signalée comme [DATA QUALITY] et non prise en compte dans le scoring

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — n = 0, pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1,0 (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

**Sector Rotation (`data/sector_rotation_2026-05-20.json`) :**
- XLC classé **bottom 3** (momentum score 0,0 / 10)
- Malus sectoriel actif : −0,5 pt composite

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9,20 | — |
| Stop-Loss | **$7,64** | 2× ATR (−17,0%) — inchangé |
| Take-Profit | **$11,54** | 3× ATR (+25,4%) — inchangé |
| Ratio R/R | **1,5×** | Stable |
| Max Pain (crédible) | $10,00 | Niveau de pinning historique réaliste à J−2 |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13,00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7,50 (support psychologique) voire $6,80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — ATTENDRE (stabilité technique, vigilance earnings, anomalie data quality options)**

La thèse d'**ATTENDRE** du 2026-05-19 reste intégralement valide et est **confirmée par le snapshot 2026-05-20 10:00 UTC**. Quatre observations :

1. **Stabilité technique absolue** : le close reste à **$9.20** pour la deuxième session consécutive. Le RSI est stable à **32.26** (à 2.3 pts de la survente). La MM50 est inchangée à **$11.79**, écart −22.0%. L'ATR reste à $0.78. Aucun signe de reversal technique n'est détectable. Le volume de 1,035,600 actions (0.69×) est légèrement supérieur à celui de la veille mais reste très faible.

2. **Anomalie data quality — Max Pain $21.00** : le max pain brut est passé de $10.00 à $21.00 entre les deux sessions. Cette valeur est **irréaliste et incohérente** pour une échéance dans 2 jours avec un spot à $9.20. Elle traduit probablement une erreur de calcul API Yahoo liée à l'illiquidité extrême des options FUBO. **Le niveau de référence crédible reste $10.00.** Cette anomalie est signalée comme [DATA QUALITY] et n'impacte pas le scoring.

3. **Earnings toujours en attente — JOUR J non résolu** : les résultats Q1 2026 sont attendus le **2026-05-20** selon `data/upcoming_events_2026-05-20.json`. Aucune donnée earnings (EPS, revenue, guidance) n'est visible dans le snapshot 10:00 UTC. Hypothèses : (a) publication post-close ce soir avec délai API, (b) report de publication, (c) données non remontées. → **À vérifier à la prochaine session impérativement.**

4. **Silence médiatique et institutionnel total** : 0 article, 0 mention Reddit, 0 événement corporate, 0 révision analyste. Le titre est en phase de "dead air" avant catalyseur.

**Arguments confirmant la patience :**
1. **Qualité dégradée 1/6** — patrimoine net négatif (−$398,9M FMP), FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Données techniques baissières** — sous MM50 (−22.0%), RSI 32.26 en descente, volume faible, aucun signe de reversal.
3. **Divergence Yahoo/FMP persistante** — P/E 2.40x et market cap $270.8M restent suspects vs les données FMP (~$3.3B).
4. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 (momentum 0.0).
5. **Quant report non significatif** — pas assez d'historique.
6. **Absence totale de news et de social sentiment** — 0 article, 0 mention Reddit.
7. **Accounting risk non disponible** — pas de données M-Score / Z-Score / F-Score / Sloan pour cette session.
8. **Liquidité réduite** — volume 0.69×, risque de slippage sur toute position.
9. **Anomalie data quality options** — max pain $21.00 incohérent, signalant des données de marché peu fiables.

**Seuls éléments modifiés vs 2026-05-19 :**
- **Volume :** 945 778 → **1 035 600** (+9.5%, 0.69× moyenne 20j)
- **Max Pain (brut API) :** $10.00 → **$21.00** ([ANOMALIE DATA QUALITY])
- **Put/Call :** 0.67 → **0.65**
- **Call OI :** 60.0% → **60.6%**

**Scénarios post-earnings (dès disponibilité des résultats) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 15% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 45% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 40% | −10–20% | Confirmer l'évitement |

**Recommandation finale :** **ATTENDRE — pas de position.** Le titre reste une spéculation pure sans fondement qualitatif. Le close stable à $9.20, le volume faible, l'absence de données earnings et l'anomalie max pain justifient de rester à l'écart. La proximité du RSI avec la survente (30) et l'écart spot/max pain crédible ($9.20 vs $10.00) laissent entrevoir un **rebond technique de courte durée** à J−1/J−0 de l'échéance options, mais ce scénario est spéculatif et non investissable. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle. Si résultats positifs ce soir, le titre reste une spéculation court terme et non un investissement long terme.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-20 (snapshot 10:00 UTC)*  
*Sources : data/latest.json (fetched 2026-05-20T10:00:12Z), data/recommandations_2026-05-20.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_2026-05-20.json, data/social_sentiment_2026-05-20.json, data/fx_exposure_2026-05-20.json, data/upcoming_events_2026-05-20.json, data/events_2026-05-20.json*
