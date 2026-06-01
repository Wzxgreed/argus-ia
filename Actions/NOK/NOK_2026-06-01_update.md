# NOK — Mise à Jour Quotidienne (2026-06-01, Snapshot 10:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-06-01 | Données source : `data/latest.json` (snapshot 2026-06-01T10:00:08 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (2026-05-27 17:00 UTC)

| Indicateur | Snapshot 27/05 | Snapshot 01/06 | Variation | Signal |
|-----------|----------------|----------------|-----------|--------|
| Cours close | $15.698 | **$14.84** | **−5.47%** | 🔴 Correction continue post-gap |
| Change % vs previous close | −4.63% | **−2.88%** | +1.75 pp | Correction ralentie mais persistante |
| RSI 14j | 63.35 | **61.3** | −2.05 | Zone neutre haute, pas de surachat |
| ATR 14j | $1.03 | **$1.01** | −$0.02 | Volatilité légèrement contractée |
| Volume | 90,863,578 | **112,624,800** | **+23.9%** | 🟢 Retour à la moyenne 20j |
| Volume relatif | 0.76× | **0.96×** | +0.20× | Normalisation — plus d'absence |
| 52-week high | $16.63 | **$16.63** | — | Inchange — high du 26/05 non re-testé |
| High intraday | $16.05 | **$15.26** | −$0.79 | 🔴 Rejet continu sous résistance |
| Low intraday | $15.54 | **$14.53** | −$1.01 | 🔴 **Casse du support $15.47** |
| P/E (TTM Yahoo) | 98.11 | **92.75** | −5.36 | Contraction mécanique avec baisse cours |
| Forward P/E | 32.19 | **30.43** | −1.76 | Contraction mécanique |
| P/B | 3.57 | **3.37** | −0.20 | Contraction mécanique |
| Premium vs consensus $9.26 | +69.5% | **+60.2%** | −9.3 pp | Divergence prix/valeur atténuée mais extrême |
| Consensus analystes (FMP) | $9.26 (6) | **$9.26 (6)** | Inchange | Silence total maintenu |
| MM 50j | $11.10 | **$11.37** | +$0.27 | Support structurel remonté |
| **Max pain options** | $16.00 | **$2.00** | −$14.00 | 🔴 **Anomalie données options** |
| **Put/Call ratio** | 0.53 | **None** | — | Données indisponibles |
| **Call OI** | 65.3% | **None** | — | Données indisponibles |

**Changements significatifs détectés :**
- **🔴 Cassure du support $15.47** : le low intraday $14.53 passe sous la base du gap haussier du 25/05 ($15.47) et sous le low du 27/05 ($15.54). Cette cassure technique ouvre un risque de retour vers la zone $14.00–$14.50, voire le close d'avant-gap (~$14.18).
- **🟢 Normalisation du volume** : le volume remonte à 112.6M (0.96× moyenne 20j), contre 90.9M (0.76×) au 27/05. La correction n'est pas accompagnée d'un volume de panique — signal d'absence de distribution institutionnelle massive.
- **🔴 Données options corrompues** : max pain passe à $2.00 (anomalie Yahoo évidente), put/call et call OI passent à `null`. Ces données sont non exploitables. Le max pain opérationnel du 27/05 ($16.00) est conservé en référence mentale mais non fiable à ce stade.
- **🔴 Options data indisponible** : absence de put/call ratio et call OI — impossible d'évaluer le sentiment options. Cette dégradation de la qualité de données est à surveiller.
- **Aucun catalyseur fondamental** identifié dans `data/events_latest.json` (vide pour NOK).

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $14.84 | Yahoo Finance | −2.88% vs previous close ($15.28) |
| Open | $15.18 | Yahoo Finance | Gap baissier d'ouverture — sous le close précédent |
| High intraday | $15.26 | Yahoo Finance | Rejet net sous le 52w high ($16.63) |
| Low intraday | $14.53 | Yahoo Finance | **Casse du support $15.47** |
| Volume | 112,624,800 | Yahoo Finance | 0.96× moyenne 20j (117,493,570) — volume normal |
| RSI 14j | 61.3 | Calcul agent | Zone neutre haute, sortie de surachat confirmée |
| ATR 14j | $1.01 | Calcul agent | 6.81% du cours — trigger ATR_SPIKE actif (seuil 5.0%) |
| MM 50j | $11.37 | Calcul agent | Cours +30.5% au-dessus du support structurel |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché — mouvement idiosyncratique |

