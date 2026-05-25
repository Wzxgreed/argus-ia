# CYTOMX — Mise à jour snapshot 2026-05-25 13:00 UTC

> **Date :** 2026-05-25
> **Type :** Update post-pipeline (snapshot 13:00 UTC)
> **Snapshot :** 13:00 UTC
> **Analyste :** Desk Argus-IA

---

## Récapitulatif des changements depuis l'analyse précédente

| Élément | Avant (snapshot 2026-05-25 10:00 UTC) | Maintenant (snapshot 2026-05-25 13:00 UTC) | Variation |
|---------|----------------------------------------|--------------------------------------------|-----------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | 50 (placeholder) | 50 (placeholder) | — |
| Volume | — | — | — |
| Score Opportunité | 5.5/10 | 5.5/10 | — |
| Score Global | 55.2/100 | 55.2/100 | — |
| Action | ATTENDRE | ATTENDRE | — |
| Earnings (FMP) | J=0 (2026-05-25) | J=0 (2026-05-25) | inchangé |
| Validation | [ERROR] fetch failed | [ERROR] fetch failed | inchangé |

**Observation principale :** Le snapshot 2026-05-25 13:00 UTC confirme l'erreur persistante `No price history` pour CYTOMX (`data/latest.json`, bloc `prices.CYTOMX.error=true`). Aucune donnée de cours, technique ou fondamentale n'a été récupérée sur les **six snapshots consécutifs** (2026-05-19 10:00/13:59/21:00 UTC, 2026-05-20 10:00 UTC, 2026-05-25 10:00 UTC et 2026-05-25 13:00 UTC). Le calendrier FMP (`upcoming_events_latest.json`) maintient la date earnings au **2026-05-25** (J=0) ; l'événement reste non résolu à ce snapshot. XLV (Healthcare) continue d'afficher un momentum score nul (0.0) et une force relative négative vs SPY (−0.48% RS 20j), signalant un headwind sectoriel persistant.

---

## Mise à jour technique

- **Cours :** [DONNÉES MANQUANTES] — `prices.CYTOMX.error=true`, raison `No price history`
- **RSI 14j :** 50 (placeholder agent recommandation) — [UNSOURCED] sans données réelles
- **ATR 14j :** [DONNÉES MANQUANTES]
- **MM 50j / 200j :** [DONNÉES MANQUANTES]
- **Volume relatif :** [DONNÉES MANQUANTES]

**Verdict timing :** INCONNU — absence totale de données de cours. Aucun niveau technique n'est calculable.

---

## Mise à jour fondamentale

- **Données FMP :** [DONNÉES MANQUANTES] — aucun bloc `fmp_key_metrics`, `fmp_ratios` ou `fmp_consensus` pour CYTOMX dans `data/latest.json`
- **Filtre Qualité 6 critères :** impossible à calculer sans états financiers extraits du snapshot
- **Consensus analystes :** [DONNÉES MANQUANTES]
- **Multiples :** [DONNÉES MANQUANTES]

**Earnings J=0 :** la date FMP est maintenue au 2026-05-25 (`upcoming_events_latest.json`, `days_until=0`, source `fmp`). Aucun résultat publié ni détecté dans les flux du pipeline au snapshot 13:00 UTC. C'est le **6e report de date** consécutif (initialement 2026-05-19, puis 2026-05-20, 2026-05-21, 2026-05-22, 2026-05-23, 2026-05-24, désormais 2026-05-25).

---

## Mise à jour sentiment / options / news

- **News :** aucune news significative détectée dans les flux unifiés du pipeline (snapshot 13:00 UTC) — `data/news_latest.json` ne mentionne pas CYTOMX
- **Options flow :** [DONNÉES MANQUANTES] — pas de données options pour CYTOMX
- **Social sentiment :** 0 mention, score 0/10, label "No data" (`social_sentiment_latest.json`) — pas de signal retail
- **Upgrades/downgrades :** aucun signal détecté
- **Activité inhabituelle :** non calculable sans volume ni cours

---

## Contexte sectoriel et macro

