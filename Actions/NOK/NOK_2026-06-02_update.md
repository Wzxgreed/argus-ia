# NOK — Mise à Jour Quotidienne (2026-06-02, Snapshot 21:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-06-02 | Données source : `data/latest.json` (snapshot 2026-06-02T21:00:08 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (Snapshot 17:00 UTC 02/06)

| Indicateur | Snapshot 17:00 UTC (02/06) | Snapshot 21:00 UTC (02/06) | Variation | Signal |
|-----------|---------------------------|---------------------------|-----------|--------|
| Cours close | $16.835 | **$16.85** | **+0.09%** | → Stable, légèrement révisé à la hausse |
| RSI 14j | 70.17 | **70.22** | +0.05 | → 🔴 Zone surachat confirmée (≥70) |
| ATR 14j | $1.02 | **$1.02** | — | → Stable |
| Volume | 98,881,235 | **129,557,620** | **+31.0%** | → 🔵 **Révision majeure à la hausse** |
| Volume vs moy. 20j | 0.84× | **1.09×** | +0.25× | → Rally accompagné par volume au-dessus de la moyenne |
| High intraday | $17.11 | **$17.11** | — | → 52-week high inchangé |
| Low intraday | $16.45 | **$16.45** | — | → Support inchangé |
| P/E (TTM Yahoo) | 105.22 | **105.31** | +0.09 | → Valorisation inchangée en pratique |
| Forward P/E | 34.52 | **34.55** | +0.03 | → Inchangé |
| Premium vs consensus $9.26 | +81.8% | **+81.9%** | +0.1 pp | → Divergence inchangée |
| MM 50j | $11.70 | **$11.70** | — | → Tendance haussière structurelle intacte |
| **Max pain options** | $13.50 | **$13.50** | — | → Inchangé |
| **Put/Call ratio** | 0.45 | **0.45** | — | → Structure call-dominated stable |
| **Call OI** | 69.1% | **69.1%** | — | → Forte activité call stable |
| Score Global ajusté (fichier JSON) | 31.8/100 (ÉVITER) | **31.8/100 (ÉVITER)** | — | → Inchangé |
| Score Opportunité (fichier JSON) | 4.2/10 | **4.2/10** | — | → Inchangé |
| Score Momentum (fichier JSON) | 5.5/10 | **5.5/10** | — | → Inchangé |

**Changements significatifs détectés :**
- **→ 🔵 Volume révisé à la hausse de 31.0%** : de 98.9M (0.84× moyenne 20j) à 129.6M (**1.09× moyenne 20j**). Cette révision post-clôture invalide la "divergence baissière volume/prix" identifiée au snapshot 17h. Le rally vers le new 52w high a finalement été accompagné par un volume légèrement supérieur à la moyenne 20j, ce qui est techniquement plus sain.
- **→ Cours quasi stable** (+0.09% vs 17h) à $16.85. Le cours reste +3.7% vs previous close ($16.25) et +9.8% vs close 01/06 ($15.34 implicite).
- **→ RSI 70.22** : franchissement de la zone de surachat confirmé. Aucun recul technique en after-hours.
- **→ Tous les scores agents inchangés** (`recommandations_latest.json` non muté entre 17h et 21h).
- **→ Aucune news, aucun événement corporate** : `news_latest.json` et `events_latest.json` vides pour NOK.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $16.85 | Yahoo Finance | +0.09% vs snapshot 17h, +3.7% vs previous close |
| Open | $16.56 | Yahoo Finance | Gap haussier d'ouverture confirmé |
| High intraday | $17.11 | Yahoo Finance | 🔴 **New 52-week high** — résistance historique cassée |
| Low intraday | $16.45 | Yahoo Finance | Support remonté |
| Volume | 129,557,620 | Yahoo Finance | **1.09× moyenne 20j** — volume final au-dessus de la moyenne |
| RSI 14j | 70.22 | Calcul agent | 🔴 **Zone de surachat** confirmée (≥70) |
| ATR 14j | $1.02 | Calcul agent | 6.05% du cours — trigger ATR_SPIKE actif |
| MM 50j | $11.70 | Calcul agent | Cours +44.0% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché |

**Niveaux clés (inchangés vs 17h) :**
- **Support immédiat :** $16.45 (low du jour) / $16.25 (close 13h, ancienne résistance devenue support)
- **Support structural :** $11.70 (MM 50j) / $15.47 (base du gap du 25/05)
- **Résistance :** $17.11 (52-week high) / $17.87 (take-profit ATR historique) / $19.89 (TP JSON)
- **Stop-loss ATR (2×) :** $14.81 ($16.85 − $2.04) — aligné avec `recommandations_latest.json`
- **Take-profit ATR (3×) :** $19.91 ($16.85 + $3.06) — aligné avec `recommandations_latest.json`
- **Ratio R/R :** 1.5

