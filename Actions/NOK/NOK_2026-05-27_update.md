# NOK — Mise à Jour Quotidienne (2026-05-27, Snapshot 17:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-27 | Données source : `data/latest.json` (snapshot 2026-05-27T17:00:08 UTC)

---

## 1. Résumé des changements depuis l'analyse précédente (2026-05-27 13:00 UTC)

| Indicateur | Snapshot 13:00 UTC | Snapshot 17:00 UTC | Variation | Signal |
|-----------|-------------------|-------------------|-----------|--------|
| Cours close | $16.46 | **$15.698** | **−4.63%** | 🔴 Correction marquée post-gap |
| Change % vs previous close | +6.40% | **−4.63%** | −11.03 pp | Inversion de polarité — passage de gap haussier à gap baissier |
| RSI 14j | 67.16 | **63.35** | −3.81 | Sortie de la zone proche surachat (>70) |
| ATR 14j | $1.00 | **$1.03** | +$0.03 | Volatilité en légère expansion |
| Volume | 188,895,200 | **90,863,578** | **−51.9%** | 🔴 Effondrement du volume — absence de suivi acheteur |
| Volume relatif | 1.56× | **0.76×** | −0.80× | Retour sous la moyenne 20j |
| 52-week high | $16.63 | **$16.63** | — | Inchange — high du 26/05 non dépassé |
| High intraday | $16.63 | **$16.05** | −$0.58 | 🔴 Rejet sous le 52w high |
| Low intraday | $15.66 | **$15.54** | −$0.12 | Support intraday légèrement abaissé |
| P/E (TTM Yahoo) | 102.88 | **98.11** | −4.77 | Contraction mécanique avec la baisse du cours |
| Forward P/E | 33.75 | **32.19** | −1.56 | Contraction mécanique |
| P/B | 3.74 | **3.57** | −0.17 | Contraction mécanique |
| Premium vs consensus $9.26 | +77.8% | **+69.5%** | −8.3 pp | Divergence prix/valeur légèrement atténuée mais toujours extrême |
| Consensus analystes (FMP) | $9.26 (6) | **$9.26 (6)** | Inchange | Silence total maintenu |
| **Max pain options** | $16.00 | **$16.00** | $0.00 | Inchange |
| **Put/Call ratio** | 0.53 | **0.53** | 0.00 | Inchange |
| **Call OI** | 65.3% | **65.3%** | 0.0 pp | Inchange |
| **Cours vs max pain** | +2.9% | **−1.9%** | −4.8 pp | 🔴 Inversion : le cours passe **sous** le max pain |

**Changements significatifs détectés :**
- **🔴 Correction de −4.63%** : le cours qui avait grimpé de +15.6% en deux séances (25–26/05) sans catalyseur subit aujourd'hui une correction marquée. Le close $15.698 est le plus bas depuis le gap du 26/05 ($15.66).
- **🔴 Effondrement du volume** : le volume chute de 188.9M à 90.9M (−51.9%), passant de 1.56× à 0.76× la moyenne 20j. Cette absence de volume acheteur au retour confirme que le mouvement haussier précédent n'était pas soutenu par une accumulation institutionnelle durable.
- **🔴 Inversion cours/max pain** : le cours ($15.698) passe **sous** le max pain ($16.00) pour la première fois depuis le début du suivi du pin. À 13:00 UTC, le cours était +2.9% au-dessus ; il est désormais −1.9% en-dessous. Cela crée un **risque de pin gamma inversé** : le marché options a un incitant à remonter le cours vers $16.00 à l'expiration du 29 mai, mais la tendance intraday est baissière.
- **🟢 RSI en sortie de surachat** : le RSI recule de 67.16 à 63.35, sortant de la zone critique >70. Cela réduit le risque de correction technique par surachat, mais ne signale pas un retournement haussier.
- **Aucun catalyseur fondamental** identifié dans `data/events_latest.json` (vide pour NOK).

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Cours close | $15.698 | Yahoo Finance | −4.63% vs previous close ($16.46) |
| Open | $16.00 | Yahoo Finance | Ouverture sous le close précédent — gap baissier d'ouverture |
| High intraday | $16.05 | Yahoo Finance | Rejet net sous le 52w high ($16.63) |
| Low intraday | $15.54 | Yahoo Finance | Support intraday abaissé vs $15.66 du 26/05 |
| Volume | 90,863,578 | Yahoo Finance | 0.76× moyenne 20j (119,048,713) — volume d'absence |
| RSI 14j | 63.35 | Calcul agent | Zone neutre haute, sortie de la zone surachat |
| ATR 14j | $1.03 | Calcul agent | 6.56% du cours — volatilité en légère expansion |
| MM 50j | $11.10 | Calcul agent | Cours +41.4% au-dessus du support structurel (vs +50.4% hier) |
| MM 200j | — | Calcul agent | Non disponible |
| Golden Cross | Non | Calcul agent | — |
| Beta | 0.765 | Yahoo Finance | Faible sensibilité au marché — mouvement idiosyncratique |

