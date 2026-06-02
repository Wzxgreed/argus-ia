# IREN — Mise à Jour (2026-06-02, snapshot close officiel)

> **Type :** `_update.md` — Mise à jour close officiel (post-session)
> **Référence précédente :** [IREN_2026-06-02_update.md](IREN_2026-06-02_update.md) (snapshot 17:00 UTC)
> **Données source :** `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Note :** `data/latest.json` et `data/2026-06-02.json` retournent un objet vide pour IREN — les chiffres ci-dessous proviennent de `data/recommandations_latest.json` et du DRAFT_refresh du pipeline (données brutes Yahoo/FMP du close).

---

## Résumé des Changements

| Métrique | 2026-06-02 (17:00 UTC) | 2026-06-02 (close officiel) | Δ |
|----------|------------------------|----------------------------|---|
| **Cours close** | $67.30 | **$66.60** | **−$0.70 (−1.04%)** |
| **Volume** | 29.68 M (50.7% moy.) | **51.26 M (0.9× moy.)** | **+21.58 M** — volume total de session correct |
| **RSI 14j** | 61.70 | **61.11** | **−0.59 pt** |
| **ATR 14j** | $5.11 | **$5.11** | **=** |
| **MM 50j** | $48.76 | **$48.75** | **=** |
| **P/E TTM (Yahoo)** | 87.40× | **86.49×** | **−0.91 pt** |
| **Forward P/E (Yahoo)** | −71.60× | **−70.85×** | **+0.75 pt (amélioration marginale)** |
| **P/B (Yahoo)** | 8.89× | **8.89×** | **=** |
| **EV/EBITDA (Yahoo)** | 170.54× | **170.54×** | **=** |
| **Market Cap (Yahoo)** | $24.05 B | **$23.80 B** | **−$0.25 B** |
| **Short Interest** | 14.72% | **14.72%** | **=** |
| **Consensus PT (FMP)** | $66.61 (23 analysts) | **$66.61 (23 analysts)** | **=** |
| **Max Pain** | $52.00 | **$52.00** | **=** |
| **Put/Call ratio** | 2.09 | **2.09** | **=** |
| **Call OI %** | 32.4% | **32.4%** | **=** |
| **Score Opportunité** | 4.8/10 | **4.8/10** | **=** |
| **Score Global ajusté** | 53.0/100 | **52.5/100** | **−0.5 pt** |
| **Action recommandée** | ATTENDRE | **ATTENDRE** | **=** |

**Mutation significative :** Le close officiel à **$66.60 (−1.04%)** enregistre un **retrait partiel du breakout** du snapshot 17h ($67.30). Le cours est désormais **légèrement sous le consensus PT $66.61** (−0.01%), invalidant le franchissement observé en intraday. Le **volume total de la session s'établit à 51.26 M (0.9× la moyenne 20j)**, ce qui est conforme à la normale et corrige l'impression de faible participation du snapshot 17h (qui ne capturait qu'une partie de la session). La valorisation reste stretched (P/E 86.49×, Forward P/E −70.85×) et la structure options ultra-défensive (put/call 2.09) ne s'est pas améliorée.

**Points critiques :**
1. **Cours $66.60 ≈ Consensus PT $66.61** — le consensus est désormais le pivot : au-dessus = bullish, en-dessous = rejet.
2. **Volume total 0.9× moyenne** — participation normale en clôture, contrairement au snapshot 17h (50.7%).
3. **Forward P/E −70.85×** — amélioration marginale vs −71.60×, mais profitabilité attendue toujours éloignée.
4. **P/E TTM 86.49×** — légère baisse vs 87.40×, reste extrême.
5. **Score Global ajusté 52.5/100** — légère baisse (−0.5 pt), hors zone ACHETER (≥60).
6. **Structure options inchangée** — put/call 2.09, puts majoritaires à 67.6%, défiance persistante.
7. **Prochain earnings Q2 2026** : 2026-08-27 (86 jours) — aucun événement imminent.
8. **`data/latest.json` vide pour IREN** — [DONNÉES PARTIELLES] ; les métriques reposent sur le DRAFT_refresh et `recommandations_latest.json`.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 61.11 | Zone haussière — légère baisse vs 17h, pas de surachat (>70) |
| **ATR 14j** | $5.11 | Volatilité stable (beta 4.179, ATR relatif ~7.67%) |
| **MM 50j** | $48.75 | Cours **+36.6% au-dessus** — tendance haussière intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | ~56.9 M | Volume total 51.26 M = **90%** — participation normale |
| **Range intraday (session)** | $64.27 – $69.57 | Range de 8.2%, rejet du high en clôture |
| **52-week high/low** | $76.87 / $8.61 | Cours à **86.6%** du 52W high |

**Niveaux clés (révisés) :**
- Support immédiat : **$65.33** (previous close 01/06)
- Support : **$64.27** (low du 17h)
- Support intermédiaire : **$63.54** (close 01/06)
- Support structurel : **$60.26** (low 01/06)
- Support majeur : **$56.83** (breakout level du rally du 25/05)
- Support MM50 : **$48.75**
- Résistance immédiate : **$66.61** (consensus PT — pivot clé)
- Résistance majeure : **$69.57** (high intraday 17h)
- Résistance 52W : **$76.87**
- Stop-loss (2×ATR) : **$56.38** (−15.3%)
- Take-profit (3×ATR) : **$81.93** (+23.0%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — La tendance haussière reste intacte (cours +36.6% au-dessus de la MM50) mais le rejet du high à $69.57 et la clôture au contact du consensus PT ($66.60 vs $66.61) signalent une indécision. Le volume total de session est conforme à la normale. La vigilance porte sur l'ouverture du lendemain : capacité à reprendre $66.61 avec volume confirmé. Si gap down sous $65.33 → signe de faiblesse. Si gap up au-dessus de $67.30 → reprise du momentum.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** n'est intégré dans les sources Yahoo/FMP au close 2026-06-02. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $23.80 B | $3.13 B | **−87%** | Yahoo |
| **EV/EBITDA** | 170.54× | 12.34× | **−93%** | Yahoo |
| **P/B** | 8.89× | 1.72× | **−81%** | Yahoo |
| **P/E TTM** | 86.49× | 35.96× | **−59%** | Yahoo |
| **EV/Sales** | 33.15× | 7.04× | **−79%** | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−70.85)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans les données FMP

**Valorisation (stable) :**
- P/E TTM Yahoo **86.49×** — légère baisse de −0.91 pt vs snapshot 17h, reste extrême
- EV/EBITDA Yahoo **170.54×** — inchangé, toujours extrême
- Forward P/E **−70.85×** — amélioration marginale vs −71.60×, profitabilité attendue éloignée
- P/B Yahoo **8.89×** — inchangé
- **Cours $66.60 ≈ Consensus PT $66.61** — upside vers le consensus quasi nul (0.0%)

> **[DONNÉES PARTIELLES]** — `data/latest.json` et `data/2026-06-02.json` vides pour IREN. Les chiffres techniques proviennent du DRAFT_refresh pipeline et de `data/recommandations_latest.json`. `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $66.61 (23 analysts) | Inchangé — cours à −0.01% du PT |
| **Max Pain** | $52.00 (exp 2026-06-05) | Inchangé — tail risk −22.0% |
| **Put/Call ratio** | **2.09** | Inchangé — défiance persistante (puts 67.6%) |
| **Call OI %** | **32.4%** | Inchangé — calls minoritaires |
| **Short Interest** | 14.72% | Inchangé — fuel squeeze réduit vs mai mais présent |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz retail |
| **Event-Driven** | Aucun événement | `data/events_latest.json` vide |
| **News Yahoo** | Aucune | `data/news_latest.json` vide pour IREN |
| **Geo Risk** | Score 3/10, flag "low" | Inchangé |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | Neutre |

