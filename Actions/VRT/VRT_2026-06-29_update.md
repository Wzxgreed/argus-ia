# VRT — Mise à jour Snapshot Post-Séance (29/06/2026)

> **Date :** 2026-06-29
> **Cours de référence :** $303.95 (dernier close connu, 28/06/2026)
> **Fichier précédent :** [VRT_2026-06-23_update.md](./VRT_2026-06-23_update.md) (snapshot 17:00 UTC — close **$325.255**)
> **Statut thèse :** INVALIDÉE — cassure MM50, gap down −6.64% non comblé, downgrade moteur ÉVITER

---

## 1. Résumé des changements depuis l'analyse précédente (23/06 17:00 UTC)

| Métrique | 2026-06-23 17:00 UTC | Dernier connu (28/06) | Δ |
|----------|----------------------|----------------------|---|
| Cours close | **$325.255** | **$303.95** [STALE] | **−6.54%** (−$21.30) |
| RSI 14j | 47.56 | **50.9** [STALE] | +3.34 pts |
| ATR 14j | $22.13 | **$21.71** [STALE] | −$0.42 |
| MM 50j | $323.49 | **$324.04** [STALE] | +$0.55 |
| Écart vs MM50 | +0.54% | **−6.20%** | 🔴 **Cassure confirmée** |
| Volume vs 20j | 0.97× (5.95M) | **3.0× (21.97M)** [STALE] | **Explosion** |
| Change % séance | −9.14% | **−6.64%** [STALE, 26/06] | Gap down cumulé |
| P/E TTM | 81.93 | **76.37** [STALE] | −5.56 pts (mécanique) |
| Forward P/E | 36.75 | **34.35** [STALE] | −2.40 pts (mécanique) |
| Put/Call ratio | 2.38 | **1.74** [STALE] | −0.64 (atténuation bearish) |
| Call OI % | 29.5% | — [STALE] | — |
| Max pain | $245.0 | **$235.0** [STALE] | −$10.0 |
| Consensus PT (FMP) | $267.57 | **$267.57** | Stable — écart +13.6% |
| Sector rotation XLI | #2 / momentum 7.13 | **Données manquantes** | [BLACKOUT] |
| FX exposure | 45% EUR/CNY, Score 0.0 | **45% EUR/CNY, Score 0.0** (28/06) | Stable |
| Social sentiment | 0 mentions | **0 mentions** (29/06) | Stable |
| Events corporate | 0 | **0** (29/06) | Stable |
| Prochain earnings | 2026-07-29 (36 jours) | **2026-07-29 (30 jours)** | J−30 |
| Score Global Ajusté | 45.0/100 (SURVEILLER) | **20.8/100 (ÉVITER)** [28/06] | **−24.2 pts** |
| Recommandation moteur | SURVEILLER | **ÉVITER** | **Downgrade** |

**Faits marquants :**
- **Data blackout / stale price** : `data/latest.json` ne contient pas de snapshot frais pour VRT le 29/06. Le `quality_gate_2026-06-29.json` signale un `stale_price_history` (close identique sur 3 jours consécutifs). Le dernier close réellement observé est **$303.95** (26–28/06).
- **Gap down −6.64% (26/06)** : après le gap down −9.14% du 23/06, le cours a continué de glisser vers $303.95, creusant la perte totale à **−15.1%** depuis le high du 22/06 ($357.96).
- **Cassure MM50 confirmée** : le cours à $303.95 est **−6.20% sous la MM50** ($324.04). La rupture baissière est désormais structurelle, non conjoncturelle.
- **Volume explosion 3.0×** (21.97M vs moy. 7.21M) sur le gap down du 26/06 — distribution institutionnelle massivement confirmée, contrairement au profit-taking mécanique du 23/06 (0.97×).
- **Score Global Ajusté effondré** : de 45.0/100 (SURVEILLER, 23/06) à **20.8/100 (ÉVITER, 28/06)** — le plus bas depuis le début du suivi. Le moteur a progressivement dégradé le score : 29.5/100 (24/06) → 48.3/100 (25/06, rebond technique) → 27.0/100 (26/06) → 20.8/100 (28/06).
- **Options moins bearish** : put/call passé de 2.38 à 1.74, max pain de $245 à $235. L'atténuation du sentiment bearish n'est pas suffisante pour compenser la rupture technique.
- **Aucune news structurante** : pas d'événement corporate, pas de guidance, pas de contrat. Le mouvement est purement technique/driven par la liquidation.
- **[DONNÉES MANQUANTES]** : `data/sector_rotation_latest.json` corrompu/NaN pour VRT ; `data/accounting_risk_latest.json` absent ; `data/quant_report_latest.json` obsolète (2026-05-17).

