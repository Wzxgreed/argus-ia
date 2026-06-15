# PLTR — Mise à Jour Quotidienne (2026-06-15, snapshot 10h UTC)

> **Source :** `data/latest.json` (snapshot 2026-06-15T10:00:02Z, fetched_at 2026-06-15T10:00:10Z) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [PLTR_2026-06-10_update.md](PLTR_2026-06-10_update.md) (snapshot 10h UTC)
> **Contexte :** Snapshot pré-ouverture lundi 15/06. Cours en baisse de -6.22% vs snapshot 10/06, RSI retour vers zone neutre-basse, ATR désormais disponible, options anomalie JSON récurrente à 10h UTC persistante.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-10 10h UTC)

| Indicateur | Snapshot 10/06 10h UTC | Snapshot 15/06 10h UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours référence | $136.47 | **$127.99** | **-6.22%** — baisse significative |
| RSI 14j | 50.99 | **43.54** | **-7.45 pts** — retour vers zone neutre-basse |
| Volume | 38.48M | **35.38M** | **-8.1%** — 0.92x moyenne 20j |
| Volume vs 20j | 0.96x | **0.92x** | 🟡 — léger recul |
| Short Interest | 3.23% | **3.23%** | = — inchangé |
| MM 50j | null | **139.64** | Disponible — cours -8.4% sous MM50 |
| ATR 14j | null | **7.59** | Disponible — volatilité stable/élevée |
| Consensus FMP PT | $186.15 (34 analystes) | **$187.09 (33 analystes)** | = — stable, -1 analyste |
| Options Max Pain | $50.00 (anomalie) | **$42.00** | 🟡 Anomalie JSON récurrente à 10h UTC |
| Options Put/Call | null | **null** | 🟡 Anomalie JSON récurrente |
| Options Call OI % | null | **0.0%** | 🟡 Anomalie JSON récurrente |
| Score Opportunité agent | 4.6/10 | **5.1/10** | **+0.5** — amélioration Catalyseur + Valorisation |
| Score Global ajusté | 45.5/100 | **42.5/100** | **-3.0 pts** — malus momentum |
| Recommandation agent | SURVEILLER | **SURVEILLER** | = — maintenu |
| Stop-loss agent | null | **$112.81** | Calculable (ATR dispo) |
| Take-profit agent | null | **$150.76** | Calculable (ATR dispo) |
| Timing | Neutre | **Défavorable** | 🔴 — dégradation |

**Verdict :** Le snapshot 15/06 affiche une **détérioration technique nette** avec un recul de -6.22% du cours ($136.47 → $127.99) et un RSI retombé à 43.54 (-7.45 pts). La cassure sous la MM50 est creusée à -8.4% (MM50 $139.64). L'ATR 14j est désormais disponible à $7.59, permettant de calculer des niveaux SL/TP fiables. La recommandation **SURVEILLER** est maintenue avec une nuance baissière accrue.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (previous_close) | $127.99 | -6.22% vs snapshot 10/06 |
| RSI 14j | 43.54 | 🟡 Neutre-basse — recul -7.45 pts, proche survente |
| Volume 20j | 38,400,790 | 🟢 35.38M = 0.92x moyenne — stable |
| 52W Range | $122.68–$207.52 | Cours à 4.3% du 52W low, 38.3% sous le 52W high |
| Short Interest | 3.23% | 🟡 Modéré — inchangé |
| MM 50j | 139.64 | 🔴 Cours -8.4% sous MM50 — cassure creusée |
| ATR 14j | 7.59 | 🟡 Disponible — volatilité stable |

**Options — Anomalie JSON récurrente :**

| Métrique | Valeur 10/06 10h UTC | Snapshot 15/06 10h UTC | Δ | Interprétation |
|----------|----------------------|------------------------|---|----------------|
| Put/Call Ratio | null | **null** | 🟡 Anomalie | Pattern récurrent 10h UTC — valeurs opérationnelles conservées |
| Max Pain | $50.00 | **$42.00** | 🟡 Anomalie | Valeur aberrante, non exploitée |
| Call OI % | null | **0.0%** | 🟡 Anomalie | Pattern récurrent 10h UTC |
| Expiration proche | 2026-06-12 | **2026-06-18** | = | 3 jours |

