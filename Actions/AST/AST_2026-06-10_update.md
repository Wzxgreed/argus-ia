# AST — Mise à Jour Snapshot 10h UTC (2026-06-10)

> **Source :** `data/latest.json` (snapshot 2026-06-10T10:00:14 UTC) | `data/validation_report.txt` | Pipeline officiel — **données techniques partielles**
> **Référence précédente :** [AST_2026-06-09_update.md](AST_2026-06-09_update.md) (close officiel 21h UTC)
> **Contexte :** Snapshot pré-ouverture mercredi 10/06. AST persiste en erreur structurelle. ASTS affiche un `previous_close` à $92.06 — divergence probablement stale (correspond au close 13h UTC 09/06, non au close 21h $88.71). Données techniques partielles (ATR/MM50 null).

---

## 1. Résumé des Changements depuis le Close Officiel 21h UTC (2026-06-09)

| Métrique | Close 21h (09/06) | Snapshot 10h (10/06) | Variation |
|---|---|---|---|
| **AST — Erreur Yahoo** | `No price history` | `No price history` | **Confirmé stable — >37 snapshots consécutifs** |
| **ASTS — Cours close** | $88.71 | **NaN** [DONNÉES PARTIELLES] | Close indisponible |
| **ASTS — Previous close** | — | **$92.06** | [ANOMALIE STALE] — probablement close 13h UTC 09/06, non 21h |
| **ASTS — RSI 14j** | 50.27 | **51.78** | **+1.51 pts** — zone neutre |
| **ASTS — ATR 14j** | $13.29 | **null** | [DONNÉES MANQUANTES] |
| **ASTS — MM 50j** | $88.70 | **null** | [DONNÉES MANQUANTES] |
| **ASTS — Volume séance** | 26.69 M (1.01×) | **26.69 M** (1.01×) | Inchangé |
| **ASTS — Short Interest** | 17.60 % | **18.39 %** | **+0.79 pt** — hausse significative 🔴 |
| **ASTS — Consensus FMP PT** | $94.54 (12 analysts) | **$94.54 (12 analysts)** | = |
| **ASTS — Premium vs consensus** | −6.2 % | **−2.6 %** [MÉCANIQUE] | Réalignement sur previous_close stale $92.06 |
| **ASTS — Forward P/E** | −432.31 | **−432.31** | = |
| **ASTS — EV/Revenue** | 330.2× | **318.421×** | −11.8× (mécanique) |
| **ASTS — Market Cap Yahoo** | $34.43 B | **$34.43 B** | = |
| **ASTS — Options Max Pain** | $120.0 | **$45.0** | 🟡 **Anomalie JSON récurrente** |
| **ASTS — Options Put/Call** | 0.74 | **null** | 🟡 **Anomalie JSON récurrente** |
| **ASTS — Options Call OI %** | 57.4 % | **null** | 🟡 **Anomalie JSON récurrente** |
| **ASTS — Échéance options** | 2026-06-12 (3j) | **2026-06-12 (2j)** | **−1 jour** |
| **ASTS — Earnings Q2 2026** | 62 jours | **62 jours** | = |
| **Score Global ASTS (proxy)** | 45.0/100 (SURVEILLER) | **44.0/100 (SURVEILLER)** | **−1.0 pt** |
| **Score Opportunité ASTS** | 4.5/10 | **4.4/10** | **−0.1 pt** |

**Verdict :** Le snapshot 10h UTC confirme la **persistance de l'anomalie structurelle sur AST** (>37 snapshots consécutifs sans mutation depuis le 18/05). Sur ASTS, le `previous_close` à $92.06 est probablement **stale** (correspond au snapshot 13h UTC 09/06, non au close officiel 21h à $88.71) — anomalie Yahoo documentée. Seul le RSI est fiable (51.78, +1.51 pts), signalant un léger rebond technique dans la zone neutre. L'**ATR et la MM50 sont null**, empêchant toute révision des niveaux SL/TP. Le **short interest remonte significativement** (+0.79 pt à 18.39 %), signalant un nouvel engagement vendeur. L'échéance options **2026-06-12** est désormais dans **2 jours**. Le scoring ASTS (proxy) se maintient à **44.0/100 (SURVEILLER)** avec une légère dégradation du Catalyseur.

