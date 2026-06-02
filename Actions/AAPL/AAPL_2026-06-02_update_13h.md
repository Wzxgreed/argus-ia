# AAPL — Mise à Jour Snapshot 13:00 UTC (2026-06-02)

> **Source :** `data/latest.json` (snapshot 2026-06-02 13:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events, recommandation
> **Référence précédente :** [AAPL_2026-06-02_update.md](AAPL_2026-06-02_update.md) (snapshot 10:00 UTC)
> **Contexte :** Snapshot intra-journalier 13:00 UTC (09:00 NY — pré-ouverture US). Données post-correction de l'anomalie options détectée sur le snapshot 10:00 UTC.

---

## Résumé des Changements depuis le Snapshot 10:00 UTC (2026-06-02)

| Indicateur | 2026-06-02 10:00 UTC | 2026-06-02 13:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $306.31 | **$306.31** | **Inchangé** |
| Open session | $309.63 | **$309.63** | Inchangé |
| High du jour | $310.94 | **$310.94** | Inchangé |
| Low du jour | $305.02 | **$305.02** | Inchangé |
| RSI 14j | 70.58 | **70.58** | **Inchangé** |
| ATR 14j | $5.21 | **$5.21** | Inchangé |
| MM 50j | $276.26 | **$276.26** | Inchangé |
| Volume du jour | 48.80M vs 47.51M avg (1.03×) | **48.80M vs 47.51M avg (1.03×)** | Inchangé |
| 52W high | $315.00 | **$315.00** | Inchangé |
| Short Interest | 0.95% | **0.95%** | Inchangé |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes, 3 maj mois, 13 maj trim.)** | Inchangé |
| Upside vs PT | −4.0% | **−4.0%** | Inchangé |
| Max Pain | **$200.00** (anomalie) | **$315.00** | 🟢 **Anomalie RÉSOLUE** |
| Put/Call Ratio | **null** (corrompu) | **0.36** | 🟢 **Données restaurées** |
| Call OI % | **null** (corrompu) | **73.5%** | 🟢 **Données restaurées** |
| **Score Opportunité agent** | 5.1/10 | **5.1/10** | **Inchangé** |
| **Score Global ajusté** | 41.0/100 | **41.0/100** | **Inchangé** |
| **Recommandation agent** | SURVEILLER | **SURVEILLER** | → Confirmé |

**Verdict :** Le snapshot 13:00 UTC confirme la **stabilité totale** des données techniques par rapport au snapshot 10:00 UTC. Le changement majeur est la **résolution de l'anomalie options** détectée sur le snapshot 10h : les valeurs corrompues (max pain $200.00, P/C null, Call OI null) sont corrigées et cohérentes avec la structure de marché d'AAPL. La nouvelle structure options révèle une **dominance call encore plus prononcée** (Call OI 73.5%, P/C 0.36) qu'au close du 01/06 (Call OI 70.6%, P/C 0.42), avec un max pain repositionné à **$315.00** (le 52W high). L'échéance immédiate du 2026-06-03 (demain) crée un gamma risk concentré. Les scores agents, fondamentaux, consensus et niveaux macro restent strictement identiques.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $306.31 | −1.84% session du 01/06 ; repli depuis 52W high $315.00 |
| RSI 14j | 70.58 | 🟡 Surachat modéré — stable au-dessus du seuil 70 |
| ATR 14j | $5.21 | Volatilité stable |
| MM 50j | $276.26 | 🟢 Cours +10.9% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 47.51M | 🔴 **1.03× moyenne** — participation légèrement supérieure à la normale sur le repli du 01/06 |
| 52W Range | $195.07–$315.00 | Cours à 57% du 52W low, 2.8% sous le 52W high |
| Support clé | $305.02 | Low du jour — zone de défense immédiate, cassée = test de $302 |
| Support secondaire | $295.89 | Cours − 2×ATR = niveau technique de sortie (SL agent) |
| Résistance | $310.94 | High du jour — zone de rejet intraday |
| Résistance majeure | $315.00 | 52W high = max pain options — break nécessite volume > 50M en clôture |
| Résistance technique | $321.94 | Cours + 3×ATR = objectif technique (TP agent) |
| Short Interest | 0.95% | 🟢 Faible — pas de setup short squeeze |

