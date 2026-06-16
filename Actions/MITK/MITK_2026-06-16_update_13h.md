# MITK — Mise à Jour Post-Pipeline 13:00 UTC (2026-06-16)

> **Source :** `data/latest.json` (snapshot 2026-06-16 13:00 UTC) + agents recommandation, sector rotation, social sentiment, FX, events, upcoming events
> **Référence précédente :** [MITK_2026-06-16_update.md](MITK_2026-06-16_update.md) (snapshot 10:00 UTC 2026-06-16)
> **Desk :** Argus-IA | Pipeline : 13:00 UTC | Score Global Ajusté : **64.0/100** | Action : **ACHETER (Sizing Réduit)**

---

## Résumé des Changements depuis le Snapshot 10:00 UTC (2026-06-16)

| Indicateur | 10:00 UTC 16/06 | 13:00 UTC 16/06 | Δ vs Prior |
|-----------|-----------|-----------|------------|
| **Cours close** | **$16.57** | **$16.57** | **Inchangé** |
| **Previous close** | **$16.57** | **$16.45** | **Correction data source** |
| **Change %** | **0.00%** | **+0.73%** | **Recalculé** |
| **RSI 14j** | **49.16** | **49.16** | **Inchangé** |
| **ATR 14j** | **$0.88** | **$0.88** | **Inchangé** |
| **MM 50j** | **$15.09** | **$15.09** | **Inchangé** |
| **Volume du jour** | **601,400** (0.56×) | **601,400** (0.56×) | **Inchangé** |
| **Score Global Ajusté** | **64.0/100** | **64.0/100** | **Inchangé** |
| **Recommandation agent** | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | **Confirmé** |
| **Score Catalyseur** | 5.0/10 | **5.0/10** | Inchangé |
| **Score Valorisation** | 6.0/10 | **6.0/10** | Inchangé |
| **Score Momentum** | 7.0/10 | **7.0/10** | Inchangé |
| **Max Pain (JSON)** | **$2.50** (anomalie) | **$20.00** | **✅ RÉSOLU** |
| **Put/Call ratio (JSON)** | **null** | **0.20** | **✅ RÉSOLU** |
| **Call OI % (JSON)** | **null** | **83.4%** | **✅ RÉSOLU** |
| **Short Interest** | 8.56% | **8.56%** | Inchangé |

**Lecture institutionnelle :** Le snapshot 13:00 UTC du 16 juin enregistre une **stabilité quasi-totale** par rapport au snapshot 10:00 UTC. Le cours est inchangé à **$16.57**, le RSI stable à **49.16**, l'ATR à **$0.88** et la MM50 à **$15.09**. Le volume est strictement identique (**601,400**). La seule variation observable est la correction du **previous close** à **$16.45** (vs $16.57 auparavant), ce qui recalcule le change à **+0.73%** — cohérent avec l'open à $16.85 et le low à $16.41.

**Anomalie options JSON RÉSOLUE :** Pour la première fois depuis le 15 juin (21h UTC), les données options JSON sont pleinement valides : **max pain $20.00, put/call 0.20, call OI 83.4%**. Il s'agit d'une amélioration data quality significative qui supprime l'alerte jaune persistante sur l'anomalie JSON récurrente. Les valeurs opérationnelles historiques sont désormais confirmées par la source primaire.

**DRAFT_refresh du 16/06 (13h) :** Le fichier `MITK_2026-06-16_DRAFT_refresh.md` a été généré avec un trigger `ATR_SPIKE 5.31%` (medium). Or l'ATR est strictement identique au snapshot 10:00 UTC ($0.88). Ce trigger est classé comme **faux positif algorithmique** — **6e occurrence du même type sur MITK** (précédents : 31/05, 27/05, 08/06, 15/06, 16/06 10h). La règle heuristique issue des apprentissages s'applique : *si ATR inchangé vs snapshot précédent mais trigger ATR_SPIKE déclenché → archiver comme faux positif, ne pas réécrire l'analyse fondamentale.*

---

## 1. Mise à Jour Technique

| Indicateur | Valeur 13:00 UTC | Δ vs 10:00 UTC | Lecture |
|---|---|---|---|
| **Cours close** | **$16.57** | Inchangé | Stabilité parfaite post-consolidation |
| **Previous close** | **$16.45** | Correction | Recalcul du change % à +0.73% |
| **Open / High / Low** | $16.85 / $16.93 / $16.41 | — | Range intraday 3.16% — normal pour ATR $0.88 |
| **RSI (14j)** | **49.16** | Inchangé | Neutre, retrait vers médiane — pas de survente |
| **ATR (14j)** | **$0.88** | Inchangé | Volatilité stable, supports/résistances inchangés |
| **MM 50j** | **$15.09** | Inchangé | Cours +9.8% au-dessus — tendance haussière de MT validée |
| **MM 200j** | **null** | Inchangé | Toujours manquante — tendance LT non validable |
| **Volume** | **601,400** | Inchangé | **0.56× moyenne 20j (1,075,145)** — stable, sous la normale |
| **Beta** | **1.007** | Inchangé | Légèrement au-dessus du marché |
| **52w high / low** | $17.97 / $8.53 | Inchangé | Spot à −7.8% du 52w high |