---

## 2. Mise à Jour Technique

### AST (données officielles)

| Indicateur | Valeur Snapshot 10h UTC (10/06) | Valeur précédente (21h UTC 09/06) | Δ |
|-----------|--------------------------------|-----------------------------------|---|
| Cours close | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | Placeholder 50 (agent) | Placeholder 50 (agent) | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 50j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| MM 200j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |

**Verdict timing AST :** [NON ÉVALUABLE] — absence totale de données techniques sur **>37 snapshots consécutifs** (18/05 → 10/06).

### ASTS (proxy, à titre de comparaison)

| Indicateur | Valeur Snapshot 10h UTC (10/06) | Valeur Close 21h UTC (09/06) | Δ |
|-----------|--------------------------------|------------------------------|---|
| Cours close | **NaN** [DONNÉES PARTIELLES] | $88.71 | — |
| Previous close | **$92.06** (probablement stale) | — | [ANOMALIE] |
| RSI 14j | **51.78** | 50.27 | **+1.51 pts** |
| ATR 14j | **null** | $13.29 | [DONNÉES MANQUANTES] |
| MM 50j | **null** | $88.70 | [DONNÉES MANQUANTES] |
| Volume séance | **26.688 M** | 26.69 M | **=** |
| Volume relatif | **1.01×** | 1.01× | **=** |
| Short interest | **18.39 %** | 17.60 % | **+0.79 pt** 🔴 |
| 52W high | 133.86 | 133.86 | = |
| 52W low | 35.33 | 35.33 | = |

**Verdict timing ASTS (proxy) :** 🟡 **NEUTRE À TEMPÉRER — REBOND TECHNIQUE LÉGER MAIS DONNÉES PARTIELLES ET SHORT INTEREST EN HAUSSE**

- **RSI 51.78** : légère remontée de +1.51 pts, reste en zone neutre (50–60). Pas de surachat ni de survente. La tendance baissière du close 21h (distribution post-spike) n'est pas infirmée par ce léger rebond.
- **Short interest 18.39 %** (+0.79 pt) : hausse significative du short interest, signalant un nouvel engagement vendeur. À 18.39 %, ASTS reste fortement shorté. Le setup short squeeze reste théoriquement possible (short interest >15 % + volume élevé) mais la distribution du 09/06 et l'absence de catalyseur rendent un squeeze peu probable à court terme.
- **ATR et MM50 indisponibles** : [DONNÉES PARTIELLES] dans le snapshot. La dernière MM50 connue était **$88.70** (écart théorique +3.8 % si previous_close $92.06 confirmé, ou +0.01 % si close $88.71 confirmé). La dernière ATR connue était **$13.29**.
- **Volume stable** : 26.69 M (1.01× moyenne 20j) — inchangé vs close 21h, confirmant la liquidité mais sans nouveau flux directionnel en pré-ouverture.

**Niveaux clés** (conservés sur base données 21h UTC 09/06, faute de données fraîches) :
- Support immédiat : **$88.70** (MM50 du 09/06, test exact)
- Support technique : **$85.50** (low intraday 09/06)
- Support critique : **$80–85** (zone de confluence)
- Résistance immédiate : **$92.06** (close 13h UTC 09/06 / previous_close stale)
- Résistance majeure : **$97.13–97.23** (high 13h UTC + open 09/06)
- Objectif haussier : **$128.58** (spot + 3×ATR $13.29, sur base $88.71)

**Structure options** (anomalie JSON récurrente) :
- **Max Pain** : **$45.0** — divergence −51.1 % vs previous_close. Valeur non opérationnelle ; valeur historique **$120.0** conservée.
- **Put/Call ratio** : **null** — [ANOMALIE JSON]. Valeur opérationnelle historique **0.74** conservée.
- **Call OI %** : **null** — [ANOMALIE JSON]. Valeur opérationnelle historique **57.4 %** conservée.
- Expiration proche : **2026-06-12** (2 jours).

