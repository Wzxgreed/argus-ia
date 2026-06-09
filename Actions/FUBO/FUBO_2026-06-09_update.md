# FUBO — Mise à Jour (2026-06-09, snapshot 13h UTC)

> **Niveau d'impact :** 🟢 Faible — **Stabilité totale des données de marché** vs snapshot 10h UTC : cours **$9.70** inchangé, volume **904k** (0.75× moy. 20j), RSI **52.43** stable, ATR **$0.74** stable. **Anomalie options JSON RÉSOLUE** (max pain $13.00 cohérent vs $3.00 aberrant à 10h, put/call **0.23**, call OI **81.0%** — structure haussière légèrement renforcée). **Agent : ACHETER Réduit maintenu** (61.2/100), Score Opportunité **6.9/10**, Catalyseur **8.0**, Valorisation **7.0**, Momentum **5.3**, timing **Défavorable**. Anomalie earnings Q1 jour J persistante (`days_until: 0`, 23ème session). Analyste maintient **ATTENDRE** (~58.5/100).
> **Référence précédente :** [FUBO_2026-06-09_update.md](FUBO_2026-06-09_update.md) (snapshot 10:00 UTC 09/06)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-09 10h UTC)

| Métrique | 2026-06-09 10h UTC | **2026-06-09 13h UTC** | Variation |
|---|---|---|---|
| Cours close | $9.70 | **$9.70** | **0.00%** (stable) |
| Volume séance | 904 000 | **904 000** | **Inchangé** (0.75× moy. 20j) |
| RSI 14j | 52.43 | **52.43** | **Inchangé** |
| ATR 14j | $0.74 | **$0.74** | **Stable** |
| MM 50j | $10.96 | **$10.96** | Inchangé |
| Spot vs MM50 | −11.5% | **−11.5%** | Inchangé |
| Max Pain (API) | $3.00 (aberrant) | **$13.00** | **Anomalie RÉSOLUE** |
| Put/Call Ratio | 0.25 (opérationnel) | **0.23** | **Amélioration haussière** (−0.02) |
| Call OI % | 79.7% (opérationnel) | **81.0%** | **Renforcement haussier** (+1.3 pp) |
| Échéance options | 2026-06-12 | **2026-06-12** | J+3 |
| Short Interest | 25.03% | **25.03%** | Inchangé |
| **Score Global ajusté (agent)** | 61.2/100 | **61.2/100** | **Stable** |
| **Score Opportunité (agent)** | 6.9/10 | **6.9/10** | Stable |
| **Score Momentum (agent)** | 5.3/10 | **5.3/10** | Stable |
| **Recommandation (agent)** | ACHETER Réduit | **ACHETER Réduit** | Stable |
| Timing | Défavorable | **Défavorable** | Stable |

**Constats :**
1. **Stabilité totale des données de marché** — Cours, volume, RSI, ATR et MM50 inchangés entre 10h et 13h UTC. Aucune mutation technique ou fondamentale sur la séance.
2. **Anomalie options JSON RÉSOLUE** — `data/latest.json` (fetched 2026-06-09T13:00:01Z) retourne désormais un max pain cohérent à **$13.00** (vs $3.00 aberrant à 10h UTC). Le put/call ratio s'établit à **0.23** (vs 0.25 opérationnel) et le call OI à **81.0%** (vs 79.7% opérationnel) — légère amélioration de la structure haussière. [ANOMALIE RÉSOLUE]
3. **Volume stable sous la moyenne** — 904k vs 1.21M moy. 20j (0.75×). La liquidité reste réduite, sans signe d'afflux institutionnel. [VOLUME INSUFFISANT]
4. **Agent maintient ACHETER Réduit** — Aucune mutation de scoring agent (61.2/100, Score Opportunité 6.9/10, Catalyseur 8.0, Valorisation 7.0, Momentum 5.3). Le timing reste Défavorable (sous MM50).
5. **Anomalie earnings Q1 2026 persistante** — `upcoming_events_latest.json` n'est pas disponible au snapshot 13h UTC. L'anomalie calendrier (earnings jour J sans résultats visibles) est documentée depuis 23 sessions consécutives. [ANOMALIE PERSISTANTE]
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

**Options (données JSON corrigées, anomalie résolue) :**

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain (API) | $13.00 | Spot −25.4% sous max pain — aimant haussier intact |
| Put/Call Ratio | 0.23 | Très faible — biais haussier légèrement renforcé vs 0.25 |
| Call OI % | 81.0% | Dominance call renforcée — structure haussière intacte |
| Échéance | 2026-06-12 | J+3 |

