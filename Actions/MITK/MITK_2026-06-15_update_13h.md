# MITK — Mise à Jour Post-Pipeline 13:00 UTC (2026-06-15)

> **Source :** `data/latest.json` (snapshot 2026-06-15 13:00 UTC) + agents recommandation, sector rotation, social sentiment, FX, events, upcoming events
> **Référence précédente :** [MITK_2026-06-15_update.md](MITK_2026-06-15_update.md) (snapshot 10:00 UTC 2026-06-15)
> **Desk :** Argus-IA | Pipeline : 13:00 UTC | Score Global Ajusté : **64.0/100** | Action : **ACHETER (Sizing Réduit)**

---

## Résumé des Changements depuis le Snapshot 10:00 UTC (2026-06-15)

| Indicateur | 10:00 UTC | 13:00 UTC | Δ vs Prior |
|-----------|-----------|-----------|------------|
| **Cours close** | **$16.45** | **$16.45** | **Inchangé** |
| **RSI 14j** | **52.97** | **52.97** | **Inchangé** |
| **ATR 14j** | **$0.93** | **$0.93** | **Inchangé** |
| **MM 50j** | **$15.04** | **$15.04** | **Inchangé** |
| **Volume du jour** | **605,000** (0.54×) | **605,000** (0.54×) | **Inchangé** |
| **Score Global Ajusté** | **64.0/100** | **64.0/100** | **Inchangé** |
| **Recommandation agent** | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | **Confirmé** |
| **Score Catalyseur** | 5.0/10 | **5.0/10** | Inchangé |
| **Score Valorisation** | 6.0/10 | **6.0/10** | Inchangé |
| **Score Momentum** | 7.0/10 | **7.0/10** | Inchangé |
| **Max Pain** | $2.50 (anomalie) | **$20.00** | **RÉSOLU** |
| **Put/Call ratio** | null (anomalie) | **0.20** | **RÉSOLU** |
| **Call OI %** | null (anomalie) | **83.4%** | **RÉSOLU** |
| **Short Interest** | 8.56% | **8.56%** | **Inchangé** |

**Lecture institutionnelle :** Le snapshot 13:00 UTC du 15 juin enregistre une **stabilité mécanique totale** des données de cours et techniques vs le snapshot 10:00 UTC. Aucune mutation du prix ($16.45), du RSI (52.97), de l'ATR ($0.93), de la MM50 ($15.04) ni du volume (605K, 0.54×). Le Score Global Ajusté reste à **64.0/100** et la recommandation **ACHETER (Sizing Réduit)** est inchangée.

**Mutation majeure : l'anomalie options JSON est résolue.** Après 5 snapshots consécutifs avec max pain aberrant ($2.50), put/call null et call OI null, les données options 13h UTC sont désormais validées :
- **Max Pain $20.00** (vs spot $16.45, upside +21.6%)
- **Put/Call ratio 0.20** (très faible, sentiment haussier marqué)
- **Call OI 83.4%** (dominance call massive)

Cette résolution transforme le sentiment dérivé d'"inutilisable" à **clairement haussier**, renforçant la conviction sur la thèse ACHETER (Réduit) sans modifier les scores eux-mêmes. Le risque de lecture erronée du sentiment options est levé.

---

## 1. Mise à Jour Technique

| Indicateur | Valeur 13:00 UTC | Δ vs 10:00 UTC | Lecture |
|---|---|---|---|
| **Cours close** | **$16.45** | Inchangé | Stabilité du rally +6.82% depuis le 10/06 |
| **RSI (14j)** | **52.97** | Inchangé | Neutre favorable, retrait du haut sans survente |
| **ATR (14j)** | **$0.93** | Inchangé | Volatilité normalisée — niveaux SL/TP valides |
| **MM 50j** | **$15.04** | Inchangé | Cours +9.4% au-dessus — tendance haussière de MT validée |
| **MM 200j** | **null** | Inchangé | Toujours manquante — tendance LT non validable |
| **Volume** | **605,000** | Inchangé | **0.54× moyenne 20j (1,111,035)** — liquidité effondrée persistante |
| **Beta** | **1.007** | Inchangé | Légèrement au-dessus du marché |

**Niveaux clés (inchangés, ATR stable) :**
- Support immédiat : $15.52 (low 15/06)
- Support intermédiaire : $15.04 (MM50)
- Support structurel : $14.50 (zone de consolidation 09–10/06)
- Résistance immédiate : $16.86 (high 15/06)
- Résistance structurelle : $17.97 (52w high)
- Stop-loss ATR (2×, base $0.93) : **$14.59** (−11.3%)
- Take-profit ATR (3×, base $0.93) : **$19.24** (+17.0%)
- Ratio R/R : **1.5** — en-deçà du seuil institutionnel 1:2

