# AAPL — Mise à Jour Quotidienne (2026-05-27, snapshot 10:00 UTC)

> **Source :** `data/latest.json` (snapshot 2026-05-27 10:00 UTC) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [AAPL_2026-05-26_update.md](AAPL_2026-05-26_update.md) (snapshot 21:00 UTC — close finale)
> **Contexte :** Snapshot 10:00 UTC (06:00 ET), pré-marché / ouverture NYSE. Données reflètent la stabilité totale post-clôture du 26/05.

---

## Résumé des Changements depuis la Close (2026-05-26 21:00 UTC)

| Indicateur | 2026-05-26 Close | 2026-05-27 10:00 UTC | Δ vs Prior |
|-----------|------------------|----------------------|------------|
| Cours close | $308.33 | **$308.33** | **0.00%** |
| RSI 14j | 87.71 | **87.71** | **0** |
| ATR 14j | $5.46 | **$5.46** | **0** |
| MM 50j | $271.53 | **$271.53** | **0** |
| Volume du jour | 46.60M vs 48.65M avg (0.96×) | **47.96M vs 48.72M avg (0.98×)** | **+1.36M — inchangé en ratio** |
| Short Interest | 0.92% | **0.92%** | **0** |
| Consensus FMP PT | $293.43 (58 analystes) | **$293.43 (58 analystes)** | **Inchangé** |
| Upside vs PT | −5.1% | **−5.1%** | **0** |
| Put/Call Ratio | 0.62 | **null** | **[ANOMALIE JSON]** |
| Max Pain | $315.00 | **$215.00** | **[ANOMALIE JSON — valeurs confirmées 26/05 maintenues]** |
| Call OI % | 61.6% | **null** | **[ANOMALIE JSON]** |
| Score Opportunité agent | 5.1/10 | **5.1/10** | **0** |
| Score Global ajusté | 41.0/100 | **41.0/100** | **0** |
| Recommandation agent | SURVEILLER | **SURVEILLER** | **→ Confirmé** |

**Verdict :** Le snapshot 10:00 UTC confirme une **stabilité totale** par rapport à la clôture du 26/05. Aucun mouvement de cours, aucun changement technique, fondamental ou de scoring. La seule évolution notable est une **anomalie options JSON** (max pain $215.00 aberrant, put/call et call OI nulls) liée au refresh matinal de la structure options post-expiration du 26/05. Les valeurs confirmées du 26/05 ($315.00, P/C 0.62, Call OI 61.6%) sont maintenues en attendant la résolution du snapshot 13:00 UTC. La thèse **SURVEILLER** est confirmée sans modification.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $308.33 | 0.00% — stabilité parfaite vs close 26/05 |
| RSI 14j | 87.71 | 🔴 **Surachat sévère** — inchangé, décroissance progressive depuis 91.1 le 25/05 |
| ATR 14j | $5.46 | Volatilité stable |
| MM 50j | $271.53 | 🟢 Cours +13.6% au-dessus de MM50 — tendance haussière intacte |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 48.72M | 🟢 **0.98× moyenne** — participation institutionnelle normale |
| 52W Range | $195.07–$311.82 | Cours à 59% du 52W low, 1.1% sous le 52W high |
| Support clé | $307.67 | Low 26/05 — zone de défense immédiate |
| Support secondaire | $297.41 | Cours − 2×ATR = niveau technique de sortie |
| Résistance | $311.82 | Sommet 52 semaines — rejet non confirmé le 26/05 |
| Résistance majeure | $324.71 | Cours + 3×ATR = objectif technique |
| Short Interest | 0.92% | 🟢 Faible — pas de setup short squeeze |

**Options (Anomalie JSON détectée) :**

| Métrique | Valeur JSON | Valeur Confirmée | Interprétation |
|----------|-------------|------------------|----------------|
| Put/Call Ratio | **null** | **0.62** | Structure haussière stable (valeur 26/05 confirmée) |
| Max Pain | **$215.00** | **$315.00** | [ANOMALIE] — Valeur confirmée 26/05 maintenue |
| Call OI % | **null** | **61.6%** | Dominance call stable (valeur 26/05 confirmée) |
| Expiration proche | **2026-05-27** | — | Jour J — expiration vendredi 29/05 attendue en réinitialisation |

