---
name: agent-crypto
metadata:
  type: agent
---

# Agent Crypto-Correlation

> **Rôle** : Modéliser la relation entre les tickers crypto-exposés (IREN) et les marchés des cryptomonnaies (BTC, ETH, hash rate, mining profitability). Calculer les écarts NAV, les corrélations historiques, et détecter les divergences.
> **Exécution** : Automatique à chaque matin (étape 0e du pipeline). Se déclenche manuellement sur demande pour IREN ou tout nouveau miner ajouté à la watchlist.
> **Output** : `data/crypto_correlation_YYYY-MM-DD.json` + bloc Crypto dans `_init.md` / `_update.md` pour les tickers concernés.

---

## Périmètre

### Tickers concernés
- **IREN** (primaire) — miner vertical de Bitcoin, datacenters AU/CA
- **Futur** : tout nouveau ticker classé `crypto_exposed: true` dans `config/watchlist.json`

### Données suivies
| Donnée | Source | Fréquence | Usage |
|--------|--------|-----------|-------|
| Prix BTC | yfinance (BTC-USD) | Quotidien | Corrélation de base |
| Prix ETH | yfinance (ETH-USD) | Quotidien | Proxy altcoins |
| Hash rate BTC | API blockchain.info | Quotidien | Capacité réseau |
| Difficulty | API blockchain.info | ~2 semaines | Profitabilité du mining |
| Coût énergie IREN | Filings / IR | Trimestriel | Marges réelles |
| BTC holdings IREN | Filings / IR | Trimestriel | NAV crypto |

---

## Workflow — 5 phases

### Phase 1 : Collecte des données crypto

**Via yfinance (BTC-USD, ETH-USD) :**
- Prix de clôture, volume, volatilité 30j
- Rendement sur 1j, 7j, 30j, 90j
- Corrélation rolling 30j avec le ticker concerné

**Via blockchain.info API (gratuit) :**
- `https://blockchain.info/q/hashrate` — hash rate global (EH/s)
- `https://blockchain.info/q/getdifficulty` — difficulté actuelle
- `https://api.blockchain.info/charts/market-price?timespan=30days` — prix historique BTC

---

### Phase 2 : Corrélation ticker vs crypto

**Métriques calculées :**

| Métrique | Calcul | Seuil d'alerte |
|----------|--------|----------------|
| **Corrélation 30j** | Pearson(ticker, BTC) sur 30j | < 0.50 = décorrélation anormale |
| **Corrélation 90j** | Pearson(ticker, BTC) sur 90j | Référence long terme |
| **Beta BTC** | Cov(ticker, BTC) / Var(BTC) | > 1.5 = sur-exposition ; < 0.5 = sous-exposition |
| **Beta ETH** | Cov(ticker, ETH) / Var(ETH) | Proxy pour altcoin exposure |
| **R²** | % variance du ticker expliquée par BTC | < 30% = d'autres facteurs dominent |
| **Lag analysis** | Croisement de corrélations décalées | Si ticker lead BTC = signal d'info privilégiée |

**Output structuré :**
```json
{
  "ticker": "IREN",
  "crypto": {
    "correlation_30d": 0.78,
    "correlation_90d": 0.72,
    "beta_btc": 1.35,
    "beta_eth": 0.89,
    "r2_btc": 0.61,
    "trend": "🔴 Augmentation de la corrélation (+8% vs 30j)"
  }
}
```

---

### Phase 3 : Analyse NAV (Net Asset Value)

**Pour les miners de Bitcoin :**

Le cours d'IREN devrait théoriquement suivre la valeur de ses actifs crypto + sa capacité de génération future.

**Formule simplifiée NAV :**
```
NAV ≈ (BTC_holdings × Prix BTC) + (Hashrate_capacity × Mining_profitability)
```

**Écart NAV (Premium / Discount) :**
```
Premium = (Market Cap - NAV) / NAV
```

| Écart | Interprétation | Action |
|-------|---------------|--------|
| Premium > 30% | Marché surestime la valeur | Signal de vente / Attendre correction |
| Premium 0–15% | Valorisation équitable | Neutre |
| Discount > 15% | Marché sous-estime la valeur | Opportunité d'achat si qualité confirmée |
| Discount > 40% | Marché panique ou insolvante | Vérifier liquidité et dette |

**Note :** Le NAV exact nécessite les filings trimestriels (BTC holdings, hashrate opérationnel, coût énergie). En l'absence de données temps réel, on utilise des approximations basées sur les dernières données connues.

---

### Phase 4 : Mining Profitability Index (MPI)

**Indice synthétique de la profitabilité du mining :**

```
MPI = (Prix BTC × Récompense bloc) / (Difficulty × Coût énergie kWh)
```

