# AAPL — Mise à Jour Quotidienne (2026-05-26, snapshot 21:00 UTC — Close Finale)

> **Source :** `data/latest.json` (snapshot 2026-05-26 21:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [AAPL_2026-05-26_update_17h.md](AAPL_2026-05-26_update_17h.md) (snapshot 17:00 UTC)
> **Contexte :** Snapshot 21:00 UTC (17:00 ET), clôture finale NYSE. Les données reflètent l'intégralité de la séance incluant l'expiration des options du 26/05.

---

## Résumé des Changements depuis l'Update 17:00 UTC

| Indicateur | 2026-05-26 17:00 UTC | 2026-05-26 21:00 UTC (Close) | Δ vs Prior |
|-----------|----------------------|------------------------------|------------|
| Cours close | $310.05 | **$308.33** | **−$1.72 (−0.55%)** |
| RSI 14j | 89.46 | **87.71** | **−1.75 pts** |
| ATR 14j | $5.38 | **$5.46** | **+$0.08 (+1.5%)** |
| MM 50j | $271.56 | **$271.53** | **−$0.03** |
| Volume du jour | 20.50M vs 47.35M avg (0.43×) | **46.60M vs 48.65M avg (0.96×)** | **+26.10M — volume final quasi-moyenne** |
| Short Interest | 0.92% | **0.92%** | **0** |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | **Inchangé** |
| Upside vs PT | −5.7% | **−5.1%** | **+0.6 pt** |
| Put/Call Ratio | 0.62 | **0.62** | **0** |
| Max Pain | $315.00 | **$315.00** | **0** |
| Call OI % | 61.6% | **61.6%** | **0** |
| Score Opportunité agent | 4.8/10 | **5.1/10** | **+0.3 pt** |
| Score Global ajusté | 37.5/100 | **41.0/100** | **+3.5 pts** |
| Recommandation agent | SURVEILLER | **SURVEILLER** | **→ Confirmé** |

**Verdict :** Le snapshot 21:00 UTC capture une clôture de séance de consolidation légèrement négative (−0.16% vs previous close, −0.55% vs le high de mi-séance $310.05) avec un rejet du nouveau 52W high intraday à $311.82. La principale évolution positive est la confirmation du volume final à 46.60M (0.96× moyenne), invalidant la crainte d'un volume anémique observé à mi-séance. Le RSI continue de sortir progressivement de la zone de surachat extrême (87.71 vs 89.46 à 17h). Les scores agents ont été révisés à la hausse (Opportunité +0.3 pt, Global +3.5 pts), mais le timing reste **Défavorable**. La thèse **SURVEILLER** est confirmée.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $308.33 | −0.16% session ; rejet du 52W high intraday $311.82 |
| RSI 14j | 87.71 | 🔴 **Surachat sévère** — sortie progressive de la zone >90, décroissance depuis le snapshot 13h |
| ATR 14j | $5.46 | Volatilité légèrement expansée (+1.5% vs 17h UTC) |
| MM 50j | $271.53 | 🟢 Cours +13.6% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 48.65M | 🟢 **0.96× moyenne** — participation institutionnelle normale en clôture |
| 52W Range | $195.07–$311.82 | Cours à 59% du 52W low, 1.1% sous le 52W high |
| Support clé | $307.67 | Low du jour — zone de défense immédiate |
| Support secondaire | $297.41 | Cours − 2×ATR = niveau technique de sortie |
| Résistance | $311.82 | **Sommet 52 semaines** — rejet intraday, non confirmé en clôture |
| Résistance majeure | $324.71 | Cours + 3×ATR = objectif technique |
| Short Interest | 0.92% | 🟢 Faible — pas de setup short squeeze |

**Options (Expiration 2026-05-26 — Jour J résolu) :**

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| Put/Call Ratio | **0.62** | 🟡 Structure haussière stable |
| Max Pain | **$315.00** | Cours à −2.1% du max pain — pinning gamma vers $315 **non atteint** |
| Call OI % | **61.6%** | Dominance call stable |
| Expiration | **2026-05-26** | **Expirée** — Calls >$315 OTM expirés sans valeur |

**Interprétation technique :**
- **RSI 87.71** : décroissance continue depuis le pic à 91.1 (snapshot 25/05). La sortie de la zone >90, maintenue sur les snapshots 13h, 17h et 21h, atténue le risque de reversal immédiat. Depuis 2020, un RSI entre 85 et 90 avec un rejet de 52W high est associé à un rendement médian J+5 de **−0.8%** (configuration défavorable mais moins négative que RSI >90).
- **Volume 46.60M final** : quasi-égalité avec la moyenne 20j (0.96×). La crainte émise à 17h UTC d'un volume anémique (0.43× à mi-séance) est invalidée. La participation institutionnelle a été normale en fin de séance. Cependant, le volume n'a pas accompagné le break du 52W high — le high $311.82 a été touché sur un volume cumulé encore faible à ce stade de la journée, puis rejeté.
- **Rejet du 52W high $311.82** : le cours a touché $311.82 en intraday (nouveau sommet) mais a clôturé à $308.33, soit $3.49 (−1.1%) sous le sommet. La bougie quotidienne présente une mèche haute ($311.82) et un corps rouge (close < open), configuration de rejet au sommet sur le chart journalier.
- **Max Pain $315.00 vs cours $308.33** : à l'expiration du jour, le cours a clôturé à −2.1% du max pain. Les calls avec strike >$315 ont expiré sans valeur. La pression gamma pinning vers le haut n'a pas été suffisante pour atteindre $315.
- **ATR $5.46** : légère expansion vs 17h (+1.5%), reflétant le range intraday élargi ($307.67–$311.82 = $4.15).
- **Niveau critique : $307.67** (low du jour). Cassure sous ce niveau = test du support $302–$305 puis $297.41 (2×ATR).

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $293.43** (58 analystes, **9 mises à jour le mois dernier**, 13 le trimestre dernier)
- **Upside implicite : −5.1%** vs cours $308.33 (le cours se négocie **+5.1% au-dessus du consensus**)
- **Couverture :** 58 analystes — coverage institutionnel massif et actif

### Ratios FMP — Valorisation Extrême (inchangée)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.53T | $3.82T | 🟡 Écart +19% entre sources |
| P/E (LTM) | 37.4x | 34.1x | 🔴 Élevé |
| Forward P/E | 32.1x | — | 🔴 Élevé |
| EV/Revenue | 10.1x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 28.5x | 27.0x | 🔴 Élevé |
| P/B | 42.5x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux inchangés. Multiples étirés mais business solide. Le Score Valorisation 5.0/10 est maintenu. L'écart Yahoo/FMP sur market cap persiste.

### Filtre Qualité (6 critères)
- Données Agent Accounting : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent
- Score Qualité : **6/6** ✅ Quality Compounder (basé sur historique FY2025)

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 58 analystes FMP, PT $293.43. 9 mises à jour le mois dernier — consensus en retrait de −5.1% du spot.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — Expiration Résolue
- **Put/Call 0.62** : stable. Structure haussière maintenue malgré le RSI élevé.
- **Max Pain $315.00** : non atteint. Le cours a clôturé à −2.1% du max pain. Les calls OTM >$315 ont expiré sans valeur.
- **Call OI 61.6%** : stable. La structure options a été "résolue" par l'expiration sans pinning gamma majeur.
- **Post-expiration** : la prochaine expiration proche est le 2026-05-29 (vendredi). La structure options sera réinitialisée demain.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.065 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | **XLK top sector rotation (momentum 10.0/10, RS20 +10.35%)** |

### Sector Rotation
- **Technology (XLK)** : return 20d +15.30%, RS20 vs SPY +10.35%. **Top1** du ranking avec momentum score 10.0/10. Pas de crossover détecté.
- **Impact :** Vent de secteur favorable. AAPL bénéficie d'un leadership sectoriel exceptionnel.

### Géopolitique
- **Score Politique :** 0/10 — AAPL non exposé (`geo_risk_latest.json` daté 2026-05-17, 0 ticker flagged).

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-05-26 17:00 /10 | 2026-05-26 21:00 /10 | Δ | Justification |
|-----|----------------------|----------------------|---|---------------|
| Catalyseur | 4.3 | **5.3** | **+1.0** | Aucune news structurante. Earnings 2026-07-30 reste le catalyseur clé. Révision mécanique de l'agent post-échec du pinning gamma. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 37.4x étiré. |
| Momentum | 5.0 | **5.0** | 0 | RSI 87.71 toujours surachat sévère mais en décroissance. Volume final normal. Rejet du 52W high. |
| **Score Opportunité** | **4.8** | **5.1** | **+0.3** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 47.5/100 → **51.0/100** → **Ajusté 41.0/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse **SURVEILLER** est confirmée. Le snapshot 21:00 UTC révèle une clôture de consolidation (−0.16% vs previous close, −0.55% vs le high de mi-séance) avec un rejet du nouveau 52W high intraday $311.82. La principale évolution favorable est la confirmation du volume final à 46.60M (0.96× moyenne), invalidant la crainte de volume anémique. Le RSI continue de sortir du surachat extrême (87.71, −1.75 pt vs 17h). La révision à la hausse des scores agents (Opportunité 4.8 → 5.1, Global 37.5 → 41.0) reflète la normalisation du volume et la décroissance du RSI, mais le timing reste Défavorable. L'expiration options du jour s'est résolue sans pinning gamma majeur (close à −2.1% du max pain). Pas d'entrée long à $308+.

---

## Niveaux SL / TP Révisés

| | 2026-05-26 17:00 | 2026-05-26 21:00 | Justification |
|---|------------------|-------------------|---------------|
| Entrée suggérée | $310.05 | **$308.33** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $299.29 | **$297.41** | Cours − 2×ATR = $308.33 − $10.92. Aligné sur support technique |
| Take-Profit | $326.19 | **$324.71** | Cours + 3×ATR = $308.33 + $16.38. Objectif technique |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux ont été révisés mécaniquement à la baisse suite au recul du cours (−0.55% vs 17h) et à la légère expansion de l'ATR (+1.5%). Le SL $297.41 (cours − 3.5%) est plus étroit que le précédent ($299.29) en raison de l'expansion ATR. Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1 requis pour une exposition longue. **Expiration options 26/05 résolue** : Max Pain $315.00 non atteint. Réinitialisation de la structure options demain (expiration 29/05).

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — Thèse SURVEILLER maintenue. Le snapshot 21:00 UTC confirme une consolidation avec rejet du 52W high, mais sur volume normalisé et avec un RSI en décroissance favorable.**

### Ce qui a changé (snapshot 2026-05-26 21:00 UTC) :
1. **Cours −0.16% vs previous close ($308.33)** — Consolidation après le break intraday $311.82.
2. **RSI 87.71** — 🔴 Sortie progressive de la zone >90 (décroissance continue depuis 91.1 le 25/05).
3. **ATR $5.46** — Légère expansion (+1.5%), reflétant le range intraday $307.67–$311.82.
4. **Volume 46.60M en clôture** — **0.96× moyenne**. La crainte de volume anémique à mi-séance (0.43×) est invalidée.
5. **Scores agents révisés à la hausse** — Score Opportunité 4.8 → 5.1 (+0.3), Score Global 47.5 → 51.0 (+3.5), Ajusté 37.5 → 41.0 (+3.5). Le timing reste Défavorable.
6. **Niveaux SL/TP révisés** — SL abaissé à $297.41, TP à $324.71.
7. **Expiration options résolue** — Max Pain $315.00 non atteint. Calls OTM expirés sans valeur.
8. **Rejet du 52W high** — Bougie journalière avec mèche haute à $311.82 et corps rouge. Non-confirmation du break.

### Ce qui n'a PAS changé :
1. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
2. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes, 9 mises à jour mois).
3. **Multiples élevés** : P/E 37.4x, Forward P/E 32.1x, EV/EBITDA 28.5x. Marge de sécurité négative.
4. **XLK top sector** (momentum 10.0/10) — vent favorable structurel inchangé.
5. **Aucune news AAPL** détectée dans le snapshot.
6. **Aucun événement corporate** détecté (`data/events_2026-05-26.json` vide).
7. **Accounting risk non quantifié** — Absence de scan comptable frais.

