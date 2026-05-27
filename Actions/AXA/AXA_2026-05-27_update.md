# AXA — Mise à jour Quotidienne (Snapshot 13h00 UTC)

> **Date :** 2026-05-27
> **Snapshot :** 2026-05-27T13:00:02 UTC
> **Type :** `_update.md` (post-pipeline matin)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-05-27_update.md` (snapshot 10h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 2026-05-27 10h00 | État 2026-05-27 13h00 | Changement |
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
| XLF return 20j | +0.08% | **+0.08%** | **Stable** |
| XLF return 60j | +1.33% | **+1.33%** | **Stable** |
| XLF RS 20j vs SPY | −4.88% | **−4.88%** | **Stable** |
| XLF RS 60j vs SPY | −8.38% | **−8.38%** | **Stable** |
| XLF momentum score | 0.0/10 | **0.0/10** | **Stable** |
| Earnings FMP | J0 (2026-05-27) | **J0 (2026-05-27)** | Date calendrier glissante, toujours sans détails |

**Verdict :** 17e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument non coté US). Le contexte sectoriel XLF est strictement inchangé vs le snapshot 10h00 UTC : RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10. La session US midday (13h00 UTC) n'a pas permis la récupération de données pour AXA. L'absence totale de mutation entre 10h00 et 13h00 UTC confirme le caractère structurel du problème de symbole et l'inertie du secteur financier en séance.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-05-27T13:00:02 UTC).

**Contexte sectoriel (XLF) — stabilité totale vs snapshot 10h00 UTC :**
- Return 20j : +0.08% (vs SPY +4.95%)
- Return 60j : +1.33% (vs SPY +9.72%)
- RS 20j vs SPY : −4.88% (inchangé)
- RS 60j vs SPY : −8.38% (inchangé)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 4e/11 (ni top 3 ni bottom 3)

**Interprétation :** Le secteur financier maintient sa sous-performance relative vs le S&P 500 à des niveaux strictement identiques à ceux observés à 10h00 UTC. Aucune mutation technique sectorielle n'est survenue en séance US entre 10h00 et 13h00 UTC. La Tech (XLK return 20j +15.3%, momentum 10.0/10) continue de capter les flux au détriment des Financials. Sans données AXA, on ne peut évaluer si le titre sur/sous-performe son secteur. Si les données AXA étaient disponibles, cette stabilité sectorielle laisserait le score Momentum inchangé.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-05-27) :**
- Source FMP signale un earnings à J0 mais sans estimates EPS/Revenue (`"details": "Earnings "`, `"severity": "high"`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-05-27.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-05-27.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-05-27.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-05-27.json`) :
- Exposition FX : **25%** (export, primary currency USD)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned

**Géopolitique** (`geo_risk_latest.json`) :
- Aucun événement géopolitique spécifique à AXA détecté.
- Score politique global : 2/10 (🟢 bas), non exposé.

**Social Sentiment** (`social_sentiment_2026-05-27.json`) :
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

> **Note sur la significativité :** `quant_report_latest.json` indique 0 signaux historiques avec verdict, p-value = 1.0 → `[SIGNAUX NON SIGNIFICATIFS]`. Le score 55.2/100 est un placeholder algorithmique basé sur des valeurs par défaut (RSI 50, scores moyens) et ne constitue pas une recommandation investissable.

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
| **Évolution** | **Non évaluable** (données de prix absentes + stabilité totale sectorielle XLF entre 10h00 et 13h00 UTC) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Stabilité sectorielle totale en séance :** Entre 10h00 et 13h00 UTC, les métriques XLF sont strictement identiques : RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10. Aucune mutation technique sectorielle n'est survenue en séance US. Le secteur Financials reste en phase de distribution relative vs le marché.
3. **Earnings J0 non résolu :** L'événement earnings du 2026-05-27 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré. C'est le 4e jour consécutif où le calendrier FMP glisse la date J0 sans fournir de détails exploitables.
4. **Marché actif en séance :** Le snapshot 13h00 UTC confirme que les données de prix US (AAPL 47.9M, NOK 188.9M, RKLB 32.8M) sont bien récupérées, isolant AXA comme l'un des 3 tickers structurellement KO sur 26.
5. **Qualité des données :** AXA fait toujours partie des 3 tickers KO sur 26. Tout scoring est non fiable.
6. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-27T13:00:02 UTC), `data/recommandations_2026-05-27.json`, `data/fx_exposure_2026-05-27.json`, `data/upcoming_events_2026-05-27.json`, `data/social_sentiment_2026-05-27.json`, `data/events_2026-05-27.json`, `data/sector_rotation_2026-05-27.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`.*