**Niveaux clés (révisés) :**
- **Support immédiat :** $15.54 (low du jour) / $15.47 (close du 25/05, base du premier gap)
- **Support structural :** $11.10 (MM 50j)
- **Résistance :** $16.00 (max pain options, désormais résistance) / $16.63 (52-week high)
- **Stop-loss ATR (2×) :** $13.64 ($15.698 − $2.06)
- **Take-profit ATR (3×) :** $18.79 ($15.698 + $3.09)
- **Ratio R/R :** 1.5

**Mise à jour options — impact technique :**
| Niveau | Valeur 13:00 UTC | Valeur 17:00 UTC | Interprétation |
|--------|-------------|-------------------|----------------|
| Max pain | $16.00 | **$16.00** | Inchange — pin gamma inchangé |
| Put/Call ratio | 0.53 | **0.53** | Stable — dominance calls modérée |
| Call OI % | 65.3% | **65.3%** | Stable — structure bullish inchangée |
| Cours vs max pain | +2.9% | **−1.9%** | 🔴 **Inversion** : le cours passe sous le pin |
| Expiration | 2026-05-29 | **2026-05-29** | **2 jours** — risque de pin inversé |

**Verdict timing :** Neutre à défavorable. La correction de −4.63% sur volume effondré (0.76×) est un signal technique négatif majeur : elle indique que le double gap haussier (+15.6% en 2j) n'avait pas de fondamental solide et que les acheteurs ont disparu. L'inversion du cours sous le max pain ($16.00) crée un nouveau risque : si le cours ne remonte pas au-dessus de $16.00 avant l'expiration du 29 mai, le pin gamma pourrait exercer une pression vendeuse supplémentaire. Cependant, le RSI à 63.35 n'est plus en surachat, ce qui réduit le risque de continuation baissière par correction technique pure.

