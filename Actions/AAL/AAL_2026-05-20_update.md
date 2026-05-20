# AAL — Mise à Jour Snapshot Matinal

**Date :** 2026-05-20 (snapshot 10:00 UTC)
**Ticker :** AAL (NASDAQ)
**Type :** Update matinal — Données quasi inchangées vs clôture 2026-05-19
**Cours (close) :** $12.06
**Previous close :** $12.36
**Change vs previous close :** −2.43%
**Volume :** 67.1M (vs moy. 20j 51.9M, +29.4%)

---

## Résumé des Changements depuis l'Update (2026-05-19 21:00 UTC)

| Indicateur | 2026-05-19 21:00 UTC | 2026-05-20 10:00 UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours close | $12.06 | **$12.06** | **0.00 (0.00%)** |
| RSI 14j | 60.62 | **60.62** | **0.00** |
| ATR 14j | $0.47 | **$0.47** | **$0.00** |
| MM 50j | $11.56 | **$11.56** | **0.00** |
| Forward P/E | 5.50 | **5.45** | **−$0.05** |
| Volume 20j | 67.1M vs 51.9M avg (+29.4%) | 67.4M vs 51.9M avg (+29.8%) | **+0.4 pts** |
| Short Interest | 12.21% | **12.21%** | **0.00** |
| Consensus FMP PT | $16.02 (15 analystes) | **$16.02** (15 analystes) | **Inchangé** |
| Put/Call Ratio | 2.67 | **null** | **[DONNÉES MANQUANTES]** |
| Max Pain | $9.50 | **$5.00** | **⚠️ Aberration data quality** |
| Call OI % | 27.2% | **null** | **[DONNÉES MANQUANTES]** |
| Score Opportunité | 6.6/10 | **6.6/10** | **0.0** |
| Recommandation | ACHETER (Sizing Réduit) | **ACHETER (Sizing Réduit)** | **Inchangée** |

**Pas de nouvelle session de marché.** Le snapshot 10:00 UTC du 2026-05-20 reflète la clôture de la veille ($12.06). Les données techniques, fondamentales et de consensus sont strictement identiques. Seule anomalie : les données options (`put_call_ratio`, `call_oi_pct`) sont retournées `null` dans `latest.json`, et le `max_pain` affiche $5.00 (valeur aberrante — options OTM deep). Ces anomalies data quality sont probablement liées à un artefact de fetch matinal (market closed / données pré-market incomplètes). Les niveaux options valides restent ceux du snapshot 2026-05-19 21:00 UTC (put/call 2.67, max pain $9.50, call OI 27.2%).

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $12.06 | −2.43% vs previous close $12.36 (clôture veille) |
| RSI 14j | 60.62 | 🟡 Neutre — inchangé, pas de dérive |
| ATR 14j | $0.47 | Volatilité inchangée, faible |
| MM 50j | $11.56 | 🟢 Cours +4.3% au-dessus (trend haussier court terme intact) |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 67.4M | 🟡 +29.8% vs moyenne — volume élevé sur session baissière = avertissement maintenu |
| 52W Range | $10.09–$16.50 | Cours à 27% du 52W high, 19.5% au-dessus du 52W low |
| Support clé | $11.50–$11.60 | Zone MM50 + consolidation avril 2026 |
| Résistance | $12.36–$12.50 | Close précédent + support devenu résistance |
| Résistance majeure | $13.50–$14.00 | Gap janvier 2026 + ancienne MM200 |
| Short Interest | 12.21% | 🟡 Élevé — fuel pour squeeze si catalyseur positif |

**Options — [DONNÉES PARTIELLES] :**

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| Put/Call Ratio | **null** | [DONNÉES MANQUANTES] — dernière valeur valide : 2.67 (2026-05-19 21:00 UTC) |
| Max Pain | **$5.00** | ⚠️ Aberration data quality (valeur .00) — dernière valeur valide : $9.50 |
| Call OI % | **null** | [DONNÉES MANQUANTES] — dernière valeur valide : 27.2% |
| Expiration proche | 2026-05-22 | Dans 2 jours — concentration du gamma autour de $9.50–$12.50 |

