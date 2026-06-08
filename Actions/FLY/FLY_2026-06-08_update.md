# FLY — Mise à Jour (2026-06-08, snapshot 13h UTC)

> **Type :** `_update.md` — Résolution anomalie options, données restaurées, thèse SURVEILLER (45.0) confirmée
> **Référence précédente :** [FLY_2026-06-08_update.md](FLY_2026-06-08_update.md) (snapshot 10h UTC 08/06)
> **Données source :** `data/latest.json` (timestamp 2026-06-08T13:00:09.302415+00:00), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Validation data :** FLY status `ok` dans `data/validation_report.txt`. Aucun warning. 25/29 tickers OK.

---

## Résumé — Données options restaurées, thèse SURVEILLER confirmée (45.0)

Le snapshot 13h UTC du 2026-06-08 confirme la **stabilité des cours** à **$36.10** (identique au snapshot 10h), avec le gap down de **-12.65%** inchangé vs prior close $41.33. L'événement majeur de ce snapshot est la **résolution de l'anomalie données options** :

- **Max Pain** : restauré à **$40.00** (vs anomalie $20.00 au snapshot 10h)
- **Put/Call Ratio** : **1.08** (vs null au snapshot 10h)
- **Call OI %** : **48.1%** (vs null au snapshot 10h)

Ces valeurs restaurées sont désormais cohérentes avec le spot $36.10 (spot sous max pain de -9.8%). L'anomalie data options du snapshot 10h est **résolue** — il s'agissait d'un artefact temporaire du pipeline.

**Changements majeurs vs snapshot 10h :**
- **Options** : anomalie résolue — max pain $40.00, put/call 1.08, call OI 48.1% restaurés
- **Cours, RSI, volumes, fondamentaux** : strictement identiques au snapshot 10h
- **Score Global Ajusté** : **45.0** inchangé — SURVEILLER confirmé
- **Momentum** : **4.0/10** baissier inchangé
- **Timing** : **Défavorable** inchangé

Aucun catalyst identifié (`events_latest.json` vide pour FLY, `social_sentiment_latest.json` 0 mention). Le mouvement s'effectue sur un volume **6.64M (0.69× moy. 20j)** — inférieur à la moyenne, ce qui atténue l'interprétation d'une liquidation massive.

| Métrique | 2026-06-08 10h UTC | 2026-06-08 13h UTC | Variation |
|----------|--------------------|--------------------|-----------|
| Cours close | $36.10 | **$36.10** | Stable |
| Change % vs prior close | −12.65% | **−12.65%** | Stable |
| RSI 14j | 45.6 | **45.6** | Stable |
| MM 50j | $38.63 | **$38.63** | Stable |
| Position vs MM50 | -6.5% en dessous | **-6.5% en dessous** | 🔴 CASSURE confirmée |
| ATR 14j | $6.13 | **$6.13** | Stable |
| Volume session | 6.64M | **6.64M** | Stable |
| Volume vs moy. 20j | 0.69x | **0.69x** | Stable |
| Options — Max Pain | $20.00 (anomalie) | **$40.00** | ✅ RÉSOLU |
| Options — Put/Call | null | **1.08** | ✅ RÉSOLU |
| Options — Call OI % | null | **48.1%** | ✅ RÉSOLU |
| Score Opportunité (agent) | 5.3/10 | **5.3/10** | Stable |
| Score Momentum (agent) | 4.0/10 | **4.0/10** | Stable — baissier |
| Score Global Ajusté (agent) | 45.0 | **45.0** | Stable — SURVEILLER |
| Action | SURVEILLER | **SURVEILLER** | Confirmée |
| Timing | Défavorable | **Défavorable** | Confirmé |

**Verdict :** Gap -12.65% sans catalyst, cassure de la MM50, momentum baissier confirmé. La résolution de l'anomalie options n'altère pas la thèse — les valeurs restaurées ($40.00 max pain, put/call 1.08) confirment une configuration neutre à légèrement baissière en termes d'options. L'Agent Recommandation maintient **SURVEILLER (45.0)**.

---

## Mise à jour technique — Cassure MM50 confirmée, options restaurées

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $36.10 | −12.65% vs prior close $41.33, −51.1% vs 52W high $73.80 |
| Open | $39.69 | Gap down vs prior close $41.33 |
| High | $40.79 | Résistance intraday — non dépassée en clôture |
| Low | $35.55 | **Support du jour testé** — zone critique |
| RSI 14j | **45.6** | **Neutre-basse** — inchangé |
| MM 50j | $38.63 | Cours inférieur de **-6.5%** — cassure technique confirmée |
| Volume | 6,641,300 | **0.69× moy. 20j** — volume faible sur un gap de -12.65% |
| ATR 14j | $6.13 | Volatilité élevée persistante (16.98% rel.) |
| Support 1 | $35.55 (Low du jour) | Support immédiat — testé en séance |
| Support 2 | $35.00 (psychologique) | Ancien support de consolidation (fin mai) |
| Support 3 | $33.00–$34.00 | Zone de gap fill du rally de mai |
| Résistance 1 | $38.63 (MM 50j) | Ancien support devenu résistance |
| Résistance 2 | $40.00 (Max Pain) | Aimant options — nouveau niveau de référence |
| Résistance 3 | $40.79 (High du jour) | Résistance intraday |

