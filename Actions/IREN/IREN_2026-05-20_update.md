# IREN — Mise à Jour Quotidienne (2026-05-20, snapshot 13:00 UTC)

> **Type :** `_update.md` — Révision post-midi (correction données options)
> **Référence précédente :** [IREN_2026-05-20_update.md](IREN_2026-05-20_update.md) (rev. 10:00 UTC)
> **Données source :** `data/latest.json` (timestamp 2026-05-20T13:00:08+00:00), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`

---

## Résumé des Changements

| Métrique | 2026-05-20 10:00 | 2026-05-20 13:00 | Δ |
|----------|------------------|------------------|---|
| **Cours close** | $47.74 | **$47.74** | **—** |
| **Previous close** | $50.46 | **$50.46** | **—** |
| **Open** | $48.62 | **$48.62** | **—** |
| **High** | $49.27 | **$49.27** | **—** |
| **Low** | $46.00 | **$46.00** | **—** |
| **Volume** | 37.44 M | **37.44 M** | **—** |
| **Volume vs 20j** | 70.8% | **70.8%** | **—** |
| **RSI 14j** | 54.95 | **54.95** | **—** |
| **ATR 14j** | $5.62 | **$5.62** | **—** |
| **MM 50j** | $45.17 | **$45.17** | **—** |
| **P/E TTM** | 62.00× | **62.00×** | **—** |
| **Forward P/E** | −35.49× | **−35.49×** | **—** |
| **EV/EBITDA** | 127.83× | **127.83×** | **—** |
| **EV/Sales** | 24.85× | **24.85×** | **—** |
| **P/B** | 6.31× | **6.31×** | **—** |
| **Beta** | 4.18 | **4.18** | **—** |
| **Short Interest** | 0.17% | **0.17%** | **—** |
| **Max Pain** | $20.00 | **$33.00** | **+65.0%** 🟢 |
| **Put/Call ratio** | null | **1.21** | **Retour données** |
| **Call OI %** | null | **45.2%** | **Retour données** |
| **Score Opportunité** | 6.2/10 | **6.2/10** | **—** |
| **Score Global ajusté** | 67.0/100 | **67.0/100** | **—** |

**Verdict :** Données brutes inchangées entre le snapshot 10:00 UTC et le snapshot 13:00 UTC (cours, volumes, RSI, fondamentaux). **La correction majeure concerne les données options :** le **Max Pain** est révisé de **$20.00 à $33.00** (+65%), et les données **put/call ratio (1.21)** et **call OI % (45.2%)** sont de retour dans le feed. Le Max Pain à $20.00 du snapshot matinal était une **anomalie de données** (probablement un artefact lié au rollover des séries options avant expiration du 2026-05-22). Le tail risk redevient **−30.9%** (vs −58.1% erroné), cohérent avec le niveau observé depuis le 2026-05-19. **Aucun flux post-earnings Q1 2026** n'est intégré dans les sources au snapshot 13:00 UTC.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 54.95 | Zone neutre, inchangé — pas de survente ni surachat |
| **ATR 14j** | $5.62 | Volatilité élevée stable (beta 4.18) |
| **MM 50j** | $45.17 | Cours **+5.7% au-dessus** — tendance haussière sous pression, intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 52.86 M | Volume du jour 37.44 M = **70.8%** du moyen — participation modérée confirmée |
| **Range intraday** | $46.00 – $49.27 | Low $46.00 = support du 2026-05-19, non retesté ce matin |
| **52-week high/low** | $76.87 / $8.28 | Cours à **62.1%** du 52W high |

**Niveaux clés (inchangés) :**
- Support immédiat : **$46.00** (low du 2026-05-19, testé mais non cassé)
- Support structurel : **$45.17** (MM50) — niveau ultime de défense
- Résistance immédiate : **$48.48** (support ancien devenu résistance)
- Résistance majeure : **$50.46** (previous close du 2026-05-18)
- Stop-loss (2×ATR) : **$36.50** (−23.5%)
- Take-profit (3×ATR) : **$64.60** (+35.3%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Neutre** — Le cours est stable en pré-session vs la clôture précédente. La structure technique n'a pas évolué : le maintien au-dessus de $46.00 et de la MM50 ($45.17) préserve la tendance haussière moyen terme, mais la cassure de $48.48 le 2026-05-19 reste un signal de modération. La vigilance reste de mise : une cassure de $45.17 invaliderait la tendance haussière. Le Max Pain corrigé à **$33.00** (expiration 2026-05-22) ramène le tail risk à un niveau connu et plus crédible (−30.9%).

---

## Mise à Jour Fondamentale

**Aucun nouveau flux fondamental** ni données post-earnings Q1 2026 n'intègrent les sources Yahoo/FMP au snapshot 13:00 UTC. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $17.06 B | $3.13 B | **−82%** | Yahoo |
| **EV/EBITDA** | 127.83× | 17.48× | **−86%** | Yahoo |
| **P/B** | 6.31× | 1.72× | **−73%** | Yahoo |
| **P/E TTM** | 62.00× | 35.96× | **−42%** | Yahoo |
| **EV/Sales** | 24.85× | 7.04× | **−72%** | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−35.49)
- ❌ FCF négatif (price_to_fcf = −2.77)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29)
- ✅ Gross Margin 68.3%
- ✅ EBITDA Margin 40.3%
- ⚠️ Moat / TAM : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé

> **⚠️ Points de vigilance earnings (Q1 2026, FY Q3) — J=0 aujourd'hui :**
> 1. Guidance HPC/IA : % du CA guide issu du contrat NVIDIA ?
> 2. Marges HPC vs legacy mining — Operating Margin 3.5% doit s'améliorer
> 3. FCF : sur le chemin du positif ?
> 4. Dette / renégociation sous taux 10Y ~4.6%
> 5. ROIC : le pivot IA doit montrer une amélioration (ROIC actuel 0.58% FMP)

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $65.86 (21 analysts) | Inchangé — upside +37.9% vs cours $47.74 |
| **Max Pain** | $33.00 | 🟢 **Corrigé de $20.00 à $33.00** — tail risk −30.9% (cohérent avec historique) |
| **Put/Call ratio** | 1.21 | 🟢 **Retour des données** — puts-dominated modéré, inchangé vs snapshot 21:00 UTC du 2026-05-19 |
| **Call OI %** | 45.2% | 🟢 **Retour des données** — puts majoritaires, légère hausse vs 43.8% précédemment |
| **Short Interest** | 0.17% | Très faible — pas de short squeeze setup |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz Reddit/Yahoo |
| **Event-Driven** | Aucun événement | `data/events_latest.json` vide pour IREN |
| **News Yahoo** | Aucune | `data/news_latest.json` vide pour IREN |
| **Geo Risk** | Score 3/10, flag "low" | Inchangé — exposition politique limitée |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | Neutre — pas de driver du jour |

**Agent Crypto-Correlation (2026-05-17 — dernières données disponibles) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Divergence Score : **4/10**
- Premium vs NAV estimé : **+12%**
- Verdict : *Fortement corrélé — pivot IA non encore pricé*

**Commentaire :** La correction du Max Pain de **$20.00 à $33.00** est le point clé de cette révision. Le niveau à $20.00 était une anomalie de données (artefact de rollover des options avant expiration du 2026-05-22) qui exagérait artificiellement le tail risk à −58.1%. Le niveau corrigé à $33.00 ramène le tail risk à **−30.9%**, cohérent avec l'historique récent et moins alarmant. Le put/call ratio à **1.21** et le call OI à **45.2%** confirment une défiance modérée mais stable des options traders — pas de détérioration supplémentaire par rapport au snapshot 21:00 UTC du 2026-05-19 (put/call 1.28, call OI 43.8%). L'absence de mentions sociales, de news et de flux institutionnels confirme que le mouvement reste technique/correlé BTC. Aucun upgrade/downgrade ni insider trade significatif détecté.

---

## Scoring Global (Agent Recommandation — 2026-05-20, snapshot 13:00 UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 8.3/10 | 35% | 2.91 |
| **Valorisation** | 4.5/10 | 40% | 1.80 |
| **Momentum** | 6.0/10 | 25% | 1.50 |
| **Score Opportunité** | **6.2/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible (−5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : données manquantes (M-Score, Z-Score non disponibles) — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10/10), XLE bullish (9.91) — IREN exposé Technology/IA Infrastructure, alignement favorable → **bonus +10.0 pts**

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 62.0/100 | −5.0 | +10.0 | **67.0/100** |

**Action recommandée : ACHETER — Sizing Réduit**
- Prix d'entrée suggéré : $47.74
- Stop-loss : $36.50 (−23.5%)
- Take-profit : $64.60 (+35.3%)
- Ratio R/R : 1.5 : 1
- Horizon : 1–3 mois
- Timing : Favorable

> **⚠️ Avertissements :**
> 1. La recommandation reste basée sur des données **pre-earnings**. L'annonce du Q1 2026 est attendue aujourd'hui (2026-05-20, J=0) et peut modifier radicalement le score.
> 2. Le sizing réduit est impératif (beta 4.18, corrélation BTC 0.82).
> 3. Le **Max Pain corrigé à $33.00** (expiration 2026-05-22) ramène le tail risk à −30.9% — niveau plus crédible mais à surveiller.
> 4. Le put/call ratio à 1.21 et le call OI 45.2% confirment une défiance modérée sans dégradation.
> 5. Attendre la publication des résultats avant toute nouvelle entrée significative.

---

## Scénarios Post-Earnings (Inchangés)

| Scénario | Conditions | Impact cours estimé | Action |
|----------|------------|---------------------|--------|
| **Optimiste (25%)** | Beat revenue + guidance HPC forte + FCF positif + ROIC > 5% | +15–25% → $55–$60 | **Renforcer** — pivot IA validé |
| **Central (50%)** | Inline + guidance inchangée + FCF stable | ±5% → $45–$51 | **Conserver** — thèse inchangée |
| **Pessimiste (25%)** | Miss + compression marges + guidance cut + ROIC stagnant | −15–25% → $36–$41 | **Réduire** — revalorisation nécessaire |

**Prix cible :** $65.86 (consensus FMP, 21 analysts) — **inchangé en l'absence de nouveaux résultats.**

---

## Conclusion

**Thèse : CONFIRMÉE — Données brutes stables, correction anomalie Max Pain ($20.00 → $33.00), earnings J=0 en attente**

Le snapshot 13:00 UTC du 2026-05-20 confirme la stabilité du cours à **$47.74** avec un volume de **37.44 M** (70.8% de la moyenne 20j). La structure technique n'a pas évolué : le maintien au-dessus de $46.00 et de la MM50 ($45.17) préserve la tendance haussière moyen terme. La correction principale de cette révision concerne l'anomalie du **Max Pain** : le niveau de **$20.00** du snapshot 10:00 UTC était un artefact de données (rollover options avant expiration du 2026-05-22) et est corrigé à **$33.00** dans le snapshot 13:00 UTC. Cette correction ramène le tail risk de −58.1% à **−30.9%**, un niveau cohérent avec l'historique récent et moins alarmant.

**Points clés :**
1. **Cours stable** à $47.74 — aucun nouveau gap entre 10:00 et 13:00 UTC
2. **Volume modéré confirmé** (70.8% du moyen 20j) — distribution réelle sous $48.50
3. **Low $46.00 intact** — pas de retest en pré-session
4. **Earnings J=0** — résultats Q1 2026 attendus aujourd'hui, non encore intégrés
5. **Max Pain corrigé $33.00** — 🟢 tail risk −30.9% (vs −58.1% erroné), anomalie résolue
6. **Put/Call ratio 1.21** — 🟢 données de retour, défiance modérée stable
7. **Call OI 45.2%** — 🟢 données de retour, puts majoritaires sans dégradation
8. **Score Opportunité 6.2/10** — inchangé
9. **Score Global ajusté 67.0/100** — inchangé
10. **Filtre Qualité 4/6** inchangé — Quality Partielle, FCF négatif persistant
11. **Proxy BTC intact** — corrélation 0.82, beta 2.1, divergence score 4/10
12. **Sector rotation** : XLK top momentum (10/10) — contexte macro favorable au secteur
13. **Niveau ultime de défense** : MM50 à $45.17. Si cassée → passer en ATTENDRE

**Récommandation :** Maintenir **ACHETER à sizing réduit** avec SL $36.50 / TP $64.60, **MAIS** :
- **Ne pas renforcer** avant les résultats Q1 2026
- La correction du Max Pain est rassurante mais ne change pas la vigilance requise : les résultats du jour restent le catalyseur déterminant
- Si le cours casse $45.17 (MM50) sans rebond → **passer en ATTENDRE**
- Si earnings beat + guidance HPC forte → le catalyseur pourrait justifier un relèvement du score Valorisation
- Le Max Pain à $33.00 reste un niveau de risque de queue à surveiller si guidance cut sévère

---

*Rapport généré le 2026-05-20 — Données sources : data/latest.json (13:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json*
