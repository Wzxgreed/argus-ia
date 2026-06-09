# FUBO — Mise à Jour (2026-06-09, close officielle 21h UTC)

> **Niveau d'impact :** 🟢 Faible — **Légère progression technique** (+0.31% à $9.73) sur volume retraité (0.65×), RSI progresse à 54.12 (+1.69 pt), écart sous MM50 légèrement réduit à −11.3%. **Agent légèrement downgradé** (Score Global ajusté 60.5/100, −0.7 pt vs 13h) sur recul du Momentum (5.0/10, −0.3 pt). Structure options haussière inchangée (max pain $13.00, put/call 0.23, call OI 81.0%). Anomalie earnings Q1 persistante (24 sessions). Analyste maintient **ATTENDRE** (~58.5/100).
> **Référence précédente :** [FUBO_2026-06-09_update.md](FUBO_2026-06-09_update.md) (snapshot 13:00 UTC 09/06)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-09 13h UTC)

| Métrique | 2026-06-09 13h UTC | **2026-06-09 21h UTC** | Variation |
|---|---|---|---|
| Cours close | $9.70 | **$9.73** | **+0.31%** |
| Volume séance | 904 000 | **760 665** | **−15.8%** (0.65× moy. 20j) |
| RSI 14j | 52.43 | **54.12** | **+1.69 pt** (neutre médian) |
| ATR 14j | $0.74 | **$0.74** | **Stable** |
| MM 50j | $10.96 | **$10.97** | **+$0.01** |
| Spot vs MM50 | −11.5% | **−11.3%** | **Resserrement +0.2 pp** |
| Max Pain (API) | $13.00 | **$13.00** | Inchangé |
| Put/Call Ratio | 0.23 | **0.23** | Inchangé |
| Call OI % | 81.0% | **81.0%** | Inchangé |
| Échéance options | 2026-06-12 | **2026-06-12** | J+3 |
| Short Interest | 25.03% | **25.03%** | Inchangé |
| **Score Global brut (agent)** | 69.2/100 | **68.5/100** | **−0.7 pt** |
| **Score Global ajusté (agent)** | 61.2/100 | **60.5/100** | **−0.7 pt** |
| **Score Opportunité (agent)** | 6.9/10 | **6.8/10** | **−0.1 pt** |
| **Score Momentum (agent)** | 5.3/10 | **5.0/10** | **−0.3 pt** |
| **Recommandation (agent)** | ACHETER Réduit | **ACHETER Réduit** | Stable |
| Timing | Défavorable | **Défavorable** | Stable |

**Constats :**
1. **Micro-progression technique** — Le cours gagne 3cts (+0.31%) à $9.73 en close officielle, avec un high à $10.13 et un low à $9.495. Le RSI progresse de 52.43 à 54.12, restant dans la zone neutre favorable sans surchauffe. L'écart sous MM50 se resserre marginalement de −11.5% à −11.3%. [LÉGÈRE AMÉLIORATION TECHNIQUE]
2. **Volume retraité sous la moyenne** — 760 665 actions vs 904 000 au snapshot 13h (−15.8%) et vs 1 168 898 moy. 20j (0.65×). La liquidité s'est encore réduite en fin de séance, confirmant l'absence d'afflux institutionnel et une participation faible sur la progression. [VOLUME INSUFFISANT]
3. **Agent légèrement downgradé** — Le Score Global brut recule de 69.2 à 68.5 (−0.7 pt) et le Score Global ajusté de 61.2 à 60.5 (−0.7 pt). Le Score Opportunité cède 0.1 pt (6.8/10) et le Score Momentum 0.3 pt (5.0/10). Le Catalyseur (8.0) et la Valorisation (7.0) sont maintenus. L'agent conserve **ACHETER Réduit** avec un timing **Défavorable**. [DÉGRADATION MARGINAL AGENT]
4. **Structure options haussière inchangée** — Max pain confirmé à **$13.00**, put/call **0.23**, call OI **81.0%**. Le spot reste à **−25.4%** sous le max pain, maintenant l'aimant mécanique haussier vers $13.00 à l'échéance J+3 (2026-06-12). [STRUCTURE INTACTE]
5. **Anomalie earnings Q1 2026 persistante** — `upcoming_events_latest.json` (2026-06-09) continue de placer l'earnings au **2026-06-09** (`days_until: 0`, source FMP). Aucun résultat (EPS, revenue, guidance) n'est visible dans `data/latest.json`. C'est la **24ème session consécutive** avec cette anomalie. [ANOMALIE PERSISTANTE]
6. **Données fondamentales stables** — Divergence Yahoo/FMP inchangée (market cap $286.4M vs ~$3.27B, P/B 0.35x vs 3.19x). Filtre Qualité 1/6 confirmé. Consensus analystes figé à $50.25 (4 analysts, 0 mise à jour).

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 54.12 | Neutre médian — légère progression sans surchauffe |
| MM 50j | $10.97 | Cours sous MM50 — écart réduit à −11.3% |
| ATR 14j | $0.74 | Volatilité stable (7.61% du spot) |
| Volume vs 20j | 0.65× | Retraité sous la moyenne — pas de confirmation d'afflux |
| Beta | 2.392 | Extrême |
| 52W High / Low | $56.64 / $8.31 | Distance 52W low : +17.1% |
| Short Interest | 25.03% | Très élevé — stable |

