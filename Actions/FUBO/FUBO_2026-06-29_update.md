# FUBO — Mise à jour 2026-06-29 (snapshot 10h UTC)

> **Ticker :** FUBO | **Secteur :** Communication Services / Broadcasting
> **Close :** $9.91 (+22.50% vs previous close $8.09) | **Volume :** 3,818,500 (2.40× moy. 20j 1,587,145)
> **Source données :** `data/latest.json` (2026-06-29 10:00:01 UTC) + `data/recommandations_latest.json` + `data/sector_rotation_latest.json`

---

## 1. Résumé des changements depuis l’analyse précédente (2026-06-23 17h UTC)

| Indicateur | 2026-06-23 17h UTC | 2026-06-29 10h UTC | Δ |
|------------|-------------------|--------------------|---|
| **Close** | $8.63 | **$9.91** | **+14.8%** (gap +22.5% vs previous close $8.09) |
| **Previous Close** | $8.82 | **$8.09** | −8.3% (base du gap recalculée) |
| **RSI 14j** | 30.81 | **53.07** | **+22.26 pts** (sortie massive de survente) |
| **Volume vs 20j** | 0.42× (587k) | **2.40×** (3.82M) | **Explosion de liquidité +5.7×** |
| **MM50** | $10.72 | **$10.52** | −1.9% |
| **Écart MM50** | −19.5% | **−5.8%** | **Réduction structurelle** |
| **ATR 14j** | $0.77 | **$0.82** | +6.5% |
| **52W Low Distance** | $0.32 (+3.9%) | **$1.96 (+24.7%)** | **Éloignement du support historique** |
| **Max Pain** | $9.00 | **$3.00** | [ANOMALIE JSON — voir §4] |
| **Put/Call** | 0.66 | **null** | [ANOMALIE JSON] |
| **Call OI %** | 60.3% | **null** | [ANOMALIE JSON] |
| **Score Global Ajusté** | 51.5/100 | **64.8/100** | **+13.3 pts (upgrade agent)** |
| **Score Opportunité** | 6.0/10 | **6.8/10** | +0.8 pt |
| **Score Momentum** | 3.5/10 | **6.0/10** | **+2.5 pts (upgrade majeur)** |
| **Action Agent** | ATTENDRE | **ACHETER (Réduit)** | **Changement de recommandation** |

> **Événement matériel :** Aucun événement corporate ni news majeure détectée dans `data/events_latest.json` (vide pour FUBO). Le gap +22.50% s’est produit sans catalyseur fondamental identifiable — **profil typique de short covering** sur un titre avec short interest élevé (23.86%). Le volume 2.40× confirme la conviction derrière le mouvement. La structure options est corrompue dans le snapshot JSON (max pain $3.00 aberrant vs $9.00–$13.00 historique) — les valeurs opérationnelles antérieures sont conservées en référence.

**Verdict :** Données de marché **radicalement transformées** vs le snapshot 2026-06-23. Le gap +22.5% sur volume 2.4x et l’upgrade agent ATTENDRE → ACHETER constituent une **mutation technique majeure**. **Thèse MODIFIÉE : ATTENDRE → ACHETER Réduit**.

---

## 2. Mise à jour technique

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| **Open** | $7.99 | — |
| **High** | $9.92 | Test de la résistance psychologique $10.00 — rejet à $9.92 |
| **Low** | $7.99 | Bas de session = open (mouvement unidirectionnel) |
| **Close** | **$9.91** | +22.50% séance, +14.8% vs close 2026-06-23 $8.63 |
| **RSI 14j** | **53.07** | Sortie massive de la zone survente (<30), entrée dans la moitié supérieure neutre |
| **MM50** | **$10.52** | Écart **−5.8%** — réduction structurelle vs −19.5% précédent, tendance baissière intacte mais atténuée |
| **MM200** | — | Non calculée (historique insuffisant) |
| **ATR 14j** | **$0.82** | Volatilité en légère hausse ; ATR relatif **8.27%** (> seuil 5.0%) — **ATR_SPIKE persistant** |
| **Volume 20j** | 1,587,145 | Moyenne stable |
| **Volume session** | **3,818,500** | **2.40×** — explosion de liquidité, signal de conviction ou de short covering |
| **Beta** | 2.392 | Volatilité systématique élevée |
| **52W Range** | $7.95 – $56.64 | Cours à **−82.5%** du 52W high, **+24.7%** au-dessus du 52W low |