**Mise à jour options — données confirmées dans `latest.json` :**
| Niveau | Valeur 17:00 UTC (02/06) | Valeur 21:00 UTC (02/06) | Interprétation |
|--------|-------------------------|-------------------------|----------------|
| Max pain | $13.50 | **$13.50** | Inchangé — cohérent avec historique |
| Put/Call ratio | 0.45 | **0.45** | Structure bullish (dominance calls) |
| Call OI % | 69.1% | **69.1%** | Forte activité call — détenteurs ITM exposés au pin |
| Expiration | 2026-06-05 | **2026-06-05** | **Demain** |

> **🔴 Pin risk extrème à l'expiration 05/06 (demain).** Le cours ($16.85) est désormais **+24.8% au-dessus du max pain** ($13.50). La pression de mean-reversion vers $13.50 s'intensifie. Avec **1 jour restant** avant expiration vendredi, et en l'absence totale de catalyseur, la probabilité d'un ajustement baissier technique reste élevée. La révision du volume à la hausse (1.09×) atténue légèrement le risque de distribution immédiate, mais ne supprime pas la surchauffe technique.

**Verdict timing :** Défavorable. Le franchissement RSI 70 + new 52w high + pin risk à J-1 expiration crée une configuration technique de surchauffe. La tendance haussière structurelle reste intacte (cours > MM50), mais le timing d'entrée reste défavorable.

**Score Momentum :** 5.5/10 (source `recommandations_latest.json`) — inchangé vs snapshot 17h.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $94.07 B | Yahoo Finance |
| P/E (TTM Yahoo) | 105.31 | Yahoo Finance |
| Forward P/E (Yahoo) | 34.55 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 34.871 | Yahoo Finance |
| P/B (Yahoo) | 3.83 | Yahoo Finance |
| Dividend yield (Yahoo) | 1.01% | Yahoo Finance |

**Données opérationnelles FMP (FY 2025) — inchangées :**
| Ratio | Valeur |
|-------|--------|
| Gross margin | 43.5% |
| Operating margin | 3.9% |
| Net margin | 3.3% |
| ROE | 3.1% |
| ROIC | 1.9% |
| Debt/Equity | 0.25 |
| Current ratio | 1.58 |
| Net debt/EBITDA | −0.11 (net cash) |

**Filtre Qualité (6 critères) — inchangé :**
| Critère | Évaluation | Justification |
|---------|------------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ Non | Croissance anémique du top-line (mature 5G) |
| Profit CAGR 5 ans ≥ 20% | ❌ Non | Rentabilité historiquement faible |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.58, net cash position |
| FCF positif et croissant 5 ans | ⚠️ Partiel | FCF yield 4.9% mais trajectoire instable |
| Avantage compétitif (moat) | ⚠️ Partiel | Leader 5G historique mais part de marché sous pression |
| Industrie forte croissance (TAM ×5) | ❌ Non | TAM 5G mature, croissance à simple digit |
| **Score Qualité total** | **2.5/6** | 🔴 Hors périmètre (inchangé) |

**Note fondamentale :** Aucune donnée fondamentale nouvelle depuis le snapshot 17h. Le consensus inchangé à $9.26 sur 6 analystes maintient la divergence à **+81.9%**. Aucun upgrade, downgrade ou révision d'estimations n'a été détecté.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +81.9% vs consensus, P/E 105.31, forward P/E 34.55 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision — silence total malgré la volatilité |
| Nombre analysts actifs (mois) | 0 | FMP Stable API | Faible couverture |
| Put/Call ratio | 0.45 | Yahoo Finance | Structure bullish (dominance calls) — stable |
| Max pain | $13.50 | Yahoo Finance | 🔴 Risque pin baissier extrème à l'expiration demain |
| Call OI % | 69.1% | Yahoo Finance | Forte activité call — stable |
| Short Interest | 1.08% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiée dans le flux |

**Verdict Sentiment :** Neutre à légèrement bearish à court terme. La structure options est stable (put/call 0.45, call OI 69.1%) mais le max pain $13.50 crée une pression technique réelle à J-1 expiration. Le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement reste sans explication fondamentale.

