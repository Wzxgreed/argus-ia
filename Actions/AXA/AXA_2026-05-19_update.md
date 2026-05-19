# AXA — Mise à jour Quotidienne (Snapshot 21h00 UTC)

> **Date :** 2026-05-19
> **Snapshot :** 2026-05-19T21:00:14 UTC
> **Type :** `_update.md` (flash post-pipeline 21h00)
> **Analyste :** Desk Argus-IA
> **Réf. précédent :** `AXA_2026-05-19_update.md` (snapshot 17h00)

---

## Résumé des changements depuis le snapshot 17h00

| Élément | État 17h00 | État 21h00 | Changement |
|---------|-----------|------------|------------|
| Cours | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| Volume | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| Tickers KO pipeline | 3 / 25 | **3 / 25** | Stable (AST, AXA, CYTOMX) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | Stable |
| Score Global | 55.2/100 | **55.2/100** | Stable |
| Recommandation | ATTENDRE | **ATTENDRE** | Confirmée |
| Timing | Neutre | **Neutre** | Stable |
| XLF return 20j | −1.52% | **−2.29%** | 🔴 Dégradation −77 bp |
| XLF return 60j | +2.05% | **+1.25%** | 🔴 Réduction +80 bp |
| XLF RS 20j vs SPY | −6.06% | **−6.51%** | 🔴 Dégradation −45 bp |
| XLF RS 60j vs SPY | −6.11% | **−6.57%** | 🔴 Dégradation −46 bp |
| XLF momentum score | 0.0/10 | **0.0/10** | Stable (dernier du classement) |
| Earnings | J0 (2026-05-19) | **J0 (2026-05-19)** | Confirmé, non résolu |

**Alerte pipeline :** AXA fait toujours partie des **3 tickers KO** sur 25 (`AST`, `AXA`, `CYTOMX`). `data/latest.json` enregistre `error: true`, `reason: "No price history"` à 21:00:14 UTC. Aucune métrique technique ou fondamentale brute n'est exploitable.

---

## Mise à jour technique

**[DONNÉES MANQUANTES — NON SOURCÉ]**

- Cours : non disponible (`latest.json` → `error: true`, `reason: No price history`)
- RSI 14j : non disponible
- ATR 14j : non disponible → SL/TP non calculables
- MM 50j / 200j : non disponibles
- Volume relatif vs moy. 20j : non disponible
- Supports / Résistances : non identifiables

**Headwind sectoriel actualisé :** Le secteur Financials (XLF) a subi une légère dégradation entre 17h00 et 21h00 UTC :
- Return 20j : **−2.29%** (vs −1.52% à 17h00) → pression quotidienne accrue
- Return 60j : **+1.25%** (vs +2.05% à 17h00) → erosion du momentum de moyen terme
- RS 20j vs SPY : **−6.51%** (vs −6.06% à 17h00) → sous-performance relative qui s'accentue
- RS 60j vs SPY : **−6.57%** (vs −6.11% à 17h00) → même tendance sur 60j
- Momentum score XLF : **0.0/10** (dernier du classement sectoriel, ex-aequo avec 7 autres secteurs)

**Remarque desk :** Le symbole "AXA" n'est pas un ticker Yahoo Finance US valide. Le titre est coté à Euronext Paris sous `CS.PA` (ISIN FR0000120628) ; son ADR US est `AXAHY`. Le mismatch explique l'absence totale de données dans `fetch_prices.py` (source yfinance). Sans correction de symbole dans `config/watchlist.json`, aucune analyse technique n'est possible.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES — NON SOURCÉ]**

Aucun bloc fondamental alimenté par `latest.json` : pas de `price`, `technical`, `fundamentals` pour AXA. Les métriques FMP (`fmp_consensus`, `fmp_ratios`, `fmp_key_metrics`) sont absentes.

**Événement du jour :**
- **Earnings J0** (2026-05-19) selon `upcoming_events_latest.json` — source FMP.
- Aucun consensus EPS/Revenue ni résultat publié n'a été récupéré par les sources connectées.

**Exposition sectorielle (actualisée snapshot 21h00) :**
- AXA est classé dans le secteur **Financials** (via XLF). `sector_rotation_latest.json` (2026-05-19) montre une sous-performance sectorielle persistante et légèrement dégradée vs 17h00 :
  - XLF return 20j : **−2.29%**
  - XLF return 60j : **+1.25%**
  - XLF RS 20j vs SPY : **−6.51%**
  - XLF RS 60j vs SPY : **−6.57%**
  - Momentum score XLF : **0.0/10** (dernier du classement, ex-aequo avec Industrials, Utilities, Healthcare, Consumer Discretionary, Materials, Real Estate, Communication Services)
- Pas de crossover détecté. Le secteur financier reste en phase de distribution relative vs le marché.

**Implication desk :** Même si les données AXA étaient disponibles, le headwind sectoriel s'est légèrement accentué entre 17h00 et 21h00 UTC. La dégradation de la RS 20j (−6.51% vs −6.06%) et du return 20j (−2.29% vs −1.52%) confirme la pression relative sur le secteur. Cela peserait sur le score Momentum et le timing d'entrée.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-05-19.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_latest.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_latest.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_latest.json`) :
- Exposition FX : **25%** (export, primary currency USD)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned

**Géopolitique** (`geo_risk_latest.json`) :
- Aucun événement géopolitique spécifique à AXA détecté.
- Score politique global non calculé pour ce ticker (absent du JSON).

**Social Sentiment** (`social_sentiment_latest.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 17h00 |
|-------|--------|----------------------------|
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
| **Évolution** | **Non évaluable** (données de prix absentes + headwind sectoriel légèrement accentué) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Earnings J0 non suivi :** L'événement earnings du 2026-05-19 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré.
3. **Headwind sectoriel légèrement accentué :** Le secteur Financials (XLF) sous-performe le S&P 500 de −6.51% sur 20j (vs −6.06% à 17h00) et −6.57% sur 60j (vs −6.11% à 17h00). Le return 20j est passé de −1.52% à −2.29%. Le momentum score reste à 0.0/10. Si les données AXA étaient disponibles, ce contexte sectoriel peserait légèrement plus sur le score Momentum qu'à 17h00.
4. **Qualité des données :** AXA est toujours l'un des 3 tickers KO sur 25. Tout scoring est non fiable.
5. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-19T21:00:14 UTC), `data/recommandations_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`.*
