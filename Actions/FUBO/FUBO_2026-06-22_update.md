# FUBO — Mise à jour 2026-06-22 (snapshot 13h UTC)

> **Ticker :** FUBO | **Secteur :** Communication Services / Broadcasting
> **Close :** $9.22 (+3.6% vs previous close $8.90) | **Volume :** 1,712,500 (1.20× moy. 20j 1.42M)
> **Source données :** `data/latest.json` (2026-06-22 13:00:13 UTC) + `data/recommandations_latest.json`

---

## 1. Résumé des changements depuis l’analyse précédente (2026-06-22 10h UTC)

| Indicateur | 2026-06-22 10h UTC | 2026-06-22 13h UTC | Δ |
|------------|-------------------|-------------------|---|
| **Close** | $9.22 | **$9.22** | **stable** |
| **RSI 14j** | 43.86 | **43.86** | **stable** |
| **Volume vs 20j** | 1.20× (1.71M) | **1.20×** (1.71M) | **stable** |
| **MM50** | $10.85 | **$10.85** | **stable** |
| **Écart MM50** | −15.0% | **−15.0%** | **stable** |
| **ATR 14j** | $0.87 | **$0.87** | **stable** |
| **Max Pain (JSON)** | $7.50 (corrompu) | **$9.00** | **⚠️ CORRECTION JSON — valeur cohérente mais ↓$2.00 vs réf. opérationnelle** |
| **Put/Call (JSON)** | null (corrompu) | **0.66** | **⚠️ CORRECTION JSON — valeur cohérente mais ↑0.21 vs réf. opérationnelle** |
| **Call OI % (JSON)** | 0.0% (corrompu) | **60.3%** | **⚠️ CORRECTION JSON — valeur cohérente mais ↓8.7 pp vs réf. opérationnelle** |
| **Short Interest** | 24.32% | **24.32%** | **stable** |
| **Score Global Ajusté** | 52.8/100 | **52.8/100** | **stable** |
| **Score Opportunité** | 6.1/10 | **6.1/10** | **stable** |
| **Score Valorisation** | 7.0/10 | **7.0/10** | **stable** |
| **Score Momentum** | 4.0/10 | **4.0/10** | **stable** |

> **⚠️ Data quality — résolution de l’anomalie options JSON :** Le snapshot 13h UTC corrige l’incohérence observée à 10h (max pain $7.50 aberrant, put/call `null`, call OI 0.0%). Les valeurs sont désormais **cohérentes et exploitables** : max pain **$9.00**, put/call **0.66**, call OI **60.3%**, échéance **2026-06-26**.
>
> **Cependant**, ces valeurs corrigées diffèrent significativement de la référence opérationnelle utilisée depuis le 17/06 ($11.00 / 0.45 / 69.0%) :
> - Max pain : **−18.2%** ($11.00 → $9.00) — aimant baissier révisé au plus près du spot
> - Put/call : **+46.7%** (0.45 → 0.66) — biais haussier des calls atténué
> - Call OI % : **−8.7 pp** (69.0% → 60.3%) — dominance call réduite
>
> **Impact :** Le spot ($9.22) passe d’une position −16.2% sous max pain ($11.00, potentiel d’aspiration haussière) à **+2.4% au-dessus du max pain** ($9.00, pinning réduit, neutre). La structure options est désormais **moins haussière** qu’antérieurement estimée.

**Verdict :** Les données de marché (cours, volume, RSI, ATR, MM50) sont **strictement identiques** entre les snapshots 10h et 13h UTC. La seule évolution matérielle concerne la **résolution de l’anomalie options JSON** avec des valeurs désormais cohérentes mais **moins favorables** que la référence opérationnelle précédente. Le scoring agent est inchangé (ATTENDRE 52.8/100). **Thèse inchangée : ATTENDRE.**

---

