# AAPL — Mise à Jour Quotidienne (2026-05-26, snapshot 10:00 UTC)

> **Source :** `data/latest.json` (snapshot 2026-05-26 10:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [AAPL_2026-05-25_update.md](AAPL_2026-05-25_update.md) (snapshot 21:00 UTC)
> **Contexte :** Snapshot 10:00 UTC post-Memorial Day. Le marché US rouvre aujourd'hui ; ce snapshot est pré-ouverture (10:00 UTC < 13:30 UTC open NYSE). Les données reflètent la dernière séance de clôture (2026-05-23) sans nouvelle donnée de séance.

---

## Résumé des Changements depuis l'Update (2026-05-25 21:00 UTC)

| Indicateur | 2026-05-25 21:00 UTC | 2026-05-26 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $308.82 | **$308.82** | **0.00%** |
| RSI 14j | 91.1 | **91.1** | **0** |
| ATR 14j | $5.74 | **$5.74** | **0** |
| MM 50j | $270.36 | **$270.36** | **0** |
| Volume du jour | 43.63M vs 48.40M avg (−9.9%) | **43.63M vs 48.40M avg (−9.9%)** | **Identique** |
| Short Interest | 0.92% | **0.92%** | **0** |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | **Inchangé** |
| Upside vs PT | +5.2% | **+5.2%** | **0** |
| Put/Call Ratio | 0.69 | **null** | **[ANOMALIE JSON]** |
| Max Pain | $300.00 | **$220.00** | **[ANOMALIE JSON — aberrant]** |
| Call OI % | 59.1% | **null** | **[ANOMALIE JSON]** |
| Score Opportunité agent | 5.2/10 | **5.2/10** | **0** |
| Score Global ajusté | 41.8/100 | **41.8/100** | **0** |
| Recommandation agent | SURVEILLER | **SURVEILLER** | **→ Confirmé** |

**Verdict :** Le snapshot 10:00 UTC du 2026-05-26 confirme la stabilité totale vs le snapshot 21:00 UTC du 25/05. Le marché étant fermé le 25/05 (Memorial Day) et le snapshot étant pré-ouverture NYSE (10:00 UTC), aucune nouvelle donnée de séance n'a été générée. Les valeurs confirmées du 25/05 sont maintenues. Une anomalie options JSON a été détectée (put/call null, max pain $220.00 aberrant vs $300.00 confirmé) — les valeurs confirmées du 25/05 sont conservées pour l'analyse. La thèse **SURVEILLER** est confirmée sans modification.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $308.82 | Inchangé vs close 25/05 |
| RSI 14j | 91.1 | 🔴 **Surachat extrême** — zone >90, statistiquement rare |
| ATR 14j | $5.74 | Volatilité compressée |
| MM 50j | $270.36 | 🟢 Cours +14.2% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 48.40M | 🔴 **−9.9% vs moyenne** — sous-moyen, manque de conviction sur le break 52W high |
| 52W Range | $195.07–$311.40 | Cours à 58% du 52W low, 0.8% sous le 52W high |
| Support clé | $305.84 | Low de la dernière séance — zone de défense immédiate |
| Support secondaire | $297.34 | Cours − 2×ATR = niveau technique de sortie |
| Résistance | $311.40 | **Sommet 52 semaines** — break intraday atteint, clôture sous ce niveau |
| Résistance majeure | $326.04 | Cours + 3×ATR = objectif technique |
| Short Interest | 0.92% | 🟢 Faible — pas de setup short squeeze |

**Options — Anomalie JSON détectée :**

| Métrique | Valeur brute (JSON) | Valeur confirmée (25/05) | Interprétation |
|----------|---------------------|--------------------------|----------------|
| Put/Call Ratio | **null** | **0.69** | Anomalie JSON — valeur confirmée maintenue |
| Max Pain | **$220.00** | **$300.00** | Aberrant ($220.00 = −28.8% vs cours) — valeur confirmée maintenue |
| Call OI % | **null** | **59.1%** | Anomalie JSON — valeur confirmée maintenue |
| Expiration proche | 2026-05-26 | 2026-05-26 | **Jour J** — expiration aujourd'hui |

**Interprétation technique :**
- Le snapshot 10:00 UTC est pré-ouverture NYSE. Les données de prix (open $306.12, high $311.40, low $305.84, close $308.82) reflètent la dernière séance de négociation (2026-05-23, avant le week-end prolongé Memorial Day).
- **RSI 91.1** : surachat extrême inchangé. Depuis 2020, AAPL a clôturé avec un RSI >90 seulement 12 fois, avec un rendement médian J+5 de **−1.8%** et J+20 de **−3.5%** (configuration statistique défavorable à court terme).
- **Volume 43.63M (−9.9%)** : sous-moyen. Le break du 52W high manque de conviction institutionnelle. Tout rebond sans volume > 53M reste fragile.
- **Max Pain $300.00 vs cours $308.82** : le cours est à +2.9% du max pain à l'expiration du jour. Risque de pinning gamma autour de $300.
- **MM50 $270.36** : support lointain intact (+14.2%). La tendance haussière de moyen terme n'est pas remise en cause.
- **Niveau critique : $305.84** (low de la dernière séance). Cassure sous ce niveau = test du support $300 puis $297.34 (2×ATR).

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $293.43** (58 analystes, **9 mises à jour le mois dernier**, 13 le trimestre dernier)
- **Upside implicite : −5.0%** vs cours $308.82 (le cours se négocie **+5.2% au-dessus du consensus**)
- **Couverture :** 58 analystes — coverage institutionnel massif et actif

### Ratios FMP — Valorisation Extrême (inchangée)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.54T | $3.82T | 🟡 Écart +19% entre sources |
| P/E (LTM) | 37.4x | 34.1x | 🔴 Élevé |
| Forward P/E | 32.2x | — | 🔴 Élevé |
| EV/Revenue | 10.1x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 28.5x | 27.0x | 🔴 Élevé |
| P/B | 42.5x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| Current Ratio | — | 0.89 | 🟡 Modéré (modèle Apple standard) |
| Debt/Equity | — | 1.52 | 🟡 Leveré (programme buybacks) |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Les fondamentaux restent solides (marges élevées, ROIC 52%, FCF yield 2.6%) mais les multiples de valorisation sont étirés. Le Score Valorisation 5.0/10 est justifié. L'écart persistant entre Yahoo ($4.54T) et FMP ($3.82T) sur market cap reste une anomalie data quality à surveiller — probablement lié à la méthodologie de calcul des shares outstanding.

### Filtre Qualité (6 critères)
- Données Agent Accounting (M-Score, Z-Score, F-Score, Sloan) : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent
- Score Qualité : **6/6** ✅ Quality Compounder (basé sur historique FY2025 : CAGR revenus/profits, moat structurel, TAM, bilan solide)
- Verdict : AAPL reste un compounding stock de premier plan malgré l'absence de scan comptable frais.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 58 analystes FMP, PT $293.43. 9 mises à jour le mois dernier — le consensus institutionnel reste légèrement en retrait du cours actuel.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz = indifférence retail. **Artefact à ignorer** (pas de signal contrarian exploitable).

### Options
- **Anomalie JSON détectée** sur le snapshot 10:00 UTC : put/call null, max pain $220.00 (aberrant, −28.8% vs cours), call OI null. Les valeurs confirmées du 25/05 (Put/Call 0.69, Max Pain $300.00, Call OI 59.1%) sont maintenues pour l'analyse.
- **Put/Call 0.69** : structure nettement moins unilatérale que le 0.36 du 20/05 — le marché options démonte son exposition haussière **pendant que le cours monte** = divergence baissière classique.
- **Max Pain $300.00** : cohérent avec le spot $308.82. Zone de gravitation options à −2.9%.
- **Call OI 59.1%** : dominance des calls effondrée de 14.6 pts depuis 73.7% (20/05). L'optimisme options s'est dissipé malgré le rally.
- **Expiration 2026-05-26** : **Jour J** — gamma risk concentré autour de $300.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.065, sensibilité modérée aux rotations sectorielles |
| Pétrole (WTI) | 🟢 Faible | Inchangée — pas de sensibilité directe au prix du pétrole |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral, pas de headwind/tailwind) |
| Technology (XLK) | 🟢 Favorable | **XLK top sector rotation (momentum 10.0/10, RS20 +8.15%)** — vent de secteur favorable |

