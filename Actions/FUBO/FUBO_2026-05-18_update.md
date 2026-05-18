# FUBO — Mise à Jour Post-Close Finale (2026-05-18 20h UTC)

> **Niveau d'impact :** 🟡 Modéré — Close final $9.38 (-2.49% vs veille), volume corrigé à 0.56×, liquidité toujours réduite
> **Référence précédente :** [FUBO_2026-05-18_update.md](FUBO_2026-05-18_update.md) (17h UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (17h UTC)

| Métrique | 17h UTC (précédent) | 20h UTC (actuel) | Variation |
|---|---|---|---|
| Cours close | $9,53 | **$9,38** | **−1,57%** 🔴 |
| Volume | 484 253 | **873 702** | **+80,4%** (volume total séance) |
| Volume vs 20j | 0,31× | **0,56×** | **+0,25×** mais reste faible |
| RSI 14j | 36,93 | **36,21** | −0,72 |
| ATR 14j | $0,80 | **$0,80** | inchangé |
| MM 50j | $11,89 | **$11,89** | inchangé |
| Market Cap (Yahoo) | $280,5M | **$276,1M** | −1,6% |
| P/E (Yahoo) | 2,48x | **2,44x** | −1,6% |
| P/B | 0,345x | **0,340x** | −1,4% |
| Short Interest | 22,84% | 22,84% | — |
| Put/Call Ratio | 0,90 | 0,90 | — |
| Max Pain | $10,00 | $10,00 | — |

**Constat :** Le snapshot 20h UTC révèle un **close final de $9.38**, inférieur au cours partiel de 17h UTC ($9,53). Le titre a donc cédé **−2,49% vs clôture veille** ($9,62) et non −0,94% comme estimé à 17h. Le volume total de séance s'établit à **873 702 actions** (0,56× moyenne 20j), corrigeant le volume très faible du snapshot 17h (484k, 0,31×) mais restant **significativement sous la norme**. Le RSI recule légèrement à **36,21**, s'approchant de la zone de survente (30). Aucune donnée earnings n'est apparue dans le snapshot 20h UTC — les résultats Q1 2026 restent **non visibles** dans `data/latest.json` et `data/events_latest.json`.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 36,21 | Zone neutre baissière, proximité survente (seuil 30) |
| MM 50j | $11,89 | Cours sous la moyenne — écart −20,2% |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,80 | Volatilité absolue élevée (8,5% du spot) |
| Volume vs 20j | 0,56× | Faiblesse persistante, sous la moyenne |
| Beta | 2,508 | Volatilité systématique extrême |
| 52W High / Low | $56,64 / $8,31 | Distance au 52W low : +12,9% |

**Niveaux clés (révisés post-close 20h UTC) :**
- Support immédiat : $9,31 (low du jour)
- Support secondaire : $8,31 (52W low)
- Résistance : $10,00 (niveau psychologique / max pain)
- Résistance majeure : $11,89 (MM50)
- Stop-loss ATR (2×) : **$7,78** (−17,1%)
- Take-profit ATR (3×) : **$11,78** (+25,5%)

**Verdict timing :** Défavorable — sous MM50, RSI proche survente mais non confirmé, volume faible. Le low du jour à $9,31 n'a pas été testé en clôture, ce qui est un signe technique marginal de soutien intraday. Le pinning autour de $9,40–$10,00 reste le scénario de haute probabilité à J-4 de l'échéance options.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale dans le snapshot 20h UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $276,1M | 2,44x | 0,340x | — |
| FMP Stable API (implicite) | ~$3,27B | 5,65x | 3,19x | 16,10x |

**Écart :** ×11,8 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-18)

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

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à 5/10.

**Données Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — scan comptable non disponible pour cette session.

---

## 4. Mise à Jour Sentiment / Options / News

### Options (inchangées depuis 13h UTC)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $10,00 | Pinning probable autour du spot |
| Put/Call Ratio | 0,90 | Put-biased — sentiment dérivés baissier |
| Call OI % | 52,5% | Baisse du positionnement haussier near-term |
| Échéance | 2026-05-22 | J-4 |

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

### News

- `data/news_2026-05-18.json` : **0 article** pour FUBO
- `data/events_2026-05-18.json` : **0 événement corporate** détecté

**Verdict Sentiment :** Neutre à légèrement baissier. Silence médiatique total, options put-biased, consensus figé. Aucun catalyseur de sentiment détecté.

---

## 5. Scoring Global

| Composante | Valeur Moteur | Valeur Ajustée Manuelle |
|---|---|---|
| Score Global | 64,8 / 100 | — |
| Score Global Ajusté | 56,8 / 100 | **~51 / 100** |
| Score Opportunité | 6,5 / 10 | **~5,1 / 10** |
| Score Catalyseur | 8,0 / 10 | **7,5 / 10** (malus options put-biased −0,5) |
| Score Valorisation | 7,0 / 10 | **5,0 / 10** (plafonné Qualité 1/6) |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation** | **ATTENDRE** | **ATTENDRE** |

