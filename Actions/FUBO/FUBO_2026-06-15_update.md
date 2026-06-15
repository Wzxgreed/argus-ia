# FUBO — Mise à Jour (2026-06-15, snapshot 10h UTC)

> **Niveau d'impact :** 🔴 Élevé — **Gap down -6.11%** à $9.83 sur **volume en explosion 1.36×** (1 745 900 vs moy. 20j 1 284 230), **ATR spike +16.4%** à $0.85, RSI retraité à **50.56** (−3.56 pts vs close 09/06), écart sous MM50 creusé à **−10.9%**. Données options JSON anomalie persistante (max pain $3.00 / call OI 0% → valeurs opérationnelles conservées : max pain **$13.00**, call OI **81.0%**). Échéance options **J+3** (2026-06-18). Anomalie earnings Q1 persistante — calendrier FMP jour J non résolu après ~30 sessions.
> **Référence précédente :** [FUBO_2026-06-09_update.md](FUBO_2026-06-09_update.md) (close officielle 21h UTC $9.73)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-09 21h UTC)

| Métrique | 2026-06-09 21h UTC | **2026-06-15 10h UTC** | Variation |
|---|---|---|---|
| Cours close | $9.73 | **$9.83** | **+1.03% inter-snapshot**, session −6.11% |
| Previous close | $9.70 | **$10.47** | — |
| Volume séance | 760 665 | **1 745 900** | **+129.5%** (1.36× moy. 20j) |
| RSI 14j | 54.12 | **50.56** | **−3.56 pts** |
| ATR 14j | $0.74 | **$0.85** | **+$0.11 (+16.4%)** [ATR_SPIKE] |
| MM 50j | $10.97 | **$11.03** | +$0.06 |
| Spot vs MM50 | −11.3% | **−10.9%** | Légèrement amélioré (MM50 monte) |
| Beta | 2.392 | **2.392** | Stable |
| Short Interest | 25.03% | **24.32%** | **−0.71 pp** |
| 52W High / Low | $56.64 / $8.31 | **$56.64 / $8.31** | Stable |
| Max Pain (opérationnel) | $13.00 | **$13.00** | Inchangé |
| Put/Call Ratio (opérationnel) | 0.23 | **0.23** | Inchangé |
| Call OI % (opérationnel) | 81.0% | **81.0%** | Inchangé |
| Échéance options | 2026-06-12 | **2026-06-18** | Repoussée J+3 |
| **Score Global ajusté (analyste)** | ~58.5/100 | **~43.0/100** | **Downgrade −15.5 pts** |
| **Score Opportunité (analyste)** | ~5.9/10 | **~4.3/10** | **−1.6 pt** |
| **Recommandation (analyste)** | ATTENDRE | **SURVEILLER** | **Downgrade** |

**Constats :**
1. **Gap down -6.11%** — Le cours ouvre à $10.25, plonge en séance jusqu'à $9.42 (low du jour), et clôture à $9.83. Le previous close de $10.47 suggère que le titre avait remonté entre le 9 et le 14 juin, avant ce gap down brutal.
2. **Volume de liquidation 1.36×** — 1.75M actions échangées vs moyenne 1.28M. C'est le volume le plus élevé depuis le 2 juin. Sur un gap down, ce volume élevé traduit une pression vendeuse active et un désengagement des positions, pas une accumulation.
3. **ATR spike +16.4%** — L'ATR passe de $0.74 à $0.85, confirmant l'expansion de la volatilité. Le ratio ATR/spot atteint 8.65%, au-dessus du seuil institutionnel de 5.0%.
4. **RSI retraité à 50.56** — Sortie de la zone neutre médiane-haute (54.12) vers la médiane. Pas de survente, mais perte de momentum.
5. **Short interest légèrement baissé** — 24.32% (−0.71 pp). Le léger recul du short interest combiné au volume élevé pourrait indiquer des couvertures partielles, mais le niveau reste extrêmement élevé.
6. **Données options JSON anomalie persistante** — `latest.json` affiche max pain $3.00 et call OI 0.0%, valeurs aberrantes récurrentes depuis début juin. Les valeurs opérationnelles du 09/06 ($13.00 / 0.23 / 81.0%) sont conservées. La nouvelle échéance options est le 2026-06-18 (J+3).
7. **Anomalie earnings Q1 persistante** — `upcoming_events_latest.json` (dernière lecture 09/06) plaçait l'earnings au 2026-06-09 (jour J). À la date du 15/06, aucun résultat Q1 n'est visible dans `latest.json`. L'anomalie persiste après ~30 sessions.
8. **Divergence Yahoo/FMP Market Cap** — $289.4M (Yahoo) vs ~$3.27B (FMP) : écart ×11.3 inchangé.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 50.56 | Neutre médian — retrait de +3.56 pts |
| MM 50j | $11.03 | Cours sous MM50 — écart −10.9% |
| ATR 14j | $0.85 | Volatilité en expansion (+16.4%) |
| Volume vs 20j | 1.36× | **Élevé** — liquidation active |
| Beta | 2.392 | Extrême |
| 52W High / Low | $56.64 / $8.31 | Distance 52W low : +18.3% |
| Short Interest | 24.32% | Très élevé — légèrement retraité |