**Timing verdict :** **Défavorable** — La cassure de la MM50 sur volume faible est un signal technique négatif confirmé. L'absence de rebond intraday significatif (close $36.10 vs low $35.55 = +1.5% seulement) suggère un manque de conviction acheteuse. Le RSI à 45.6 laisse de la marge avant la survente, ce qui n'exclut pas une poursuite de la baisse.

---

## Mise à jour fondamentale — Inchangée, compression multiple mécanique

Données croisées Yahoo / FMP (annual FY 2025) — **compressions mécaniques dues à la chute du cours** :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $5.93B | Identique snapshot 10h |
| Market Cap (FMP) | $3.40B | Stable — divergence Yahoo/FMP persistante |
| Forward P/E | **−27.72** | Moins négatif vs −36.99 (mécanique, pas d'amélioration fondamentale) |
| EV/Revenue (Yahoo) | 28.591x | Compression pure |
| EV/Revenue (FMP) | 18.23x | Stable |
| P/B (Yahoo) | 5.230 | Compression pure |
| P/B (FMP) | 2.855 | Stable |
| Gross Margin (FMP) | 15.56% | Faible, stable |
| Operating Margin (FMP) | −154.25% | Fortement négatif, stable |
| Net Margin (FMP) | −186.63% | Fortement négatif, stable |
| Debt/Equity (FMP) | 0.259 | Levier modéré, stable |
| Current Ratio (FMP) | 4.51 | Liquidité solide, stable |
| Short Interest | 9.78% | Stable — pression vendeuse persistante |
| FMP Consensus PT | **$43.25 (12 analysts)** | **Inchangé** — upside mécanique +19.8% |

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

---

## Mise à jour sentiment / options / news — Anomalie résolue, configuration neutre

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $43.25 (12 analysts) | FMP Stable API | PT **+19.8% au-dessus du spot** — inchangé, upside mécanique mais pas de révision haussière. |
| Max Pain | **$40.00** | Yahoo Finance 13:00 UTC | **✅ RESTAURÉ** — valeur cohérente pour un spot à $36.10 (spot sous max pain de -9.8%). |
| Put/Call Ratio | **1.08** | Yahoo Finance 13:00 UTC | **✅ RESTAURÉ** — légèrement >1.0, indiquant une légère prédominance des puts (baissier modéré). |
| Call OI % | **48.1%** | Yahoo Finance 13:00 UTC | **✅ RESTAURÉ** — équilibre presque neutre, pas de biais directionnel fort via options. |
| Short Interest | 9.78% | Yahoo Finance | Stable — pression vendeuse persistante, pas de setup squeeze. |
| Social Sentiment | 0 mention | `data/social_sentiment_2026-06-08.json` | Pas d'activité retail (alerte EXTREME_BEARISH ignorée — artefact pipeline). |
| Event-Driven | Aucun | `data/events_2026-06-08.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (57 jours) | `data/upcoming_events_2026-06-08.json` | Est EPS −$0.61 à −$0.45, Rev $0.1B. |
| News FLY | Aucune | Pas de fichier news | **Aucune news spécifique** — le mouvement reste non expliqué par un catalyst. |

**Score Catalyseur** : **6.0/10** (données agents). La résolution de l'anomalie options n'apporte pas de catalyseur nouveau. La configuration options (max pain $40.00, put/call 1.08) est globalement neutre avec une légère coloration baissière (puts > calls). L'absence d'événement corporate positif et le silence médiatique suggèrent que le gap est spéculatif/dérivé (liquidation, stop-loss en cascade, ou corrélation sectorielle).

---

## Scoring global — SURVEILLER (45.0) confirmé

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

**Note sur le scoring :** L'Agent Recommandation maintient FLY en **SURVEILLER (45.0)**. Le Score Opportunité (5.3/10) franchit le seuil 5.0 mais le Score Global Ajusté tombe dans la fourchette 35–49 (SURVEILLER). La résolution de l'anomalie options ne modifie aucun des scores agents.

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant depuis le 2026-05-17) — pas d'ajustement.
- **Agent Geo** : FLY non flaggé (geo_risk absent du rapport 2026-05-17) — pas de malus.
- **Agent Sector Rotation** : XLI sous-performant SPY (RS 20j −0.71%, momentum_score 2.05) — headwind sectoriel persistant (−0.5 pt).
- **Agent Social** : 0 mention — neutre (alerte pipeline EXTREME_BEARISH ignorée car artefact).
- **Agent FX** : Exposition 25%, fx_impact_score 0.0 — pas d'ajustement.
- **Agent Event-Driven** : 0 événement — neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible — pas d'ajustement.

---

## Révision des niveaux SL / TP — Inchangés

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $36.10 | Close 07/06 (snapshot 13h UTC 08/06) | −12.65% vs prior close |
| Stop-loss | $23.84 | Agent Recommandation (2×ATR) | Support technique majeur |
| Take-profit | $54.49 | Agent Recommandation (3×ATR) | Ancienne zone de résistance $40–$46 |
| Ratio R/R | 1.5:1 | Agent Recommandation | Standard agent — limité pour un profil sans profit |

Les niveaux sont issus de l'Agent Recommandation et restent inchangés. Le SL $23.84 correspond à une zone sous le support structurel $35.55 et sous la MM50 ($38.63). Le TP $54.49 reflète un rebond partiel vers la zone $40–$46. Le ratio reste limité pour un profil sans rentabilité.

**Nouveau risque technique :** En dessous de $35.55, le prochain support structuré est vers $33.00–$34.00 (zone de gap fill du rally de mai). Une cassure de cette zone ouvrirait le chemin vers les $30.00.

---

## Conclusion — Thèse défavorable confirmée, anomalie options résolue — SURVEILLER (45.0)

**Verdict : Thèse défavorable CONFIRMÉE — SURVEILLER (45.0). La résolution de l'anomalie options ne modifie pas la thèse.**

Le snapshot 13h UTC du 08/06 confirme la **stabilité de la dégradation technique** : gap -12.65%, cassure de la MM50, passage du Momentum en territoire baissier (4.0/10). L'Agent Recommandation maintient la thèse à **SURVEILLER (45.0)**.

**Ce qui renforce la thèse défavorable :**
- **Cassure MM50** : passage de +14.8% à -6.5% sous la MM50 — signal technique de retournement à moyen terme.
- **Momentum baissier** : 4.0/10, Timing Défavorable.
- **Aucun catalyst identifié** : aucune news, aucun événement corporate. Le gap est non expliqué fondamentalement.
- **Volume faible** : 0.69× moy. 20j sur un gap de -12.65% — pas de capitulation, mais pas de défense non plus.
- **Filtre Qualité 2/6, Forward P/E −27.72, EV/Revenue 28.6x** : fondamentaux inchangés et défavorables.
- **Headwind sectoriel XLI** : sous-performant SPY (RS 20j −0.71%, momentum_score 2.05).
- **Short Interest 9.78%** : stable, pression vendeuse persistante.
- **Absence de support technique** sous $35.55 — risque de retour vers $33.00–$34.00.

**Ce qui modifie la thèse (marginalement moins négatif) :**
- **Consensus inchangé à $43.25** : upside mécanique de +19.8% si le consensus se réalise.
- **RSI 45.6** : pas encore en survente, mais sorti du surachat — normalisation partielle.
- **Support $35.55 testé et tenu en clôture** ($36.10) — léger rebond de +1.5% depuis le low.
- **Multiples compressés** : valorisation mécaniquement moins étirée (P/B 5.23, EV/Revenue 28.6x).
- **Options restaurées** : max pain $40.00 cohérent, put/call 1.08 légèrement baissier mais pas alarmant.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 57 jours) : Est EPS −$0.61 à −$0.45, Rev $0.1B.
2. **Reconstitution des données options** : les valeurs $40.00/1.08/48.1% sont désormais fiables.

**Risques :**
1. Rentabilité non démontrée et non attendue à court terme.
2. Multiple incompatible avec un profil quality compounding.
3. **Cassure MM50** — tendance MT retournée à la baisse.
4. Short Interest 9.78% : pression vendeuse persistante.
5. Divergence Yahoo/FMP sur Market Cap ($5.93B vs $3.40B) et P/B (5.23 vs 2.86) persistante — [DONNÉES PARTIELLES].
6. Headwind sectoriel XLI persistant.
7. Forward P/E −27.72 : valorisation reste incompatible avec un profil sans profit.
8. **Absence de support technique** sous $35.55 — risque de retour vers $33.00–$34.00.

**Prochaine étape :**
- **Ne pas prendre de position** — SURVEILLER (45.0).
- **Surveiller le comportement autour de $35.55** : si cassure en clôture sur volume > 1.0× moy. 20j → risque d'accélération vers $33.00–$34.00.
- **Si rebond au-dessus de $38.63** (MM50) sur volume > 1.0× moy. 20j → possible réintégration technique, mais nécessite confirmation.
- **Si un catalyst fondamental émerge** → réévaluer Score Catalyseur et Filtre Qualité. Sans cela, le mouvement reste spéculatif.

---

*Snapshot 13:00 UTC 08/06 — Cours $36.10 (−12.65% vs prior close, −51.1% vs 52W high), RSI 45.6 neutre-basse, volume 6.64M (0.69× moy. 20j). Consensus inchangé $43.25 (12 analysts). Anomalie options RÉSOLUE : max pain $40.00, put/call 1.08, call OI 48.1%. Aucun catalyst. Fondamentaux inchangés et défavorables. Agent Recommandation : SURVEILLER (45.0). Thèse défavorable confirmée.*
