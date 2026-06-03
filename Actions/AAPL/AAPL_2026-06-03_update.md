# AAPL — Mise à Jour Snapshot 10h UTC (2026-06-03)

> **Source :** `data/latest.json` (snapshot 2026-06-03 10:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events, recommandation
> **Référence précédente :** [AAPL_2026-06-02_update.md](AAPL_2026-06-02_update.md) (snapshot final 21:00 UTC 2026-06-02)
> **Contexte :** Snapshot matinal pré-ouverture US. Données de clôture 2026-06-02 confirmées.

---

## Résumé des Changements depuis le Snapshot Final 21:00 UTC (2026-06-02)

| Indicateur | 2026-06-02 21:00 UTC | 2026-06-03 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $315.20 | **$315.20** | **Inchangé** |
| RSI 14j | 75.58 | **75.58** | Inchangé |
| ATR 14j | $5.67 | **$5.67** | Inchangé |
| MM 50j | $277.61 | **$277.61** | Inchangé |
| Volume du jour | 44.37M vs 47.40M avg (0.94×) | **44.42M vs 47.40M avg (0.94×)** | Inchangé |
| 52W high | $315.45 | **$315.45** | Inchangé — nouveau high confirmé |
| Short Interest | 0.95% | **0.95%** | Inchangé |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | Inchangé |
| Upside vs PT | −7.1% | **−7.1%** | Inchangé |
| Max Pain | $315.00 | **$200.00** | 🔴 **Anomalie JSON détectée** |
| Put/Call Ratio | 0.36 | **null** | 🔴 Anomalie JSON |
| Call OI % | 73.5% | **null** | 🔴 Anomalie JSON |
| **Score Opportunité agent** | 4.8/10 | **4.8/10** | Inchangé |
| **Score Global ajusté** | 38.3/100 | **38.3/100** | Inchangé |
| **Recommandation agent** | SURVEILLER | **SURVEILLER** | → Confirmé |

**Verdict :** Le snapshot 10:00 UTC du 2026-06-03 confirme une **stabilité totale** par rapport à la clôture du 2026-06-02. Le cours reste à **$315.20**, le RSI à **75.58** en surachat modéré stable, l'ATR à **$5.67**, et le volume final à **0.94× la moyenne 20j** (44.42M vs 47.40M), confirmant la distribution réelle du breakout haussier de la veille. **Anomalie options JSON détectée** (max pain $200.00, P/C et Call OI null) — identique au snapshot 10:00 UTC du 2026-06-02. Les valeurs opérationnelles du 02/06 (max pain $315.00, P/C 0.36, Call OI 73.5%) sont conservées. L'échéance hebdomadaire des options est aujourd'hui (**2026-06-03**), ce qui concentre le gamma risk autour du max pain $315.00. Les scores agents sont strictement inchangés (Opportunité 4.8/10, Global ajusté 38.3/100, SURVEILLER). Aucune news AAPL détectée. Aucun événement corporate. Aucun changement fondamental.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $315.20 | Stable vs close 02/06 — consolidation au sommet |
| RSI 14j | 75.58 | 🟡 **Surachat modéré stable** — inchangé depuis le 02/06 |
| ATR 14j | $5.67 | Volatilité stable — inchangée |
| MM 50j | $277.61 | 🟢 Cours +13.5% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 47.40M | 🟢 **0.94× moyenne** — participation institutionnelle confirmée |
| 52W Range | $195.07–$315.45 | Cours à 99.9% du 52W high |
| Support clé | $306.69 | Low du 02/06 — zone de défense immédiate |
| Support secondaire | $306.72 | Low du snapshot 17h 02/06 — cassure = test $303.86 |
| Support technique | $303.86 | Cours − 2×ATR = niveau SL agent |
| Résistance | $315.45 | 52W high — break nécessite volume > 50M en clôture |
| Résistance technique | $332.21 | Cours + 3×ATR = objectif TP agent |
| Short Interest | 0.95% | 🟢 Faible — pas de setup short squeeze |

**Options — ANOMALIE JSON + GAMMA RISK JOUR J**

| Métrique | Valeur brute (JSON) | Valeur opérationnelle (conservée) | Interprétation |
|----------|---------------------|-----------------------------------|----------------|
| Max Pain | $200.00 | **$315.00** | 🔴 Anomalie JSON aberrante — valeur 02/06 conservée |
| Put/Call Ratio | null | **0.36** | 🔴 Anomalie JSON — structure très haussière stable |
| Call OI % | null | **73.5%** | 🔴 Anomalie JSON — dominance call record stable |
| Expiration | 2026-06-03 | **2026-06-03** | ⚠️ **Échéance aujourd'hui** — gamma risk maximal |

**Interprétation technique :**
- **RSI 75.58** : surachat modéré stable. L'absence de variation depuis le 02/06 indique une consolidation du momentum haussier sans accélération ni détente. Le risque de correction technique persiste tant que le RSI reste > 70.
- **Volume 44.42M (0.94×)** : participation normale confirmée. Le volume collapse du snapshot 17h (0.39×) a été entièrement invalidé par la clôture à 0.94×. La distribution est réelle et institutionnelle.
- **ATR $5.67** : volatilité stable. La fourchette du 02/06 ($306.69–$315.45) = 1.54× ATR, large mais cohérente avec un breakout sur 52W high.
- **52W high $315.45** : le cours à $315.20 se situe à −0.08% du sommet. La résistance est psychologique et technique. Un break au-dessus sur volume > 50M en clôture ouvrirait la voie vers le TP $332.21.
- **Spot vs max pain** : $315.20 est à +0.06% du max pain opérationnel $315.00. Avec l'échéance **aujourd'hui (2026-06-03)** et une dominance call de 73.5%, les market makers ont un intérêt maximal à maintenir le cours proche de $315.00. La zone $314.80–$315.20 est un champ de bataille gamma. Tout écart significatif au-dessus pourrait déclencher un covering gamma haussier ; un retour sous $314.00 activerait le put wing faible.
- **MM50 $277.61** : la tendance haussière reste intacte avec un écart de +13.5%. Seul un retour sous $306 sur volume élevé remettrait en cause la tendance.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $293.43** (58 analystes, 3 mises à jour le mois dernier)
- **Upside implicite : −7.1%** vs cours $315.20
- **Couverture :** 58 analystes — coverage institutionnel massif et actif

### Ratios FMP — Valorisation inchangée
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.63T | $3.82T | 🟡 Écart +21% entre sources |
| P/E (LTM) | 38.2x | 34.1x | 🔴 Élevé |
| Forward P/E | 32.8x | — | 🔴 Élevé |
| EV/Revenue | 10.3x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 29.0x | 27.0x | 🔴 Élevé |
| P/B | 43.4x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples toujours étirés, avec un upside vs consensus à −7.1% (cours éloigné du PT). Le Score Valorisation 5.0/10 est maintenu. Filtre Qualité 6/6 ✅ Quality Compounder (basé sur historique FY2025).

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 58 analystes FMP, PT $293.43. Consensus en retrait de −7.1% du spot.
- **Aucun upgrade/downgrade** détecté dans le snapshot.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — ANOMALIE JSON + GAMMA RISK JOUR J
- **Max Pain $315.00** (opérationnel) : inchangé, aligné sur le 52W high. Spot à +0.06% → pinning gamma maximal à l'expiration aujourd'hui.
- **Put/Call 0.36** : structure très haussière stable.
- **Call OI 73.5%** : dominance call record stable. Risque de dégarnissage gamma en cas de retournement inchangé.
- **Échéance :** **2026-06-03 (aujourd'hui)** — gamma risk concentré autour de $315.00. Surveillance accrue de l'ouverture US et de la dynamique d'expiration.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.065 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | **XLK top sector rotation (momentum 10.0/10, RS20 +16.53%)** |

### Sector Rotation
- **Technology (XLK)** : return 20d +22.31%, RS20 vs SPY +16.53%. **Top1** du ranking avec momentum score 10.0/10. Pas de crossover détecté.
- **Signal système :** NEUTRAL (régime UNKNOWN).

### Géopolitique
- **Score Politique :** Non spécifique à AAPL. Aucun événement géopolitique détecté (`geo_risk_latest.json` daté 2026-05-17).

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0, n=0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-06-02 21h /10 | 2026-06-03 10h /10 | Δ | Justification |
|-----|--------------------|--------------------|---|---------------|
| Catalyseur | 4.3 | **4.3** | 0 | Absence de catalyseur structurant, earnings 2026-07-30 à 57 jours. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 38.2x étiré. Cours +7.1% vs consensus. |
| Momentum | 5.3 | **5.3** | 0 | Breakout confirmé sur volume normalisé, mais RSI 75.58 et proximité 52W high pénalisent. |
| **Score Opportunité** | **4.8** | **4.8** | **0** | Pondération régime default 35/40/25 |

**Score Global Composite agent :** 48.3/100 → **Ajusté 38.3/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** Le snapshot 10:00 UTC du 2026-06-03 confirme l'intégralité de la configuration technique et fondamentale du 2026-06-02. La stabilité est le signal dominant : cours, RSI, ATR, volume, consensus, scores agents — tous inchangés. L'unique événement notable est l'**expiration des options hebdomadaires aujourd'hui (2026-06-03)** avec un max pain à $315.00 et une dominance call record (73.5%), ce qui crée un pinning gamma maximal autour du spot actuel ($315.20). L'anomalie options JSON (max pain $200.00) est identique à celle du snapshot 10:00 UTC du 02/06 et doit être ignorée au profit des valeurs opérationnelles du 02/06. **Pas d'entrée long à $315.20.**

---

## Niveaux SL / TP

| | 2026-06-02 21:00 | 2026-06-03 10:00 | Justification |
|---|------------------|------------------|---------------|
| Entrée suggérée | $315.20 | **$315.20** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $303.86 | **$303.86** | Cours − 2×ATR = $315.20 − $11.34. Inchangé |
| Take-Profit | $332.21 | **$332.21** | Cours + 3×ATR = $315.20 + $17.01. Inchangé |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont strictement inchangés car le cours ($315.20) et l'ATR ($5.67) n'ont pas varié. Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1. **Le support $306.69** (low du 02/06) est la zone immédiate à surveiller : cassure = retour vers le SL $303.86. **La résistance $315.45** (52W high) doit être breakée sur volume > 50M en clôture pour être crédible. **Attention gamma aujourd'hui (2026-06-03)** : avec max pain à $315.00 et Call OI 73.5%, la zone $314.80–$315.20 est un champ de bataille. Un break au-dessus de $315.45 pourrait déclencher un covering gamma haussier ; une cassure de $306.69 sur volume > 50M pourrait activer le put wing faible.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE.** Le snapshot 10:00 UTC du 2026-06-03 confirme intégralement la thèse **SURVEILLER** établie à la clôture du 2026-06-02. Aucun changement significatif n'est enregistré sur les données techniques, fondamentales, de sentiment ou de scoring. La stabilité totale est le signal dominant.

### Ce qui n'a PAS changé (stabilité totale) :
1. **Cours $315.20** — inchangé vs close 02/06.
2. **RSI 75.58** — surachat modéré stable.
3. **ATR $5.67** — volatilité stable.
4. **Volume 44.42M (0.94×)** — participation institutionnelle confirmée.
5. **52W high $315.45** — nouveau sommet confirmé.
6. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
7. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes).
8. **Multiples élevés** : P/E 38.2x, Forward P/E 32.8x, EV/EBITDA 29.0x.
9. **Scores agents** : Opportunité 4.8/10, Global ajusté 38.3/100 — strictement inchangés.
10. **Timing Défavorable** — maintenu par l'agent recommandation.
11. **Structure options opérationnelle** — max pain $315.00, P/C 0.36, Call OI 73.5%.
12. **Aucune news AAPL** détectée (`data/news_2026-06-03.json` vide).
13. **Aucun événement corporate** détecté (`data/events_2026-06-03.json` vide).
14. **XLK top sector** — momentum 10.0/10, signal NEUTRAL.
15. **FX Exposure Score 0.0** — neutral.
16. **Validation data** — AAPL OK (`validation_report.txt` 2026-06-03).

### Ce qui a changé (alertes et anomalies) :
1. **Anomalie options JSON** — max pain $200.00, P/C null, Call OI null (identique au snapshot 10h 02/06). Valeurs opérationnelles du 02/06 conservées ($315.00 / 0.36 / 73.5%).
2. **Échéance options 2026-06-03** — JOUR J. Gamma risk maximal autour de $315.00. Surveillance accrue de l'ouverture US et de la dynamique d'expiration.

### Risques identifiés (inchangés)
1. **Gamma risk JOUR J (2026-06-03)** — Max pain $315.00, Call OI 73.5%, échéance aujourd'hui. Spot à +0.06% du max pain = tension gamma maximale. Surveiller l'interaction avec $315.00 et $315.45.
2. **RSI 75.58** — Surachat modéré stable. Tout retournement sous $306.69 pourrait déclencher une correction technique vers $303.86 (SL).
3. **Support $306.69** — Low du 02/06. Cassure = retour vers $303.86 puis test MM50 $277.61.
4. **Valorisation étirée** — P/E 38.2x, cours +7.1% vs consensus. Compression multiple possible si guidance décevante le 2026-07-30.
5. **Dégarnissage gamma call** — Call OI 73.5% à niveau record. Tout retournement sous $305 pourrait déclencher un unwinding rapide post-expiration.
6. **Signal NEUTRAL sector rotation** — XLK reste top performer mais pas de rotation active détectée.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $315.20.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (57 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Gamma watch JOUR J (2026-06-03) :** Surveiller l'interaction avec $315.00 (max pain) et $315.45 (52W high) à l'ouverture US et en fin de séance d'expiration.
- **Si cours > $315.45 (52W high) sur volume > 50M en clôture :** Break confirmé — réévaluer l'entrée avec SL $303.86.
- **Si cours < $306.69 (low 02/06) sur volume > 50M :** Support cassé — risque de test du SL $303.86 puis retour vers MM50 $277.61. Couverture gamma put faible pourrait amplifier la baisse post-expiration.
- **Si RSI redescend < 70 avec volume normalisé > 0.8× :** Signal d'apaisement du surachat — surveillance renforcée, possible relèvement du scoring.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan Ratio) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 2026-06-03 10:00 UTC) — Cours $315.20, RSI 75.58, ATR $5.67, MM50 $277.61, volume 44.42M, short interest 0.95%, consensus FMP $293.43, options max_pain $200.00 (anomalie), null P/C et Call OI
- `data/recommandations_latest.json` — Score Opportunité 4.8/10, Score Global 48.3/100 (ajusté 38.3), Recommandation SURVEILLER, SL $303.86, TP $332.21
- `data/validation_report.txt` (2026-06-03) — AAPL OK
- `data/sector_rotation_2026-06-03.json` — XLK top sector (momentum 10.0/10, NEUTRAL)
- `data/fx_exposure_2026-06-03.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-03.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-06-03.json` — Earnings 2026-07-30, 57 jours
- `data/events_2026-06-03.json` — Aucun événement corporate détecté
- `data/news_2026-06-03.json` — Aucune news AAPL détectée
- `data/geo_risk_2026-05-17.json` — Aucun flag spécifique AAPL
- `data/quant_2026-05-17.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
