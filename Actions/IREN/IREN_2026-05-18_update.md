# IREN — Mise a Jour Quotidienne (2026-05-18)

> **Type :** `_update.md` — Mise a jour post-pipeline (revue manuelle post-DAG)
> **Reference precedente :** [IREN_2026-05-17_init.md](IREN_2026-05-17_init.md)
> **DRAFT refresh traites :** `_DRAFT_refresh_2026-05-18.md` + `IREN_2026-05-18_DRAFT_refresh.md` — triggers PRICE_GAP -9.35% + ATR_SPIKE 10.39% (duplicatas de la session precedente)
> **Donnees source :** `data/latest.json` (timestamp 2026-05-18T13:00:07 UTC)

---

## Resume des Changements

| Metrique | 2026-05-17 (init) | 2026-05-18 (update) | Δ |
|----------|-------------------|----------------------|---|
| **Cours close** | $58.40 | $52.94 | **-9.35%** (gap du 2026-05-17, stable ce jour) |
| **Volume** | — | 48.5 M | 0.93× moy. 20j |
| **RSI 14j** | — | 54.61 | Zone neutre favorable |
| **ATR 14j** | — | 5.50 | Volatilite elevee (beta 4.18) |
| **MM 50j** | — | $44.72 | Cours +18.4% au-dessus |
| **P/E TTM** | 68.75× | 68.75× | **Inchange** |
| **Forward P/E** | -39.36× | -39.36× | **Inchange** |
| **EV/EBITDA (Yahoo)** | 140.45× | 140.45× | **Inchange** |
| **P/B (Yahoo)** | 6.99× | 6.99× | **Inchange** |
| **Beta** | 4.18 | 4.18 | **Inchange** |
| **Short Interest** | 0.17% | 0.17% | **Inchange** |
| **Put/Call ratio** | 1.47 | 1.55 | **↑ 0.08** — legerement plus baissier |
| **Max Pain** | $33.00 | $33.00 | **Inchange** |
| **BTC-USD** | — | $78,144 | -1.17% |
| **Score Opportunite** | 5.8/10 | **5.8/10** | **Inchange** |
| **Score Global ajuste** | 63.3/100 | **63.3/100** | **Inchange** |

**Verdict :** Les donnees brutes (cours, volumes, ratios, scores agents) sont **identiques** au snapshot 13:00 UTC du 2026-05-18. Aucun nouveau mouvement directionnel ni flux fondamental post-earnings n'a ete integre dans les feeds Yahoo/FMP. L'**earnings call Q1 2026 (FY Q3, exercice juin)** est programme aujourd'hui — les resultats ne sont pas encore disponibles dans `data/latest.json`. Les triggers du DRAFT full refresh (PRICE_GAP -9.35%, ATR_SPIKE 10.39%) sont des **duplicatas** de la session precedente ; ils confirment la volatilite inherente mais **n'invalident pas** la these.

---

## Mise a Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 54.61 | Zone neutre favorable, ni surachat ni survente |
| **ATR 14j** | $5.50 | Volatilite elevee mais stable (beta 4.18) |
| **MM 50j** | $44.72 | Cours **+18.4% au-dessus** — tendance haussiere intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 52.4 M | Volume du jour 48.5 M = **92.5%** du moyen |
| **Range intraday** | $52.86 – $56.79 | Aucune cassure de support ni de resistance |
| **52-week high/low** | $76.87 / $8.11 | Cours a **68.9%** du 52W high |

**Niveaux cles :**
- Support immediat : $52.86 (low du jour)
- Support structurel : $50.00 (psychologique) puis MM50 $44.72
- Resistance : $56.79 (high du jour) puis $58.40 (close pre-gap)
- Stop-loss (2×ATR) : **$41.94** — inchange
- Take-profit (3×ATR) : **$69.44** — inchange
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — structure technique intacte au-dessus de la MM50, RSI neutre propice. La volatilite extreme (beta 4.18) impose un sizing reduit strict.

---

## Mise a Jour Fondamentale

**Aucun nouveau flux fondamental** depuis l'init du 2026-05-17. Les donnees FMP restent au FY 2025 (clos 2025-06-30). **Point de vigilance majeur : divergence Yahoo vs FMP sur les metriques de valorisation.**

