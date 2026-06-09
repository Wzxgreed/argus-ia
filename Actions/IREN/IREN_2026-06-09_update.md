# IREN — Mise à Jour (2026-06-09, snapshot 13:00 UTC)

> **Type :** `_update.md` — Snapshot intra-journalier, 13:00 UTC
> **Référence précédente :** [IREN_2026-06-09_update.md](IREN_2026-06-09_update.md) (snapshot 10:00 UTC)
> **Référence full refresh :** [IREN_2026-06-08_init.md](IREN_2026-06-08_init.md)
> **Données source :** `data/latest.json` (fetched_at 2026-06-09T13:00:01 UTC), `data/recommandations_2026-06-09.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-09.json`, `data/social_sentiment_2026-06-09.json`, `data/fx_exposure_2026-06-09.json`, `data/events_2026-06-09.json`, `data/upcoming_events_2026-06-09.json`

---

## Résumé des Changements (vs snapshot 10:00 UTC 09/06)

| Métrique | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Δ |
|----------|-------------------|-------------------|---|
| **Cours close** | **$59.19** | **$59.19** | **=** |
| **Open** | $56.60 | $56.60 | = |
| **High** | $59.67 | $59.67 | = |
| **Low** | $55.14 | $55.14 | = |
| **Previous close** | $54.35 | $54.35 | = |
| **Volume** | 40.99 M (0.74× moy.) | 40.99 M (0.74× moy.) | = |
| **RSI 14j** | 58.78 | 58.78 | = |
| **ATR 14j** | $5.68 | $5.68 | = |
| **MM 50j** | $50.32 | $50.32 | = |
| **P/E TTM (Yahoo)** | 76.87× | 76.87× | = |
| **Forward P/E** | −62.97× | −62.97× | = |
| **EV/EBITDA (Yahoo)** | 143.88× | **155.63×** | **+8.2%** |
| **EV/Revenue (Yahoo)** | 27.97× | **30.25×** | **+8.2%** |
| **Market Cap (Yahoo)** | $21.15 B | $21.15 B | = |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | $69.12 (26 analysts) | = |
| **Max Pain** | $33.00 | $33.00 | = |
| **Put/Call ratio** | **3.95** | **2.22** | **−1.73 (−43.8%)** |
| **Call OI %** | **20.2%** | **31.0%** | **+10.8 pts** |
| **Short Interest** | 14.72% | 14.72% | = |
| **Score Opportunité** | 5.7/10 | 5.7/10 | = |
| **Score Global ajusté** | 61.8/100 | 61.8/100 | = |
| **Action recommandée** | **ACHETER (Sizing Réduit)** | **ACHETER (Sizing Réduit)** | **=** |

