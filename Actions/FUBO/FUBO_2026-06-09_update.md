# FUBO — Mise à Jour (2026-06-09, snapshot 10h UTC)

> **Niveau d'impact :** 🟢 Faible — **Stabilité totale** vs close 08/06 : cours **$9.70** inchangé, volume **904k** (0.75× moy. 20j) stable, RSI **52.43** inchangé, ATR **$0.74** (+$0.01). **Agent : ACHETER Réduit maintenu** (61.2/100), Score Opportunité **6.9/10**, Catalyseur **8.0**, Valorisation **7.0**, Momentum **5.3**, timing **Défavorable**. Anomalie options JSON récurrente (max pain $3.00 aberrant vs $13.00 opérationnel). Anomalie earnings Q1 jour J persistante (`days_until: 0`). Analyste maintient **ATTENDRE** (~58.5/100).
> **Référence précédente :** [FUBO_2026-06-08_update.md](FUBO_2026-06-08_update.md) (snapshot 21:00 UTC 08/06)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-08 21:00 UTC)

| Métrique | 2026-06-08 21:00 UTC | **2026-06-09 10:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.70 | **$9.70** | **0.00%** (stable) |
| Volume séance | 898 262 | **904 000** | **+0.6%** (0.7× → **0.75×** moy. 20j) |
| RSI 14j | 52.43 | **52.43** | **Inchangé** |
| ATR 14j | $0.73 | **$0.74** | **+$0.01** (stable) |
| MM 50j | $10.96 | **$10.96** | Inchangé |
| Spot vs MM50 | −11.5% | **−11.5%** | Inchangé |
| Max Pain (opérationnel) | $13.00 | **$13.00** | Inchangé (valeurs JSON aberrantes $3.00 — voir §4) |
| Put/Call Ratio | 0.25 | **0.25** | Inchangé |
| Call OI % | 79.7% | **79.7%** | Inchangé |
| Échéance options | 2026-06-12 | **2026-06-12** | J+3 |
| Short Interest | 25.03% | **25.03%** | Inchangé |
| **Score Global ajusté (agent)** | 61.2/100 | **61.2/100** | **Stable** |
| **Score Opportunité (agent)** | 6.9/10 | **6.9/10** | Stable |
| **Score Momentum (agent)** | 5.3/10 | **5.3/10** | Stable |
| **Recommandation (agent)** | ACHETER Réduit | **ACHETER Réduit** | Stable |
| Timing | Défavorable | **Défavorable** | Stable |

**Constats :**
1. **Stabilité totale des données de marché** — Aucun changement significatif entre le close du 08/06 et le snapshot 10h UTC du 09/06. Le cours $9.70, le RSI 52.43, la MM50 $10.96 et le volume ~0.75× sont tous alignés avec les niveaux du snapshot précédent.
2. **Volume stable sous la moyenne** — 904k vs 1.21M moy. 20j (0.75×). La liquidité reste réduite, sans signe d'afflux institutionnel. [VOLUME INSUFFISANT]
3. **Agent maintient ACHETER Réduit** — Aucune mutation de scoring agent (61.2/100, Score Opportunité 6.9/10, Catalyseur 8.0, Valorisation 7.0, Momentum 5.3). Le timing reste Défavorable (sous MM50).
4. **Anomalie options JSON récurrente** — `data/latest.json` retourne `max_pain: $3.00` pour FUBO, valeur aberrante par rapport à l'historique opérationnel ($10.00–$13.00 sur les 30 derniers jours). Les valeurs opérationnelles ($13.00, put/call 0.25, call OI 79.7%) sont conservées pour l'analyse. [ANOMALIE JSON RÉCURRENTE]
5. **Anomalie earnings Q1 2026 persistante** — `upcoming_events_latest.json` (2026-06-09) place toujours l'earnings au **2026-06-09** (jour J, `days_until: 0`). Aucun résultat Q1 visible dans les données. C'est la 22ème session consécutive avec cette anomalie calendrier. [ANOMALIE PERSISTANTE]
6. **Données fondamentales stables** — Aucun changement dans les ratios FMP ou le consensus (price target $50.25, 4 analysts, 0 mise à jour récente).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 52.43 | Neutre médian — stable au-dessus de 50 |
| MM 50j | $10.96 | Cours sous MM50 — écart stable à −11.5% |
| ATR 14j | $0.74 | Volatilité stable (7.63% du spot) |
| Volume vs 20j | 0.75× | Stable sous la moyenne — pas de confirmation d'afflux |
| Beta | 2.392 | Extrême |
| 52W High / Low | $56.64 / $8.31 | Distance 52W low : +16.7% |
| Short Interest | 25.03% | Très élevé — stable |

