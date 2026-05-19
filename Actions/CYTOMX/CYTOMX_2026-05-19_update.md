# CYTOMX — Mise a jour post-pipeline 2026-05-19

> **Date :** 2026-05-19
> **Type :** Update post-pipeline
> **Snapshot :** 10:00 UTC

---

## Recapitulatif des changements depuis l'analyse precedente

| Element | Avant (2026-05-18) | Maintenant (2026-05-19) | Variation |
|---------|--------------------|-------------------------|-----------|
| Cours | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| RSI 14j | — | 50 (placeholder) | — |
| Volume | — | — | — |
| Score Opportunite | — | 5.5/10 | — |
| Score Global | — | 55.2/100 | — |
| Action | — | ATTENDRE | — |
| Earnings | J=0 (2026-05-18) | J=0 (2026-05-19) | toujours en attente |

**Observation principale :** les donnees de cours pour CYTOMX restent indisponibles dans `data/latest.json` (`error: No price history`). Le pipeline du 2026-05-19 n'a pas reussi a recuperer les series historiques. L'earnings annonce pour le 2026-05-19 (source FMP) est toujours non resolu a l'heure du snapshot 10:00 UTC.

---

## Mise a jour technique

- **Cours :** [DONNEES MANQUANTES] — impossible de calculer les niveaux techniques
- **RSI 14j :** 50 (placeholder agent recommandation) — [UNSOURCED] sans donnees reelles
- **ATR 14j :** [DONNEES MANQUANTES]
- **MM 50j / 200j :** [DONNEES MANQUANTES]
- **Volume relatif :** [DONNEES MANQUANTES]

**Verdict timing :** INCONNU — absence de donnees de cours. Aucun niveau de support/resistance n'est calculable.

---

## Mise a jour fondamentale

- **Donnees FMP :** [DONNEES MANQUANTES] — aucun enrichissement fondamental dans le snapshot du jour
- **Consensus analystes :** [DONNEES MANQUANTES]
- **Multiples :** [DONNEES MANQUANTES]

**Earnings J=0 :** la date prevue est le 2026-05-19. Aucun resultat n'a ete publie au moment du snapshot. Le preview du 2026-05-19 reste un template non complete en raison de l'absence de consensus EPS/Revenue exploitable.

---

## Mise a jour sentiment / options / news

- **News :** aucune news significative detectee dans les flux du pipeline
- **Options flow :** [DONNEES MANQUANTES] — pas de donnees options pour CYTOMX dans le snapshot
- **Social sentiment :** score 0/10, 0 mention — [NO DATA]
- **Upgrades/downgrades :** aucun signal detecte

---

## Scoring global (agents)

| Axe | Score | Ponderation | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 5.0/10 | 25% | 1.25 |
| **Score Opportunite** | **5.5/10** | — | — |
| **Score Global** | **55.2/100** | — | — |

**Action recommandee :** ATTENDRE
**Timing :** Neutre
**Sizing :** —

**Note :** les scores proviennent de l'agent recommandation mais sont bases sur des placeholders en l'absence de donnees reelles. La fiabilite est faible.

---

## Revision des niveaux SL / TP

**Impossible a etablir** — prix actuel et ATR indisponibles.

- Stop-loss suggere : [DONNEES MANQUANTES]
- Take-profit suggere : [DONNEES MANQUANTES]
- Ratio R/R : [DONNEES MANQUANTES]

---

## Conclusion

**Theses : NON ETABLIE**

CYTOMX n'a fait l'objet d'aucune analyse initiale (`_init.md`). Les donnees de cours sont indisponibles depuis au moins deux snapshots consecutifs (2026-05-18 et 2026-05-19). L'earnings annonce pour le 2026-05-19 n'a pas ete resolu au moment du snapshot 10:00 UTC.

**Recommandation :**
- Attendre la resolution de l'earnings et la recuperation des donnees de cours via yfinance/FMP
- Si les donnees redeviennent disponibles : lancer une analyse initiale complete (`_init.md`) avec Filtre Qualite 6 criteres
- Sans donnees de cours : le ticker ne peut pas etre evalue dans le cadre du scoring institutionnel

**Alertes actives :**
- [DONNEES MANQUANTES] cours introuvable
- Earnings J=0 non resolu

---

*Rapport genere automatiquement — snapshot 2026-05-19 10:00 UTC.*
