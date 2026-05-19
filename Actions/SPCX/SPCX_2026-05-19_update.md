# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-05-19

**Date :** 2026-05-19
**Type :** Mise à jour technique post-pipeline quotidien
**Analyse précédente :** [SPCX_2026-05-18_update.md](./SPCX_2026-05-18_update.md)

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (2026-05-18) | Actuel 2026-05-19 | Changement |
|--------|------------------------|-------------------|------------|
| Cours close | $22.005 | $21.99 | −0.07% |
| RSI 14j | 48.93 | 46.07 | −2.86 pts |
| ATR 14j | $0.25 | $0.24 | −$0.01 |
| MM 50j | $21.97 | $21.97 | Stable |
| Volume | 2 670 | 3 415 | +27.9% |
| Volume vs moy. 20j | 1.28× (base 2 091) | 1.53× (base 2 226) | Intérêt modéré ↑ |
| 52w range | $21.32 – $26.61 | $21.32 – $26.61 | Inchangé |

**Verdict macro :** Aucun mouvement significatif. Le cours reste au-dessus de la MM50 avec une volatilité extrêmement faible. Le volume journalier a augmenté de ~28% mais reste anémique en valeur absolue.

---

## Mise à jour technique

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 46.07 | Neutre — légèrement plus bas vs hier, zone favorable |
| Position vs MM50j | $21.99 > $21.97 | Au-dessus — micro-tendance haussière maintenue |
| Position vs MM200j | N/A | Non disponible dans `data/latest.json` |
| Volume vs moy. 20j | 1.53× | Intérêt modéré, mais liquidité globale faible |
| ATR 14j | $0.24 | Volatilité extrêmement faible (range intraday $0.21) |
| 52w low / high | $21.32 / $26.61 | −17.4% vs 52w high, +3.1% vs 52w low |

**Niveaux clés :**
- Support immédiat : $21.97 (MM50)
- Support majeur : $21.32 (52w low)
- Résistance : $22.09 (high du jour)

**Verdict timing :** Neutre à légèrement favorable. Le cours continue de tenir au-dessus de la MM50 malgré le RSI en légère baisse. L'ATR de $0.24 offre un range d'action très étroit — le setup technique reste valide mais offre peu de récompense sans catalyseur externe.

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

**Thèse ETF :** Aucun changement. La décote de −17% vs 52w high reflète la fatigue structurelle du marché SPAC. Aucun catalyseur sectoriel (reprise IPO/SPAC, baisse des taux, M&A) n'a été identifié dans les news du jour (`data/events_latest.json` vide).

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

**Conclusion sentiment :** Silence complet. Pas de bruit retail, pas d'activité options inhabituelle, pas d'insider trades, pas de news. Le fichier `SPCX_2026-05-19_preview.md` (preview earnings) est un template inapproprié pour un ETF sans earnings classique — il est ignoré dans l'analyse.

---

## Scoring global (agents pipeline 2026-05-19)

| Axe | Score | Commentaire |
|-----|-------|-------------|
| Score Catalyseur | 6.5/10 | Modéré — absence de catalyseur immédiat mais exposition optionnelle sectorielle |
| Score Valorisation | 5.0/10 | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 7.0/10 | Haussier — cours au-dessus MM50, volume légèrement supérieur |
| **Score Opportunité** | **6.0/10** | Pondération régime : C×35% + V×40% + M×25% (`recommandations_latest.json`) |
| **Score Global** | **60.2/100** | Avant ajustements |
| **Score Global Ajusté** | **65.2/100** | — |

**Malus / Bonus appliqués :**
- Accounting : N/A (fichier absent — ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (exposition 25%, 🟢 aligned)
- Event : 0 (aucun événement corporate dans `events_latest.json`)
- Social : 0 (no data)
- Quant : 0 (pas assez de signaux historiques — calibration en cours, `quant_report_latest.json`)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé.

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix entrée suggéré | $21.99 | Close du jour (source `data/latest.json`) |
| Stop-loss | $21.51 | Close − 2×ATR = $21.99 − $0.48 |
| Take-profit | $22.71 | Close + 3×ATR = $21.99 + $0.72 |
| Ratio R/R | 1.5× | Gain $0.72 / Perte $0.48 |

**Verdict sizing :** Réduit — volatilité faible offre un SL serré, mais le potentiel de gain reste limité (3.3% upside jusqu'au TP) sans catalyseur externe.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟢 Thèse **CONFIRMÉE**

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ✅ Au-dessus ($21.99 > $21.97) |
| RSI | ✅ Neutre favorable (46.07) |
| Volume | ⚠️ Faible mais en légère hausse (1.53×) |
| Catalyseur | ❌ Aucun identifié |
| Risque technique | 🟡 Cassure MM50 = signal de sortie |

- **Confirmation :** Le setup technique micro-haussier est inchangé. Cours au-dessus MM50, RSI neutre, SL serré. Aucun signal de distribution ni de pression vendeuse.
- **Nuances :** Le volume reste anémique malgré la hausse de 28% d'un jour sur l'autre. L'ETF est proche du 52w low. L'absence totale de catalyseur limite l'upside à la récompense ATR-based (~3.3%).
- **Invalidation :** Une clôture sous $21.32 (52w low) ou sous $21.97 (MM50) avec volume >2× moyenne invaliderait le momentum haussier et justifierait un reclassement en SURVEILLER.

**Recommandation :** **ACHETER (Réduit)**
**Prix cible :** $22.71
**Stop-loss :** $21.51
**Horizon :** 1–3 mois
**Conviction :** Faible à Modérée — le setup technique est stable mais le manque de catalyseur et de liquidité limite l'attrait relatif.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 1.53× moy. 20j | Léger ↑ | Neutre — pas d'accumulation ni de distribution flagrante |
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
| Cassure du 52w low ($21.32) | Immédiat | — | −3–5% supplémentaires |
| Cassure MM50 ($21.97) + volume >2× | 1–5j | — | Signal de distribution |
| Volume >2× moyenne | 1–5j | Accumulation détectée | Distribution détectée |
| News macro favorable (taux en baisse) | Variable | Soutien aux SPACs | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : [SPCX_2026-05-18_update.md](./SPCX_2026-05-18_update.md)
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : $22.75
- Prix cible révisé : $22.71 (−$0.04, ajustement ATR)
- Recommandation : ACHETER (Réduit) (confirmée)
- Raison principale : Setup technique stable — cours au-dessus MM50, RSI neutre, volatilité faible, aucun catalyseur ni news
- Thèse : 🟢 Confirmée