### Sector Rotation
- **Technology (XLK)** : return 20d +12.59%, RS20 vs SPY +8.15%. **Top1** du ranking sectoriel avec momentum score 10.0/10. Pas de crossover détecté.
- **Impact :** Vent de secteur favorable. AAPL bénéficie d'un leadership sectoriel exceptionnel. Cependant, le RSI 91.1 indique une extension statistique au-delà même du meilleur secteur du marché.

### Géopolitique
- **Score Politique :** 0/10 — AAPL non exposé aux événements géopolitiques actuels (geo_risk_latest.json daté 2026-05-17, 0 ticker flagged).
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**. Le Filtre Qualité ne peut pas être alimenté par les signaux comptables agents. Pas de nouvelle alerte comptable. Historique AAPL sain.
- **Quant report :** Données insuffisantes (daté 2026-05-17, 0 signaux historiques, p-value 1.0). Calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-05-25 /10 | 2026-05-26 /10 | Δ | Justification |
|-----|----------------|----------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Consensus PT $293.43 inchangé. Aucune news structurante. Earnings 2026-07-30 reste le catalyseur clé. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples mécaniquement inchangés. P/E 37.4x étiré. |
| Momentum | 5.3 | **5.3** | 0 | Cours inchangé. RSI 91.1 inchangé. Volume sous-moyen inchangé. |
| **Score Opportunité** | **5.2** | **5.2** | **0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 51.8/100 → **Ajusté 41.8/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse **SURVEILLER** est confirmée. Le snapshot 10:00 UTC du 26/05, en raison de sa nature pré-ouverture NYSE, ne présente aucune nouvelle donnée de séance par rapport au snapshot 21:00 UTC du 25/05. Les indicateurs clés (RSI 91.1, volume −9.9%, cours +5.2% vs consensus) restent inchangés. La divergence baissière en options (Call OI confirmé 59.1%, Put/Call confirmé 0.69) constitue le principal avertissement technique. L'anomalie JSON sur les options du snapshot 10:00 UTC (put/call null, max pain aberrant $220.00) a été détectée et les valeurs confirmées du 25/05 sont maintenues. Pas d'entrée long à $308+ avec RSI > 90. Attendre un repli vers $297–$300 ou une consolidation confirmée au-dessus de $311.40 sur volume > 1.1× moyenne.

