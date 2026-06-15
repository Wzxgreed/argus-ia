# IREN — Mise à Jour (2026-06-15, snapshot 10:00 UTC)

> **Type :** `_update.md` — Mise à jour post-FULL REFRESH
> **Référence précédente :** [IREN_2026-06-10_update.md](IREN_2026-06-10_update.md) (snapshot 13h UTC 10/06)
> **Données source :** `data/latest.json` (fetched_at 2026-06-15T10:00:02 UTC), `data/recommandations_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`
> **Triggers FULL REFRESH :** PRICE_GAP +5.40% (seuil ±5.0%), ATR_SPIKE 10.49% (seuil 5.0%)

---

## Résumé des Changements (vs Snapshot 13h UTC 2026-06-10)

| Métrique | 2026-06-10 | 2026-06-15 | Δ |
|----------|-----------|-----------|---|
| **Cours close** | Indisponible (pre-market) | **$59.77** | — |
| **Previous close** | $59.19 | **$56.71** | −$2.48 (−4.2%) |
| **Change % session** | — | **+5.40%** | — |
| **Volume** | 56.48 M | **45.35 M** | −11.13 M (−19.7%) |
| **Volume vs 20j** | 108.1% | **91.0%** | −17.1 pts |
| **RSI 14j** | 62.18 | **52.86** | −9.32 pts (normalisation) |
| **ATR 14j** | N/A | **$6.27** | ✅ Disponible |
| **MM 50j** | N/A | **$52.06** | ✅ Disponible |
| **MM 200j** | N/A | **N/A** | = — [DONNÉES MANQUANTES] |
| **Short Interest** | 16.05% | **16.05%** | = |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | **$69.12 (26 analysts)** | = |
| **P/E TTM** | 70.16× | **77.62×** | +7.46 pts (dégradation mécanique) |
| **Forward P/E** | −57.47× | **−63.59×** | −6.12 pts (détérioration) |
| **EV/EBITDA** | 143.08× | **157.04×** | +13.96 pts (dégradation mécanique) |
| **EV/Revenue** | 27.81× | **30.53×** | +2.72 pts |
| **P/B** | 6.91× | **7.65×** | +0.74 pt |
| **Max Pain** | $50.00 (valeur fiable) | **$100.00** | **ANOMALIE** — [DONNÉES CORROMPUES] |
| **Put/Call ratio** | 1.92 | **null** | **Indisponible** — [DONNÉES MANQUANTES] |
| **Call OI %** | 34.2% | **0.0%** | **ANOMALIE** — [DONNÉES CORROMPUES] |
| **Score Opportunité** | 4.4/10 | **5.7/10** | **+1.3 pt** |
| **Score Catalyseur** | 5.3/10 | **6.3/10** | **+1.0 pt** |
| **Score Valorisation** | 3.0/10 | **4.0/10** | **+1.0 pt** |
| **Score Momentum** | 5.5/10 | **7.5/10** | **+2.0 pts** |
| **Score Global ajusté** | 44.3/100 | **61.8/100** | **+17.5 pts** |
| **Action recommandée** | **SURVEILLER** | **ACHETER (Sizing Réduit)** | **UPGRADE** |

**Mutation principale : Upgrade algorithmique majeur SURVEILLER → ACHETER.** Le snapshot du 2026-06-15 révèle une révision substantielle du scoring agent : Score Global ajusté rehaussé de **44.3 à 61.8/100** (+17.5 pts), porté par une amélioration simultanée des trois axes (Catalyseur +1.0, Valorisation +1.0, Momentum +2.0). Le Momentum technique bondit à **7.5/10** (vs 5.5), le Catalyseur à **6.3/10** (vs 5.3), et la Valorisation à **4.0/10** (vs 3.0). Cet upgrade coïncide avec le **gap +5.40%** et l'ATR spike de 10.49% qui ont déclenché le FULL REFRESH.

**Mutation secondaire : Données techniques désormais complètes.** L'ATR 14j (**$6.27**) et la MM50 (**$52.06**) sont enfin disponibles dans `data/latest.json`, après plusieurs jours d'indisponibilité. Le cours à **$59.77** se situe à **+14.8%** au-dessus de la MM50, confirmant une tendance haussière intermédiaire. Le RSI se normalise à **52.86** (zone neutre) contre 62.18 (neutre-haute) précédemment, ce qui est favorable à l'entrée (moins de surachat).

