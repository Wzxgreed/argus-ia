# FLY — Mise a Jour (2026-06-15)

> **Type :** `_update.md` — Snapshot 10h UTC, gap baissier -19.05%, donnees techniques restaurees (ATR, MM50), these SURVEILLER (45.0) confirmee avec intensite negative renforcee
> **Reference precedente :** [FLY_2026-06-10_update_13h.md](FLY_2026-06-10_update_13h.md) (snapshot 13h UTC 10/06)
> **Donnees source :** `data/latest.json` (timestamp 2026-06-15T10:00:09.987422+00:00), `data/recommandations_2026-06-15.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-15.json`, `data/social_sentiment_2026-06-15.json`, `data/fx_exposure_2026-06-15.json`, `data/upcoming_events_2026-06-15.json`, `data/events_2026-06-15.json`
> **Validation data :** FLY status `ok` dans `data/validation_report.txt`. Aucun warning.

---

## Resume — Gap baissier -19.05%, RSI en survente, donnees techniques restaurees, SURVEILLER (45.0) confirme avec intensite negative renforcee

Le snapshot du 2026-06-15 enregistre un **gap baissier majeur de -19.05%** : le close tombe a **$31.87** (vs $36.18 precedent, previous_close $39.37), effacant le rebond du 10/06 et invalidant le support $35.00–$36.00. Le **RSI 14j franchit la zone neutre pour entrer en survente a 32.85** (vs 42.81). L'**ATR 14j et la MM50 sont enfin restaurees** dans `latest.json` (6.09 et 39.47 respectivement), confirmant que le cours evolue desormais **-19.3% sous la MM50** et que la volatilite realisee sur 14j est de $6.09.

Le volume explose a **14.54M (1.51x moy. 20j)**, soit +130% vs le snapshot precedent, confirmant la participation vendeuse active lors du gap.

L'**Agent Recommandation maintient SURVEILLER** avec un **Score Global Ajuste de 45.0** (vs 46.8), malgre une composition modifiee :
- Score Catalyseur **6.5/10** (+1.5 pt) — consensus revise a la hausse ($43.77, 13eme analyste)
- Score Valorisation **6.0/10** (+1.5 pt) — multiple legerement moins defavorable
- Score Momentum **2.5/10** (-2.0 pt) — gap baissier et cassure technique amplifiee

Le timing bascule **Defavorable** (vs Neutre).

**Comparatif 10/06 -> 15/06 :**

| Metrique | 2026-06-10 13h UTC | 2026-06-15 10h UTC | Variation |
|----------|--------------------|--------------------|-----------|
| Cours close | $36.18 | **$31.87** | **-11.9%** (-19.05% vs prior close $39.37) |
| RSI 14j | 42.81 | **32.85** | **-9.96 pts -> survente** |
| MM 50j | null | **39.47** | [DONNEES RESTAUREES] — cours -19.3% sous MM50 |
| ATR 14j | null | **6.09** | [DONNEES RESTAUREES] |
| Volume session | 6.31M | **14.54M** | **+130.3%** |
| Volume vs moy. 20j | 0.69x | **1.51x** | Participation vendeuse active |
| Short Interest | 12.12% | **12.12%** | Inchange |
| Score Catalyseur | 5.0/10 | **6.5/10** | +1.5 pt |
| Score Valorisation | 4.5/10 | **6.0/10** | +1.5 pt |
| Score Momentum | 4.5/10 | **2.5/10** | **-2.0 pt** |
| Score Opportunite | 4.7/10 | **5.3/10** | +0.6 pt |
| Score Global Ajuste | 46.8 | **45.0** | -1.8 pt |
| Action | SURVEILLER | **SURVEILLER** | Confirmee |
| Timing | Neutre | **Defavorable** | **Degrade** |
| Max Pain | $40.00 | **$20.00** | **ANOMALIE DATA** |
| Put/Call Ratio | 0.93 | **null** | **ANOMALIE DATA** |
| Call OI % | 51.8% | **null** | **ANOMALIE DATA** |
| Consensus PT | $43.25 (12 analysts) | **$43.77 (13 analysts)** | **+$0.52, +1 analyste** |

