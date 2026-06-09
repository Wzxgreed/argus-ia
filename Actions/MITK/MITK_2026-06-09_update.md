# MITK — Mise à Jour Snapshot 13:00 UTC (2026-06-09)

> **Source :** `data/latest.json` (snapshot 2026-06-09 13:00 UTC) + agents quant, geo, sector, social, FX, events, recommandation
> **Référence précédente :** [MITK_2026-06-09_update.md](MITK_2026-06-09_update.md) (snapshot 10:00 UTC 2026-06-09)
> **Desk :** Argus-IA | Pipeline : 13:00 UTC | Score Global Ajusté : **65.2/100** | Action : **ACHETER (Sizing Réduit)**

---

## Résumé des Changements depuis le Snapshot 10:00 UTC

| Indicateur | 2026-06-09 10:00 UTC | 2026-06-09 13:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| **Cours close** | **$15.40** | **$15.40** | **0.00%** |
| Open session | $14.94 | **$14.94** | Inchangé |
| High du jour | $15.54 | **$15.54** | Inchangé |
| Low du jour | $14.73 | **$14.73** | Inchangé |
| **RSI 14j** | **58.01** | **58.01** | **Inchangé** |
| **ATR 14j** | **$0.91** | **$0.91** | **Inchangé** |
| **MM 50j** | **$14.82** | **$14.82** | **Inchangé** |
| **Volume du jour** | **1,020,200** vs 1,240,110 avg (0.82×) | **1,020,200** vs 1,240,110 avg (**0.82×**) | **Inchangé** |
| **Score Global Ajusté** | **65.2/100** | **65.2/100** | **Inchangé** |
| **Recommandation agent** | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | **Confirmée** |
| **Score Catalyseur** | 5.0/10 | **5.0/10** | Inchangé |
| **Score Valorisation** | 6.0/10 | **6.0/10** | Inchangé |
| **Score Momentum** | 7.5/10 | **7.5/10** | Inchangé |
| **Max Pain** | $2.50 (JSON) / $20.00 (opérationnel) | **$20.00** | **Anomalie JSON RÉSOLUE** |
| **Put/Call ratio** | null (JSON) / 0.23 (opérationnel) | **0.22** | **Anomalie JSON RÉSOLUE** |
| **Call OI %** | null (JSON) / 81.5% (opérationnel) | **81.7%** | **Anomalie JSON RÉSOLUE** |

**Lecture institutionnelle :** Le snapshot 13:00 UTC du 9 juin présente une **stabilité totale** des données de prix, volume et technique par rapport au snapshot 10:00 UTC. La donnée majeure de cette mise à jour est la **résolution définitive de l'anomalie options JSON récurrente** : pour la première fois depuis le 3 juin 2026, le champ `options` de `latest.json` retourne des valeurs cohérentes et valides — Max Pain $20.00, Put/Call 0.22, Call OI 81.7%. Ces valeurs confirment la structure options haussière déjà documentée manuellement et invalident les lectures aberrantes ($2.50, null, null) des trois snapshots précédents (03/06, 08/06, 10/06). **La thèse ACHETER (Sizing Réduit) est totalement confirmée et inchangée.**

---

## 1. Mise à Jour Technique

| Indicateur | Valeur 13:00 UTC | Δ vs 10:00 UTC | Lecture |
|---|---|---|---|
| **Cours close** | **$15.40** | 0.00% | Stabilité pré-ouverture / session US non ouverte |
| **Open / High / Low** | 14.94 / 15.54 / 14.73 | — | Range intraday $0.81 (5.3%) — session 08/06 |
| **Change % vs prev close** | +3.43% | Inchangé | Rebond +3.43% vs 08/06 ($14.89) confirmé |
| **RSI (14j)** | **58.01** | Inchangé | Neutre favorable, stabilisation sous 60 |
| **ATR (14j)** | **$0.91** | Inchangé | Volatilité stabilisée post-gap |
| **MM 50j** | **$14.82** | Inchangé | **Cours AU-DESSUS de MM50 (+3.9%)** — marge confortable |
| **Volume** | **1,020,200** | Inchangé | **0.82× moyenne 20j** — liquidité normalisée confirmée |
| **Beta** | **1.007** | Inchangé | Légèrement au-dessus du marché |