**Options — ANOMALIE RÉSOLUE ✅**

| Métrique | Snapshot 10h UTC | Snapshot 13h UTC | Interprétation |
|----------|------------------|------------------|----------------|
| Max Pain | **$200.00** (anomalie) | **$315.00** | 🟢 Valeur corrigée, cohérente avec le 52W high. Spot −2.8% sous max pain → léger pinning gamma vers le bas |
| Put/Call Ratio | **null** (corrompu) | **0.36** | 🟢 Structure très haussière, en amélioration vs 0.42 du 01/06 |
| Call OI % | **null** (corrompu) | **73.5%** | 🟢 Dominance call record, en hausse vs 70.6% du 01/06 |
| Expiration | **2026-06-03** | **2026-06-03** | ⚠️ Échéance hebdomadaire demain — gamma risk imminent |

**Interprétation technique :**
- **RSI 70.58** : stable en surachat modéré. Aucun changement depuis le close du 01/06.
- **Volume 48.80M (1.03× moyenne)** : inchangé vs snapshot 10h. Le repli de −1.84% du 01/06 s'est effectué sur une participation légèrement supérieure à la normale — nuance défavorable confirmée.
- **Options corrigées — structure plus haussière** : la résolution de l'anomalie révèle une structure options **plus haussière** que celle du 01/06. Le put/call ratio passe de 0.42 à **0.36** (nouveau minimum observé sur la série), et le Call OI grimpe de 70.6% à **73.5%**. Cette extrême dominance call est un double tranchant : elle confirme la conviction haussière du marché options, mais amplifie le risque de dégarnissage gamma en cas de retournement.
- **Max pain $315.00** : repositionné exactement sur le 52W high. Le spot ($306.31) se situe −2.8% sous ce niveau, ce qui crée une dynamique de pinning gamma modérée vers le bas pour l'échéance du 2026-06-03. Les market makers ont un intérêt à ce que le cours se rapproche de $315.00 à l'expiration.
- **Échéance 2026-06-03 (demain)** : avec un max pain à $315.00 et une dominance call de 73.5%, le gamma risk est concentré. Un mouvement au-dessus de $315 pourrait déclencher un covering gamma haussier ; un mouvement sous $305 pourrait activer un covering baissier sur le put wing faible.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $293.43** (58 analystes, 3 mises à jour le mois dernier, 13 le trimestre dernier)
- **Upside implicite : −4.0%** vs cours $306.31
- **Couverture :** 58 analystes — coverage institutionnel massif et actif

### Ratios FMP — Valorisation inchangée
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.50T | $3.82T | 🟡 Écart +18% entre sources |
| P/E (LTM) | 37.0x | 34.1x | 🔴 Élevé |
| Forward P/E | 31.9x | — | 🔴 Élevé |
| EV/Revenue | 10.2x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 28.8x | 27.0x | 🔴 Élevé |
| P/B | 42.2x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples toujours étirés. Le Score Valorisation 5.0/10 est maintenu.

### Filtre Qualité (6 critères)
- Données Agent Accounting : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent
- Score Qualité : **6/6** ✅ Quality Compounder (basé sur historique FY2025)

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 58 analystes FMP, PT $293.43. Consensus en retrait de −4.0% du spot.
- **Aucun upgrade/downgrade** détecté dans le snapshot.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — ANOMALIE RÉSOLUE ✅
- **Max Pain $315.00** : cohérent, aligné sur le 52W high. Spot −2.8% sous max pain → pinning gamma modéré vers le bas.
- **Put/Call 0.36** : structure très haussière, en amélioration vs 0.42 du 01/06 (Call OI 70.6%).
- **Call OI 73.5%** : dominance call record, +2.9 pts vs 01/06. Risque de dégarnissage gamma en cas de retournement accru.
- **Échéance prochaine :** 2026-06-03 (demain) — gamma risk concentré autour de $315.00.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.065 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | **XLK top sector rotation (momentum 10.0/10, RS20 +15.7%)** |

