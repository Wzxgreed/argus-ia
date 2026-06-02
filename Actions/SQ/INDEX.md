# SQ — Block, Inc.

## Thèse courante

**ATTENDRE** (2026-06-02 · snapshot 21:00 UTC) — Qualité opérationnelle classée **hors périmètre (3/6)** après injection FMP FY 2025-12-31 : bilan structurellement négatif (tangible asset value −$32.5B, current ratio −0.18), rentabilité GAAP inexistante (ROIC −12.8%, net margin ~0%), et dilution SBC à 5% des revenus. La valorisation reflète cette dégradation (EV/EBITDA 18.2x, P/S 1.45x) sans marge de sécurité. Le timing est bloqué par l'**anomalie de données critique** : **cours figé $83.46 sur ≥30 snapshots consécutifs couvrant ≥13 jours calendaires** (20/05 → 02/06) et **earnings placeholder glissant depuis 13+ jours** (date initialement prévue 20/05, glissée au 02/06). SQ est le **dernier ticker** du snapshot 02/06 avec `source: fmp_fallback` et `change_pct: null`. Le consensus sell-side est **figé à $85.67** (3 analystes, upside +2.6%) — silence institutionnel complet depuis le 27/05. Le quality gate du 02/06 affiche `0 excluded by quality gate` (validation 20:07 UTC) mais le stale price SQ reste le cas le plus ancien et le plus sévère. Le signal sectoriel reste **`NEUTRAL`** (`data/sector_rotation_2026-06-02.json`, XLK top3 mais crossovers vides) — le signal `ROTATION_TO_CYCLICAL` détecté au snapshot 13h reste **neutralisé**. Ce contexte sectoriel reste globalement favorable pour SQ mais **ne compense pas** le stale price, la qualité hors périmètre, et le silence informationnel. Tout positionnement avant résolution du stale price est déconseillé. Priorité opérationnelle : vérifier cours live via broker, date réelle de publication Q1 2026, forcer re-fetch isolé de SQ. Risque de gap violent (±10–15%) à la réouverture d'un cours live maximal.

---

## Historique des analyses

| Date | Fichier | Type | Conclusion |
|------|---------|------|------------|
| 2026-06-02 | [SQ_2026-06-02_update.md](SQ_2026-06-02_update.md) | Mise à jour snapshot **21:00 UTC** post-session US + after-hours | **ATTENDRE** — Qualité 3/6, **stale price ≥30 snapshots / ≥13 jours**, earnings placeholder **glissant 13+ jours** (date glissée au 02/06), consensus PT **figé** $85.67 (3 analystes), signal sectoriel **`NEUTRAL`** stable, **zero mutation données brutes SQ vs 17:00 UTC**, scoring inchangé 5.4/10 institutionnel, Score Global Ajusté **~59.0**, validation **6 [ERROR]** |
| 2026-06-02 | [SQ_2026-06-02_update.md](SQ_2026-06-02_update.md) *(archive 17:00 UTC)* | Mise à jour snapshot **17:00 UTC** | **ATTENDRE** — Qualité 3/6, **stale price ≥29 snapshots / ≥13 jours**, earnings placeholder **glissant 13+ jours** (date glissée au 02/06), consensus PT **figé** $85.67 (3 analystes), signal sectoriel **`NEUTRAL`** (was `ROTATION_TO_CYCLICAL` au snapshot 13h), **zero mutation données brutes SQ vs 13:00 UTC**, scoring inchangé 5.4/10 institutionnel, Score Global Ajusté révisé **~59.0** (vs ~61.0 au snapshot 13h), validation **6 [ERROR]** |
| 2026-06-02 | [SQ_2026-06-02_update.md](SQ_2026-06-02_update.md) *(archive 13:00 UTC)* | Mise à jour snapshot **13:00 UTC** | **ATTENDRE** — Qualité 3/6, **stale price ≥28 snapshots / ≥13 jours**, earnings placeholder **glissant 13+ jours** (date glissée au 02/06), consensus PT **figé** $85.67 (3 analystes), signal `ROTATION_TO_CYCLICAL` **stable**, **zero mutation données brutes SQ vs 21:00 UTC 01/06**, scoring inchangé 5.4/10 institutionnel |
| 2026-06-01 | [SQ_2026-06-01_update.md](SQ_2026-06-01_update.md) | Mise à jour snapshot **21:00 UTC** post-session US + after-hours | **ATTENDRE** — Qualité 3/6, **stale price ≥27 snapshots / 12+ jours**, earnings placeholder **glissant 12+ jours**, consensus PT **figé** $85.67 (3 analystes), signal `ROTATION_TO_CYCLICAL` **stable**, **zero mutation données brutes SQ vs 17:00 UTC**, correction factuelle : aucun `quality_gate_2026-06-01.json` n'existe (validation 20:07 UTC confirme 0 excluded), scoring inchangé 5.4/10 institutionnel |
| 2026-06-01 | [SQ_2026-06-01_update.md](SQ_2026-06-01_update.md) *(archive 17:00 UTC)* | Mise à jour snapshot **17:00 UTC** post-session US | **ATTENDRE** — Qualité 3/6, **stale price ≥26 snapshots / 12+ jours**, earnings placeholder **glissant 12+ jours**, consensus PT **figé** $85.67 (3 analystes), signal sectoriel **bascoulé `ROTATION_TO_CYCLICAL`** (was défensive), mention erronée quality gate eruption (corrigée au snapshot 21h), 5 [ERROR] validation (>2), divergence gate/validation persistante, **zero changement données brutes SQ vs 13:00 UTC**, scoring inchangé 5.4/10 institutionnel |
| 2026-06-01 | [SQ_2026-06-01_update.md](SQ_2026-06-01_update.md) *(archive 13:00 UTC)* | Mise à jour snapshot **13:00 UTC** post-session US | **ATTENDRE** — Qualité 3/6, **stale price ≥25 snapshots / 12+ jours**, earnings placeholder **glissant 12+ jours**, consensus PT **figé** $85.67 (3 analystes), signal `ROTATION_TO_DEFENSIVE` sectoriel, **quality gate eruption** (23/24 excluded), 5 [ERROR] validation (>2), divergence gate/validation persistante, **zero changement données brutes SQ vs 10:00 UTC**, scoring agent reco révisé 5.8/10 (non plafonné) vs 5.4/10 institutionnel |
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