**Niveaux clés (inchangés, ATR $0.91) :**
- Support immédiat : $14.73 (low 08/06)
- Support intermédiaire : $14.50 (zone psychologique)
- Support structurel : $14.34 (ancien breakout 25/05)
- Support MM50 : $14.82 (cours +3.9% au-dessus)
- Résistance immédiate : $15.54 (high 08/06)
- Résistance structurelle : $16.00 (consensus PT)
- Résistance majeure : $17.97 (52w high)
- Stop-loss ATR (2×) : **$13.58** (−11.8%)
- Take-profit ATR (3×) : **$18.13** (+17.7%)
- Ratio R/R : **1.5**

**Verdict timing :** **Favorable.** Aucune mutation technique entre le snapshot 10:00 UTC et le snapshot 13:00 UTC du 9 juin. Le cours se maintient nettement au-dessus de MM50 (+3.9%) avec un volume normalisé (0.82×). Le RSI à 58.01 reste dans la zone neutre favorable sans approcher le surachat. En l'absence d'ouverture du marché US entre les deux snapshots, la configuration technique reste identique à celle validée au snapshot 10h.

---

## 2. Mise à Jour Fondamentale

| Métrique | Valeur 13:00 UTC | Source | Δ vs 10:00 UTC |
|----------|-------------------|--------|-----------------|
| Market Cap | $695.4M (Yahoo) / $446.6M (FMP) | Yahoo + FMP | Inchangé |
| P/E (TTM) | 45.29x (Yahoo) / 50.78x (FMP) | Yahoo + FMP | Inchangé |
| Forward P/E | 12.69x | Yahoo Finance | Inchangé |
| EV/EBITDA | 16.07x (Yahoo) / 12.15x (FMP) | Yahoo + FMP | Inchangé |
| P/B | 2.88x (Yahoo) / 1.86x (FMP) | Yahoo + FMP | Inchangé |
| Gross Margin | 85.1% | FMP | — |
| Operating Margin | 9.3% | FMP | — |
| Net Margin | 4.9% | FMP | — |
| ROIC | 3.16% | FMP key metrics | — |
| FCF Yield | 12.1% | FMP | — |

**Filtre Qualité :** 3–4 / 6 — **Quality Partielle** (inchangé). Aucun changement fondamental entre les snapshots. Le snapshot 13h UTC du 9 juin n'intègre aucune nouvelle donnée fondamentale (pas de filing, pas de guidance, pas de revision d'estimates).

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur 13:00 UTC | Δ vs 10:00 UTC | Lecture |
|---|---|---|---|
| Consensus PT | $16.00 (2 analysts) | Inchangé | Spot sous PT, upside +3.9% |
| **Max Pain** | **$20.00** | Anomalie RÉSOLUE | +29.9% vs spot — structure haussière validée par JSON |
| **Put/Call ratio** | **0.22** | Anomalie RÉSOLUE | Extrêmement haussier — domination call confirmée |
| **Call OI %** | **81.7%** | Anomalie RÉSOLUE | Domination call massive — légèrement supérieure au 10h (81.5%) |
| Short Interest | 8.31% | Inchangé | Modéré |
| Social Sentiment | 0 / No data | Inchangé | Sous le radar retail |
| Upgrades/Downgrades | Aucun | Inchangé | Silence analystes |
| News structurantes | Aucune | Inchangé | 0 news MITK |
| Événements corporate | Aucun | Inchangé | 0 événement MITK |

**Verdict Sentiment :** Neutre à légèrement haussier. **Anomalie options JSON résolue** — les valeurs retournées par `latest.json` sont désormais cohérentes avec les données opérationnelles historiques. La structure options reste haussière avec un put/call 0.22 très bas et une domination call à 81.7%. Aucun flux de news, aucun insider trade, aucun upgrade/downgrade. MITK reste sous le radar institutionnel et retail.

---

## 4. Scoring Global — Confirmé, Anomalie Options Résolue

| Pilier | Valeur 10:00 UTC | Valeur 13:00 UTC | Poids | Pondéré |
|---|---|---|---|---|
| **Catalyseur** | 5.0/10 | **5.0/10** | 35% | 1.750 |
| **Valorisation** | 6.0/10 | **6.0/10** | 40% | 2.400 |
| **Momentum** | 7.5/10 | **7.5/10** | 25% | 1.875 |
| **Score Opportunité** | **6.0/10** | **6.0/10** | — | — |
| **Score Global Ajusté** | **65.2/100** | **65.2/100** | — | — |

| Seuil | Action | Sizing |
|---|---|---|
| Score Global 65.2/100 | **ACHETER** | **Réduit** |