**Niveaux clés (révisés) :**
- **Support immédiat :** $14.53 (low du jour) / $14.18 (close estimé du 24/05, base d'avant-gap)
- **Support structural :** $11.37 (MM 50j)
- **Résistance :** $15.26 (high du jour) / $15.47 (ancien support, désormais résistance) / $16.63 (52-week high)
- **Stop-loss ATR (2×) :** $12.82 ($14.84 − $2.02)
- **Take-profit ATR (3×) :** $17.87 ($14.84 + $3.03)
- **Ratio R/R :** 1.5

**Mise à jour options — anomalie majeure :**
| Niveau | Valeur 27/05 | Valeur 01/06 | Interprétation |
|--------|-------------|--------------|----------------|
| Max pain | $16.00 | **$2.00** | 🔴 **Anomalie Yahoo** — données corrompues, non fiables |
| Put/Call ratio | 0.53 | **None** | Données indisponibles |
| Call OI % | 65.3% | **None** | Données indisponibles |
| Expiration | 2026-05-29 | **2026-06-05** | Nouvelle expiration la plus proche |

> **⚠️ Données options Yahoo corrompues.** Le max pain $2.00 est irréaliste (94% sous le cours). Put/call ratio et call OI sont `null`. L'analyse options est suspendue jusqu'à restauration des données. En référence historique, la structure était bullish (put/call 0.53, call OI 65.3%) au 27/05.

**Verdict timing :** Neutre à défavorable. La cassure du support $15.47 est un signal technique négatif majeur qui confirme l'invalidation du double gap haussier du 25–26/05. Cependant, la correction se déroule sur volume normal (0.96×), sans panique, et le RSI à 61.3 n'est pas en zone de survente. Le cours reste +30.5% au-dessus de la MM 50j, ce qui maintient une tendance haussière structurelle à moyen terme. Le verdict est **défavorable à court terme** (risque de retour $14.00–$14.50) mais **neutre à moyen terme** (tendance MM50 intacte).

**Score Momentum :** 6.5/10 — révisé à la hausse dans `recommandations_latest.json` (vs 6.0/10 au 27/05). Le maintien au-dessus de la MM 50j et la normalisation du volume soutiennent le momentum structurel, malgré la cassure du support $15.47.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $82.84 B | Yahoo Finance |
| P/E (TTM Yahoo) | 92.75 | Yahoo Finance |
| Forward P/E (Yahoo) | 30.43 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 31.76 | Yahoo Finance |
| P/B (Yahoo) | 3.37 | Yahoo Finance |
| Dividend yield (Yahoo) | 1.10% | Yahoo Finance |

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

**Note fondamentale :** Aucune donnée fondamentale nouvelle depuis le 27/05. La contraction du P/E (92.75 vs 98.11) et du forward P/E (30.43 vs 32.19) est purement mécanique, liée à la baisse du cours de −5.47% depuis le dernier snapshot. Le consensus inchangé à $9.26 sur 6 analystes maintient la divergence à +60.2% (vs +69.5% précédemment). Aucun upgrade, downgrade ou révision d'estimations n'a été détecté.

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 92.75 vs FMP 45.81 ; P/B Yahoo 3.37 vs FMP 1.42. Cette divergence n'affecte pas le verdict consensus calibré sur l'ADR, mais elle signale que le multiple ADR reste en surchauffe extrême même après la correction.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +60.2% vs consensus, P/E 92.75, forward P/E 30.43 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision détectée — silence total malgré la volatilité |
| Nombre analysts actifs (mois) | 0 | FMP Stable API | Faible couverture, aucun upgrade massif |
| Put/Call ratio | None | Yahoo Finance | 🔴 Données indisponibles |
| Max pain | $2.00 | Yahoo Finance | 🔴 **Anomalie** — valeur irréaliste, non fiable |
| Call OI % | None | Yahoo Finance | 🔴 Données indisponibles |
| Short Interest | 1.08% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiée dans le flux |

**Verdict Sentiment :** Neutre à légèrement bearish. L'absence totale de données options rend l'évaluation du sentiment institutionnel impossible. Historiquement, la structure était bullish (put/call 0.53, call OI 65.3%), mais cette configuration est obsolète face à la correction de −5.47% et à la cassure du support $15.47. Le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement reste sans explication fondamentale.

**Score Catalyseur :** 4.0/10 — inchangé dans `recommandations_latest.json`. Aucun catalyseur identifiable ; double gap suivi d'une correction non expliquée par news/event ; earnings éloignés (52 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Unknown (régime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable — double gap et correction non expliqués |
| Valorisation | 3.5/10 | → | P/E 92.75, cours +60.2% vs consensus, forward P/E 30.43 |
| Momentum | 6.5/10 | ↑ | Maintien au-dessus MM50 ($11.37), volume normalisé, RSI 61.3 sain |
| **Score Opportunité** | **4.4/10** | ↑ | (4.0×0.35) + (3.5×0.40) + (6.5×0.25) = 4.4 |
| **Score Global** | **44.2/100** | → | Malus : Valorisation faible + momentum érodé mais structurel |
| **Score Global ajusté** | **49.2/100** | ↑ | — |

**Action recommandée :** **SURVEILLER** (seuil 35–49)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

**Note de scoring :** Le Score Global ajusté est passé de 48.0/100 au 27/05 à **49.2/100** dans `recommandations_latest.json`. Cette révision à la marge reflète la légère amélioration du momentum (6.0 → 6.5) due au maintien au-dessus de la MM 50j et à la normalisation du volume. Le ticker reste fermement dans la zone SURVEILLER. L'entrée reste exclue.

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (27/05) | Nouveau (01/06) | Justification |
|--------|-----------------|-----------------|---------------|
| Stop-loss | $13.64 | **$12.82** | Révisé — recalcul ATR 2× ($14.84 − $2.02) |
| Take-profit | $18.79 | **$17.87** | Révisé — recalcul ATR 3× ($14.84 + $3.03) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | −41.0% | **−37.6%** | Légère amélioration (close plus bas) |
| Downside SL | −13.1% | **−13.6%** | Légère dégradation (prix plus bas) |

**⚠️ Attention :** Le cours ($14.84) a cassé le support $15.47 (base du gap du 25/05) avec un low à $14.53. Si le cours franchit $14.50 en clôture, le risque d'accélération vendeuse vers $14.00 puis $13.00 augmente significativement. Le SL à $12.82 reste la barrière de sortie principale. En l'absence de données options fiables, le max pain historique ($16.00) n'est plus un repère actif.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −5.97%, RS60d −13.01%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (52 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **confirmée** — la correction post-gap se poursuit de manière ordonnée (volume normal, pas de panique) et le support $15.47 a cédé, ouvrant un risque de retour vers $14.00–$14.50. La recommandation reste **SURVEILLER** (Score Global ajusté 49.2/100).

**Analyse :**
- **Technique :** Correction continue (−2.88% vs previous close, −5.47% depuis le 27/05). Close $14.84, low $14.53. Cassure du support $15.47 (base du gap du 25/05) et du low du 27/05 ($15.54). Le double gap haussier (+9.1% le 25/05, +6.4% le 26/05) est désormais quasi-entièrement invalidé. RSI 61.3 (neutre haute), ATR $1.01 (trigger ATR_SPIKE actif à 6.81%). Le cours reste +30.5% au-dessus de la MM50 ($11.37), maintenant la tendance haussière structurelle.
- **Volume :** 112.6M actions (0.96× moyenne 20j) est un volume normal. Contrairement au 27/05 (0.76×), la séance du 01/06 ne montre pas une absence d'acheteurs. Cependant, le volume n'est pas non plus un signal d'accumulation (pas de spike >1.5×). Interprétation : correction technique ordonnée sans distribution massive.
- **Options (données corrompues) :** Max pain $2.00 (anomalie), put/call et call OI indisponibles. L'analyse options est suspendue. Historiquement, la structure était bullish au 27/05 (put/call 0.53, call OI 65.3%) mais cette configuration est obsolète.
- **Fondamentaux :** Aucune amélioration. P/E Yahoo 92.75, forward P/E 30.43. Consensus inchangé $9.26. Divergence prix/valeur à +60.2%.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d −5.97%, RS60d −13.01%). Le mouvement de NOK reste totalement idiosyncratique et fragile.

