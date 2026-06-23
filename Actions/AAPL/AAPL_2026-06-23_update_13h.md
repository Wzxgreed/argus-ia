# AAPL — Mise à Jour Snapshot 13:00 UTC (2026-06-23)

> **Source :** `data/latest.json` (snapshot 2026-06-23 13:00 UTC) + agents recommandations, sector rotation, FX, quant, geo, social
> **Référence précédente :** [AAPL_2026-06-23_update.md](AAPL_2026-06-23_update.md) (snapshot 10:00 UTC 23/06)
> **Contexte :** Snapshot après-midi. Données prix/technique répliquées du close officiel 22/06. **Anomalie options JSON résolue** avec valeurs révisées.

---

## Résumé des Changements depuis le Snapshot 10:00 UTC (2026-06-23)

| Indicateur | Snapshot 10h UTC (23/06) | Snapshot 13h UTC (23/06) | Δ vs Prior |
|-----------|--------------------------|--------------------------|------------|
| Cours close | **$297.01** | **$297.01** | 🟢 **Inchangé** (close officiel répliqué) |
| Previous close | $298.01 | **$298.01** | 🟢 Inchangé |
| Change vs prior | −0.34% | **−0.34%** | 🟢 Inchangé |
| RSI 14j | **42.19** | **42.19** | 🟢 **Inchangé** — zone neutre favorable |
| ATR 14j | **$8.07** | **$8.07** | 🟢 **Inchangé** |
| MM 50j | **$289.37** | **$289.37** | 🟢 **Inchargé** |
| Volume du jour | 44.81M vs 52.80M avg (0.85×) | **44.81M vs 52.80M avg (0.85×)** | 🟢 **Inchangé** — normalisation complète |
| Short Interest | 1.06% | **1.06%** | 🟢 Inchangé |
| Consensus FMP PT | $296.27 (62 analystes) | **$296.27 (62 analystes)** | 🟢 Inchangé |
| Upside implicite | −0.2% | **−0.2%** | 🟢 Inchangé |
| Max Pain JSON | $225.00 (anomalie) | **$290.00** | 🟢 **Résolu** — correspond à la valeur opérationnelle conservée |
| Put/Call Ratio JSON | null (corrompu) | **1.18** | 🔴 **Révisé** — vs 0.80 opérationnel conservé, structure plus baissière |
| Call OI % JSON | null (corrompu) | **45.9%** | 🔴 **Révisé** — vs 55.6% opérationnel conservé, sous les 50% |
| Score Opportunité agent | 5.2/10 | **5.2/10** | 🟢 Inchangé |
| Score Global ajusté | 57.3/100 | **57.3/100** | 🟢 Inchangé |
| Recommandation agent | ATTENDRE | **ATTENDRE** | 🟢 Confirmée |
| Timing agent | Favorable | **Favorable** | 🟢 Confirmé |

