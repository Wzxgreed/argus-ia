# TEST — Mise à Jour Post-Session (2026-05-19)

> **Date :** 2026-05-19
> **Heure snapshot :** 21:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-19T21:00:02 UTC), `data/recommandations_latest.json`
> **Type :** Mise à jour post-session — snapshot 21:00 UTC vs snapshot 17:00 UTC

---

## Résumé des Changements

| Métrique | Snapshot 17:00 UTC | Snapshot 21:00 UTC | Delta |
|----------|-------------------|-------------------|-------|
| Cours | $43.395 | **$44.185** | **+1.82%** |
| RSI 14j | 53.18 | **56.47** | **+3.29 pts** |
| ATR 14j | $1.27 | **$1.27** | Inchangé |
| MM 50j | $43.53 | **$43.54** | +0.02% |
| Volume | 1,597 (0.88×) | **2,448 (1.32×)** | **Au-dessus moyenne 20j** |
| Position vs MM50 | En-dessous (−0.31%) | **Au-dessus (+1.48%)** | **Signal haussier** |
| Score Opportunité (agent) | 5.4/10 | **6.0/10** | **+0.6 pt** |
| Score Global (agent) | 46.0/100 | **65.2/100** | **+19.2 pts** |
| Verdict agent reco | SURVEILLER | **ACHETER (Réduit)** | **Upgrade** |
| Timing | Défavorable | **Favorable** | **Amélioré** |

**Événement majeur :** Rebond technique en fin de soirée. Le cours a regagné la MM50 ($43.54) avec un high à $44.245 (+2.0% vs 17:00 UTC), portant le RSI de 53.18 à 56.47. Le volume de 2,448 dépasse la moyenne 20j (1,857) de 32%, confirmant un intérêt acheteur en after-hours ou sur la clôture étendue. L'Agent Recommandation a upgradé le verdict de **SURVEILLER → ACHETER (Réduit)** et le timing de **Défavorable → Favorable**.

---

## Mise à Jour Technique

- **Cours :** $44.185 (open $43.57 / high $44.245 / low $43.16 / previous close $44.935)
- **Variation session :** −1.67% vs previous close
- **Variation vs snapshot 17:00 UTC :** +1.82% — rebond partiel du gap-down matinal
- **RSI 14j :** 56.47 — zone neutre favorable, retour au-dessus du seuil 55
- **ATR 14j :** $1.27 — inchangé, volatilité stable
- **MM 50j :** $43.54 — **regagnée en clôture** (cours +1.48% au-dessus)
- **MM 200j :** N/A
- **Volume relatif :** 1.32× moyenne 20j (2,448 vs 1,857) — **soutien acheteur confirmé**
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette, à +9.6% du 52W low

**Verdict timing :** Favorable. La récupération au-dessus de la MM50 en clôture annule le signal baissier de 17:00 UTC. Le high $44.245 a testé la résistance du previous close ($44.935) sans la franchir. Configuration de marteau inversé : le cours a ouvert bas ($43.57), creusé un plus bas ($43.16), puis rebondi pour clôturer proche du high ($44.185).

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 21:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Validation données :** TEST non listé dans les [ERROR] ni [WARNING] du rapport de validation (22/25 OK)

**Impact earnings du jour :** Aucun résultat post-earnings injecté dans `latest.json` à 21:00 UTC. L'événement earnings (source FMP) reste non observable. Le rebond de +1.82% entre 17:00 et 21:00 UTC est purement technique (récupération de la MM50) sans catalyseur fondamental identifiable.

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
| **Upcoming Events** | Earnings 2026-05-19 — days_until 0 | JOUR J — résultats toujours non observables |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation du rebond purement technique.

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
| Bonus / Timing | +5.2 | Récupération MM50 + volume > moyenne + timing Favorable |
| **Score Global ajusté** | **65.2/100** | **ACHETER (Réduit)** |

**Proximité des seuils :** À 65.2/100, TEST est passé au-dessus du seuil ACHETER réduit (60–74). L'upgrade de 19.2 points est entièrement expliqué par la récupération technique (cassure MM50 inversée, volume en hausse, RSI en zone favorable) et le momentum upgradé de 4.5 à 7.0/10. Le Score Opportunité à 6.0/10 franchit le seuil d'entrée minimal.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 21:00 UTC (cours $44.19, ATR $1.27) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.19 | Snapshot 21:00 UTC |
| Stop-loss suggéré (2×ATR) | **$41.65** | −5.75% sous le cours |
| Take-profit suggéré (3×ATR) | **$48.00** | +8.62% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.54 (−1.47%) — ancienne résistance devenue support dynamique
- **Support gap :** $43.395 (−1.80%) — low de 17:00 UTC, niveau de validation du rebond
- **Résistance previous close :** $44.935 (+1.69%) — combler le gap-down matinal
- **Résistance 52W high :** $57.74 (+30.66%)
- **Support 52W low :** $40.27 (−8.87%) — dernier niveau de défense

**Note :** Le stop-loss à $41.65 se situe au-dessus du 52W low ($40.27) et sous le support gap ($43.395). Une cassure de ce support intermédiaire invaliderait le rebond technique.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse UPGRADÉE de SURVEILLER → ACHETER (Réduit) suite à la récupération technique au-dessus de la MM50.**

Le snapshot 21:00 UTC révèle une amélioration technique significative par rapport au snapshot 17:00 UTC :
- **Rebond de +1.82%** entre 17:00 et 21:00 UTC ($43.395 → $44.185)
- **Récupération de la MM50** en clôture ($44.185 vs MM50 $43.54) — signal haussier de court terme
- **RSI en zone favorable** à 56.47 — momentum haussier confirmé
- **Volume au-dessus de la moyenne** à 2,448 (1.32× moyenne 20j) — soutien acheteur visible

**Trois facteurs de prudence restent :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle faible** — volume moyen 20j < 2K actions
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils tolérants au risque. Le timing Favorable et le retour au-dessus de la MM50 offrent un setup technique court terme.
- **Seuil de confirmation :** Clôture au-dessus de $44.93 (previous close / combler le gap) avec volume > 2,500
- **Seuil d'invalidation :** Retour sous $43.54 (MM50) ou cassure de $43.395 (low 17:00 UTC) → revenir SURVEILLER
- **Sizing :** Réduit (max 5% du capital) en raison de la liquidité limitée et de l'absence de fondamentaux

**Earnings JOUR J** : Les résultats restent non observables à 21:00 UTC. Sur publication post-marché ou demain, générer immédiatement un `_earnings.md` flash si les données FMP/Yahoo sont injectées.

**Niveau de confiance :** Faible — l'analyse repose sur des proxies et des valeurs par défaut. La volatilité sur faible liquidité amplifie le risque de faux signaux. Le rebond technique est validé mais fragile.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 21:00 UTC. Données : `data/latest.json`, `data/recommandations_latest.json`, `data/validation_report.txt`.*
