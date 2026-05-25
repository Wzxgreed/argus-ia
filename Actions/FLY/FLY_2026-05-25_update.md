# FLY — Mise a Jour (2026-05-25, snapshot 17:00 UTC)

> **Type :** `_update.md` — Confirmation post-session (snapshot 17:00 UTC)
> **Reference precedente :** [FLY_2026-05-25_update.md](FLY_2026-05-25_update.md) (snapshot 13:00 UTC)
> **Donnees source :** `data/latest.json` (timestamp 2026-05-25T17:00:08.609297+00:00), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/news_latest.json`
> **Validation data :** 4 erreurs globales (VRT schema, AST/AXA/CYTOMX fetch failed) — aucune affectant FLY. Pas de [CRITICAL]. Donnees FLY considerees fiables.
> **Note pipeline :** Snapshot 17:00 UTC reproduit strictement les memes donnees de marche que le snapshot 13:00 UTC (marche ferme Memorial Day).

---

## Resume — Stabilite totale vs snapshot 13:00 UTC

Le snapshot 17:00 UTC (`fetched_at: 2026-05-25T17:00:08.609297+00:00`) reproduit **strictement les memes donnees de marche** que le snapshot 13:00 UTC et le snapshot 10:00 UTC. Aucune nouvelle seance, aucun nouveau flux de prix, volumes, options ou fondamentaux n'a ete enregistre entre les snapshots.

| Metrique | 13:00 UTC | 17:00 UTC | Variation |
|----------|-----------|-----------|-----------|
| Cours close | $49.50 | **$49.50** | Aucune |
| Change % | +15.49% | **+15.49%** | Aucune |
| RSI 14j | 72.38 | **72.38** | Aucune |
| MM 50j | $34.62 | **$34.62** | Aucune |
| ATR 14j | $5.01 | **$5.01** | Aucune |
| Volume | 8,773,800 | **8,773,800** | Aucune |
| Forward P/E | -43.36 | **-43.36** | Aucune |
| EV/Revenue | 40.21x | **40.21x** | Aucune |
| Consensus PT (FMP) | $42.45 (11 analysts) | **$42.45 (11 analysts)** | Aucune |
| Options — Max Pain | $36.00 (exp. 29/05) | **$36.00 (exp. 29/05)** | Aucune |
| Options — Put/Call | 0.74 | **0.74** | Aucune |
| Score Opportunite | 4.2/10 | **4.2/10** | Aucune |
| Score Global Ajuste | 31.8 | **31.8** | Aucune |
| Action | EVITER | **EVITER** | Confirmee |

**Verdict :** These **EVITER** confirmee. Le gap de +15.49% reste non explique par aucun catalyst (events_latest = 0, news FLY = 0). Les fondamentaux, la structure technique et le consensus analystes sont inchanges.

---

## Mise a jour technique — Confirmee (inchangee vs 13:00 UTC)

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $49.50 | Gap +15.49% vs prior close $42.86 — **mouvement speculatif majeur, non resolu** |
| Open | $42.93 | Gap up brutal, open = low du jour |
| High | $50.02 | Test de $50.00, rejet a $49.50 en close |
| Low | $42.93 | Aucun retracement intraday |
| RSI 14j | 72.38 | **Surachat technique** (>70) — inchangé |
| MM 50j | $34.62 | Cours superieur de **+43.0%**, tendance haussiere tres etiree |
| Volume | 8,773,800 | **1.37x moy. 20j** — inchangé |
| ATR 14j | $5.01 | Volatilite elevee persistante (10.1% rel.) |
| Support 1 | $42.93 (Low du jour) | Support intraday immediat — rupture = retour vers $39–$40 |
| Support 2 | $34.62 (MM50) | Support dynamique — rupture = revision baissiere majeure |
| Resistance 1 | $50.02 (High du jour) | Teste et rejete — psychologique $50.00 |
| Resistance 2 | $73.80 (52W High) | — |

**Timing verdict :** **Defavorable** — inchangé. Tendance haussiere intacte mais extremement etiree. Risque de gap fill vers $43.00–$44.00 toujours present.

---

## Mise a jour fondamentale — Inchangee (inchangee vs 13:00 UTC)

Donnees croisees Yahoo / FMP (annual FY 2025) — **strictement inchangées vs snapshot 13:00 UTC** :

| Metrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $7.93B | Divergence Yahoo/FMP persistante (-57%) |
| Forward P/E | -43.36 | Pas de rentabilite nette attendue |
| EV/Revenue (Yahoo) | 40.21x | Multiple tres eleve |
| P/B (Yahoo) | 7.17 | Multiple structurel eleve |
| Gross Margin (FMP) | 15.6% | Faible |
| Operating Margin (FMP) | -154.3% | Fortement negatif |
| Net Margin (FMP) | -186.6% | Fortement negatif |
| Debt/Equity (FMP) | 0.26 | Levier modere |
| Current Ratio (FMP) | 4.51 | Liquidite solide |
| Short Interest | 8.66% | Stable — absence de squeeze setup |
| FMP Consensus PT | $42.45 (11 analysts) | **-14.2% sous le spot** |

**Filtre Qualite** : **2/6** (Hors perimetre) — inchangé.

| Critere | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans >= 20% | ❌ | Pas de donnees >20% (FY 2025 Revenue/Share $1.05) |
| Profit CAGR 5 ans >= 20% | ❌ | Marges negatives |
| Assets/Liabilities > 1.0 | ✅ | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | ❌ | FCF yield negatif (-7.0%) |
| Avantage competitif (moat) | ❌ | Aucun moat structurel identifie |
| Industrie forte croissance (TAM x5) | ❌ | Aerospace & Defense en croissance, mais pas x5 pour ce profil |
| **Score Qualite total** | **2/6** | 🔴 Hors perimetre |

**Regle** : Score <= 3/6 -> Score Valorisation plafonne a 5/10. L'Agent Recommandation applique **3.5/10**.

---

## Mise a jour sentiment / options / news — Inchangee (inchangee vs 13:00 UTC)

| Signal | Valeur | Source | Interpretation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **-14.2% sous le spot** — consensus bearish vs prix actuel |
| Max Pain | $36.00 | Yahoo Finance | Expiration 29/05. Max pain **-27.3% sous le spot** |
| Put/Call Ratio | 0.74 | Yahoo Finance | Preference call moderee |
| Call OI % | 57.4% | Yahoo Finance | Biais haussier modere |
| Short Interest | 8.66% | Yahoo Finance | Stable |
| Social Sentiment | EXTREME_BEARISH (0.0) | `data/social_sentiment_2026-05-25.json` | Signal artefact (0 mention) — pas d'activite retail |
| Event-Driven | Aucun | `data/events_2026-05-25.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (71 jours) | `data/upcoming_events_2026-05-25.json` | Est EPS -$0.60 a -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_2026-05-25.json` | **Aucune news specifique** — le gap reste non explique |

**Score Catalyseur** : **4.0/10** — inchangé. Absence de catalyseur immediat.

---

## Scoring global — Confirme (Agent Recommandation, inchangé vs 13:00 UTC)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 4.0/10 | 35% | 1.40 |
| Valorisation | 3.5/10 | 40% | 1.40 |
| Momentum | 5.5/10 | 25% | 1.38 |
| **Score Opportunite** | **4.2/10** | | |
| Malus/Bonus | -10.0 pts | | Sectoriel XLI (-0.5), surachat RSI >70 (-1.5), gap non explique (-3.0), consensus sous spot (-2.0), volatilite extreme (-3.0) |
| **Score Global** | **41.8** | | |
| **Score Global Ajuste** | **31.8** | | |

**Action** : **EVITER**
**Direction** : Neutre
**Timing** : Defavorable
**Horizon** : —

**Ajustements agents complementaires** (inchanges vs 13:00 UTC) :
- **Agent Quant** : Signaux non significatifs — pas d'ajustement.
- **Agent Geo** : FLY non flagge — pas de malus.
- **Agent Sector Rotation** : XLI sous-performant SPY (RS 20j -4.85%, momentum_score 0.0) — headwind sectoriel persistant (-0.5 pt).
- **Agent Social** : Signal artefact — neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0 — pas d'ajustement.
- **Agent Event-Driven** : 0 evenement — neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible — pas d'ajustement.

---

## Revision des niveaux SL / TP — Inchanges

| Niveau | Valeur | Methode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $49.50 | Close 17:00 UTC | Identique 13:00 UTC |
| Stop-loss | $39.48 | Cours - 2xATR ($5.01) | Support technique cle |
| Take-profit | $64.53 | Cours + 3xATR ($5.01) | Aligne sur l'upside mecanique |
| Ratio R/R | 1.5:1 | Gain $15.03 / Perte $10.02 | Limite pour profil sans rentabilite |

Les niveaux sont maintenus. En pratique, une cassure de $42.93 (low du jour) reste le premier signal de retournement.

---

## Conclusion — These confirmee, modifiee ou invalidee ?

**Verdict : These CONFIRMEE — EVITER a court terme.**

Le snapshot 17:00 UTC est **strictement identique** au snapshot 13:00 UTC (marche ferme Memorial Day). Aucun nouvel evenement corporate, aucune news, aucun changement de consensus ou de fondamental n'est survenu.

**Ce qui confirme la these EVITER :**
- Gap +15.49% **toujours non explique** par un catalyst identifiable.
- RSI 72.38 **surachat technique confirme**.
- Consensus analystes $42.45 **-14.2% sous le spot** — ecart anomal.
- Filtre Qualite 2/6, Forward P/E -43.36, EV/Revenue 40.21x — **fondamentaux inchanges et defavorables**.
- Score Global Ajuste 31.8 — **zone EVITER** (< 35).
- Headwind sectoriel XLI sous-performant SPY.
- Divergence Yahoo/FMP sur Market Cap et P/B persistante — [DONNEES PARTIELLES].

**Catalyseurs forward** (inchanges) :
1. **Earnings Q2 2026** (2026-08-04, 71 jours) : Est EPS -$0.45 a -$0.60, Rev $0.1B.
2. **Expiration options 29/05** (4 jours) : surveillance post-expiration.

**Risques** (inchanges) :
1. Rentabilite non demontree.
2. Multiple incompatible avec un profil quality compounding.
3. Gap non explique — risque eleve de gap fill vers $43.00–$44.00.
4. Cours 16.3% au-dessus du consensus analystes.
5. Divergence Yahoo/FMP persistante.

**Prochaine etape :**
- **Ne pas prendre de position** — EVITER a court terme.
- Surveiller la consolidation post-gap : si $48.00 tient 3 seances, reevaluer.
- Surveiller l'expiration options du 29/05.
- Si cassure de $42.93 -> gap fill probable, maintenir EVITER.
- Si un catalyst fondamental emerge -> reevaluer Score Catalyseur et Filtre Qualite.
- **Verifier la divergence Yahoo/FMP** avant la prochaine analyse.

---

*Snapshot 17:00 UTC confirme stabilite totale vs 13:00 UTC. Aucun changement materiel.*
