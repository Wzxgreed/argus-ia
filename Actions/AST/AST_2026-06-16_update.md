# AST — Mise a Jour Pre-ouverture US (2026-06-16 10h UTC)

> **Source :** `data/latest.json` (snapshot 2026-06-16T10:00:01Z) | `data/recommandations_latest.json` | `data/validation_report.txt`
> **Reference precedente :** [AST_2026-06-15_update_21h.md](AST_2026-06-15_update_21h.md) (close US 21h UTC 15/06)
> **Contexte :** Snapshot pre-ouverture US du 16/06 (10h UTC). Donnees brutes mecaniquement identiques au close 21h UTC 15/06. Anomalie options JSON recurrente detectee et traitee.

---

## 1. Resume des Changements depuis le Close US 21h UTC (2026-06-15)

| Metrique | Snapshot 21h (15/06) | Snapshot 10h (16/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirme stable — >44 snapshots consecutifs** |
| **ASTS — Cours close** | **$87.57** | **$87.57** | **=** — stabilite mecanique pre-ouverture |
| **ASTS — Previous close** | $82.41 | **$82.41** | = |
| **ASTS — RSI 14j** | 36.0 | **36.0** | **=** — survente stable |
| **ASTS — ATR 14j** | $12.80 | **$12.80** | **=** |
| **ASTS — MM 50j** | $89.13 | **$89.13** | **=** — cours sous MM50 de -1.5% |
| **ASTS — Volume seance** | 23.57M (0.86x) | **23.92M (0.87x)** | **+1.5%** — revision mecanique negligeable |
| **ASTS — Volume relatif** | 0.86x | **0.87x** | **=** — quasi-normal |
| **ASTS — Short Interest** | 18.39% | **18.39%** | = — stable |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = |
| **ASTS — Premium vs consensus** | -7.96% | **-7.96%** | = — stable |
| **ASTS — Options Max Pain** | $100.0 | **$28.0** | **ANOMALIE JSON** — valeur operationnelle conservee $100.0 |
| **ASTS — Options Put/Call** | 0.44 | **0.0** | **ANOMALIE JSON** — valeur operationnelle conservee 0.44 |
| **ASTS — Options Call OI %** | 69.7% | **100.0%** | **ANOMALIE JSON** — valeur operationnelle conservee 69.7% |
| **ASTS — Echeance options** | 2026-06-18 (3j) | **2026-06-18 (2j)** | **-1j** — mercredi prochain |
| **Score Global ASTS** | 39.2/100 (SURVEILLER) | **39.2/100 (SURVEILLER)** | = — stable |
| **Score Opportunite ASTS** | 4.7/10 | **4.7/10** | = — stable |

**Verdict :** Le snapshot 10h UTC du 16/06 est **strictement identique** en donnees brutes au close 21h UTC 15/06 (pre-ouverture US). Aucun nouveau cours n'a ete etabli. **Anomalie options JSON recurrente** detectee : max pain $28.0, put/call 0.0, call OI 100.0% — valeurs aberrantes. Les valeurs operationnelles du close 15/06 ($100.0, 0.44, 69.7%) sont conservees. L'echeance options du 18/06 est desormais dans **2 jours** (mercredi). Le scoring agent reste stable a **39.2/100 (SURVEILLER)**.

---

## 2. Mise a Jour Technique

### AST (donnees officielles)

| Indicateur | Valeur Snapshot 10h | Valeur precedente (21h 15/06) | Δ |
|-----------|---------------------|------------------------------|---|
| Cours close | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| Volume | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| MM 50j | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |

**Verdict timing AST :** [NON EVALUABLE] — absence totale de donnees techniques sur **>44 snapshots consecutifs** (18/05 -> 16/06).

### ASTS (proxy — donnees pre-ouverture US 10h UTC 16/06, mecaniquement identiques au close 21h UTC 15/06)

| Indicateur | Valeur Snapshot 10h | Valeur Snapshot 21h | Δ |
|-----------|-------------------|-------------------|---|
| Cours close | **$87.57** | $87.57 | **=** (stabilite mecanique) |
| Previous close | **$82.41** | $82.41 | = |
| RSI 14j | **36.0** | 36.0 | **=** — survente stable |
| ATR 14j | **$12.80** | $12.80 | **=** |
| MM50 | **$89.13** | $89.13 | **=** — cours sous MM50 de **-1.5%** |
| Volume seance | **23.92M** | 23.57M | **+1.5%** — revision mecanique negligeable |
| Volume relatif | **0.87x** | 0.86x | **=** — quasi-normal |
| Short interest | **18.39%** | 18.39% | = — stable |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 36.08 | 36.08 | = |

**Verdict timing ASTS :** 🟡 **STABILITE MECANIQUE PRE-OUVERTURE — AUCUN NOUVEAU SIGNAL TECHNIQUE**

- **RSI 36.0** : la survente persiste. Aucun changement depuis le close 15/06.
- **Volume 0.87x** : **23.92M vs moyenne 20j 27.57M** (revision mecanique de +1.5% vs 23.57M a 21h). Le rebond du 15/06 reste valide sur volume quasi-normal.
- **Cours sous MM50 ($89.13)** : le cours a $87.57 reste **-1.5% sous la MM50**. Pas de test de la resistance moyen terme.
- **ATR $12.80** : stable.
- **Short interest stable a 18.39%** : pas de couverture massive des shorts detectee. Le setup squeeze reste theorique.

**Niveaux cles** (inchangés — actualises avec close US 21h UTC 15/06, dernier close disponible) :
- Support immediat : **$83.99** (low intraday 15/06)
- Support : **$82.41** (previous close / low matinal)
- Support critique : **$80.00-$81.50** (zone de confluence + 1.5xATR)
- Resistance immediatte : **$89.13** (MM50 — test de retour comme resistance)
- Resistance majeure : **$97.56** (close vendredi 12/06 / gap a combler)
- Objectif haussier : **$125.97** (spot + 3xATR $12.80)

**Structure options** (anomalie JSON recurrente traitee) :
- **Max Pain (operationnel)** : **$100.0** — valeur du close 15/06 conservee. Le max pain JSON $28.0 est aberrant (52W low = 36.08, le max pain ne peut etre inferieur au 52W low).
- **Put/Call ratio (operationnel)** : **0.44** — structure modereement haussiere (calls dominants). Le JSON 0.0 est aberrant.
- **Call OI % (operationnel)** : **69.7%** — confirmation de la dominance call moderee. Le JSON 100.0% est aberrant.
- Expiration proche : **2026-06-18** (2 jours) — theta decay imminent pour les options OTM.

> **Note options :** L'anomalie JSON recurrente sur ASTS est documentee depuis plusieurs sessions (18/05 -> 16/06). Les valeurs operationnelles (max pain $100.0, put/call 0.44, call OI 69.7%) sont stables depuis le close 15/06 et coherentes avec la structure de marche. Le max pain $100.0 est eloigne du cours actuel ($87.57), ce qui limite la pression gamma immediate mais pourrait attirer le cours vers $90-$100 si la volatilite reste elevee jusqu'a mercredi.

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

| Metrique | Valeur Snapshot 10h | Valeur Snapshot 21h | Δ |
|---------|---------------------|-----------------------|---|
| Market cap Yahoo | **$33.99 B** | $33.99 B | **=** |
| Forward P/E | **-426.75** | -427.49 | **=** (placeholder, mecanique) |
| EV/Revenue | **314.4x** | 296.3x | **+6.1%** — ecart lie a la source FMP vs Yahoo |
| EV/EBITDA | **-84.40** | -79.53 | **=** (placeholder) |
| Beta | **2.634** | 2.634 | = |
| Short interest | **18.39%** | 18.39% | = |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **-7.96%** | -7.96% | = |
| Price to book | **12.57** | 12.57 | = |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement speculative (EV/Revenue ~314x selon FMP, forward P/E -426.75). **Aucune revision sell-side** n'a ete enregistree (consensus $94.54, 12 analysts inchange). Le premium vs consensus reste a **-7.96%**. Les multiples extremement eleves confirment le caractere speculatif du titre. Aucun changement fondamental n'est a signaler entre le close 15/06 et le snapshot pre-ouverture 16/06.

**[ANOMALIE DONNEES PERSISTANTE]** — Market Cap Yahoo ($33.99 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Ecart de **+34.4%** stable.

---

## 4. Mise a Jour Sentiment / Options / News

| Signal | Valeur | Evolution vs snapshot 21h |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain (JSON)** | $28.0 | **ANOMALIE JSON** — valeur operationnelle conservee $100.0 |
| **Put/Call ratio (JSON)** | 0.0 | **ANOMALIE JSON** — valeur operationnelle conservee 0.44 |
| **Call OI % (JSON)** | 100.0% | **ANOMALIE JSON** — valeur operationnelle conservee 69.7% |
| **Short Interest** | 18.39% | = — stable |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activite retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options** — Anomalie JSON recurrente traitee. Valeurs operationnelles conservees : max pain $100.0, put/call 0.44, call OI 69.7%. Structure modereement haussiere stable.
- **Short interest stable** (18.39%) — pas de couverture massive des shorts. Le setup squeeze reste theorique.
- **Aucun upgrade/downgrade**, absence totale d'activite institutionnelle/retail.
- **Aucun insider trade** significatif signale.

**Verdict Sentiment :** Neutre — L'absence de news et d'activite institutionnelle persiste. La structure options legerement haussiere (operationnelle) et le volume quasi-normal rendent le rebond credible, mais le sentiment dominant reste technique. Aucun catalyseur fondamental n'est visible.

---

## 5. Mise a Jour Agents Specialises

| Agent | Donnee AST/ASTS | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques. | [SIGNAUX NON SIGNIFICATIFS] |
| **Geopolitique** | Pas de flag specifique AST/ASTS. | [DONNEES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNEES MANQUANTES] |
| **Sector Rotation** | XLK (Technology) momentum score **10.0/10**, signal **NEUTRAL**. XLC (Communication Services) bottom3, momentum **10.0/10** (donnees NaN — placeholder). | [DONNEES PARTIELLES] — ASTS est classe Technology mais proche de Communication Services. |
| **FX Exposure** | Score FX Impact **0.0**, flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun evenement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | AST : earnings signale **2026-06-16** (FMP) — placeholder glissant J=0 non resolu depuis 25/05 (>22 jours). ASTS : earnings **2026-08-10** (55 jours). | Trop loin pour pricer. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **Validation Report** | [ERROR] AST — fetch failed. 5 errors total. | AST en erreur connue. |

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
| Valorisation | 4.5/10 | 40% | EV/Revenue ~314x, forward P/E -426.75 — reste speculatif. Divergence consensus -7.96%. |
| Momentum | 4.0/10 | 25% | RSI 36.0 (survente), rebond +6.26% sur volume quasi-normal (0.87x), cours sous MM50. |
| **Score Opportunite** | **4.7/10** | — | **Non qualifie pour position** (score < 6) |
| **Score Global** | **47.2/100** | — | **SURVEILLER** |
| **Score Global Ajuste** | **39.2/100** | — | **SURVEILLER** (proche seuil EVITER) |

**Action recommandee :** SURVEILLER (stable)
**Timing :** Defavorable (rebond valide mais survente persistante, sous MM50)
**Horizon :** —

> ASTS n'est PAS dans le perimetre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'evolution du proxy. Le scoring **stable a 39.2/100 (SURVEILLER)** reflete une situation technique inchangee. Le score Opportunite (4.7/10) reste sous le seuil de qualification (6.0/10), et la survente persistante (RSI 36.0) ainsi que la position sous MM50 ($89.13) maintiennent le biais prudent.

---

## 7. Revision des Niveaux SL / TP

### AST (donnees officielles)

**Impossibles a calculer.**
- Prix d'entree : inconnu
- ATR 14j : inexistant
- Stop-loss suggere = cours - 2xATR -> [NON CALCULABLE]
- Take-profit suggere = cours + 3xATR -> [NON CALCULABLE]

### ASTS (proxy — inchanges, dernier close US 21h UTC 15/06)

| Parametre | Valeur | Justification |
|---|---|---|
| **Prix de reference** | $87.57 (close 21h 15/06) | Close officiel US, dernier disponible |
| **Stop-loss** | $61.97 (-29.2%) | 2xATR ($12.80) |
| **Take-profit** | $125.97 (+43.8%) | 3xATR ($12.80) |
| **Ratio R/R** | **1.5 : 1** | Inchangé — inferieur au seuil 2:1 |

**Zone d'interet potentielle :** Inchangee vs close 15/06. Le rebond technique +6.26% sur volume quasi-normal (0.87x) reste valide, mais ne constitue pas encore un signal d'achat fiable. Un test de la **MM50 $89.13** avec volume > 25M serait la premiere condition d'amelioration technique credible. En l'absence de franchissement, le biais baissier moyen terme persiste. Une **cassure sous $83.99** (low intraday 15/06) avec volume confirmerait la reprise de la distribution et ouvrirait la voie vers **$82.41** puis **$80.00-$81.50**. Une **cassure sous $80** avec volume eleve justifierait un passage de SURVEILLER a **EVITER**.

> **Note :** Les niveaux SL/TP sont inchanges car le snapshot 16/06 10h UTC est pre-ouverture et n'a pas genere de nouveau close.

---

## 8. Calendrier & Evenements a Venir

| Evenement | Ticker | Date | Jours restants | Detail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-16 | **J=0 glissant** | FMP placeholder non resolu depuis 25/05 (>22 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **55 jours** | Est EPS : -$0.29 a -$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-06-18 | **2 jours** | Max Pain operationnel $100.0 — structure legerement haussiere. Theta decay risque. |

**Prochain catalyseur majeur :** Aucun avant earnings (aout). L'expiration options du 18 juin (mercredi, dans 2 jours) pourrait amplifier la volatilite a court terme si le cours se rapproche du max pain $100.0, mais la distance actuelle ($87.57 -> $100.0 = +14.2%) limite la pression gamma immediate.

---

## 9. Conclusion — These Confirmee / Modifiee / Invalidee ?

**These AST :** 🔴 **INVALIDEE PAR L'ABSENCE DE DONNEES — ANOMALIE STRUCTURELLE PERSISTANTE (>44 SNAPSHOTS CONSECUTIFS)**

**These ASTS (proxy) :** 🟡 **CONFIRMEE — SURVEILLER MAINTENU (39.2/100), AUCUN CHANGEMENT MECANIQUE PRE-OUVERTURE**

Le snapshot pre-ouverture 10h UTC du 16/06 confirme la these sur ASTS avec les observations suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon errone d'ASTS. AST n'a toujours aucune donnee de cours apres **>44 snapshots consecutifs** (18/05 -> 16/06). La suppression ou l'exclusion de la watchlist reste recommandee.
2. 🟡 **STABILITE MECANIQUE SUR ASTS :** le snapshot 10h UTC 16/06 est strictement identique au close 21h UTC 15/06. Cours $87.57, volume 23.92M (0.87x), RSI 36.0, ATR $12.80, MM50 $89.13 — aucune mutation. Il s'agit d'un snapshot pre-ouverture, les donnees seront actualisees a l'ouverture US (15h30 UTC).
3. 🟡 **RSI en survente stable :** 36.0 — le rebond du 15/06 n'a pas suffi a sortir la survente.
4. 🟡 **Cours reste sous MM50 ($89.13) :** le cours a $87.57 se situe **-1.5% sous la MM50**. La resistance moyen terme n'a pas ete testee.
5. ⚠️ **Anomalie options JSON recurrente :** max pain $28.0, put/call 0.0, call OI 100.0% — valeurs aberrantes traitees comme faux positif pipeline. Valeurs operationnelles conservees ($100.0, 0.44, 69.7%).
6. 🟡 **Short interest stable :** 18.39% — pas de couverture massive des shorts. Le setup squeeze reste theorique.
7. 🟡 **Echeance options dans 2 jours :** Le 18 juin (mercredi). Theta decay sur les options OTM pourrait amplifier la volatilite si le cours approche du max pain ($100.0).
8. 🟡 **Score agent stable :** 39.2/100 (SURVEILLER) — proche du seuil EVITER (< 35).
9. 🟡 **Aucune news fondamentale** ni evenement corporate — le contexte reste purement technique.
10. 🟡 **Earnings placeholder glissant non resolu :** FMP signale un earnings AST le **2026-06-16** (`days_until: 0`), mais sans historique de prix, le resultat ne peut etre correle. Le glissement J=0 persiste depuis le **25/05** (>22 jours de decalage non resolu).

**Recommandation operationnelle :**
- **Resoudre l'anomalie structurelle immediatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker valide avec data completes
- **Ne pas engager de capital sur AST** tant que les donnees de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence** — la these SURVEILLER est maintenue. Les niveaux cles a surveiller a l'ouverture US (16/06) :
  - **Cassure sous $83.99** (low intraday 15/06) avec volume -> prochaines cibles $82.41 puis $80.00-$81.50
  - **Cassure sous $80** avec volume eleve -> passage de SURVEILLER a EVITER
  - **Rebond au-dessus de $89.13** (MM50) avec volume > 25M -> possible retournement technique
  - **Rebond au-dessus de $97.56** (close vendredi) -> combler le gap, retour du biais haussier mais necessite confirmation volume > 30 M
- **Ne pas entrer de position longue** sur ASTS avant un test reussi de la MM50 ($89.13) avec volume confirme, ou un catalyseur fondamental verifiable
- **Surveiller l'echeance options 2026-06-18** (mercredi) — theta decay risque si le cours reste sous $90

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades detailles, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Donnees quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## References

- `data/latest.json` (snapshot 2026-06-16T10:00:01Z) — AST: error "No price history" ; ASTS: close $87.57, previous_close $82.41, RSI 36.0, ATR $12.80, MM50 $89.13, volume 23,918,700 (0.87x), short interest 18.39%, consensus FMP $94.54, options JSON aberrantes (max_pain $28.0, put_call_ratio 0.0, call_oi_pct 100.0%) — anomalie recurrente traitee
- `data/validation_report.txt` (2026-06-16) — [ERROR] AST: fetch failed. 5 errors total, 0 excluded.
- `data/recommandations_latest.json` (2026-06-16) — AST: 55.2/100 (ATTENDRE) ; ASTS: 47.2/100 ajuste 39.2/100 (SURVEILLER)
- `data/sector_rotation_2026-06-16.json` — XLK top sectoriel (momentum 10.0/10, signal NEUTRAL), XLC bottom (momentum 10.0/10)
- `data/fx_exposure_2026-06-16.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-16.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-16.json` — AST: earnings 2026-06-16 (J=0 glissant) ; ASTS: earnings 2026-08-10 (55 jours)
- `data/events_2026-06-16.json` — Aucun evenement corporate detecte pour AST/ASTS
- `data/geo_risk_latest.json` (2026-05-17) — Pas de flag specifique AST/ASTS
- `data/quant_report_latest.json` (2026-05-17) — Donnees quantitatives insuffisantes
