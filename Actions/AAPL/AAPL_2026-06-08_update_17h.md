# AAPL — Mise à Jour Quotidienne (2026-06-08, snapshot 17:00 UTC)

> **Source :** `data/latest.json` (snapshot 2026-06-08 17:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events, recommandation
> **Référence précédente :** Snapshot 13:00 UTC 2026-06-08 ([AAPL_2026-06-08_update.md](AAPL_2026-06-08_update.md))
> **Contexte :** Rebond technique intraday +2.01% sur volume effondré (pas de conviction). RSI remonté vers zone de surachat.

---

## Résumé des Changements depuis le Snapshot 13:00 UTC (2026-06-08)

| Indicateur | Snapshot 13:00 UTC | Snapshot 17:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $307.34 | **$313.505** | 🟢 **+2.01%** |
| RSI 14j | 58.28 | **66.77** | 🟡 **+8.49 pts** — approche surachat |
| ATR 14j | $5.73 | **$5.89** | +$0.16 (+2.8%) |
| MM 50j | $281.09 | **$282.3** | +$1.21 (+0.4%) |
| Volume du jour | 65.25M vs 47.81M avg (1.37×) | **23.49M vs 46.35M avg (0.51×)** | 🔴 **Effondré — pas de conviction** |
| Short Interest | 0.95% | **0.95%** | Inchangé |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | Inchangé |
| Max Pain (JSON) | $330.00 | **$330.00** | Inchangé |
| Put/Call Ratio | 0.42 | **0.42** | Inchangé |
| Call OI % | 70.6% | **70.6%** | Inchangé |
| **Score Opportunité agent** | 5.6/10 | **5.4/10** | 🟡 **−0.2 pt** (rebond sans volume) |
| **Score Global ajusté** | 61.0/100 | **54.0/100** | 🟡 **−7.0 pts** |
| **Recommandation agent** | ACHETER (Sizing Réduit) | **ATTENDRE** | 🔴 **Downgrade** |
| **Timing agent** | Favorable | **Neutre** | 🟡 Dégradé |

**Verdict :** Le snapshot 17h enregistre un **rebond technique +2.01%** ($307.34 → $313.505) sur un **volume effondré à 0.51×** moyenne 20j. Ce pattern est caractéristique d'un rebond sans conviction institutionnelle — le manque de participation au volume invalide la force du mouvement. Le RSI remonte de 8.49 pts vers la zone de surachat (66.77), réduisant la marge de sécurité technique. L'upside implicite vs consensus FMP ($293.43) se dégrade à **−6.4%** (vs −4.7% à $307.34). Les scores agents sont révisés à la baisse : Score Opportunité **5.4/10**, Score Global ajusté **54.0/100**, recommandation **ATTENDRE** (downgrade depuis ACHETER Sizing Réduit). La structure options reste inchangée et haussière (max pain $330.00, P/C 0.42, Call OI 70.6%), mais le spot s'est rapproché du max pain (+5.3% vs +7.4% à 13h), augmentant le risque de pinning gamma à l'expiration du jour. **Timing passe de Favorable à Neutre.**

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $313.505 | Rebond +2.01% — consolidation sous 52W high $316.94 (−1.08%) |
| RSI 14j | 66.77 | 🟡 Zone haussière — approche surachat >70 (sortie de la zone neutre favorable) |
| ATR 14j | $5.89 | Volatilité légèrement en hausse |
| MM 50j | $282.3 | 🟢 Cours +11.1% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 46.35M | 🔴 0.51× moyenne — épuisement vendeur / absence acheteur institutionnel |
| 52W Range | $195.07–$316.94 | Cours à −1.08% du 52W high |
| Support clé | $301.73 | Cours − 2×ATR = $313.505 − $11.78 |
| Support secondaire | $282.3 | MM50 — cassure = retour vers $275 |
| Résistance | $316.94 | 52W high — break nécessite volume > 50M en clôture |
| Résistance mécaniste | $330.00 | Max pain options — call wall à +5.3% du spot |
| Résistance technique | $331.18 | Cours + 3×ATR = objectif TP agent |
| Short Interest | 0.95% | 🟢 Faible — pas de setup short squeeze |

**Options — Inchangées (Snapshot 17h)**

| Métrique | Valeur brute 17h | Valeur opérationnelle (03/06) | Interprétation |
|----------|------------------|-------------------------------|----------------|
| Max Pain | $330.00 | $310.00 | 🟢 Spot s'est rapproché : +5.3% (vs +7.4% à 13h) |
| Put/Call Ratio | 0.42 | 0.62 | 🟢 Domination call renforcée |
| Call OI % | 70.6% | 61.9% | 🟢 Appétit call élevé |
| Expiration | 2026-06-08 | 2026-06-08 | ⚠️ Échéance aujourd'hui — gamma risk actif |

**Interprétation technique :**
- **RSI 66.77** : remontée de 8.49 pts en quelques heures, sortie de la zone neutre favorable (50–60) vers la zone haussière (60–70). Franchissement de 70 = signal de surachat à surveiller. La remontée rapide sur volume faible est un signal de faiblesse structurelle, pas de force.
- **Volume 23.49M (0.51×)** : effondrement vs 65.25M (1.37×) du snapshot 13h. Ce volume collapse sur une hausse de +2% est un pattern de **rebond sans conviction** — probablement du short-covering ou du flux algorithmique, pas de l'accumulation institutionnelle. 🟡 Négatif pour la durabilité du mouvement.
- **Max pain $330.00** : le spot ($313.505) est désormais à +$16.495 du max pain, soit +5.3% (vs +7.4% à 13h). Le rapprochement du spot vers le max pain augmente la probabilité de pinning gamma vers $330.00 à l'expiration, mais la distance reste significative sans catalyseur.
- **MM50 $282.3** : support dynamique intact, écart +11.1%.
- **52W high $316.94** : le cours est à seulement −1.08% du sommet. Un break sur volume faible serait suspect ; une confirmation nécessiterait >50M en clôture.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $293.43** (58 analystes, 2 mises à jour le mois dernier)
- **Upside implicite : −6.4%** vs cours $313.505 (dégradé de −4.7% à $307.34)
- **Couverture :** 58 analystes — coverage institutionnel massif

### Ratios FMP — Inchangés (FY2025)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.60T | $3.82T | 🟡 Écart +20% entre sources |
| P/E (LTM) | 37.9x | 34.1x | 🔴 Élevé |
| Forward P/E | 32.6x | — | 🔴 Élevé |
| EV/Revenue | 10.0x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 28.3x | 27.0x | 🔴 Élevé |
| P/B | 43.2x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples élevés mais qualité institutionnelle intacte (Filtre Qualité 6/6 ✅ Quality Compounder, confirmé par `data/quality_report_latest.json` status OK). Le Score Valorisation est révisé à la baisse à **4.5/10** (vs 5.0/10) car le rebond de +2% étire encore la valorisation sans nouveau fondamental.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 58 analystes FMP, PT $293.43. Consensus stable.
- **Aucun upgrade/downgrade** détecté dans le snapshot.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — Inchangées mais contexte modifié
- **Max Pain $330.00** : spot à +5.3% (vs +7.4% à 13h). Le rapprochement mécaniste augmente le gamma risk vers le haut.
- **Put/Call 0.42** : structure haussière renforcée.
- **Call OI 70.6%** : record récent. Risque de dégarnissage gamma si le cours stagne sous $315.
- **Échéance :** **2026-06-08 (aujourd'hui)** — gamma risk actif, pinning vers $330 possible si le spot approche $315–$320 en fin de séance.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.086 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | XLK top sector rotation (momentum 10.0/10, RS20 +5.44%) |

### Sector Rotation
- **Technology (XLK)** : return 20d +6.25%, RS20 vs SPY +5.44%. **Top1** du ranking avec momentum score 10.0/10. Pas de crossover détecté.
- **Signal système :** NEUTRAL (régime UNKNOWN).

### Géopolitique
- **Score Politique :** Non spécifique à AAPL. `geo_risk_latest.json` daté 2026-05-17, aucun flag AAPL.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `data/accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0, n=0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | Snapshot 13h /10 | Snapshot 17h /10 | Δ | Justification |
|-----|------------------|------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucun catalyseur nouveau. Earnings 2026-07-30 dans 52 jours. |
| Valorisation | 5.0 | **4.5** | −0.5 | Cours +2% = upside vs consensus dégradé à −6.4%. Multiples encore plus étirés. |
| Momentum | 7.0 | **6.5** | −0.5 | Rebond +2% mais volume effondré 0.51× = pas de conviction. RSI 66.77 approche surachat. |
| **Score Opportunité** | **5.6** | **5.4** | **−0.2** | Pondération régime default 35/40/25 |

**Score Global Composite agent :** 54.0/100
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Neutre** (rebond sans volume, RSI remonté)
- **Recommandation agent : ATTENDRE** (downgrade depuis ACHETER Sizing Réduit)

**Verdict institutionnel Argus-IA :** Le rebond technique de +2.01% sur volume effondré (0.51×) est un mouvement de **faible qualité**. Il traduit probablement du short-covering ou de la microstructure de marché (pinning gamma vers $330) plutôt que de l'accumulation institutionnelle. Le RSI 66.77 sort de la zone neutre favorable et approche le surachat, réduisant le timing d'entrée. L'upside vs consensus ($293.43) est désormais négatif (−6.4%), rendant le rapport risque/rendement défavorable. Le ratio R/R calculé à 1.5:1 reste inférieur au seuil institutionnel de 2:1. La recommandation est **downgradée de ACHETER (Sizing Réduit) à ATTENDRE**. Le call wall $330.00 reste une résistance mécaniste crédible à surveiller en fin de séance d'expiration.

---

## Niveaux SL / TP Révisés

| | Snapshot 13:00 | Snapshot 17:00 | Justification |
|---|----------------|----------------|---------------|
| Entrée suggérée | $307.34 | **$313.505** | Close actuel — rebondé |
| Stop-Loss | $295.88 | **$301.73** | Cours − 2×ATR = $313.505 − $11.78. Révisé à la hausse |
| Take-Profit | $324.53 | **$331.18** | Cours + 3×ATR = $313.505 + $17.67. Révisé à la hausse |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Le ratio R/R reste à 1.5:1, inférieur au seuil de 2:1. Le SL $301.73 est juste sous le seuil psychologique $300. La résistance $316.94 (52W high) doit être breakée sur volume > 50M en clôture pour confirmer une continuation. Le max pain $330.00 est la résistance mécaniste clé post-expiration. **Post-expiration (demain) :** surveiller si le call wall $330.00 reste un niveau de liquidité pertinent pour les options du cycle suivant, et si le volume se normalise (> 0.8×) pour valider la qualité du rebond.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : MODIFIÉE — Downgrade de ACHETER (Sizing Réduit) à ATTENDRE.**

La thèse est modifiée car le rebond technique de +2.01% se produit sur un volume effondré (0.51×), indiquant une absence de conviction institutionnelle. Le RSI remonté à 66.77 réduit la marge de sécurité technique. L'upside vs consensus est désormais négatif (−6.4%).

### Ce qui a changé (évolutions significatives) :
1. **Cours +2.01%** ($307.34 → $313.505) — rebond technique. 🟡
2. **RSI +8.49 pts** (58.28 → 66.77) — approche surachat, timing moins favorable. 🟡
3. **Volume effondré** (1.37× → 0.51×) — pas de conviction derrière le rebond. 🔴
4. **Spot vs Max Pain** : écart réduit à +5.3% (vs +7.4%), pinning gamma plus probable. 🟡
5. **Recommandation downgradée** : ACHETER (Sizing Réduit) → **ATTENDRE**. 🔴
6. **Score Global ajusté** : 61.0/100 → **54.0/100**. 🟡
7. **Score Valorisation** : 5.0/10 → **4.5/10**. 🟡
8. **Score Momentum** : 7.0/10 → **6.5/10**. 🟡
9. **Timing** : Favorable → **Neutre**. 🟡

### Ce qui n'a PAS changé (stabilité) :
1. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes).
2. **Fondamentaux FMP FY2025** — inchangés.
3. **Short Interest 0.95%** — inchangé.
4. **Filtre Qualité 6/6** ✅ Quality Compounder.
5. **Structure options** : max pain $330.00, P/C 0.42, Call OI 70.6% — inchangée.
6. **XLK top sector** — momentum 10.0/10, signal NEUTRAL.
7. **FX Exposure Score 0.0** — neutral.
8. **Validation data** — AAPL OK (`validation_report.txt` 2026-06-08).
9. **Qualité report** — status OK (`quality_report_latest.json`).

### Risques identifiés (révisés)
1. **Volume effondré 0.51×** — absence de conviction sur le rebond. Si le volume ne se normalise pas demain, le rebond risque d'être éphémère. 🔴
2. **RSI 66.77** — approche surachat >70. Un RSI >70 sur volume faible = signal de distribution déguisée. 🟡
3. **Call wall $330.00** — résistance mécaniste à +5.3%. Pinning gamma possible à l'expiration. 🟡
4. **Valorisation étirée** — P/E 37.9x, Forward P/E 32.6x. Compression multiple possible si guidance décevante le 2026-07-30. 🔴
5. **Cours +4.7% vs consensus** (à 13h) → **+6.8% vs consensus** (à 17h) : décote toujours négative. 🔴
6. **Absence de catalyseur immédiat** — prochain earnings dans 52 jours. Zone sans catalyseur = risque de dérive latérale. 🟡

### Positionnement Argus-IA
- **Action : ATTENDRE** — Pas d'entrée à $313.505
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (52 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Gamma watch (2026-06-08) :** Surveiller l'interaction avec $330.00 (max pain) et $316.94 (52W high) en fin de séance d'expiration. Le rapprochement du spot vers $330 augmente le risque de pinning gamma haussier, mais la distance ($16.50) rend un pinning complet peu probable sans catalyseur.
- **Si cours > $316.94 (52W high) sur volume > 50M en clôture :** Break confirmé — réévaluer vers ACHETER avec SL $301.73.
- **Si cours < $301.73 (SL) sur volume > 50M :** Support cassé — sortie long, risque de test MM50 $282.3.
- **Si volume demain reste < 0.6× avec cours stagnant :** Le rebond est invalidé — rester à l'écart.
- **Si RSI redescend < 60 avec volume normalisé > 0.8× :** Retour en zone neutre favorable — réévaluer l'entrée.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan Ratio) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 2026-06-08 17:00 UTC) — Cours $313.505, RSI 66.77, ATR $5.89, MM50 $282.3, volume 23.49M (0.51×), short interest 0.95%, consensus FMP $293.43, options max_pain $330.00, P/C 0.42, Call OI 70.6%
- `data/quality_report_latest.json` (2026-05-17) — AAPL status OK
- `data/validation_report.txt` (2026-06-08) — AAPL OK
- `data/sector_rotation_2026-06-08.json` — XLK top sector (momentum 10.0/10, NEUTRAL)
- `data/fx_exposure_2026-06-08.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-08.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-06-08.json` — Earnings 2026-07-30, 52 jours
- `data/events_2026-06-08.json` — Aucun événement corporate détecté
- `data/news_2026-06-08.json` — Aucune news AAPL détectée
- `data/geo_risk_2026-05-17.json` — Aucun flag spécifique AAPL
- `data/quant_2026-05-17.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
