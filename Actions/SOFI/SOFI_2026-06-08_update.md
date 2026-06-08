# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-08 (snapshot 13:00 UTC — close du 05/06 confirmé)
**Type :** `_update.md` — Correction options + confirmation reclassement ACHETER → SURVEILLER
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-08_update.md` (10:00 UTC) | **Snapshot 2026-06-08 (13:00 UTC)** | **Δ** |
|----------|-----------------------------------------|-------------------------------------|-------|
| Cours close | $16.03 | **$16.03** | **Inchangé** |
| RSI 14j | 52.78 | **52.78** | **Inchangé** |
| ATR 14j | $0.99 | **$0.99** | **Inchangé** |
| MM 50j | $16.75 | **$16.75** | **Inchangé** |
| Volume | 81.21M (1.15×) | **81.21M (1.15×)** | **Inchangé** |
| **Max Pain options** | **$5.00 [ABERRANT]** | **$17.00** | **✅ Corrigé** |
| **Put/Call ratio** | **null** | **0.57** | **✅ Corrigé** |
| **Call OI %** | **null** | **63.7%** | **✅ Corrigé** |
| Score Opportunité | 5.8/10 | **5.8/10** | **Inchangé** |
| Score Global ajusté | 49.8/100 | **49.8/100** | **Inchangé** |
| Action | SURVEILLER | **SURVEILLER** | **Confirmé** |

**Verdict :** Le snapshot 13:00 UTC confirme l'intégralité des données de prix du snapshot 10:00 UTC (close du 05/06 à $16.03). **[RÉSOLU]** L'anomalie options JSON (`Max Pain $5.00` aberrant, `Put/Call` et `Call OI` `null`) est corrigée : **Max Pain $17.00**, **Put/Call 0.57**, **Call OI 63.7%**. La posture **SURVEILLER** est confirmée.

**[ALERTE DATA QUALITY]** `data/quality_report_latest.json` flagge SOFI comme `excluded` pour `stale_price_history` (close identique sur 4 jours consécutifs). Cet état reflète la période de fermeture marché US (week-end + pré-ouverture lundi matin avant 9:30 ET) — **pas une exclusion opérationnelle**. Les données de clôture du 05/06 ($16.03) restent valides pour l'analyse.

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-06-08 | Signal |
|------------|-------------------|--------|
| RSI 14j | 52.78 | 🟡 Zone neutre — sortie de la zone constructive (>60) |
| MM 50j | $16.75 | 🔴 Cours −0.43% sous MM50 — breakout du 01/06 invalidé |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.99 | 🔴 Volatilité en hausse (+8.8% vs 03/06) — ATR relatif 6.18% |
| Support clé | $15.68 (low du 05/06) / $15.00 | 🔴 Support immédiat fragile |
| Résistance clé | $16.75 (MM50) / $17.46 (low 02/06) | 🔴 MM50 devient résistance dynamique |
| Volume relatif | 1.15× | 🔴 Distribution active confirmée sur gap baissier |
| Beta | 2.152 | ⚠️ Volatilité extrême amplifiée |

**Analyse technique :** Aucun changement de données vs snapshot 10:00 UTC. Le gap de **−6.53%** ($17.15 → $16.73 open, close $16.03) s'est effectué sur un volume de **81.21M (1.15× moy. 20j)**, confirmant une distribution institutionnelle active. La **MM50 à $16.75** reste résistance dynamique. Le RSI à **52.78** n'est pas en survente mais a perdu toute traction haussière. L'ATR à **$0.99** maintient la volatilité élevée.

**Niveaux clés révisés :**
- Support immédiat : **$15.68** (low du 05/06) — si cassé, test de **$15.00** puis **$14.05** (SL 2×ATR)
- Résistance immédiate : **$16.75** (MM50) — reclaim nécessaire pour réactiver la thèse haussière
- Résistance intermédiaire : **$17.46** (ancien low du 02/06)

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market cap | $20.56B | Stable (close 05/06 inchangé) |
| P/E LTM (Yahoo) | 35.62 | Compression multiple liée à la baisse |
| Forward P/E | 20.54 | Valorisation mécaniquement attractive |
| EV/Revenue | 4.839 | Stable |
| P/B (Yahoo) | 1.90 | Stable |
| Gross margin (FMP) | 75.1% | Excellent, stable |
| Operating margin | 11.0% | Stable |
| Net margin | 10.1% | Stable |
| Debt/Equity (FMP) | 0.173 | Très faible — bilan sain |
| FCF yield | −13.2% | FCF négatif — modèle en investissement |
| SBC/Revenue | 5.5% | Modéré, sous contrôle |
| ROE (FMP) | 4.6% | Faible — limite le Filtre Qualité à 4/6 |

**Aucune news structurante ni événement corporate détecté** (`data/events_latest.json` vide, `data/news_latest.json` vide). Le mouvement reste **purement technique et macro-correlé** : le secteur financier (XLF) a une force relative faible (momentum 4.0/10) et les valeurs à beta élevé (SOFI beta 2.152) sont sur-vendues en rotation défensive.

**Filtre Qualité (6 critères) :** Inchangé à **4/6 (Quality Partielle)**. Aucun nouvel état financier ni guidance. Le charter bancaire, le TAM fintech et la marque SoFi restent intacts.

**Short interest 13.68%** (inchangé) — élevé mais le potentiel de squeeze est annulé tant que le cours reste sous MM50 avec momentum baissier.

---

## 4. Mise à jour sentiment / options / news

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Consensus PT (FMP) | $25.41 (27 analystes) | 🟢 Upside consensus +58.5% vs cours $16.03 |
| Analystes actifs (1M) | 1 | 🟡 Couverture stable mais faible |
| Analystes actifs (1T) | 10 | 🟡 Couverture stable |
| **Max Pain** | **$17.00** | 🟢 Cohérent — proche du cours, pinning possible vers ce niveau |
| **Put/Call ratio** | **0.57** | 🟡 Légèrement haussier (put < call), mais moins bullish que 0.54 du 03/06 |
| **Call OI %** | **63.7%** | 🟡 Majorité calls, mais −1.3 pts vs 65.0% du 03/06 |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit |
| Pump detected | false | 🟢 Aucun signal pump |

**[RÉSOLU] Anomalie options corrigée dans `data/latest.json` (snapshot 13:00 UTC) :**
- Max Pain : **$17.00** (vs $5.00 aberrant à 10:00 UTC) — cohérent avec le range 52W ($13.46–$32.73)
- Put/Call ratio : **0.57** (vs `null`) — légèrement plus défensif que le 0.54 du 03/06
- Call OI % : **63.7%** (vs `null`) — légère baisse vs 65.0% du 03/06 (prise de profit sur calls post-gap)
- Expiration prochaine : **2026-06-12** (4 jours ouvrés)

**Interprétation options :** Le repositionnement options vers **Max Pain $17.00** (au-dessus du cours $16.03) crée une pression de pinning vers le haut à très court terme. Cependant, le Put/Call 0.57 est moins haussier que le 0.44 du 01/06, et le Call OI a légèrement baissé. Le sentiment options reste modérément positif mais s'affaiblit.

**News** — Aucune news structurante détectée via les flux automatiques (`data/news_latest.json` vide).

---

## 5. Scoring global révisé

| Score | Snapshot 2026-06-03 (ACHETER) | **Snapshot 2026-06-08 (SURVEILLER)** | **Δ** |
|-------|-------------------------------|---------------------------------------|-------|
| Score Opportunité | 6.1/10 | **5.8/10** | **−0.3** |
| Score Catalyseur | 6.8/10 | **6.8/10** | 0.0 |
| Score Valorisation | 5.5/10 | **6.0/10** | **+0.5** |
| Score Momentum | 6.0/10 | **4.0/10** | **−2.0 pts 🔴** |
| Score Global Composite | 60.8/100 | **57.8/100** | **−3.0 pts** |
| Score Global ajusté | 65.8/100 | **49.8/100** | **−16.0 pts 🔴** |
| Action | ACHETER | **SURVEILLER** | **🔴 Reclassement** |
| Timing | Favorable | **Défavorable** | **Inversé** |
| Sizing | Réduit | **—** | **Position non recommandée** |
| Horizon | 1–3 mois | **—** | **Suspendu** |

**Pondération régime :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime inconnu — pondération par défaut).

**Malus / Bonus appliqués (Score Global ajusté) :**
- Malus accounting : 0 (fichier absent)
- Malus geo : 0 (SOFI geo_risk_score 2/10, non exposé)
- Malus FX : 0 (fx_impact_score 0.0, exposition 55% mais stable)
- Malus social : 0 (pas de données — EXTREME_BEARISH par absence, pas de malus appliqué)
- Malus quant : 0 (pas de signaux historiques)
- Bonus event : 0 (pas d'événement corporate)
- Timing technique : **−8.0** (cours sous MM50 + gap baissier sur volume — malus sévère)

**Analyse du reclassement :** La baisse du cours améliore le Score Valorisation (+0.5 pt, Forward P/E 20.54), mais le **Score Momentum s'effondre de 6.0 à 4.0/10** (baissier) et le malus timing technique pèse lourd (−8 pts). Le résultat est un **Score Global ajusté à 49.8/100**, dans la zone SURVEILLER (35–49).

**Règle de disqualification :** Aucun score individuel ≤ 2/10 — SOFI n'est pas exclu, mais le momentum à 4.0/10 est proche de la zone de disqualification.

---

## 6. Niveaux révisés

| Niveau | Snapshot 2026-06-03 | Snapshot 2026-06-08 | Calcul |
|--------|---------------------|---------------------|--------|
| Prix d'entrée suggéré | $17.74 | **—** | Aucune entrée recommandée en SURVEILLER |
| Stop-loss | $15.92 | **$14.05** | $16.03 − 2×ATR ($0.99) = $14.05 |
| Take-profit | $20.47 | **$19.00** | $16.03 + 3×ATR ($0.99) = $19.00 |
| Upside / Downside | +15.4% / −10.3% | **+18.5% / −12.4%** | — |
| Ratio R/R | 1.50 | **1.50** | Stable (~1.5×) |

**Note sur les niveaux :** Les niveaux SL/TP sont recalculés sur la base du cours ($16.03) et de l'ATR ($0.99). Le ratio R/R reste à 1.5×, mais la probabilité de succès est réduite par le momentum baissier et la cassure de MM50. En zone SURVEILLER, **aucune entrée n'est recommandée**.

**Scénarios pour repasser en ACHETER :**
1. **Reclaim MM50** — Cours au-dessus de $16.75 en close avec volume >1.0× → réactivation technique possible
2. **Rebound sur support** — Rebond vif à partir de $15.68 avec volume acheteur >1.2× et RSI remontant >55
3. **Catalyseur fondamental** — News positive (guidance, contrat, M&A) permettant de passer le momentum

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**🔴 THÈSE INVALIDÉE — Reclassement ACHETER → SURVEILLER, breakout MM50 du 01/06 rompu**

Le gap baissier de **−6.53%** du 05/06 a **invalidé le breakout technique** qui avait justifié le reclassement en ACHETER le 01/06. En 4 séances, le cours est repassé de +10.9% au-dessus de la MM50 à −0.43% en dessous — un **fakeout baissier classique** qui pénalise les acheteurs du gap du 01/06.

**Ce qui a changé fondamentalement :**
- Aucun événement corporate ni news négative — la rupture est technique/macro
- La valorisation s'améliore mécaniquement (Forward P/E 20.54) mais ne suffit pas à compenser le momentum perdu
- Le secteur financier (XLF) est dans le top3 sectoriel mais avec un momentum faible (4.0/10) — le classement relatif est dû à la faiblesse générale des autres secteurs, pas à une force absolue
- Les options corrigées (Max Pain $17.00, Put/Call 0.57, Call OI 63.7%) indiquent un pinning haussier à très court terme, mais le sentiment s'affaiblit par rapport au 01/06

**Éléments invalidant la thèse :**
- Cours sous MM50 ($16.75) — trend haussier court terme rompu
- RSI retombé de 63.90 à 52.78 — perte de traction
- Gap baissier sur volume 1.15× = distribution institutionnelle confirmée
- Score Momentum chuté de 6.0 à 4.0/10 (baissier)
- Score Global ajusté de 65.8 à 49.8/100 — sortie de la zone ACHETER (60–74)
- Timing passé de Favorable à Défavorable

**Éléments conservant un potentiel long terme :**
- Forward P/E 20.54 attractif vs historique et vs consensus PT $25.41 (+58.5%)
- Short interest 13.68% reste élevé — squeeze potentiel si rebond technique
- Filtre Qualité 4/6 inchangé — business model intact
- Earnings Q2 dans 50j (28 juillet, EPS $0.10–$0.11) — catalyseur forward
- Consensus 27 analystes maintenu à $25.41
- Max Pain $17.00 au-dessus du cours = pinning options favorable à court terme

**Risques à surveiller :**
- Cassure sous $15.68 (low du 05/06) ouvrirait un test de $15.00 puis $14.05 (SL)
- ATR $0.99 = volatilité persistante — sizing réduit obligatoire si re-entrée
- XLF momentum 4.0/10 = headwind sectoriel relatif (top3 par exclusion)
- Score Global ajusté 49.8 — proche du seuil ÉVITER (< 35) si nouvelle baisse
- Filtre Qualité 4/6 — Quality Partielle, FCF négatif, ROE faible

**Action : SURVEILLER — Aucune entrée recommandée — Attendre reclaim MM50 $16.75 ou rebond sur $15.68 avec volume**

---

*Données sourcées : data/latest.json (2026-06-08T13:00:08+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json, data/quality_report_latest.json.*
