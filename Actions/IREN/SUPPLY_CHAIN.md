# IREN — Cartographie Supply Chain

**Date :** 2026-05-17
**Méthode :** Analyse basée sur les déclarations publiques, partenariats annoncés et secteur d'activité.

---

## Overview

IREN opère à l'intersection de **trois chaînes de valeur** :
1. **Mining Bitcoin** (legacy) — dépendance énergie + hardware ASIC
2. **Infrastructure HPC/IA** (pivot) — dépendance GPU + refroidissement + énergie
3. **Cloud Computing** (ambition) — dépendance clients enterprise + connectivité

---

## 🔴 Fournisseurs Critiques

| Fournisseur | Produit / Service | Dépendance | Risque | Opportunité |
|-------------|-------------------|-----------|--------|-------------|
| **NVIDIA** | GPU H100/H200/Blackwell | **Très élevée** ($3.4B contrat) | Single-source. Pénuries GPU = retard CAPEX HPC. | Partenariat stratégique = accès privilégié aux nouvelles générations |
| **Bitmain / MicroBT** | ASIC miners (BTC) | Élevée (legacy) | Tarifs / restrictions d'export Chine = pénurie ASIC | — |
| **Fournisseurs énergie** | Électricité (PJM, Texas, Australie) | **Très élevée** | Brent $109 = coûts énergie en hausse. Accords PPA à renégocier. | IREN a des accords long terme en Australie et US — pricing fixe partiel |
| **Vertiv (VRT)** | Refroidissement data centers | Modérée (pivot) | Vertiv leader mondial. Si pénurie = retard déploiement HPC. | IREN et VRT partagent l'écosystème NVIDIA — synergies possibles |

---

## 🟡 Clients / Débouchés Importants

| Client / Débouché | Revenus estimés | Exposition | Risque | Opportunité |
|--------------------|-----------------|------------|--------|-------------|
| **NVIDIA (contrat $3.4B)** | ~60–70% revenus futurs HPC | Très élevée | Single-client = concentration extrême. Si NVIDIA ralentit ses CAPEX IA = chute directe. | Contrat multi-annuel = visibilité à moyen terme |
| **Marché spot BTC** | Legacy mining | Décroissante | Prix BTC = volatilité extrême. Si BTC < $50k = mining non rentable. | Hedge naturel via diversification HPC |
| **Entreprises cloud / IA** | Future croissance | Croissante | Concurrence intense (AWS, GCP, Azure, CoreWeave) | Niche géo-stratégique (Australie = proche Asie) |

---

## Chaîne de Valeur IREN

```
ÉNERGIE (PJM, Texas, Australie)
    ↓
[ Data Centers IREN ] ——— GPU NVIDIA ——— Refroidissement Vertiv?
    ↓                    ASIC Bitmain (legacy)
    ↓
┌─────────────────┬─────────────────┐
│  HPC / IA Cloud │  BTC Mining     │
│  (Client : NVDA)│  (Marché spot)  │
└─────────────────┴─────────────────┘
```

---

## Risques Supply Chain

| Risque | Probabilité | Impact | Mitigation IREN |
|--------|------------|--------|----------------|
| Pénurie GPU NVIDIA | Moyenne | Très élevé | Contrat $3.4B = allocation privilégiée |
| Hausse énergie >30% | Moyenne | Élevé | Accords PPA long terme + sites en zones à bas coût énergie |
| Tarifs ASIC Chine | Faible | Élevé | Legacy : déjà en cours de réduction |
| Régulation anti-mining US | Moyenne | Très élevé | **C'est le catalyseur du pivot IA** |
| Défaillance refroidissement | Faible | Élevé | Sites modernes, mais dépendance Vertiv si upgrade |

---

## Opportunités Supply Chain

1. **Nouveau client majeur non-NVIDIA** — Si IREN signe un deuxième client HPC >$500M, la concentration NVIDIA diminue et la thèse pivot est validée.
2. **Expansion géographique** — Sites en Australie = proche marché asiatique IA (Singapour, Japon). Potentiel clientèle régionale.
3. **Synergies Vertiv** — Refroidissement mutualisé entre IREN et NVIDIA. Partenariat VRT possible.

---

## Monitoring Quotidien

Scanner les news sur :
- **NVIDIA** : annonces CAPEX, pénuries GPU, guidance datacenter
- **Vertiv (VRT)** : nouveaux contrats refroidissement, pénuries
- **BTC** : prix, hash rate, régulation US (Texas notamment)
- **Énergie** : prix PJM, politique énergétique Australie

---

*Mise à jour : 2026-05-17 — Première version.*
