# FUBO — Mise à Jour Post-Close (2026-05-18 17h UTC)

> **Niveau d'impact :** 🟡 Modéré — Cours quasi inchangé, mais volume effondré (-68% vs 20j), liquidité dégradée
> **Référence précédente :** [FUBO_2026-05-18_update.md](FUBO_2026-05-18_update.md) (13h UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (13h UTC)

| Métrique | 13h UTC (précédent) | 17h UTC (actuel) | Variation |
|---|---|---|---|
| Cours close | $9,62 | **$9,53** | **−0,94%** |
| Volume | 944 400 | **484 253** | **−48,7%** 🔴 |
| Volume vs 20j | 0,60× | **0,31×** | **−48% relatif** 🔴 |
| RSI 14j | 36,84 | **36,93** | +0,09 (inchangé) |
| ATR 14j | $0,79 | **$0,80** | +1,3% |
| MM 50j | $11,98 | **$11,89** | −0,75% |
| Market Cap (Yahoo) | $283M | **$280,5M** | −0,9% |
| P/E (Yahoo) | 2,51x | **2,48x** | −1,2% |
| P/B | 0,35x | **0,345x** | −1,4% |
| Short Interest | 22,84% | 22,84% | — |
| Put/Call Ratio | 0,90 | [NON RAFRAÎCHI] | — |
| Max Pain | $10,00 | [NON RAFRAÎCHI] | — |

**Constat :** La séance de clôture n'a pas apporté de nouvelles données fondamentales ni de résultats d'earnings visibles. Le mouvement de cours (−0,94%) est marginal. En revanche, le **volume s'est effondré à 484k actions**, soit seulement **31% de la moyenne 20j** (1,53M). Cette liquidité très réduite est un signal de désintérêt du marché — absence de capitaux participant à la découverte de prix post-earnings.

**Anomalie :** Les résultats Q1 2026 étaient attendus ce jour (2026-05-18). Aucune donnée earnings (EPS, revenue, guidance) n'apparaît dans `data/latest.json` ni dans `data/events_latest.json`. Deux hypothèses :
1. Publication après la clôture des marchés (après 17h UTC) → résultats à intégrer demain matin
2. Données non récupérées par les APIs (Yahoo/FMP)

→ **Statut :** [EARNINGS EN ATTENTE — aucun chiffre disponible au snapshot 17h UTC]

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 36,93 | Zone neutre baissière, proche survente (seuil 30) |
| MM 50j | $11,89 | Cours sous la moyenne — écart −19,8% (dégradé vs −19,7% à 13h) |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,80 | Volatilité absolue élevée (8,4% du spot) |
| Volume vs 20j | 0,31× | **Liquidity trap** — volume très inférieur à la norme |
| Beta | 2,508 | Volatilité systématique extrême |
| 52W High / Low | $56,64 / $8,31 | Distance au 52W low : +14,7% |

**Niveaux clés (révisés post-close) :**
- Support immédiat : $9,31 (low du jour)
- Support secondaire : $8,31 (52W low)
- Résistance : $10,00 (niveau psychologique / max pain matinal)
- Résistance majeure : $11,89 (MM50)
- Stop-loss ATR (2×) : **$7,93** (−16,8%) — ajusté vs $8,04 précédent
- Take-profit ATR (3×) : **$11,93** (+25,2%) — ajusté vs $11,99 précédent

**Verdict timing :** Défavorable — sous MM50, RSI non confirmé en survente, volume en chute libre. Le faible volume post-earnings suggère soit une absence de catalyseur immédiat, soit une attente des chiffres réels après la clôture. Le pinning autour de $9,50–$10,00 reste le scénario de haute probabilité.

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale n'est disponible dans le snapshot 17h UTC par rapport au snapshot 13h UTC. La divergence Yahoo/FMP persiste :

| Source | Market Cap | P/B | EV/Revenue |
|---|---|---|---|
| Yahoo Finance | $280,5M | 0,345x | 0,433x |
| FMP Stable API (implicite) | ~$3,27B | 3,19x | — |

**Écart :** ×11,7 sur la capitalisation (stable vs 13h UTC).

### Ratios disponibles (Yahoo, close 2026-05-18)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM | 2,48x | Anormalement bas — suspect (divergence Yahoo/FMP) |
| Forward P/E | 20,19x | Elevé — anticipation de bénéfices faibles NTM |
| EV/Revenue | 0,433x | Bas — valorisation type turnaround/distressed |
| P/B | 0,345x | < 1x — patrimoine net suspect ou négatif |
| Beta | 2,508 | Extrême |
| Short Interest | 22,84% | Très élevé |

**Règle Filtre Qualité :** Score 1/6 confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à 5/10.

---

## 4. Mise à Jour Sentiment / Options / News

### Options (dernières données disponibles : 13h UTC)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $10,00 | Pinning probable autour du spot |
| Put/Call Ratio | 0,90 | Put-biased — sentiment dérivés baissier |
| Call OI % | 52,5% | Baisse du positionnement haussier near-term |

**Note :** Les données options n'ont pas été rafraîchies entre 13h et 17h UTC. Le repositionnement put-biased observé ce matin reste le signal dominant.

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +427%. Aucune révision récente — les analystes n'ont pas réagi au cours actuel.

### Social Sentiment

- Mention count Reddit : 0 (no data)
- Pump detected : false
- Alertes `EXTREME_BEARISH` : artefact d'absence de données (0 mentions)

**Verdict Sentiment :** Neutre à légèrement baissier. Aucun signal retail, options put-biased, consensus figé. Le silence des réseaux sociaux et l'effondrement du volume traduisent un désintérêt du marché.

---

## 5. Scoring Global

| Composante | Valeur Moteur | Valeur Ajustée Manuelle |
|---|---|---|
| Score Global | 64,8 / 100 | — |
| Score Global Ajusté | **56,8 / 100** | **~51 / 100** |
| Score Opportunité | 6,5 / 10 | **5,1 / 10** |
| Score Catalyseur | 8,0 / 10 | **7,5 / 10** (malus options put-biased −0,5) |
| Score Valorisation | 7,0 / 10 | **5,0 / 10** (plafonné Qualité 1/6) |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation** | **ATTENDRE** | **ATTENDRE** |

**Ajustements qualitatifs (inchangés vs 13h UTC) :**
- Malus Qualité (1/6) : Valorisation plafonnée à 5/10
- Malus Sectoriel : XLC bottom 3 (momentum 0,0) → −0,5 pt composite
- Malus Options : put/call ratio 0,90 + max pain $10 → −0,5 pt Catalyseur
- Malus Liquidité : volume 0,31× (nouveau) → pas de malus scoring, mais signal de prudence

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1,0 (non significatif)
- **Conclusion :** Aucune calibration auto applicable.

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9,53 | — |
| Stop-Loss | **$7,93** | Révisé à la baisse — 2× ATR (−16,8%) |
| Take-Profit | **$11,93** | Révisé à la baisse — 3× ATR (+25,2%) |
| Ratio R/R | **1,5×** | Stable |
| Max Pain | $10,00 | Niveau de pinning probable |

**Condition de révision post-earnings (si résultats disponibles demain) :**
- Beat + guidance raise → réviser TP à $13,50+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7,50 (support psychologique) voire $6,80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — ATTENDRE**

La thèse d'**ATTENDRE** du 2026-05-18 reste intégralement valide. La séance de clôture n'a apporté aucun élément modifiant la thèse structurelle. Deux observations nouvelles :

1. **Volume effondré (0,31×)** : le marché est passé d'un volume faible (0,6×) à un volume très faible (0,31×). Cette liquidité réduite augmente le risque de gap et réduit la fiabilité des niveaux techniques. Aucun flux institutionnel ne semble engagé.
2. **Earnings en attente de confirmation** : les résultats Q1 2026 étaient attendus ce jour. L'absence de données dans le snapshot 17h UTC suggère soit une publication post-close (après 17h UTC), soit un retard de récupération API. → **À vérifier demain matin.**

**Arguments confirmant la patience :**
1. **Qualité dégradée 1/6** — inchangée. Patrimoine net négatif, FCF négatif, current ratio 0,84, debt/equity 2,43.
2. **Données techniques inchangées** — sous MM50, RSI ~37, aucun signe de reversal. Le faible volume est un signal de désintérêt, pas d'accumulation.
3. **Repositionnement options baissier** — put/call 0,90, max pain $10 (données 13h UTC non révisées).
4. **Divergence Yahoo/FMP persistante** — P/E 2,48x et market cap $280M restent suspects vs les données FMP.
5. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 (momentum 0,0).
6. **Quant report non significatif** — pas assez d'historique.
7. **Liquidité dégradée** — volume 0,31× = risque de slippage élevé.

**Seuls éléments modifiés :**
- SL/TP ajustés à la baisse ($7,93 / $11,93) en raison du nouveau close à $9,53
- Ajout du signal "liquidity trap" — volume très faible post-earnings

**Scénarios post-earnings (dès disponibilité des résultats) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 15% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 45% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 40% | −10–20% | Confirmer l'évitement |

> **Note de probabilité :** Inchangée vs 13h UTC. Le repositionnement options put-biased maintient la probabilité bearish à 40%.

**Recommandation finale :** **ATTENDRE — pas de position.** Le titre reste une spéculation pure sans fondement qualitatif. Le volume effondré et l'attente des résultats earnings justifient de rester à l'écart. Si résultats positifs demain, le titre reste une spéculation court terme et non un investissement long terme. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-18 (post-close 17h UTC)*  
*Sources : data/latest.json (fetched 2026-05-18T17:00:01Z), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json*
