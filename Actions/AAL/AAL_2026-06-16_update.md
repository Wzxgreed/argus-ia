# AAL — Mise à Jour 2026-06-16 (Snapshot 10h UTC)

**Date :** 2026-06-16 (snapshot 10h UTC, pré-ouverture NY)
**Ticker :** AAL (NASDAQ)
**Type :** Mise à jour — downgrade recommandation, données techniques partielles, anomalie options
**Cours :** [DONNÉES MANQUANTES] (Open/High/Low/Close NaN dans `data/latest.json`)
**Previous close :** $14.98 (vs close officiel $15.46 le 15/06 = **−$0.48, −3.1%** en pré-market/implied)

> **Alerte data quality majeure :** Les données de cours du jour (open/high/low/close) sont **toutes NaN** dans `data/latest.json`. Seul `previous_close` ($14.98) est renseigné. Le volume affiché (178.76M) est **identique au volume du 15/06** — probablement stale/copié. Les données options sont **corrompues** (Max Pain $1.00 vs $10.00 hier, Put/Call et Call OI passés à null). L'ATR 14j et la MM50 sont passés à null. L'analyse repose sur les données disponibles avec marquage explicite des anomalies.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-15 21h UTC)

| Indicateur | 2026-06-15 21h UTC | 2026-06-16 10h UTC | Δ vs Prior |
|-----------|-------------------|-------------------|------------|
| Cours close | **$15.46** | **NaN** | **[DONNÉES MANQUANTES]** — Previous close $14.98 = −3.1% vs hier |
| RSI 14j | 55.88 | **51.38** | **−4.50 pts** — sortie de la zone neutre favorable, détente technique |
| ATR 14j | $0.65 | **null** | **[DONNÉES MANQUANTES]** |
| MM 50j | $12.79 | **null** | **[DONNÉES MANQUANTES]** |
| Volume (session) | 178.76M | **178.76M** | **Identique — probablement stale** |
| Volume vs moy. 20j | +78.9% | **+78.9%** | **Identique — suspect** |
| Forward P/E | 6.94 | **6.94** | **Inchangé** (mécanique, previous close plus bas) |
| Consensus FMP PT | $16.60 (17 analystes) | **$16.60 (17 analystes)** | **Inchangé** |
| Short Interest | 11.39% | **11.39%** | **Inchangé** |
| Options Max Pain | $10.00 | **$1.00** | **🔴 ANOMALIE MAJEURE** — artefact/corruption data |
| Options Put/Call | 1.69 | **null** | **[DONNÉES MANQUANTES]** |
| Options Call OI | 37.2% | **null** | **[DONNÉES MANQUANTES]** |
| Earnings Q2 (jours) | 38 | **37** | **−1 jour** — 2026-07-23 |
| Recommandation agent | ACHETER (Sizing Réduit) | **ATTENDRE** | **🔴 DOWNGRADE** |
| Score Opportunité | 5.9/10 | **5.2/10** | **−0.7 pt** |
| Score Catalyseur | 5.8 | **5.3** | **−0.5 pt** |
| Score Valorisation | 5.0 | **4.5** | **−0.5 pt** |
| Score Momentum | 7.5 | **6.0** | **−1.5 pt** — dégradation majeure |
| Score Global ajusté | 64.0/100 | **51.5/100** | **−12.5 pts** — sortie de la zone d'achat |
| Timing | Favorable | **Neutre** | **Dégradé** |