**Agent Sector Rotation (2026-06-02) :**
- XLK : momentum score **10.0/10** (top sector, return 20d +21.8%)
- Signal global : **NEUTRAL** (regime UNKNOWN)
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Commentaire :** La structure options reste **défensive** au close :
- **Put/Call ratio 2.09** — inchangé, puts majoritaires à 67.6%. Les options traders n'ont pas réduit leur couverture malgré le test du high à $69.57, signalant que le marché options anticipe toujours une correction ou maintient une protection massive.
- **Call OI 32.4%** — calls minoritaires, sentiment défensif inchangé.
- **Max Pain $52.00** — inchangé, valeur cohérente avec le range historique récent.

Le consensus analystes reste stable (23 analysts, PT $66.61). Le cours à $66.60 est désormais exactement au contact du consensus. Aucun événement corporate détecté.

---

## Scoring Global (Agent Recommandation — 2026-06-02, close officiel)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 5.3/10 | 35% | 1.86 |
| **Valorisation** | 3.0/10 | 40% | 1.20 |
| **Momentum** | 6.8/10 | 25% | 1.70 |
| **Score Opportunité** | **4.8/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible (−5.0 pts)
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
> 1. La recommandation reste basée sur des données **pre-earnings Q1 2026** (résultats toujours non intégrés dans les feeds Yahoo/FMP au 2026-06-02).
> 2. **Forward P/E négatif** : −70.85× — la profitabilité attendue s'éloigne davantage.
> 3. **Valorisation extrême** : P/E 86.49×, P/B 8.89×, EV/EBITDA 170.54×. Toute déception pourrait déclencher une correction sévère.
> 4. **Breakout invalidé en clôture** : le cours a testé $69.57 en intraday mais clôturé à $66.60, sous le consensus PT. Le volume total de session (90% moyenne) est correct, mais la clôture sous $66.61 invalide le signal bullish du 17h.
> 5. **Put/Call 2.09** — la structure options reste défensive (puts 67.6%). Le marché options anticipe une correction.
> 6. **Consensus PT $66.61 désormais résistance** — upside vers consensus devenu nul (0.0%).
> 7. Si cours casse $64.27 sans rebond → signe de faiblesse.
> 8. Si cours casse $60.26 sans rebond → **passer en SURVEILLER**.
> 9. Si cours casse $56.83 sans rebond → **passer en ÉVITER**.
> 10. Si cours casse $48.75 (MM50) → **passer en ÉVITER**.