**Lecture institutionnelle :** L'absence de variation entre 10h et 13h UTC confirme la phase de consolidation latente de FUBO autour de $9.50–$9.90. Le RSI à 52.43 reste dans la zone neutre favorable mais sans momentum directionnel. Le franchissement persistant sous la MM50 ($10.96) maintient le timing défavorable. La résolution de l'anomalie options JSON valide la structure haussière : max pain $13.00 confirmé, put/call 0.23 et call OI 81.0% renforcent légèrement le biais haussier par rapport aux valeurs opérationnelles précédentes (0.25 / 79.7%). Le short interest 25.03% combiné à la structure call dominante maintient un setup de short squeeze latent, mais dormant en l'absence de catalyseur déclencheur. L'échéance options J+3 (2026-06-12) rapproche l'horizon de l'aimant mécanique vers $13.00.

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

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 13h UTC. Divergence Yahoo/FMP inchangée :

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
- `data/events_latest.json` : **fichier non disponible** au snapshot 13h UTC.
- **Earnings Q1 2026** : anomalie calendrier persistante (23 sessions avec `days_until: 0`), aucun résultat visible.

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
| Score Catalyseur | **7.5 / 10** | Malus earnings anomalie persistante −0.3 pt, malus volume insuffisant −0.2 pt ; bonus anomalie options résolue +0.0 pt (information confirmatoire, non catalyseur actif) |
| Score Valorisation | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | **5.0 / 10** | Stable sous MM50, RSI neutre sans direction |
| **Score Opportunité** | **~5.9 / 10** | (7.5×0.35) + (5.0×0.40) + (5.0×0.25) |
| **Score Global** | **~59.0 / 100** | 5.9 × 10 |
| Malus sectoriel XLC bottom 3 | **−0.5 pt** | Composite |
| **Score Global Ajusté** | **~58.5 / 100** | Zone 50–59 |
| **Recommandation analyste** | **ATTENDRE** | Zone 50–59 : Qualité présente mais pas de catalyseur clair |

**Note :** L'agent maintient ACHETER Réduit (61.2) avec des composantes Catalyseur et Valorisation très élevées. L'analyste maintient **ATTENDRE** (~58.5) car le plafonnement Qualité 1/6 limite la valorisation fondamentale à 5/10, le volume 0.75× reste sous la moyenne (pas de confirmation d'afflux institutionnel), le timing défavorable persiste (sous MM50) et l'anomalie earnings jour J non résolue constitue un risque de calendrier. La résolution de l'anomalie options JSON ($13.00 confirmé, put/call 0.23, call OI 81.0%) est un signal confirmatoire de structure mais ne constitue pas un catalyseur directionnel actif.

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

### **Verdict : THÈSE ATTENDRE CONFIRMÉE (~58.5/100). Stabilité totale des données de marché. Anomalie options JSON résolue (max pain $13.00, put/call 0.23, call OI 81.0%). Aucun catalyseur nouveau. Échéance options J+3.**

La thèse **ATTENDRE** du snapshot 10h UTC est **confirmée** avec trois observations principales :

1. **Stabilité totale des données de marché** — Cours, volume, RSI, ATR, MM50 et scores agents tous inchangés entre 10h et 13h UTC. Cette stabilité confirme l'absence de momentum directionnel et la phase de consolidation latente.

2. **Anomalie options JSON RÉSOLUE** — Le `max_pain: $3.00` aberrant du snapshot 10h UTC est corrigé à **$13.00** dans `data/latest.json` (fetched 13h UTC). Le put/call ratio est confirmé à **0.23** (vs 0.25 opérationnel précédent) et le call OI à **81.0%** (vs 79.7%). Cette résolution valide la structure haussière et renforce légèrement le biais call, mais ne constitue pas un catalyseur directionnel actif. L'échéance J+3 (2026-06-12) rapproche l'horizon de l'aimant mécanique vers $13.00.

3. **Anomalie earnings jour J persistante** — 23 sessions consécutives avec `days_until: 0` sans résultats visibles. Ce phénomène constitue un risque opérationnel majeur pour la qualité des données et limite la confiance dans tout catalyseur fondamental à court terme.

**Recommandation finale :** **ATTENDRE.** Aucune mutation de données entre 10h et 13h UTC. Les conditions d'entrée ne sont pas réunies : cours sous MM50 (−11.5%), volume sous la moyenne, timing défavorable, earnings Q1 jour J non résolu après 23 sessions, qualité fondamentale dégradée 1/6. La structure options haussière (max pain $13.00, put/call 0.23, call OI 81.0%) et le short interest 25.03% maintiennent un setup latent favorable, mais il nécessite un catalyseur déclencheur (résolution earnings, upgrade/downgrade, ou volume confirmé >1.0× avec clôture au-dessus de MM50). **Un retour au-dessus de MM50 ($10.96) avec volume confirmé (>1.0×) reste la condition préalable à toute réactivation haussière et au suivi de l'upgrade agent ACHETER Réduit.**

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-06-09 (snapshot 13:00 UTC)*  
*Sources : data/latest.json (fetched 2026-06-09T13:00:01Z), data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/quality_report_latest.json (2026-05-17)*
