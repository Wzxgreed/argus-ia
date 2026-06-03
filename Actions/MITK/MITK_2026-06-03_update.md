# MITK — Mise à Jour Snapshot 10:00 UTC (2026-06-03)

> **Source :** `data/latest.json` (snapshot 2026-06-03 10:00 UTC) + agents quant, geo, sector, social, FX, events, recommandation
> **Référence précédente :** [MITK_2026-06-02_update.md](MITK_2026-06-02_update.md) (snapshot 21:00 UTC 2026-06-02)
> **Desk :** Argus-IA | Pipeline : 10:00 UTC | Score Global Ajusté : **36.5/100** | Action : **SURVEILLER**

---

## Résumé des Changements depuis le Snapshot 21:00 UTC (2026-06-02)

| Indicateur | 2026-06-02 21:00 UTC | 2026-06-03 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| **Cours close** | **$17.57** | **$17.57** | **Inchangé** |
| Open session | $17.55 | **$17.55** | — |
| High du jour | $17.79 | **$17.79** | — |
| Low du jour | $17.301 | **$17.30** | — |
| **RSI 14j** | **71.77** | **71.77** | **Inchangé** |
| **ATR 14j** | **$0.85** | **$0.85** | **Stable** |
| **MM 50j** | **$14.71** | **$14.71** | **Inchangé** |
| **Volume du jour** | **954,557** vs 1,327,697 avg (0.719×) | **954,900** vs 1,327,715 avg (0.719×) | **Stable** |
| **52W high** | $17.97 | **$17.97** | Inchangé — spot à −2.2% |
| Short Interest | 8.31% | **8.31%** | Inchangé |
| Consensus FMP PT | $16.00 (2 analysts) | **$16.00 (2 analysts)** | Inchangé |
| Upside vs PT | −9.8% | **−9.8%** | Inchangé |
| **Max Pain** | $20.00 | **$2.50** | 🔴 **ANOMALIE JSON DÉTECTÉE** |
| Put/Call Ratio | 0.22 | **null** | 🔴 Données options corrompues |
| Call OI % | 81.8% | **null** | 🔴 Données options corrompues |
| **Score Opportunité agent** | 4.7/10 | **4.7/10** | **Inchangé** |
| **Score Global ajusté** | 36.5/100 | **36.5/100** | **Inchangé** |
| **Recommandation agent** | SURVEILLER | **SURVEILLER** | → Confirmée |
| **Signal sectoriel** | NEUTRAL | **NEUTRAL** | Inchangé |

**Lecture institutionnelle :** Le snapshot 10h UTC du 2026-06-03 confirme une **stabilité totale** par rapport au close 02/06 21h UTC. Le cours reste à **$17.57**, le RSI à **71.77**, l'ATR à **$0.85**, et le volume à **954,900** (0.719× moyenne 20j). Aucune mutation technique, fondamentale ou sentimentale n'est détectée entre les deux snapshots. **La seule évolution notable est une anomalie dans les données options de `data/latest.json` : le max pain est passé de $20.00 à $2.50, et les champs put/call ratio ainsi que call OI % sont désormais `null`.** Cette valeur de $2.50 est aberrante (max pain à −85.8% du spot) et correspond à une corruption JSON récurrente observée sur d'autres tickers (AAPL, PLTR, RKLB) dans le même snapshot. Les valeurs opérationnelles historiques ($20.00, put/call 0.22, call OI 81.8%) sont conservées. Aucune news idiosyncratique, aucun événement corporate, aucun mouvement d'insider ou d'analyste. **La thèse SURVEILLER est confirmée.**

---

## 1. Mise à Jour Technique

