# AAPL — Mise à Jour Snapshot 10:00 UTC (2026-06-02)

> **Source :** `data/latest.json` (snapshot 2026-06-02 10:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events, recommandation
> **Référence précédente :** [AAPL_2026-06-01_update_21h.md](AAPL_2026-06-01_update_21h.md) (snapshot final 21:00 UTC)
> **Contexte :** Snapshot pré-ouverture US (10:00 UTC = 06:00 NY). Données techniques reflètent la clôture du 2026-06-01 avec ajustements de reporting post-close.

---

## Résumé des Changements depuis le Snapshot 21:00 UTC (2026-06-01)

| Indicateur | 2026-06-01 21:00 UTC | 2026-06-02 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $306.31 | **$306.31** | **Inchangé** |
| Open session | $309.625 | **$309.63** | +$0.005 |
| High du jour | $310.93 | **$310.94** | +$0.01 |
| Low du jour | $305.03 | **$305.02** | −$0.01 |
| Previous close | $312.06 | **$312.06** | Inchangé |
| RSI 14j | 70.58 | **70.58** | **Inchangé** |
| ATR 14j | $5.21 | **$5.21** | **Inchangé** |
| MM 50j | $276.26 | **$276.26** | Inchangé |
| Volume du jour | 44.17M vs 47.27M avg (0.93×) | **48.80M vs 47.51M avg (1.03×)** | **+10.5%** 🔴 |
| 52W high | $315.00 | **$315.00** | Inchangé |
| Short Interest | 0.95% | **0.95%** | Inchangé |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes, 3 maj mois, 13 maj trim.)** | Inchangé |
| Upside vs PT | −4.0% | **−4.0%** | Inchangé |
| Max Pain | $310.00 | **$200.00** | 🔴 **Anomalie data** |
| Put/Call Ratio | 0.42 | **null** | 🔴 **Données corrompues** |
| Call OI % | 70.6% | **null** | 🔴 **Données corrompues** |
| **Score Opportunité agent** | 5.1/10 | **5.1/10** | **Inchangé** |
| **Score Global ajusté** | 41.0/100 | **41.0/100** | **Inchangé** |
| **Recommandation agent** | SURVEILLER | **SURVEILLER** | → Confirmé |

**Verdict :** Le snapshot 10:00 UTC du 2026-06-02 reflète une **stabilité totale** des données techniques par rapport au close du 2026-06-01 — cohérent avec un marché US encore fermé à cette heure. Le seul mouvement notable est l'ajustement du volume de séance à **48.80M (1.03× la moyenne 20j)** vs 44.17M (0.93×) rapporté hier soir. Ce recalcul post-close confirme que la distribution de −1.84% du 01/06 s'est effectuée sur une participation légèrement **supérieure** à la moyenne, renforçant l'interprétation d'une pression vendeuse réelle. **Données options corrompues détectées** (max pain $200.00, null P/C et Call OI) — ces valeurs sont absurdes pour un cours à $306 et doivent être ignorées. Les scores agents, le consensus analyste, les fondamentaux et les niveaux macro sont strictement identiques.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $306.31 | −1.84% session du 01/06 ; repli depuis 52W high $315.00 |
| RSI 14j | 70.58 | 🟡 Surachat modéré — stable au-dessus du seuil 70 |
| ATR 14j | $5.21 | Volatilité stable |
| MM 50j | $276.26 | 🟢 Cours +10.9% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 47.51M | 🔴 **1.03× moyenne** — participation légèrement supérieure à la moyenne (ajustement post-close) |
| 52W Range | $195.07–$315.00 | Cours à 57% du 52W low, 2.8% sous le 52W high |
| Support clé | $305.02 | Low du jour — zone de défense immédiate, cassée = test de $302 |
| Support secondaire | $295.89 | Cours − 2×ATR = niveau technique de sortie (SL agent) |
| Résistance | $310.94 | High du jour — zone de rejet intraday |
| Résistance majeure | $315.00 | 52W high — break nécessite volume > 50M en clôture |
| Résistance technique | $321.94 | Cours + 3×ATR = objectif technique (TP agent) |
| Short Interest | 0.95% | 🟢 Faible — pas de setup short squeeze |

