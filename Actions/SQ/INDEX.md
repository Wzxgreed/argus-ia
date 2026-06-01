# SQ — Block, Inc.

## Thèse courante

**ATTENDRE** (2026-06-01 · snapshot 13:00 UTC) — Qualité opérationnelle classée **hors périmètre (3/6)** après injection FMP FY 2025-12-31 : bilan structurellement négatif (tangible asset value −$32.5B, current ratio −0.18), rentabilité GAAP inexistante (ROIC −12.8%, net margin ~0%), et dilution SBC à 5% des revenus. La valorisation reflète cette dégradation (EV/EBITDA 18.2x, P/S 1.45x) sans marge de sécurité. Le timing est bloqué par l'**anomalie de données critique** : **cours figé $83.46 sur ≥25 snapshots consécutifs couvrant ≥12 jours calendaires** (20/05 → 01/06) et **earnings placeholder glissant depuis 12+ jours** (date initialement prévue 20/05). SQ est le **dernier ticker** du snapshot 01/06 avec `source: fmp_fallback` et `change_pct: null`. Le consensus sell-side est **figé à $85.67** (3 analystes, upside +2.6%) — silence institutionnel complet depuis le 27/05. Le quality gate du 01/06 éclate : **23/24 tickers excluded** (CRITICAL stale price 4j) — SQ n'est plus isolé mais reste le cas le plus ancien et le plus sévère. `validation_report.txt` (12:07 UTC) affiche 5 [ERROR] (>2) et continue de signaler `0 excluded by quality gate`, divergence persistante. Un signal **`ROTATION_TO_DEFENSIVE`** est détecté dans `sector_rotation_2026-06-01.json` (crossover bearish XLE) — vent contraire pour les multiples growth si confirmé post-session. Tout positionnement avant résolution du stale price est déconseillé. Priorité opérationnelle : vérifier cours live via broker, date réelle de publication Q1 2026, forcer re-fetch isolé de SQ. Risque de gap violent (±10–15%) à la réouverture d'un cours live maximal.

---

## Historique des analyses

