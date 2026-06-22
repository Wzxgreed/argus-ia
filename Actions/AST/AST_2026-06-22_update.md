# AST — Mise à jour 2026-06-22

> **Source :** `data/latest.json` (snapshot 2026-06-22T10:00:01Z) | `data/recommandations_latest.json` | `data/validation_report.txt`
> **Référence précédente :** [AST_2026-06-17_update.md](AST_2026-06-17_update.md) (snapshot 10h UTC 17/06)
> **Contexte :** Snapshot pré-ouverture US du 22/06. Données établies pour ASTS. AST reste sans données.

---

## 1. Résumé des Changements depuis le Snapshot Précédent (10h UTC 17/06)

| Métrique | Snapshot 10h (17/06) | Snapshot 10h (22/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirmé stable — >50 snapshots consécutifs** |
| **ASTS — Cours close** | **$82.25** | **$80.66** | **-1.93%** — poursuite de la baisse |
| **ASTS — Previous close** | $87.57 | **$85.43** | **-2.44%** (nouveau référence) |
| **ASTS — Variation vs previous** | -6.08% | **-5.58%** | **+0.50 pt** — légère amélioration mécanique |
| **ASTS — RSI 14j** | 28.51 | **32.75** | **+4.24 pts** — sortie de survente extrême (<30) |
| **ASTS — ATR 14j** | $12.40 | **$10.66** | **-14.0%** — volatilité en contraction |
| **ASTS — MM 50j** | $88.88 | **$88.42** | **-0.52%** — légère décroissance |
| **ASTS — Distance MM50** | -7.4% | **-8.8%** | **écart élargi** — cours s'éloigne de la MM50 |
| **ASTS — Volume séance** | 20.04M (0.73x) | **31.68M (1.12x)** | **+58.1% / volume au-dessus de la moyenne 20j** |
| **ASTS — Short Interest** | 18.39% | **18.39%** | = — stable |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = |
| **ASTS — Premium vs consensus** | -13.0% | **-14.7%** | **dégradation -1.7 pt** |
| **ASTS — Options Max Pain (JSON)** | $18.0 (aberrant) | **$45.0 (JSON)** | **🟡 ANOMALIE JSON PERSISTANTE** |
| **ASTS — Options Put/Call (JSON)** | null | **null** | **🟡 ANOMALIE JSON PERSISTANTE** |
| **ASTS — Options Call OI % (JSON)** | null | **null** | **🟡 ANOMALIE JSON PERSISTANTE** |
| **ASTS — Échéance options** | 2026-06-18 (1j) | **2026-06-26 (4j)** | **Nouvelle expiration** |
| **Score Global ASTS** | 43.0/100 (SURVEILLER) | **39.2/100 (SURVEILLER)** | **-3.8 pts** — approche seuil ÉVITER |
| **Score Opportunité ASTS** | 4.6/10 | **4.7/10** | **+0.1 pt** — stable |

**Verdict :** Le snapshot 10h UTC du 22/06 enregistre une **détérioration mécanique persistante** sur ASTS. Le cours recule de **-5.58%** à **$80.66** vs previous close $85.43, mais le **volume franchit la barre de la moyenne 20j à 1.12x** (31.68M vs 28.35M moy. 20j) — premier signal de distribution/capitulation notable depuis plusieurs sessions. Le RSI remonte marginalement à **32.75** (sortie de la zone de survente extrême <30), mais reste en territoire de survente. L'écart à la MM50 s'est élargi à **-8.8%** ($80.66 vs $88.42). **Anomalie options JSON PERSISTANTE** : max pain JSON $45.0 aberrant, put/call et call OI passés à null — faux positif pipeline confirmé. L'échéance options du 26/06 est dans **4 jours**. Le scoring agent dégrade ASTS à **39.2/100 (SURVEILLER)** — proche du seuil ÉVITER (< 35).

---

## 2. Mise à jour Technique

### AST (données officielles)

| Indicateur | Valeur Snapshot 10h | Valeur précédente (10h 17/06) | Δ |
|-----------|---------------------|------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur **>50 snapshots consécutifs** (18/05 -> 22/06).

### ASTS (proxy — données 10h UTC 22/06)

| Indicateur | Valeur Snapshot 10h | Valeur Snapshot 10h 17/06 | Δ |
|-----------|-------------------|-------------------|---|
| Cours close | **$80.66** | $82.25 | **-1.93%** |
| Previous close | **$85.43** | $87.57 | **-2.44%** |
| RSI 14j | **32.75** | 28.51 | **+4.24 pts** — sortie survente extrême |
| ATR 14j | **$10.66** | $12.40 | **-14.0%** — volatilité en contraction |
| MM50 | **$88.42** | $88.88 | **-0.52%** |
| Distance MM50 | **-8.8%** | -7.4% | **écart élargi** |
| Volume séance | **31.68M** | 20.04M | **+58.1%** — volume > moyenne |
| Volume relatif | **1.12x** | 0.73x | **au-dessus moyenne** |
| Short interest | **18.39%** | 18.39% | = — stable |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 36.08 | 36.08 | = |

**Verdict timing ASTS :** 🔴 **DÉTÉRIORATION MÉCANIQUE PERSISTANTE — VOLUME DE CAPITULATION ?**

- **RSI 32.75** : sortie de la survente extrême (<30) mais reste en zone de survente prononcée. Le rebond technique attendu n'a pas eu lieu malgré la sortie de l'extrême.
- **Volume 1.12x** : **31.68M vs moyenne 20j 28.35M** — première fois au-dessus de la moyenne depuis le gap down du 15/06 (54.91M, 2.0x). Ce volume élevé sur baisse de -5.58% peut signaler une distribution accélérée ou une capitulation partielle.
- **Cours sous MM50 ($88.42)** : le cours à $80.66 se situe désormais **-8.8% sous la MM50**. L'écart s'est élargi, confirmant la rupture de la tendance moyen terme.
- **ATR $10.66** : contraction de la volatilité (-14.0%) — le range journalier se rétrécit malgré le volume, ce qui peut précéder une accélération.
- **Short interest stable à 18.39%** : pas de couverture massive des shorts détectée. Le setup squeeze reste théorique.

**Niveaux clés** (actualisés avec snapshot 10h UTC 22/06) :
- Support immédiat : **$77.12** (low intraday 22/06 — testé mais non cassé)
- Support : **$76-78** (zone de confluence + 1.5xATR, test du 15/06)
- Support critique : **$72-74** (2xATR sous close)
- Résistance immédiate : **$85.30** (open 22/06)
- Résistance : **$85.43** (previous close / gap à combler)
- Résistance majeure : **$88.42** (MM50 — test de retour comme résistance)
- Objectif haussier : **$112.64** (spot + 3xATR $10.66)

**Structure options** (anomalie JSON PERSISTANTE — valeurs opérationnelles conservées) :
- **Max Pain JSON** : **$45.0** — valeur aberrante, **non opérationnelle**. Valeur opérationnelle estimée **$100.0** (cohérente avec historique).
- **Put/Call ratio JSON** : **null** — aberrant. Valeur opérationnelle estimée **~0.45** (cohérente avec historique).
- **Call OI % JSON** : **null** — aberrant. Valeur opérationnelle estimée **~69%** (cohérente avec historique).
- Expiration proche : **2026-06-26** (4 jours) — theta decay à surveiller.

> **Note options :** L'anomalie JSON persistante sur ASTS est **de retour** dans le snapshot 10h UTC du 22/06. Les valeurs natives (max pain $45.0, put/call null, call OI null) sont aberrantes. Il s'agit d'un **faux positif pipeline confirmé** — les valeurs opérationnelles ($100.0, 0.45, 69%) restent les références. Le max pain $100.0 est éloigné du cours actuel ($80.66 -> $100.0 = +24.0%), ce qui limite la pression gamma immédiate. L'expiration dans 4 jours (26/06) pourrait amplifier la volatilité si le cours se rapproche du max pain, mais la distance rend ce scénario peu probable.

---

## 3. Mise à jour Fondamentale

### AST (données officielles)

| Métrique | Valeur Snapshot 10h | Valeur précédente | Δ |
|---------|---------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur Snapshot 10h | Valeur Snapshot 10h 17/06 | Δ |
|---------|---------------------|-----------------------|---|
| Market cap Yahoo | **$31.06 B** | $31.92 B | **-2.7%** (mécanique, lié au cours) |
| Forward P/E | **-393.08** | -400.83 | **=** (placeholder, convergence mécanique) |
| EV/Revenue | **290.1x** | 295.7x | **-1.9%** |
| EV/EBITDA | **-77.88** | -79.38 | **=** |
| Beta | **2.634** | 2.634 | = |
| Short interest | **18.39%** | 18.39% | = |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **-14.7%** | -13.0% | **dégradation -1.7 pt** |
| Price to book | **11.58** | 11.81 | **-1.9%** |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement spéculative (EV/Revenue ~290.1x selon FMP, forward P/E -393.08). **Aucune révision sell-side** n'a été enregistrée (consensus $94.54, 12 analysts inchangé). Le premium vs consensus se dégrade mécaniquement à **-14.7%** suite à la baisse de cours. Les multiples extrêmement élevés confirment le caractère spéculatif du titre. Aucun changement fondamental n'est à signaler entre le snapshot 10h du 17/06 et le snapshot 10h du 22/06.

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($31.06 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Écart de **+22.9%** stable.

---

## 4. Mise à jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 10h 17/06 |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain (JSON)** | $45.0 (aberrant) | **ANOMALIE PERSISTANTE** — valeur opérationnelle $100.0 conservée |
| **Put/Call ratio (JSON)** | null (aberrant) | **ANOMALIE PERSISTANTE** — valeur opérationnelle ~0.45 conservée |
| **Call OI % (JSON)** | null (aberrant) | **ANOMALIE PERSISTANTE** — valeur opérationnelle ~69% conservée |
| **Short Interest** | 18.39% | = — stable |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options** — Anomalie JSON **PERSISTANTE**. Valeurs JSON aberrantes (max pain $45.0, put/call null, call OI null). Valeurs opérationnelles estimées $100.0 / 0.45 / 69.0% conservées.
- **Short interest stable** (18.39%) — pas de couverture massive des shorts. Le setup squeeze reste théorique.
- **Aucun upgrade/downgrade**, absence totale d'activité institutionnelle/retail.
- **Aucun insider trade** significatif signalé.

**Verdict Sentiment :** Neutre-Baissier — L'absence de news et d'activité institutionnelle persiste. La structure options légèrement haussière (opérationnelle) ne suffit pas à contrebalancer la survente technique et la détérioration du cours. Le sentiment dominant reste technique et s'oriente à la baisse malgré la sortie de la survente extrême. Aucun catalyseur fondamental n'est visible.

---

## 5. Mise à jour Agents Spécialisés

| Agent | Donnée AST/ASTS | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques. | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique AST/ASTS. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLK (Technology) momentum score **10.0/10**, signal **NEUTRAL**. XLC (Communication Services) **bottom3**, momentum **0.0/10**. | 🟡 **Malus sectoriel** — ASTS est classé Technology mais proche de Communication Services (bottom3). |
| **FX Exposure** | Score FX Impact **0.0**, flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | AST : earnings signalé **2026-06-22** (FMP) — placeholder glissant J=0 non résolu depuis 25/05 (>28 jours). ASTS : earnings **2026-08-10** (49 jours). | Trop loin pour pricer. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **Validation Report** | [ERROR] AST — fetch failed. 5 errors total. | AST en erreur connue. |

---

## 6. Scoring Global Révisé

### AST (données officielles — placeholder)

| Axe | Score Snapshot 10h | Pondération | Note |
|-----|-------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35% | [NON FONDÉ] — aucun catalyseur vérifiable |
| Valorisation | 5.0/10 (placeholder) | 40% | [NON FONDÉ] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25% | [NON FONDÉ] — pas de cours, pas de momentum |
| **Score Opportunité** | **5.5/10** | — | Placeholder — **non utilisable pour décision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |
| **Score Global Ajusté** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, à titre indicatif uniquement)

| Axe | Score Snapshot 10h | Pondération | Note |
|-----|-------------------|-------------|------|
| Catalyseur | 6.0/10 | 35% | Aucun catalyseur court terme. Earnings 10/08 distant. |
| Valorisation | 5.0/10 | 40% | EV/Revenue ~290.1x, forward P/E -393.08 — reste spéculatif. Divergence consensus -14.7%. |
| Momentum | 2.5/10 | 25% | RSI 32.75 (survente), baisse -5.58% vs previous, cours sous MM50 -8.8%, volume 1.12x. |
| **Score Opportunité** | **4.7/10** | — | **Non qualifié pour position** (score < 6) |
| **Score Global** | **47.2/100** | — | **SURVEILLER** |
| **Score Global Ajusté** | **39.2/100** | — | **SURVEILLER** (proche seuil ÉVITER < 35) |

**Action recommandée :** SURVEILLER (détérioration)
**Timing :** Défavorable (survente, sous MM50, volume de capitulation)
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. Le scoring **39.2/100 (SURVEILLER)** reflète une situation technique dégradée et proche du seuil ÉVITER. Le score Opportunité (4.7/10) reste sous le seuil de qualification (6.0/10), et la position sous MM50 ($88.42) de -8.8% maintient le biais prudent. Le volume de 1.12x sur baisse est un signal mitigé — possible capitulation ou distribution accélérée.

---

## 7. Révision des Niveaux SL / TP

### AST (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours - 2xATR -> [NON CALCULABLE]
- Take-profit suggéré = cours + 3xATR -> [NON CALCULABLE]

### ASTS (proxy — actualisés avec snapshot 10h UTC 22/06)

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $80.66 (close 10h 22/06) | Snapshot pré-ouverture US |
| **Stop-loss** | $59.34 (-26.4%) | 2xATR ($10.66) |
| **Take-profit** | $112.64 (+39.6%) | 3xATR ($10.66) |
| **Ratio R/R** | **1.5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Zone d'intérêt potentielle :** La baisse de -5.58% sur volume supérieur à la moyenne (1.12x) est un signal de distribution ou de capitulation. La sortie de la survente extrême (RSI 28.51 -> 32.75) n'a pas généré de rebond. Un test de la **MM50 $88.42** avec volume > 30M serait la première condition d'amélioration technique crédible. En l'absence de franchissement, le biais baissier moyen terme se maintient. Une **cassure sous $77.12** (low intraday 22/06) avec volume confirmerait la reprise de la distribution et ouvrirait la voie vers **$72-74**. Une **cassure sous $72** avec volume élevé justifierait un passage de SURVEILLER à **ÉVITER**.

> **Note :** Les niveaux SL/TP sont actualisés avec le nouveau close $80.66. Le ratio R/R reste à 1.5:1, inférieur au seuil institutionnel de 2:1.

---

## 8. Calendrier & Événements à Venir

| Événement | Ticker | Date | Jours restants | Détail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-22 | **J=0 glissant** | FMP placeholder non résolu depuis 25/05 (>28 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **49 jours** | Est EPS : -$0.29 à -$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-06-26 | **4 jours** | Max Pain opérationnel $100.0 — anomalie JSON persistante. Theta decay à surveiller. |

**Prochain catalyseur majeur :** Aucun avant earnings (août). L'expiration options du 26 juin (dans 4 jours) pourrait amplifier la volatilité à court terme si le cours se rapproche du max pain $100.0, mais la distance actuelle ($80.66 -> $100.0 = +24.0%) limite la pression gamma immédiate.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>50 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🔴 **CONFIRMÉE — DÉTÉRIORATION MÉCANIQUE, BIAIS SURVEILLER RENFORCÉ (39.2/100, PROCHE ÉVITER)**

Le snapshot 10h UTC du 22/06 confirme et renforce la thèse SURVEILLER sur ASTS avec les observations suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS. AST n'a toujours aucune donnée de cours après **>50 snapshots consécutifs** (18/05 -> 22/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. 🔴 **DÉTÉRIORATION MÉCANIQUE SUR ASTS :** le cours recule de **-5.58%** à **$80.66** sur **volume de capitulation à 1.12x** (31.68M vs 28.35M moy. 20j). C'est la première fois que le volume dépasse la moyenne depuis le gap down du 15/06.
3. 🟡 **RSI sort de la survente extrême :** 32.75 vs 28.51 — le titre quitte la zone de survente extrême (< 30) mais reste en survente. Aucun rebond technique n'est visible.
4. 🔴 **Cours s'éloigne de la MM50 ($88.42) :** le cours à $80.66 se situe désormais **-8.8% sous la MM50**. L'écart s'est élargi, confirmant la rupture de la tendance moyen terme.
5. 🟡 **Anomalie options JSON PERSISTANTE :** max pain JSON $45.0 aberrant (opérationnel $100.0), put/call null, call OI null — faux positif pipeline confirmé. Valeurs opérationnelles conservées.
6. 🟡 **Short interest stable :** 18.39% — pas de couverture massive des shorts. Le setup squeeze reste théorique.
7. ⚠️ **Échéance options dans 4 jours :** Le 26 juin. Theta decay à surveiller sur les options OTM.
8. 🔴 **Score agent dégradé :** 39.2/100 (SURVEILLER) — proche du seuil ÉVITER (< 35). Le score Opportunité (4.7/10) reste sous le seuil de qualification.
9. 🟡 **Aucune news fondamentale** ni événement corporate — le contexte reste purement technique.
10. 🟡 **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-22** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé. Le glissement J=0 persiste depuis le **25/05** (>28 jours de décalage non résolu).
11. 🟡 **Malus sectoriel** — XLC (Communication Services) bottom3 sectoriel avec momentum 0.0/10. ASTS est classé Technology mais proche de Communication Services.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker valide avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence** — la thèse SURVEILLER est renforcée. Les niveaux clés à surveiller :
  - **Cassure sous $77.12** (low intraday 22/06) avec volume -> prochaines cibles $72-74
  - **Cassure sous $72** avec volume élevé -> passage de SURVEILLER à ÉVITER
  - **Rebond au-dessus de $85.30** (open 22/06) avec volume > 25M -> possible stabilisation
  - **Rebond au-dessus de $88.42** (MM50) avec volume > 30M -> possible retournement technique
  - **Rebond au-dessus de $97.56** (close vendredi 12/06) -> combler le gap, retour du biais haussier mais nécessite confirmation volume > 30M
- **Ne pas entrer de position longue** sur ASTS avant un test réussi de la MM50 ($88.42) avec volume confirmé, ou un catalyseur fondamental vérifiable
- **Surveiller l'échéance options 2026-06-26** — theta decay risque si le cours reste sous $85

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références

- `data/latest.json` (snapshot 2026-06-22T10:00:01Z) — AST: error "No price history" ; ASTS: close $80.66, previous_close $85.43, RSI 32.75, ATR $10.66, MM50 $88.42, volume 31,679,200 (1.12x), short interest 18.39%, consensus FMP $94.54, options JSON aberrantes (max_pain $45.0, put_call_ratio null, call_oi_pct null)
- `data/validation_report.txt` (2026-06-22) — [ERROR] AST: fetch failed. 5 errors total, 0 excluded.
- `data/recommandations_latest.json` (2026-06-22) — AST: 55.2/100 (ATTENDRE) ; ASTS: 47.2/100 ajusté 39.2/100 (SURVEILLER)
- `data/sector_rotation_2026-06-22.json` — XLK top sectoriel (momentum 10.0/10, signal NEUTRAL), XLC bottom (momentum 0.0/10)
- `data/fx_exposure_2026-06-22.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-22.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-22.json` — AST: earnings 2026-06-22 (J=0 glissant) ; ASTS: earnings 2026-08-10 (49 jours)
- `data/events_2026-06-22.json` — Aucun événement corporate détecté pour AST/ASTS
- `data/geo_risk_latest.json` (2026-05-17) — Pas de flag spécifique AST/ASTS
- `data/quant_report_latest.json` (2026-05-17) — Données quantitatives insuffisantes
