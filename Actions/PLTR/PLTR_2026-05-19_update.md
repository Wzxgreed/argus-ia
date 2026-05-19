# PLTR — Mise à Jour Quotidienne (2026-05-19, snapshot 13:00 UTC)

> **Source :** `data/latest.json` (snapshot 2026-05-19 13:00 UTC) + `data/recommandations_latest.json` + agents sector, FX, watchman, events, social, quant, geo  
> **Référence précédente :** [PLTR_2026-05-18_update.md](PLTR_2026-05-18_update.md)  
> **Dernier update :** 2026-05-19 10:00 UTC — snapshot stable avec anomalies options  

---

## Résumé des Changements depuis l'Update Précédent (2026-05-19 10:00 UTC)

| Indicateur | 10:00 UTC | 13:00 UTC | Δ |
|-----------|-----------|-----------|---|
| Cours close | **$135.14** | **$135.14** | **0.00%** |
| RSI 14j | 42.52 | 42.52 | 0 |
| Volume jour | 31.91M | **31.91M** | 0 |
| Volume vs moy. 20j | −28.0% | **−28.0%** | Stable |
| ATR 14j | 5.80 | 5.80 | 0 |
| MM 50j | 143.96 | 143.96 | 0 |
| **Max Pain options** | **$50.00** (anomalie) | **$140.00** | **+$90.00** |
| **Put/Call Ratio** | **null** | **0.64** | **Corrigé** |
| **Call OI %** | **null** | **60.8%** | **+1.5 pp** |
| Score Catalyseur | 6.8/10 | **6.8/10** | 0 |
| Score Valorisation | 4.5/10 | **4.5/10** | 0 |
| Score Momentum | 3.5/10 | **3.5/10** | 0 |
| Score Opportunité | 5.1/10 | **5.1/10** | 0 |
| Score Global ajusté | 42.5/100 | **42.5/100** | 0 |
| Action | SURVEILLER | **SURVEILLER** | → **Confirmé** |

**Verdict :** Snapshot 13:00 UTC confirme la stabilité des données de marché (cours, RSI, ATR, MM50 inchangés) et corrige les anomalies options du snapshot matinal. Le Max Pain revient à **$140.00** (cohérent avec le spot à $135.14, écart +3.6%), le Put/Call Ratio est rétabli à **0.64** (vs 0.69 au 18/05) et le Call OI % à **60.8%** (vs 59.3% au 18/05). Cette structure options révisée indique un biais haussier modéré légèrement renforcé par rapport à la clôture du 18/05. **Thèse SURVEILLER confirmée sans modification.**

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| Cours | **$135.14** | 0.00% vs previous close — consolidation |
| RSI 14j | **42.52** | Neutre-baisse, inchangé depuis le 18/05 |
| MM 50j | **143.96** | Cours **−6.1% sous MM50** — résistance dynamique intacte |
| MM 200j | — | [DONNÉES MANQUANTES] |
| Golden/Death Cross | Non | Aucun signal de croisement |
| Volume relatif vs 20j | **−28.0%** | 31.91M vs 44.28M moy. — contraction persistante |
| Fourchette 52 semaines | $118.93 / $207.52 | Positionné à 37% du range |
| ATR 14j | **$5.80** | Volatilité stable |
| Beta | **1.521** | Élevé — amplifie les rotations sectorielles |
| Timing verdict | **Défavorable** | Sous MM50 + volume sous moyenne |

**Évolution vs update 10:00 UTC :**
- **Cours / RSI / MM50 / ATR** : inchangés — le snapshot 13:00 UTC reflète la stabilisation post-close du 18/05.
- **Volume** : stable à 31.91M, contraction sévère persistante (−28% vs moyenne 20j). Liquidité institutionnelle absente.
- **Options :** correction majeure des données. Le Max Pain passe de l'anomalie $50 (artefact lié à l'expiration hebdomadaire du 2026-05-22) à **$140.00**, désormais cohérent avec le spot. Le Put/Call Ratio est rétabli à **0.64** (baisse de 0.05 vs 18/05 = biais haussier modéré renforcé). Le Call OI % remonte à **60.8%** (+1.5 pp vs 18/05 = appétence haussière modérée en hausse). L'expiration la plus proche reste le 2026-05-22 (3 jours).

---

## Mise à Jour Fondamentale

### Données FMP Annual FY2025 (inchangées vs précédent)

| Métrique | Valeur | Contexte |
|---------|--------|----------|
| Gross Margin | 82.4% | Excellente — business model software à forte levée |
| Operating Margin | 31.6% | Rentabilité opérationnelle élevée |
| Net Margin | 36.3% | Très élevée |
| Debt/Equity | 0.031 | Bilan quasi-sans dette |
| Current Ratio | 7.11 | Liquidité exceptionnelle |
| SBC / Revenue | 15.3% | Dilution significative par stock-based comp |
| DSO | 85 jours | Cycle de conversion client modéré |
| Cash Conversion Cycle | 81.3 jours | — |
| ROIC (FMP key metrics) | 17.9% | Création de valeur confirmée |
| Consensus Price Target | $187.61 | 33 analysts — upside théorique **+38.8%** |