## 2. Mise à jour technique

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| **Open** | $8.78 | — |
| **High** | $9.35 | Test de la résistance immédiate $9.35 — rejet au close |
| **Low** | $8.48 | Approche du 52W low ($8.31) — support psychologique testé et tenu |
| **Close** | $9.22 | Micro-rebond intraday +8.7% du low, close sous le high |
| **RSI 14j** | **43.86** | Zone neutre inférieure, inchangé vs 10h |
| **MM50** | **$10.85** | Écart **−15.0%** — tendance baissière intacte |
| **MM200** | — | Non calculée (historique insuffisant) |
| **ATR 14j** | **$0.87** | Volatilité élevée ; ATR relatif **9.44%** (> seuil 5.0%) — **ATR_SPIKE actif** |
| **Volume 20j** | 1.42M | Moyenne stable |
| **Volume session** | **1,712,500** | **1.20×** — liquidité en récupération |
| **Beta** | 2.392 | Volatilité systématique élevée |
| **52W Range** | $8.31 – $56.64 | Cours à **−83.7%** du 52W high, +11.0% au-dessus du 52W low |

**Supports / Résistances (ATR-based)**
- R1 (résistance immédiate) : $9.35 – $9.40 (high session + zone de rejet)
- R2 : $10.00 – $10.85 (seuil psychologique + MM50)
- S1 (support immédiat) : $8.90 – $9.00 (previous close + nouveau max pain $9.00)
- S2 : $8.48 (low session — testé et tenu)
- S3 : $8.31 (52W low — rupture = signal baissier majeur)

**Timing technique : Défavorable**
- Cours sous MM50 depuis 15+ sessions consécutives ; MM50 stable à $10.85
- Écart sous MM50 −15.0% — aucun signe de retournement
- RSI 43.86 — zone neutre inférieure sans momentum directionnel
- Close sous high ($9.22 < $9.35) → rejet en fin de séance
- Volume en récupération (1.20×) mais sans close au-dessus de la résistance $9.35
- ATR_SPIKE 9.44% — volatilité élevée = risque de whipsaw élevé

---

## 3. Mise à jour fondamentale

Aucune nouvelle donnée fondamentale publiée depuis le 2026-06-22 10h UTC. Les métriques restent inchangées :

| Métrique | Valeur | Contexte |
|----------|--------|----------|
| **Market Cap (Yahoo)** | $271.4M | — |
| **Market Cap (FMP)** | $3,268.5M | Divergence Yahoo/FMP persistante (×12.0) — [ANOMALIE DATA] |
| **Forward P/E** | 19.53 | Pricing d’une infime rentabilité future |
| **EV/Revenue** | 0.431 | Multiple très bas, méfiance du marché |
| **P/B** | 0.334 | Patrimoine net négatif (−$398.9M tangible) — discount profond |
| **Debt/Equity** | 2.433 | Levier élevé ; couverture intérêts négative (−4.7×) |
| **Current Ratio** | 0.844 | Risque de liquidité |
| **Gross Margin** | 11.1% | Faible |
| **Operating Margin** | −2.6% | Non rentable à l’opérationnel |
| **EBITDA Margin** | 7.96% | Légèrement positif |
| **Net Margin** | 5.72% | Rentabilité nette exceptionnelle (non opérationnelle) |
| **FCF Yield** | −18.91% | FCF négatif |
| **ROE (FMP)** | 56.5% | Artificiellement gonflé par patrimoine net négatif |
| **ROIC** | −2.15% | Destruction de valeur à l’investissement |
| **Consensus (FMP)** | $50.25 (4 analystes) | Upside théorique +445% — spéculatif |

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

### Options — Anomalie JSON RÉSOLUE, mais pivot structurel

| Indicateur | Valeur JSON 10h (corrompu) | Valeur JSON 13h (cohérent) | Réf. opérationnelle (depuis 17/06) | Signal |
|------------|-----------------------------|---------------------------|-----------------------------------|--------|
| **Max Pain** | $7.50 (aberrant) | **$9.00** | $11.00 | **↓$2.00 — aimant baissier révisé au plus près du spot** |
| **Put/Call Ratio** | null (corrompu) | **0.66** | 0.45 | **↑0.21 — moins de dominance call** |
| **Call OI %** | 0.0% (corrompu) | **60.3%** | 69.0% | **↓8.7 pp — biais haussier atténué** |
| **Échéance** | 2026-06-26 | 2026-06-26 | — | J+4 |