**Ce qui a changé :**
- **Prix :** $15.698 → $14.84 (−5.47%) — correction continue
- **RSI :** 63.35 → 61.3 — zone neutre haute stable
- **Volume :** 0.76× → 0.96× — normalisation
- **P/E Yahoo :** 98.11 → 92.75 — contraction mécanique
- **Forward P/E :** 32.19 → 30.43 — contraction mécanique
- **Premium consensus :** +69.5% → +60.2% — atténuation mécanique
- **Support :** Cassure de $15.47 — signal technique négatif
- **MM50 :** $11.10 → $11.37 — support structurel remonté
- **Score Momentum :** 6.0 → 6.5 — maintien au-dessus MM50
- **Score Global ajusté :** 48.0 → **49.2** — inchangé de facto (SURVEILLER)
- **SL/TP :** $13.64/$19.46 → **$12.82/$17.87** — recalculs sur nouveau close/ATR
- **Options data :** Max pain $16.00 → **$2.00 (anomalie)** — données corrompues

**Ce qui n'a pas changé :**
- **Consensus :** $9.26 (6 analysts) — silence total malgré la volatilité
- **Qualité :** 2.5/6 hors périmètre
- **Catalyseur :** 4.0/10 — aucun identifié
- **52-week high :** $16.63 — non re-testé
- **Event-Driven :** Aucun événement corporate