**Verdict timing :** **Favorable.** Configuration technique inchangée : cours au-dessus de la MM50 (+9.4%), RSI neutre favorable (52.97), ATR disponible. La résolution de l'anomalie options renforce la conviction sans changer la note technique. **Le volume effondré (0.54×) reste le principal point de fragilité.**

---

## 2. Mise à Jour Fondamentale

| Métrique | Valeur 13:00 UTC | Source | Δ vs 10:00 UTC |
|----------|-------------------|--------|-----------------|
| Market Cap | $742.9M (Yahoo) / $446.6M (FMP) | Yahoo + FMP | Inchangé |
| P/E (TTM) | 48.38x (Yahoo) / 50.78x (FMP) | Yahoo + FMP | Inchangé |
| Forward P/E | 13.55x | Yahoo Finance | Inchangé |
| EV/EBITDA | 17.20x (Yahoo) / 12.15x (FMP) | Yahoo + FMP | Inchangé |
| P/B | 3.08x (Yahoo) / 1.86x (FMP) | Yahoo + FMP | Inchangé |
| Gross Margin | 85.1% | FMP | — |
| Operating Margin | 9.3% | FMP | — |
| Net Margin | 4.9% | FMP | — |
| ROIC | 3.16% | FMP key metrics | — |
| FCF Yield | 12.1% | FMP | — |
| Short Interest | 8.56% | Yahoo | Inchangé |

**Filtre Qualité :** 3–4 / 6 — **Quality Partielle** (inchangé). Aucune mutation fondamentale entre les snapshots 10h et 13h UTC. Le Forward P/E à 13.55x reste attractif pour une small-cap tech à forte marge brute (85.1%), mais le ROIC faible (3.16%) et la couverture analystes limitée (2 analysts, consensus PT $16.00) limitent la conviction.

**Divergence Yahoo/FMP persistante :** Market cap $742.9M vs $446.6M (-40%), P/E 48.38x vs 50.78x, EV/EBITDA 17.20x vs 12.15x. Cette divergence structurelle est récurrente et doit être prise en compte dans l'analyse. Nous utilisons Yahoo comme source primaire pour le cours et les données temps réel.

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur 13:00 UTC | Δ vs 10:00 UTC | Lecture |
|---|---|---|---|
| Consensus PT | $16.00 (2 analysts) | Inchangé | Spot $16.45 **au-dessus du PT** — consensus dépassé |
| **Max Pain** | **$20.00** | **Anomalie RÉSOLUE** | Valeur opérationnelle rétablie — upside vers max pain +21.6% |
| **Put/Call ratio** | **0.20** | **Anomalie RÉSOLUE** | Très faible — sentiment haussier marqué |
| **Call OI %** | **83.4%** | **Anomalie RÉSOLUE** | Dominance call massive — alignement haussier |
| Short Interest | 8.56% | Inchangé | Modéré, stable |
| Social Sentiment | 0 / No data | Inchangé | Sous le radar retail |
| Upgrades/Downgrades | Aucun | Inchangé | Silence analystes |
| News structurantes | Aucune | Inchangé | 0 news MITK |
| Événements corporate | Aucun | Inchangé | 0 événement MITK |
| FX Impact | 0.0 / 🟢 | Inchangé | Pas d'exposition FX significative |

**Verdict Sentiment :** **Haussier.** La résolution de l'anomalie options JSON est l'événement majeur de ce snapshot. Après 5 snapshots consécutifs avec des données dérivées inutilisables (max pain $2.50, put/call null, call OI null), le système 13h UTC valide :
- **Max Pain $20.00** — niveau plausible, +21.6% au-dessus du spot
- **Put/Call 0.20** — ratio très faible, indiquant un déséquilibre haussier notable
- **Call OI 83.4%** — dominance des positions call, alignement avec une attente de hausse

Ces valeurs sont cohérentes avec la thèse ACHETER (Réduit) et renforcent la conviction dérivée. Aucun flux de news, aucun insider trade, aucun upgrade/downgrade. MITK reste sous le radar institutionnel et retail, mais le marché options anticipe un mouvement haussier vers la zone $20.00 (max pain).

---

## 4. Scoring Global — Confirmé avec Conviction Renforcée