### Sector Rotation
- **Technology (XLK)** : return 20d +20.9%, RS20 vs SPY +15.7%. **Top1** du ranking avec momentum score 10.0/10. Pas de crossover détecté.
- **Signal système :** ROTATION_TO_CYCLICAL — XLK reste le top performer.

### Géopolitique
- **Score Politique :** Non spécifique à AAPL. Aucun événement géopolitique détecté (`geo_risk_latest.json` daté 2026-05-17).

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0, n=0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-06-02 10h /10 | 2026-06-02 13h /10 | Δ | Justification |
|-----|--------------------|--------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucune news structurante. Résolution anomalie options = data quality, pas catalyseur. Earnings 2026-07-30 reste le catalyseur clé. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 37.0x étiré. |
| Momentum | 5.0 | **5.0** | 0 | RSI 70.58 stable en surachat modéré. Volume 1.03× = distribution réelle confirmée. Structure options plus haussière mais pas signal d'entrée. |
| **Score Opportunité** | **5.1** | **5.1** | **0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 51.0/100 → **Ajusté 41.0/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse **SURVEILLER** est confirmée sans changement de score. La résolution de l'anomalie options est une information positive pour la **qualité des données** mais ne modifie pas la thèse. La structure options révélée (Call OI 73.5%, P/C 0.36, max pain $315.00) est **plus haussière** que celle du 01/06, ce qui confirme la conviction du marché options mais représente aussi un **risque gamma accru** avec l'échéance du 2026-06-03 (demain). Le spot à $306.31 reste sous le max pain (−2.8%), ce qui crée une pression pinning modérée vers le bas à très court terme. La valorisation reste étirée (P/E 37.0x, cours +4.0% vs consensus) et le timing défavorable persiste. Les scores agents sont inchangés (Global ajusté 41.0/100), bien sous le seuil d'action (50). **Pas d'entrée long à $306.31.**

---

## Niveaux SL / TP Révisés

| | 2026-06-02 10:00 | 2026-06-02 13:00 | Justification |
|---|------------------|------------------|---------------|
| Entrée suggérée | $306.31 | **$306.31** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $295.89 | **$295.89** | Cours − 2×ATR = $306.31 − $10.42. Inchangé |
| Take-Profit | $321.94 | **$321.94** | Cours + 3×ATR = $306.31 + $15.63. Inchangé |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont inchangés car le cours close est stable ($306.31). Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1. **Le support $305.02** (low du jour) est la zone immédiate à surveiller : cassure = test du SL $295.89. **La résistance $310.94** (high du jour) doit être reclaimée pour envisager un retour vers le 52W high $315.00 (= max pain). **Attention gamma demain (2026-06-03)** : avec max pain à $315.00 et Call OI 73.5%, un mouvement au-dessus de $315 pourrait déclencher un covering gamma rapide ; inversement, une cassure de $305 sur volume > 50M pourrait activer le put wing faible.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE. Le snapshot 13:00 UTC confirme la thèse SURVEILLER (Global ajusté 41.0/100) avec stabilité totale des données techniques et résolution de l'anomalie options. La structure options corrigée révèle une dominance call encore plus prononcée (73.5% vs 70.6%), ce qui est neutre à légèrement négatif pour le timing à court terme (gamma risk demain).**

### Ce qui a changé (snapshot 13:00 UTC) :
1. **Anomalie options RÉSOLUE** — max pain corrigé $200.00 → **$315.00** (cohérent, aligné sur 52W high), put/call null → **0.36** (très haussier, −14.3% vs 0.42 du 01/06), call OI null → **73.5%** (+2.9 pts vs 70.6% du 01/06). [ANOMALIE DATA RÉSOLUE]
2. **Gamma risk 2026-06-03** — Avec max pain $315.00 et échéance demain, le pinning gamma est le facteur technique dominant du jour. Spot −2.8% sous max pain = pression modérée vers le bas à expiration.
3. **Earnings countdown** : 58 jours → inchangé (2026-07-30).

