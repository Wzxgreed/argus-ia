# Historique des Scores — Log de tous les signaux émis

**Mis à jour le :** —
**Total signaux émis :** 0
**Win rate global J+20 :** —

> Ce fichier est le registre exhaustif de tous les signaux publiés dans les rapports `Opportunités/YYYY-MM-DD.md`.
> Il alimente `Opportunités/BACKTESTING.md` (suivi des verdicts) et `Opportunités/MODULE_PERFORMANCE_SIGNAUX.md` (analyse par type de signal).

---

## 📋 Log des signaux — Tous les signaux émis

| Date | Ticker | Score Final | Cat. | Val. | Mom. | Régime macro | Type catalyseur | Qualité | Cours signal | Statut |
|------|--------|------------|------|------|------|-------------|----------------|---------|-------------|--------|
| — | — | — | — | — | — | — | — | — | — | — |

> **Colonnes :** Cat. = Score Catalyseur · Val. = Score Valorisation · Mom. = Score Momentum

---

## 📊 Statistiques globales

| Métrique | Valeur |
|----------|--------|
| Total signaux émis | 0 |
| Signaux clôturés (verdict connu J+20) | 0 |
| ✅ Hits (J+20 > +5%) | 0 |
| ❌ Misses (J+20 < −5%) | 0 |
| ⬜ Scratch (J+20 entre −5% et +5%) | 0 |
| **Win rate global J+20** | — |
| Gain moyen sur les Hits | — |
| Perte moyenne sur les Misses | — |
| Score moyen des signaux émis | — |
| Score moyen des Hits | — |
| Score moyen des Misses | — |

---

## 📈 Performance par tranche de score

| Tranche de score | Nb signaux | Win rate J+20 | Gain moy. Hits | Perte moy. Misses | Calibré ? |
|-----------------|-----------|--------------|---------------|------------------|----------|
| 9–10 | 0 | — | — | — | — |
| 8–8.9 | 0 | — | — | — | — |
| 7–7.9 | 0 | — | — | — | — |
| 6–6.9 | 0 | — | — | — | — |

> Seuil de calibration : win rate cible ≥ 70% pour 9-10 · ≥ 60% pour 8-8.9 · ≥ 55% pour 7-7.9

---

## 📅 Performance par mois

| Mois | Signaux émis | Win rate J+20 | Gain moy. | Régime dominant | Nb post-mortems |
|------|-------------|--------------|-----------|----------------|----------------|
| — | 0 | — | — | — | 0 |

---

## 🏷️ Performance par type de catalyseur

| Type de catalyseur | Nb signaux | Win rate | Gain moy. | Tendance |
|-------------------|-----------|----------|-----------|---------|
| Upgrade analyste (track record élevé) | 0 | — | — | — |
| Earnings beat + guidance relevée | 0 | — | — | — |
| Cluster buying insiders | 0 | — | — | — |
| Short squeeze setup | 0 | — | — | — |
| Unusual options activity | 0 | — | — | — |
| EPS Revision Momentum fort | 0 | — | — | — |
| Nouveau contrat gouvernemental | 0 | — | — | — |
| Signal supply chain positif | 0 | — | — | — |
| Rotation sectorielle / macro | 0 | — | — | — |
| Pattern récurrent détecté | 0 | — | — | — |
| Autre | 0 | — | — | — |

---

## 🌍 Performance par secteur

| Secteur | Nb signaux | Win rate | Gain moy. | Meilleur signal dans ce secteur |
|---------|-----------|----------|-----------|--------------------------------|
| Tech / IA | 0 | — | — | — |
| Semi-conducteurs | 0 | — | — | — |
| Défense | 0 | — | — | — |
| Santé / Biotech | 0 | — | — | — |
| Énergie | 0 | — | — | — |
| Finance | 0 | — | — | — |
| Consommation | 0 | — | — | — |

---

## 🏆 Hall of Fame — Meilleurs signaux

| Date | Ticker | Score | Perf. J+20 | Perf. J+60 | Catalyseur principal |
|------|--------|-------|-----------|-----------|---------------------|
| — | — | — | — | — | — |

---

## 💀 Post-mortems — Pires signaux

| Date | Ticker | Score | Perf. J+20 | Cause racine | Règle extraite |
|------|--------|-------|-----------|-------------|---------------|
| — | — | — | — | — | — |

---

## 🔍 Signaux manqués (actions non détectées mais forte hausse)

> Actions qui ont progressé de >15% sans avoir été signalées. Identifiées en retrospective.

| Date détectée | Ticker | Perf. | Pourquoi non détecté | Amélioration suggérée |
|--------------|--------|-------|---------------------|----------------------|
| — | — | — | — | — |

---

## Protocole de mise à jour

```
CHAQUE MATIN (après la Phase 3 — Rapport Opportunités) :
→ Pour chaque nouvelle opportunité publiée dans Opportunités/YYYY-MM-DD.md :
   1. Ajouter une ligne dans "Log des signaux" avec tous les champs
   2. Le signal est créé avec statut "⏳ En cours"
   3. Le même signal est enregistré dans BACKTESTING.md

CHAQUE FOIS QU'UN VERDICT J+20 EST RENDU (dans BACKTESTING.md) :
→ Mettre à jour le statut dans le log : ✅ Hit / ❌ Miss / ⬜ Scratch
→ Mettre à jour les statistiques globales
→ Mettre à jour la performance par tranche de score
→ Mettre à jour la performance par type de catalyseur
→ Si Hit → candidat Hall of Fame (si Perf. J+20 > +15%)
→ Si Miss avec score ≥ 8 → candidat post-mortem "Pires signaux"

CHAQUE MOIS (premier lundi du mois) :
→ Calculer le win rate mensuel et l'ajouter dans "Performance par mois"
→ Identifier le catalyseur le plus performant du mois
→ Vérifier si des signaux manqués sont identifiables (actions >15% non détectées)
```
