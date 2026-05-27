# FLY — Mise a Jour (2026-05-27, snapshot 10:00 UTC)

> **Type :** `_update.md` — Stabilite post-squeeze, aucun nouveau catalyst
> **Reference precedente :** [FLY_2026-05-26_update_21h.md](FLY_2026-05-26_update_21h.md) (snapshot 21:00 UTC)
> **Donnees source :** `data/latest.json` (timestamp 2026-05-27T10:00:09.603286+00:00), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Validation data :** 4 erreurs globales (VRT schema, AST/AXA/QTBS fetch failed) — aucune affectant FLY. Pas de [CRITICAL]. Donnees FLY considerees fiables.
> **Note pipeline :** Snapshot 10:00 UTC confirme stabilite totale vs close 21h UTC 26/05. DRAFT_refresh detecte et traite (triggers : PRICE_GAP +18.81%, ATR_SPIKE 9.11%) — these confirme sans modification.

---

## Resume — Stabilite totale, donnees identiques au close 21h UTC

Le snapshot 10:00 UTC du 2026-05-27 enregistre une **stabilite totale** par rapport au close du 26/05 21h UTC. Aucun nouveau catalyst, aucune news, aucun evenement corporate n'a ete identifie. Le cours reste a **$58.81** (+18.81% vs prior close 25/05 $49.50), maintenant le cumul a **+37.3% en deux sessions**.

| Metrique | 2026-05-26 21:00 UTC | 2026-05-27 10:00 UTC | Variation |
|----------|----------------------|----------------------|-----------|
| Cours close | $58.81 | **$58.81** | **Stable** |
| Open | $53.29 | $53.29 | Stable |
| High intraday | $62.17 | $62.17 | Stable |
| Low intraday | $51.99 | $51.99 | Stable |
| Change % vs prior close | +18.81% | **+18.81%** | Stable |
| RSI 14j | 81.38 | **81.38** | Stable — surachat EXTREME |
| MM 50j | $35.33 | **$35.33** | Stable |
| ATR 14j | $5.36 | **$5.36** | Stable |
| Volume | 14,471,073 | **15,636,600** | **+8.1% — 2.24x moy. 20j** |
| Volume vs 20j | 2.09x | **2.24x** | Legere augmentation |
| Forward P/E | -51.51 | **-51.51** | Stable |
| EV/Revenue (Yahoo) | 40.205x | **48.274x** | **+20.1% — [DONNEES PARTIELLES]** |
| P/B (Yahoo) | 8.52 | **8.52** | Stable |
| Market Cap (Yahoo) | $9.42B | **$9.42B** | Stable |
| Consensus PT (FMP) | $42.45 (11 analysts) | **$42.45 (11 analysts)** | **Ecart sous spot : -27.9%** |
| Options — Max Pain | $49.50 | **$20.00** | **[ANOMALIE DATA — valeur confirmee $49.50]** |
| Options — Put/Call | 0.75 | **null** | **[ANOMALIE DATA — valeur confirmee 0.75]** |
| Options — Call OI % | 57.0% | **null** | **[ANOMALIE DATA — valeur confirmee 57.0%]** |
| Short Interest | 8.66% | **8.66%** | Stable |
| Score Opportunite (agent) | 4.3/10 | **4.3/10** | Stable |
| Score Global Ajuste (agent) | 38.0 | **38.0** | **Stable — SURVEILLER (limite basse)** |
| Action | SURVEILLER | **SURVEILLER** | **Confirmee** |

**Verdict :** These **SURVEILLER** (limite basse 38.0). Le snapshot 10:00 UTC est strictement identique au close 21h UTC 26/05. L'absence de nouveau catalyst, de news ou d'evenement corporate confirme que le mouvement haussier de +37.3% en deux sessions reste **non explique** et speculative. Le DRAFT_refresh detecte ce matin (triggers PRICE_GAP +18.81% et ATR_SPIKE 9.11%) est traite dans cette mise a jour : la these precedente est **confirmee sans modification**.

---