> **Note options :** Anomalie JSON détectée au snapshot 10h UTC (Max Pain $45.0 aberrant, Put/Call null, Call OI null). Ce pattern récurrent à 10h UTC est documenté depuis le 08/06. **Valeurs opérationnelles conservées** du snapshot 09/06 13h UTC : Max Pain $120.0, Put/Call 0.74, Call OI 57.4 %. Le positionnement options reste nettement haussier mais le max pain à $120.0 (+35.3 % du close 21h $88.71, ou +30.3 % du previous_close $92.06) est très éloigné. Le theta decay sur les calls OTM pourrait amplifier la pression vendeuse demain (vendredi) si le cours reste sous $90.

---

## 3. Mise à Jour Fondamentale

### AST (données officielles)

| Métrique | Valeur Snapshot 10h UTC (10/06) | Valeur précédente | Δ |
|---------|--------------------------------|-------------------|---|
| Market cap | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| P/E LTM | — | — | — |
| Forward P/E | — | — | — |
| EV/EBITDA | — | — | — |
| Beta | — | — | — |
| Filtre Qualité (6 critères) | [NON APPLICABLE] | [NON APPLICABLE] | — |

**Filtre Qualité :** impossible à calculer sans états financiers accessibles.

### ASTS (proxy)

| Métrique | Valeur Snapshot 10h UTC (10/06) | Valeur Close 21h UTC (09/06) | Δ |
|---------|--------------------------------|------------------------------|---|
| Market cap | **$34.43 B** | $34.43 B | = |
| Forward P/E | **−432.31** | −432.31 | = |
| EV/Revenue | **318.421×** | 330.2× | **−11.8×** (mécanique) |
| EV/EBITDA | **−85.479** | −88.642 | **+3.2** (mécanique) |
| Beta | **2.634** | 2.634 | = |
| Short interest | **18.39 %** | 17.60 % | **+0.79 pt** 🔴 |
| Consensus PT | **$94.54** (12 analysts) | $94.54 (12 analysts) | = |
| Premium vs consensus | **−2.6 %** [MÉCANIQUE] | −6.2 % | [ANOMALIE stale] |
| Price to book | **12.73** | 12.73 | = |
| Sector | Technology | Technology | = |
| Industry | Communication Equipment | Communication Equipment | = |

La valorisation reste purement spéculative (EV/Revenue ~318×, forward P/E −432.31). Aucune révision sell-side n'a été enregistrée. Le `previous_close` stale à $92.06 affiche un premium mécanique de −2.6 % vs consensus, mais sur la base du close confirmé du 09/06 ($88.71), la divergence réelle reste **−6.2 %** — dégradation confirmée. Les multiples extrêmement élevés confirment le caractère spéculatif du titre.

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($34.43 B) vs FMP sous-jacent ($25.32 B, `fmp_key_metrics`). Écart de **+36.2 %** inchangé.

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs close 21h (09/06) |
|---|---|---|
| **News AST / ASTS** | Aucune | 0 article — vide |
| **Consensus analystes (FMP)** | $94.54 (12 analysts) | = |
| **Max Pain (JSON)** | $45.0 | [ANOMALIE JSON RÉCURRENTE] |
| **Put/Call ratio (JSON)** | null | [ANOMALIE JSON RÉCURRENTE] |
| **Call OI % (JSON)** | null | [ANOMALIE JSON RÉCURRENTE] |
| **Short Interest** | 18.39 % | **+0.79 pt** — nouvel engagement vendeur |
| **Social Sentiment** | 0 mentions, score 0/10 | Aucune activité retail |
| **Upgrades/downgrades AST** | Pas de consensus | — |
| **Upgrades/downgrades ASTS** | 12 analysts, PT $94.54 | = |

