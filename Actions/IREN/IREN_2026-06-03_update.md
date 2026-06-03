# IREN — Mise à Jour (2026-06-03, snapshot 13:00 UTC)

> **Type :** `_update.md` — Mise à jour intra-journalière (snapshot 13:00 UTC)
> **Référence précédente :** [IREN_2026-06-03_update.md](IREN_2026-06-03_update.md) (snapshot 10:00 UTC)
> **Données source :** `data/2026-06-03.json` (fetched_at 2026-06-03T13:00:07 UTC), `data/recommandations_2026-06-03.json`, `data/quant_2026-06-03.json`, `data/geo_2026-06-03.json`, `data/sector_rotation_2026-06-03.json`, `data/social_sentiment_2026-06-03.json`, `data/fx_exposure_2026-06-03.json`, `data/upcoming_events_2026-06-03.json`, `data/events_2026-06-03.json`
> **Note :** Snapshot 13:00 UTC = données live intra-session (marché US ouvert depuis 14:30 UTC, mais données déjà disponibles post-fetch). Données strictement identiques au snapshot 10:00 UTC à l'exception de la **résolution des anomalies options**.

---

## Résumé des Changements

| Métrique | 2026-06-03 (snapshot 10h) | 2026-06-03 (snapshot 13h) | Δ |
|----------|--------------------------|--------------------------|---|
| **Cours close** | **$66.60** | **$66.60** | **=** |
| **Volume** | 51.34 M (0.86× moy.) | **51.34 M (0.86× moy.)** | **=** |
| **RSI 14j** | **61.11** | **61.11** | **=** |
| **ATR 14j** | **$5.11** | **$5.11** | **=** |
| **MM 50j** | **$48.75** | **$48.75** | **=** |
| **P/E TTM (Yahoo)** | **86.49×** | **86.49×** | **=** |
| **Forward P/E (Yahoo)** | **−70.85×** | **−70.85×** | **=** |
| **P/B (Yahoo)** | **8.80×** | **8.80×** | **=** |
| **EV/EBITDA (Yahoo)** | **173.62×** | **173.62×** | **=** |
| **Market Cap (Yahoo)** | **$23.80 B** | **$23.80 B** | **=** |
| **Short Interest** | **14.72%** | **14.72%** | **=** |
| **Consensus PT (FMP)** | **$66.61 (23 analysts)** | **$66.61 (23 analysts)** | **=** |
| **Max Pain** | **$20.00** (anomalie) | **$52.00** | **✅ Résolu** |
| **Put/Call ratio** | **null** (anomalie) | **1.95** | **✅ Résolu** |
| **Call OI %** | **null** (anomalie) | **33.9%** | **✅ Résolu** |
| **Score Opportunité** | **4.8/10** | **4.8/10** | **=** |
| **Score Global ajusté** | **52.5/100** | **52.5/100** | **=** |
| **Action recommandée** | **ATTENDRE** | **ATTENDRE** | **=** |

**Mutation significative :** Aucune sur les données brutes. Le snapshot 13:00 UTC confirme la **stabilité totale** vs snapshot 10:00 UTC. Le seul changement matériel est la **résolution des anomalies de feed options** détectées au snapshot 10:00 UTC :
- **Max Pain : $20.00 → $52.00** — correction de l'anomalie, valeur cohérente avec le range historique
- **Put/Call ratio : null → 1.95** — légère amélioration vs close 02/06 (2.09), puts désormais 66.1% (vs 67.6%)
- **Call OI % : null → 33.9%** — légère amélioration vs close 02/06 (32.4%)

**Interprétation :** La structure options reste défensive (put/call > 1.0, calls minoritaires) mais la défiance s'est légèrement atténuée entre le close 02/06 et le snapshot 13h du 03/06. Cependant, le ratio 1.95 reste élevé et signale que le marché options anticipe toujours une correction ou maintient une protection massive.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 61.11 | Zone haussière — inchangé vs snapshot précédent |
| **ATR 14j** | $5.11 | Volatilité stable (beta 4.179, ATR relatif ~7.67%) |
| **MM 50j** | $48.75 | Cours **+36.6% au-dessus** — tendance haussière intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | ~59.6 M | Volume snapshot 51.34 M = **86.1%** — participation normale |
| **Range intraday (session 02/06)** | $64.27 – $69.57 | Range de 8.2%, rejet du high en clôture |
| **52-week high/low** | $76.87 / $8.70 | Cours à **86.6%** du 52W high |

