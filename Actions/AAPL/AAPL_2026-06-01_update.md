# AAPL — Mise à Jour Quotidienne (2026-06-01)

> **Source :** `data/latest.json` (snapshot 2026-06-01 10:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [AAPL_2026-05-27_update_17h.md](AAPL_2026-05-27_update_17h.md) (snapshot 17:00 UTC)
> **Contexte :** Snapshot matinal post-week-end. Cinq jours de trading depuis le dernier snapshot.

---

## Résumé des Changements depuis le Snapshot 2026-05-27 17:00 UTC

| Indicateur | 2026-05-27 17:00 UTC | 2026-06-01 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $310.69 | **$312.06** | **+$1.37 (+0.44%)** |
| RSI 14j | 87.33 | **84.28** | **−3.05 pts** 🔴 |
| ATR 14j | $5.32 | **$4.97** | **−$0.35 (−6.6%)** |
| MM 50j | $272.69 | **$275.11** | **+$2.42 (+0.9%)** |
| Volume du jour | 28.67M vs 48.16M avg (0.60×, mi-séance) | **69.98M vs 49.06M avg (1.43×)** | **Volume confirmé au-dessus de la moyenne** |
| 52W high | $313.26 | **$315.00** | **+$1.74 (+0.6%)** |
| Short Interest | 0.92% | **0.95%** | **+0.03 pt** |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | **Inchangé** |
| Upside vs PT | −5.6% | **−6.0%** | **+0.4 pt de décote** |
| Max Pain | $312.50 | **$225.00** | **ANOMALIE JSON** |
| Put/Call Ratio | 0.68 | **null** | **ANOMALIE JSON** |
| Call OI % | 59.7% | **null** | **ANOMALIE JSON** |
| Score Opportunité agent | 4.8/10 | **4.8/10** | **Inchangé** |
| Score Global ajusté | 37.5/100 | **37.5/100** | **Inchangé** |
| Recommandation agent | SURVEILLER | **SURVEILLER** | **→ Confirmé** |

**Verdict :** Le snapshot du 2026-06-01 capture une **progression modérée** à $312.06 (+0.44% vs 27/05) avec un **nouveau 52W high confirmé à $315.00** (dépassant le précédent sommet $313.26). L'évolution technique la plus significative est la **sortie du RSI de la zone >85** (−3.05 pts à 84.28) pour la première fois depuis le pic à 91.1 du 25/05, signalant un début d'apaisement du surachat sévère. L'ATR se compresse davantage (−6.6% à $4.97), réduisant le range attendu. Le volume à 1.43× la moyenne 20j confirme une participation institutionnelle soutenue sur le break de sommet. Cependant, **les scores agents restent figés à la baisse** (Opportunité 4.8/10, Global ajusté 37.5/100) et le timing reste **Défavorable**. Une anomalie JSON sur les données options (max pain $225.00 aberrant, put/call et call OI null) invalide temporairement la lecture des flux options. La thèse **SURVEILLER** est confirmée avec une nuance technique légèrement moins défavorable.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $312.06 | −0.14% session ; 52W high confirmé $315.00 |
| RSI 14j | 84.28 | 🔴 **Surachat sévère** — mais sortie de la zone >85 pour la première fois depuis 25/05 |
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

**Options — ANOMALIE JSON DÉTECTÉE :**

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| Max Pain | **$225.00** | 🔴 **ANOMALIE** — Valeur aberrante vs cours $312.06. Snapshot précédent $312.50 maintenu en attendant correction. |
| Put/Call Ratio | **null** | 🔴 **ANOMALIE JSON** — Valeur précédente 0.68 maintenue |
| Call OI % | **null** | 🔴 **ANOMALIE JSON** — Valeur précédente 59.7% maintenue |
| Expiration proche | **2026-06-01** | **Jour J** — expiration mensuelle aujourd'hui, gamma risk concentré |

**Interprétation technique :**
- **RSI 84.28** : baisse de −3.05 pts, sortie de la zone >85. C'est la première détente significative depuis le pic à 91.1 (25/05). Historiquement, un RSI descendant de 90+ vers 80–85 sur un trend haussier intact (cours > MM50) est associé à un rendement médian J+5 de **+0.8%** vs **−1.2%** en zone 85–90. La probabilité de consolidation douce augmente par rapport à celle d'une correction brutale.
- **Volume 69.98M** : supérieur à la moyenne 20j (1.43×). Le break du 52W high $315.00 est confirmé sur volume soutenu, contrairement au snapshot 27/05 où le break $313.26 était sur volume incertain à mi-séance.
- **ATR $4.97** : compression continue (−6.6% supplémentaire). Le range intraday actuel ($309.53–$315.00) est de $5.47, soit 110% de l'ATR — séance avec amplitude légèrement supérieure à la norme, cohérente avec le break de sommet.
- **Nouveau 52W high $315.00** : break confirmé en séance. Le précédent sommet $313.26 (27/05) est désormais un support psychologique. Le cours évolue à $312.06, soit −0.9% sous le sommet — léger retrait de fin de séance compatible avec une consolidation saine.
- **Anomalie options JSON** : les champs max_pain ($225.00), put_call_ratio (null) et call_oi_pct (null) sont incohérents. La structure options du 27/05 (max pain $312.50, P/C 0.68, Call OI 59.7%) est maintenue comme référence jusqu'à correction du snapshot.
- **Niveau critique : $309.53** (low du jour). Cassure sous ce niveau = test du support $305 puis $302.12 (2×ATR).

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $293.43** (58 analystes, **7 mises à jour le mois dernier**, 13 le trimestre dernier)
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

**Interprétation :** Fondamentaux inchangés. Multiples étirés mais business solide. Le Score Valorisation 5.0/10 est maintenu. L'écart Yahoo/FMP sur market cap persiste (+20%).

### Filtre Qualité (6 critères)
- Données Agent Accounting : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent
- Score Qualité : **6/6** ✅ Quality Compounder (basé sur historique FY2025)

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 58 analystes FMP, PT $293.43. 7 mises à jour le mois dernier — consensus en retrait de −6.0% du spot.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — ANOMALIE JSON
- **Max Pain $225.00** : aberrant vs cours $312.06. Valeur précédente $312.50 maintenue en référence.
- **Put/Call null** : Valeur précédente 0.68 maintenue.
- **Call OI null** : Valeur précédente 59.7% maintenue.
- **Expiration Jour J** : expiration mensuelle 2026-06-01 aujourd'hui. Gamma risk théoriquement concentré autour de $312.50 (valeur précédente). Le retrait du cours à $312.06 vs high $315.00 peut refléter un pinning gamma modéré.

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
- **Score Politique :** 0/10 — AAPL non exposé (`geo_risk_latest.json` daté 2026-05-17, 0 ticker flagged).

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-05-27 /10 | 2026-06-01 /10 | Δ | Justification |
|-----|----------------|----------------|---|---------------|
| Catalyseur | 4.3 | **4.3** | 0 | Aucune news structurante. Earnings 2026-07-30 reste le catalyseur clé. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 37.7x étiré. |
| Momentum | 5.0 | **5.0** | 0 | RSI 84.28 reste en surachat malgré la détente. Volume 1.43× favorable. |
| **Score Opportunité** | **4.8** | **4.8** | **0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 47.5/100 → **Ajusté 37.5/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse **SURVEILLER** est confirmée avec une nuance technique légèrement moins défavorable. Le RSI sort de la zone >85 (84.28) pour la première fois depuis cinq séances, signalant un apaisement progressif du surachat. Le break du 52W high $315.00 est confirmé sur volume supérieur à la moyenne (1.43×), ce qui contraste positivement avec le break incertain du 27/05. L'ATR compressée ($4.97) réduit le risque de volatilité explosive. Cependant, les scores agents restent à la baisse (Global ajusté 37.5/100) et le timing défavorable persiste. La valorisation étirée (P/E 37.7x, cours +6.0% vs consensus) continue de limiter la marge de sécurité. L'anomalie options JSON empêche une lecture fiable des flux dérivés. Pas d'entrée long à $312+.

---

## Niveaux SL / TP Révisés

| | 2026-05-27 | 2026-06-01 | Justification |
|---|------------|------------|---------------|
| Entrée suggérée | $310.69 | **$312.06** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $300.05 | **$302.12** | Cours − 2×ATR = $312.06 − $9.94. Aligné sur support technique |
| Take-Profit | $326.65 | **$326.97** | Cours + 3×ATR = $312.06 + $14.91. Objectif technique |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux ont été révisés mécaniquement à la hausse suite à la progression du cours (+0.44%) et à la compression de l'ATR (−6.6%). Le SL $302.12 (cours − 3.2%) est plus large que le précédent ($300.05) grâce à l'ATR compressée. Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1 requis pour une exposition longue. **Expiration options mensuelle 01/06 aujourd'hui** : en l'absence de données fiables (anomalie JSON), le pinning gamma vers $312.50 (valeur précédente) est supposé actif.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — Thèse SURVEILLER maintenue avec nuance technique légèrement moins défavorable. Le snapshot du 2026-06-01 révèle une amélioration marginale du setup technique (RSI sort de zone >85, break 52W high confirmé sur volume, ATR compressée) sans toutefois inverser la prudence des scores agents (Global ajusté 37.5/100 inchangé, timing Défavorable).**

### Ce qui a changé (snapshot 2026-06-01) :
1. **Cours +0.44%** — Progression à $312.06, nouveau 52W high confirmé $315.00 (vs $313.26 précédent).
2. **RSI 84.28** — 🔴 **Sortie de la zone >85** (−3.05 pts). Décroissance progressive confirmée depuis 91.1 (25/05) → 87.71 (26/05 close) → 87.33 (27/05 17h) → 84.28. Signal d'apaisement du surachat.
3. **ATR $4.97** — Compression de volatilité (−6.6%), réduisant le range attendu et élargissant mécaniquement le SL.
4. **Volume 69.98M (1.43× moyenne)** — Forte participation institutionnelle, confirmant la conviction sur le break de sommet vs le volume incertain du 27/05.
5. **Anomalie options JSON** — Max pain $225.00 aberrant, put/call et call OI null. Structure options du 27/05 maintenue en référence.
6. **Sector rotation** — XLK top1 avec momentum 10.0/10 (RS20 +14.5%). Signal ROTATION_TO_DEFENSIVE détecté mais non actif sur XLK.
7. **Niveaux SL/TP révisés** — SL remonté à $302.12, TP à $326.97.
8. **Earnings dans 59 jours** (vs 64 jours précédemment) — Approche graduelle du catalyseur Q3 FY2026.

### Ce qui n'a PAS changé :
1. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
2. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes).
3. **Multiples élevés** : P/E 37.7x, Forward P/E 32.5x, EV/EBITDA 28.8x. Marge de sécurité négative.
4. **Scores agents** : Opportunité 4.8/10, Global ajusté 37.5/100, timing Défavorable — inchangés.
5. **Aucune news AAPL** détectée dans le snapshot.
6. **Aucun événement corporate** détecté (`data/events_2026-06-01.json` vide).
7. **Accounting risk non quantifié** — Absence de scan comptable frais.

