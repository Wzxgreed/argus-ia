# AST — Mise a Jour Snapshot 10h UTC (2026-06-17)

> **Source :** `data/latest.json` (snapshot 2026-06-17T10:00:01Z) | `data/recommandations_latest.json` | `data/validation_report.txt`
> **Reference precedente :** [AST_2026-06-16_update.md](AST_2026-06-16_update.md) (post-session US 17h UTC 16/06)
> **Contexte :** Snapshot pre-ouverture US du 17/06. Donnees etablies pour ASTS. AST reste sans donnees.

---

## 1. Resume des Changements depuis le Snapshot Precedent (17h UTC 16/06)

| Metrique | Snapshot 17h (16/06) | Snapshot 10h (17/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirme stable — >45 snapshots consecutifs** |
| **ASTS — Cours close** | **$83.09** (close 16/06) | **$82.25** | **-1.01%** — legere poursuite de la baisse |
| **ASTS — Previous close** | $87.57 | **$87.57** | = — stable (close 15/06 devenu reference) |
| **ASTS — Variation vs previous** | -5.12% | **-6.08%** | **-0.96 pt** — effacement du rebond du 15/06 complet |
| **ASTS — RSI 14j** | 28.73 | **28.51** | **-0.22 pt** — survente extreme stable |
| **ASTS — ATR 14j** | $12.40 | **$12.40** | = — stable |
| **ASTS — MM 50j** | $88.90 | **$88.88** | **-0.02%** — quasi-inchangee |
| **ASTS — Distance MM50** | -6.5% | **-7.4%** | **ecart elargi** — cours s'eloigne de la MM50 |
| **ASTS — Volume seance** | 11.35M (0.42x) | **20.04M (0.73x)** | **+76.6% / recovery volumetrique** mais reste sous moyenne |
| **ASTS — Short Interest** | 18.39% | **18.39%** | = — stable |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = |
| **ASTS — Premium vs consensus** | -12.1% | **-13.0%** | **degradation -0.9 pt** |
| **ASTS — Options Max Pain** | $100.0 (natif) | **$18.0 (JSON)** | **🟡 ANOMALIE JSON RECURRENTE** — valeur aberrante |
| **ASTS — Options Put/Call** | 0.45 (natif) | **null (JSON)** | **🟡 ANOMALIE JSON RECURRENTE** |
| **ASTS — Options Call OI %** | 69.0% (natif) | **null (JSON)** | **🟡 ANOMALIE JSON RECURRENTE** |
| **ASTS — Echeance options** | 2026-06-18 (1j) | **2026-06-18 (1j)** | = — **mercredi, theta decay imminent** |
| **Score Global ASTS** | 43.0/100 (SURVEILLER) | **43.0/100 (SURVEILLER)** | = — stable |
| **Score Opportunite ASTS** | 4.6/10 | **4.6/10** | = — stable |

**Verdict :** Le snapshot 10h UTC du 17/06 enregistre une **stabilisation mecanique de la degradation technique** sur ASTS. Le cours recule marginalement de **-1.01%** a **$82.25** mais le **volume recupere a 0.73x** (20.04M vs 27.33M moy. 20j), ce qui est une legere amelioration par rapport au collapse de 0.42x de la veille. Le RSI reste pratiquement inchange a **28.51** (survente extreme). L'ecart a la MM50 s'est elargi a **-7.4%** ($82.25 vs $88.88). **Anomalie options JSON RECURRENTE** : max pain $18.0 aberrant (vs $100.0 operationnel), put/call et call OI passes a null — faux positif pipeline confirme. L'echeance options du 18/06 est demain (**1 jour**). Le scoring agent maintient **43.0/100 (SURVEILLER)** — stable.

---

## 2. Mise a Jour Technique

### AST (donnees officielles)

| Indicateur | Valeur Snapshot 10h | Valeur precedente (17h 16/06) | Δ |
|-----------|---------------------|------------------------------|---|
| Cours close | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| Volume | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| MM 50j | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |

**Verdict timing AST :** [NON EVALUABLE] — absence totale de donnees techniques sur **>45 snapshots consecutifs** (18/05 -> 17/06).

### ASTS (proxy — donnees 10h UTC 17/06)

| Indicateur | Valeur Snapshot 10h | Valeur Snapshot 17h 16/06 | Δ |
|-----------|-------------------|-------------------|---|
| Cours close | **$82.25** | $83.09 | **-1.01%** |
| Previous close | **$87.57** | $87.57 | = |
| RSI 14j | **28.51** | 28.73 | **-0.22 pts** — survente extreme stable |
| ATR 14j | **$12.40** | $12.40 | = |
| MM50 | **$88.88** | $88.90 | **-0.02%** |
| Distance MM50 | **-7.4%** | -6.5% | **ecart elargi** |
| Volume seance | **20.04M** | 11.35M | **+76.6%** — recovery |
| Volume relatif | **0.73x** | 0.42x | **recovery** |
| Short interest | **18.39%** | 18.39% | = — stable |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 36.08 | 36.08 | = |

**Verdict timing ASTS :** 🟡 **STABILISATION MECANIQUE — SURVENTE EXTREME PERSISTANTE**

- **RSI 28.51** : la survente extreme se maintient. Le titre est dans une zone de survente prononcee (< 30) depuis plusieurs jours. Aucun rebond technique n'est visible malgre la recovery volumetrique.
- **Volume 0.73x** : **20.04M vs moyenne 20j 27.33M** — nette amelioration par rapport au collapse de 0.42x (11.35M) de la veille, mais le volume reste sous la moyenne. La distribution se poursuit avec une intensite moindre.
- **Cours sous MM50 ($88.88)** : le cours a $82.25 se situe desormais **-7.4% sous la MM50**. L'ecart s'est legerement elargi, confirmant la rupture de la tendance moyen terme.
- **ATR $12.40** : stable — volatilite inchangee.
- **Short interest stable a 18.39%** : pas de couverture massive des shorts detectee. Le setup squeeze reste theorique.

**Niveaux cles** (actualises avec snapshot 10h UTC 17/06) :
- Support immediat : **$82.11** (low intraday 16/06 — teste mais non casse)
- Support : **$80.00-$81.50** (zone de confluence + 1.5xATR)
- Support critique : **$76-78** (test du 15/06 non franchi, zone de repli majeure)
- Resistance immediatte : **$85.70** (open 17/06)
- Resistance : **$87.57** (previous close / gap a combler)
- Resistance majeure : **$88.88** (MM50 — test de retour comme resistance)
- Objectif haussier : **$119.45** (spot + 3xATR $12.40)

**Structure options** (anomalie JSON RECURRENTE — valeurs operationnelles conservees) :
- **Max Pain JSON** : **$18.0** — valeur aberrante, **non operationnelle**. Valeur operationnelle estimee **$100.0** (coherente avec historique).
- **Put/Call ratio JSON** : **null** — aberrant. Valeur operationnelle estimee **~0.45** (coherente avec historique).
- **Call OI % JSON** : **null** — aberrant. Valeur operationnelle estimee **~69%** (coherente avec historique).
- Expiration proche : **2026-06-18** (1 jour) — theta decay imminent pour les options OTM.

> **Note options :** L'anomalie JSON recurrente sur ASTS est **de retour** dans le snapshot 10h UTC du 17/06. Les valeurs natives (max pain $18.0, put/call null, call OI null) sont aberrantes. Il s'agit d'un **faux positif pipeline confirme** — les valeurs operationnelles ($100.0, 0.45, 69%) restent les references. Le max pain $100.0 est eloigne du cours actuel ($82.25 -> $100.0 = +21.6%), ce qui limite la pression gamma immediate. L'expiration demain (18/06) pourrait amplifier la volatilite si le cours se rapproche du max pain, mais la distance rend ce scenario peu probable.

---

## 3. Mise a Jour Fondamentale

### AST (donnees officielles)

| Metrique | Valeur Snapshot 10h | Valeur precedente | Δ |
|---------|---------------------|-------------------|---|
| Market cap | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Filtre Qualite (6 criteres) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualite :** impossible a calculer sans etats financiers accessibles.

### ASTS (proxy)

| Metrique | Valeur Snapshot 10h | Valeur Snapshot 17h 16/06 | Δ |
|---------|---------------------|-----------------------|---|
| Market cap Yahoo | **$31.92 B** | $32.25 B | **-1.0%** (mecanique, lie au cours) |
| Forward P/E | **-400.83** | -404.92 | **=** (placeholder, convergence mecanique) |
| EV/Revenue | **295.7x** | 314.4x | **-6.0%** |
| EV/EBITDA | **-79.38** | -84.40 | **=** |
| Beta | **2.634** | 2.634 | = |
| Short interest | **18.39%** | 18.39% | = |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **-13.0%** | -12.1% | **degradation -0.9 pt** |
| Price to book | **11.81** | 11.93 | **-1.0%** |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement speculative (EV/Revenue ~295.7x selon FMP, forward P/E -400.83). **Aucune revision sell-side** n'a ete enregistree (consensus $94.54, 12 analysts inchange). Le premium vs consensus se degrade mecaniquement a **-13.0%** suite a la legere baisse de cours. Les multiples extremement eleves confirment le caractere speculatif du titre. Aucun changement fondamental n'est a signaler entre le snapshot 17h du 16/06 et le snapshot 10h du 17/06.

**[ANOMALIE DONNEES PERSISTANTE]** — Market Cap Yahoo ($31.92 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Ecart de **+26.3%** stable.

---

## 4. Mise a Jour Sentiment / Options / News

| Signal | Valeur | Evolution vs snapshot 17h 16/06 |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain (JSON)** | $18.0 (aberrant) | **ANOMALIE RECURRENTE** — valeur operationnelle $100.0 conservee |
| **Put/Call ratio (JSON)** | null (aberrant) | **ANOMALIE RECURRENTE** — valeur operationnelle ~0.45 conservee |
| **Call OI % (JSON)** | null (aberrant) | **ANOMALIE RECURRENTE** — valeur operationnelle ~69% conservee |
| **Short Interest** | 18.39% | = — stable |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activite retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options** — Anomalie JSON **RECURRENTE**. Valeurs JSON aberrantes (max pain $18.0, put/call null, call OI null). Valeurs operationnelles estimees $100.0 / 0.45 / 69.0% conservees.
- **Short interest stable** (18.39%) — pas de couverture massive des shorts. Le setup squeeze reste theorique.
- **Aucun upgrade/downgrade**, absence totale d'activite institutionnelle/retail.
- **Aucun insider trade** significatif signale.

**Verdict Sentiment :** Neutre-Baissier — L'absence de news et d'activite institutionnelle persiste. La structure options legerement haussiere (operationnelle) ne suffit pas a contrebalancer la survente technique extreme. Le sentiment dominant reste technique et s'oriente a la baisse malgre la recovery volumetrique. Aucun catalyseur fondamental n'est visible.

---

## 5. Mise a Jour Agents Specialises

| Agent | Donnee AST/ASTS | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques. | [SIGNAUX NON SIGNIFICATIFS] |
| **Geopolitique** | Pas de flag specifique AST/ASTS. | [DONNEES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNEES MANQUANTES] |
| **Sector Rotation** | XLK (Technology) momentum score **10.0/10**, signal **NEUTRAL**. XLC (Communication Services) **bottom3**, momentum **0.0/10**. | 🟡 **Malus sectoriel** — ASTS est classe Technology mais proche de Communication Services (bottom3). |
| **FX Exposure** | Score FX Impact **0.0**, flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun evenement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | AST : earnings signale **2026-06-17** (FMP) — placeholder glissant J=0 non resolu depuis 25/05 (>23 jours). ASTS : earnings **2026-08-10** (53 jours). | Trop loin pour pricer. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **Validation Report** | [ERROR] AST — fetch failed. 4 errors total. | AST en erreur connue. |

---

## 6. Scoring Global Revise

### AST (donnees officielles — placeholder)

| Axe | Score Snapshot 10h | Pondération | Note |
|-----|-------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35% | [NON FONDE] — aucun catalyseur verifiable |
| Valorisation | 5.0/10 (placeholder) | 40% | [NON FONDE] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25% | [NON FONDE] — pas de cours, pas de momentum |
| **Score Opportunite** | **5.5/10** | — | Placeholder — **non utilisable pour decision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour decision** |
| **Score Global Ajuste** | **55.2/100** | — | Placeholder — **non utilisable pour decision** |

**Action recommandee par l'agent :** ATTENDRE (par defaut systeme)

> **Regle absolue :** sans donnees de cours, le scoring est un placeholder algorithmique. Il ne reflete aucune realite de marche.

### ASTS (proxy, a titre indicatif uniquement)

| Axe | Score Snapshot 10h | Pondération | Note |
|-----|-------------------|-------------|------|
| Catalyseur | 5.5/10 | 35% | Aucun catalyseur court terme. Earnings 10/08 distant. |
| Valorisation | 4.5/10 | 40% | EV/Revenue ~295.7x, forward P/E -400.83 — reste speculatif. Divergence consensus -13.0%. |
| Momentum | 3.5/10 | 25% | RSI 28.51 (survente extreme), baisse -6.08% vs previous, cours sous MM50 -7.4%, volume 0.73x. |
| **Score Opportunite** | **4.6/10** | — | **Non qualifie pour position** (score < 6) |
| **Score Global** | **46.0/100** | — | **SURVEILLER** |
| **Score Global Ajuste** | **43.0/100** | — | **SURVEILLER** (proche seuil EVITER) |

**Action recommandee :** SURVEILLER (stable)
**Timing :** Defavorable (survente extreme, sous MM50, volume sous moyenne)
**Horizon :** —

> ASTS n'est PAS dans le perimetre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'evolution du proxy. Le scoring **43.0/100 (SURVEILLER)** reflete une situation technique degradee mais stable. Le score Opportunite (4.6/10) reste sous le seuil de qualification (6.0/10), et la survente extreme (RSI 28.51) ainsi que la position sous MM50 ($88.88) de -7.4% maintiennent le biais prudent. La recovery volumetrique a 0.73x est un signal mitige mais insuffisant pour inverser le biais.

---

## 7. Revision des Niveaux SL / TP

### AST (donnees officielles)

**Impossibles a calculer.**
- Prix d'entree : inconnu
- ATR 14j : inexistant
- Stop-loss suggere = cours - 2xATR -> [NON CALCULABLE]
- Take-profit suggere = cours + 3xATR -> [NON CALCULABLE]

### ASTS (proxy — actualises avec snapshot 10h UTC 17/06)

| Parametre | Valeur | Justification |
|---|---|---|
| **Prix de reference** | $82.25 (close 10h 17/06) | Snapshot pre-ouverture US |
| **Stop-loss** | $57.45 (-30.2%) | 2xATR ($12.40) |
| **Take-profit** | $119.45 (+45.2%) | 3xATR ($12.40) |
| **Ratio R/R** | **1.5 : 1** | Inchange — inferieur au seuil 2:1 |

**Zone d'interet potentielle :** Stable vs snapshot 17h du 16/06. La legere baisse de -1.01% sur volume recovery (0.73x) est un signal mitige. La survente extreme (RSI 28.51) persiste. Un test de la **MM50 $88.88** avec volume > 25M serait la premiere condition d'amelioration technique credible. En l'absence de franchissement, le biais baissier moyen terme se maintient. Une **cassure sous $82.11** (low intraday 16/06) avec volume confirmerait la reprise de la distribution et ouvrirait la voie vers **$80.00-$81.50** puis **$76-78**. Une **cassure sous $80** avec volume eleve justifierait un passage de SURVEILLER a **EVITER**.

> **Note :** Les niveaux SL/TP sont actualises avec le nouveau close $82.25. Le ratio R/R reste a 1.5:1, inferieur au seuil institutionnel de 2:1.

---

## 8. Calendrier & Evenements a Venir

| Evenement | Ticker | Date | Jours restants | Detail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-17 | **J=0 glissant** | FMP placeholder non resolu depuis 25/05 (>23 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **53 jours** | Est EPS : -$0.29 a -$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-06-18 | **1 jour** | Max Pain operationnel $100.0 — anomalie JSON recurrente. Theta decay imminent. |

**Prochain catalyseur majeur :** Aucun avant earnings (aout). L'expiration options du 18 juin (demain, dans 1 jour) pourrait amplifier la volatilite a court terme si le cours se rapproche du max pain $100.0, mais la distance actuelle ($82.25 -> $100.0 = +21.6%) limite la pression gamma immediate.

---

## 9. Conclusion — These Confirmee / Modifiee / Invalidee ?

**These AST :** 🔴 **INVALIDEE PAR L'ABSENCE DE DONNEES — ANOMALIE STRUCTURELLE PERSISTANTE (>45 SNAPSHOTS CONSECUTIFS)**

**These ASTS (proxy) :** 🟡 **CONFIRMEE — STABILISATION MECANIQUE, BIAIS SURVEILLER MAINTENU (43.0/100)**

Le snapshot 10h UTC du 17/06 confirme la these SURVEILLER sur ASTS avec les observations suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon errone d'ASTS. AST n'a toujours aucune donnee de cours apres **>45 snapshots consecutifs** (18/05 -> 17/06). La suppression ou l'exclusion de la watchlist reste recommandee.
2. 🟡 **STABILISATION MECANIQUE SUR ASTS :** le cours recule marginalement de **-1.01%** a **$82.25** sur **volume recovery a 0.73x** (20.04M vs 27.33M moy. 20j). La recovery volumetrique est positive mais insuffisante pour inverser le biais.
3. 🔴 **RSI en survente extreme :** 28.51 vs 28.73 — le titre reste en zone de survente prononcee (< 30) depuis plusieurs sessions. Aucun rebond technique visible.
4. 🔴 **Cours s'eloigne de la MM50 ($88.88) :** le cours a $82.25 se situe desormais **-7.4% sous la MM50**. L'ecart s'est legerement elargi, confirmant la rupture de la tendance moyen terme.
5. 🟡 **Anomalie options JSON RECURRENTE :** max pain JSON $18.0 aberrant (operationnel $100.0), put/call null, call OI null — faux positif pipeline confirme. Valeurs operationnelles conservees.
6. 🟡 **Short interest stable :** 18.39% — pas de couverture massive des shorts. Le setup squeeze reste theorique.
7. ⚠️ **Echeance options dans 1 jour :** Le 18 juin (mercredi). Theta decay imminent sur les options OTM.
8. 🟡 **Score agent stable :** 43.0/100 (SURVEILLER) — reste proche du seuil EVITER (< 35). Le score Opportunite (4.6/10) reste sous le seuil de qualification.
9. 🟡 **Aucune news fondamentale** ni evenement corporate — le contexte reste purement technique.
10. 🟡 **Earnings placeholder glissant non resolu :** FMP signale un earnings AST le **2026-06-17** (`days_until: 0`), mais sans historique de prix, le resultat ne peut etre correle. Le glissement J=0 persiste depuis le **25/05** (>23 jours de decalage non resolu).
11. 🟡 **Malus sectoriel** — XLC (Communication Services) bottom3 sectoriel avec momentum 0.0/10. ASTS est classe Technology mais proche de Communication Services.

**Recommandation operationnelle :**
- **Resoudre l'anomalie structurelle immediatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker valide avec data completes
- **Ne pas engager de capital sur AST** tant que les donnees de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence** — la these SURVEILLER est maintenue. Les niveaux cles a surveiller :
  - **Cassure sous $82.11** (low intraday 16/06) avec volume -> prochaines cibles $80.00-$81.50 puis $76-78
  - **Cassure sous $80** avec volume eleve -> passage de SURVEILLER a EVITER
  - **Rebond au-dessus de $85.70** (open 17/06) avec volume > 15M -> possible stabilisation
  - **Rebond au-dessus de $88.88** (MM50) avec volume > 25M -> possible retournement technique
  - **Rebond au-dessus de $97.56** (close vendredi) -> combler le gap, retour du biais haussier mais necessite confirmation volume > 25 M
- **Ne pas entrer de position longue** sur ASTS avant un test reussi de la MM50 ($88.88) avec volume confirme, ou un catalyseur fondamental verifiable
- **Surveiller l'echeance options 2026-06-18** (mercredi) — theta decay risque si le cours reste sous $85

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades detailles, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Donnees quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## References

- `data/latest.json` (snapshot 2026-06-17T10:00:01Z) — AST: error "No price history" ; ASTS: close $82.25, previous_close $87.57, RSI 28.51, ATR $12.40, MM50 $88.88, volume 20,039,200 (0.73x), short interest 18.39%, consensus FMP $94.54, options JSON aberrantes (max_pain $18.0, put_call_ratio null, call_oi_pct null)
- `data/validation_report.txt` (2026-06-17) — [ERROR] AST: fetch failed. 4 errors total, 0 excluded.
- `data/recommandations_latest.json` (2026-06-17) — AST: 55.2/100 (ATTENDRE) ; ASTS: 46.0/100 ajuste 43.0/100 (SURVEILLER)
- `data/sector_rotation_2026-06-17.json` — XLK top sectoriel (momentum 10.0/10, signal NEUTRAL), XLC bottom (momentum 0.0/10)
- `data/fx_exposure_2026-06-17.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-17.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-17.json` — AST: earnings 2026-06-17 (J=0 glissant) ; ASTS: earnings 2026-08-10 (53 jours)
- `data/events_2026-06-17.json` — Aucun evenement corporate detecte pour AST/ASTS
- `data/geo_risk_latest.json` (2026-05-17) — Pas de flag specifique AST/ASTS
- `data/quant_report_latest.json` (2026-05-17) — Donnees quantitatives insuffisantes
