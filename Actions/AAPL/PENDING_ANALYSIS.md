# AAPL — Analyse en attente

> **Date :** 2026-05-16
> **Statut :** 🟡 DRAFT généré — prêt pour interprétation LLM
> **Priorité :** high

---

## Fichiers disponibles

| Fichier | Statut | Description |
|---------|--------|-------------|
| `AAPL_2026-05-16_DRAFT_init.md` | ✅ Prêt | DRAFT avec données brutes pré-collectées |
| `INDEX.md` | ⏳ En attente | À créer après complétion du DRAFT |
| `SUPPLY_CHAIN.md` | ⏳ En attente | À créer après analyse |
| `AAPL_2026-05-16_init.md` | ⏳ En attente | Version finale (copie du DRAFT complété) |

---

## Données pré-collectées (snapshot)

| Donnée | Valeur |
|--------|--------|
| **Cours** | $300.23 |
| **Change** | 0.68% |
| **Market Cap** | 4,409,585,041,408 |
| **P/E (TTM)** | 36.347458 |
| **Secteur** | Technology |

---

## Commande pour lancer l'analyse automatique

L'agent LLM détecte automatiquement les DRAFT au démarrage (voir Étape 0 du CLAUDE.md).

**Commande manuelle alternative :**
```
Analyse AAPL en complétant le DRAFT AAPL_2026-05-16_DRAFT_init.md.
Lis data/latest.json pour les données temps réel.
Sauvegarde sous Actions/AAPL/AAPL_2026-05-16_init.md
```

---

## Workflow de complétion

1. **Lire le DRAFT** (`AAPL_2026-05-16_DRAFT_init.md`) — tous les blocs de données sont pré-structurés
2. **Lire `data/latest.json`** — remplir les champs techniques (RSI, ATR, MM, FMP, options)
3. **Lire `data/quant_report_latest.json`** — remplir le bloc Quant
4. **Lire `data/geo_risk_latest.json`** — remplir le bloc Géopolitique
5. **Market Researcher** — remplir TAM, peers, competitive landscape
6. **Agent Fondamental** — calculer Filtre Qualité 6 critères, DCF, valorisation
7. **Agent Technique** — interpréter RSI, niveaux, timing
8. **Agent Sentiment** — analyser consensus, options, news
9. **Copier le DRAFT complété** → `AAPL_2026-05-16_init.md`
10. **Créer `INDEX.md`** avec thèse courante
11. **Mettre à jour `WATCHLIST_SCORES.md`** et `CALENDRIER_EARNINGS.md`
12. **Supprimer le DRAFT** (ou le renommer `_DRAFT_init.md` pour archive)