| Metrique | Yahoo Finance | FMP Stable API | Ecart | Source preferee |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $18.92 B | $3.13 B | **-83%** | Yahoo (coherent avec close × shares out.) |
| **EV/EBITDA** | 140.45× | 17.48× | **-88%** | Yahoo (FMP market cap errone infecte l'EV) |
| **P/B** | 6.99× | 1.72× | **-75%** | Yahoo |
| **P/E TTM** | 68.75× | 35.96× | **-48%** | Yahoo |
| **EV/Sales** | 27.30× | 7.04× | **-74%** | Yahoo |

**Diagnostic divergence :** Le market cap FMP ($3.13B) est incompatible avec le cours $52.94 et 357M shares outstanding ($18.9B theorique). Les metriques FMP derivees de cette base (EV multiples, P/B, P/S) sont donc **non fiables** pour IREN. Cela peut indiquer :
1. FMP reference une ancienne classe d'actions ou une entite filiale (ex : IREN Australia vs IREN Limited NASDAQ)
2. Donnees FMP non reconciliees post-restructuration ou ADS conversion
3. Lag de mise a jour FMP vs Yahoo

**Metriques fondamentales retenues (source Yahoo, cross-check FMP raw ratios) :**

| Metrique | Valeur | Signal |
|----------|--------|--------|
| **Market Cap** | $18.92 B | — |
| **P/E TTM** | 68.75× | Tres eleve — prime IA/mining |
| **Forward P/E** | -39.36× | **Negatif — pas de profitabilite forward attendue** |
| **EV/EBITDA** | 140.45× | Extreme — prix du pivot IA inclus |
| **P/B** | 6.99× | Eleve |
| **Gross Margin** | 68.3% | Bon (infrastructure a forte marge) |
| **EBITDA Margin** | 40.3% | Bon |
| **Operating Margin** | 3.46% | Faible — couts operationnels eleves |
| **Net Margin** | 17.4% | Rentable au net sur FY 2025 |
| **Debt/Equity** | 53.1% | Modere |
| **Interest Coverage** | 1.57× | Faible — pression si taux montent |
| **FCF Yield** | -36.0% | **Cash burn confirme** |
| **Capex/Revenue** | 2.7% | Modere |
| **ROIC (FMP)** | 0.58% | Tres faible — capital pas encore rentable |
| **ROE (FMP)** | 4.78% | Faible |
| **Net Debt/EBITDA (FMP)** | 1.98× | Modere |

**Filtre Qualite : 4/6 — ⚠️ Quality Partielle** (inchange)
- ❌ Forward P/E negatif (pas de profitabilite forward)
- ❌ FCF negatif (price_to_fcf = -2.77)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29)
- ✅ Gross Margin 68.3% (infrastructure a forte marge)
- ✅ EBITDA Margin 40.3%
- ⚠️ Moat / TAM : le contrat NVIDIA $3.4B est un catalyseur mais pas encore un moat structurel prouve

> **⚠️ Points de vigilance earnings (Q1 2026, FY Q3, exercice juin) :**
> 1. Guidance HPC/IA : quel % du CA guide provient du contrat NVIDIA ?
> 2. Marges HPC vs legacy mining — Operating Margin 3.5% doit s'ameliorer
> 3. FCF : sur le chemin du positif ? Capex/OCF 5.6× est eleve
> 4. Dette / renociation sous taux 10Y a ~4.6%
> 5. ROIC : le pivot IA doit montrer une amelioration de la rentabilite du capital

---

## Mise a Jour Sentiment / Options / News

| Signal | Valeur | Evolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $65.86 (21 analysts) | **Inchange** |
| **Max Pain** | $33.00 | **Inchange** — niveau tres bas, attention |
| **Put/Call ratio** | 1.55 | **↑ 0.08** depuis l'init — sentiment options legerement plus baissier |
| **Call OI %** | 39.2% | — |
| **Short Interest** | 0.17% | Tres faible — pas de short squeeze setup |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz Reddit/Yahoo |
| **Event-Driven** | Aucun evenement | `data/events_latest.json` vide pour IREN |

**Agent Crypto-Correlation (2026-05-17) :**
- Correlation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Divergence Score : **4/10**
- Premium vs NAV estime : **+12%**
- Verdict : *Fortement correle — pivot IA non encore price*

**Commentaire :** L'absence totale de mention sur les reseaux sociaux et le max pain a $33 (très en dessous du cours) suggerent soit une option activity tres faible, soit des donnees options partielles. Le titre reste un proxy BTC avec beta 2.1. Le max pain a $33 represente un risque de queue important — si les resultats decoi vent, la gravite technique vers $33 est theoriquement possible (distance -38%).

---

## Scoring Global (Agent Recommandation — 2026-05-18)

| Axe | Score | Pondération | Poids ajuste |
|-----|-------|-------------|--------------|
| **Catalyseur** | 7.8/10 | 35% | 2.73 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 6.0/10 | 25% | 1.50 |
| **Score Opportunite** | **5.8/10** | | |

