# AXA — Mise à jour Quotidienne (Snapshot 21h00 UTC)

> **Date :** 2026-05-26
> **Snapshot :** 2026-05-26T21:00:02 UTC
> **Type :** `_update.md` (post-pipeline matin)
> **Analyste :** Desk Argus-IA
> **Réf. précédent :** `AXA_2026-05-26_update.md` (snapshot 17h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 2026-05-26 17h00 | État 2026-05-26 21h00 | Changement |
|---------|----------------------|----------------------|------------|
| Cours | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 3 / 26 | **3 / 26** | Stable (AXA, AST, QTBS) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | 0.00% | **+0.08%** | **Légère amélioration** (+0.08 pp) |
| XLF return 60j | +1.26% | **+1.33%** | **Légère amélioration** (+0.07 pp) |
| XLF RS 20j vs SPY | −4.74% | **−4.88%** | **Dégradation marginale** (−0.14 pp) |
| XLF RS 60j vs SPY | −8.24% | **−8.38%** | **Dégradation marginale** (−0.14 pp) |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Earnings FMP | J0 (2026-05-26) | **J0 (2026-05-26)** | Date calendrier glissante, toujours sans détails |

**Verdict :** 15e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument non coté US). Mutation sectorielle marginale entre 17h00 et 21h00 UTC : amélioration infime du return 20j (+0.08 pp) et 60j (+0.07 pp), mais dégradation du RS 20j (−4.74% → −4.88%) et RS 60j (−8.24% → −8.38%), traduisant une poursuite de la sous-performance relative du secteur Financials vs SPY. Le momentum sectoriel reste à 0.0/10. La session US est close (volumes confirmés : AAPL 46.6M, RKLB 31.5M, NOK 178.7M) sans résolution du blocage de données pour AXA.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 21h00 UTC).

**Contexte sectoriel (XLF) :**
- Return 20j : +0.08% (vs SPY +4.95%)
- Return 60j : +1.33% (vs SPY +9.72%)
- RS 20j vs SPY : −4.88% (vs −4.74% à 17h00)
- RS 60j vs SPY : −8.38% (vs −8.24% à 17h00)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 4e/11 (ni top 3 ni bottom 3)

**Interprétation :** Le secteur financier poursuit sa sous-performance relative vs le S&P 500. La dégradation du RS 20j (−0.14 pp) et RS 60j (−0.14 pp) entre 17h00 et 21h00 UTC est marginale mais confirme la tendance de distribution relative. La Tech (XLK return 20j +15.3%, momentum 10.0/10) continue de capter les flux au détriment des Financials. Sans données AXA, on ne peut évaluer si le titre sur/sous-performe son secteur. Si les données AXA étaient disponibles, cette dégradation relative légère peserait marginalement sur le score Momentum.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-05-26) :**
- Source FMP signale un earnings à J0 mais sans estimates EPS/Revenue (`"details": "Earnings "`, `"severity": "high"`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

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

**Géopolitique** (`geo_risk_latest.json`) :
- Aucun événement géopolitique spécifique à AXA détecté.
- Score politique global : 2/10 (🟢 bas), non exposé.

**Social Sentiment** (`social_sentiment_latest.json`) :
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

> **Note sur la significativité :** `quant_report_latest.json` indique 0 signaux historiques avec verdict, p-value = null → `[SIGNAUX NON SIGNIFICATIFS]`. Le score 55.2/100 est un placeholder algorithmique basé sur des valeurs par défaut (RSI 50, scores moyens) et ne constitue pas une recommandation investissable.

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
| **Évolution** | **Non évaluable** (données de prix absentes + dégradation sectorielle marginale XLF entre 17h00 et 21h00) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Dégradation sectorielle marginale :** Entre 17h00 et 21h00 UTC, le RS 20j de XLF est passé de −4.74% à −4.88% et le RS 60j de −8.24% à −8.38%. Le secteur Financials poursuit sa sous-performance relative vs le marché. Si les données AXA étaient disponibles, cette dégradation peserait marginalement sur le score Momentum.
3. **Earnings J0 non résolu :** L'événement earnings du 2026-05-26 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré.
4. **Marché actif mais close :** La session de trading US est close aujourd'hui (volumes confirmés élevés sur AAPL 46.6M, NOK 178.7M, RKLB 31.5M) mais n'a pas permis la récupération de données pour AXA, confirmant que le problème est structurel (symbole) et non lié à la liquidité du marché.
5. **Qualité des données :** AXA fait toujours partie des 3 tickers KO sur 26. Tout scoring est non fiable.
6. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-26T21:00:02 UTC), `data/recommandations_2026-05-26.json`, `data/fx_exposure_2026-05-26.json`, `data/upcoming_events_2026-05-26.json`, `data/social_sentiment_2026-05-26.json`, `data/events_2026-05-26.json`, `data/sector_rotation_2026-05-26.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`.*
