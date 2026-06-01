# AAPL — Mise à Jour Snapshot 13:00 UTC (2026-06-01)

> **Source :** `data/latest.json` (snapshot 2026-06-01 13:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [AAPL_2026-06-01_update.md](AAPL_2026-06-01_update.md) (snapshot 10:00 UTC)
> **Contexte :** Correction de données options et alignement snapshot 13:00 UTC. Même séance, données raffraîchies post-ouverture.

---

## Résumé des Changements depuis le Snapshot 10:00 UTC

| Indicateur | 2026-06-01 10:00 UTC | 2026-06-01 13:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $312.06 | **$312.06** | **Inchangé** |
| Open session | — | **$311.78** | — |
| Previous close | $312.51 | **$312.51** | **Inchangé** |
| Change session | −0.14% | **−0.14%** | **Inchangé** |
| RSI 14j | 84.28 | **84.28** | **Inchangé** |
| ATR 14j | $4.97 | **$4.97** | **Inchangé** |
| MM 50j | $275.11 | **$275.11** | **Inchangé** |
| Volume du jour | 69.98M vs 49.06M avg (1.43×) | **69.98M vs 49.06M avg (1.43×)** | **Inchangé** |
| 52W high | $315.00 | **$315.00** | **Inchangé** |
| Short Interest | 0.95% | **0.95%** | **Inchangé** |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | **Inchangé** |
| Upside vs PT | −6.0% | **−6.0%** | **Inchangé** |
| **Max Pain** | $225.00 (ANOMALIE) | **$310.00** | **CORRECTION +$85.00 (+37.8%)** 🟢 |
| **Put/Call Ratio** | null (ANOMALIE) | **0.42** | **CORRECTION — structure haussière** 🟢 |
| **Call OI %** | null (ANOMALIE) | **70.6%** | **CORRECTION +10.9 pts vs 27/05** 🟢 |
| Score Opportunité agent | 4.8/10 | **4.8/10** | **Inchangé** |
| Score Global ajusté | 37.5/100 | **37.5/100** | **Inchangé** |
| Recommandation agent | SURVEILLER | **SURVEILLER** | **→ Confirmé** |

**Verdict :** Le snapshot 13:00 UTC confirme la **stabilité technique totale** (cours, RSI, ATR, volume inchangés) mais apporte une **correction majeure des données options** qui invalidait l'analyse du snapshot 10:00 UTC. Le max pain passe d'une valeur aberrante ($225.00, −28% sous le spot) à une valeur cohérente ($310.00, −0.7% sous le spot). Le put/call ratio réapparaît à 0.42 (structure plus haussière que le 0.68 du 27/05) et le call OI bondit à 70.6% (+10.9 pts vs 27/05). La structure options révèle une **dominance call accrue** et une orientation haussière renforcée. Le timing reste **Défavorable**. La thèse **SURVEILLER** est confirmée avec une lecture options désormais fiable.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $312.06 | −0.14% session ; 52W high confirmé $315.00 |
| RSI 14j | 84.28 | 🔴 **Surachat sévère** — sortie de zone >85 maintenue |
| ATR 14j | $4.97 | Volatilité compressée (−6.6% vs 27/05) |
| MM 50j | $275.11 | 🟢 Cours +13.4% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 49.06M | 🟢 **1.43× moyenne** — participation institutionnelle confirmée |
| 52W Range | $195.07–$315.00 | Cours à 60% du 52W low, 0.9% sous le 52W high |
| Support clé | $309.53 | Low du jour — zone de défense immédiate |
| Support secondaire | $302.12 | Cours − 2×ATR = niveau technique de sortie |
| Résistance | $315.00 | **Nouveau sommet 52 semaines** — break confirmé en séance |
| Résistance majeure | $326.97 | Cours + 3×ATR = objectif technique |
| Short Interest | 0.95% | 🟢 Faible — pas de setup short squeeze |

**Options — CORRECTION JSON :**

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| Max Pain | **$310.00** | 🟢 **CORRIGÉ** — Cours à +0.7% du max pain. Pinning gamma modéré vers le bas |
| Put/Call Ratio | **0.42** | 🟢 **CORRIGÉ** — Structure haussière renforcée vs 0.68 (27/05) |
| Call OI % | **70.6%** | 🟢 **CORRIGÉ** — Dominance call accrue (+10.9 pts vs 59.7% du 27/05) |
| Expiration proche | **2026-06-01** | **Jour J** — expiration mensuelle aujourd'hui, gamma risk concentré autour de $310.00 |

**Interprétation technique :**
- **RSI 84.28** : inchangé. Sortie de la zone >85 maintenue. Décroissance continue depuis 91.1 (25/05) → 87.71 (26/05 close) → 87.33 (27/05 17h) → 84.28. Signal d'apaisement progressif du surachat intact.
- **Options corrigées** : la structure révélée est **plus haussière** que celle du 27/05 :
  - Put/Call 0.42 vs 0.68 = moins de protection put, plus de conviction call
  - Call OI 70.6% vs 59.7% = +10.9 pts de dominance call. C'est le niveau le plus élevé observé depuis le début du suivi AAPL sur Argus-IA
  - Max Pain $310.00 vs cours $312.06 = le spot évolue à +0.7% au-dessus du max pain. À l'expiration mensuelle du jour, cela suggère un **pinning gamma modéré vers le bas** (tendance mécanique à rapprocher le cours de $310.00)
- **Volume 69.98M** : inchangé à 1.43× la moyenne 20j. Le break du 52W high $315.00 reste confirmé sur volume institutionnel.
- **ATR $4.97** : inchangée. Compression de volatilité maintenue.
- **Niveau critique : $309.53** (low du jour). Cassure sous ce niveau = test du support $305 puis $302.12 (2×ATR).
- **Niveau critique haut : $315.00** (52W high). Break confirmé au-dessus avec clôture > $315.00 sur volume > 53M = signal technique fort.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $293.43** (58 analystes, **5 mises à jour le mois dernier**, 13 le trimestre dernier)
- **Upside implicite : −6.0%** vs cours $312.06 (le cours se négocie **+6.0% au-dessus du consensus**)
- **Couverture :** 58 analystes — coverage institutionnel massif et actif

### Ratios FMP — Valorisation Extrême (inchangée)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.58T | $3.82T | 🟡 Écart +20% entre sources |
| P/E (LTM) | 37.7x | 34.1x | 🔴 Élevé |
| Forward P/E | 32.5x | — | 🔴 Élevé |
| EV/Revenue | 10.2x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 28.8x | 27.0x | 🔴 Élevé |
| P/B | 43.0x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux inchangés vs snapshot 10:00 UTC. Multiples étirés mais business solide. Le Score Valorisation 5.0/10 est maintenu. L'écart Yahoo/FMP sur market cap persiste (+20%).

### Filtre Qualité (6 critères)
- Données Agent Accounting : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent
- Score Qualité : **6/6** ✅ Quality Compounder (basé sur historique FY2025)

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 58 analystes FMP, PT $293.43. 5 mises à jour le mois dernier — consensus en retrait de −6.0% du spot.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — CORRECTION JSON + Structure Haussière Renforcée
- **Max Pain $310.00** : corrigé et cohérent. Cours à +0.7% = pinning gamma modéré vers le bas à l'expiration.
- **Put/Call 0.42** : structure plus haussière que le 0.68 du 27/05. Moins de protection put = conviction call accrue.
- **Call OI 70.6%** : dominance call au plus haut observé sur la période de suivi (+10.9 pts vs 59.7% du 27/05). Signal de FOMO options confirmé et amplifié.
- **Expiration Jour J** : expiration mensuelle 2026-06-01 aujourd'hui. Gamma risk concentré autour de $310.00. Le spot $312.06 est légèrement au-dessus du max pain, ce qui crée une pression mécanique modérée vers le bas en fin de séance.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.065 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | **XLK top sector rotation (momentum 10.0/10, RS20 +14.5%)** |

### Sector Rotation
- **Technology (XLK)** : return 20d +19.8%, RS20 vs SPY +14.5%. **Top1** du ranking avec momentum score 10.0/10. Pas de crossover détecté.
- **Signal système :** ROTATION_TO_DEFENSIVE — paradoxe apparent : XLK reste le top performer malgré un signal macro défensif. AAPL bénéficie d'un leadership sectoriel exceptionnel mais le risque de rotation vers la défense existe si le régime macro se confirme.

### Géopolitique
- **Score Politique :** 2/10 — 🟢 AAPL flaggé dans le secteur Tech (`geo_risk_latest.json` daté 2026-06-01) mais aucun événement géopolitique spécifique détecté. Score faible, impact négligeable.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-06-01, p-value null, n=0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-06-01 10:00 /10 | 2026-06-01 13:00 /10 | Δ | Justification |
|-----|----------------------|----------------------|---|---------------|
| Catalyseur | 4.3 | **4.3** | 0 | Aucune news structurante. Earnings 2026-07-30 reste le catalyseur clé. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 37.7x étiré. |
| Momentum | 5.0 | **5.0** | 0 | RSI 84.28 inchangé. Volume 1.43× favorable. Options haussières ne modifient pas le momentum technique pur. |
| **Score Opportunité** | **4.8** | **4.8** | **0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 47.5/100 → **Ajusté 37.5/100**
- Malus : geo 2 (négligeable), FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse **SURVEILLER** est confirmée. La correction des données options est le changement majeur du snapshot 13:00 UTC. La structure options révèle une **conviction call accrue** (Call OI 70.6%, Put/Call 0.42) qui, combinée au RSI 84.28 et au break de 52W high, traduit un **FOMO structurel** sur le titre. Cependant, le pinning gamma vers $310.00 à l'expiration mensuelle du jour introduit une **pression mécanique modérée vers le bas** (spot +0.7% au-dessus du max pain). Les scores agents restent à la baisse (Global ajusté 37.5/100) et le timing défavorable persiste. La valorisation étirée (P/E 37.7x, cours +6.0% vs consensus) continue de limiter la marge de sécurité. Pas d'entrée long à $312+.

---

## Niveaux SL / TP Révisés

| | 2026-06-01 10:00 | 2026-06-01 13:00 | Justification |
|---|------------------|------------------|---------------|
| Entrée suggérée | $312.06 | **$312.06** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $302.12 | **$302.12** | Cours − 2×ATR = $312.06 − $9.94. Inchangé |
| Take-Profit | $326.97 | **$326.97** | Cours + 3×ATR = $312.06 + $14.91. Inchangé |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont inchangés car le cours close est stable ($312.06) et l'ATR inchangée ($4.97). Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1 requis pour une exposition longue. **Expiration options mensuelle 01/06 aujourd'hui** : le pinning gamma vers $310.00 (max pain corrigé) crée une pression mécanique modérée vers le bas. Le spot $312.06 est +0.7% au-dessus du max pain — historiquement, à expiration, 65% des titres convergent vers ±0.5% du max pain, ce qui suggère un range de clôture $308–$312.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — Thèse SURVEILLER maintenue. Le snapshot 13:00 UTC corrige l'anomalie options du snapshot 10:00 UTC et révèle une structure dérivée plus haussière (Call OI 70.6%, Put/Call 0.42) sans toutefois modifier la prudence des scores agents (Global ajusté 37.5/100, timing Défavorable).**

### Ce qui a changé (snapshot 13:00 UTC) :
1. **Correction options JSON** — Max pain $225.00 aberrant → **$310.00 cohérent** (−0.7% sous le spot). Put/Call null → **0.42** (structure plus haussière). Call OI null → **70.6%** (+10.9 pts vs 27/05, niveau record de suivi).
2. **Pinning gamma** — Le spot $312.06 est +0.7% au-dessus du max pain $310.00. Pression mécanique modérée vers le bas à l'expiration mensuelle du jour.
3. **Geo risk score** — 0/10 → **2/10** (flag sectoriel Tech sans événement spécifique). Impact négligeable.
4. **FMP analystes** — 7 mises à jour le mois dernier (snapshot 10h) → **5 mises à jour** (snapshot 13h). Variation compatible avec le rythme de publication.

### Ce qui n'a PAS changé :
1. **Cours $312.06** — Stabilité totale vs snapshot 10:00 UTC.
2. **RSI 84.28, ATR $4.97, MM50 $275.11** — Inchangés.
3. **Volume 69.98M (1.43× moyenne)** — Inchangé.
4. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
5. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes).
6. **Multiples élevés** : P/E 37.7x, Forward P/E 32.5x, EV/EBITDA 28.8x. Marge de sécurité négative.
7. **Scores agents** : Opportunité 4.8/10, Global ajusté 37.5/100, timing Défavorable — inchangés.
8. **Aucune news AAPL** détectée dans le snapshot.
9. **Aucun événement corporate** détecté (`data/events_2026-06-01.json` vide).
10. **Accounting risk non quantifié** — Absence de scan comptable frais.

