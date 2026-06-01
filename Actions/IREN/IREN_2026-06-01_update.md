# IREN — Mise à Jour Post-Session (2026-06-01, snapshot 13:00 UTC)

> **Type :** `_update.md` — Mise à jour post-session (révision snapshot 13:00 UTC)
> **Référence précédente :** [IREN_2026-06-01_update.md](IREN_2026-06-01_update.md) (snapshot 10:00 UTC)
> **Données source :** `data/latest.json` (timestamp 2026-06-01T13:00:07+00:00), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`

---

## Résumé des Changements

| Métrique | 2026-06-01 (10:00 UTC) | 2026-06-01 (13:00 UTC) | Δ |
|----------|------------------------|------------------------|---|
| **Cours close** | $63.54 | **$63.54** | **=** |
| **Previous close** | $64.05 | **$64.05** | **=** |
| **Open** | $64.70 | **$64.70** | **=** |
| **High** | $64.745 | **$64.745** | **=** |
| **Low** | $60.73 | **$60.73** | **=** |
| **Volume** | 50.22 M | **50.22 M** | **=** |
| **Volume vs 20j** | 87.1% | **87.1%** | **=** |
| **RSI 14j** | 52.36 | **52.36** | **=** |
| **ATR 14j** | $5.26 | **$5.26** | **=** |
| **MM 50j** | $47.77 | **$47.77** | **=** |
| **P/E TTM (Yahoo)** | 82.52× | **82.52×** | **=** |
| **Forward P/E (Yahoo)** | −67.60× | **−67.60×** | **=** |
| **P/B (Yahoo)** | 8.39× | **8.39×** | **=** |
| **Market Cap (Yahoo)** | $22.71 B | **$22.71 B** | **=** |
| **Short Interest** | 14.72% | **14.72%** | **=** |
| **Consensus PT (FMP)** | $66.61 (23 analysts) | **$66.61 (23 analysts)** | **=** |
| **Max Pain** | $20.00 [ANOMALIE] | **$52.00** | **✅ CORRIGÉ** |
| **Put/Call ratio** | null | **3.01** | **✅ DISPONIBLE** |
| **Call OI %** | null | **24.9%** | **✅ DISPONIBLE** |
| **Score Opportunité** | 4.8/10 | **4.8/10** | **=** |
| **Score Global ajusté** | 53.0/100 | **53.0/100** | **=** |
| **Action recommandée** | ATTENDRE | **ATTENDRE** | **=** |

**Mutation significative :** Aucune mutation de prix ou de données fondamentales entre les snapshots 10:00 UTC et 13:00 UTC. **Seule la structure options a été corrigée** : Max Pain passe de **$20.00 (anomalie)** à **$52.00** (cohérent avec le range historique récent), put/call ratio **3.01**, call OI **24.9%**. Cette correction confirme la défiance massive des options traders (puts à 75.1%) mais élimine le tail risk aberrant de −68.5% vers $20.00. Le cours reste inchangé à **$63.54**, sous le consensus ($66.61), avec un upside restauré de **+4.8%**.

**Points critiques :**
1. **Cours $63.54 < Consensus PT $66.61** — upside vers consensus : **+4.8%** (inchangé).
2. **Forward P/E −67.60×** — détérioration sévère maintenue, profitabilité attendue s'éloigne.
3. **Short Interest 14.72%** — baisse de 2.15 pts vs 27/05, moins de fuel squeeze.
4. **Max Pain corrigé $52.00** — ✅ anomalie résolue. Tail risk désormais −18.2% (cohérent vs −68.5% erroné).
5. **Put/Call 3.01** — défiance record des options traders, puts majoritaires à 75.1%.
6. **Score Global ajusté 53.0/100** — creuse l'écart avec le seuil ACHETER (≥60).

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 52.36 | Zone neutre — pas de surachat, pas de survente |
| **ATR 14j** | $5.26 | Volatilité élevée mais en retrait (beta 4.179, ATR relatif 8.28%) |
| **MM 50j** | $47.77 | Cours **+33.0% au-dessus** — tendance haussière intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 57.65 M | Volume du jour 50.22 M = **87.1%** du moyen |
| **Range intraday** | $60.73 – $64.745 | Range de 6.6%, consolidé |
| **52-week high/low** | $76.87 / $8.315 | Cours à **82.6%** du 52W high |

**Niveaux clés (inchangés) :**
- Support immédiat : **$60.73** (low du jour)
- Support intermédiaire : **$59.83** (low du 27/05)
- Support structurel : **$56.83** (breakout level du rally du 25/05)
- Support majeur : **$47.77** (MM50)
- Résistance immédiate : **$64.745** (high du jour)
- Résistance majeure : **$66.29** (high du 27/05) / **$76.87** (52-week high)
- Stop-loss (2×ATR) : **$53.02** (−16.6%)
- Take-profit (3×ATR) : **$79.32** (+24.8%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — La tendance haussière reste intacte (cours +33% au-dessus de la MM50). Cependant, le retrait de −4% depuis le sommet du 27/05 et la détérioration du Forward P/E imposent la prudence. La vigilance porte sur le maintien au-dessus de $60.73 en clôture.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** n'est intégré dans les sources Yahoo/FMP au snapshot 2026-06-01. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $22.71 B | $3.13 B | **−86%** | Yahoo |
| **EV/EBITDA** | 166.19× | 12.34× | **−93%** | Yahoo |
| **P/B** | 8.39× | 1.72× | **−80%** | Yahoo |
| **P/E TTM** | 82.52× | 35.96× | **−56%** | Yahoo |
| **EV/Sales** | 32.31× | 7.04× | **−78%** | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−67.60)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans les données FMP

**Valorisation :**
- P/E TTM Yahoo **82.52×** — retrait de 4% vs 27/05 mais reste extrême
- EV/EBITDA Yahoo **166.19×** — inchangé, toujours extrême
- Forward P/E **−67.60×** — détérioration sévère maintenue
- P/B Yahoo **8.39×** — book value ne justifie pas le multiple
- **Cours $63.54 < Consensus PT $66.61** — upside vers consensus : **+4.8%**

> **[DONNÉES PARTIELLES]** — `data/validation_report.txt` indique le warning IREN : Quality Partielle 4/6, Forward PE négatif, FCF négatif. `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $66.61 (23 analysts) | Inchangé — +2 analysts vs 27/05, PT +$0.75 |
| **Max Pain** | $52.00 (exp 2026-06-05) | **✅ CORRIGÉ** vs $20.00 anomalie (10:00 UTC) |
| **Put/Call ratio** | **3.01** | **✅ DISPONIBLE** — défiance record, puts 75.1% |
| **Call OI %** | **24.9%** | **✅ DISPONIBLE** — calls minoritaires |
| **Short Interest** | 14.72% | Inchangé vs 10:00 UTC, −2.15 pts vs 27/05 |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz |
| **Event-Driven** | Aucun événement | `data/events_latest.json` vide |
| **News Yahoo** | Aucune | `data/news_latest.json` vide |
| **Geo Risk** | Score 3/10, flag "low" | Inchangé |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | Neutre |