**Recommandation révisée :**
- **Action :** **SURVEILLER** (Score Global ajusté 49.2/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $12.82 (révisé — 2×ATR)
- **Take-profit :** $17.87 (révisé — 3×ATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scénarios forward (révisés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 15% | Catalyseur non capturé + rebond technique sur MM50 | $16.00–$17.00 |
| Central | 50% | Consolidation $14.50–$15.50 sans catalyseur | Range |
| Pessimiste | 35% | Cassure $14.50 en clôture + aucun catalyseur → retour MM50 $11.37 | $12.00–$14.00 |

**⚠️ Risque principal :** Cassure du support $15.47 avec low $14.53. Si le cours clôture sous $14.50, l'accélération vendeuse vers $14.00 puis $13.00 devient probable. Le double gap haussier est quasi-comblé. Aucun catalyseur ne soutient le niveau. Le SL à $12.82 est la barrière de sortie principale. En l'absence de données options fiables, la surveillance du volume et des niveaux techniques est prioritaire.

**Prochains points de contrôle :**
- Franchissement technique du SL à $12.82
- Franchissement sous $14.50 en clôture (risque d'accélération)
- Earnings Q2 FY2026 au **2026-07-23** (dans **52 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Restauration des données options Yahoo (max pain, put/call, call OI)
- Catalyseur éventuel expliquant le double gap (M&A, contrat, upgrade)

---

*Données sources : `data/latest.json` (2026-06-01T10:00:08 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
