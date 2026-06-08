# FUBO — Mise à Jour (2026-06-08, snapshot 13h UTC)

> **Niveau d'impact :** 🟡 Modéré — **Stabilité totale des données marché** vs snapshot 10h UTC, mais **résolution majeure de l'anomalie options JSON** (max pain $3.00 aberrant → $13.00 cohérent). Cours stable **$9.54**, volume stable **1.28M (1.02× moy. 20j)**, RSI **49.4**, spot sous MM50 **−12.96%**. Scores agents **inchangés** : **ATTENDRE 58.0/100**. Structure options désormais fiable : max pain **$13.00**, put/call **0.25**, call OI **79.7%** — setup de short squeeze re-quantifiable.
> **Référence précédente :** [FUBO_2026-06-08_update.md](FUBO_2026-06-08_update.md) (snapshot 10:00 UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-08 10:00 UTC)

| Métrique | 2026-06-08 10:00 UTC | **2026-06-08 13:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.54 | **$9.54** | **Stable** |
| Volume séance | 1 281 500 | **1 281 500** | **Stable** |
| RSI 14j | 49.4 | **49.4** | Stable |
| ATR 14j | $0.72 | **$0.72** | Stable |
| MM 50j | $10.96 | **$10.96** | Stable |
| Spot vs MM50 | −12.96% | **−12.96%** | Stable |
| **Max Pain (API)** | **$3.00** | **$13.00** | **[ANOMALIE JSON RÉSOLUE]** 🟢 |
| **Put/Call Ratio (API)** | **null** | **0.25** | **Résolu** 🟢 |
| **Call OI % (API)** | **null** | **79.7%** | **Résolu** 🟢 |
| Échéance options | 2026-06-12 | **2026-06-12** | Inchangée |
| Score Global (agent) | 58.0/100 | **58.0/100** | Inchangé |
| Score Opportunité (agent) | 6.6/10 | **6.6/10** | Inchangé |
| Score Momentum (agent) | 4.0/10 | **4.0/10** | Inchangé |
| Recommandation (agent) | ATTENDRE | **ATTENDRE** | Inchangée |

**Constats :**
1. **Stabilité totale des prix et indicateurs techniques** — Aucune variation entre les snapshots 10h et 13h UTC. Le cours $9.54, le volume 1.28M, le RSI 49.4 et l'ATR $0.72 sont strictement identiques.
2. **Résolution de l'anomalie options JSON** — Le snapshot 13h UTC corrige l'anomalie persistante depuis le 01/06. Les données options redeviennent cohérentes : max pain **$13.00** (vs $3.00 aberrant), put/call **0.25** (vs null), call OI **79.7%** (vs null). L'échéance reste au **2026-06-12**.
3. **Setup short squeeze re-quantifiable** — Avec des données options fiables, le setup redevient observable : short interest **25.03%** + call OI dominant **79.7%** + put/call **0.25** = structure haussière options. Le spot à **$9.54** est désormais **−26.6% sous le max pain $13.00**, ce qui réactive l'aimant haussier mécanique vers $13.00 à échéance J+4 (2026-06-12).
4. **Earnings Q1 2026 anomalie persistante** — `upcoming_events_latest.json` (2026-06-08) place toujours l'earnings au **2026-06-08** (jour J, `days_until: 0`). Aucun résultat Q1 visible.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 49.4 | Neutre médian — inchangé |
| MM 50j | $10.96 | Cours sous MM50 — écart −12.96% |
| ATR 14j | $0.72 | Volatilité en expansion (7.55% du spot) |
| Volume vs 20j | 1.02× | Liquidation — stable |
| Beta | 2.392 | Extrême |
| 52W High / Low | $56.64 / $8.31 | Distance 52W low : +14.8% |
| Short Interest | 25.03% | Très élevé — stable |

**Options (données résolues) :**

| Signal | Valeur 10h | Valeur 13h | Lecture |
|---|---|---|---|
| Max Pain | $3.00 (anomalie) | **$13.00** | Cohérent — spot −26.6% sous max pain |
| Put/Call Ratio | null | **0.25** | Très faible — biais haussier |
| Call OI % | null | **79.7%** | Dominance call — structure haussière |
| Échéance | 2026-06-12 | **2026-06-12** | J+4 |

**Lecture institutionnelle :** La résolution de l'anomalie options révèle une structure haussière significative pour l'échéance du 2026-06-12. Le max pain $13.00 est désormais l'aimant mécanique naturel. Le put/call 0.25 et le call OI 79.7% confirment un biais acheteur sur les options. Le short interest 25.03% combiné à cette structure reconstitue un setup de short squeeze technique mesurable. Cependant, le cours n'a pas réagi à cette résolution d'anomalie (stable à $9.54), ce qui indique que le marché ne "trade" pas encore cette structure options comme catalyseur.

