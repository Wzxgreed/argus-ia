# AST — Mise a Jour Post-Session US (2026-06-16 17h UTC)

> **Source :** `data/latest.json` (snapshot 2026-06-16T17:00:01Z) | `data/recommandations_latest.json` | `data/validation_report.txt`
> **Reference precedente :** [AST_2026-06-16_update.md](AST_2026-06-16_update.md) (pre-ouverture US 10h UTC 16/06)
> **Contexte :** Snapshot post-session US du 16/06. Donnees de trading reelles etablies pour ASTS. Anomalie options JSON resolue.

---

## 1. Resume des Changements depuis le Snapshot Pre-Ouverture (10h UTC 16/06)

| Metrique | Snapshot 10h (16/06) | Snapshot 17h (16/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirme stable — >44 snapshots consecutifs** |
| **ASTS — Cours close** | **$87.57** (close 15/06) | **$83.09** | **-5.12%** — deterioration nette de la seance |
| **ASTS — Previous close** | $82.41 | **$87.57** | rebond du 15/06 devenu previous |
| **ASTS — RSI 14j** | 36.0 | **28.73** | **-7.27 pts** — survente aggravee |
| **ASTS — ATR 14j** | $12.80 | **$12.40** | **-3.1%** — compression volatilite |
| **ASTS — MM 50j** | $89.13 | **$88.90** | **-0.26%** — legere baisse |
| **ASTS — Distance MM50** | -1.5% | **-6.5%** | **ecart elargi** — cours s'eloigne de la MM50 |
| **ASTS — Volume seance** | 23.92M (0.87x) | **11.35M (0.42x)** | **-52.5% / collapse volumetrique** |
| **ASTS — Volume relatif** | 0.87x | **0.42x** | **effondre** — distribution sur volume faible |
| **ASTS — Short Interest** | 18.39% | **18.39%** | = — stable |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = |
| **ASTS — Premium vs consensus** | -7.96% | **-12.1%** | **degradation -4.1 pts** |
| **ASTS — Options Max Pain** | $100.0 (operationnel) | **$100.0** | = — **anomalie JSON RESOLUE** |
| **ASTS — Options Put/Call** | 0.44 (operationnel) | **0.45** | = — **anomalie JSON RESOLUE** |
| **ASTS — Options Call OI %** | 69.7% (operationnel) | **69.0%** | = — **anomalie JSON RESOLUE** |
| **ASTS — Echeance options** | 2026-06-18 (2j) | **2026-06-18 (1j)** | **-1j** — mardi soir |
| **Score Global ASTS** | 39.2/100 (SURVEILLER) | **43.0/100 (SURVEILLER)** | **+3.8 pts** (ajuste mecanique) |
| **Score Opportunite ASTS** | 4.7/10 | **4.6/10** | **-0.1 pt** |

**Verdict :** Le snapshot post-session 17h UTC du 16/06 enregistre une **deterioration technique nette** sur ASTS. Le cours a recule de **-5.12%** a **$83.09** sur un **volume collapse a 0.42x** (11.35M vs 26.89M moy. 20j). Le RSI s'est enfonce a **28.73** (survente aggravee vs 36.0) et l'ecart a la MM50 s'est elargi a **-6.5%** ($83.09 vs $88.90). **Anomalie options JSON resolue** : les valeurs JSON sont desormais coherentes (max pain $100.0, put/call 0.45, call OI 69.0%). L'echeance options du 18/06 est desormais dans **1 jour** (mardi soir). Le scoring agent ajuste remonte mecaniquement a **43.0/100 (SURVEILLER)** malgre la baisse du cours — probable recalibration interne de l'agent.

---

## 2. Mise a Jour Technique

### AST (donnees officielles)

| Indicateur | Valeur Snapshot 17h | Valeur precedente (10h 16/06) | Δ |
|-----------|---------------------|------------------------------|---|
| Cours close | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| Volume | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| MM 50j | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |

**Verdict timing AST :** [NON EVALUABLE] — absence totale de donnees techniques sur **>44 snapshots consecutifs** (18/05 -> 16/06).

### ASTS (proxy — donnees post-session US 17h UTC 16/06)

| Indicateur | Valeur Snapshot 17h | Valeur Snapshot 10h | Δ |
|-----------|-------------------|-------------------|---|
| Cours close | **$83.09** | $87.57 | **-5.12%** |
| Previous close | **$87.57** | $82.41 | rebond 15/06 devenu reference |
| RSI 14j | **28.73** | 36.0 | **-7.27 pts** — survente aggravee |
| ATR 14j | **$12.40** | $12.80 | **-3.1%** |
| MM50 | **$88.90** | $89.13 | **-0.26%** |
| Distance MM50 | **-6.5%** | -1.5% | **ecart elargi** |
| Volume seance | **11.35M** | 23.92M | **-52.5%** — collapse |
| Volume relatif | **0.42x** | 0.87x | **effondre** |
| Short interest | **18.39%** | 18.39% | = — stable |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 36.08 | 36.08 | = |

**Verdict timing ASTS :** 🔴 **DETERIORATION TECHNIQUE NETTE — DISTRIBUTION SUR VOLUME COLLAPSE**

- **RSI 28.73** : la survente s'est aggravee. Le titre est desormais en zone de survente prononcee (< 30). Le rebond du 15/06 a ete completement efface.
- **Volume 0.42x** : **11.35M vs moyenne 20j 26.89M** — effondrement volumetrique. La distribution se fait sur volume tres faible, ce qui est baissier : les vendeurs ne trouvent pas d'acheteurs et le cours s'effrite.
- **Cours sous MM50 ($88.90)** : le cours a $83.09 se situe desormais **-6.5% sous la MM50**. L'ecart s'est elargi, confirmant la rupture de la tendance moyen terme.
- **ATR $12.40** : legere compression de la volatilite malgre la baisse — signe que le marche s'endort sur la baisse (danger de continuation).
- **Short interest stable a 18.39%** : pas de couverture massive des shorts detectee. Le setup squeeze reste theorique mais le volume effondre rend toute couverture risquee.

**Niveaux cles** (actualises avec close US 17h UTC 16/06) :
- Support immediat : **$82.11** (low intraday 16/06)
- Support : **$80.00-$81.50** (zone de confluence + 1.5xATR)
- Support critique : **$76-78** (test du 15/06 non franchi, zone de repli majeure)
- Resistance immediatte : **$85.78** (open 16/06 / gap a combler)
- Resistance majeure : **$88.90** (MM50 — test de retour comme resistance)
- Objectif haussier : **$120.29** (spot + 3xATR $12.40)

**Structure options** (anomalie JSON resolue — valeurs desormais natives) :
- **Max Pain** : **$100.0** — valeur JSON native coherente. Le max pain reste eloigne du cours ($83.09 -> $100.0 = +20.3%).
- **Put/Call ratio** : **0.45** — structure modereement haussiere (calls dominants). Valeur JSON native coherente.
- **Call OI %** : **69.0%** — confirmation de la dominance call moderee. Valeur JSON native coherente.
- Expiration proche : **2026-06-18** (1 jour) — theta decay imminent pour les options OTM.

> **Note options :** L'anomalie JSON recurrente sur ASTS est **RESOLUE** dans le snapshot 17h UTC. Les valeurs natives (max pain $100.0, put/call 0.45, call OI 69.0%) sont coherentes et conformes a la structure operationnelle du marche. Le max pain $100.0 est eloigne du cours actuel ($83.09), ce qui limite la pression gamma immediate mais pourrait attirer le cours vers $90-$100 si la volatilite reste elevee jusqu'a mercredi.

---

## 3. Mise a Jour Fondamentale

### AST (donnees officielles)

| Metrique | Valeur Snapshot 17h | Valeur precedente | Δ |
|---------|---------------------|-------------------|---|
| Market cap | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Filtre Qualite (6 criteres) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualite :** impossible a calculer sans etats financiers accessibles.

### ASTS (proxy)

| Metrique | Valeur Snapshot 17h | Valeur Snapshot 10h | Δ |
|---------|---------------------|-----------------------|---|
| Market cap Yahoo | **$32.25 B** | $33.99 B | **-5.1%** (mecanique, lie au cours) |
| Forward P/E | **-404.92** | -426.75 | **=** (placeholder, convergence mecanique) |
| EV/Revenue | **314.4x** | 314.4x | = |
| EV/EBITDA | **-84.40** | -84.40 | = |
| Beta | **2.634** | 2.634 | = |
| Short interest | **18.39%** | 18.39% | = |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **-12.1%** | -7.96% | **degradation -4.1 pts** |
| Price to book | **11.93** | 12.57 | **-5.1%** |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement speculative (EV/Revenue ~314x selon FMP, forward P/E -404.92). **Aucune revision sell-side** n'a ete enregistree (consensus $94.54, 12 analysts inchange). Le premium vs consensus se degrade mecaniquement a **-12.1%** suite a la baisse de cours. Les multiples extremement eleves confirment le caractere speculatif du titre. Aucun changement fondamental n'est a signaler entre le snapshot 10h et le snapshot 17h du 16/06.

**[ANOMALIE DONNEES PERSISTANTE]** — Market Cap Yahoo ($32.25 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Ecart de **+27.5%** stable.

---

## 4. Mise a Jour Sentiment / Options / News

| Signal | Valeur | Evolution vs snapshot 10h |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain (JSON)** | $100.0 | **RESOLU** — valeur native coherente |
| **Put/Call ratio (JSON)** | 0.45 | **RESOLU** — valeur native coherente |
| **Call OI % (JSON)** | 69.0% | **RESOLU** — valeur native coherente |
| **Short Interest** | 18.39% | = — stable |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activite retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options** — Anomalie JSON **RESOLUE**. Valeurs natives desormais coherentes : max pain $100.0, put/call 0.45, call OI 69.0%. Structure modereement haussiere stable.
- **Short interest stable** (18.39%) — pas de couverture massive des shorts. Le setup squeeze reste theorique mais le volume collapse limite la probabilite d'un short squeeze spontane.
- **Aucun upgrade/downgrade**, absence totale d'activite institutionnelle/retail.
- **Aucun insider trade** significatif signale.

**Verdict Sentiment :** Neutre-Baissier — L'absence de news et d'activite institutionnelle persiste. La structure options legerement haussiere (native) ne suffit pas a contrebalancer la deterioration technique. Le sentiment dominant reste technique et s'oriente a la baisse avec le volume collapse. Aucun catalyseur fondamental n'est visible.

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
| **Upcoming Events** | AST : earnings signale **2026-06-16** (FMP) — placeholder glissant J=0 non resolu depuis 25/05 (>22 jours). ASTS : earnings **2026-08-10** (54 jours). | Trop loin pour pricer. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **Validation Report** | [ERROR] AST — fetch failed. 4 errors total. | AST en erreur connue. |

---

## 6. Scoring Global Revise

### AST (donnees officielles — placeholder)

| Axe | Score Snapshot 17h | Pondération | Note |
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

| Axe | Score Snapshot 17h | Pondération | Note |
|-----|-------------------|-------------|------|
| Catalyseur | 5.5/10 | 35% | Aucun catalyseur court terme. Earnings 10/08 distant. |
| Valorisation | 4.5/10 | 40% | EV/Revenue ~314x, forward P/E -404.92 — reste speculatif. Divergence consensus -12.1%. |
| Momentum | 3.5/10 | 25% | RSI 28.73 (survente aggravee), baisse -5.12% sur volume collapse 0.42x, cours sous MM50 -6.5%. |
| **Score Opportunite** | **4.6/10** | — | **Non qualifie pour position** (score < 6) |
| **Score Global** | **46.0/100** | — | **SURVEILLER** |
| **Score Global Ajuste** | **43.0/100** | — | **SURVEILLER** (proche seuil EVITER) |

**Action recommandee :** SURVEILLER (stable)
**Timing :** Defavorable (distribution sur volume collapse, survente aggravee, sous MM50)
**Horizon :** —

> ASTS n'est PAS dans le perimetre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'evolution du proxy. Le scoring **43.0/100 (SURVEILLER)** reflete une situation technique degradee. Le score Opportunite (4.6/10) reste sous le seuil de qualification (6.0/10), et la survente aggravee (RSI 28.73) ainsi que la position sous MM50 ($88.90) de -6.5% maintiennent le biais prudent. Le volume collapse a 0.42x est un signal baissier additionnel.

---

## 7. Revision des Niveaux SL / TP

### AST (donnees officielles)

**Impossibles a calculer.**
- Prix d'entree : inconnu
- ATR 14j : inexistant
- Stop-loss suggere = cours - 2xATR -> [NON CALCULABLE]
- Take-profit suggere = cours + 3xATR -> [NON CALCULABLE]

### ASTS (proxy — actualises avec close US 17h UTC 16/06)

| Parametre | Valeur | Justification |
|---|---|---|
| **Prix de reference** | $83.09 (close 17h 16/06) | Close officiel US, post-session |
| **Stop-loss** | $58.29 (-29.2%) | 2xATR ($12.40) |
| **Take-profit** | $120.29 (+44.8%) | 3xATR ($12.40) |
| **Ratio R/R** | **1.5 : 1** | Inchange — inferieur au seuil 2:1 |

**Zone d'interet potentielle :** Degradee vs snapshot 10h. La baisse de -5.12% sur volume collapse (0.42x) est un signal de distribution. Le rebond du 15/06 a ete completement efface. Un test de la **MM50 $88.90** avec volume > 20M serait la premiere condition d'amelioration technique credible. En l'absence de franchissement, le biais baissier moyen terme s'intensifie. Une **cassure sous $82.11** (low intraday 16/06) avec volume confirmerait la reprise de la distribution et ouvrirait la voie vers **$80.00-$81.50** puis **$76-78**. Une **cassure sous $80** avec volume eleve justifierait un passage de SURVEILLER a **EVITER**.

> **Note :** Les niveaux SL/TP sont actualises avec le nouveau close $83.09 et le nouvel ATR $12.40. Le ratio R/R reste a 1.5:1, inferieur au seuil institutionnel de 2:1.

---

## 8. Calendrier & Evenements a Venir

| Evenement | Ticker | Date | Jours restants | Detail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-16 | **J=0 glissant** | FMP placeholder non resolu depuis 25/05 (>22 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **54 jours** | Est EPS : -$0.29 a -$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-06-18 | **1 jour** | Max Pain $100.0 — structure legerement haussiere. Theta decay imminent. |

**Prochain catalyseur majeur :** Aucun avant earnings (aout). L'expiration options du 18 juin (mercredi, dans 1 jour) pourrait amplifier la volatilite a court terme si le cours se rapproche du max pain $100.0, mais la distance actuelle ($83.09 -> $100.0 = +20.3%) limite la pression gamma immediate.

---

## 9. Conclusion — These Confirmee / Modifiee / Invalidee ?

**These AST :** 🔴 **INVALIDEE PAR L'ABSENCE DE DONNEES — ANOMALIE STRUCTURELLE PERSISTANTE (>44 SNAPSHOTS CONSECUTIFS)**

**These ASTS (proxy) :** 🔴 **MODIFIEE — DETERIORATION TECHNIQUE NETTE, BIAIS SURVEILLER RENFORCE (43.0/100)**

Le snapshot post-session 17h UTC du 16/06 degrade la these sur ASTS avec les observations suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon errone d'ASTS. AST n'a toujours aucune donnee de cours apres **>44 snapshots consecutifs** (18/05 -> 16/06). La suppression ou l'exclusion de la watchlist reste recommandee.
2. 🔴 **DETERIORATION TECHNIQUE NETTE SUR ASTS :** le cours a recule de **-5.12%** a **$83.09** sur **volume collapse a 0.42x** (11.35M vs 26.89M moy. 20j). Cette distribution sur volume effondre est baissiere.
3. 🔴 **RSI en survente aggravee :** 28.73 vs 36.0 — le titre est desormais en zone de survente prononcee (< 30). Le rebond du 15/06 a ete completement efface.
4. 🔴 **Cours s'eloigne de la MM50 ($88.90) :** le cours a $83.09 se situe desormais **-6.5% sous la MM50**. L'ecart s'est elargi, confirmant la rupture de la tendance moyen terme.
5. 🟢 **Anomalie options JSON RESOLUE :** max pain $100.0, put/call 0.45, call OI 69.0% — valeurs JSON desormais natives et coherentes. Faux positif pipeline confirme.
6. 🟡 **Short interest stable :** 18.39% — pas de couverture massive des shorts. Le setup squeeze reste theorique mais le volume collapse limite la probabilite.
7. ⚠️ **Echeance options dans 1 jour :** Le 18 juin (mercredi). Theta decay imminent sur les options OTM.
8. 🟡 **Score agent ajuste mecaniquement :** 43.0/100 (SURVEILLER) — reste proche du seuil EVITER (< 35). Le score Opportunite (4.6/10) reste sous le seuil de qualification.
9. 🟡 **Aucune news fondamentale** ni evenement corporate — le contexte reste purement technique.
10. 🟡 **Earnings placeholder glissant non resolu :** FMP signale un earnings AST le **2026-06-16** (`days_until: 0`), mais sans historique de prix, le resultat ne peut etre correle. Le glissement J=0 persiste depuis le **25/05** (>22 jours de decalage non resolu).
11. 🟡 **Malus sectoriel** — XLC (Communication Services) bottom3 sectoriel avec momentum 0.0/10. ASTS est classe Technology mais proche de Communication Services.

**Recommandation operationnelle :**
- **Resoudre l'anomalie structurelle immediatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker valide avec data completes
- **Ne pas engager de capital sur AST** tant que les donnees de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence accrue** — la these SURVEILLER est maintenue mais renforcee par la deterioration technique. Les niveaux cles a surveiller :
  - **Cassure sous $82.11** (low intraday 16/06) avec volume -> prochaines cibles $80.00-$81.50 puis $76-78
  - **Cassure sous $80** avec volume eleve -> passage de SURVEILLER a EVITER
  - **Rebond au-dessus de $85.78** (open 16/06 / gap) avec volume > 15M -> possible stabilisation
  - **Rebond au-dessus de $88.90** (MM50) avec volume > 20M -> possible retournement technique
  - **Rebond au-dessus de $97.56** (close vendredi) -> combler le gap, retour du biais haussier mais necessite confirmation volume > 25 M
- **Ne pas entrer de position longue** sur ASTS avant un test reussi de la MM50 ($88.90) avec volume confirme, ou un catalyseur fondamental verifiable
- **Surveiller l'echeance options 2026-06-18** (mercredi) — theta decay risque si le cours reste sous $85

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades detailles, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Donnees quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## References

- `data/latest.json` (snapshot 2026-06-16T17:00:01Z) — AST: error "No price history" ; ASTS: close $83.09, previous_close $87.57, RSI 28.73, ATR $12.40, MM50 $88.90, volume 11,345,332 (0.42x), short interest 18.39%, consensus FMP $94.54, options JSON resolues (max_pain $100.0, put_call_ratio 0.45, call_oi_pct 69.0%)
- `data/validation_report.txt` (2026-06-16) — [ERROR] AST: fetch failed. 4 errors total, 0 excluded.
- `data/recommandations_latest.json` (2026-06-16) — AST: 55.2/100 (ATTENDRE) ; ASTS: 46.0/100 ajuste 43.0/100 (SURVEILLER)
- `data/sector_rotation_2026-06-16.json` — XLK top sectoriel (momentum 10.0/10, signal NEUTRAL), XLC bottom (momentum 0.0/10)
- `data/fx_exposure_2026-06-16.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-16.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-16.json` — AST: earnings 2026-06-16 (J=0 glissant) ; ASTS: earnings 2026-08-10 (54 jours)
- `data/events_2026-06-16.json` — Aucun evenement corporate detecte pour AST/ASTS
- `data/geo_risk_latest.json` (2026-05-17) — Pas de flag specifique AST/ASTS
- `data/quant_report_latest.json` (2026-05-17) — Donnees quantitatives insuffisantes
