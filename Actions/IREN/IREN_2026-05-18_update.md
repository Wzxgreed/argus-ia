# IREN — Mise à Jour Quotidienne (2026-05-18)

> **Type :** `_update.md` — Mise à jour post-gap + earnings J-0
> **Référence précédente :** [IREN_2026-05-17_init.md](IREN_2026-05-17_init.md)

---

## Résumé des Changements

| Métrique | 2026-05-17 | 2026-05-18 | Δ |
|----------|------------|------------|---|
| **Cours close** | $52.94 | $52.94 | **0.00%** |
| **Volume** | 48.5 M | 48.5 M | 0.93× moy. 20j |
| **RSI 14j** | 54.61 | 54.61 | **Inchangé** |
| **ATR 14j** | 5.50 | 5.50 | **Inchangé** |
| **MM 50j** | $44.72 | $44.72 | **Inchangé** |
| **P/E TTM** | 68.75× | 68.75× | **Inchangé** |
| **Forward P/E** | -39.36× | -39.36× | **Inchangé** |
| **EV/EBITDA** | 140.45× | 140.45× | **Inchangé** |
| **Beta** | 4.18 | 4.18 | **Inchangé** |
| **Short Interest** | 0.17% | 0.17% | **Inchangé** |
| **Max Pain** | $33.00 | $20.00 | **↓ $13.00** |
| **BTC-USD** | — | $78,144 | — |
| **Score Opportunité** | 5.8/10 | **5.8/10** | **Inchangé** |
| **Score Global ajusté** | — | **63.3/100** | — |

**Verdict :** Le cours n'a pas bougé d'un centime depuis le gap de -9.35% d'hier. Les données techniques et fondamentales sont identiques. Le seul élément nouveau : l'earnings call programmé aujourd'hui (2026-05-18, J-0) — **résultats non encore intégrés dans les feeds FMP/Yahoo**.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 54.61 | Zone neutre favorable, ni surachat ni survente |
| **ATR 14j** | $5.50 | Volatilité élevée mais stable vs hier |
| **MM 50j** | $44.72 | Cours **+18.4% au-dessus** — tendance haussière intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 52.4 M | Volume du jour 48.5 M = **92.5%** du moyen |
| **Range intraday** | $52.86 – $56.79 | Aucune cassure de support ni de résistance |

**Niveaux clés :**
- Support immédiat : $52.86 (low du jour)
- Support structurel : $50.00 (psychologique) puis MM50 $44.72
- Résistance : $56.79 (high du jour) puis $58.40 (close précédent)
- Stop-loss (2×ATR) : **$41.94** — inchangé
- Take-profit (3×ATR) : **$69.44** — inchangé
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — structure technique intacte au-dessus de la MM50, RSI neutre propice, mais volatilité extrême (beta 4.18) requiert sizing réduit.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux fondamental** depuis l'init du 2026-05-17. Les données FMP restent au FY 2025 (clos 2025-06-30) :

| Métrique | Valeur | Signal |
|----------|--------|--------|
| **Market Cap** | $18.92 B | — |
| **P/E TTM** | 68.75× | Très élevé |
| **Forward P/E** | -39.36× | **Négatif — pas de profitabilité forward attendue** |
| **EV/EBITDA** | 140.45× | Extrême |
| **P/B** | 6.99× | Élevé |
| **Gross Margin** | 68.3% | Bon (infrastructure à forte marge) |
| **EBITDA Margin** | 40.3% | Bon |
| **Net Margin** | 17.4% | Rentable au net sur FY 2025 |
| **Debt/Equity** | 53.1% | Modéré |
| **Interest Coverage** | 1.57× | Faible — pression si taux montent |
| **FCF Yield** | -36.0% | **Cash burn confirmé** |
| **Capex/Revenue** | 2.7% | Modéré |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (pas de profitabilité forward)
- ❌ FCF négatif (price_to_fcf = -2.77)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29)
- ✅ Gross Margin 68.3% (infrastructure à forte marge)
- ✅ EBITDA Margin 40.3%
- ⚠️ Moat / TAM : à valider post-earnings (contrat NVIDIA $3.4B = catalyseur mais pas encore moat prouvé)

