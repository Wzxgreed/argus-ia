# FLY — Mise à Jour (2026-05-25, snapshot 21:00 UTC)

> **Type :** `_update.md` — Confirmation post-session (snapshot 21:00 UTC)
> **Référence précédente :** [FLY_2026-05-25_update.md](FLY_2026-05-25_update.md) (snapshot 17:00 UTC)
> **Données source :** `data/latest.json` (timestamp 2026-05-25T21:00:09.299648+00:00), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Validation data :** 4 erreurs globales (VRT schema, AST/AXA/CYTOMX fetch failed) — aucune affectant FLY. Pas de [CRITICAL]. Données FLY considérées fiables.
> **Note pipeline :** Snapshot 21:00 UTC reproduit strictement les mêmes données de marché que les snapshots 13:00 UTC et 17:00 UTC (marché fermé Memorial Day).

---

## Résumé — Stabilité totale vs snapshot 17:00 UTC

Le snapshot 21:00 UTC (`fetched_at: 2026-05-25T21:00:09.299648+00:00`) reproduit **strictement les mêmes données de marché** que les précédents snapshots de la journée. Aucune nouvelle séance, aucun nouveau flux de prix, volumes, options ou fondamentaux n'a été enregistré entre les snapshots.

| Métrique | 17:00 UTC | 21:00 UTC | Variation |
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
| Score Opportunité | 4.2/10 | **4.2/10** | Aucune |
| Score Global Ajusté | 31.8 | **31.8** | Aucune |
| Action | ÉVITER | **ÉVITER** | Confirmée |

**Verdict :** Thèse **ÉVITER** confirmée. Le gap de +15.49% reste non expliqué par aucun catalyst (events_latest = 0, news FLY = 0). Les fondamentaux, la structure technique et le consensus analystes sont inchangés.

---

## Mise à jour technique — Confirmée (inchangée vs 17:00 UTC)

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $49.50 | Gap +15.49% vs prior close $42.86 — **mouvement spéculatif majeur, non résolu** |
| Open | $42.93 | Gap up brutal, open = low du jour |
| High | $50.02 | Test de $50.00, rejet à $49.50 en close |
| Low | $42.93 | Aucun retracement intraday |
| RSI 14j | 72.38 | **Surachat technique** (>70) — inchangé |
| MM 50j | $34.62 | Cours supérieur de **+43.0%**, tendance haussière très étirée |
| Volume | 8,773,800 | **1.37x moy. 20j** — inchangé |
| ATR 14j | $5.01 | Volatilité élevée persistante (10.1% rel.) |
| Support 1 | $42.93 (Low du jour) | Support intraday immédiat — rupture = retour vers $39–$40 |
| Support 2 | $34.62 (MM50) | Support dynamique — rupture = révision baissière majeure |
| Résistance 1 | $50.02 (High du jour) | Testé et rejeté — psychologique $50.00 |
| Résistance 2 | $73.80 (52W High) | — |

**Timing verdict :** **Défavorable** — inchangé. Tendance haussière intacte mais extrêmement étirée. Risque de gap fill vers $43.00–$44.00 toujours présent.

---

## Mise à jour fondamentale — Inchangée (vs 17:00 UTC)

Données croisées Yahoo / FMP (annual FY 2025) — **strictement inchangées** :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $7.93B | Divergence Yahoo/FMP persistante (-57%) |
| Forward P/E | -43.36 | Pas de rentabilité nette attendue |
| EV/Revenue (Yahoo) | 40.21x | Multiple très élevé |
| P/B (Yahoo) | 7.17 | Multiple structurel élevé |
| Gross Margin (FMP) | 15.6% | Faible |
| Operating Margin (FMP) | -154.3% | Fortement négatif |
| Net Margin (FMP) | -186.6% | Fortement négatif |
| Debt/Equity (FMP) | 0.26 | Levier modéré |
| Current Ratio (FMP) | 4.51 | Liquidité solide |
| Short Interest | 8.66% | Stable — absence de squeeze setup |
| FMP Consensus PT | $42.45 (11 analysts) | **-14.2% sous le spot** |

**Filtre Qualité** : **2/6** (Hors périmètre) — inchangé.

| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans >= 20% | ❌ | Pas de données >20% (FY 2025 Revenue/Share $1.05) |
| Profit CAGR 5 ans >= 20% | ❌ | Marges négatives |
| Assets/Liabilities > 1.0 | ✅ | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | ❌ | FCF yield négatif (-7.0%) |
| Avantage compétitif (moat) | ❌ | Aucun moat structurel identifié |
| Industrie forte croissance (TAM x5) | ❌ | Aerospace & Defense en croissance, mais pas x5 pour ce profil |
| **Score Qualité total** | **2/6** | 🔴 Hors périmètre |

**Règle** : Score <= 3/6 → Score Valorisation plafonné à 5/10. L'Agent Recommandation applique **3.5/10**.

---

