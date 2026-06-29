# AST — Mise à jour 2026-06-29

> **Source :** `data/2026-06-29.json` (snapshot 2026-06-29T10:00:14Z) | `data/recommandations_latest.json` | `data/validation_report.txt`
> **Référence précédente :** [AST_2026-06-23_update_17h.md](AST_2026-06-23_update_17h.md) (snapshot 17h UTC 23/06)
> **Contexte :** AST reste sans données. ASTS proxy — données complètes.

---

## 1. Résumé des Changements depuis l'Analyse Précédente (17h UTC 23/06)

| Métrique | Snapshot 17h (23/06) | Snapshot 10h (29/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirme stable — >58 snapshots consécutifs** |
| **ASTS — Cours close** | **$76.15** | **$71.45** | **-6.17%** (gap down inter-sessions $76.15 → previous close $65.62) |
| **ASTS — Previous close** | $73.19 | **$65.62** | = (nouvelle référence post-gap) |
| **ASTS — Variation vs previous** | +4.04% | **+8.88%** | Rebond mécanique vs gap down |
| **ASTS — RSI 14j** | 25.31 | **34.39** | **+9.08 pts** — sortie de survente extrême |
| **ASTS — ATR 14j** | $9.87 | **$8.50** | **-13.9%** — contraction volatilité |
| **ASTS — MM 50j** | $87.68 | **$86.23** | **-1.65%** — légère baisse mécanique |
| **ASTS — Distance MM50** | -13.2% | **-17.1%** | **Détérioration** (gap down amplifié) |
| **ASTS — Volume séance** | 12.10M (0.44x) | **22.16M (0.85x)** | **Recovery volumétrique** (+83% vs 23/06, normalisation) |
| **ASTS — Short Interest** | 18.39% | **20.98%** | **+2.59 pts** — hausse significative |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = — inchangé |
| **ASTS — Premium vs consensus** | -19.5% | **-24.4%** | **Dégradation mécanique** (cours plus bas) |
| **ASTS — Options Max Pain** | $100.0 (cohérent) | **$45.0 (ABERRANT)** | 🟡 **NOUVELLE ANOMALIE JSON** |
| **ASTS — Options Put/Call** | 0.69 | **null** | 🟡 Anomalie JSON (null) |
| **ASTS — Options Call OI %** | 59.3% | **null** | 🟡 Anomalie JSON (null) |
| **ASTS — Échéance options** | 2026-06-26 | **2026-07-02** | Nouvelle échéance |
| **Score Global ASTS (agent)** | 43.0/100 (SURVEILLER) | **46.8/100 (SURVEILLER)** | **+3.8 pts** — mécanique |
| **Score Opportunité ASTS** | 5.1/10 | **5.5/10** | +0.4 pt (mécanique) |

**Verdict :** Le snapshot du 29/06 enregistre un **gap down inter-sessions** ($76.15 → $65.62) suivi d'un **rebond intraday de +8.88%** à $71.45. Le RSI remonte de 25.31 à **34.39** (sortie de la survente extrême <30), tandis que l'ATR se contracte à **$8.50** (-13.9%). Le volume se normalise à **0.85x** (22.16M vs moyenne 20j 26.04M), signalant un retour d'intérêt. Le **short interest grimpe à 20.98%** (+2.59 pts), renforçant le setup squeeze théorique mais confirmant aussi la pression vendeuse. Une **nouvelle anomalie JSON** apparaît sur les options (max pain $45.0 aberrant, put/call et call OI nulls). Le score agent remonte mécaniquement à **46.8/100 (SURVEILLER)**.

---

## 2. Mise à jour Technique

### AST (données officielles)

| Indicateur | Valeur Snapshot 29/06 | Valeur précédente (17h 23/06) | Δ |
|-----------|----------------------|------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur **>58 snapshots consécutifs** (18/05 → 29/06).

### ASTS (proxy — données 10h UTC 29/06)

| Indicateur | Valeur Snapshot 29/06 | Valeur Snapshot 17h 23/06 | Δ |
|-----------|----------------------|--------------------------|---|
| Cours close | **$71.45** | $76.15 | **-6.17%** (gap down inter-sessions) |
| Previous close | **$65.62** | $73.19 | = (nouvelle référence) |
| Variation vs previous | **+8.88%** | +4.04% | Rebond amplifié vs gap |
| RSI 14j | **34.39** | 25.31 | **+9.08 pts** — sortie survente extrême |
| ATR 14j | **$8.50** | $9.87 | **-13.9%** — contraction volatilité |
| MM50 | **$86.23** | $87.68 | **-1.65%** |
| Distance MM50 | **-17.1%** | -13.2% | **Détérioration** (gap down) |
| Volume séance | **22.16M** | 12.10M | **+83.1%** — recovery |
| Volume relatif | **0.85x** | 0.44x | **Normalisation** |
| Short interest | **20.98%** | 18.39% | **+2.59 pts** — hausse significative |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 36.08 | 36.08 | = |

**Verdict timing ASTS :** 🟡 **REBOND POST-GAP — SURVEILLER MAINTENU**

- **RSI 34.39** : sortie de la zone de survente extrême (<30) mais reste en survente modérée. L'amélioration de +9.08 pts est mécanique (gap down suivi de rebond) et non un signal de momentum haussier structurel.
- **Volume 0.85x** : **22.16M vs moyenne 20j 26.04M** — recovery significative vs le collapse 0.44x du 23/06. Le rebond de +8.88% s'accompagne d'un volume crédible, contrairement au rebond précédent. Cela suggère un intérêt acheteur réel, potentiellement lié au short interest élevé.
- **Cours sous MM50 ($86.23)** : le cours à $71.45 se situe **-17.1% sous la MM50**. La rupture de tendance moyen terme s'est aggravée par le gap down inter-sessions.
- **ATR $8.50** : contraction de -13.9%, indiquant une compression de la volatilité malgré le rebond. Un ATR réduit diminue la marge de manœuvre pour les stops.
- **Short interest 20.98%** : hausse de +2.59 pts vs 23/06. Ce niveau élevé renforce le setup squeeze théorique mais confirme aussi que la pression vendeuse reste importante.
- **Low intraday $64.51** (high $73.20, open $64.675) : le cours a ouvert à $64.675, pratiquement au plus bas, puis rebondi à $71.45. La fourchette intraday ($8.69) est large (1.02xATR), signe d'une volatilité intraday élevée.

**Niveaux clés** (actualisés avec snapshot 29/06) :
- Support immédiat : **$64.51** (low intraday 29/06 — nouveau plancher)
- Support : **$63.00–$65.00** (zone psychologique post-gap)
- Support critique : **$60.00–$62.00** (2xATR sous close $71.45 → $54.45 est le SL)
- Résistance immédiate : **$73.20** (high intraday 29/06)
- Résistance : **$76.15** (close 23/06 — gap à combler)
- Résistance majeure : **$86.23** (MM50 — test de retour comme résistance)
- Objectif haussier : **$96.95** (spot + 3xATR $8.50)

**Structure options** (anomalie JSON détectée) :
- **Max Pain JSON** : **$45.0** — 🟡 **ABERRANT** (vs $100.0 opérationnel historique). Faux positif pipeline.
- **Put/Call ratio JSON** : **null** — 🟡 Anomalie.
- **Call OI % JSON** : **null** — 🟡 Anomalie.
- **Expiration proche** : **2026-07-02** (3 jours) — theta decay imminent sur options OTM.

> **Note options :** La nouvelle anomalie JSON (max pain $45.0, put/call null, call OI null) est un faux positif pipeline. Les valeurs historiques cohérentes ($100.0, put/call ~0.7, call OI ~59%) restent la référence opérationnelle jusqu'à correction. L'échéance 2026-07-02 est dans 3 jours.

---

## 3. Mise à jour Fondamentale

### AST (données officielles)

| Métrique | Valeur Snapshot 29/06 | Valeur précédente | Δ |
|---------|----------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur Snapshot 29/06 | Valeur Snapshot 17h 23/06 | Δ |
|---------|----------------------|-----------------------|---|
| Market cap Yahoo | **$27.73 B** | $29.56 B | **-6.2%** (mécanique) |
| Forward P/E | **-348.20** | -371.10 | = (placeholder) |
| EV/Revenue | **257.7x** | 263.8x | = (stable) |
| EV/EBITDA | **-69.18** | -70.83 | = (stable) |
| Beta | **2.634** | 2.634 | = |
| Short interest | **20.98%** | 18.39% | **+2.59 pts** |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **-24.4%** | -19.5% | **Dégradation mécanique** |
| Price to book | **10.26** | 10.93 | **-6.1%** (mécanique) |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement spéculative (EV/Revenue ~257.7x, forward P/E -348.20). **Aucune révision sell-side** n'a été enregistrée (consensus $94.54, 12 analysts inchangé). Le premium vs consensus se dégrade mécaniquement à **-24.4%** suite au gap down. Les multiples extrêmement élevés confirment le caractère spéculatif du titre. Aucun changement fondamental n'est à signaler entre le snapshot 23/06 et le 29/06.

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($27.73 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Écart de **+9.5%** (mécanique).

---

## 4. Mise à jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 17h 23/06 |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain JSON** | $45.0 (ABERRANT) | 🟡 Nouvelle anomalie |
| **Put/Call ratio JSON** | null (anomalie) | 🟡 Nouvelle anomalie |
| **Call OI % JSON** | null (anomalie) | 🟡 Nouvelle anomalie |
| **Short Interest** | 20.98% | **+2.59 pts** — hausse significative |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options** — 🟡 **NOUVELLE ANOMALIE JSON** : max pain $45.0 aberrant, put/call null, call OI null. Valeurs historiques cohérentes ($100.0, ~0.7, ~59%) à utiliser.
- **Short interest en hausse** (20.98%) : +2.59 pts. Renforce le setup squeeze théorique mais confirme la pression vendeuse.
- **Aucun upgrade/downgrade**, absence totale d'activité institutionnelle/retail.
- **Aucun insider trade** significatif signalé.

**Verdict Sentiment :** Neutre-Baissier — L'absence de news et d'activité institutionnelle persiste. Le rebond de +8.88% sur volume 0.85x est plus crédible que le rebond précédent (+4% sur 0.44x), mais le contexte fondamental reste vide. La hausse du short interest à 20.98% crée un potentiel squeeze théorique si un catalyseur émerge, mais sans catalyseur ce n'est qu'un setup. Le sentiment dominant reste technique et mixte.

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
| **Upcoming Events** | AST : earnings signalé **2026-06-29** (FMP) — placeholder glissant J=0 non résolu depuis 25/05 (>35 jours). ASTS : earnings **2026-08-10** (42 jours). | Trop loin pour pricer. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **Validation Report** | [ERROR] AST — fetch failed. | AST en erreur connue. |

---

## 6. Scoring Global Révisé

### AST (données officielles — placeholder)

| Axe | Score Snapshot 29/06 | Pondération | Note |
|-----|---------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35% | [NON FONDÉ] — aucun catalyseur vérifiable |
| Valorisation | 5.0/10 (placeholder) | 40% | [NON FONDÉ] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25% | [NON FONDÉ] — pas de cours, pas de momentum |
| **Score Opportunité** | **5.5/10** | — | Placeholder — **non utilisable pour décision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |
| **Score Global Ajusté** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, à titre indicatif uniquement)

| Axe | Score Snapshot 29/06 | Pondération | Note |
|-----|---------------------|-------------|------|
| Catalyseur | 6.5/10 | 35% | Aucun catalyseur court terme. Earnings 10/08 distant. Short interest élevé = setup squeeze théorique. |
| Valorisation | 5.5/10 | 40% | EV/Revenue ~257.7x, forward P/E -348.20 — reste spéculatif. Divergence consensus -24.4%. |
| Momentum | 4.0/10 | 25% | RSI 34.39 (sortie survente extrême), rebond +8.88% sur volume 0.85x, cours sous MM50 -17.1%. |
| **Score Opportunité** | **5.5/10** | — | **Non qualifié pour position** (score < 6) |
| **Score Global** | **54.8/100** | — | **SURVEILLER** |
| **Score Global Ajusté** | **46.8/100** | — | **SURVEILLER** (proche seuil ÉVITER < 35) |

**Action recommandée :** SURVEILLER (stable)
**Timing :** Défavorable (sous MM50, gap down non comblé, rebond non confirmé)
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. Le scoring **46.8/100 (SURVEILLER)** reflète une situation technique encore dégradée malgré le rebond. Le score Opportunité (5.5/10) reste sous le seuil de qualification (6.0/10). Le rebond de +8.88% sur volume 0.85x est plus crédible que le précédent (+4% sur 0.44x) mais reste un rebond post-gap sans catalyseur fondamental.

---

## 7. Révision des Niveaux SL / TP

### AST (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours - 2xATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3xATR → [NON CALCULABLE]

### ASTS (proxy — actualisés avec snapshot 29/06)

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $71.45 (close 29/06) | Rebond +8.88% vs previous close $65.62 |
| **Stop-loss** | $54.45 (-23.8%) | 2xATR ($8.50) |
| **Take-profit** | $96.95 (+35.7%) | 3xATR ($8.50) |
| **Ratio R/R** | **1.5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Zone d'intérêt potentielle :** Le rebond technique de +8.88% sur volume normalisé (0.85x) est plus crédible que le rebond précédent (+4% sur volume collapse 0.44x). Cependant, il s'agit d'un rebond post-gap down ($76.15 → $65.62 inter-sessions) et le cours à $71.45 n'a comblé qu'en partie le gap. La **MM50 $86.23** reste une résistance majeure lointaine (-17.1%). Le short interest à **20.98%** renforce le setup squeeze théorique. Une **cassure sous $64.51** (low intraday 29/06) avec volume > 20M justifierait un passage de SURVEILLER à **ÉVITER**. Un **franchissement de $76.15** (close 23/06 / haut du gap) avec volume > 25M serait le premier signal technique positif crédible. Un **test réussi de la MM50 $86.23** avec volume > 26M serait nécessaire pour envisager un retournement de tendance.

> **Note :** Les niveaux SL/TP sont révisés avec le close $71.45 et l'ATR $8.50. Le ratio R/R reste à 1.5:1, inférieur au seuil institutionnel de 2:1. L'ATR contracté réduit la distance SL/TP.

---

## 8. Calendrier & Événements à Venir

| Événement | Ticker | Date | Jours restants | Détail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-29 | **J=0 glissant** | FMP placeholder non résolu depuis 25/05 (>35 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **42 jours** | Est EPS : -$0.29 à -$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-07-02 | **3 jours** | Anomalie JSON (max pain $45.0 aberrant). Theta decay à surveiller. |

**Prochain catalyseur majeur :** Aucun avant earnings (août). L'expiration options du 02 juillet (dans 3 jours) pourrait amplifier la volatilité à court terme. Le max pain aberrant ($45.0) est un faux positif ; la valeur historique cohérente ($100.0) reste la référence opérationnelle. Le short interest élevé (20.98%) crée un potentiel squeeze si un catalyseur inattendu émergeait avant l'échéance.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>58 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **MODIFIÉE — REBOND POST-GAP PLUS CRÉDIBLE, BIAIS SURVEILLER MAINTENU (46.8/100)**

Le snapshot du 29/06 modifie légèrement la thèse SURVEILLER sur ASTS avec les observations suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS. AST n'a toujours aucune donnée de cours après **>58 snapshots consécutifs** (18/05 → 29/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. 🟡 **GAP DOWN INTER-SESSIONS SUIVI DE REBOND +8.88% :** le cours a ouvert à $64.675 (gap down vs $76.15 close 23/06) puis rebondi à **$71.45** (+8.88% vs previous close $65.62). Le rebond s'accompagne d'un **volume normalisé à 0.85x** (22.16M), nettement plus crédible que le rebond du 23/06 (+4% sur 0.44x).
3. 🟢 **SORTIE DE SURVENTE EXTRÊME :** RSI **34.39** (vs 25.31 à 17h 23/06). Le titre sort de la zone de survente extrême (<30), ce qui est un signal technique positif à court terme.
4. 🔴 **DISTANCE MM50 AGGRAVÉE :** le cours à $71.45 se situe **-17.1% sous la MM50** ($86.23) vs -13.2% précédemment. Le gap down a aggravé la rupture de tendance moyen terme.
5. 🟡 **Short interest en hausse :** 20.98% (+2.59 pts) — renforce le setup squeeze théorique mais confirme la pression vendeuse.
6. 🟡 **ATR contracté :** $8.50 (-13.9%) — compression de la volatilité qui réduit la marge de manœuvre pour les stops et les objectifs.
7. 🟡 **Score agent remonte à 46.8/100 (SURVEILLER)** — +3.8 pts mécaniques, reste proche du seuil ÉVITER (< 35 est éloigné mais le score est faible). Le score Opportunité (5.5/10) reste sous le seuil de qualification.
8. 🟡 **Nouvelle anomalie JSON options :** max pain $45.0 aberrant, put/call null, call OI null. Faux positif pipeline à ignorer ; référence opérationnelle $100.0.
9. 🟡 **Aucune news fondamentale** ni événement corporate — le contexte reste purement technique.
10. 🟡 **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-29** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé. Le glissement J=0 persiste depuis le **25/05** (>35 jours de décalage non résolu).
11. 🟡 **Malus sectoriel** — XLC (Communication Services) bottom3 sectoriel avec momentum 0.0/10. ASTS est classé Technology mais proche de Communication Equipment.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker valide avec données complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence** — la thèse SURVEILLER est confirmée malgré le rebond plus crédible. Les niveaux clés à surveiller :
  - **Cassure sous $64.51** (low intraday 29/06) avec volume > 20M → prochaines cibles $60–62
  - **Cassure sous $60** avec volume élevé → passage de SURVEILLER à ÉVITER
  - **Rebond au-dessus de $76.15** (close 23/06 / haut du gap) avec volume > 25M → possible stabilisation
  - **Rebond au-dessus de $86.23** (MM50) avec volume > 26M → possible retournement technique
  - **Rebond au-dessus de $97.56** (close vendredi 12/06) → combler le gap, retour du biais haussier mais nécessite confirmation volume > 26M
- **Ne pas entrer de position longue** sur ASTS avant un test réussi de la MM50 ($86.23) avec volume confirmé, ou un catalyseur fondamental vérifiable
- **Surveiller l'échéance options 2026-07-02** — theta decay risqué si le cours reste sous $80
- **Attention au faux signal haussier** : le rebond +8.88% est plus crédible que le précédent mais reste un rebond post-gap sans catalyseur. Attendre la confirmation sur 2–3 sessions (volume > 20M, close > $73.20) avant toute interprétation haussière.
- **Monitorer le short interest** : si la hausse se poursuit au-delà de 25%, le setup squeeze devient plus pertinent mais nécessite un catalyseur déclencheur.

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références

- `data/2026-06-29.json` (snapshot 2026-06-29T10:00:14Z) — AST: error "No price history" ; ASTS: close $71.45, previous_close $65.62, RSI 34.39, ATR $8.50, MM50 $86.23, volume 22,164,500 (0.85x), short interest 20.98%, consensus FMP $94.54, options max_pain $45.0 (aberrant), put_call_ratio null, call_oi_pct null, expiration 2026-07-02
- `data/validation_report.txt` (2026-06-29) — [ERROR] AST: fetch failed.
- `data/recommandations_latest.json` (2026-06-29) — AST: 55.2/100 (ATTENDRE) ; ASTS: 54.8/100 ajusté 46.8/100 (SURVEILLER), prix actuel $71.45, SL $54.45, TP $96.95, ratio R/R 1.5
- `data/sector_rotation_2026-06-29.json` — XLK top sectoriel (momentum 10.0/10, signal NEUTRAL), XLC bottom (momentum 0.0/10)
- `data/fx_exposure_2026-06-29.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-29.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-29.json` — AST: earnings 2026-06-29 (J=0 glissant) ; ASTS: earnings 2026-08-10 (42 jours)
- `data/events_2026-06-29.json` — Aucun événement corporate détecté pour AST/ASTS
- `data/geo_risk_latest.json` (2026-06-29) — Pas de flag spécifique AST/ASTS
- `data/quant_report_latest.json` (2026-05-17) — Données quantitatives insuffisantes
