# IREN — Mise à Jour Quotidienne (2026-05-18)

> **Type :** `_update.md` — Mise à jour post-gap + earnings J-0 + traitement DRAFT full refresh
> **Référence précédente :** [IREN_2026-05-18_update.md](IREN_2026-05-18_update.md) (même séance, données inchangées)
> **DRAFT refresh traité :** `_DRAFT_refresh_2026-05-18.md` — triggers PRICE_GAP -9.35% + ATR_SPIKE 10.39%

---

## Résumé des Changements

| Métrique | 2026-05-17 (init) | 2026-05-18 (update) | Δ |
|----------|-------------------|----------------------|---|
| **Cours close** | $58.40 | $52.94 | **-9.35%** |
| **Volume** | — | 48.5 M | 0.93× moy. 20j |
| **RSI 14j** | — | 54.61 | Zone neutre favorable |
| **ATR 14j** | — | 5.50 | Volatilité extrême |
| **MM 50j** | — | $44.72 | Cours +18.4% au-dessus |
| **P/E TTM** | 68.75× | 68.75× | **Inchangé** |
| **Forward P/E** | -39.36× | -39.36× | **Inchangé** |
| **EV/EBITDA (Yahoo)** | 140.45× | 140.45× | **Inchangé** |
| **EV/EBITDA (FMP)** | 17.48× | 17.48× | Divergence Yahoo/FMP — voir § fondamental |
| **P/B (Yahoo)** | 6.99× | 6.99× | **Inchangé** |
| **P/B (FMP)** | 1.72× | 1.72× | Divergence Yahoo/FMP |
| **Beta** | 4.18 | 4.18 | **Inchangé** |
| **Short Interest** | 0.17% | 0.17% | **Inchangé** |
| **Max Pain** | $33.00 | $20.00 | **↓ $13.00** |
| **BTC-USD** | — | $78,144 | -1.17% |
| **Score Opportunité** | 5.8/10 | **5.8/10** | **Inchangé** |
| **Score Global ajusté** | 63.3/100 | **63.3/100** | **Inchangé** |

**Verdict :** Le cours est figé à $52.94 depuis le gap de -9.35% d'hier. Les données techniques et fondamentales brutes sont identiques. **L'earnings call Q1 2026 est programmé aujourd'hui (J-0)** — résultats non encore intégrés dans les feeds FMP/Yahoo au moment du fetch 08:44 UTC. Le DRAFT full refresh a été traité : les triggers (gap + ATR spike) confirment la volatilité inhérente mais **n'invalident pas** la thèse.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 54.61 | Zone neutre favorable, ni surachat ni survente |
| **ATR 14j** | $5.50 | Volatilité élevée mais stable (beta 4.18) |
| **MM 50j** | $44.72 | Cours **+18.4% au-dessus** — tendance haussière intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 52.4 M | Volume du jour 48.5 M = **92.5%** du moyen |
| **Range intraday** | $52.86 – $56.79 | Aucune cassure de support ni de résistance |
| **52-week high/low** | $76.87 / $8.11 | Cours à **68.9%** du 52W high |

