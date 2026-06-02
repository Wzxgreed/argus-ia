# NOK — Mise à Jour Quotidienne (2026-06-02, Snapshot 13:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-06-02 | Données source : `data/latest.json` (snapshot 2026-06-02T13:00:08 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (Snapshot 10:00 UTC 02/06)

| Indicateur | Snapshot 10:00 UTC (02/06) | Snapshot 13:00 UTC (02/06) | Variation | Signal |
|-----------|---------------------------|---------------------------|-----------|--------|
| Cours close | $16.25 | **$16.25** | — | → Stable |
| RSI 14j | 62.59 | **62.59** | — | → Zone neutre haute |
| ATR 14j | $1.04 | **$1.04** | — | → Trigger ATR_SPIKE actif |
| Volume | 171,815,100 | **171,815,100** | — | → 1.45× moyenne 20j confirmé |
| High intraday | $16.52 | **$16.52** | — | → Résistance du jour respectée |
| Low intraday | $14.93 | **$14.93** | — | → Support du jour respecté |
| P/E (TTM Yahoo) | 101.56 | **101.56** | — | → Valorisation inchangée |
| Forward P/E | 33.32 | **33.32** | — | → Stable |
| Premium vs consensus $9.26 | +75.5% | **+75.5%** | — | → Divergence inchangée |
| MM 50j | $11.53 | **$11.53** | — | → Tendance haussière intacte |
| **Max pain options** | $2.00 (corrompu) | **$13.50** | ✅ Restauré | → Données Yahoo corrigées |
| **Put/Call ratio** | null (corrompu) | **0.45** | ✅ Restauré | → Structure call-dominated confirmée |
| **Call OI** | null (corrompu) | **69.1%** | ✅ Restauré | → Forte activité call confirmée |

**Changements significatifs détectés :**
- **→ Stabilité totale du prix et des métriques techniques** entre 10h et 13h UTC. Le cours $16.25 est strictement identique, confirmant l'absence de mutation intraday.
- **→ ✅ Données options restaurées** dans `data/latest.json` : le max pain revient à **$13.50** (vs $2.00 aberrant à 10h), le put/call ratio à **0.45** (vs null), et le call OI à **69.1%** (vs null). Ces valeurs confirment les données opérationnelles du snapshot 21h du 01/06 (max pain $13.50, put/call 0.46, call OI 68.5%) avec une légère convergence vers une structure légèrement plus call-heavy.
- **→ Volume, RSI, ATR, fondamentaux inchangés** : aucune nouvelle donnée FMP, aucun consensus révisé, aucune news.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $16.25 | Yahoo Finance | Inchangé vs snapshot 10h UTC 02/06 |
| Open | $15.07 | Yahoo Finance | Gap haussier d'ouverture +1.55% (séance 01/06) |
| High intraday | $16.52 | Yahoo Finance | Test de résistance sous le 52w high |
| Low intraday | $14.93 | Yahoo Finance | Support égal au low matinal |
| Volume | 171,815,100 | Yahoo Finance | **1.45× moyenne 20j** — participation élevée confirmée |
| RSI 14j | 62.59 | Calcul agent | Zone neutre haute, pas de surachat |
| ATR 14j | $1.04 | Calcul agent | 6.40% du cours — trigger ATR_SPIKE actif |
| MM 50j | $11.53 | Calcul agent | Cours +40.9% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché |

**Niveaux clés (inchangés) :**
- **Support immédiat :** $15.47 (ancien support, base du gap du 25/05) / $14.93 (low du jour)
- **Support structural :** $11.53 (MM 50j)
- **Résistance :** $16.52 (high du jour) / $16.63 (52-week high) / $17.87 (take-profit ATR)
- **Stop-loss ATR (2×) :** $14.17 ($16.25 − $2.08)
- **Take-profit ATR (3×) :** $19.37 ($16.25 + $3.12)
- **Ratio R/R :** 1.5

**Mise à jour options — données restaurées dans `latest.json` :**
| Niveau | Valeur 10:00 UTC (02/06) | Valeur 13:00 UTC (02/06) | Interprétation |
|--------|-------------------------|-------------------------|----------------|
| Max pain | $2.00 (corrompu) | **$13.50** | ✅ Valeur restaurée — cohérente avec historique |
| Put/Call ratio | null (corrompu) | **0.45** | ✅ Structure bullish (dominance calls) |
| Call OI % | null (corrompu) | **69.1%** | ✅ Forte activité call — détenteurs ITM exposés au pin |
| Expiration | 2026-06-05 | **2026-06-05** | **2 jours restants** |

> **🔴 Pin risk extrème à l'expiration 05/06.** Le cours ($16.25) reste **+20.4% au-dessus du max pain** ($13.50). Avec **2 jours restants** avant expiration vendredi, la pression de mean-reversion vers $13.50 reste élevée en l'absence de catalyseur. La restauration des données options confirme l'alerte émise à 10h : la structure call-dominated est intacte et la divergence est réelle.

