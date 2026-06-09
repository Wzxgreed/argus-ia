# AAPL — Mise à Jour Snapshot 13:00 UTC (2026-06-09)

> **Source :** `data/latest.json` (snapshot 2026-06-09 13:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events, recommandation
> **Référence précédente :** [AAPL_2026-06-09_update.md](AAPL_2026-06-09_update.md) (snapshot 10:00 UTC)
> **Contexte :** Stabilité technique absolue + résolution de l'anomalie options JSON + léger rehaussement du consensus analyste.

---

## Résumé des Changements depuis le Snapshot 10:00 UTC (2026-06-09)

| Indicateur | Snapshot 10h UTC | Snapshot 13h UTC | Δ vs Prior |
|-----------|------------------|------------------|------------|
| Cours close | $301.54 | **$301.54** | Inchangé |
| RSI 14j | 53.99 | **53.99** | Inchangé — zone neutre favorable maintenue |
| ATR 14j | $6.48 | **$6.48** | Inchangé |
| MM 50j | $282.06 | **$282.06** | Inchangé — tendance haussière intacte (+6.9%) |
| Volume du jour | 77.73M vs 49.06M avg (1.58×) | **77.73M vs 49.06M avg (1.58×)** | Inchangé — distribution vendeuse persistante sans accélération |
| Short Interest | 0.95% | **0.95%** | Inchangé |
| Consensus FMP PT | $293.43 (58 analystes) | **$295.06 (60 analystes)** | 🟢 **+$1.63 (+0.6%), +2 analystes** |
| Upside implicite | −2.7% | **−2.2%** | 🟢 Amélioration mécanique du spread consensus/spot |
| Max Pain | $330.00 (opérationnel) | **$332.50** | 🟡 **+$2.50** — JSON corrigé, écart spot élargi |
| Put/Call Ratio | 0.42 (opérationnel) | **0.51** | 🟡 **+0.09** — structure légèrement moins haussière mais reste bullish |
| Call OI % | 70.6% (opérationnel) | **66.1%** | 🟡 **−4.5 pts** — dominance call modérée mais majoritaire |
| **Score Opportunité agent** | 5.6/10 | **5.6/10** | Inchangé |
| **Score Global ajusté** | 61.0/100 | **61.0/100** | Inchangé |
| **Recommandation agent** | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | Confirmée |
| **Timing agent** | Favorable | **Favorable** | Inchangé |

**Verdict :** Le snapshot 13:00 UTC confirme la **stabilité totale** des données techniques par rapport au snapshot 10:00 UTC. Le cours reste à **$301.54**, le RSI à **53.99** (zone neutre favorable), l'ATR à **$6.48** et la MM50 à **$282.06** (+6.9%). Le volume est inchangé à **77.73M (1.58×)**, maintenant le signal de distribution vendeuse sans accélération.

**Changement majeur : résolution de l'anomalie options JSON.** Le snapshot 13h fournit des données options cohérentes et exploitables :
- **Max pain $332.50** (vs $250.00 aberrant en JSON 10h, et $330.00 opérationnel du 08/06) — repositionné +$2.50 au-dessus de la valeur opérationnelle précédente.
- **Put/Call 0.51** (vs null en JSON 10h, et 0.42 opérationnel du 08/06) — structure légèrement moins haussière mais reste bullish (< 1.0).
- **Call OI 66.1%** (vs null en JSON 10h, et 70.6% opérationnel du 08/06) — dominance call modérée, majorité maintenue.

**Consensus analyste rehaussé :** le PT moyen FMP passe de **$293.43 (58 analystes)** à **$295.06 (60 analystes)**. L'upside implicite s'améliore mécaniquement de **−2.7%** à **−2.2%** vs cours $301.54.

**Geo risk mis à jour :** `geo_risk_2026-06-09.json` confirme un score politique de **2/10** (🟢), aucun événement géopolitique spécifique à AAPL.

Les scores agents, fondamentaux, niveaux macro, sector rotation, FX et social sentiment restent **strictement identiques** au snapshot 10h.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $301.54 | Consolidation absolue post-rejet du rebond 08/06 |
| RSI 14j | 53.99 | 🟢 Zone neutre favorable inchangée — timing d'entrée sécurisé maintenu |
| ATR 14j | $6.48 | 🟡 Volatilité stabilisée en expansion modérée |
| MM 50j | $282.06 | 🟢 Cours +6.9% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 49.06M | 🟡 1.58× moyenne — distribution persistante mais sans accélération |
| 52W Range | $195.07–$317.40 | Cours à −5.0% du 52W high ($317.40) |
| Support clé | $288.58 | Cours − 2×ATR = $301.54 − $12.96 |
| Support secondaire | $282.06 | MM50 — cassure = retour vers $275 |
| Résistance | $317.40 | 52W high — break nécessite volume > 55M en clôture |
| Résistance mécaniste | $332.50 | Max pain options (JSON corrigé) — call wall à +10.3% |
| Short Interest | 0.95% | 🟢 Faible — pas de setup short squeeze |

**Options — Anomalie JSON RÉSOLUE ✅**

| Métrique | Snapshot 10h UTC | Snapshot 13h UTC | Interprétation |
|----------|------------------|------------------|----------------|
| Max Pain | **$250.00** (anomalie) → opérationnel $330.00 | **$332.50** | 🟢 Valeur corrigée et cohérente. Spot à +10.3% — pinning gamma vers le bas peu probable |
| Put/Call Ratio | **null** (corrompu) → opérationnel 0.42 | **0.51** | 🟢 Données restaurées. Structure légèrement moins haussière vs 08/06 mais reste bullish |
| Call OI % | **null** (corrompu) → opérationnel 70.6% | **66.1%** | 🟢 Données restaurées. Dominance call modérée, majoritaire |
| Expiration | 2026-06-10 | 2026-06-10 | ⚠️ Échéance demain — gamma risk imminent mais écart spot/max pain réduit le risque de pinning |

**Interprétation technique :**
- **RSI 53.99** : stabilité en zone neutre favorable (50–60). Historiquement favorable pour les entrées long sur AAPL dans un contexte de tendance haussière intacte. 🟢
- **Volume 77.73M (1.58×)** : inchangé vs snapshot 10h. La distribution vendeuse persiste mais n'accélère pas. Absence de poursuite baissière sur volume stable = signe de consolidation plutôt que de rupture. 🟡
- **ATR $6.48** : stabilisé. Range intraday maintenu autour de $16 ($301.17–$317.40 intraday selon JSON). 🟡
- **Max pain $332.50** (corrigé) : le spot ($301.54) est désormais à +$30.96 du max pain, soit **+10.3%** (vs +9.4% avec la valeur opérationnelle $330.00). Échéance 2026-06-10 demain — le pinning gamma vers le bas reste peu probable vu l'écart accru. 🟢
- **MM50 $282.06** : support dynamique intact. Une cassure sous MM50 sur volume > 1.0× invaliderait la tendance haussière de moyen terme. 🟢
- **52W high $317.40** : le cours reste à −5.0% du sommet. Le rejet sous $317.40 le 08/06 constitue un double top de courte durée à surveiller. 🟡

---

## Mise à Jour Fondamentale

### Consensus Analystes — Rehaussé
- **Price Target moyen FMP : $295.06** (60 analystes, 4 mises à jour le mois dernier, 12 le trimestre dernier)
- **Upside implicite : −2.2%** vs cours $301.54 (amélioré de −2.7% au snapshot 10h)
- **Couverture :** 60 analystes — coverage institutionnel massif, +2 analystes vs snapshot 10h

### Ratios FMP — Inchangés (FY2025)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.43T | $3.82T | 🟡 Écart +16% entre sources |
| P/E (LTM) | 36.5x | 34.1x | 🔴 Élevé |
| Forward P/E | 31.4x | — | 🔴 Élevé |
| EV/Revenue | 9.8x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 27.8x | 27.0x | 🔴 Élevé |
| P/B | 41.5x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples élevés mais qualité institutionnelle intacte (Filtre Qualité 6/6 ✅ Quality Compounder). Le Score Valorisation agent reste à **5.0/10**.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 60 analystes FMP, PT $295.06. Consensus légèrement rehaussé.
- **Aucun upgrade/downgrade** détecté dans le snapshot.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — Anomalie Résolue + Échéance Imminente
- **Max Pain $332.50** (corrigé) : spot à +10.3% (vs +9.4% avec valeur opérationnelle $330.00). Échéance demain 2026-06-10.
- **Put/Call 0.51** : structure haussière confirmée, légèrement moins prononcée que l'opérationnel 0.42 du 08/06.
- **Call OI 66.1%** : appétit call majoritaire, en recul de 4.5 pts vs l'opérationnel 70.6% du 08/06.
- **Gamma risk J−1** : échéance 2026-06-10 demain. Pinning gamma vers le bas peu probable (spot éloigné du max pain à +10.3%).

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.086 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | **XLK top sector rotation (momentum 10.0/10, RS20 +4.72%)** |

### Sector Rotation
- **Technology (XLK)** : return 20d +4.93%, RS20 vs SPY +4.72%. **Top1** du ranking avec momentum score 10.0/10. Pas de crossover détecté.
- **Signal système :** NEUTRAL (régime UNKNOWN).

### Géopolitique
- **Score Politique :** 2/10 (🟢). `geo_risk_2026-06-09.json` : aucun événement géopolitique spécifique à AAPL. Aucun flag.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `data/accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0, n=0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | Snapshot 10h /10 | Snapshot 13h /10 | Δ | Justification |
|-----|-----------------|------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucun catalyseur nouveau. Earnings 2026-07-30 dans 51 jours. |
| Valorisation | 5.0 | **5.0** | 0 | Cours inchangé $301.54. Consensus rehaussé mécaniquement mais upside reste négatif. |
| Momentum | 7.0 | **7.0** | 0 | RSI 53.99 stable — zone neutre favorable maintenue. Tendance haussière intacte vs MM50. |
| **Score Opportunité** | **5.6** | **5.6** | **0** | Pondération régime default 35/40/25 |

**Score Global Composite agent :** 56.0/100 → **Ajusté 61.0/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Favorable**
- **Recommandation agent : ACHETER (Sizing Réduit)**

**Verdict institutionnel Argus-IA :** La stabilité totale des données techniques et fondamentales confirme le setup du snapshot 10h. La résolution de l'anomalie options JSON est un signal positif de qualité de données : les valeurs corrigées (max pain $332.50, P/C 0.51, Call OI 66.1%) sont cohérentes avec la structure de marché d'AAPL. La structure options reste haussière malgré un léger reflux de la dominance call (−4.5 pts vs 08/06), ce qui peut refléter un ajustement post-expiration du cycle précédent. Le consensus analyste rehaussé à $295.06 (+$1.63, +2 analystes) est un micro-signal positif de coverage mais ne modifie pas l'upside négatif (−2.2%). Le ratio R/R calculé à 1.5:1 reste **inférieur au seuil institutionnel de 2:1**, justifiant le sizing réduit. La recommandation **ACHETER (Sizing Réduit)** est confirmée.

---

## Niveaux SL / TP Révisés

| | Snapshot 10h UTC | Snapshot 13h UTC | Justification |
|---|------------------|------------------|---------------|
| Entrée suggérée | $301.54 | **$301.54** | Close actuel — inchangé |
| Stop-Loss | $288.58 | **$288.58** | Cours − 2×ATR = $301.54 − $12.96. Inchangé |
| Take-Profit | $320.98 | **$320.98** | Cours + 3×ATR = $301.54 + $19.44. Inchangé |
| Ratio R/R | 1.5 | **1.5** | Inchangé — inférieur au seuil 2:1 |

**Note institutionnelle :** Le ratio R/R reste à 1.5:1, inférieur au seuil de 2:1. Le SL $288.58 est le niveau clé : une cassure sous $288.58 sur volume > 50M en clôture invaliderait la tendance haussière de court terme et ouvrirait un retour vers MM50 $282.06 puis $275. La résistance $317.40 (52W high) doit être breakée sur volume > 55M en clôture pour confirmer une reprise haussière. Le max pain $332.50 reste une résistance mécaniste crédible post-expiration. **Échéance options demain (2026-06-10)** : surveiller si le call wall $332.50 reste un niveau de liquidité pertinent pour le cycle suivant, et si le volume se normalise (> 0.8×) pour valider l'absence de distribution continue.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — La recommandation ACHETER (Sizing Réduit) et le timing Favorable sont maintenus.**

La thèse est confirmée car l'ensemble des données techniques et fondamentales est stable vs le snapshot 10h. La résolution de l'anomalie options JSON est un élément de qualité de données positif : les nouvelles valeurs (max pain $332.50, P/C 0.51, Call OI 66.1%) sont cohérentes et exploitables. La structure options reste haussière malgré un léger reflux de la dominance call, ce qui peut refléter un rééquilibrage post-expiration du cycle du 08/06. Le consensus analyste rehaussé à $295.06 (+$1.63, +2 analystes) est un micro-signal positif mais ne modifie pas l'upside négatif (−2.2%). Le RSI 53.99 reste en zone neutre favorable, la MM50 $282.06 est intacte (+6.9%), et le volume de distribution stable (1.58×) n'accélère pas. La recommandation de l'agent **ACHETER (Sizing Réduit)** est confirmée avec le même niveau de prudence : le ratio R/R 1.5:1 reste insuffisant pour un sizing standard.

### Ce qui a changé (évolutions significatives)
1. **Anomalie options JSON RÉSOLUE** : max pain $332.50 (vs $250.00 aberrant), P/C 0.51 (vs null), Call OI 66.1% (vs null) — données désormais cohérentes et exploitables. 🟢
2. **Consensus FMP rehaussé** : $293.43 (58) → **$295.06 (60)** — +$1.63, +2 analystes. Upside amélioré à −2.2% (vs −2.7%). 🟢
3. **Geo risk mis à jour** : score 2/10 (🟢), aucun flag spécifique AAPL. 🟢

### Ce qui n'a PAS changé (stabilité)
1. **Cours** $301.54 — consolidation absolue.
2. **RSI 53.99** — zone neutre favorable inchangée.
3. **ATR $6.48** — volatilité stabilisée.
4. **MM50 $282.06** — tendance haussière intacte.
5. **Volume 77.73M (1.58×)** — distribution vendeuse persistante sans accélération.
6. **Short Interest 0.95%** — inchangé.
7. **Fondamentaux FMP FY2025** — inchangés.
8. **Filtre Qualité 6/6** ✅ Quality Compounder.
9. **XLK top sector** — momentum 10.0/10, signal NEUTRAL.
10. **FX Exposure Score 0.0** — neutral.
11. **Scores agents** : Opportunité 5.6/10, Global ajusté 61.0/100, ACHETER (Sizing Réduit), Timing Favorable.
12. **Validation data** — AAPL OK (`validation_report.txt` 2026-06-09).

### Risques identifiés (inchangés)
1. **Volume de distribution 1.58×** — persistance du signal vendeur. Si le volume reste élevé à la baisse demain, le risque de cassure du support $288.58 augmente. 🔴
2. **ATR $6.48** — volatilité en expansion. Range intraday élargi = stops plus larges et ratio R/R dégradé. 🟡
3. **Call wall $332.50** — résistance mécaniste post-expiration. Surveillance maintenue. 🟡
4. **Valorisation étirée** — P/E 36.5x, Forward P/E 31.4x. Compression multiple possible si guidance décevante le 2026-07-30. 🔴
5. **Double top court terme** — rejet sous $317.40 (52W high) sur volume élevé = pattern de distribution potentiel. 🟡
6. **Absence de catalyseur immédiat** — prochain earnings dans 51 jours (2026-07-30). Zone sans catalyseur = risque de dérive latérale. 🟡

### Positionnement Argus-IA
- **Action : ACHETER (Sizing Réduit)** — Entrée possible à $301.54, sous réserve de normalisation du volume demain
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (51 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Post-expiration (demain)** : Surveiller le volume d'ouverture. Si volume > 0.8× avec cours stable > $300 : entrée validée. Si volume > 1.2× avec cours < $298 : distribution continue — réévaluer.
- **Si cours > $317.40 (52W high) sur volume > 55M en clôture :** Break confirmé — réévaluer le sizing vers standard avec SL $288.58.
- **Si cours < $288.58 (SL) sur volume > 50M :** Support cassé — sortie long, risque de test MM50 $282.06 puis $275.
- **Si RSI redescend < 50 avec volume normalisé > 0.8× :** Signal de faiblesse — réduire ou sortir la position.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan Ratio) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 2026-06-09 13:00 UTC) — Cours $301.54, RSI 53.99, ATR $6.48, MM50 $282.06, volume 77.73M (1.58×), short interest 0.95%, consensus FMP $295.06 (60 analystes), options max_pain $332.50, put/call 0.51, call_oi 66.1%, previous_close $307.34
- `data/recommandations_2026-06-09.json` — Score Opportunité 5.6/10, Score Global 56.0/100 (ajusté 61.0), Recommandation ACHETER (Sizing Réduit), SL $288.58, TP $320.98, Timing Favorable
- `data/validation_report.txt` (2026-06-09) — AAPL OK
- `data/sector_rotation_2026-06-09.json` — XLK top sector (momentum 10.0/10, NEUTRAL)
- `data/fx_exposure_2026-06-09.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-09.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-06-09.json` — Earnings 2026-07-30, 51 jours
- `data/events_2026-06-09.json` — Aucun événement corporate détecté
- `data/geo_risk_2026-06-09.json` — Score Politique 2/10, 🟢, aucun flag AAPL
- `data/quant_2026-05-17.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