**Verdict institutionnel :** Le downgrade en **ATTENDRE** est piloté par la combinaison de trois facteurs : (1) absence de données de cours fiables (NaN), (2) dégradation du momentum (RSI −4.5 pts, score momentum −1.5 pt), et (3) anomalies data quality généralisées (options corrompues, ATR/MM50 nulls, volume suspect). Le `previous_close` à $14.98, si confirmé comme close de la veille, implique un repli de −3.1% par rapport au close officiel du 15/06 ($15.46), ce qui est cohérent avec une correction technique post-rally. La thèse **ACHETER (Sizing Réduit)** est **suspendue** jusqu'à récupération des données de cours et confirmation du support $15.00.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | NaN | 🔴 [DONNÉES MANQUANTES] — Previous close $14.98 |
| RSI 14j | 51.38 | 🟡 Détente de 4.5 pts, reste dans zone neutre mais moins favorable |
| ATR 14j | null | 🔴 [DONNÉES MANQUANTES] — Impossible de calculer SL/TP mécaniques |
| MM 50j | null | 🔴 [DONNÉES MANQUANTES] — Impossible d'évaluer la tendance intermédiaire |
| MM 200j | null | 🔴 [DONNÉES MANQUANTES] |
| Volume session | 178.76M | 🔴 Identique au 15/06 — données probablement stale, à ignorer |
| 52W Range | $10.09–$16.50 | 48.5% du 52W low, 9.2% sous le 52W high |
| Support immédiat | **$14.98** | 🟡 Previous close — premier niveau à surveiller |
| Support clé | **$15.00** | 🟡 Support psychologique cassé si previous_close = close réel |
| Support secondaire | **$14.16** | 🟢 Ancien SL ATR-based (basé sur cours $15.46, ATR $0.65) — référence historique |
| Support majeur | $12.79 | 🟢 Ancienne MM50 — référence historique, [DONNÉES MANQUANTES] aujourd'hui |
| Résistance | **$15.46** | 🔴 Close officiel du 15/06 — niveau à recapture |
| Résistance majeure | $16.50 | 🔴 52W high |
| Short Interest | 11.39% | 🟡 Stable — squeeze fuel intact mais inactionnable sans cours |

**Interprétation technique — Setup dégradé, données insuffisantes :**
- **RSI 51.38 :** Baisse de 4.5 pts en une session (implied). Sortie de la zone 55–60 favorable vers une zone neutre plus fragile. Si le cours est effectivement à $14.98, le RSI à 51.38 est cohérent avec une consolidation post-rally. Pas de survente, mais la marge de sécurité s'amenuise.
- **Volume stale :** Le chiffre 178.76M est identique à celui du 15/06. Il est hautement probable que ce soit une donnée copiée/stale et non le volume réel de la session du 16/06. **Ne pas interpréter ce chiffre.**
- **Données options corrompues :** Max Pain $1.00 est une anomalie flagrante (vs $10.00 hier). Put/Call et Call OI nulls. Le risque gamma pour l'expiration du 18/06 (J−2) est **inévaluable** aujourd'hui.
- **Verdict technique : NEUTRE DÉGRADÉ — données insuffisantes pour un positionnement.** Le repli implied de −3.1% ($15.46 → $14.98) est une correction technique modérée et attendue après le rally +3.2% du 15/06. Cependant, sans confirmation de cours, de volume et de niveaux ATR, tout positionnement est suspendu.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $16.60** (17 analystes, 2 mises à jour le mois dernier, 5 le trimestre dernier) — Inchangé depuis le 01/06.
- **Upside implicite :** Indéterminé (cours NaN). Si previous_close $14.98 = cours réel : **+10.8%** upside vs consensus.
- **Couverture :** 17 analystes — stable.

### Ratios FMP — Inchangés (données LTM FY2025)
| Ratio | Valeur | Signal |
|-------|--------|--------|
| Forward P/E | 6.94 | 🟢 Asymétrie intacte (trade tactique) |
| P/B (Yahoo) | −2.51 | 🔴 Equity négatif |
| EV/EBITDA (FMP) | 11.44 | 🟡 Élevé vs industrie |
| Gross Margin | 19.2% | 🟡 Sector norm |
| Operating Margin | 2.7% | 🔴 Faible |
| Net Margin | 0.2% | 🔴 Quasi nul |
| Current Ratio | 0.50 | 🔴 Trésorerie insuffisante |
| Net Debt / EBITDA | 8.83x | 🔴🔴 Extrême |
| Interest Coverage | 0.85x | 🔴 Service dette > EBIT |
| Tangible Asset Value | −$9.88B | 🔴 Patrimoine négatif |
| ROE | −3.0% | 🔴 Destruction de valeur |
| FCF Yield | −6.7% | 🔴 FCF négatif |

**Évolution fondamentale :** Aucun changement structurel. Le Forward P/E 6.94 reste le principal argument valorisation. Le bilan reste extrêmement fragile (Filtre Qualité 0–1/6). Si le cours est à $14.98, l'upside consensus remonte mécaniquement à +10.8% (vs +7.4% à $15.46), ce qui améliore la thèse valorisation — mais c'est un effet mécanique de baisse de cours, pas un renforcement fondamental.

### Événement Clé — Earnings Q2 FY2026
- **Date :** 2026-07-23 (**37 jours**)
- **Estimates EPS :** −$0.34 à $0.52 (fourchette large)
- **Estimates Revenue :** $16.6B
- **Implication :** Binary event inchangé. La fenêtre d'entrée tactique se rétrécit. Aucune nouvelle information pré-earnings détectée.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Inchangé :** PT moyen $16.60 (17 analystes). Aucune mise à jour depuis le 03/06.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions (No data). Aucun pump/dump détecté.

### Options — 🔴 CORROMPUES
| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| Max Pain | $1.00 | 🔴 ANOMALIE — vs $10.00 hier. Artefact flagrant, à ignorer |
| Put/Call ratio | null | 🔴 [DONNÉES MANQUANTES] |
| Call OI % | null | 🔴 [DONNÉES MANQUANTES] |
| Expiration | 2026-06-18 | J−2 — risque gamma inévaluable |

**Analyse options :** Les données options sont totalement corrompues aujourd'hui. Le Max Pain $1.00 est irréaliste (spot implied $14.98, écart de −93.3%). Le risque gamma pour l'expiration du 18/06 ne peut pas être évalué. **Nécessite une vérification manuelle des données sources Yahoo.**

### Sector Rotation — 🔴 DONNÉES INVALIDES
- **Industriels (XLI)** : `return_20d` NaN, `rs_20d` NaN, `momentum_score` 10.0 (artefact — tous les secteurs ont 10.0).
- **Signal global : NEUTRAL** — Fichier `data/sector_rotation_2026-06-16.json` corrompu (NaN généralisés sauf XLRE/XLC). Pas de malus/bonus sectoriel applicable.

### Exposition Macro — Inchangée
| Facteur | Exposition | Signal |
|---------|-----------|--------|
| Taux 10Y US | 🔴 Élevée | Dette variable ~$40B, +1% = +$400M/an |
| Pétrole (WTI) | 🔴🔴 Critique | Jet fuel 25–30% coûts opérationnels |
| DXY | 🟡 Modérée | FX Exposure Score 0.0 (neutral), 25% revenus export |
| Industriels (XLI) | 🟡 Modérée | Données sectorielles invalides aujourd'hui |

### Géopolitique — Inchangé
- **Score Politique :** AAL non flaggé dans `data/geo_risk_latest.json` (date 2026-05-17). Aucun ajustement.

### Accounting Risk / Quant — Inchangé
- **Accounting risk :** Fichier `data/quality_report_latest.json` (2026-05-17) ne couvre pas AAL. Pas d'alerte comptable.
- **Quant report :** Données insuffisantes (0 signaux historiques). Pas d'alerte de significativité.
- **Validation report 2026-06-16 :** AAL non concerné par les 5 errors / 2 warnings. [DONNÉES VALIDES au niveau structurale].

---

## Score Opportunité Révisé

| Axe | 2026-06-15 21h UTC /10 | 2026-06-16 10h UTC /10 | Δ | Justification |
|-----|------------------------|------------------------|---|---------------|
| Catalyseur | 5.8 | **5.3** | **−0.5** | Consensus stable, earnings J−37 inchangé, short interest stable. Pas de news. Incertitude data pèse. |
| Valorisation | 5.0 | **4.5** | **−0.5** | Forward P/E 6.94 inchangé. Si cours $14.98, upside mécanique +10.8% — mais effet de baisse de cours, pas de renforcement fondamental. Filtre Qualité 0–1/6 inchangé. |
| Momentum | 7.5 | **6.0** | **−1.5** | RSI −4.5 pts (51.38), repli implied −3.1%. Volume stale non interprétable. Données options corrompues. |
| **Score Opportunité** | **5.9** | **5.2** | **−0.7** | Pondération 35/40/25 (régime inconnu = default). |