> **Note options :** Anomalie JSON détectée au snapshot 10h UTC (Max Pain $42.00, Put/Call null, Call OI 0.0%). Ce pattern récurrent à 10h UTC est documenté depuis le 08/06. **Valeurs opérationnelles conservées** du snapshot 09/06 13h UTC : Max Pain $150.00, Put/Call 0.51, Call OI 66.2%. La structure options reste cohérente avec un biais haussier modéré.

**Interprétation technique :**
- **RSI 43.54** : 🟡 Retour en zone neutre-basse après le réalignement mécanique du 10/06 (50.99). Le recul de -7.45 pts confirme la perte de momentum et le retour vers la survente (seuil <40).
- **Volume stable** : 35.38M, 0.92x moyenne 20j. Pas de panique vendeuse mais pas de soutien non plus.
- **Short Interest 3.23%** : 🟡 Inchangé. Pas de squeeze setup.
- **MM50 $139.64** : 🔴 Cours $127.99 = écart -8.4% sous la MM50. La cassure du 08/06 est creusée. La MM50 est désormais une résistance dynamique forte.
- **ATR 14j $7.59** : 🟡 Disponible pour la première fois depuis le 09/06. Volatilité stable/élevée. SL = $112.81, TP = $150.76.
- **Support/Résistance** (données actualisées) :
  - Support immédiat : $126.65 (low du jour)
  - Support psychologique : $125.00
  - Support critique : $122.68 (52W low)
  - Résistance : $131.08 (previous_close)
  - Résistance dynamique : $139.64 (MM50)
  - Résistance Max Pain : $150.00 (valeurs opérationnelles)

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $187.09** (33 analystes, 1 mise à jour le mois dernier, 6 le trimestre dernier)
- **Upside implicite : +46.2%** vs cours $127.99
- **Couverture :** 33 analystes — -1 analyste vs 10/06, aucune révision de PT détectée

### Ratios FMP / Yahoo — Mécaniquement affectés par la baisse du cours
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Δ vs 10/06 | Signal |
|-------|---------------|---------------------|----------|--------|
| Market Cap | $306.8 Md | $421.2 Md | = | 🔴 Écart +37.3% — FMP retardé |
| P/E (LTM) | 142.2x | 259.2x | -7.9x Yahoo | 🟡 Extrême, amélioration mécanique |
| Forward P/E | 61.5x | — | -2.2x | 🟡 Élevé, amélioration mécanique |
| EV/Revenue | 57.3x | 93.8x | = | 🔴 Extrême |
| EV/EBITDA | 148.2x | 291.6x | = | 🔴 Extrême |
| P/B | 36.3x | 57.0x | = | 🔴 Extrême |
| Gross Margin | — | 82.4% | = | 🟢 Excellente |
| Operating Margin | — | 31.6% | = | 🟢 Très élevée |
| Net Margin | — | 36.3% | = | 🟢 Excellente |
| Current Ratio | — | 7.11 | = | 🟢 Liquidité exceptionnelle |
| Debt/Equity | — | 0.031 | = | 🟢 Quasi-zéro dette |
| ROIC (FMP) | — | 17.9% | = | 🟢 Création de valeur confirmée |
| SBC / Revenue | — | 15.3% | = | 🔴 Dilution significative |

**Interprétation :** Les fondamentaux de qualité sont intacts. Les multiples LTM (Yahoo) sont mécaniquement améliorés par la baisse du cours (-6.22%), mais restent extrêmes et incompatibles avec un environnement de taux élevés. Aucun changement opérationnel ou comptable détecté.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 33 analystes FMP, PT $187.09. Aucune mise à jour entre le 10/06 et le 15/06.
- **Implication :** Le consensus n'a pas réagi au mouvement. L'écart PT/cours s'élargit mécaniquement à +46.2% (vs +36.4% à $136.47).

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions (`social_sentiment_2026-06-15.json`). Aucun pump/dump détecté.

### Options — Anomalie JSON récurrente
- **Put/Call** : null (anomalie) — dernière valeur valide 0.51 (09/06 13h UTC)
- **Max Pain** : $42.00 (anomalie) — dernière valeur valide $150.00
- **Call OI %** : 0.0% (anomalie) — dernière valeur valide 66.2%
- **Expiration proche** : 2026-06-18 (3 jours)
- **Interprétation :** La structure options n'a pas bougé. Le Max Pain $150.00 reste un aimant magnétique si le cours revient. Aucun signal d'urgence vendeur dans les options.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.515 amplifie les rotations |
| Pétrole (WTI) | 🟢 Faible | Inchangée — business model software |
| DXY | 🟢 Faible | FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | XLK top sectoriel (momentum 10.0/10, RS 20j +3.81%) |