**Niveaux clés (inchangés) :**
- Support immédiat : **$65.33** (previous close 01/06)
- Support : **$64.27** (low du 02/06)
- Support intermédiaire : **$63.54** (close 01/06)
- Support structurel : **$60.26** (low 01/06)
- Support majeur : **$56.83** (breakout level du rally du 25/05)
- Support MM50 : **$48.75**
- Résistance immédiate : **$66.61** (consensus PT — pivot clé)
- Résistance majeure : **$69.57** (high intraday 02/06)
- Résistance 52W : **$76.87**
- Stop-loss (2×ATR) : **$56.38** (−15.3%)
- Take-profit (3×ATR) : **$81.93** (+23.0%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — La tendance haussière reste intacte (cours +36.6% au-dessus de la MM50) mais le rejet du high à $69.57 et la clôture au contact du consensus PT ($66.60 vs $66.61) signalent une indécision. Aucun nouveau flux technique n'est disponible depuis le close officiel. La vigilance porte sur la session du 2026-06-03 : capacité à reprendre $66.61 avec volume confirmé. Si gap down sous $65.33 → signe de faiblesse. Si gap up au-dessus de $67.30 → reprise du momentum.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** n'est intégré dans les sources Yahoo/FMP au snapshot 2026-06-03. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $23.80 B | $3.13 B | **−87%** | Yahoo |
| **EV/EBITDA** | 173.62× | 12.34× | **−93%** | Yahoo |
| **P/B** | 8.80× | 1.72× | **−81%** | Yahoo |
| **P/E TTM** | 86.49× | 35.96× | **−59%** | Yahoo |
| **EV/Sales** | 33.75× | 7.04× | **−79%** | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−70.85)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans les données FMP

**Valorisation (stable à légèrement dégradée) :**
- P/E TTM Yahoo **86.49×** — inchangé, reste extrême
- EV/EBITDA Yahoo **173.62×** — révisé +3.08 pts vs 170.54× close 01/06, toujours extrême
- Forward P/E **−70.85×** — inchangé, profitabilité attendue éloignée
- P/B Yahoo **8.80×** — stable
- **Cours $66.60 ≈ Consensus PT $66.61** — upside vers le consensus quasi nul (0.0%)

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $66.61 (23 analysts) | Inchangé — cours à −0.01% du PT |
| **Max Pain** | **$52.00** (exp 2026-06-05) | **✅ Résolu** — anomalie $20.00 corrigée |
| **Put/Call ratio** | **1.95** | **✅ Résolu** — légère amélioration vs 2.09 (close 02/06) |
| **Call OI %** | **33.9%** | **✅ Résolu** — légère amélioration vs 32.4% (close 02/06) |
| **Short Interest** | 14.72% | Inchangé — fuel squeeze réduit vs mai mais présent |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz retail |
| **Event-Driven** | Aucun événement | `data/events_2026-06-03.json` vide |
| **News Yahoo** | Aucune | `data/news_2026-06-03.json` vide pour IREN |
| **Geo Risk** | Score 2/10, flag "low" | Inchangé |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | Neutre |

**Agent Sector Rotation (2026-06-03) :**
- XLK : momentum score **10.0/10** (top sector, return 20d +22.3%)
- Signal global : **NEUTRAL** (regime UNKNOWN)
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Commentaire :** La structure options reste **défensive** mais la défiance s'est légèrement atténuée :
- **Put/Call ratio 1.95** — puts majoritaires à 66.1% (vs 67.6% au close 02/06). Les options traders ont légèrement réduit leur couverture, mais le ratio reste élevé et signale une protection massive maintenue.
- **Call OI 33.9%** — calls minoritaires mais en légère hausse vs 32.4%.
- **Max Pain $52.00** — valeur cohérente avec le range historique récent. L'anomalie $20.00 du snapshot 10h est confirmée comme erronée et corrigée.

Le consensus analystes reste stable (23 analysts, PT $66.61). Le cours à $66.60 est désormais exactement au contact du consensus. Aucun événement corporate détecté.

---

## Scoring Global (Agent Recommandation — 2026-06-03, snapshot 13h00 UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 5.3/10 | 35% | 1.86 |
| **Valorisation** | 3.0/10 | 40% | 1.20 |
| **Momentum** | 6.8/10 | 25% | 1.70 |
| **Score Opportunité** | **4.8/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 2/10 → malus faible (−5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10.0/10) — alignement favorable → bonus +5.0 pts
- Quant Report : insuffisant (p-value 1.0, 0 signaux) — pas de malus/bonus

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 48.0/100 | −5.0 | +5.0 | **52.5/100** |