**Mutation tertiaire : Anomalies options persistantes.** Le snapshot 10h UTC du 15/06 retourne des valeurs options incohérentes : Max Pain **$100.00** (vs $50.00 fiable), put/call **null**, call OI **0.0%**. Ces données sont considérées comme corrompues. Les dernières valeurs fiables restent : Max Pain **$50.00**, put/call **1.92**, call OI **34.2%** (snapshot 13h 10/06). Le spread option est donc stable mais non confirmé par le dernier snapshot.

**Mutation quaternaire : Multiples mécaniquement dégradés.** Le rally +5.4% a poussé la valorisation à des niveaux encore plus élevés : P/E TTM **77.62×** (vs 70.16×), EV/EBITDA **157.04×** (vs 143.08×), Forward P/E **−63.59×** (vs −57.47×). Cette dégradation mécanique est cohérente avec la hausse de cours sans amélioration fondamentale mesurable dans les feeds.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 52.86 | Zone neutre, normalisation vs 62.18 (10/06). Moins de surachat, favorable à l'entrée |
| **ATR 14j** | $6.27 | **Disponible** — volatilité journalière moyenne 10.49% du cours |
| **MM 50j** | $52.06 | **Disponible** — cours à +14.8% au-dessus, tendance haussière intermédiaire confirmée |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 49.85 M | Volume session 45.35 M = **91.0%** moyenne — volume normal, pas de distribution |
| **52-week high/low** | $76.87 / $9.52 | Close à **77.7%** du 52W high |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |
| **Open / High / Low** | $56.505 / $61.40 / $55.94 | Range intraday 9.6% — volatilité élevée mais contrôlée |

**Niveaux clés (basés sur données réelles du 2026-06-15) :**
- Support immédiat : **$55.94** (low du 2026-06-15)
- Support secondaire : **$56.71** (previous close du 14/06)
- Support critique : **$52.06** (MM50) — cassure = révision en ATTENDRE
- Support structurel : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support majeur : **$47.23** (stop-loss ATR 2× = $59.77 − $12.54)
- Résistance immédiate : **$61.40** (high du 2026-06-15)
- Résistance : **$66.60** (close 2026-06-02, ancien sommet)
- Résistance majeure : **$69.12** (consensus PT FMP)
- Résistance extrême : **$76.87** (52-week high)
- Stop-loss (2×ATR) : **$47.23** (−21.0% vs close) — niveau fiable désormais
- Take-profit (3×ATR) : **$78.58** (+31.5% vs close) — niveau fiable désormais
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable.** Après plusieurs jours d'indisponibilité, les données techniques sont rétablies. Le RSI à 52.86 est en zone neutre favorable (ni surachat ni survente). Le cours se tient nettement au-dessus de la MM50 ($52.06), confirmant une tendance haussière intermédiaire. Le volume est normal (91% moyenne), sans signe de distribution. Le range intraday 9.6% est élevé mais cohérent avec le beta 4.232. La normalisation du RSI (62.18 → 52.86) est un signal d'entrée favorable.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-15 (21 jours après le J0 annoncé). Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$21.36 B** | $3.13 B | **−85%** | Yahoo |
| P/E (TTM) | **77.62×** | 35.96× | **−54%** | Yahoo |
| P/B | **7.65×** | 1.72× | **−78%** | Yahoo |
| Forward P/E | **−63.59×** | N/A | — | Yahoo |
| EV/EBITDA | **157.04×** | 12.34× | **−92%** | Yahoo |
| EV/Revenue | **30.53×** | 7.04× | **−77%** | Yahoo |
| Short Interest | **16.05%** | N/A | — | Yahoo |