> **⚠️ Point de vigilance :** L'earnings Q1 2026 (FY Q3, exercice juin) est attendu aujourd'hui. Les 4 questions clés restent valides :
> 1. Guidance HPC/IA : quel % du CA guide provient du contrat NVIDIA ?
> 2. Marges HPC vs legacy mining
> 3. FCF : sur le chemin du positif ?
> 4. Dette / renégociation sous taux 10Y à ~4.6%

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

**Agent Crypto-Correlation :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Divergence Score : **4/10**
- Premium vs NAV estimé : **+12%**
- Verdict : *Fortement corrélé — pivot IA non encore pricé*

**Commentaire :** L'absence totale de mention sur les réseaux sociaux et le max pain à $20 (très en dessous du cours) suggèrent soit une option activity très faible, soit des données options partielles. Le titre reste un proxy BTC avec beta 2.1.

---

## Scoring Global (Agent Recommandation — 2026-05-18)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 7.8/10 | 35% | 2.73 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 6.0/10 | 25% | 1.50 |
| **Score Opportunité** | **5.8/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible
- FX Impact Score 0/10 → neutre
- Accounting Risk : données manquantes (M-Score, Z-Score non disponibles)
- Event-Driven : aucun malus/bonus (pas d'événement détecté)
- Social Sentiment : 0 → pas de malus/bonus

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

> **⚠️ Avertissement :** La recommandation agent est basée sur des données **pré-earnings** (FY 2025). L'annonce du Q1 2026, attendue aujourd'hui, peut modifier radicalement le score Catalyseur et Valorisation. Le sizing réduit est impératif compte tenu du beta 4.18 et de la corrélation BTC 0.82.

---

## Scénarios Post-Earnings (Mise à jour)

| Scénario | Conditions | Impact cours estimé | Action |
|----------|------------|---------------------|--------|
| **Optimiste (25%)** | Beat revenue + guidance HPC forte + FCF positif | +15–25% → $61–$66 | **Renforcer** — pivot IA validé |
| **Central (50%)** | Inline + guidance inchangée + FCF stable | ±5% → $50–$56 | **Conserver** — thèse inchangée |
| **Pessimiste (25%)** | Miss + compression marges + guidance cut | -15–25% → $40–$45 | **Réduire** — revalorisation nécessaire |

**Prix cible révisé :** $65.86 (consensus FMP, 21 analysts) — **inchangé en l'absence de nouveaux résultats.**

---

## Conclusion

**Thèse : CONFIRMÉE — avec réserve earnings**

La structure technique et fondamentale d'IREN est **inchangée** par rapport à hier. Le gap de -9.35% n'a pas été comblé ni creusé — le titre est figé en attendant les résultats du Q1 2026. Aucun nouveau catalyseur ni risque n'est apparu dans les feeds.

**Points clés :**
1. **Cours stable** à $52.94 post-gap — aucun mouvement directionnel intraday
2. **Earnings J-0** — résultats non encore disponibles dans les données FMP/Yahoo
3. **Score Opportunité 5.8/10** inchangé — Catalyseur fort (7.8) compense Valorisation faible (4.0)
4. **Filtre Qualité 4/6** inchangé — Quality Partielle, FCF négatif persistant
5. **Proxy BTC intact** — corrélation 0.82, beta 2.1
6. **Max pain $20** — très éloigné du cours, suggérant une option activity faible ou des données partielles

**Recommandation :** Maintenir l'**ACHETER à sizing réduit** avec SL $41.94 / TP $69.44, **MAIS** attendre la publication des résultats Q1 2026 avant toute nouvelle entrée. Le beta 4.18 et le FCF négatif imposent une discipline de sizing stricte.

---

*Rapport généré le 2026-05-18 — Données sources : data/latest.json, data/recommandations_latest.json, data/crypto_correlation_latest.json, data/geo_risk_latest.json, data/fx_exposure_latest.json, data/social_sentiment_latest.json, data/upcoming_events_latest.json, data/events_latest.json*