**Options (valeurs opérationnelles conservées, JSON anomalie) :**

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $13.00 | Spot −24.4% sous max pain |
| Put/Call Ratio | 0.23 | Très faible — biais haussier latent |
| Call OI % | 81.0% | Dominance call — structure haussière |
| Échéance | 2026-06-18 | J+3 |

**Lecture institutionnelle :** Le gap down -6.11% sur volume de liquidation (1.36×) est un signal technique baissier significatif. L'ATR spike à $0.85 confirme que la volatilité s'installe. Le RSI à 50.56 n'est pas encore en survente, ce qui laisse une marge de baisse technique. Le franchissement persistant sous la MM50 ($11.03) et l'écart à −10.9% maintiennent le timing défavorable.

La structure options haussière historique (max pain $13.00, call OI 81.0%) reste un facteur latent positif, mais les données corrompues du snapshot actuel ($3.00 / 0%) empêchent toute analyse options fiable à J+3. Le short interest 24.32% maintient un setup de short squeeze latent, mais il nécessite un catalyseur déclencheur qui n'est pas présent aujourd'hui.

**Niveaux clés :**
- Support immédiat : **$9.42** (low du jour 15/06)
- Support psychologique : **$9.00**
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$10.47** (previous close 14/06)
- Résistance : **$11.03** (MM50)
- Résistance majeure : **$11.50–$13.00** (zone max pain / ancienne structure)
- Stop-loss ATR (2×) : **$8.13** (−17.3%)
- Take-profit ATR (3×) : **$12.38** (+25.9%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — gap down sur volume de liquidation, cours sous MM50 (−10.9%), ATR en expansion, absence de catalyseur positif.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot du 15/06. Les ratios FMP sont inchangés (date FY 2025-12-31) :

| Source | Market Cap | P/E TTM | Forward P/E | P/B | EV/Revenue |
|---|---|---|---|---|---|
| Yahoo Finance | $289.4M | 2.56× | 20.83× | 0.36× | 0.434× |
| FMP Stable API | ~$3.27B | 5.65× | — | 3.19× | 1.281× |

**Signaux fondamentaux préoccupants :**
- **P/E TTM 2.56×** — Extrêmement bas, probablement artéfact d'un bénéfice comptable exceptionnel ou distorsion liée à la capitalisation. Le Forward P/E de 20.83× est plus représentatif de la valorisation attendue.
- **P/B 0.36× (Yahoo)** — Patrimoine net négatif confirmé par FMP (tangible asset value −$398.9M). Le P/B bas reflète une dette élevée (debt/equity 2.43) et un bilan dégradé.
- **Current ratio 0.84** — Insuffisance de liquidité à court terme.
- **FCF yield négatif** −18.9% — Pas de génération de cash libre.
- **Consensus figé** — Price target $50.25 (4 analysts, 0 mise à jour récente).

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à **5/10** en analyse manuelle.

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)
- Price Target Moyen : **$50.25** (4 analysts, 0 mise à jour récente) — écart +410.8%, consensus figé depuis plusieurs semaines.

### News & Événements Corporates
- `data/events_latest.json` : **absent** — aucun événement corporate détecté par l'agent.
- **Earnings Q1 2026** : anomalie calendrier persistante (~30 sessions avec `days_until: 0`). Le snapshot 15/06 ne montre toujours aucun résultat (EPS, revenue, guidance). [ANOMALIE NON RÉSOLUE]
- **Social Sentiment / FX Exposure / Sector Rotation / Quant** : fichiers JSON absents (`social_sentiment_latest.json`, `fx_exposure_latest.json`, `sector_rotation_latest.json`, `accounting_risk_latest.json`, `upcoming_events_latest.json`). Malus sectoriel XLC bottom 3 (−0.5 pt) maintenu sur base dernière lecture (09/06).

---

## 5. Scoring Global

### Scoring ajusté analyste (données agents indisponibles)

