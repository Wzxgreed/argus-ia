# TEST — Mise à Jour Post-Session (2026-05-20)

> **Date :** 2026-05-20
> **Heure snapshot :** 13:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-20T13:00:02 UTC), `data/recommandations_latest.json`
> **Type :** Mise à jour quotidienne — snapshot 13:00 UTC vs snapshot 10:00 UTC précédent

---

## Résumé des Changements

| Métrique | Snapshot 10:00 UTC (2026-05-20) | Snapshot 13:00 UTC (2026-05-20) | Delta |
|----------|--------------------------------|--------------------------------|-------|
| Cours close | $44.185 | **$44.185** | **Inchangé** |
| Previous close | $44.713 | **$44.713** | **Inchangé** |
| Variation vs previous close | −1.18% | **−1.18%** | — |
| RSI 14j | 57.46 | **57.46** | — |
| ATR 14j | $1.25 | **$1.25** | — |
| MM 50j | $43.33 | **$43.33** | — |
| Volume | 2,500 (1.34×) | **2,500 (1.34×)** | — |
| Position vs MM50 | +1.85% | **+1.85%** | — |
| Score Opportunité (agent) | 6.0/10 | **6.0/10** | Inchangé |
| Score Global (agent) | 65.2/100 | **65.2/100** | Inchangé |
| Verdict agent reco | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| Timing | Favorable | **Favorable** | Confirmé |

**Observation clé :** Aucune variation de prix, de volume ni d'indicateur technique entre les snapshots 10:00 UTC et 13:00 UTC. Le cours reste figé à $44.185 avec un RSI stable à 57.46. Cette immobilité est cohérente avec la liquidité structurellement faible du titre (volume moyen 20j < 2K). Aucune nouvelle donnée fondamentale, comptable ni corporate n'est injectée dans le snapshot 13:00 UTC. L'événement earnings (source FMP, `days_until: 0`) reste non observable.

---

## Mise à Jour Technique

- **Cours :** $44.185 (open $43.57 / high $44.245 / low $43.16 / previous close $44.713)
- **Variation session :** −1.18% vs previous close
- **Range intraday :** $43.16–$44.245 (2.46%)
- **RSI 14j :** 57.46 — zone neutre favorable, inchangé depuis le snapshot 10:00 UTC
- **ATR 14j :** $1.25 — volatilité stable, pas de contraction ni d'expansion
- **MM 50j :** $43.33 — cours maintenu à +1.85% au-dessus
- **MM 200j :** N/A
- **Volume relatif :** 1.34× moyenne 20j (2,500 vs 1,860) — soutien acheteur confirmé, stable
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette, +9.6% du 52W low

**Verdict timing :** Favorable. La configuration technique reste intacte : cours au-dessus de la MM50, RSI dans la zone neutre favorable proche de 60, volume au-dessus de la moyenne. Le non-mouvement entre 10h et 13h UTC n'invalide pas le setup ; il confirme la consolidation autour de $44.18 après le rebond du matin (low $43.16). La configuration en marteau inversé du snapshot matinal se maintient.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 13:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Validation données :** TEST non listé dans les [ERROR] ni [WARNING] du rapport de validation (22/25 OK)

**Earnings JOUR J (2026-05-20) :** `data/upcoming_events_latest.json` flague un earnings pour TEST avec `days_until: 0`. Aucun résultat post-earnings n'est injecté dans `latest.json` à 13:00 UTC. L'événement earnings (source FMP) reste non observable. Le mouvement intraday (−1.18% vs previous close) est purement technique / microstructurel sur faible liquidité.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail (inchangé) |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles (`options: {}`) |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism |
| **Geo Risk** | Non flaggé | Score politique non spécifique pour TEST |
| **FX Exposure** | Exposition 25%, impact 0%, divergence alignée | DXY neutre, pas de headwind/tailwind |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-20 — days_until 0 | JOUR J — résultats toujours non observables |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation purement technique.

---

## Scoring Global (Agent Recommandation)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 7.0/10 | 25% | 1.75 |
| **Score Opportunité** | **6.0/10** | — | **6.03** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (n = 0) |
| Bonus / Timing | +5.2 | Cours au-dessus MM50 + volume > moyenne + timing Favorable |
| **Score Global ajusté** | **65.2/100** | **ACHETER (Réduit)** |

**Proximité des seuils :** À 65.2/100, TEST reste dans la zone ACHETER réduit (60–74). Aucun changement de score depuis le snapshot 10:00 UTC. Le Score Opportunité à 6.0/10 franchit le seuil d'entrée minimal. Le momentum à 7.0/10 reste le pilier haussier du scoring.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 13:00 UTC (cours $44.19, ATR $1.25) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.19 | Snapshot 13:00 UTC |
| Stop-loss suggéré (2×ATR) | **$41.69** | −5.75% sous le cours |
| Take-profit suggéré (3×ATR) | **$47.94** | +8.50% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.33 (−1.95%) — support dynamique, inchangé
- **Support gap / low 19/05 :** $43.395 (−1.80%) — non cassé en clôture
- **Support intraday :** $43.16 (−2.30%) — low du jour, à surveiller si cassé en clôture
- **Résistance previous close :** $44.713 (+1.19%) — combler le gap-down matinal
- **Résistance 52W high :** $57.74 (+30.66%)
- **Support 52W low :** $40.27 (−8.87%) — dernier niveau de défense

**Note :** Le stop-loss à $41.69 se situe au-dessus du 52W low ($40.27) et sous le support gap ($43.395). Une cassure de $43.16 en clôture invaliderait le rebond technique et justifierait un retrait vers SURVEILLER.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse CONFIRMÉE. Aucun changement entre les snapshots 10:00 UTC et 13:00 UTC 2026-05-20.**

Le snapshot 13:00 UTC confirme la stabilité technique autour de $44.19 établie au snapshot 10:00 UTC :
- **Cours inchangé** à $44.185 — consolidation sans repli
- **RSI stable** à 57.46 — momentum haussier intact, pas de surachat
- **MM50 stable** à $43.33 — cours maintenu à +1.85% au-dessus
- **Volume stable** à 2,500 (1.34× moyenne 20j) — soutien acheteur confirmé

**Trois facteurs de prudence inchangés :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle faible** — volume moyen 20j < 2K actions, spread et slippage élevés
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils tolérants au risque. Le timing Favorable et le maintien au-dessus de la MM50 offrent un setup technique court terme.
- **Seuil de confirmation :** Clôture au-dessus de $44.71 (previous close / combler le gap) avec volume > 2,500
- **Seuil d'invalidation :** Retour sous $43.33 (MM50) ou cassure de $43.16 (low intraday) en clôture → revenir SURVEILLER
- **Sizing :** Réduit (max 5% du capital) en raison de la liquidité limitée et de l'absence de fondamentaux

**Earnings JOUR J** : Les résultats restent non observables à 13:00 UTC. Sur publication post-marché, générer immédiatement un `_earnings.md` flash si les données FMP/Yahoo sont injectées.

**Niveau de confiance :** Faible — l'analyse repose sur des proxies et des valeurs par défaut. La volatilité sur faible liquidité amplifie le risque de faux signaux. Le rebond technique est validé mais fragile. Aucun catalyseur fondamental n'est visible.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 13:00 UTC. Données : `data/latest.json`, `data/recommandations_latest.json`, `data/validation_report.txt`.*