- **Structure options corrompues à nouveau** — Les valeurs JSON (Put/Call null, Call OI null, Max Pain $45.0) sont identifiées comme une anomalie récurrente du pipeline. Les métriques directionnelles opérationnelles historiques (0.74 et 57.4 %) restent la référence jusqu'à résolution.
- **Short interest en hausse significative** (18.39 % vs 17.60 %) — +0.79 pt, signalant un nouvel engagement vendeur. Le ratio reste élevé (>15 %) mais la distribution du 09/06 a probablement attiré de nouveaux shorts. Pas de squeeze setup imminent.
- **Aucun upgrade/downgrade**, absence totale d'activité retail.
- **Aucun insider trade** significatif signalé dans les rapports agents.

**Verdict Sentiment :** Neutre à légèrement baissier — L'absence de news et d'activité institutionnelle/retail persiste. La hausse du short interest est le signal dominant du jour (+0.79 pt). La structure options reste inutilisable sur ce snapshot.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée AST/ASTS | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques. | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Pas de flag spécifique AST/ASTS. | [DONNÉES MANQUANTES] |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLK (Technology) momentum score **10.0/10**, signal **NEUTRAL**. | [DONNÉES PARTIELLES] — returns NaN. |
| **FX Exposure** | Score FX Impact **0.0**, flag 🟢. | Aucun malus/bonus. |
| **Event-Driven** | Aucun événement corporate. | Aucun bonus/malus. |
| **Upcoming Events** | AST : earnings signalé **2026-06-08** (FMP) — placeholder glissant J=0 non résolu depuis 25/05 (>19 jours). ASTS : earnings **2026-08-10** (62 jours). | Trop loin pour pricer. |
| **Social Sentiment** | 0 mentions, 0 pump. | Aucun signal. |
| **Validation Report** | [ERROR] AST — fetch failed. 5 errors total. | AST en erreur connue. |

---

## 6. Scoring Global Révisé

### AST (données officielles — placeholder)

| Axe | Score Snapshot 10h UTC (10/06) | Pondération | Note |
|-----|-------------------------------|-------------|------|
| Catalyseur | 6.5/10 (placeholder) | 35 % | [NON FONDÉ] — aucun catalyseur vérifiable |
| Valorisation | 5.0/10 (placeholder) | 40 % | [NON FONDÉ] — aucun multiple ni DCF possible |
| Momentum | 5.0/10 (placeholder) | 25 % | [NON FONDÉ] — pas de cours, pas de momentum |
| **Score Opportunité** | **5.5/10** | — | Placeholder — **non utilisable pour décision** |
| **Score Global** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |
| **Score Global Ajusté** | **55.2/100** | — | Placeholder — **non utilisable pour décision** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, à titre indicatif uniquement)

| Axe | Score Snapshot 10h UTC (10/06) | Pondération | Note |
|-----|-------------------------------|-------------|------|
| Catalyseur | 4.0/10 | 35 % | Aucun catalyseur court terme. Distribution post-spike persistante. Earnings 10/08 distant. |
| Valorisation | 4.0/10 | 40 % | EV/Revenue ~318×, forward P/E −432.31 — reste spéculatif. Divergence consensus −6.2 % (réelle) vs −2.6 % (mécanique stale). |
| Momentum | 5.0/10 | 25 % | RSI 51.78 (+1.51 pts), mais données ATR/MM50 manquantes. Short interest en hausse (+0.79 pt) = momentum mitigé. |
| **Score Opportunité** | **4.4/10** | — | **Non qualifié pour position** (score < 6) |
| **Score Global** | **44.0/100** | — | **SURVEILLER** (stable vs 45.0/100 close 21h) |
| **Score Global Ajusté** | **44.0/100** | — | **SURVEILLER** |

**Action recommandée :** SURVEILLER (stable)
**Timing :** Défavorable (données partielles, short interest en hausse, échéance options dans 2j)
**Horizon :** —