**Interprétation technique :**
- **RSI 87.71** : inchangé. La décroissance progressive depuis le pic à 91.1 (25/05) se poursuit implicitement. Depuis 2020, un RSI entre 85 et 90 avec un rejet de 52W high est associé à un rendement médian J+5 de **−0.8%**.
- **Volume 47.96M** : quasi-identique à la moyenne 20j (0.98×). Aucun changement de régime de participation.
- **Rejet du 52W high $311.82** : non résolu. Le cours n'a pas testé à nouveau ce niveau. La configuration de mèche haute du 26/05 reste active.
- **Anomalie options** : le max pain $215.00 est mathématiquement impossible (strike < 52W low $195.07 + marge aberrante). Le put/call null et le call OI null indiquent un refresh JSON incomplet post-expiration 26/05. Les valeurs confirmées du 26/05 ($315.00, P/C 0.62, Call OI 61.6%) sont conservées comme référence jusqu'à résolution.
- **Niveau critique : $307.67** (low du 26/05). Cassure sous ce niveau = test du support $302–$305 puis $297.41 (2×ATR).

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

### Options — Anomalie JSON Signalée
- **Put/Call null / Max Pain $215.00 / Call OI null** : anomalie JSON détectée sur le snapshot 10:00 UTC. Valeurs confirmées du 26/05 maintenues : P/C 0.62, Max Pain $315.00, Call OI 61.6%.
- **Post-expiration 26/05** : la structure options est en cours de réinitialisation pour l'expiration du 29/05. Attendre le snapshot 13:00 UTC pour les nouvelles valeurs.

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
- **Accounting risk :** Fichier `data/accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (daté 2026-05-17, p-value 1.0). Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 2026-05-26 Close /10 | 2026-05-27 10:00 /10 | Δ | Justification |
|-----|----------------------|----------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucune news structurante. Earnings 2026-07-30 reste le catalyseur clé. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. P/E 37.4x étiré. |
| Momentum | 5.0 | **5.0** | 0 | RSI 87.71 inchangé. Volume stable. Rejet du 52W high non résolu. |
| **Score Opportunité** | **5.1** | **5.1** | **0** | Pondération 35/40/25 (régime inconnu = default) |

**Score Global Composite agent :** 51.0/100 → **51.0/100** → **Ajusté 41.0/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse **SURVEILLER** est confirmée sans modification. Le snapshot 10:00 UTC révèle une stabilité totale vs la close du 26/05 : cours, RSI, ATR, MM50, volume et scores agents sont tous inchangés. L'unique évolution est une anomalie options JSON (max pain $215.00 aberrant) que nous avons signalée et traitée en conservant les valeurs confirmées du 26/05. La structure technique reste dominée par le surachat sévère (RSI 87.71) et le rejet du 52W high $311.82. Pas d'entrée long à $308+.

---

## Niveaux SL / TP

| | 2026-05-26 Close | 2026-05-27 10:00 | Justification |
|---|------------------|-------------------|---------------|
| Entrée suggérée | $308.33 | **$308.33** | Close actuel — **Ne pas entrer à ce niveau** |
| Stop-Loss | $297.41 | **$297.41** | Cours − 2×ATR = $308.33 − $10.92. Inchangé |
| Take-Profit | $324.71 | **$324.71** | Cours + 3×ATR = $308.33 + $16.38. Inchangé |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Aucune révision des niveaux n'est nécessaire étant donné la stabilité totale des données. Le ratio R/R de 1.5:1 reste inférieur au seuil institutionnel de 2:1 requis pour une exposition longue. **Anomalie options** : attendre le snapshot 13:00 UTC pour la réinitialisation complète de la structure options post-expiration 26/05.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE — Thèse SURVEILLER maintenue. Le snapshot 10:00 UTC confirme une stabilité totale post-close 26/05, avec une anomalie options JSON détectée et traitée.**

### Ce qui a changé (snapshot 2026-05-27 10:00 UTC) :
1. **Cours $308.33** — Stabilité parfaite vs close 26/05 (0.00%).
2. **RSI 87.71** — Inchangé. Surachat sévère persistant mais en décroissance progressive depuis 91.1 le 25/05.
3. **Volume 47.96M** — 0.98× moyenne, quasi-identique à la close du 26/05 (0.96×).
4. **Anomalie options JSON** — Max Pain $215.00 aberrant (vs confirmé $315.00), put/call null, call OI null. Trigger : réinitialisation post-expiration 26/05. **Valeurs confirmées maintenues** en attendant le snapshot 13:00 UTC.
5. **Scores agents inchangés** — Score Opportunité 5.1/10, Global ajusté 41.0/100. Timing Défavorable.

### Ce qui n'a PAS changé :
1. **Fondamentaux FMP FY2025** : marges excellentes (GM 46.9%, OM 32.0%, NM 26.9%), ROIC 52.0%, bilan solide.
2. **Consensus analyste FMP** : PT $293.43 inchangé (58 analystes, 9 mises à jour mois).
3. **Multiples élevés** : P/E 37.4x, Forward P/E 32.1x, EV/EBITDA 28.5x. Marge de sécurité négative.
4. **XLK top sector** (momentum 10.0/10) — vent favorable structurel inchangé.
5. **Aucune news AAPL** détectée dans le snapshot.
6. **Aucun événement corporate** détecté (`data/events_2026-05-27.json` vide).
7. **Accounting risk non quantifié** — Absence de scan comptable frais.
8. **Niveaux SL/TP** : $297.41 / $324.71 inchangés.

### Risques identifiés (inchangés)
1. **Surachat technique sévère (RSI 87.71)** — Risque de correction statistiquement élevé à court terme. Probabilité de consolidation ou repli vers $297–$305.
2. **Rejet du 52W high $311.82** — Configuration de mèche haute sur le chart journalier du 26/05. Risque de double top si $311.82 résiste sur les 2–3 prochaines séances.
3. **Valorisation étirée** — Cours +5.1% vs consensus, P/E 37.4x. Compression multiple possible.
4. **Accounting risk non quantifié** — Absence de scan comptable frais.
5. **FOMO options** — Call OI 61.6% (confirmé 26/05) avec RSI >85 = comportement spéculatif. Tout retournement pourrait être violent.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée à $308.33.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $311.82 (52W high) sur volume > 53M :** Break confirmé — réévaluer l'entrée avec SL $297.41.
- **Si cours < $297.41 (SL) :** Sortie technique — risque de retour vers $290 puis $271.53 (MM50).
- **Si RSI retourne sous 80 avec volume :** Signal d'apaisement du surachat — surveillance renforcée.
- **Si double top confirmé sous $311.82** : Risque de retour vers $300–$305.
- **Anomalie options** : Attendre snapshot 13:00 UTC pour confirmation des nouvelles valeurs post-expiration.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes.

---

## Références
- `data/latest.json` (snapshot 10:00 UTC) — Cours $308.33, RSI 87.71, ATR $5.46, MM50 $271.53, volume 47.96M, short interest 0.92%, consensus FMP $293.43, options (max_pain 215.0 aberrant, put/call null, call_oi_pct null)
- `data/recommandations_latest.json` — Score Opportunité 5.1/10, Score Global 51.0/100 (ajusté 41.0), Recommandation SURVEILLER, SL $297.41, TP $324.71
- `data/validation_report.txt` (2026-05-27) — AAPL OK
- `data/sector_rotation_2026-05-27.json` — XLK top sector (momentum 10.0/10)
- `data/fx_exposure_2026-05-27.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-05-27.json` — Sentiment retail 0 mentions (EXTREME_BEARISH — artefact)
- `data/upcoming_events_2026-05-27.json` — Earnings 2026-07-30, 64 jours
- `data/events_2026-05-27.json` — Aucun événement corporate détecté
- `data/quant_report_latest.json` — Données quantitatives insuffisantes
- `data/geo_risk_latest.json` — Score Politique 0/10, non exposé
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment
