# FLY — Mise à Jour (2026-06-08, snapshot 10h UTC)

> **Type :** `_update.md` — Gap -12.65%, cassure MM50, dégradation ATTENDRE → SURVEILLER
> **Référence précédente :** [FLY_2026-06-03_update.md](FLY_2026-06-03_update.md) (snapshot 10h UTC 03/06)
> **Données source :** `data/latest.json` (timestamp 2026-06-08T10:00:09.932317+00:00), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Validation data :** FLY status `ok` dans `data/validation_report.txt`. Aucun warning. 25/29 tickers OK.

---

## Résumé — Gap -12.65%, cassure MM50, dégradation ATTENDRE → SURVEILLER (45.0)

Le snapshot 10h UTC du 2026-06-08 enregistre une **chute de -12.65%** à **$36.10** (vs close 02/06 $43.37), avec un **gap down** depuis le prior close $41.33. L'Agent Recommandation dégrade la thèse de **ATTENDRE (58.0) à SURVEILLER (45.0)**.

**Changements majeurs :**
- **Cassure de la MM 50j** : le spot passe de +14.8% au-dessus ($43.37 vs $37.79) à **-6.5% en dessous** ($36.10 vs $38.63). Cassure technique majeure.
- **RSI** : chute de 54.62 à **45.6**, sortie de la zone neutre haute vers neutre-basse.
- **Momentum** : effondrement de **7.0/10 à 4.0/10** — passage en momentum baissier.
- **Multiples** : compression mécanique (EV/Revenue 34.9x → 28.6x, P/B 6.28 → 5.23) du fait de la chute du cours.
- **Consensus** : inchangé à $43.25 (12 analysts), désormais à **+19.8% au-dessus du spot** (vs -0.3% sous le spot précédemment).
- **Score Opportunité** : stable à **5.3/10** mais composition modifiée (Catalyseur +1.0, Valorisation +1.0, Momentum -3.0).
- **Timing** : passage de **Favorable à Défavorable**.

Aucun catalyst identifié (`events_latest.json` vide pour FLY, `social_sentiment_latest.json` 0 mention). Le mouvement s'effectue sur un volume **6.64M (0.69× moy. 20j)** — inférieur à la moyenne, ce qui atténue l'interprétation d'une liquidation massive.

| Métrique | 2026-06-03 10h UTC | 2026-06-08 10h UTC | Variation |
|----------|--------------------|--------------------|-----------|
| Cours close | $43.37 | **$36.10** | **-$7.27 (-16.8%)** |
| Open | $44.03 | **$39.69** | **Gap down -10.1% vs prior close** |
| High intraday | $46.44 | **$40.79** | **-$5.65** |
| Low intraday | $43.03 | **$35.55** | **-$7.48** |
| Change % vs prior close | −1.97% | **−12.65%** | **Dégradation -10.7 pts** |
| RSI 14j | 54.62 | **45.6** | **-9.0 pts, zone neutre-basse** |
| MM 50j | $37.79 | **$38.63** | **+0.8%** |
| Position vs MM50 | +14.8% au-dessus | **-6.5% en dessous** | **🔴 CASSURE** |
| ATR 14j | $5.91 | **$6.13** | **+3.7%** |
| Volume session | 6.18M | **6.64M** | **+7.4%** |
| Volume vs moy. 20j | 0.64x | **0.69x** | **Légèrement supérieur, reste faible** |
| Forward P/E | −36.99 | **−27.72** | **Moins négatif (mécanique)** |
| EV/Revenue (Yahoo) | 34.892x | **28.591x** | **-18.0% (compression multiple)** |
| P/B (Yahoo) | 6.283 | **5.230** | **-16.8% (compression multiple)** |
| Market Cap (Yahoo) | $7.12B | **$5.93B** | **-$1.19B (-16.7%)** |
| Consensus PT (FMP) | $43.25 (12 analysts) | **$43.25 (12 analysts)** | **Inchangé** |
| Écart consensus | −0.3% sous le spot | **+19.8% au-dessus du spot** | **Réalignement haussier mécanique** |
| Short Interest | 9.78% | **9.78%** | **Stable** |
| Options — Max Pain | $20.00 (anomalie) | **$20.00 (anomalie)** | **Persistant — [DONNÉES PARTIELLES]** |
| Options — Put/Call | null | **null** | **Données manquantes** |
| Options — Call OI % | null | **null** | **Données manquantes** |
| Score Opportunité (agent) | 5.3/10 | **5.3/10** | **Inchangé — shift composition** |
| Score Momentum (agent) | 7.0/10 | **4.0/10** | **🔴 -3.0 pts — baissier** |
| Score Global Ajusté (agent) | 58.0 | **45.0** | **-13.0 pts — passage SURVEILLER** |
| Action | ATTENDRE | **SURVEILLER** | **Dégradation** |
| Timing | Favorable | **Défavorable** | **Dégradation** |