**Verdict timing :** Favorable structurellement (cours au-dessus de MM50, tendance haussière intacte), mais **défavorable à court terme** (pin risk extrême + proximité du 52w high + absence de catalyseur). Le verdict est **favorable pour le momentum** mais **défavorable pour le timing d'entrée**.

**Score Momentum :** 7.0/10 — inchangé dans `recommandations_latest.json`. Le momentum structurel est soutenu par le maintien au-dessus de la MM50 et le volume supérieur à la moyenne.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $90.72 B | Yahoo Finance |
| P/E (TTM Yahoo) | 101.56 | Yahoo Finance |
| Forward P/E (Yahoo) | 33.32 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 34.871 | Yahoo Finance |
| P/B (Yahoo) | 3.69 | Yahoo Finance |
| Dividend yield (Yahoo) | 1.01% | Yahoo Finance |

**Données opérationnelles FMP (FY 2025) :**
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

**Filtre Qualité (6 critères) :**
| Critère | Évaluation | Justification |
|---------|------------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ Non | Croissance anémique du top-line (mature 5G) |
| Profit CAGR 5 ans ≥ 20% | ❌ Non | Rentabilité historiquement faible |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.58, net cash position |
| FCF positif et croissant 5 ans | ⚠️ Partiel | FCF yield 4.9% mais trajectoire instable |
| Avantage compétitif (moat) | ⚠️ Partiel | Leader 5G historique mais part de marché sous pression |
| Industrie forte croissance (TAM ×5) | ❌ Non | TAM 5G mature, croissance à simple digit |
| **Score Qualité total** | **2.5/6** | 🔴 Hors périmètre (inchangé) |

**Note fondamentale :** Aucune donnée fondamentale nouvelle depuis le snapshot 10h du 02/06. Le consensus inchangé à $9.26 sur 6 analystes maintient la divergence à **+75.5%**. Aucun upgrade, downgrade ou révision d'estimations n'a été détecté. Le quality report du pipeline matinal confirme le warning « Quality hors périmètre 2–2.5/6 ; P/E 87.19 très élevé ; Cours +50% vs consensus » — ce warning est qualitatif et n'indique pas de données manquantes.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +75.5% vs consensus, P/E 101.56, forward P/E 33.32 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision — silence total malgré la volatilité |
| Nombre analysts actifs (mois) | 0 | FMP Stable API | Faible couverture |
| Put/Call ratio | 0.45 | Yahoo Finance (restauré) | Structure bullish (dominance calls) — confirmé vs 0.46 opérationnel |
| Max pain | $13.50 | Yahoo Finance (restauré) | 🔴 Risque pin baissier extrême à l'expiration 05/06 |
| Call OI % | 69.1% | Yahoo Finance (restauré) | Forte activité call — détenteurs ITM exposés au pin |
| Short Interest | 1.08% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiée dans le flux |

**Verdict Sentiment :** Neutre à légèrement bearish à court terme. La structure options est désormais **confirmée par des données propres** : put/call 0.45 et call OI 69.1% sont cohérents avec les valeurs opérationnelles du 01/06. Le max pain $13.50 est rétabli, confirmant le **pin risk baissier extrême** ($16.25 vs $13.50, soit +20.4% de divergence). Le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement reste sans explication fondamentale.

