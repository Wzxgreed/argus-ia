# CYTOMX — Mise à jour snapshot 2026-05-26 10:00 UTC

> **Date :** 2026-05-26
> **Type :** Update post-pipeline (snapshot 10:00 UTC)
> **Snapshot :** 10:00 UTC
> **Analyste :** Desk Argus-IA

---

## Récapitulatif des changements depuis l'analyse précédente

| Élément | Avant (snapshot 2026-05-25 21:00 UTC) | Maintenant (snapshot 2026-05-26 10:00 UTC) | Variation |
|---------|----------------------------------------|--------------------------------------------|-----------|
| Cours | [DONNÉES MANQUANTES] | [DONNÉES MANQUANTES] | — |
| RSI 14j | 50 (placeholder) | 50 (placeholder) | — |
| Volume | — | — | — |
| Score Opportunité | 5.5/10 | 5.5/10 | — |
| Score Global | 55.2/100 | 55.2/100 | — |
| Action | ATTENDRE | ATTENDRE | — |
| Earnings (FMP) | J=0 (2026-05-25) | J=0 (2026-05-26) | glissement +1j |
| Validation | [ERROR] fetch failed | [ERROR] fetch failed | inchangé |

**Observation principale :** Le snapshot 2026-05-26 10:00 UTC (post-Memorial Day) confirme la **stabilité totale** vs 2026-05-25 21:00 UTC. Aucune donnée de cours n'a été récupérée. L'erreur persistante `No price history` pour CYTOMX remonte désormais à **huit snapshots consécutifs** (2026-05-19 10:00/13:59/21:00 UTC, 2026-05-20 10:00 UTC, 2026-05-25 10:00/13:00/21:00 UTC, 2026-05-26 10:00 UTC).

**Découverte structurante :** une vérification manuelle via `yfinance` confirme que le ticker **CYTOMX n'existe pas** sur Yahoo Finance (HTTP 404 Not Found). Le ticker correct de CytomX Therapeutics, Inc. sur NASDAQ est **CTMX** (cours ~$3.76 au test). L'absence persistante de données sur huit snapshots n'est donc pas une suspension de cotation ni un délai post-earnings, mais une **anomalie structurelle de la watchlist**.

---

## Mise à jour technique

- **Cours :** [DONNÉES MANQUANTES] — `prices.CYTOMX.error=true`, raison `No price history`
- **RSI 14j :** 50 (placeholder agent recommandation) — [UNSOURCED] sans données réelles
- **ATR 14j :** [DONNÉES MANQUANTES]
- **MM 50j / 200j :** [DONNÉES MANQUANTES]
- **Volume relatif :** [DONNÉES MANQUANTES]

**Verdict timing :** INCONNU — absence totale de données de cours. Le marché US a rouvert ce jour (post-Memorial Day) ; le fait que CYTOMX reste sans cotation confirme l'invalidité du symbole.

---

## Mise à jour fondamentale

- **Données FMP :** [DONNÉES MANQUANTES] — aucun bloc `fmp_key_metrics`, `fmp_ratios` ou `fmp_consensus` pour CYTOMX dans `data/latest.json`
- **Filtre Qualité 6 critères :** impossible à calculer sans états financiers extraits du snapshot
- **Consensus analystes :** [DONNÉES MANQUANTES]
- **Multiples :** [DONNÉES MANQUANTES]

**Earnings J=0 :** la date FMP a glissé au **2026-05-26** (`upcoming_events_latest.json`, `days_until=0`, source `fmp`). C'est le **8e snapshot consécutif** sans données exploitables. Le glissement quotidien de la date earnings (2026-05-19 → 2026-05-20 → ... → 2026-05-26) est cohérent avec une date FMP auto-générée ou placeholder sur un ticker inexistant.

---

## Mise à jour sentiment / options / news

- **News :** aucune news significative détectée dans les flux unifiés du pipeline (snapshot 10:00 UTC) — `data/news_latest.json` ne mentionne pas CYTOMX
- **Options flow :** [DONNÉES MANQUANTES] — pas de données options pour CYTOMX
- **Social sentiment :** 0 mention, score 0/10, label "No data" (`social_sentiment_latest.json`) — pas de signal retail
- **Upgrades/downgrades :** aucun signal détecté
- **Activité inhabituelle :** non calculable sans volume ni cours

---

## Contexte sectoriel et macro

- **Sector rotation (snapshot 2026-05-26) :** CYTOMX non flaggé dans `sector_rotation_latest.json`. XLV (Healthcare) n'est pas mentionné spécifiquement pour ce ticker.
- **FX Exposure :** score 0.0, direction "neutral", 25% exposure generic, zéro impact calculé (`fx_exposure_latest.json`)
- **Geo risk :** CYTOMX non flaggé dans `geo_risk_latest.json`
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

**Note de fiabilité :** les scores proviennent de l'agent recommandation mais reposent sur des placeholders (RSI par défaut 50, scores médians) en l'absence de données réelles. La fiabilité est **nulle** et le scoring ne doit pas servir de base à une décision d'investissement. Le validation report (`data/validation_report.txt`) confirme l'erreur `[ERROR] CYTOMX: fetch failed — No price history`.

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

**Thèse : INVALIDÉE — ANOMALIE STRUCTURELLE**

CYTOMX n'a fait l'objet d'aucune analyse initiale (`_init.md`). Les données de cours sont indisponibles sur **huit snapshots consécutifs** (2026-05-19 10:00/13:59/21:00 UTC ; 2026-05-20 10:00 UTC ; 2026-05-25 10:00/13:00/21:00 UTC ; 2026-05-26 10:00 UTC). La vérification manuelle du symbole confirme que **CYTOMX n'existe pas sur Yahoo Finance** (HTTP 404) ; le ticker correct de CytomX Therapeutics sur NASDAQ est **CTMX**.

**Recommandation opérationnelle :**
1. **Corriger immédiatement** `config/watchlist.json` : remplacer `CYTOMX` par `CTMX`
2. **Lancer un fetch frais** pour `CTMX` via `scripts/fetch_prices.py --tickers CTMX`
3. **Vérifier** que `data/latest.json` contient bien les données `CTMX` (cours, RSI, ATR, FMP)
4. **Si OK** : lancer une analyse initiale complète (`CTMX_YYYY-MM-DD_init.md`) avec Filtre Qualité 6 critères, Market Researcher (TAM, peers, comps) et Earnings Reviewer
5. **Archiver** le dossier `Actions/CYTOMX/` ou le renommer en `Actions/CTMX/` après migration des fichiers historiques si nécessaire
6. Jusqu'à correction : le ticker est **hors périmètre** du scoring institutionnel

**Alertes actives :**
- 🔴 **[ANOMALIE STRUCTURELLE]** ticker CYTOMX inexistant sur Yahoo Finance — remplacer par CTMX
- [WARNING] Earnings J=0 non résolu (source FMP, date glissée au 2026-05-26)
- [WARNING] XLV (Healthcare) headwind sectoriel persistant (momentum nul, RS négative)
- Accounting risk scan indisponible (`accounting_risk_latest.json` absent)
- Quant report indisponible (date 2026-05-17, insuffisant, 0 signaux)

---

*Rapport généré automatiquement — snapshot 2026-05-26 10:00 UTC.*
