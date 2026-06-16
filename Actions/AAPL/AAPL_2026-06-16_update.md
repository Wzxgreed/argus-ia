# AAPL — Mise à Jour Snapshot 10:00 UTC (2026-06-16)

> **Source :** `data/latest.json` (snapshot 2026-06-16 10:00 UTC, pré-ouverture US) + agents quant, geo, quality
> **Référence précédente :** [AAPL_2026-06-15_update_21h.md](AAPL_2026-06-15_update_21h.md) (snapshot 21:00 UTC 15/06)
> **Contexte :** Snapshot pré-ouverture — données prix live indisponibles (marché non ouvert). Close officiel du 15/06 actualisé par Yahoo à $291.13, inférieur au mid-session $296.88/$296.42 précédemment rapporté. RSI retour en survente. Données techniques partielles.

---

## Résumé des Changements depuis le Snapshot 21h UTC (2026-06-15)

| Indicateur | Snapshot 21h UTC (15/06) | Snapshot 10h UTC (16/06) | Δ vs Prior |
|-----------|--------------------------|--------------------------|------------|
| Cours close | $296.42 | **$291.13** | 🔴 **−$5.29 (−1.78%)** — divergence majeure : le close Yahoo actualisé du 15/06 est inférieur au mid-session précédemment rapporté |
| RSI 14j | 40.19 | **34.49** | 🔴 **−5.70 pts** — retour en zone de survente (<35) |
| ATR 14j | $7.77 | **null** | 🔴 **[DONNÉES MANQUANTES]** |
| MM 50j | $286.18 | **null** | 🔴 **[DONNÉES MANQUANTES]** |
| MM 200j | null | **null** | ⚠️ Toujours indisponible |
| Volume du jour (15/06) | 45.30M vs 50.01M avg (0.91×) | **45.30M vs 50.01M avg (0.91×)** | 🟢 Inchangé — volume quasi-normalisé confirmé |
| Short Interest | 1.06% | **1.06%** | 🟢 Inchangé |
| Consensus FMP PT | $295.96 (61 analystes) | **$295.96 (61 analystes)** | 🟢 Inchangé |
| Upside implicite | −0.3% | **+1.7%** | 🟢 **Amélioration** — upside redevient positif vs $291.13 |
| Max Pain | $300.00 | **$230.00** | 🔴 **[ANOMALIE JSON]** — valeur aberrante vs spot $291.13 |
| Put/Call Ratio | 0.48 | **null** | 🔴 **[ANOMALIE JSON]** — données corrompues |
| Call OI % | 67.6% | **null** | 🔴 **[ANOMALIE JSON]** — données corrompues |
| Score Opportunité agent | 5.3/10 | **Indisponible** | ⚠️ `data/recommandations_latest.json` absent |
| Score Global ajusté | 58.0/100 | **Indisponible** | ⚠️ `data/recommandations_latest.json` absent |
| Recommandation agent | ATTENDRE | **Indisponible** | ⚠️ Fichier agents indisponible |
| Timing agent | Favorable | **Indisponible** | ⚠️ Fichier agents indisponible |

**Verdict :** Le snapshot 10h UTC du 16/06 révèle une **divergence majeure sur le close du 15/06** : Yahoo actualise le close officiel à **$291.13**, soit **$5.29 sous le $296.42** rapporté en fin de session précédente. Cette divergence indique que le rebond intraday du 15/06 (de $291.13 à $296.88 en mid-session) **ne s'est pas maintenu en close officielle** selon la source Yahoo. Le RSI retombe en survente (**34.49**, −5.70 pts), invalidant la sortie de survente observée à 21h UTC (RSI 40.19). Les données techniques sont partielles (ATR et MM50 null). Les données options sont corrompues dans le JSON (max pain $230.00 aberrant). La structure haussière post-expiration (P/C 0.48, Call OI 67.6%) est conservée sur valeur opérationnelle. L'upside consensus redevient **+1.7%** vs le close $291.13, un micro-signal positif. **Recommandation ATTENDRE maintenue — nuance technique dégradée par le retour en survente.**

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (close 15/06) | $291.13 | 🔴 Rejet du rebond intraday — close officiel Yahoo sous le mid-session $296.42 |
| RSI 14j | 34.49 | 🔴 **Retour en zone de survente** (<35) — invalidation de la sortie observée à 21h UTC |
| ATR 14j | null | 🔴 [DONNÉES MANQUANTES] — dernière valeur opérationnelle $7.77 |
| MM 50j | null | 🔴 [DONNÉES MANQUANTES] — dernière valeur opérationnelle $286.18 |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 50.01M | 🟢 0.91× moyenne — inchangé, quasi-normalisé |
| 52W Range | $195.07–$317.40 | Cours à −8.3% du 52W high |
| Support clé | $286.18 | MM50 (dernière valeur connue) — cassure = invalidation tendance haussière |
| Support secondaire | $275.59 | Cours − 2×ATR historique ($7.77) = $291.13 − $15.54 [PROVISOIRE] |
| Support tertiaire | $267.82 | Cours − 3×ATR historique = $291.13 − $23.31 [PROVISOIRE] |
| Résistance | $317.40 | 52W high — break nécessite volume > 55M en clôture |
| Résistance proche | $295.96 | Consensus FMP — micro-mur de résistance |
| Short Interest | 1.06% | 🟢 Faible — pas de setup short squeeze |