**Options — DONNÉES CORROMPUES ⚠️**

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| Max Pain | **$200.00** | 🔴 Anomalie data — valeur absurde pour un cours à $306.31. Ignorer. |
| Put/Call Ratio | **null** | 🔴 Données corrompues — non exploitables. |
| Call OI % | **null** | 🔴 Données corrompues — non exploitables. |
| Expiration | **2026-06-03** | Échéance hebdomadaire prochaine |

**Interprétation technique :**
- **RSI 70.58** : stable en surachat modéré. Pas de changement depuis le close du 01/06.
- **Volume 48.80M** : ajustement post-close du 01/06. Le recalcul porte le ratio à **1.03× la moyenne 20j**, confirmant que le repli de −1.84% s'est effectué sur une participation légèrement supérieure à la normale. C'est une nuance défavorable qui renforce l'hypothèse de distribution réelle plutôt qu'un simple repli technique sans conviction.
- **Low $305.02** : quasi-identique au $305.03 rapporté hier. Support immédiat inchangé.
- **ATR $5.21** : stable, reflétant un range intraday maîtrisé ($305.02–$310.94 = $5.92).
- **Options corrompues** : le snapshot du 02/06 10h UTC retourne des données options non fiables (max pain $200, null pour P/C et Call OI). Ces valeurs sont incohérentes avec la structure de marché d'AAPL. **La structure options réelle reste celle du 01/06** : max pain $310.00, P/C 0.42, Call OI 70.6% (dominance call record). [DONNÉES OPTIONS CORROMPUES]

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

### Options — DONNÉES CORROMPUES
- **Max Pain $200.00** : valeur incohérente, absurde pour un cours à $306. [ANOMALIE DATA]
- **Put/Call null / Call OI null** : données non récupérées par le worker.
- **Référence structure options :** Les dernières données fiables restent celles du 2026-06-01 13:00 UTC : max pain $310.00, P/C 0.42, Call OI 70.6%. La dominance call record persiste pour les échéances suivantes.
- **Échéance prochaine :** 2026-06-03 (hebdomadaire) — gamma risk limité.

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
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value null, n=0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-06-01 21h /10 | 2026-06-02 10h /10 | Δ | Justification |
|-----|--------------------|--------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucune news structurante. Earnings 2026-07-30 reste le catalyseur clé. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 37.0x étiré. |
| Momentum | 5.0 | **5.0** | 0 | RSI 70.58 stable en surachat modéré. Volume ajusté 1.03× = distribution réelle. |
| **Score Opportunité** | **5.1** | **5.1** | **0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 51.0/100 → **Ajusté 41.0/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse **SURVEILLER** est confirmée sans changement. Le snapshot pré-ouverture du 2026-06-02 reflète la stabilité post-close du 01/06. L'ajustement du volume à 48.80M (1.03× moyenne) renforce légèrement l'interprétation d'une distribution réelle sur le repli de −1.84%. Le RSI stable à 70.58 maintient le surachat modéré. La valorisation reste étirée (P/E 37.0x, cours +4.0% vs consensus) et le timing défavorable persiste. Les scores agents sont inchangés (Global ajusté 41.0/100), bien sous le seuil d'action (50). **Données options corrompues détectées** — la structure réelle reste haussière (réf. 01/06). Pas d'entrée long à $306.31.

---

## Niveaux SL / TP Révisés

| | 2026-06-01 21:00 | 2026-06-02 10:00 | Justification |
|---|------------------|------------------|---------------|
| Entrée suggérée | $306.31 | **$306.31** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $295.89 | **$295.89** | Cours − 2×ATR = $306.31 − $10.42. Inchangé |
| Take-Profit | $321.94 | **$321.94** | Cours + 3×ATR = $306.31 + $15.63. Inchangé |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont inchangés car le cours close est stable ($306.31). Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1. **Le support $305.02** (low du jour ajusté) est la zone immédiate à surveiller : cassure = test du SL $295.89. **La résistance $310.94** (high du jour ajusté) doit être reclaimée pour envisager un retour vers le 52W high $315.00.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE. Le snapshot 10:00 UTC confirme la thèse SURVEILLER (Global ajusté 41.0/100) avec stabilité totale des données techniques post-close. L'ajustement du volume (1.03× moyenne) renforce légèrement la nuance défavorable d'une distribution réelle.**