| Date | Fichier | Type | Conclusion |
|------|---------|------|------------|
| 2026-06-01 | [SQ_2026-06-01_update.md](SQ_2026-06-01_update.md) | Mise à jour snapshot **13:00 UTC** post-session US | **ATTENDRE** — Qualité 3/6, **stale price ≥25 snapshots / 12+ jours**, earnings placeholder **glissant 12+ jours**, consensus PT **figé** $85.67 (3 analystes), signal `ROTATION_TO_DEFENSIVE` sectoriel, **quality gate eruption** (23/24 excluded), 5 [ERROR] validation (>2), divergence gate/validation persistante, **zero changement données brutes SQ vs 10:00 UTC**, scoring agent reco révisé 5.8/10 (non plafonné) vs 5.4/10 institutionnel |
| 2026-06-01 | [SQ_2026-06-01_update.md](SQ_2026-06-01_update.md) *(archive 10:00 UTC)* | Mise à jour snapshot **10:00 UTC** | **ATTENDRE** — Qualité 3/6, **stale price ≥23 snapshots / 12+ jours**, earnings placeholder **glissant 12+ jours**, consensus PT **figé** $85.67 (3 analystes), signal `ROTATION_TO_DEFENSIVE` sectoriel, **quality gate eruption** (23/24 excluded), 5 [ERROR] validation (>2), divergence gate/validation persistante, zero changement données SQ vs 27/05 |
| 2026-05-27 | [SQ_2026-05-27_update.md](SQ_2026-05-27_update.md) | Mise à jour snapshot **17:00 UTC** | **ATTENDRE** — Qualité 3/6, earnings **non résolu après 8 jours**, **stale price 19 snapshots / 8 jours calendaires**, consensus PT **révisé à la baisse** $87.50→$85.67 (+1 analyste), 4 [ERROR] dans validation (>2), SPCX retiré de l'exclusion, SQ seul ticker excluded |
| 2026-05-27 | [SQ_2026-05-27_update.md](SQ_2026-05-27_update.md) *(archive 13:00 UTC)* | Mise à jour snapshot 13:00 UTC | **ATTENDRE** — Qualité 3/6, earnings **non résolu après 8 jours**, **stale price 18 snapshots / 8 jours calendaires**, 4 [ERROR] dans validation (>2), SPCX retiré de l'exclusion, SQ seul ticker excluded, zero changement vs 10:00 UTC |
| 2026-05-27 | [SQ_2026-05-27_update.md](SQ_2026-05-27_update.md) *(archive 10:00 UTC)* | Mise à jour snapshot 10:00 UTC pré-marché US | **ATTENDRE** — Qualité 3/6, earnings **non résolu après 8 jours**, **stale price 17 snapshots / 8 jours calendaires (quality gate excluded — SQ seul ticker excluded ce jour)**, SPCX retiré de l'exclusion, zero changement vs 26/05 21:00 UTC |
| 2026-05-26 | [SQ_2026-05-26_update.md](SQ_2026-05-26_update.md) | Mise à jour snapshot **21:00 UTC** post-session US | **ATTENDRE** — Qualité 3/6, earnings **non résolu après 7 jours**, **stale price 16 snapshots / 7 jours calendaires (quality gate excluded officiellement)**, SQ et SPCX excluded, pipeline partial, zero changement vs 17:00 UTC |
| 2026-05-26 | [SQ_2026-05-26_update.md](SQ_2026-05-26_update.md) *(archive 17:00 UTC)* | Mise à jour snapshot 17:00 UTC | **ATTENDRE** — Qualité 3/6, earnings non résolu après 7 jours, stale price 15 snapshots / 7 jours calendaires, zero changement vs 13:00 UTC |
| 2026-05-25 | [SQ_2026-05-25_update.md](SQ_2026-05-25_update.md) | Mise à jour snapshot **21:00 UTC** | **ATTENDRE** — Qualité 3/6, earnings J=0 **non résolu après 5 jours**, **stale price 12 snapshots / 5 jours calendaires (quality gate excluded)**, Memorial Day (marché fermé) n'explique pas le stale price depuis le 20/05, pipeline partial, zero changement vs snapshot 17:00 UTC |
| 2026-05-25 | [SQ_2026-05-25_update.md](SQ_2026-05-25_update.md) *(archive 17:00 UTC)* | Mise à jour snapshot 17:00 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0 **non résolu après 5 jours**, **stale price 11 snapshots / 5 jours calendaires (quality gate excluded)**, zero changement vs snapshot 13:00 UTC |
| 2026-05-25 | [SQ_2026-05-25_update.md](SQ_2026-05-25_update.md) *(archive 13:00 UTC)* | Mise à jour snapshot 13:00 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0 non résolu après 5 jours, stale price 10 snapshots / 5 jours calendaires (quality gate excluded), zero changement vs snapshot matinal 10:00 UTC |
| 2026-05-25 | [SQ_2026-05-25_update.md](SQ_2026-05-25_update.md) *(archive 10:00 UTC)* | Mise à jour snapshot matinal | **ATTENDRE** — Qualité 3/6, earnings J=0 non résolu après 5 jours, stale price 9 snapshots / 5 jours calendaires (quality gate excluded), zero changement vs 20/05 13:00 UTC |
| 2026-05-20 | [SQ_2026-05-20_update.md](SQ_2026-05-20_update.md) | Mise à jour snapshot 13:00 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0, **stale price ≥4 jours (quality gate excluded)**, zero changement vs snapshot matinal |
| 2026-05-20 | [SQ_2026-05-20_update.md](SQ_2026-05-20_update.md) *(archive 10:00 UTC)* | Mise à jour snapshot matinal | **ATTENDRE** — Qualité 3/6, earnings J=0, stale price ≥4 jours, zero changement vs 19/05 21:00 UTC |
| 2026-05-20 | [SQ_2026-05-20_preview.md](SQ_2026-05-20_preview.md) | Preview earnings | Scénarios pré-earnings (beat/in-line/miss) — prédictions non renseignées |
| 2026-05-19 | [SQ_2026-05-19_update.md](SQ_2026-05-19_update.md) | Mise à jour snapshot 21:00 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0, stale price ≥3 jours, zero changement vs 17:00 UTC |
| 2026-05-19 | [SQ_2026-05-19_preview.md](SQ_2026-05-19_preview.md) | Preview earnings | Scénarios pré-earnings (beat/in-line/miss) — prédictions non renseignées |
| 2026-05-19 | [SQ_2026-05-19_update.md](SQ_2026-05-19_update.md) *(archive 17:00 UTC)* | Mise à jour snapshot 17:00 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0, stale price 3 jours, données inchangées vs 13:00 UTC |
| 2026-05-19 | [SQ_2026-05-19_update.md](SQ_2026-05-19_update.md) *(archive 13:00 UTC)* | Mise à jour snapshot 13:00 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0, stale price, données inchangées vs 10:00 UTC |
| 2026-05-19 | [SQ_2026-05-19_update.md](SQ_2026-05-19_update.md) *(archive 10:00 UTC)* | Mise à jour snapshot 10:00 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0, données inchangées vs 18/05 |
| 2026-05-18 | [SQ_2026-05-18_update.md](SQ_2026-05-18_update.md) | Mise à jour post-pipeline 22:35 UTC | **ATTENDRE** — Qualité 3/6, earnings J=0, snapshot 22:35 UTC inchangé vs 21:00 UTC |
| 2026-05-18 | [SQ_2026-05-18_preview.md](SQ_2026-05-18_preview.md) | Preview earnings | Scénarios pré-earnings (beat/in-line/miss) |
| 2026-05-17 | [SQ_2026-05-17_init.md](SQ_2026-05-17_init.md) | Analyse initiale (auto) | SURVEILLER — thèse structurelle bullish, qualité partielle 4/6, données absentes |