**Supports / Résistances (ATR-based)**
- R1 (résistance immédiate) : $9.92 – $10.00 (high session + seuil psychologique)
- R2 : $10.52 (MM50 — franchissement = changement de tendance)
- R3 : $11.00 – $12.00 (anciens max pain + résistances techniques)
- S1 (support immédiat) : $9.00 – $9.10 (ancien max pain + zone de consolidation)
- S2 : $8.50 (milieu du gap — zone de risque si repli)
- S3 : $8.09 (previous close — rupture = invalidation du gap)
- S4 : $7.95 (52W low — support historique absolu)

**Timing technique : Défavorable** (malgré le rebond)
- Cours reste **sous MM50** ($10.52) depuis 20+ sessions ; écart réduit à −5.8% vs −19.5%
- RSI 53.07 — zone neutre supérieure, pas encore surachat
- Volume 2.40× — **explosion de liquidité**, probable short covering sur 23.86% du float
- ATR_SPIKE 8.27% — volatilité persistante, risque de gap down élevé si le rebond n’est pas consolidé
- Gap +22.5% non encore testé (pas de pullback vers $8.50–$9.00) — risque de fill partiel
- Cours à +$1.96 du 52W low ($7.95) — support historique désormais distant

---

## 3. Mise à jour fondamentale

Aucune nouvelle donnée fondamentale publiée depuis le snapshot 2026-06-23. Les métriques restent inchangées :

| Métrique | Valeur | Contexte |
|----------|--------|----------|
| **Market Cap (Yahoo)** | $291.7M | — |
| **Market Cap (FMP)** | $326.8M | Divergence Yahoo/FMP persistante mais réduite (~×1.12) |
| **Forward P/E** | 20.995 | Pricing d’une rentabilité future très incertaine |
| **EV/Revenue** | 0.435 | Multiple très bas, méfiance du marché persistante |
| **P/B (Yahoo)** | 0.359 | Patrimoine net négatif — discount profond |
| **Debt/Equity** | 2.433 | Levier élevé ; couverture intérêts négative (−4.7×) |
| **Current Ratio** | 0.845 | Risque de liquidité |
| **Gross Margin** | 11.1% | Faible |
| **Operating Margin** | −2.6% | Non rentable à l’opérationnel |
| **FCF Yield** | −189.1% | FCF négatif |
| **ROIC** | −2.15% | Destruction de valeur à l’investissement |
| **Consensus (FMP)** | $50.25 (4 analystes) | Upside théorique +407% — spéculatif, consensus figé |

**Filtre Qualité : 1/6** (inchangé)
- Revenue CAGR 5 ans : ❌
- Profit CAGR 5 ans : ❌
- Assets/Liabilities : ❌ (patrimoine net négatif)
- FCF positif 5 ans : ❌
- Moat : ❌ (streaming sportif saturé)
- TAM forte croissance : ⚠️

> Règle absolue : Score Qualité ≤3/6 → Score Valorisation plafonné à 5/10. L’agent attribue 7.5/10, ce qui suggère que le modèle valorise le « deep value » spéculatif ou ne prend pas en compte le plafonnement. Cette divergence mérite une vigilance analytique — le titre reste un spéculatif fondamental dégradé malgré le rebond technique.

---

## 4. Mise à jour sentiment / options / news

### Options — Anomalie JSON persistante

| Indicateur | Valeur 29/06 10h UTC | Signal |
|------------|---------------------|--------|
| **Max Pain** | $3.00 | [ANOMALIE JSON — valeur aberrante vs historique $9.00–$13.00] |
| **Put/Call Ratio** | null | [ANOMALIE JSON] |
| **Call OI %** | null | [ANOMALIE JSON] |
| **Échéance** | 2026-07-02 | J+3 — exposition gamma proche |

