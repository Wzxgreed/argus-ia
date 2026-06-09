# MITK — Mise à Jour Snapshot 21:00 UTC (2026-06-09)

> **Source :** `data/latest.json` (snapshot 2026-06-09 21:00 UTC) + agents quant, geo, sector, social, FX, events, recommandation
> **Référence précédente :** [MITK_2026-06-09_update.md](MITK_2026-06-09_update.md) (snapshot 13:00 UTC 2026-06-09)
> **Desk :** Argus-IA | Pipeline : 21:00 UTC | Score Global Ajusté : **64.0/100** | Action : **ACHETER (Sizing Réduit)**

---

## Résumé des Changements depuis le Snapshot 13:00 UTC

| Indicateur | 2026-06-09 13:00 UTC | 2026-06-09 21:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| **Cours close** | **$15.40** | **$15.49** | **+0.58%** |
| Open session | $14.94 | **$15.40** | Session US ouverte |
| High du jour | $15.54 | **$15.96** | **+$0.42 (+2.7%)** |
| Low du jour | $14.73 | **$14.50** | **−$0.23 (−1.6%)** |
| **RSI 14j** | **58.01** | **58.37** | **+0.36 pt** |
| **ATR 14j** | **$0.91** | **$0.98** | **+$0.07 (+7.7%)** |
| **MM 50j** | **$14.82** | **$14.87** | **+$0.05** |
| **Volume du jour** | **1,020,200** (0.82×) | **1,481,772** (**1.24×**) | **+45.2%** |
| **Score Global Ajusté** | **65.2/100** | **64.0/100** | **−1.2 pt** |
| **Recommandation agent** | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | **Confirmée** |
| **Score Catalyseur** | 5.0/10 | **5.0/10** | Inchangé |
| **Score Valorisation** | 6.0/10 | **6.0/10** | Inchangé |
| **Score Momentum** | 7.5/10 | **7.0/10** | **−0.5 pt** |
| **Max Pain** | $20.00 | **$20.00** | Inchangé |
| **Put/Call ratio** | 0.22 | **0.22** | Inchangé |
| **Call OI %** | 81.7% | **81.7%** | Inchangé |

**Lecture institutionnelle :** Le snapshot 21:00 UTC du 9 juin capture la **première session US réelle** depuis le snapshot 13h. Le cours clôture à $15.49 (+0.58% vs previous close, +0.6% vs 13h) après un range intraday étendu de $14.50 à $15.96 (10.1%). Le volume a bondi de 45% pour atteindre 1.24× la moyenne 20j, confirmant la liquidité crédible. **La baisse du Score Momentum (−0.5 pt à 7.0/10) et du Score Global Ajusté (−1.2 pt à 64.0/100)** reflètent le rejet du high ($15.96) et la fermeture sous le milieu du range, malgré le gain nominal. Le DRAFT_refresh généré par `detect_major_events` (trigger ATR_SPIKE 6.33%) est un **faux positif algorithmique** — il capture la volatilité intraday normale de la session US, pas un événement structurel. La thèse ACHETER (Sizing Réduit) reste validée avec vigilance accrue sur la volatilité.

---

## 1. Mise à Jour Technique

| Indicateur | Valeur 21:00 UTC | Δ vs 13:00 UTC | Lecture |
|---|---|---|---|
| **Cours close** | **$15.49** | +0.58% | Gain modeste, clôture sous le milieu du range |
| **Open / High / Low** | 15.40 / 15.96 / 14.50 | — | Range $1.46 (10.1%) — volatilité élevée |
| **Change % vs prev close** | +0.58% | Nouveau | Rebond +3.43% du 8 juin partiellement préservé |
| **RSI (14j)** | **58.37** | +0.36 pt | Neutre favorable, stabilisation sous 60 |
| **ATR (14j)** | **$0.98** | +$0.07 (+7.7%) | Volatilité en hausse — range intraday étendu |
| **MM 50j** | **$14.87** | +$0.05 | **Cours AU-DESSUS de MM50 (+4.2%)** — marge maintenue |
| **Volume** | **1,481,772** | +45.2% | **1.24× moyenne 20j** — liquidité confirmée, session réelle |
| **Beta** | **1.007** | Inchangé | Légèrement au-dessus du marché |