**Options (données JSON 21h UTC) :**

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain (API) | $13.00 | Spot −25.4% sous max pain — aimant haussier intact |
| Put/Call Ratio | 0.23 | Très faible — biais haussier stable |
| Call OI % | 81.0% | Dominance call maintenue — structure haussière intacte |
| Échéance | 2026-06-12 | J+3 |

**Lecture institutionnelle :** La séance du 09/06 se caractérise par une micro-progression (+0.31%) sans conviction volume (0.65×). Le RSI à 54.12 reste dans la zone neutre favorable mais sans momentum directionnel marqué. Le franchissement persistant sous la MM50 ($10.97) maintient le timing défavorable malgré le resserrement marginal de l'écart. La structure options reste le principal facteur technique positif : max pain $13.00, put/call 0.23 et call OI 81.0% valident un aimant mécanique haussier avec un horizon J+3. Le short interest 25.03% combiné à cette structure call dominante maintient un setup de short squeeze latent, mais dormant en l'absence de catalyseur déclencheur et de volume confirmé.

**Niveaux clés :**
- Support immédiat : **$9.495** (low 09/06)
- Support psychologique : **$9.00**
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$10.13** (high 09/06)
- Résistance : **$10.16** (previous close 07/06)
- Résistance : **$10.97** (MM50)
- Résistance majeure : **$11.00–$13.00** (zone max pain / ancienne structure)
- Stop-loss ATR (2×) : **$8.25** (−15.2%)
- Take-profit ATR (3×) : **$11.95** (+22.8%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — cours sous MM50 (−11.3%), momentum neutre sans direction claire malgré la micro-progression RSI. La structure options haussière reste un facteur latent positif mais pas un catalyseur actif en l'absence de volume.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 21h UTC. Divergence Yahoo/FMP inchangée :

| Source | Market Cap | P/E | P/B |
|---|---|---|---|
| Yahoo Finance | $286.4M | 2.53x | 0.35x |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x |

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à **5/10** en analyse manuelle.

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)
- Price Target Moyen : **$50.25** (4 analysts, 0 mise à jour récente) — écart +416.4%, consensus figé.

### News & Événements Corporates
- `data/events_latest.json` : **aucun événement corporate détecté** (0 events, 2026-06-09).
- **Earnings Q1 2026** : anomalie calendrier persistante (24 sessions avec `days_until: 0`), aucun résultat visible.

### FX Exposure / Social Sentiment / Sector Rotation / Geo Risk / Quant
- FX Impact **0.0/10** (exposition nulle, divergence aligned).
- Social Sentiment **0.0/10** (silence total, 0 mention Reddit).
- Sector Rotation : XLC **bottom 3** (momentum score 0.0 / 10) — malus sectoriel **−0.5 pt** actif.
- Quant Report : insuffisant (date 2026-05-17, pas assez de signaux historiques).
- Geo Risk : pas de flag spécifique sur FUBO.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)
Score Global **68.5/100** (brut), Score Global Ajusté **60.5/100**, Score Opportunité **6.8/10**, Score Catalyseur **8.0/10**, Score Valorisation **7.0/10**, Score Momentum **5.0/10**, Recommandation **ACHETER Réduit**, Timing **Défavorable**.

### Scoring ajusté analyste

| Composante | Valeur Ajustée | Règle appliquée |
|---|---|---|
| Score Catalyseur | **7.5 / 10** | Malus earnings anomalie persistante −0.3 pt (24 sessions), malus volume retraité 0.65× −0.2 pt |
| Score Valorisation | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | **5.0 / 10** | Stable sous MM50, RSI neutre sans direction, léger recul agent −0.3 pt |
| **Score Opportunité** | **~5.9 / 10** | (7.5×0.35) + (5.0×0.40) + (5.0×0.25) |
| **Score Global** | **~59.0 / 100** | 5.9 × 10 |
| Malus sectoriel XLC bottom 3 | **−0.5 pt** | Composite |
| **Score Global Ajusté** | **~58.5 / 100** | Zone 50–59 |
| **Recommandation analyste** | **ATTENDRE** | Zone 50–59 : Qualité présente mais pas de catalyseur clair |