| Composante | Valeur Ajustée | Règle appliquée |
|---|---|---|
| Score Catalyseur | **3.5 / 10** | Pas de catalyseur actif, anomalie earnings persistante −1.0 pt, données options corrompues −0.5 pt |
| Score Valorisation | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 (Score 1/6) |
| Score Momentum | **3.5 / 10** | Gap down -6.11% sur volume élevé, ATR spike, sous MM50 |
| **Score Opportunité** | **~4.3 / 10** | (3.5×0.35) + (5.0×0.40) + (3.5×0.25) = 1.225 + 2.0 + 0.875 |
| **Score Global** | **~43.0 / 100** | 4.3 × 10 |
| Malus sectoriel XLC bottom 3 | **−0.5 pt** | Maintenu (dernière lecture 09/06) |
| **Score Global Ajusté** | **~42.5 / 100** | Zone 35–49 |
| **Recommandation analyste** | **SURVEILLER** | Zone 35–49 : Risques détectés — pas d'action |

**Note :** Le downgrade de ATTENDRE (~58.5) à SURVEILLER (~42.5) est motivé par le gap down -6.11% sur volume de liquidation (1.36×), l'ATR spike (+16.4%), et la persistance de l'anomalie earnings sans résolution. La structure options haussière historique (max pain $13.00, call OI 81.0%) et le short interest élevé (24.32%) maintiennent un setup latent favorable, mais ils sont totalement éclipsés par le momentum baissier actif et l'absence de catalyseur. Le plafonnement Qualité 1/6 empêche toute valorisation au-dessus de 5/10 en analyse fondamentale.

---

## 6. Révision des Niveaux SL / TP

Révisés à la hausse avec l'expansion de l'ATR :

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9.83 | — |
| Stop-Loss | **$8.13** | 2× ATR (−17.3%) |
| Take-Profit | **$12.38** | 3× ATR (+25.9%) |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$9.42** | Low 15/06 |
| Support psychologique | **$9.00** | — |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$10.47** | Previous close 14/06 |
| Résistance | **$11.03** | MM50 |
| Résistance majeure | **$11.50–$13.00** | Zone max pain / historique |

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE MODIFIÉE — DE ATTENDRE (~58.5/100) À SURVEILLER (~42.5/100). Gap down -6.11% sur volume de liquidation avec ATR spike confirme une détérioration technique active. L'anomalie earnings persistante et les données options corrompues aggravent le risque opérationnel.**

La thèse **ATTENDRE** du 9 juin est **modifiée à la baisse** vers **SURVEILLER** pour trois raisons principales :

1. **Gap down technique significatif sur volume de liquidation** — Le cours chute de -6.11% (previous close $10.47 → close $9.83) avec un volume en explosion de +129.5% (1.36× la moyenne). Ce n'est pas un repli ordinaire : c'est un signal de désengagement actif des participants. L'ATR spike à $0.85 (+16.4%) confirme que la volatilité monte en régime, ce qui augmente le risque de slippage sur les stops.

2. **Absence totale de catalyseur et anomalie earnings non résolue** — L'earnings Q1, attendu depuis ~30 sessions, n'a toujours pas produit de résultats visibles. Cette anomalie calendrier crée un risque de "surprise" non contrôlée. Aucune news corporate, aucun upgrade/downgrade, aucun flux institutionnel détecté (`events_latest.json` absent). Le vide informationnel est un risque en soi.

3. **Structure options non fiable à J+3** — Les données options du snapshot 15/06 (max pain $3.00, call OI 0%) sont manifestement corrompues, récurrentes depuis début juin. En l'absence de données options fiables à 3 jours de l'échéance, le setup haussier historique (max pain $13.00) ne peut plus être quantifié avec certitude. Cette incertitude technique justifie une prudence accrue.

**Recommandation finale :** **SURVEILLER.** Le gap down -6.11% sur volume de liquidation confirme une pression vendeuse active. L'anomalie earnings persistante (~30 sessions) et les données options corrompues empêchent toute prise de position en l'état. Le plafonnement Qualité 1/6 limite la valorisation fondamentale à 5/10. Le short interest 24.32% et la structure options haussière historique ($13.00) maintiennent un setup latent favorable, mais il nécessite un catalyseur déclencheur (résolution earnings, upgrade, volume confirmé à l'achat).

**Conditions de réactivation haussière (pour sortir de SURVEILLER) :**
- Retour au-dessus de **MM50 ($11.03)** avec volume confirmé **>1.0×**
- Résolution de l'anomalie earnings avec résultats Q1 supérieurs au consensus
- Données options fiables confirmant le max pain au-dessus du spot

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-06-15 (snapshot 10:00 UTC)*  
*Sources : data/latest.json (fetched 2026-06-15T10:00:13Z), data/quant_report_latest.json, data/geo_risk_latest.json, data/quality_report_latest.json — fichiers recommandations/accounting/sector/social/fx/events/upcoming_events absents au snapshot.*
