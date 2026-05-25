# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-05-25

**Date :** 2026-05-25
**Type :** Mise à jour technique post-pipeline quotidien
**Analyse précédente :** [SPCX_2026-05-20_update.md](./SPCX_2026-05-20_update.md)

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (2026-05-20) | Actuel 2026-05-25 | Changement |
|--------|------------------------|-------------------|------------|
| Cours close | $21.95 | $22.40 | **+2.05%** |
| RSI 14j | 44.5 | 62.4 | **+17.9 pts** |
| ATR 14j | $0.25 | $0.27 | +$0.02 |
| MM 50j | $21.97 | $21.99 | +$0.02 |
| Position vs MM50 | Sous | **Au-dessus** | 🟢 **Retour haussier** |
| Volume | 2 647 | 16 751 | **+533%** |
| Volume vs moy. 20j | 1.26× (base 2 108) | **4.48×** (base 3 739) | 🔴 **Explosion de volume** |
| 52w range | $21.32 – $26.61 | $21.32 – $26.61 | Inchangé |
| Distance 52w high | −17.4% | −15.8% | +1.6 pt |
| Distance 52w low | +3.0% | +5.1% | +2.1 pt |
| Recommandation | SURVEILLER | **ATTENDRE** | 🟢 Reclassement haussier |
| Score Opportunité | 5.2/10 | 5.8/10 | +0.6 pt |
| Score Momentum | 3.5/10 | 7.5/10 | **+4.0 pts** |
| Score Global Ajusté | 43.5/100 | 58.0/100 | +14.5 pts |
| Timing | Défavorable | Neutre | 🟢 Amélioration |

**Verdict macro :** Aucun catalyseur sectoriel identifié dans les news du jour (`data/events_latest.json` absent, `data/news_latest.json` absent). Le mouvement du jour (+2.05%) est entièrement piloté par la technique : retour au-dessus de la MM50 ($22.40 > $21.99) avec un volume anormal (4.48× moyenne 20j), signalant un possible intérêt institutionnel ou un repositionnement de fonds thématiques. L'ETF s'éloigne de son 52w low ($21.32) et réduit sa décote vs 52w high à −15.8%.

---

## Mise à jour technique

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 62.4 | Zone haussière — franchissement de 60, pas de surachat |
| Position vs MM50j | $22.40 > $21.99 | **Au-dessus** — réparation de la cassure du 20/05 |
| Position vs MM200j | N/A | Non disponible dans `data/latest.json` |
| Volume vs moy. 20j | 4.48× | 🔴 **Anomalie volume** — accumulation ou repositionnement détecté |
| ATR 14j | $0.27 | Volatilité extrêmement faible (range intraday $0.47) |
| 52w low / high | $21.32 / $26.61 | −15.8% vs 52w high, +5.1% vs 52w low |

**Niveaux clés :**
- Support immédiat : $21.99 (MM50, ancienne résistance devenue support)
- Support secondaire : $21.32 (52w low)
- Résistance immédiate : $22.76 (high du jour)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Neutre. La cassure sous la MM50 du 20/05 est réparée après 3 séances de consolidation. Le volume de 16 751 actions (vs moyenne 3 739) est le plus élevé observé depuis le début du suivi (18/05). Ce pic de volume sans news macro ni sectorielle suggère un flux d'ordres interne (rééquilibrage de fonds, arbitrage NAV/premium, ou rotation sectorielle). L'ATR de $0.27 confirme un range d'action très étroit — le mouvement de +2.05% est donc significatif en termes relatifs.

---

## Mise à jour fondamentale

SPCX est un ETF thématique SPAC/post-IPO (Financial Services / Asset Management). Le Filtre Qualité 6 critères et les métriques fondamentales classiques ne s'appliquent pas.

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| P/E | N/A | ETF — non applicable |
| Forward P/E | N/A | ETF — non applicable |
| Market cap | N/A | ETF — non applicable |
| Beta | N/A | Non calculé dans `data/latest.json` |
| Dividend yield | N/A | Non distribué |
| Sector | Financial Services | Asset Management |

**Thèse ETF :** Aucun changement fondamental. La décote de −15.8% vs 52w high reflète la fatigue structurelle du marché SPAC, mais le rapprochement avec la MM50 et le volume anomalie suggèrent un potentiel de rebond technique. Aucun catalyseur sectoriel (reprise IPO/SPAC, baisse des taux, M&A) n'a été identifié dans les news du jour. `data/events_latest.json` absent — 0 événement corporate pour SPCX.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_latest.json` absent, `data/news_latest.json` absent |
| Social sentiment | No data | `data/social_sentiment_latest.json` absent |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable à un ETF thématique |
| FX Exposure | 🟢 | `data/fx_exposure_latest.json` absent — ETF non concerné |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` absent — pas de flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` absent — pas assez de signaux historiques |
| Recommandations | N/A | `data/recommandations_latest.json` absent — pas de scoring agent pour SPCX |

**Anomalie data quality :** `data/upcoming_events_latest.json` absent. Le pipeline précédent signalait un faux événement `earnings` pour SPCX (erreur FMP) — cet artefact n'est plus présent.

**Conclusion sentiment :** Silence fondamental complet. Le volume anormal est donc 100% technique/arbitrage et non piloté par une news. Cela limite la durabilité du mouvement mais confirme l'absence de risque de gap baissier immédiat.

---

## Scoring global (agents pipeline 2026-05-25)