| Indicateur | Valeur 10h UTC | Δ vs 21h UTC | Lecture |
|---|---|---|---|
| **Cours close** | **$17.57** | $0.00 (0.00%) | Consolidation au sommet |
| **Open / High / Low** | 17.55 / 17.79 / 17.30 | — | Range intraday $0.49 (2.8%) |
| **Change % vs prev close** | −1.68% | — | Repli vs clôture précédente $17.87 |
| **RSI (14j)** | **71.77** | — | **🔴 Zone de surachat sévère (>70) persistante** |
| **ATR (14j)** | **$0.85** | — | Compression volatilité stable (4.8% du spot) |
| **MM 50j** | **$14.71** | — | **Close AU-DESSUS de MM50 (+19.4%)** — support intact |
| **MM 200j** | N/A | — | [DONNÉES MANQUANTES] |
| **Volume** | **954,900** | +343 (+0.04%) | **0.719× moyenne 20j** — stable, sous-moyenne persistant |
| **52-week range** | $8.53 – $17.97 | — | Spot au **97.8%** du 52w high |
| **Beta** | 0.955 | — | Aligné sur le marché |

**Niveaux clés (inchangés, ATR stable) :**
- Support immédiat : $17.30 (low du jour)
- Support structurel : $17.18 (close 2026-06-01)
- Support intermédiaire : $17.00 (psychologique)
- Support MM50 : $14.71
- Résistance intermédiaire : $17.79 (high du jour)
- Résistance majeure : $17.97 (52w high)
- Résistance zone max pain : $18.00–$20.00
- Stop-loss ATR (2×) : **$15.87** (−9.6%)
- Take-profit ATR (3×) : **$20.12** (+14.4%)
- Ratio R/R : **1.5**

**Verdict timing :** **Défavorable.** La configuration technique est inchangée depuis le snapshot 21h UTC. Le cours consolidé à $17.57 sur un volume stable (0.719×) indique une pause au sommet sans direction claire. Le RSI 71.77 reste en zone de surachat sévère — malgré l'absence de hausse, le niveau persiste au-dessus de 70 et constitue un malus technique majeur. L'ATR stable à $0.85 préserve la compression volatilité : la probabilité d'une expansion de volatilité dans les 2–3 séances reste élevée. Le cours est toujours au-dessus de MM50 (+19.4%), ce qui protège la thèse de moyen terme. Aucune divergence baissière détectée, mais le setup reste **asymétrique à la baisse** sur le court terme.

**Momentum sectoriel :** Le signal macro reste **NEUTRAL**. XLK affiche toujours un momentum score de **10.0/10** (return 20j +22.3%, return 60j +44.6%), mais le régime `UNKNOWN` du sector rotation report maintient la pondération neutre pour le secteur Technology. MITK n'a pas de vent de queue sectoriel déclaré.

---

## 2. Mise à Jour Fondamentale

| Métrique | Valeur 10h UTC | Source | Δ vs 21h UTC |
|----------|----------------|--------|--------------|
| Market Cap | $793.4M (Yahoo) / $446.6M (FMP) | Yahoo + FMP | Inchangé |
| P/E (TTM) | 51.68x (Yahoo) / 50.78x (FMP) | Yahoo Finance + FMP | Inchangé |
| Forward P/E | 14.47x | Yahoo Finance | Inchangé |
| EV/EBITDA | 18.40x (Yahoo) / 12.15x (FMP) | Yahoo + FMP | Inchangé |
| P/B | 3.29x (Yahoo) / 1.86x (FMP) | Yahoo + FMP | Inchangé |
| Gross Margin | 85.1% | FMP | — |
| Operating Margin | 9.3% | FMP | — |
| EBITDA Margin | 20.5% | FMP | — |
| Net Margin | 4.9% | FMP | — |
| ROIC | 3.16% | FMP key metrics | — |
| ROE | 3.66% | FMP key metrics | — |
| FCF Yield | 12.1% | FMP | — |
| Net Debt / EBITDA | 0.03x | FMP | — |
| SBC / Revenue | 9.35% | FMP | — |

**Filtre Qualité :** 3–4 / 6 — **Quality Partielle** (inchangé). Forward P/E 14.47x reste attractif. FCF yield solide (12.1%), ROIC faible (3.16%), séries historiques incomplètes. Pas de mutation fondamentale détectée entre les snapshots.

