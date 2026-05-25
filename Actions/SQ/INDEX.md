# SQ — Block, Inc.

## Thèse courante

**ATTENDRE** (2026-05-25 · snapshot 21:00 UTC) — Qualité opérationnelle classée **hors périmètre (3/6)** après injection FMP FY 2025-12-31 : bilan structurellement négatif (tangible asset value −$32.5B, current ratio −0.18), rentabilité GAAP inexistante (ROIC −12.8%, net margin ~0%), et dilution SBC à 5% des revenus. La valorisation reflète cette dégradation (EV/EBITDA 18.2x, P/S 1.45x) sans marge de sécurité. Le timing est bloqué par l'**anomalie de données critique** : **cours figé $83.46 sur 12 snapshots consécutifs couvrant 5 jours calendaires** (20/05 → 25/05) et **earnings Q1 2026 J=0 non résolu après 5 jours**. Le marché US était fermé ce jour (Memorial Day), ce qui explique mécaniquement l'absence de nouveau close le 25/05, mais ne justifie pas le stale price depuis le 20/05. **🔴 SQ est le seul ticker de la watchlist avec un cours stale sur 12 snapshots consécutifs** — source `"fmp_fallback"` vs `"yahoo_worker_daemon"` pour tous les autres tickers. Le fichier `recommandations_latest.json` affiche un RSI placeholder 50 mais le bloc `technical` est vide. Le secteur Technology bénéficie d'une rotation favorable (XLK top3), mais cela ne compense pas la fragilité fondamentale ni l'anomalie de données. Le pipeline du 25/05 a généré un statut **partial** (phases C/D failed, validate + detect_major_events failed), ce qui peut impacter la fraîcheur de certaines métriques agrégées. Tout positionnement avant résolution du stale price et intégration des résultats Q1 est déconseillé. Priorité opérationnelle : vérifier cours live via broker et date réelle de publication des résultats.

---

## Historique des analyses

| Date | Fichier | Type | Conclusion |
|------|---------|------|------------|
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

- **2026-05-20** · 🔴 **Earnings Q1 2026** — J=0, résultats **toujours non intégrés** dans le snapshot 25/05 (5 jours après date prévue)
- **Action opérationnelle urgente :** Vérifier date réelle de publication Q1 2026 via site IR Block / SEC EDGAR. Forcer re-fetch si résultats déjà publiés.
- Post-earnings : réviser le Filtre Qualité, le scoring, et le timing technique dès disponibilité des données RSI/ATR/MM **non stale**
- Vérifier résolution du stale price dans le prochain snapshot (marché réouvert mardi 26/05)

---

## Alertes actives

- 🔴 **Quality Gate Exclusion** — stale price 12 snapshots / ≥5 jours calendaires (2026-05-20 → 2026-05-25)
- 🔴 **Data Pipeline Alert** — Earnings Q1 2026 J=0 non résolu après 5 jours calendaires (`upcoming_events_2026-05-25.json` confirme `days_until: 0`)
- 🔴 **Source FMP Fallback** — SQ est le seul ticker du snapshot 25/05 avec `"fmp_fallback"` et `change_pct: null`
- 🟡 **Pipeline Partial** — Phases C/D failed (validate + detect_major_events) le 25/05 ; agent accounting skipped
- Aucune alerte de seuil de cours déclenchée

---

## Contexte macro & secteur

- **Rotation sectorielle :** XLK (Technology) top3 sectoriel avec momentum score 10.0 — vent favorable pour SQ
- **Régime macro :** Normal (pondération 35/40/25)
- **Exposition :** Haute sensibilité taux, modérée DXY (25% export), corrélation crypto historique élevée
- **FX Exposure :** Score 0.0, direction neutral (🟢)
- **Geo Risk :** Non flaggué, score politique 2/10 (🟢)

---

*Dernière mise à jour : 2026-05-25 · Snapshot 21:00 UTC*