**Verdict :** Le snapshot 13h UTC du 23/06 confirme une **stabilité mécanique totale** des prix et des indicateurs techniques par rapport au snapshot 10h UTC. Le cours reste calé sous le niveau psychologique **$300.00** avec un RSI stable en zone neutre favorable (**42.19**). L'unique évolution notable est la **résolution de l'anomalie options JSON** : le max pain revient à **$290.00** (cohérent avec la valeur opérationnelle conservée), mais le **put/call ratio affiche désormais 1.18** (vs 0.80 conservé) et le **call OI % tombe à 45.9%** (vs 55.6% conservé). Ces valeurs révisées indiquent une **structure options modérément baissière** (P/C > 1.0, Call OI < 50%), alors que les valeurs opérationnelles conservées du matin suggéraient une structure modérément haussière. Cette divergence mérite d'être prise en compte, notamment à J-1 de l'expiration hebdomadaire (2026-06-24) où les flux de couverture peuvent fausser la lecture directionnelle. Les scores agents, le consensus FMP, les fondamentaux et l'ensemble des métriques de risque restent **strictement inchangés**. **Recommandation ATTENDRE maintenue** — aucun nouvel élément directionnel.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (snapshot 23/06 13h) | $297.01 | 🟢 Inchangé vs snapshot 10h — stabilité mécanique |
| Open / High / Low (22/06) | $297.31 / $302.42 / $296.76 | High teste $302.42, rejet sous $300.00, range $5.66 (0.70× ATR) |
| RSI 14j | 42.19 | 🟢 Zone neutre favorable (40–50) — stable, hors survente |
| ATR 14j | $8.07 | 🟢 Stable — volatilité réelle inchangée |
| MM 50j | $289.37 | 🟢 Support dynamique stable — marge +$7.64 (+2.6%) |
| MM 200j | null | 🔴 [DONNÉES MANQUANTES] |
| Volume 20j | 52.80M | 🟢 0.85× moyenne — normalisation complète, participation standard |
| 52W Range | $199.26–$317.40 | Cours à −6.4% du 52W high |
| Support clé | $289.37 | MM50 confirmé — cassure = invalidation tendance haussière |
| Support secondaire | $280.87 | Cours − 2×ATR ($8.07) = $297.01 − $16.14 |
| Support tertiaire | $272.80 | Cours − 3×ATR ($8.07) = $297.01 − $24.21 |
| Résistance proche | $300.00 | Niveau psychologique — non testé ce matin, break nécessite volume > 1.0× |
| Résistance | $302.42 | High intraday 22/06 — à breaker sur volume > 55M pour confirmation haussière |
| Résistance | $317.40 | 52W high — break nécessite volume > 55M en clôture |
| Résistance consensus | $296.27 | Cours $297.01 légèrement au-dessus — micro-mur modéré |
| Short Interest | 1.06% | 🟢 Faible — pas de setup short squeeze |

**Interprétation technique :**
- **RSI 42.19** : stable en zone neutre favorable. Le franchissement de 50 reste la prochaine étape clé pour confirmer un momentum haussier. 🟢
- **Volume 44.81M (0.85×)** : stable, normalisation complète. La participation est standard, invalidant toute hypothèse de mouvement léger. 🟢
- **ATR $8.07** : stable. Le range intraday réel du 22/06 ($5.66) reste inférieur à l'ATR, indiquant une volatilité contenue. 🟢
- **MM50 $289.37** : inchangé, pente haussière du support dynamique maintenue. Marge confortable de +$7.64. 🟢
- **Anomalie options JSON résolue** : max pain affiché désormais **$290.00** (cohérent avec la valeur opérationnelle conservée, +2.4% vs spot $297.01). Le spot reste au-dessus du max pain, maintenant une pression gamma baissière modérée post-expiration. 🟡

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $296.27** (62 analystes, 4 mises à jour le mois dernier, 14 le trimestre dernier)
- **Upside implicite : −0.2%** vs cours $297.01 — quasi-alignement cours/consensus
- **Couverture :** 62 analystes — coverage institutionnel massif

### Ratios FMP — Inchangés (FY2025, close 27/09/2025)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.36T | $3.82T | 🟡 Écart +15% entre sources |
| P/E (LTM) | 36.0x | 34.1x | 🔴 Élevé |
| Forward P/E | 30.9x | — | 🔴 Élevé |
| EV/Revenue | 9.7x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 27.4x | 27.0x | 🔴 Élevé |
| P/B | 40.9x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |
| FCF Yield | — | 2.59% | 🟡 Modéré |
| Net Debt / EBITDA | — | 0.53x | 🟢 Très faible endettement |

**Interprétation :** Fondamentaux strictement inchangés. Multiples élevés mais qualité institutionnelle intacte. Le Filtre Qualité reste **6/6** ✅ Quality Compounder. Pas de changement de guidance, pas de news majeure détectée dans `data/events_latest.json` (2026-06-23). AAPL non concerné par les erreurs de validation du jour.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 62 analystes FMP, PT $296.27. Aucun upgrade/downgrade majeur détecté dans le snapshot.
- **Upside consensus** négatif mais resserré (−0.2%) — signal neutre, convergence cours/consensus.

