# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-05-20

**Date :** 2026-05-20
**Type :** Mise à jour technique post-pipeline quotidien
**Analyse précédente :** [SPCX_2026-05-19_update.md](./SPCX_2026-05-19_update.md)

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (2026-05-19) | Actuel 2026-05-20 | Changement |
|--------|------------------------|-------------------|------------|
| Cours close | $21.99 | $21.95 | −0.18% |
| RSI 14j | 46.07 | 44.5 | −1.57 pts |
| ATR 14j | $0.24 | $0.25 | +$0.01 |
| MM 50j | $21.97 | $21.97 | Stable |
| Position vs MM50 | Au-dessus | **Sous** | 🔴 Cassure technique |
| Volume | 3 415 | 2 647 | −22.5% |
| Volume vs moy. 20j | 1.53× (base 2 226) | 1.26× (base 2 108) | Normalisation |
| 52w range | $21.32 – $26.61 | $21.32 – $26.61 | Inchangé |
| Recommandation | ACHETER (Réduit) | **SURVEILLER** | 🔴 Reclassement |
| Score Opportunité | 6.0/10 | 5.2/10 | −0.8 pt |
| Score Momentum | 7.0/10 | 3.5/10 | −3.5 pts |
| Score Global Ajusté | 65.2/100 | 43.5/100 | −21.7 pts |
| Timing | Favorable | Défavorable | 🔴 Inflexion |

**Verdict macro :** Aucun catalyseur sectoriel. Le mouvement du jour est minime (−0.18%) mais la **cassure sous la MM50** ($21.95 < $21.97) constitue un signal technique d'inflexion. Le volume est retourné vers sa moyenne (1.26×), invalidant le léger pic d'intérêt observé hier. L'ETF est à −17.4% de son 52w high et à +3.0% de son 52w low.

---

## Mise à jour technique

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 44.5 | Neutre — légère baisse, zone favorable inchangée |
| Position vs MM50j | $21.95 < $21.97 | **Sous** — cassure micro, tendance baissière |
| Position vs MM200j | N/A | Non disponible dans `data/latest.json` |
| Volume vs moy. 20j | 1.26× | Retour à la normale, absence d'accumulation |
| ATR 14j | $0.25 | Volatilité extrêmement faible (range intraday $0.13) |
| 52w low / high | $21.32 / $26.61 | −17.4% vs 52w high, +3.0% vs 52w low |

**Niveaux clés :**
- Support immédiat : $21.32 (52w low)
- Résistance immédiate : $21.97 (MM50, ancien support devenu résistance)
- Résistance : $22.08 (high du jour)

**Verdict timing :** Défavorable. La cassure sous la MM50, même marginale (−$0.02), invalide le setup micro-haussier observé depuis le 18/05. L'absence de volume à la baisse atténue la gravité du signal, mais la direction technique est désormais négative. L'ATR de $0.25 offre toujours un range d'action très étroit.

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

