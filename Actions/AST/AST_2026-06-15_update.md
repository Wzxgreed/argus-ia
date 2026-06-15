# AST — Mise à Jour Close US (2026-06-17h UTC)

> **Source :** `data/latest.json` (snapshot 2026-06-15T17:00:01Z) | `data/recommandations_latest.json` | `data/validation_report.txt`
> **Référence précédente :** [AST_2026-06-15_update.md](AST_2026-06-15_update.md) (snapshot 10h UTC)
> **Contexte :** Close officiel US post-gap down. ASTS rebondit **+6.49%** à $87.76 mais sur **volume collapse extrême 0.53×** (14.50M vs moy. 20j 27.10M). L'anomalie options JSON est **résolue**.

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC (2026-06-15)

| Métrique | Snapshot 10h (15/06) | Snapshot 17h (15/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirmé stable — >43 snapshots consécutifs** |
| **ASTS — Cours close** | **$82.41** | **$87.76** | **+6.49%** — rebond technique post-gap down |
| **ASTS — Previous close** | $97.56 (vendredi) | **$82.41** | Référence Yahoo mise à jour (close 12/06 devient previous) |
| **ASTS — RSI 14j** | 40.50 | **36.10** | **−4.4 pts** — survente s'aggrave malgré rebond 🔴 |
| **ASTS — ATR 14j** | $13.80 | **$12.73** | **−$1.07** — volatilité en retrait |
| **ASTS — MM 50j** | $89.23 | **$89.14** | **−$0.09** — cours reste sous MM50 |
| **ASTS — Volume séance** | 54.91M (2.00×) | **14.50M (0.53×)** | **Volume collapse extrême −73.6%** 🔴 |
| **ASTS — Short Interest** | 18.39% | **18.39%** | = — stable |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = |
| **ASTS — Premium vs consensus** | −12.8% | **−7.2%** | Amélioration mécanique +5.6 pts |
| **ASTS — Options Max Pain** | $28.0 [ANOMALIE JSON] | **$100.0** | **Anomalie résolue** — valeur opérationnelle rétablie |
| **ASTS — Options Put/Call** | 0.0 [ANOMALIE JSON] | **0.44** | **Anomalie résolue** — structure haussière |
| **ASTS — Options Call OI %** | 100.0% [ANOMALIE JSON] | **69.7%** | **Anomalie résolue** — call dominance modérée |
| **ASTS — Échéance options** | 2026-06-18 (3j) | **2026-06-18 (3j)** | Inchangé — theta decay imminent |
| **Score Global ASTS** | 35.5/100 (SURVEILLER) | **39.2/100 (SURVEILLER)** | **+3.7 pts** — remontée mécanique, reste proche ÉVITER |
| **Score Opportunité ASTS** | 4.3/10 | **4.7/10** | **+0.4 pt** |

**Verdict :** La séance US confirme un **rebond technique +6.49%** sur ASTS, mais la force du mouvement est fortement questionnée par un **volume collapse extrême à 0.53×** (14.50M vs 54.91M ce matin). Le RSI continue de descendre (**36.10**, −4.4 pts) pour entrer plus profondément en survente, ce qui est atypique sur un rebond de +6% et signale une absence de conviction acheteuse. L'**anomalie options JSON est résolue** : max pain $100.0, put/call 0.44, call OI 69.7% — structure modérément haussière mais le max pain reste éloigné au-dessus du cours. Le scoring agent remonte légèrement de **35.5 à 39.2/100 (SURVEILLER)** mais reste dans la zone de danger. La **MM50 ($89.14) n'est pas retestée** : le cours à $87.76 reste **−1.5% en dessous**, confirmant le biais baissier à moyen terme.

---

## 2. Mise à Jour Technique

### AST (données officielles)

| Indicateur | Valeur Snapshot 17h | Valeur précédente (10h) | Δ |
|-----------|---------------------|-------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur **>43 snapshots consécutifs** (18/05 → 15/06).

### ASTS (proxy — données actualisées close US)

| Indicateur | Valeur Snapshot 17h | Valeur Snapshot 10h | Δ |
|-----------|-------------------|-------------------|---|
| Cours close | **$87.76** | $82.41 | **+6.49%** |
| Previous close | **$82.41** | $97.56 | Yahoo a mis à jour la référence (close 12/06) |
| RSI 14j | **36.10** | 40.50 | **−4.4 pts** — survente s'aggrave |
| ATR 14j | **$12.73** | $13.80 | **−$1.07** — volatilité en retrait |
| MM 50j | **$89.14** | $89.23 | **−$0.09** — cours sous MM50 de **−1.5%** |
| Volume séance | **14.50M** | 54.91M | **−73.6%** — volume collapse extrême |
| Volume relatif | **0.53×** | 2.00× | **Effondrement** 🔴 |
| Short interest | **18.39%** | 18.39% | = — stable |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 36.08 | 36.08 | = |

**Verdict timing ASTS :** 🟡 **REBOND TECHNIQUE FRAGILE — VOLUME COLLAPSE, SURVENTE PERSISTANTE, SOUS MM50**

- **RSI 36.10** : la survente s'aggrave de −4.4 pts **malgré le rebond +6.49%**. Ce divergence prix/momentum est typique d'un rebond sans conviction (short covering ou arbitrage algorithmique) plutôt que d'un retournement de tendance fondé.
- **Volume collapse 0.53×** : 14.50M vs moyenne 20j 27.10M. Le rebond s'est effectué sur un tiers du volume de ce matin. Cela invalide l'hypothèse d'un retournement institutionnel. La distribution du matin n'a pas trouvé de suivi acheteur dans l'après-midi.
- **Cassure MM50 ($89.14)** : le cours à $87.76 reste **−1.5% sous la MM50**. La résistance moyen terme n'a pas été testée. Un franchissement de $89.14 avec volume > 20M serait la première condition d'amélioration technique.
- **ATR $12.73** : volatilité en retrait de −7.8% vs ce matin, cohérent avec un marché hésitant après le choc du gap down.
- **Short interest stable à 18.39%** : pas de couverture massive des shorts détectée sur cette séance. Le rebond n'a pas été alimenté par un short squeeze.

**Niveaux clés** (actualisés avec données close US du 15/06) :
- Support immédiat : **$83.99** (low intraday 15/06)
- Support : **$82.41** (previous close / low matinal)
- Support critique : **$80.00–$81.50** (zone de confluence + 1.5×ATR)
- Résistance immédiate : **$89.14** (MM50 — test de retour comme résistance)
- Résistance majeure : **$97.56** (close vendredi 12/06 / gap à combler)
- Objectif haussier : **$125.94** (spot + 3×ATR $12.73)

**Structure options** (anomalie JSON résolue) :
- **Max Pain** : **$100.0** — cohérent, au-dessus du cours de +13.9%. Le max pain agit comme aimant gamma si le cours reste dans une fourchette étroite jusqu'à mercredi.
- **Put/Call ratio** : **0.44** — structure modérément haussière (calls dominants).
- **Call OI %** : **69.7%** — confirmation de la dominance call, mais pas excessive.
- Expiration proche : **2026-06-18** (3 jours) — theta decay risqué pour les options OTM.

> **Note options :** L'anomalie JSON du matin ($28.0 / 0.0 / 100.0%) est **résolue** dans le snapshot 17h. Les valeurs opérationnelles rétablies (max pain $100.0, put/call 0.44, call OI 69.7%) sont cohérentes avec une structure légèrement haussière. Le max pain $100.0 est éloigné du cours actuel, ce qui limite la pression gamma immédiate mais pourrait attirer le cours vers $90–$100 si la volatilité reste élevée jusqu'à mercredi.

---

## 3. Mise à Jour Fondamentale

### AST (données officielles)

| Métrique | Valeur Snapshot 17h | Valeur précédente | Δ |
|---------|---------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur Snapshot 17h | Valeur Snapshot 10h | Δ |
|---------|---------------------|-----------------------|---|
| Market cap Yahoo | **$34.05 B** | $31.99 B | **+$2.06 B (+6.4%)** mécanique |
| Forward P/E | **−427.49** | −401.61 | **−25.9 pts** (mécanique cours plus haut, EPS négatif) |
| EV/Revenue | **296.3×** | 296.3× | = |
| EV/EBITDA | **−79.53** | −79.53 | = |
| Beta | **2.634** | 2.634 | = |
| Short interest | **18.39%** | 18.39% | = |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **−7.2%** | −12.8% | **Amélioration mécanique +5.6 pts** |
| Price to book | **12.59** | 11.83 | **+0.76** (mécanique) |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement spéculative (EV/Revenue ~296×, forward P/E −427.49). **Aucune révision sell-side** n'a été enregistrée (consensus $94.54, 12 analysts inchangé). Le premium vs consensus s'améliore mécaniquement de −12.8% à **−7.2%** du fait du rebond, mais la divergence reste significative. Les multiples extrêmement élevés confirment le caractère spéculatif du titre. Aucun changement fondamental n'est à signaler.

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($34.05 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Écart de **+34.5%** (réduit vs +36.2% précédemment mais toujours élevé).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 10h |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain (JSON)** | $100.0 | **Anomalie résolue** — cohérent |
| **Put/Call ratio (JSON)** | 0.44 | **Anomalie résolue** — structure haussière |
| **Call OI % (JSON)** | 69.7% | **Anomalie résolue** — call dominance modérée |
| **Short Interest** | 18.39% | = — stable |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options rétablies** — Max pain $100.0, put/call 0.44, call OI 69.7%. Structure modérément haussière. Le max pain $100.0 est éloigné du cours actuel, ce qui laisse de la marge avant une pression gamma significative.
- **Short interest stable** (18.39%) — pas de couverture massive des shorts sur la séance. Le setup squeeze reste théorique mais le rebond sur volume faible n'en est pas la confirmation.
- **Aucun upgrade/downgrade**, absence totale d'activité institutionnelle/retail.
- **Aucun insider trade** significatif signalé.

**Verdict Sentiment :** Neutre — L'absence de news et d'activité institutionnelle persiste. La résolution de l'anomalie options révèle une structure légèrement haussière, mais le volume collapse extrême du rebond (+6.49%) invalide l'hypothèse d'un retournement de sentiment. Le sentiment dominant reste technique : rebond sans conviction dans une tendance baissière.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée AST/ASTS | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques. | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique AST/ASTS. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLK (Technology) momentum score **10.0/10**, signal **NEUTRAL**. XLC (Communication Services) bottom3, momentum **0.0/10**. | [DONNÉES PARTIELLES] — ASTS est classé Technology mais proche de Communication Services. |
| **FX Exposure** | Score FX Impact **0.0**, flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | AST : earnings signalé **2026-06-15** (FMP) — placeholder glissant J=0 non résolu depuis 25/05 (>21 jours). ASTS : earnings **2026-08-10** (56 jours). | Trop loin pour pricer. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **Validation Report** | [ERROR] AST — fetch failed. 5 errors total. | AST en erreur connue. |

---

## 6. Scoring Global Révisé

### AST (données officielles — placeholder)

| Axe | Score Snapshot 17h | Pondération | Note |
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

| Axe | Score Snapshot 17h | Pondération | Note |
|-----|-------------------|-------------|------|
| Catalyseur | 5.5/10 | 35% | Aucun catalyseur court terme. Earnings 10/08 distant. Distribution matinale partiellement effacée. |
| Valorisation | 4.5/10 | 40% | EV/Revenue ~296×, forward P/E −427.49 — reste spéculatif. Divergence consensus −7.2%. |
| Momentum | 4.0/10 | 25% | RSI 36.10 (survente aggravée), rebond +6.49% sur volume collapse, cours sous MM50. |
| **Score Opportunité** | **4.7/10** | — | **Non qualifié pour position** (score < 6) |
| **Score Global** | **47.2/100** | — | **SURVEILLER** |
| **Score Global Ajusté** | **39.2/100** | — | **SURVEILLER** (proche seuil ÉVITER) |

**Action recommandée :** SURVEILLER (stable)
**Timing :** Défavorable (rebond sans volume, survente persistante, sous MM50)
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. La remontée de **35.5 → 39.2/100 (SURVEILLER)** est entièrement mécanique (rebond du cours) et masque une détérioration technique sous-jacente (RSI en survente aggravée, volume collapse). Le score Opportunité (4.7/10) reste sous le seuil de qualification (6.0/10).

---

## 7. Révision des Niveaux SL / TP

### AST (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy — actualisés avec close US 15/06)

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $87.76 (close 15/06) | Close officiel US |
| **Stop-loss** | $62.30 (−29.0%) | 2×ATR ($12.73) — révisé à la baisse (vs $54.81 base $13.80 ancienne) |
| **Take-profit** | $125.94 (+43.5%) | 3×ATR ($12.73) — révisé à la baisse (vs $123.81 base ancienne) |
| **Ratio R/R** | **1.5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Zone d'intérêt potentielle :** Le rebond technique +6.49% sur volume collapse ne constitue pas un signal d'achat. Un test de la **MM50 $89.14** avec volume > 20M serait la première étape d'une amélioration technique. En l'absence de volume, tout rebond au-dessus de $89.14 serait suspect. Une **cassure sous $83.99** (low intraday 15/06) avec volume confirmerait la reprise de la distribution et ouvrirait la voie vers **$82.41** puis **$80.00–$81.50**. Une **cassure sous $80** avec volume élevé justifierait un passage de SURVEILLER à **ÉVITER**.

> **Note :** Les niveaux SL/TP sont recalculés sur l'ATR actualisée ($12.73). Ils restent indicatifs étant donné le caractère spéculatif et volatile du titre.

---

## 8. Calendrier & Événements à Venir

| Événement | Ticker | Date | Jours restants | Détail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-15 | **J=0 glissant** | FMP placeholder non résolu depuis 25/05 (>21 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **56 jours** | Est EPS : −$0.29 à −$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-06-18 | **3 jours** | Max Pain $100.0 — structure légèrement haussière. Theta decay risque. |

**Prochain catalyseur majeur :** Aucun avant earnings (août). L'expiration options du 18 juin (mercredi) pourrait amplifier la volatilité à court terme si le cours se rapproche du max pain $100.0, mais la distance actuelle ($87.76 → $100.0 = +14.0%) limite la pression gamma immédiate.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>43 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **MODIFIÉE — SURVEILLER MAINTENU, SCORE LÉGÈREMENT REMONTÉ (35.5 → 39.2/100) MAIS FRAGILITÉ TECHNIQUE ACCRUE**

Le close US du 15/06 modifie la thèse sur ASTS avec les observations suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS. AST n'a toujours aucune donnée de cours après **>43 snapshots consécutifs** (18/05 → 15/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. 🟡 **Rebond technique ASTS +6.49% :** le cours remonte à $87.76 mais sur un **volume collapse extrême 0.53×** (14.50M vs 54.91M ce matin). Ce rebond est qualitatif et non quantitatif — il manque de conviction institutionnelle.
3. 🔴 **RSI en survente aggravée :** 36.10 (−4.4 pts) — le rebond du cours n'a pas été accompagné d'une amélioration du momentum. Divergence prix/momentum baissière.
4. 🟡 **Cours reste sous MM50 ($89.14) :** le cours à $87.76 se situe **−1.5% sous la MM50**. La résistance moyen terme n'a pas été testée. Un franchissement avec volume > 20M serait requis pour infirmer le biais baissier.
5. ✅ **Anomalie options JSON résolue :** max pain $100.0, put/call 0.44, call OI 69.7% — structure modérément haussière. Le max pain éloigné limite la pression gamma immédiate.
6. 🟡 **Short interest stable :** 18.39% — pas de couverture massive des shorts sur la séance. Le setup squeeze reste théorique mais le rebond sans volume n'en est pas la preuve.
7. 🟡 **Échéance options dans 3 jours :** Le 18 juin. Theta decay sur les options OTM pourrait amplifier la volatilité si le cours approche du max pain ($100.0).
8. 🟡 **Score agent remonte mécaniquement :** 35.5 → 39.2/100 (SURVEILLER) — cette remontée est entièrement expliquée par le rebond du cours et ne reflète pas une amélioration fondamentale ou technique. Le score reste proche du seuil ÉVITER (< 35).
9. 🟡 **Aucune news fondamentale** ni événement corporate — le contexte reste purement technique.
10. 🟡 **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-15** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé. Le glissement J=0 persiste depuis le **25/05** (>21 jours de décalage non résolu).

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence** — la thèse SURVEILLER est maintenue mais le score à **39.2/100** reste proche du seuil ÉVITER. Les niveaux clés à surveiller :
  - **Cassure sous $83.99** (low intraday 15/06) avec volume → prochaines cibles $82.41 puis $80.00–$81.50
  - **Cassure sous $80** avec volume élevé → passage de SURVEILLER à ÉVITER
  - **Rebond au-dessus de $89.14** (MM50) avec volume > 20M → possible retournement technique
  - **Rebond au-dessus de $97.56** (close vendredi) → combler le gap, retour du biais haussier mais nécessite confirmation volume > 30 M
- **Ne pas entrer de position longue** sur ASTS avant un test réussi de la MM50 ($89.14) avec volume confirmé, ou un catalyseur fondamental vérifiable
- **Surveiller l'échéance options 2026-06-18** (mercredi) — theta decay risque si le cours reste sous $90

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références

- `data/latest.json` (snapshot 2026-06-15T17:00:01Z) — AST: error "No price history" ; ASTS: close $87.755, previous_close $82.41, RSI 36.10, ATR $12.73, MM50 $89.14, volume 14,495,882 (0.53×), short interest 18.39%, consensus FMP $94.54, options (max_pain $100.0, put_call_ratio 0.44, call_oi_pct 69.7%)
- `data/validation_report.txt` (2026-06-15) — [ERROR] AST: fetch failed. 5 errors total, 0 excluded.
- `data/recommandations_latest.json` (2026-06-15) — AST: 55.2/100 (ATTENDRE) ; ASTS: 47.2/100 ajusté 39.2/100 (SURVEILLER)
- `data/sector_rotation_2026-06-15.json` — XLK top sectoriel (momentum 10.0/10, signal NEUTRAL), XLC bottom (momentum 0.0/10)
- `data/fx_exposure_2026-06-15.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-15.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-15.json` — AST: earnings 2026-06-15 (J=0 glissant) ; ASTS: earnings 2026-08-10 (56 jours)
- `data/events_2026-06-15.json` — Aucun événement corporate détecté pour AST/ASTS
- `data/geo_risk_latest.json` (2026-05-17) — Pas de flag spécifique AST/ASTS
- `data/quant_report_latest.json` (2026-05-17) — Données quantitatives insuffisantes