**Interprétation technique :**
- Aucun changement technique depuis le snapshot 21:00 UTC du 19/05. Le cours $12.06, le RSI 60.62, l'ATR $0.47 et la MM50 $11.56 sont inchangés.
- **Alerte data quality options** : le snapshot matinal ne fournit pas les données options complètes. Le Max Pain à $5.00 est une valeur aberrante (options deep OTM) qui ne reflète pas la réalité du marché. Il est recommandé de réutiliser les données du snapshot 2026-05-19 21:00 UTC pour les décisions impliquant le gamma / le max pain.
- **Gamma risk 22/05** : dans 2 jours. Avec un Max Pain valide à $9.50 vs cours $12.06, le risque de pinning mécanique persiste. Le repli de −2.43% rapproche le cours de la zone Max Pain ($9.50–$12.00). Un passage sous $11.80 déclencherait une décharge gamma baissière accélérée.

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $16.02** (15 analystes, 2 mises à jour le mois dernier)
- **Upside implicite : +32.8%** vs cours $12.06
- **Couverture :** 15 analystes — coverage significatif

### Ratios FMP — Bilan Stressé (inchangé)
| Ratio | Valeur | Seuil | Signal |
|-------|--------|-------|--------|
| P/E (LTM, FMP) | 91.22 | — | 🔴 Élevé (charges récentes) |
| P/E (LTM, Yahoo) | **38.90** | — | 🔴 Élevé |
| P/B | -2.72 | — | 🔴 Equity négatif |
| P/S | 0.185 | — | 🟢 Très faible |
| EV/EBITDA (Yahoo) | 8.54 | — | 🟡 Élevé vs FMP 11.44 |
| EV/Revenue | 0.81 | — | 🟢 Faible |
| Gross Margin | 19.2% | — | 🟡 Sector norm |
| Operating Margin | 2.7% | — | 🔴 Faible |
| Net Margin | 0.2% | — | 🔴 Quasi nul |
| Current Ratio | 0.50 | >1.0 | 🔴 Trésorerie insuffisante |
| Quick Ratio | 0.38 | >0.8 | 🔴 Liquidity stress |
| Net Debt / EBITDA | 8.83x | <3.0 | 🔴🔴 Extrême |
| Interest Coverage | 0.85x | >2.0 | 🔴 Service dette > EBIT |
| Tangible Asset Value | -$9.88B | >0 | 🔴 Patrimoine négatif |
| Working Capital | -$12.3B | >0 | 🔴 Capacité opérationnelle négative |
| ROE | -3.0% | >10% | 🔴 Destruction de valeur |
| ROIC | 2.0% | >8% | 🔴 Très faible |
| FCF Yield | -6.7% | >0 | 🔴 FCF négatif |

**Forward P/E 5.45** (vs 5.50 2026-05-19) — réduction mécanique liée à un léger ajustement de calcul, pas à un changement fondamental.

### Événement Clé — Earnings Q2 FY2026
- **Date :** 2026-07-23 (64 jours)
- **Estimates EPS :** -$0.34 à $0.17
- **Estimates Revenue :** $16.6B
- **Implication :** La fourchette EPS large reflète l'incertitude. Un beat au-dessus de $0.17 serait un catalyseur majeur compte tenu du short interest 12.2% et du put/call 2.67.

---

## Mise à Jour Sentiment / Flux / Macro

### Sentiment Analystes
- **Inchangé :** 15 analystes FMP, PT $16.02. Le consensus institutionnel reste structuré.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz = indifférence retail.

### Options
- **[DONNÉES PARTIELLES]** — `put_call_ratio` et `call_oi_pct` sont `null` dans le snapshot matinal. Dernières valeurs valides (2026-05-19 21:00 UTC) :
  - Put/Call : 2.67
  - Max Pain : $9.50
  - Call OI : 27.2%
- **Implication :** Le setup contrarian reste valide sur la base des dernières données complètes. Le repositionnement vers les calls n'a pas été réversé (dernier snapshot valide). Si le cours rebondit au-dessus de $12.50, le squeeze mécanique reste activable.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🔴 Élevée | Inchangée — dette variable, +1% = +$400M/an |
| Pétrole (WTI) | 🔴🔴 Critique | Inchangée — jet fuel 25-30% coûts |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (pas de headwind/tailwind actif) |
| Industriels (XLI) | 🟡 Modérée | Pas de rotation favorable détectée dans le snapshot sectoriel |

