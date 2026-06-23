# FUBO — Mise à jour 2026-06-23 (snapshot 10h UTC)

> **Ticker :** FUBO | **Secteur :** Communication Services / Broadcasting
> **Close :** $8.82 (0.00% vs close 22/06 21h UTC) | **Volume :** 1,139,100 (0.79× moy. 20j 1.44M)
> **Source données :** `data/latest.json` (2026-06-23 10:00:14 UTC) + `data/recommandations_latest.json`

---

## 1. Résumé des changements depuis l’analyse précédente (2026-06-22 21h UTC)

| Indicateur | 2026-06-22 21h UTC | 2026-06-23 10h UTC | Δ |
|------------|-------------------|--------------------|---|
| **Close** | $8.82 | **$8.82** | **0.00% — stabilité mécanique totale** |
| **RSI 14j** | 27.72 | **27.72** | **0.00 pt — survente maintenue** |
| **Volume vs 20j** | 0.79× (1.14M) | **0.79×** (1.14M) | **+0.2% — sous moyenne** |
| **MM50** | $10.78 | **$10.78** | **0.00%** |
| **Écart MM50** | −18.2% | **−18.2%** | **Inchangé** |
| **ATR 14j** | $0.81 | **$0.81** | **Stable** |
| **Max Pain (opérationnel)** | $9.00 | **$9.00** | **Stable** |
| **Put/Call** | 0.66 | **0.66** | **Stable** |
| **Call OI %** | 60.3% | **60.3%** | **Stable** |
| **Score Global Ajusté** | 57.8/100 | **57.8/100** | **Inchangé** |
| **Score Opportunité** | 6.1/10 | **6.1/10** | **Inchangé** |
| **Score Momentum** | 4.0/10 | **4.0/10** | **Inchangé** |

> **Anomalie options JSON récurrente détectée et traitée :** `data/latest.json` retourne max_pain **$7.50**, put/call **null**, call OI **0.0%** — valeurs aberrantes cohérentes avec le pattern JSON corrompu observé sur les 5 derniers snapshots. Les valeurs opérationnelles du close officiel 22/06 ($9.00 / 0.66 / 60.3%) sont conservées et utilisées pour l'analyse.

> **Événement matériel :** Aucun. Le snapshot 10h UTC enregistre une **stabilité mécanique totale** vs le close officiel 21h UTC du 22/06. Zero mutation des données brutes (cours, RSI, ATR, MM, volume, fondamentaux). Le scoring agent n'a pas été recalculé sur de nouvelles données — les scores du `recommandations_latest.json` restent identiques (57.8/100). Le DRAFT_refresh déclenché par `ATR_SPIKE` (9.18%) est traité : l'événement ne modifie pas la thèse car il s'agit d'un état de volatilité persistant déjà intégré dans les analyses des 5 derniers jours.

**Verdict :** Données de marché **stables**. La configuration technique (RSI 27.72, écart MM50 −18.2%, spot sous max pain) est inchangée. **Thèse ATTENDRE confirmée** — pas d'entrée en l'état.

---

## 2. Mise à jour technique

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| **Open** | $9.04 | — |
| **High** | $9.48 | Rejet matinal inchangé |
| **Low** | $8.80 | Support $8.80 testé — non rompu |
| **Close** | $8.82 | Identique au close 22/06 |
| **RSI 14j** | **27.72** | **Survente technique** (<30) — troisième jour consécutif |
| **MM50** | **$10.78** | Écart **−18.2%** — tendance baissière intacte |
| **MM200** | — | Non calculée (historique insuffisant) |
| **ATR 14j** | **$0.81** | Volatilité stable ; ATR relatif **9.19%** (> seuil 5.0%) — **ATR_SPIKE persistant** |
| **Volume 20j** | 1.44M | Moyenne stable |
| **Volume session** | **1,139,100** | **0.79×** — sous moyenne, pas de conviction institutionnelle |
| **Beta** | 2.392 | Volatilité systématique élevée |
| **52W Range** | $8.31 – $56.64 | Cours à **−84.4%** du 52W high, **+6.1%** au-dessus du 52W low |

**Supports / Résistances (ATR-based)**
- R1 (résistance immédiate) : $9.00 – $9.04 (max pain + zone de clôture)
- R2 : $9.20 – $9.22 (previous close 21/06)
- R3 : $10.00 – $10.78 (seuil psychologique + MM50)
- S1 (support immédiat) : $8.80 – $8.82 (low session + close)
- S2 : $8.31 (52W low — rupture = signal baissier majeur, gap risk)
- S3 : Aucun support technique visible sous $8.31

**Timing technique : Défavorable**
- Cours sous MM50 depuis 15+ sessions consécutives ; MM50 en descente lente
- Écart sous MM50 −18.2% — creusement structurel maintenu
- RSI 27.72 — **survente** sans divergence haussière ni rebond
- Volume 0.79× — absence de conviction institutionnelle
- ATR_SPIKE 9.19% — volatilité persistante, risque de gap down élevé
- Distance au 52W low maintenue à $0.51 (6.1%) — support historique sous pression