**Niveaux clés (inchangés, ATR stable) :**
- Support immédiat : $16.41 (low 16/06)
- Support intermédiaire : $15.09 (MM50)
- Support structurel : $14.50 (zone de consolidation 09–10/06)
- Résistance immédiate : $16.93 (high 16/06)
- Résistance structurelle : $17.97 (52w high)
- Stop-loss ATR (2×, base $0.88) : **$14.81** (−10.6%)
- Take-profit ATR (3×, base $0.88) : **$19.21** (+15.9%)
- Ratio R/R : **1.5** — en-deçà du seuil institutionnel 1:2

**Verdict timing :** **Favorable.** Configuration technique globalement inchangée : cours au-dessus de la MM50 (+9.8%), RSI neutre (49.16), ATR stable. Aucune cassure de support ni franchissement de résistance. La stabilité du cours sur trois snapshots consécutifs (21h 15/06, 10h 16/06, 13h 16/06) confirme la consolidation saine après le rally du 15 juin.

---

## 2. Mise à Jour Fondamentale

| Métrique | Valeur 13:00 UTC | Source | Δ vs 10:00 UTC |
|----------|-------------------|--------|-----------------|
| Market Cap | $748.3M (Yahoo) / $446.6M (FMP) | Yahoo + FMP | Inchangé |
| P/E (TTM) | 48.74 (Yahoo) / 50.78x (FMP) | Yahoo + FMP | Stable |
| Forward P/E | 13.65x | Yahoo Finance | Stable |
| EV/EBITDA | 17.33x (Yahoo) / 12.15x (FMP) | Yahoo + FMP | Stable |
| P/B | 3.10x (Yahoo) / 1.86x (FMP) | Yahoo + FMP | Stable |
| Gross Margin | 85.1% | FMP | — |
| Operating Margin | 9.34% | FMP | — |
| Net Margin | 4.90% | FMP | — |
| ROIC | 3.16% | FMP key metrics | — |
| FCF Yield | 12.1% | FMP | — |
| Short Interest | 8.56% | Yahoo | Inchangé |

**Filtre Qualité :** 3–4 / 6 — **Quality Partielle** (inchangé). Aucune mutation fondamentale entre les snapshots. Le Forward P/E à 13.65x reste attractif pour une small-cap tech à forte marge brute (85.1%), mais le ROIC faible (3.16%) et la couverture analystes limitée (2 analysts, consensus PT $16.00) limitent la conviction.

**Divergence Yahoo/FMP persistante :** Market cap $748.3M vs $446.6M (−40%), P/E 48.74x vs 50.78x, EV/EBITDA 17.33x vs 12.15x. Cette divergence structurelle est récurrente et doit être prise en compte dans l'analyse. Yahoo reste la source primaire pour le cours et les données temps réel.

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur 13:00 UTC | Δ vs 10:00 UTC | Lecture |
|---|---|---|---|
| Consensus PT | $16.00 (2 analysts) | Inchangé | Spot $16.57 **au-dessus du PT** — consensus dépassé de +3.6% |
| **Max Pain (JSON)** | **$20.00** | ✅ **RÉSOLU** | Valeur opérationnelle validée par source primaire |
| **Put/Call ratio (JSON)** | **0.20** | ✅ **RÉSOLU** | Valeur opérationnelle validée par source primaire |
| **Call OI % (JSON)** | **83.4%** | ✅ **RÉSOLU** | Valeur opérationnelle validée par source primaire |
| Short Interest | 8.56% | Inchangé | Modéré, stable |
| Social Sentiment | 0 / No data | Inchangé | Sous le radar retail |
| Upgrades/Downgrades | Aucun | Inchangé | Silence analystes |
| News structurantes | Aucune | Inchangé | 0 news MITK |
| Événements corporate | Aucun | Inchangé | 0 événement MITK |
| FX Impact | 0.0 / 🟢 | Inchangé | Pas d'exposition FX significative |

**Verdict Sentiment :** **Haussier (renforcé).** La résolution de l'anomalie options JSON est un signal positif data quality. Les valeurs validées (max pain $20.00, put/call 0.20, call OI 83.4%) confirment une posture haussiere du marché options. L'absence de news structurante et le silence médiatique/analyste suggèrent que ce sentiment est technique (positionnement avant expiration du 18/06) plutôt que fondamental. MITK reste sous le radar institutionnel et retail.

