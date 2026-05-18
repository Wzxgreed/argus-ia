# PLTR — Mise à Jour Quotidienne (2026-05-18, close 21:00 UTC)

> **Source :** `data/latest.json` (snapshot 2026-05-18 22:35 UTC) + `data/recommandations_latest.json` + agents sector, FX, watchman, events, social  
> **Référence précédente :** [PLTR_2026-05-17_init.md](PLTR_2026-05-17_init.md) (initiale)  
> **Dernier update :** aucun — ce fichier remplace la première version auto-générée à 20:12 UTC (mêmes données, format institutionnel consolidé)

---

## Résumé des Changements depuis l'Analyse Initiale (2026-05-17)

| Indicateur | Initiale 17/05 | Close 18/05 | Δ |
|-----------|---------------|-------------|---|
| Cours close | $133.99 | **$135.14** | **+0.86%** |
| RSI 14j | 38.93 | **42.52** | **+3.59 pts** |
| Volume jour | 32.3M | **31.76M** | **−1.6%** |
| Volume vs moy. 20j | −27.0% | **−28.2%** | Contraction stable |
| ATR 14j | 5.80 | 5.80 | 0 |
| MM 50j | 144.40 | **143.96** | −$0.44 |
| Max Pain options | $80.00 | $80.00 | 0 |
| Put/Call Ratio | 0.80 | **0.69** | **−0.11** |
| Call OI % | 55.4% | **59.3%** | **+3.9 pp** |
| Score Catalyseur | 4.0/10 | **6.8/10** | **+2.8** |
| Score Valorisation | 2.0/10 | **4.5/10** | **+2.5** |
| Score Momentum | 3.0/10 | **3.5/10** | **+0.5** |
| Score Opportunité | 3.0/10 | **5.1/10** | **+2.1** |
| Score Global ajusté | — | **42.5/100** | — |
| Action | SURVEILLER | **SURVEILLER** | → **Confirmé** |

**Verdict :** Consolidation haussière (+0.86%) avec RSI remonté à 42.52 (sortie nette de la zone < 40). Structure options renforcée (Put/Call 0.69, Call OI 59.3%). Les scores agents ont été révisés à la hausse vs l'initiale du 17/05 (+2.1 pts sur l'Opportunité), tirés par le Catalyseur (+2.8) et la Valorisation (+2.5) suite à l'alimentation complète des données agents (consensus, FMP, options). Le Momentum reste faible (3.5/10) en raison de la position sous MM50 et du volume insuffisant. **Thèse SURVEILLER confirmée sans modification de direction.**

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| Cours | **$135.14** | +0.86% vs previous close ($133.99) |
| RSI 14j | **42.52** | Sortie nette de la zone < 40, reste neutre-baisse |
| MM 50j | **143.96** | Cours **−6.1% sous MM50** — tendance baissière intacte |
| MM 200j | — | [DONNÉES MANQUANTES] |
| Golden/Death Cross | Non | Aucun signal de croisement |
| Volume relatif vs 20j | **−28.2%** | 31.76M vs 44.26M moy. — contraction persistante |
| Fourchette 52 semaines | $118.93 / $207.52 | Positionné à 37% du range |
| ATR 14j | **$5.80** | Volatilité stable |
| Beta | **1.521** | Élevé — amplifie les rotations sectorielles |
| Timing verdict | **Défavorable** | Sous MM50 + volume sous moyenne |

**Évolution vs initiale :**
- **RSI** : remontée de 38.93 à 42.52 (+3.59) — éloignement du seuil 40, mais toujours sous 50.
- **MM50** : légère baisse de 144.40 à 143.96 — résistance dynamique descendante, rapprochant un test potentiel.
- **Volume** : stable autour de 32M, bien en deçà de la moyenne 20j (44.26M). Liquidité institutionnelle absente.
- **Options** : Put/Call replié de 0.80 à 0.69, Call OI remonté de 55.4% à 59.3% — biais haussier modéré renforcé en début de semaine.

---

## Mise à Jour Fondamentale

### Données FMP Annual FY2025 (inchangées vs initiale)

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
| P/E | 153.6x | 259.2x | **+69%** |
| EV/Revenue | 60.0x | 93.8x | **+56%** |
| EV/EBITDA | 155.3x | 291.6x | **+88%** |
| P/B | 43.7x | 57.0x | **+30%** |

**Interprétation :** Écart persistant entre sources. Aucune nouvelle donnée fondamentale ce jour. Les multiples restent extrêmes dans les deux cas, justifiant le Score Valorisation contenu (4.5/10).

**Filtre Qualité (6 critères)**
- Données Agent Accounting (M-Score, Z-Score, F-Score, Sloan) : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent (agent skipped lors du pipeline)
- Score Qualité : `[NON ÉVALUABLE]`
- Verdict : Le Filtre Qualité ne peut pas être appliqué sans les signaux comptables agents. Cette absence est un risque méthodologique à noter.

---

## Mise à Jour Sentiment / Options / News

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| News du jour | — | Aucune news PLTR détectée dans le snapshot `data/latest.json` |
| Social Sentiment (Reddit) | No data | Aucun post collecté — absence de signal retail |
| Put/Call Ratio | **0.69** | Biais modéré vers les calls (vs 0.80 hier) |
| Call OI % | **59.3%** | Appétence haussière modérée renforcée (vs 55.4%) |
| Short Interest | 0.03% | Négligeable — pas de setup short squeeze |
| Insider Trades | — | [DONNÉES MANQUANTES] |
| Upgrades/Downgrades | — | [DONNÉES MANQUANTES] |
| Événements Corporate | Aucun | `data/events_latest.json` vide pour PLTR |