> **🟡 Pivot structurel options :** La résolution de l’anomalie JSON révèle une structure **moins haussière** que la référence opérationnelle utilisée depuis 6 jours :
> - Le spot ($9.22) n’est plus −16.2% sous un max pain à $11.00 (configuration « aimant haussier ») mais **+2.4% au-dessus d’un max pain à $9.00** (configuration « pinning neutre / légèrement baissier »).
> - Le put/call à 0.66 signifie que les puts représentent désormais 40% de l’OI vs 31% précédemment — une couverture baissière plus épaisse.
> - Le call OI à 60.3% reste majoritairement call, mais la marge de sécurité haussière s’est réduite de 8.7 pp.
>
> **Implication :** La probabilité d’un pinning haussier vers $11.00 à l’échéance du 26/06 est **fortement réduite**. Le max pain $9.00 est désormais le niveau d’équilibre options — un close sous $9.00 à l’expiration générerait une valorisation des puts ITM et une pression vendeuse additionnelle.

### Sentiment
- **Short Interest** : 24.32% du float (29.2M shares) — niveau élevé, potentiel short squeeze latent inchangé
- **Social Sentiment** : 0 mentions Reddit, score 0/10 — aucun buzz retail détecté
- **Analystes** : 4 analystes FMP, $50.25 price target, 0 couverture récente — consensus figé

### News / Événements
- Aucun événement corporate détecté dans `data/events_latest.json`
- Aucune news détectée dans `data/news_2026-06-22.json` (FUBO : tableau vide)
- Prochain earnings : **2026-08-06** (45 jours, Est EPS $−0.32–$0.07, Rev $1.5B)
- Aucune upgrade/downgrade, aucun insider trade significatif signalé

---

## 5. Scoring global actualisé

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.5/10 | 35% | 2.28 |
| **Valorisation** | 7.0/10 | 40% | 2.80 |
| **Momentum** | **4.0/10** | 25% | 1.00 |
| **Score Opportunité brut** | — | — | **6.1/10** |
| **Score Global brut** | — | — | **60.8/100** |
| **Malus / Bonus** | — | — | **−8.0 pts** |
| **Score Global Ajusté** | — | — | **52.8/100** |

**Règle de disqualification :** Aucun score ≤2/10 → pas d’exclusion automatique.

**Interprétation :**
- Le Score Global Ajusté **52.8/100** se situe dans la fourchette **ATTENDRE** (50–59).
- Le scoring agent est **inchangé** vs 10h UTC : aucune révision des scores Catalyseur, Valorisation ou Momentum.
- **Malus sectoriel** : XLC (Communication Services) est Bottom 3 dans `data/sector_rotation_latest.json` (momentum score 0.0) → malus −0.5 pt implicite non encore reflété dans le scoring agent.
- **Malus timing** : sous MM50 + RSI < 50 + ATR_SPIKE = pas de confirmation technique d’entrée.
- **Nouveau malus options** : la révision du max pain de $11.00 à $9.00 élimine le catalyseur technique latent lié au pinning haussier. Cet élément n’est pas capturé dans le scoring agent actuel.

---

## 6. Niveaux SL / TP / Ratio R/R

| Niveau | Valeur | Distance vs Close | Commentaire |
|--------|--------|-------------------|-------------|
| **Stop-Loss** | $7.48 | −18.9% (2× ATR = $1.74) | Inchangé — issu du scoring agent |
| **Take-Profit** | $11.83 | +28.3% (3× ATR = $2.61) | **Révisé ↓** — ancien TP $12.50 aligné sur max pain $11.00 désormais obsolète |
| **Ratio R/R** | **1.5×** | — | À la limite inférieure de l’acceptabilité institutionnelle |

> **Révision du TP :** L’ancien take-profit opérationnel ($12.50, aligné sur le max pain à $11.00 + marge technique) est désormais **incompatible** avec la nouvelle structure options (max pain $9.00). Le TP est ajusté à **$11.83** (proposé par le scoring agent) qui correspond à un niveau de résistance technique (MM50 $10.85 + marge ATR). Cependant, avec le max pain révisé à $9.00, la probabilité d’atteindre $11.83 d’ici l’échéance 2026-06-26 (J+4) est **faible** — cela exigerait un mouvement de +28.3% en 4 sessions.
>
> Le SL $7.48 reste sous le 52W low ($8.31), ce qui le rend risqué en cas de gap down.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