| Axe | Score | Changement vs 20/05 | Commentaire |
|-----|-------|---------------------|-------------|
| Score Catalyseur | 5.5/10 | +0.5 | Modéré — absence de catalyseur fondamental, mais volume anormal = signal d'intérêt |
| Score Valorisation | 5.0/10 | = | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 7.5/10 | +4.0 | 🟢 **Haussier** — retour au-dessus MM50, RSI 62.4, volume ×4.5 |
| **Score Opportunité** | **5.8/10** | +0.6 | Pondération régime Normal : C×35% + V×40% + M×25% |
| **Score Global** | **58.0/100** | +14.5 | Avant ajustements |
| **Score Global Ajusté** | **58.0/100** | +14.5 | Pas de malus/bonus (fichiers agents absents) |

**Malus / Bonus appliqués :**
- Accounting : N/A (fichier absent — ETF non concerné)
- Geo : 0 (fichier absent — pas de flag)
- FX : 0 (fichier absent)
- Event : 0 (fichier absent — aucun événement corporate réel)
- Social : 0 (fichier absent)
- Quant : 0 (fichier absent)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé.

---

## Révision des niveaux SL / TP

La recommandation est désormais **ATTENDRE** — les niveaux ci-dessous sont fournis à titre de référence en cas de confirmation au-dessus de la MM50 avec volume soutenu.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix entrée suggéré | $22.40 | Close du jour (source `data/latest.json`) |
| Stop-loss | $21.86 | Close − 2×ATR = $22.40 − $0.54 |
| Take-profit | $23.21 | Close + 3×ATR = $22.40 + $0.81 |
| Ratio R/R | 1.5× | Gain $0.81 / Perte $0.54 |

**Verdict sizing :** Aucune entrée immédiate. Le setup technique s'améliore mais le score global (58/100) reste sous le seuil de 60 pour un ACHETER Réduit. Le volume anormal est un signal positif mais non confirmé par un catalyseur fondamental. Attendre une deuxième clôture au-dessus de la MM50 avec volume >2× moyenne pour réactiver un achat réduit.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **MODIFIÉE** — reclassement de SURVEILLER à ATTENDRE

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ✅ **Au-dessus** ($22.40 > $21.99) — réparation technique |
| RSI | ✅ Haussier (62.4) — franchissement de 60, pas de surachat |
| Volume | 🟢 **Anomalie haussière** (4.48× moyenne) — signal d'intérêt |
| Catalyseur | ❌ Aucun identifié — mouvement 100% technique |
| Risque technique | 🟡 MM50 redevient support, 52w low tient |

- **Modification :** La micro-tendance baissière observée depuis le 20/05 est cassée. Le cours a clôturé au-dessus de la MM50 pour la première fois depuis la cassure du 20/05, avec un volume record (16 751 vs moyenne 3 739). Le score Momentum est remonté de 3.5 à 7.5/10, entraînant une remontée du Score Global Ajusté de 43.5 à 58.0. La recommandation passe de SURVEILLER à ATTENDRE.
- **Nuances :** Le mouvement de +2.05% est d'amplitude modérée mais le volume est exceptionnel pour cet ETF peu liquide. L'absence de news fondamentale limite la conviction — il peut s'agir d'un rééquilibrage de fonds ou d'un arbitrage NAV. Le range intraday ($0.47) reste faible, confirmant un mouvement contrôlé et non spéculatif.
- **Invalidation :** Une clôture sous $21.32 (52w low) avec volume >1.5× moyenne invaliderait totalement la thèse et justifierait un reclassement en ÉVITER. Une clôture sous $21.99 (MM50) sans volume anormal ramènerait à SURVEILLER.
- **Rehaussement :** Une deuxième clôture au-dessus de $22.40 avec volume >2× moyenne et RSI stable > 55 réactiverait le setup ACHETER (Réduit).

**Recommandation :** **ATTENDRE**
**Prix cible référence :** $23.21 (+3.6% upside)
**Stop-loss référence :** $21.86 (−2.4% downside)
**Horizon :** 1–2 semaines (attente de confirmation)
**Conviction :** Modérée — le setup technique se répare mais le manque de catalyseur fondamental et la faible liquidité historique rendent l'entrée prématurée. Surveiller le volume demain.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 4.48× moy. 20j | 🔴 Anomalie | Signal d'accumulation ou repositionnement de fonds |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | N/A | — | Données non disponibles |
| Révisions consensus | N/A | — | Non applicable |

**Conclusion radar :** Volume anormal haussier — le seul signal inhabituel détecté. À surveiller demain pour confirmer l'accumulation ou identifier un repli.

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|------------------|
| Reprise du marché SPAC / IPO | 1–3 mois | +5–10% sur SPCX | — |
| Cassure du 52w low ($21.32) | Immédiat | — | −3–5% supplémentaires, reclassement ÉVITER |
| Retour sous MM50 ($21.99) sans volume | 1–3j | — | Retour à SURVEILLER |
| Volume >2× moyenne demain | 1j | Confirmation accumulation | Distribution si cours baisse |
| News macro favorable (taux en baisse) | Variable | Soutien aux SPACs | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : [SPCX_2026-05-20_update.md](./SPCX_2026-05-20_update.md)
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : $22.70
- Prix cible révisé : $23.21 (+$0.51, ajustement ATR + retour MM50)
- Recommandation précédente : SURVEILLER
- Recommandation révisée : **ATTENDRE**
- Raison principale : Retour au-dessus MM50 ($22.40 > $21.99), volume anormal ×4.5, RSI remonté à 62.4 — setup technique réparé mais sans catalyseur fondamental
- Thèse : 🟡 Modifiée
