# Patterns Historiques — Bibliothèque de Configurations Récurrentes

**Mis à jour le :** YYYY-MM-DD
**Nb patterns documentés :** 0

> Ce fichier accumule les configurations (technique + fondamental + sentiment) qui se sont produites dans le passé sur la watchlist, avec leur résultat.
> Quand une configuration actuelle ressemble à une configuration passée à ≥ 70%, un signal de similarité est émis.

---

## Comment ce fichier fonctionne

### Principe de détection

À chaque bulletin du matin et à chaque `_update.md`, l'agent compare la configuration actuelle d'un ticker à tous les patterns de sa bibliothèque sur les 3 dimensions :

```
CONFIGURATION D'UN TICKER = snapshot à un instant T de :
  1. Dimension Technique (5 indicateurs)
  2. Dimension Fondamentale (4 métriques)
  3. Dimension Sentiment (4 signaux)

SCORE DE SIMILARITÉ = (Sim. Technique × 40%) + (Sim. Fondamentale × 35%) + (Sim. Sentiment × 25%)
Si Score ≥ 70% → émettre un signal "Configuration similaire à [DATE] à XX%"
```

---

## Méthode de scoring des similarités

### Dimension Technique (40% du score de similarité)

| Indicateur | Actuel | Pattern | Similarité |
|-----------|--------|---------|-----------|
| RSI 14j | [X] | [X] | Identique si |Δ| ≤ 5 pts |
| Position vs MM50 | [Au-dessus / En dessous / Sur] | [idem] | Identique si même position |
| Position vs MM200 | [idem] | [idem] | Identique si même position |
| Volume relatif (vs moy. 20j) | [×X] | [×X] | Identique si |Δ| ≤ 0.3× |
| Force relative vs S&P (90j) | [Outperform/Underperform] | [idem] | Identique si même quartile |

**Calcul similarité technique** = (nb indicateurs identiques / 5) × 100%

### Dimension Fondamentale (35% du score de similarité)

| Métrique | Actuelle | Pattern | Similarité |
|----------|---------|---------|-----------|
| Révisions EPS 30j (solde net) | [+X/-X] | [+X/-X] | Identique si même direction + |Δ| ≤ 2 |
| NLP Score Confiance Management | [X/10] | [X/10] | Identique si |Δ| ≤ 1.5 pts |
| Valorisation vs médiane secteur | [Prime/Décote/Ligne] | [idem] | Identique si même position |
| FCF Yield vs historique propre | [Haut/Médian/Bas quartile] | [idem] | Identique si même quartile |

**Calcul similarité fondamentale** = (nb métriques identiques / 4) × 100%

### Dimension Sentiment (25% du score de similarité)

| Signal | Actuel | Pattern | Similarité |
|--------|--------|---------|-----------|
| Court interest | [>15%/5-15%/<5%] | [idem] | Identique si même tranche |
| IV Rank | [>70/40-70/<40] | [idem] | Identique si même tranche |
| Insiders (3 mois) | [Net acheteur/vendeur/neutre] | [idem] | Identique si même direction |
| Consensus analystes | [>70% Buy/>50% Hold/majoritaire Sell] | [idem] | Identique si même catégorie |

**Calcul similarité sentiment** = (nb signaux identiques / 4) × 100%

---

## Format d'un pattern documenté

