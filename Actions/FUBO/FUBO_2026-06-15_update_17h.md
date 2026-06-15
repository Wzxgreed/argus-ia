# FUBO — Mise à Jour (2026-06-15, snapshot 17h UTC)

> **Niveau d'impact :** 🟡 Modéré — Rebound +1.82% à $10.01 sur volume collapse 0.55×, RSI remonté à 53.45, données options JSON résolues (max pain $11.00), calendrier earnings actualisé (2026-08-06). Référence précédente : [FUBO_2026-06-15_update.md](FUBO_2026-06-15_update.md) (snapshot 10h UTC $9.83)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-06-15 10h UTC)

| Métrique | 2026-06-15 10h UTC | **2026-06-15 17h UTC** | Variation |
|---|---|---|---|
| Cours close | $9.83 | **$10.01** | **+1.82%** |
| Previous close | $10.47 | **$9.83** | — |
| Volume séance | 1 745 900 | **704 000** | **−59.7%** (0.55× moy. 20j) |
| RSI 14j | 50.56 | **53.45** | **+2.89 pts** |
| ATR 14j | $0.85 | **$0.85** | Stable |
| MM 50j | $11.03 | **$11.03** | Stable |
| Spot vs MM50 | −10.9% | **−9.2%** | Réduction de l'écart |
| Beta | 2.392 | **2.392** | Stable |
| Short Interest | 24.32% | **24.32%** | Stable |
| Options max pain | $13.00 (opérationnel) | **$11.00** | Données JSON résolues, révision à la baisse |
| Put/Call Ratio | 0.23 | **0.46** | Hausse (biais haussier atténué) |
| Call OI % | 81.0% | **68.4%** | Baisse |
| Score Global Ajusté | ~42.5 (analyste) | **56.0 (agent)** | **Upgrade +13.5 pts** |
| Score Opportunité | ~4.3 (analyste) | **6.4/10** | **Upgrade** |
| Recommandation | SURVEILLER | **ATTENDRE** | **Upgrade** |

**Constats :**
1. **Rebound +1.82%** après le gap down −6.11% du matin. Le cours passe de $9.83 à $10.01, récupérant une partie du territoire perdu.
2. **Volume collapse à 0.55×** — 704k actions vs moyenne 20j 1.27M. La liquidation matinale est terminée ; le rebond se fait sur faible volume, ce qui limite la conviction.
3. **RSI remonté à 53.45** (+2.89 pts), sortie de la zone médiane-basse vers la médiane-haute.
4. **Données options JSON résolues** — plus d'anomalie ($3.00 / call OI 0%). Le max pain passe à **$11.00** (vs $13.00 opérationnel historique), put/call **0.46** (vs 0.23), call OI **68.4%** (vs 81.0%). La structure reste haussière mais moins fortement qu'auparavant.
5. **Calendrier earnings actualisé** — `upcoming_events_latest.json` place désormais le prochain earnings au **2026-08-06** (52 jours, Est EPS $-0.32-$0.07, Rev $1.5B). L'anomalie Q1 (jour J récurrent depuis ~30 sessions) semble résolue par avancement du calendrier.
6. **Écart sous MM50 réduit** à −9.2% (vs −10.9%). Pas encore au-dessus.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 53.45 | Neutre médian-haut — progression |
| MM 50j | $11.03 | Cours sous MM50 — écart −9.2% |
| ATR 14j | $0.85 | Volatilité élevée stable |
| Volume vs 20j | 0.55× | Faible — pas de conviction acheteuse |
| Beta | 2.392 | Extrême |
| 52W High / Low | $56.64 / $8.31 | Distance 52W low : +20.5% |

**Options (données JSON résolues, snapshot 17h) :**

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $11.00 | Spot −9.1% sous max pain |
| Put/Call Ratio | 0.46 | Faible-modéré — biais haussier atténué |
| Call OI % | 68.4% | Dominance call persistante mais réduite |
| Échéance | 2026-06-18 | J+3 |

