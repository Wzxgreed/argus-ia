# AAPL — Mise à Jour Snapshot 13:00 UTC (2026-06-22)

> **Source :** `data/latest.json` (snapshot 2026-06-22 13:00 UTC, post-ouverture US) + agents recommandations, sector rotation, FX, quant, geo, social
> **Référence précédente :** [AAPL_2026-06-22_update.md](AAPL_2026-06-22_update.md) (snapshot 10:00 UTC 22/06)
> **Contexte :** Snapshot post-ouverture. **Résolution majeure : anomalie options JSON corrigée** avec valeurs opérationnelles fiables. Consensus FMP rehaussé. Données prix/volumes/techniques strictement inchangées vs 10h.

---

## Résumé des Changements depuis le Snapshot 10h UTC (2026-06-22)

| Indicateur | Snapshot 10h UTC (22/06) | Snapshot 13h UTC (22/06) | Δ vs Prior |
|-----------|--------------------------|--------------------------|------------|
| Cours close prior | $295.95 (close 21/06) | **$295.95** | 🟢 Inchangé |
| Cours actuel | **$298.01** | **$298.01** | 🟢 Inchangé |
| RSI 14j | **39.07** | **39.07** | 🟢 Inchangé |
| ATR 14j | **$8.16** | **$8.16** | 🟢 Inchangé |
| MM 50j | **$288.63** | **$288.63** | 🟢 Inchangé |
| Volume du jour | 85.96M vs 52.71M avg (1.63×) | **85.96M vs 52.71M avg (1.63×)** | 🟢 Inchangé |
| Short Interest | 1.06% | **1.06%** | 🟢 Inchangé |
| Consensus FMP PT | $295.96 (61 analystes) | **$296.27 (62 analystes)** | 🟢 **+$0.31 (+1 analyste)** — micro-rehaussement |
| Upside implicite | −0.7% | **−0.6%** | 🟢 **Amélioration marginale** |
| Max Pain | $225.00 (anomalie JSON) | **$290.00** | 🟢 **RÉSOLU — valeur opérationnelle** |
| Put/Call Ratio | null (anomalie JSON) | **0.80** | 🟢 **RÉSOLU** |
| Call OI % | null (anomalie JSON) | **55.6%** | 🟢 **RÉSOLU** |
| Score Opportunité agent | 5.2/10 | **5.2/10** | 🟢 Inchangé |
| Score Global ajusté | 57.3/100 | **57.3/100** | 🟢 Inchangé |
| Recommandation agent | ATTENDRE | **ATTENDRE** | 🟢 Confirmée |
| Timing agent | Favorable | **Favorable** | 🟢 Confirmé |

**Verdict :** Le snapshot 13h UTC apporte une **stabilité mécanique totale** sur les données prix, volumes et techniques. L'évolution majeure est la **résolution définitive de l'anomalie options JSON** qui persistait depuis le snapshot 10h. Le max pain est corrigé à **$290.00**, le put/call ratio à **0.80** et le Call OI à **55.6%**. Ces valeurs sont opérationnelles et révisent la lecture mécaniste : le spot ($298.01) est désormais **au-dessus du max pain** (+2.7%), ce qui crée une pression gamma baissière vers $290.00 à l'expiration (jour J). Le consensus FMP est micro-rehaussé à $296.27 (+$0.31) avec 62 analystes. Les scores agents restent inchangés. **Recommandation ATTENDRE maintenue — nuance technique légèrement dégradée par le pinning gamma baissier, partiellement compensée par la résolution de l'anomalie et la structure options modérément haussière.**

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (close 21/06) | $295.95 | 🟢 Inchangé vs 10h |
| Cours actuel (22/06) | $298.01 | 🟢 +$2.06 (+0.70%) vs previous close — inchangé vs 10h |
| Open / High / Low (22/06) | $298.11 / $300.57 / $295.62 | 🟢 High teste $300.00, range intraday $4.95 (0.6× ATR) — inchangé |
| RSI 14j | 39.07 | 🟡 Zone neutre favorable — approche survente (< 30) — inchangé |
| ATR 14j | $8.16 | 🔴 Expansion +3.6% vs $7.88 (17/06) — volatilité réelle en hausse — inchangé vs 10h |
| MM 50j | $288.63 | 🟢 Support dynamique en hausse — marge +$9.38 (+3.1%) — inchangé vs 10h |
| MM 200j | null | 🔴 [DONNÉES MANQUANTES] |
| Volume 20j | 52.71M | 🟢 1.63× moyenne — explosion volumétrique, plus du double vs 17/06 — inchangé vs 10h |
| 52W Range | $198.96–$317.40 | Cours à −6.1% du 52W high — inchangé |
| Support clé | $288.63 | MM50 confirmé — cassure = invalidation tendance haussière |
| Support secondaire | $281.69 | Cours − 2×ATR ($8.16) = $298.01 − $16.32 |
| Support tertiaire | $273.53 | Cours − 3×ATR ($8.16) = $298.01 − $24.48 |
| Résistance proche | $300.00 | Niveau psychologique — testé en intraday 22/06 |
| Résistance | $317.40 | 52W high — break nécessite volume > 55M en clôture |
| Résistance consensus | $296.27 | Micro-mur — cours $298.01 au-dessus, signal de sur-ajustement persistant |
| Short Interest | 1.06% | 🟢 Faible — pas de setup short squeeze |