---

## Agenda

- **2026-05-20 (initialement prévu)** · 🔴 **Earnings Q1 2026** — résultats **toujours non intégrés** dans le snapshot 01/06 (**12+ jours après date prévue**). `upcoming_events_2026-06-01.json` affiche `"date": "2026-06-01"` avec `"days_until": 0`, mais le champ `"details": "Earnings "` est vide, et ce pattern est identique pour TEST, FUBO, AST, AXA, SPCX, QTBS, ASTSPACE (7 autres tickers), suggérant un placeholder FMP générique.
- **Action opérationnelle urgente :** Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR. Forcer re-fetch isolé de SQ (`scripts/fetch_prices.py --tickers SQ`) pour diagnostiquer l'échec spécifique du worker daemon.
- Post-earnings : réviser le Filtre Qualité, le scoring, et le timing technique dès disponibilité des données RSI/ATR/MM **non stale**
- Vérifier résolution du stale price dans le prochain snapshot (risque de gap violent ±10–15% à réouverture)

---

## Alertes actives

- 🔴 **Quality Gate Exclusion aggravée** — stale price ≥23 snapshots / ≥12 jours calendaires (2026-05-20 → 2026-06-01). SQ est désormais **l'un de 23 tickers excluded** par `quality_gate_2026-06-01.json` (CRITICAL stale 4j), mais reste le cas le plus ancien et le plus sévère.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **12+ jours calendaires** (date initiale 20/05). `upcoming_events_2026-06-01.json` affiche `days_until: 0` avec date 01/06 (glissement depuis 20/05), mais champ details vide (placeholder FMP générique).
- 🔴 **Source FMP Fallback** — SQ est le **dernier ticker** du snapshot 01/06 avec `"fmp_fallback"` et `change_pct: null` (23/24 autres tickers OK via yahoo_worker_daemon).
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🟡 **Validation Divergence systémique** — `validation_report.txt` (09:07 UTC) indique `0 excluded by quality gate` alors que **23 tickers** sont réellement excluded. Divergence persistante et aggravée.
- 🔴 **Pipeline Degradation** — `validation_report.txt` affiche **5 [ERROR]** (VRT schema, AST/AXA/QTBS/ASTSPACE fetch) — seuil >2 franchi.
- 🟡 **Rotation Défensive** — Signal `ROTATION_TO_DEFENSIVE` détecté dans `sector_rotation_2026-06-01.json` (crossover bearish XLE). Vent contraire pour les multiples growth si confirmé post-session.
- Aucune alerte de seuil de cours déclenchée

---

## Contexte macro & secteur

- **Rotation sectorielle :** XLK (Technology) top3 sectoriel avec momentum score 10.0 — vent favorable pour SQ, **mais signal `ROTATION_TO_DEFENSIVE` détecté** (crossover bearish XLE). Vent contraire potentiel pour les multiples growth.
- **Régime macro :** Normal (pondération 35/40/25) — `regime_macro` affiché `"Unknown"` dans `recommandations_2026-06-01.json` (dégradation vs 27/05)
- **Exposition :** Haute sensibilité taux, modérée DXY (25% export), corrélation crypto historique élevée
- **FX Exposure :** Score 0.0, direction neutral (🟢)
- **Geo Risk :** Non flaggué, score politique 2/10 (🟢)

---

*Dernière mise à jour : 2026-06-01 · Snapshot 10:00 UTC*