**Verdict :** Le gap baissier -19.05% du 15/06 est le mouvement le plus significatif depuis le debut du suivi. Il confirme la rupture de la consolidation $35–$40 amorcee le 08/06 et positionne le cours en **territoire de survente technique** (RSI 32.85). La restauration des donnees MT (ATR, MM50) permet enfin de calibrer la structure technique : le cours est en forte detresse vs la MM50 (-19.3%) et la volatilite est elevee (ATR $6.09). L'absence de catalyst fondamental (events = 0, news = 0) et le Filtre Qualite 2/6 inchange maintiennent la prudence. These **SURVEILLER (45.0)** confirmee avec intensite negative **renforcee**.

---

## Mise a jour technique — Gap baissier majeur, survente, MM50/ATR restaures

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours (close) | $31.87 | Gap -19.05% vs prior close $39.37 |
| Cours (previous_close) | $39.37 | Reference du gap |
| RSI 14j | **32.85** | **Survente** — franchissement sous 35 |
| MM 50j | **39.47** | **Cours -19.3% sous MM50** — tendance baissiere confirmee |
| ATR 14j | **6.09** | Volatilite elevee, desormais calculable |
| Volume session | 14,538,100 | **1.51x moy. 20j** — participation active |
| Volume vs moy. 20j | 1.51x | Vendeurs actifs |
| Support 1 | $31.40 (low du jour) | Teste aujourd'hui, tenue incertaine |
| Support 2 | $30.00 (psychologique) | Support structurel majeur |
| Support 3 | $28.00–$28.50 | Gap fill du rally de mai si $30 casse |
| Resistance 1 | $35.00–$36.00 (ancien support) | Resistance technique cle |
| Resistance 2 | $39.47 (MM50) | Resistance majeure |
| Resistance 3 | $40.00 (max pain historique) | Resistance options |
| 52W Range | $16.00 – $73.80 | Midpoint $44.90 — cours -28.9% sous midpoint |

**Options — Anomalie DATA :**

| Metrique | Valeur 10/06 | Valeur 15/06 | Statut |
|----------|-------------|-------------|--------|
| Max Pain | $40.00 | **$20.00** | ANOMALIE — valeur aberrante |
| Put/Call Ratio | 0.93 | **null** | Anomalie data |
| Call OI % | 51.8% | **null** | Anomalie data |
| Expiration | 2026-06-12 | **2026-06-18** | Reportee |

Les donnees options sont a nouveau corrompues dans `latest.json` (max pain $20.00 = irrealiste vs spot $31.87). L'expiration a ete reportee au 2026-06-18.

**Timing verdict :** **Defavorable** — Le gap baissier -19.05% sur volume eleve confirme la rupture technique. Le RSI en survente (32.85) pourrait justifier un rebond technique, mais la tendance sous MM50 est clairement baissiere. Aucun signal de retournement.

---

## Mise a jour fondamentale — Legere amelioration mecanique, Filtre Qualite inchange

Donnees croisees Yahoo / FMP (annual FY 2025) :

| Metrique | Valeur 10/06 | Valeur 15/06 | Variation | Commentaire |
|----------|-------------|-------------|-----------|-------------|
| Market Cap (Yahoo) | $5.49B | **$5.23B** | -4.7% | Revision cours |
| Forward P/E (Yahoo) | -25.68 | **-24.75** | +0.93 pt | Moins negatif |
| EV/Revenue (Yahoo) | 26.29x | **24.925x** | -1.365x | Legereement moins defavorable |
| P/B (Yahoo) | 4.845 | **4.617** | -0.228 | Stable |
| Gross Margin (FMP) | 15.56% | **15.56%** | Inchange | Faible |
| Operating Margin (FMP) | -154.25% | **-154.25%** | Inchange | Fortement negatif |
| Net Margin (FMP) | -186.63% | **-186.63%** | Inchange | Fortement negatif |
| Debt/Equity (FMP) | 0.259 | **0.259** | Inchange | Levier modere |
| Current Ratio (FMP) | 4.51 | **4.51** | Inchange | Liquidite solide |
| Short Interest | 12.12% | **12.12%** | Inchange | Pression vendeuse accrue |
| FMP Consensus PT | $43.25 (12 analysts) | **$43.77 (13 analysts)** | +$0.52, +1 analyste | Upside +37.3% vs $31.87 |