### Ce qui a changé (snapshot 10:00 UTC) :
1. **Volume ajusté 44.17M → 48.80M** — Passage de 0.93× à **1.03× moyenne 20j**. Ce recalcul post-close confirme une participation légèrement supérieure à la normale sur le repli du 01/06 — nuance technique légèrement moins favorable.
2. **Données options CORROMPUES** — max_pain $200.00 (absurde), P/C null, Call OI null. [ANOMALIE DATA] — ignorer. Référence fiable : structure du 01/06 (max pain $310, P/C 0.42, Call OI 70.6%).
3. **Earnings countdown** : 59 jours → **58 jours** (2026-07-30).

### Ce qui n'a PAS changé :
1. **Cours** — $306.31 inchangé (snapshot pré-ouverture).
2. **RSI 70.58 / ATR $5.21 / MM50 $276.26** — stabilité totale.
3. **Structure options réelle** — dominance call record maintenue (réf. 01/06).
4. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
5. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes).
6. **Multiples élevés** : P/E 37.0x, Forward P/E 31.9x, EV/EBITDA 28.8x.
7. **Timing Défavorable** — maintenu par l'agent recommandation.
8. **Scores agents** — Opportunité 5.1/10, Global ajusté 41.0/100, SURVEILLER.
9. **Aucune news AAPL** détectée (`data/news_2026-06-02.json` vide).
10. **Aucun événement corporate** détecté (`data/events_2026-06-02.json` vide).
11. **Accounting risk non quantifié** — Absence de scan comptable frais.
12. **Validation data** — AAPL OK (`validation_report.txt` 2026-06-02).

### Risques identifiés (inchangés)
1. **Support $305.02** — Low du jour ajusté. Cassure = test de $302 puis SL $295.89. Risque de retour vers MM50 $276.26 si breakdown confirmé sur volume > 50M.
2. **Volume normalisé (1.03×)** — La distribution de −1.84% sur volume légèrement supérieur à la moyenne confirme une pression vendeuse réelle.
3. **FOMO options persistant** — Call OI 70.6% maintenu (réf. 01/06). Tout retournement pourrait déclencher un dégarnissage gamma.
4. **Valorisation étirée** — P/E 37.0x, cours +4.0% vs consensus. Compression multiple possible si guidance décevante le 2026-07-30.
5. **Signal ROTATION_TO_CYCLICAL** — XLK reste top performer mais un pivot macro défensif reste un risque latérent.
6. **Accounting risk non quantifié** — Absence de scan comptable frais.
7. **Données options corrompues** — Nécessite surveillance du pipeline pour correction au prochain snapshot.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $306.31.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (58 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $310.94 (high du jour) sur volume > 47M en clôture :** Reclaim de la zone de rejet — possible relèvement du scoring.
- **Si cours > $315.00 (52W high) sur volume > 50M en clôture :** Break confirmé — réévaluer l'entrée avec SL $295.89.
- **Si cours < $305.02 (low du jour) sur volume > 50M :** Support cassé — risque de test du SL $295.89 puis retour vers MM50 $276.26.
- **Si RSI < 70 avec volume normalisé > 0.8× :** Signal d'apaisement complet du surachat — surveillance renforcée, possible relèvement du scoring vers ATTENDRE.
- **Attention structure options** : dominance call 70.6% maintenue (réf. 01/06). Le gamma risk de l'expiration mensuelle du 01/06 est dissipé mais la conviction call reste élevée pour les échéances suivantes.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.
- Données options du snapshot 2026-06-02 10h UTC corrompues (max pain $200, P/C null, Call OI null) — utilisées comme référence les dernières données fiables du 2026-06-01 13h UTC.

---

## Références
- `data/latest.json` (snapshot 2026-06-02 10:00 UTC) — Cours $306.31, RSI 70.58, ATR $5.21, MM50 $276.26, volume 48.80M, short interest 0.95%, consensus FMP $293.43, options [CORROMPUES : max_pain 200.0, put/call null, call_oi_pct null]
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