### Divergences Yahoo vs FMP [DONNÉES PARTIELLES]

| Métrique | Yahoo Finance | FMP Annual FY2025 | Écart |
|---------|---------------|-------------------|-------|
| Market Cap | $324.0 Md | $421.2 Md | **+30%** |
| P/E | 151.8x | 259.2x | **+71%** |
| EV/Revenue | 60.5x | 93.8x | **+55%** |
| EV/EBITDA | 156.7x | 291.6x | **+86%** |
| P/B | 43.7x | 57.0x | **+30%** |

**Interprétation :** Écart persistant entre sources, inchangé vs matin. Les multiples restent extrêmes dans les deux cas, justifiant le Score Valorisation contenu (4.5/10). Aucune nouvelle donnée fondamentale ce jour.

**Filtre Qualité (6 critères)**
- Données Agent Accounting (M-Score, Z-Score, F-Score, Sloan) : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent (agent skipped lors du pipeline)
- Score Qualité : `[NON ÉVALUABLE]`
- Verdict : Le Filtre Qualité ne peut pas être appliqué sans les signaux comptables agents. Cette absence est un risque méthodologique persistant à noter.

---

## Mise à Jour Sentiment / Options / News

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| News du jour | — | Aucune news PLTR détectée dans le snapshot `data/latest.json` |
| Social Sentiment (Reddit) | No data | Aucun post collecté — absence de signal retail |
| Put/Call Ratio | **0.64** | Biais modéré vers les calls (vs 0.69 hier, 0.80 initiale) |
| Call OI % | **60.8%** | Appétence haussière modérée renforcée (vs 59.3% hier, 55.4% initiale) |
| Short Interest | 0.03% | Négligeable — pas de setup short squeeze |
| Insider Trades | — | [DONNÉES MANQUANTES] |
| Upgrades/Downgrades | — | [DONNÉES MANQUANTES] |
| Événements Corporate | Aucun | `data/events_latest.json` vide pour PLTR |

**Catalyseur prochain :** Earnings Q2 FY2026 le **2026-08-03** (76 jours). Est. EPS $0.32–$0.40, Rev $1.8B. Pas de preview requis (> 5j).

**Notes options :** Le snapshot 13:00 UTC corrige l'anomalie Max Pain $50 du matin. La valeur rétablie à $140.00 est cohérente avec le spot ($135.14) et suggère que les strikes concentrés se situent autour de $140 pour l'expiration du 2026-05-22. Le Put/Call en repli (0.64 vs 0.69) et le Call OI en hausse (60.8% vs 59.3%) traduisent une légère accumulation de biais haussier en début de semaine, malgré l'absence de volume au comptant.

---

## Scoring Global — Révision

| Axe | Score 13:00 UTC | Score 10:00 UTC | Δ | Pondération (Unknown) |
|-----|----------------|----------------|---|---------------------|
| Catalyseur | **6.8/10** | 6.8/10 | 0 | 35% |
| Valorisation | **4.5/10** | 4.5/10 | 0 | 40% |
| Momentum | **3.5/10** | 3.5/10 | 0 | 25% |
| **Score Opportunité** | **5.1/10** | **5.1/10** | **0** | — |

**Score Global brut :** 50.5/100  
**Score Global ajusté :** **42.5/100** (malus technique et structuraux)  
**Action :** **SURVEILLER**

**Explication :** Aucun changement de scoring entre les snapshots 10:00 et 13:00 UTC. Les données agents (recommandations, sector rotation, FX, geo) sont stables. Le Momentum reste le maillon faible (3.5/10) en raison de la position sous MM50 et du volume insuffisant. L'anomalie Max Pain du matin est résolue et n'impacte pas le score. L'agent recommandation maintient le statut SURVEILLER. Pas d'entrée avant confirmation technique (franchissement MM50 à $143.96 avec volume > moyenne 20j).

---

## Niveaux et Ratio R/R

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| Cours actuel | $135.14 | — |
| Entrée suggérée | $135.14 | — |
| Stop-loss suggéré | **$123.54** | Cours − 2×ATR = $135.14 − $11.60 |
| Take-profit suggéré | **$152.54** | Cours + 3×ATR = $135.14 + $17.40 |
| Ratio R/R | **1.5** | Ratio institutionnel standard |
| Upside vers consensus PT | +38.8% | $187.61 — horizon long terme |
| Max Pain (exp. 2026-05-22) | **$140.00** | +3.6% au-dessus du spot — zone de gravitation options |

---

## Contexte Macro, Sectoriel & Risques