> **Note :** Les écarts Yahoo vs FMP demeurent extrêmes. L'EV/EBITDA Yahoo **157.04×** et l'EV/Revenue **30.53×** se sont encore dégradés mécaniquement vs le snapshot 10/06 (143.08× / 27.81×) suite au rally +5.4%.

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−63.59)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **77.62×** — rally mécanique, niveau extrêmement élevé
- Forward P/E **−63.59×** — profitabilité attendue éloignée
- EV/EBITDA Yahoo **157.04×** — extrême
- **Close $59.77 vs Consensus PT $69.12** — upside **+15.6%**

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].
> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, multiples extrêmes.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 2026-06-10 |
|--------|--------|-------------------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = |
| **Max Pain** | **$100.00** (exp 2026-06-18) | **ANOMALIE** — valeur fiable maintenue à **$50.00** |
| **Put/Call ratio** | **null** | **Indisponible** — dernière valeur fiable **1.92** |
| **Call OI %** | **0.0%** | **ANOMALIE** — dernière valeur fiable **34.2%** |
| **Short Interest** | **16.05%** | = — défiance accrue stable |
| **Social Sentiment** | Aucun buzz retail | = (0 mentions) |
| **Event-Driven** | Aucun événement | = |
| **News Yahoo** | Aucune | = |
| **Geo Risk** | Score 3/10, flag "low" | = |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = |

**Agent Sector Rotation (2026-06-15) :**
- Régime macro : **UNKNOWN** (VIX indisponible)
- Technology (XLK) leader : momentum score **10.0/10**, RS 20j **+3.81%** vs SPY
- IREN classé "Financial Services" par Yahoo mais thèse réelle = IA Infrastructure / BTC Mining
- Alignement macro : **NEUTRAL** — impossible d'évaluer l'alignement sans régime défini

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Verdict : Fortement corrélé — inchangé

**Interprétation institutionnelle :**
La structure options du snapshot 15/06 est **non fiable** (Max Pain $100.00, put/call null, call OI 0%). Ces valeurs sont manifestement corrompues et ne reflètent pas la réalité du marché. Les dernières valeurs fiables (snapshot 13h 10/06 : Max Pain $50.00, put/call 1.92, call OI 34.2%) suggèrent une défiance options atténuée mais persistante. Le short interest stable à **16.05%** maintient le fuel potentiel d'un squeeze, sans activation.

L'absence totale de news Yahoo et de mentions Reddit (0 posts) indique un mouvement purement technique / algorithmique, sans catalyseur fondamental visible aujourd'hui.

---

## Scoring Global (Agent Recommandation — 2026-06-15, snapshot 10h UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.3/10 | 35% | 2.21 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 7.5/10 | 25% | 1.88 |
| **Score Opportunité** | **5.7/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Le Score Global ajusté de **61.8/100** reflète le Score Opportunité × 10, sans malus/bonus additionnels majeurs documentés dans `recommandations_latest.json`.

**Action recommandée : ACHETER (Sizing Réduit)**
- Prix d'entrée suggéré : **$59.77** (close actuel)
- Stop-loss : **$47.23** (−21.0%, basé sur ATR réel $6.27)
- Take-profit : **$78.58** (+31.5%, basé sur ATR réel $6.27)
- Ratio R/R : **1.5 : 1**
- Horizon : **1–3 mois**
- Timing : **Favorable**
- Sizing : **Réduit** (beta 4.232, volatilité extrême)

> **⚠️ Avertissements :**
> 1. **Multiples extrêmes** — P/E 77.6×, EV/EBITDA 157×, Forward P/E −63.6×. Toute hausse est purement spéculative/momentum.
> 2. **Données options corrompues** — Max Pain $100.00, put/call null, call OI 0% dans `latest.json`. Dernières valeurs fiables : Max Pain $50.00, put/call 1.92, call OI 34.2% (10/06).
> 3. **Short Interest élevé stable** — 16.05% = défiance accrue du marché maintenue, fuel squeeze inactif.
> 4. **Forward P/E négatif** : −63.59× — profitabilité attendue éloignée.
> 5. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC. Seuil critique BTC ~$75k.
> 6. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (21 jours après le J0 annoncé). Prochain earnings Q2 2026 : **2026-08-27** (73 jours).
> 7. **MM200 indisponible** — tendance long terme non évaluable.
> 8. **Accounting risk** : `data/accounting_risk_latest.json` inexistant — pas de scan M-Score/Z-Score/F-Score disponible.
> 9. Si le cours casse **$52.06** (MM50) sans rebond → **passer en ATTENDRE**.
> 10. Si le cours casse **$48.75** (ancienne MM50) → **stopper toute position existante**.
> 11. Si le cours casse **$47.23** (SL 2×ATR) → **stopper la position**.
> 12. Si rebond confirme au-dessus de **$61.40** (high du 15/06) avec volume > moyenne 20j → réviser TP vers $66.60 puis $69.12.