> ASTS n'est PAS dans le périmètre d'analyse officiel d'AST. Ces scores sont fournis uniquement pour quantifier l'évolution du proxy. La stabilité du score à **44.0/100 (SURVEILLER)** reflète un équilibre entre le léger rebond RSI (+1.51 pts) et la hausse du short interest (+0.79 pt) combinée à l'absence de données ATR/MM50. Le score Opportunité (4.4/10) reste sous le seuil de qualification (6.0/10).

---

## 7. Révision des Niveaux SL / TP

### AST (données officielles)

**Impossibles à calculer.**
- Prix d'entrée : inconnu
- ATR 14j : inexistant
- Stop-loss suggéré = cours − 2×ATR → [NON CALCULABLE]
- Take-profit suggéré = cours + 3×ATR → [NON CALCULABLE]

### ASTS (proxy, à titre indicatif uniquement — conservés sur base 21h UTC 09/06)

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix de référence** | $88.71 (close 09/06 21h) | [DONNÉES PARTIELLES] — close 10/06 indisponible. Previous_close $92.06 probablement stale. |
| **Stop-loss** | $62.13 (−30.0 %) | 2×ATR ($13.29 du 09/06) — **non révisé**, ATR 10/06 manquant |
| **Take-profit** | $128.58 (+44.8 %) | 3×ATR ($13.29 du 09/06) — **non révisé**, ATR 10/06 manquant |
| **Ratio R/R** | **1.5 : 1** | Inchangé — inférieur au seuil 2:1 |

**Zone d'intérêt potentielle :** Un test réussi de la **MM50 $88.70** avec volume faible pourrait signaler une consolidation. Une **cassure sous $85.50** (low intraday 09/06) avec volume > 1.0× confirmerait la distribution et ouvrirait la voie vers **$80–85**. Une **cassure sous $80** avec volume élevé justifierait un passage de SURVEILLER à **ÉVITER**.

> ⚠️ **Note :** Les niveaux SL/TP sont marqués [DONNÉES PARTIELLES] car l'ATR 14j est null dans `data/latest.json`. Les estimations ci-dessus utilisent la dernière ATR connue ($13.29) à titre indicatif uniquement. **Ne pas trader sur ces niveaux avant confirmation de l'ATR.**

---

## 8. Calendrier & Événements à Venir

| Événement | Ticker | Date | Jours restants | Détail |
|---|---|---|---|---|
| **Earnings (placeholder)** | AST | 2026-06-08 | **J=0 glissant** | FMP placeholder non résolu depuis 25/05 (>19 jours de glissement) |
| **Earnings Q2 2026** | ASTS | 2026-08-10 | **62 jours** | Est EPS : −$0.29 à −$0.17 ; Rev : $0.0 B |
| **Expiration options** | ASTS | 2026-06-12 | **2 jours** | Max Pain JSON $45.0 — [NON OPÉRATIONNEL]. Valeur historique $120.0 conservée. |

**Prochain catalyseur majeur :** Aucun avant earnings (août). L'expiration options du 12 juin (2 jours) pourrait amplifier la volatilité à court terme, notamment via le theta decay sur les calls OTM si le cours reste sous $90.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Thèse AST :** 🔴 **INVALIDÉE PAR L'ABSENCE DE DONNÉES — ANOMALIE STRUCTURELLE PERSISTANTE (>37 SNAPSHOTS CONSÉCUTIFS)**

**Thèse ASTS (proxy) :** 🟡 **CONFIRMÉE AVEC RÉSERVES — SURVEILLER MAINTENU (44.0/100)**

Le snapshot 10h UTC du 10/06 confirme la posture **SURVEILLER** sur ASTS avec les réserves suivantes :