- **Sector rotation (snapshot 2026-05-25) :** XLV (Healthcare) affiche un momentum score 0.0 et une force relative RS 20j de −0.48% vs SPY (`sector_rotation_latest.json`). Le segment biotech thérapeutique reste sous headwind sectoriel. Noter que XLV a gagné +3.96% sur 20j en absolu, mais sous-performe le SPY (+4.44% sur 20j).
- **FX Exposure :** score 0.0, direction "neutral", 25% exposure generic, zéro impact calculé (`fx_exposure_latest.json`)
- **Geo risk :** CYTOMX non flaggé dans `geo_risk_latest.json` (seul IREN a un score geo = 3)
- **Event-driven :** aucun événement corporate détecté (`events_latest.json` : `tickers_with_events=0`)
- **Accounting risk :** fichier `accounting_risk_latest.json` absent — scan comptable non disponible pour ce ticker
- **Quant report :** date 2026-05-17, insuffisant (0 signaux), p-value = 1.0, conclusion "Insuffisant"

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
**Timing :** Neutre
**Sizing :** —

**Note de fiabilité :** les scores proviennent de l'agent recommandation mais reposent sur des placeholders (RSI par défaut 50, scores médians) en l'absence de données réelles. La fiabilité est **faible** et le scoring ne doit pas servir de base à une décision d'investissement tant que les données de cours ne sont pas récupérées. Le validation report (`data/validation_report.txt`) confirme l'erreur `[ERROR] CYTOMX: fetch failed — No price history`.

---

## Révision des niveaux SL / TP

**Impossible à établir** — prix actuel et ATR indisponibles.

| Niveau | Valeur |
|--------|--------|
| Stop-loss suggéré | [DONNÉES MANQUANTES] |
| Take-profit suggéré | [DONNÉES MANQUANTES] |
| Ratio R/R | [DONNÉES MANQUANTES] |

---

## Conclusion

**Thèse : NON ÉTABLIE — CONFIRMÉE**

CYTOMX n'a fait l'objet d'aucune analyse initiale (`_init.md`). Les données de cours sont indisponibles sur **six snapshots consécutifs** (2026-05-19 10:00/13:59/21:00 UTC ; 2026-05-20 10:00 UTC ; 2026-05-25 10:00 UTC ; 2026-05-25 13:00 UTC). L'earnings FMP, initialement annoncé au 2026-05-19, puis reporté successivement jusqu'au 2026-05-25, reste non résolu au snapshot 13:00 UTC. XLV (Healthcare) affiche un momentum score nul (0.0) et une force relative négative vs SPY, signalant un headwind sectoriel persistant.

**Recommandation opérationnelle :**
- Attendre la résolution de l'earnings et la récupération des données de cours via yfinance/FMP
- Dès que les données redeviennent disponibles : lancer une analyse initiale complète (`_init.md`) avec Filtre Qualité 6 critères, Market Researcher (TAM, peers, comps) et Earnings Reviewer
- Sans données de cours : le ticker ne peut pas être évalué dans le cadre du scoring institutionnel
- Si l'earnings est effectivement aujourd'hui (2026-05-25) et que les résultats sont publiés après l'ouverture US, un snapshot post-séance ou une vérification manuelle est nécessaire pour résoudre l'événement
- Envisager un changement de ticker ou une suspension de cotation comme cause alternative à l'erreur `No price history` persistante sur six snapshots

**Alertes actives :**
- [DONNÉES MANQUANTES] cours introuvable dans `data/latest.json` (snapshots 2026-05-19 10:00/13:59/21:00 UTC, 2026-05-20 10:00 UTC, 2026-05-25 10:00 UTC et 2026-05-25 13:00 UTC)
- [WARNING] XLV (Healthcare) momentum 0.0 — headwind sectoriel
- Earnings J=0 non résolu (source FMP, date révisée au 2026-05-25)
- Accounting risk scan indisponible (`accounting_risk_latest.json` absent)
- Quant report indisponible (date 2026-05-17, insuffisant, 0 signaux)

---

*Rapport généré automatiquement — snapshot 2026-05-25 13:00 UTC.*