**Malus/Bonus appliques :**
- Geo Risk Score 3/10 → malus faible (-5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : donnees manquantes (M-Score, Z-Score non disponibles dans `data/accounting_risk_latest.json`) — [DONNEES MANQUANTES]
- Event-Driven : aucun malus/bonus (pas d'evenement detecte)
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10/10), XLE bullish crossover — IREN est expose Technology/IA Infrastructure, aligne partiellement avec le momentum sectoriel → leger contexte favorable

| Score brut | Malus | Bonus | **Score Global ajuste** |
|------------|-------|-------|------------------------|
| 58.3/100 | -5.0 | +10.0 | **63.3/100** |

**Action recommandee : ACHETER — Sizing Reduit**
- Prix d'entree suggere : $52.94
- Stop-loss : $41.94 (-20.8%)
- Take-profit : $69.44 (+31.1%)
- Ratio R/R : 1.5 : 1
- Horizon : 1–3 mois
- Timing : Favorable

> **⚠️ Avertissement :** La recommandation agent est basee sur des donnees **pre-earnings** (FY 2025). L'annonce du Q1 2026, attendue aujourd'hui, peut modifier radicalement le score Catalyseur et Valorisation. Le sizing reduit est imperatif compte tenu du beta 4.18 et de la correlation BTC 0.82. Le max pain $33 represente un risque de queue importante (-38%) en cas de guidance cut severe.

---

## Scenarios Post-Earnings (Mise a jour)

| Scenario | Conditions | Impact cours estime | Action |
|----------|------------|---------------------|--------|
| **Optimiste (25%)** | Beat revenue + guidance HPC forte + FCF positif + ROIC > 5% | +15–25% → $61–$66 | **Renforcer** — pivot IA valide |
| **Central (50%)** | Inline + guidance inchangee + FCF stable | ±5% → $50–$56 | **Conserver** — these inchangee |
| **Pessimiste (25%)** | Miss + compression marges + guidance cut + ROIC stagnant | -15–25% → $40–$45 (-38% tail risk vers max pain $33) | **Reduire** — revalorisation necessaire |

**Prix cible revise :** $65.86 (consensus FMP, 21 analysts) — **inchange en l'absence de nouveaux resultats.**

---

## Conclusion

**These : CONFIRMEE — avec reserve earnings et divergence donnees FMP**

La structure technique et fondamentale d'IREN est **inchangee** par rapport a l'init du 2026-05-17. Le gap de -9.35% n'a pas ete comble ni creuse — le titre est fige en attendant les resultats du Q1 2026. Les triggers du DRAFT full refresh (PRICE_GAP -9.35%, ATR_SPIKE 10.39%) sont des **duplicatas** de la session precedente ; ils confirment la volatilite inherente au titre mais **n'invalident pas la these** : le pivot IA/HPC reste le catalyseur structurant, la MM50 est intacte, et le consensus maintient son PT a $65.86.

**Points cles :**
1. **Cours stable** a $52.94 post-gap — aucun mouvement directionnel intraday
2. **Earnings J-0** — resultats non encore disponibles dans les donnees FMP/Yahoo (fetch 13:00 UTC)
3. **Score Opportunite 5.8/10** inchange — Catalyseur fort (7.8) compense Valorisation faible (4.0)
4. **Filtre Qualite 4/6** inchange — Quality Partielle, FCF negatif persistant, ROIC 0.6% tres faible
5. **Divergence Yahoo/FMP** : market cap, EV/EBITDA, P/B — FMP non fiable pour IREN, privilegier Yahoo
6. **Proxy BTC intact** — correlation 0.82, beta 2.1, divergence score 4/10
7. **Max pain $33** — tres eloigne du cours, tail risk important en cas de guidance cut severe
8. **Sector rotation** : XLK top momentum, XLE bullish crossover — contexte macro modere ment favorable aux infrastructures physiques

**Recommandation :** Maintenir l'**ACHETER a sizing reduit** avec SL $41.94 / TP $69.44, **MAIS** attendre la publication des resultats Q1 2026 avant toute nouvelle entree. Le beta 4.18, le FCF negatif et le ROIC 0.6% imposent une discipline de sizing stricte. Si earnings beat + guidance HPC forte, le catalyseur pourrait justifier un relevement du score Valorisation et un renforcement de position.

---

*Rapport genere le 2026-05-18 — Donnees sources : data/latest.json, data/recommandations_latest.json, data/crypto_correlation_latest.json, data/geo_risk_latest.json, data/fx_exposure_latest.json, data/social_sentiment_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/sector_rotation_latest.json*