**Verdict :** Gap down de -12.65% sans catalyst, cassure de la MM50, momentum basculé en baissier. La thèse est **modifiée en intensité négative** — passage de ATTENDRE à SURVEILLER. Le consensus inchangé à $43.25 offre un upside mécanique de +19.8%, mais l'absence de support technique immédiat sous $35.55 et la tendance baissière fraîche rendent toute position risquée à court terme.

---

## Mise à jour technique — Cassure MM50, support $35.55 testé

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $36.10 | −12.65% vs prior close $41.33, −51.1% vs 52W high $73.80 |
| Open | $39.69 | Gap down vs prior close $41.33 |
| High | $40.79 | Résistance intraday — non dépassée en clôture |
| Low | $35.55 | **Support du jour testé** — zone critique |
| RSI 14j | **45.6** | **Neutre-basse** — perte de 9.0 pts en 5 séances |
| MM 50j | $38.63 | Cours inférieur de **-6.5%** — cassure technique majeure |
| Volume | 6,641,300 | **0.69× moy. 20j** — volume faible sur un gap de -12.65% |
| ATR 14j | $6.13 | Volatilité élevée persistante (16.98% rel.) |
| Support 1 | $35.55 (Low du jour) | Support immédiat — testé en séance |
| Support 2 | $35.00 (psychologique) | Ancien support de consolidation (fin mai) |
| Support 3 | $33.00–$34.00 | Zone de gap fill du rally de mai |
| Résistance 1 | $38.63 (MM 50j) | Ancien support devenu résistance |
| Résistance 2 | $40.79 (High du jour) | Résistance intraday |
| Résistance 3 | $41.33 (Prior close) | Gap fill objectif |

**Timing verdict :** **Défavorable** — La cassure de la MM50 sur volume faible est un signal technique négatif. L'absence de rebond intraday significatif (close $36.10 vs low $35.55 = +1.5% seulement) suggère un manque de conviction acheteuse. Le RSI à 45.6 laisse de la marge avant la survente, ce qui n'exclut pas une poursuite de la baisse.

---

## Mise à jour fondamentale — Multiples compressés, consensus inchangé

