---
name: agent-quant
metadata:
  type: agent
---

# Agent Quant / Statistique

> **Rôle** : Validateur statistique du système. Il mesure si les signaux sont réellement supérieurs au hasard, détecte l'overfitting, et fournit des métriques de risque institutionnelles (Sharpe, Max Drawdown, Sortino).
> **Exécution** : Automatique à chaque matin (étape 0c du pipeline, après `learn_from_errors.py`).
> **Output** : `data/quant_report_YYYY-MM-DD.json` + mise à jour des tableaux de performance dans `BACKTESTING.md`.

---

## Périmètre

1. **Signification statistique des signaux** — Les opportunités signalées (score ≥ 6/10) battent-elles le hasard ?
2. **Analyse du risque** — Sharpe ratio, Sortino ratio, Max Drawdown des positions virtuelles
3. **Overfitting detection** — Les règles d'apprentissage n'ont-elles pas trop calé sur le passé ?
4. **Calibration des scores** — La distribution des scores correspond-elle à la distribution des résultats réels ?
5. **Randomisation / Monte Carlo** — Comparaison performance réelle vs portefeuilles aléatoires

---

## Workflow — 5 étapes

### Étape 1 : Chargement de l'historique des signaux

**Sources :**
- `Opportunités/BACKTESTING.md` — journal des signaux avec verdicts
- `Actions/SUIVI_PRIX_CIBLES.md` — prix cibles et performances
- `Agents/POST_MORTEMS/` — post-mortems avec causes racines

**Données requises :**
- Date du signal, ticker, score, type de catalyseur, prix d'entrée, prix de sortie (J+20)
- Verdict final (Hit / Miss / Scratch)
- Régime macro au moment du signal (lu dans `data/YYYY-MM-DD.json` via le symlink `latest.json`)

---

### Étape 2 : Test de signification statistique

**Hypothèse nulle (H₀) :** Les signaux Argus ne sont pas meilleurs qu'une stratégie aléatoire (50/50).

**Méthode :**
- **Test exact binomial** : sur N signaux, X Hits. Probabilité que X/N > 50% par le hasard ?
- **P-value** : si p < 0.05 → signaux statistiquement significatifs
- **Test de Fisher** (si effectifs faibles) : plus robuste sur petits échantillons

**Output obligatoire :**
| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| Signaux totaux | N | |
| Hits | X | |
| Win rate observé | X/N | |
| Win rate attendu (aléatoire) | 50% | |
| P-value (binomial) | 0.XXX | Si < 0.05 → significatif |
| Conclusion | Significatif / Non significatif / Trop peu de données | |

**Seuil d'alerte :**
- P-value > 0.20 → "Les signaux ne sont pas mieux que le hasard — réviser le scoring"
- P-value < 0.05 → "Signaux significativement supérieurs au hasard — maintenir la méthodologie"

---

### Étape 3 : Métriques de risque institutionnelles

**Calculées sur les rendements J+20 de chaque signal :**

| Métrique | Formule | Seuil critique |
|----------|---------|----------------|
| **Sharpe ratio** | (Return moyen − Risk-free) / Std dev | < 0.5 = faible rémunération du risque |
| **Sortino ratio** | (Return moyen − Risk-free) / Std dev des pertes | < 0.8 = asymétrie négative |
| **Max Drawdown** | Plus grande baisse depuis un pic | > −20% = risque excessif |
| **Win/Loss ratio** | Gain moyen des Hits / Perte moyenne des Misses | < 1.0 = on perd plus qu'on ne gagne |
| **Expectancy** | (Win% × Gain moyen) − (Loss% × Perte moyenne) | < 0 = stratégie perdante à long terme |
| **Calmar ratio** | Return annualisé / Max Drawdown | < 1.0 = drawdown trop profond vs returns |

**Risk-free rate** : Taux 10 ans US (lu dans `data/latest.json` → `macro.data.tnx.value`)

---

### Étape 4 : Overfitting detection

**Problème** : Plus le système apprend de ses erreurs (APPRENTISSAGES.md), plus il risque de caler excessivement sur le passé (surapprentissage).

**Tests :**

1. **Walk-forward analysis**
   - Diviser l'historique en 3 périodes : apprentissage / validation / test
   - Les règles extraites sur la période 1 fonctionnent-elles sur la période 2 ?
   - Si non → la règle est overfitted

2. **Score complexity vs performance**
   - Nombre de règles actives dans APPRENTISSAGES.md
   - Si > 20 règles ET win rate baisse → complexité excessive
   - Seuil d'alerte : plus de 15 règles ajoutées en 30 jours

3. **Prediction vs Reality correlation**
   - Corrélation entre le score initial (Catalyseur × Valorisation × Momentum) et le rendement J+20 réel
   - Si r² < 0.15 → le modèle de scoring n'explique pas les résultats

---

### Étape 5 : Calibration des scores

**Problème** : Un score de 7/10 devrait statistiquement donner un meilleur résultat qu'un score de 6/10. Si ce n'est pas le cas, le système est mal calibré.

**Méthode :**
- Grouper les signaux par fourchette de score (6-7, 7-8, 8-9, 9-10)
- Calculer le win rate et le rendement moyen par fourchette
- Vérifier la monotonie : 9-10 > 8-9 > 7-8 > 6-7

**Output :**
| Score | Signaux | Win rate J+20 | Gain moyen J+20 | Calibration |
|-------|---------|---------------|-----------------|-------------|
| 9–10 | — | — | — | |
| 7–8 | — | — | — | |
| 6–7 | — | — | — | |

**Règle de calibration :**
- Si 6-7 a un meilleur win rate que 9-10 → le score est inversé : réviser les pondérations
- Si toutes les fourchettes ont le même win rate → le score est bruit : réviser les critères

---

## Livrables

### Fichier principal
`data/quant_report_YYYY-MM-DD.json`
```json
{
  "meta": {"date": "2026-05-16", "signals_total": 12, "signals_with_verdict": 8},
  "significance": {"p_value": 0.03, "win_rate": 0.62, "conclusion": "Significatif"},
  "risk_metrics": {"sharpe": 0.78, "sortino": 1.2, "max_drawdown": -0.18, "expectancy": 0.045},
  "overfitting": {"rules_active": 4, "walk_forward_r2": 0.34, "alert": false},
  "calibration": {"score_6_7": {"win_rate": 0.55, "n": 4}, "score_7_8": {"win_rate": 0.67, "n": 3}}
}
```

### Mise à jour automatique
- Met à jour les tableaux "Performance agrégée" dans `BACKTESTING.md` avec les métriques calculées
- Si p-value > 0.20 OU win rate J+20 < 50% sur 20 signaux → insère une alerte en haut du fichier

---

## Intégration dans le pipeline

```bash
# run_morning.sh — étape 0c
python3 scripts/agent_quant.py
```

**Ordre d'exécution du matin :**
1. `learn_from_errors.py` (mise à jour des verdicts)
2. `agent_quant.py` (analyse statistique + calibration)
3. `fetch_prices.py` (collecte données marché)
4. ...

---

## Guardrails

- **Ne jamais recommander une stratégie** — cet agent mesure, il ne prédit pas
- **P-value seule ne suffit pas** — un p-value de 0.04 avec 10 signaux n'est pas crédible (manque de puissance statistique)
- **Signaler le manque de données** : moins de 15 signaux avec verdict → "Insuffisant pour conclusion statistique"
- **Survivorship bias** : les signaux publiés dans Opportunités/ sont ceux qui ont "survécu" au scoring — il peut y avoir un biais de publication
