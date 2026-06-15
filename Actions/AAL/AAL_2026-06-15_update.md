# AAL — Mise à Jour 2026-06-15 (Snapshot 13h UTC)

**Date :** 2026-06-15 (snapshot 13h UTC)
**Ticker :** AAL (NASDAQ)
**Type :** Mise à jour post-pipeline 13h UTC — correction data quality options
**Cours :** $14.98
**Previous close :** $14.65 (+2.25% session)

> **Correction data quality majeure (13h UTC) :** Les données options (Put/Call, Call OI, Max Pain) sont désormais disponibles dans `data/latest.json`. Le Max Pain $1.00 aberrant du snapshot 10h est corrigé à **$10.00** — valeur plausible historiquement (range $9.50–$15.50) bien que très éloignée du spot ($14.98, −33%). Les données techniques et fondamentales restent inchangées vs snapshot 10h.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-15 10h UTC)

| Indicateur | 2026-06-15 10h UTC | 2026-06-15 13h UTC | Δ vs Prior |
|-----------|-------------------|-------------------|------------|
| Cours close | **$14.98** | **$14.98** | **Inchangé** |
| RSI 14j | 59.89 | **59.89** | **Inchangé** |
| ATR 14j | $0.66 | **$0.66** | **Inchangé** |
| MM 50j | $12.70 | **$12.70** | **Inchangé** |
| Volume (session) | 153.31M | **153.31M** | **Inchangé** — +65.2% vs moyenne 20j |
| Forward P/E | 6.72 | **6.72** | **Inchangé** |
| Consensus FMP PT | $16.60 (17 analystes) | **$16.60 (17 analystes)** | **Inchangé** |
| Short Interest | 11.39% | **11.39%** | **Inchangé** — squeeze fuel stable |
| Options Max Pain | $1.00 (ABERRANT) | **$10.00** | **CORRIGÉ** — valeur historiquement dans la fourchette AAL ($9.50–$15.50) mais $4.98 sous le spot |
| Options Put/Call | null (CORROMPU) | **1.69** | **CORRIGÉ** — skew baissier, moins extrême que le 1.92 du 08/06 |
| Options Call OI | null (CORROMPU) | **37.2%** | **CORRIGÉ** — modéré, entre le 34.2% du 08/06 et le 40.4% du 10/06 |
| Options Expiration | 2026-06-18 (J−3) | **2026-06-18 (J−3)** | **Inchangé** |
| Earnings Q2 (jours) | 38 | **38** | **Inchangé** — 2026-07-23 |
| Recommandation agent | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | **CONFIRMÉE** |
| Score Opportunité | 5.9/10 | **5.9/10** | **Inchangé** |
| Score Global ajusté | 63.5/100 | **63.5/100** | **Inchangé** |

**Verdict institutionnel :** La récupération des données options à 13h UTC résout l'anomalie majeure du snapshot 10h. Le setup technique, fondamental et macro reste parfaitement stable. Le Max Pain corrigé à **$10.00**, bien que loin du spot ($14.98), réintroduit un élément de vigilance : soit les dealers attendent un pin vers la baisse (irrationnel à J−3 sans catalyseur négatif majeur), soit le calcul Max Pain souffre d'un biais data quality résiduel (strikes OTM pondérés anormalement). Le Put/Call **1.69** confirme un skew baissier modéré — moins extrême que le 1.92 du 08/06, mais défensivement positionné. La thèse **ACHETER (Sizing Réduit)** reste intacte. L'incertitude gamma pour l'expiration du 18/06 est désormais quantifiable : si le Max Pain $10.00 est exact, le risque de pin baissier est théoriquement élevé, bien que contradictoire avec le momentum technique haussier.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $14.98 | 🟢 Inchangé — rally +10.1% depuis 10/06 confirmé, support $14.00 validé |
| RSI 14j | 59.89 | 🟢 Zone neutre favorable, sortie surachat saine conservée |
| ATR 14j | $0.66 | 🟢 Volatilité modérée, SL/TP fiables |
| MM 50j | $12.70 | 🟢 Cours +18.0% au-dessus, tendance haussière confirmée |
| MM 200j | null | 🔴 [DONNÉES MANQUANTES] |
| Volume session | 153.31M | 🟢 +65.2% vs moyenne 20j (92.80M) — participation institutionnelle soutenue |
| 52W Range | $10.09–$16.50 | 48.5% du 52W low, 9.2% sous le 52W high |
| Support clé | **$14.00** | 🟢 Validé — 3 closes consécutifs au-dessus |
| Support secondaire | **$13.66** | 🟢 SL ATR-based (2×ATR) |
| Support majeur | $12.77 | 🟡 Confluence MM50 ($12.70) + ancien gap |
| Résistance | $15.02 | 🟡 High du jour atteint le 15/06 — à breaker |
| Résistance majeure | $16.50 | 🟡 52W high + zone consensus PT haute |
| Short Interest | 11.39% | 🟡 Stable — squeeze potential intact |

