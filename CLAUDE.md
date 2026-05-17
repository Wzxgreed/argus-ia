# Système d'Analyse d'Actions IA

Chaque matin, le système produit trois livrables en un seul workflow :
1. **Bulletin d'actualités** mondial (`Actualités/YYYY-MM-DD.md`)
2. **Analyses d'impact approfondies** sur les actions de la watchlist touchées par les news (`Actions/[TICKER]/`)
3. **Rapport d'opportunités** scorées par catalyseur × valorisation × momentum (`Opportunités/YYYY-MM-DD.md`)

---

## Structure du projet

```
Argus-IA/
├── CLAUDE.md                              ← Ce fichier
├── Makefile                               ← Commandes rapides (install, test, lint, pipeline, agents)
├── INSTALL.md                             ← Guide d'installation rapide
├── README.md                              ← Présentation du projet
├── requirements.txt                       ← Dépendances Python
├── pyproject.toml                         ← Configuration Python (packaging, outils)
├── .env                                   ← Template de configuration API
│
├── .github/
│   └── workflows/
│       └── ci.yml                         ← CI GitHub Actions (lint + test + validation)
│
├── config/
│   └── watchlist.json                     ← Tickers, secteurs, symboles macro, settings
│
├── scripts/                               ← Pipeline de données Python
│   ├── run_morning.sh                     ← Pipeline complet du matin (20 étapes + auto-push GitHub)
│   ├── auto_push.sh                       ← Helper commit + push automatique post-agent/pipeline
│   ├── yahoo_worker.py                   ← Worker isolé yfinance (one-shot subprocess + timeout OS)
│   ├── yahoo_worker_daemon.py            ← Worker yfinance pré-chauffé (daemon stdin/stdout)
│   ├── yahoo_client.py                   ← Client HTTP REST Yahoo (requests, sans yfinance)
│   ├── http_utils.py                     ← Wrapper HTTP : retry 3×, backoff exponentiel, cache disque, circuit breaker
│   ├── fetch_prices.py                   ← Cours, volumes, technique, fondamentaux, options (Yahoo + FMP)
│   ├── fetch_macro.py                    ← Indices, VIX, taux, FX, commodités, régime macro (Yahoo)
│   ├── fetch_calendar.py                 ← Earnings dates, calendrier économique (Yahoo + FMP)
│   ├── agent_news_fetcher.py             ← Fetch unifié des news pour tous les agents
│   ├── learn_from_errors.py              ← Boucle d'apprentissage auto (fenêtres J+5/20/60/30/90/180)
│   ├── agent_quant.py                    ← Agent Quant : signification statistique, Sharpe, calibration
│   ├── agent_geo.py                      ← Agent Géopolitique : scan politique, exposition, scénarios
│   ├── agent_crypto.py                   ← Agent Crypto-Correlation : BTC beta, NAV, divergence
│   ├── agent_watchman.py                 ← Surveillance proactive : earnings, CEO, insiders, news, upgrades
│   ├── detect_major_events.py            ← Détection événements majeurs : gap, volume, ATR, news keywords
│   ├── agent_accounting.py               ← Fraude & qualité comptable : Beneish M-Score, Altman Z-Score, Piotroski F-Score, Sloan Ratio
│   ├── agent_sector_rotation.py          ← Rotation sectorielle : RS vs SPY, crossovers, alignement macro
│   ├── agent_event_driven.py             ← Event-Driven : M&A, buybacks, activism, guidance
│   ├── agent_fx.py                       ← Exposition FX par ticker, impact revenus/EPS
│   ├── agent_social.py                   ← Sentiment retail Reddit : mentions, pump detection, score social
│   ├── agent_recommandation.py           ← Scoring 3 axes régime-aware + reco ACHETER/ATTENDRE/ÉVITER
│   ├── paper_trading.py                  ← Moteur paper trading : sizing ATR, SL/TP, time stop, journal de performance
│   ├── fetch_transcripts.py              ← NLP Transcript Analysis via FMP (optionnel — plan Enterprise+ requis)
│   ├── fmp_client.py                     ← Client HTTP FMP Stable API (base /stable/, session keep-alive)
│   └── validate.py                       ← Sanity checks + rapport d'erreurs
│
├── data/                                  ← Snapshots quotidiens (lu par l'agent)
│   ├── YYYY-MM-DD.json                    ← Snapshot complet du jour (prix + macro + calendar)
│   ├── latest.json                        ← Symlink vers le snapshot actuel
│   ├── validation_report.txt             ← Rapport de validation des données
│   ├── transcripts_NLP_YYYY-MM-DD.json   ← Analyse NLP management (si FMP activé)
│   ├── transcripts_NLP_latest.json       ← Symlink vers le dernier NLP
│   ├── upcoming_events_YYYY-MM-DD.json   ← Événements à venir (watchman)
│   ├── upcoming_events_latest.json       ← Symlink vers le dernier watchman
│   ├── quant_report_YYYY-MM-DD.json       ← Signification statistique, Sharpe, calibration
│   ├── quant_report_latest.json           ← Symlink vers le dernier quant
│   ├── geo_risk_YYYY-MM-DD.json           ← Score politique, exposition, scénarios
│   ├── geo_risk_latest.json               ← Symlink vers le dernier geo
│   ├── crypto_correlation_YYYY-MM-DD.json ← Corrélation BTC, beta, NAV, divergence
│   ├── crypto_correlation_latest.json     ← Symlink vers le dernier crypto
│   ├── accounting_risk_YYYY-MM-DD.json    ← M-Score, Z-Score, F-Score, Sloan, risk level par ticker
│   ├── accounting_risk_latest.json        ← Symlink vers le dernier accounting
│   ├── sector_rotation_YYYY-MM-DD.json    ← RS 20j/60j vs SPY, ranking, crossovers, signal macro
│   ├── sector_rotation_latest.json        ← Symlink vers le dernier sector rotation
│   ├── social_sentiment_YYYY-MM-DD.json   ← Mentions Reddit, sentiment retail, pump detection
│   ├── social_sentiment_latest.json       ← Symlink vers le dernier social sentiment
│   ├── fx_exposure_YYYY-MM-DD.json        ← Exposition FX par ticker, impact revenus/EPS
│   ├── fx_exposure_latest.json            ← Symlink vers le dernier FX
│   ├── events_YYYY-MM-DD.json             ← Événements corporates (M&A, buybacks, activism)
│   ├── events_latest.json                 ← Symlink vers le dernier event-driven
│   ├── recommandations_YYYY-MM-DD.json    ← Recommandations : action, niveaux, ratio R/R
│   ├── recommandations_latest.json        ← Symlink vers les dernières recommandations
│   ├── news_YYYY-MM-DD.json               ← News unifiées par ticker (Yahoo v1/search)
│   ├── news_latest.json                   ← Symlink vers les dernières news
│   └── history/
│       └── prices/                        ← (futur) timeseries pour backtesting
│
├── Actions/
│   ├── _TEMPLATE_ACTION/                  ← Modèles à copier pour chaque nouvelle action
│   │   ├── INDEX.md
│   │   ├── TICKER_YYYY-MM-DD_init.md      ← Analyse initiale (fondamentaux + technique + macro)
│   │   ├── TICKER_YYYY-MM-DD_preview.md   ← Preview pré-earnings + modèle prédiction surprise
│   │   ├── TICKER_YYYY-MM-DD_earnings.md
│   │   ├── TICKER_YYYY-MM-DD_update.md    ← Inclut radar activité inhabituelle
│   │   └── SUPPLY_CHAIN.md               ← Carte supply chain du ticker
│   │
│   ├── WATCHLIST_SCORES.md               ← Dashboard scores quotidiens de toute la watchlist
│   ├── CORRELATIONS_WATCHLIST.md         ← Matrice corrélations inter-tickers + cascade
│   ├── PATTERNS_HISTORIQUES.md           ← Bibliothèque de configurations récurrentes
│   ├── SUIVI_PRIX_CIBLES.md              ← Suivi J+30/90/180 de tous les prix cibles émis
│   ├── SUIVI_EARNINGS_PREDICTIONS.md     ← Suivi précision prédictions earnings
│   │
│   ├── AAPL/                             ← Un dossier par action
│   │   ├── INDEX.md
│   │   ├── AAPL_2026-05-09_init.md
│   │   ├── AAPL_2026-05-09_preview.md
│   │   ├── AAPL_2026-07-01_earnings.md
│   │   ├── AAPL_2026-05-15_update.md
│   │   └── SUPPLY_CHAIN.md
│   └── ...
│
├── Actualités/
│   ├── WATCHLIST.md                       ← Tickers, secteurs & seuils d'alertes par ticker
│   ├── CALENDRIER_EARNINGS.md             ← Agenda earnings 30 prochains jours
│   ├── _TEMPLATE_ACTU.md                  ← Modèle bulletin quotidien
│   ├── YYYY-MM-DD.md                      ← Bulletin du jour
│   └── Semaines/
│       └── YYYY-WXX.md                   ← Rapport de revue hebdomadaire
│
├── Alertes/
│   ├── ALERTES.md                         ← Seuils simples + alertes composites + log déclenchements
│   └── UPCOMING_EVENTS.md                ← Dashboard événements à venir (watchman génère chaque matin)
│
├── Agents/                                ← Définition des agents spécialisés
│   ├── AGENT_MACRO.md                     ← Régime macro, banques centrales, taux, DXY + hedge Risk-off
│   ├── AGENT_FLUX.md                      ← Flux 13F, ETF, dark pool, gamma, max pain
│   ├── AGENT_TECHNIQUE.md                 ← Cours, indicateurs, force relative, saisonnalité
│   ├── AGENT_FONDAMENTAL.md               ← Résultats, ratios, DCF, NLP transcripts, modèle prédiction surprise
│   ├── AGENT_SENTIMENT.md                 ← News, analystes, insiders, options, EPS revision momentum, contrats gouv.
│   ├── AGENT_SUPPLY_CHAIN.md              ← Cartographie fournisseurs/clients, monitoring
│   ├── SKILL_MARKET_RESEARCHER.md         ← Protocole institutionnel : TAM, peer comps, competitive landscape
│   ├── SKILL_EARNINGS_REVIEWER.md         ← Protocole institutionnel : variance table, estimate revisions, NLP management
│   ├── ANALYST_TRACK_RECORD.md            ← Précision historique des analystes sell-side
│   ├── APPRENTISSAGES.md                  ← Mémoire institutionnelle + calibration automatique des scores
│   ├── ORCHESTRATION.md                   ← Comment les agents coopèrent
│   └── WORKFLOW_SEMAINE.md               ← Protocole de revue hebdomadaire (lundi)
│
├── Portefeuille/
│   ├── POSITIONS.md                       ← Positions ouvertes réelles + P&L temps réel
│   ├── PERFORMANCE.md                     ← Historique des trades fermés réels
│   ├── PAPER_POSITIONS.json              ← Positions ouvertes paper trading
│   ├── PAPER_TRADES.md                   ← Journal des trades virtuels (entrées/sorties)
│   ├── PAPER_PERFORMANCE.md              ← Performance paper trading : capital, win rate, positions ouvertes
│   ├── MODULE_SIZING.md                   ← Règles de dimensionnement des positions
│   └── MODULE_RISQUE_PORTEFEUILLE.md      ← Corrélations, stress tests, VaR
│
└── Opportunités/
    ├── _TEMPLATE_OPPORTUNITES.md
    ├── HISTORIQUE_SCORES.md
    ├── BACKTESTING.md                     ← Suivi performance signaux J+5/J+20/J+60
    └── YYYY-MM-DD.md
```

