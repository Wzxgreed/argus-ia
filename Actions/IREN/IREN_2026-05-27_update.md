# IREN — Mise à Jour Quotidienne (2026-05-27, snapshot 13:00 UTC)

> **Type :** `_update.md` — Mise à jour post-session (snapshot 13:00 UTC)
> **Référence précédente :** [IREN_2026-05-26_update.md](IREN_2026-05-26_update.md) (snapshot 21:00 UTC)
> **Données source :** `data/latest.json` (timestamp 2026-05-27T13:00:07+00:00), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/news_latest.json`

---

## Résumé des Changements

| Métrique | 2026-05-26 (21:00 UTC) | 2026-05-27 (13:00 UTC) | Δ |
|----------|------------------------|------------------------|---|
| **Cours close** | $59.78 | **$59.78** | **=** |
| **Previous close** | $56.83 | **$56.83** | **=** |
| **Open** | $59.68 | **$59.68** | **=** |
| **High** | $61.47 | **$61.49** | **+$0.02** |
| **Low** | $58.61 | **$58.61** | **=** |
| **Volume** | 40.53 M | **41.65 M** | **+2.8%** |
| **Volume vs 20j** | 76.2% | **78.2%** | **+2.0 pts** |
| **RSI 14j** | 54.85 | **54.85** | **=** |
| **ATR 14j** | $5.68 | **$5.68** | **=** |
| **MM 50j** | $46.46 | **$46.46** | **=** |
| **P/E TTM (Yahoo)** | 77.64× | **77.64×** | **=** |
| **Forward P/E (Yahoo)** | −44.45× | **−44.45×** | **=** |
| **P/B (Yahoo)** | 7.90× | **7.90×** | **=** |
| **EV/EBITDA (Yahoo)** | 149.90× | **157.06×** | **+4.8%** |
| **Max Pain** | $45.00 | **$45.00** | **=** |
| **Put/Call ratio** | 3.16 | **1.88** | **−1.28 pt** |
| **Call OI %** | 24.0% | **34.7%** | **+10.7 pts** |
| **Score Opportunité** | 5.8/10 | **5.8/10** | **=** |
| **Score Global ajusté** | 63.3/100 | **63.3/100** | **=** |

**Mutation significative :** Aucune mutation de cours ni de scores entre le close du 26/05 et le snapshot 13:00 UTC du 27/05. Le cours reste à **$59.78** (+5.19% vs previous close du 25/05). Cependant, **deux ajustements notables** apparaissent :

1. **Données options corrigées** : le put/call ratio est révisé à **1.88** (vs 3.16 au snapshot 21:00 UTC) et le call OI remonte à **34.7%** (vs 24.0%). Cette révision indique une **défiance options nettement moins extrême** que ce qui était lu hier soir. L'expiration hebdomadaire du 2026-05-29 reste imminente.
2. **EV/EBITDA Yahoo révisé à 157.06×** (vs 149.90×) — écart de +4.8%, possible ajustement post-close. Le multiple reste extrême.

**Earnings Q1 2026 (J=0) :** toujours attendu — aucun flux post-earnings intégré au snapshot 13:00 UTC.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 54.85 | Zone neutre inchangée — pas de surachat malgré le rally |
| **ATR 14j** | $5.68 | Volatilité élevée persistante (beta 4.179, ATR relatif 9.50%) |
| **MM 50j** | $46.46 | Cours **+28.7% au-dessus** — tendance haussière intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 53.24 M | Volume du jour 41.65 M = **78.2%** du moyen |
| **Range intraday** | $58.61 – $61.49 | Expansion haussière du range, high à +2.9% du close |
| **52-week high/low** | $76.87 / $8.28 | Cours à **77.8%** du 52W high |

**Niveaux clés (inchangés) :**
- Support immédiat : **$58.61** (low du jour)
- Support intermédiaire : **$56.83** (previous close du 25/05)
- Support structurel : **$50.46** (breakout level du rally) / **$46.46** (MM50)
- Résistance immédiate : **$61.49** (high du jour)
- Résistance majeure : **$65.86** (consensus PT FMP, 21 analysts)
- Stop-loss (2×ATR) : **$48.42** (−19.0%)
- Take-profit (3×ATR) : **$76.82** (+28.5%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — La tendance haussière reste intacte. Le cours évolue largement au-dessus de la MM50. La vigilance porte sur le maintien au-dessus de $56.83 et sur le test de $61.49 en clôture.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** n'est intégré dans les sources Yahoo/FMP au snapshot 13:00 UTC. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $21.36 B | $3.13 B | **−85%** | Yahoo |
| **EV/EBITDA** | 157.06× | 12.34× | **−92%** | Yahoo |
| **P/B** | 7.90× | 1.72× | **−78%** | Yahoo |
| **P/E TTM** | 77.64× | 35.96× | **−54%** | Yahoo |
| **EV/Sales** | 30.53× | 7.04× | **−77%** | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−44.45)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans les données FMP

**Valorisation dégradée — reste stretched :**
- P/E TTM Yahoo **77.64×** — expansion significative post-rally
- EV/EBITDA Yahoo **157.06×** (+4.8% vs snapshot 21:00 UTC) — multiple extrême révisé à la hausse
- Forward P/E **−44.45×** — attente de profits s'éloigne encore
- P/B Yahoo **7.90×** — book value ne justifie pas le multiple

> **[DONNÉES PARTIELLES]** — `data/validation_report.txt` confirme le warning IREN : Quality Partielle 4/6, Forward PE négatif, FCF négatif.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $65.86 (21 analysts) | Inchangé — upside +10.2% |
| **Max Pain** | $45.00 (exp 2026-05-29) | Inchangé — tail risk −24.7% |
| **Put/Call ratio** | 1.88 | **Révisé à la baisse** — défiance nettement moins extrême |
| **Call OI %** | 34.7% | **Révisé à la hausse** — calls majoritaires vs 24.0% hier |
| **Short Interest** | 0.169% | Très faible |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz |
| **Event-Driven** | Aucun événement | `data/events_latest.json` vide |
| **News Yahoo** | Aucune | `data/news_latest.json` vide |
| **Geo Risk** | Score 3/10, flag "low" | Inchangé |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | Neutre |

**Agent Sector Rotation (2026-05-27) :**
- XLK : momentum score **10.0/10** (top sector)
- XLE : bullish crossover détecté
- Signal global : **ROTATION_TO_CYCLICAL**
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Commentaire :** La structure options affiche une **révision notable** par rapport au snapshot 21:00 UTC du 26/05. Le put/call ratio est révisé de 3.16 à **1.88** et le call OI de 24.0% à **34.7%**. Cette correction suggère que la "défiance record" constatée hier était en partie un artefact de données (probablement lié à l'expiration imminente du 2026-05-29 et au rollover des positions). La structure reste défensive (puts majoritaires à 65.3%), mais nettement moins extrême. Le consensus analystes ($65.86 PT) reste haussier.

---

## Scoring Global (Agent Recommandation — 2026-05-27, snapshot 13:00 UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 7.3/10 | 35% | 2.56 |
| **Valorisation** | 3.5/10 | 40% | 1.40 |
| **Momentum** | 7.5/10 | 25% | 1.88 |
| **Score Opportunité** | **5.8/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible (−5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10/10) — alignement favorable → **bonus +10.0 pts**

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 58.3/100 | −5.0 | +10.0 | **63.3/100** |

**Action recommandée : ACHETER — Sizing Réduit**
- Prix d'entrée suggéré : $59.78
- Stop-loss : $48.42 (−19.0%)
- Take-profit : $76.82 (+28.5%)
- Ratio R/R : 1.5 : 1
- Horizon : 1–3 mois
- Timing : Favorable

> **⚠️ Avertissements :**
> 1. La recommandation reste basée sur des données **pre-earnings**. L'annonce du Q1 2026 est attendue aujourd'hui (J=0, 2026-05-27) — aucun flux post-earnings intégré au snapshot 13:00 UTC.
> 2. Sizing réduit impératif (beta 4.179, ATR relatif 9.50%).
> 3. **Défiance options atténuée** : put/call 1.88, call OI 34.7% — le marché reste défensif mais moins extrême qu'hier. Max Pain $45.00 = ancrage de risque de queue −24.7%.
> 4. Si cours casse $56.83 sans rebond → **passer en ATTENDRE**.
> 5. Si cours casse $50.46 sans rebond → **passer en ATTENDRE**.
> 6. Si cours casse $46.46 (MM50) → **passer en ÉVITER**.

---

## Conclusion

**Thèse : CONFIRMÉE — Le rally haussier se maintient à $59.78 (+5.19% vs previous close du 25/05, +25.2% depuis le 20/05) avec une correction notable de la structure options (put/call 1.88 vs 3.16 hier). La valorisation reste stretched (P/E 77.6×, EV/EBITDA 157.1×). Le Score Global ajusté reste à 63.3/100 (bas de la zone ACHETER). Earnings Q1 2026 (J=0) toujours attendu, résultats non publiés au snapshot 13:00 UTC.**

Le snapshot 13:00 UTC du 2026-05-27 confirme la stabilité des données de cours ($59.78, RSI 54.85, ATR $5.68, MM50 $46.46) avec deux ajustements importants :
1. **Structure options révisée** : put/call 1.88 (vs 3.16) et call OI 34.7% (vs 24.0%) — la "défiance record" d'hier était en partie un artefact de données lié à l'expiration du 2026-05-29
2. **EV/EBITDA Yahoo révisé à 157.06×** (vs 149.90×) — valuation encore plus stretched

**Points clés :**
1. **Cours stable à $59.78** — consolidation au sommet du rally
2. **High $61.49** — test de la zone $61–$62, à +2.9% du close
3. **Volume légèrement en hausse** (41.65M, 78.2% du moyen) mais toujours sous la moyenne 20j
4. **P/E TTM 77.64×** — valuation stretched inchangée
5. **Scores inchangés** — Opportunité 5.8/10, Global 63.3/100
6. **Momentum inchangé** — 7.5/10, MM50 $46.46
7. **Défiance options atténuée** — put/call 1.88, call OI 34.7%, puts à 65.3%
8. **Earnings J=0** — résultats attendus aujourd'hui (2026-05-27), non publiés au snapshot 13:00 UTC
9. **Filtre Qualité 4/6** — Quality Partielle inchangée
10. **Sector XLK top momentum** (10/10) — alignement favorable

**Recommandation :** Maintenir **ACHETER à sizing réduit** avec SL $48.42 / TP $76.82.
- **Ne pas renforcer** avant publication des résultats Q1 2026
- Si earnings beat + guidance HPC forte + FCF positif → possibilité de renforcement
- Si miss ou guidance cut → attendre retour vers $56.83 puis $50.46
- Si cours casse $56.83 sans rebond → **passer en ATTENDRE**
- Si cours casse $50.46 sans rebond → **passer en ATTENDRE**
- Si cours casse $46.46 (MM50) → **passer en ÉVITER**

---

*Rapport généré le 2026-05-27 — Données sources : data/latest.json (13:00 UTC), data/recommandations_latest.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/news_latest.json*