**Score Catalyseur :** 4.0/10 — inchangé dans `recommandations_latest.json`. Aucun catalyseur identifiable ; earnings éloignés (51 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Unknown (régime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable |
| Valorisation | 3.5/10 | → | P/E 101.56, cours +75.5% vs consensus |
| Momentum | 7.0/10 | → | Maintien au-dessus MM50, volume confirmé, rally +9.5% |
| **Score Opportunité** | **4.5/10** | → | (4.0×0.35) + (3.5×0.40) + (7.0×0.25) = 4.5 |
| **Score Global** | **45.5/100** | → | Malus : Valorisation faible + pin risk extrême |
| **Score Global ajusté** | **50.5/100** | → | Seuil ATTENDRE (50–59) maintenu |

**Action recommandée :** **ATTENDRE** (seuil 50–59)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (10:00 UTC 02/06) | Nouveau (13:00 UTC 02/06) | Justification |
|--------|--------------------------|--------------------------|---------------|
| Stop-loss | $14.17 | **$14.17** | Inchangé — ATR 2× ($16.25 − $2.08) |
| Take-profit | $19.37 | **$19.37** | Inchangé — ATR 3× ($16.25 + $3.12) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | −43.0% | **−43.0%** | Inchangé |
| Downside SL | −12.8% | **−12.8%** | Stable |

**⚠️ Attention :** Le cours ($16.25) est revenu au-dessus du support $15.47 et approche le 52w high ($16.63). Si le cours casse $16.52 en clôture avec volume, le test du 52w high ($16.63) devient probable à court terme. Inversement, si le cours clôture sous $15.47, le faux breakout haussier du 01/06 sera confirmé et le risque de retour vers $14.17 (SL) puis $13.50 (max pain) augmente. Le **pin risk options ($13.50, expiration 05/06)** reste la menace principale à court terme. Avec **2 jours restants** avant l'expiration, la pression technique s'intensifie.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −6.21%, RS60d −13.72%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (51 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |
| **Quality Report** | Warning | Quality hors périmètre 2–2.5/6 ; P/E élevé ; cours +50% vs consensus. Pas d'exclusion. |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **confirmée** — le snapshot 13:00 UTC du 02/06 ne révèle aucune mutation significative par rapport au snapshot 10:00 UTC du 02/06. La recommandation reste **ATTENDRE** (Score Global ajusté 50.5/100). L'entrée reste exclue.

**Analyse :**
- **Technique :** Cours stable $16.25 (strictement inchangé vs snapshot 10h UTC 02/06). Le high du jour ($16.52) teste la résistance avant le 52w high ($16.63). RSI 62.59 (pas de surachat). ATR $1.04 (trigger ATR_SPIKE actif à 6.40%). Volume 171.8M (1.45×) — participation élevée confirmée. Le cours reste +40.9% au-dessus de la MM50 ($11.53) — tendance haussière structurelle intacte.
- **Options :** ✅ **Données restaurées** dans `data/latest.json` : max pain $13.50 (vs $2.00 anomalie à 10h), put/call 0.45 (vs null), call OI 69.1% (vs null). Ces valeurs confirment la structure call-dominated et le **pin risk baissier extrême** à l'expiration vendredi 05/06 (dans 2 jours). Le cours +20.4% au-dessus du max pain crée une pression technique réelle.
- **Volume :** 171.8M (1.45×) — volume total élevé confirmé. La participation élevée suggère des ajustements de positions avant l'expiration vendredi.
- **Fondamentaux :** Aucune amélioration. P/E Yahoo 101.56, forward P/E 33.32. Consensus inchangé $9.26. Divergence prix/valeur à +75.5%.
- **Qualité :** Toujours hors périmètre (2.5/6). Quality report du matin confirme le warning.
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news. Le rally de +9.5% reste non justifié fondamentalement.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d −6.21%). Le mouvement de NOK reste totalement idiosyncratique.

**Ce qui a changé (10:00 UTC 02/06 → 13:00 UTC 02/06) :**
- **Options :** Données corrompues → **données restaurées** (max pain $13.50, put/call 0.45, call OI 69.1%). C'est la seule mutation.

**Ce qui n'a pas changé :**
- **Cours :** $16.25 — strictement identique
- **Consensus :** $9.26 (6 analysts) — silence total
- **Qualité :** 2.5/6 hors périmètre
- **Catalyseur :** 4.0/10 — aucun identifié
- **Event-Driven :** Aucun événement corporate
- **Sectoriel :** XLC bottom 3
- **Score Global ajusté :** 50.5/100 — ATTENDRE maintenu

**Recommandation révisée :**
- **Action :** **ATTENDRE** (Score Global ajusté 50.5/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $14.17 (2×ATR)
- **Take-profit :** $19.37 (3×ATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scénarios forward (inchangés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 15% | Breakout $16.63 + catalyseur non capturé | $18.00–$19.00 |
| Central | 45% | Consolidation $15.50–$16.50 sans catalyseur | Range |
| Pessimiste | 40% | Pin options $13.50 + retour MM50 $11.53 | $12.00–$14.00 |

**⚠️ Risque principal :** Pin options à $13.50 avec expiration dans **2 jours** (05/06). Le cours +20.4% au-dessus du max pain crée une pression baissière technique extrême à court terme. Si le cours clôture sous $15.47, le faux breakout haussier sera confirmé et l'accélération vendeuse vers $14.17 (SL) puis $13.50 devient probable. Le rally de +9.5% est non justifié fondamentalement et donc fragile. Aucun catalyseur ne soutient le niveau au-delà du momentum technique.

**Prochains points de contrôle :**
- Franchissement du 52w high à $16.63 (ou rejet)
- Franchissement sous $15.47 en clôture (confirmation faux breakout)
- **Expiration options 2026-06-05** (vendredi, dans 2 jours) — comportement autour du max pain $13.50
- Earnings Q2 FY2026 au **2026-07-23** (dans **51 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Catalyseur éventuel expliquant le rally de +9.5% (M&A, contrat, upgrade)

---

*Données sources : `data/latest.json` (2026-06-02T13:00:08 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