---

## Règles de nommage des fichiers

| Type de fichier | Nom |
|----------------|-----|
| Analyse initiale | `TICKER_YYYY-MM-DD_init.md` |
| Preview pré-earnings | `TICKER_YYYY-MM-DD_preview.md` |
| Mise à jour earnings | `TICKER_YYYY-MM-DD_earnings.md` |
| Mise à jour actualité | `TICKER_YYYY-MM-DD_update.md` |
| Index du dossier | `INDEX.md` |
| Bulletin actualités | `YYYY-MM-DD.md` (dans `Actualités/`) |

---

## Les agents spécialisés

> Fichiers de référence complets dans `Agents/`. Ce qui suit est le résumé opérationnel.
> Schéma de coopération complet : [Agents/ORCHESTRATION.md](Agents/ORCHESTRATION.md)

---

### Agent Macro — [Agents/AGENT_MACRO.md](Agents/AGENT_MACRO.md) ← S'EXÉCUTE EN PREMIER
**Périmètre :** régime macroéconomique, banques centrales, courbe des taux, DXY, VIX, spreads crédit, calendrier économique
**Sources :** `indexes`, `economics`, `forex`, `commodity`, `news`, `calendar`
**Produit :** Régime actif + pondération du score final + carte d'exposition sectorielle + alertes macro

Régimes gérés : Normal, Risk-off, Risk-on/Bull, Pré-FOMC, Pré-earnings, Stagflation, Récession.
Ajustements automatiques : bonus/malus sur le score final selon le régime et l'exposition sectorielle.

---

### Agent Flux — [Agents/AGENT_FLUX.md](Agents/AGENT_FLUX.md) ← S'EXÉCUTE EN SECOND
**Périmètre :** flux institutionnels 13F, flux ETF, short interest & borrow rate, dark pool, gamma exposure, max pain
**Sources :** `form13F`, `etfAndMutualFunds`, `quote`, `insiderTrades`, `marketPerformance`
**Produit :** Bloc Flux dans `_init.md` / `_update.md` + bonus/malus Score Catalyseur

Signaux clés : accumulation/distribution 13F, flux ETF nets, short squeeze setup (4 conditions), dark pool blocs, max pain, call wall/put wall, GEX, IV Rank, unusual options activity.

---

### Agent Technique — [Agents/AGENT_TECHNIQUE.md](Agents/AGENT_TECHNIQUE.md)
**Périmètre :** cours, indicateurs, volumes, force relative, saisonnalité, niveaux clés, timing
**Sources :** `quote`, `technicalIndicators`, `chart`, `marketPerformance`
**Produit :** Bloc Technique dans chaque `_init.md` / `_update.md` + Score Momentum /10

Indicateurs calculés : RSI 14j, MACD 12/26/9, MM 50j & 200j, Golden/Death cross, volume relatif vs moy. 20j, OBV, supports & résistances, **force relative vs S&P 500 et vs secteur (90j)**, **saisonnalité mensuelle et sectorielle**.

---

### Agent Fondamental — [Agents/AGENT_FONDAMENTAL.md](Agents/AGENT_FONDAMENTAL.md)
**Périmètre :** résultats financiers, ratios, valorisation, analyse sectorielle, earnings, qualité bénéfices, NLP transcripts
**Sources :** `statements`, `earningsTranscript`, `secFilings`, `discountedCashFlow`, `company`, `analyst`
**Produit :** Filtre Qualité /6 + Bloc Fondamental dans chaque `_init.md` / `_earnings.md` + Score Valorisation /10 + **Score Confiance Management /10 (NLP)**

Métriques clés : **Filtre Qualité 6 critères** (CAGR revenus/profits 5 ans, Assets/Liabilities, FCF trend 5 ans, moat, TAM industrie), croissance CA/EPS LTM & NTM, marges, FCF yield, accruals ratio, qualité bénéfices, capital allocation, dette/EBITDA, ROIC, comps sectoriels (P/E, EV/EBITDA, EV/FCF), DCF + valeur intrinsèque.

**Filtre Qualité — règle absolue :**
- Score 5–6/6 → ✅ Quality Compounder — analyse complète, score Valorisation non plafonné
- Score 4/6 → ⚠️ Quality Partielle — analyse complète, −0.5 pt, préciser les critères manquants
- Score ≤ 3/6 → 🔴 Hors périmètre — Score Valorisation plafonné à 5/10, trade court terme uniquement

---

### Agent Sentiment — [Agents/AGENT_SENTIMENT.md](Agents/AGENT_SENTIMENT.md)
**Périmètre :** news mondiales, consensus analystes (avec track record), insiders, short interest, options flow complet, job postings
**Sources :** `news`, `analyst`, `insiderTrades`, `senate`, `commitmentOfTraders`, `indexes`, `quote`
**Produit :** Bloc Sentiment dans chaque `_init.md` / `_update.md` + Score Catalyseur /10

Signaux clés : upgrades/downgrades **pondérés par track record** (voir `Agents/ANALYST_TRACK_RECORD.md`), achats insiders, short squeeze setup, VIX, put/call ratio, **IV Rank**, **max pain**, **GEX**, **unusual options activity**, earnings whisper, transactions politiques US, cluster buying, **job postings comme leading indicator (6-12 mois)**.

---

### Agent Supply Chain — [Agents/AGENT_SUPPLY_CHAIN.md](Agents/AGENT_SUPPLY_CHAIN.md) ← NOUVEAU
**Périmètre :** cartographie des dépendances critiques (fournisseurs et clients), monitoring quotidien, détection des impacts en avance
**Sources :** `secFilings`, `company`, `news`, `earningsTranscript`, `statements`, `quote`
**Produit :** `Actions/[TICKER]/SUPPLY_CHAIN.md` + alertes dans `_update.md` + bonus/malus Score Catalyseur

Signaux clés : résultats d'un fournisseur critique → impact estimé sur marges [TICKER], profits warning d'un client clé → impact revenus, reshoring/diversification supply, nouveau client majeur annoncé.

---

### Agent Quant — [Agents/AGENT_QUANT.md](Agents/AGENT_QUANT.md) ← NOUVEAU
**Périmètre :** validation statistique du système, signification des signaux, métriques de risque institutionnelles (Sharpe, Max Drawdown, Sortino), overfitting detection, calibration des scores
**Sources :** `Opportunités/BACKTESTING.md`, `Actions/SUIVI_PRIX_CIBLES.md`, `Agents/POST_MORTEMS/`, `data/latest.json`
**Produit :** `data/quant_report_YYYY-MM-DD.json` + mise à jour des tableaux de performance + alertes de calibration