**Score Global Composite agent :** 51.5/100 (vs 64.0/100 au snapshot 21h UTC du 15/06)
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Bonus : sectoriel 0 (données invalides)
- Timing : **Neutre**
- **Recommandation agent : ATTENDRE**
- **Recommandation institutionnelle Argus-IA : ATTENDRE** — downgrade de ACHETER (Sizing Réduit)

---

## Niveaux SL / TP — Suspendus

| | 2026-06-15 21h UTC | 2026-06-16 10h UTC | Justification |
|---|----------------------|----------------------|---------------|
| Entrée suggérée | $15.46 | **Indisponible** | Cours NaN, pas d'entrée suggérée |
| Stop-Loss | $14.16 | **$14.16 (référence)** | Basé sur ancien cours $15.46 et ATR $0.65 — **obsolète** |
| Take-Profit | $17.41 | **$17.41 (référence)** | Basé sur ancien cours $15.46 et ATR $0.65 — **obsolète** |
| Ratio R/R | 1.5 | **Indisponible** | Impossible à recalculer sans cours et ATR |

**Note institutionnelle :** Tous les niveaux SL/TP sont **suspendus** en raison de l'absence de données de cours et d'ATR. Si les données sont récupérées et que le cours se situe effectivement autour de $14.98 avec un ATR similaire ($0.65), les niveaux mécaniques seraient :
- SL ≈ $14.98 − $1.30 = **$13.68**
- TP ≈ $14.98 + $1.95 = **$16.93**
- R/R ≈ 1.5

Cependant, ces calculs sont **hypothétiques** et ne peuvent être validés sans données confirmées.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : MODIFIÉE — Downgrade de ACHETER (Sizing Réduit) à ATTENDRE.**

Entre le snapshot 21h UTC du 15/06 et le snapshot 10h UTC du 16/06, trois évolutions matérielles :
- **🔴 Downgrade recommandation agent :** ACHETER (Sizing Réduit) → ATTENDRE, Score Global 64.0 → 51.5 (−12.5 pts)
- **🔴 Anomalies data quality généralisées :** cours NaN, options corrompues (Max Pain $1.00), ATR/MM50 nulls, volume stale
- **🟡 RSI en détente :** 55.88 → 51.38 (−4.5 pts) — correction technique modérée

**Impact sur la thèse :**
- **Affaiblissement technique :** Le repli implied de −3.1% ($15.46 → $14.98) et la baisse du RSI indiquent une consolidation post-rally. Le support $15.00, clé hier, est désormais **cassé** si le previous_close reflète le cours réel.
- **Impossibilité de positionnement :** Sans données de cours fiables, sans ATR et sans options évaluables, tout positionnement est irrationnel. La règle de précaution prime.
- **Pas d'invalidation complète :** Les fondamentaux sont inchangés (Forward P/E 6.94, consensus $16.60, short interest 11.39%). Pas de news négative. Si les données sont récupérées et que le cours tient au-dessus de $14.50, la thèse pourrait être réactivée.
- **Conclusion :** La thèse est **suspendue à ATTENDRE**. Objectif : attendre la récupération des données de cours (snapshot 13h ou 17h UTC) et confirmer le comportement du support $15.00 / $14.98.

### Ce qui a changé (16/06 vs 15/06) :
1. **🔴 Recommandation downgradée :** ACHETER (Sizing Réduit) → **ATTENDRE**
2. **🔴 Score Global 64.0 → 51.5** (−12.5 pts) — sortie de la zone d'achat
3. **🔴 Score Momentum 7.5 → 6.0** (−1.5 pt) — dégradation majeure
4. **🟡 RSI 55.88 → 51.38** (−4.5 pts) — correction technique
5. **🔴 Cours NaN** — pas de donnée fiable (previous_close $14.98 = −3.1% implied)
6. **🔴 Options corrompues** — Max Pain $1.00 (artefact), Put/Call et Call OI nulls
7. **🔴 ATR et MM50 nulls** — impossibilité de calculer niveaux techniques