---

## Conclusion

**Thèse : MODIFIÉE FAVORABLEMENT — UPGRADE SURVEILLER → ACHETER (Sizing Réduit).**

Le snapshot 10h UTC du 2026-06-15 apporte trois évolutions majeures par rapport au snapshot 13h du 2026-06-10 :

1. **Données techniques rétablies.** L'ATR ($6.27) et la MM50 ($52.06) sont enfin disponibles, permettant de fixer des niveaux SL/TP fiables pour la première fois depuis le gap du 2026-06-08. Le cours à $59.77 se tient à +14.8% au-dessus de la MM50, confirmant une tendance haussière intermédiaire. Le RSI s'est normalisé à 52.86 (neutre), ce qui est favorable à l'entrée.

2. **Upgrade algorithmique massif.** Le Score Global ajusté bondit de **44.3 à 61.8/100** (+17.5 pts), porté par une amélioration simultanée des trois axes de scoring. Le Momentum technique grimpe à 7.5/10 (+2.0 pts), le Catalyseur à 6.3/10 (+1.0 pt), et la Valorisation à 4.0/10 (+1.0 pt). L'action passe de **SURVEILLER** à **ACHETER (Sizing Réduit)** avec un timing déclaré **Favorable**.

3. **Anomalies options persistantes.** Le snapshot retourne des valeurs options manifestement corrompues (Max Pain $100.00, put/call null, call OI 0%). Les dernières valeurs fiables (10/06) restent la référence : défiance atténuée mais persistante.

**Différentiels clés vs snapshot 13:00 UTC 2026-06-10 :**
1. **Cours** : $59.19 (previous close 09/06) → **$59.77** (+5.4% vs previous close $56.71 du 14/06). Le close officiel du 14/06 n'est pas documenté dans l'historique immédiat ; le previous close $56.71 suggère une consolidation intermédiaire.
2. **Volume** : 56.48 M → **45.35 M** (−19.7%) — volume normalisé
3. **RSI** : 62.18 → **52.86** (−9.32 pts) — normalisation favorable
4. **ATR/MM50** : N/A → **$6.27 / $52.06** — ✅ rétablis
5. **Multiples** : P/E 70.16× → **77.62×** (+7.46 pts), EV/EBITDA 143.08× → **157.04×** (+13.96 pts) — dégradation mécanique rally
6. **Consensus PT** : $69.12 — inchangé, upside depuis close **+15.6%**
7. **Short Interest** : 16.05% → **16.05%** — stable
8. **Options** : Max Pain $50.00 / put/call 1.92 → **ANOMALIES** ($100.00 / null / 0.0%) — données corrompues
9. **Scores** : Catalyseur 5.3→**6.3**, Valorisation 3.0→**4.0**, Momentum 5.5→**7.5**. Opportunité 4.4→**5.7**, Global 44.3→**61.8**
10. **Action** : **SURVEILLER** → **ACHETER (Sizing Réduit)** — upgrade majeur
11. **Aucune news** : Le mouvement est purement technique / algorithmique

**Recommandation :**
- **ACHETER (Sizing Réduit)** — Entrée possible à $59.77 avec SL $47.23 et TP $78.58 (R/R 1.5)
- **Position existante** : Si un sizing réduit était ouvert, maintenir avec les nouveaux niveaux SL/TP
- **Attendre** : Si le cours rejette $61.40 (high du 15/06) sans volume → attendre un retour sur MM50 ($52.06)
- Premier objectif haussier : **$61.40** (high du 15/06)
- Deuxième objectif : **$66.60** (close 2026-06-02)
- Troisième objectif : **$69.12** (consensus PT)
- Si rupture sous **$52.06** (MM50) sans rebond → **passer en ATTENDRE**
- Si rupture sous **$48.75** (ancienne MM50) → **stopper toute position**
- Si rupture sous **$47.23** (SL 2×ATR) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds (21 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (73 jours). Sizing réduit obligatoire (beta 4.232, ATR 10.49%). Surveiller BTC — seuil critique $75k.

---

*Rapport rédigé le 2026-06-15 — Données sources : `data/latest.json` (fetched_at 2026-06-15T10:00:02 UTC), `data/recommandations_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`.*