---

## 3. Mise à jour fondamentale

Aucune nouvelle donnée fondamentale publiée depuis le 2026-06-22 21h UTC. Les métriques restent inchangées :

| Métrique | Valeur | Contexte |
|----------|--------|----------|
| **Market Cap (Yahoo)** | $259.6M | — |
| **Market Cap (FMP)** | $3,268.5M | Divergence Yahoo/FMP persistante (×12.6) — [ANOMALIE DATA] |
| **Forward P/E** | 18.69 | Pricing d’une infime rentabilité future |
| **EV/Revenue** | 0.431 | Multiple très bas, méfiance du marché |
| **P/B** | 0.320 | Patrimoine net négatif — discount profond |
| **Debt/Equity** | 2.433 | Levier élevé ; couverture intérêts négative (−4.7×) |
| **Current Ratio** | 0.845 | Risque de liquidité |
| **Gross Margin** | 11.1% | Faible |
| **Operating Margin** | −2.6% | Non rentable à l’opérationnel |
| **FCF Yield** | −18.91% | FCF négatif |
| **ROIC** | −2.15% | Destruction de valeur à l’investissement |
| **Consensus (FMP)** | $50.25 (4 analystes) | Upside théorique +470% — spéculatif |

**Filtre Qualité : 1/6** (inchangé)
- Revenue CAGR 5 ans : ❌
- Profit CAGR 5 ans : ❌
- Assets/Liabilities : ❌ (patrimoine net négatif)
- FCF positif 5 ans : ❌
- Moat : ❌ (streaming sportif saturé)
- TAM forte croissance : ⚠️

> Règle absolue : Score Qualité ≤3/6 → Score Valorisation plafonné à 5/10. L’agent attribue 7.0/10, ce qui suggère que le plafonnement n’est pas appliqué ou que le modèle valorise le « deep value » spéculatif. Cette divergence mérite une vigilance analytique.

---

## 4. Mise à jour sentiment / options / news

### Options — Structure inchangée (pinning neutre / légèrement baissier)

| Indicateur | Valeur 23/06 10h UTC | Signal |
|------------|---------------------|--------|
| **Max Pain (opérationnel)** | $9.00 | Spot **−2.0%** au-dessus — pinning légèrement baissier |
| **Put/Call Ratio** | 0.66 | Dominance call atténuée (40% puts) |
| **Call OI %** | 60.3% | Majorité call mais marge réduite |
| **Échéance** | 2026-06-26 | J+3 — exposition gamma concentrée |

> **Anomalie data :** `data/latest.json` retourne max_pain **$7.50**, put_call_ratio **null**, call_oi_pct **0.0%** — pattern JSON corrompu identifié et traité. Valeurs opérationnelles conservées du snapshot 22/06 21h UTC.

> **Implication :** La structure options n’a pas évolué. Le spot ($8.82) reste **−2.0% sous le max pain** ($9.00). À J+3 de l’échéance, le spot sous le max pain expose à une pression vendeuse gamma si le cours ne remonte pas au-dessus de $9.00 avant vendredi.

### Sentiment
- **Short Interest** : 24.32% du float (29.2M shares) — niveau élevé, combustible latent inchangé
- **Social Sentiment** : 0 mentions Reddit, score 0/10 — aucun buzz retail
- **Analystes** : 4 analystes FMP, $50.25 price target, 0 couverture récente — consensus figé

### News / Événements
- Aucun événement corporate dans `data/events_latest.json`
- Aucune news détectée dans `data/news_2026-06-23.json` (FUBO : tableau vide)
- Prochain earnings : **2026-08-06** (44 jours, Est EPS $−0.32–$0.07, Rev $1.5B)
- Aucune upgrade/downgrade, aucun insider trade significatif

---

## 5. Scoring global actualisé

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.5/10 | 35% | 2.28 |
| **Valorisation** | 7.0/10 | 40% | 2.80 |
| **Momentum** | **4.0/10** | 25% | 1.00 |
| **Score Opportunité brut** | — | — | **6.1/10** |
| **Score Global brut** | — | — | **60.8/100** |
| **Malus / Bonus** | — | — | **−3.0 pts** |
| **Score Global Ajusté** | — | — | **57.8/100** |

**Règle de disqualification :** Aucun score ≤2/10 → pas d’exclusion automatique.

**Interprétation :**
- Le Score Global Ajusté **57.8/100** se situe dans la fourchette **ATTENDRE** (50–59).
- **Aucun changement** vs le close officiel 22/06 21h UTC : le scoring agent n'a pas recalculé de nouveaux scores sur un snapshot stable.
- **Malus sectoriel** : XLC (Communication Services) reste Bottom 3 dans `data/sector_rotation_latest.json` (momentum score 0.0, RS 20j −8.20%) → malus −0.5 pt implicite non capturé dans le scoring agent.
- **Malus timing** : sous MM50 + RSI survente + pas de confirmation technique d’entrée.
- **Malus options** : le spot sous le max pain ($8.82 < $9.00) à J+3 — exposition gamma vendeuse accrue.