**Niveaux clés :**
- Support immédiat : **$9.44** (low 08/06)
- Support psychologique : **$9.00**
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$10.16** (previous close)
- Résistance : **$10.96** (MM50)
- Résistance majeure : **$11.00–$13.00** (zone max pain / ancienne structure)
- Stop-loss ATR (2×) : **$8.10** (−15.1%)
- Take-profit ATR (3×) : **$11.70** (+22.6%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — cours sous MM50 (−12.96%), momentum baissier confirmé (Score Momentum 4.0/10). La structure options haussière est un facteur latent positif mais pas un catalyseur actif sans résolution de l'anomalie earnings ou upgrade/downgrade.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 13h. Divergence Yahoo/FMP inchangée :

| Source | Market Cap | P/E | P/B |
|---|---|---|---|
| Yahoo Finance | $280.8M | 2.48x | 0.35x |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x |

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à **5/10**.

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)
- Price Target Moyen : **$50.25** (4 analysts, 0 mise à jour récente) — écart +426.7%, consensus figé.

### News & Événements Corporates
- `data/events_latest.json` (2026-06-08) : **vide** — aucun événement corporate.
- **Earnings Q1 2026** : anomalie calendrier persistante (`days_until: 0`), aucun résultat visible.

### FX Exposure / Social Sentiment / Sector Rotation / Geo Risk / Quant
- Inchangés vs snapshot 10h. FX Impact **0.0/10**, Social Sentiment **0.0/10** (silence total), XLC **bottom 3** (malus sectoriel −0.5 pt).

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)
Inchangé vs 10h : Score Global **58.0/100**, Score Opportunité **6.6/10**, Score Momentum **4.0/10**, Recommandation **ATTENDRE**, Timing **Défavorable**.

### Scoring ajusté analyste

| Composante | Valeur Ajustée | Règle appliquée |
|---|---|---|
| Score Catalyseur | **7.7 / 10** | Malus earnings anomalie persistante −0.3 pt |
| Score Valorisation | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | **4.0 / 10** | Inchangé |
| **Score Opportunité** | **~5.7 / 10** | (7.7×0.35) + (5.0×0.40) + (4.0×0.25) |
| **Score Global** | **57.0 / 100** | 5.7 × 10 |
| Malus sectoriel XLC bottom 3 | **−0.5 pt** | Composite |
| **Score Global Ajusté** | **~56.5 / 100** | Zone 50–59 |
| **Recommandation analyste** | **ATTENDRE** | |

**Note :** La résolution de l'anomalie options JSON ne modifie pas mécaniquement le scoring (les agents n'intègrent pas de bonus options explicite dans leur modèle), mais elle réactive un setup technique latent positif (short squeeze) qui pourrait justifier un relèvement du Score Catalyseur si un catalyseur déclencheur apparaît.

---

## 6. Révision des Niveaux SL / TP

Inchangés vs snapshot 10h :

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.54 | — |
| Stop-Loss | **$8.10** | 2× ATR (−15.1%) |
| Take-Profit | **$11.70** | 3× ATR (+22.6%) |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$9.44** | Low 08/06 |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$10.16** | Previous close |
| Résistance | **$10.96** | MM50 |
| Résistance majeure | **$11.00–$13.00** | Zone max pain / historique |

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE ATTENDRE CONFIRMÉE (~56.5/100). Stabilité totale des données marché vs snapshot 10h, avec résolution majeure de l'anomalie options JSON (max pain $13.00, put/call 0.25, call OI 79.7%).**

La thèse **ATTENDRE** du snapshot 10h est **confirmée** sur base de deux observations :

1. **Stabilité totale des prix et indicateurs** — Aucune variation de cours, volume, RSI, ATR ou MM50 entre 10h et 13h UTC. La détérioration technique majeure (gap −6.1%, cours $9.54, spot −12.96% sous MM50) reste le cadre de référence.

2. **Résolution de l'anomalie options et réactivation du setup short squeeze** — La structure options est désormais fiable : max pain $13.00, put/call 0.25, call OI 79.7%. Le spot à −26.6% sous le max pain réactive l'aimant haussier mécanique vers $13.00 à échéance J+4 (2026-06-12). Le short interest 25.03% combiné à cette structure reconstitue un setup de short squeeze quantifiable. C'est un élément latent positif mais pas un catalyseur actif en l'absence de news ou de résolution earnings.

**Recommandation finale :** **ATTENDRE.** La structure options haussière est un élément technique latent favorable, mais le cours n'y a pas réagi ($9.54 stable). Le franchissement profond sous MM50 (−12.96%) et l'absence de catalyseur positif (earnings jour J non résolu, silence médiatique) maintiennent la thèse neutre. Surveiller l'échéance options du 2026-06-12 comme catalyseur technique potentiel, ainsi que toute résolution de l'anomalie earnings. Un retour au-dessus de MM50 ($10.96) avec volume confirmé (>1.0×) reste la condition préalable à toute réactivation haussière.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-06-08 (snapshot 13:00 UTC)*  
*Sources : data/latest.json (fetched 2026-06-08T13:00:01Z), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json*