## Mise à jour sentiment / options / news — Inchangée (vs 17:00 UTC)

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $42.45 (11 analysts) | FMP Stable API | PT **-14.2% sous le spot** — consensus bearish vs prix actuel |
| Max Pain | $36.00 | Yahoo Finance | Expiration 29/05. Max pain **-27.3% sous le spot** |
| Put/Call Ratio | 0.74 | Yahoo Finance | Préférence call modérée |
| Call OI % | 57.4% | Yahoo Finance | Biais haussier modéré |
| Short Interest | 8.66% | Yahoo Finance | Stable |
| Social Sentiment | EXTREME_BEARISH (0.0) | `data/social_sentiment_2026-05-25.json` | Signal artefact (0 mention) — pas d'activité retail |
| Event-Driven | Aucun | `data/events_2026-05-25.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (71 jours) | `data/upcoming_events_2026-05-25.json` | Est EPS -$0.60 à -$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_2026-05-25.json` | **Aucune news spécifique** — le gap reste non expliqué |

**Score Catalyseur** : **4.0/10** — inchangé. Absence de catalyseur immédiat.

---

## Scoring global — Confirmé (Agent Recommandation, inchangé vs 17:00 UTC)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 4.0/10 | 35% | 1.40 |
| Valorisation | 3.5/10 | 40% | 1.40 |
| Momentum | 5.5/10 | 25% | 1.38 |
| **Score Opportunité** | **4.2/10** | | |
| Malus/Bonus | -10.0 pts | | Sectoriel XLI (-0.5), surachat RSI >70 (-1.5), gap non expliqué (-3.0), consensus sous spot (-2.0), volatilité extrême (-3.0) |
| **Score Global** | **41.8** | | |
| **Score Global Ajusté** | **31.8** | | |

**Action** : **ÉVITER**
**Direction** : Neutre
**Timing** : Défavorable
**Horizon** : —

**Ajustements agents complémentaires** (inchangés vs 17:00 UTC) :
- **Agent Quant** : Signaux non significatifs — pas d'ajustement.
- **Agent Geo** : FLY non flaggé — pas de malus.
- **Agent Sector Rotation** : XLI sous-performant SPY (RS 20j -4.85%, momentum_score 0.0) — headwind sectoriel persistant (-0.5 pt).
- **Agent Social** : Signal artefact — neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0 — pas d'ajustement.
- **Agent Event-Driven** : 0 événement — neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible — pas d'ajustement.

---

## Révision des niveaux SL / TP — Inchangés

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $49.50 | Close 21:00 UTC | Identique 17:00 UTC |
| Stop-loss | $39.48 | Cours - 2xATR ($5.01) | Support technique clé |
| Take-profit | $64.53 | Cours + 3xATR ($5.01) | Aligné sur l'upside mécanique |
| Ratio R/R | 1.5:1 | Gain $15.03 / Perte $10.02 | Limite pour profil sans rentabilité |

Les niveaux sont maintenus. En pratique, une cassure de $42.93 (low du jour) reste le premier signal de retournement.

---

## Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : Thèse CONFIRMÉE — ÉVITER à court terme.**

Le snapshot 21:00 UTC est **strictement identique** aux snapshots précédents de la journée (marché fermé Memorial Day). Aucun nouvel événement corporate, aucune news, aucun changement de consensus ou de fondamental n'est survenu.

**Ce qui confirme la thèse ÉVITER :**
- Gap +15.49% **toujours non expliqué** par un catalyst identifiable.
- RSI 72.38 **surachat technique confirmé**.
- Consensus analystes $42.45 **-14.2% sous le spot** — écart anomal.
- Filtre Qualité 2/6, Forward P/E -43.36, EV/Revenue 40.21x — **fondamentaux inchangés et défavorables**.
- Score Global Ajusté 31.8 — **zone ÉVITER** (< 35).
- Headwind sectoriel XLI sous-performant SPY.
- Divergence Yahoo/FMP sur Market Cap et P/B persistante — [DONNÉES PARTIELLES].

**Catalyseurs forward** (inchangés) :
1. **Earnings Q2 2026** (2026-08-04, 71 jours) : Est EPS -$0.45 à -$0.60, Rev $0.1B.
2. **Expiration options 29/05** (4 jours) : surveillance post-expiration.

**Risques** (inchangés) :
1. Rentabilité non démontrée.
2. Multiple incompatible avec un profil quality compounding.
3. Gap non expliqué — risque élevé de gap fill vers $43.00–$44.00.
4. Cours 16.3% au-dessus du consensus analystes.
5. Divergence Yahoo/FMP persistante.

**Prochaine étape :**
- **Ne pas prendre de position** — ÉVITER à court terme.
- Surveiller la consolidation post-gap : si $48.00 tient 3 séances, réévaluer.
- Surveiller l'expiration options du 29/05.
- Si cassure de $42.93 → gap fill probable, maintenir ÉVITER.
- Si un catalyst fondamental émerge → réévaluer Score Catalyseur et Filtre Qualité.
- **Vérifier la divergence Yahoo/FMP** avant la prochaine analyse.

---

*Snapshot 21:00 UTC confirme stabilité totale vs 17:00 UTC. Aucun changement matériel.*