### Social Sentiment
- **Fichier `data/social_sentiment_latest.json` (2026-06-23) :** 0 mentions pour AAPL.
- **Label :** EXTREME_BEARISH (artefact, 0 mentions) — à ignorer. Pas de pump/dump détecté.

### Options — Anomalie JSON Résolue, Valeurs Révisées
- **Max Pain JSON : $290.00** — **RÉSOLU** (cohérent avec la valeur opérationnelle conservée). Écart +2.4% vs spot $297.01.
- **Put/Call Ratio JSON : 1.18** — **NOUVEAU** (vs null ce matin, vs 0.80 valeur opérationnelle conservée). P/C > 1.0 indique une structure **modérément baissière**.
- **Call OI % JSON : 45.9%** — **NOUVEAU** (vs null ce matin, vs 55.6% valeur opérationnelle conservée). Call OI sous les 50% confirme une structure **moins haussière**.
- **Prochaine échéance :** 2026-06-24 (demain, hebdomadaire — J-1)
- **Pinning gamma (valeurs résolues) :** Max pain $290.00 à **−2.4% du spot**. Le spot étant au-dessus du max pain, une pression mécaniste **baissière modérée** persiste post-expiration du 22/06.
- **Structure (valeurs résolues) :** Modérément baissière. P/C 1.18 > 1.0, Call OI 45.9% < 50%. ⚠️ À J-1 de l'expiration, ces flux peuvent refléter des opérations de couverture/désarbitrage plutôt qu'une conviction directionnelle réelle.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Beta 1.086 — inchangé |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟢 Faible | `data/fx_exposure_latest.json` (2026-06-23) : AAPL exposure 25%, flag 🟢, impact 0.0 — pas de headwind/tailwind |
| Technology (XLK) | 🟢 Favorable | `data/sector_rotation_latest.json` (2026-06-23) : XLK **top performer** (momentum 10.0/10) — contexte sectoriel favorable |

### Sector Rotation
- **XLK top performer** : RS 20j +7.23%, RS 60j +27.04%, momentum score 10.0/10 — contexte favorable pour AAPL, inchangé.
- **Crossover :** Aucun — signal NEUTRAL sur la rotation.

### Géopolitique
- `data/geo_risk_latest.json` (2026-05-17, dernier disponible) : AAPL non flagué. 🟢 Aucun risque géopolitique spécifique.

### Accounting Risk / Quant
- `data/accounting_risk_latest.json` — **indisponible**.
- `data/quant_report_latest.json` (2026-05-17) — données insuffisantes (signals_total 0, significance "Insuffisant"). Pas d'alerte.

---

## Score Opportunité Révisé (Agents Officiels)

> **Note :** Les scores agents sont disponibles (`data/recommandations_latest.json`, snapshot 2026-06-23 13:00 UTC).

| Axe | Snapshot 10h 23/06 /10 | Snapshot 13h 23/06 /10 | Δ | Justification |
|-----|------------------------|------------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucun catalyseur nouveau. Earnings 2026-07-30 dans 37 jours. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. Upside consensus −0.2%. |
| Momentum | 5.5 | **5.5** | 0 | RSI 42.19 stable (zone neutre favorable), volume normalisé 0.85×. |
| **Score Opportunité** | **5.2** | **5.2** | **0** | Pondération régime default 35/40/25 |
| **Score Global** | **52.3** | **52.3** | **0** | Base |
| **Score Global ajusté** | **57.3** | **57.3** | **0** | Pas de malus/bonus majeur détecté |

**Recommandation officielle : ATTENDRE** — Timing **Favorable**

