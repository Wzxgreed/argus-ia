# AXA — Mise à jour Quotidienne (Snapshot 17h00 UTC)

> **Date :** 2026-05-19
> **Snapshot :** 2026-05-19T17:00:01 UTC
> **Type :** `_update.md` (flash post-pipeline 17h00)
> **Analyste :** Desk Argus-IA
> **Réf. précédent :** `AXA_2026-05-19_update.md` (snapshot matinal)

---

## Résumé des changements depuis le snapshot matinal

| Élément | État snapshot matin | État snapshot 17h00 | Changement |
|---------|--------------------|---------------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Tickers KO pipeline | 4 / 25 | **3 / 25** | Amélioration (1 ticker corrigé, pas AXA) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | Stable |
| Score Global | 55.2/100 | **55.2/100** | Stable |
| Recommandation | ATTENDRE | **ATTENDRE** | Confirmée |
| Timing | Neutre | **Neutre** | Stable |
| XLF RS 20j vs SPY | −5.91% | **−6.06%** | Légère dégradation |
| XLF RS 60j vs SPY | −8.35% | **−6.11%** | Réduction de l'écart |
| XLF return 20j | — | **−1.52%** | Nouveau datapoint |
| XLF return 60j | — | **+2.05%** | Nouveau datapoint |
| Earnings | J0 (2026-05-19) | **J0 (2026-05-19)** | Confirmé, non résolu |

**Alerte pipeline :** AXA fait partie des **3 tickers KO** sur 25 requêtés (`AST`, `AXA`, `CYTOMX`). `validation_report.txt` (16:06 UTC) enregistre **4 erreurs + 2 warnings** — au-delà du seuil critique de 2 `[ERROR]`. Aucune métrique technique ou fondamentale brute n'est exploitable pour AXA.

---

## Mise à jour technique

**[DONNÉES MANQUANTES — NON SOURCÉ]**

- Cours : non disponible (`latest.json` → `error: true`, `reason: No price history`)
- RSI 14j : non disponible
- ATR 14j : non disponible → SL/TP non calculables
- MM 50j / 200j : non disponibles
- Volume relatif vs moy. 20j : non disponible
- Supports / Résistances : non identifiables

**Remarque desk :** Le symbole "AXA" n'est pas un ticker Yahoo Finance US valide. Le titre est coté à Euronext Paris sous `CS.PA` (ISIN FR0000120628) ; son ADR US est `AXAHY`. Le mismatch explique l'absence totale de données dans `fetch_prices.py` (source yfinance). Sans correction de symbole dans `config/watchlist.json`, aucune analyse technique n'est possible.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES — NON SOURCÉ]**

Aucun bloc fondamental alimenté par `latest.json` : pas de `price`, `technical`, `fundamentals` pour AXA. Les métriques FMP (`fmp_consensus`, `fmp_ratios`, `fmp_key_metrics`) sont absentes.

**Événement du jour :**
- **Earnings J0** (2026-05-19) selon `upcoming_events_latest.json` — source FMP.
- Aucun consensus EPS/Revenue ni résultat publié n'a été récupéré par les sources connectées.

**Exposition sectorielle (actualisée snapshot 17h00) :**
- AXA est classé dans le secteur **Financials** (via XLF). `sector_rotation_latest.json` (2026-05-19) montre une sous-performance sectorielle persistante :
  - XLF return 20j : **−1.52%**
  - XLF return 60j : **+2.05%**
  - XLF RS 20j vs SPY : **−6.06%**
  - XLF RS 60j vs SPY : **−6.11%**
  - Momentum score XLF : **0.0/10** (dernier du classement, ex-aequo avec Industrials, Utilities, Healthcare, Consumer Discretionary, Materials, Real Estate, Communication Services)
- Pas de crossover détecté. Le secteur financier reste en phase de distribution relative vs le marché.

**Implication desk :** Même si les données AXA étaient disponibles, le headwind sectoriel serait un malus structurel sur le score Momentum et le timing d'entrée. La dégradation de la RS 20j (−6.06% vs −5.91% ce matin) confirme la pression relative sur le secteur.

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

| Score | Valeur | Évolution vs snapshot matin |
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
| **Évolution** | **Non évaluable** (données de prix absentes + headwind sectoriel identifié) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Earnings J0 non suivi :** L'événement earnings du 2026-05-19 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré.
3. **Headwind sectoriel confirmé :** Le secteur Financials (XLF) sous-performe le S&P 500 de −6.06% sur 20j et −6.11% sur 60j, avec un momentum score de 0.0/10. La RS 20j s'est légèrement dégradée vs ce matin (−6.06% vs −5.91%). Si les données AXA étaient disponibles, ce contexte sectoriel peserait sur le score Momentum.
4. **Qualité des données :** Le validation report du jour enregistre 4 erreurs + 2 warnings (>2 ERROR → STOP). AXA est l'un des 3 tickers KO. Tout scoring est non fiable.
5. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-19T17:00:01 UTC), `data/recommandations_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/validation_report.txt`.*