| Pilier | Valeur 10:00 UTC | Valeur 13:00 UTC | Poids | Pondéré |
|---|---|---|---|---|
| **Catalyseur** | 5.0/10 | **5.0/10** | 35% | 1.750 |
| **Valorisation** | 6.0/10 | **6.0/10** | 40% | 2.400 |
| **Momentum** | 7.0/10 | **7.0/10** | 25% | 1.750 |
| **Score Opportunité** | **5.9/10** | **5.9/10** | — | — |
| **Score Global Ajusté** | **64.0/100** | **64.0/100** | — | — |

| Seuil | Action | Sizing |
|---|---|---|
| Score Global 64.0/100 | **ACHETER** | **Réduit** |

**Confirmation de la thèse.** Le snapshot 13:00 UTC maintient le Score Global Ajusté à **64.0/100** (catégorie ACHETER Réduit, fourchette 60–74). Les trois piliers sont inchangés : Catalyseur 5.0/10, Valorisation 6.0/10, Momentum 7.0/10. Le timing reste **Favorable**.

**La conviction est néanmoins renforcée** par la résolution de l'anomalie options, qui élimine un brouillard significatif sur le sentiment dérivé. Le put/call 0.20 et le call OI 83.4% confirment une posture haussière du marché options, cohérente avec la recommandation.

**Risques additionnels :**
- Geo risk : Pas de données spécifiques MITK dans `geo_risk_latest.json`
- FX impact : 0.0 — exposition USD, pas de divergence, flag 🟢
- Social sentiment : 0/10 — pas de signal retail
- Events corporate : aucun
- Sector rotation : XLK top rank (momentum 10.0), signal NEUTRAL — favorable pour MITK (Technology)
- Quant significance : Insuffisant (0 signaux historiques, p-value 1.0)

---

## 5. Révision des Niveaux SL / TP

| Niveau | Valeur | Δ vs 10:00 UTC |
|---|---|---|
| **Stop-loss** | **$14.59** (base ATR $0.93) | Inchangé |
| **Take-profit** | **$19.24** (base ATR $0.93) | Inchangé |
| **Ratio R/R** | **1.5** | Inchangé |

**SL/TP maintenus.** Aucune mutation de l'ATR ($0.93) ni du cours ($16.45) entre les deux snapshots. Le SL à $14.59 (−11.3%) reste cohérent avec le support MM50 ($15.04) et le support structurel $14.50. Le TP à $19.24 (+17.0%) vise la zone de résistance majeure ($17.97 52w high) avec une marge de dépassement. Le ratio R/R reste à 1.5, en-deçà du seuil institutionnel 1:2, ce qui justifie le sizing Réduit.

---

## 6. Calendrier & Événements

| Événement | Date | Jours restants |
|---|---|---|
| **Earnings Q3 FY2026** | 2026-08-06 | **52** |
| **Expiration options** | 2026-06-18 | **3** |

**Alertes actives (révisées) :**
- 🟢 **[ANOMALIE OPTIONS JSON RÉSOLUE]** Max pain $20.00, put/call 0.20, call OI 83.4% — données dérivées validées après 5 snapshots — 2026-06-15
- 🟡 **[VOLUME EFFONDRE]** 605,000 = 0.54× moyenne 20j — liquidité réduite de moitié, rally peu crédible — 2026-06-15
- 🟡 **[CONSENSUS PT SOUS LE SPOT]** $16.00 < $16.45 — objectif moyen dépassé, absence de catalyseur analyste — 2026-06-15
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital — 2026-05-18
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($742.9M Yahoo vs $446.6M FMP), P/E, EV multiples — persistant
- 🟡 **[BETA LÉGÈREMENT SUPÉRIEUR AU MARCHÉ]** 1.007 — sensibilité marché accrue — 2026-06-08
- 🟢 **[DONNÉES TECHNIQUES RÉCUPÉRÉES]** ATR $0.93, MM50 $15.04 — validation des niveaux de support — 2026-06-15
- 🟢 **[RSI NEUTRE FAVORABLE]** 52.97 — zone neutre, pas de surachat — 2026-06-15
- 🟢 **[COURS AU-DESSUS DE MM50]** $16.45 vs $15.04 (+9.4%) — tendance haussière de MT validée — 2026-06-15
- 🔴 **[PULLBACK −15.3% SANS CATALYSEUR IDENTIFIABLE]** Risque de continuation baissière si support MM50 cède — 2026-06-08

---

## 7. Conclusion — Thèse CONFIRMÉE : ACHETER (Sizing Réduit)