**Niveaux clés :**
- Support immédiat : $52.86 (low du jour)
- Support structurel : $50.00 (psychologique) puis MM50 $44.72
- Résistance : $56.79 (high du jour) puis $58.40 (close pré-gap)
- Stop-loss (2×ATR) : **$41.94** — inchangé
- Take-profit (3×ATR) : **$69.44** — inchangé
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — structure technique intacte au-dessus de la MM50, RSI neutre propice. La volatilité extrême (beta 4.18) et l'ATR 10.39% imposent un sizing réduit strict.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux fondamental** depuis l'init du 2026-05-17. Les données FMP restent au FY 2025 (clos 2025-06-30). **Point de vigilance majeur : divergence Yahoo vs FMP sur les métriques de valorisation.**

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $18.92 B | $3.13 B | **-83%** | Yahoo (coherent avec close × shares out.) |
| **EV/EBITDA** | 140.45× | 17.48× | **-88%** | Yahoo (FMP market cap erroné infecte l'EV) |
| **P/B** | 6.99× | 1.72× | **-75%** | Yahoo |
| **P/E TTM** | 68.75× | 35.96× | **-48%** | Yahoo |
| **EV/Sales** | 27.30× | 7.04× | **-74%** | Yahoo |

**Diagnostic divergence :** Le market cap FMP ($3.13B) est incompatible avec le cours $52.94 et 357M shares outstanding ($18.9B théorique). Les métriques FMP dérivées de cette base (EV multiples, P/B, P/S) sont donc **non fiables** pour IREN. Cela peut indiquer :
1. FMP référence une ancienne classe d'actions ou une entité filiale (ex : IREN Australia vs IREN Limited NASDAQ)
2. Données FMP non reconciliées post-restructuration ou ADS conversion
3. Lag de mise à jour FMP vs Yahoo

**Métriques fondamentales retenues (source Yahoo, cross-checkée avec FMP raw ratios) :**

| Métrique | Valeur | Signal |
|----------|--------|--------|
| **Market Cap** | $18.92 B | — |
| **P/E TTM** | 68.75× | Très élevé — prime IA/mining |
| **Forward P/E** | -39.36× | **Négatif — pas de profitabilité forward attendue** |
| **EV/EBITDA** | 140.45× | Extrême — prix du pivot IA inclus |
| **P/B** | 6.99× | Élevé |
| **Gross Margin** | 68.3% | Bon (infrastructure à forte marge) |
| **EBITDA Margin** | 40.3% | Bon |
| **Operating Margin** | 3.46% | Faible — coûts opérationnels élevés |
| **Net Margin** | 17.4% | Rentable au net sur FY 2025 |
| **Debt/Equity** | 53.1% | Modéré |
| **Interest Coverage** | 1.57× | Faible — pression si taux montent |
| **FCF Yield** | -36.0% | **Cash burn confirmé** |
| **Capex/Revenue** | 2.7% | Modéré |
| **ROIC (FMP)** | 0.58% | Très faible — capital pas encore rentable |
| **ROE (FMP)** | 4.78% | Faible |
| **Net Debt/EBITDA (FMP)** | 1.98× | Modéré |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (pas de profitabilité forward)
- ❌ FCF négatif (price_to_fcf = -2.77)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29)
- ✅ Gross Margin 68.3% (infrastructure à forte marge)
- ✅ EBITDA Margin 40.3%
- ⚠️ Moat / TAM : le contrat NVIDIA $3.4B est un catalyseur mais pas encore un moat structurel prouvé

> **⚠️ Points de vigilance earnings (Q1 2026, FY Q3, exercice juin) :**
> 1. Guidance HPC/IA : quel % du CA guide provient du contrat NVIDIA ?
> 2. Marges HPC vs legacy mining — Operating Margin 3.5% doit s'améliorer
> 3. FCF : sur le chemin du positif ? Capex/OCF 5.6× est élevé
> 4. Dette / renégociation sous taux 10Y à ~4.6%
> 5. ROIC : le pivot IA doit montrer une amélioration de la rentabilité du capital

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $65.86 (21 analysts) | **Inchangé** |
| **Max Pain** | $20.00 | **↓ de $33.00** — niveau très bas, attention |
| **Put/Call ratio** | N/A | Non disponible |
| **Short Interest** | 0.17% | Très faible — pas de short squeeze setup |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz Reddit/Yahoo |
| **Event-Driven** | Aucun événement | `data/events_latest.json` vide pour IREN |

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Divergence Score : **4/10**
- Premium vs NAV estimé : **+12%**
- Verdict : *Fortement corrélé — pivot IA non encore pricé*

**Commentaire :** L'absence totale de mention sur les réseaux sociaux et le max pain à $20 (très en dessous du cours) suggèrent soit une option activity très faible, soit des données options partielles. Le titre reste un proxy BTC avec beta 2.1. Le max pain à $20 est un niveau de concentration des options puts très agressif — si les résultats déçoivent, la gravité technique vers $20 est théoriquement possible (distance -62%).

---