---

## 4. Scoring Global — Confirmé sans Mutation

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

**Confirmation de la thèse.** Le snapshot 13:00 UTC du 16 juin maintient la recommandation **ACHETER (Sizing Réduit)** sur un Score Global Ajusté de **64.0/100** (inchangé vs 10:00 UTC). Aucun pilier n'a muté : Catalyseur 5.0/10, Valorisation 6.0/10, Momentum 7.0/10. Le timing reste **Favorable**.

**La prudence est maintenue** pour les mêmes raisons que le snapshot 10:00 UTC :
1. **Volume encore réduit** — 0.56× moyenne 20j, la liquidité reste inférieure à la normale
2. **RSI retrait vers la médiane** — 49.16, le momentum ralentit sans inverser
3. **Ratio R/R 1.5** — en-deçà du seuil institutionnel 1:2

**Risques additionnels :**
- Geo risk : Pas de données spécifiques MITK dans `geo_risk_latest.json` (date 2026-05-17)
- Accounting risk : Fichier `data/accounting_risk_latest.json` absent — pas de scan comptable disponible
- FX impact : 0.0 — exposition USD, pas de divergence, flag 🟢
- Social sentiment : 0/10 — pas de signal retail
- Events corporate : aucun
- Sector rotation : signal NEUTRAL (régime UNKNOWN), XLK top rank (momentum 10.0) — favorable pour MITK (Technology), bien que les données RS soient corrompues (NaN) et que le momentum_score 10.0 soit uniforme sur tous les secteurs (signal peu discriminant)
- Quant significance : Insuffisant (0 signaux historiques, p-value 1.0)
- Validation data : aucune erreur ni warning sur MITK dans `validation_report.txt`

---

## 5. Révision des Niveaux SL / TP

| Niveau | Valeur | Δ vs 10:00 UTC |
|---|---|---|
| **Stop-loss** | **$14.81** (base ATR $0.88) | Inchangé (ATR stable) |
| **Take-profit** | **$19.21** (base ATR $0.88) | Inchangé |
| **Ratio R/R** | **1.5** | Inchangé |

**SL/TP stables.** L'ATR inchangé à $0.88 maintient les niveaux. Le SL à $14.81 (−10.6%) reste cohérent avec le support MM50 ($15.09) et le support structurel $14.50. Le TP à $19.21 (+15.9%) vise la zone de résistance majeure ($17.97 52w high) avec une marge de dépassement. Le ratio R/R reste à 1.5, en-deçà du seuil institutionnel 1:2, ce qui justifie le sizing Réduit.

---

## 6. Calendrier & Événements

| Événement | Date | Jours restants |
|---|---|---|
| **Earnings Q3 FY2026** | 2026-08-06 | **51** |
| **Expiration options** | 2026-06-18 | **2** |

**Alertes actives (révisées) :**
- 🟡 **[VOLUME RÉDUIT]** 601,400 = 0.56× moyenne 20j — stable mais liquidité toujours inférieure à la normale — 2026-06-16
- 🟡 **[CONSENSUS PT SOUS LE SPOT]** $16.00 < $16.57 — objectif moyen dépassé de +3.6%, absence de catalyseur analyste — 2026-06-15
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital dans les prochains filings — 2026-05-18
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($748.3M Yahoo vs $446.6M FMP), P/E, EV multiples — persistant
- 🟡 **[BETA LÉGÈREMENT SUPÉRIEUR AU MARCHÉ]** 1.007 — sensibilité marché accrue — 2026-06-08
- 🟢 **[ANOMALIE OPTIONS JSON RÉSOLUE]** Max pain $20.00, put/call 0.20, call OI 83.4% — données validées par source primaire, alerte levée — 2026-06-16
- 🟢 **[RSI NEUTRE FAVORABLE]** 49.16 — zone neutre, pas de surachat — 2026-06-16
- 🟢 **[COURS AU-DESSUS DE MM50]** $16.57 vs $15.09 (+9.8%) — tendance haussière de MT validée — 2026-06-16
- 🔴 **[PULLBACK −15.3% SANS CATALYSEUR IDENTIFIABLE]** Risque de continuation baissière si support MM50 cède — 2026-06-08

---

## 7. Conclusion — Thèse CONFIRMÉE : ACHETER (Sizing Réduit)

**Verdict : THÈSE CONFIRMÉE.** Snapshot 13:00 UTC 2026-06-16 : la recommandation **ACHETER (Sizing Réduit)** est maintenue sur un Score Global Ajusté de **64.0/100** (inchangé vs 10:00 UTC 16/06). Aucune mutation technique, fondamentale ou sentimentale n'est observée entre les deux snapshots. Le cours est stable à **$16.57**, le RSI à **49.16**, l'ATR à **$0.88**. Le volume est stable à **0.56×** moyenne 20j.