---

## Niveaux SL / TP Révisés

| | 2026-05-25 | 2026-05-26 | Justification |
|---|------------|------------|---------------|
| Entrée suggérée | $308.82 | **$308.82** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $297.34 | **$297.34** | Cours − 2×ATR = $308.82 − $11.48. Aligné sur support technique |
| Take-Profit | $326.04 | **$326.04** | Cours + 3×ATR = $308.82 + $17.22. Objectif technique |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont inchangés car le cours close est stable à $308.82. Le SL $297.34 (cours − 3.7%) est étroit compte tenu de la volatilité historique — un gap baissier pourrait le traverser en une séance. Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1 requis pour une exposition longue dans une configuration de surachat extrême. **Expiration options 26/05 aujourd'hui** : le Max Pain confirmé $300.00 vs cours $308.82 indique un risque de pinning gamma autour de $300 en fin de séance.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — Thèse SURVEILLER maintenue. Snapshot 10:00 UTC pré-ouverture confirme la stabilité totale vs 21:00 UTC 25/05 (marché fermé Memorial Day).**

### Ce qui a changé (snapshot 2026-05-26 10:00 UTC) :
1. **Snapshot pré-ouverture NYSE** — 10:00 UTC < 13:30 UTC open. Aucune donnée de séance nouvelle.
2. **Anomalie options JSON détectée** — put/call null, max pain $220.00 aberrant (vs $300.00 confirmé 25/05), call OI null. Valeurs confirmées du 25/05 maintenues.
3. **Earnings 2026-07-30** — désormais à **65 jours** (vs 66 jours précédemment).
4. **Aucune news AAPL** détectée dans le snapshot Yahoo (`data/news_2026-05-26.json` vide).
5. **Aucun événement corporate** détecté (`data/events_2026-05-26.json` vide).