Signaux clés : **test binomial** (p-value < 0.05 = significatif), **walk-forward analysis** (détection d'overfitting), **corrélation score vs rendement réel** (r²), **Sharpe/Sortino/Calmar** sur les rendements J+20.

---

### Agent Politique / Géopolitique — [Agents/AGENT_GEO.md](Agents/AGENT_GEO.md) ← NOUVEAU
**Périmètre :** risques et opportunités politiques, décisions gouvernementales (tarifs, budgets, sanctions), événements géopolitiques (guerres, Hormuz, OTAN), exposition sectorielle
**Sources :** `news` (Yahoo Finance), `secFilings` (8-K), calendrier économique, regex politiques
**Produit :** `data/geo_risk_YYYY-MM-DD.json` + Bloc Géopolitique dans `_update.md` + alertes composites

Signaux clés : **Score Politique /10** (tarifs, sanctions, guerre, élection), **cartographie d'exposition** (revenus géo 40%, supply chain 30%, macro 30%), **3 scénarios** (optimiste/central/pessimiste avec probabilités), déclenchement automatique d'`_update.md` si score ≥ 7.

---

### Agent Crypto-Correlation — [Agents/AGENT_CRYPTO.md](Agents/AGENT_CRYPTO.md) ← NOUVEAU
**Périmètre :** modélisation de la relation entre tickers crypto-exposés et cryptomonnaies (BTC, ETH), calcul NAV/premium/discount, détection des divergences
**Sources :** `yfinance` (BTC-USD, ETH-USD), `blockchain.info` (hash rate, difficulty), filings trimestriels
**Produit :** `data/crypto_correlation_YYYY-MM-DD.json` + Bloc Crypto dans `_init.md` / `_update.md`

Signaux clés : **corrélation 30j/90j** avec BTC, **beta BTC** (>1.5 = sur-exposition), **NAV estimé** vs market cap (premium/discount), **Mining Profitability Index** (MPI), **Score Divergence /10** (anomalie ticker vs BTC).

---

### Agent Watchman — `scripts/agent_watchman.py` + `Alertes/UPCOMING_EVENTS.md` ← NOUVEAU
**Périmètre :** surveillance proactive des événements futurs par ticker : earnings dates, news CEO/M&A/guidance, insider trades significatifs, upgrades/downgrades, contrats gouvernementaux
**Sources :** `yfinance` (calendar, news), `FMP Stable API` (earnings-calendar, insider-trading, upgrades-downgrades)
**Produit :** `data/upcoming_events_YYYY-MM-DD.json` + `Alertes/UPCOMING_EVENTS.md` + `_preview.md` auto-généré si earnings ≤ 3j + `_update.md` flash si CEO/insider/analyste majeur

Signaux clés : **calendrier earnings 30j** avec estimates EPS/Revenue, **news keywords futurs** (investor day, guidance, M&A, FDA), **insider trades >$1M**, **upgrades/downgrades massifs**, **alertes timeline** (🔴 ≤3j / 🟡 ≤7j / 🟢 ≤30j).

---

### Agent Accounting — `scripts/agent_accounting.py` + `data/accounting_risk_YYYY-MM-DD.json` ← NOUVEAU
**Périmètre :** détection de manipulation comptable et évaluation de la santé financière via 4 métriques institutionnelles
**Sources :** `FMP Stable API` (income-statement, balance-sheet-statement, cash-flow-statement)
**Produit :** `data/accounting_risk_YYYY-MM-DD.json` + alertes intégrées dans le Filtre Qualité et le paper trading

Signaux clés : **Beneish M-Score** (> -1.78 = 🔴 manipulation suspectée), **Altman Z-Score** (< 1.81 = 🔴 distress/faillite probable), **Piotroski F-Score** (≤ 3 = 🔴 santé faible), **Sloan Ratio** (> 0.1 = 🔴 accruals élevés). Règle absolue : si M-Score > -1.78 OU Z-Score < 1.81 → exclure du long / paper trading bloqué.

---

### Agent Sector Rotation — `scripts/agent_sector_rotation.py` + `data/sector_rotation_YYYY-MM-DD.json` ← NOUVEAU
**Périmètre :** surveillance de la rotation sectorielle via ETFs SPDR et alignement avec le régime macro
**Sources :** `yfinance` (XLK, XLE, XLF, XLI, XLU, XLV, XLP, XLY, XLB, XLRE, XLC, SPY)
**Produit :** `data/sector_rotation_YYYY-MM-DD.json` + ranking sectoriel + signaux crossover

Signaux clés : **force relative 20j/60j vs SPY**, **crossover RS20/RS60** (bullish/bearish), **momentum score /10**, **alignement régime macro** (risk-on = cyclical growth, risk-off = defensive, stagflation = energy/materials). Alertes si rotation majeure détectée.

---

### Agent Social Sentiment — `scripts/agent_social.py` + `data/social_sentiment_YYYY-MM-DD.json` ← NOUVEAU
**Périmètre :** scan du sentiment retail sur les réseaux sociaux (Reddit, Yahoo Finance Community) pour compléter le sentiment institutionnel
**Sources :** Reddit API publique (r/wallstreetbets, r/stocks, r/investing, r/StockMarket), Yahoo Finance news comments
**Produit :** `data/social_sentiment_YYYY-MM-DD.json` + score retail /10 + alertes pump/dump

Signaux clés : **mention count** par ticker, **sentiment score /10** (lexique positif/négatif), **pump detection** (mots-clés YOLO/lambo/all-in), **mention spike** >3× moyenne 7j, **top posts** par engagement. Alertes si sentiment extrême (>8.5 ou <1.5) ou pump détecté.

---

### Agent FX Exposure — `scripts/agent_fx.py` + `data/fx_exposure_YYYY-MM-DD.json` ← NOUVEAU
**Périmètre :** exposition de chaque ticker aux fluctuations de change (USD, EUR, JPY, CNY) et impact estimé sur revenus, marges et valorisation
**Sources :** `data/latest.json` (macro/forex), `config/watchlist.json` (secteurs), `fmp_key_metrics` (revenus géo)
**Produit :** `data/fx_exposure_YYYY-MM-DD.json` + Bloc FX dans `_init.md` / `_update.md` + ajustements Score Fondamental/Valorisation

Signaux clés : **% revenus hors-USD** par ticker, **impact revenus/EPS estimé** selon le trend DXY, **divergence cours / modèle FX** (anomalie = autre facteur), **Score FX Impact /10** (0 = pas d'exposition, 10 = exposition + headwind actif), **classification** (Élevée/Modérée/Faible/Inverse).

**Règle absolue :** Exposition élevée + DXY headwind + non pricé → −1 pt Score Fondamental (EPS NTM sur-estimé). Exposition élevée + DXY tailwind + non pricé → +0.5 pt Score Valorisation.

---

### Agent Event-Driven — `scripts/agent_event_driven.py` + `data/events_YYYY-MM-DD.json` ← NOUVEAU
**Périmètre :** détection et analyse des événements corporates structurants — M&A, buybacks, spin-offs, activism (13D filings), changements de guidance, settlements, FDA decisions
**Sources :** `news` (Yahoo), `secFilings` (8-K, 13D), `company`, `quote`
**Produit :** `data/events_YYYY-MM-DD.json` + `Alertes/EVENT_DRIVEN.md` + `_update.md` flash + bonus/malus Score Catalyseur

Signaux clés : **spread M&A** (arbitrage), **buyback net yield** (buyback − SBC dilution), **activisme** (track record par activiste, probabilité de succès par type de demande), **guidance changes** (raise/cut/withdraw), **Score Event-Driven /10** pondéré par probabilité × asymétrie × timeline × "déjà pricé ?"

**Règles absolues :**
- M&A avec spread attractif + probabilité élevée → +2 pt Catalyseur
- Buyback net yield > 4% + cours sous-évalué → +1 pt Valorisation
- Guidance cut > 5% → −3 pt Catalyseur
- Guidance withdrawn → −2.5 pt Catalyseur
- 13D filing → `_update.md` flash automatique

---

### Agent Recommandation — `scripts/agent_recommandation.py` + `data/recommandations_YYYY-MM-DD.json` + `Recommandations/YYYY-MM-DD.md` ← NOUVEAU
**Périmètre :** traduire la synthèse de tous les agents en actions explicites : **ACHETER / CONSERVER / ATTENDRE / RÉDUIRE / VENDRE** avec niveaux d'entrée, stop-loss, take-profit et ratio risque/rendement
**Sources :** Tous les JSON `*_latest.json` (`latest`, `quant`, `geo`, `crypto`, `accounting`, `sector_rotation`, `social_sentiment`, `fx_exposure`, `events`, `upcoming_events`)
**Produit :** `data/recommandations_YYYY-MM-DD.json` + `Recommandations/YYYY-MM-DD.md` + déclenchement paper trading

**Architecture du scoring (3 axes, pondération régime-aware) :**
```
Score Opportunité = (Catalyseur × A%) + (Valorisation × B%) + (Momentum × C%)
```
Pondérations par régime macro (A/B/C = Catalyseur/Valorisation/Momentum) :
- Normal : 35 / 40 / 25
- Risk-off : 30 / 45 / 25
- Risk-on/Bull : 40 / 30 / 30
- Pré-FOMC : 35 / 40 / 25
- Pré-earnings : 45 / 30 / 25
- Stagflation : 35 / 40 / 25
- Récession : 25 / 50 / 25

**Règle de disqualification :** si un score individuel ≤ 2/10 → action exclue du rapport, même si les deux autres sont élevés.

**Score Global Composite /100 :**
```
Score Global = Score Opportunité × 10
               − Malus Accounting (0–30) + Geo (0–20) + FX (0–15) + Event (0–15) + Social (0–10) + Quant (0–20)
               + Bonus Event (0–20) + Buyback (0–10) + Sector (0–10)
               ± Timing technique (−15 à +10)
```

| Score Global ajusté | Action | Sizing | Condition |
|--------------------|--------|--------|-----------|
| ≥ 75 | **ACHETER** | Standard | Score Opportunité solide + timing favorable |
| 60–74 | **ACHETER** | Réduit | Opportunité mais confirmation technique manquante |
| 50–59 | **ATTENDRE** | — | Qualité présente mais pas de catalyseur clair |
| 35–49 | **SURVEILLER** | — | Risques détectés — pas d'action |
| < 35 | **ÉVITER** | — | Multiple malus cumulés — éviter |

**Niveaux automatiques :**
- Stop-loss suggéré = cours − 2×ATR
- Take-profit suggéré = cours + 3×ATR
- Ratio R/R = gain / perte

**Règle absolue :** Malus Accounting ≥ 25 (M-Score > −1.78 ou Z-Score < 1.81) → **ÉVITER** quel que soit le score.

---

### Paper Trading Engine — `scripts/paper_trading.py` + `Portefeuille/PAPER_*.md`
**Périmètre :** exécution virtuelle de trades sur la watchlist avec sizing institutionnel et règles de sortie strictes
**Sources :** `data/latest.json`, `data/accounting_risk_latest.json`, `Actions/*/WATCHLIST_SCORES.md`, `yfinance`
**Produit :** `Portefeuille/PAPER_POSITIONS.json` + `PAPER_TRADES.md` + `PAPER_PERFORMANCE.md`

Règles d'entrée : Score Opportunité ≥ 7/10, Filtre Qualité ≥ 4/6, Accounting ≠ 🔴, prix et ATR disponibles.
Sizing : risk 1% capital / (2×ATR), max 10% par position, Kelly fraction 0.25.
Sorties : SL = entrée − 2×ATR, TP = entrée + 3×ATR, time stop J+60, exit anticipé si score < 4/10.

---

### Score Opportunité = (Sentiment × A%) + (Fondamental × B%) + (Technique × C%)
*(pondération A/B/C déterminée par l'Agent Macro selon le régime actif)*
*(bonus/malus additionnels de l'Agent Macro et de l'Agent Flux sur le score final)*

**Règle de disqualification :** si un score individuel ≤ 2/10 → action exclue du rapport,
même si les deux autres sont élevés. Un signal très négatif prime.

**Règle Filtre Qualité :** Score Qualité ≤ 3/6 → Score Valorisation plafonné à 5/10 avant calcul final.

---

## Outils complémentaires

### Earnings Reviewer (skill) — [Agents/SKILL_EARNINGS_REVIEWER.md](Agents/SKILL_EARNINGS_REVIEWER.md)
Analyse profonde post-earnings via transcript + SEC filings. Protocole institutionnel (JPM/GS/MS format) : variance table, estimate revisions, NLP Score Confiance Management, valuation update, catalysts forward. Déclenché automatiquement sur le dernier trimestre lors de chaque nouvelle analyse d'action. Voir `Agents/SKILL_EARNINGS_REVIEWER.md` pour le workflow complet.

### NLP Transcript Analysis — `scripts/fetch_transcripts.py` + FMP ← NOUVEAU
Analyse automatisée du ton du management sur les earnings calls via FMP. Récupère les transcripts des 3 derniers trimestres, calcule : ratio Confiance/Prudence, pivots ambigus, évasions Q&A, fermeté de la guidance, Score Confiance Management /10 avec évolution inter-trimestrielle.
- **Source :** FMP Stable API (nécessite plan **Enterprise+** — le plan Starter retourne 402)
- **Output :** `data/transcripts_NLP_YYYY-MM-DD.json` → lu par l'Earnings Reviewer avant analyse manuelle
- **Règle :** si `data/transcripts_NLP_latest.json` est disponible, ses scores prévalent sur l'analyse manuelle du transcript
- **Intégration :** étape automatique dans `scripts/run_morning.sh` — si plan insuffisant, l'étape est skipped avec un message explicite. L'Earnings Reviewer bascule alors sur l'analyse manuelle.

### Market Researcher (skill) — [Agents/SKILL_MARKET_RESEARCHER.md](Agents/SKILL_MARKET_RESEARCHER.md)
Panorama sectoriel et positionnement concurrentiel. Protocole institutionnel : TAM validation (critère qualité n°6), competitive landscape (5–10 peers), peer comps spread (LTM + NTM), investment implications. Intégré dans `_init.md` lors de l'analyse initiale. Voir `Agents/SKILL_MARKET_RESEARCHER.md` pour le workflow complet.

### Calendrier earnings proactif
Lire `Actualités/CALENDRIER_EARNINGS.md` chaque matin. Si un earnings est dans ≤ 5 jours
pour un ticker watchlist → générer automatiquement `[TICKER]_YYYY-MM-DD_preview.md`.

### Alertes sur seuils
Lire `Alertes/ALERTES.md` à chaque session. Si un cours a franchi un seuil défini, générer automatiquement un `_update.md` pour le ticker concerné et logger le déclenchement dans `Alertes/ALERTES.md`.

### Module Backtesting + Apprentissage — `scripts/learn_from_errors.py` + [Opportunités/BACKTESTING.md](Opportunités/BACKTESTING.md) + [Agents/APPRENTISSAGES.md](Agents/APPRENTISSAGES.md) ← NOUVEAU
**Automatisé par `scripts/learn_from_errors.py` (étape 0 du pipeline).**

Suivi de la performance réelle de chaque opportunité signalée. Le script vérifie chaque matin les fenêtres ouvertes (J+5, J+20, J+60 pour les opportunités ; J+30, J+90, J+180 pour les prix cibles), récupère les cours via yfinance, calcule les verdicts (✅ Hit / ❌ Miss / ⚪ Scratch), et met à jour les fichiers de suivi.

**Post-mortem automatique sur Miss J+20 / J+60 :**
- Génère un fichier JSON structuré dans `Agents/POST_MORTEMS/`
- Extrait une règle corrective heuristique basée sur le type de signal
- Écrit la règle dans `Agents/APPRENTISSAGES.md` (section "Règles actives")
- Ces règles surpassent les règles par défaut des agents à chaque nouvelle session

**Alertes de calibration intégrées :**
- Win rate J+20 < 50% sur 20 derniers signaux → révision globale du scoring
- 3 misses consécutifs sur même type de catalyseur → pénalité −0.5 pt
- 3 hits consécutifs sur même type → bonus +0.3 pt empirique

---

### Module Quant — `scripts/agent_quant.py` + `data/quant_report_YYYY-MM-DD.json` ← NOUVEAU
**Étape 1 du pipeline.**

Validation statistique du système : test binomial de signification (p-value), Sharpe/Sortino/Max Drawdown sur les rendements J+20, walk-forward analysis (overfitting detection), calibration des scores par fourchette. Émet une alerte si les signaux ne sont pas significativement supérieurs au hasard (p-value > 0.20).

---

### Module Géopolitique — `scripts/agent_geo.py` + `data/geo_risk_YYYY-MM-DD.json` ← NOUVEAU
**Étape 2 du pipeline.**

Scan automatique des news politiques via regex (tarifs, sanctions, guerres, budgets, élections). Cartographie l'exposition de chaque ticker par secteur. Génère un Score Politique /10 et 3 scénarios (optimiste/central/pessimiste). Crée automatiquement un `_update.md` si score ≥ 7.

---

### Module Crypto-Correlation — `scripts/agent_crypto.py` + `data/crypto_correlation_YYYY-MM-DD.json` ← NOUVEAU
**Étape 3 du pipeline.**

Analyse la corrélation entre les tickers `crypto_exposed` (IREN) et BTC/ETH. Calcule beta BTC, NAV estimé, premium/discount, Mining Profitability Index (MPI), et Score Divergence /10. Alertes si divergence majeure ou MPI < 0.8.

### Module Sizing — [Portefeuille/MODULE_SIZING.md](Portefeuille/MODULE_SIZING.md) ← NOUVEAU
Calcul du dimensionnement optimal de chaque position : méthode ATR-based, Kelly partiel, ajustements selon score et Filtre Qualité, limites de concentration. À consulter avant tout achat.

### Module Risque Portefeuille — [Portefeuille/MODULE_RISQUE_PORTEFEUILLE.md](Portefeuille/MODULE_RISQUE_PORTEFEUILLE.md) ← NOUVEAU
Évaluation du risque global : corrélation entre positions, concentration sectorielle/factorielle, stress tests (marché -10%, taux +1%, DXY +5%, Chine -15%), VaR historique simplifiée. À lire chaque matin si des positions sont ouvertes.

### Analyst Track Record — [Agents/ANALYST_TRACK_RECORD.md](Agents/ANALYST_TRACK_RECORD.md) ← NOUVEAU
Base de données de la précision historique des analystes sell-side sur la watchlist. Alimente la pondération des upgrades/downgrades dans l'Agent Sentiment.

---

## Étape 0 absolue — Chargement données + Mémoire (CHAQUE SESSION)

> **Cette étape précède absolument tout, y compris l'Agent Macro.**
> Sans elle, le système utilise des chiffres hallucinés ou obsolètes.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 0a — CHARGEMENT DES DONNÉES (OBLIGATOIRE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Lire data/validation_report.txt
   → Si [CRITICAL] ou >2 [ERROR] : STOP. Ne pas lancer l'analyse du jour.
   → Si [WARNING] sur un ticker : noter [DONNÉES PARTIELLES] dans l'analyse.
   → Si 100% OK : continuer normalement.

2. Lire data/latest.json (snapshot du jour)
   → Extraire cours, volumes, RSI, ATR, MM pour chaque ticker watchlist
   → Extraire régime macro, VIX, taux, pétrole, DXY
   → Extraire calendrier earnings et alertes imminentes
   → Extraire blocs FMP enrichis (si clé configurée) :
     • `fmp_consensus` : price_target_avg, num_analysts
     • `fmp_ratios` : ROE, ROIC, marges, leverage, P/E, P/B (données annuelles)
     • `fmp_key_metrics` : EV multiples, returns, working capital (données annuelles)
   → Les données FMP sont en **annual** avec le plan Starter (quarterly = 402)

3. Lire data/quant_report_latest.json (si présent)
   → Signification statistique des signaux (p-value, win rate)
   → Sharpe, Sortino, Max Drawdown sur les rendements J+20
   → Calibration des scores (win rate par fourchette 6-7 / 7-8 / 8-9)
   → Si p-value > 0.20 → noter [SIGNAUX NON SIGNIFICATIFS] dans l'analyse

4. Lire data/geo_risk_latest.json (si présent)
   → Score Politique par ticker, événements détectés, scénarios
   → Si score ≥ 7 sur un ticker → créer automatiquement un `_update.md`

5. Lire data/crypto_correlation_latest.json (si présent)
   → Corrélation BTC, beta, NAV, premium/discount pour les tickers crypto-exposés
   → Si divergence_score > 7 → créer automatiquement un `_update.md`

6. Lire data/accounting_risk_latest.json (si présent)
   → Vérifier M-Score > -1.78 ou Z-Score < 1.81 → exclure du long / marquer 🔴 dans l'analyse
   → Piotroski F-Score ≤ 3 → plafonner Score Valorisation à 5/10
   → Sloan Ratio > 0.1 → qualifier la qualité des bénéfices comme faible

7. Lire data/sector_rotation_latest.json (si présent)
   → Top3 sectors → privilégier les tickers de ces secteurs dans le scoring
   → Bottom3 sectors → pénaliser les tickers de ces secteurs (−0.5 pt)
   → Crossover détecté → mentionner la rotation en cours dans le bulletin

8. Lire data/social_sentiment_latest.json (si présent)
   → Sentiment retail /10 par ticker, mention count, pump detection
   → Si sentiment extrême (>8.5 ou <1.5) → noter dans l'analyse avec [RETAIL EXTREME]
   → Si pump detected → mentionner avec [PUMP ALERT] et vérifier avec sources institutionnelles

9. Lire data/transcripts_NLP_latest.json (si présent)
   → Extraire Score Confiance Management pour chaque ticker
   → Si un earnings a été publié récemment → le NLP pré-calculé prime sur l'analyse manuelle
   → Si absent (plan Starter = transcripts indisponibles) → l'analyse NLP sera faite manuellement

10. Lire data/fx_exposure_latest.json (si présent)
    → Score FX Impact par ticker, direction (headwind/tailwind), divergence cours/modèle
    → Si exposition élevée + DXY headwind → noter [FX HEADWIND] dans l'analyse
    → Si divergence > 5% → alerter [ANOMALIE FX] et chercher autre facteur

11. Lire data/events_latest.json (si présent)
    → Événements corporates détectés : M&A, buybacks, activism, guidance changes
    → Si M&A annoncé sur ticker watchlist → ajuster Score Catalyseur +2 pt
    → Si buyback net yield > 4% → ajuster Score Valorisation +0.5 pt
    → Si guidance cut > 5% → ajuster Score Catalyseur −3 pt
    → Si 13D filing → créer `_update.md` flash si pas déjà fait

12. Lire `data/upcoming_events_latest.json` (si présent) et `Alertes/UPCOMING_EVENTS.md`
   → Earnings à ≤ 3j : vérifier que `_preview.md` existe, sinon alerter immédiatement
   → Insider trades significatifs : noter dans l'analyse du jour
   → Upgrades/downgrades massifs : ajuster le Score Catalyseur
   → News CEO / M&A / guidance : générer `_update.md` flash si pas encore fait

13. Scanner Actions/ pour les fichiers `*_DRAFT_init.md` — COMPLÉTION AUTO OBLIGATOIRE
   → Pour chaque DRAFT détecté : l'agent LLM complète automatiquement l'analyse sans prompt utilisateur
   → Lire `data/latest.json` pour remplir les champs techniques (RSI, ATR, MM, FMP, options)
   → Lire `data/quant_report_latest.json` pour le bloc Quant
   → Lire `data/geo_risk_latest.json` pour le bloc Géopolitique
   → Exécuter Market Researcher (TAM, peers, competitive landscape, multiples LTM+NTM)
   → Exécuter Agent Fondamental (Filtre Qualité 6 critères, DCF, valorisation)
   → Exécuter Agent Technique (interprétation RSI, niveaux, timing, force relative)
   → Exécuter Agent Sentiment (consensus, options, news, upgrades/downgrades)
   → Sauvegarder le fichier complété sous `Actions/{TICKER}/{TICKER}_YYYY-MM-DD_init.md`
   → Créer `INDEX.md` avec thèse courante + historique des fichiers
   → Mettre à jour `Actions/WATCHLIST_SCORES.md` et `Actualités/CALENDRIER_EARNINGS.md`
   → Renommer le DRAFT en `_DRAFT_init.md` (archive) ou le supprimer
   → **Règle absolue : ne JAMAIS laisser un DRAFT non complété** — c'est une tâche automatique

14. Scanner Actions/ pour les fichiers `*_DRAFT_refresh.md` — FULL REFRESH AUTO OBLIGATOIRE
   → Pour chaque FULL REFRESH détecté : l'agent LLM réécrit l'analyse complète
   → Lire la thèse précédente dans `Actions/{TICKER}/INDEX.md` (section 📜 du DRAFT)
   → Lire `data/latest.json` pour les données actualisées
   → Déterminer si l'événement majeur **confirme, modifie ou invalide** la thèse précédente
   → Recalculer le Filtre Qualité 6 critères (l'événement peut changer le moat, le TAM, etc.)
   → Réviser le prix cible et le Score Opportunité
   → Sauvegarder le fichier complété sous `Actions/{TICKER}/{TICKER}_YYYY-MM-DD_init.md`
   → **Créer / mettre à jour `Actions/{TICKER}/REFRESH_LOG.md`** avec la date, les triggers, et la conclusion
   → **Mettre à jour `INDEX.md`** avec la nouvelle thèse courante et un lien vers l'ancienne
   → Renommer le DRAFT_refresh en `_DRAFT_refresh.md` (archive) ou le supprimer
   → **Règle absolue : ne JAMAIS laisser un DRAFT_refresh non complété**

15. RÈGLE ABSOLUE : utiliser EXCLUSIVEMENT les chiffres de data/latest.json
   → Ne JAMAIS "deviner" un cours, un multiple, ou une métrique technique
   → Si une donnée est manquante dans latest.json → marquer [UNSOURCED] ou [DONNÉES MANQUANTES]
   → Le LLM ne remplace PAS une API de données.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 0b — CHARGEMENT DE LA MÉMOIRE (OBLIGATOIRE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. Lire Agents/APPRENTISSAGES.md en entier
5. Charger toutes les règles de la section "Règles actives issues des erreurs"
6. Ces règles surpassent les règles par défaut de tous les agents

7. Vérifier les 3 fichiers de suivi pour les fenêtres à clôturer :
   → Opportunités/BACKTESTING.md (J+5, J+20, J+60)
   → Actions/SUIVI_PRIX_CIBLES.md (J+30, J+90, J+180)
   → Actions/SUIVI_EARNINGS_PREDICTIONS.md (fenêtres en attente de résultats)

8. **Automatique — `scripts/learn_from_errors.py`** :
   → Ce script est exécuté en étape 0 du pipeline `run_morning.sh`
   → Il lit les fenêtres ouvertes, récupère les cours via yfinance, calcule les verdicts
   → Met à jour les fichiers de suivi (BACKTESTING.md, SUIVI_PRIX_CIBLES.md)
   → Sur Miss J+20/J+60 : génère un post-mortem JSON dans `Agents/POST_MORTEMS/`
   → Écrit la règle corrective extraite dans `Agents/APPRENTISSAGES.md`
   → L'agent relit ensuite ces fichiers pour charger les règles actives

9. Seulement ensuite → lancer l'Agent Macro
```

---

## Workflows

### Créer une nouvelle analyse d'action

Ce workflow produit **toujours** 3 livrables en séquence automatique, sans attendre de commande supplémentaire.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 1 — STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Créer le dossier Actions/[TICKER]/
2. Copier les templates depuis _TEMPLATE_ACTION/
3. Renommer les fichiers avec le bon ticker et la date du jour

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 2 — FILTRE QUALITÉ ← OBLIGATOIRE EN PREMIER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Avant toute valorisation, calculer les 6 critères qualité (voir Agents/AGENT_FONDAMENTAL.md) :
→ Revenue CAGR 5 ans ≥ 20% (calculer depuis `statements`)
→ Profit CAGR 5 ans ≥ 20% (EPS ajusté, calculer depuis `statements`)
→ Total Assets / Total Liabilities > 1.0 (dernier bilan)
→ FCF positif et en croissance sur 5 ans (tendance sur 5 exercices)
→ Avantage compétitif identifiable (moat structurel)
→ Industrie en forte croissance (TAM ×5 minimum / 10 ans)

Verdict :
- 5–6/6 → ✅ Quality Compounder — continuer l'analyse complète
- 4/6 → ⚠️ Quality Partielle — continuer, signaler les manques, −0.5 pt score Val
- ≤ 3/6 → 🔴 Hors périmètre — mentionner dans l'analyse, plafonner score Val à 5/10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 3 — ANALYSE INITIALE (Market Researcher + Technique + Macro)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. Lancer Market Researcher (voir `Agents/SKILL_MARKET_RESEARCHER.md`) :
   → Panorama sectoriel et position concurrentielle (5–10 peers)
   → TAM du marché addressable (valider le critère 6 du Filtre Qualité)
   → Multiples de valorisation vs pairs LTM ET NTM (P/E, EV/EBITDA, EV/Sales)
   → Peer comps spread avec outlier flags et valuation context
   → DCF simplifié + valeur intrinsèque + Reverse DCF (croissance implicite)
   → Thèse d'investissement, catalyseurs sectoriels et risques
5. Ajouter automatiquement la couche technique :
   → RSI 14j, MACD, ATR 14j, VWAP, Bollinger Bands, MM50j/MM200j
   → Stop-loss ATR = cours − 2×ATR
   → Verdict timing : Favorable / Neutre / Défavorable
6. Ajouter la carte d'exposition macro :
   → Sensibilité USD, taux 10 ans US, pétrole, Chine, inflation
   → Exprimer en impact estimé sur le cours (ex : "+1% taux → -X%")
   → Sauvegarder le tout dans [TICKER]_YYYY-MM-DD_init.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 3b — RÉSULTATS TRIMESTRIELS (Earnings Reviewer) ← AUTOMATIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. Lancer AUTOMATIQUEMENT Earnings Reviewer (voir `Agents/SKILL_EARNINGS_REVIEWER.md`) :
   → Identifier le dernier trimestre disponible (actuellement Q1 2026)
   → Récupérer le transcript du call earnings + dépôts SEC (10-Q / 8-K)
   → Variance table : Actual vs Consensus vs Prior Estimate (Revenue, GM, EBITDA, EPS, FCF)
   → NLP Score Confiance Management (Ratio Confiance/Prudence, évasions, pivots)
   → Estimate revisions : old vs new FY / next FY estimates avec justification
   → Valuation update : DCF, P/E, EV/EBITDA → nouveau price target si nécessaire
   → Catalysts forward : 3–5 événements à surveiller avec timeline et probabilité
   → Évaluer l'impact sur la thèse construite à l'étape 3
   → Sauvegarder dans [TICKER]_YYYY-MM-DD_earnings.md
   → Si preview existait : comparer prédictions vs réalités dans SUIVI_EARNINGS_PREDICTIONS.md
   → Si les résultats ne sont pas encore disponibles pour Q1 2026 :
      utiliser le dernier trimestre connu et le mentionner explicitement

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 4 — INDEX, WATCHLIST ET ALERTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. Remplir INDEX.md :
   → Thèse courante (synthèse init + earnings)
   → Historique des fichiers créés
   → Agenda des prochains événements (prochain earnings, conférences)
8. Ajouter [TICKER] dans Actualités/WATCHLIST.md avec seuils d'alerte par défaut
9. Ajouter [TICKER] dans Actualités/CALENDRIER_EARNINGS.md avec la date du prochain earnings
10. Ajouter les seuils d'alerte dans Alertes/ALERTES.md :
    → Alerte baisse : cours < prix cible - 15%
    → Alerte hausse : cours > prix cible
    → Alerte volume : volume > 2x moyenne 20j

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPE 5 — ENREGISTREMENT SUIVI APPRENTISSAGE ← OBLIGATOIRE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
11. Enregistrer le prix cible dans Actions/SUIVI_PRIX_CIBLES.md :
    → Ligne : Date · Ticker · _init.md · Reco · Prix cible · Cours actuel · Upside%
    → Calculer et noter les dates J+30, J+90, J+180
    → Ajouter dans la section "Fenêtres ouvertes"
12. Si le prochain earnings est dans ≤ 30 jours : créer [TICKER]_YYYY-MM-DD_preview.md
    → Enregistrer les prédictions dans Actions/SUIVI_EARNINGS_PREDICTIONS.md
```

> **Règle absolue :** l'Earnings Reviewer est toujours lancé automatiquement lors d'une nouvelle analyse, sans qu'il soit nécessaire de le demander. Le trimestre cible par défaut est le plus récent disponible (Q1 2026 à la date du 2026-05-09).

**Commande :** `Analyse [TICKER], crée le dossier Actions/[TICKER]/ et sauvegarde l'analyse initiale`

---

### Workflow du matin — Bulletin + Analyses + Opportunités

Ce workflow produit les 3 livrables en séquence. Une seule commande suffit.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0 — ALERTES ET CALENDRIER (AVANT TOUT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Lire Alertes/ALERTES.md → vérifier chaque seuil vs cours du jour
   → Si seuil franchi : créer automatiquement un _update.md + logger le déclenchement
2. Lire Alertes/UPCOMING_EVENTS.md → identifier les événements 🔴 ≤3j et 🟡 ≤7j
   → Pour chaque earnings ≤ 3j : vérifier que _preview.md existe
   → Pour chaque insider/upgrade/downgrade majeur : noter dans l'analyse
3. Lire Actualités/CALENDRIER_EARNINGS.md → identifier les earnings dans les 5 prochains jours
   → Pour chaque ticker concerné : générer automatiquement un _preview.md
4. Lire Portefeuille/POSITIONS.md → calculer P&L ouvert sur chaque position

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0b — SUPPLY CHAIN CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. Pour chaque ticker watchlist ayant un fichier SUPPLY_CHAIN.md :
   → Scanner les news du jour sur les fournisseurs/clients 🔴 Critiques et 🟡 Importants
   → Si news significative détectée → préparer une analyse d'impact (traitée en Phase 2)
   → Si résultats publiés par un fournisseur/client clé → déclencher le protocole d'impact

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0c — FULL REFRESH CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. Vérifier s'il existe des `*_DRAFT_refresh.md` dans Actions/
   → Pour chaque DRAFT_refresh : réécrire l'analyse complète (confirme/modifie/invalide la thèse)
   → Mettre à jour INDEX.md + REFRESH_LOG.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — COLLECTE MONDIALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. Lire Actualités/WATCHLIST.md
8. Récupérer cours d'ouverture de tous les tickers de la watchlist
9. Scanner les news mondiales du jour :
   • Amériques : USA, Canada, Amérique latine
   • Europe : UE, UK, Suisse, Russie/Ukraine
   • Asie-Pacifique : Chine, Japon, Corée, Inde, Australie
   • Moyen-Orient & Afrique
   • Thèmes transversaux : banques centrales, macro, matières premières,
     M&A, régulation, géopolitique, IA/tech

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — ANALYSES D'IMPACT (watchlist)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10. Pour chaque actu à impact ≥ modéré :
   → Identifier les tickers watchlist concernés (direct + indirect)
   → Utiliser la carte d'exposition macro de l'_init.md pour chiffrer l'impact
11. Pour chaque ticker impacté :
   → Lire TOUS les fichiers Actions/[TICKER]/ (historique complet)
   → Analyser : exposition revenus géo, supply chain, coûts, devises, taux
   → Comparer position vs concurrents face à cet événement
   → Scanner radar activité inhabituelle : volume, short interest, insiders, options
   → Construire 3 scénarios (optimiste/central/pessimiste) + probabilités
   → Réviser thèse et prix cible si nécessaire
   → Créer Actions/[TICKER]/[TICKER]_YYYY-MM-DD_update.md
   → Mettre à jour Actions/[TICKER]/INDEX.md
   → Si position ouverte dans Portefeuille/POSITIONS.md : recalculer P&L et réviser stop-loss

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — DÉTECTION D'OPPORTUNITÉS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
12. Pour chaque actu identifiée, chercher quelles actions en bénéficient :
   → Actions de la watchlist ★ (lire leur dossier pour contexte complet)
   → Actions hors watchlist détectées via les news du jour
13. Scorer chaque opportunité détectée sur 3 axes :
   • Catalyseur actualité /10 — l'actu crée-t-elle un avantage concret ?
   • Valorisation /10 — l'action est-elle décotée vs pairs et valeur intrinsèque ?
   • Momentum /10 — le cours confirme-t-il le signal fondamental ?
   → Score final = (Catalyseur × 40%) + (Valorisation × 35%) + (Momentum × 25%)
14. Ne retenir que les scores ≥ 6/10
15. Regrouper par thème (ex : réarmement, IA, baisse des taux, énergie...)
16. Créer Opportunités/YYYY-MM-DD.md avec le podium + analyse par thème
17. Mettre à jour Opportunités/HISTORIQUE_SCORES.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — BULLETIN FINAL & AUTO-PUSH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
18. Sauvegarder Actualités/YYYY-MM-DD.md avec :
    → Toutes les news mondiales classées par zone
    → Section "Analyses approfondies" (liens vers _update.md créés)
    → Section "Opportunités du jour" (extrait du podium + lien vers rapport)
19. `run_morning.sh` exécute `scripts/auto_push.sh` automatiquement :
    → Commit des nouveaux fichiers générés (data, analyses, bulletins)
    → Push vers `origin main` sur https://github.com/Wzxgreed/argus-ia
    → Si push échoue (réseau, etc.) → log warning, pipeline continue
```

**Commande unique du matin :**
`Lance le bulletin du matin : actualités mondiales, analyse d'impact sur ma watchlist et rapport d'opportunités du jour`

**Ou via Makefile :**
```bash
make pipeline
```

---

### Workflow du lundi — Revue hebdomadaire

> Voir `Agents/WORKFLOW_SEMAINE.md` pour le protocole complet.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE H0 — Mémoire + fenêtres à clôturer (3 fichiers de suivi)
PHASE H1 — Portefeuille : P&L + révision stop-loss ATR
PHASE H2 — Risque : corrélations + VaR + stress tests
PHASE H3 — Watchlist scores + révision prix cibles
PHASE H4 — Calendrier earnings + alertes composites
PHASE H5 — Rapport hebdomadaire YYYY-WXX.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Commande :** `Lance la revue hebdomadaire du portefeuille et de la watchlist`

---

### Mise à jour post-earnings

```
1. Lire Actions/[TICKER]/INDEX.md → contexte et thèse précédente
2. Lire toutes les analyses dans Actions/[TICKER]/ pour avoir l'historique complet
3. Lancer Earnings Reviewer
4. Créer Actions/[TICKER]/[TICKER]_YYYY-MM-DD_earnings.md
5. Mettre à jour INDEX.md (thèse courante + historique)
6. Lier au bulletin Actualités/YYYY-MM-DD.md si existant
```

**Commande :** `Analyse les résultats Q[X] de [TICKER] et mets à jour le dossier Actions/[TICKER]/`

---

## Niveaux d'impact (utilisés dans tous les fichiers)

| Niveau | Définition | Action de l'agent |
|--------|-----------|-------------------|
| 🔴 Élevé | Mouvement >3% probable ou thèse remise en cause | Analyse approfondie complète + créer `_update.md` + maj INDEX.md |
| 🟡 Modéré | Mouvement 1-3% ou élément à surveiller | Analyse exposition partielle + mentionner dans INDEX.md + bulletin |
| 🟢 Faible | Contexte de fond, impact indirect | Logguer dans le bulletin uniquement |

## Profondeur de l'analyse approfondie

Quand un ticker suivi est détecté dans l'actualité, l'agent doit obligatoirement :

1. **Lire l'historique complet** — tous les fichiers du dossier `Actions/[TICKER]/` dans l'ordre chronologique
2. **Recontextualiser** — replacer l'événement par rapport aux risques déjà identifiés dans les analyses passées
3. **Mesurer l'exposition** — revenus géographiques, supply chain, coûts, devises, taux
4. **Comparer aux concurrents** — cet événement avantage-t-il ou désavantage-t-il [TICKER] vs ses pairs ?
5. **Chiffrer l'impact** — estimer l'effet en % sur le cours et réviser le prix cible si nécessaire
6. **Construire 3 scénarios** — avec probabilités et impact sur la thèse pour chacun
7. **Conclure clairement** — la thèse est-elle confirmée, renforcée, ou remise en cause ?

---

## Commandes rapides

| Action | Commande |
|--------|----------|
| ☀️ **Matin complet** | `Lance le bulletin du matin : actualités mondiales, analyse d'impact sur ma watchlist et rapport d'opportunités du jour` |
| Nouvelle analyse | `Analyse [TICKER], crée le dossier Actions/[TICKER]/ et sauvegarde l'analyse initiale` |
| Post-earnings | `Analyse les résultats Q[X] de [TICKER] et mets à jour le dossier Actions/[TICKER]/` |
| Impact spécifique | `Analyse l'impact de [événement] sur [TICKER] en te basant sur l'historique du dossier` |
| Opportunités seules | `Quelles sont les meilleures opportunités aujourd'hui en fonction des actualités et des cours ?` |
| Thème spécifique | `Quelles actions bénéficient le plus de [thème/événement] aujourd'hui ?` |
| Comparaison | `Compare [TICKER1] et [TICKER2] face à [événement] en lisant leurs dossiers respectifs` |
| Ajouter à la watchlist | `Ajoute [TICKER] en priorité [haute/moyenne/basse] dans Actualités/WATCHLIST.md` |
| Exposition géo | `Quelles actions de ma watchlist sont exposées à [pays/région] ?` |
| Perf. des signaux | `Montre-moi la performance des opportunités signalées ce mois-ci` |
| **Analyse technique** | `Analyse technique de [TICKER] : RSI, MACD, moyennes mobiles, niveaux clés` |
| **Preview earnings** | `Prépare le preview earnings de [TICKER] avant les résultats du [DATE]` |
| **Portefeuille** | `Mets à jour mon portefeuille : j'ai acheté/vendu [X] actions [TICKER] à $[PRIX]` |
| **P&L portefeuille** | `Quel est mon P&L actuel sur toutes mes positions ?` |
| **Radar activité** | `Scanne l'activité inhabituelle sur [TICKER] : volume, insiders, short interest, options` |
| **Exposition macro** | `Quelles actions de ma watchlist sont les plus exposées à [hausse des taux / dollar / pétrole] ?` |
| **Alertes actives** | `Montre-moi les alertes actives et celles déclenchées cette semaine` |
| **Ajouter alerte** | `Ajoute une alerte sur [TICKER] : cours < $[PRIX] / cours > $[PRIX] / volume > 2x` |
| **Clôturer position** | `Clôture ma position sur [TICKER] vendu à $[PRIX], mets à jour la performance` |
| **Régime macro** | `Quel est le régime macro actuel ? Quelle pondération appliquer aujourd'hui ?` |
| **Analyse flux** | `Analyse les flux institutionnels sur [TICKER] : 13F, ETF, dark pool, gamma` |
| **Force relative** | `Quels tickers de ma watchlist ont la meilleure force relative vs S&P ce mois-ci ?` |
| **Sizing position** | `Quel sizing recommandes-tu pour [TICKER] avec un capital de $[MONTANT] ?` |
| **Risque portefeuille** | `Analyse le risque de mon portefeuille actuel : corrélations, concentration, stress tests` |
| **Suivi backtesting** | `Mets à jour le suivi des signaux : quels résultats à J+5/J+20/J+60 aujourd'hui ?` |
| **Unusual options** | `Scanne l'activité options inhabituelles sur [TICKER] : volume vs OI, max pain, GEX` |
| **Short squeeze** | `Y a-t-il des setups short squeeze dans ma watchlist aujourd'hui ?` |
| **Saisonnalité** | `Quels tickers de ma watchlist sont en période saisonnièrement favorable en [mois] ?` |
| **Supply chain** | `Analyse la supply chain de [TICKER] : fournisseurs et clients clés, risques et opportunités` |
| **Supply chain news** | `Y a-t-il des news aujourd'hui sur les fournisseurs ou clients clés de ma watchlist ?` |
| **NLP transcript** | `Analyse le ton du management de [TICKER] sur les 3 derniers trimestres` |
| **Job postings** | `Quels signaux de recrutement/licenciements détectes-tu sur [TICKER] ?` |
| **Revue hebdo** | `Lance la revue hebdomadaire du portefeuille et de la watchlist` |
| **Watchlist scorée** | `Mets à jour le dashboard WATCHLIST_SCORES.md avec les scores du jour` |
| **Révisions EPS** | `Quelles actions de ma watchlist ont le meilleur momentum de révisions d'estimations ?` |
| **Alerte composite** | `Ajoute une alerte composite sur [TICKER] : [condition1] ET [condition2]` |
| **Corrélations** | `Quels sont les tickers les plus corrélés dans ma watchlist ? Y a-t-il une sur-concentration ?` |
| **Impact corrélé** | `[TICKER] a bougé de X% — quels autres tickers de ma watchlist sont impactés par corrélation ?` |
| **Calibration** | `Effectue la calibration trimestrielle des scores : compare les distributions vs les résultats réels` |
| **Pattern similaire** | `Y a-t-il un pattern historique similaire à la configuration actuelle de [TICKER] ?` |
| **Prédiction earnings** | `Lance le modèle de prédiction de surprise earnings pour [TICKER] (earnings le [DATE])` |
| **Hedge Risk-off** | `Le régime est Risk-off — calcule le hedge recommandé pour mon portefeuille actuel` |
| **Market Researcher** | `Quel est le panorama sectoriel de [TICKER] ? Compare-le à ses pairs (TAM, comps, landscape)` |
| **Earnings Reviewer** | `Analyse les résultats Q[X] de [TICKER] avec variance table, NLP management, estimate revisions` |
| **Peer comps refresh** | `Actualise les multiples comparatifs de [TICKER] et de ses concurrents directs` |
| **NLP management deep dive** | `Analyse le ton du management de [TICKER] sur les 3 derniers trimestres (NLP Score Confiance)` |
| **Estimate revision track** | `Quelles revisions d'estimations pour [TICKER] depuis le dernier earnings ?` |
| **Contrats gouvernementaux** | `Y a-t-il des nouveaux contrats gouvernementaux annoncés sur [TICKER] ou ses concurrents ?` |
| **Événements à venir** | `Quels sont les prochains événements sur ma watchlist ? (earnings, CEO, M&A, guidance)` |
| **Watchman scan** | `Lance le scan watchman : détecte les earnings, insiders, upgrades, news structurantes` |
| **Full refresh ticker** | `Force un full refresh de [TICKER] : réécris l'analyse complète avec les données du jour` |
| **REFRESH_LOG** | `Montre-moi l'historique des full refreshes pour [TICKER]` |
| **Accounting scan** | `Lance le scan comptable : M-Score, Z-Score, F-Score, Sloan Ratio pour toute la watchlist` |
| **Sector rotation** | `Quelle est la rotation sectorielle du jour ? RS vs SPY, crossovers, alignement macro` |
| **Paper trading** | `Lance le paper trading engine : nouvelles entrées, exits, mise à jour performance` |
| **Paper P&L** | `Quel est le P&L du portefeuille paper trading ?` |
| **Social sentiment** | `Quel est le sentiment retail sur [TICKER] aujourd'hui ?` |
| **Pump detection** | `Y a-t-il des signaux de pump/dump sur ma watchlist ?` |
| **Exposition FX** | `Quelle est l'exposition FX de [TICKER] ? DXY, EUR, CNY — impact revenus/EPS` |
| **Recommandations** | `Quelles sont les recommandations aujourd'hui ?` |
| **Recommandation ticker** | `Que faire sur [TICKER] ? Acheter, conserver, ou vendre ?` |
| **Niveaux d'entrée** | `Quel est le ratio risque/rendement de [TICKER] ? SL et TP suggérés ?` |
| **Positions à fermer** | `Quelles positions devrais-je fermer ?` |
| **FX scan watchlist** | `Scanne l'exposition FX de toute ma watchlist : headwind, tailwind, divergence` |
| **Event-Driven scan** | `Y a-t-il des événements corporates sur [TICKER] ? (M&A, buyback, guidance, activism)` |
| **M&A radar** | `Scanne les rumeurs et annonces M&A sur ma watchlist` |
| **Buyback quality** | `Quel est le net buyback yield de [TICKER] ? Qualité du programme ?` |
| **Activism tracker** | `Y a-t-il des 13D filings ou activism sur ma watchlist ?` |
| **Guidance tracker** | `Quels tickers ont changé de guidance récemment ?` |

---

## Infrastructure & Auto-Push GitHub

### Architecture fetch Yahoo — worker daemon pré-chauffé
Pour éviter les hangs au niveau C (libcurl) et le coût d'import répété de yfinance (60–90s), `fetch_prices.py` utilise un **pool de daemons** (`scripts/yahoo_worker_daemon.py`) :
- Chaque daemon charge yfinance **une seule fois** au démarrage, puis sert plusieurs tickers via stdin/stdout (JSON line protocol)
- `fetch_prices.py` instancie `YahooWorkerPool(num_workers=2)` qui répartit les tickers en round-robin entre les daemons
- Si un daemon échoue, le worker est automatiquement remplacé
- **Timeout daemon** : 240s pour le chargement initial, 60s par ticker post-import
- **Inactivité** : le daemon s'arrête automatiquement après 300s sans requête
- **Fallback FMP** : si Yahoo est indisponible, `fetch_prices.py` tente `fmp.get_quote()` pour récupérer au moins le cours de clôture
- **Écriture atomique** : `tempfile.NamedTemporaryFile` + `os.replace()` pour éviter les fichiers corrompus

Résultat : 6 tickers en ~40s au lieu de 5–8 min avec l'ancienne architecture one-shot.

### Wrapper HTTP — `scripts/http_utils.py`
Tous les appels réseau passent par `http_get()` avec :
- **Retry exponentiel** : 3 tentatives, backoff 1s → 2s → 4s
- **Caching disque** : `data/cache/YYYY-MM-DD/<md5>.json`, TTL = fin de journée UTC
- **Timeout** : 15s par défaut
- **Gestion d'erreurs** : retourne `{"error": True, "reason": "..."}` au lieu de raise

**Circuit breaker** (P4) — par domaine :
- 3 échecs consécutifs → circuit **OPEN** (bloque les appels pendant 60s)
- Après 60s → circuit **HALF_OPEN** (teste un appel)
- Succès → circuit **CLOSED** (normal)
- Empêche les cascades de requêtes vers un service en panne (ex: rate-limit Yahoo)

### Helper `scripts/auto_push.sh`
Commit + push automatique des artefacts générés (data, analyses, alertes, logs). Usage :
```bash
./scripts/auto_push.sh "Message de commit optionnel"
```
Stage automatiquement : `data/`, `Actions/`, `Actualités/`, `Opportunités/`, `Alertes/`, `Portefeuille/`, `Agents/`, `logs/`, `scripts/`, `Makefile`, `README.md`, `requirements.txt`, `pyproject.toml`, `.github/`.

### `Makefile` — Commandes disponibles
```bash
make install           # Créer venv + installer dépendances
make test              # Suite de tests (pytest)
make lint              # Ruff + Black check
make format            # Black + Ruff fix
make pipeline          # Lancer le pipeline du matin (avec auto-push final)
make push              # Lint + test + push manuel
make clean             # Nettoyer fichiers temporaires

# Pipeline parallèle en 4 phases :
make group-a           # Phase A : agents indépendants (parallel)
make group-b           # Phase B : fetch données brutes (séquentiel)
make group-c           # Phase C : agents dépendants (parallel)
make group-d           # Phase D : agrégation finale (séquentiel)
make pipeline-make      # Pipeline complet via Makefile (group-a → b → c → d)

# Agents individuels avec auto-push intégré :
make agent-watchman    # Watchman → commit + push
make agent-geo         # Géopolitique → commit + push
make agent-crypto      # Crypto-correlation → commit + push
make agent-accounting  # Accounting risk → commit + push
make agent-sector      # Sector rotation → commit + push
make agent-social      # Social sentiment → commit + push
make agent-fx          # FX exposure → commit + push
make agent-event       # Event-Driven (M&A, buybacks, activism) → commit + push
make agent-reco        # Recommandations (acheter/conserver/vendre) → commit + push
```

### CI GitHub Actions
Fichier `.github/workflows/ci.yml` — exécuté à chaque push :
1. Lint (Ruff)
2. Tests (pytest, filtre `-m "not integration and not slow"`)
3. Validation JSON Schema (`scripts/validate.py`)

### Dépôt GitHub
URL distante : `https://github.com/Wzxgreed/argus-ia.git`

---

## Notes

- L'`INDEX.md` de chaque dossier est la source de vérité sur la thèse courante — toujours le lire avant une mise à jour.
- Les fichiers `_update.md` permettent de retracer l'évolution de la thèse dans le temps.
- Ne jamais modifier une analyse passée — toujours créer un nouveau fichier daté.
- Ces fichiers sont des outils d'analyse, pas des conseils en investissement.
