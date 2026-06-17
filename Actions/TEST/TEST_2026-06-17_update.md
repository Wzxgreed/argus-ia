# TEST — Mise à jour quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-17
> **Type :** Mise à jour post-pipeline 10h UTC
> **Source :** `data/latest.json` (snapshot 10:00:11 UTC), `data/recommandations_latest.json`

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-16 17h UTC | 2026-06-17 10h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | **$44.836** | **$44.76** | **−$0.076 (−0.17%)** 🔴 |
| Previous close | $44.121 | **$45.228** | **Révision données Yahoo** ⚠️ |
| Change session | +1.62% | **−1.03%** | **Baisse confirmée** 🔴 |
| RSI 14j | **47.08** | **42.39** | **−4.69 pts** 🔴 |
| MM 50j | $43.6 | $43.6 | Stable ⚪ |
| MM 200j | `null` | `null` | [DONNÉES MANQUANTES] |
| ATR 14j | **$1.25** | **$1.23** | **−$0.02** ⚪ |
| Volume session | 1,000 | **900** | **−10%** 🔴 |
| Volume avg 20j | 2,410 | **1,690** | **−30%** 🔴 |
| Volume vs avg 20j | 0.41× | **0.53×** | Ratio mécanique ⚪ |
| 52w high | $57.74 | $57.74 | — |
| 52w low | $40.27 | $40.27 | — |

**Mutation technique négative modérée.** Le cours recule de −1.03% vs le previous close révisé à $45.228 (données Yahoo actualisées — le snapshot 17h du 16/06 sous-estimait le niveau de clôture officielle). Le RSI chute de 4.69 pts à 42.39, revenant au voisinage de la zone 40. Le pipeline recalcule un **Score Global de 56.5/100** (61.5 ajusté), en retrait de 4.5 pts vs le snapshot précédent. Le verdict **ACHETER (Réduit)** est maintenu de justesse au-dessus du seuil de 60 en score ajusté.

---

## Mise à jour technique

- **Cours :** $44.76 (close 10h UTC), −1.03% vs previous close $45.228. Open $44.745, high $44.77, low $44.745. Session très étroite (range $0.025), quasi-figée en dehors du gap baissier d'ouverture.
- **RSI 14j :** 42.39, en baisse de 4.69 pts vs 47.08 à 17h hier. Retour au voisinage de la zone 40 — le momentum de la séance de rattrapage haussier du 16/06 est entièrement dissipé.
- **MM 50j :** $43.6, inchangée. Cours +2.7% au-dessus de la MM50 — support technique valide mais en rétrécissement.
- **MM 200j :** `null` — donnée manquante persistante.
- **ATR 14j :** $1.23, quasi-stable (−$0.02 vs $1.25). Volatilité quotidienne très faible, cohérente avec la session étroite observée.
- **Volume :** 900 unités (0.53× moyenne 20j de 1,690). En recul de 10% vs le snapshot 17h hier (1,000) et sur une moyenne 20j elle-même en effondrement (−30% vs 2,410). **Illiquidité structurelle aggravée — la moyenne 20j atteint son plus bas niveau historique dans notre série.**
- **52w range :** $40.27–$57.74. Cours à 22.5% du low, 22.5% sous le high.

**Verdict timing :** Neutre. Le recul du RSI et l'absence de range intraday neutralisent le signal haussier de la veille. Le cours reste au-dessus de la MM50, ce qui évite une dégradation en SURVEILLER. La faiblesse du volume et du range laissent le timing sans direction claire.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI) — bloc vide dans `latest.json`

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-17, flag persistant depuis 17+ jours) — hypothèse artefact calendrier FMP toujours valide. Aucun résultat observable. Le flag est passé à J+1 sans événement.

---

## Mise à jour sentiment / options / news

Données issues de l'écosystème agents (snapshot 10h UTC) :

| Module | Statut | Commentaire |
|--------|--------|-------------|
| `recommandations_latest.json` | **Présent** | Scores recalculés — verdict maintenu ACHETER (Réduit) malgré le recul |
| `quant_report_latest.json` | 2026-05-17 | Insuffisant — pas de signaux historiques pour TEST |
| `geo_risk_latest.json` | 2026-05-17 | Score géo non disponible pour TEST |
| `accounting_risk_latest.json` | Absent | Évaluation impossible |
| `sector_rotation_latest.json` | 2026-06-17 | TEST sans secteur assigné — pas de privilège/pénalité sectorielle |
| `social_sentiment_latest.json` | 2026-06-17 | 0 mention, sentiment « No data », pas de pump détecté |
| `fx_exposure_latest.json` | 2026-06-17 | Exposition 25%, direction neutre, divergence « aligned », score FX 0.0 |
| `events_latest.json` | 2026-06-17 | 0 événement corporate détecté pour TEST |
| `upcoming_events_latest.json` | 2026-06-17 | Earnings JOUR J (2026-06-17) non résolu — artefact FMP, J+1 imminent |

**Absence de flux sentiment/options/news** pour ce snapshot. Aucun catalyseur externe identifié. Le sentiment retail « No data » et le score FX neutre n'apportent ni bonus ni malus au scoring global.

---

## Nouveau scoring global

Le pipeline a recalculé les scores agents pour le snapshot 10h UTC (`data/recommandations_latest.json` présent). Comparaison avec les données du snapshot 17h UTC du 16/06 :