### Ce qui n'a PAS changé (et reste valide) :
1. Consensus FMP $16.60 (17 analystes), Forward P/E 6.94 — fondamentaux inchangés.
2. Short interest 11.39% — squeeze fuel intact.
3. Bilan extrêmement fragile — Filtre Qualité 0–1/6.
4. Earnings Q2 dans 37 jours — binary event inchangé.
5. Géopolitique non flaggé, FX 0.0 — malus/bonus inchangés.
6. Pas de news détectée sur AAL (15–16/06).

### Risques identifiés (révisés)
1. **🔴🔴 Données techniques partielles** — Impossibilité d'évaluer le setup en temps réel.
2. **🔴 Options corrompues** — Risque gamma J−2 inévaluable.
3. **🔴 Support $15.00 cassé** (si previous_close = réel) — retour dans le range $14.00–$15.00.
4. **🔴 Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value négatif.
5. **🔴 Value trap** — Forward EPS ~$2.23/share peut ne pas se matérialiser.
6. **🔴 Filtre Qualité 0–1/6** — Hors périmètre qualité, trade tactique uniquement.
7. **🔴 Earnings binaire dans 37 jours** — Fourchette EPS large.

### Positionnement Argus-IA (révisé)
- **Action : ATTENDRE**
- **Sizing :** — (aucune position recommandée)
- **Horizon :** — (suspendu)
- **Catalyseur clé court terme :** Récupération des données de cours + test du support $15.00
- **Catalyseur clé moyen terme :** Earnings 2026-07-23
- **Si cours confirmé > $15.00 sur données fiables :** Réactivation possible de la thèse ACHETER (Sizing Réduit)
- **Si cours confirmé < $14.50 :** Sortie définitive du setup haussier, passer à SURVEILLER
- **Si données non récupérées à 17h UTC :** Maintenir ATTENDRE, attendre snapshot 21h UTC

---

## [ANOMALIES]
- **Cours NaN** — Open/High/Low/Close tous null dans `data/latest.json`. Seul `previous_close` ($14.98) disponible.
- **Volume stale** — 178.76M identique au 15/06. Donnée probablement copiée et non actualisée.
- **Max Pain $1.00** — vs $10.00 hier. Écart de −93.3% vs spot implied ($14.98). Artefact de calcul évident.
- **Options Put/Call et Call OI nulls** — corruption data ou erreur de parsing.
- **ATR null, MM50 null** — impossible de calculer les niveaux ATR-based.
- **Sector rotation NaN généralisé** — Fichier `data/sector_rotation_2026-06-16.json` inutilisable (tous les returns et RS en NaN, tous les momentum_score à 10.0).
- **Social sentiment** : 0 mentions, label EXTREME_BEARISH = artefact scanner sans données.

## [DONNÉES PARTIELLES]
- Cours de session (open/high/low/close), ATR, MM50, MM200, MACD.
- Options (Put/Call, Call OI, IV Rank, earnings whisper).
- Volume de session fiable.
- Sector rotation (returns RS20/RS60).
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier indisponible pour AAL.
- Transcripts NLP, insider trades détaillés, 13F complets, ETF flows, dark pool.

---

## Références
- `data/latest.json` (snapshot 10:00 UTC) — Previous close $14.98, RSI 51.38, ATR null, MM50 null, volume 178.76M (suspect), short interest 11.39%, consensus FMP $16.60 (17 analysts), Forward P/E 6.94, options (Max Pain $1.00 aberrant, Put/Call null, Call OI null, expiration 2026-06-18)
- `data/recommandations_2026-06-16.json` — Score Opportunité 5.2/10 (C:5.3 V:4.5 M:6.0), Score Global 51.5/100, Recommandation ATTENDRE, Timing Neutre
- `data/sector_rotation_2026-06-16.json` — Données NaN généralisés, signal NEUTRAL (artefact)
- `data/validation_report.txt` (2026-06-16) — AAL non concerné (25/29 OK, 0 excluded)
- `data/geo_risk_latest.json` (2026-05-17) — AAL non flaggé
- `data/quant_report_latest.json` (2026-05-17) — Données quantitatives insuffisantes
- `data/quality_report_latest.json` (2026-05-17) — AAL non scanné
- Analyse précédente : `Actions/AAL/AAL_2026-06-15_update_21h00.md` (snapshot 21h UTC)
