# AXA — Mise à jour Quotidienne (Snapshot 13h00 UTC)

> **Date :** 2026-05-26
> **Snapshot :** 2026-05-26T13:00:16 UTC
> **Type :** `_update.md` (post-pipeline matin)
> **Analyste :** Desk Argus-IA
> **Réf. précédent :** `AXA_2026-05-26_update.md` (snapshot 10h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 2026-05-26 10h00 | État 2026-05-26 13h00 | Changement |
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
| XLF return 20j | +1.01% | **+1.01%** | **Stable** |
| XLF return 60j | −0.56% | **−0.56%** | **Stable** |
| XLF RS 20j vs SPY | −3.43% | **−3.43%** | **Stable** |
| XLF RS 60j vs SPY | −9.03% | **−9.03%** | **Stable** |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Earnings FMP | J0 (2026-05-26) | **J0 (2026-05-26)** | Date calendrier glissante, toujours sans détails |

**Verdict :** 13e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible. Les métriques sectorielles XLF sont strictement inchangées vs le snapshot 10h00 UTC (return 20j +1.01%, RS 20j −3.43%, momentum 0.0/10). La session US est ouverte et active (volume élevé sur AAPL, AMD, NOK) mais cela n'a pas permis la résolution du blocage de données pour AXA.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 13h00 UTC).

**Contexte sectoriel (XLF) :**
- Return 20j : +1.01% (vs SPY +4.44%)
- Return 60j : −0.56% (vs SPY +8.47%)
- RS 20j vs SPY : −3.43% (stable vs 2026-05-26 10h00)
- RS 60j vs SPY : −9.03% (stable vs 2026-05-26 10h00)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 5e/11 (ni top 3 ni bottom 3)

**Interprétation :** Le secteur financier est stable vs le snapshot précédent. Sans données AXA, on ne peut évaluer si le titre sur/sous-performe son secteur. Le headwind sectoriel persiste : SPY surperforme XLF de +3.4pp sur 20j. Si les données AXA étaient disponibles, ce contexte peserait sur le score Momentum. L'activité du marché US aujourd'hui (volumes élevés sur plusieurs tickers) n'a pas généré de nouvelle information de prix pour ce ticker.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-05-26) :**
- Source FMP signale un earnings à J0 mais sans estimates EPS/Revenue (`"details": "Earnings "`, `"severity": "high"`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` toujours absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

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

**Géopolitique** (`geo_risk_latest.json`, date 2026-05-17) :
- Aucun événement géopolitique spécifique à AXA détecté.
- Score politique global non calculé pour ce ticker (absent du JSON).

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

> **Note sur la significativité :** `quant_report_latest.json` (2026-05-17) indique 0 signaux historiques avec verdict, p-value = 1.0 → `[SIGNAUX NON SIGNIFICATIFS]`. Le score 55.2/100 est un placeholder algorithmique basé sur des valeurs par défaut (RSI 50, scores moyens) et ne constitue pas une recommandation investissable.

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
| **Évolution** | **Non évaluable** (données de prix absentes + headwind sectoriel stable + marché actif sans impact sur le sourcing) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Earnings J0 non résolu :** L'événement earnings du 2026-05-26 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré. Le passage à J+1 n'apportera pas d'information sans correction du symbole.
3. **Headwind sectoriel stable :** Le secteur Financials (XLF) sous-performe le S&P 500 de −3.43% sur 20j et −9.03% sur 60j. Le momentum score reste à 0.0/10. Si les données AXA étaient disponibles, ce contexte sectoriel peserait sur le score Momentum.
4. **Marché actif :** La session de trading US est ouverte et liquide aujourd'hui (volumes élevés sur AAPL 43.6M, AMD 34.7M, NOK 127.4M) mais cela n'a pas permis la récupération de données pour AXA, confirmant que le problème est structurel (symbole) et non lié à la liquidité du marché.
5. **Qualité des données :** AXA fait toujours partie des 4 tickers KO sur 26. Tout scoring est non fiable.
6. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-26T13:00:02 UTC), `data/recommandations_latest.json`, `data/fx_exposure_2026-05-26.json`, `data/upcoming_events_2026-05-26.json`, `data/social_sentiment_2026-05-26.json`, `data/events_2026-05-26.json`, `data/sector_rotation_2026-05-26.json`, `data/geo_risk_latest.json` (2026-05-17), `data/quant_report_latest.json` (2026-05-17).*