**Thèse ETF :** Aucun changement fondamental. La décote de −17.4% vs 52w high reflète la fatigue structurelle du marché SPAC. Aucun catalyseur sectoriel (reprise IPO/SPAC, baisse des taux, M&A) n'a été identifié dans les news du jour (`data/events_latest.json` vide).

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_latest.json` vide — 0 événement corporate pour SPCX |
| Social sentiment | No data | 0 mention Reddit, sentiment 0/10 (`social_sentiment_latest.json`) |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable à un ETF thématique |
| FX Exposure | 🟢 | Exposition 25%, impact revenus/EPS 0%, divergence aligned (`fx_exposure_latest.json`) |
| Géopolitique | 🟢 | Pas de flag SPCX dans `geo_risk_latest.json` |
| Accounting | N/A | Fichier absent — ETF non concerné |
| Quant | N/A | Pas assez de signaux historiques — calibration en cours (`quant_report_latest.json`) |

**Anomalie data quality :** `data/upcoming_events_latest.json` signale un événement `earnings` le 2026-05-20 pour SPCX (source FMP, severity high). SPCX est un ETF thématique sans earnings classique — **cet événement est une erreur de source FMP et doit être ignoré**. Le fichier `SPCX_2026-05-20_preview.md` généré par le pipeline est un template inapproprié pour un ETF et n'est pas pris en compte dans cette analyse.

**Conclusion sentiment :** Silence complet. Pas de bruit retail, pas d'activité options inhabituelle, pas de news. Le marché ignore SPCX.

---

## Scoring global (agents pipeline 2026-05-20)

| Axe | Score | Changement vs 19/05 | Commentaire |
|-----|-------|---------------------|-------------|
| Score Catalyseur | 6.5/10 | = | Modéré — absence de catalyseur immédiat |
| Score Valorisation | 5.0/10 | = | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 3.5/10 | −3.5 | 🔴 **Baissier** — cassure sous MM50, volume normalisé |
| **Score Opportunité** | **5.2/10** | −0.8 | Pondération régime : C×35% + V×40% + M×25% |
| **Score Global** | **51.5/100** | −8.7 | Avant ajustements |
| **Score Global Ajusté** | **43.5/100**** | −21.7 | Après malus |

**Malus / Bonus appliqués :**
- Accounting : N/A (fichier absent — ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (exposition 25%, aligned)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (no data)
- Quant : 0 (pas assez de signaux)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé.

---

## Révision des niveaux SL / TP

La recommandation est désormais **SURVEILLER** — les niveaux ci-dessous sont fournis à titre de référence en cas de retour au-dessus de la MM50.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix entrée suggéré | $21.95 | Close du jour (source `data/latest.json`) |
| Stop-loss | $21.45 | Close − 2×ATR = $21.95 − $0.50 |
| Take-profit | $22.70 | Close + 3×ATR = $21.95 + $0.75 |
| Ratio R/R | 1.5× | Gain $0.75 / Perte $0.50 |

**Verdict sizing :** Aucune entrée. Le setup technique est invalide tant que le cours ne clôture pas au-dessus de la MM50 ($21.97) avec volume confirmatoire.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse **MODIFIÉE** — reclassement de ACHETER (Réduit) à SURVEILLER

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ❌ **Sous** ($21.95 < $21.97) — cassure marginale |
| RSI | ✅ Neutre favorable (44.5) |
| Volume | ⚠️ Normalisé (1.26×), absence d'accumulation |
| Catalyseur | ❌ Aucun identifié |
| Risque technique | 🔴 Cassure MM50 = signal de sortie / reclassement |

- **Modification :** La micro-tendance haussière observée depuis le 18/05 est cassée. Le cours a clôturé sous la MM50 pour la première fois depuis le snapshot du 18/05. Le score Momentum est tombé de 7.0 à 3.5/10, entraînant un recul du Score Global Ajusté de 65.2 à 43.5. La recommandation passe de ACHETER (Réduit) à SURVEILLER.
- **Nuances :** Le mouvement est d'amplitude très faible (−0.18%, range intraday $0.13). La cassure sous MM50 est marginale (−$0.02). L'absence de volume à la baisse suggère une faible conviction vendeuse — le risque d'accélération baissière reste limité tant que le 52w low ($21.32) tient.
- **Invalidation :** Une clôture sous $21.32 (52w low) avec volume >1.5× moyenne invaliderait totalement la thèse et justifierait un reclassement en ÉVITER.
- **Rehaussement :** Un retour au-dessus de $21.97 (MM50) avec volume >1.5× moyenne et RSI > 45 réactiverait le setup ACHETER (Réduit).

**Recommandation :** **SURVEILLER**
**Prix cible référence :** $22.70 (si rehaussement technique)
**Stop-loss référence :** $21.45
**Horizon :** —
**Conviction :** Faible — le setup technique est cassé, le manque de catalyseur et de liquidité rend l'ETF non attractif en entrée immédiate. Surveiller le test du 52w low ($21.32).

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 1.26× moy. 20j | Normal | Aucun signal d'accumulation ni de distribution |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | N/A | — | Données non disponibles |
| Révisions consensus | N/A | — | Non applicable |

**Conclusion radar :** Pas de signal inhabituel.

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|------------------|
| Reprise du marché SPAC / IPO | 1–3 mois | +5–10% sur SPCX | — |
| Cassure du 52w low ($21.32) | Immédiat | — | −3–5% supplémentaires, reclassement ÉVITER |
| Retour au-dessus MM50 ($21.97) + volume >1.5× | 1–5j | Réactivation ACHETER (Réduit) | — |
| Volume >2× moyenne | 1–5j | Accumulation détectée | Distribution détectée |
| News macro favorable (taux en baisse) | Variable | Soutien aux SPACs | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : [SPCX_2026-05-19_update.md](./SPCX_2026-05-19_update.md)
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : $22.71
- Prix cible révisé : $22.70 (−$0.01, ajustement ATR)
- Recommandation précédente : ACHETER (Réduit)
- Recommandation révisée : **SURVEILLER**
- Raison principale : Cassure technique sous MM50 ($21.95 < $21.97), score momentum en chute (7.0 → 3.5), volume normalisé
- Thèse : 🟡 Modifiée
