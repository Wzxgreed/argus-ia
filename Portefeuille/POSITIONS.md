# Portefeuille — Positions ouvertes

Mis à jour à chaque achat, vente partielle, ou recalcul de P&L.
Le P&L et les stop-loss ATR sont recalculés automatiquement lors de chaque bulletin du matin.

---

## Positions ouvertes

| Ticker | Nb actions | Prix entrée | Cours actuel | P&L $ | P&L % | Stop ATR | Stop % | Prix cible | Score | Qualité | % Capital | ATR 14j | Ouvert le | Analyse |
|--------|-----------|-------------|--------------|-------|-------|---------|--------|-----------|-------|---------|----------|---------|-----------|---------|
| | X | $XXX | $XXX | $XXX | +/-XX% | $XXX | -XX% | $XXX | X/10 | ✅⚠️🔴 | XX% | $X.XX | YYYY-MM-DD | [INDEX](../Actions/TICKER/INDEX.md) |

> **Stop ATR** = cours d'achat − 2 × ATR 14j (révisé chaque lundi, jamais abaissé)
> **Score** = score opportunité au moment de l'entrée (lu depuis le fichier _init.md ou _update.md source)
> **Qualité** = verdict Filtre Qualité (✅ Compounder / ⚠️ Partielle / 🔴 Hors périmètre)
> **% Capital** = capital alloué à cette position / capital total × 100

---

## Résumé portefeuille

| Métrique | Valeur |
|----------|--------|
| Capital total disponible | $XXX |
| Capital déployé | $XXX (XX%) |
| Cash disponible | $XXX (XX%) |
| P&L total ouvert | $XXX (+/-XX%) |
| P&L total depuis début | $XXX (+/-XX%) |
| Meilleure position | TICKER (+XX%) |
| Pire position | TICKER (−XX%) |
| Nb positions ouvertes | X |
| Exposition sectorielle max | SECTEUR (XX%) |
| Corrélation max entre positions | X.X (TICK1/TICK2) |
| VaR 95% (7j estimée) | −X% |
| Dernière mise à jour | YYYY-MM-DD |

---

## Détail par position — Sizing & Risque

> Cette section complète le tableau principal avec les détails de dimensionnement.
> Voir `Portefeuille/MODULE_SIZING.md` pour la méthode complète.

| Ticker | Capital alloué | Méthode sizing | Risk par trade | ATR entrée | Ratio ATR/Prix | Pyramide ? | Reinforcement possible |
|--------|---------------|---------------|---------------|-----------|---------------|-----------|----------------------|
| | $XXX (XX%) | ATR-based / Kelly | X% capital | $X.XX | X.X% | Oui/Non | Oui si +5% → +30% |

---

## Stop-loss tracker — Révision hebdomadaire

> Révisé chaque lundi matin via `Agents/WORKFLOW_SEMAINE.md` Phase H1.
> Le stop ne peut que monter, jamais descendre.

| Ticker | Stop initial | Stop actuel | ATR actuel | Nouveau stop calculé | Action |
|--------|-------------|------------|-----------|---------------------|--------|
| | $XXX | $XXX | $X.XX | $XXX (= cours − 2×ATR) | Monter / Conserver |

**Règle trailing stop :**
- Position en profit > 20% → stop = cours actuel − 1.5×ATR
- Position en profit > 50% → stop = cours actuel − 1×ATR (protéger les gains)

---

## Alertes actives sur positions ouvertes

| Ticker | Type d'alerte | Condition | Statut |
|--------|--------------|-----------|--------|
| | Stop ATR | Cours < $XXX | 🟢 OK |
| | Prix cible | Cours > $XXX | 🟢 OK |
| | Perte max | P&L < −15% | 🟢 OK |

---

## Règles de gestion du risque

Voir `Portefeuille/MODULE_RISQUE_PORTEFEUILLE.md` pour le protocole complet.

**Règles opérationnelles clés :**
- **Stop-loss ATR :** cours entrée − 2×ATR 14j (jamais un stop fixe en %)
- **Taille max par position :** 20% (Quality Compounder) · 10% (Quality Partielle) · 5% (Hors périmètre)
- **Taille max par secteur :** 35% du portefeuille
- **Drawdown mensuel > 10% :** réduire l'exposition de 50%
- **Drawdown total > 25% :** passer majoritairement en cash, post-mortem obligatoire
- **Révision stop-loss :** chaque lundi matin (WORKFLOW_SEMAINE.md Phase H1)
- **Corrélation alerte :** si 2 positions > 0.7 corrélation et > 25% exposition combinée → réduire l'une

---

## Protocole de mise à jour

```
À CHAQUE OPÉRATION (achat / vente / renforcement) :
1. Mettre à jour le tableau "Positions ouvertes" avec tous les champs
2. Calculer le stop ATR initial : cours − 2 × ATR 14j du jour
3. Calculer le % capital alloué
4. Ajouter une alerte dans Alertes/ALERTES.md (stop ATR + prix cible)
5. Enregistrer dans Portefeuille/PERFORMANCE.md si c'est une vente

CHAQUE MATIN (bulletin) :
1. Récupérer cours actuels via `quote`
2. Recalculer P&L$ et P&L% pour chaque position
3. Mettre à jour "Dernière mise à jour" dans Résumé
4. Si P&L d'une position < −15% → déclencher _update.md d'urgence

CHAQUE LUNDI (revue hebdomadaire) :
1. Recalculer ATR 14j pour chaque position via `technicalIndicators`
2. Calculer nouveau stop = MAX(stop actuel, cours − 2×ATR)
3. Mettre à jour le tableau "Stop-loss tracker"
4. Recalculer VaR et corrélations (MODULE_RISQUE_PORTEFEUILLE.md)
```