**Score Momentum :** 6.0/10 — révisé à la baisse dans `recommandations_latest.json` (vs 7.0/10 dans l'analyse 13:00 UTC). La perte du double gap et le rejet sous le 52w high pèsent sur le momentum.

---

## 3. Mise à Jour Fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | $87.63 B | Yahoo Finance |
| P/E (TTM Yahoo) | 98.11 | Yahoo Finance |
| Forward P/E (Yahoo) | 32.19 | Yahoo Finance |
| EV/EBITDA (Yahoo) | 35.33 | Yahoo Finance |
| P/B (Yahoo) | 3.57 | Yahoo Finance |
| Dividend yield (Yahoo) | 1.00% | Yahoo Finance |

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

**Note fondamentale :** Aucune donnée fondamentale nouvelle entre le snapshot 13:00 UTC et 17:00 UTC. La contraction du P/E (98.11 vs 102.88) et du forward P/E (32.19 vs 33.75) est purement mécanique, liée à la baisse du cours de −4.63%. Le consensus inchangé à $9.26 sur 6 analystes maintient la divergence à +69.5% (vs +77.8% hier). Aucun upgrade, downgrade ou révision d'estimations n'a été détecté.

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 98.1 vs FMP 45.8 ; P/B Yahoo 3.57 vs FMP 1.42. Cette divergence n'affecte pas le verdict consensus calibré sur l'ADR, mais elle signale que le multiple ADR reste en surchauffe extrême même après la correction.

**Score Valorisation :** 3.5/10 — plafonné par règle Filtre Qualité ≤ 3/6 (max 5/10). Premium +69.5% vs consensus, P/E 98.1, forward P/E 32.2 sur stock mature.

---

## 4. Mise à Jour Sentiment & Options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API | Aucune révision détectée — silence total malgré la volatilité |
| Nombre analysts actifs (mois) | 0 | FMP Stable API | Faible couverture, aucun upgrade massif |
| Put/Call ratio | 0.53 | Yahoo Finance | Dominance calls modérée, inchangée |
| Max pain | $16.00 | Yahoo Finance | Inchange — pin gamma à 2 jours |
| Call OI % | 65.3% | Yahoo Finance | Stable — structure bullish inchangée |
| Short Interest | 1.2% | Yahoo Finance | Faible — pas de squeeze setup |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` | Aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK | Pas de M&A, buyback, guidance, activism |
| Agent FX Exposure | Score 0.0/10, aligned | `fx_exposure_latest.json` | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| News du jour | 0 article | Yahoo Finance | Aucune news NOK identifiée dans le flux |

**Verdict Sentiment :** Neutre à légèrement bearish. La structure options (put/call 0.53, call OI 65.3%) reste bullish, mais le cours qui passe sous le max pain ($16.00) est un signal d'avertissement : les détenteurs de calls pourraient être incités à prendre des bénéfices ou à laisser expirer, tandis que les puts au strike $16.00 deviennent plus attractifs. Le consensus sell-side reste silencieux ($9.26, 6 analysts) et le mouvement reste sans explication fondamentale.

**Score Catalyseur :** 4.0/10 — inchangé dans `recommandations_latest.json`. Aucun catalyseur identifiable ; double gap suivi d'une correction non expliquée par news/event ; earnings éloignés (57 jours).

---

## 5. Scoring Global

**Pondération régime macro :** Inconnu (régime = Unknown dans `recommandations_latest.json`) — appliquée par défaut 35/40/25 (Catalyseur/Valorisation/Momentum).

| Axe | Score | Évolution | Justification |
|-----|-------|-----------|---------------|
| Catalyseur | 4.0/10 | → | Aucun catalyseur identifiable — double gap et correction non expliqués |
| Valorisation | 3.5/10 | → | P/E 98.1, cours +69.5% vs consensus, forward P/E 32.2 |
| Momentum | 6.0/10 | ↓ | Correction −4.63%, rejet sous 52w high, volume effondré — momentum érodé |
| **Score Opportunité** | **4.3/10** | ↓ | (4.0×0.35) + (3.5×0.40) + (6.0×0.25) = 4.3 |
| **Score Global** | **43.0/100** | ↓ | Malus : Valorisation faible + momentum érodé |
| **Score Global ajusté** | **48.0/100** | ↓ | — |

**Action recommandée :** **SURVEILLER** (seuil 35–49)

> Règle de disqualification : aucun score individuel ≤ 2/10 → ticker non exclu.
> Règle Filtre Qualité : score 2.5/6 ≤ 3/6 → Score Valorisation plafonné à 5/10 (appliqué).

**Note de scoring :** Le Score Global ajusté est passé de 50.5/100 (ATTENDRE) à **48.0/100** (SURVEILLER) dans `recommandations_latest.json`. Cette révision à la baisse reflète l'érosion du momentum (7.0 → 6.0) et la correction de −4.63% qui invalide partiellement le double gap haussier. Le titre sort de la zone ATTENDRE pour entrer en zone SURVEILLER, signalant une dégradation du profil risque/rendement.

---

## 6. Révision des niveaux SL/TP

| Niveau | Ancien (13:00 UTC) | Nouveau (17:00 UTC) | Justification |
|--------|---------------------|---------------------|---------------|
| Stop-loss | $14.46 | **$13.64** | Révisé — recalcul ATR 2× ($15.698 − $2.06) |
| Take-profit | $19.46 | **$18.79** | Révisé — recalcul ATR 3× ($15.698 + $3.09) |
| Prix cible (consensus) | $9.26 | $9.26 | Inchange — 6 analysts, silence total |
| Upside consensus | −43.7% | **−41.0%** | Légère amélioration (close plus bas) |
| Downside SL | −12.2% | **−13.1%** | Légère dégradation (ATR plus élevé) |
| Max pain options | $16.00 | **$16.00** | Inchange — désormais résistance au-dessus du cours |

**⚠️ Attention :** Le cours ($15.698) est désormais **−1.9% sous le max pain** ($16.00) avec expiration dans 2 jours (29 mai). Cette inversion est un signal technique négatif : si le cours ne remonte pas au-dessus de $16.00 avant vendredi, les options au strike $16.00 expireront hors de la monnaie pour les calls, ce qui pourrait déclencher une pression vendeuse supplémentaire en fin de semaine. Le SL à $13.64 reste la barrière de sortie principale, mais la probabilité de l'atteindre a augmenté avec la correction du jour.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0, insuffisant | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 3, flag 🟢 (IREN seul flaggé) | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS20d −4.82%, RS60d −10.5%. |
| **Agent FX Exposure** | Score 0.0/10, aligned | Exposition 25% export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention, 0.0/10 | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Watchman** | Earnings 2026-07-23 (57 j) | 🟢 >30j — pas de preview requis. Est EPS $0.06–$0.08, Rev $4.8B |

---

## 8. Conclusion — Évolution de la thèse

**Verdict :** La thèse est **modifiée** — la correction de −4.63% sur volume effondré invalide partiellement le double gap haussier et érode le momentum. L'inversion du cours sous le max pain ($16.00) crée un nouveau risque technique. La recommandation passe de **ATTENDRE** à **SURVEILLER** (Score Global ajusté 48.0/100).

**Analyse :**
- **Technique :** Correction de −4.63% (close $15.698), rejet sous le 52-week high ($16.63 non dépassé), high intraday $16.05. Le double gap haussier (+9.1% le 25/05, +6.4% le 26/05) est partiellement invalidé par la séance du 27/05. RSI 63.35 (sortie de la zone surachat), ATR $1.03 en expansion. Le cours reste +41.4% au-dessus de la MM50 ($11.10).
- **Volume :** 90.9M actions (0.76× moyenne 20j) est un volume d'absence. Après le volume de clôture massif du 26/05 (1.48×) et le volume révisé à la hausse du 27/05 13:00 UTC (1.56×), l'effondrement à 0.76× confirme que les acheteurs institutionnels n'ont pas suivi. Interprétation : distribution retail ou couverture de positions spéculatives.
- **Options (mutation technique) :** Max pain $16.00 inchangé, put/call 0.53, call OI 65.3%. La structure options n'a pas corrigé avec le prix — le marché options maintient son pari haussier. Cependant, le cours sous le max pain (−1.9%) crée un risque de pin inversé à l'expiration du 29 mai.
- **Fondamentaux :** Aucune amélioration. P/E Yahoo 98.1, forward P/E 32.2. Consensus inchangé $9.26. Divergence prix/valeur à +69.5%.
- **Qualité :** Toujours hors périmètre (2.5/6).
- **Catalyseur :** Aucun — pas d'event corporate, pas d'upgrade, pas de guidance raise, pas de news.
- **Sectoriel :** XLC (Communication Services) reste en sous-performance relative vs SPY (bottom 3, RS20d −4.82%). Le mouvement de NOK reste totalement idiosyncratique.

**Ce qui a changé :**
- **Prix :** $16.46 → $15.698 (−4.63%) — correction marquée
- **RSI :** 67.16 → 63.35 — sortie de la zone proche surachat
- **Volume :** 1.56× → 0.76× — effondrement du volume (−51.9% en nombre d'actions)
- **P/E Yahoo :** 102.88 → 98.11 — contraction mécanique
- **Forward P/E :** 33.75 → 32.19 — contraction mécanique
- **Premium consensus :** +77.8% → +69.5% — légère atténuation
- **Cours vs max pain :** +2.9% → **−1.9%** — inversion sous le pin
- **Score Momentum :** 7.0 → 6.0 — érosion du momentum
- **Score Global ajusté :** 50.5 → **48.0** — passage de ATTENDRE à SURVEILLER
- **SL/TP :** $14.46/$19.46 → **$13.64/$18.79** — recalculs sur nouveau close/ATR

**Ce qui n'a pas changé :**
- **Consensus :** $9.26 (6 analysts) — silence total malgré la volatilité
- **Options :** Max pain $16.00, put/call 0.53, call OI 65.3% — structure stable
- **Qualité :** 2.5/6 hors périmètre
- **Catalyseur :** 4.0/10 — aucun identifié
- **52-week high :** $16.63 — non dépassé

**Recommandation révisée :**
- **Action :** **SURVEILLER** (Score Global ajusté 48.0/100)
- **Prix cible :** $9.26 (consensus inchangé)
- **Stop-loss :** $13.64 (révisé — 2×ATR)
- **Take-profit :** $18.79 (révisé — 3×ATR)
- **Ratio R/R :** 1.5
- **Sizing :** — (pas de position)

**Scénarios forward (révisés) :**
| Scénario | Probabilité | Trigger | Impact cours |
|----------|-------------|---------|------------|
| Optimiste | 15% | Remontée vers max pain $16.00 avant expiration 29/05 + catalyseur non capturé | $16.00–$17.50 |
| Central | 50% | Consolidation autour de $15.50–$16.00 avec test du max pain à l'expiration | Range |
| Pessimiste | 35% | Aucun catalyseur + pin inversé → retour vers $15.00 puis $14.50 | $14.50–$15.50 |

**⚠️ Risque principal :** Double gap haussier non expliqué suivi d'une correction de −4.63% sur volume effondré = mouvement parabolique vulnerable. Le max pain options à $16.00 avec expiration dans 2 jours est désormais une résistance au-dessus du cours. Un franchissement sous $15.47 (close du 25/05, base du premier gap) déclencherait une accélération vendeuse vers $14.50. Le SL à $13.64 est la barrière de sortie principale.

**Prochains points de contrôle :**
- Expiration options **2026-05-29** (dans **2 jours**) — observer le pin au max pain $16.00 et le comportement du cours autour de ce niveau
- Earnings Q2 FY2026 au **2026-07-23** (dans **57 jours**) — Est EPS $0.06–$0.08, Rev $4.8B
- Franchissement technique du SL à $13.64
- Franchissement sous $15.47 (base du gap du 25/05)
- Catalyseur éventuel expliquant le double gap (M&A, contrat, upgrade)

---

*Données sources : `data/latest.json` (2026-05-27T17:00:08 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Aucune donnée hallucinée.*
