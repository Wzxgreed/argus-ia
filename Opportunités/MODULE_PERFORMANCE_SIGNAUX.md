# Module Performance des Signaux

**Mis à jour le :** YYYY-MM-DD
**Périmètre :** Tous les signaux publiés dans `Opportunités/BACKTESTING.md` avec verdict J+20 connu

> Ce fichier répond à une question centrale : **quels types de signaux prédisent le mieux la performance réelle ?**
> Il permet d'affiner dynamiquement la pondération du Score Catalyseur selon les signaux qui ont prouvé leur efficacité sur la watchlist.

---

## Classement des signaux par win rate (J+20)

> Un signal "gagnant" = cours +5% ou plus à J+20 après le signal.
> Mis à jour à chaque clôture de fenêtre J+20 dans BACKTESTING.md.

| Rang | Type de signal | Nb signaux | Gagnants J+20 | Win rate | Gain moyen gagnants | Perte moy. perdants | Score confiance |
|------|---------------|-----------|--------------|----------|--------------------|--------------------|----------------|
| 1 | | 0 | — | — | — | — | Faible |
| 2 | | 0 | — | — | — | — | Faible |
| 3 | | 0 | — | — | — | — | Faible |

> **Score confiance :** Faible (<10 signaux) · Moyen (10-25) · Fort (>25)

---

## Performance par type de signal — Détail

### Signaux Sentiment

| Signal | Nb obs. | Win rate J+20 | Gain moy. | Perte moy. | Meilleur contexte | Pire contexte |
|--------|---------|--------------|-----------|------------|------------------|--------------|
| **Upgrade analyste >65% track record** | 0 | — | — | — | — | — |
| **Upgrade analyste <45% track record** | 0 | — | — | — | — | — |
| **Cluster buying insiders (≥3 pers.)** | 0 | — | — | — | — | — |
| **Achat CEO/CFO isolé (>$500k)** | 0 | — | — | — | — | — |
| **Short squeeze setup (4 conditions)** | 0 | — | — | — | — | — |
| **Unusual options activity (vol >3×OI)** | 0 | — | — | — | — | — |
| **EPS Revision Momentum fort (+>5 sur 30j)** | 0 | — | — | — | — | — |
| **Transactions politiques (achat sénat)** | 0 | — | — | — | — | — |
| **Contrat gouvernemental majeur (>5% CA)** | 0 | — | — | — | — | — |

### Signaux Fondamentaux

| Signal | Nb obs. | Win rate J+20 | Gain moy. | Perte moy. | Meilleur contexte | Pire contexte |
|--------|---------|--------------|-----------|------------|------------------|--------------|
| **NLP Confiance Management ≥8/10 en hausse** | 0 | — | — | — | — | — |
| **Earnings beat + guidance relevée** | 0 | — | — | — | — | — |
| **Décote vs pairs >20% sur EV/FCF NTM** | 0 | — | — | — | — | — |
| **FCF yield >5% + ROIC >15%** | 0 | — | — | — | — | — |
| **Reverse DCF : croissance implicite < réaliste** | 0 | — | — | — | — | — |

### Signaux Techniques

| Signal | Nb obs. | Win rate J+20 | Gain moy. | Perte moy. | Meilleur contexte | Pire contexte |
|--------|---------|--------------|-----------|------------|------------------|--------------|
| **Golden cross (MM50 > MM200)** | 0 | — | — | — | — | — |
| **RSI <30 sur Quality Compounder** | 0 | — | — | — | — | — |
| **Breakout MM200 + volume >1.5×** | 0 | — | — | — | — | — |
| **Force relative double leader (vs S&P + secteur)** | 0 | — | — | — | — | — |
| **Saisonnalité favorable + momentum positif** | 0 | — | — | — | — | — |

### Signaux Supply Chain

| Signal | Nb obs. | Win rate J+20 | Gain moy. | Perte moy. | Meilleur contexte | Pire contexte |
|--------|---------|--------------|-----------|------------|------------------|--------------|
| **Nouveau client majeur annoncé (>10% CA)** | 0 | — | — | — | — | — |
| **Client critique : guidance en forte hausse** | 0 | — | — | — | — | — |
| **Fournisseur critique : pénurie annoncée** | 0 | — | — | — | — | — |
| **Reshoring / diversification supply** | 0 | — | — | — | — | — |

### Signaux Macro