| Facteur | État | Impact PLTR |
|---------|------|-------------|
| Régime macro | Unknown (VIX/DXY/taux non alimentés) | Pas d'ajustement régime-aware applicable |
| DXY | Stable | Neutre — pas de divergence FX détectée |
| XLK (Technology) | **Top sector** — Momentum 10.0/10, RS 20j +8.6% | **Vent favorable** structurel inchangé |
| Beta 1.52 | Élevé | Amplifie les rotations sectorielles |
| Geo Risk | Score 0 | Pas d'événement géopolitique spécifique |
| Accounting Risk | [DONNÉES MANQUANTES] | `data/accounting_risk_latest.json` absent — agent skipped |
| Quant Calibration | Insuffisant | Pas assez de signaux historiques (`p_value` 1.0) — calibration en cours |
| Social Sentiment | No data | Pas de signal retail exploitable |
| FX Exposure | 55% export EUR/CNY | FX Impact Score 0.0 — neutral, divergence aligned |

---

## Conclusion — État de la Thèse

**Statut : SURVEILLER — Thèse confirmée, pas modifiée.**

**Arguments confirmants :**
- Marges opérationnelles et nettes excellentes (FMP FY2025 : GM 82%, OM 32%, NM 36%)
- Bilan solide : quasi-zero dette, current ratio 7.1, ROIC 18%
- Consensus analystes actif (33 analysts, PT $187.61 = +38.8% upside)
- XLK leader sectoriel (momentum 10.0/10) — environnement favorable aux techs
- Options : structure modérément haussière renforcée (Put/Call 0.64, Call OI 60.8%, Max Pain $140)
- RSI 42.52 stable, sortie nette de la zone < 40 depuis le 17/05
- Cours stable à $135.14 — consolidation sans pression vendeuse renforcée

**Arguments limitants :**
- Timing technique défavorable : sous MM50 (−6.1%), volume moyen 20j non atteint (−28.0%)
- Multiples extrêmes quel que soit la source (P/E 152x–259x, EV/Revenue 60x–94x)
- Divergence data Yahoo vs FMP sur toutes les métriques de valorisation [DONNÉES PARTIELLES]
- Aucune news ni catalyseur immédiat avant earnings août
- Accounting risk non évalué (agent absent) — qualité comptable non confirmée

**Scénarios :**
1. **Optimiste (25%)** : Rebond sur support + retour du volume institutionnel → test MM50 ($144) puis consolidation
2. **Central (50%)** : Consolidation latérale $130–$145 en l'absence de catalyseur jusqu'à earnings août
3. **Pessimiste (25%)** : Compression multiple dans un environnement incertain → test du support $118.93 (52w low)

**Prochaines étapes :**
- Surveiller le franchissement de la MM50 ($143.96) avec volume supérieur à la moyenne 20j (> 44M)
- Préparer `_preview.md` si earnings approchent à ≤ 5 jours (actuellement 76j)
- Réactiver l'agent accounting dès que possible pour valider le Filtre Qualité 6 critères
- Surveiller l'expiration options du 2026-05-22 et la cohérence des données post-expiration

---

## Validation Analyste Senior — Snapshot 13:00 UTC

**Analyste :** Desk Argus-IA  
**Timestamp validation :** 2026-05-19 13:00 UTC  
**Status :** ✅ Confirmé — snapshot stable avec correction des anomalies options vs 10:00 UTC.

| Check | Résultat |
|-------|----------|
| `data/latest.json` (13:00 UTC) | Cours $135.14, RSI 42.52, ATR 5.80, MM50 143.96 — identique à la clôture 18/05 |
| Options (13:00 UTC) | Max Pain $140.00, Put/Call 0.64, Call OI 60.8% — **correction des anomalies du matin** |
| `data/recommandations_latest.json` | Scores inchangés : C 6.8 / V 4.5 / M 3.5 → Opp 5.1 / Global 42.5 |
| `data/geo_risk_latest.json` | Score 0, aucun ticker PLTR flaggé |
| `data/fx_exposure_latest.json` | FX Impact Score 0.0, divergence aligned, pas de headwind |
| `data/events_latest.json` | Aucun événement corporate détecté |
| `data/news_latest.json` | Aucune news PLTR dans le snapshot Yahoo |
| `data/social_sentiment_latest.json` | No data — pas de signal retail |
| `data/upcoming_events_latest.json` | Earnings Q2 FY2026 confirmé 2026-08-03 (76j) |
| `data/quant_report_latest.json` | Pas assez de signaux historiques (p-value 1.0) — calibration en cours |
| `data/sector_rotation_latest.json` | XLK top sector (momentum 10.0/10) — vent favorable inchangé |
| Accounting Risk | `data/accounting_risk_latest.json` absent — risque méthodologique persistant |

**Conclusion validation :** Le snapshot 2026-05-19 13:00 UTC confirme la stabilité des données de marché vs la clôture du 18/05 et corrige les anomalies options du snapshot matinal (Max Pain $50 → $140, Put/Call et Call OI rétablis). La structure options révisée (Put/Call 0.64, Call OI 60.8%) est légèrement plus haussière que la clôture du 18/05. La thèse **SURVEILLER** reste inchangée. Le timing d'entrée reste conditionné au franchissement de la MM50 ($143.96) avec volume > 44M.
