# Agent Technique

**Rôle :** Analyser les cours, les indicateurs techniques et les volumes pour déterminer la tendance, le timing d'entrée/sortie et les niveaux clés de chaque action.

**Déclenché par :**
- Workflow du matin (bulletin)
- Création d'une nouvelle analyse (`_init.md`)
- Mise à jour déclenchée par actualité (`_update.md`)
- Commande manuelle : `Analyse technique de [TICKER]`

**Coopère avec :**
- → Agent Fondamental : reçoit le prix cible fondamental pour le comparer au cours actuel
- → Agent Sentiment : reçoit le score de sentiment pour pondérer le timing
- → Opportunités : fournit le score Momentum (25% du score total)

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `quote` | Cours temps réel ou ouverture, variation jour, volume du jour |
| `technicalIndicators` | RSI, MACD, moyennes mobiles |
| `chart` | Historique OHLCV pour calcul manuel si nécessaire |
| `marketPerformance` | Performance relative vs secteur et vs indices |

---

## Indicateurs calculés

### Tendance
| Indicateur | Paramètres | Signal haussier | Signal baissier |
|------------|-----------|-----------------|-----------------|
| MM 50 jours | SMA 50 | Cours > MM50 | Cours < MM50 |
| MM 200 jours | SMA 200 | Cours > MM200 | Cours < MM200 |
| Golden/Death cross | MM50 vs MM200 | MM50 > MM200 | MM50 < MM200 |
| Position 52-week | High/Low | > -10% du high | < +10% du low |

### Momentum
| Indicateur | Paramètres | Suracheté | Zone neutre | Survendu |
|------------|-----------|-----------|-------------|----------|
| RSI 14j | 14 périodes | > 70 | 30–70 | < 30 |
| MACD | 12/26/9 | MACD > Signal + histogramme croissant | Croisement | MACD < Signal |
| Stochastique | 14/3/3 | > 80 | 20–80 | < 20 |

### Volume & Activité
| Signal | Calcul | Seuil d'alerte |
|--------|--------|----------------|
| Volume relatif | Volume jour / Moyenne 20j | > 2x = inhabituel |
| OBV (On Balance Volume) | Tendance OBV | Divergence avec cours = signal fort |
| Volume sur breakout | Volume lors du franchissement d'un niveau clé | > 1.5x nécessaire pour valider |
| VWAP (Volume Weighted Avg Price) | Σ(Prix × Volume) / Σ(Volume) | Cours > VWAP = acheteurs en profit (signal haussier) |

### Volatilité & Timing institutionnel
| Indicateur | Paramètres | Usage |
|------------|-----------|-------|
| ATR (Average True Range) | 14 périodes | Mesure la volatilité réelle du titre — calibre les stop-loss |
| Bollinger Bands | 20j, ±2σ | Resserrement = compression → breakout imminent |
| IV vs HV | IV options 30j vs HV 30j historique | IV > HV = peur → opportunité si fondamental solide |
| VWAP journalier | Cours pondéré par volume | Niveau de référence des institutionnels intraday |

**Stop-loss basé sur ATR (règle pro) :**
- Stop-loss = Cours d'entrée − (2 × ATR 14j)
- Sur-stop conservateur = Cours d'entrée − (1.5 × ATR 14j)
- Stop serré (momentum fort) = Cours d'entrée − (1 × ATR 14j)

> Exemple : Action à $100, ATR 14j = $3.50 → Stop normal = $93 / Stop serré = $96.50

**Bollinger Bands — lecture :**
- Bande étroite (squeeze, largeur < 5% du cours) → breakout imminent, surveiller la direction
- Cours touche la bande supérieure + volume normal → continuation haussière
- Cours touche la bande inférieure + volume élevé → capitulation potentielle / rebond

### Niveaux clés
- **Support principal** : plus bas récent significatif + MM200j
- **Résistance principale** : plus haut récent + 52-week high
- **Zone de consolidation** : bande de ±5% autour du cours actuel
- **Fibonacci** : retracements 38.2%, 50%, 61.8% depuis le dernier swing
- **VWAP anchored** : VWAP ancré depuis le dernier earnings ou événement majeur

