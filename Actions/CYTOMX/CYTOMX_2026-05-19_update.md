# CYTOMX — Mise a jour snapshot final 2026-05-19 21:00 UTC

> **Date :** 2026-05-19
> **Type :** Update post-pipeline (snapshot final)
> **Snapshot :** 21:00 UTC
> **Analyste :** Desk Argus-IA

---

## Recapitulatif des changements depuis l'analyse precedente

| Element | Avant (snapshot 13:59 UTC) | Maintenant (snapshot 21:00 UTC) | Variation |
|---------|---------------------------|--------------------------------|-----------|
| Cours | [DONNEES MANQUANTES] | [DONNEES MANQUANTES] | — |
| RSI 14j | 50 (placeholder) | 50 (placeholder) | — |
| Volume | — | — | — |
| Score Opportunite | 5.5/10 | 5.5/10 | — |
| Score Global | 55.2/100 | 55.2/100 | — |
| Action | ATTENDRE | ATTENDRE | — |
| Earnings | J=0 (2026-05-19) | J=0 (2026-05-19) | toujours non resolu |
| Validation | [ERROR] fetch failed | [ERROR] fetch failed | inchangé |

**Observation principale :** Le snapshot final 21:00 UTC confirme l'erreur persistante `No price history` pour CYTOMX. L'earnings annonce pour le 2026-05-19 (source FMP) reste non resolu a la cloture de la session US. Aucune donnee de cours, technique ou fondamentale n'a ete recuperee sur les trois snapshots du jour (10:00 UTC, 13:59 UTC, 21:00 UTC).

---

## Mise a jour technique

- **Cours :** [DONNEES MANQUANTES] — aucune serie historique disponible
- **RSI 14j :** 50 (placeholder agent recommandation) — [UNSOURCED] sans donnees reelles
- **ATR 14j :** [DONNEES MANQUANTES]
- **MM 50j / 200j :** [DONNEES MANQUANTES]
- **Volume relatif :** [DONNEES MANQUANTES]

**Verdict timing :** INCONNU — absence totale de donnees de cours. Aucun niveau technique n'est calculable.

---

## Mise a jour fondamentale

- **Donnees FMP :** [DONNEES MANQUANTES] — aucun bloc `fmp_key_metrics`, `fmp_ratios` ou `fmp_consensus` pour CYTOMX dans `data/latest.json`
- **Filtre Qualite 6 criteres :** impossible a calculer sans etats financiers extraits du snapshot
- **Consensus analystes :** [DONNEES MANQUANTES]
- **Multiples :** [DONNEES MANQUANTES]

**Earnings J=0 :** la date prevue est le 2026-05-19. Aucun resultat publie ni detecte dans les flux du pipeline aux trois snapshots du jour. Le preview `CYTOMX_2026-05-19_preview.md` reste un template vide en l'absence de consensus EPS/Revenue exploitable.

---

## Mise a jour sentiment / options / news

- **News :** aucune news significative detectee dans les flux unifies du pipeline (snapshot 21:00 UTC)
- **Options flow :** [DONNEES MANQUANTES] — pas de donnees options pour CYTOMX
- **Social sentiment :** 0 mention, score 0/10, label "No data" — pas de signal retail
- **Upgrades/downgrades :** aucun signal detecte
- **Activite inhabituelle :** non calculable sans volume ni cours

---

## Contexte sectoriel et macro

- **Sector rotation (snapshot 21:00 UTC) :** XLV (Healthcare) en position faible — momentum score 0.0, RS 20j -0.0325 vs SPY, regime UNKNOWN. Le segment biotech therapeutique subit un headwind sectoriel qui penalisera CYTOMX des l'ouverture des donnees.
- **FX Exposure :** score 0.0, direction "neutral" — 25% exposure generic, zero impact calcule (donnees manquantes)
- **Geo risk :** CYTOMX non flagge dans `geo_risk_latest.json` (seul IREN a un score geo = 3)
- **Event-driven :** aucun evenement corporate detecte (M&A, buyback, activism, guidance change)
- **Accounting risk :** fichier `accounting_risk_latest.json` absent — scan comptable non disponible pour ce ticker

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

**Note de fiabilite :** les scores proviennent de l'agent recommandation mais sont fondes sur des placeholders (RSI par defaut 50, scores medians) en l'absence de donnees reelles. La fiabilite est **faible** et le scoring ne doit pas servir de base a une decision d'investissement tant que les donnees de cours ne sont pas recuperees.

---

## Revision des niveaux SL / TP

**Impossible a etablir** — prix actuel et ATR indisponibles.

| Niveau | Valeur |
|--------|--------|
| Stop-loss suggere | [DONNEES MANQUANTES] |
| Take-profit suggere | [DONNEES MANQUANTES] |
| Ratio R/R | [DONNEES MANQUANTES] |

---

## Conclusion

**These : NON ETABLIE — CONFIRMEE**

CYTOMX n'a fait l'objet d'aucune analyse initiale (`_init.md`). Les donnees de cours sont indisponibles sur l'ensemble des trois snapshots du 2026-05-19 (10:00 UTC, 13:59 UTC, 21:00 UTC). L'earnings annonce pour le 2026-05-19 n'a pas ete resolu au snapshot final 21:00 UTC. XLV (Healthcare) affiche un momentum score nul (0.0) et une force relative negative vs SPY, signalant un headwind sectoriel en cas de reprise des donnees.

**Recommandation operationnelle :**
- Attendre la resolution de l'earnings et la recuperation des donnees de cours via yfinance/FMP
- Des que les donnees redeviennent disponibles : lancer une analyse initiale complete (`_init.md`) avec Filtre Qualite 6 criteres, Market Researcher (TAM, peers, comps) et Earnings Reviewer
- Sans donnees de cours : le ticker ne peut pas etre evalue dans le cadre du scoring institutionnel

**Alertes actives :**
- [DONNEES MANQUANTES] cours introuvable dans `data/latest.json` (snapshots 10:00 UTC, 13:59 UTC, 21:00 UTC)
- [WARNING] XLV (Healthcare) momentum 0.0 — headwind sectoriel
- Earnings J=0 non resolu (source FMP)
- Accounting risk scan indisponible (`accounting_risk_latest.json` absent)

---

*Rapport genere automatiquement — snapshot final 2026-05-19 21:00 UTC.*