**Verdict institutionnel Argus-IA :** Les scores agents sont **strictement inchangés** entre le snapshot 10h et le snapshot 13h UTC du 23/06, reflétant l'absence de nouvelles données directionnelles. L'anomalie options JSON est résolue : le max pain $290.00 est confirmé cohérent avec la valeur opérationnelle conservée. Cependant, le **put/call ratio révisé à 1.18** (vs 0.80 conservé) et le **call OI % à 45.9%** (vs 55.6% conservé) indiquent une structure options **modérément baissière** à J-1 de l'expiration hebdomadaire. Cette détente peut refléter une couverture accrue des positions longues avant l'expiration du 24/06 plutôt qu'un renversement de conviction. Le pinning gamma baissier modéré persiste (spot +2.4% vs max pain). Le ratio R/R reste sous le seuil institutionnel 2:1.

---

## Niveaux SL / TP Révisés

| | Snapshot 10h 23/06 | Snapshot 13h 23/06 | Justification |
|---|--------------------|--------------------|---------------|
| Entrée suggérée | $297.01 | **$297.01** | Cours inchangé (close répliqué) |
| Stop-Loss | $280.87 | **$280.87** | Cours − 2×ATR ($8.07) = $297.01 − $16.14 |
| Take-Profit | $321.22 | **$321.22** | Cours + 3×ATR ($8.07) = $297.01 + $24.21 |
| Ratio R/R | 1.5 | **1.5** | Inchangé — inférieur au seuil 2:1 |

**Note institutionnelle :** Le ratio R/R reste à 1.5:1, inférieur au seuil de 2:1 requis pour un sizing Standard. Le MM50 confirmé à $289.37 reste le support clé. Une cassure sous $289.37 sur volume > 55M en clôture invaliderait la tendance haussière et activerait le SL $280.87. La résistance $317.40 (52W high) doit être breakée sur volume > 55M en clôture pour confirmer une reprise haussière. Le max pain $290.00 à −2.4% du cours est un niveau mécaniste à surveiller — une reclôture sous ce niveau renforcerait la pression gamma baissière. Une reclôture au-dessus de $300.00 sur volume > 1.0× moyenne serait un signal technique positif.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — Stabilité mécanique totale. Anomalie options résolue avec nuance baissière modérée. Recommandation ATTENDRE maintenue. Timing Favorable maintenu.**

Le snapshot 13h UTC du 23/06 confirme une **stabilité mécanique quasi-totale** par rapport au snapshot 10h UTC. Le cours reste à **$297.01**, le RSI stable à **42.19** (zone neutre favorable), l'ATR inchangé à **$8.07** et le MM50 calé à **$289.37**. Le volume est stable à **44.81M (0.85× moyenne)**, confirmant la normalisation complète de la participation. Le consensus FMP reste inchangé à **$296.27** (62 analystes), et le cours est quasi-aligné avec le consensus (−0.2% upside).

L'évolution principale est la **résolution de l'anomalie options JSON** : le max pain revient à **$290.00** (cohérent avec la valeur opérationnelle conservée), mais le **put/call ratio affiche 1.18** (vs 0.80 conservé) et le **call OI % tombe à 45.9%** (vs 55.6% conservé). Ces valeurs révisées indiquent une **structure options modérément baissière** à J-1 de l'expiration hebdomadaire. Cette détente peut refléter des flux de couverture/désarbitrage plutôt qu'un renversement de conviction — elle n'est pas suffisante pour modifier la thèse, mais mérite d'être intégrée dans le radar de risque. Les fondamentaux et les scores agents sont strictement inchangés.

### Ce qui a changé (évolutions)
1. **Anomalie options JSON résolue** : max pain $225.00 aberrant → **$290.00** (cohérent). 🟢
2. **Put/Call Ratio révisé** : null → **1.18** (vs 0.80 conservé) — structure plus baissière. 🔴
3. **Call OI % révisé** : null → **45.9%** (vs 55.6% conservé) — sous les 50%. 🔴