**Options (valeurs opérationnelles conservées, anomalie JSON traitée) :**

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain (opérationnel) | $13.00 | Spot −25.4% sous max pain |
| Put/Call Ratio | 0.25 | Très faible — biais haussier |
| Call OI % | 79.7% | Dominance call — structure haussière |
| Échéance | 2026-06-12 | J+3 |

**Lecture institutionnelle :** L'absence de variation inter-session confirme la phase de consolidation latente de FUBO autour de $9.50–$9.90. Le RSI à 52.43 reste dans la zone neutre favorable mais sans momentum directionnel. Le franchissement persistant sous la MM50 ($10.96) maintient le timing défavorable. La structure options reste haussière avec un aimant mécanique vers $13.00 à J+3, mais le marché ne semble pas trader cette asymétrie activement en l'absence de catalyseur. Le short interest 25.03% combiné à la structure call dominante maintient un setup de short squeeze latent, mais dormant. L'anomalie JSON max pain $3.00 est traitée comme un artefact technique sans impact sur l'analyse opérationnelle.

**Niveaux clés :**
- Support immédiat : **$9.40** (low 09/06)
- Support psychologique : **$9.00**
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$9.99** (high 09/06)
- Résistance : **$10.16** (previous close 07/06)
- Résistance : **$10.96** (MM50)
- Résistance majeure : **$11.00–$13.00** (zone max pain / ancienne structure)
- Stop-loss ATR (2×) : **$8.22** (−15.3%)
- Take-profit ATR (3×) : **$11.92** (+22.9%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — cours sous MM50 (−11.5%), momentum neutre sans direction claire. La structure options haussière reste un facteur latent positif mais pas un catalyseur actif.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 10h UTC. Divergence Yahoo/FMP inchangée :

| Source | Market Cap | P/E | P/B |
|---|---|---|---|
| Yahoo Finance | $285.5M | 2.53x | 0.35x |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x |

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à **5/10** en analyse manuelle.

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)
- Price Target Moyen : **$50.25** (4 analysts, 0 mise à jour récente) — écart +418.0%, consensus figé.

### News & Événements Corporates
- `data/events_latest.json` (2026-06-09) : **vide** — aucun événement corporate.
- **Earnings Q1 2026** : anomalie calendrier persistante (`days_until: 0`), aucun résultat visible. Cette anomalie est documentée depuis le 2026-05-17 (22 sessions).

### FX Exposure / Social Sentiment / Sector Rotation / Geo Risk / Quant
- FX Impact **0.0/10** (exposition nulle).
- Social Sentiment **0.0/10** (silence total, 0 mention Reddit).
- Sector Rotation : XLC **bottom 3** (momentum score 0.0 / 10) — malus sectoriel **−0.5 pt** actif.
- Quant Report : insuffisant (pas assez de signaux historiques).
- Geo Risk : pas de flag spécifique sur FUBO.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)
Score Global **69.2/100** (brut), Score Global Ajusté **61.2/100**, Score Opportunité **6.9/10**, Score Catalyseur **8.0/10**, Score Valorisation **7.0/10**, Score Momentum **5.3/10**, Recommandation **ACHETER Réduit**, Timing **Défavorable**.

### Scoring ajusté analyste

