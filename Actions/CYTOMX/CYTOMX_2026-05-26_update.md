# CYTOMX — Mise à jour snapshot 2026-05-26 17:00 UTC

> **Date :** 2026-05-26
> **Type :** Update post-pipeline (snapshot 17:00 UTC) — **FINAL**
> **Snapshot :** 17:00 UTC
> **Analyste :** Desk Argus-IA

---

## Récapitulatif des changements depuis l'analyse précédente

| Élément | Avant (snapshot 2026-05-26 10:00 UTC) | Maintenant (snapshot 2026-05-26 17:00 UTC) | Variation |
|---------|----------------------------------------|--------------------------------------------|-----------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | 50 (placeholder) | 50 (placeholder) | — |
| Volume | — | — | — |
| Score Opportunité | 5.5/10 | 5.5/10 | — |
| Score Global | 55.2/100 | 55.2/100 | — |
| Action | ATTENDRE | ATTENDRE | — |
| Snapshots consécutifs sans données | 8 | **9** | +1 |

**Observation principale :** Le snapshot 2026-05-26 17:00 UTC confirme la **stabilité totale** vs 10:00 UTC. CYTOMX reste avec `error=true`, `reason=No price history`. C'est le **9ème snapshot consécutif** sans données exploitables.

**Découverte structurante confirmée et résolue :**
- Le ticker **CYTOMX n'existe pas** sur Yahoo Finance (HTTP 404 Not Found).
- Le ticker correct de CytomX Therapeutics, Inc. sur NASDAQ est **CTMX**.
- Un fetch frais pour **CTMX a été exécuté avec succès** (close=$3.60, RSI=28.95) — voir `data/2026-05-26.json` et `data/latest.json` (snapshot 17:39 UTC).
- `config/watchlist.json` a été **corrigé** : remplacement de CYTOMX par CTMX avec nom, secteur et notes à jour.
- L'analyse institutionnelle migre désormais vers **`Actions/CTMX/`**.

---

## Mise à jour technique

- **Cours :** [DONNÉES MANQUANTES] — `prices.CYTOMX.error=true`, raison `No price history`
- **RSI 14j :** 50 (placeholder agent recommandation) — [UNSOURCED]
- **ATR 14j :** [DONNÉES MANQUANTES]
- **MM 50j / 200j :** [DONNÉES MANQUANTES]
- **Volume relatif :** [DONNÉES MANQUANTES]

**Verdict timing :** INCONNU — absence totale de données de cours sur 9 snapshots consécutifs.

---

## Mise à jour fondamentale

- **Données FMP :** [DONNÉES MANQUANTES] — aucun bloc `fmp_key_metrics`, `fmp_ratios` ou `fmp_consensus` pour CYTOMX
- **Filtre Qualité :** impossible à calculer
- **Consensus analystes :** [DONNÉES MANQUANTES]
- **Multiples :** [DONNÉES MANQUANTES]

**Earnings J=0 :** date FMP glissée au **2026-05-26** (`upcoming_events_latest.json`, `days_until=0`). C'est un **placeholder hérité** du symbole invalide. L'événement n'a pas lieu car CYTOMX n'existe pas.

---

## Mise à jour sentiment / options / news

- **News :** aucune news significative dans `data/news_latest.json`
- **Options flow :** [DONNÉES MANQUANTES]
- **Social sentiment :** 0 mention, score 0/10
- **Upgrades/downgrades :** aucun signal

---

## Contexte sectoriel et macro

- **Sector rotation :** CYTOMX non flaggé. XLV (Healthcare) momentum 0.0, RS négative vs SPY.
- **FX Exposure :** score 0.0
- **Geo risk :** non flaggé
- **Event-driven :** aucun événement
- **Accounting risk :** scan indisponible
- **Quant report :** date 2026-05-17, insuffisant (0 signaux), p-value = 1.0

---

## Scoring global (agents)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 5.0/10 | 25% | 1.25 |
| **Score Opportunité** | **5.5/10** | — | — |
| **Score Global** | **55.2/100** | — | — |

**Action recommandée :** ATTENDRE
**Note de fiabilité :** NULLE. Les scores reposent sur des placeholders (RSI 50, scores médians). Ce ticker est désormais hors périmètre institutionnel.

---

## Révision des niveaux SL / TP

**Impossible à établir** — prix actuel et ATR indisponibles.

---

## Conclusion

**Thèse : INVALIDÉE — MIGRATION VERS CTMX COMPLÉTÉE**

CYTOMX est définitivement un **symbole erroné**. Neuf snapshots consécutifs sans données, vérification Yahoo Finance confirmée (HTTP 404). La correction opérationnelle a été appliquée :

1. ✅ `config/watchlist.json` corrigé (CYTOMX → CTMX)
2. ✅ Fetch frais CTMX réussi ($3.60, RSI 28.95)
3. ✅ Dossier `Actions/CTMX/` créé avec analyse initiale complète (`CTMX_2026-05-26_init.md`)
4. ✅ `Actions/CTMX/INDEX.md` et `CONTEXT.md` créés

**Recommandation opérationnelle :**
- Ne plus utiliser CYTOMX dans aucun rapport de scoring.
- L'analyse de CytomX Therapeutics se poursuit dans **`Actions/CTMX/`**.
- L'ancien dossier `Actions/CYTOMX/` est archivé à des fins d'audit.

---

*Rapport final — snapshot 2026-05-26 17:00 UTC. Migration CTMX complétée.*