---

## 2. Mise à jour technique

| Indicateur | Valeur | Signal |
|-------------|--------|--------|
| Cours | $303.95 [STALE] | — |
| RSI 14j | 50.9 [STALE] | Neutre, légère remontée depuis 47.56 |
| ATR 14j | $21.71 [STALE] | Élevé (7.14% du cours) — volatilité persistante |
| MM 50j | $324.04 [STALE] | **Cassée — cours −6.20% en-dessous** |
| MM 200j | N/A | — |
| Golden Cross | N/A | — |
| Volume 20j moy. | 7,214,525 | — |
| Volume séance | 21,974,500 [STALE, 26/06] | **3.0× — distribution confirmée** |
| 52-week high | $379.935 | Cours −20.0% du sommet |
| 52-week low | $110.06 | Cours +176.3% du plancher |

**Niveaux clés (révisés) :**
- **Support 1** : $300.00 (zone psychologique — testée le 08/06 à $300.57)
- **Support 2** : $294.40 (low du 08/06)
- **Support 3** : $280.09 (low du 09/06)
- **Résistance 1** : $315.00 (ancien support devenu résistance)
- **Résistance 2** : $323.49 / $324.04 (MM50 — désormais résistance majeure)
- **Résistance 3** : $338.00 (ancien support)

**Verdict timing :** Défavorable — la cassure de la MM50 sur volume 3.0× est un signal baissier structurel. Le rally +19.5% du 17–22/06 est entièrement effacé. Aucun catalyseur technique ne justifie un retournement à court terme.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $116.7B | Yahoo Finance [STALE] |
| P/E (TTM) | 76.37 | Yahoo Finance [STALE] |
| Forward P/E | 34.35 | Yahoo Finance [STALE] |
| EV/EBITDA (FMP) | 29.73 | FMP Stable API |
| Beta | 2.037 | Yahoo Finance |
| Short Interest | 3.73% | Yahoo Finance |
| FMP ROIC | 18.55% | FMP Stable API |
| FMP ROCE | 24.30% | FMP Stable API |
| FMP Net Debt/EBITDA | 0.78× | FMP Stable API |
| FMP Interest Coverage | 22.03× | FMP Stable API |
| FMP Current Ratio | 1.55× | FMP Stable API |

**Filtre Qualité (6 critères) :**
| Critère | Évaluation | Commentaire |
|---------|-----------|-------------|
| Revenue CAGR 5 ans ≥ 20% | ✅ Oui | Croissance data centers + IA |
| Profit CAGR 5 ans ≥ 20% | ✅ Oui | Marges en expansion |
| Assets/Liabilities > 1.0 | ✅ Oui | Current ratio 1.55× |
| FCF positif et croissant 5 ans | ✅ Oui | FCF yield 3.06% |
| Avantage compétitif (moat) | ✅ Oui | Leader refroidissement DC, parts dominantes |
| Industrie en forte croissance (TAM ×5) | ✅ Oui | TAM refroidissement IA en explosion |
| **Score Qualité total** | **6/6** | **Quality Compounder** |

**Observations :**
- Les fondamentaux restent **strictement inchangés** et solides (Quality Compounder 6/6).
- Les multiples se sont **mécaniquement améliorés** (P/E 76.4 vs 81.9, Forward P/E 34.3 vs 36.7) mais restent **extrêmement élevés** pour un industriel, surtout en contexte de rupture technique.
- Le consensus PT $267.57 est désormais seulement **+13.6% sous le cours** (vs +21.8% à $325.255). La divergence analystes/cours se réduit, ce qui diminue l'upside contrarien.
- **Règle absolue :** malgré la qualité fondamentale, le score Valorisation reste plafonné par l'extrême multiple (Forward P/E 34.3 >> secteur).

---

## 4. Mise à jour sentiment / options / news