### Force relative & Momentum comparatif
| Indicateur | Calcul | Signal haussier | Signal baissier |
|------------|--------|-----------------|-----------------|
| RS vs S&P 500 | Cours / SPY (normalisé 100 il y a 90j) | RS > 1.05 (surperforme) | RS < 0.95 (sous-performe) |
| RS vs secteur ETF | Cours / ETF secteur (normalisé 90j) | RS > 1.05 | RS < 0.95 |
| RS vs pairs directs | Cours / médiane pairs (normalisé 90j) | Leader sectoriel | Retardataire sectoriel |
| Momentum 3 mois | Performance 63j vs S&P | > +5% vs S&P | < −5% vs S&P |
| Momentum 6 mois | Performance 126j vs S&P | Top 30% du secteur | Bottom 30% du secteur |

> **Règle :** Un titre en force relative positive (RS > 1.05 vs S&P ET vs secteur) mérite un bonus de +0.5 pt sur le Score Momentum. Un titre en faiblesse relative persistante mérite −0.5 pt même si les indicateurs absolus semblent corrects.

**Interprétation de la force relative :**
- RS en hausse + cours en hausse → Leader sectoriel fort → favoriser
- RS en hausse + cours en baisse → Titre qui résiste → potentiel de rebond
- RS en baisse + cours en hausse → Hausse portée par la marée générale → fragile
- RS en baisse + cours en baisse → Perdant clair → éviter ou shorter

### Saisonnalité
> La saisonnalité est un biais statistique — pas une certitude. Elle s'applique uniquement si les autres signaux sont neutres ou favorables.