1. 🔴 **Anomalie structurelle persistante sur AST :** AST reste probablement un doublon erroné d'ASTS (AST SpaceMobile — NASDAQ). AST n'a toujours aucune donnée de cours après **>37 snapshots consécutifs** (18/05 → 10/06). La suppression ou l'exclusion de la watchlist reste recommandée.
2. 🟡 **Données techniques partielles sur ASTS :** Close NaN, `previous_close` stale ($92.06 = probablement close 13h UTC 09/06, non $88.71 close 21h), ATR null, MM50 null. Seul le RSI (51.78) est fiable et affiche un léger rebond technique.
3. 🔴 **Short interest en hausse significative :** +0.79 pt à **18.39 %**, signalant un nouvel engagement vendeur post-distribution. Le ratio >15 % maintient le setup squeeze théorique mais la distribution du 09/06 rend un squeeze peu probable sans catalyseur.
4. 🟡 **RSI en zone neutre :** 51.78 (+1.51 pts) — léger rebond sans signification directionnelle forte. La tendance baissière du close 21h n'est pas infirmée.
5. 🟡 **Options anomalie JSON récurrente :** Max Pain $45.0 aberrant (vs $120.0 opérationnel). Put/Call et Call OI null. Pattern documenté depuis le 08/06.
6. 🟡 **Échéance options dans 2 jours :** Le 12 juin. Theta decay sur les calls OTM pourrait amplifier la pression vendeuse si le cours reste sous $90 vendredi.
7. 🟡 **Earnings placeholder glissant non résolu :** FMP signale un earnings AST le **2026-06-08** (`days_until: 0`), mais sans historique de prix, le résultat ne peut être corrélé à un mouvement de marché. Le glissement J=0 persiste depuis le **25/05** (>19 jours de décalage non résolu).
8. ✅ **Aucune news fondamentale** ni événement corporate — le contexte reste purement technique.

**Recommandation opérationnelle :**
- **Résoudre l'anomalie structurelle immédiatement :** supprimer AST de `config/watchlist.json` ou le marquer `excluded`
- **Rediriger toute exposition space / telecom satellite vers ASTS**, ticker validé avec data complètes
- **Ne pas engager de capital sur AST** tant que les données de cours ne sont pas disponibles
- **Surveiller ASTS avec prudence** — la thèse SURVEILLER est maintenue à 44.0/100. Les niveaux clés à surveiller aujourd'hui :
  - **Cassure sous $85.50** (low intraday 09/06) avec volume > 1.0× → prochaines cibles $80–85
  - **Cassure sous $80** avec volume élevé → passage de SURVEILLER à ÉVITER
  - **Rebond au-dessus de $90** avec volume faible → possible consolidation avant test de $92.06
  - **Rebond au-dessus de $97.23** (open 09/06) → retour du biais haussier mais nécessite confirmation volume > 20 M
- **Ne pas entrer de position longue** sur ASTS avant un test réussi de la MM50 ($88.70) ou un catalyseur fondamental vérifiable
- **Surveiller l'échéance options 2026-06-12** (vendredi) — theta decay sur les calls OTM pourrait amplifier la pression vendeuse si le cours reste sous $90

---

## [UNSOURCED]

- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.
- ATR 14j et MM50 — null dans `data/latest.json` (snapshot 10h UTC).

---

## Références

- `data/latest.json` (snapshot 2026-06-10T10:00:14Z) — AST: error "No price history" ; ASTS: previous_close $92.06 (stale probable), RSI 51.78, volume 26,688,955, short interest 18.39 %, consensus FMP $94.54, options (max_pain $45.0 anomalie, put_call_ratio null, call_oi_pct null)
- `data/validation_report.txt` (2026-06-10) — [ERROR] AST: fetch failed. 5 errors total, 0 excluded.
- `data/sector_rotation_2026-06-10.json` — XLK top sectoriel (momentum 10.0/10, RS indisponible)
- `data/fx_exposure_2026-06-10.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-10.json` — Sentiment retail 0 mentions
- `data/upcoming_events_2026-06-10.json` — AST: earnings 2026-06-08 (J=0 glissant) ; ASTS: earnings 2026-08-10 (62 jours)
- `data/events_2026-06-10.json` — Aucun événement corporate détecté pour AST/ASTS
- `data/geo_risk_latest.json` (2026-05-17) — Pas de flag spécifique AST/ASTS
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