**Verdict : THÈSE CONFIRMÉE.** Snapshot 13:00 UTC 2026-06-15 : la recommandation **ACHETER (Sizing Réduit)** est maintenue sur un Score Global Ajusté stable à **64.0/100**. Aucune mutation des données de cours ($16.45), techniques (RSI 52.97, ATR $0.93, MM50 $15.04) ni fondamentales entre les snapshots 10h et 13h UTC.

**La thèse est confirmée et la conviction renforcée pour les raisons suivantes :**
1. **Résolution de l'anomalie options JSON** — max pain $20.00, put/call 0.20, call OI 83.4% validés, éliminant le risque de lecture erronée du sentiment
2. **Score Global stable à 64.0/100** — dans la fourchette ACHETER (Réduit) 60–74
3. **Configuration technique haussière inchangée** — cours +9.4% au-dessus de MM50, RSI neutre favorable
4. **Sentiment dérivé désormais haussier** — put/call 0.20 et call OI 83.4% confirment une posture haussiere du marché options
5. **Timing Favorable maintenu** — sans surachat ni survente

**Points de vigilance qui justifient le sizing Réduit (inchangés) :**
1. **Volume effondré** — 0.54× moyenne 20j, le rally s'opère sur une liquidité réduite de moitié
2. **Consensus PT sous le spot** — $16.00 < $16.45, pas de catalyseur analyste
3. **Ratio R/R 1.5** — en-deçà du seuil institutionnel 1:2
4. **Aucune news structurante** — silence complet sur le ticker
5. **MM200 toujours manquante** — impossible de valider la tendance de long terme

**Points de vigilance :**
- Confirmation volume à la prochaine séance US — un retour >1.0× moyenne 20j est nécessaire pour valider la conviction
- Tenue du support MM50 $15.04 — cassure = retour ATTENDRE
- Earnings Q3 FY2026 (2026-08-06) — 52j, Est EPS $0.24–$0.34, Rev ~$0.1B
- Expiration options 2026-06-18 — 3j, max pain $20.00 (upside +21.6% vs spot)

**Catalyseurs forward :**
1. **Test de la résistance $17.97** (52w high) — scénario le plus probable à MT si volume se normalise
2. **Earnings Q3 FY2026 (2026-08-06)** — 52j, Est EPS $0.24–$0.34, Rev ~$0.1B
3. **Expiration options 2026-06-18** — 3j, structure max pain $20.00 (upside +21.6% vs spot)

**Risques :**
- Volume faible — risque de dead-cat bounce ou gap-fill sans conviction
- Support MM50 $15.04 — cassure = invalidation de la thèse haussière de MT
- Consensus PT faible couverture ($16.00, 2 analysts)
- ROIC faible (3.16%)
- SBC / Revenue élevé (9.35%)
- Faible liquidité de la small-cap

**Recommandation :** **ACHETER (Sizing Réduit).**

**Entrée suggérée :** $16.45 (spot) — timing Favorable, mais attendre un retour de volume >1.0× pour confirmation.
**Stop-loss :** $14.59 (base ATR $0.93, −11.3%) — ajustable si ATR évolue.
**Take-profit :** $19.24 (base ATR $0.93, +17.0%).
**Sizing :** Réduit — le ratio R/R 1.5 est en-deçà du seuil institutionnel 1:2, et le volume faible limite la conviction.

**Déteneurs :** maintenir la position avec le SL strict à $14.59. Surveiller le retour du volume et la tenue du support MM50 $15.04. Sur cassure de $15.04, envisager une réduction de position.

**Non-déteneurs :** entrée possible à $16.45 avec sizing Réduit, mais préférer attendre un snapshot avec volume >1.0× moyenne 20j pour confirmer la conviction. Ne pas chasser le rally sur volume faible.

---

*Révision post-pipeline 13:00 UTC — Données : `data/latest.json` (2026-06-15T13:00:14Z), `data/recommandations_2026-06-15.json` (ACHETER Réduit, 64.0/100, C:5.0 V:6.0 M:7.0), `data/quant_2026-05-17.json` (insuffisant), `data/geo_risk_2026-05-17.json` (pas de données MITK), `data/sector_rotation_2026-06-15.json` (signal NEUTRAL, XLK top rank momentum 10.0), `data/fx_exposure_2026-06-15.json` (impact 0.0), `data/social_sentiment_2026-06-15.json` (pas de données), `data/upcoming_events_2026-06-15.json` (earnings 2026-08-06), `data/events_2026-06-15.json` (0 événement) — Date : 2026-06-15*