**Note :** L'agent maintient ACHETER Réduit (60.5) avec des composantes Catalyseur et Valorisation très élevées. L'analyste maintient **ATTENDRE** (~58.5) car le plafonnement Qualité 1/6 limite la valorisation fondamentale à 5/10, le volume 0.65× est encore plus retraité qu'au snapshot 13h (pas de confirmation d'afflux institutionnel), le timing défavorable persiste (sous MM50), l'anomalie earnings jour J non résolue constitue un risque de calendrier après 24 sessions, et l'agent a lui-même downgradé son Score Momentum (−0.3 pt). La structure options haussière (max pain $13.00, put/call 0.23, call OI 81.0%) reste un signal confirmatoire de structure mais ne constitue pas un catalyseur directionnel actif.

---

## 6. Révision des Niveaux SL / TP

Révisés avec le close officiel $9.73 :

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.73 | Close officielle 21h UTC |
| Stop-Loss | **$8.25** | 2× ATR (−15.2%) |
| Take-Profit | **$11.95** | 3× ATR (+22.8%) |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$9.495** | Low 09/06 |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$10.13** | High 09/06 |
| Résistance | **$10.16** | Previous close 07/06 |
| Résistance | **$10.97** | MM50 |
| Résistance majeure | **$11.00–$13.00** | Zone max pain / historique |

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE ATTENDRE CONFIRMÉE (~58.5/100). Micro-progression technique sans conviction (+0.31% sur volume retraité 0.65×). Structure options haussière inchangée. Anomalie earnings persistante (24 sessions). Agent légèrement downgradé.**

La thèse **ATTENDRE** du snapshot 13h UTC est **confirmée** avec quatre observations principales :

1. **Micro-progression technique sans conviction** — Le cours gagne 3cts (+0.31%) à $9.73, mais le volume recule de 904k à 760k (0.65× moy. 20j). Cette progression sur volume décroissant confirme l'absence de momentum directionnel et de participation institutionnelle. Le RSI progresse à 54.12 (+1.69 pt) sans franchir de seuil significatif.

2. **Agent légèrement downgradé** — Le Score Global ajusté recule de 61.2 à 60.5 (−0.7 pt), le Score Opportunité de 6.9 à 6.8 (−0.1 pt) et le Score Momentum de 5.3 à 5.0 (−0.3 pt). Cette auto-dégradation de l'agent confirme que la micro-progression de cours n'est pas interprétée comme un signal technique positif. L'agent conserve néanmoins **ACHETER Réduit**.

3. **Structure options haussière inchangée** — Max pain **$13.00**, put/call **0.23**, call OI **81.0%** — le spot à **−25.4%** sous le max pain maintient l'aimant mécanique haussier vers $13.00 à échéance J+3 (2026-06-12). Ce facteur reste le principal soutien technique latent mais non actif.

4. **Anomalie earnings jour J persistante** — 24 sessions consécutives avec `days_until: 0` sans résultats visibles. Ce phénomène constitue un risque opérationnel majeur pour la qualité des données et limite la confiance dans tout catalyseur fondamental à court terme.

**Recommandation finale :** **ATTENDRE.** Les conditions d'entrée ne sont pas réunies : cours sous MM50 (−11.3%), volume retraité sous la moyenne (0.65×), timing défavorable, earnings Q1 jour J non résolu après 24 sessions, qualité fondamentale dégradée 1/6, et agent auto-downgradé sur le Momentum. La structure options haussière (max pain $13.00, put/call 0.23, call OI 81.0%) et le short interest 25.03% maintiennent un setup latent favorable, mais il nécessite un catalyseur déclencheur (résolution earnings, upgrade/downgrade, ou volume confirmé >1.0× avec clôture au-dessus de MM50). **Un retour au-dessus de MM50 ($10.97) avec volume confirmé (>1.0×) reste la condition préalable à toute réactivation haussière et au suivi de l'upgrade agent ACHETER Réduit.**

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-06-09 (close officielle 21:00 UTC)*  
*Sources : data/latest.json (fetched 2026-06-09T21:00:02Z), data/recommandations_latest.json (2026-06-09), data/sector_rotation_latest.json (2026-06-09), data/social_sentiment_latest.json (2026-06-09), data/upcoming_events_latest.json (2026-06-09), data/events_latest.json (2026-06-09)*