### Ce qui n'a PAS changé (stabilité)
1. **Cours** : $297.01 — inchangé (close officiel répliqué).
2. **RSI** : 42.19 — inchangé.
3. **ATR** : $8.07 — inchangé.
4. **MM50** : $289.37 — inchangé.
5. **Volume** : 44.81M (0.85×) — inchangé.
6. **Consensus FMP** : $296.27 (62 analystes) — inchangé.
7. **Short Interest** : 1.06% — inchangé.
8. **Fondamentaux FMP FY2025** — inchangés.
9. **Filtre Qualité 6/6** ✅ Quality Compounder.
10. **Geo risk** — aucun flag spécifique AAPL.
11. **FX exposure** : 25%, flag 🟢, impact nul — inchangé.
12. **Sector rotation** : XLK top performer (10.0/10) — contexte favorable inchangé.
13. **Scores agents** : Score Opportunité 5.2/10, Score Global ajusté 57.3/100 — inchangés.
14. **Recommandation** : ATTENDRE, Timing Favorable — inchangée.

### Risques identifiés (évolutions)
1. **Structure options modérément baissière** — P/C 1.18, Call OI 45.9%. À J-1 expiration 24/06, peut refléter couverture plutôt que conviction. À surveiller post-expiration. 🟡
2. **Valorisation étirée** — P/E 36.0x, Forward P/E 30.9x. Compression multiple possible si guidance décevante le 2026-07-30. 🔴
3. **Rejet du niveau $300.00** — résistance psychologique active, non testée ce matin. 🟡

### Positionnement Argus-IA
- **Action : ATTENDRE** — Aucun nouvel élément directionnel. La stabilité mécanique confirme l'absence de conviction immédiate.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (37 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $302.42 sur volume > 1.0× moyenne :** Break du high intraday — réévaluer le momentum.
- **Si cours > $300.00 sur volume > 0.9× sur 2 séances consécutives :** Confirmation haussière — upgrade possible.
- **Si cours < $289.37 (MM50) sur volume > 55M :** Tendance haussière invalidée — risque de test $280.87 (SL).
- **Si RSI remonte > 50 avec volume > 0.8× :** Signal de force — confirmerait le timing Favorable.
- **Post-expiration 24/06 :** Vérifier si la structure options reste baissière (P/C > 1.0, Call OI < 50%) ou si elle se rééquilibre haussier.

---

## [DONNÉES PARTIELLES]
- MACD, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings
- `data/accounting_risk_latest.json` — indisponible
- `data/quant_report_latest.json` (2026-05-17) — données insuffisantes (signals_total 0, significance "Insuffisant")
- `data/transcripts_NLP_latest.json` — indisponible
- `data/validation_report.txt` (2026-06-23) — 5 [ERROR] système (VRT schema, AST/AXA/QTBS/ASTSPACE fetch failed), 2 [WARNING] (IREN, NOK). **AAPL non concerné.**

---

## Références
- `data/latest.json` (snapshot 2026-06-23 13:00 UTC) — Close $297.01 (−0.34% vs previous close $298.01), RSI 42.19, ATR $8.07, MM50 $289.37, volume 44.81M (0.85×), short interest 1.06%, consensus FMP $296.27 (62 analystes), options max_pain $290.00 (résolu), put/call 1.18, call_oi_pct 45.9%
- `data/recommandations_latest.json` (2026-06-23) — Score Opportunité 5.2/10, Score Global 52.3/100, Score Global ajusté 57.3/100, Recommandation ATTENDRE, Timing Favorable, SL $280.87, TP $321.22, R/R 1.5
- `data/sector_rotation_latest.json` (2026-06-23) — XLK top performer, momentum 10.0/10
- `data/fx_exposure_latest.json` (2026-06-23) — AAPL exposure 25%, flag 🟢, impact 0.0
- `data/social_sentiment_latest.json` (2026-06-23) — 0 mentions, EXTREME_BEARISH artefact
- `data/upcoming_events_latest.json` (2026-06-23) — Earnings 2026-07-30 (37 jours), Est EPS $1.83–$1.99, Rev $109.0B
- `data/events_latest.json` (2026-06-23) — Aucun événement corporate
- `data/geo_risk_latest.json` (2026-05-17) — AAPL non flagué
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