**Ajustements qualitatifs (inchangés vs 17h UTC) :**
- Malus Qualité (1/6) : Valorisation plafonnée à 5/10
- Malus Sectoriel : XLC bottom 3 (momentum 0,0) → −0,5 pt composite
- Malus Options : put/call ratio 0,90 + max pain $10 → −0,5 pt Catalyseur
- Signal de prudence Liquidité : volume 0,56× (corrigé vs 0,31×) — reste faible, risque de slippage élevé

**Quant Report (`data/quant_2026-05-18.json`) :**
- n = 0 — pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : null (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9,38 | — |
| Stop-Loss | **$7,78** | Révisé à la baisse — 2× ATR (−17,1%) |
| Take-Profit | **$11,78** | Révisé à la baisse — 3× ATR (+25,5%) |
| Ratio R/R | **1,5×** | Stable |
| Max Pain | $10,00 | Niveau de pinning probable |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13,00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7,50 (support psychologique) voire $6,80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — ATTENDRE**

La thèse d'**ATTENDRE** du 2026-05-18 reste intégralement valide. Le close final à **$9.38** (−2,49% vs veille) confirme la faiblesse technique sans catalyseur de reversal. Trois observations actualisées :

1. **Close final révisé à la baisse :** le snapshot 20h UTC capture un close de $9.38, inférieur au $9.53 du snapshot 17h. Le titre a donc sous-performé l'estimation intermédiaire. Le low du jour ($9,31) a été testé mais non cassé en clôture — un soutien technique marginal reste en place.
2. **Volume corrigé à 0,56× :** le volume total de séance (873k) est supérieur au volume partiel de 17h (484k), ce qui normalise partiellement le signal "liquidity trap". Cependant, 0,56× reste bien sous la moyenne 20j (1,55M) — le désintérêt du marché persiste.
3. **Earnings toujours en attente :** les résultats Q1 2026 étaient attendus ce jour. Aucune donnée (EPS, revenue, guidance) n'est visible dans le snapshot 20h UTC. Hypothèses : (a) publication post-close avec délai de récupération API, (b) report de publication, (c) données non remontées par Yahoo/FMP. → **À vérifier demain matin impérativement.**

**Arguments confirmant la patience :**
1. **Qualité dégradée 1/6** — inchangée. Patrimoine net négatif (−$398,9M FMP), FCF négatif, current ratio 0,84, debt/equity 2,43.
2. **Données techniques baissières** — sous MM50 (−20,2%), RSI 36,21 proche survente, aucun signe de reversal. Le faible volume traduit un désintérêt, pas une accumulation.
3. **Repositionnement options baissier** — put/call 0,90, max pain $10 (données inchangées).
4. **Divergence Yahoo/FMP persistante** — P/E 2,44x et market cap $276M restent suspects vs les données FMP (~$3,3B).
5. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 (momentum 0,0).
6. **Quant report non significatif** — pas assez d'historique.
7. **Absence totale de news et de social sentiment** — 0 article, 0 mention Reddit.
8. **Accounting risk non disponible** — pas de données M-Score / Z-Score / F-Score / Sloan pour cette session.

**Seuls éléments modifiés :**
- Close révisé à $9.38 (vs $9.53 à 17h UTC)
- SL/TP ajustés à la baisse ($7,78 / $11,78) en raison du nouveau close
- Volume corrigé à 0,56× (vs 0,31×) — liqudité légèrement moins critique

**Scénarios post-earnings (dès disponibilité des résultats) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 15% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 45% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 40% | −10–20% | Confirmer l'évitement |

> **Note de probabilité :** Inchangée vs 17h UTC. Le repositionnement options put-biased maintient la probabilité bearish à 40%.

**Recommandation finale :** **ATTENDRE — pas de position.** Le titre reste une spéculation pure sans fondement qualitatif. Le close final à $9.38, le volume faible et l'absence de données earnings justifient de rester à l'écart. Si résultats positifs demain, le titre reste une spéculation court terme et non un investissement long terme. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-18 (post-close 20h UTC)*  
*Sources : data/2026-05-18.json (fetched 2026-05-18T20:40:01Z), data/recommandations_2026-05-18.json, data/quant_2026-05-18.json, data/geo_2026-05-18.json, data/sector_rotation_2026-05-18.json, data/social_sentiment_2026-05-18.json, data/fx_exposure_2026-05-18.json, data/upcoming_events_2026-05-18.json, data/events_2026-05-18.json, data/news_2026-05-18.json, data/transcripts_NLP_2026-05-18.json*