**Agent Sector Rotation (2026-06-01) :**
- XLK : momentum score **10.0/10** (top sector, return 20d +19.76%)
- Signal global : **ROTATION_TO_DEFENSIVE** (regime UNKNOWN)
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Commentaire :** La structure options a été **corrigée et enrichie** au snapshot 13:00 UTC :
- **Max Pain $52.00** (vs $20.00 erroné au 10:00 UTC) — valeur cohérente avec le range historique récent ($33–$45 précédemment, désormais $52.00 sur expiration 2026-06-05). Le tail risk aberrant de −68.5% est éliminé ; le nouveau tail risk est −18.2%.
- **Put/Call ratio 3.01** — puts majoritaires à 75.1%, niveau de défiance record (vs 2.35 au 25/05, 1.88 au 27/05). Les options traders anticipent une correction ou se couvrent massivement.
- **Call OI 24.9%** — calls minoritaires, confirmant le sentiment défensif.

Le consensus analystes reste stable (23 analysts, PT $66.61). La baisse du Short Interest (−2.15 pts à 14.72%) réduit le potentiel de short squeeze mais atténue aussi la pression technique à la baisse. Aucun événement corporate détecté.

---

## Scoring Global (Agent Recommandation — 2026-06-01, snapshot 13:00 UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 5.3/10 | 35% | 1.86 |
| **Valorisation** | 3.0/10 | 40% | 1.20 |
| **Momentum** | 7.0/10 | 25% | 1.75 |
| **Score Opportunité** | **4.8/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible
- FX Impact Score 0/10 → neutre
- Accounting Risk : `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10.0/10) — alignement favorable → bonus

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 48.0/100 | — | +5.0 | **53.0/100** |

**Action recommandée : ATTENDRE**
- Prix d'entrée suggéré : $63.54
- Stop-loss : $53.02 (−16.6%)
- Take-profit : $79.32 (+24.8%)
- Ratio R/R : 1.5 : 1
- Horizon : —
- Timing : Favorable

> **⚠️ Avertissements :**
> 1. La recommandation reste basée sur des données **pre-earnings Q1 2026** (résultats toujours non intégrés dans les feeds Yahoo/FMP au 2026-06-01).
> 2. **Forward P/E détérioré** : −67.60× vs −49.20× du 27/05 — la profitabilité attendue s'éloigne.
> 3. **Valorisation extrême** : P/E 82.52×, P/B 8.39×, EV/EBITDA 166.19×. Toute déception pourrait déclencher une correction sévère.
> 4. **Put/Call 3.01** — défiance record des options traders. Le marché options anticipe une correction.
> 5. **Short Interest 14.72%** — en baisse, moins de fuel squeeze.
> 6. Si cours casse $60.73 sans rebond → **passer en SURVEILLER**.
> 7. Si cours casse $56.83 sans rebond → **passer en ÉVITER**.
> 8. Si cours casse $47.77 (MM50) → **passer en ÉVITER**.

---

## Conclusion

**Thèse : CONFIRMÉE — Le statut ATTENDRE est maintenu.** Aucune mutation de prix ni de données fondamentales entre les snapshots 10:00 UTC et 13:00 UTC du 2026-06-01. La seule évolution matérielle est la **correction de l'anomalie options** (Max Pain $20.00 → $52.00) et la disponibilité du put/call ratio (3.01) et du call OI (24.9%). Ces données corrigées confirment la **défiance massive des options traders** (puts à 75.1%) mais éliminent le tail risk aberrant de −68.5%. Le Score Global ajusté reste à **53.0/100**, hors zone ACHETER. Aucun nouvel élément structurant n'est apparu depuis le 27/05.

**Différentiels clés vs analyse précédente (snapshot 10:00 UTC) :**
1. **Cours inchangé** à $63.54 — consolidation stable post-sommet $66.29
2. **Max Pain corrigé** : $20.00 [ANOMALIE] → $52.00 ✅ — tail risk réaligné à −18.2%
3. **Put/Call ratio 3.01** — nouveau signal de défiance record (puts 75.1%)
4. **Call OI 24.9%** — calls minoritaires, couverture massive
5. **Consensus PT, Short Interest, RSI, ATR, MM50 inchangés**
6. **Forward P/E −67.60×** — détérioration fondamentale maintenue
7. **Scores inchangés** : Opportunité 4.8/10, Global 53.0/100
8. **Filtre Qualité 4/6** — Quality Partielle inchangée
9. **Earnings Q1 2026** — résultats toujours non intégrés dans les feeds
10. **Prochain earnings** : 2026-08-27 (Q2 2026, 87 jours)

**Recommandation :** Maintenir **ATTENDRE**.
- **Ne pas entrer** à $63.54 — le risque/rendement reste défavorable (Forward P/E −67.6×, EV/EBITDA 166×, put/call 3.01)
- Les détenteurs de positions existantes peuvent maintenir avec SL $53.02 / TP $79.32
- Si earnings beat + guidance HPC forte + FCF positif → réévaluation possible vers ACHETER
- Si miss ou guidance cut → attendre retour vers $56.83 puis $50
- Si cours casse $60.73 sans rebond → **passer en SURVEILLER**
- Si cours casse $56.83 sans rebond → **passer en ÉVITER**
- Si cours casse $47.77 (MM50) → **passer en ÉVITER**

---

*Rapport généré le 2026-06-01 — Données sources : data/latest.json (13:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json*