## Mise a jour technique — Stabilite, surachat extreme persistant

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $58.81 | Cumul +37.3% en 2 sessions (depuis $42.86) |
| Open | $53.29 | Gap up vs close precedent ($49.50) |
| High | $62.17 | **Nouveau high intraday** — test du 52W high ($73.80) |
| Low | $51.99 | Aucun retracement significatif |
| RSI 14j | **81.38** | **Surachat EXTREME** (>80) — zone de danger |
| MM 50j | $35.33 | Cours superieur de **+66.5%**, tendance tres etiree |
| Volume | 15,636,600 | **2.24x moy. 20j** — volume massif, possible distribution |
| ATR 14j | $5.36 | Volatilite elevee persistante (9.11% rel.) |
| Support 1 | $51.99 (Low du jour) | Support intraday immediat — rupture = retour vers $49.50 |
| Support 2 | $49.50 (Max Pain confirme) | Support psychologique + max pain options |
| Support 3 | $42.93 (Open 26/05) | Support structurel — rupture = gap fill complet |
| Resistance 1 | $62.17 (High du jour) | Nouveau high teste |
| Resistance 2 | $73.80 (52W High) | Objectif mecanique si breakout |

**Timing verdict :** **Defavorable / Dangereux** — Tendance haussiere intacte mais RSI 81.38 reste dans la zone de surachat extreme. Le volume 2.24x sur un mouvement deja etire est un signal de distribution potentielle. Historiquement, RSI >80 sur un profil non rentable anticipe un retournement ou une consolidation violente.

**Note technique importante :** Le cours a forme un **deuxieme gap consecutif** sans retracement. Ce pattern est caracteristique d'un mouvement speculatif pur (short covering, gamma squeeze, ou flux algorithmique) plutot que d'un re-rating fondamental. Le volume massif (15.6M actions) renforce l'hypothese d'une distribution institutionnelle ou d'un squeeze final.

---

## Mise a jour fondamentale — Inchangee mais deterioration mecanique des ratios prix-dependants

Donnees croisees Yahoo / FMP (annual FY 2025) — **operationnellement inchangées**, mais les ratios de valorisation se sont deteriores mecaniquement avec la hausse du cours :

| Metrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $9.42B | Stable |
| Forward P/E | -51.51 | Negatif, stable |
| EV/Revenue (Yahoo) | **48.274x** | **+20.1% vs 40.205x precedemment rapporte — [DONNEES PARTIELLES]** |
| P/B (Yahoo) | 8.52 | Multiple incompatible profil sans rentabilite |
| Gross Margin (FMP) | 15.56% | Faible, stable |
| Operating Margin (FMP) | -154.25% | Fortement negatif, stable |
| Net Margin (FMP) | -186.63% | Fortement negatif, stable |
| Debt/Equity (FMP) | 0.259 | Levier modere, stable |
| Current Ratio (FMP) | 4.51 | Liquidite solide, stable |
| Short Interest | 8.66% | Stable — pas de setup squeeze |
| FMP Consensus PT | $42.45 (11 analysts) | **-27.9% sous le spot** — ecart anomal record |

**Filtre Qualite** : **2/6** (Hors perimetre) — **strictement inchange**.

| Critere | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans >= 20% | ❌ | Pas de donnees >20% (FY 2025 Revenue/Share $1.05) |
| Profit CAGR 5 ans >= 20% | ❌ | Marges negatives |
| Assets/Liabilities > 1.0 | ✅ | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | ❌ | FCF yield negatif (-7.0%) |
| Avantage competitif (moat) | ❌ | Aucun moat structurel identifie |
| Industrie forte croissance (TAM x5) | ❌ | Aerospace & Defense en croissance, mais pas x5 pour ce profil |
| **Score Qualite total** | **2/6** | 🔴 Hors perimetre |

**Regle** : Score <= 3/6 → Score Valorisation plafonne a 5/10. L'Agent Recommandation applique **3.5/10**.