**Données comptables :** `data/accounting_risk_latest.json` inexistant — pas de scan comptable disponible. Pas d'alerte M-Score/Z-Score/F-Score/Sloan.

**Validation des données :** `data/validation_report.txt` (2026-06-03T10:00:01Z) — MITK dans les 24/29 tickers OK, 0 warning, 0 exclusion. Données utilisables normalement.

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur 10h UTC | Lecture |
|---|---|---|
| Consensus PT | $16.00 (2 analysts) | **DÉPASSÉ** — spot $17.57 = +9.8% au-dessus du PT |
| **Max Pain** | **$2.50** | 🔴 **ANOMALIE JSON** — valeur aberrante (−85.8% vs spot). Valeur opérationnelle historique **$20.00** conservée |
| **Put/Call ratio** | **null** | 🔴 Données corrompues dans latest.json. Valeur opérationnelle historique **0.22** conservée |
| **Call OI %** | **null** | 🔴 Données corrompues dans latest.json. Valeur opérationnelle historique **81.8%** conservée |
| Short Interest | 8.31% | Modéré, pas de squeeze setup |
| Social Sentiment | 0 / No data | Sous le radar retail (0 mentions Reddit) |
| Upgrades/Downgrades | Aucun | Silence analystes persistant (0 analyste actif ce mois) |
| News structurantes | Aucune | `data/news_2026-06-03.json` : 0 news MITK |
| Événements corporate | Aucun | `data/events_2026-06-03.json` : 0 événement MITK |

**Verdict Sentiment :** Neutre à légèrement négatif. Le consensus PT reste dépassé avec une marge stable (+9.8%). Aucun flux de news, aucun insider trade, aucun upgrade/downgrade. MITK reste sous le radar institutionnel et retail (0 mentions sur Reddit, sentiment 0/10). **La structure options est théoriquement inchangée** : max pain $20.00 (+13.8% vs spot), put/call 0.22 (extrêmement haussier), call OI 81.8% (dominance call massive). Cependant, la corruption des données options dans `latest.json` (max pain $2.50, put/call et call OI `null`) constitue une alerte data quality à monitorer. La faible liquidité du sous-jacent (volume <1.0× moyenne) limite la fiabilité du signal dérivé. Le dépassement persistant du PT analyste constitue un risque de retracement accentué vers $16.00–$16.50. Aucun pump/dump détecté.

---

## 4. Scoring Global — Inchangé

| Pilier | Score | Poids | Pondéré |
|---|---|---|---|
| **Catalyseur** | 4.0/10 | 35% | 1.400 |
| **Valorisation** | 5.0/10 | 40% | 2.000 |
| **Momentum** | 5.0/10 | 25% | 1.250 |
| **Score Opportunité** | **4.7/10** | — | **4.650** |
| **Score Global Ajusté** | **36.5/100** | — | — |

| Seuil | Action | Sizing |
|---|---|---|
| Score Global 36.5/100 | **SURVEILLER** | **—** |

**Explication :** Le Score Opportunité reste inchangé à **4.7/10**, avec les trois piliers stables : Catalyseur 4.0/10 (absence de news idiosyncratique), Valorisation 5.0/10 (Forward P/E attractif mais PT dépassé), Momentum 5.0/10 (consolidation au sommet, RSI surachat). Le malus technique lié au RSI > 70, au timing défavorable et au volume sous-moyenne persistant pèse de **−10.0 pts** sur le Score Global, le maintenant à **36.5/100** (catégorie SURVEILLER, fourchette 35–49). Le timing reste **Défavorable**.

