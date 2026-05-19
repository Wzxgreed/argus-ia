# AXA — Mise à jour Quotidienne

> **Date :** 2026-05-19
> **Type :** `_update.md` (flash post-événement + données manquantes)
> **Analyste :** Desk Argus-IA

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 2026-05-18 | État 2026-05-19 | Changement |
|---------|-----------------|-----------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | 5.5/10 (C:6.5 V:5.0 M:5.0) | Stable |
| Score Global | 55.2/100 | 55.2/100 | Stable |
| Recommandation | ATTENDRE | ATTENDRE | Confirmée |
| Timing | Neutre | Neutre | Stable |
| Événement | Earnings J0 (2026-05-18) | Earnings J0 (2026-05-19) | Calendrier FMP |
| News | Aucune | Aucune | Stable |

**Alerte pipeline :** AXA fait toujours partie des 4 tickers KO sur 25 requêtés (`tickers_ko: 4`). Aucune métrique technique ou fondamentale brute n'est exploitable.

---

## Mise à jour technique

**[DONNÉES MANQUANTES — NON SOURCÉ]**

- Cours : non disponible (`latest.json` → `error: true, reason: No price history`)
- RSI 14j : non disponible
- ATR 14j : non disponible → stop-loss/take-profit non calculables
- MM 50j / 200j : non disponibles
- Volume vs moy. 20j : non disponible
- Support / Résistance : non identifiables

**Remarque desk :** Le mismatch de symbole persiste. "AXA" n'est pas un ticker Yahoo Finance US valide. Le titre est coté à Euronext Paris sous `CS.PA` ; son ADR US est `AXAHY`. Le pipeline `fetch_prices.py` (source yfinance) ne retourne aucun historique pour ce symbole.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES — NON SOURCÉ]**

Aucun bloc fondamental n'est alimenté par `latest.json` (pas de `price`, pas de `technical`, pas de `fundamentals` pour AXA). Les métriques FMP (`fmp_consensus`, `fmp_ratios`, `fmp_key_metrics`) sont également absentes.

**Événement du jour :**
- **Earnings J0** (2026-05-19) selon `upcoming_events_latest.json` — source FMP.
- Aucune donnée de consensus EPS/Revenue n'est disponible dans le pipeline pour ce ticker.
- Aucun résultat publié n'a été récupéré par les sources connectées.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-05-19.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 — `social_sentiment_latest.json` |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| News événements corporate | 🟢 Aucun | `events_latest.json` → 0 événement pour AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_latest.json`) :
- Exposition FX : **25%** (export, primary currency USD)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned

**Sector Rotation** (`sector_rotation_latest.json`) :
- Régime macro : UNKNOWN
- XLF (Financials) : momentum score 0.0/10, RS 20j vs SPY −5.91%, RS 60j −8.35%
- Pas de crossover détecté

**Géopolitique** (`geo_risk_latest.json`) :
- Aucun événement géopolitique spécifique à AXA détecté.
- Score politique global non calculé pour ce ticker (absent du JSON).

---

## Scoring global (agents)

| Score | Valeur | Évolution vs 2026-05-18 |
|-------|--------|-------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | Neutre | Stable |

**Pondération appliquée :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime macro inconnu → poids par défaut).

> **Règle de disqualification :** aucun score individuel ≤ 2/10 → le ticker n'est pas exclu du rapport, mais le manque de données empêche tout positionnement.

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
| **Évolution** | **Non évaluable** (données de prix absentes) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux.
2. **Earnings J0 non suivi :** L'événement earnings du 2026-05-19 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré.
3. **Scores agents :** Le score 55.2/100 (ATTENDRE) est un placeholder algorithmique basé sur des valeurs par défaut (RSI 50, scores moyens) faute de données réelles. Il ne doit pas être interprété comme une recommandation investissable.
4. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json`, `data/recommandations_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/events_latest.json`, `data/sector_rotation_latest.json`, `data/geo_risk_latest.json`.*