**Mutation principale : Détente structure options.** Le put/call ratio est passé de 3.95 (record historique de défiance) à 2.22, et le call OI a grimpé de 20.2% à 31.0%. Cette détente traduit un retrait partiel du hedging put massif observé depuis le gap down du 8 juin. Les puts restent majoritaires (69.0% de l'OI), signalant que la prudence structurale persiste sans atteindre l'extrémisme du snapshot 10h.

**Mutation secondaire : Révision EV/EBITDA Yahoo (+8.2%).** Les multiples EV/EBITDA et EV/Revenue calculés par Yahoo ont été révisés à la hausse (+8.2%) sans changement de cours, traduisant probablement un ajustement des données sous-jacentes (EBITDA, Revenue) dans le feed Yahoo entre les deux snapshots. Les données FMP (EV/EBITDA 12.34×) restent inchangées.

**Mutations tertiaires : aucune.** Toutes les autres données de cours, technique, fondamentale et consensus sont strictement identiques.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 58.78 | Zone neutre-haute inchangée, à 1.2 pt du seuil 60 |
| **ATR 14j** | $5.68 | Volatilité stable, ATR relatif 9.60% |
| **MM 50j** | $50.32 | Cours **+17.6% au-dessus** — support dynamique intact |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 55.06 M | Volume session ~41.0 M = **74.5%** — sous-moyen confirmé |
| **Range intraday (08/06)** | $55.14 – $59.67 | Clôture à 99.2% du range — domination acheteuse confirmée |
| **52-week high/low** | $76.87 / $8.82 | Cours à **77.0%** du 52W high |

**Niveaux clés (inchangés) :**
- Support immédiat : **$55.14** (low du 2026-06-08)
- Support : **$50.32** (MM50)
- Support intermédiaire : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support structurel : **$46.00** (low 2026-05-19)
- Support majeur : **$45.00** (alerte baisse historique)
- Résistance immédiate : **$59.31** (open du 2026-06-08, gap fill quasi atteint)
- Résistance : **$61.86** (previous close avant gap down du 8 juin)
- Résistance majeure : **$66.60** (close 2026-06-03)
- Résistance consensus : **$69.12** (consensus PT FMP)
- Stop-loss (2×ATR) : **$47.83** (−19.2%)
- Take-profit (3×ATR) : **$76.23** (+28.8%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — Aucun changement technique depuis le snapshot 10h. Le cours stabilisé à $59.19 confirme le rebond post-gap. Le gap fill à $59.31 reste le niveau immédiat à surveiller.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-09. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$21.15 B** | $3.13 B | **−85%** | Yahoo |
| EV/EBITDA | **155.63×** | 12.34× | **−91%** | Yahoo |
| P/B | 7.57× | 1.72× | **−77%** | Yahoo |
| P/E TTM | 76.87× | 35.96× | **−53%** | Yahoo |
| EV/Revenue | **30.25×** | 7.04× | **−77%** | Yahoo |

> **Note :** EV/EBITDA et EV/Revenue Yahoo révisés +8.2% vs snapshot 10h (143.88× / 27.97×). Les données FMP sont inchangées.

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−62.97)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **76.87×** — niveaux élevés, inchangés
- Forward P/E **−62.97×** — profitabilité attendue éloignée
- EV/EBITDA Yahoo **155.63×** — révisé +8.2% vs 10h, niveau extrêmement élevé
- **Cours $59.19 vs Consensus PT $69.12** — upside **+16.8%**

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].
> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs snapshot 10:00 UTC |
|--------|--------|-----------------------------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = |
| **Max Pain** | **$33.00** (exp 2026-06-12) | = |
| **Put/Call ratio** | **2.22** | **−1.73 (−43.8%)** — détente significative |
| **Call OI %** | **31.0%** | **+10.8 pts** — regain d'intérêt call |
| **Short Interest** | 14.72% | = — fuel squeeze présent |
| **Social Sentiment** | Aucun buzz retail | = |
| **Event-Driven** | Aucun événement | = |
| **News Yahoo** | Aucune | = |
| **Geo Risk** | Score 3/10, flag "low" | = |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = |

**Agent Sector Rotation (2026-06-09) :**
- XLK : momentum score **10.0/10** (top sector, return 20d +4.93%)
- Signal global : **NEUTRAL** (regime UNKNOWN)
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Verdict : Fortement corrélé — inchangé

**Analyse options — détente significative mais prudence persistante :**
La structure options s'est nettement détendue entre le snapshot 10h et 13h :
- Put/call **2.22** (vs 3.95 record) — retrait du hedging défensif massif
- Call OI **31.0%** (vs 20.2%) — regain d'intérêt pour les calls
- Puts **69.0%** — toujours majoritaires, la défiance reste élevée

**Interprétation institutionnelle :**
La détente de 3.95 à 2.22 traduit probablement un **déshedging partiel** des positions puts ouvertes en amont du gap down du 8 juin, ou un arbitrage post-gap. Avec 69% de puts encore en OI, la structure reste défensive. Le niveau 2.22 est encore supérieur à la moyenne historique observée sur IREN (typiquement 1.0–1.5), signalant que le marché ne fait pas encore confiance au rebond.

Deux scénarios possibles :
1. **Déshedging technique** — les puts ouverts à $54–$56 sont en train d'être clos ou roulés, libérant du gamma haussier si le cours se maintient
2. **Repositionnement call** — anticipation d'un test du gap fill $59.31 ou de la résistance $61.86

Le signal contrarian s'atténue mais persiste. Le passage sous put/call 2.0 serait un signal de confirmation haussier additionnel.

---

## Scoring Global (Agent Recommandation — 2026-06-09, snapshot 13:00 UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.3/10 | 35% | 2.21 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 7.5/10 | 25% | 1.88 |
| **Score Opportunité** | **5.7/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible (−5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10.0/10) — alignement favorable → bonus +5.0 pts
- Quant Report : insuffisant (p-value 1.0, 0 signaux) — pas de malus/bonus
- Crypto Correlation : divergence score 4/10, beta 2.1 → malus volatilité (−5.0 pts)

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 57.0/100 | −10.0 | +5.0 | **61.8/100** |