| Signal | Valeur | Commentaire |
|--------|--------|-------------|
| Consensus PT (FMP) | $267.57 (47 analysts) | +13.6% sous cours — divergence réduite |
| Put/Call ratio | 1.74 [STALE] | Bearish atténué vs 2.38 (23/06) |
| Max pain | $235.0 [STALE] | Sous cours de 22.7% |
| Social sentiment | 0 mentions (29/06) | Aucune mention Reddit |
| Pump detection | Non | — |
| FX exposure | 45% EUR/CNY | Score FX Impact 0.0 (🟢) — stable |
| Events corporate | 0 événement (29/06) | Aucun catalyseur externe |
| News | Aucune (29/06) | Data blackout news confirmé |

**Observations :**
- Le sentiment options s'est **légèrement amélioré** (put/call 1.74 vs 2.38), mais reste bearish. Cette amélioration est insuffisante face à la rupture technique.
- Aucune news, aucun insider trade, aucun événement corporate détecté sur la période 24–29/06.
- Le data blackout complet (prix, news, sector rotation) empêche toute analyse de sentiment frais.

---

## 5. Scoring global révisé

**Données du moteur recommandations (dernier connu : 28/06/2026) :**

| Score | Valeur | Δ vs 23/06 |
|-------|--------|------------|
| Score Opportunité | 3.4/10 | −1.0 pt |
| Score Catalyseur | 4.3/10 | Stable |
| Score Valorisation | 2.5/10 | Stable |
| Score Momentum | 3.5/10 | **−2.5 pts** |
| Score Global | 33.8/100 | −11.2 pts |
| Score Global Ajusté | **20.8/100** | **−24.2 pts** |
| Recommandation moteur | **ÉVITER** | **Downgrade SURVEILLER → ÉVITER** |

**Révision desk Argus-IA :**

Le gap down du 26/06 (−6.64%) et la cassure de la MM50 sur volume 3.0× constituent un signal technique structurellement baissier. Les conditions définies le 23/06 pour un upgrade ont été **toutes invalidées** :

| Condition | Seuil | Statut 29/06 | Verdict |
|-----------|-------|---------------|---------|
| Cours > MM50 | > $324.04 | **$303.95 (−6.20%)** | 🔴 **ROMPUE** |
| Cours > $338 + volume >1.0× | > $338 | **$303.95 / 3.0×** | 🔴 ROMPUE (prix) |
| Catalyseur externe | Contrat/guidance/M&A | Aucun | 🔴 Non remplie |
| Forward P/E < 35 | < 35 | 34.35 | ✅ Remplie (mécanique) |
| Put/call < 2.0 | < 2.0 | 1.74 | ✅ Atteint |

**Verdict desk :** La rupture de la MM50 sur volume massif est le signal dominant. Le score Global Ajusté à 20.8/100 est le plus bas historique du dossier. La thèse est **downgradée de SURVEILLER à ÉVITER**. Le fondamental reste intact (Quality Compounder 6/6) mais la configuration technique est désormais structurellement baissière. Aucune position longue n'est justifiable avant un retour confirmé au-dessus de la MM50 avec volume >1.0×.

| Score révisé desk | Valeur |
|-------------------|--------|
| Score Opportunité | 3.4/10 (downgrade — rupture MM50 + gap down cumulé) |
| Score Catalyseur | 4.3/10 (stable — pas de catalyseur) |
| Score Valorisation | 2.5/10 (stable — amélioration mécanique insuffisante) |
| Score Momentum | 3.5/10 (−2.5 pts — cassure MM50, tendance baissière) |
| **Score Global Ajusté desk** | **20.8/100** |
| **Recommandation desk** | **ÉVITER** (downgrade depuis SURVEILLER) |

---

## 6. Révision des niveaux SL / TP

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix actuel | $303.95 | — [STALE] |
| Stop-loss (engine) | $260.53 | Cours − 2× ATR ($303.95 − $43.42) |
| Stop-loss (desk suggéré) | $290.00 | Sous le low du 09/06 ($280.09) + marge, avant support $294.40 |
| Take-profit (engine) | $369.08 | Cours + 3× ATR ($303.95 + $65.13) |
| Ratio R/R (engine) | 1.50 | Engine standard |