**Interprétation technique :**
- **RSI 34.49** : retour en survente confirmé. Historiquement, les rebonds depuis RSI < 35 se confirment si le RSI franchit 45 dans les 2–3 séances suivantes avec volume > 0.8×. Le retour en survente est un signal de **mean reversion favorable** mais le manque de confirmation de la veille (le rebond à 40.19 ne s'est pas maintenu) fragilise le setup. 🟡
- **Close $291.13 vs mid-session $296.88** : le rebond intraday du 15/06 a été **rejeté en close officielle**. C'est un signal de distribution vendeuse persistante. Les acheteurs n'ont pas réussi à défendre les gains de la mi-journée. 🔴
- **Volume 45.30M (0.91×)** : inchangé vs le snapshot précédent. Le volume quasi-normalisé est confirmé, mais il a servi à un **rejet de rebond** plutôt qu'à une confirmation haussière. 🟡
- **ATR null / MM50 null** : perte de données techniques critiques. La marge de sécurité au-dessus du MM50 ($286.18) ne peut pas être vérifiée. Surveillance renforcée requise. 🔴
- **Max pain $230.00** : valeur aberrante dans le JSON (écart de −21% vs spot). Identifié comme anomalie JSON récurrente. Valeurs opérationnelles conservées : max pain **$300.00**, P/C **0.48**, Call OI **67.6%**. 🔴 [ANOMALIE JSON]
- **Upside consensus +1.7%** vs $291.13 : micro-signal positif — le cours est désormais légèrement sous le consensus. 🟢

---

## Mise à Jour Fondamentale

### Consensus Analystes — Micro-signal Positif
- **Price Target moyen FMP : $295.96** (61 analystes, 3 mises à jour le mois dernier, 13 le trimestre dernier)
- **Upside implicite : +1.7%** vs cours $291.13 — retour en territoire positif (vs −0.3% précédemment)
- **Couverture :** 61 analystes — coverage institutionnel massif

### Ratios FMP — Inchangés (FY2025)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.35T | $3.82T | 🟡 Écart +14% entre sources |
| P/E (LTM) | 35.8x | 34.1x | 🔴 Élevé |
| Forward P/E | 30.9x | — | 🔴 Élevé |
| EV/Revenue | 9.5x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 26.8x | 27.0x | 🔴 Élevé |
| P/B | 40.8x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples élevés mais qualité institutionnelle intacte. Le micro-signal positif est l'upside consensus revenu en positif (+1.7%) grâce à la baisse du cours. Le Filtre Qualité reste **6/6** ✅ Quality Compounder (quality report : `ok`).

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 61 analystes FMP, PT $295.96. Aucun upgrade/downgrade majeur détecté dans le snapshot.
- **Upside consensus** revenu positif (+1.7%) — micro-signal positif.

### Social Sentiment
- **Fichier `data/social_sentiment_latest.json` indisponible.**
- Label précédent : EXTREME_BEARISH (artefact, 0 mentions). Pas de pump/dump détecté.

### Options — Anomalie JSON Récurrente, Structure Opérationnelle Conservée
- **Max Pain JSON : $230.00** — valeur aberrante (−21% vs spot $291.13). Identifié comme anomalie JSON récurrente.
- **Valeurs opérationnelles conservées :** max pain **$300.00**, P/C **0.48**, Call OI **67.6%**.
- **Prochaine échéance :** 2026-06-17 (demain) — pinning gamma possible autour de $300.00.
- **Structure :** haussière (P/C 0.48, Call OI 67.6%) — inchangée sur base opérationnelle.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.086 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | `data/fx_exposure_latest.json` indisponible |
| Technology (XLK) | 🟢 Favorable | `data/sector_rotation_latest.json` indisponible — référence précédente : XLK top sector (momentum 10.0/10) |

### Sector Rotation
- `data/sector_rotation_latest.json` **indisponible**.
- Référence précédente : XLK top performer (momentum 10.0/10), signal NEUTRAL.

### Géopolitique
- `data/geo_risk_latest.json` (2026-05-17) : AAPL non flagué. 🟢 Aucun risque géopolitique spécifique.

### Accounting Risk / Quant
- `data/accounting_risk_latest.json` **indisponible**.
- `data/quant_report_latest.json` (2026-05-17) : données insuffisantes (p-value 1.0, n=0). Pas d'alerte.
- `data/quality_report_latest.json` (2026-05-17) : AAPL status **ok**.

---

## Score Opportunité Révisé (Estimation Technique)

> **Note :** Les scores agents officiels ne sont pas disponibles (`data/recommandations_latest.json` absent). L'estimation suivante est une extrapolation technique à partir des données brutes.

| Axe | Snapshot 21h 15/06 /10 | Snapshot 10h 16/06 /10 | Δ | Justification |
|-----|-----------------------|------------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucun catalyseur nouveau. Earnings 2026-07-30 dans 44 jours. |
| Valorisation | 5.0 | **5.2** | +0.2 | Upside consensus revenu positif (+1.7% vs −0.3%). Multiples inchangés. |
| Momentum | 5.8 | **5.2** | −0.6 | RSI retour en survente (34.49), rejet du rebond intraday en close officielle ($291.13 vs $296.42). |
| **Score Opportunité estimé** | **5.3** | **5.2** | **−0.1** | Pondération régime default 35/40/25 |

**Score Global Composite estimé :** ~57.0/100 (vs 58.0/100 précédemment)
- Malus : données techniques partielles (−2 pts), anomalie options JSON (−1 pt)
- Bonus : upside consensus positif (+1 pt)
- Timing technique : **Favorable** (RSI < 35 = zone mean reversion historique favorable)
- **Recommandation estimée : ATTENDRE** (inchangée)

**Verdict institutionnel Argus-IA :** La divergence majeure sur le close du 15/06 ($296.42 → $291.13) est le changement le plus significatif. Elle invalide l'hypothèse d'un rebond validé en close et réinstalle le RSI en survente. L'upside consensus positif (+1.7%) est un micro-signal favorable, mais il est contrebalancé par le rejet technique. Les données partielles (ATR, MM50 null) empêchent tout positionnement agressif. La structure options haussière reste intacte sur base opérationnelle. Le ratio R/R reste sous le seuil institutionnel 2:1.

---

## Niveaux SL / TP Révisés

> **Note :** ATR 14j indisponible dans le snapshot. Calculs provisoires sur dernière valeur opérationnelle connue ($7.77) avec mention [PROVISOIRE].

| | Snapshot 21h 15/06 | Snapshot 10h 16/06 | Justification |
|---|--------------------|--------------------|---------------|
| Entrée suggérée | $296.42 | **$291.13** | Close officiel Yahoo actualisé |
| Stop-Loss | $280.88 | **$275.59** | Cours − 2×ATR historique ($7.77) = $291.13 − $15.54 [PROVISOIRE] |
| Take-Profit | $319.73 | **$314.44** | Cours + 3×ATR historique ($7.77) = $291.13 + $23.31 [PROVISOIRE] |
| Ratio R/R | 1.5 | **1.5** | Inchangé — inférieur au seuil 2:1 [PROVISOIRE] |

**Note institutionnelle :** Le ratio R/R reste à 1.5:1 sur base provisoire, inférieur au seuil de 2:1 requis pour un sizing Standard. Sans MM50 confirmé, le niveau $286.18 (dernière valeur connue) reste le support clé théorique. Une cassure sous $286.18 sur volume > 50M en clôture serait le premier signal d'alerte avant le SL provisoire $275.59. La résistance $317.40 (52W high) doit être breakée sur volume > 55M en clôture pour confirmer une reprise haussière. Le max pain opérationnel $300.00 à +3.0% du close est un niveau mécaniste à surveiller à l'échéance 2026-06-17 (demain).

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec NUANCE TECHNIQUE DÉGRADÉE — La recommandation reste ATTENDRE. Le timing reste Favorable (mean reversion).**

La thèse est confirmée mais avec une nuance technique dégradée car le close officiel Yahoo du 15/06 ($291.13) invalide le rebond observé en fin de session ($296.42). Le RSI retourne en survente (34.49), ce qui est à la fois un signal de faiblesse technique (rejet du rebond) et un setup de mean reversion favorable (zone < 35). L'absence de données ATR et MM50 empêche toute révision technique complète.

### Ce qui a changé (évolutions significatives)
1. **Cours close** : $296.42 → **$291.13** (−1.78%) — divergence majeure : rejet du rebond intraday en close officielle. 🔴
2. **RSI** : 40.19 → **34.49** (−5.70 pts) — retour en zone de survente. 🔴
3. **Upside consensus** : −0.3% → **+1.7%** — retour positif grâce à la baisse du cours. 🟢
4. **Données techniques** : ATR et MM50 passés de disponibles à **null** — perte de visibilité. 🔴
5. **Options JSON** : max pain corrompu ($300.00 → $230.00 aberrant), P/C et Call OI null — anomalie récurrente. 🔴

### Ce qui n'a PAS changé (stabilité)
1. **Volume** : 45.30M (0.91×) — quasi-normalisé, inchangé.
2. **Consensus FMP** : $295.96 (61 analystes) — inchangé.
3. **Short Interest** : 1.06% — inchangé.
4. **Fondamentaux FMP FY2025** — inchangés.
5. **Filtre Qualité 6/6** ✅ Quality Compounder (quality report : `ok`).
6. **Geo risk** — aucun flag spécifique AAPL.
7. **Structure options opérationnelle** — max pain $300.00, P/C 0.48, Call OI 67.6% (conservées sur base historique).

### Risques identifiés (évolutions)
1. **Données techniques partielles** — ATR et MM50 null empêchent le calcul précis des niveaux de SL/TP. 🔴
2. **Rejet du rebond intraday** — close $291.13 sous le mid-session $296.88 = distribution vendeuse persistante. 🔴
3. **RSI en survente** — 34.49 = zone favorable au rebond mean reversion, mais aussi signal de faiblesse si la survente s'étend. 🟡
4. **Valorisation étirée** — P/E 35.8x, Forward P/E 30.9x. Compression multiple possible si guidance décevante le 2026-07-30. 🔴
5. **Absence de catalyseur immédiat** — prochain earnings dans 44 jours (2026-07-30). Zone sans catalyseur = risque de dérive latérale. 🟡
6. **Anomalie options JSON récurrente** — empêche la surveillance mécaniste en temps réel. 🟡

### Positionnement Argus-IA
- **Action : ATTENDRE** — Le retour en survente est un setup de mean reversion favorable, mais le rejet du rebond en close officielle et l'absence de données techniques justifient la patience.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (44 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $296 sur volume > 1.0× moyenne :** Rebond validé — réévaluer le timing.
- **Si cours < $286.18 (MM50 historique) sur volume > 50M :** Tendance haussière invalidée — risque de test $275.59 (SL provisoire).
- **Si RSI remonte > 40 avec volume > 0.8× :** Signal de force — confirmerait le timing Favorable.
- **Si données ATR/MM50 ne reviennent pas dans le prochain snapshot :** Surveillance renforcée, pas de sizing standard sans niveaux confirmés.

---

## [DONNÉES PARTIELLES]
- Cours live du 16/06 — snapshot pré-ouverture (10h UTC), open/high/low/close NaN
- ATR 14j — null dans le snapshot
- MM50 / MM200 — null dans le snapshot
- MACD, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings
- `data/recommandations_latest.json` — indisponible (scores agents non actualisés)
- `data/accounting_risk_latest.json` — indisponible
- `data/sector_rotation_latest.json` — indisponible
- `data/social_sentiment_latest.json` — indisponible
- `data/fx_exposure_latest.json` — indisponible
- `data/upcoming_events_latest.json` — indisponible
- `data/events_latest.json` — indisponible
- `data/transcripts_NLP_latest.json` — indisponible

---

## Références
- `data/latest.json` (snapshot 2026-06-16 10:00 UTC) — Previous close $291.13, RSI 34.49, ATR null, MM50 null, volume 45.30M (0.91×), short interest 1.06%, consensus FMP $295.96 (61 analystes), options max_pain $230.00 (anomalie), put/call null, call_oi_pct null
- `data/recommandations_2026-06-15.json` — Score Opportunité 5.3/10, Score Global 58.0/100, Recommandation ATTENDRE, Timing Favorable (derniers scores agents connus)
- `data/validation_report.txt` (2026-06-16) — AAPL OK
- `data/quality_report_2026-05-17.json` — AAPL status `ok`
- `data/geo_risk_2026-05-17.json` — AAPL non flagué
- `data/quant_2026-05-17.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