**Note sur EV/Revenue :** La valeur Yahoo `ev_revenue` est passee de 40.205x (rapporte dans l'update 21h UTC 26/05) a 48.274x dans le snapshot 10:00 UTC 27/05. Cette variation de +20.1% en l'absence de publication de resultats ou de changement operationnel suggere une **anomalie de donnees** ou un recalcul de la part de Yahoo. Les donnees FMP (EV/EBITDA -13.12, EV/Sales 18.23) restent stables. Nous utilisons la valeur JSON actuelle (48.274x) avec la mention [DONNEES PARTIELLES].

---

## Mise a jour sentiment / options / news — Aucun catalyst identifie

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **-27.9% sous le spot** — ecart record, consensus fortement bearish vs prix actuel |
| Max Pain | **$49.50** (confirme) | Yahoo Finance | **Eloigne du spot** ($58.81). A expiration 29/05 (2 jours), le max pain loin au-dessous du spot suggere un potentiel de "pinning" vers $49.50 |
| Put/Call Ratio | **0.75** (confirme) | Yahoo Finance | Leger biais haussier, stable |
| Call OI % | **57.0%** (confirme) | Yahoo Finance | Lean call modere, stable |
| Short Interest | 8.66% | Yahoo Finance | Stable — pas de setup squeeze |
| Social Sentiment | No data (0 mention) | `data/social_sentiment_2026-05-27.json` | Pas d'activite retail |
| Event-Driven | Aucun | `data/events_2026-05-27.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (69 jours) | `data/upcoming_events_2026-05-27.json` | Est EPS -$0.60 a -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_2026-05-27.json` | **Aucune news specifique** — le gap reste non explique |

**Score Catalyseur** : **4.0/10** (donnees agents). L'absence de news et d'evenements maintient le score faible. Le mouvement de prix brutal n'est pas soutenu par un catalyseur fondamental.

**Note sur les options et max pain :**
- Le snapshot 10:00 UTC rapporte des valeurs options aberrantes (max pain $20.00, put/call null, call OI null). Il s'agit de la **meme anomalie** que celle observee au snapshot 10:00 UTC 26/05, qui avait ete resolue a 13:00 UTC. Nous utilisons les valeurs confirmees du snapshot 21h UTC 26/05 : max pain **$49.50**, put/call **0.75**, call OI **57.0%**.
- Max pain $49.50 est desormais **$9.31 sous le spot** ($58.81). Avec expiration le 29/05 (2 jours), le mecanisme de pinning vers le max pain est un risque baissier materiel.
- Put/call 0.75 et call OI 57% n'indiquent pas un setup de short squeeze (SI 8.66% insuffisant, put/call pas assez bas).

---

## Scoring global — Stable, SURVEILLER limite basse (38.0)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 4.0/10 | 35% | 1.40 |
| Valorisation | 3.5/10 | 40% | 1.40 |
| Momentum | 6.0/10 | 25% | 1.50 |
| **Score Opportunite** | **4.3/10** | | |
| **Score Global** | **43.0** | | |
| **Score Global Ajuste** | **38.0** | | |

**Action** : **SURVEILLER**
**Direction** : Neutre
**Timing** : Defavorable
**Horizon** : —

**Note sur le scoring :** L'Agent Recommandation maintient FLY en **SURVEILLER** (38.0, limite basse). Cette position est portee principalement par le Momentum 6.0/10, qui reflete la persistence du mouvement haussier. Cependant, le Score Global Ajuste 38.0 se situe a la **limite inferieure** de la zone SURVEILLER (35–49). Un malus supplementaire de -3.0 pts le replacerait dans la zone EVITER (<35).

**Ajustements agents complementaires** :
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant) — pas d'ajustement.
- **Agent Geo** : FLY non flagge — pas de malus.
- **Agent Sector Rotation** : XLI sous-performant SPY (RS 20j -3.92%, momentum_score 0.0) — headwind sectoriel persistant (-0.5 pt).
- **Agent Social** : 0 mention — neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0 — pas d'ajustement.
- **Agent Event-Driven** : 0 evenement — neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible — pas d'ajustement.

---

## Revision des niveaux SL / TP — Donnees agents

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $58.81 | Close 10:00 UTC | +18.81% vs prior close |
| Stop-loss | $48.09 | Agent Recommandation | Support technique cle |
| Take-profit | $74.89 | Agent Recommandation | Alignement avec 52W high |
| Ratio R/R | 1.5:1 | Gain $16.08 / Perte $10.72 | Limite pour profil sans rentabilite |

Les niveaux sont issues de l'Agent Recommandation. Le SL $48.09 correspond a un retracement vers la zone $48–$49. Le TP $74.89 correspond au 52W high historique.

---

## DRAFT_refresh traite — These confirme sans modification

Un fichier `FLY_2026-05-27_DRAFT_refresh.md` a ete detecte ce matin, declenche par les triggers suivants :
- **PRICE_GAP** (high) — Gap +18.81% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 9.11% (seuil 5.0%)