---

## 6. Niveaux SL / TP / Ratio R/R

| Niveau | Valeur | Distance vs Close | Commentaire |
|--------|--------|-------------------|-------------|
| **Stop-Loss** | $7.20 | −18.4% (2× ATR = $1.62) | Issu du scoring agent — sous le 52W low ($8.31), très risqué |
| **Take-Profit** | $11.25 | +27.6% (3× ATR = $2.43) | Aligné sur résistance technique (MM50 $10.78 + marge) |
| **Ratio R/R** | **1.5×** | — | Seuil minimal institutionnel |

> **Note de risque :** Le SL $7.20 est inférieur au 52W low ($8.31) de $1.11, ce qui le rend hautement vulnérable à un gap down. Avec un cours à seulement $0.51 du 52W low, la probabilité de toucher le SL en cas de rupture de support est élevée. Le ratio R/R de 1.5× est à la limite inférieure de l’acceptabilité et ne compense pas le risque de gap.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

### Verdict : **THÈSE ATTENDRE CONFIRMÉE — STABILITÉ MÉCANIQUE TOTALE, AUCUNE MUTATION**

Le snapshot 2026-06-23 10h UTC enregistre une **stabilité mécanique totale** vs le close officiel 2026-06-22 21h UTC : cours inchangé ($8.82), RSI 27.72 (survente maintenue), volume stable (1.14M, 0.79×), écart sous MM50 −18.2% inchangé, distance au 52W low maintenue à **$0.51**. Le scoring agent n'a pas produit de nouveaux scores (pas de données nouvelles à intégrer) — les scores du `recommandations_latest.json` restent identiques : **Score Global Ajusté 57.8/100**, Momentum **4.0/10**, confirmant que la survente n’est pas interprétée comme un setup positif.

**Arguments confirmant l’ATTENDRE :**
1. **Survente technique** : RSI 27.72 — troisième jour sous 30, potentiel de rebond technique latent
2. **Valorisation attractive inchangée** : P/B 0.320, EV/Rev 0.431
3. **Short interest élevé** : 24.32% = combustible latent
4. **Structure options stable** : max pain $9.00 cohérent

**Arguments contre une entrée (inchangés) :**
1. **Aucun rebond technique** : survente persistante sans divergence ni volume
2. **Approche du 52W low** : à $0.51 ($8.31) — rupture = signal baissier majeur, gap risk
3. **RSI survente sans divergence** : 27.72 sans volume ni signal de retournement = survente qui peut durer
4. **MM50 en descente** : $10.78, écart −18.2% — tendance baissière intacte
5. **Volume sous moyenne** : 0.79× — pas de conviction institutionnelle
6. **Qualité fondamentale dégradée** : Score Qualité 1/6, FCF négatif, patrimoine net négatif
7. **Pas de catalyseur actif** : aucune news, aucun upgrade, aucun événement corporate
8. **Malus sectoriel** : XLC Bottom 3 sector rotation (momentum score 0.0)
9. **Spot sous max pain à J+3** : $8.82 < $9.00 — exposition gamma vendeuse, pinning baissier
10. **SL sous 52W low** : niveau de sortie $7.20 incompatible avec le support historique $8.31

**Conditions de réactivation d’une thèse ACHETER (inchangées) :**
- Retour au-dessus de $9.00 avec close confirmé et volume >1.0× moyenne 20j
- Retour au-dessus de MM50 ($10.78) avec close confirmé au-dessus de $10.50
- RSI remonté au-dessus de 35 avec divergence haussière
- Catalyseur fondamental (earnings beat, upgrade analyste, guidance positive)
- **Impératif** : le cours ne doit pas casser le 52W low ($8.31) — rupture = invalidation de la thèse de rebond

**Recommandation :** **ATTENDRE** — pas d’entrée en l’état. La configuration technique, fondamentale et sectorielle est **strictement inchangée** vs le close officiel du 22/06. L’anomalie options JSON récurrente (max_pain $7.50 aberrant) a été traitée et les valeurs opérationnelles ($9.00 / 0.66 / 60.3%) sont conservées. Le DRAFT_refresh déclenché par ATR_SPIKE (9.19%) est traité : ce signal de volatilité persistant est déjà intégré dans la thèse depuis 5 sessions et ne modifie pas la conclusion. Le titre reste un spéculatif fondamental dégradé (Qualité 1/6) sans catalyseur observable, sous exposition gamma vendeuse à J+3. Aucune position longue recommandée. Surveillance renforcée si rupture du 52W low.

---

*Rapport généré par le desk Argus-IA — Données sources : `data/latest.json` (2026-06-23 10:00:14 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`.*
