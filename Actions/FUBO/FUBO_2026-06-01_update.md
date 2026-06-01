# FUBO — Mise à Jour (2026-06-01, snapshot 10:00 UTC)

> **Niveau d'impact :** 🟡 Modéré — Évolution technique mixte : cours **$10.09 (−3.26% vs previous close)**, RSI **47.2** (+3.85 pts vs 2026-05-27 17:00 UTC), volume **1 942 000** (1.31× moy. 20j, explosion de liquidité). Short interest hausse significative **22.84% → 25.03%** (+2.19 pp). Scoring agent stable **ATTENDRE** (67.2/100, ajusté 59.2/100). Ajustement analyste inchangé **SURVEILLER (~46/100)**. Earnings Q1 2026 anomalie persistante (FMP place jour J au 2026-06-01, aucun résultat visible). Anomalie options majeure détectée : **max pain $3.00** (vs $10.00 historique), put/call et call OI passés à null.
> **Référence précédente :** [FUBO_2026-05-27_update.md](FUBO_2026-05-27_update.md) (snapshot 17:00 UTC — close $9.97, RSI 43.35, volume 920 203 / 0.64×, scoring agent 66.0/100 ATTENDRE, thèse SURVEILLER)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-27 17:00 UTC)

| Métrique | 2026-05-27 17:00 UTC | **2026-06-01 10:00 UTC** | Variation |
|---|---|---|---|
| Cours close | $9.97 | **$10.09** | **+1.2%** (mais −3.26% vs previous close $10.43) |
| Change % vs previous | +4.73% | **−3.26%** | **Recul séance** |
| Volume séance | 920 203 | **1 942 000** | **+111%** |
| Volume vs 20j | 0.64× | **1.31×** | **Retour de liquidité** |
| RSI 14j | 43.35 | **47.2** | **+3.85 pts** |
| ATR 14j | $0.55 | **$0.54** | **Stable** |
| MM 50j | $11.34 | **$11.19** | **−1.3%** |
| Market Cap (Yahoo) | $293.5M | **$297.0M** | **+1.2%** |
| P/E TTM (Yahoo) | 2.60x | **2.63x** | **Stable** |
| Forward P/E | 21.12x | **21.38x** | **+1.2%** |
| Short Interest | 22.84% | **25.03%** | **+2.19 pp** |
| Max Pain (API) | $10.00 | **$3.00** | **[ANOMALIE]** |
| Put/Call Ratio (API) | 0.51 | **null** | **Données absentes** |
| Call OI % (API) | 66.3% | **null** | **Données absentes** |
| Échéance options | 2026-05-29 | **2026-06-05** | **Nouvelle échéance** |
| **Score Global (agent)** | 66.0/100 | **67.2/100** | **+1.2 pt** |
| **Score Global Ajusté (agent)** | 58.0/100 | **59.2/100** | **+1.2 pt** |
| **Score Opportunité (agent)** | 6.6/10 | **6.7/10** | **+0.1 pt** |
| **Score Momentum (agent)** | 4.0/10 | **4.5/10** | **+0.5 pt** |
| **Recommandation (agent)** | ATTENDRE | **ATTENDRE** | **Stable** |

