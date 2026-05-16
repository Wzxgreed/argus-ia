# Corrélations Watchlist — Matrice & Cascade

**Mis à jour le :** YYYY-MM-DD
**Fréquence de recalcul :** Hebdomadaire (chaque lundi matin) + immédiatement si mouvement > 3% sur un ticker

> Ce fichier mappe les corrélations entre tous les tickers de la watchlist. Quand un ticker bouge fortement, les tickers corrélés sont automatiquement vérifiés et des analyses d'impact peuvent être déclenchées en cascade.

---

## Matrice de corrélation (30 jours glissants)

> Corrélation calculée sur les rendements journaliers des 30 derniers jours.
> Mise à jour chaque lundi matin via `quote` (historique de cours).
> **Alerte si corrélation > 0.7 ET exposition combinée > 25% du portefeuille.**

| Ticker | [TICK1] | [TICK2] | [TICK3] | [TICK4] | [TICK5] |
|--------|---------|---------|---------|---------|---------|
| [TICK1] | 1.00 | | | | |
| [TICK2] | | 1.00 | | | |
| [TICK3] | | | 1.00 | | |
| [TICK4] | | | | 1.00 | |
| [TICK5] | | | | | 1.00 |

**Légende :** 🔴 > 0.7 (forte) · 🟡 0.4–0.7 (modérée) · 🟢 < 0.4 (faible) · ⚫ < 0 (inverse)

---

## Carte des dépendances — Facteurs communs

> Identifie pourquoi des tickers sont corrélés (facteur commun, secteur, supply chain partagée).

| Paire de tickers | Corrélation | Facteur commun | Type de lien |
|-----------------|-------------|---------------|-------------|
| [TICK1] / [TICK2] | 0.XX | Exposition USD / Taux / Secteur | Macro / Sectoriel / Supply chain |

---

## Protocole de cascade automatique

```
DÉCLENCHEUR : Un ticker watchlist bouge de > ±3% dans la journée

ÉTAPE 1 — Identification des corrélés
→ Lire la matrice ci-dessus
→ Identifier tous les tickers avec corrélation > 0.6 avec le ticker en mouvement

ÉTAPE 2 — Évaluation du type de mouvement
→ Le mouvement est-il idiosyncratique (news spécifique) ou systématique (macro) ?
   → Idiosyncratique (earnings, M&A, FDA) : impact sur corrélés limité, vérifier supply chain
   → Systématique (macro, secteur) : impact probable sur TOUS les corrélés > 0.6

ÉTAPE 3 — Analyse d'impact sur les corrélés
→ Pour chaque ticker corrélé (> 0.6) :
   a. Lire son INDEX.md → sensibilité identifiée au facteur en jeu
   b. Estimer l'impact en % (corrélation × amplitude du mouvement initial × 0.7)
   c. Si impact estimé > 1.5% → créer un _update.md "Impact corrélé"
   d. Si impact estimé > 3% → créer un _update.md complet + réviser prix cible

ÉTAPE 4 — Mise à jour WATCHLIST_SCORES.md
→ Insérer dans la section "Corrélations watchlist — Alertes du jour"
→ Mentionner dans le bulletin Actualités du jour
```

---

## Clusters sectoriels watchlist

> Groupes de tickers qui bougent ensemble. Mis à jour manuellement quand le portefeuille évolue.

| Cluster | Tickers | Facteur dominant | Beta sectoriel moyen |
|---------|---------|-----------------|---------------------|
| Semi-conducteurs | | Cycle semis, demande data center, TSMC | |
| IA / Cloud | | Dépenses capex IA, AWS/Azure/GCP | |
| Défense | | Budget DoD, géopolitique | |
| Énergie | | Prix pétrole WTI/Brent, DXY | |
| Taux sensibles | | Fed Funds Rate, taux 10Y US | |
| Chine exposure | | Tarifs douaniers, demande chinoise | |

---

## Corrélations avec actifs macro (beta calculé)

> Beta de chaque ticker watchlist par rapport aux grands actifs macro.
> Calculé sur 90 jours. Utilisé par l'Agent Macro pour chiffrer les impacts.

| Ticker | Beta S&P500 | Sensib. Taux 10Y (+1%) | Sensib. DXY (+5%) | Sensib. Pétrole (+10%) | Sensib. Chine (-10%) |
|--------|------------|----------------------|------------------|-----------------------|---------------------|
| | | -X% | -X% | +/-X% | -X% |

> **Source :** Calculé via `quote` (historique cours) croisé avec `economics` (données macro).
> Ces valeurs alimentent directement la "carte d'exposition macro" dans chaque `_init.md`.

---

## Alertes corrélation actives

> Paires dont la corrélation dépasse 0.7 avec une exposition combinée > 25% du portefeuille.

| Paire | Corrélation | Exposition combinée | Alerte |
|-------|------------|--------------------|----|
| | | | ⚠️ Sur-concentration / ✅ OK |

---

## Historique des cascades déclenchées

| Date | Ticker déclencheur | Mouvement | Tickers impactés | Corrélation | _update.md créé |
|------|-------------------|-----------|-----------------|-------------|----------------|
| — | — | — | — | — | — |

---

## Protocole de recalcul hebdomadaire

```
CHAQUE LUNDI MATIN (avant le bulletin) :

1. Pour chaque paire de tickers watchlist :
   → Récupérer 30 jours de cours via `quote`
   → Calculer le coefficient de corrélation de Pearson sur les rendements journaliers
   → Mettre à jour la matrice

2. Identifier les nouvelles alertes (corrélation franchit 0.7) :
   → Si nouvelle paire > 0.7 + exposition combinée > 25% → alerter dans WATCHLIST_SCORES.md

3. Recalculer les betas macro (tous les 90 jours) :
   → Régresser cours vs S&P500, taux 10Y, DXY, pétrole, indice China (MCHI ou FXI)
   → Mettre à jour le tableau "Corrélations avec actifs macro"

4. Mettre à jour les clusters sectoriels si nécessaire
```
