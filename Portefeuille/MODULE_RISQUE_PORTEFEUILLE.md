# Module Risque Portefeuille

Ce module évalue le risque global du portefeuille : corrélation entre positions, concentration, stress tests, et VaR simplifiée. À lire lors du workflow du matin et à mettre à jour après chaque ajout ou clôture de position.

**Commande :** `Analyse le risque de mon portefeuille actuel`

---

## 1. Matrice de corrélation

> Calculer la corrélation historique (30j de cours quotidiens) entre chaque paire de positions ouvertes.

| Niveau corrélation | Valeur | Implication |
|-------------------|--------|-------------|
| Forte positive | > 0.7 | Les 2 positions bougent ensemble — peu de diversification |
| Modérée | 0.3 – 0.7 | Diversification partielle |
| Faible / nulle | -0.3 – 0.3 | Bonne diversification |
| Négative | < -0.3 | Couverture naturelle |

**Règle :** Si 2 positions ont une corrélation > 0.7 ET représentent ensemble > 25% du capital → **alerte de concentration**.

**Matrice à mettre à jour :** Voir `Portefeuille/POSITIONS.md` — section Corrélations.

---

## 2. Concentration sectorielle et factorielle

### Par secteur
| Secteur | Positions | Exposition ($) | % Capital | Seuil alerte |
|---------|-----------|---------------|-----------|-------------|
| — | — | — | — | > 35% |

### Par facteur d'exposition macro
| Facteur | Tickers exposés | Exposition nette | Risque |
|---------|----------------|-----------------|--------|
| Dollar fort (USD) | — | — | — |
| Taux 10Y hausse | — | — | — |
| Pétrole hausse | — | — | — |
| Chine ralentissement | — | — | — |
| Récession US | — | — | — |
| IA / tech croissance | — | — | — |

**Règle :** Si un facteur macro unique impacte > 40% du capital dans le même sens → **réduction recommandée ou couverture**.

---

## 3. Stress Tests

> Estimer l'impact d'un scénario adverse sur la valeur totale du portefeuille.

### Scénarios standards (à recalculer à chaque changement de composition)

| Scénario | Description | Impact estimé portefeuille |
|---------|-------------|--------------------------|
| **Marché −10%** | Correction générale des indices | Calculer : Σ(bêta × taille position × −10%) |
| **Marché −20%** | Bear market modéré | Calculer : Σ(bêta × taille position × −20%) |
| **Taux 10Y +1%** | Resserrement monétaire inattendu | Calculer via carte d'exposition sectorielle |
| **DXY +5%** | Fort rebond du dollar | Calculer via exposition géographique des revenus |
| **Pétrole +30%** | Choc pétrolier | Calculer via exposition énergie / consommation |
| **Chine −15%** | Choc sur la demande chinoise | Calculer via revenus Chine de chaque ticker |
| **Récession US** | PIB −2%, chômage +3% | Calculer via sensibilité cyclique de chaque ticker |

**Méthode de calcul :**
```
Impact scénario = Σ pour chaque position :
  (Taille position en $) × (bêta ou exposition estimée) × (choc en %)

Exemple : AAPL ($10 000, bêta 1.2, 35% revenus Chine)
  Scénario Chine −15% : $10 000 × 0.35 × (−15%) = −$525
```

**Seuil d'alerte :** Si un scénario génère une perte estimée > 15% du capital total → **réduction de l'exposition ou ajout d'une couverture**.

---

## 4. VaR Historique Simplifiée (Value at Risk)

> Estimation de la perte maximale sur 1 jour avec 95% de confiance, basée sur les performances historiques.

**Méthode :**
```
1. Récupérer les 60 derniers jours de performance quotidienne de chaque position
2. Calculer la variation quotidienne du portefeuille total (somme pondérée)
3. Trier les performances du pire au meilleur
4. VaR 95% = 5e percentile des performances (la 3e pire journée sur 60j)
5. VaR 99% = 1er percentile (la pire journée)
```

| Métrique | Valeur calculée | Seuil d'alerte |
|----------|----------------|----------------|
| VaR 95% (1 jour) | $XXX — X% du capital | > 3% du capital |
| VaR 99% (1 jour) | $XXX — X% du capital | > 5% du capital |
| Volatilité annualisée portefeuille | X% | > 25% |

---

## 5. Score de diversification global

> Score synthétique calculé automatiquement.

| Critère | Points |
|---------|--------|
| Nombre de positions ≥ 5 | +2 pts |
| Aucun secteur > 35% | +2 pts |
| Aucune position individuelle > 20% | +2 pts |
| Corrélation moyenne < 0.5 | +2 pts |
| Au moins 1 position décorrélée (Or, Utilities, Healthcare) | +2 pts |

**Score /10 :**
- 9–10 : Portefeuille bien diversifié ✅
- 7–8 : Diversification acceptable ⚠️
- 5–6 : Concentration à corriger 🟡
- < 5 : Risque de concentration élevé 🔴

---

## 6. Règles de gestion du risque global

```
STOP-LOSS GLOBAL :
→ Si le portefeuille perd > 10% de sa valeur initiale sur un mois
→ Réduire toutes les positions de 50% et réévaluer avant de réinvestir

DRAWDOWN MAXIMUM :
→ Si drawdown depuis le plus haut atteint −15% : réduire l'exposition globale à 50%
→ Si drawdown atteint −25% : passer en cash majoritaire, attendre signal de retournement

LEVIER :
→ Aucun levier > 1.5× la valeur du portefeuille
→ Positions shorts : maximum 20% du capital total

COUVERTURE AUTOMATIQUE :
→ Si VIX > 30 ET exposition marchés > 80% du capital → envisager achat de puts S&P ou VIX
```

---

## Template rapport de risque quotidien

> À générer lors du workflow du matin si des positions sont ouvertes.

```markdown
## Rapport Risque Portefeuille — YYYY-MM-DD

**Valeur totale :** $XXX,XXX | **P&L du jour :** +/−$XXX (+/−X%) | **Drawdown depuis ATH :** −X%

### Concentration
| Secteur le plus concentré | XX% | [OK / ⚠️ Surveiller / 🔴 Réduire] |
| Position la plus grande | [TICKER] XX% | [OK / ⚠️ Surveiller / 🔴 Réduire] |
| Score diversification | X/10 | [OK / ⚠️ / 🔴] |

### Stress test du jour
| Scénario | Impact estimé |
| Marché −10% | −$XXX (−X%) |
| Taux +1% | −$XXX (−X%) |

### Alertes actives
- [Alerte si applicable]

### Action recommandée
- [None / Réduire [TICKER] / Couvrir avec... / Rééquilibrer...]
```