**Risques additionnels :**
- Geo risk : Score 2/10 — pas d'exposition spécifique MITK (`data/geo_risk_2026-05-17.json`), flag 🟢
- FX impact : 0.0 — exposition USD, pas de divergence (`data/fx_exposure_2026-06-03.json`)
- Social sentiment : 0/10 — pas de signal retail (`data/social_sentiment_2026-06-03.json`)
- Events corporate : aucun (`data/events_2026-06-03.json`)
- Sector rotation : `NEUTRAL` — pas de vent de queue sectoriel déclaré (`data/sector_rotation_2026-06-03.json`)
- Quant significance : Insuffisant (0 signaux historiques, p-value 1.0) — pas de biais statistique détecté (`data/quant_report_2026-05-17.json`)

---

## 5. Révision des Niveaux SL / TP

| Niveau | Prix | Distance |
|---|---|---|
| **Stop-loss** | $15.87 | −9.6% |
| **Take-profit** | $20.12 | +14.4% |
| **Ratio R/R** | 1.5 | Seuil institutionnel non atteint (cible 1:2) |

Les niveaux sont **inchangés** : close $17.57 et ATR stable $0.85. Le SL à $15.87 correspond au support structurel $17.00 + marge ATR. Le TP à $20.12 reste aligné avec la zone max pain opérationnelle ($20.00). Le ratio R/R reste à 1.5, en-deçà du seuil institutionnel.

---

## 6. Calendrier & Événements

| Événement | Date | Jours restants |
|---|---|---|
| **Earnings Q3 FY2026** | 2026-08-06 | **64** |
| **Expiration options** | 2026-06-18 | **15** |

**Alertes actives (révisées) :**
- 🟢 **[CASSURE MM50 CONFIRMÉE]** Cours $17.57 > MM50 $14.71 (+19.4%) — signal technique intact — 2026-06-03
- 🟢 **[BREAK 52-WEEK HIGH]** 52w high $17.97 proche — break testé mais non confirmé — 2026-06-03
- 🟡 **[RSI SURACHAT SEVERE]** 71.77 > 70 — timing défavorable, malus technique majeur — 2026-06-03
- 🟡 **[VOLUME SOUS-MOYENNE PERSISTANT]** 954,900 = 0.719× moyenne 20j — stable mais toujours sous moyenne — 2026-06-03
- 🔴 **[CONSENSUS PT DÉPASSÉ]** $16.00 dépassé de 9.8% — upside théorique nul, risque de retracement accentué — 2026-06-03
- 🟢 **[STRUCTURE OPTIONS HAUSSIÈRE CONFIRMÉE]** Max Pain $20.00 (opérationnel), Put/Call 0.22, Call OI 81.8% — signal dérivé haussier inchangé — 2026-06-03
- 🔴 **[ANOMALIE OPTIONS JSON]** Max pain $2.50 aberrant dans latest.json (was $20.00), put/call et call OI null — valeurs opérationnelles historiques conservées — 2026-06-03
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital dans les prochains filings — 2026-05-18
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($793.4M Yahoo vs $446.6M FMP), P/E, EV multiples — utiliser Yahoo comme primaire — persistant
- 🟡 **[LIQUIDITÉ DÉRIVÉE FAIBLE]** Faible couverture strike — prudence sur le hedging — 2026-06-03
- 🟢 **[VOLUME COLLAPSE RÉSOLU]** 0.719× moyenne (was 0.225× le 02/06 17h) — invalidation persistante — 2026-06-03

---

## 7. Conclusion — Thèse SURVEILLER Confirmée

**Verdict : THÈSE SURVEILLER CONFIRMÉE. Snapshot 10:00 UTC 2026-06-03 : cours $17.57 (inchangé vs close 02/06 21h UTC, −1.68% vs previous close $17.87), RSI 71.77 (surachat sévère persistant), ATR $0.85 (stable), volume 954,900 (0.719× moyenne, stable). Score Global Ajusté inchangé : 36.5/100. Action SURVEILLER maintenue.**