- **2026-05-20 (initialement prévu)** · 🔴 **Earnings Q1 2026** — résultats **toujours non intégrés** dans le snapshot 02/06 (**13+ jours après date prévue**). `upcoming_events_2026-06-02.json` affiche `"date": "2026-06-02"` avec `"days_until": 0`, mais le champ `"details": "Earnings "` est vide, et ce pattern est identique pour TEST, FUBO, AST, AXA, SPCX, QTBS, ASTSPACE (7 autres tickers), suggérant un placeholder FMP générique.
- **Action opérationnelle urgente :** Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR. Forcer re-fetch isolé de SQ (`scripts/fetch_prices.py --tickers SQ`) pour diagnostiquer l'échec spécifique du worker daemon.
- Post-earnings : réviser le Filtre Qualité, le scoring, et le timing technique dès disponibilité des données RSI/ATR/MM **non stale**
- Vérifier résolution du stale price dans le prochain snapshot (risque de gap violent ±10–15% à réouverture)

---

## Alertes actives

- 🔴 **Stale Price aggravé** — cours figé ≥29 snapshots / ≥13 jours calendaires (2026-05-20 → 2026-06-02). SQ est le cas le plus ancien et le plus sévère de stale price dans le snapshot.
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 non résolu après **13+ jours calendaires** (date initiale 20/05). `upcoming_events_2026-06-02.json` affiche `days_until: 0` avec date 02/06 (glissement depuis 20/05), mais champ details vide (placeholder FMP générique).
- 🔴 **Source FMP Fallback** — SQ est le **dernier ticker** du snapshot 02/06 avec `"fmp_fallback"` et `change_pct: null`.
- 🟡 **Consensus PT Figé** — Price target consensus **$85.67** (3 analystes) inchangé depuis le 27/05. Silence sell-side prolongé ; upside +2.6% quasi-insuffisant.
- 🔴 **Pipeline Degradation** — `validation_report.txt` (16:07 UTC) affiche **6 [ERROR]** (VRT schema + AST/AXA/SPCX/QTBS/ASTSPACE fetch) — seuil >2 franchi, aggravation vs 5 errors à 12:07 UTC.
- 🟡 **Rotation Sectorielle Neutralisée** — XLK (Technology) reste top3 sectoriel avec momentum score 10.0, mais le signal global est passé de **`ROTATION_TO_CYCLICAL`** (snapshot 13h) à **`NEUTRAL`** (snapshot 17h, crossovers vides). Vent favorable growth/tech atténué.
- Aucune alerte de seuil de cours déclenchée

---

## Contexte macro & secteur

- **Rotation sectorielle :** XLK (Technology) top3 sectoriel avec momentum score 10.0 — vent favorable pour SQ, **mais signal global `NEUTRAL`** (crossovers vides). Le signal `ROTATION_TO_CYCLICAL` détecté au snapshot 13h est **neutralisé**.
- **Régime macro :** Normal (pondération 35/40/25) — `regime_macro` affiché `"Unknown"` dans `recommandations_2026-06-02.json` (dégradation vs 27/05)
- **Exposition :** Haute sensibilité taux, modérée DXY (25% export), corrélation crypto historique élevée
- **FX Exposure :** Score 0.0, direction neutral (🟢)
- **Geo Risk :** Non flaggué, score politique 2/10 (🟢)

---

*Dernière mise à jour : 2026-06-02 · Snapshot 21:00 UTC*