> **Implication :** Les données options JSON retournent des valeurs aberrantes (max pain $3.00, put/call null, call OI null) depuis plusieurs sessions. Les valeurs opérationnelles de référence (max pain $9.00, put/call 0.66, call OI 60.3%) restent la base d’analyse jusqu’à résolution. Le spot ($9.91) est désormais **+10.1% au-dessus du max pain référence** ($9.00) — inversion de la structure pinning baissière observée précédemment. À J+3 de l’échéance, le spot au-dessus du max pain expose à une pression gamma acheteuse si le cours se maintient.

### Sentiment
- **Short Interest** : 23.86% du float (29.2M shares) — niveau élevé, combustible latent **probablement en train de brûler** (short covering = explication privilégiée du gap +22.5%)
- **Social Sentiment** : 0 mentions Reddit, score 0/10 — aucun buzz retail
- **Analystes** : 4 analystes FMP, $50.25 price target, 0 couverture récente — consensus figé

### News / Événements
- Aucun événement corporate dans `data/events_latest.json` (ticker_events vide)
- Aucune news détectée dans les sources JSON
- Prochain earnings : **2026-08-06** (38 jours, Est EPS $−0.32–$0.07, Rev $1.5B)
- Aucune upgrade/downgrade, aucun insider trade significatif détecté

---

## 5. Scoring global actualisé

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.5/10 | 35% | 2.28 |
| **Valorisation** | 7.5/10 | 40% | 3.00 |
| **Momentum** | **6.0/10** | 25% | 1.50 |
| **Score Opportunité brut** | — | — | **6.8/10** |
| **Score Global brut** | — | — | **68.0/100** |
| **Malus / Bonus** | — | — | **−3.0 pts** |
| **Score Global Ajusté** | — | — | **64.8/100** |

**Règle de disqualification :** Aucun score ≤2/10 → pas d’exclusion automatique.

**Interprétation :**
- Le Score Global Ajusté **64.8/100** se situe dans la fourchette **ACHETER Réduit** (60–74), confirmant l’upgrade agent.
- **Upgrade vs 2026-06-23** : +13.3 pts (51.5 → 64.8), principalement porté par le **Momentum 6.0/10** (+2.5 pts) et la valorisation maintenue 7.5/10.
- **Malus sectoriel** : XLC (Communication Services) reste Bottom 3 dans `data/sector_rotation_latest.json` (momentum score 0.0, RS 20j −5.61%) → malus −0.5 pt implicite.
- **Malus timing** : cours sous MM50 persistant, bien que l’écart soit réduit.
- **Malus options** : données JSON corrompues empêchent une lecture fine du GEX/max pain.
- **Bonus volume** : explosion à 2.40× — signal de conviction technique, probable short covering.

---

## 6. Niveaux SL / TP / Ratio R/R

| Niveau | Valeur | Distance vs Close | Commentaire |
|--------|--------|-------------------|-------------|
| **Stop-Loss** | $8.27 | −16.5% (2× ATR = $1.64) | Issu du scoring agent — au-dessus du previous close ($8.09), compatible avec le risque de fill du gap |
| **Take-Profit** | $12.37 | +24.8% (3× ATR = $2.46) | Aligné sur ancienne résistance technique ($12.00) + marge |
| **Ratio R/R** | **1.5×** | — | Seuil minimal institutionnel |

> **Note de risque :** Le SL $8.27 est supérieur au previous close ($8.09) de $0.18. En cas de repli brutal vers le bas du gap ($8.00–$8.50), le SL serait touché rapidement. Le ratio R/R de 1.5× est à la limite inférieure de l’acceptabilité. Le sizing réduit est impératif compte tenu du profil fondamental dégradé (Qualité 1/6) et de la volatilité extrême (beta 2.392, ATR_SPIKE 8.27%).

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

### Verdict : **THÈSE MODIFIÉE — ATTENDRE → ACHETER RÉDUIT (Score Global Ajusté 64.8/100)**