Données croisées Yahoo / FMP (annual FY 2025) — **compressions mécaniques dues à la chute du cours** :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $5.93B | -$1.19B (-16.7%) vs 03/06 |
| Market Cap (FMP) | $3.40B | Stable — divergence Yahoo/FMP persistante |
| Forward P/E | **−27.72** | Moins négatif vs −36.99 (mécanique, pas d'amélioration fondamentale) |
| EV/Revenue (Yahoo) | 28.591x | -18.0% vs 34.892x — compression pure |
| EV/Revenue (FMP) | 18.23x | Stable |
| P/B (Yahoo) | 5.230 | -16.8% vs 6.283 — compression pure |
| P/B (FMP) | 2.855 | Stable |
| Gross Margin (FMP) | 15.56% | Faible, stable |
| Operating Margin (FMP) | −154.25% | Fortement négatif, stable |
| Net Margin (FMP) | −186.63% | Fortement négatif, stable |
| Debt/Equity (FMP) | 0.259 | Levier modéré, stable |
| Current Ratio (FMP) | 4.51 | Liquidité solide, stable |
| Short Interest | 9.78% | Stable — pression vendeuse persistante |
| FMP Consensus PT | **$43.25 (12 analysts)** | **Inchangé** — désormais +19.8% au-dessus du spot |

**Filtre Qualité** : **2/6** (Hors périmètre) — **strictement inchangé**. L'événement prix ne modifie aucun des 6 critères qualité.

| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans >= 20% | ❌ | Pas de données >20% (FY 2025 Revenue/Share $1.05) |
| Profit CAGR 5 ans >= 20% | ❌ | Marges négatives |
| Assets/Liabilities > 1.0 | ✅ | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | ❌ | FCF yield négatif (−7.0%) |
| Avantage compétitif (moat) | ❌ | Aucun moat structurel identifié |
| Industrie forte croissance (TAM ×5) | ❌ | Aerospace & Defense en croissance, mais pas ×5 pour ce profil |
| **Score Qualité total** | **2/6** | 🔴 Hors périmètre |

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10. L'Agent Recommandation applique **5.5/10** (léger relèvement mécanique du fait de la compression multiple, mais reste plafonné).

**Note sur le consensus** : Le consensus inchangé à $43.25 avec 12 analysts offre désormais un upside de +19.8%. Cependant, le consensus n'a pas été révisé à la hausse malgré la chute — ce qui suggère que les analystes maintiennent leurs estimations sans paniquer, mais n'encouragent pas non plus l'achat à ce niveau. Le multiple de 12 analystes reste faible.

---

## Mise à jour sentiment / options / news — Aucun catalyst, max pain anomalie persistante

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $43.25 (12 analysts) | FMP Stable API | PT **+19.8% au-dessus du spot** — inchangé, upside mécanique mais pas de révision haussière. |
| Max Pain | $20.00 | Yahoo Finance 10:00 UTC | **⚠️ ANOMALIE DATA PERSISTANTE** — valeur aberrante pour un spot à $36.10. [DONNÉES PARTIELLES] |
| Put/Call Ratio | null | Yahoo Finance 10:00 UTC | **Données manquantes** — dernière valeur valide 0.68 (03/06). |
| Call OI % | null | Yahoo Finance 10:00 UTC | **Données manquantes** — dernière valeur valide 59.5% (03/06). |
| Short Interest | 9.78% | Yahoo Finance | Stable — pression vendeuse persistante, pas de setup squeeze. |
| Social Sentiment | 0 mention | `data/social_sentiment_2026-06-08.json` | Pas d'activité retail (alerte EXTREME_BEARISH ignorée — artefact). |
| Event-Driven | Aucun | `data/events_2026-06-08.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (57 jours) | `data/upcoming_events_2026-06-08.json` | Est EPS −$0.61 à −$0.45 (vs −$0.47 à −$0.45 précédemment), Rev $0.1B. |
| News FLY | Aucune | Pas de fichier news | **Aucune news spécifique** — le mouvement reste non expliqué par un catalyst. |

**Score Catalyseur** : **6.0/10** (données agents). La hausse du score Catalyseur (+1.0 pt) est paradoxale — elle reflète probablement la détection d'un "événement" (gap) par l'algorithme, mais en l'absence de news fondamentale, ce n'est pas un catalyseur constructif. L'absence d'événement corporate positif et le silence médiatique suggèrent que le gap est spéculatif/dérivé (liquidation, stop-loss en cascade, ou corrélation sectorielle).

---

## Scoring global — Dégradation : SURVEILLER (45.0)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 6.0/10 | 35% | 2.10 |
| Valorisation | 5.5/10 | 40% | 2.20 |
| Momentum | 4.0/10 | 25% | 1.00 |
| **Score Opportunité** | **5.3/10** | | |
| **Score Global** | **53.0** | | |
| **Score Global Ajusté** | **45.0** | | |

**Action** : **SURVEILLER**
**Direction** : Neutre
**Timing** : Défavorable
**Horizon** : —

**Note sur le scoring :** L'Agent Recommandation dégrade FLY en **SURVEILLER (45.0)**. Le Score Opportunité (5.3/10) franchit le seuil 5.0 mais le Score Global Ajusté tombe dans la fourchette 35–49 (SURVEILLER). Le principal driver de la dégradation est le **Momentum qui chute de 7.0 à 4.0/10**, entraînant le passage du Timing de Favorable à Défavorable.

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant depuis le 2026-05-17) — pas d'ajustement.
- **Agent Geo** : FLY non flaggé (geo_risk absent du rapport 2026-05-17) — pas de malus.
- **Agent Sector Rotation** : XLI sous-performant SPY (RS 20j −0.71%, momentum_score 2.05) — headwind sectoriel persistant (−0.5 pt).
- **Agent Social** : 0 mention — neutre (alerte pipeline EXTREME_BEARISH ignorée car artefact).
- **Agent FX** : Exposition 25%, fx_impact_score 0.0 — pas d'ajustement.
- **Agent Event-Driven** : 0 événement — neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible — pas d'ajustement.

---

## Révision des niveaux SL / TP — Ajustés à la baisse

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $36.10 | Close 07/06 (snapshot 10h UTC 08/06) | −12.65% vs prior close |
| Stop-loss | $23.84 | Agent Recommandation (2×ATR) | Support technique majeur — sous MM50 de $14.8% |
| Take-profit | $54.49 | Agent Recommandation (3×ATR) | Ancienne zone de résistance $40–$46 |
| Ratio R/R | 1.5:1 | Agent Recommandation | Standard agent — limité pour un profil sans profit |

Les niveaux sont issus de l'Agent Recommandation. Le SL $23.84 correspond à une zone sous le support structurel $35.55 et sous la MM50 ($38.63). Le TP $54.49 reflète un rebond partiel vers la zone $40–$46. Le ratio reste limité pour un profil sans rentabilité.

**Nouveau risque technique :** En dessous de $35.55, le prochain support structuré est vers $33.00–$34.00 (zone de gap fill du rally de mai). Une cassure de cette zone ouvrirait le chemin vers les $30.00.

---

## Conclusion — Thèse défavorable renforcée, cassure MM50 sans catalyst — SURVEILLER (45.0)

**Verdict : Thèse défavorable MODIFIÉE EN INTENSITÉ NÉGATIVE — passage ATTENDRE → SURVEILLER (45.0).**

Le snapshot 10h UTC du 08/06 confirme une **dégradation technique majeure** : gap -12.65%, cassure de la MM50, passage du Momentum en territoire baissier (4.0/10). L'Agent Recommandation dégrade la thèse à **SURVEILLER (45.0)**.

**Ce qui renforce la thèse défavorable :**
- **Cassure MM50** : passage de +14.8% à -6.5% sous la MM50 — signal technique de retournement à moyen terme.
- **Momentum baissier** : chute de 7.0/10 à 4.0/10, Timing passé de Favorable à Défavorable.
- **Aucun catalyst identifié** : aucune news, aucun événement corporate. Le gap est non expliqué fondamentalement.
- **Volume faible** : 0.69× moy. 20j sur un gap de -12.65% — pas de capitulation, mais pas de défense non plus.
- **Filtre Qualité 2/6, Forward P/E −27.72, EV/Revenue 28.6x** : fondamentaux inchangés et défavorables.
- **Headwind sectoriel XLI** : sous-performant SPY (RS 20j −0.71%, momentum_score 2.05).
- **Short Interest 9.78%** : stable, pression vendeuse persistante.
- **Anomalie data options** : max pain $20.00 persistant dans latest.json — [DONNÉES PARTIELLES].

**Ce qui modifie la thèse (marginalement moins négatif) :**
- **Consensus inchangé à $43.25** : upside mécanique de +19.8% si le consensus se réalise.
- **RSI 45.6** : pas encore en survente, mais sorti du surachat — normalisation partielle.
- **Support $35.55 testé et tenu en clôture** ($36.10) — léger rebond de +1.5% depuis le low.
- **Multiples compressés** : valorisation mécaniquement moins étirée (P/B 5.23, EV/Revenue 28.6x).

**Catalyseurs forward** :
1. **Earnings Q2 2026** (2026-08-04, 57 jours) : Est EPS −$0.61 à −$0.45 (borne basse dégradée vs −$0.47 précédemment), Rev $0.1B.
2. **Reconstitution des données options** : si Yahoo restaure max pain / put-call / call OI, surveillance du niveau de pin risk.

**Risques** :
1. Rentabilité non démontrée et non attendue à court terme.
2. Multiple incompatible avec un profil quality compounding.
3. **Cassure MM50** — tendance MT retournée à la baisse.
4. Short Interest 9.78% : pression vendeuse persistante.
5. Divergence Yahoo/FMP sur Market Cap ($5.93B vs $3.40B) et P/B (5.23 vs 2.86) persistante — [DONNÉES PARTIELLES].
6. Headwind sectoriel XLI persistant.
7. Forward P/E −27.72 : valorisation reste incompatible avec un profil sans profit.
8. **Anomalie data options** : max pain $20.00 persistant dans latest.json.
9. **Absence de support technique** sous $35.55 — risque de retour vers $33.00–$34.00.

**Prochaine étape :**
- **Ne pas prendre de position** — SURVEILLER (45.0).
- **Surveiller le comportement autour de $35.55** : si cassure en clôture sur volume > 1.0× moy. 20j → risque d'accélération vers $33.00–$34.00.
- **Si rebond au-dessus de $38.63** (MM50) sur volume > 1.0× moy. 20j → possible réintégration technique, mais nécessite confirmation.
- **Si un catalyst fondamental émerge** → réévaluer Score Catalyseur et Filtre Qualité. Sans cela, le mouvement reste spéculatif.

---

*Snapshot 10:00 UTC 08/06 — Cours $36.10 (−12.65% vs prior close, −51.1% vs 52W high), RSI 45.6 neutre-basse, volume 6.64M (0.69× moy. 20j). Consensus inchangé $43.25 (12 analysts). Anomalie max pain $20.00 persistante. Aucun catalyst. Fondamentaux inchangés et défavorables. Agent Recommandation : SURVEILLER (45.0). Thèse défavorable renforcée, cassure MM50 sans catalyst.*
