# IREN — Mise à Jour (2026-06-03, snapshot 10:00 UTC)

> **Type :** `_update.md` — Mise à jour pré-ouverture (snapshot 10:00 UTC)
> **Référence précédente :** [IREN_2026-06-02_update.md](IREN_2026-06-02_update.md) (close officiel 2026-06-02)
> **Données source :** `data/latest.json` (fetched_at 2026-06-03T10:00:07 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Note :** Snapshot 10:00 UTC = close officiel 2026-06-02 (marché US fermé, ouverture 14:30 UTC). Données strictement identiques au close précédent à l'exception de révisions marginales Yahoo/FMP.

---

## Résumé des Changements

| Métrique | 2026-06-02 (close officiel) | 2026-06-03 (snapshot 10h) | Δ |
|----------|----------------------------|--------------------------|---|
| **Cours close** | **$66.60** | **$66.60** | **=** |
| **Volume** | 51.26 M (0.9× moy.) | **51.34 M (0.86× moy.)** | **+0.08 M** — quasi identique |
| **RSI 14j** | **61.11** | **61.11** | **=** |
| **ATR 14j** | **$5.11** | **$5.11** | **=** |
| **MM 50j** | **$48.75** | **$48.75** | **=** |
| **P/E TTM (Yahoo)** | **86.49×** | **86.49×** | **=** |
| **Forward P/E (Yahoo)** | **−70.85×** | **−70.85×** | **=** |
| **P/B (Yahoo)** | **8.89×** | **8.80×** | **−0.09 pt** |
| **EV/EBITDA (Yahoo)** | **170.54×** | **173.62×** | **+3.08 pts** |
| **Market Cap (Yahoo)** | **$23.80 B** | **$23.80 B** | **=** |
| **Short Interest** | **14.72%** | **14.72%** | **=** |
| **Consensus PT (FMP)** | **$66.61 (23 analysts)** | **$66.61 (23 analysts)** | **=** |
| **Max Pain** | **$52.00** | **$20.00** | **Anomalie détectée** |
| **Put/Call ratio** | **2.09** | **null** | **[DONNÉES MANQUANTES]** |
| **Call OI %** | **32.4%** | **null** | **[DONNÉES MANQUANTES]** |
| **Score Opportunité** | **4.8/10** | **4.8/10** | **=** |
| **Score Global ajusté** | **52.5/100** | **52.5/100** | **=** |
| **Action recommandée** | **ATTENDRE** | **ATTENDRE** | **=** |

**Mutation significative :** Aucune. Le snapshot 10:00 UTC du 2026-06-03 capture le **close officiel du 2026-06-02** (marché US fermé jusqu'à 14:30 UTC). Les données brutes sont **strictement identiques** au close précédent, à l'exception de deux révisions marginales Yahoo :
- **EV/EBITDA Yahoo +3.08 pts** (170.54 → 173.62) — révision technique de la base de calcul, pas un mouvement de marché
- **P/B Yahoo −0.09 pt** (8.89 → 8.80) — révision marginale

**Anomalies détectées :**
1. **`data/latest.json` retourne Max Pain $20.00** (vs $52.00 au close précédent). Cette valeur est **hors range historique** (52W low $8.70, support structurel $56.83) et correspond à une anomalie de feed Yahoo. La valeur fiable reste **$52.00** (expiration 2026-06-05).
2. **`data/latest.json` retourne put/call ratio et call OI % à `null`** — les données options ne sont pas alimentées dans ce snapshot. Les dernières valeurs fiables restent **put/call 2.09** et **call OI 32.4%**.
3. **DRAFT_refresh déclenché automatiquement** à 10:00 UTC par `ATR_SPIKE` (medium, ATR relatif 7.67%) — **faux positif** : l'ATR n'a pas changé ($5.11 =), le trigger est mécanique sur une volatilité historique déjà intégrée. Le DRAFT_refresh a été archivé.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 61.11 | Zone haussière — inchangé vs close précédent |
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

**Verdict timing : Favorable** — La tendance haussière reste intacte (cours +36.6% au-dessus de la MM50) mais le rejet du high à $69.57 et la clôture au contact du consensus PT ($66.60 vs $66.61) signalent une indécision. Aucun nouveau flux technique n'est disponible depuis le close officiel. La vigilance porte sur l'ouverture du 2026-06-03 : capacité à reprendre $66.61 avec volume confirmé. Si gap down sous $65.33 → signe de faiblesse. Si gap up au-dessus de $67.30 → reprise du momentum.

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
- EV/EBITDA Yahoo **173.62×** — révisé +3.08 pts vs 170.54×, toujours extrême
- Forward P/E **−70.85×** — inchangé, profitabilité attendue éloignée
- P/B Yahoo **8.80×** — légère baisse vs 8.89×
- **Cours $66.60 ≈ Consensus PT $66.61** — upside vers le consensus quasi nul (0.0%)

> **[DONNÉES PARTIELLES]** — `data/latest.json` retourne des valeurs options anormales (Max Pain $20.00, put/call null). Les métriques options fiables proviennent du close officiel 2026-06-02. `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $66.61 (23 analysts) | Inchangé — cours à −0.01% du PT |
| **Max Pain** | **$52.00** (exp 2026-06-05) | **Valeur fiable** — `$20.00` dans latest.json = anomalie |
| **Put/Call ratio** | **2.09** | **Valeur fiable** — `null` dans latest.json = données manquantes |
| **Call OI %** | **32.4%** | **Valeur fiable** — `null` dans latest.json = données manquantes |
| **Short Interest** | 14.72% | Inchangé — fuel squeeze réduit vs mai mais présent |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz retail |
| **Event-Driven** | Aucun événement | `data/events_latest.json` vide |
| **News Yahoo** | Aucune | `data/news_latest.json` vide pour IREN |
| **Geo Risk** | Score 3/10, flag "low" | Inchangé |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | Neutre |

**Agent Sector Rotation (2026-06-03) :**
- XLK : momentum score **10.0/10** (top sector, return 20d +22.3%)
- Signal global : **NEUTRAL** (regime UNKNOWN)
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Commentaire :** La structure options reste **défensive** d'après les dernières données fiables (close 2026-06-02) :
- **Put/Call ratio 2.09** — puts majoritaires à 67.6%. Les options traders n'ont pas réduit leur couverture malgré le test du high à $69.57, signalant que le marché options anticipe toujours une correction ou maintient une protection massive.
- **Call OI 32.4%** — calls minoritaires, sentiment défensif inchangé.
- **Max Pain $52.00** — valeur cohérente avec le range historique récent. La valeur $20.00 retournée par `data/latest.json` est une anomalie de feed à ignorer.

Le consensus analystes reste stable (23 analysts, PT $66.61). Le cours à $66.60 est désormais exactement au contact du consensus. Aucun événement corporate détecté.

---

## Scoring Global (Agent Recommandation — 2026-06-03, snapshot 10h00 UTC)

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
> 1. La recommandation reste basée sur des données **pre-earnings Q1 2026** (résultats toujours non intégrés dans les feeds Yahoo/FMP au 2026-06-03).
> 2. **Forward P/E négatif** : −70.85× — la profitabilité attendue s'éloigne davantage.
> 3. **Valorisation extrême** : P/E 86.49×, P/B 8.80×, EV/EBITDA 173.62×. Toute déception pourrait déclencher une correction sévère.
> 4. **Consensus PT $66.61 désormais résistance** — upside vers consensus devenu nul (0.0%).
> 5. **Put/Call 2.09** — la structure options reste défensive (puts 67.6%). Le marché options anticipe une correction.
> 6. **Anomalie Max Pain $20.00** dans `data/latest.json` — valeur incohérente, à ignorer. Valeur fiable : $52.00.
> 7. Si cours casse $64.27 sans rebond → signe de faiblesse.
> 8. Si cours casse $60.26 sans rebond → **passer en SURVEILLER**.
> 9. Si cours casse $56.83 sans rebond → **passer en ÉVITER**.
> 10. Si cours casse $48.75 (MM50) → **passer en ÉVITER**.

---

## Conclusion

**Thèse : CONFIRMÉE — Le statut ATTENDRE est maintenu.** Le snapshot 10:00 UTC du 2026-06-03 est **strictement identique** au close officiel du 2026-06-02 ($66.60, RSI 61.11, ATR $5.11, MM50 $48.75). Aucun nouveau flux de marché n'est disponible (marché US fermé jusqu'à 14:30 UTC). Le **DRAFT_refresh déclenché automatiquement à 10:00 UTC par ATR_SPIKE est un faux positif** : l'ATR n'a pas changé ($5.11 =), le trigger est mécanique sur une volatilité historique déjà intégrée dans l'analyse précédente.

**Différentiels clés vs analyse précédente (close officiel 2026-06-02) :**
1. **Cours identique** à $66.60 — aucun mouvement de marché
2. **Volume 51.34 M** — quasi identique (86.1% moyenne vs 90%)
3. **RSI 61.11 =** — inchangé
4. **Forward P/E −70.85× =** — inchangé
5. **P/E TTM 86.49× =** — inchangé
6. **EV/EBITDA Yahoo 170.54× → 173.62×** — révision technique +3.08 pts, pas un mouvement de marché
7. **P/B Yahoo 8.89× → 8.80×** — révision marginale −0.09 pt
8. **Market Cap $23.80 B =** — inchangé
9. **Options : anomalie détectée** — Max Pain $20.00 dans latest.json (incohérent), put/call et call OI null. Valeurs fiables maintenues : Max Pain $52.00, put/call 2.09, call OI 32.4%.
10. **Score Global ajusté 52.5/100 =** — inchangé
11. **Filtre Qualité 4/6 =** — Quality Partielle inchangée
12. **Earnings Q1 2026** — résultats toujours non intégrés dans les feeds
13. **Prochain earnings** : 2026-08-27 (Q2 2026, 85 jours)
14. **DRAFT_refresh archivé** — faux positif ATR_SPIKE, données inchangées

**Recommandation :** Maintenir **ATTENDRE**.
- **Ne pas entrer** à $66.60 — valuation extrême, Forward P/E négatif, consensus PT = cours
- Surveiller l'ouverture du 2026-06-03 : si gap up au-dessus de $67.30 avec volume → reprise du momentum possible
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

*Rapport généré le 2026-06-03 — Données sources : `data/latest.json` (snapshot 10:00 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`.*