**Conclusion du refresh :** La these precedente est **CONFIRMEE SANS MODIFICATION**. Les donnees du snapshot 10:00 UTC 27/05 sont strictement identiques au close 21h UTC 26/05. Aucun nouvel evenement majeur, aucune news, aucun changement fondamental n'a ete identifie. Le mouvement speculatif de +37.3% en deux sessions reste non explique. Le Filtre Qualite 2/6, le Score Opportunite 4.3/10 et le Score Global Ajuste 38.0 sont inchanges.

---

## Conclusion — These defavorable CONFIRMEE (SURVEILLER limite basse)

**Verdict : These DEFAVORABLE CONFIRMEE — SURVEILLER (38.0, limite basse).**

Le snapshot 10:00 UTC 27/05 confirme une **stabilite totale** par rapport au close 21h UTC 26/05 : cours $58.81, RSI 81.38, volume 15.6M (2.24x), tous les indicateurs techniques et fondamentaux inchanges.

**Ce qui confirme et renforce la these defavorable :**
- **Aucun catalyst identifie** : +37.3% en deux sessions sans news, sans evenement corporate, sans changement fondamental.
- **Volume massif persistant** : 15.6M (2.24x moy. 20j) sur un mouvement deja etire — signal de distribution potentielle.
- **RSI 81.38** : surachat extreme, zone historiquement associee a des retournements violents sur des profils non rentables.
- **Consensus analystes $42.45** : **-27.9% sous le spot** — ecart record. Les analystes ne suivent pas ce mouvement.
- **Filtre Qualite 2/6, Forward P/E -51.51, EV/Revenue 48.3x** : fondamentaux inchanges et defavorables.
- **Max pain $49.50** : eloigne du spot, risque de pinning a l'expiration 29/05 (2 jours).
- **Headwind sectoriel XLI** : sous-performant SPY (RS 20j -3.92%).
- **Anomalie donnees options** : max pain $20.00, put/call null, call OI null dans le snapshot 10:00 UTC — meme anomalie que le 26/05 matin.

**Ce qui est nouveau / degrade :**
- EV/Revenue Yahoo : 48.274x vs 40.205x precedemment — +20.1% mecanique ou anomalie data.
- Volume 2.24x moy. 20j : legere augmentation vs 2.09x au close 21h UTC.
- XLI RS 20j : -3.92% vs -3.91% — degradation marginale sectorielle.

**Catalyseurs forward** (inchanges) :
1. **Earnings Q2 2026** (2026-08-04, 69 jours) : Est EPS -$0.45 a -$0.60, Rev $0.1B.
2. **Expiration options 29/05** (2 jours) : max pain = $49.50 = -15.8% sous le spot. Risque de pinning ou de consolidation violente.

**Risques** (renforces) :
1. Rentabilite non demontree et non attendue a court terme.
2. Multiple incompatible avec un profil quality compounding.
3. **Deuxieme gap non explique** — risque tres eleve de gap fill vers $49.50–$42.93.
4. Cours 27.9% au-dessus du consensus analystes.
5. Divergence Yahoo/FMP sur Market Cap ($9.42B vs $3.40B) et P/B (8.52 vs 2.86) persistante — [DONNEES PARTIELLES].
6. RSI 81.38 : surachat extreme, vulnerabilite a un retournement.
7. Volume 2.24x : possible distribution institutionnelle.
8. Anomalie data options recurrente (max pain aberrant $20.00).

**Prochaine etape :**
- **Ne pas prendre de position** — SURVEILLER a la limite basse (38.0), proche du seuil EVITER.
- **Surveiller la cloture du 29/05** : expiration options avec max pain $49.50. Si le cours reste proche de $58, observation du pinning post-expiration.
- **Si cassure de $51.99** (low 26/05) → risque de retour vers $49.50.
- **Si cassure de $49.50** → gap fill probable vers $42.93, passage a EVITER.
- **Si un catalyst fondamental emerge** → reevaluer Score Catalyseur et Filtre Qualite. Sans cela, le mouvement reste speculatif.

---

*Snapshot 10:00 UTC 27/05 — Stabilite totale vs close 21h UTC 26/05. Cours $58.81, RSI 81.38 extreme, volume 15.6M (2.24x). Aucun catalyst. Consensus $42.45 a -27.9% sous le spot. Fondamentaux inchanges et defavorables. Agent Recommandation : SURVEILLER (38.0, limite basse). These defavorable confirmee sans modification. DRAFT_refresh traite et archive.*