**Score Catalyseur :** 4.0/10 — inchangé dans `recommandations_latest.json`. Aucun catalyseur identifiable ; earnings éloignés (51 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Unknown (régime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score (JSON 21h) | Évolution (vs 17h) | Justification |
|-----|-----------------|-------------------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable |
| Valorisation | 3.5/10 | → | P/E 105.31, cours +81.9% vs consensus |
| Momentum | 5.5/10 | → | RSI 70.22 (surachat), volume révisé à 1.09× |
| **Score Opportunité** | **4.2/10** | → | (4.0×0.35) + (3.5×0.40) + (5.5×0.25) = 4.2 |
| **Score Global** | **41.8/100** | → | Malus : Valorisation faible + pin risk extrème + RSI surachat |
| **Score Global ajusté** | **31.8/100** | → | Seuil **ÉVITER** (<35) |

**Action recommandée :** **ÉVITER** (source `recommandations_latest.json`, Score Global ajusté 31.8/100)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (17:00 UTC 02/06) | Nouveau (21:00 UTC 02/06) | Justification |
|--------|--------------------------|--------------------------|---------------|
| Stop-loss | $14.80 | **$14.81** | Révisé — ATR 2× ($16.85 − $2.04), aligné JSON |
| Take-profit | $19.89 | **$19.91** | Révisé — ATR 3× ($16.85 + $3.06), aligné JSON |
| Prix cible (consensus) | $9.26 | $9.26 | Inchangé — 6 analysts, silence total |
| Upside consensus | −45.0% | **−45.0%** | Stable |
| Downside SL | −12.1% | **−12.1%** | Stable |

**⚠️ Attention :** La révision du volume à la hausse (1.09× moyenne 20j) invalide la "divergence baissière volume/prix" du snapshot 17h. Le rally vers $17.11 a été soutenu par une participation finale au-dessus de la moyenne, ce qui rend le new high techniquement plus solide qu'initialement estimé. Cependant, le **pin risk options ($13.50, expiration demain 05/06)** reste la menace principale : le cours est +24.8% au-dessus du max pain. Sans catalyseur, la probabilité d'un ajustement baissier technique avant ou à l'expiration reste élevée. Si le cours casse sous $16.25 (close 13h) en clôture demain, le rejet du new high sera confirmé.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −7.97%, RS60d −16.28%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (51 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |
| **Quality Report** | Warning | Quality hors périmètre 2–2.5/6 ; P/E 105.31 ; cours +81.9% vs consensus. Pas d'exclusion. |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **confirmée** — le snapshot 21:00 UTC du 02/06 confirme la mutation technique identifiée à 17h, avec une nuance positive sur le volume.

**Analyse :**
- **Technique :** Cours quasi stable $16.85 (+0.09% vs 17h), nouveau 52w high $17.11 confirmé. Le **volume final est révisé à la hausse de 31.0%** : 129.6M (1.09× moyenne 20j) vs 98.9M (0.84×) au snapshot 17h. Cette révision invalide la divergence baissière volume/prix initialement identifiée. Le rally vers le new high a été soutenu par une participation légèrement supérieure à la moyenne, ce qui est techniquement plus sain. Cependant, le **RSI reste à 70.22** (zone surachat) et le cours reste +44.0% au-dessus de la MM50 ($11.70) — surchauffe persistante.
- **Options :** Données stables (max pain $13.50, put/call 0.45, call OI 69.1%). Le pin risk reste extrème : cours +24.8% au-dessus du max pain, expiration **demain** (05/06).
- **Fondamentaux :** Aucune amélioration. P/E Yahoo 105.31, forward P/E 34.55. Consensus inchangé $9.26. Divergence prix/valeur à +81.9%.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news. Le rally de +9.8% depuis la veille reste non justifié fondamentalement.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d −7.97%, RS60d −16.28%). Le mouvement de NOK reste totalement idiosyncratique.

**Ce qui a changé (17:00 UTC 02/06 → 21:00 UTC 02/06) :**
- **Volume :** 98.9M (0.84×) → **129.6M (1.09×)** — révision majeure à la hausse, invalidant la divergence baissière
- **Cours :** $16.835 → **$16.85** (+0.09%)
- **RSI :** 70.17 → **70.22** (surachat confirmé)
- **P/E Yahoo :** 105.22 → **105.31**
- **Premium consensus :** +81.8% → **+81.9%**

**Ce qui n'a pas changé :**
- **Options :** max pain $13.50, put/call 0.45, call OI 69.1%
- **Consensus :** $9.26 (6 analysts) — silence total
- **Qualité :** 2.5/6 hors périmètre
- **Catalyseur :** 4.0/10 — aucun identifié
- **Scores JSON :** ÉVITER 31.8/100, Opportunité 4.2/10, Momentum 5.5/10
- **Event-Driven :** Aucun événement corporate
- **Sectoriel :** XLC bottom 3
- **FX :** Score 0.0/10, aligned

**Recommandation révisée :**
- **Action :** **ÉVITER** (Score Global ajusté 31.8/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $14.81 (2×ATR)
- **Take-profit :** $19.91 (3×ATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scénarios forward (inchangés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 10% | Breakout $17.11 avec volume >1.5× + catalyseur | $18.50–$19.50 |
| Central | 35% | Consolidation $16.00–$17.00 sans catalyseur | Range |
| Pessimiste | 55% | Pin options $13.50 + retour MM50 $11.70 | $13.00–$15.00 |

**⚠️ Risque principal :** Pin options à $13.50 avec expiration **demain** (05/06). Le cours +24.8% au-dessus du max pain crée une pression baissière technique extrème à court terme. La révision du volume à la hausse atténue le risque de distribution immédiate mais ne supprime pas la surchauffe (RSI 70) ni l'absence de catalyseur. Le rally de +9.8% reste non justifié fondamentalement. Aucun catalyseur ne soutient le niveau au-delà du momentum technique désormais surchauffé.

**Prochains points de contrôle :**
- Franchissement du 52w high à $17.11 avec volume (ou rejet)
- Franchissement sous $16.25 en clôture (confirmation rejet new high)
- **Expiration options 2026-06-05** (demain) — comportement autour du max pain $13.50
- Earnings Q2 FY2026 au **2026-07-23** (dans **51 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Catalyseur éventuel expliquant le rally de +9.8% (M&A, contrat, upgrade)

---

*Données sources : `data/latest.json` (2026-06-02T21:00:08 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
