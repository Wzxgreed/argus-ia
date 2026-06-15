# IREN — Mise à Jour (2026-06-15, snapshot 13:00 UTC)

> **Type :** `_update.md` — Révision post-pipeline (correction données options)
> **Référence précédente :** [IREN_2026-06-15_update.md](IREN_2026-06-15_update.md) (snapshot 10h UTC 15/06)
> **Données source :** `data/latest.json` (fetched_at 2026-06-15T13:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`
> **Trigger :** PIPELINE_CORRECTION — données options rétablies post-anomalie snapshot 10h

---

## Résumé des Changements (vs Snapshot 10h UTC 2026-06-15)

| Métrique | 10h UTC | 13h UTC | Δ |
|----------|---------|---------|---|
| **Cours close** | **$59.77** | **$59.77** | = |
| **Previous close** | $56.71 | **$56.71** | = |
| **Change % session** | **+5.40%** | **+5.40%** | = |
| **Volume** | 45.35 M | **45.35 M** | = |
| **Volume vs 20j** | 91.0% | **91.0%** | = |
| **RSI 14j** | 52.86 | **52.86** | = |
| **ATR 14j** | $6.27 | **$6.27** | = |
| **MM 50j** | $52.06 | **$52.06** | = |
| **MM 200j** | N/A | **N/A** | = — [DONNÉES MANQUANTES] |
| **Short Interest** | 16.05% | **16.05%** | = |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | **$69.12 (26 analysts)** | = |
| **P/E TTM** | 77.62× | **77.62×** | = |
| **Forward P/E** | −63.59× | **−63.59×** | = |
| **EV/EBITDA** | 157.04× | **157.04×** | = |
| **EV/Revenue** | 30.53× | **30.53×** | = |
| **P/B** | 7.65× | **7.65×** | = |
| **Max Pain** | $100.00 (anomalie) | **$40.00** | **✅ CORRECTION** — valeur fiable rétablie |
| **Put/Call ratio** | null (anomalie) | **1.62** | **✅ CORRECTION** — valeur fiable rétablie |
| **Call OI %** | 0.0% (anomalie) | **38.1%** | **✅ CORRECTION** — valeur fiable rétablie |
| **Score Opportunité** | 5.7/10 | **5.7/10** | = |
| **Score Catalyseur** | 6.3/10 | **6.3/10** | = |
| **Score Valorisation** | 4.0/10 | **4.0/10** | = |
| **Score Momentum** | 7.5/10 | **7.5/10** | = |
| **Score Global ajusté** | 61.8/100 | **61.8/100** | = |
| **Action recommandée** | **ACHETER (Sizing Réduit)** | **ACHETER (Sizing Réduit)** | = |

**Mutation principale : Correction majeure des données options.** Le pipeline 13h UTC rétablit des valeurs options cohérentes après l'anomalie du snapshot 10h (Max Pain $100.00, put/call null, call OI 0.0%). Le Max Pain passe à **$40.00** (expiration 2026-06-18), le put/call à **1.62**, et le call OI à **38.1%**. Ces valeurs sont plausibles au regard de l'historique récent ($33.00–$52.00) et retirent l'incertitude technique du matin.

**Impact sur la thèse : Prudence accrue à court terme.** Le Max Pain à $40.00 est nettement inférieur au cours actuel ($59.77), écart de **+49.4%**. Cet écart élargi réduit le risque de pin vers le Max Pain à l'expiration du 18/06 (3 jours), mais indique que le marché options n'anticipe pas de retour sous $40 à très court terme. Le put/call **1.62** confirme une défiance atténuée mais persistante (vs 3.95 record 08/06, 1.92 10/06).

**Constat :** Les données brutes (cours, RSI, ATR, MM, volumes, multiples, scores agents) sont **strictement inchangées** vs snapshot 10h. Le scoring global reste **61.8/100**, action **ACHETER (Sizing Réduit)**. L'évolution est purement structurelle options.

---

## Mise à Jour Technique

Données techniques inchangées vs snapshot 10h UTC.

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 52.86 | Zone neutre, favorable à l'entrée. Inchangé |
| **ATR 14j** | $6.27 | Volatilité journalière moyenne 10.49% du cours. Inchangé |
| **MM 50j** | $52.06 | Cours à +14.8% au-dessus, tendance haussière intermédiaire confirmée |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 49.85 M | Volume session 45.35 M = **91.0%** moyenne — volume normal, pas de distribution |
| **52-week high/low** | $76.87 / $9.52 | Close à **77.7%** du 52W high |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |
| **Open / High / Low** | $56.505 / $61.40 / $55.94 | Range intraday 9.6% — volatilité élevée mais contrôlée |

**Niveaux clés (identiques au snapshot 10h) :**
- Support immédiat : **$55.94** (low du 2026-06-15)
- Support secondaire : **$56.71** (previous close du 14/06)
- Support critique : **$52.06** (MM50) — cassure = révision en ATTENDRE
- Support structurel : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support majeur : **$47.23** (stop-loss ATR 2× = $59.77 − $12.54)
- Résistance immédiate : **$61.40** (high du 2026-06-15)
- Résistance : **$66.60** (close 2026-06-02, ancien sommet)
- Résistance majeure : **$69.12** (consensus PT FMP)
- Résistance extrême : **$76.87** (52-week high)
- Stop-loss (2×ATR) : **$47.23** (−21.0% vs close)
- Take-profit (3×ATR) : **$78.58** (+31.5% vs close)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable.** Inchangé vs snapshot 10h. Le RSI à 52.86 reste en zone neutre favorable. Le cours se tient nettement au-dessus de la MM50 ($52.06), confirmant la tendance haussière intermédiaire. Le volume est normal (91% moyenne).

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

> **Note :** Les écarts Yahoo vs FMP demeurent extrêmes. Multiples mécaniquement dégradés par le rally +5.4% sans amélioration fondamentale mesurable.

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−63.59)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **77.62×** — niveau extrêmement élevé
- Forward P/E **−63.59×** — profitabilité attendue éloignée
- EV/EBITDA Yahoo **157.04×** — extrême
- **Close $59.77 vs Consensus PT $69.12** — upside **+15.6%**

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].
> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, multiples extrêmes.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur 13h UTC | Évolution vs 10h UTC | Évolution vs 10/06 |
|--------|---------------|----------------------|------------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = | = |
| **Max Pain** | **$40.00** (exp 2026-06-18) | **✅ CORRECTION** (vs $100.00 anomalie) | **↓ $10.00** (vs $50.00) |
| **Put/Call ratio** | **1.62** | **✅ CORRECTION** (vs null) | ↓ −0.30 (vs 1.92) — détente |
| **Call OI %** | **38.1%** | **✅ CORRECTION** (vs 0.0%) | ↑ +3.9 pts (vs 34.2%) |
| **Short Interest** | **16.05%** | = | = — défiance accrue stable |
| **Social Sentiment** | Aucun buzz retail | = | = (0 mentions) |
| **Event-Driven** | Aucun événement | = | = |
| **News Yahoo** | Aucune | = | = |
| **Geo Risk** | Score 3/10, flag "low" | = | = |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = | = |

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
La correction des données options retire l'incertitude technique du matin. Le pipeline 13h UTC confirme des valeurs plausibles et cohérentes avec l'historique récent. Cependant, le **Max Pain à $40.00** est un niveau significativement plus bas que les **$50.00–$52.00** observés début juin. Cette baisse peut refléter : (i) un rebalancing du open interest vers les strikes bas après le gap baissier du 08/06, (ii) une anticipation de volatilité post-expiration, ou (iii) une couverture accrue des positions short.

Le put/call à **1.62** reste élevé (défiance persistante), mais est en **nette détente** vs le record **3.95** du 08/06 et le **1.92** du 10/06. Le call OI à **38.1%** indique un intérêt call stable, en légère hausse vs le 34.2% du 10/06. La structure options ne suggère plus la panique observée début juin.

**Risk spécifique expiration 18/06 :** Avec le cours à $59.77 et le Max Pain à $40.00, l'écart de +49.4% est trop large pour un pin risk classique vers le Max Pain. Toutefois, si le cours rejette **$61.40** sans volume d'ici vendredi, une compression volatilité vers les strikes denses historiques ($50.00–$52.00) reste possible.

L'absence totale de news Yahoo et de mentions Reddit (0 posts) confirme un mouvement purement technique / algorithmique, sans catalyseur fondamental visible aujourd'hui.

---

## Scoring Global (Agent Recommandation — 2026-06-15, snapshot 13h UTC)

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
> 2. **Max Pain $40.00** — écart de +49.4% au-dessus du cours. Risque de volatilité anormale vers l'expiration 18/06 (3 jours). Niveau historiquement bas vs début juin.
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

**Thèse : CONFIRMÉE avec prudence accrue sur l'expiration options.**

Le snapshot 13h UTC confirme l'intégralité des données brutes du snapshot 10h (cours $59.77, RSI 52.86, ATR $6.27, MM50 $52.06, scores 5.7/61.8). La seule évolution majeure est la **correction structurelle des données options** : le pipeline a rétabli des valeurs fiables (Max Pain **$40.00**, put/call **1.62**, call OI **38.1%**). Ces valeurs retirent l'avertissement de données corrompues mais introduisent un niveau de Max Pain plus bas que prévu (baisse de $50.00 à $40.00 en 5 jours).

**Différentiels clés vs snapshot 10h UTC :**
1. **Cours / Technique** : strictement inchangés
2. **Options** : ANOMALIES ($100.00 / null / 0.0%) → **CORRECTION** ($40.00 / 1.62 / 38.1%)
3. **Put/call** : valeur fiable rétablie à 1.62 — détente vs 1.92 (10/06) et 3.95 (08/06)
4. **Call OI** : 38.1% — intérêt call stable, légère hausse vs 34.2% (10/06)
5. **Max Pain** : $40.00 — baisse de $10.00 vs 10/06. Niveau à surveiller pour l'expiration 18/06
6. **Scores / Action** : inchangés — **ACHETER (Sizing Réduit)**

**Recommandation :**
- Maintenir **ACHETER (Sizing Réduit)** — Entrée possible à $59.77 avec SL $47.23 et TP $78.58 (R/R 1.5)
- **Position existante** : Si un sizing réduit était ouvert, maintenir avec les niveaux SL/TP inchangés
- **Attention expiration 18/06** : le Max Pain à $40.00 est un niveau bas. Si le cours rejette $61.40 sans volume d'ici vendredi, surveiller une compression vers $50.00–$52.00
- Premier objectif haussier : **$61.40** (high du 15/06)
- Deuxième objectif : **$66.60** (close 2026-06-02)
- Troisième objectif : **$69.12** (consensus PT)
- Si rupture sous **$52.06** (MM50) sans rebond → **passer en ATTENDRE**
- Si rupture sous **$48.75** (ancienne MM50) → **stopper toute position**
- Si rupture sous **$47.23** (SL 2×ATR) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds (21 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (73 jours). Sizing réduit obligatoire (beta 4.232, ATR 10.49%). Surveiller BTC — seuil critique $75k.

---

*Rapport rédigé le 2026-06-15 — Données sources : `data/latest.json` (fetched_at 2026-06-15T13:00:01 UTC), `data/recommandations_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`.*