**Interprétation technique — Setup inchangé, favorable :**
- Aucune variation technique entre 10h et 13h UTC. Le setup haussier reste validé : cours au-dessus de MM50 (+18.0%), RSI dans la zone neutre favorable (59.89), volume massif soutenant le rally.
- L'unique évolution est la disponibilité des données options, qui permet pour la première fois depuis le 10/06 d'évaluer le risque gamma pour l'expiration 18/06.
- **Verdict technique : FAVORABLE** — inchangé.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $16.60** (17 analystes, 2 mises à jour le mois dernier, 5 le trimestre dernier) — Inchangé depuis le 01/06.
- **Upside implicite : +10.8%** vs cours $14.98.
- **Couverture :** 17 analystes — stable.

### Ratios FMP — Inchangés
| Ratio | Valeur | Signal |
|-------|--------|--------|
| P/E (LTM, Yahoo) | 48.32 | 🔴 Élevé (charges récentes) |
| Forward P/E | 6.72 | 🟢 Asymétrie intacte, trade tactique attrayant |
| P/B (Yahoo) | −2.43 | 🔴 Equity négatif |
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

**Évolution fondamentale :** Aucun changement depuis 10h. Le Forward P/E 6.72 reste le principal argument valorisation pour un trade tactique. Le bilan reste extrêmement fragile (Filtre Qualité 0–1/6).

### Événement Clé — Earnings Q2 FY2026
- **Date :** 2026-07-23 (**38 jours**)
- **Estimates EPS :** −$0.34 à $0.52 (fourchette large)
- **Estimates Revenue :** $16.6B
- **Implication :** Binary event inchangé. Fenêtre d'entrée tactique en rétrécissement.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Inchangé :** PT moyen $16.60 (17 analystes). Aucune mise à jour depuis le 03/06.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions (No data). Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (artefact scanner sans données — à ignorer).

### Options — CORRECTION DATA QUALITY MAJEURE (13h UTC)
| Métrique | 10h UTC (corrompu) | 13h UTC (corrigé) | Interprétation |
|----------|-------------------|-------------------|----------------|
| Max Pain | $1.00 (ABERRANT) | **$10.00** | Corrigé. Historiquement dans la fourchette AAL ($9.50–$15.50) mais **$4.98 sous le spot** — écart inhabituel pour une expiration à J−3 |
| Put/Call ratio | null | **1.69** | Skew baissier modéré. Inférieur au 1.92 du 08/06 (moins défensif), supérieur au 1.42 du 03/06 (plus défensif) |
| Call OI % | null | **37.2%** | Modéré. Entre le 34.2% du 08/06 et le 40.4% du 10/06. Pas de setup gamma squeeze |
| Expiration | 2026-06-18 | **2026-06-18** | J−3 — risque gamma évaluable |

**Analyse institutionnelle des options corrigées :**
- **Max Pain $10.00 :** Cette valeur, bien que corrigée de l'aberration $1.00, pose une question méthodologique. Avec un spot à $14.98 et une expiration dans 3 jours, un Max Pain à $10 représente un écart de **−33.2%**. Historiquement, le Max Pain AAL a oscillé entre $9.50 (mai) et $15.50 (juin), mais était toujours proche du spot (±$1.50). Trois hypothèses :
  1. **Hypothèse data quality résiduelle** : le calcul Max Pain est biaisé par des strikes OTM profonds (PUT $10 fortement souscrits par des hedges de shorts) — la plus probable.
  2. **Hypothèse positioning institutionnel** : des dealers ont massivement vendu des calls $15/$16 et acheté des puts $10/$11, créant un pin synthétique vers la baisse — peu probable sans catalyseur négatif.
  3. **Hypothèse calculation artifact** : la formule Max Pain est sensible aux volumes extremes sur strikes éloignés (YOLO puts) — plausible sur AAL avec un retail actif.
- **Put/Call 1.69 :** Confirme une posture défensive modérée. Pour chaque 100 calls, il y a 169 puts. C'est cohérent avec le short interest élevé (11.39%) et le bilan fragile. Cependant, le ratio a baissé par rapport au 1.92 du 08/06, suggérant une légère atténuation de la prudence.
- **Call OI 37.2% :** La proportion d'Open Interest sur les calls est modérée. Ce n'est pas un setup de gamma squeeze (qui requiert typiquement >60% Call OI et Max Pain proche du spot). La distribution reste équilibrée-biaisée vers les puts.
- **Risque gamma J−3 :** Si le Max Pain est effectivement proche de $10 (hypothèse 1 retenue = artefact), le risque gamma est **négligeable** car le spot est trop loin. Si le Max Pain réel est proche de $15 (non observable avec les données actuelles), le risque serait élevé. En l'absence de certitude, le sizing réduit reste justifié.