---

## Conclusion

**Thèse : CONFIRMÉE — Le statut ATTENDRE est maintenu.** Le close officiel du 2026-06-02 à **$66.60 (−1.04% vs snapshot 17h)** enregistre un **retrait partiel du breakout** observé en intraday ($67.30, high $69.57). Le cours clôture **exactement au contact du consensus PT $66.61**, invalidant le franchissement haussier. Le **volume total de la session s'établit à 51.26 M (0.9× la moyenne 20j)**, ce qui est conforme à la normale et corrige l'impression de faible participation du snapshot 17h. La valorisation reste stretched (P/E 86.49×, Forward P/E −70.85×) et la structure options ultra-défensive (put/call 2.09).

**Différentiels clés vs analyse précédente (snapshot 17:00 UTC) :**
1. **Cours −1.04%** à $66.60 — retour sous le consensus PT $66.61
2. **Volume total 51.26 M** — participation normale (0.9× moyenne), vs 50.7% au snapshot 17h
3. **RSI 61.70 → 61.11** — légère baisse, reste dans la zone haussière
4. **Forward P/E −71.60× → −70.85×** — amélioration marginale, fondamentalement inchangé
5. **P/E TTM 87.40× → 86.49×** — légère baisse, valuation toujours extrême
6. **Market Cap $24.05 B → $23.80 B** — −$0.25 B
7. **Options inchangées** : put/call 2.09, call OI 32.4%, Max Pain $52.00
8. **Score Global ajusté 53.0 → 52.5** (−0.5 pt)
9. **Filtre Qualité 4/6** — Quality Partielle inchangée
10. **Earnings Q1 2026** — résultats toujours non intégrés dans les feeds
11. **Prochain earnings** : 2026-08-27 (Q2 2026, 86 jours)

**Recommandation :** Maintenir **ATTENDRE**.
- **Ne pas entrer** à $66.60 — breakout invalidé en clôture, valuation extrême, Forward P/E négatif
- Surveiller l'ouverture du lendemain : si gap up au-dessus de $67.30 avec volume → reprise du momentum possible
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

*Rapport généré le 2026-06-02 — Données sources : `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`. Note : `data/latest.json` vide pour IREN — chiffres issus du DRAFT_refresh pipeline.*