```markdown
## Pattern #[ID] — [TICKER] — [DATE] — Score résultant : +/-X% à J+[N]

**Date de la configuration :** YYYY-MM-DD
**Cours au moment du pattern :** $XXX
**Résultat observé :** +/-X% à J+20 · +/-X% à J+60 · [Hit/Miss si signal émis]

### Snapshot de la configuration

| Dimension | Indicateur | Valeur au moment du pattern |
|-----------|-----------|---------------------------|
| **Technique** | RSI 14j | XX |
| | Position vs MM50 | Au-dessus / En dessous |
| | Position vs MM200 | Au-dessus / En dessous |
| | Volume relatif | ×X vs moy. 20j |
| | Force relative 90j vs S&P | Outperform / Underperform / Neutre |
| **Fondamental** | Révisions EPS 30j | Solde net +X/-X |
| | NLP Score Confiance | X/10 |
| | Valorisation vs pairs | Prime XX% / Décote XX% / Ligne |
| | FCF Yield position | Haut / Médian / Bas quartile |
| **Sentiment** | Short interest | XX% float |
| | IV Rank | XX% |
| | Insiders (3 mois) | Net acheteur / vendeur / neutre |
| | Consensus | XX% Buy |

### Contexte macro au moment du pattern
| Régime macro | VIX | Taux 10Y | DXY |
|-------------|-----|---------|-----|
| [Normal/Risk-off/Risk-on] | XX | X.X% | XXX |

### Déclencheur identifié
> [Qu'est-ce qui a créé cette configuration ? Earnings ? News macro ? Rotation sectorielle ?]

### Ce qui s'est passé ensuite
> [Narrative factuelle de la trajectoire du cours à J+5, J+20, J+60]

### Leçon extraite
> [Quelle règle générale peut-on tirer de ce pattern pour l'appliquer aux futures occurrences similaires ?]

### Tags
`#secteur-tech` `#RSI-survendu` `#insiders-acheteurs` `#régime-normal` `#earnings-beat`
```

---

## Bibliothèque des patterns documentés

> Section vide au démarrage. Se remplit automatiquement au fil des `_update.md` et `_init.md`.

*(Aucun pattern documenté pour le moment)*

---

## Protocole de détection quotidienne

```
CHAQUE MATIN (après Phase 2 du bulletin) :

POUR CHAQUE TICKER WATCHLIST :

1. Construire le snapshot actuel (13 indicateurs sur 3 dimensions)

2. Pour chaque pattern dans la bibliothèque du même ticker :
   → Calculer la similarité sur les 3 dimensions
   → Calculer le score de similarité global = (SimTech×40%) + (SimFond×35%) + (SimSent×25%)

3. Si score de similarité ≥ 70% :
   → Émettre le signal : "⚡ Configuration similaire au Pattern #[ID] à XX%"
   → Rappeler le résultat historique : "→ Résultat historique : +/-X% à J+20"
   → Ajuster le score final : si résultat historique positif (+>5%) → +0.3 pt Score Final
   → Insérer dans WATCHLIST_SCORES.md + dans le bulletin

4. Si score ≥ 85% (similarité très forte) :
   → Signal prioritaire dans le bulletin
   → Ajustement score : +0.5 pt Score Final si résultat historique positif
   → Déclencher automatiquement un _update.md avec la section "Pattern récurrent détecté"
```

---

## Protocole de documentation d'un nouveau pattern

```
UN NOUVEAU PATTERN EST DOCUMENTÉ QUAND :
1. Un signal est émis (opportunité scorée ≥ 6/10) ET
2. Son résultat est connu à J+20 (Hit ou Miss)

PROCÉDURE :
→ Créer un nouveau bloc "Pattern #[ID]" avec le format ci-dessus
→ Remplir le snapshot au moment du signal (récupérer depuis le _update.md source)
→ Documenter le résultat observé
→ Extraire une leçon si le pattern est répété ≥ 2 fois
→ Incrémenter le compteur "Nb patterns documentés" en en-tête
```

---

## Statistiques de la bibliothèque

| Métrique | Valeur |
|----------|--------|
| Total patterns documentés | 0 |
| Patterns avec résultat positif (J+20 > +5%) | 0 |
| Patterns avec résultat négatif (J+20 < -5%) | 0 |
| Taux de succès moyen des patterns réactivés | — |
| Pattern le plus fréquemment réactivé | — |
| Meilleur prédicteur individuel identifié | — |

---

## Patterns cross-tickers — Configurations sectorielles

> Certains patterns ne sont pas spécifiques à un titre mais s'observent sur tout un secteur au même moment.

| Date | Secteur | Configuration commune | Résultat J+30 | Nb tickers watchlist concernés |
|------|---------|----------------------|--------------|-------------------------------|
| — | — | — | — | — |

> **Exemple attendu :** *"En janvier 2026, tous les semi-conducteurs de la watchlist avaient RSI < 35 + révisions négatives. Résultat J+30 : +18% en moyenne."*
> Ce type de pattern sectoriel est un signal particulièrement fort car il confirme que c'est le secteur qui est sous-évalué, pas juste un titre.