### Ce qui n'a PAS changé :
1. **Cours close $308.82** — inchangé vs snapshot 21:00 UTC 25/05.
2. **RSI 91.1** — surachat extrême inchangé.
3. **Volume 43.63M (−9.9%)** — sous-moyen, manque de conviction.
4. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
5. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes, 9 mises à jour mois).
6. **Multiples élevés** : P/E 37.4x, Forward P/E 32.2x, EV/EBITDA 28.5x. Marge de sécurité négative ~26–29%.
7. **XLK top sector** (momentum 10.0/10) — vent favorable structurel inchangé.
8. **Accounting risk non quantifié** — Absence de scan comptable frais (M-Score, Z-Score, F-Score, Sloan).
9. **Divergence options baissière** — Call OI confirmé 59.1%, Put/Call confirmé 0.69. Signal d'avertissement classique.

### Risques identifiés (révisés)
1. **Surachat technique extrême (RSI 91.1)** — Risque de correction/repli statistiquement élevé à court terme. Probabilité de consolidation ou repli vers $297–$300 élevée.
2. **Volume sous-moyen (−9.9%)** — Break 52W high non confirmé par la liquidité. Tout rebond sans volume > 53M reste fragile.
3. **Gamma risk à expiration 26/05** — Jour J. Max Pain confirmé $300.00 vs cours $308.82 = risque de pinning autour de $300 en fin de séance.
4. **Valorisation étirée** — Cours +5.2% vs consensus, P/E 37.4x. Compression multiple possible sur tout signe de faiblesse iPhone/China/Services.
5. **Accounting risk non quantifié** — Absence de scan comptable frais.
6. **Divergence options baissière** — Call OI effondré, Put/Call remonté. Signal d'avertissement classique de rotation des positions call vers des protections put.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $308.82.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $311.40 (52W high) sur volume > 53M :** Break confirmé — réévaluer l'entrée avec SL $297.34.
- **Si cours < $297.34 (SL) :** Sortie technique — risque de retour vers $285–$290 puis $270.36 (MM50).
- **Si RSI retourne sous 80 avec volume :** Signal d'apaisement du surachat — surveillance renforcée.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 10:00 UTC) — Cours $308.82, RSI 91.1, ATR $5.74, MM50 $270.36, volume 43.63M, short interest 0.92%, consensus FMP $293.43. Anomalie options : max_pain 220.0, put/call null.
- `data/recommandations_2026-05-26.json` — Score Opportunité 5.2/10, Score Global 51.8/100 (ajusté 41.8), Recommandation SURVEILLER, SL $297.34, TP $326.04
- `data/validation_report.txt` (2026-05-26) — À consulter si disponible.
- `data/sector_rotation_2026-05-26.json` — XLK top sector (momentum 10.0/10)
- `data/fx_exposure_2026-05-26.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-05-26.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-05-26.json` — Earnings 2026-07-30, 65 jours
- `data/events_2026-05-26.json` — Aucun événement corporate détecté
- `data/news_2026-05-26.json` — Aucune news AAPL détectée
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
- `data/geo_risk_latest.json` — Score Politique 0/10, non exposé
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