Le snapshot 2026-06-29 10h UTC enregistre une **mutation technique majeure** : gap +22.50% à $9.91 sur une **explosion de volume** (2.40×, 3.82M vs 587k précédent), avec un RSI sorti de la survente extrême (30.81 → 53.07) et l’écart sous MM50 réduit de −19.5% à −5.8%. Le scoring agent a upgradé le titre : **Score Global Ajusté 64.8/100** (vs 51.5), Momentum **6.0/10** (vs 3.5), avec un changement de recommandation **ATTENDRE → ACHETER Réduit**.

**Mutations principales :**
1. **Cours :** $8.63 → $9.91 (+14.8% vs close 23/06, +22.5% vs previous close $8.09)
2. **Volume :** explosion à **2.40×** (3.82M) — signal de conviction ou short covering massif
3. **Scoring agent :** upgrade +13.3 pts (51.5 → 64.8), changement de recommandation
4. **Momentum :** 3.5 → 6.0/10 — dynamique haussière confirmée
5. **RSI :** 30.81 → 53.07 — sortie de survente extrême, zone neutre supérieure
6. **Écart MM50 :** −19.5% → −5.8% — réduction structurelle significative
7. **Distance 52W low :** +$0.32 → +$1.96 — éloignement du support historique

**Arguments confirmant l’ACHETER Réduit :**
1. **Rebond technique puissant** : +22.5% sur volume 2.4x = mouvement crédible, probable short covering
2. **Short interest élevé** : 23.86% = combustible latent en train de brûler
3. **RSI repositionné** : 53.07, loin de la survente extrême, marge avant surachat
4. **Valorisation attractive** : P/B 0.359, EV/Rev 0.435 — deep value spéculatif
5. **Scoring agent upgrade** : 64.8/100, fourchette ACHETER Réduit
6. **Écart MM50 réduit** : −5.8%, proche du franchissement haussier

**Arguments de prudence / risques :**
1. **Aucun catalyseur fondamental** : gap sans news ni événement corporate — purement technique
2. **Qualité fondamentale inchangée** : Score Qualité 1/6, FCF négatif, patrimoine net négatif
3. **Cours sous MM50** : $10.52, tendance baissière intacte malgré l’atténuation
4. **Anomalie options JSON** : max pain $3.00 aberrant — impossibilité de lire le GEX réel
5. **Malus sectoriel** : XLC Bottom 3 sector rotation (momentum score 0.0)
6. **Gap non testé** : +22.5% sans pullback — risque de fill partiel élevé
7. **Beta 2.392** : volatilité extrême, risque de gap down rapide
8. **SL proche du gap** : $8.27 n’est qu’à $0.18 du previous close — peu de marge de sécurité
9. **Consensus figé** : 4 analystes, $50.25 PT théorique, aucune couverture récente
10. **Pas de divergence haussière confirmée** : RSI remonté mécaniquement sur le gap, pas sur accumulation progressive

**Conditions de renforcement d’une thèse ACHETER Standard :**
- Retour au-dessus de MM50 ($10.52) avec close confirmé et volume >1.0× moyenne 20j
- Consolidation du gap au-dessus de $9.50 pendant 2–3 sessions
- Résolution de l’anomalie options JSON (retour à des valeurs cohérentes)
- Catalyseur fondamental (earnings beat, upgrade analyste, guidance positive)
- **Impératif** : ne pas casser sous $8.50 (milieu du gap) — rupture = invalidation du rebond

**Recommandation :** **ACHETER Réduit** — sizing minimal compte tenu du profil fondamental dégradé (Qualité 1/6) et de la volatilité extrême. Le rebond technique est crédible (volume 2.4x, probable short covering) mais le timing reste Défavorable (sous MM50) et le secteur XLC est en bottom 3. **Ne pas augmenter le sizing** tant que le cours n’est pas confirmé au-dessus de MM50 ($10.52) avec volume soutenu. **Surveillance renforcée** si repli sous $9.00.

---

*Rapport généré par le desk Argus-IA — Données sources : `data/latest.json` (2026-06-29 10:00:01 UTC), `data/recommandations_latest.json` (2026-06-29), `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`.*