**Constats :**
1. **Recul séance −3.26% après rallye** — Le close passe de $9.97 à **$10.09** (+1.2% net depuis le 27/05), mais le previous close de la séance précédente était $10.43. Le titre a donc connu un rallye post-week-end vers ~$10.45 (open du jour) suivi d'un recul en séance (low $9.92). La séance dessine une mèche haute ($10.49) et un close faible, signal de rejet des niveaux supérieurs.
2. **Volume explosion (+111%)** — De 920 203 à **1 942 000**, passage de 0.64× à **1.31×** la moyenne 20j. C'est le volume le plus élevé observé depuis plusieurs semaines. Le recul de −3.26% s'effectue sur volume en hausse = **distribution potentielle** (ventes sur rallye) plutôt qu'accumulation.
3. **RSI continue de remonter** — De **43.35 à 47.2** (+3.85 pts), approchant la zone neutre (50). Amélioration technique progressive sur 5 jours (+26 pts depuis le 26/05). Cependant, le RSI reste sous 50 et le cours sous MM50 (−9.8%).
4. **Short interest hausse significative (+2.19 pp)** — Passage de 22.84% à **25.03%** du float. Les shorts s'empilent alors que le cours remonte, signalant un scepticisme institutionnel persistant. Le setup short squeeze latent s'intensifie mécaniquement (25% du float shorté = combustible élevé), mais sans catalyseur, le timing reste incertain.
5. **Anomalie options majeure** — Max pain API passe de $10.00 à **$3.00**, put/call et call OI passés à **null**. Cette discontinuité est aberrante (max pain $3.00 avec un spot à $10.09 est impossible sous une logique options standard). Probable artefact de données (changement d'échéance 2026-05-29 → 2026-06-05, reset des données OI). Les données options précédentes ($10.00, put/call 0.51, call OI 66.3%) sont plus fiables et doivent être conservées comme référence jusqu'à résolution.
6. **Agent stable en ATTENDRE (59.2/100 ajusté)** — Malgré le recul séance, le modèle quantitatif maintient la recommandation et remonte légèrement le Score Momentum (4.0 → 4.5) et le Score Global Ajusté (58.0 → 59.2). Cette contre-intuition suggère que le modèle valorise la hausse du volume et la continuité du rebond RSI plus que le recul intraday.
7. **Anomalie calendrier earnings persistante** : `data/upcoming_events_latest.json` (2026-06-01) place l'earnings au **2026-06-01** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible dans `data/latest.json`. [ANOMALIE CALENDRIER PERSISTANTE — J+? NON RÉSOLU]
8. **Validation report** (`data/validation_report.txt`, 2026-06-01) : 24/28 tickers OK, 5 errors (VRT schema, AST/AXA/QTBS/ASTSPACE fetch failed), 2 warnings (IREN, NOK). FUBO **non flaggué** — données considérées fiables.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 47.2 | **Neutre-baisse** — progression continue (+26 pts depuis 21.08 le 26/05), mais sous 50 |
| MM 50j | $11.19 | Cours sous la moyenne — écart **−9.8%** (vs −12.1% le 27/05) |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0.54 | Volatilité absolue stable (5.4% du spot) |
| Volume vs 20j | 1.31× | **Retour de liquidité** — volume supérieur à la moyenne pour la première fois depuis le 20/05 |
| Beta | 2.508 | Volatilité systématique extrême |
| 52W High / Low | $56.64 / $8.31 | Distance au 52W low : **+21.4%** (vs +20.0% le 27/05) |
| Short Interest | 25.03% | **Très élevé et haussier** — +2.19 pp en 5 jours |

**Niveaux clés :**
- Support immédiat : **$9.92** (low du jour)
- Support secondaire : **$9.53** (low du 27/05)
- Support majeur : **$8.31** (52W low)
- Résistance : **$10.49** (high du jour — rejet net en séance)
- Résistance majeure : **$11.19** (MM50 — breakout requis pour inflexion de tendance)
- Stop-loss ATR (2×) : **$9.01** (−10.7%)
- Take-profit ATR (3×) : **$11.71** (+16.1%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — sous MM50 (−9.8%), RSI neutre-baisse malgré la progression, recul de −3.26% sur volume en hausse (distribution potentielle). Le rejet du high $10.49 et la mèche haute de la séance confirment la présence de vendeurs au-dessus de $10.40. L'explosion du volume (1.31×) est le signal le plus notable : elle peut indiquer soit un changement de main (sortie des faibles mains, entrée des shorts — cohérent avec +2.19 pp de short interest), soit une distribution institutionnelle. Sans confirmation de clôture au-dessus de $10.50 sur volume soutenu, la tendance baissière primaire reste intacte.

---

## 3. Mise à Jour Fondamentale

Aucun nouveau résultat Q1 2026 ni donnée fondamentale structurante dans le snapshot 2026-06-01. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $297.0M | 2.63x | 0.37x | — |
| FMP Stable API | ~$3.27B | 5.65x | 3.19x | 16.10x |

**Écart :** ×11.0 sur la capitalisation (stable vs ×11.2 le 27/05).

### Ratios disponibles (Yahoo + FMP, close 2026-06-01)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2.63x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 21.38x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0.436x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0.37x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3.19x | Écart ×8.6 avec Yahoo |
| Beta | 2.508 | Extrême |
| Short Interest | 25.03% | Très élevé — hausse récente |
| Gross Margin (FMP) | 11.1% | Très faible |
| Operating Margin (FMP) | −2.6% | Perte opérationnelle |
| Current Ratio (FMP) | 0.84 | Illiquidité structurelle |
| Debt/Equity (FMP) | 2.43 | Levier élevé |
| Tangible Asset Value (FMP) | −$398.9M | Patrimoine net négatif |
| Net Debt/EBITDA (FMP) | 1.01x | Couverture faible |
| ROIC (FMP) | −2.1% | Destruction de valeur |
| ROE (FMP) | 56.5% | Élevé — structure de capital très levée |

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à **5/10** (règle absolue Argus-IA).

**Données Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — scan comptable non disponible pour cette session.

---

## 4. Mise à Jour Sentiment / Options / News

### Options

| Signal | Valeur 27/05 | Valeur 01/06 | Lecture |
|---|---|---|---|
| Max Pain | $10.00 | **$3.00** | **[ANOMALIE — non crédible]** |
| Put/Call Ratio | 0.51 | **null** | **Données absentes** |
| Call OI % | 66.3% | **null** | **Données absentes** |
| Échéance options | 2026-05-29 | **2026-06-05** | J+4 — reset des données |

**Lecture institutionnelle :** Les données options du snapshot 2026-06-01 sont **non exploitables** (max pain $3.00 aberrant, put/call et call OI null). Cette anomalie coïncide avec le changement d'échéance (2026-05-29 → 2026-06-05). En attendant la stabilisation des données, les valeurs du 27/05 (max pain $10.00, put/call 0.51, call OI 66.3%) restent la meilleure approximation. Le spot à $10.09 se situe à **+0.9%** au-dessus de ce max pain historique (vs −0.3% le 27/05), signalant un léger biais haussier post-échéance si les données historiques sont retenues.

Le setup short squeeze latent s'intensifie avec le short interest à **25.03%** (+2.19 pp) combiné au call OI historique dominant (66.3%). Cependant, l'absence de données options actualisées et le volume de distribution en séance (−3.26% sur 1.31×) réduisent la probabilité de déclenchement immédiat.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50.25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +398%. Consensus figé.

### News & Événements Corporates

- `data/events_latest.json` (2026-06-01) : **vide** (0 événement) — aucun M&A, buyback, guidance change ou activism détecté.
- **Earnings Q1 2026** : `data/upcoming_events_latest.json` (2026-06-01) place l'événement au **2026-06-01** (jour J, `days_until: 0`). Aucun résultat Q1 n'est visible après plusieurs jours d'attente. [ANOMALIE CALENDRIER PERSISTANTE]

### FX Exposure

- `data/fx_exposure_latest.json` (2026-06-01) : Score FX Impact **0.0/10** — neutre. Aucun impact revenus/EPS estimé.

### Social Sentiment

- `data/social_sentiment_latest.json` (2026-06-01) : 0 mentions Reddit, sentiment 0.0/10, pas de pump détecté. Silence retail total.

**Verdict Sentiment :** Neutre à prudent. Silence médiatique et institutionnel. L'unique signal observable est la hausse du short interest (+2.19 pp), qui augmente le potentiel de squeeze mécanique mais confirme aussi le scepticisme du marché. Les données options sont corrompues ; aucune conclusion fiable ne peut être tirée sur le positionnement options actuel.

---

## 5. Scoring Global

### Scoring brut agent (recommandations_latest.json)

| Composante | Valeur |
|---|---|
| Score Global | 67.2 / 100 |
| Score Global Ajusté | **59.2 / 100** |
| Score Opportunité | **6.7 / 10** |
| Score Catalyseur | 8.0 / 10 |
| Score Valorisation | 7.0 / 10 |
| Score Momentum | **4.5 / 10** |
| Recommandation agent | **ATTENDRE** |
| Timing agent | **Défavorable** |

### Scoring ajusté analyste (règles Argus-IA)

| Composante | Valeur Agent | Valeur Ajustée | Règle appliquée |
|---|---|---|---|
| Score Opportunité | 6.7 / 10 | **~4.6 / 10** | Plafonnement Valorisation à 5/10 (Qualité 1/6) ; malus sectoriel XLC bottom 3 (−0.5 pt) ; malus timing défavorable (−0.3 pt) ; malus données earnings Q1 manquantes (−0.5 pt) |
| Score Catalyseur | 8.0 / 10 | **7.5 / 10** | Malus options données corrompues −0.5 pt |
| Score Valorisation | 7.0 / 10 | **5.0 / 10** | Plafonnement absolu Qualité ≤ 3/6 |
| Score Momentum | 4.5 / 10 | **4.5 / 10** | = |
| **Score Global Ajusté** | 59.2 / 100 | **~46 / 100** | Recalculé sur base 4.6/10 × 10 = 46 |
| **Recommandation analyste** | — | **SURVEILLER** | Score 35–49 ; Qualité 1/6 exclut tout sizing standard |

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — n = 0, pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1.0 (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

**Sector Rotation (`data/sector_rotation_latest.json`) :**
- Date 2026-06-01 : XLC classé **bottom 3** (momentum score 0.0 / 10). Signal système : **ROTATION_TO_DEFENSIVE**.
- Malus sectoriel maintenu : −0.5 pt composite.

**Geo Risk (`data/geo_risk_latest.json`) :**
- Date 2026-05-17 — FUBO non flaggué. Score Politique non calculé.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $10.09 | — |
| Stop-Loss | **$9.01** | 2× ATR (−10.7%) — confirmé par recommandations agent |
| Take-Profit | **$11.71** | 3× ATR (+16.1%) — confirmé par recommandations agent |
| Ratio R/R | **1.5×** | Stable |
| Résistance intermédiaire | **$10.49** | High du jour — rejet net, à surveiller |
| Résistance majeure | **$11.19** | MM50 — breakout requis pour inflexion de tendance |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13.00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7.50 (support psychologique) voire $6.80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — SURVEILLER (~46/100). Évolution technique ambiguë : amélioration RSI/volume mais recul séance + shorts qui s'empilent + données options corrompues.**

La thèse de **SURVEILLER** du snapshot 2026-05-27 17:00 UTC est **confirmée** avec une nuance d'ambivalence technique. Cinq observations :

1. **RSI continue de remonter (+3.85 pts à 47.2)** — Sortie progressive de la zone de survente extrême (RSI 21 le 26/05) vers la zone neutre. C'est une amélioration technique objective sur 5 jours. Cependant, le RSI reste sous 50 et le cours demeure sous la MM50 (−9.8%).

2. **Explosion de volume (1.31×) mais sur recul séance (−3.26%)** — Le volume de 1 942 000 est le plus élevé observé depuis plusieurs semaines. La combinaison **volume en hausse + cours en baisse** est un signal de distribution (ventes sur rallye) plus probable qu'accumulation. Le rejet du high $10.49 et la clôture proche du low ($9.92) confirment la domination vendeuse en fin de séance.

3. **Short interest hausse significative (+2.19 pp à 25.03%)** — Les shorts s'empilent alors que le cours remonte depuis le 26/05. Ce comportement est cohérent avec le recul séance : les shorts utilisent les rallyes pour renforcer leurs positions. Le setup short squeeze latent s'intensifie mécaniquement (25% du float shorté est un niveau élevé), mais le timing de déclenchement reste totalement incertain sans catalyseur.

4. **Anomalie options majeure** — Max pain $3.00 aberrant, put/call et call OI null. Cette corruption des données coïncide avec le rollover d'échéance (2026-05-29 → 2026-06-05). Les valeurs historiques ($10.00, 0.51, 66.3%) doivent être conservées comme référence. L'incapacité à lire le positionnement options actuel est un handicap analytique.

5. **Agent stable ATTENDRE (59.2/100)** — Le modèle quantitatif ne valide pas le recul comme un signal de vente, mais ne l'interprète pas non plus comme un achat. Le Score Momentum remonte légèrement (4.0 → 4.5), suggérant que le modèle valorise la progression RSI et la hausse du volume plus que le recul intraday. L'ajustement analyste ramène le Score Global à **~46/100** (SURVEILLER) sur base des règles absolues (Qualité 1/6, XLC bottom 3, earnings manquants).

**Arguments confirmant la prudence :**
1. **Qualité dégradée 1/6** — patrimoine net négatif, FCF négatif, current ratio 0.84, debt/equity 2.43, ROIC −2.1%.
2. **Divergence Yahoo/FMP persistante** — market cap $297.0M vs ~$3.3B (×11.0).
3. **Timing défavorable** — sous MM50 (−9.8%), RSI neutre-baisse, recul séance sur volume de distribution.
4. **Données options corrompues** — impossible d'évaluer le positionnement institutionnel actuel.
5. **Données manquantes** — pas de résultats Q1, pas de accounting risk, pas de social sentiment.
6. **Quant report non significatif** — pas assez d'historique.
7. **Earnings Q1 anomalie persistante** — incertitude sur le calendrier et les résultats attendus.
8. **Sector rotation défavorable** — XLC bottom 3, signal ROTATION_TO_DEFENSIVE.

**Recommandation finale :** **SURVEILLER — pas de position.** L'explosion de volume (1.31×) et la remontée du RSI (47.2) sont des évolutions techniques notables, mais la directionnalité reste incertaine. Le recul de −3.26% sur volume en hausse, le rejet du high $10.49 et l'empilement des shorts (+2.19 pp) suggèrent une distribution plutôt qu'une accumulation. Le setup short squeeze latent persiste et s'intensifie (25% du float shorté), mais sans catalyseur fondamental ni données options fiables, toute entrée reste un trade spéculatif avec sizing minimal. La résolution de l'anomalie earnings et la stabilisation des données options sont les deux catalyseurs clés à surveiller.

---

*Analyste institutionnel senior — Desk Argus-IA*
*Date : 2026-06-01 (snapshot 10:00 UTC)*
*Sources : data/latest.json (fetched 2026-06-01T10:00:13Z), data/recommandations_latest.json, data/quant_report_latest.json (2026-05-17), data/geo_risk_latest.json (2026-05-17), data/sector_rotation_latest.json (2026-06-01), data/social_sentiment_latest.json (2026-06-01), data/fx_exposure_latest.json (2026-06-01), data/upcoming_events_latest.json (2026-06-01), data/events_latest.json (2026-06-01), data/validation_report.txt (2026-06-01)*