**Lecture institutionnelle :** Le rebond +1.82% sur volume collapse (0.55×) est un soulagement technique mais pas un signal d'accumulation. Le RSI à 53.45 récupère de la zone médiane-basse mais reste loin de la zone de momentum haussier (>60). Le cours reste sous MM50 ($11.03) avec un écart de −9.2%, maintenant le timing défavorable.

La structure options est désormais lisible sans anomalie JSON. Le max pain à $11.00 est plus proche du spot que l'ancien $13.00 opérationnel, ce qui réduit l'aimant haussier mécanique. Le put/call à 0.46 (vs 0.23) et le call OI à 68.4% (vs 81.0%) indiquent une couverture baissière légèrement plus élevée qu'auparavant. Le setup de short squeeze reste latent (short interest 24.32%) mais sans catalyseur déclencheur.

**Niveaux clés :**
- Support immédiat : **$9.84** (low 17h)
- Support psychologique : **$9.50**
- Support majeur : **$8.31** (52W low)
- Résistance immédiate : **$10.47** (previous close 14/06, ancien gap)
- Résistance : **$11.03** (MM50)
- Résistance majeure : **$11.00–$13.00** (zone max pain / historique)
- Stop-loss ATR (2×) : **$8.31** (−17.0%)
- Take-profit ATR (3×) : **$12.56** (+25.5%)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — rebond sans volume, sous MM50, ATR élevé.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale dans le snapshot 17h. Les ratios FMP restent inchangés (FY 2025-12-31) :

| Source | Market Cap | P/E TTM | Forward P/E | P/B | EV/Revenue |
|---|---|---|---|---|---|
| Yahoo Finance | $294.6M | 2.61× | 21.21× | 0.36× | 0.434× |
| FMP Stable API | ~$3.27B | 5.65× | — | 3.19× | 1.281× |