### Sector Rotation
- **Industrials (XLI)** : données sectorielles inchangées vs snapshot précédent. Pas de crossover détecté.
- **Impact :** Pas de vent de secteur favorable. Le momentum d'AAL reste idiosyncratique.

### Géopolitique
- **Score Politique :** 2/10 — AAL non exposé aux événements géopolitiques actuels.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**. Le Filtre Qualité (0-1/6) et les ratios FMP (interest coverage <1x, tangible asset value négative) suggèrent une santé financière très faible.
- **Quant report :** Données insuffisantes — 0 signaux historiques, calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-05-19 21:00 UTC /10 | 2026-05-20 10:00 UTC /10 | Δ | Source |
|-----|--------------------------|--------------------------|---|--------|
| Catalyseur | 6.8 | **6.8** | 0.0 | Consensus PT $16.02 (+33%), earnings 23/07, short interest 12.2%, put/call 2.67 (dernier valide) |
| Valorisation | 6.5 | **6.5** | 0.0 | Forward P/E 5.45 + PT $16.02 = asymétrie favorable |
| Momentum | 6.5 | **6.5** | 0.0 | RSI 60.62, au-dessus MM50, données techniques inchangées |
| **Score Opportunité** | **6.6** | **6.6** | **0.0** | Pondération 35/40/25 |

**Score Global Composite :** 66.1/100 → **Ajusté 71.1/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Bonus : aucun
- **Pas de malus accounting** (données indisponibles, mais Filtre Qualité 0-1/6 = risque structurel élevé)

**Recommandation Agent :** ACHETER — Sizing Réduit — Horizon 1-3 mois.

---

## Niveaux SL / TP Révisés

| | 2026-05-19 21:00 UTC | 2026-05-20 10:00 UTC | Justification |
|---|----------------------|----------------------|---------------|
| Entrée suggérée | $12.06 | **$12.06** | Close actuel — inchangé |
| Stop-Loss | $11.12 | **$11.12** | Cours − 2×ATR = $12.06 − $0.94. Aligné sur MM50 ($11.56) − 0.94×ATR |
| Take-Profit | $13.47 | **$13.47** | Cours + 3×ATR = $12.06 + $1.41. Conservateur |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Aucun changement de niveau — les données techniques sont inchangées. Le SL à $11.12 correspond à la MM50 ($11.56) − 0.94×ATR. Une cassure sous $11.12 = signal de sortie technique (trend haussier court terme invalidé). Le TP $13.47 est conservateur ; réviser à $14.00 (gap janvier) si momentum confirmé sur volume > 50M. L'expiration options du 22/05 est dans 2 jours — le Max Pain validé à $9.50 vs cours $12.06 indique un risque de pinning baissier atténué par la distance. Cependant, un passage sous $11.80 déclencherait une décharge gamma baissière. Le volume élevé sur baisse du 19/05 reste un avertissement : si la session du 20/05 confirme un volume >60M avec une poursuite de la baisse sous $11.80, EXIT anticipé recommandé.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — ACHETER (Sizing Réduit) — PAS DE NOUVELLE INFORMATION**

### Ce qui a changé (snapshot 2026-05-20 10:00 UTC) :
1. **Aucun changement de cours** — Le snapshot matinal reflète la même clôture ($12.06) que le snapshot 21:00 UTC du 19/05.
2. **Alerte data quality options** — `put_call_ratio` et `call_oi_pct` sont `null` dans `latest.json`. Le `max_pain` affiche $5.00 (aberrant .00). Ces anomalies sont probablement liées au fetch matinal (market closed / pré-market incomplet). Les dernières données valides (2026-05-19 21:00 UTC) doivent être utilisées : put/call 2.67, max pain $9.50, call OI 27.2%.
3. **Forward P/E 5.45** (vs 5.50) — ajustement mécanique de calcul, pas de changement fondamental.
4. **Jours jusqu'aux earnings : 64** (vs 65 hier).

