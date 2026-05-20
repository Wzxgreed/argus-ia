# TEST — Mise à Jour Post-Session (2026-05-20)

> **Date :** 2026-05-20
> **Heure snapshot :** 10:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-20T10:00:11 UTC), `data/recommandations_latest.json`
> **Type :** Mise à jour quotidienne — snapshot 10:00 UTC vs snapshot 21:00 UTC précédent

---

## Résumé des Changements

| Métrique | Snapshot 21:00 UTC (2026-05-19) | Snapshot 10:00 UTC (2026-05-20) | Delta |
|----------|--------------------------------|--------------------------------|-------|
| Cours close | $44.185 | **$44.185** | **Inchangé** |
| Previous close | $44.935 | **$44.713** | — |
| Variation vs previous close | −1.67% | **−1.18%** | **+0.49 pt** |
| RSI 14j | 56.47 | **57.46** | **+0.99 pt** |
| ATR 14j | $1.27 | **$1.25** | −$0.02 |
| MM 50j | $43.54 | **$43.33** | −$0.21 |
| Volume | 2,448 (1.32×) | **2,500 (1.34×)** | **+52 (+2.1%)** |
| Position vs MM50 | +1.48% | **+1.85%** | **+0.37 pt** |
| Score Opportunité (agent) | 6.0/10 | **6.0/10** | Inchangé |
| Score Global (agent) | 65.2/100 | **65.2/100** | Inchangé |
| Verdict agent reco | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| Timing | Favorable | **Favorable** | Confirmé |

**Observation clé :** Le cours a ouvert à $43.57, creusé un low à $43.16 (−2.3% vs close), puis rebondi pour clôturer à $44.185 — inchangé en valeur absolue par rapport au snapshot 21:00 UTC précédent. Le RSI a continué de monter (+0.99 pt) vers 57.46, renforçant la zone neutre favorable. La MM50 a reculé de $43.54 à $43.33, ce qui élargit la marge au-dessus de la moyenne mobile (+1.85% vs +1.48%). Le volume reste au-dessus de la moyenne 20j (1.34×), confirmant un intérêt acheteur soutenu malgré la liquidité structurellement faible. Aucune nouvelle donnée fondamentale ou comptable n'est injectée dans le snapshot.

---

## Mise à Jour Technique

- **Cours :** $44.185 (open $43.57 / high $44.245 / low $43.16 / previous close $44.713)
- **Variation session :** −1.18% vs previous close
- **Range intraday :** $43.16–$44.245 (2.46%)
- **RSI 14j :** 57.46 — zone neutre favorable, progression continue depuis 53.18 (snapshot 17:00 UTC 2026-05-19)
- **ATR 14j :** $1.25 — légère contraction de $0.02, volatilité stable
- **MM 50j :** $43.33 — recul de $0.21, cours désormais +1.85% au-dessus
- **MM 200j :** N/A
- **Volume relatif :** 1.34× moyenne 20j (2,500 vs 1,860) — soutien acheteur confirmé pour le 2e snapshot consécutif
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette, +9.6% du 52W low

**Verdict timing :** Favorable. Le cours a testé le support gap ($43.395) sans le casser en clôture (low $43.16, close $44.185). La configuration en marteau inversé se confirme sur un 2e snapshot : ouverture basse, creusement de plus bas intraday, puis rebond pour clôturer proche du high. Le RSI progresse doucement vers 60 sans signal de surachat. La MM50 recule mais le cours s'en éloigne positivement, ce qui renforce le signal de court terme.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 10:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Validation données :** TEST non listé dans les [ERROR] ni [WARNING] du rapport de validation (22/25 OK)

**Earnings JOUR J (2026-05-20) :** `data/upcoming_events_latest.json` flague un earnings pour TEST avec `days_until: 0`. Aucun résultat post-earnings n'est injecté dans `latest.json` à 10:00 UTC. L'événement earnings (source FMP) reste non observable. Le mouvement intraday (−1.18% vs previous close) est purement technique / microstructurel sur faible liquidité.

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

**Proximité des seuils :** À 65.2/100, TEST reste dans la zone ACHETER réduit (60–74). Aucun changement de score depuis le snapshot 21:00 UTC. Le Score Opportunité à 6.0/10 franchit le seuil d'entrée minimal. Le momentum à 7.0/10 reste le pilier haussier du scoring.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 10:00 UTC (cours $44.19, ATR $1.25) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.19 | Snapshot 10:00 UTC |
| Stop-loss suggéré (2×ATR) | **$41.69** | −5.75% sous le cours |
| Take-profit suggéré (3×ATR) | **$47.94** | +8.50% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.33 (−1.95%) — support dynamique, marge élargie par rapport à hier
- **Support gap / low 19/05 :** $43.395 (−1.80%) — low de 17:00 UTC 2026-05-19, non cassé en clôture (low $43.16, close $44.185)
- **Support intraday :** $43.16 (−2.30%) — low du jour, à surveiller si cassé en clôture
- **Résistance previous close :** $44.713 (+1.19%) — combler le gap-down matinal
- **Résistance 52W high :** $57.74 (+30.66%)
- **Support 52W low :** $40.27 (−8.87%) — dernier niveau de défense

**Note :** Le stop-loss à $41.69 se situe au-dessus du 52W low ($40.27) et sous le support gap ($43.395). Une cassure de $43.16 en clôture invaliderait le rebond technique et justifierait un retrait vers SURVEILLER.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse CONFIRMÉE. Aucun changement de fond par rapport au snapshot 21:00 UTC 2026-05-19.**

Le snapshot 10:00 UTC 2026-05-20 révèle une stabilité technique autour de $44.19 avec des améliorations sous-jacentes :
- **Cours inchangé** en clôture ($44.185) mais avec un range intraday de 2.46% — le titre a digéré la baisse du matin et rebondi
- **RSI progresse** de 56.47 à 57.46 — momentum haussier intact, pas de surachat
- **MM50 recule** à $43.33 mais le cours s'en éloigne positivement (+1.85%) — élargissement du buffer technique
- **Volume soutenu** à 2,500 (1.34× moyenne 20j) — 2e snapshot consécutif au-dessus de la moyenne, signal d'intérêt acheteur

**Trois facteurs de prudence inchangés :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle faible** — volume moyen 20j < 2K actions, spread et slippage élevés
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils tolérants au risque. Le timing Favorable et le maintien au-dessus de la MM50 offrent un setup technique court terme.
- **Seuil de confirmation :** Clôture au-dessus de $44.71 (previous close / combler le gap) avec volume > 2,500
- **Seuil d'invalidation :** Retour sous $43.33 (MM50) ou cassure de $43.16 (low intraday) en clôture → revenir SURVEILLER
- **Sizing :** Réduit (max 5% du capital) en raison de la liquidité limitée et de l'absence de fondamentaux

**Earnings JOUR J** : Les résultats restent non observables à 10:00 UTC. Sur publication post-marché, générer immédiatement un `_earnings.md` flash si les données FMP/Yahoo sont injectées.

**Niveau de confiance :** Faible — l'analyse repose sur des proxies et des valeurs par défaut. La volatilité sur faible liquidité amplifie le risque de faux signaux. Le rebond technique est validé mais fragile. Aucun catalyseur fondamental n'est visible.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 10:00 UTC. Données : `data/latest.json`, `data/recommandations_latest.json`, `data/validation_report.txt`.*