**Signaux fondamentaux inchangés :**
- **P/E TTM 2.61×** — Artéfact comptable probable.
- **P/B 0.36× (Yahoo)** — Patrimoine net négatif confirmé (tangible asset value −$398.9M).
- **Current ratio 0.84** — Insuffisance liquidité à court terme.
- **FCF yield négatif −18.9%** — Pas de génération de cash libre.
- **Consensus figé** — Price target $50.25 (4 analysts, 0 mise à jour récente).

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Plafonnement Score Valorisation à **5/10** en analyse manuelle (l'agent non plafonné affiche 7.0/10).

---

## 4. Mise à Jour Sentiment / Options / News

### Consensus Analystes (FMP)
- Price Target Moyen : **$50.25** (4 analysts, 0 mise à jour récente) — écart +402.5%.

### News & Événements Corporates
- `data/events_latest.json` : aucun événement corporate détecté.
- **Earnings Q2 2026** : `upcoming_events_latest.json` place désormais l'earnings au **2026-08-06** (52 jours, Est EPS $-0.32-$0.07, Rev $1.5B). L'anomalie calendrier Q1 (jour J récurrent depuis ~30 sessions) semble résolue par avancement du calendrier vers Q2. *[RÉSOLUTION PARTIELLE — confirmer publication Q1]*
- **Social Sentiment** : 0 mentions Reddit, sentiment 0/10, pas de pump. [NEUTRE]
- **FX Exposure** : exposition 25%, impact neutre, divergence alignée. [NEUTRE]
- **Sector Rotation** : XLC (Communication Services) classé **bottom 3** (momentum score 0.0). Malus sectoriel −0.5 pt maintenu.

---

## 5. Scoring Global

### Scoring agent (data/recommandations_latest.json, snapshot 17h)

| Composante | Valeur Agent | Lecture |
|---|---|---|
| Score Catalyseur | 6.5 / 10 | Catalyseur neutre-modéré |
| Score Valorisation | 7.0 / 10 | Non plafonné par agent |
| Score Momentum | 5.3 / 10 | Neutre — rebond sans volume |
| **Score Opportunité** | **6.4 / 10** | Pondération régime : 35/40/25 |
| **Score Global** | **64.0 / 100** | Base |
| Malus intégrés (sector, FX, etc.) | −8.0 pt | XLC bottom 3, autres |
| **Score Global Ajusté** | **56.0 / 100** | Zone 50–59 |
| **Recommandation agent** | **ATTENDRE** | Qualité présente mais pas de catalyseur clair |

**Note analyste :** Le upgrade de SURVEILLER (~42.5) à ATTENDRE (56.0) est justifié par le rebond technique, la normalisation du volume, la résolution des données options JSON et l'actualisation du calendrier earnings. Cependant, le non-franchissement de la MM50, le volume faible du rebond et le Filtre Qualité 1/6 maintiennent la prudence. Le Score Valorisation 7.0 de l'agent n'est pas plafonné ; en analyse manuelle avec plafonnement qualité, il serait limité à 5.0/10.

---

## 6. Révision des Niveaux SL / TP

Révisés avec le close 17h et ATR stable :

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $10.01 | — |
| Stop-Loss | **$8.31** | 2× ATR (−17.0%) |
| Take-Profit | **$12.56** | 3× ATR (+25.5%) |
| Ratio R/R | **1.5×** | Stable |
| Support immédiat | **$9.84** | Low 17h |
| Support psychologique | **$9.50** | — |
| Support majeur | **$8.31** | 52W low |
| Résistance immédiate | **$10.47** | Previous close 14/06 |
| Résistance | **$11.03** | MM50 |
| Résistance majeure | **$11.00–$13.00** | Zone max pain / historique |

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE MODIFIÉE — DE SURVEILLER (~42.5/100) À ATTENDRE (56.0/100). Le rebond technique +1.82% et la résolution des anomalies données/calendrier justifient l'upgrade, mais le profil fondamental dégradé et le non-franchissement de la MM50 empêchent tout passage à ACHETER.**

La thèse **SURVEILLER** du snapshot 10h est upgradée vers **ATTENDRE** pour quatre raisons principales :

1. **Rebound technique post-gap down** — Le cours remonte de $9.83 à $10.01 (+1.82%) après le gap down −6.11% du matin. La pression vendeuse s'est atténuée.
2. **Normalisation du volume** — Le volume passe de 1.36× à 0.55×, indiquant que la liquidation matinale est terminée.
3. **Résolution des anomalies** — Les données options JSON sont désormais cohérentes (max pain $11.00, pas d'aberration $3.00). Le calendrier earnings avance vers le 2026-08-06, résolvant l'anomalie Q1 récurrente.
4. **Scoring agent upgrade** — Le Score Global Ajusté passe de la zone SURVEILLER à la zone ATTENDRE (56.0/100).

**Risques persistants :**
- Cours sous MM50 (−9.2%) — timing défavorable
- Volume faible du rebond — pas de confirmation d'accumulation
- Filtre Qualité 1/6 — plafond fondamental
- Sector XLC bottom 3 — headwind sectoriel
- Short interest 24.32% — survente latente mais pas de catalyseur de squeeze

**Recommandation finale :** **ATTENDRE.** Pas d'entrée longue en l'état. Le rebond est un soulagement technique, pas un signal de renversement. Attendre un retour confirmé au-dessus de la MM50 ($11.03) avec volume >1.0× avant toute révision haussière.

**Conditions de réactivation haussière (pour sortir de ATTENDRE) :**
- Retour au-dessus de **MM50 ($11.03)** avec volume confirmé **>1.0×**
- Données options confirmant un max pain en hausse au-dessus du spot
- Publication confirmée des résultats Q1 (si non publiés) ou Q2 (2026-08-06)

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-06-15 (snapshot 17:00 UTC)*  
*Sources : data/latest.json (fetched 2026-06-15T17:00:14Z), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/quant_report_latest.json (2026-05-17, insuffisant)*