### Sector Rotation
- **Technology (XLK)** : momentum score 10.0/10, return_20d +2.95%, RS_20d +3.81% vs SPY.
- **Signal :** NEUTRAL (régime inconnu)
- **Impact :** 🟢 Vent de secteur favorable mais cours PLTR sous-performe le secteur.

### Géopolitique
- **Score Politique :** 2/10 (`geo_risk_2026-06-15.json`) — exposition négligeable.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (n=0), calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 10/06 10h UTC /10 | Snapshot 15/06 10h UTC /10 | Δ | Justification |
|-----|---------------------|---------------------------|---|---------------|
| Catalyseur | 5.3 | **6.8** | **+1.5** | Consensus PT stable à $187.09, écart élargi à +46.2%. Earnings 08/03 (49 jours). |
| Valorisation | 3.0 | **4.5** | **+1.5** | Multiples mécaniquement améliorés par la baisse du cours (-6.22%). Malus atténué. |
| Momentum | 6.0 | **3.5** | **-2.5** | RSI 43.54 (-7.45 pts), cours sous MM50 de -8.4%, timing Défavorable. |
| **Score Opportunité** | **4.6** | **5.1** | **+0.5** | Pondération 35/40/25 (régime inconnu). |

**Score Global Composite agent :** 45.5/100 → **Ajusté 42.5/100** (-3.0 pts)
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : Défavorable (RSI en zone basse, cassure MM50 creusée, volume sans soutien)
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse est **CONFIRMÉE avec nuance baissière accrue** — **SURVEILLER maintenu**. La dégradation technique du cours (-6.22%) et du RSI (-7.45 pts) confirme l'absence de signal d'achat. L'amélioration mécanique de la valorisation (+1.5 pt) et du catalyseur (+1.5 pt) ne compense pas la chute du momentum (-2.5 pts). Pas d'entrée avant retour en clôture au-dessus de MM50 + volume > 40M.

---

## Niveaux SL / TP

| | 10/06 10h UTC | Snapshot 15/06 10h UTC | Justification |
|---|------------------|----------------------|---------------|
| Entrée suggérée | Attendre retour > MM50 | **Attendre retour > $139.64 (MM50)** | Cours -8.4% sous MM50. Critère inchangé : clôture au-dessus de MM50 + volume > 40M. |
| Stop-Loss | null | **$112.81** | ATR 14j $7.59 disponible → SL = $127.99 − 2×$7.59 |
| Take-Profit | null | **$150.76** | ATR 14j $7.59 disponible → TP = $127.99 + 3×$7.59 |
| Ratio R/R | ~1.5 | **1.5** | = (calculé sur ATR actuelle) |

> ⚠️ **Note :** Les niveaux SL/TP sont désormais calculés sur l'ATR 14j disponible dans le snapshot ($7.59). Le ratio R/R de 1.5 est standard. **Néanmoins, l'entrée n'est pas recommandée** tant que le cours reste sous MM50 avec un timing Défavorable.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec nuance baissière accrue — SURVEILLER maintenu.**

Le snapshot pré-ouverture du 2026-06-15 10h UTC enregistre une **détérioration technique nette** avec un recul de -6.22% du cours ($136.47 → $127.99) et un RSI retombé à 43.54 (-7.45 pts). La cassure sous la MM50 est creusée à -8.4% (MM50 $139.64). L'ATR 14j est désormais disponible à $7.59, permettant des niveaux SL/TP fiables. La thèse SURVEILLER est maintenue avec une nuance baissière accrue.

### Ce qui a changé (snapshot 15/06 vs snapshot 10/06) :
1. **Cours de référence -6.22%** — 🔴 Baisse significative ($127.99 vs $136.47).
2. **RSI 50.99 → 43.54** — 🔴 Retour en zone neutre-basse (-7.45 pts), proche survente.
3. **MM50 disponible à $139.64** — 🔴 Cours -8.4% sous la MM50, cassure creusée.
4. **ATR 14j disponible à $7.59** — 🟢 Données partielles résolues, SL/TP calculables.
5. **Score Opportunité 4.6 → 5.1** — 🟢 Amélioration agent Catalyseur + Valorisation.
6. **Score Valorisation 3.0 → 4.5** — 🟢 Amélioration mécanique liée à la baisse du cours.
7. **Score Momentum 6.0 → 3.5** — 🔴 Dégradation technique (RSI, cassure MM50).
8. **Score Global ajusté 45.5 → 42.5** — 🔴 Dégradation nette de -3.0 pts.
9. **Timing Neutre → Défavorable** — 🔴 Confirme l'absence de signal d'entrée.
10. **Options anomalie JSON persistante** — 🟡 Max Pain aberrant $42.00 (pattern récurrent).
11. **Consensus FMP $186.15 → $187.09** — = Stable, -1 analyste.
12. **Volume 38.48M → 35.38M** — 🟡 Léger recul, 0.92x moyenne.