**Filtre Qualite** : **2/6** (Hors perimetre) — **strictement inchange**. L'evenement prix ne modifie aucun critere fondamental.

| Critere | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans >= 20% | | Pas de donnees >20% |
| Profit CAGR 5 ans >= 20% | | Marges negatives |
| Assets/Liabilities > 1.0 | | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | | FCF yield negatif |
| Avantage competitif (moat) | | Aucun moat structurel |
| Industrie forte croissance (TAM x5) | | Aerospace & Defense en croissance, mais pas x5 |
| **Score Qualite total** | **2/6** | Hors perimetre |

**Note :** L'amelioration des scores Catalyseur (+1.5) et Valorisation (+1.5) par l'agent est **mecanique** (ajustement de multiples suite a la baisse du cours) et ne reflete pas une amelioration fondamentale reelle. Le Filtre Qualite 2/6 et les marges negatives restent des barrieres structurelles.

---

## Mise a jour sentiment / options / news — Consensus revise a la hausse, silence mediatique persistant, anomalie options

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | **$43.77 (13 analysts)** | FMP Stable API | PT **+37.3% au-dessus du spot** — revision a la hausse malgre la chute. |
| Max Pain | **$20.00** | `latest.json` 10:00 UTC | **ANOMALIE DATA** — valeur aberrante, non operationnelle |
| Put/Call Ratio | **null** | `latest.json` 10:00 UTC | Anomalie data |
| Call OI % | **null** | `latest.json` 10:00 UTC | Anomalie data |
| Short Interest | **12.12%** | Yahoo Finance | **Eleve** — pression vendeuse accrue, pas de setup squeeze |
| Social Sentiment | 0 mention | `data/social_sentiment_2026-06-15.json` | Pas d'activite retail |
| Event-Driven | Aucun | `data/events_2026-06-15.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (50 jours) | `data/upcoming_events_2026-06-15.json` | Est EPS -$0.61 a -$0.45, Rev $0.1B |
| News FLY | Aucune | Pas de fichier news | **Silence mediatique persistant** |
| Expiration options | **2026-06-18 (J+3)** | Yahoo Finance | Max pain aberrant $20.00 |

**Score Catalyseur** : **6.5/10** (+1.5 pt vs precedent). La revision du consensus a la hausse ($43.77, +1 analyste) est le seul element positif. Cependant, ce catalyseur est **theorique** : le consensus n'a pas ete revu a la baisse malgre le gap -19.05%, ce qui pourrait indiquer un decalage de publication ou une resistance des analystes a couper leurs estimations. Aucun catalyst fondamental nouveau.

---

## Scoring global — SURVEILLER (45.0), composition modifiee, timing Defavorable

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 6.5/10 | 35% | 2.275 |
| Valorisation | 6.0/10 | 40% | 2.400 |
| Momentum | 2.5/10 | 25% | 0.625 |
| **Score Opportunite** | **5.3/10** | | |
| **Score Global** | **53.0** | | |
| **Score Global Ajuste** | **45.0** | | |

**Action :** **SURVEILLER**
**Direction :** Neutre
**Timing :** **Defavorable**
**Horizon :** —

**Ajustements agents complementaires :**
- **Agent Quant** : Signaux non significatifs (p-value null, n=0, insuffisant) — pas d'ajustement.
- **Agent Geo** : FLY non flagge — pas de malus.
- **Agent Sector Rotation** : Industrials (XLI) momentum_score 3.89, hors top3/bottom3 — pas d'ajustement.
- **Agent Social** : 0 mention — neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0, flag — pas d'ajustement.
- **Agent Event-Driven** : 0 evenement — neutre.
- **Agent Accounting** : Fichier indisponible — pas d'ajustement.

---

## Revision des niveaux SL / TP — Donnees restaurees, niveaux calculables

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $31.87 | Close 15/06 | Gap -19.05% vs prior close |
| Stop-loss | **$19.69** | Cours - 2xATR ($12.18) | Niveau technique inferieur au low 52W ($16.00) |
| Take-profit | **$50.14** | Cours + 3xATR ($18.27) | Reconciliation avec zone resistance historique |
| Ratio R/R | **1.5** | Gain / Perte | Standard agent |

**Risque technique :** Le SL $19.69 est proche du low 52W ($16.00). Une cassure de $30.00 en cloture sur volume > 1.0x moy. 20j ouvrirait le chemin vers $28.00–$26.00, rendant le SL obsolete. Surveiller le comportement autour de $31.40 (low du jour) et $30.00.

---

## Conclusion — These confirmee avec intensite negative renforcee : gap baissier majeur, survente technique, fondamentaux inchanges

**Verdict : These confirmee avec intensite negative renforcee — SURVEILLER (45.0), timing Defavorable.**

Le gap baissier -19.05% du 15/06 est un evenement technique majeur qui confirme la rupture de la consolidation $35–$40. La restauration des donnees MT (ATR $6.09, MM50 $39.47) permet enfin de qualifier la structure : le cours est en **forte detresse technique** (-19.3% sous MM50, RSI 32.85 en survente) et la volatilite est elevee.

**Ce qui maintient la prudence :**
- **Gap baissier -19.05% sans catalyst** : aucune news, aucun evenement corporate, aucun fondamental modifie. Le mouvement est purement technique / speculatif.
- **Filtre Qualite 2/6** : profil fondamental inchange et defavorable.
- **Forward P/E -24.75, EV/Revenue 24.9x** : valorisation incompatible avec un profil sans profit.
- **Short Interest 12.12%** : pression vendeuse accrue.
- **Timing Defavorable** : tendance baissiere confirmee sous MM50.

**Ce qui est legerement positif / modifie :**
- **Consensus revise a la hausse $43.77** (+$0.52, 13eme analyste) — divergence analystes/spot s'elargit a +37.3%.
- **Forward P/E et EV/Revenue mecaniquement moins defavorables** suite a la baisse du cours.
- **RSI 32.85** : survente technique qui pourrait justifier un rebond technique a court terme.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 50 jours) : Est EPS -$0.61 a -$0.45, Rev $0.1B.
2. **Expiration options** (2026-06-18, J+3) : surveillance du comportement si donnees restaurees.
3. **Rebond technique** : RSI 32.85 pourrait attirer des acheteurs techniques si $31.40 tient.

**Risques :**
1. **Gap baissier sans catalyst** : risque de continuation si les vendeurs restent agressifs.
2. **Cours sous MM50 -19.3%** : tendance baissiere structuree.
3. **Short Interest 12.12%** : pression vendeuse continue.
4. **Anomalie options** : impossibilite de lire le sentiment options.
5. **Support $30.00** : si casse, retour vers $28.00–$26.00.
6. **Fondamentaux inchanges** : pas de justification fondamentale a un retournement.

**Prochaine etape :**
- **Ne pas prendre de position** — SURVEILLER (45.0), timing Defavorable.
- **Surveiller le comportement autour de $31.40** (low du jour) et **$30.00** (support psychologique).
- **Attendre un rebond technique** sur RSI 32.85 pourrait offrir une entree speculative, mais la tendance sous MM50 est defavorable.
- **Si un catalyst fondamental emerge** -> reevaluer Score Catalyseur. Sans cela, le risque de continuation baissiere prime.

---

*Snapshot 10:00 UTC 15/06 — Close $31.87 (gap -19.05% vs prior close $39.37), RSI 32.85 (survente), ATR 6.09, MM50 39.47, volume 14.54M (1.51x moy. 20j), Short Interest 12.12%. Consensus $43.77 (13 analysts). Options : anomalie data (max pain $20.00 aberrant). Fondamentaux inchanges (Filtre Qualite 2/6). Agent Recommandation : SURVEILLER (45.0), timing Defavorable. These confirmee avec intensite negative renforcee.*