## Scoring Global (Agent Recommandation — 2026-05-18)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 7.8/10 | 35% | 2.73 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 6.0/10 | 25% | 1.50 |
| **Score Opportunité** | **5.8/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible (-5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : données manquantes (M-Score, Z-Score non disponibles dans data/accounting_risk_latest.json) — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus (pas d'événement détecté)
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top (momentum 10/10), XLE bullish crossover — IREN est exposé Technology/IA Infrastructure, aligné partiellement avec le momentum sectoriel → léger contexte favorable

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 58.3/100 | -5.0 | +10.0 | **63.3/100** |

**Action recommandée : ACHETER — Sizing Réduit**
- Prix d'entrée suggéré : $52.94
- Stop-loss : $41.94 (-20.8%)
- Take-profit : $69.44 (+31.1%)
- Ratio R/R : 1.5 : 1
- Horizon : 1–3 mois
- Timing : Favorable

> **⚠️ Avertissement :** La recommandation agent est basée sur des données **pré-earnings** (FY 2025). L'annonce du Q1 2026, attendue aujourd'hui, peut modifier radicalement le score Catalyseur et Valorisation. Le sizing réduit est impératif compte tenu du beta 4.18 et de la corrélation BTC 0.82. Le max pain $20 représente un risque de queue importante (-62%) en cas de guidance cut sévère.

---

## Scénarios Post-Earnings (Mise à jour)

| Scénario | Conditions | Impact cours estimé | Action |
|----------|------------|---------------------|--------|
| **Optimiste (25%)** | Beat revenue + guidance HPC forte + FCF positif + ROIC > 5% | +15–25% → $61–$66 | **Renforcer** — pivot IA validé |
| **Central (50%)** | Inline + guidance inchangée + FCF stable | ±5% → $50–$56 | **Conserver** — thèse inchangée |
| **Pessimiste (25%)** | Miss + compression marges + guidance cut + ROIC stagnant | -15–25% → $40–$45 (-62% tail risk vers max pain $20) | **Réduire** — revalorisation nécessaire |

**Prix cible révisé :** $65.86 (consensus FMP, 21 analysts) — **inchangé en l'absence de nouveaux résultats.**

---

## Conclusion

**Thèse : CONFIRMÉE — avec réserve earnings et divergence données FMP**

La structure technique et fondamentale d'IREN est **inchangée** par rapport à l'init du 2026-05-17. Le gap de -9.35% n'a pas été comblé ni creusé — le titre est figé en attendant les résultats du Q1 2026. Les triggers du DRAST full refresh (PRICE_GAP -9.35%, ATR_SPIKE 10.39%) confirment la volatilité inhérente au titre mais **n'invalident pas la thèse** : le pivot IA/HPC reste le catalyseur structurant, la MM50 est intacte, et le consensus maintient son PT à $65.86.

**Points clés :**
1. **Cours stable** à $52.94 post-gap — aucun mouvement directionnel intraday
2. **Earnings J-0** — résultats non encore disponibles dans les données FMP/Yahoo (fetch 08:44 UTC)
3. **Score Opportunité 5.8/10** inchangé — Catalyseur fort (7.8) compense Valorisation faible (4.0)
4. **Filtre Qualité 4/6** inchangé — Quality Partielle, FCF négatif persistant, ROIC 0.6% très faible
5. **Divergence Yahoo/FMP** : market cap, EV/EBITDA, P/B — FMP non fiable pour IREN, privilégier Yahoo
6. **Proxy BTC intact** — corrélation 0.82, beta 2.1, divergence score 4/10
7. **Max pain $20** — très éloigné du cours, tail risk important en cas de guidance cut sévère
8. **Sector rotation** : XLK top momentum, XLE bullish crossover — contexte macro modérément favorable aux infrastructures physiques

**Recommandation :** Maintenir l'**ACHETER à sizing réduit** avec SL $41.94 / TP $69.44, **MAIS** attendre la publication des résultats Q1 2026 avant toute nouvelle entrée. Le beta 4.18, le FCF négatif et le ROIC 0.6% imposent une discipline de sizing stricte. Si earnings beat + guidance HPC forte, le catalyseur pourrait justifier un relèvement du score Valorisation et un renforcement de position.

---

*Rapport généré le 2026-05-18 — Données sources : data/latest.json, data/recommandations_latest.json, data/crypto_correlation_latest.json, data/geo_risk_latest.json, data/fx_exposure_latest.json, data/social_sentiment_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/sector_rotation_latest.json*