### Verdict : **THÈSE ATTENDRE CONFIRMÉE — OPTIONS LANDSCAPE RÉVISÉ À LA BAISSE**

Le snapshot 2026-06-22 13h UTC confirme la **stabilité totale des données de marché** (cours, volume, RSI, ATR, MM50 identiques au snapshot 10h). L’événement matériel du snapshot est la **résolution de l’anomalie options JSON** avec des valeurs désormais cohérentes mais **moins favorables** que la référence opérationnelle utilisée depuis le 17/06. Le max pain révisé à **$9.00** (vs $11.00), le put/call à **0.66** (vs 0.45) et le call OI à **60.3%** (vs 69.0%) dessinent un **landscape options moins haussier**, éliminant le catalyseur technique latent lié au pinning vers $11.00. Le scoring agent reste inchangé à **ATTENDRE 52.8/100**.

**Arguments pour la confirmation :**
1. **Récupération volume maintenue** : 1.71M (1.20×) — liquidité présente
2. **RSI en zone neutre inférieure** : 43.86 — pas de survente, marge de rebond
3. **Low $8.48 tenu** : au-dessus du 52W low ($8.31)
4. **Valorisation attractive inchangée** : P/B 0.334, EV/Rev 0.431
5. **Short interest élevé** : 24.32% = combustible latent
6. **Données options désormais cohérentes** : fin de l’incertitude data quality

**Arguments contre une entrée (renforcés) :**
1. **Landscape options révisé à la baisse** : max pain $9.00 (vs $11.00), put/call 0.66 (vs 0.45), call OI 60.3% (vs 69.0%) — catalyseur technique latent éliminé
2. **Close sous résistance** : rejet à $9.35, close $9.22 — pas de breakout
3. **MM50 en descente** : $10.85 — tendance baissière intacte
4. **Écart MM50 creusé** : −15.0% — pas d’amélioration structurelle
5. **ATR_SPIKE** : 9.44% — volatilité élevée = risque de whipsaw
6. **Qualité fondamentale dégradée** : Score Qualité 1/6, FCF négatif, patrimoine net négatif
7. **Pas de catalyseur actif** : aucune news, aucun upgrade, aucun événement corporate
8. **Timing Défavorable** : sous MM50 + RSI < 50 + ATR_SPIKE = pas de confirmation technique
9. **Malus sectoriel** : XLC bottom 3 sector rotation (momentum score 0.0)
10. **Pinning réduit** : avec max pain $9.00 et spot $9.22, l’échéance 2026-06-26 (J+4) n’offre plus de levier haussier significatif

**Conditions de réactivation d’une thèse ACHETER (révisées) :**
- Retour au-dessus de MM50 ($10.85) avec close confirmé au-dessus de $10.50
- Volume >1.0× moyenne 20j en confirmation (condition partiellement remplie aujourd’hui)
- **Nouveau** : données options JSON maintenues cohérentes avec max pain remonté ≥$10.00 et call OI >65%
- Catalyseur fondamental (earnings beat, upgrade analyste, guidance positive)

**Recommandation :** **ATTENDRE** — pas d’entrée en l’état. La résolution de l’anomalie options JSON est une avancée data quality, mais les valeurs corrigées révèlent une **structure options moins favorable** qu’antérieurement estimée. Le max pain à $9.00 élimine le catalyseur technique latent (pinning vers $11.00) et place le spot en position de légère surperformance vs l’équilibre options (+2.4%), ce qui réduit l’asymétrie haussière. L’échéance 2026-06-26 (J+4) pourrait générer de la volatilité autour du max pain $9.00, mais sans directionnalité privilégiée. Aucune position longue recommandée.

---

*Rapport généré par le desk Argus-IA — Données sources : `data/latest.json` (2026-06-22 13:00:13 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`. Anomalie options JSON résolue — valeurs corrigées intégrées.*
