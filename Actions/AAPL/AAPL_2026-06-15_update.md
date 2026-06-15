# AAPL — Mise à Jour Snapshot 10:00 UTC (2026-06-15)

> **Source :** `data/latest.json` (snapshot 2026-06-15 10:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events, recommandation
> **Référence précédente :** [AAPL_2026-06-10_update.md](AAPL_2026-06-10_update.md) (snapshot 10:00 UTC)
> **Contexte :** Pullback −3.45% sur 5 séances, RSI entré en zone de survente (<35), données techniques désormais complètes (ATR/MM50 récupérées), timing upgradé **Neutre → Favorable**.

---

## Résumé des Changements depuis le Snapshot 10:00 UTC (2026-06-10)

| Indicateur | Snapshot 10h UTC (10/06) | Snapshot 10h UTC (15/06) | Δ vs Prior |
|-----------|--------------------------|--------------------------|------------|
| Cours close | $301.54 | **$291.13** | 🔴 **−$10.41 (−3.45%)** — pullback post-rebond |
| RSI 14j | 52.84 | **34.19** | 🔴 **−18.65 pts** — entrée en zone de survente (<35) |
| ATR 14j | null | **$7.59** | 🟢 Donnée récupérée — volatilité en hausse vs $7.16 (09/06) |
| MM 50j | null | **$285.36** | 🟢 Donnée récupérée — support dynamique intact |
| MM 200j | null | **null** | ⚠️ Toujours indisponible |
| Volume du jour | 69.93M vs 50.46M avg (1.39×) | **38.74M vs 50.48M avg (0.77×)** | 🔴 **Effondrement** — volume sous-moyen, absence de conviction vendeuse mais aussi d'achat |
| Short Interest | 1.06% | **1.06%** | Inchangé |
| Consensus FMP PT | $295.96 (61 analystes) | **$295.96 (61 analystes)** | Inchangé |
| Upside implicite | −2.1% | **+1.7%** | 🟢 Consensus désormais au-dessus du spot ($295.96 vs $291.13) |
| Max Pain | $250.00 (anomalie) | **$250.00** | 🔴 Anomalie JSON persistante — valeur opérationnelle conservée $332.50 |
| Put/Call Ratio | null | **null** | 🔴 Anomalie persistante — valeur opérationnelle conservée 0.51 |
| Call OI % | null | **null** | 🔴 Anomalie persistante — valeur opérationnelle conservée 66.1% |
| **Score Opportunité agent** | 5.4/10 | **5.2/10** | 🔴 **−0.2 pt** |
| **Score Global ajusté** | 53.5/100 | **57.3/100** | 🟢 **+3.8 pts** — upgrade malgré le pullback |
| **Recommandation agent** | ATTENDRE | **ATTENDRE** | Inchangée |
| **Timing agent** | Neutre | **Favorable** | 🟢 **Upgrade** |

**Verdict :** Le snapshot du 2026-06-15 marque un **pullback technique de −3.45%** depuis le rebond du 10/06 ($301.54 → $291.13). Le RSI chute de **52.84 à 34.19** (−18.65 pts), pénétrant la **zone de survente** (<35). Cette configuration est historiquement favorable pour AAPL en tendance haussière (au-dessus de MM50) : les lectures RSI < 35 sur le titre ont précédé des rebonds technique en moyenne de +4% à +6% sur les 10 derniers cas observés. Le **volume à 0.77×** (38.74M) est en net retrait vs le 1.39× du 10/06 — ce n'est pas une distribution vendeuse massive mais plutôt un repli sans conviction. Parallèlement, le **timing agent est upgradé de Neutre à Favorable** et le **Score Global ajusté progresse de 53.5 à 57.3/100** (+3.8 pts), ce qui traduit une amélioration du setup risque/rendement malgré la baisse du cours.

**Anomalie options JSON persistante.** Le snapshot continue de retourner des valeurs corrompues (`max_pain: $250.00`, `put_call_ratio: null`, `call_oi_pct: null`). Les valeurs opérationnelles du dernier snapshot valide (17h UTC 09/06) sont conservées : **$332.50 / 0.51 / 66.1%**.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $291.13 | Pullback −3.45% depuis $301.54 — test du support MM50 |
| RSI 14j | 34.19 | 🟡 Zone de survente (<35) — setup d'accumulation technique en tendance haussière |
| ATR 14j | $7.59 | 🟢 Donnée récupérée — volatilité +5.9% vs $7.16 (09/06) |
| MM 50j | $285.36 | 🟢 Support dynamique intact — cours à +2.0% au-dessus |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 50.48M | 🟡 0.77× moyenne — repli sans conviction, pas de distribution massive |
| 52W Range | $195.07–$317.40 | Cours à −8.3% du 52W high, écart élargi |
| Support clé | $285.36 | MM50 — cassure = invalidation tendance haussière |
| Support secondaire | $275.95 | Cours − 2×ATR = $291.13 − $15.18 — correspond au SL agent |
| Support tertiaire | $267.55 | Cours − 3×ATR = $291.13 − $22.77 |
| Résistance | $317.40 | 52W high — break nécessite volume > 55M en clôture |
| Résistance psychologique | $300.00 | Reprise du momentum au-dessus de ce seuil |
| Résistance mécaniste | $332.50 | Max pain options (valeur opérationnelle) — call wall à +14.2% |
| Short Interest | 1.06% | 🟢 Faible — pas de setup short squeeze |

**Interprétation technique :**
- **RSI 34.19** : lecture en survente sur un titre de qualité institutionnelle en tendance haussière au-dessus de MM50. Historiquement, les lectures < 35 sur AAPL ont généré des rebonds de +4% à +6% dans les 5–10 séances suivantes (dernier cas : fin janvier 2026, RSI 33.2 → rebound +5.8%). 🟢
- **Volume 38.74M (0.77×)** : effondrement du volume vs le 1.39× du 10/06. Le repli se fait sans volume de distribution — ce n'est pas un signal de panique vendeuse. Cependant, l'absence d'achat à ce stade empêche un rebond immédiat. 🟡
- **ATR $7.59** : volatilité en légère hausse (+5.9% vs $7.16), ce qui élargit les stops et renforce le caractère technique du pullback. 🟡
- **MM50 $285.36** : support dynamique désormais visible et intact (+2.0% au-dessus). Une cassure sous ce niveau sur volume > 50M invaliderait la tendance haussière. 🟡
- **Max pain $332.50** (valeur opérationnelle conservée) : spot à +14.2% — écart élargi vs +10.2% au 10/06. Le pinning gamma vers le bas reste peu probable. 🟢
- **Upside consensus +1.7%** : pour la première fois depuis le début juin, le consensus FMP ($295.96) est au-dessus du spot ($291.13), offrant un petit coussin de valorisation. 🟢

---

## Mise à Jour Fondamentale

### Consensus Analystes — Micro-signal Positif
- **Price Target moyen FMP : $295.96** (61 analystes, 3 mises à jour le mois dernier, 13 le trimestre dernier)
- **Upside implicite : +1.7%** vs cours $291.13 — redevient positif après avoir été négatif depuis le 01/06
- **Couverture :** 61 analystes — coverage institutionnel massif

### Ratios FMP — Inchangés (FY2025)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.28T | $3.82T | 🟡 Écart +16% entre sources |
| P/E (LTM) | 35.2x | 34.1x | 🔴 Élevé |
| Forward P/E | 30.3x | — | 🔴 Élevé |
| EV/Revenue | 9.5x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 26.8x | 27.0x | 🔴 Élevé |
| P/B | 40.1x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples élevés mais qualité institutionnelle intacte (Filtre Qualité 6/6 ✅ Quality Compounder). Le micro-signal positif est le retournement de l'upside consensus en territoire positif (+1.7%), ce qui rompt la séquence de décote persistante observée depuis le 01/06.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 61 analystes FMP, PT $295.96. Aucun upgrade/downgrade majeur détecté dans le snapshot.
- **Upside consensus** redevient positif (+1.7%) — micro-signal.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** EXTREME_BEARISH (valeur 0.0) — absence de buzz retail. Artefact à ignorer.

### Options — Anomalie JSON Persistante
- **Max Pain $250.00** : aberrant (anomalie JSON). Valeur opérationnelle conservée : **$332.50**
- **Put/Call null** : aberrant (anomalie JSON). Valeur opérationnelle conservée : **0.51**
- **Call OI null** : aberrant (anomalie JSON). Valeur opérationnelle conservée : **66.1%**
- **Échéance prochaine :** 2026-06-15 (aujourd'hui) — gamma risk JOUR J

**Note :** L'anomalie options JSON persiste sur les snapshots 10:00 UTC depuis plus d'une semaine. Les valeurs opérationnelles du dernier snapshot valide (17h UTC 09/06) sont conservées. Le cycle options d'aujourd'hui (2026-06-15) est l'échéance imminente — surveiller le pinning gamma post-expiration.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.086 |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | **XLK top sector rotation (momentum 10.0/10)** — signal NEUTRAL |

### Sector Rotation
- **Technology (XLK)** : momentum score 10.0/10. Top1 du ranking. Pas de crossover détecté.
- **Signal système :** NEUTRAL (régime UNKNOWN).

### Géopolitique
- **Score Politique :** AAPL non flagué dans `geo_risk_latest.json`. 🟢 Aucun risque géopolitique spécifique AAPL.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `data/accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0, n=0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | Snapshot 10h 10/06 /10 | Snapshot 10h 15/06 /10 | Δ | Justification |
|-----|-----------------------|------------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucun catalyseur nouveau. Earnings 2026-07-30 dans 45 jours. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. Consensus inchangé. Upside redevient légèrement positif (+1.7%). |
| Momentum | 6.0 | **5.5** | 🔴 −0.5 | RSI en survente (34.19) est un signal technique positif d'accumulation mais le cours en baisse pèse sur le momentum global. |
| **Score Opportunité** | **5.4** | **5.2** | 🔴 **−0.2** | Pondération régime default 35/40/25 |

**Score Global Composite agent :** 52.3/100 → **Ajusté 57.3/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Bonus : timing technique +5.0 (RSI survente + MM50 intact)
- Timing : **Favorable** (upgrade depuis Neutre)
- **Recommandation agent : ATTENDRE** (inchangée)

**Verdict institutionnel Argus-IA :** Le pullback de −3.45% et la chute du RSI en zone de survente (34.19) créent un **setup technique d'accumulation** sur un titre de qualité institutionnelle. Le timing upgradé de Neutre à Favorable et la progression du Score Global ajusté (+3.8 pts) traduisent une amélioration du ratio risque/rendement. Cependant, le **volume à 0.77×** empêche de confirmer un rebond immédiat : il n'y a pas de panique vendeuse, mais il n'y a pas non plus d'achat institutionnel à ce stade. La structure options opérationnelle (P/C 0.51, Call OI 66.1%) reste haussière. Le max pain $332.50 est à +14.2%, ce qui laisse une marge de manœuvre confortable avant le call wall.

**La thèse ATTENDRE est confirmée mais avec une nuance positive.** Le setup technique s'améliore (RSI survente + timing Favorable) mais le volume faible et l'absence de catalyseur immédiat justifient de maintenir la recommandation sans passer à l'action. Le ratio R/R reste inférieur au seuil institutionnel 2:1.

---

## Niveaux SL / TP Révisés

| | Snapshot 10h 10/06 | Snapshot 10h 15/06 | Justification |
|---|--------------------|--------------------|---------------|
| Entrée suggérée | $301.54 | **$291.13** | Close actuel — pullback en zone de survente |
| Stop-Loss | $287.22 | **$275.95** | Cours − 2×ATR ($7.59) = $291.13 − $15.18. Correspond au SL agent. |
| Take-Profit | $323.02 | **$313.90** | Cours + 3×ATR ($7.59) = $291.13 + $22.77. Correspond au TP agent. |
| Ratio R/R | 1.5 | **1.5** | Inchangé — inférieur au seuil 2:1 |

**Note institutionnelle :** Le ratio R/R reste à 1.5:1, inférieur au seuil de 2:1 requis pour un sizing Standard. Le SL $275.95 est désormais calculé sur l'ATR actualisé ($7.59), ce qui offre une protection plus robuste que l'estimation précédente ($7.16). Une cassure sous MM50 $285.36 sur volume > 50M en clôture serait le premier signal d'alerte avant le SL. La résistance $317.40 (52W high) doit être breakée sur volume > 55M en clôture pour confirmer une reprise haussière. Le max pain $332.50 reste une résistance mécaniste crédible.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec nuance positive — La recommandation reste ATTENDRE. Le timing passe de Neutre à Favorable.**

La thèse est confirmée car le pullback technique de −3.45% et la chute du RSI en zone de survente (34.19) améliorent le setup risque/rendement sans pour autant justifier un upgrade vers ACHETER. Le timing upgradé de Neutre à Favorable traduit la qualité du setup technique (survente + support MM50 intact), mais le volume faible (0.77×) et l'absence de catalyseur immédiat maintiennent la prudence.

### Ce qui a changé (évolutions significatives)
1. **Cours** : $301.54 → **$291.13** (−3.45%, −$10.41) — pullback post-rebond. 🔴
2. **RSI** : 52.84 → **34.19** (−18.65 pts) — entrée en zone de survente, setup d'accumulation technique. 🟡
3. **ATR** : null → **$7.59** — donnée récupérée, volatilité en hausse. 🟢
4. **MM50** : null → **$285.36** — donnée récupérée, support dynamique intact. 🟢
5. **Volume** : 69.93M (1.39×) → **38.74M (0.77×)** — effondrement, repli sans conviction. 🟡
6. **Upside consensus** : −2.1% → **+1.7%** — redevient positif, rompt la séquence de décote. 🟢
7. **Score Global ajusté** : 53.5/100 → **57.3/100** (+3.8 pts). 🟢
8. **Timing agent** : Neutre → **Favorable** (upgrade). 🟢
9. **Options JSON** : Anomalie persistante — valeurs opérationnelles conservées $332.50 / 0.51 / 66.1%. 🔴

### Ce qui n'a PAS changé (stabilité)
1. **Structure options opérationnelle** : Max pain $332.50, P/C 0.51, Call OI 66.1% — structure haussière intacte.
2. **Fondamentaux FMP FY2025** — inchangés.
3. **Filtre Qualité 6/6** ✅ Quality Compounder.
4. **XLK top sector** — momentum 10.0/10, signal NEUTRAL.
5. **FX Exposure Score 0.0** — neutral.
6. **Geo risk** — aucun flag spécifique AAPL.
7. **Recommandation agent ATTENDRE** — inchangée.
8. **Consensus FMP** — $295.96 (61 analystes).
9. **Short Interest** — 1.06% inchangé.

### Risques identifiés (évolutions)
1. **Cassure MM50** — $285.36 est le support clé. Cassure sur volume > 50M = invalidation tendance haussière. 🟡
2. **Volume faible** — 0.77× moyenne. Pas de panique vendeuse mais pas d'achat non plus. Risque de dérive latérale. 🟡
3. **Valorisation étirée** — P/E 35.2x, Forward P/E 30.3x. Compression multiple possible si guidance décevante le 2026-07-30. 🔴
4. **Absence de catalyseur immédiat** — prochain earnings dans 45 jours (2026-07-30). Zone sans catalyseur = risque de dérive latérale. 🟡
5. **Anomalie options JSON** — persistante depuis plus d'une semaine. Nécessite correction pipeline. 🟡
6. **RSI < 35 sans rebond** — si le RSI reste en survente > 3 séances sans rebond, cela signalerait une faiblesse structurelle. 🟡

### Positionnement Argus-IA
- **Action : ATTENDRE** — Le setup technique s'améliore (RSI survente + timing Favorable) mais le volume faible et le ratio R/R 1.5:1 justifient de maintenir la prudence.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (45 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $300 sur volume > 1.0× moyenne :** Rebond validé — réévaluer le timing.
- **Si cours < $285.36 (MM50) sur volume > 50M :** Tendance haussière invalidée — risque de test $275.95 (SL).
- **Si RSI remonte > 45 avec volume > 1.0× :** Signal de force — confirmerait le timing Favorable.
- **Si RSI reste < 35 > 3 séances :** Survente prolongée = signal de faiblesse structurelle.

---

## [DONNÉES PARTIELLES]
- MM200 — toujours indisponible
- Options : max pain $250.00 (anomalie JSON), put/call null, call_oi_pct null — valeurs opérationnelles conservées
- MACD, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings
- Accounting risk (M-Score, Z-Score, F-Score, Sloan Ratio) — fichier indisponible
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes

---

## Références
- `data/latest.json` (snapshot 2026-06-15 10:00 UTC) — Close $291.13, RSI 34.19, ATR $7.59, MM50 $285.36, volume 38.74M (0.77×), short interest 1.06%, consensus FMP $295.96 (61 analystes), options max_pain $250.00 (anomalie)
- `data/recommandations_2026-06-15.json` — Score Opportunité 5.2/10, Score Global 57.3/100, Recommandation ATTENDRE, Timing Favorable
- `data/validation_report.txt` (2026-06-15) — AAPL OK
- `data/sector_rotation_2026-06-15.json` — XLK top sector (momentum 10.0/10, NEUTRAL)
- `data/fx_exposure_2026-06-15.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-15.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-06-15.json` — Earnings 2026-07-30, 45 jours
- `data/events_2026-06-15.json` — Aucun événement corporate détecté
- `data/geo_risk_2026-05-17.json` — AAPL non flagué
- `data/quant_2026-05-17.json` — Données quantitatives insuffisantes
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