### Sector Rotation — Inchangé
- **Industriels (XLI)** : return 20d **+0.96%**, RS20 vs SPY **+1.82%**, momentum score **3.89** (6ème sur 11 secteurs).
- **Signal global : NEUTRAL** — XLI ni dans le top3 ni dans le bottom3. Pas de malus sectoriel.

### Exposition Macro — Inchangée
| Facteur | Exposition | Signal |
|---------|-----------|--------|
| Taux 10Y US | 🔴 Élevée | Dette variable ~$40B, +1% = +$400M/an |
| Pétrole (WTI) | 🔴🔴 Critique | Jet fuel 25–30% coûts opérationnels |
| DXY | 🟡 Modérée | FX Exposure Score 0.0 (neutral), 25% revenus export |
| Industriels (XLI) | 🟡 Modérée | RS20 vs SPY +1.82% — neutre, pas de malus |

### Géopolitique — Inchangé
- **Score Politique :** AAL non flaggé dans `data/geo_risk_latest.json`. Aucun ajustement.

### Accounting Risk / Quant — Inchangé
- **Accounting risk :** Fichier indisponible. Pas d'alerte comptable.
- **Quant report :** Données insuffisantes (0 signaux historiques). Pas d'alerte de significativité.
- **Validation report 2026-06-15 :** AAL non concerné par les 5 errors / 2 warnings. [DONNÉES VALIDES].

---

## Score Opportunité Révisé

| Axe | 2026-06-15 10h UTC /10 | 2026-06-15 13h UTC /10 | Δ | Justification |
|-----|------------------------|------------------------|---|---------------|
| Catalyseur | 5.8 | **5.8** | **0.0** | Consensus stable, earnings J−38 inchangé, short interest stable. Pas de news. |
| Valorisation | 5.0 | **5.0** | **0.0** | Forward P/E 6.72 inchangé, Filtre Qualité 0–1/6 inchangé. Upside +10.8% stable. |
| Momentum | 7.3 | **7.3** | **0.0** | Données techniques inchangées (RSI 59.89, MM50 $12.70, volume +65.2%). Récupération options = confirmation setup, mais Max Pain $10 anomalie résiduelle = malus mineur annulant le bonus de data quality. |
| **Score Opportunité** | **5.9** | **5.9** | **0.0** | Pondération 35/40/25 (régime inconnu = default). Setup stable. |

**Score Global Composite agent :** 63.5/100
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Bonus : sectoriel 0 (XLI neutre)
- Timing : **Favorable**
- **Recommandation agent : ACHETER (Sizing Réduit)**
- **Recommandation institutionnelle Argus-IA : ACHETER (Sizing Réduit)** — maintenue

---

## Niveaux SL / TP — Inchangés

| | 2026-06-15 10h UTC | 2026-06-15 13h UTC | Justification |
|---|----------------------|----------------------|---------------|
| Entrée suggérée | $14.98 | **$14.98** | Cours actuel — setup technique inchangé |
| Stop-Loss | $13.66 | **$13.66** | Cours − 2×ATR ($14.98 − $1.32 = $13.66) |
| Take-Profit | $16.96 | **$16.96** | Cours + 3×ATR ($14.98 + $1.98 = $16.96). Aligné consensus PT $16.60 |
| Ratio R/R | 1.5 | **1.5** | Inchangé |

**Note institutionnelle :** Les niveaux sont inchangés vs 10h UTC. Le SL $13.66 est protégé par le support $14.00 et la MM50 $12.70. Si cours < $14.00 en close : sortie anticipée partielle (50%). Si cours < $13.66 : SL déclenché. Si cours > $15.50 sur volume > 100M : TP révisable à $17.50.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — Thèse ACHETER (Sizing Réduit) inchangée.**

Entre le snapshot 10h UTC et le snapshot 13h UTC, le seul changement matériel est la **correction data quality des options**. Ce changement n'altère ni ne renforce de manière décisive la thèse :
- **Pas de renforcement** : le Max Pain $10.00, bien que corrigé, est éloigné du spot et introduit une incertitude méthodologique. Le Put/Call 1.69 reste défensif.
- **Pas d'affaiblissement** : les données techniques, fondamentales, consensus, volume et macro sont strictement identiques. Le setup haussier reste intact.
- **Conclusion** : la thèse est **maintenue à l'identique** avec la même prudence (sizing réduit) motivée par le bilan fragile et l'incertitude residuelle sur le Max Pain.