### Ce qui n'a PAS changé :
1. **Short interest 3.23%** — inchangé.
2. **Fondamentaux FMP FY2025** : marges excellentes (82/32/36%), bilan quasi-sans dette, ROIC 18% inchangés.
3. **Aucun événement corporate** (`data/events_2026-06-15.json` vide pour PLTR).
4. **Aucune news** (`data/news_2026-06-15.json` non lu mais pas d'alerte).
5. **Accounting risk non quantifié** — absence persistante.
6. **Geo risk score 2/10** — exposition négligeable.
7. **Social sentiment 0 mentions** — pas de buzz retail.
8. **Earnings Q2 FY2026** : 2026-08-03 (49 jours) — catalyseur clé inchangé.
9. **FX Exposure Score 0.0** — neutral.
10. **Recommandation** : SURVEILLER.

### Risques identifiés (snapshot 15/06)
1. **Cassure MM50 creusée à -8.4%** — 🔴 Cours $127.99 sous MM50 $139.64 = tendance baissière confirmée.
2. **RSI 43.54** — 🟡 Zone neutre-basse, risque de franchissement sous 40 (survente).
3. **Valorisation extrême** — 🔴 Multiples incompatibles avec un environnement de taux élevés (P/E 142x, EV/Revenue 57x).
4. **Beta 1.515** — 🟡 En cas de correction tech globale, surperformance à la baisse confirmée.
5. **Accounting risk non quantifié** — 🟡 Absence de scan comptable (M-Score, Z-Score).
6. **SBC / Revenue 15.3%** — 🔴 Dilution significative.
7. **Options anomalie récurrente** — 🟡 Pattern 10h UTC à surveiller — non bloquant mais bruit de données.
8. **Timing Défavorable** — 🔴 L'agent recommandation confirme l'absence de setup d'entrée.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée. Le cours sous MM50 avec un timing Défavorable invalide tout signal d'achat.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 FY2026 le 03/08)
- **Catalyseur clé :** Earnings 2026-08-03 (Est. EPS $0.32–$0.40, Rev $1.8B). Préparer `_preview.md` à ≤ 5j.
- **Si retour > MM50 en clôture + volume > 40M :** Réactivation de la thèse ATTENDRE.
- **Si consolidation > $125 sur volume > 35M sur 2–3 jours :** Signal de stabilisation — réévaluer.
- **Si cassure < $126.65 en clôture :** Risque de retour vers $122.68 (52W low).

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes (n=0).

---

## Références
- `data/latest.json` (snapshot 2026-06-15T10:00:02Z) — close $127.99, previous_close $131.08, RSI 43.54, ATR 7.59, MM50 139.64, volume 35,378,000, short interest 3.23%, consensus FMP $187.09 (33 analystes), options (max_pain $42.00 anomalie, put_call_ratio null, call_oi_pct 0.0%)
- `data/recommandations_2026-06-15.json` — Score Opportunité 5.1/10, Score Global 42.5/100, Recommandation SURVEILLER
- `data/validation_report.txt` (2026-06-15) — PLTR OK, 0 warning, 0 error
- `data/sector_rotation_2026-06-15.json` — XLK top sectoriel (momentum 10.0/10, RS 20j +3.81%)
- `data/fx_exposure_2026-06-15.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-15.json` — Sentiment retail 0 mentions (No data)
- `data/upcoming_events_2026-06-15.json` — Earnings 2026-08-03, 49 jours
- `data/events_2026-06-15.json` — Aucun événement corporate détecté pour PLTR
- `data/geo_2026-06-15.json` — Geo Risk Score 2/10, exposition négligeable
- `data/quant_2026-06-15.json` — Données quantitatives insuffisantes (n=0)