**Stabilité totale confirmée.** Le snapshot 13:00 UTC du 9 juin valide la structure du score établie au snapshot 10:00 UTC : Catalyseur 5.0/10, Valorisation 6.0/10, Momentum 7.5/10. Le Score Opportunité reste à 6.0/10. Aucun ajustement de scoring n'est justifié.

**Risques additionnels (inchangés) :**
- Geo risk : Pas de données spécifiques MITK dans `geo_risk_latest.json` (2026-05-17)
- FX impact : 0.0 — exposition USD, pas de divergence, flag 🟢
- Social sentiment : 0/10 — pas de signal retail
- Events corporate : aucun
- Sector rotation : `NEUTRAL` — XLK top rank (momentum 10.0)
- Quant significance : Insuffisant (0 signaux historiques, p-value 1.0)

---

## 5. Révision des Niveaux SL / TP

| Niveau | Valeur | Δ vs 10:00 UTC |
|---|---|---|
| **Stop-loss** | **$13.58** | Inchangé |
| **Take-profit** | **$18.13** | Inchangé |
| **Ratio R/R** | **1.5** | Inchangé |

Aucune révision nécessaire — les données sont strictement identiques au snapshot précédent. L'ATR reste à $0.91. Le ratio R/R reste à 1.5, en-deçà du seuil institutionnel 1:2.

---

## 6. Calendrier & Événements

| Événement | Date | Jours restants |
|---|---|---|
| **Earnings Q3 FY2026** | 2026-08-06 | **58** |
| **Expiration options** | 2026-06-18 | **9** |

**Alertes actives (révisées) :**
- 🟢 **[ANOMALIE OPTIONS JSON RÉSOLUE]** Max pain $20.00, put/call 0.22, call OI 81.7% — données JSON corrigées dans latest.json (13h UTC) — 2026-06-09
- 🟢 **[STABILITÉ TOTALE]** Aucune mutation technique, fondamentale ou sentimentale entre 10h UTC et 13h UTC 09/06 — 2026-06-09
- 🟢 **[CASSURE MM50 CONFIRMÉE — MARGE CONFORTABLE]** Cours $15.40 > MM50 $14.82 (+3.9%) — marge maintenue — 2026-06-08
- 🟢 **[VOLUME NORMALISÉ]** 1,020,200 = 0.82× moyenne 20j — liquidité crédible confirmée — 2026-06-09
- 🟡 **[RSI STABLE SOUS 60]** 58.01 — zone neutre favorable, pas de surachat — 2026-06-09
- 🟢 **[CONSENSUS PT SOUS LE SPOT]** $16.00 > $15.40 — upside théorique de +3.9% — 2026-06-09
- 🟢 **[STRUCTURE OPTIONS HAUSSIÈRE CONFIRMÉE]** Max Pain $20.00, Put/Call 0.22, Call OI 81.7% — signal dérivé haussier stable (données JSON validées) — 2026-06-09
- 🟡 **[DRAFT_refresh FAUX POSITIF]** Trigger ATR_SPIKE 5.91% généré par `detect_major_events` — aucune mutation réelle des données — à archiver — 2026-06-09
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital — 2026-05-18
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($695.4M Yahoo vs $446.6M FMP), P/E, EV multiples — persistant
- 🟡 **[LIQUIDITÉ DÉRIVÉE FAIBLE]** Faible couverture strike — prudence sur le hedging — 2026-06-08
- 🟡 **[BETA LÉGÈREMENT SUPÉRIEUR AU MARCHÉ]** 1.007 — sensibilité marché accrue — 2026-06-08
- 🔴 **[PULLBACK −15.3% SANS CATALYSEUR IDENTIFIABLE]** Risque de continuation baissière si support MM50 cède — 2026-06-08

---

## 7. Conclusion — Thèse CONFIRMÉE : ACHETER (Sizing Réduit)

**Verdict : THÈSE CONFIRMÉE.** Snapshot 13:00 UTC 2026-06-09 : **stabilité totale** vs snapshot 10:00 UTC 2026-06-09. Tous les indicateurs sont identiques à la virgule près (cours $15.40, RSI 58.01, ATR $0.91, MM50 $14.82, volume 0.82×). **Anomalie options JSON résolue** — les données JSON retournent désormais des valeurs cohérentes (max pain $20.00, put/call 0.22, call OI 81.7%) qui confirment la structure haussière déjà documentée manuellement. Score Opportunité inchangé 6.0/10 (C:5.0 V:6.0 M:7.5). Score Global Ajusté **65.2/100** inchangé. Action **ACHETER (Sizing Réduit)** confirmée, timing **Favorable**.

