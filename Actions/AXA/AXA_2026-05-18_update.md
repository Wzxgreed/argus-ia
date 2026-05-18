# AXA — Mise à jour Quotidienne

> **Date :** 2026-05-18
> **Type :** `_update.md` (flash post-événement + données manquantes)
> **Analyste :** Desk Argus-IA

---

## Résumé des changements depuis l'analyse précédente

L'analyse précédente (`AXA_2026-05-18_preview.md`) était un template pré-earnings vierge — sans prédictions chiffrées ni consensus. Aucune donnée de cours n'était alors disponible. Cette situation persiste : **les données de prix pour le ticker "AXA" restent indisponibles** dans `data/latest.json` (`error: true, reason: No price history`).

| Élément | État précédent | État actuel | Changement |
|---------|---------------|-------------|------------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| ATR 14j | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Volume | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| Score Opportunité | — | **5.5/10** (C:6.5 V:5.0 M:5.0) | Nouveau |
| Score Global | — | **55.2/100** | Nouveau |
| Recommandation | — | **ATTENDRE** | Nouveau |
| Timing | — | Neutre | Nouveau |
| Événement | Preview earnings J0 | **Earnings J0 (aujourd'hui)** | Confirmé |

**Alerte pipeline :** AXA fait partie des 3 tickers KO sur 22 requêtés (tickers OK: 19/22). Aucune métrique technique ou fondamentale brute n'est exploitable à ce stade.

---

## Mise à jour technique

**[DONNÉES MANQUANTES — NON SOURCÉ]**

- Cours : non disponible (`latest.json` → `error: true`)
- RSI 14j : non disponible
- ATR 14j : non disponible → stop-loss/take-profit non calculables
- MM 50j / 200j : non disponibles
- Volume vs moy. 20j : non disponible
- Support / Résistance : non identifiables

**Remarque desk :** Le ticker "AXA" sur Yahoo Finance US ne correspond pas à un instrument coté. Le titre AXA est coté à Euronext Paris sous le ticker `CS.PA` (ISIN FR0000120628) ; son ADR US est `AXAHY`. Le mismatch de symbole explique l'absence de données historiques dans le pipeline `fetch_prices.py` (source yfinance).

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES — NON SOURCÉ]**

Aucun bloc fondamental n'est alimenté par `latest.json` (pas de `price`, pas de `technical`, pas de `fundamentals` pour AXA). Les métriques FMP (`fmp_consensus`, `fmp_ratios`, `fmp_key_metrics`) sont également absentes.

**Événement du jour :**
- **Earnings J0** (2026-05-18) selon `upcoming_events_latest.json` — source FMP.
- Aucune donnée de consensus EPS/Revenue n'est disponible dans le pipeline pour ce ticker.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
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

---

## Scoring global (agents)

| Score | Valeur | Évolution vs précédent |
|-------|--------|------------------------|
| Score Opportunité | **5.5/10** | Nouveau (premier calcul) |
| — Catalyseur | 6.5/10 | — |
| — Valorisation | 5.0/10 | — |
| — Momentum | 5.0/10 | — |
| Score Global | **55.2/100** | Nouveau |
| Recommandation | **ATTENDRE** | — |
| Timing | Neutre | — |

**Pondération appliquée :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime macro inconnu → poids par défaut).

> **Règle de disqualification :** aucun score individuel ≤ 2/10 → le ticker n'est pas exclu du rapport, mais le manque de données empêche toute positionnement.

---

## Niveaux suggérés

**[NON CALCULABLES — MANQUE DE DONNÉES]**

- Prix actuel : `null`
- Prix d'entrée suggéré : `null`
- Stop-loss : `null`
- Take-profit : `null`
- Ratio R/R : `null`

Sans cours ni ATR, aucun niveau technique ne peut être établi de manière fiable. Toute simulation serait une hallucination.

---

## Conclusion — Thèse

| Verdict | Statut |
|---------|--------|
| **Thèse initiale** | Aucune — pas d'`_init.md` préalable |
| **Évolution** | **Non évaluable** (données de prix absentes) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole identifié :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux.
2. **Earnings J0 non suivi :** L'événement earnings du 2026-05-18 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré.
3. **Scores agents :** Le score 55.2/100 (ATTENDRE) est un placeholder algorithmique basé sur des valeurs par défaut (RSI 50, scores moyens) faute de données réelles. Il ne doit pas être interprété comme une recommandation investissable.
4. **Next steps :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_2026-05-18_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json`, `data/recommandations_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/social_sentiment_latest.json`, `data/events_latest.json`.*