**Interprétation technique :**
- **RSI 39.07** : inchangé vs 10h. Détente, approche la zone de survente (< 30). Historiquement, la zone 35–40 est une zone d'accumulation/distribution. La prochaine cassure sous 35 activerait un signal de survente. 🟡
- **Volume 85.96M (1.63×)** : inchangé vs 10h. Explosion volumétrique sans équivalent depuis le 08/06 (1.51×). Un volume > 1.5× sur un mouvement de +0.7% suggère un **transfert de marché** (institutionnels rééquilibrant) plutôt qu'un mouvement directionnel. La faible amplitude vs volume est un signal d'indécision. 🟡
- **ATR $8.16** : inchangé vs 10h. Expansion de +3.6% vs $7.88 (17/06), confirmant une volatilité réelle en hausse post-sell-off. 🔴
- **MM50 $288.63** : inchangé vs 10h. En hausse continue (+$1.64 vs $286.99 17/06), confirmant la pente haussière du support dynamique. Marge confortable de +$9.38. 🟢
- **Max pain $290.00** : résolu à $290.00 (vs $225.00 aberrant à 10h). Le spot $298.01 est **+2.7% au-dessus** du max pain. À expiration (jour J 2026-06-22), cela crée une **pression gamma baissière** (market makers ont intérêt à rapprocher le prix vers $290.00). 🔴

---

## Mise à Jour Fondamentale

### Consensus Analystes — Micro-signal Positif Atténué
- **Price Target moyen FMP : $296.27** (62 analystes, 4 mises à jour le mois dernier, 14 le trimestre dernier)
- **Upside implicite : −0.6%** vs cours $298.01 — amélioré vs −0.7% (10h) et −1.1% (17/06) grâce au rehaussement consensus
- **Couverture :** 62 analystes — coverage institutionnel massif, cours reste au-dessus du consensus

### Ratios FMP — Inchangés (FY2025)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.38T | $3.82T | 🟡 Écart +15% entre sources |
| P/E (LTM) | 36.1x | 34.1x | 🔴 Élevé |
| Forward P/E | 31.0x | — | 🔴 Élevé |
| EV/Revenue | 9.7x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 27.5x | 27.0x | 🔴 Élevé |
| P/B | 41.0x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples élevés mais qualité institutionnelle intacte. Le Filtre Qualité reste **6/6** ✅ Quality Compounder. Pas de changement de guidance, pas de news majeure détectée dans `data/events_latest.json` (2026-06-22).

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 62 analystes FMP, PT $296.27. Aucun upgrade/downgrade majeur détecté dans le snapshot.
- **Upside consensus** négatif (−0.6%) — micro-signal négatif persistant mais atténué vs les snapshots précédents.