**Niveaux clés (révisés, ATR $0.98) :**
- Support immédiat : $14.50 (low du jour)
- Support intermédiaire : $14.50 (zone psychologique)
- Support structurel : $14.34 (ancien breakout 25/05)
- Support MM50 : $14.87 (cours +4.2% au-dessus)
- Résistance immédiate : $15.96 (high du jour) — **rejet net**
- Résistance structurelle : $16.00 (consensus PT)
- Résistance majeure : $17.97 (52w high)
- Stop-loss ATR (2×) : **$13.53** (−12.6%)
- Take-profit ATR (3×) : **$18.43** (+19.0%)
- Ratio R/R : **1.5**

**Verdict timing :** **Favorable avec vigilance.** La session US a confirmé la liquidité (1.24× moyenne) mais a révélé une volatilité intraday élevée (range 10.1%). Le rejet du high $15.96 (test du consensus PT $16.00) et la clôture à $15.49 (sous le milieu du range) suggèrent une prise de profit à la résistance. Le cours reste nettement au-dessus de MM50 (+4.2%) et le RSI à 58.37 évite le surachat. L'ATR remonté à $0.98 élargit les stops et réduit le ratio R/R à 1.5.

---

## 2. Mise à Jour Fondamentale

| Métrique | Valeur 21:00 UTC | Source | Δ vs 13:00 UTC |
|----------|-------------------|--------|-----------------|
| Market Cap | $699.5M (Yahoo) / $446.6M (FMP) | Yahoo + FMP | +$4.1M Yahoo |
| P/E (TTM) | 45.56x (Yahoo) / 50.78x (FMP) | Yahoo + FMP | Inchangé |
| Forward P/E | 12.76x | Yahoo Finance | +0.07x |
| EV/EBITDA | 16.07x (Yahoo) / 12.15x (FMP) | Yahoo + FMP | Inchangé |
| P/B | 2.90x (Yahoo) / 1.86x (FMP) | Yahoo + FMP | Inchangé |
| Gross Margin | 85.1% | FMP | — |
| Operating Margin | 9.3% | FMP | — |
| Net Margin | 4.9% | FMP | — |
| ROIC | 3.16% | FMP key metrics | — |
| FCF Yield | 12.1% | FMP | — |

**Filtre Qualité :** 3–4 / 6 — **Quality Partielle** (inchangé). Aucun changement fondamental entre les snapshots. Le snapshot 21h UTC du 9 juin n'intègre aucune nouvelle donnée fondamentale (pas de filing, pas de guidance, pas de revision d'estimates).

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur 21:00 UTC | Δ vs 13:00 UTC | Lecture |
|---|---|---|---|
| Consensus PT | $16.00 (2 analysts) | Inchangé | Spot sous PT, upside +3.3% |
| **Max Pain** | **$20.00** | Inchangé | +29.1% vs spot — structure haussière stable |
| **Put/Call ratio** | **0.22** | Inchangé | Extrêmement haussier — domination call confirmée |
| **Call OI %** | **81.7%** | Inchangé | Domination call massive — inchangée |
| Short Interest | 8.31% | Inchangé | Modéré |
| Social Sentiment | 0 / No data | Inchangé | Sous le radar retail |
| Upgrades/Downgrades | Aucun | Inchangé | Silence analystes |
| News structurantes | Aucune | Inchangé | 0 news MITK |
| Événements corporate | Aucun | Inchangé | 0 événement MITK |

**Verdict Sentiment :** Neutre à légèrement haussier. Aucune mutation du sentiment entre 13h et 21h UTC. La structure options reste haussière avec un put/call 0.22 très bas et une domination call à 81.7%. Le test du consensus PT $16.00 ($15.96 high) et le rejet immédiat suggèrent que ce niveau agit comme résistance technique ET sentimentale. Aucun flux de news, aucun insider trade, aucun upgrade/downgrade. MITK reste sous le radar institutionnel et retail.

---

## 4. Scoring Global — Confirmé, Volatilité en Hausse

| Pilier | Valeur 13:00 UTC | Valeur 21:00 UTC | Poids | Pondéré |
|---|---|---|---|---|
| **Catalyseur** | 5.0/10 | **5.0/10** | 35% | 1.750 |
| **Valorisation** | 6.0/10 | **6.0/10** | 40% | 2.400 |
| **Momentum** | 7.5/10 | **7.0/10** | 25% | 1.750 |
| **Score Opportunité** | **6.0/10** | **5.9/10** | — | — |
| **Score Global Ajusté** | **65.2/100** | **64.0/100** | — | — |

| Seuil | Action | Sizing |
|---|---|---|
| Score Global 64.0/100 | **ACHETER** | **Réduit** |