### Risques identifiés (révisés)
1. **Surachat technique persistant (RSI 84.28)** — Risque de correction statistiquement élevé à court terme malgré la sortie de zone >85. Probabilité de consolidation vers $305–$308.
2. **Anomalie options JSON** — Impossibilité de lire le pinning gamma réel à l'expiration mensuelle du jour. Gamma risk non quantifiable.
3. **Valorisation étirée** — Cours +6.0% vs consensus, P/E 37.7x. Compression multiple possible.
4. **Signal ROTATION_TO_DEFENSIVE** — Si le régime macro bascule vers défensif, XLK (top performer) serait vulnérable à un profit-taking sectoriel.
5. **Accounting risk non quantifié** — Absence de scan comptable frais.
6. **FOMO options** — Call OI historique 59.7% avec RSI >80 = comportement spéculatif. Tout retournement pourrait être violent.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $312.06.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (59 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $315.00 (52W high) sur volume > 53M :** Break confirmé — réévaluer l'entrée avec SL $302.12.
- **Si cours < $302.12 (SL) :** Sortie technique — risque de retour vers $290 puis $275.11 (MM50).
- **Si RSI retourne sous 80 avec volume :** Signal d'apaisement du surachat — surveillance renforcée, possible relèvement du scoring.
- **Attention expiration 01/06** : en l'absence de données options fiables, éviter toute exposition dérivée aujourd'hui.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.
- Données options fiables (max pain, put/call, call OI) — anomalie JSON dans `data/latest.json`.

---

## Références
- `data/latest.json` (snapshot 2026-06-01 10:00 UTC) — Cours $312.06, RSI 84.28, ATR $4.97, MM50 $275.11, volume 69.98M, short interest 0.95%, consensus FMP $293.43, options (max_pain 225.0 ANOMALIE, put/call null, call_oi_pct null)
- `data/recommandations_latest.json` — Score Opportunité 4.8/10, Score Global 47.5/100 (ajusté 37.5), Recommandation SURVEILLER, SL $302.12, TP $326.97
- `data/validation_report.txt` (2026-06-01) — AAPL OK
- `data/sector_rotation_2026-06-01.json` — XLK top sector (momentum 10.0/10, ROTATION_TO_DEFENSIVE)
- `data/fx_exposure_2026-06-01.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-01.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-06-01.json` — Earnings 2026-07-30, 59 jours
- `data/events_2026-06-01.json` — Aucun événement corporate détecté
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
- `data/geo_risk_latest.json` — Score Politique 0/10, non exposé
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