MITK affiche une **stabilité totale** entre le close 02/06 21h UTC et le snapshot 03/06 10h UTC : aucun indicateur technique, fondamental ou sentimental n'a varié de manière significative. Le cours consolidé à $17.57 sur un volume stable (0.719×) indique une pause au sommet sans direction claire. Le RSI 71.77 reste en zone de surachat sévère, justifiant le maintien du malus technique majeur. Le consensus PT ($16.00) reste dépassé de 9.8%, rendant l'upside théorique négatif à court terme sans révision analystes.

**La principale évolution est une anomalie data quality dans les options** : `data/latest.json` affiche un max pain de $2.50 (vs $20.00 historique) et des champs put/call ratio et call OI % à `null`. Cette valeur de $2.50 est aberrante (−85.8% vs spot) et correspond à une corruption JSON récurrente observée sur d'autres tickers dans le même snapshot (AAPL, PLTR, RKLB). Les valeurs opérationnelles historiques ($20.00, 0.22, 81.8%) sont conservées et la structure options reste haussière.

**Catalyseurs forward :**
1. **Pullback technique vers $16.50–$17.00** — scénario le plus probable compte tenu du RSI > 70 et du volume sous-moyenne. Si pullback sur volume >1.0× moyenne, cela constituerait une base plus saine
2. **Earnings Q3 FY2026 (2026-08-06)** — 64j, Est EPS $0.24–$0.34, Rev ~$0.1B — beat sur guidance ou margins = révision analystes et justification du dépassement du PT
3. **Révision du consensus** — 2 analysts seulement, faible couverture = forte élasticité du PT en cas de beat

**Risques :**
- **RSI surachat sévère** (71.77 > 70) — correction technique probable dans les 2–5 séances
- **Consensus PT dépassé** ($16.00 < $17.57, +9.8%) — upside théorique nul sans révision. Risque de retracement accentué vers $16.50–$16.00
- **Volume sous-moyenne persistant** (0.719×) — malgré la stabilité, la liquidité reste faible pour une small-cap
- **Timing défavorable** — malus technique majeur sur le scoring global
- Absence de catalyseur idiosyncratique avéré (Catalyseur 4.0/10)
- ROIC faible (3.16%) — efficacité du capital à prouver
- SBC / Revenue élevé (9.35%) — dilution potentielle
- Faible liquidité de la small-cap (volume moyen <1.3M) — risque de glissement important en sortie
- **Anomalie options JSON** — monitorer la résolution dans les prochains snapshots

**Recommandation :** **SURVEILLER.**

Nouvelles positions : **déconseillées à ce stade.** Attendre un pullback significatif vers $16.00–$16.50 avec volume >1.0× moyenne et RSI sous 60 avant toute considération d'entrée. Déteneurs : **maintenir la prudence**. Le SL technique à $15.87 (−9.6%) est le seuil de vigilance absolu. Une cassure sous $17.00 avec volume élevé ou une cassure sous $15.87 (SL) confirmerait le scénario de distribution et justifierait un passage à **VENDRE** sur le court terme. Une cassure sous $14.71 (MM50) invaliderait la thèse haussière de moyen terme. Une amélioration du volume au-dessus de la moyenne 20j (>1.33M) avec stabilisation du cours au-dessus de $17.50 pourrait justifier un relèvement vers **ATTENDRE**.

---

*Révision post-pipeline 10:00 UTC — Données : `data/latest.json` (2026-06-03T10:00:14Z), `data/recommandations_2026-06-03.json` (SURVEILLER, 36.5/100), `data/quant_2026-05-17.json` (insuffisant), `data/geo_risk_2026-05-17.json` (score 2, pas exposé), `data/sector_rotation_2026-06-03.json` (signal NEUTRAL, XLK top rank), `data/fx_exposure_2026-06-03.json` (impact 0.0), `data/social_sentiment_2026-06-03.json` (pas de données), `data/upcoming_events_2026-06-03.json` (earnings 2026-08-06), `data/events_2026-06-03.json` (0 événement), `data/news_2026-06-03.json` (0 news) — Date : 2026-06-03*
