# Suivi des Prédictions Earnings — Registre centralisé

Ce fichier recense **toutes les prédictions de réaction post-earnings** émises dans les fichiers `_preview.md`, et les compare avec la réaction réelle documentée dans les `_earnings.md`. Il permet de calibrer précisément la sensibilité du cours aux surprises.

**Mise à jour :** Automatique à chaque création d'un `_preview.md` (enregistrement de la prédiction) et à chaque création d'un `_earnings.md` (enregistrement de la réalité).

**Fichier lié :** `Agents/APPRENTISSAGES.md` — reçoit les règles extraites des post-mortems earnings.

---

## Protocole d'enregistrement obligatoire

```
À LA CRÉATION D'UN _preview.md :
1. Extraire : Ticker · Date earnings · Consensus EPS · Consensus Revenus
2. Extraire les prédictions de réaction : Beat → +X% / Inline → ±X% / Miss → -X%
3. Extraire la probabilité de beat estimée (XX%)
4. Ajouter dans le journal (colonnes "Prédiction")

À LA CRÉATION D'UN _earnings.md :
1. Retrouver la ligne du preview correspondant dans ce journal
2. Remplir : Surprise réelle revenus · Surprise réelle EPS · Réaction cours effective
3. Calculer l'écart prédiction vs réalité
4. Si écart > 5% sur la réaction → déclencher post-mortem earnings
```

---

## Définition des verdicts

| Verdict | Condition | Interprétation |
|---------|-----------|----------------|
| ✅ Précis | Réaction réelle dans ±3% de la prédiction | Calibration correcte |
| ⚠️ Approximatif | Écart 3–8% entre prédiction et réalité | Acceptable, affiner |
| ❌ Imprécis | Écart > 8% entre prédiction et réalité | Post-mortem requis |
| 🔄 Exogène | Réaction dominée par macro externe le jour J | Pas une erreur de prédiction earnings |

---

## Journal des prédictions earnings

| Date preview | Ticker | Date earnings | EPS consensus | Reco preview | Prédiction beat | Prédiction miss | Proba beat | EPS réel | Surprise EPS | Rev réel | Surprise Rev | Réaction cours réelle | Verdict | Post-mortem |
|-------------|--------|--------------|--------------|-------------|----------------|----------------|-----------|---------|-------------|---------|-------------|----------------------|---------|-------------|
| — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

---

## Fenêtres en attente (preview créé, earnings pas encore publiés)

| Ticker | Date preview | Date earnings prévue | Prédictions enregistrées |
|--------|-------------|---------------------|--------------------------|
| — | — | — | — |

---

## Performance agrégée des prédictions earnings

### Précision globale
| Métrique | Valeur |
|----------|--------|
| Previews réalisés | 0 |
| Verdicts ✅ Précis | 0 (—%) |
| Verdicts ⚠️ Approximatifs | 0 (—%) |
| Verdicts ❌ Imprécis | 0 (—%) |
| Erreur moyenne sur réaction cours | — |

### Biais de prédiction
| Type de biais | Fréquence | Correction appliquée |
|--------------|-----------|----------------------|
| Surestimation réaction positive (beat) | 0 | — |
| Sous-estimation réaction négative (miss) | 0 | — |
| Mauvaise proba de beat (systématiquement trop optimiste) | 0 | — |
| Bonne direction, mauvaise amplitude | 0 | — |

### Par secteur
| Secteur | Previews | Précision | Biais identifié |
|---------|---------|-----------|----------------|
| Tech | 0 | — | — |
| Santé | 0 | — | — |
| Finance | 0 | — | — |
| Énergie | 0 | — | — |

### Historique surprise vs prédiction par ticker

> S'enrichit au fil du temps pour détecter les tickers systématiquement mal prédits.

| Ticker | Previews réalisés | Précision moyenne | Pattern identifié |
|--------|------------------|------------------|-------------------|
| — | — | — | — |

---

## Protocole Post-Mortem Earnings

> Déclenché automatiquement quand verdict = ❌ Imprécis (écart > 8% entre prédiction et réaction réelle).

```
ÉTAPE 1 — COLLECTE
→ Lire Actions/[TICKER]/[TICKER]_YYYY-MM-DD_preview.md (prédictions)
→ Lire Actions/[TICKER]/[TICKER]_YYYY-MM-DD_earnings.md (résultats réels)
→ Comparer en détail : revenus, EPS, marges, guidance, réaction cours

ÉTAPE 2 — DIAGNOSTIC
→ L'erreur vient-elle de :
   A) SURPRISE mal estimée : beat/miss plus fort qu'anticipé
      → Le consensus de marché était-il mal calibré ? Whisper ignoré ?
   B) BARRE IMPLICITE ignorée : beat sur les chiffres mais déception sur la guidance
      → L'agent a prédit "+5% si beat" mais le marché avait une barre plus haute
   C) RÉACTION atypique : résultats conformes mais réaction exagérée
      → VIX élevé ? Contexte macro défavorable ce jour-là ? Positionnement court terme ?
   D) MÉTRIQUES CLÉS ignorées : l'agent a prédit sur EPS mais le marché regardait ailleurs
      → Ex : réaction dominée par la guidance et non les chiffres passés

ÉTAPE 3 — RÈGLE EXTRAITE
→ Ex : "Pour [TICKER], le marché réagit principalement à la guidance, pas à l'EPS — ajuster
  le modèle de prédiction pour pondérer la guidance à 60% dans la réaction estimée"
→ Ex : "En régime Risk-off, multiplier la réaction négative estimée par 1.5 — le marché
  punit plus durement les misses en contexte volatile"

ÉTAPE 4 — DOCUMENTATION
→ Écrire le post-mortem dans Agents/APPRENTISSAGES.md (section Earnings Predictions)
→ Ajouter la règle dans "Règles actives"
→ Mettre à jour colonne "Post-mortem" dans ce journal
→ Si pattern sur un ticker spécifique : noter dans "Historique par ticker"
```

---

## Règles de calibration par ticker

> Règles spécifiques découvertes sur chaque ticker après plusieurs cycles d'earnings.

| Ticker | Règle de calibration | Depuis | Confiance |
|--------|---------------------|--------|-----------|
| — | — | — | — |

---

## Statistiques d'apprentissage

| Métrique | Valeur |
|----------|--------|
| Prédictions enregistrées | 0 |
| Post-mortems earnings réalisés | 0 |
| Précision moyenne sur réaction | — |
| Biais principal identifié | — |
| Règles de calibration actives | 0 |