**Le DRAFT_refresh MITK_2026-06-09_DRAFT_refresh.md est un FAUX POSITIF algorithmique.** Le trigger ATR_SPIKE 5.91% a été généré par `agents/detect_major_events/agent.py` sans mutation réelle des données sous-jacentes. Le snapshot 13h UTC du 9 juin confirme l'absence totale de changement et valide la conclusion du snapshot 10h.

**La thèse reste inchangée pour les raisons suivantes :**
1. **Anomalie options JSON résolue** — données JSON corrigées, structure haussière validée algorithmiquement
2. **Stabilité totale des données** — aucun changement de cours, RSI, volume, ATR, MM50 entre 10h et 13h UTC
3. **Volume normalisé confirmé** — 0.82× moyenne 20j valide le rebond du 8 juin
4. **Cours au-dessus de MM50 avec marge confortable** — $15.40 vs $14.82 (+3.9%)
5. **RSI stable dans la zone neutre favorable** — 58.01, pas de surachat
6. **Structure options haussière stable** — max pain $20.00, put/call 0.22, call OI 81.7%
7. **Valorisation inchangée** — Forward P/E 12.69x, spot sous consensus PT $16.00
8. **Aucune news négative** — le gap −6.47% du matin du 8 juin reste sans catalyseur identifié
9. **Score Global Ajusté stable** — 65.2/100, dans la fourchette ACHETER Réduit (60–74)

**Points de vigilance :**
- Ratio R/R 1.5 — en-deçà du seuil institutionnel 1:2
- Consensus PT faible couverture ($16.00, 2 analysts)
- ROIC faible (3.16%)
- SBC / Revenue élevé (9.35%)
- Faible liquidité de la small-cap
- DRAFT_refresh faux positif — le mécanisme de détection d'événements majeurs doit être calibré pour éviter les triggers sur des snapshots pré-ouverture

**Catalyseurs forward :**
1. **Rebond technique vers $16.00–$16.50** — scénario le plus probable à court terme si volume se maintient >0.8×
2. **Earnings Q3 FY2026 (2026-08-06)** — 58j, Est EPS $0.24–$0.34, Rev ~$0.1B
3. **Expiration options 2026-06-18** — 9j, max pain $20.00 (loin au-dessus du spot, favorable aux détenteurs de calls)

**Risques :**
- Support MM50 $14.82 — cassure = invalidation de la thèse haussière de moyen terme
- Pullback −15.3% sans catalyseur identifiable — risque de continuation baissière si marché tech faible
- Consensus PT faible couverture ($16.00, 2 analysts)
- ROIC faible (3.16%)
- SBC / Revenue élevé (9.35%)
- Faible liquidité de la small-cap
- Ratio R/R 1.5 — en-deçà du seuil institutionnel 1:2

**Recommandation :** **ACHETER (Sizing Réduit).**

**Entrée suggérée :** $15.40 (spot actuel) à $15.20. **Ne pas chasser** au-dessus de $15.70.
**Stop-loss :** $13.58 (−11.8%).
**Take-profit :** $18.13 (+17.7%).
**Sizing :** Réduit — max 3–5% du capital.

**Déteneurs :** maintenir, le SL à $13.58 protège le capital. Surveiller l'ouverture du marché US ce jour pour confirmation de la tenue du support MM50.

**Non-déteneurs :** entrée possible à ces niveaux avec sizing réduit et SL strict. Attendre un volume >0.8× moyenne pour confirmation (condition remplie sur la session du 8 juin).

---

*Révision post-pipeline 13:00 UTC — Données : `data/latest.json` (2026-06-09T13:00:12Z), `data/recommandations_2026-06-09.json` (ACHETER Réduit, 65.2/100, C:5.0 V:6.0 M:7.5), `data/quant_2026-05-17.json` (insuffisant), `data/geo_risk_2026-05-17.json` (pas de données MITK), `data/sector_rotation_2026-06-09.json` (signal NEUTRAL, XLK top rank momentum 10.0), `data/fx_exposure_2026-06-09.json` (impact 0.0), `data/social_sentiment_2026-06-09.json` (pas de données), `data/upcoming_events_2026-06-09.json` (earnings 2026-08-06), `data/events_2026-06-09.json` (0 événement), `data/news_2026-06-09.json` (0 news) — Date : 2026-06-09*