### Ce qui n'a PAS changé :
1. **Cours $12.06, RSI 60.62, ATR $0.47, MM50 $11.56** — strictement inchangés.
2. **Volume 67.4M (+29.8%)** — même session de référence.
3. **Filtre Qualité : 0-1/6** — Hors périmètre compounding. AAL reste une commodité sans moat, bilan stressé.
4. **Bilan extrêmement fragile** — Current ratio 0.50, interest coverage 0.85x, tangible asset value -$9.88B, working capital -$12.3B.
5. **Consensus analyste FMP** : PT $16.02 inchangé. Upside +32.8%.
6. **Short Interest 12.2%** — setup squeeze intact.
7. **Régime macro défavorable** — Stagflation (fuel, taux élevés, salaires) = pire environnement pour les airlines.
8. **Score Opportunité 6.6/10** — stable.

### Risques identifiés (maintenus)
1. **Data quality options** — Les données options du snapshot matinal sont incomplètes. Ne pas prendre de décision basée sur le Max Pain $5.00 affiché.
2. **Volume élevé sur baisse = avertissement** — Si la session du 20/05 confirme un volume >60M avec cours sous $11.80, EXIT anticipé.
3. **Value trap confirmé possible** — Forward EPS ~$2.19/an peut ne pas se matérialiser si fuel/grèves/récession.
4. **Recapitalisation / dilution** — Si interest coverage reste <1.0x, restructuration de dette ou émission d'actions possible.
5. **Earnings Q2 = binary event** — Estimates large = forte volatilité post-announcement. SL doit être respecté si guidance cut.
6. **Gamma risk à expiration 22/05** — Dans 2 jours. Max Pain validé $9.50 vs cours $12.06 = risque de pinning baissier atténué par la distance.
7. **Accounting risk non quantifié** — Absence de scan comptable (M-Score, Z-Score, F-Score, Sloan).
8. **Divergence P/E Yahoo/FMP** — P/E 38.90 vs 91.22. Vérifier la cohérence des earnings LTM dans le prochain 10-Q.

### Positionnement Argus-IA
- **Action : ACHETER** avec sizing réduit (max 3-5% du portefeuille, risk 0.5% capital)
- **Horizon :** 1-3 mois (jusqu'à earnings Q2 + réaction post-announcement)
- **Catalyseur clé :** Earnings 2026-07-23. Préparer exit anticipé si guidance cut >5%.
- **Si cours < $11.12 (SL) :** EXIT immédiat — trend haussier invalidé.
- **Si cours > $13.47 (TP) :** Réviser TP vers $14.00 (gap janvier) si momentum confirmé sur volume > 50M.
- **Si cours < $11.80 avant expiration 22/05 :** EXIT anticipé — risque de décharge gamma baissière + cassure du support intermédiaire.
- **Si volume > 50M avec reprise > $12.30 :** Confirmation shakeout — maintenir la position, SL inchangé à $11.12.
- **Si volume > 60M avec baisse sous $11.80 :** Signal de distribution — EXIT anticipé recommandé avant SL.
- **Si put/call repasse sous 2.00 avec volume calls > 30% OI :** Le setup contrarian s'efface — réévaluer la thèse avant earnings.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan).
- Données options complètes dans le snapshot matinal (put/call ratio, call OI %).

---

## Références
- `data/2026-05-20.json` (snapshot 10:00 UTC) — Cours $12.06, RSI 60.62, ATR $0.47, MM50 $11.56, volume 67.4M, short interest 12.21%, consensus FMP $16.02, options (max_pain $5.00 aberrant, put/call null, call_oi null), P/E Yahoo 38.90, Forward P/E 5.45
- `data/recommandations_2026-05-20.json` — Scores agents inchangés (Score Global 66.1, Ajusté 71.1, SL $11.12, TP $13.47)
- `data/fx_exposure_2026-05-20.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-05-20.json` — Sentiment retail (EXTREME_BEARISH, 0 mentions)
- `data/upcoming_events_2026-05-20.json` — Earnings 2026-07-23, 64 jours
- `data/events_2026-05-20.json` — Événements corporates (aucun détecté)
- `data/validation_report.txt` — 22/25 OK, AAL pas dans les erreurs/warnings
- `data/quant_report_latest.json` — Données quantitatives (insuffisantes)
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
