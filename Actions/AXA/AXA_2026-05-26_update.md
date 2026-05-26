# AXA — Mise à jour Quotidienne (Snapshot 17h00 UTC)

> **Date :** 2026-05-26
> **Snapshot :** 2026-05-26T17:00:02 UTC
> **Type :** `_update.md` (post-pipeline matin)
> **Analyste :** Desk Argus-IA
> **Réf. précédent :** `AXA_2026-05-26_update.md` (snapshot 13h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 2026-05-26 13h00 | État 2026-05-26 17h00 | Changement |
|---------|----------------------|----------------------|------------|
| Cours | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 4 / 26 | **4 / 26** | Stable (AXA, AST, CYTOMX, QTBS) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | +1.01% | **0.00%** | **Mutation** (−1.01 pp) |
| XLF return 60j | −0.56% | **+1.26%** | **Mutation** (+1.82 pp) |
| XLF RS 20j vs SPY | −3.43% | **−4.74%** | **Dégradation** (−1.31 pp) |
| XLF RS 60j vs SPY | −9.03% | **−8.24%** | **Amélioration** (+0.79 pp) |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Earnings FMP | J0 (2026-05-26) | **J0 (2026-05-26)** | Date calendrier glissante, toujours sans détails |

**Verdict :** 14e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument non coté US). En revanche, **mutation sectorielle détectée** entre 13h00 et 17h00 UTC : le return 20j de XLF est passé de +1.01% à 0.00% et le return 60j de −0.56% à +1.26%, traduisant une dégradation de la force relative 20j (−3.43% → −4.74%) et un resserrement de l'écart sur 60j (−9.03% → −8.24%). Le momentum sectoriel reste à 0.0/10. La session US est active (volumes élevés sur AAPL 20.5M, AMD, NOK 138.9M) mais n'a pas permis la résolution du blocage de données pour AXA.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 17h00 UTC).

**Contexte sectoriel (XLF) :**
- Return 20j : 0.00% (vs SPY +4.74%)
- Return 60j : +1.26% (vs SPY +9.49%)
- RS 20j vs SPY : −4.74% (vs −3.43% à 13h00)
- RS 60j vs SPY : −8.24% (vs −9.03% à 13h00)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 4e/11 (ni top 3 ni bottom 3)

**Interprétation :** Le secteur financier a vu sa performance relative se dégrader sur 20j entre les deux snapshots du jour (−1.31 pp d'écart vs SPY), probablement sous l'effet de la rotation sectorielle vers la Tech (XLK return 20j +14.93%, momentum 10.0/10) et de l'absence de catalyseurs propres aux Financials. L'amélioration du return 60j (+1.26% vs −0.56%) atténue partiellement le headwind long terme mais ne modifie pas la tendance de sous-performance structurelle. Sans données AXA, on ne peut évaluer si le titre sur/sous-performe son secteur. Si les données AXA étaient disponibles, la dégradation RS 20j peserait légèrement sur le score Momentum.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-05-26) :**
- Source FMP signale un earnings à J0 mais sans estimates EPS/Revenue (`"details": "Earnings "`, `"severity": "high"`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données.

**Accounting Risk :** Fichier `data/accounting_risk_2026-05-26.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-05-26.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-05-26.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-05-26.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-05-26.json`) :
- Exposition FX : **25%** (export, primary currency USD)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned

**Géopolitique** (`geo_risk_2026-05-26.json`) :
- Aucun événement géopolitique spécifique à AXA détecté.
- Score politique global : 2/10 (🟢 bas), non exposé.

**Social Sentiment** (`social_sentiment_2026-05-26.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot précédent |
|-------|--------|--------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | Neutre | Stable |

**Pondération appliquée :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime macro inconnu → poids par défaut).

> **Règle de disqualification :** aucun score individuel ≤ 2/10 → le ticker n'est pas exclu du rapport, mais le manque de données empêche tout positionnement.

> **Note sur la significativité :** `quant_report_2026-05-26.json` indique 0 signaux historiques avec verdict, p-value = null → `[SIGNAUX NON SIGNIFICATIFS]`. Le score 55.2/100 est un placeholder algorithmique basé sur des valeurs par défaut (RSI 50, scores moyens) et ne constitue pas une recommandation investissable.

---

## Niveaux suggérés

**[NON CALCULABLES — MANQUE DE DONNÉES]**

- Prix actuel : `null`
- Prix d'entrée suggéré : `null`
- Stop-loss : `null`
- Take-profit : `null`
- Ratio R/R : `null`

Sans cours ni ATR, aucun niveau technique ne peut être établi de manière fiable.

---

## Conclusion — Thèse

| Verdict | Statut |
|---------|--------|
| **Thèse initiale** | Aucune — pas d'`_init.md` préalable |
| **Évolution** | **Non évaluable** (données de prix absentes + mutation sectorielle XLF entre 13h00 et 17h00) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Mutation sectorielle XLF détectée :** Entre 13h00 et 17h00 UTC, le return 20j de XLF est passé de +1.01% à 0.00% et le RS 20j de −3.43% à −4.74%. Le secteur Financials perd du terrain face à la Tech (XLK) en séance. Si les données AXA étaient disponibles, cette dégradation relative courte terme pourrait peser marginalement sur le score Momentum.
3. **Earnings J0 non résolu :** L'événement earnings du 2026-05-26 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré. Le passage à J+1 n'apportera pas d'information sans correction du symbole.
4. **Marché actif :** La session de trading US est ouverte et liquide aujourd'hui (volumes élevés sur AAPL 20.5M, NOK 138.9M) mais cela n'a pas permis la récupération de données pour AXA, confirmant que le problème est structurel (symbole) et non lié à la liquidité du marché.
5. **Qualité des données :** AXA fait toujours partie des 4 tickers KO sur 26. Tout scoring est non fiable.
6. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-26T17:00:02 UTC), `data/recommandations_2026-05-26.json`, `data/fx_exposure_2026-05-26.json`, `data/upcoming_events_2026-05-26.json`, `data/social_sentiment_2026-05-26.json`, `data/events_2026-05-26.json`, `data/sector_rotation_2026-05-26.json`, `data/geo_2026-05-26.json`, `data/quant_2026-05-26.json`.*