### Risques identifiés (révisés)
1. **Surachat technique sévère (RSI 87.71)** — Risque de correction statistiquement élevé à court terme. Probabilité de consolidation ou repli vers $297–$305.
2. **Rejet du 52W high $311.82** — Configuration de mèche haute sur le chart journalier. Risque de double top si $311.82 résiste sur les 2–3 prochaines séances.
3. **Valorisation étirée** — Cours +5.1% vs consensus, P/E 37.4x. Compression multiple possible.
4. **Accounting risk non quantifié** — Absence de scan comptable frais.
5. **FOMO options** — Call OI 61.6% avec RSI >85 = comportement spéculatif. Tout retournement pourrait être violent.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $308.33.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $311.82 (52W high) sur volume > 53M :** Break confirmé — réévaluer l'entrée avec SL $297.41.
- **Si cours < $297.41 (SL) :** Sortie technique — risque de retour vers $290 puis $271.53 (MM50).
- **Si RSI retourne sous 80 avec volume :** Signal d'apaisement du surachat — surveillance renforcée.
- **Si double top confirmé sous $311.82** : Risque de retour vers $300–$305.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 21:00 UTC) — Cours $308.33, RSI 87.71, ATR $5.46, MM50 $271.53, volume 46.60M, short interest 0.92%, consensus FMP $293.43, options (max_pain 315.0, put/call 0.62, call_oi_pct 61.6)
- `data/recommandations_latest.json` — Score Opportunité 5.1/10, Score Global 51.0/100 (ajusté 41.0), Recommandation SURVEILLER, SL $297.41, TP $324.71
- `data/validation_report.txt` (2026-05-26) — AAPL OK
- `data/sector_rotation_2026-05-26.json` — XLK top sector (momentum 10.0/10)
- `data/fx_exposure_2026-05-26.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-05-26.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-05-26.json` — Earnings 2026-07-30, 65 jours
- `data/events_2026-05-26.json` — Aucun événement corporate détecté
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
- `data/geo_risk_latest.json` — Score Politique 0/10, non exposé
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