| Composante | Valeur Ajustée | Règle appliquée |
|---|---|---|
| Score Catalyseur | **7.5 / 10** | Malus earnings anomalie persistante −0.3 pt, malus volume insuffisant −0.2 pt |
| Score Valorisation | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | **5.0 / 10** | Stable sous MM50, RSI neutre sans direction |
| **Score Opportunité** | **~5.9 / 10** | (7.5×0.35) + (5.0×0.40) + (5.0×0.25) |
| **Score Global** | **~59.0 / 100** | 5.9 × 10 |
| Malus sectoriel XLC bottom 3 | **−0.5 pt** | Composite |
| **Score Global Ajusté** | **~58.5 / 100** | Zone 50–59 |
| **Recommandation analyste** | **ATTENDRE** | Zone 50–59 : Qualité présente mais pas de catalyseur clair |

**Note :** L'agent maintient ACHETER Réduit (61.2) avec des composantes Catalyseur et Valorisation très élevées. Cependant, l'analyste maintient **ATTENDRE** (~58.5) car le plafonnement Qualité 1/6 limite la valorisation fondamentale à 5/10, le volume 0.75× reste sous la moyenne (pas de confirmation d'afflux institutionnel), le timing défavorable persiste (sous MM50) et l'anomalie earnings jour J non résolue constitue un risque de calendrier. L'upgrade agent est noté comme un signal positif mais non suivi en l'état.

---

## 6. Révision des Niveaux SL / TP

Stables avec le cours inchangé :

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.70 | — |
| Stop-Loss | **$8.22** | 2× ATR (−15.3%) |
| Take-Profit | **$11.92** | 3× ATR (+22.9%) |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$9.40** | Low 09/06 |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$9.99** | High 09/06 |
| Résistance | **$10.16** | Previous close 07/06 |
| Résistance | **$10.96** | MM50 |
| Résistance majeure | **$11.00–$13.00** | Zone max pain / historique |

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE ATTENDRE CONFIRMÉE (~58.5/100). Stabilité totale des données vs close 08/06. Aucun catalyseur nouveau. Anomalies techniques persistantes.**

La thèse **ATTENDRE** du snapshot 08/06 21h UTC est **confirmée** avec trois observations principales :

1. **Stabilité totale des données de marché** — Cours, RSI, volume, ATR, MM50 et scores agents tous inchangés entre le close du 08/06 et le snapshot 10h UTC du 09/06. Cette stabilité confirme l'absence de momentum directionnel et la phase de consolidation latente.

2. **Anomalie options JSON récurrente** — Le `max_pain: $3.00` retourné par `data/latest.json` est à nouveau aberrant (vs $13.00 opérationnel). Cette anomalie a été documentée sur plusieurs sessions précédentes (06/01, 06/03, 06/08) et est traitée comme un artefact technique sans impact sur l'analyse. Les valeurs opérationnelles ($13.00, put/call 0.25, call OI 79.7%) sont conservées.

3. **Anomalie earnings jour J persistante** — 22 sessions consécutives avec `days_until: 0` sans résultats visibles. Ce phénomène constitue un risque opérationnel majeur pour la qualité des données et limite la confiance dans tout catalyseur fondamental à court terme.

**Recommandation finale :** **ATTENDRE.** Aucune mutation de données entre le 08/06 et le 09/06. Les conditions d'entrée ne sont pas réunies : cours sous MM50 (−11.5%), volume sous la moyenne, timing défavorable, earnings Q1 jour J non résolu après 22 sessions, qualité fondamentale dégradée 1/6. La structure options haussière (max pain $13.00, put/call 0.25, call OI 79.7%) et le short interest 25.03% maintiennent un setup latent favorable, mais il nécessite un catalyseur déclencheur (résolution earnings, upgrade/downgrade, ou volume confirmé >1.0× avec clôture au-dessus de MM50). **Un retour au-dessus de MM50 ($10.96) avec volume confirmé (>1.0×) reste la condition préalable à toute réactivation haussière et au suivi de l'upgrade agent ACHETER Réduit.**

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-06-09 (snapshot 10:00 UTC)*  
*Sources : data/latest.json (fetched 2026-06-09T10:00:15Z), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json*
