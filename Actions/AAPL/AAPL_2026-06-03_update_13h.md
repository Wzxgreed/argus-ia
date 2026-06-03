# AAPL — Mise à Jour Snapshot 13h UTC (2026-06-03)

> **Source :** `data/latest.json` (snapshot 2026-06-03 13:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events, recommandation
> **Référence précédente :** [AAPL_2026-06-03_update.md](AAPL_2026-06-03_update.md) (snapshot 10:00 UTC 2026-06-03)
> **Contexte :** Snapshot 13h UTC = ouverture US (9:30 EDT). Données de clôture 2026-06-02 confirmées ; options hebdomadaires expirent à la clôture aujourd'hui.

---

## Résumé des Changements depuis le Snapshot 10h UTC (2026-06-03)

| Indicateur | 2026-06-03 10:00 UTC | 2026-06-03 13:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $315.20 | **$315.20** | **Inchangé** |
| RSI 14j | 75.58 | **75.58** | Inchangé |
| ATR 14j | $5.67 | **$5.67** | Inchangé |
| MM 50j | $277.61 | **$277.61** | Inchangé |
| Volume 20j avg | 47.40M | **47.40M** | Inchangé |
| 52W high | $315.45 | **$315.45** | Inchangé |
| Short Interest | 0.95% | **0.95%** | Inchangé |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | Inchangé |
| **Max Pain (brut JSON)** | $200.00 (anomalie) | **$310.00** | 🟢 **Anomalie CORRIGÉE** |
| **Put/Call Ratio (brut JSON)** | null (anomalie) | **0.62** | 🟢 **Anomalie CORRIGÉE** |
| **Call OI % (brut JSON)** | null (anomalie) | **61.9%** | 🟢 **Anomalie CORRIGÉE** |
| Max Pain opérationnel (conservé) | $315.00 | **$310.00** | 🔴 **−$5.00 (−1.6%)** |
| Put/Call opérationnel (conservé) | 0.36 | **0.62** | 🔴 **+72% — moins haussier** |
| Call OI % opérationnel (conservé) | 73.5% | **61.9%** | 🔴 **−11.6 pts — moins haussier** |
| **Score Opportunité agent** | 4.8/10 | **4.8/10** | Inchangé |
| **Score Global ajusté** | 38.3/100 | **38.3/100** | Inchangé |
| **Recommandation agent** | SURVEILLER | **SURVEILLER** | → Confirmé |

**Verdict :** Le snapshot 13:00 UTC confirme la **stabilité totale des données prix et techniques** par rapport au snapshot 10:00 UTC. Le cours reste à **$315.20**, le RSI à **75.58**, l'ATR à **$5.67**. L'événement majeur est la **correction de l'anomalie options JSON** : les valeurs brutes sont désormais cohérentes (max pain $310.00, P/C 0.62, Call OI 61.9%). Cependant, **les valeurs opérationnelles révisées sont significativement moins haussières** que celles du 02/06 :
- Max pain **$310.00** (vs $315.00) = **−$5.20 sous le spot** → pinning gamma baissier à expiration
- Put/Call **0.62** (vs 0.36) = structure moins haussière, puts plus actifs
- Call OI **61.9%** (vs 73.5%) = dominance call en forte détente (−11.6 pts)

Cette révision structurelle des options est le **changement le plus significatif** de la séance. Elle indique que le sentiment options s'est refroidi par rapport au 02/06, et que les market makers ont un intérêt mécanique à ce que le cours se rapproche de **$310.00** à l'expiration d'aujourd'hui (2026-06-03). Les scores agents restent strictement inchangés (Opportunité 4.8/10, Global ajusté 38.3/100, SURVEILLER).

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $315.20 | Stable vs close 02/06 — consolidation au sommet |
| RSI 14j | 75.58 | 🟡 **Surachat modéré stable** — inchangé |
| ATR 14j | $5.67 | Volatilité stable — inchangée |
| MM 50j | $277.61 | 🟢 Cours +13.5% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j avg | 47.40M | Base de référence inchangée |
| 52W Range | $195.07–$315.45 | Cours à 99.9% du 52W high |
| Support clé | $306.69 | Low du 02/06 — zone de défense immédiate |
| Support secondaire | $303.86 | Cours − 2×ATR = niveau SL agent |
| Résistance | $315.45 | 52W high — break nécessite volume > 50M en clôture |
| Résistance technique | $332.21 | Cours + 3×ATR = objectif TP agent |
| Short Interest | 0.95% | 🟢 Faible — pas de setup short squeeze |

**Options — ANOMALIE CORRIGÉE + GAMMA RISK JOUR J (RÉVISÉ)**

| Métrique | Valeur brute 10h (JSON) | Valeur brute 13h (JSON) | Valeur opérationnelle (révisée) | Interprétation |
|----------|--------------------------|-------------------------|----------------------------------|----------------|
| Max Pain | $200.00 (anomalie) | **$310.00** | **$310.00** | 🟢 Corrigé — mais **$5.20 sous le spot** |
| Put/Call Ratio | null (anomalie) | **0.62** | **0.62** | 🟢 Corrigé — structure moins haussière |
| Call OI % | null (anomalie) | **61.9%** | **61.9%** | 🟢 Corrigé — dominance call en détente |
| Expiration | 2026-06-03 | **2026-06-03** | **2026-06-03** | ⚠️ **Échéance aujourd'hui** — gamma risk actif |

**Interprétation technique révisée :**
- **RSI 75.58** : surachat modéré stable. L'absence de variation depuis le 02/06 indique une consolidation du momentum haussier sans accélération ni détente.
- **Max Pain $310.00 vs Spot $315.20** : le décalage de **+$5.20 (+1.65%)** au-dessus du max pain est inhabituel à JOUR J. Les market makers ont un intérêt mécanique à ramener le cours vers $310.00 par le pinning gamma. Cela crée une **pression baissière implicite** de ~1.6% d'ici la clôture, sauf si un flux d'achat institutionnel domine le gamma unwinding.
- **Put/Call 0.62** : la structure reste globalement haussière (P/C < 1.0), mais nettement moins qu'hier (0.36). L'activité put a augmenté, signalant une couverture des longs ou des paris baissiers autour de l'expiration.
- **Call OI 61.9%** : en détente de 11.6 points par rapport au 73.5% du 02/06. Moins de call gamma à défendre au-dessus du spot, ce qui réduit le risque de covering gamma haussier en cas de break. Inversement, le put gamma sous $310 est plus épais qu'hier.
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

### Options — ANOMALIE CORRIGÉE + GAMMA RISK JOUR J (RÉVISÉ)
- **Max Pain $310.00** (corrigé) : **$5.20 sous le spot** → pinning gamma baissier à expiration.
- **Put/Call 0.62** (corrigé) : structure haussière atténuée vs 02/06 (0.36). Couverture put en hausse.
- **Call OI 61.9%** (corrigé) : dominance call en détente de 11.6 pts vs 02/06. Moins de gamma call à défendre au-dessus.
- **Échéance :** **2026-06-03 (aujourd'hui)** — gamma risk actif. La zone $310.00 est la cible mécanique des market makers. Surveillance accrue de l'ouverture US et de la dynamique d'expiration.

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

| Axe | 2026-06-03 10h /10 | 2026-06-03 13h /10 | Δ | Justification |
|-----|--------------------|--------------------|---|---------------|
| Catalyseur | 4.3 | **4.3** | 0 | Absence de catalyseur structurant, earnings 2026-07-30 à 57 jours. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 38.2x étiré. Cours +7.1% vs consensus. |
| Momentum | 5.3 | **5.3** | 0 | Breakout confirmé sur volume normalisé, mais RSI 75.58 et proximité 52W high pénalisent. |
| **Score Opportunité** | **4.8** | **4.8** | **0** | Pondération régime default 35/40/25 |

**Score Global Composite agent :** 48.3/100 → **Ajusté 38.3/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** Le snapshot 13:00 UTC du 2026-06-03 confirme la stabilité des données prix et techniques du snapshot 10:00 UTC. L'événement dominant est la **correction de l'anomalie options JSON** et la **révision à la baisse des métriques options** : max pain $310.00 (vs $315.00 opérationnel du 02/06), P/C 0.62 (vs 0.36), Call OI 61.9% (vs 73.5%). Cette détente de la structure options haussière, combinée à un max pain désormais **$5.20 sous le spot**, crée un **gamma risk baissier** à l'expiration d'aujourd'hui. Les market makers ont un intérêt mécanique à ramener le cours vers $310.00. **Pas d'entrée long à $315.20.** Surveillance accrue du comportement autour de $310.00 (max pain) et $315.45 (52W high).

---

## Niveaux SL / TP

| | 2026-06-03 10:00 | 2026-06-03 13:00 | Justification |
|---|------------------|------------------|---------------|
| Entrée suggérée | $315.20 | **$315.20** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $303.86 | **$303.86** | Cours − 2×ATR = $315.20 − $11.34. Inchangé |
| Take-Profit | $332.21 | **$332.21** | Cours + 3×ATR = $315.20 + $17.01. Inchangé |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont strictement inchangés car le cours ($315.20) et l'ATR ($5.67) n'ont pas varié. Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1. **Le support $306.69** (low du 02/06) est la zone immédiate à surveiller : cassure = retour vers le SL $303.86. **La résistance $315.45** (52W high) doit être breakée sur volume > 50M en clôture pour être crédible. **Attention gamma aujourd'hui (2026-06-03)** : avec max pain révisé à **$310.00** (vs $315.00 hier), la pression mécanique est désormais baissière. Un retour vers $310.00 serait cohérent avec le pinning gamma. Un break sous $310.00 sur volume élevé activerait le put wing et pourrait accélérer la baisse vers $306.69.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec NUANCE GAMMA NÉGATIVE.** Le snapshot 13:00 UTC du 2026-06-03 confirme intégralement la thèse **SURVEILLER** établie à la clôture du 2026-06-02 et au snapshot 10:00 UTC. Les données prix, RSI, ATR, volume et scores agents sont strictement inchangés. Cependant, la **correction de l'anomalie options JSON** révèle une **structure options moins haussière** que prévu :

### Ce qui n'a PAS changé (stabilité dominante) :
1. **Cours $315.20** — inchangé vs close 02/06.
2. **RSI 75.58** — surachat modéré stable.
3. **ATR $5.67** — volatilité stable.
4. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
5. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes).
6. **Multiples élevés** : P/E 38.2x, Forward P/E 32.8x, EV/EBITDA 29.0x.
7. **Scores agents** : Opportunité 4.8/10, Global ajusté 38.3/100 — strictement inchangés.
8. **Timing Défavorable** — maintenu par l'agent recommandation.
9. **Aucune news AAPL** détectée (`data/news_2026-06-03.json` vide).
10. **Aucun événement corporate** détecté (`data/events_2026-06-03.json` vide).
11. **XLK top sector** — momentum 10.0/10, signal NEUTRAL.
12. **FX Exposure Score 0.0** — neutral.
13. **Validation data** — AAPL OK (`validation_report.txt` 2026-06-03).

### Ce qui a changé (nuance gamma négative) :
1. **Anomalie options JSON CORRIGÉE** — max pain $310.00, P/C 0.62, Call OI 61.9% (données valides et cohérentes).
2. **Max pain révisé à $310.00** (vs $315.00 opérationnel du 02/06) = **$5.20 sous le spot** → pinning gamma baissier à expiration.
3. **Put/Call révisé à 0.62** (vs 0.36) = couverture put en hausse, structure moins haussière.
4. **Call OI révisé à 61.9%** (vs 73.5%) = dominance call en forte détente, moins de gamma haussier à défendre.
5. **Échéance options 2026-06-03** — JOUR J. Gamma risk actif avec pression mécanique vers $310.00.

### Risques identifiés (révisés)
1. **Gamma risk JOUR J révisé BAISSIER (2026-06-03)** — Max pain $310.00, Call OI 61.9%, échéance aujourd'hui. Spot à +1.65% du max pain = **pression gamma baissière**. Surveiller l'interaction avec $310.00 et $315.45.
2. **RSI 75.58** — Surachat modéré stable. Tout retournement sous $306.69 pourrait déclencher une correction technique vers $303.86 (SL).
3. **Support $306.69** — Low du 02/06. Cassure = retour vers $303.86 puis test MM50 $277.61.
4. **Valorisation étirée** — P/E 38.2x, cours +7.1% vs consensus. Compression multiple possible si guidance décevante le 2026-07-30.
5. **Dégarnissage gamma call** — Call OI en détente de 11.6 pts. Moins de support gamma au-dessus du spot ; un retournement pourrait être plus rapide.
6. **Signal NEUTRAL sector rotation** — XLK reste top performer mais pas de rotation active détectée.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $315.20.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (57 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Gamma watch JOUR J (2026-06-03) révisé :** Surveiller l'interaction avec **$310.00** (max pain révisé — cible mécanique baissière) et **$315.45** (52W high). La pression gamma est désormais baissière ; un retour vers $310.00 est mécaniquement cohérent.
- **Si cours > $315.45 (52W high) sur volume > 50M en clôture :** Break confirmé — réévaluer l'entrée avec SL $303.86. Nécessiterait un flux d'achat institutionnel dominant le gamma pinning.
- **Si cours < $310.00 (max pain) sur volume > 50M :** Pinning gamma cassé vers le bas — risque de test du support $306.69 puis du SL $303.86. Le put wing à $310 est plus épais qu'hier (P/C 0.62).
- **Si cours < $306.69 (low 02/06) sur volume > 50M :** Support cassé — risque de test du SL $303.86 puis retour vers MM50 $277.61.
- **Si RSI redescend < 70 avec volume normalisé > 0.8× :** Signal d'apaisement du surachat — surveillance renforcée, possible relèvement du scoring.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan Ratio) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 2026-06-03 13:00 UTC) — Cours $315.20, RSI 75.58, ATR $5.67, MM50 $277.61, volume 44.42M, short interest 0.95%, consensus FMP $293.43, options max_pain $310.00, P/C 0.62, Call OI 61.9%
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