### Ce qui n'a PAS changé :
1. **Cours** — $306.31 inchangé.
2. **RSI 70.58 / ATR $5.21 / MM50 $276.26** — stabilité totale.
3. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
4. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes).
5. **Multiples élevés** : P/E 37.0x, Forward P/E 31.9x, EV/EBITDA 28.8x.
6. **Timing Défavorable** — maintenu par l'agent recommandation.
7. **Scores agents** — Opportunité 5.1/10, Global ajusté 41.0/100, SURVEILLER.
8. **Aucune news AAPL** détectée (`data/news_2026-06-02.json` vide).
9. **Aucun événement corporate** détecté (`data/events_2026-06-02.json` vide).
10. **Accounting risk non quantifié** — Absence de scan comptable frais.
11. **Volume normalisé (1.03×)** — Distribution réelle confirmée sur le repli du 01/06.
12. **Validation data** — AAPL OK (`validation_report.txt` 2026-06-02).

### Risques identifiés (révisés)
1. **Gamma risk 2026-06-03** — Max pain $315.00, Call OI 73.5%, échéance demain. Spot sous max pain = pinning modéré vers le bas. Surveiller l'open US pour détection de covering gamma.
2. **Support $305.02** — Low du jour. Cassure = test de $302 puis SL $295.89. Risque de retour vers MM50 $276.26 si breakdown confirmé sur volume > 50M.
3. **Dégarnissage gamma call** — Call OI 73.5% à un niveau record. Tout retournement sous $305 pourrait déclencher un unwinding rapide.
4. **Valorisation étirée** — P/E 37.0x, cours +4.0% vs consensus. Compression multiple possible si guidance décevante le 2026-07-30.
5. **Signal ROTATION_TO_CYCLICAL** — XLK reste top performer mais un pivot macro défensif reste un risque latérent.
6. **Accounting risk non quantifié** — Absence de scan comptable frais.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $306.31.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (58 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Gamma watch 2026-06-03 :** Surveiller l'interaction avec $315.00 (max pain) et $305.02 (support) à l'ouverture US et en fin de séance.
- **Si cours > $310.94 (high du jour) sur volume > 47M en clôture :** Reclaim de la zone de rejet — possible relèvement du scoring.
- **Si cours > $315.00 (52W high = max pain) sur volume > 50M en clôture :** Break confirmé — réévaluer l'entrée avec SL $295.89.
- **Si cours < $305.02 (low du jour) sur volume > 50M :** Support cassé — risque de test du SL $295.89 puis retour vers MM50 $276.26. Couverture gamma put faible pourrait amplifier la baisse.
- **Si RSI < 70 avec volume normalisé > 0.8× :** Signal d'apaisement complet du surachat — surveillance renforcée, possible relèvement du scoring vers ATTENDRE.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan Ratio) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 2026-06-02 13:00 UTC) — Cours $306.31, RSI 70.58, ATR $5.21, MM50 $276.26, volume 48.80M, short interest 0.95%, consensus FMP $293.43, options max_pain $315.00, put/call 0.36, call_oi_pct 73.5%
- `data/recommandations_latest.json` — Score Opportunité 5.1/10, Score Global 51.0/100 (ajusté 41.0), Recommandation SURVEILLER, SL $295.89, TP $321.94
- `data/validation_report.txt` (2026-06-02) — AAPL OK
- `data/sector_rotation_2026-06-02.json` — XLK top sector (momentum 10.0/10, ROTATION_TO_CYCLICAL)
- `data/fx_exposure_2026-06-02.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-02.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-06-02.json` — Earnings 2026-07-30, 58 jours
- `data/events_2026-06-02.json` — Aucun événement corporate détecté
- `data/news_2026-06-02.json` — Aucune news AAPL détectée
- `data/geo_risk_2026-05-17.json` — Aucun flag spécifique AAPL
- `data/quant_2026-05-17.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