| Métrique | Valeur 17h UTC 16/06 | Valeur 10h UTC 17/06 (pipeline) | Δ |
|----------|---------------------|----------------------------------|---|
| Score Catalyseur | 6.5/10 | **6.5/10** | Stable ⚪ |
| Score Valorisation | 5.0/10 | **5.0/10** | Stable ⚪ |
| Score Momentum | 7.3/10 | **5.5/10** | **−1.8 pts** 🔴 |
| Score Opportunité | 6.1/10 | **5.7/10** | **−0.4 pt** 🔴 |
| Score Global | 61.0/100 | **56.5/100** | **−4.5 pts** 🔴 |
| Score Global Ajusté | 66.0/100 | **61.5/100** | **−4.5 pts** 🔴 |
| Verdict | ACHETER (Réduit) | **ACHETER (Réduit)** | Maintenu ⚪ |
| Timing | Favorable | **Neutre** | Dégradation 🔴 |
| Horizon | 1–3 mois | 1–3 mois | Stable ⚪ |
| Sizing | Réduit | **Réduit** | Stable ⚪ |

**Interprétation :** La dégradation est entièrement portée par le **Score Momentum** qui recule de 7.3 à 5.5 (−1.8 pts). Ce retrait s'explique par :
1. Le recul du cours (−1.03% vs previous close révisé $45.228) qui pénalise le momentum de prix
2. La chute du RSI (−4.69 pts à 42.39), sortant de la zone neutre médiane favorable et revenant au voisinage de 40
3. L'effondrement de la moyenne volume 20j (1,690 vs 2,410) qui renforce le signal de faiblesse structurelle

Le Score Catalyseur (6.5) et le Score Valorisation (5.0) sont inchangés. La pondération régime (Catalyseur 35% / Valorisation 40% / Momentum 25%) fait du Momentum un facteur discriminant mais non dominant. Avec un Score Momentum à 5.5, le Score Opportunité recule à 5.7, entraînant le Score Global en retrait à 56.5 (61.5 ajusté). Le verdict **ACHETER (Réduit)** est maintenu de justesse grâce au score ajusté (61.5) qui reste au-dessus du seuil de 60.

**Règle de disqualification :** Non activée (aucun score ≤ 2/10).

---

## Révision des niveaux SL / TP

| Niveau | Valeur précédente (17h UTC 16/06) | Valeur 10h UTC 17/06 | Δ |
|--------|-----------------------------------|----------------------|---|
| Stop-loss | $42.34 | **$42.30** | −$0.04 ⚪ |
| Take-profit | $48.59 | **$48.45** | −$0.14 ⚪ |
| Ratio R/R | 1.5 | **1.5** | Stable ⚪ |

**Méthode :** SL = close − 2×ATR = $44.76 − 2×$1.23 = $42.30. TP = close + 3×ATR = $44.76 + 3×$1.23 = $48.45. Ratio gain/perte = ($48.45 − $44.76) / ($44.76 − $42.30) = 1.5.

**Note :** Les niveaux sont quasi-identiques à ceux du snapshot 17h UTC du 16/06, car la légère baisse du close (−$0.076) compense pratiquement la baisse de l'ATR (−$0.02).

---

## Conclusion — Thèse confirmée avec vigilance

**La thèse est CONFIRMÉE : verdict maintenu à ACHETER (Réduit), mais avec vigilance accrue.**

**Raisons du maintien :**
1. **Cours toujours au-dessus de la MM50** : $44.76 vs $43.6 (+2.7% d'écart), support technique intact.
2. **Scores Catalyseur et Valorisation stables** : 6.5 et 5.0 inchangés, assurant la base du scoring.
3. **Score Global Ajusté** à 61.5, au-dessus du seuil de 60 — la regradation en ATTENDRE n'est pas déclenchée.
4. **Aucun catalyseur négatif externe** : pas de news, pas d'événement corporate, pas de pump/dump.

**Points de vigilance renforcés :**
- **Recul du RSI au voisinage de 40** : 42.39 (−4.69 pts). Si le RSI franchit 40 à la baisse sur le prochain snapshot, le Score Momentum risque de tomber sous 5.0, entraînant le Score Global Ajusté sous 60 et une regradation en ATTENDRE.
- **Illiquidité structurelle aggravée** : volume 900 sur une moyenne 20j effondrée à 1,690. C'est le niveau de liquidité le plus faible observé dans toute la série. Toute position doit rester de taille réduite.
- **Previous close révisé à $45.228** : le snapshot 17h du 16/06 sous-estimait le niveau de clôture officielle. La séance du 16/06 était donc moins haussière qu'interprété en temps réel (+1.62% vs un previous close sous-estimé, alors que le vrai previous était probablement plus élevé).
- **Absence totale de données fondamentales et options** : aucune couche de protection qualitative.
- **Earnings JOUR J persistant** : artefact calendrier FMP non résolu après 17+ jours.
- **MM200 toujours indisponible** : impossibilité d'évaluer la tendance long terme.

**Scénarios de suivi :**
- Si RSI remonte > 45 sur prochain snapshot avec volume > 0.6× avg → maintien **ACHETER (Réduit)**, possible amélioration du timing à Favorable.
- Si RSI passe sous 40 malgré données complètes → dégradation immédiate **ATTENDRE** (Score Global Ajusté < 60).
- Si close redevient NaN ou ATR/MM50 perdues de nouveau → retour immédiat **ATTENDRE**, suspension SL/TP.
- Si volume retombe sous 0.3× avg (soit < 507 sur la moyenne actuelle) → signal de faiblesse structurelle extrême, révision du sizing à très réduit ou clôture.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 10h UTC), data/recommandations_latest.json*