**Baisse technique du score.** Le snapshot 21:00 UTC du 9 juin enregistre une légère dégradation du Score Global Ajusté de 65.2 à 64.0/100 (−1.2 pt), entraînée par la baisse du Score Momentum de 7.5 à 7.0/10 (−0.5 pt). Cette révision reflète le rejet du high à $15.96 et la fermeture sous le milieu du range intraday, plutôt que la performance absolue (+0.58%). Le Score Opportunité passe de 6.0 à 5.9/10 (−0.1 pt), inchangé dans la fourchette ACHETER Réduit (60–74).

**Risques additionnels (inchangés) :**
- Geo risk : Pas de données spécifiques MITK dans `geo_risk_latest.json` (2026-05-17)
- FX impact : 0.0 — exposition USD, pas de divergence, flag 🟢
- Social sentiment : 0/10 — pas de signal retail
- Events corporate : aucun
- Sector rotation : `NEUTRAL` — XLK top rank (momentum 10.0)
- Quant significance : Insuffisant (0 signaux historiques, p-value 1.0)

---

## 5. Révision des Niveaux SL / TP

| Niveau | Valeur | Δ vs 13:00 UTC |
|---|---|---|
| **Stop-loss** | **$13.53** | −$0.05 |
| **Take-profit** | **$18.43** | +$0.30 |
| **Ratio R/R** | **1.5** | Inchangé |

**Révision liée à l'ATR remonté.** L'ATR passe de $0.91 à $0.98 (+7.7%), ce qui élargit la fourchette SL/TP. Le SL descend à $13.53 (−12.6%) et le TP remonte à $18.43 (+19.0%). Le ratio R/R reste à 1.5, en-deçà du seuil institutionnel 1:2. Cette extension des stops est le reflet direct de la volatilité intraday observée ($14.50–$15.96).

---

## 6. Calendrier & Événements

| Événement | Date | Jours restants |
|---|---|---|
| **Earnings Q3 FY2026** | 2026-08-06 | **58** |
| **Expiration options** | 2026-06-18 | **9** |

**Alertes actives (révisées) :**
- 🟢 **[SESSION US CONFIRMÉE]** Volume 1,481,772 = 1.24× moyenne 20j — liquidité réelle validée — 2026-06-09
- 🟢 **[CASSURE MM50 CONFIRMÉE — MARGE CONFORTABLE]** Cours $15.49 > MM50 $14.87 (+4.2%) — marge maintenue — 2026-06-09
- 🟡 **[RSI STABLE SOUS 60]** 58.37 — zone neutre favorable, pas de surachat — 2026-06-09
- 🟡 **[VOLATILITÉ INTRADAY ÉLEVÉE]** Range $14.50–$15.96 (10.1%), ATR +7.7% — prudence sur les stops — 2026-06-09
- 🟡 **[REJET DU HIGH $15.96]** Test du consensus PT $16.00 suivi d'un rejet — résistance technique active — 2026-06-09
- 🟢 **[CONSENSUS PT SOUS LE SPOT]** $16.00 > $15.49 — upside théorique de +3.3% — 2026-06-09
- 🟢 **[STRUCTURE OPTIONS HAUSSIÈRE CONFIRMÉE]** Max Pain $20.00, Put/Call 0.22, Call OI 81.7% — signal dérivé haussier stable — 2026-06-09
- 🟡 **[DRAFT_refresh FAUX POSITIF]** Trigger ATR_SPIKE 6.33% généré par `detect_major_events` — session US normale, pas d'événement structurel — à archiver — 2026-06-09
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital — 2026-05-18
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($699.5M Yahoo vs $446.6M FMP), P/E, EV multiples — persistant
- 🟡 **[LIQUIDITÉ DÉRIVÉE FAIBLE]** Faible couverture strike — prudence sur le hedging — 2026-06-08
- 🟡 **[BETA LÉGÈREMENT SUPÉRIEUR AU MARCHÉ]** 1.007 — sensibilité marché accrue — 2026-06-08
- 🔴 **[PULLBACK −15.3% SANS CATALYSEUR IDENTIFIABLE]** Risque de continuation baissière si support MM50 cède — 2026-06-08

---

## 7. Conclusion — Thèse CONFIRMÉE avec vigilance : ACHETER (Sizing Réduit)

**Verdict : THÈSE CONFIRMÉE.** Snapshot 21:00 UTC 2026-06-09 : la session US a validé la liquidité (volume 1.24×) mais a révélé une volatilité intraday élevée (range 10.1%). Le cours clôture à $15.49 (+0.58%) après un test du consensus PT $16.00 ($15.96 high) et un rejet immédiat. **Le Score Global Ajusté recule légèrement de 65.2 à 64.0/100** (−1.2 pt) du fait de la baisse du Momentum de 7.5 à 7.0/10, probablement liée au rejet du high et à la performance relative sectorielle. La thèse ACHETER (Sizing Réduit) reste dans la fourchette 60–74. Action **ACHETER (Sizing Réduit)** confirmée, timing **Favorable avec vigilance**.