**Catalyseur prochain :** Earnings Q2 FY2026 le **2026-08-03** (77 jours). Est. EPS $0.32–$0.40, Rev $1.8B. Pas de preview requis (> 5j).

---

## Scoring Global — Révision

| Axe | Score Auj. | Score Initiale 17/05 | Δ | Pondération (Unknown) |
|-----|-----------|---------------------|---|---------------------|
| Catalyseur | **6.8/10** | 4.0/10 | **+2.8** | 35% |
| Valorisation | **4.5/10** | 2.0/10 | **+2.5** | 40% |
| Momentum | **3.5/10** | 3.0/10 | **+0.5** | 25% |
| **Score Opportunité** | **5.1/10** | **3.0/10** | **+2.1** | — |

**Score Global brut :** 50.5/100  
**Score Global ajusté :** **42.5/100** (malus technique et structuraux)  
**Action :** **SURVEILLER**

**Explication :** L'amélioration des scores Catalyseur et Valorisation par rapport à l'initiale du 17/05 reflète une meilleure alimentation des données agents (options, consensus, FMP) plutôt qu'un changement de fondamentaux réel. Le Momentum reste le maillon faible (3.5/10) en raison de la position sous MM50 et du volume insuffisant. L'agent recommandation maintient le statut SURVEILLER. Pas d'entrée avant confirmation technique (franchissement MM50 à $143.96 avec volume > moyenne 20j).

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

---

## Contexte Macro, Sectoriel & Risques

| Facteur | État | Impact PLTR |
|---------|------|-------------|
| Régime macro | Unknown (VIX/DXY/taux non alimentés) | Pas d'ajustement régime-aware applicable |
| DXY | Stable | Neutre — pas de divergence FX détectée |
| XLK (Technology) | **Top sector** — Momentum 10.0/10, RS 20j +8.6% | **Vent favorable** structurel |
| Beta 1.52 | Élevé | Amplifie les rotations sectorielles |
| Geo Risk | Score 0 | Pas d'événement géopolitique spécifique (`data/geo_risk_latest.json`) |
| Accounting Risk | [DONNÉES MANQUANTES] | `data/accounting_risk_latest.json` absent — agent skipped |
| Quant Calibration | Insuffisant | Pas assez de signaux historiques (`p_value` 1.0) |
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
- Options : structure modérément haussière renforcée (Put/Call 0.69, Call OI 59.3%)
- RSI remonté à 42.52, sortie nette de la zone < 40

**Arguments limitants :**
- Timing technique défavorable : sous MM50 (−6.1%), volume moyen 20j non atteint (−28.2%)
- Multiples extrêmes quel que soit la source (P/E 153x–259x, EV/Revenue 60x–94x)
- Divergence data Yahoo vs FMP sur toutes les métriques de valorisation [DONNÉES PARTIELLES]
- Aucune news ni catalyseur immédiat avant earnings août
- Accounting risk non évalué (agent absent) — qualité comptable non confirmée

**Scénarios :**
1. **Optimiste (25%)** : Rebond sur support + retour du volume institutionnel → test MM50 ($144) puis consolidation
2. **Central (50%)** : Consolidation latérale $130–$145 en l'absence de catalyseur jusqu'à earnings août
3. **Pessimiste (25%)** : Compression multiple dans un environnement incertain → test du support $118.93 (52w low)

**Prochaines étapes :**
- Surveiller le franchissement de la MM50 ($143.96) avec volume supérieur à la moyenne 20j (> 44M)
- Préparer `_preview.md` si earnings approchent à ≤ 5 jours (actuellement 77j)
- Réactiver l'agent accounting dès que possible pour valider le Filtre Qualité 6 critères

---

## Validation Analyste Senior — Re-check 22:35 UTC

**Analyste :** Desk Argus-IA  
**Timestamp validation :** 2026-05-18 22:35 UTC  
**Status :** ✅ Confirmé — aucun changement de données vs consolidation 21:00 UTC.

| Check | Résultat |
|-------|----------|
| `data/latest.json` (22:35 UTC) | Cours $135.14, RSI 42.52, ATR 5.80, MM50 143.96 — identique à la clôture |
| `data/recommandations_latest.json` | Scores inchangés : C 6.8 / V 4.5 / M 3.5 → Opp 5.1 / Global 42.5 |
| `data/geo_risk_latest.json` | Score 0, aucun ticker PLTR flaggé |
| `data/fx_exposure_latest.json` | FX Impact Score 0.0, divergence aligned, pas de headwind |
| `data/events_latest.json` | Aucun événement corporate détecté |
| `data/news_latest.json` | Aucune news PLTR dans le snapshot Yahoo |
| `data/social_sentiment_latest.json` | No data — pas de signal retail |
| `data/upcoming_events_latest.json` | Earnings Q2 FY2026 confirmé 2026-08-03 (77j) |
| `data/quant_report_latest.json` | Pas assez de signaux historiques (p-value 1.0) — calibration en cours |
| `data/sector_rotation_latest.json` | XLK top sector (momentum 10.0/10) — vent favorable inchangé |
| Accounting Risk | `data/accounting_risk_latest.json` absent — risque méthodologique persistant |

**Conclusion validation :** La consolidation institutionnelle est validée. Aucun nouvel élément de marché, fondamental ou événementiel depuis la clôture. La thèse **SURVEILLER** reste inchangée. Le timing d'entrée reste conditionné au franchissement de la MM50 ($143.96) avec volume > 44M.