**Anomalie options JSON RÉSOLUE — signal positif data quality.** Pour la première fois depuis le 15 juin, les données options JSON sont pleinement validées : max pain $20.00, put/call 0.20, call OI 83.4%. L'alerte jaune sur l'anomalie récurrente est levée.

**Le DRAFT_refresh `MITK_2026-06-16_DRAFT_refresh.md` (trigger ATR_SPIKE 5.31%) est classé comme FAUX POSITIF (6e occurrence)** et archivé. L'ATR n'a pas muté ($0.88 strictement identique sur trois snapshots consécutifs). La règle heuristique des apprentissages s'applique : pas de réécriture de l'analyse fondamentale sans mutation réelle des données.

**La thèse est confirmée pour les raisons suivantes :**
1. **Score Global stable dans la fourchette ACHETER (Réduit)** 60–74 à 64.0/100
2. **Configuration technique haussière de MT inchangée** — cours +9.8% au-dessus de MM50, RSI neutre favorable
3. **Sentiment dérivé haussier confirmé et validé** — options JSON réparées : max pain $20.00, put/call 0.20, call OI 83.4%
4. **Timing Favorable maintenu** — sans surachat ni survente
5. **Stabilité des données** — aucun changement significatif entre les trois derniers snapshots

**Points de vigilance qui justifient le sizing Réduit (maintenus) :**
1. **Volume encore réduit** — 0.56× moyenne 20j, la liquidité reste inférieure à la normale
2. **Consensus PT sous le spot** — $16.00 < $16.57, pas de catalyseur analyste
3. **Ratio R/R 1.5** — en-deçà du seuil institutionnel 1:2
4. **Aucune news structurante** — silence complet sur le ticker
5. **MM200 toujours manquante** — impossible de valider la tendance de long terme

**Points de vigilance :**
- Confirmation volume à la prochaine séance US — un retour >0.8× moyenne 20j est nécessaire pour valider la conviction
- Tenue du support MM50 $15.09 — cassure = retour ATTENDRE
- Earnings Q3 FY2026 (2026-08-06) — 51j, Est EPS $0.24–$0.34, Rev ~$0.1B
- Expiration options 2026-06-18 — 2j, max pain $20.00 (upside +20.7% vs spot)

**Catalyseurs forward :**
1. **Test de la résistance $17.97** (52w high) — scénario le plus probable à MT si volume se normalise
2. **Earnings Q3 FY2026 (2026-08-06)** — 51j, Est EPS $0.24–$0.34, Rev ~$0.1B
3. **Expiration options 2026-06-18** — 2j, structure max pain $20.00 (upside +20.7% vs spot)

**Risques :**
- Volume réduit — risque de mouvement non crédible ou gap-fill sans conviction
- Support MM50 $15.09 — cassure = invalidation de la thèse haussière de MT
- Consensus PT faible couverture ($16.00, 2 analysts)
- ROIC faible (3.16%)
- SBC / Revenue élevé (9.35%)
- Faible liquidité de la small-cap

**Recommandation :** **ACHETER (Sizing Réduit).**

**Entrée suggérée :** $16.57 (spot) — timing Favorable, mais attendre un retour de volume >0.8× pour confirmation.
**Stop-loss :** $14.81 (base ATR $0.88, −10.6%) — ajustable si ATR évolue.
**Take-profit :** $19.21 (base ATR $0.88, +15.9%).
**Sizing :** Réduit — le ratio R/R 1.5 est en-deçà du seuil institutionnel 1:2, et le volume réduit limite la conviction.

**Déteneurs :** maintenir la position avec le SL strict à $14.81. Surveiller le retour du volume et la tenue du support MM50 $15.09. Sur cassure de $15.09, envisager une réduction de position.

**Non-déteneurs :** entrée possible à $16.57 avec sizing Réduit, mais préférer attendre un snapshot avec volume >0.8× moyenne 20j pour confirmer la conviction.

---

*Révision post-pipeline 13:00 UTC — Données : `data/latest.json` (2026-06-16T13:00:14Z), `data/recommandations_2026-06-16.json` (ACHETER Réduit, 64.0/100, C:5.0 V:6.0 M:7.0), `data/quant_2026-05-17.json` (insuffisant), `data/geo_risk_2026-05-17.json` (pas de données MITK), `data/sector_rotation_2026-06-16.json` (signal NEUTRAL, XLK top rank momentum 10.0), `data/fx_exposure_2026-06-16.json` (impact 0.0), `data/social_sentiment_2026-06-16.json` (pas de données), `data/upcoming_events_2026-06-16.json` (earnings 2026-08-06), `data/events_2026-06-16.json` (0 événement), `data/validation_report.txt` (0 erreur/warning MITK) — Date : 2026-06-16*