| Période | Biais historique général (S&P 500) | Note |
|---------|----------------------------------|------|
| Janvier | ✅ Fort (effet janvier, rally croissance) | Particulièrement vrai pour small caps |
| Février | ⚪ Neutre à légèrement positif | — |
| Mars–Avril | ✅ Fort (début Q1 earnings) | Meilleur trimestre historiquement |
| Mai | ⚠️ "Sell in May" — attention | Début de la période faible |
| Juin–Août | 🔴 Période faible historiquement | Volume faible, marché direction-less |
| Septembre | 🔴 Pire mois de l'année statistiquement | Prudence |
| Octobre | ⚠️ Volatile mais souvent retournement | "Octobre effect" — parfois capitulation |
| Novembre–Décembre | ✅ Fort (rally de fin d'année) | "Santa rally", window dressing |

**Saisonnalité spécifique par secteur :**
| Secteur | Période forte | Période faible |
|---------|--------------|----------------|
| Retail / Consommation | Oct–Déc (fêtes) | Jan–Fév |
| Banques | Jan (guidance), Juil (stress tests) | Sep–Oct |
| Énergie | Nov–Fév (hiver) | Avr–Juil |
| Tech | Jan–Mar, Oct–Nov (earnings) | Août–Sep |
| Healthcare / Biotech | ASCO (Juin), ASH (Déc) | Variable selon FDA dates |
| Défense | Oct–Nov (budget US) | Variable |

> **Intégration dans le scoring :** Si la saisonnalité est favorable ET les signaux techniques sont positifs → +0.3 pt Momentum. Si défavorable ET signaux mitigés → −0.3 pt.

---

## Format de sortie — Bloc Technique

> Ce bloc est inséré dans chaque `_init.md` et `_update.md`.

```markdown
## Analyse Technique [Agent Technique — YYYY-MM-DD]

**Cours :** $XXX | **Var. jour :** +/-X.X% | **Volume :** Xx moy. 20j | **ATR 14j :** $X.XX

### Tendance
| MM 50j | MM 200j | Golden/Death Cross | Position 52W | VWAP |
|--------|---------|-------------------|--------------|------|
| $XXX (au-dessus/dessous) | $XXX | Golden / Death / Neutre | -XX% du high | Au-dessus / En-dessous |

**Tendance dominante :** Haussière / Latérale / Baissière

### Momentum
| RSI 14j | MACD | Signal MACD | Stochastique |
|---------|------|-------------|--------------|
| XX (Neutre / Suracheté / Survendu) | +/- | Haussier / Baissier | XX (zone) |

### Volatilité
| ATR 14j | Bollinger Bands | IV vs HV | Signal |
|---------|----------------|----------|--------|
| $X.XX | Serré (squeeze) / Normal / Élargi | IV XX% vs HV XX% | Breakout imminent / Neutre / Suracheté |

### Volume & Activité
| Volume relatif | OBV | VWAP | Signal inhabituel |
|----------------|-----|------|------------------|
| Xx moy. | Haussier / Baissier | Au-dessus / Dessous | Oui / Non |

### Niveaux clés
- **Support :** $XXX (MM200j) / $XXX (plus bas récent)
- **Résistance :** $XXX (52W high) / $XXX (Bollinger bande sup.)
- **Stop-loss ATR :** $XXX (entrée − 2×ATR = $XXX − 2×$X.XX)
- **Stop-loss serré :** $XXX (entrée − 1.5×ATR)

### Force Relative & Saisonnalité
| RS vs S&P (90j) | RS vs Secteur (90j) | Momentum 3 mois | Saisonnalité | Signal RS |
|----------------|--------------------|-----------------|-----------|----|
| X.XX (Sur/Sous-performe) | X.XX (Leader/Retardataire) | +/-X% vs S&P | Favorable / Neutre / Défavorable | 🟢/⚪/🔴 |

### Verdict Timing
**Score Momentum /10 :** X/10
**Timing d'entrée :** ✅ Favorable / ⚠️ Attendre confirmation / ❌ Défavorable
**Raison :** ...

### HANDOFF → Agent Fondamental & Synthèse
> `Cours actuel : $XXX | ATR : $X.XX | Stop suggéré : $XXX | Score Momentum : X/10 | Tendance : Haussière/Latérale/Baissière | Signal Bollinger : Squeeze/Normal | VWAP : Au-dessus/Dessous | RS vs S&P : X.XX (Sur/Sous-performe) | RS vs Secteur : X.XX | Saisonnalité : Favorable/Neutre/Défavorable`
```

---

## Règles d'interprétation

### Signaux forts haussiers (score 8-10)
- Cours > MM50 > MM200 (Golden Cross en place)
- RSI entre 50 et 65 (momentum sans excès)
- Volume en hausse sur les jours de progression
- Breakout d'une résistance clé avec volume > 1.5x

### Signaux forts baissiers (score 1-3)
- Cours < MM50 < MM200 (Death Cross en place)
- RSI < 40 et en baisse
- Volume en hausse sur les jours de baisse
- Rupture d'un support clé avec volume > 1.5x

### Divergences (signaux à surveiller)
- Cours monte mais RSI baisse → divergence baissière, prudence
- Cours baisse mais RSI monte → divergence haussière, potentiel rebond
- Cours monte mais volume baisse → momentum fragile

---

## Scoring Momentum pour le rapport Opportunités

| Fourchette score | Interprétation |
|-----------------|----------------|
| 9–10 | Breakout confirmé, tendance forte, timing excellent |
| 7–8 | Tendance favorable, bon point d'entrée |
| 5–6 | Signal mixte, attendre confirmation |
| 3–4 | Tendance défavorable, éviter ou shorter |
| 1–2 | Signal baissier fort, danger |

**Calcul score :**
- Tendance (MM50/200 + Golden/Death cross) : 0–3 pts
- Momentum (RSI/MACD/Stochastique) : 0–3 pts
- Volume & VWAP : 0–2 pts
- Position vs niveaux clés + Bollinger : 0–2 pts

**Bonus/malus volatilité :**
- Bollinger squeeze + catalyseur fondamental → +0.5 pt (breakout potentiel)
- IV >> HV sans catalyseur clair → −0.5 pt (peur du marché, risque de gap baissier)

**Bonus/malus force relative :**
- RS vs S&P > 1.10 ET RS vs secteur > 1.05 → +0.5 pt (leader double)
- RS vs S&P < 0.90 ET RS vs secteur < 0.95 → −0.5 pt (retardataire structurel)
- Saisonnalité favorable + signaux positifs → +0.3 pt
- Saisonnalité défavorable + signaux mitigés → −0.3 pt
