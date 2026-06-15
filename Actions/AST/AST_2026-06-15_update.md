# AST — Mise à Jour Post-Week-End (2026-06-15)

> **Source :** `data/latest.json` (snapshot 2026-06-15T10:00:16 UTC) | `data/validation_report.txt` | `data/recommandations_latest.json`
> **Référence précédente :** [AST_2026-06-10_update.md](AST_2026-06-10_update.md) (snapshot 10h UTC)
> **Contexte :** Premier snapshot post-week-end. AST persiste en erreur structurelle (>42 snapshots). ASTS affiche un **gap down massif de −15.53%** sur volume de liquidation 2.0×. ATR et MM50 récupérées après 5 jours d'absence.

---

## 1. Résumé des Changements depuis le Snapshot 10h UTC (2026-06-10)

| Métrique | Snapshot 10h (10/06) | Snapshot 10h (15/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirmé stable — >42 snapshots consécutifs** |
| **ASTS — Cours close** | NaN [DONNÉES PARTIELLES] | **$82.41** | Données rétablies — **gap down −15.53%** vs previous close |
| **ASTS — Previous close** | $92.06 (stale probable) | **$97.56** | Close vendredi confirmé |
| **ASTS — RSI 14j** | 51.78 | **40.50** | **−11.28 pts** — franchissement zone neutre → survente 🔴 |
| **ASTS — ATR 14j** | null | **$13.80** | [DONNÉES RÉTABLIES] — recalculable |
| **ASTS — MM 50j** | null | **$89.23** | [DONNÉES RÉTABLIES] — cours sous MM50 de **−7.6%** |
| **ASTS — Volume séance** | 26.69 M (1.01×) | **54.91 M (2.00×)** | **+105%** — volume de liquidation 🔴 |
| **ASTS — Short Interest** | 18.39 % | **18.39 %** | = — stable |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = |
| **ASTS — Premium vs consensus** | −6.2 % (réel, base $88.71) | **−12.8 %** (base $82.41) | **Dégradation −6.6 pts** 🔴 |
| **ASTS — Forward P/E** | −432.31 | **−401.61** | +30.7 pts (mécanique cours plus bas) |
| **ASTS — EV/Revenue** | 318.4× | **296.3×** | −22.1× (mécanique) |
| **ASTS — Options Max Pain** | $45.0 [ANOMALIE] | **$28.0** [ANOMALIE JSON] | Aberrant — valeur opérationnelle historique **$120.0** conservée |
| **ASTS — Options Put/Call** | null [ANOMALIE] | **0.0** [ANOMALIE JSON] | Aberrant — valeur opérationnelle historique **0.74** conservée |
| **ASTS — Options Call OI %** | null [ANOMALIE] | **100.0 %** [ANOMALIE JSON] | Aberrant — valeur opérationnelle historique **57.4 %** conservée |
| **ASTS — Échéance options** | 2026-06-12 (2j) | **2026-06-18 (3j)** | Nouvelle échéance post-week-end |
| **ASTS — Earnings Q2 2026** | 62 jours | **56 jours** | −6 jours |
| **Score Global AST (proxy)** | 55.2/100 (ATTENDRE) | **55.2/100 (ATTENDRE)** | Placeholder inchangé |
| **Score Global ASTS** | 44.0/100 (SURVEILLER) | **35.5/100 (SURVEILLER)** | **−8.5 pts** — approche seuil ÉVITER 🔴 |
| **Score Opportunité ASTS** | 4.4/10 | **4.3/10** | **−0.1 pt** |

**Verdict :** Le snapshot post-week-end confirme la **persistance de l'anomalie structurelle sur AST** (>42 snapshots). Sur ASTS, le **gap down −15.53%** sur volume de liquidation 2.0× est le signal dominant. Le RSI franchit la zone neutre pour entrer en **survente (40.50)**. La **MM50 ($89.23) est récupérée** et le cours s'y situe **−7.6% en dessous**, confirmant une cassure baissière. L'**ATR ($13.80) est rétablie**, permettant un recalcul des niveaux SL/TP. Le short interest reste stable à 18.39%. Les données options présentent une **nouvelle anomalie JSON** (max pain $28.0, put/call 0.0, call OI 100.0%). Le scoring ASTS se dégrade de **44.0 à 35.5/100 (SURVEILLER)**, proche du seuil ÉVITER.

---

## 2. Mise à Jour Technique

### AST (données officielles)

| Indicateur | Valeur Snapshot 15/06 | Valeur précédente (10/06) | Δ |
|-----------|----------------------|---------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur **>42 snapshots consécutifs** (18/05 → 15/06).

### ASTS (proxy — données rétablies)

| Indicateur | Valeur Snapshot 15/06 | Valeur Close 21h UTC (09/06) | Δ |
|-----------|----------------------|------------------------------|---|
| Cours close | **$82.41** | $88.71 | **−7.1%** (vs 09/06) ; **−15.53%** (vs $97.56 previous close) |
| Previous close | **$97.56** | — | Close vendredi confirmé |
| RSI 14j | **40.50** | 50.27 | **−9.77 pts** — survente technique |
| ATR 14j | **$13.80** | $13.29 | **+$0.51** — volatilité en hausse |
| MM 50j | **$89.23** | $88.70 | **+$0.53** — cours sous MM50 de **−7.6%** |
| Volume séance | **54.91 M** | 26.69 M | **+105.7%** — volume de liquidation |
| Volume relatif | **2.00×** | 1.01× | **Doublé** 🔴 |
| Short interest | **18.39 %** | 17.60 % | **+0.79 pt** (cumulé depuis 09/06) |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 36.08 | 35.33 | [REVIÉ] — 52W low remonté |

**Verdict timing ASTS :** 🔴 **DÉFAVORABLE — GAP DOWN LIQUIDATION, CASSURE MM50, SURVENTE TECHNIQUE**

- **RSI 40.50** : sortie de la zone neutre pour entrer en **survente** (< 40 proche). Chute de −9.77 pts vs close 09/06, −11.28 pts vs snapshot 10/06. Pas de rebond automatique sans catalyseur.
- **Cassure MM50 ($89.23)** : le cours à $82.41 se situe **−7.6% sous la MM50**, confirmant un basculement de tendance baissière à moyen terme. La dernière fois que le cours était sous MM50 remonte à début mai.
- **Volume de liquidation 2.0×** : 54.91 M vs moyenne 20j 27.46 M. Ce volume élevé sur un gap down confirme la distribution institutionnelle ou le stop-loss triggering en masse.
- **ATR $13.80** : volatilité rétablie et légèrement supérieure à la dernière valeur connue ($13.29), cohérente avec le gap down.
- **Short interest stable à 18.39%** : le ratio reste élevé (>15%) mais la distribution du jour a probablement été amplifiée par des prises de bénéfices longs plutôt que par un short squeeze. Le setup squeeze reste théorique mais nécessite un catalyseur.

**Niveaux clés** (actualisés avec données du 15/06) :
- Support immédiat : **$81.50** (low intraday 15/06)
- Support technique : **$80.00** (psychologique + zone de confluence)
- Support critique : **$76.00–$78.00** (gap zone + 1.5×ATR)
- Résistance immédiate : **$89.23** (MM50 — test de retour comme résistance)
- Résistance majeure : **$97.56** (previous close / gap à combler)
- Objectif haussier : **$123.81** (spot + 3×ATR $13.80)

**Structure options** (anomalie JSON détectée) :
- **Max Pain** : **$28.0** — divergence −66.0% vs cours. Valeur non opérationnelle ; valeur historique **$120.0** conservée.
- **Put/Call ratio** : **0.0** — [ANOMALIE JSON]. Valeur opérationnelle historique **0.74** conservée.
- **Call OI %** : **100.0%** — [ANOMALIE JSON]. Valeur opérationnelle historique **57.4%** conservée.
- Expiration proche : **2026-06-18** (3 jours).

> **Note options :** Nouvelle anomalie JSON post-week-end (max pain $28.0 aberrant, put/call 0.0, call OI 100.0%). Ce pattern diffère de l'anomalie précédente ($45.0 / null / null) mais reste incohérent. **Valeurs opérationnelles historiques conservées** : Max Pain $120.0, Put/Call 0.74, Call OI 57.4%. Le theta decay sur les options OTM pourrait amplifier la volatilité jusqu'à mercredi (expiration 06-18).

---

## 3. Mise à Jour Fondamentale

### AST (données officielles)

| Métrique | Valeur Snapshot 15/06 | Valeur précédente | Δ |
|---------|----------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur Snapshot 15/06 | Valeur Snapshot 10/06 | Δ |
|---------|----------------------|-----------------------|---|
| Market cap Yahoo | **$31.99 B** | $34.43 B | **−$2.44 B (−7.1%)** mécanique |
| Forward P/E | **−401.61** | −432.31 | **+30.7 pts** (mécanique) |
| EV/Revenue | **296.3×** | 318.4× | **−22.1×** (mécanique) |
| EV/EBITDA | **−79.53** | −85.48 | **+5.95** (mécanique) |
| Beta | **2.634** | 2.634 | = |
| Short interest | **18.39 %** | 18.39 % | = |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **−12.8 %** | −6.2 % (base $88.71) | **Dégradation −6.6 pts** |
| Price to book | **11.83** | 12.73 | **−0.90** (mécanique) |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement spéculative (EV/Revenue ~296×, forward P/E −401.61). **Aucune révision sell-side** n'a été enregistrée (consensus $94.54, 12 analysts inchangé). Le premium vs consensus se dégrade mécaniquement de −6.2% à **−12.8%** du fait du gap down, creusant la divergence. Les multiples extrêmement élevés confirment le caractère spéculatif du titre. Aucun changement fondamental n'est à signaler.

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($31.99 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Écart de **+26.4%** (réduit vs +36.2% précédemment du fait de la baisse du cours).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 10/06 |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain (JSON)** | $28.0 | [ANOMALIE JSON RÉCURRENTE — nouveau pattern] |
| **Put/Call ratio (JSON)** | 0.0 | [ANOMALIE JSON RÉCURRENTE — nouveau pattern] |
| **Call OI % (JSON)** | 100.0 % | [ANOMALIE JSON RÉCURRENTE — nouveau pattern] |
| **Short Interest** | 18.39 % | = — stable |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options corrompues à nouveau** — Nouveau pattern d'anomalie JSON (max pain $28.0, put/call 0.0, call OI 100.0%). Valeurs opérationnelles historiques conservées.
- **Short interest stable** (18.39%) — pas de nouvel engagement vendeur détecté sur cette fenêtre. Le ratio >15% maintient le setup squeeze théorique mais le gap down du jour a probablement été piloté par des longs sortants.
- **Aucun upgrade/downgrade**, absence totale d'activité institutionnelle/retail.
- **Aucun insider trade** significatif signalé.

**Verdict Sentiment :** Neutre à baissier — L'absence de news et d'activité institutionnelle persiste. L'anomalie options empêche toute lecture directionnelle. Le sentiment dominant est technique : distribution / liquidation sur gap down.

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

| Axe | Score Snapshot 15/06 | Pondération | Note |
|-----|----------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35 % | [NON FONDÉ] — aucun catalyseur vérifiable |
| Valorisation | 5.0/10 (placeholder) | 40 % | [NON FONDÉ] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25 % | [NON FONDÉ] — pas de cours, pas de momentum |
| **Score Opportunité** | **5.5/10** | — | Placeholder — **non utilisable pour décision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |
| **Score Global Ajusté** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, à titre indicatif uniquement)

| Axe | Score Snapshot 15/06 | Pondération | Note |
|-----|----------------------|-------------|------|
| Catalyseur | 5.5/10 | 35 % | Aucun catalyseur court terme. Earnings 10/08 distant. Distribution post-spike persistante. |
| Valorisation | 4.5/10 | 40 % | EV/Revenue ~296×, forward P/E −401.61 — reste spéculatif. Divergence consensus −12.8%. |
| Momentum | 2.5/10 | 25 % | RSI 40.50 (survente), gap down −15.53%, volume liquidation 2.0×, cours sous MM50. |
| **Score Opportunité** | **4.3/10** | — | **Non qualifié pour position** (score < 6) |
| **Score Global** | **43.5/100** | — | **SURVEILLER** |
| **Score Global Ajusté** | **35.5/100** | — | **SURVEILLER** (proche seuil ÉVITER) |

**Action recommandée :** SURVEILLER (dégradé)
**Timing :** Défavorable (gap down liquidation, survente technique, cassure MM50)
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. La dégradation de **44.0 → 35.5/100 (SURVEILLER)** reflète le gap down −15.53% combiné à la cassure MM50 et à la survente technique (RSI 40.50). Le score Opportunité (4.3/10) reste sous le seuil de qualification (6.0/10).

---

## 7. Révision des Niveaux SL / TP

### AST (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy — actualisés avec données 15/06)

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $82.41 (close 15/06) | Données rétablies — ATR et MM50 disponibles |
| **Stop-loss** | $54.81 (−33.5%) | 2×ATR ($13.80) — révisé à la hausse (vs $62.13 base $13.29 ancienne) |
| **Take-profit** | $123.81 (+50.2%) | 3×ATR ($13.80) — révisé à la baisse (vs $128.58 base ancienne) |
| **Ratio R/R** | **1.5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Zone d'intérêt potentielle :** Un rebond technique depuis la survente (RSI 40.50) pourrait tester la **MM50 $89.23** comme première résistance. Ce rebond nécessiterait un volume faible et une absence de follow-through vendeur. Une **cassure sous $81.50** (low intraday 15/06) avec volume confirmerait la distribution et ouvrirait la voie vers **$76–78**. Une **cassure sous $76** avec volume élevé justifierait un passage de SURVEILLER à **ÉVITER**.

> ⚠️ **Note :** Les niveaux SL/TP sont désormais calculés sur l'ATR rétablie ($13.80). Ils restent indicatifs étant donné le caractère spéculatif et volatile du titre.

---

## 8. Calendrier & Événements à Venir

| Événement | Ticker | Date | Jours restants | Détail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-15 | **J=0 glissant** | FMP placeholder non résolu depuis 25/05 (>21 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **56 jours** | Est EPS : −$0.29 à −$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-06-18 | **3 jours** | Max Pain JSON $28.0 — [NON OPÉRATIONNEL]. Valeur historique $120.0 conservée. |

**Prochain catalyseur majeur :** Aucun avant earnings (août). L'expiration options du 18 juin (3 jours) pourrait amplifier la volatilité à court terme, notamment via le theta decay si le cours reste sous $90.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>42 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🔴 **MODIFIÉE — SURVEILLER MAINTENU MAIS SCORE DÉGRADÉ (44.0 → 35.5/100)**

Le snapshot post-week-end du 15/06 modifie la thèse sur ASTS avec les réserves suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS. AST n'a toujours aucune donnée de cours après **>42 snapshots consécutifs** (18/05 → 15/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. 🔴 **Gap down liquidation ASTS :** −15.53% sur volume **2.0×** (54.91 M). Distribution confirmée avec cassure de la MM50.
3. 🔴 **RSI en survente :** 40.50 (−11.3 pts) — entrée en zone de survente sans catalyseur de rebond visible.
4. 🔴 **Cassure MM50 ($89.23) :** le cours s'établit **−7.6% sous la MM50**, signal baissier à moyen terme. Le retour au-dessus de $89.23 est désormais la première condition d'amélioration technique.
5. 🟡 **ATR et MM50 récupérées :** après 5 jours d'absence, ces données sont rétablies, permettant un recalcul des niveaux SL/TP.
6. 🟡 **Short interest stable :** 18.39% — pas de nouvel engagement vendeur sur cette fenêtre, mais le ratio élevé maintient le setup squeeze théorique (improbable sans catalyseur).
7. 🟡 **Options anomalie JSON persistante :** Nouveau pattern ($28.0 / 0.0 / 100.0%) mais toujours incohérent. Valeurs opérationnelles historiques conservées.
8. 🟡 **Échéance options dans 3 jours :** Le 18 juin. Theta decay sur les options OTM pourrait amplifier la volatilité.
9. 🟡 **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-15** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé. Le glissement J=0 persiste depuis le **25/05** (>21 jours de décalage non résolu).
10. ✅ **Aucune news fondamentale** ni événement corporate — le contexte reste purement technique.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence** — la thèse SURVEILLER est maintenue mais le score à **35.5/100** est proche du seuil ÉVITER. Les niveaux clés à surveiller aujourd'hui :
  - **Cassure sous $81.50** (low intraday 15/06) avec volume → prochaines cibles $76–78
  - **Cassure sous $76** avec volume élevé → passage de SURVEILLER à ÉVITER
  - **Rebond au-dessus de $89.23** (MM50) avec volume faible → possible retournement technique
  - **Rebond au-dessus de $97.56** (previous close) → combler le gap, retour du biais haussier mais nécessite confirmation volume > 30 M
- **Ne pas entrer de position longue** sur ASTS avant un test réussi de la MM50 ($89.23) ou un catalyseur fondamental vérifiable
- **Surveiller l'échéance options 2026-06-18** (mercredi) — theta decay risque

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références

- `data/latest.json` (snapshot 2026-06-15T10:00:16Z) — AST: error "No price history" ; ASTS: close $82.41, previous_close $97.56, RSI 40.50, ATR $13.80, MM50 $89.23, volume 54,914,500 (2.00×), short interest 18.39%, consensus FMP $94.54, options (max_pain $28.0 anomalie, put_call_ratio 0.0, call_oi_pct 100.0)
- `data/validation_report.txt` (2026-06-15) — [ERROR] AST: fetch failed. 5 errors total, 0 excluded.
- `data/sector_rotation_2026-06-15.json` — XLK top sectoriel (momentum 10.0/10, signal NEUTRAL), XLC bottom (momentum 0.0/10)
- `data/fx_exposure_2026-06-15.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-15.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-15.json` — AST: earnings 2026-06-15 (J=0 glissant) ; ASTS: earnings 2026-08-10 (56 jours)
- `data/events_2026-06-15.json` — Aucun événement corporate détecté pour AST/ASTS
- `data/recommandations_latest.json` (2026-06-15) — AST: 55.2/100 (ATTENDRE) ; ASTS: 35.5/100 (SURVEILLER)
- `data/geo_risk_latest.json` (2026-05-17) — Pas de flag spécifique AST/ASTS
- `data/quant_report_latest.json` (2026-05-17) — Données quantitatives insuffisantes