**Action recommandée : ACHETER (Sizing Réduit)**
- Prix d'entrée suggéré : $59.19
- Stop-loss : $47.83 (−19.2%)
- Take-profit : $76.23 (+28.8%)
- Ratio R/R : 1.5 : 1
- Horizon : 1–3 mois
- Timing : Favorable

> **⚠️ Avertissements :**
> 1. Recommandation basée sur des données **pre-earnings Q1 2026** (résultats toujours non intégrés dans les feeds Yahoo/FMP, 15 jours après le J0 annoncé).
> 2. **Sizing réduit obligatoire** — Beta 4.232 et ATR 9.60% imposent max 5% du portefeuille.
> 3. **Volume sous-moyen** — 0.74× moyenne 20j = participation institutionnelle modérée.
> 4. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC. Surveiller $75k comme seuil critique.
> 5. **Forward P/E négatif** : −62.97× — profitabilité attendue éloignée.
> 6. **Valorisation** : P/E 76.9×, EV/EBITDA 155.6× — multiples extrêmement élevés.
> 7. **Défiance options atténuée mais persistante** : put/call 2.22, puts 69.0% — le marché reste sur la défensive.
> 8. Si cours casse $50.32 (MM50) sans rebond → réviser la position.
> 9. Si cours casse $46.00 (low 19/05) → **passer en SURVEILLER**.
> 10. Si cours casse $47.83 (SL) → **stopper la position**.
> 11. Si gap fill $59.31 avec volume confirmé > moyenne 20j → momentum haussier retrouvé.
> 12. Si structure options se détend davantage (put/call < 2.0) avec rebond du cours → signal haussier additionnel.

---

## Conclusion

**Thèse : CONFIRMÉE — ACHETER (Sizing Réduit) maintenu.**

Le snapshot 13:00 UTC confirme la **stabilité totale** des données de cours, technique et fondamentale principales vs le snapshot 10:00 UTC. La seule mutation significative est la **détente de la structure options** (put/call 3.95 → 2.22, call OI 20.2% → 31.0%), qui atténue l'alerte contrarian sans l'annuler. La thèse reste inchangée.

**Différentiels clés vs analyse précédente (snapshot 10:00 UTC) :**
1. **Cours** : $59.19 → $59.19 — stabilité totale
2. **Volume** : 40.99 M → 40.99 M — inchangé
3. **RSI** : 58.78 → 58.78 — inchangé
4. **MM50** : $50.32 → $50.32 — inchangé
5. **Multiples** : P/E 76.87×, Forward P/E −62.97× — inchangés ; EV/EBITDA 143.88× → **155.63×** (+8.2%, révision Yahoo)
6. **Consensus PT** : $69.12 — inchangé
7. **Options put/call** : 3.95 → **2.22** — **détente significative**
8. **Call OI** : 20.2% → **31.0%** — **regain d'intérêt call**
9. **Max Pain** : $33.00 — inchangé
10. **Scores** : Catalyseur 6.3, Valorisation 4.0, Momentum 7.5 — Score Opportunité 5.7/10, Global 61.8/100
11. **Niveaux** : SL $47.83, TP $76.23 — inchangés
12. **Aucune news** : Le calme intra-journalier maintient la configuration technique du 8 juin

**Recommandation :**
- **Entrer** à $59.19 avec SL $47.83 / TP $76.23 (R/R 1.5)
- **Sizing réduit** — max 5% du portefeuille (beta 4.232, ATR 9.60%)
- Surveiller la suite de séance US du 9 juin — si le cours comble le gap $59.31 avec volume > moyenne 20j → confirmation haussière
- Premier objectif : $61.86 (previous close avant gap down)
- Deuxième objectif : $66.60 (close 03/06) puis $69.12 (consensus PT)
- Si structure options se détend sous put/call 2.0 → signal contrarian s'atténue, momentum renforcé
- Si rupture sous $50.32 (MM50) → réviser la position
- Si rupture sous $46.00 (low 19/05) → **passer en SURVEILLER**
- Si rupture sous $47.83 (SL) → **stopper la position**

---

*Rapport rédigé le 2026-06-09 — Données sources : `data/latest.json` (fetched_at 2026-06-09T13:00:01 UTC), `data/recommandations_2026-06-09.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-09.json`, `data/social_sentiment_2026-06-09.json`, `data/fx_exposure_2026-06-09.json`, `data/events_2026-06-09.json`, `data/upcoming_events_2026-06-09.json`.*