**Le DRAFT_refresh MITK_2026-06-09_DRAFT_refresh.md est un FAUX POSITIF algorithmique.** Le trigger ATR_SPIKE 6.33% a été généré par `agents/detect_major_events/agent.py` lors de la session US normale. Il n'y a aucun événement structurel (news, guidance, M&A, filing) sous-jacent. Le snapshot 21h UTC confirme l'absence de mutation fondamentale.

**La thèse reste inchangée pour les raisons suivantes :**
1. **Session US réelle confirmée** — volume 1.24× moyenne, liquidité crédible
2. **Cours au-dessus de MM50 avec marge confortable** — $15.49 vs $14.87 (+4.2%)
3. **RSI stable dans la zone neutre favorable** — 58.37, pas de surachat
4. **Structure options haussière stable** — max pain $20.00, put/call 0.22, call OI 81.7%
5. **Valorisation inchangée** — Forward P/E 12.76x, spot sous consensus PT $16.00
6. **Aucune news négative** — le gap −6.47% du matin du 8 juin reste sans catalyseur identifié
7. **Score Global Ajusté stable** — 64.0/100, dans la fourchette ACHETER Réduit (60–74)

**Points de vigilance nouveaux :**
- **Rejet du high $15.96** — résistance technique à $16.00 confirmée, prise de profit active
- **Volatilité intraday élevée** — range 10.1%, ATR +7.7% — stops élargis à $13.53
- **Ratio R/R 1.5** — en-deçà du seuil institutionnel 1:2
- **Score Momentum révisé à la baisse** — 7.0/10 vs 7.5/10 précédemment

**Catalyseurs forward :**
1. **Test de la résistance $16.00** — scénario le plus probable à court terme si volume se maintient >1.0×
2. **Earnings Q3 FY2026 (2026-08-06)** — 58j, Est EPS $0.24–$0.34, Rev ~$0.1B
3. **Expiration options 2026-06-18** — 9j, max pain $20.00 (loin au-dessus du spot, favorable aux détenteurs de calls)

**Risques :**
- Support MM50 $14.87 — cassure = invalidation de la thèse haussière de moyen terme
- Volatilité intraday élevée — risque de stop hunt sur un gap overnight
- Pullback −15.3% sans catalyseur identifiable — risque de continuation baissière si marché tech faible
- Consensus PT faible couverture ($16.00, 2 analysts)
- ROIC faible (3.16%)
- SBC / Revenue élevé (9.35%)
- Faible liquidité de la small-cap
- Ratio R/R 1.5 — en-deçà du seuil institutionnel 1:2

**Recommandation :** **ACHETER (Sizing Réduit).**

**Entrée suggérée :** $15.49 (spot actuel) à $15.20. **Ne pas chasser** au-dessus de $15.70.
**Stop-loss :** $13.53 (−12.6%).
**Take-profit :** $18.43 (+19.0%).
**Sizing :** Réduit — max 3–5% du capital.

**Déteneurs :** maintenir, le SL à $13.53 protège le capital. Surveiller la tenue du support MM50 $14.87 et le volume à l'ouverture des prochaines séances.

**Non-déteneurs :** entrée possible à ces niveaux avec sizing réduit et SL strict. Attendre un test de $15.20–$15.30 pour une entrée optimale. Éviter d'entrer au-dessus de $15.70 en raison du rejet récent à $15.96.

---

*Révision post-pipeline 21:00 UTC — Données : `data/latest.json` (2026-06-09T21:00:12Z), `data/recommandations_2026-06-09.json` (ACHETER Réduit, 64.0/100, C:5.0 V:6.0 M:7.0), `data/quant_2026-05-17.json` (insuffisant), `data/geo_risk_2026-05-17.json` (pas de données MITK), `data/sector_rotation_2026-06-09.json` (signal NEUTRAL, XLK top rank momentum 10.0), `data/fx_exposure_2026-06-09.json` (impact 0.0), `data/social_sentiment_2026-06-09.json` (pas de données), `data/upcoming_events_2026-06-09.json` (earnings 2026-08-06), `data/events_2026-06-09.json` (0 événement), `data/news_2026-06-09.json` (0 news) — Date : 2026-06-09*
