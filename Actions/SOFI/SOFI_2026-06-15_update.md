# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-15 (snapshot 13:00 UTC)
**Type :** `_update.md` — Données options partiellement restaurées, stabilité technique globale
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-15_update.md` (10:00 UTC) | **Snapshot 2026-06-15 (13:00 UTC)** | **Δ** |
|----------|-----------------------------------------|-------------------------------------|-------|
| Cours close | $16.58 | **$16.58** | **Inchangé** |
| RSI 14j | 55.69 | **55.69** | **Inchangé** |
| ATR 14j | 1.08 | **1.08** | **Inchangé** |
| MM 50j | 16.83 | **16.83** | **Inchangé** |
| Écart MM50 | −1.49% | **−1.49%** | **Inchangé** |
| Volume | 50.31M (0.69×) | **50.31M (0.69×)** | **Inchangé** |
| Short interest | 14.71% | **14.71%** | **Stable** |
| Max Pain | $1.00 [ALERTE] | **$1.00** | **[ALERTE PERSISTANTE]** |
| Put/Call ratio | null [ALERTE] | **0.42** | **Rétabli — vs historique 0.48 (−0.06)** |
| Call OI % | null [ALERTE] | **70.5%** | **Rétabli — vs historique 67.7% (+2.8 pts)** |
| **Score Opportunité** | **6.0/10** | **6.0/10** | **Inchangé** |
| **Score Catalyseur** | **6.8/10** | **6.8/10** | **Inchangé** |
| **Score Valorisation** | **6.0/10** | **6.0/10** | **Inchangé** |
| **Score Momentum** | **5.0/10** | **5.0/10** | **Inchangé** |
| **Score Global ajusté** | **52.3/100** | **52.3/100** | **Inchangé** |
| **Action** | **ATTENDRE** | **ATTENDRE** | **Inchangée** |
| Timing | Défavorable | **Défavorable** | **Inchangé** |

**Verdict :** Le snapshot **13:00 UTC** confirme une **stabilité mécanique totale** du cours ($16.58), des indicateurs techniques (RSI, ATR, MM50) et des scores agents par rapport au snapshot 10:00 UTC. Le seul changement matériel concerne les **données options**, partiellement rétablies dans `data/latest.json` : Put/Call **0.42** et Call OI **70.5%** sont désormais disponibles (vs `null` à 10h). Le Put/Call à **0.42** est légèrement inférieur à l'historique 0.48 (signal haussier marginal). Le Call OI à **70.5%** représente une hausse de **+2.8 pts** vs l'historique 67.7%, indiquant un **repositionnement haussier** sur les options à très court terme (expiration 2026-06-18). Le Max Pain reste aberrant à **$1.00** — [ALERTE DATA QUALITY] persistante. Le **Score Global 52.3/100** et la recommandation **ATTENDRE** sont maintenus.

---

## 2. Mise à jour technique

| Indicateur | Valeur snapshot 13:00 UTC | Signal |
|------------|---------------------------|--------|
| RSI 14j | 55.69 | 🟡 Zone neutre — inchangée |
| MM 50j | $16.83 | 🔴 Cours $16.58 = −1.49% sous MM50 — résistance proche |
| MM 200j | null | ⚪ [DONNÉES PARTIELLES] |
| ATR 14j | $1.08 | 🟢 Stable — expansion mécanique mineure |
| Support clé | $15.651 (low 09/06) / $16.23 (low 15/06) | 🟢 Support immédiat tenu |
| Résistance clé | $16.83 (MM50) / $17.00 (Max Pain historique) | 🔴 MM50 = résistance immédiate |
| Volume relatif | 0.69× | 🔴 Retrait significatif — manque de conviction |
| Beta | 2.152 | ⚠️ Volatilité extrême amplifiée |
| Short interest | 14.71% | 🔴 Élevé — squeeze potentiel intact |

**Analyse technique :** Aucun changement technique entre les snapshots 10:00 et 13:00 UTC. Le cours est stable à **$16.58** sur un volume en retrait (**0.69×**, −37% relatif). Le RSI **55.69** est en zone neutre. La MM50 à **$16.83** constitue la résistance immédiate. L'ATR **$1.08** est stable.

**Options (rétablissement partiel) :**
- Max Pain : **$1.00** — [ALERTE DATA QUALITY] persistante (historique $17.00 conservé)
- Put/Call : **0.42** — rétabli (vs `null` à 10h) ; légèrement inférieur à l'historique 0.48 = **sentiment légèrement plus haussier**
- Call OI : **70.5%** — rétabli (vs `null` à 10h) ; **+2.8 pts** vs historique 67.7% = **repositionnement haussier**
- Expiration prochaine : **2026-06-18** (3 jours ouvrés restants)

**Niveaux (ATR = $1.08) :**
- Support immédiat : **$16.23** (low du 15/06)
- Support intermédiaire : **$15.651** (low du 09/06)
- Support majeur : **$15.00** (psychologique)
- Résistance immédiate : **$16.83** (MM50)
- Résistance intermédiaire : **$17.00** (Max Pain historique)
- Résistance majeure : **$17.10** (high du 09/06)

**Verdict timing :** Défavorable — inchangé. Cours sous MM50 confirmé, volume faible.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market cap | $21.27B | Stable — mécanique |
| P/E LTM (Yahoo) | 36.84 | Stable |
| Forward P/E | 21.25 | Stable — mécaniquement attractif |
| EV/Revenue | 5.02 | Stable |
| P/B (Yahoo) | 1.965 | Stable |
| Gross margin (FMP) | 75.1% | Excellent, stable |
| Operating margin | 11.0% | Stable |
| Net margin | 10.1% | Stable |
| Debt/Equity (FMP) | 0.173 | Très faible — bilan sain |
| FCF yield | −13.2% | FCF négatif — modèle en investissement |
| SBC/Revenue | 5.5% | Modéré, stable |
| ROE (FMP) | 4.59% | Faible — limite Filtre Qualité à 4/6 |

**Aucune news structurante ni événement corporate détecté** (`data/events_latest.json` vide pour SOFI). Le mouvement reste **purement technique/sentiment**. Les fondamentaux n'ont pas changé.

**Filtre Qualité (6 critères) :** Inchangé à **4/6 (Quality Partielle)**. Aucun nouvel état financier ni guidance.

---

## 4. Mise à jour sentiment / options / news

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Consensus PT (FMP) | $25.41 (27 analystes) | 🟢 Upside consensus +53.3% vs cours $16.58 |
| Analystes actifs (1M) | 0 | 🟡 Aucune couverture récente |
| Analystes actifs (1T) | 10 | 🟡 Couverture stable |
| **Short interest** | **14.71%** | 🔴 Élevé — squeeze potentiel renforcé |
| **Max Pain** | **$1.00** [ALERTE] | 🔴 Données aberrantes — historique $17.00 conservé |
| **Put/Call ratio** | **0.42** | 🟢 Rétabli — légèrement haussier vs historique 0.48 |
| **Call OI %** | **70.5%** | 🟢 Rétabli — repositionnement haussier (+2.8 pts) |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit |
| Pump detected | false | 🟢 Aucun signal pump |

**Short interest :** Stable à **14.71%**. Le setup asymétrique squeeze/pression vendeuse est inchangé.

**Options :** [RÉSOLU PARTIELLEMENT] Les données options sont partiellement rétablies dans le snapshot 13:00 UTC. Put/Call **0.42** et Call OI **70.5%** sont désormais disponibles (vs `null` à 10h). Le repositionnement est **marginalement haussier** : Put/Call en baisse (−0.06 vs 0.48) et Call OI en hausse (+2.8 pts vs 67.7%). Le Max Pain à **$1.00** reste aberrant — valeur historique **$17.00** conservée avec mention [ALERTE].

**News** — Aucune news structurante détectée via les flux automatiques.

---

## 5. Scoring global révisé

| Score | Snapshot 10:00 UTC (ATTENDRE) | **Snapshot 13:00 UTC (ATTENDRE)** | **Δ** |
|-------|-------------------------------|-----------------------------------|-------|
| Score Opportunité | 6.0/10 | **6.0/10** | **Inchangé** |
| Score Catalyseur | 6.8/10 | **6.8/10** | **Inchangé** |
| Score Valorisation | 6.0/10 | **6.0/10** | **Inchangé** |
| Score Momentum | 5.0/10 | **5.0/10** | **Inchangé** |
| Score Global Composite | 60.3/100 | **60.3/100** | **Inchangé** |
| Score Global ajusté | 52.3/100 | **52.3/100** | **Inchangé** |
| Action | ATTENDRE | **ATTENDRE** | **Inchangée** |
| Timing | Défavorable | **Défavorable** | **Inchangé** |
| Sizing | — | **—** | **—** |
| Horizon | — | **—** | **—** |

**Pondération régime :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime Unknown — pondération par défaut).

**Malus / Bonus appliqués (Score Global ajusté) :**
- Malus accounting : 0 (fichier absent)
- Malus geo : 0 (SOFI non listé dans geo_risk — exposition neutre)
- Malus FX : 0 (fx_impact_score 0.0, exposition 55% mais stable)
- Malus social : 0 (pas de données — pas de malus appliqué)
- Malus quant : 0 (pas de signaux historiques)
- Bonus event : 0 (pas d'événement corporate)
- Timing technique : **−5.0** (cours sous MM50)
- Sector rotation : XLF #2 (momentum 6.73) — léger vent de poupe sectoriel

**Analyse du scoring :** Le **Score Global ajusté 52.3/100** est strictement inchangé vs le snapshot 10:00 UTC. SOFI reste en zone **ATTENDRE** (50–59), à **2.3 pt du seuil SURVEILLER** (<50). Les scores individuels n'ont pas évolué car les données de prix et de fondamentaux sont identiques.

**Règle de disqualification :** Aucun score individuel ≤ 2/10 — SOFI n'est pas exclu.

---

## 6. Niveaux révisés

| Niveau | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Calcul |
|--------|--------------------|--------------------|--------|
| Prix d'entrée suggéré | — | **—** | Aucune entrée recommandée en ATTENDRE |
| Stop-loss | $14.42 | **$14.42** | $16.58 − 2×ATR ($1.08) = $14.42 |
| Take-profit | $19.82 | **$19.82** | $16.58 + 3×ATR ($1.08) = $19.82 |
| Upside / Downside | +19.5% / −12.4% | **+19.5% / −12.4%** | — |
| Ratio R/R | 1.50 | **1.50** | Stable (~1.5×) |

**Note sur les niveaux :** Inchangés. En zone ATTENDRE, **aucune entrée n'est recommandée**.

**Scénarios pour repasser en ACHETER :**
1. **Reclaim MM50** — Cours au-dessus de $16.83 en close avec volume >1.0× → réactivation technique
2. **Breakout $17.00** — Dépassement du Max Pain historique avec volume >1.2× → signal haussier fort
3. **Short squeeze** — Short interest 14.71% + catalyseur positif → mouvement amplifié
4. **Catalyseur fondamental** — News positive (guidance, contrat, M&A) permettant de repasser Momentum >6/10

**Scénarios de vigilance (risque SURVEILLER) :**
1. **Cassure sous $16.23** (low 15/06) — ouvre le retour à $15.651
2. **Score Global < 50** — À 2.3 pt du seuil. Une baisse du Momentum ou de la Valorisation pourrait basculer en SURVEILLER
3. **Guidance cut ou news macro négative** (taux, prêts étudiants) — catalyseur baissier
4. **Augmentation short interest > 15%** — Niveau critique de pression vendeuse

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**🟢 THÈSE CONFIRMÉE — Stabilité mécanique totale, données options partiellement restaurées, repositionnement haussier marginal sur options. SOFI à 2.3 pt du seuil SURVEILLER.**

Le snapshot du **2026-06-15 à 13:00 UTC** confirme l'**absence de changement** sur les données de cours, de technique et de fondamentaux par rapport au snapshot 10:00 UTC. Le cours reste à **$16.58**, le RSI à **55.69**, l'ATR à **$1.08** et la MM50 à **$16.83**. Le volume à **0.69×** demeure en retrait significatif.

**Ce qui a changé :**
- **[RÉSOLU PARTIELLEMENT] Données options** — Put/Call **0.42** et Call OI **70.5%** désormais disponibles (vs `null` à 10h). Repositionnement **marginalement haussier** : Put/Call −0.06 vs historique, Call OI +2.8 pts vs historique.
- **[ALERTE PERSISTANTE] Max Pain $1.00** — Valeur aberrante inchangée dans `data/latest.json`. Historique **$17.00** conservé.

**Ce qui est inchangé :**
- Cours stable à **$16.58**
- Données techniques complètes (RSI, ATR, MM50)
- Short interest **14.71%** (setup squeeze intact)
- Forward P/E **21.25** attractif
- Consensus PT **$25.41** (+53.3% upside)
- Filtre Qualité **4/6** (Quality Partielle)
- Aucune news structurante, aucun événement corporate
- Earnings Q2 dans **43j** (28 juillet, EPS $0.10–$0.11, Rev $1.1B)
- Score Global **52.3/100** (ATTENDRE), timing Défavorable
- XLF (Financials) #2 sector rotation (momentum 6.73)

**Ce qui maintient ATTENDRE :**
- Score Global **52.3** — à **2.3 pt du seuil SURVEILLER** (<50)
- Cours sous MM50 **$16.83** = timing Défavorable
- Volume **0.69×** — retrait de participation, pas de conviction haussière
- Score Momentum **5.0/10** — seuil de neutralité
- [ALERTE DATA QUALITY] Max Pain corrompu — impossible d'évaluer le pinning exact

**Ce qui pourrait rebasculer vers ACHETER :**
- Reclaim complet de la MM50 ($16.83) avec volume >1.0×
- Breakout $17.00 (Max Pain historique) avec volume >1.2×
- Catalyseur fondamental positif guidant le momentum au-dessus de 6/10
- Short squeeze sur short interest 14.71% si catalyseur inattendu

**Risques à surveiller :**
- **Proximité du seuil SURVEILLER** — Score Global 52.3, une baisse de 2.3 pt basculerait la recommandation
- **Short interest 14.71%** — niveau critique ; >15% = pression vendeuse très élevée
- **Volume faible** — 0.69× = manque de conviction, risque de faux mouvements
- **Filtre Qualité 4/6** — Quality Partielle, FCF négatif, ROE faible
- **Beta 2.152** — exposition accrue aux mouvements macro
- **Anomalie Max Pain JSON** — persistante, valeur historique $17.00 conservée

**Action : ATTENDRE — Aucune entrée recommandée — Surveiller de près la proximité avec le seuil SURVEILLER (<50). Attendre reclaim MM50 $16.83 en close avec volume >1.0× ou breakout $17.00 pour réactiver la thèse haussière. Surveiller le support $16.23 (low du jour). Si cassé, risque de retour à $15.651. Attention au short interest 14.71% qui crée un setup asymétrique squeeze/pression. [ALERTE DATA QUALITY] Max Pain $1.00 aberrant persistant — historique $17.00 conservé.**

---

*Données sourcées : data/latest.json (2026-06-15T13:00:08+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/fx_exposure_latest.json, data/validation_report.txt.*