**Notes :**
- Le SL engine $260.53 correspond au support technique $280–$285 + marge ATR étendue. C'est large mais cohérent avec un beta 2.037.
- Le desk suggère un **SL intermédiaire à $290.00** (sous le support $294.40 du 08/06) pour limiter l'exposition si la rupture s'accélère.
- Le TP $369.08 est cohérent avec la zone de résistance long terme, mais nécessiterait un catalyseur majeur (earnings 29/07) pour être atteint.
- **Pas de position recommandée.** Les niveaux SL/TP ne sont fournis qu'à titre de référence pour les positions existantes.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE INVALIDÉE — rupture MM50 sur volume 3.0×, gap down cumulé −15.1% depuis le 22/06, downgrade ÉVITER (20.8/100)**

La thèse de fond reste intacte : VRT est un **Quality Compounder 6/6** bénéficiant du boom IA infrastructure. Cependant, la configuration technique s'est structurellement dégradée entre le 23/06 et le 26/06, invalidant la thèse de court/moyen terme.

**Ce qui a changé depuis le snapshot 23/06 17:00 UTC :**
1. **Cours** : $325.255 → **$303.95** [STALE] (−6.54% additionnel, −15.1% cumulé depuis le 22/06)
2. **MM50** : support à +0.54% → **cassure à −6.20%** — signal structurel baissier
3. **Volume** : 0.97× (profit-taking) → **3.0× (distribution massive)**
4. **Score Global Ajusté** : 45.0/100 (SURVEILLER) → **20.8/100 (ÉVITER)** — plus bas historique
5. **Recommandation moteur** : SURVEILLER → **ÉVITER**
6. **Momentum** : 6.0/10 → **3.5/10** — tendance baissière confirmée
7. **Options** : put/call 2.38 → **1.74** — bearish atténué mais insuffisant
8. **Max pain** : $245 → **$235**

**Ce qui n'a pas changé :**
1. Fondamentaux (marges, ROIC, dette, quality 6/6) — inchangés
2. FX exposure — Score 0.0 (🟢)
3. Social sentiment — 0 mentions
4. Events corporate — 0 événement
5. Forward earnings — 2026-07-29 (30 jours)

**Data blackout du 29/06 :**
- `data/latest.json` ne contient pas de snapshot frais pour VRT.
- `quality_gate_2026-06-29.json` signale `stale_price_history` (close identique sur 3 jours).
- Aucune news, aucun social sentiment, aucun événement corporate détecté.
- Le dossier est en **data blackout** — toute décision doit intégrer cette incertitude.

**Scénarios forward (révisés) :**

| Scénario | Déclencheur | Probabilité | Impact cours |
|----------|-------------|-------------|--------------|
| **Optimiste** | Rebond au-dessus de MM50 ($324) avec volume >1.2× + catalyseur externe | 10% | +8–12% vers $340–$350 |
| **Central** | Consolidation $295–$315 en attendant earnings 29/07 | 45% | ±5% |
| **Pessimiste** | Perte de $300 avec volume >1.0× | 45% | −8–12% vers $280–$290 |

**Conditions de maintenance du grade ÉVITER :**
- Cours sous MM50 ($324.04)
- Aucun catalyseur externe
- Pas de clôture au-dessus de $315 avec volume >1.0×

**Conditions d'upgrade vers SURVEILLER :**
- Clôture > MM50 ($324.04) avec volume >1.2×
- Catalyseur externe confirmé (contrat, guidance raise, M&A)
- Put/call < 1.50 en confirmation

**Prochain événement :** Earnings Q2 FY2026 le **2026-07-29** (30 jours) — Est EPS $1.38–$1.59, Rev $3.4B. Ce sera le seul catalyseur susceptible d'inverser la tendance technique.

---

*Rapport généré par le desk Argus-IA — données source : `data/recommandations_2026-06-28.json` (dernier score connu), `data/quality_gate_2026-06-29.json` (stale_price_history), `data/geo_risk_2026-06-29.json` (Score 2, 🟢), `data/social_sentiment_2026-06-29.json` (0 mentions), `data/news_2026-06-29.json` (aucune news), `data/fx_exposure_2026-06-29.json` (Score 0.0). **[DONNÉES MANQUANTES]** : `data/latest.json` (pas de snapshot VRT), `data/accounting_risk_latest.json` absent, `data/quant_report_latest.json` obsolète (2026-05-17), `data/sector_rotation_latest.json` corrompu/NaN.*
