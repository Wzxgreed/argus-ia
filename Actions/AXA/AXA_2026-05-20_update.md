# AXA — Mise à jour Quotidienne (Snapshot 10h00 UTC)

> **Date :** 2026-05-20
> **Snapshot :** 2026-05-20T10:00:02 UTC
> **Type :** `_update.md` (post-pipeline matin)
> **Analyste :** Desk Argus-IA
> **Réf. précédent :** `AXA_2026-05-19_update.md` (snapshot 21h00 UTC)

---

## Résumé des changements depuis le snapshot précédent

| Élément | État 2026-05-19 21h00 | État 2026-05-20 10h00 | Changement |
|---------|----------------------|----------------------|------------|
| Cours | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| Volume | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | — |
| Tickers KO pipeline | 3 / 25 | **3 / 25** | Stable (AST, AXA, CYTOMX) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | Stable |
| Score Global | 55.2/100 | **55.2/100** | Stable |
| Recommandation | ATTENDRE | **ATTENDRE** | Confirmée |
| Timing | Neutre | **Neutre** | Stable |
| XLF return 20j | −2.29% | **−2.29%** | Stable |
| XLF return 60j | +1.25% | **+1.25%** | Stable |
| XLF RS 20j vs SPY | −6.51% | **−6.51%** | Stable |
| XLF RS 60j vs SPY | −6.57% | **−6.57%** | Stable |
| XLF momentum score | 0.0/10 | **0.0/10** | Stable (dernier du classement) |
| Earnings | J0 (2026-05-19) | **J0 (2026-05-20)** | Confirmé, non résolu |

**Alerte pipeline :** AXA fait toujours partie des **3 tickers KO** sur 25 (`AST`, `AXA`, `CYTOMX`). `data/latest.json` (fetched_at 2026-05-20T10:00:02 UTC) enregistre `error: true`, `reason: "No price history"`. Aucune métrique technique ou fondamentale brute n'est exploitable.

---

## Mise à jour technique

**[DONNÉES MANQUANTES — NON SOURCÉ]**

- Cours : non disponible (`latest.json` → `error: true`, `reason: No price history`)
- RSI 14j : non disponible
- ATR 14j : non disponible → SL/TP non calculables
- MM 50j / 200j : non disponibles
- Volume relatif vs moy. 20j : non disponible
- Supports / Résistances : non identifiables

**Headwind sectoriel stable :** Le secteur Financials (XLF) affiche des métriques identiques au snapshot 21h00 UTC d'hier :
- Return 20j : **−2.29%** (stable)
- Return 60j : **+1.25%** (stable)
- RS 20j vs SPY : **−6.51%** (stable)
- RS 60j vs SPY : **−6.57%** (stable)
- Momentum score XLF : **0.0/10** (dernier du classement sectoriel, ex-aequo avec 7 autres secteurs)

Pas de crossover détecté. Le secteur financier reste en phase de distribution relative vs le marché.

**Remarque desk :** Le symbole "AXA" n'est pas un ticker Yahoo Finance US valide. Le titre est coté à Euronext Paris sous `CS.PA` (ISIN FR0000120628) ; son ADR US est `AXAHY`. Le mismatch explique l'absence totale de données dans `fetch_prices.py` (source yfinance). Sans correction de symbole dans `config/watchlist.json`, aucune analyse technique n'est possible.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES — NON SOURCÉ]**

Aucun bloc fondamental alimenté par `latest.json` : pas de `price`, `technical`, `fundamentals` pour AXA. Les métriques FMP (`fmp_consensus`, `fmp_ratios`, `fmp_key_metrics`) sont absentes.

**Événement du jour :**
- **Earnings J0** (2026-05-20) selon `upcoming_events_latest.json` — source FMP.
- Aucun consensus EPS/Revenue ni résultat publié n'a été récupéré par les sources connectées.
- Le pipeline du matin n'a pas résolu l'événement earnings ; l'absence de données empêche toute analyse post-earnings.

**Exposition sectorielle (actualisée snapshot 10h00) :**
- AXA est classé dans le secteur **Financials** (via XLF). `sector_rotation_latest.json` (2026-05-20) montre une sous-performance sectorielle persistante, stable vs hier :
  - XLF return 20j : **−2.29%**
  - XLF return 60j : **+1.25%**
  - XLF RS 20j vs SPY : **−6.51%**
  - XLF RS 60j vs SPY : **−6.57%**
  - Momentum score XLF : **0.0/10** (dernier du classement, ex-aequo avec Industrials, Utilities, Healthcare, Consumer Discretionary, Materials, Real Estate, Communication Services)
- Pas de crossover détecté. Le secteur financier reste en phase de distribution relative vs le marché.

**Implication desk :** Le headwind sectoriel est stable ce matin. Si les données AXA étaient disponibles, ce contexte peserait sur le score Momentum et le timing d'entrée. L'absence de données fondamentales empêche toute révision de valorisation ou de Filtre Qualité.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-05-20.json`) | **Aucune** | `AXA: []` — 0 article |
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
| **Évolution** | **Non évaluable** (données de prix absentes + headwind sectoriel stable) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Earnings J0 non résolu :** L'événement earnings du 2026-05-20 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré. Le passage à J+1 n'apportera pas d'information sans correction du symbole.
3. **Headwind sectoriel stable :** Le secteur Financials (XLF) sous-performe le S&P 500 de −6.51% sur 20j et −6.57% sur 60j. Le momentum score reste à 0.0/10. Si les données AXA étaient disponibles, ce contexte sectoriel peserait sur le score Momentum.
4. **Qualité des données :** AXA est toujours l'un des 3 tickers KO sur 25. Tout scoring est non fiable.
5. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-20T10:00:02 UTC), `data/recommandations_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`.*