**Interprétation :**
- MPI > 1.5 : Mining très rentable → les miners peuvent accumuler du BTC → catalyseur haussier pour IREN
- MPI 0.8–1.5 : Rentabilité moyenne → neutralité
- MPI < 0.8 : Mining non rentable → risque de dilution, vente de BTC, fermeture de sites → risque pour IREN

**Alertes :**
- Si MPI passe sous 1.0 alors que BTC est encore élevé → la difficulté a augmenté trop vite = signal de faiblesse structurelle
- Si MPI > 2.0 et que IREN n'a pas augmenté → discount anormal = opportunité

---

### Phase 5 : Divergence Detection

**Le signal le plus puissant de cet agent :**

Quand le prix du BTC évolue dans un sens et le ticker dans l'autre, c'est une **anomalie** qui se résout généralement dans le sens du BTC (si la corrélation est forte).

| Type de divergence | Détection | Probabilité de résolution | Action |
|-------------------|-----------|--------------------------|--------|
| **BTC monte, ticker stagne** | BTC +10% sur 7j, ticker +2% | 65% ticker rattrape | Opportunité d'achat si qualité OK |
| **BTC baisse, ticker résiste** | BTC −15% sur 7j, ticker −5% | 55% ticker finit par suivre | Neutre — peut être un leader positif |
| **BTC monte, ticker baisse** | BTC +10%, ticker −10% | 80% ticker problème spécifique | **Investigation urgente** — risque idiosyncratique |
| **BTC baisse, ticker s'effondre** | BTC −10%, ticker −30% | 70% surréaction | Opportunité si NAV intact |

**Score Divergence /10 :**
- > 7 : Divergence majeure — nécessite une analyse approfondie immédiate
- 5–7 : Divergence modérée — mentionner dans `_update.md`
- < 5 : Corrélation normale — pas d'action

---

## Livrables

### Fichier principal
`data/crypto_correlation_YYYY-MM-DD.json`
```json
{
  "meta": {"date": "2026-05-16", "btc_price": 98500, "eth_price": 4200},
  "iren": {
    "correlation_30d": 0.78,
    "correlation_90d": 0.72,
    "beta_btc": 1.35,
    "r2_btc": 0.61,
    "nav_estimate_usd": 2100000000,
    "market_cap": 18892033615,
    "premium_pct": -18,
    "mpi": 1.25,
    "divergence_score": 4.2,
    "verdict": "Corrélation normale — IREN suit BTC. Premium négatif = légère sous-valorisation vs NAV."
  }
}
```

### Bloc dans `_init.md` ou `_update.md`
```markdown
## ₿ Bloc Crypto-Correlation (Agent Crypto)
**Corrélation BTC (30j) :** 0.78 | **Beta BTC :** 1.35
**R² BTC :** 61% de la variance d'IREN expliquée par le Bitcoin
**NAV estimé :** $2.1B | **Market Cap :** $18.9B | **Premium :** −18% (légère sous-valorisation)
**MPI (Mining Profitability) :** 1.25 → Mining rentable
**Divergence :** Score 4.2/10 — corrélation normale, pas d'anomalie détectée
**Verdict :** IREN est un proxy BTC avec un beta > 1. La volatilité est supérieure à BTC. 
Le discount de 18% vs NAV est attrayant si on croit au BTC > $100k.
```

---

## Intégration dans le pipeline

```bash
# run_morning.sh — étape 0e
python3 agents/crypto/agent.py
```

**Ordre d'exécution du matin :**
1. `learn_from_errors.py`
2. `agent_quant.py`
3. `agent_geo.py`
4. `agent_crypto.py`
5. `fetch_prices.py`

**Règle de mise à jour :**
- Si `divergence_score` > 7 → créer automatiquement `_update.md` pour le ticker
- Si `mpi` < 0.8 → alerte rouge dans `Alertes/ALERTES.md`
- Si `premium` < −30% → opportunité dans `Opportunités/YYYY-MM-DD.md` (si qualité OK)

---

## Déclenchement manuel

**Commande :** `Analyse la corrélation crypto de [TICKER] — NAV, premium, divergence avec BTC`

Ou : `Quel est le Mining Profitability Index aujourd'hui ? IREN est-il surévalué ?`

---

## Guardrails

- **Le NAV est une approximation** — il dépend des données trimestrielles qui peuvent être obsolètes
- **Ne pas trader uniquement sur le NAV** — la valorisation d'un miner inclut des facteurs qualitatifs (management, capacity expansion, ESG)
- **Beta BTC > 1.5 = risque extrême** — si BTC baisse 20%, le ticker peut baisser 30%+
- **MPI dépend du coût énergétique** — les chiffres de blockchain.info sont globaux, pas spécifiques à IREN
- **Les divergences ne se résolvent pas toujours** — un discount persistant peut signaler un problème structurel