### Ce qui a changé (13h UTC vs 10h UTC) :
1. **🟢 Options corrigées** : Max Pain $10.00 (vs $1.00 aberrant), Put/Call 1.69 (vs null), Call OI 37.2% (vs null). L'anomalie data quality est résolue.
2. **🟡 Max Pain $10.00 éloigné du spot** : −33% sous le cours. Probable artefact de calcul (strikes OTM pondérés) mais à monitorer.

### Ce qui n'a PAS changé (et reste valide) :
1. Cours $14.98, RSI 59.89, ATR $0.66, MM50 $12.70 — setup technique inchangé.
2. Consensus $16.60 (17 analystes), Forward P/E 6.72 — fondamentaux inchangés.
3. Volume 153.31M (+65.2% vs moyenne) — participation soutenue.
4. Short interest 11.39% — squeeze fuel stable.
5. Bilan extrêmement fragile — Filtre Qualité 0–1/6.
6. Earnings Q2 dans 38 jours — binary event inchangé.
7. Score Global 63.5/100, Score Opportunité 5.9/10 — scoring inchangé.
8. XLI neutre, FX 0.0, geo non flaggé — malus/bonus inchangés.

### Risques identifiés (inchangés)
1. **🔴 Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value négatif.
2. **🔴 Value trap** — Forward EPS ~$2.23/share peut ne pas se matérialiser.
3. **🟡 Incertitude Max Pain** — Le $10.00 est plausible historiquement mais éloigné du spot. Si réel = risque gamma non évalué ; si artefact = data quality résiduelle.
4. **🔴 Filtre Qualité 0–1/6** — Hors périmètre qualité, trade tactique uniquement.
5. **🟡 Earnings binaire dans 38 jours** — Fourchette EPS large.

### Positionnement Argus-IA (inchangé)
- **Action : ACHETER (Sizing Réduit)**
- **Sizing max :** Réduit (capital exposé limité, Filtre Qualité 0–1/6)
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 + réaction post-announcement)
- **Catalyseur clé court terme :** Aucun — maintien du momentum technique.
- **Catalyseur clé moyen terme :** Earnings 2026-07-23.
- **Si cours < $14.00 en close :** Sortie anticipée partielle (50%).
- **Si cours < $13.66 :** SL déclenché.
- **Si cours < $12.77 :** Invalidation complète du setup haussier.
- **Si cours > $15.50 sur volume > 100M :** Réévaluer le momentum. TP révisable à $17.50.

---

## [ANOMALIE]
- **Max Pain $10.00 à J−3** — Écart de −33% vs spot ($14.98). Probable artefact de calcul (ponderation anormale de strikes OTM profonds) ou data quality residuelle. Valeur historiquement dans le range AAL ($9.50–$15.50) mais atypique par rapport au spot actuel.
- **MM200 null** dans `data/latest.json` — impossibilité d'évaluer la tendance long terme.
- **Social sentiment** : 0 mentions, label EXTREME_BEARISH = artefact scanner sans données.

## [DONNÉES PARTIELLES]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 13:00 UTC) — Cours $14.98, RSI 59.89, ATR $0.66, MM50 $12.70, volume 153.31M, short interest 11.39%, consensus FMP $16.60 (17 analysts), Forward P/E 6.72, options (Max Pain $10.00, Put/Call 1.69, Call OI 37.2%, expiration 2026-06-18)
- `data/recommandations_2026-06-15.json` — Score Opportunité 5.9/10 (C:5.8 V:5.0 M:7.3), Score Global 63.5/100, Recommandation ACHETER (Sizing Réduit), SL $13.66, TP $16.96, R/R 1.5
- `data/sector_rotation_2026-06-15.json` — XLI return 20d +0.96%, RS20 vs SPY +1.82%, momentum_score 3.89, signal NEUTRAL
- `data/fx_exposure_2026-06-15.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-15.json` — Sentiment retail 0 mentions (No data)
- `data/upcoming_events_2026-06-15.json` — Earnings 2026-07-23, 38 jours, Est EPS −$0.34 à $0.52, Rev $16.6B
- `data/events_2026-06-15.json` — Aucun événement corporate détecté
- `data/geo_risk_latest.json` — AAL non flaggé
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
- `data/validation_report.txt` (2026-06-15 12:07 UTC) — AAL non concerné (25/29 OK, 0 excluded)
- Analyse précédente : `Actions/AAL/AAL_2026-06-15_update.md` (snapshot 10h UTC)