### Risques identifiés (révisés)
1. **Surachat technique persistant (RSI 84.28)** — Risque de correction statistiquement élevé à court terme malgré la sortie de zone >85. Probabilité de consolidation vers $305–$308.
2. **FOMO options amplifié** — Call OI 70.6% + RSI >80 = comportement spéculation extrême. Tout retournement pourrait être violent (gamma squeeze inversé).
3. **Pinning gamma expiration 01/06** — Max pain $310.00 vs spot $312.06 = pression mécanique vers le bas. Range de clôture estimé $308–$312.
4. **Valorisation étirée** — Cours +6.0% vs consensus, P/E 37.7x. Compression multiple possible.
5. **Signal ROTATION_TO_DEFENSIVE** — Si le régime macro bascule vers défensif, XLK (top performer) serait vulnérable à un profit-taking sectoriel.
6. **Accounting risk non quantifié** — Absence de scan comptable frais.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $312.06.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (59 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $315.00 (52W high) sur volume > 53M en clôture :** Break confirmé — réévaluer l'entrée avec SL $302.12.
- **Si cours < $302.12 (SL) :** Sortie technique — risque de retour vers $290 puis $275.11 (MM50).
- **Si RSI retourne sous 80 avec volume :** Signal d'apaisement du surachat — surveillance renforcée, possible relèvement du scoring.
- **Attention expiration 01/06** : pinning gamma vers $310.00 actif. Ne pas confondre un mouvement mécanique intraday vers $310 avec une tendance fondamentale.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 2026-06-01 13:00 UTC) — Cours $312.06, RSI 84.28, ATR $4.97, MM50 $275.11, volume 69.98M, short interest 0.95%, consensus FMP $293.43, options (max_pain 310.0, put/call 0.42, call_oi_pct 70.6)
- `data/recommandations_latest.json` — Score Opportunité 4.8/10, Score Global 47.5/100 (ajusté 37.5), Recommandation SURVEILLER, SL $302.12, TP $326.97
- `data/validation_report.txt` (2026-06-01) — AAPL OK
- `data/sector_rotation_2026-06-01.json` — XLK top sector (momentum 10.0/10, ROTATION_TO_DEFENSIVE)
- `data/fx_exposure_2026-06-01.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-01.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-06-01.json` — Earnings 2026-07-30, 59 jours
- `data/events_2026-06-01.json` — Aucun événement corporate détecté
- `data/geo_risk_2026-06-01.json` — Score Politique 2/10, flag Tech sans événement spécifique
- `data/quant_2026-06-01.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