### Social Sentiment
- **Fichier `data/social_sentiment_latest.json` (2026-06-22) :** 0 mentions pour AAPL.
- **Label :** EXTREME_BEARISH (artefact, 0 mentions) — à ignorer. Pas de pump/dump détecté.

### Options — Anomalie JSON RÉSOLUE ✅ (Nouvelles Valeurs Opérationnelles)
- **Max Pain JSON : $290.00** — valeur corrigée et cohérente (−2.7% vs spot $298.01). Résolution de l'anomalie $225.00 aberrant du snapshot 10h.
- **Put/Call Ratio : 0.80** — modérément haussier (< 1.0, plus d'OI calls que puts).
- **Call OI % : 55.6%** — skew haussier modéré (> 50%).
- **Prochaine échéance :** 2026-06-22 (aujourd'hui, JOUR J) — expiration hebdomadaire.
- **Pinning gamma révisé :** Max pain $290.00 à **−2.7% du spot**. Le spot étant **au-dessus** du max pain, une pression mécaniste **baissière** modérée est possible en fin de séance (market makers ont intérêt à rapprocher le prix du max pain). Ce signal contraste avec la structure modérément haussière (P/C 0.80, Call OI 55.6%).
- **Structure :** Modérément haussière. P/C 0.80 < 1.0, Call OI 55.6% > 50%. Pas de setup squeeze extrême.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Beta 1.086 — inchangé |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟢 Faible | `data/fx_exposure_latest.json` (2026-06-22) : AAPL exposure 25%, flag 🟢, impact 0.0 — pas de headwind/tailwind |
| Technology (XLK) | 🟢 Favorable | `data/sector_rotation_latest.json` (2026-06-22) : XLK **top performer** (momentum 10.0/10) — contexte sectoriel favorable |

### Sector Rotation
- **XLK top performer** : RS 20j +7.07%, RS 60j +25.99%, momentum score 10.0/10 — contexte favorable pour AAPL, inchangé.
- **Crossover :** Aucun — signal NEUTRAL sur la rotation.

### Géopolitique
- `data/geo_risk_latest.json` (2026-05-17) : AAPL non flagué. 🟢 Aucun risque géopolitique spécifique.

### Accounting Risk / Quant
- `data/accounting_risk_latest.json` : **indisponible**.
- `data/quant_report_latest.json` (2026-05-17) : données insuffisantes (p-value 1.0, n=0). Pas d'alerte.

---

## Score Opportunité Révisé (Agents Officiels)

> **Note :** Les scores agents sont disponibles (`data/recommandations_latest.json`, 2026-06-22).

| Axe | Snapshot 10h 22/06 /10 | Snapshot 13h 22/06 /10 | Δ | Justification |
|-----|------------------------|------------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucun catalyseur nouveau. Earnings 2026-07-30 dans 38 jours. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. Upside consensus négatif persistant (−0.6%). |
| Momentum | 5.5 | **5.5** | 0 | RSI inchangé (39.07), volume inchangé (1.63×), structure options résolue modérément haussière mais pinning gamma baissier. |
| **Score Opportunité** | **5.2** | **5.2** | **0** | Pondération régime default 35/40/25 |
| **Score Global** | **52.3** | **52.3** | **0** | Base |
| **Score Global ajusté** | **57.3** | **57.3** | **0** | Pas de malus/bonus majeur détecté |

**Recommandation officielle : ATTENDRE** — Timing **Favorable**

**Verdict institutionnel Argus-IA :** Les scores agents sont **strictement inchangés** entre les deux snapshots, ce qui reflète la stabilité mécanique totale des données prix et techniques. L'évolution positive est la **résolution définitive de l'anomalie options JSON**, qui restaure la visibilité mécaniste. Cependant, la nouvelle valeur opérationnelle du max pain (**$290.00**) révise la lecture gamma : le spot étant au-dessus (+2.7%), la pression mécaniste est désormais **baissière** (vs haussière à $305.00 le 17/06). La structure options (P/C 0.80, Call OI 55.6%) reste modérément haussière, créant une tension mécaniste. Le consensus FMP micro-rehaussé ($296.27, 62 analystes) atténue légèrement le signal négatif. Cependant, le ratio R/R reste sous le seuil institutionnel 2:1.

---

## Niveaux SL / TP Révisés

| | Snapshot 10h 22/06 | Snapshot 13h 22/06 | Justification |
|---|--------------------|--------------------|---------------|
| Entrée suggérée | $298.01 | **$298.01** | Cours inchangé |
| Stop-Loss | $281.69 | **$281.69** | Cours − 2×ATR ($8.16) = $298.01 − $16.32 |
| Take-Profit | $322.49 | **$322.49** | Cours + 3×ATR ($8.16) = $298.01 + $24.48 |
| Ratio R/R | 1.5 | **1.5** | Inchangé — inférieur au seuil 2:1 |

**Note institutionnelle :** Le ratio R/R reste à 1.5:1, inférieur au seuil de 2:1 requis pour un sizing Standard. Le MM50 confirmé à $288.63 reste le support clé. Une cassure sous $288.63 sur volume > 55M en clôture invaliderait la tendance haussière et activerait le SL $281.69. La résistance $317.40 (52W high) doit être breakée sur volume > 55M en clôture pour confirmer une reprise haussière. Le max pain $290.00 à −2.7% du cours est un niveau mécaniste à surveiller aujourd'hui (expiration 2026-06-22) : un retour vers $290.00 est mécaniquement plausible en fin de séance.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec NUANCE MIXTE — Options résolues mais pinning gamma baissier, consensus micro-rehaussé. Recommandation ATTENDRE maintenue. Timing Favorable maintenu.**

Le snapshot 13h UTC confirme l'absence de volatilité nouvelle par rapport au snapshot 10h. Les données prix, volumes, RSI, ATR et MM50 sont strictement inchangées. L'évolution significative est la **résolution définitive de l'anomalie options JSON** qui permet désormais une analyse mécaniste fiable : max pain **$290.00**, P/C **0.80**, Call OI **55.6%**. Cette structure est modérément haussière en termes de skew (P/C < 1.0, Call OI > 50%), mais le **pinning gamma est baissier** (spot au-dessus du max pain = pression vers le bas). Le consensus FMP est micro-rehaussé à $296.27 (+$0.31) avec 62 analystes (+1), atténuant légèrement le signal négatif. Cependant, ces évolutions techniques restent marginales face aux facteurs de poids : upside consensus négatif (−0.6%), multiples élevés (P/E 36.1x), et ratio R/R insuffisant (1.5:1).

### Ce qui a changé (évolutions significatives)
1. **Options JSON résolues** : max pain $225.00 aberrant → **$290.00** (cohérent), P/C null → **0.80**, Call OI null → **55.6%**. Anomalie résolue. 🟢
2. **Pinning gamma révisé** : max pain $290.00 à −2.7% du spot = pression mécaniste **baissière** modérée possible en fin de séance (vs haussière à $305.00 le 17/06). 🔴
3. **Consensus FMP rehaussé** : $295.96 (61 analystes) → **$296.27 (62 analystes)**. Upside −0.7% → **−0.6%**. 🟢
4. **Structure options** : Modérément haussière (P/C 0.80 < 1.0, Call OI 55.6% > 50%). 🟢

### Ce qui n'a PAS changé (stabilité)
1. **Cours** : $298.01 — inchangé vs 10h.
2. **RSI** : 39.07 — inchangé.
3. **ATR** : $8.16 — inchangé.
4. **MM50** : $288.63 — inchangé.
5. **Volume** : 85.96M (1.63×) — inchangé.
6. **Short Interest** : 1.06% — inchangé.
7. **Fondamentaux FMP FY2025** — inchangés.
8. **Filtre Qualité 6/6** ✅ Quality Compounder.
9. **Geo risk** — aucun flag spécifique AAPL.
10. **FX exposure** : 25%, flag 🟢, impact nul — inchangé.
11. **Sector rotation** : XLK top performer (10.0/10) — contexte favorable inchangé.
12. **Scores agents** : Score Opportunité 5.2/10, Score Global ajusté 57.3/100 — inchangés.
13. **Recommandation** : ATTENDRE, Timing Favorable — inchangée.

### Risques identifiés (évolutions)
1. **Pinning gamma baissier** — max pain $290.00, spot $298.01 = +2.7% au-dessus. Pression mécaniste vers le bas à expiration aujourd'hui. 🔴
2. **Divergence volume/prix** — volume 1.63× sur mouvement +0.7% = signal d'indécision ou de transfert de marché. 🟡
3. **Cours au-dessus du consensus** — upside négatif (−0.6%) = le cours est au-dessus de la cible moyenne des analystes. 🔴
4. **Valorisation étirée** — P/E 36.1x, Forward P/E 31.0x. Compression multiple possible si guidance décevante le 2026-07-30. 🔴
5. **RSI proche survente** — 39.07, une cassure sous 35 activerait un signal de survente. 🟡
6. **Expiration options aujourd'hui** — 2026-06-22, max pain $290.00. Pinning gamma baissier si spot reste au-dessus. 🔴

### Positionnement Argus-IA
- **Action : ATTENDRE** — La résolution de l'anomalie options est positive mais le pinning gamma baissier ($290.00) justifie la patience. Attendre une résolution du signal mécaniste post-expiration (demain).
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (38 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $300.00 sur volume > 1.0× moyenne :** Break du niveau psychologique — réévaluer le momentum.
- **Si cours < $288.63 (MM50) sur volume > 55M :** Tendance haussière invalidée — risque de test $281.69 (SL).
- **Si cours < $290.00 à la clôture :** Pinning gamma validé — pas de signal directionnel pour demain.
- **Si volume > 1.2× moyenne sur 2 séances consécutives avec cours > $300 :** Confirmation institutionnelle haussière — upgrade possible.
- **Si RSI remonte > 45 avec volume > 0.8× :** Signal de force — confirmerait le timing Favorable.

---

## [DONNÉES PARTIELLES]
- MACD, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings
- `data/accounting_risk_latest.json` — indisponible
- `data/quant_report_latest.json` (2026-05-17) — données insuffisantes (p-value 1.0, n=0)
- `data/transcripts_NLP_latest.json` — indisponible
- `data/validation_report.txt` (2026-06-22) — 5 [ERROR] système (VRT schema, AST/AXA/QTBS/ASTSPACE fetch failed), 2 [WARNING] (IREN, NOK). AAPL non concerné.

---

## Références
- `data/latest.json` (snapshot 2026-06-22 13:00 UTC) — Close $298.01 (+0.70% vs previous close $295.95), RSI 39.07, ATR $8.16, MM50 $288.63, volume 85.96M (1.63×), short interest 1.06%, consensus FMP $296.27 (62 analystes), options max_pain $290.00, put/call 0.80, call_oi_pct 55.6%
- `data/recommandations_latest.json` (2026-06-22) — Score Opportunité 5.2/10, Score Global 52.3/100, Score Global ajusté 57.3/100, Recommandation ATTENDRE, Timing Favorable
- `data/sector_rotation_latest.json` (2026-06-22) — XLK top performer, momentum 10.0/10
- `data/fx_exposure_latest.json` (2026-06-22) — AAPL exposure 25%, flag 🟢, impact 0.0
- `data/social_sentiment_latest.json` (2026-06-22) — 0 mentions, EXTREME_BEARISH artefact
- `data/upcoming_events_latest.json` (2026-06-22) — Earnings 2026-07-30 (38 jours), Est EPS $1.83–$1.99, Rev $109.0B
- `data/events_latest.json` (2026-06-22) — Aucun événement corporate
- `data/geo_risk_latest.json` (2026-05-17) — AAPL non flagué
- `data/quant_report_latest.json` (2026-05-17) — Données quantitatives insuffisantes
- `data/quality_report_latest.json` (2026-05-17) — AAPL status `ok`
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