| Signal | Nb obs. | Win rate J+20 | Gain moy. | Perte moy. | Meilleur contexte | Pire contexte |
|--------|---------|--------------|-----------|------------|------------------|--------------|
| **Pivot banque centrale confirmé** | 0 | — | — | — | — | — |
| **VIX capitulation (>35 puis rebond)** | 0 | — | — | — | — | — |
| **Régime Risk-on déclaré** | 0 | — | — | — | — | — |
| **Flux 13F : entrée nouvel actionnaire institutionnel** | 0 | — | — | — | — | — |

### Signaux Patterns Récurrents

| Pattern | Nb fois réactivé | Win rate réactivation | Gain moy. | Contexte de défaillance |
|---------|-----------------|----------------------|-----------|------------------------|
| — | 0 | — | — | — |

---

## Performance par combinaison de signaux

> Les combinaisons multi-signaux sont en général plus fiables que les signaux isolés.

| Combinaison | Nb obs. | Win rate J+20 | Gain moy. | Note |
|------------|---------|--------------|-----------|------|
| Insiders acheteurs + EPS Rev. Momentum fort | 0 | — | — | Signal doublement confirmatoire |
| NLP confiant + Révisions hausse + Décote pairs | 0 | — | — | Triple confirmation |
| RSI <35 + Quality Compounder + Saisonnalité favorable | 0 | — | — | Contrarian de qualité |
| Short squeeze setup + Catalyseur fondamental | 0 | — | — | Squeeze avec thèse |
| Upgrade >65% track record + Unusual options | 0 | — | — | Convergence sell-side + smart money |

---

## Performance par régime macro

| Régime | Nb signaux émis | Win rate J+20 | Gain moy. | Note |
|--------|----------------|--------------|-----------|------|
| Normal | 0 | — | — | — |
| Risk-on / Bull | 0 | — | — | — |
| Risk-off | 0 | — | — | — |
| Pré-FOMC | 0 | — | — | — |
| Stagflation | 0 | — | — | — |

---

## Performance par secteur

| Secteur | Nb signaux | Win rate J+20 | Gain moy. | Signal le plus performant dans ce secteur |
|---------|-----------|--------------|-----------|------------------------------------------|
| Tech / IA | 0 | — | — | — |
| Semi-conducteurs | 0 | — | — | — |
| Défense | 0 | — | — | — |
| Santé / Biotech | 0 | — | — | — |
| Énergie | 0 | — | — | — |
| Finance | 0 | — | — | — |
| Consommation | 0 | — | — | — |

---

## Règles de pondération extraites (si confiance ≥ Moyen)

> Ces règles s'appliquent automatiquement au calcul du Score Catalyseur.
> Alimentent la section "Règles actives" de `Agents/APPRENTISSAGES.md`.

| Règle extraite | Signal concerné | Win rate observé | Ajustement appliqué | Depuis | Confiance |
|---------------|----------------|-----------------|--------------------|----|-----------|
| — | — | — | — | — | — |

---

## Protocole de mise à jour

```
CHAQUE FOIS QU'UNE FENÊTRE J+20 EST CLÔTURÉE (dans BACKTESTING.md) :

1. Identifier le type de signal principal qui avait motivé le signal
2. Incrémenter le compteur "Nb signaux" de la ligne correspondante
3. Si Hit → incrémenter "Gagnants J+20", recalculer win rate et gain moyen
4. Si Miss → recalculer win rate et perte moyenne

CHAQUE TRIMESTRE (avec la calibration) :
1. Recalculer tous les win rates sur la période complète
2. Identifier les top 3 signaux les plus fiables → renforcer leur pondération dans APPRENTISSAGES.md
3. Identifier les signaux avec win rate < 45% sur ≥ 10 obs → pénaliser dans APPRENTISSAGES.md
4. Mettre à jour le classement général
5. Remplir la table "Performance par combinaison"
```

---

## Alertes de calibration automatique

> Si un signal atteint ≥ 10 observations et affiche un win rate extrême → alerte automatique.

| Condition | Action |
|-----------|--------|
| Signal win rate > 75% sur ≥ 10 obs | → +0.5pt bonus dans Score Catalyseur pour ce signal |
| Signal win rate < 40% sur ≥ 10 obs | → −0.5pt malus dans Score Catalyseur pour ce signal |
| Signal win rate < 35% sur ≥ 15 obs | → −1pt malus + ajouter règle dans APPRENTISSAGES.md |
| Combinaison win rate > 80% sur ≥ 5 obs | → Signal "golden combo" → +1pt bonus automatique |
