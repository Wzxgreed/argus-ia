# Module Sizing — Dimensionnement des positions

Ce module calcule la taille optimale d'une position en fonction de la conviction (score), du risque (ATR), de la qualité (Filtre Qualité) et de la composition du portefeuille (diversification).

**Usage :** À consulter avant d'ouvrir ou de renforcer une position. Le sizing recommandé est indiqué dans chaque rapport Opportunités et dans chaque `_update.md`.

---

## Principes fondamentaux

### Règle d'or — Risque par trade
> **Ne jamais risquer plus de 1% à 2% du capital total sur un seul trade.**

- Capital total : à définir dans `Portefeuille/POSITIONS.md`
- Risque par trade standard : **1% du capital**
- Risque par trade conviction forte (score ≥ 8 + Quality Compounder) : **1.5%**
- Risque par trade spéculatif (score 6–7 + Hors périmètre qualité) : **0.5%**

---

## Méthode 1 — ATR-Based Sizing (recommandée)

```
Position size = (Capital × % risque) / (ATR × multiplicateur stop)

Paramètres standards :
- Multiplicateur stop = 2 (stop à 2×ATR du cours d'entrée)
- % risque = 1% (standard) / 1.5% (forte conviction) / 0.5% (spéculatif)

Exemple :
- Capital : $100 000
- % risque : 1% → Montant risqué : $1 000
- Cours d'entrée : $50 | ATR 14j : $2.50 | Stop = $50 − (2 × $2.50) = $45
- Distance au stop : $5 par action
- Nombre d'actions : $1 000 / $5 = 200 actions
- Valeur de la position : 200 × $50 = $10 000 (10% du capital)
```

**Tableau de sizing rapide (base : 1% risque, stop 2×ATR) :**
| ATR / Cours | Position en % du capital |
|------------|------------------------|
| ATR = 1% du cours | 50% — position très large, surveiller |
| ATR = 2% du cours | 25% — position significative |
| ATR = 3% du cours | 16.7% — taille standard |
| ATR = 5% du cours | 10% — titre volatile |
| ATR = 8% du cours | 6.25% — titre très volatile, petite position |

---

## Méthode 2 — Kelly Partiel (pour les positions long terme)

```
Kelly fraction = (Win rate × Gain moyen / Perte moyenne − (1 − Win rate)) / (Gain moyen / Perte moyenne)
Kelly utilisé = Kelly fraction × 25% (Kelly partiel — sécurité)

Usage : Seulement si l'historique du backtesting (BACKTESTING.md) donne ≥ 20 signaux sur ce type de catalyseur.
```

---

## Ajustements selon le score et la qualité

| Score signal | Filtre Qualité | Multiplicateur sizing |
|-------------|---------------|----------------------|
| ≥ 8/10 | ✅ Quality Compounder (5-6/6) | ×1.5 (renforcer jusqu'à 1.5% risque) |
| 7–8/10 | ✅ Quality Compounder | ×1.0 (taille standard 1%) |
| 6–7/10 | ⚠️ Quality Partielle | ×0.75 (réduire à 0.75%) |
| 6–7/10 | 🔴 Hors périmètre | ×0.5 (spéculatif, max 0.5%) |
| < 6/10 | Tous | ×0 (ne pas ouvrir de position) |

---

## Limites de concentration

### Par position
| Type position | Taille max en % du capital |
|--------------|--------------------------|
| Quality Compounder (conviction forte) | 20% |
| Quality Partielle | 12% |
| Trade spéculatif (Hors périmètre) | 5% |
| Toute position individuelle (hard cap) | 25% |

### Par secteur
| Secteur | Exposition maximale recommandée |
|---------|-------------------------------|
| Un seul secteur | 35% du capital |
| Tech (bêta élevé) | 40% du capital |
| Défensifs (Healthcare, Utilities) | Pas de limite |
| Positions shorts | 20% du capital total |

### Par facteur
| Facteur | Exposition maximale |
|---------|-------------------|
| Corrélation élevée (>0.7) entre 2 positions | Les 2 comptent pour 1.5× leur taille individuelle |
| Exposition à un même pays émergent | 15% du capital |
| Exposition à une même thèse macro | 30% du capital |

---

## Règles de renforcement

```
Renforcement autorisé si :
✅ Position déjà profitable (cours > prix d'entrée)
✅ La thèse s'est renforcée (pas affaiblie)
✅ Score ≥ 7/10 après réévaluation
✅ Le renforcement ne fait pas dépasser le hard cap (25%)

Méthode pyramide (renforcement progressif) :
- Achat initial : 50% de la taille cible
- Premier renforcement (cours +5%) : 30% de la taille cible
- Deuxième renforcement (cours +10%) : 20% de la taille cible
```

---

## Format de sizing dans les rapports

> Insérer ce bloc dans chaque opportunité signalée (rapport Opportunités et `_update.md`).

```markdown
### Sizing recommandé
| Paramètre | Valeur |
|-----------|--------|
| Score signal | X/10 |
| Filtre Qualité | ✅/⚠️/🔴 (X/6) |
| Cours d'entrée suggéré | $XXX |
| ATR 14j | $X.XX |
| Stop-loss (2×ATR) | $XXX (−X%) |
| Stop serré (1.5×ATR) | $XXX (−X%) |
| % risque recommandé | X% du capital |
| Taille position (base $100k) | $X,XXX — XX actions |
| Taille max recommandée | XX% du capital |
| Type position | Long terme / Swing / Spéculatif |
```

---

## Règle de sortie partielle

```
Gestion en cours de position :
- À +10% : sortir 25% de la position (sécuriser une partie du gain)
- À +20% : remonter le stop-loss au prix d'entrée (position gratuite)
- À +30% : sortir 25% supplémentaires
- Garder le solde jusqu'à invalidation de la thèse ou prix cible atteint
```