**Action recommandée : ATTENDRE**
- Prix d'entrée suggéré : $66.60
- Stop-loss : $56.38 (−15.3%)
- Take-profit : $81.93 (+23.0%)
- Ratio R/R : 1.5 : 1
- Horizon : —
- Timing : Favorable

> **⚠️ Avertissements :**
> 1. La recommandation reste basée sur des données **pre-earnings Q1 2026** (résultats toujours non intégrés dans les feeds Yahoo/FMP au 2026-06-03).
> 2. **Forward P/E négatif** : −70.85× — la profitabilité attendue s'éloigne davantage.
> 3. **Valorisation extrême** : P/E 86.49×, P/B 8.80×, EV/EBITDA 173.62×. Toute déception pourrait déclencher une correction sévère.
> 4. **Consensus PT $66.61 désormais résistance** — upside vers consensus devenu nul (0.0%).
> 5. **Put/Call 1.95** — la structure options reste défensive (puts 66.1%). Le marché options anticipe toujours une correction.
> 6. Si cours casse $64.27 sans rebond → signe de faiblesse.
> 7. Si cours casse $60.26 sans rebond → **passer en SURVEILLER**.
> 8. Si cours casse $56.83 sans rebond → **passer en ÉVITER**.
> 9. Si cours casse $48.75 (MM50) → **passer en ÉVITER**.

---

## Conclusion

**Thèse : CONFIRMÉE — Le statut ATTENDRE est maintenu.** Le snapshot 13:00 UTC du 2026-06-03 confirme la **stabilité totale** vs snapshot 10:00 UTC et vs close officiel du 2026-06-02 ($66.60, RSI 61.11, ATR $5.11, MM50 $48.75). Les **anomalies options du snapshot 10h sont résolues** : Max Pain $52.00 (vs $20.00 erroné), put/call 1.95 (vs null), call OI 33.9% (vs null). Aucun nouveau flux de marché n'est disponible (marché US ouvert à 14:30 UTC, données pré-session).

**Différentiels clés vs analyse précédente (snapshot 10:00 UTC 2026-06-03) :**
1. **Cours identique** à $66.60 — aucun mouvement de marché
2. **Volume 51.34 M =** — inchangé
3. **RSI 61.11 =** — inchangé
4. **Forward P/E −70.85× =** — inchangé
5. **P/E TTM 86.49× =** — inchangé
6. **EV/EBITDA Yahoo 173.62× =** — inchangé
7. **P/B Yahoo 8.80× =** — inchangé
8. **Market Cap $23.80 B =** — inchangé
9. **Options : anomalies résolues** — Max Pain $52.00 (coherent), put/call 1.95 (léger recul de la défiance vs 2.09), call OI 33.9% (vs 32.4%).
10. **Score Global ajusté 52.5/100 =** — inchangé
11. **Filtre Qualité 4/6 =** — Quality Partielle inchangée
12. **Earnings Q1 2026** — résultats toujours non intégrés dans les feeds
13. **Prochain earnings** : 2026-08-27 (Q2 2026, 85 jours)

**Recommandation :** Maintenir **ATTENDRE**.
- **Ne pas entrer** à $66.60 — valuation extrême, Forward P/E négatif, consensus PT = cours
- Surveiller la session du 2026-06-03 : si gap up au-dessus de $67.30 avec volume → reprise du momentum possible
- Si gap down sous $65.33 → retour vers $64.27 puis $63.54
- Si clôture au-dessus de $66.61 avec volume confirmé → retest de $69.57 possible
- Les détenteurs de positions existantes peuvent maintenir avec SL $56.38 / TP $81.93
- Si earnings beat + guidance HPC forte + FCF positif → réévaluation possible vers ACHETER
- Si miss ou guidance cut → attendre retour vers $56.83 puis $50
- Si cours casse $64.27 sans rebond → signe de faiblesse
- Si cours casse $60.26 sans rebond → **passer en SURVEILLER**
- Si cours casse $56.83 sans rebond → **passer en ÉVITER**
- Si cours casse $48.75 (MM50) → **passer en ÉVITER**

---

*Rapport généré le 2026-06-03 — Données sources : `data/2026-06-03.json` (snapshot 13:00 UTC), `data/recommandations_2026-06-03.json`, `data/quant_2026-06-03.json`, `data/geo_2026-06-03.json`, `data/sector_rotation_2026-06-03.json`, `data/social_sentiment_2026-06-03.json`, `data/fx_exposure_2026-06-03.json`, `data/upcoming_events_2026-06-03.json`, `data/events_2026-06-03.json`.*
