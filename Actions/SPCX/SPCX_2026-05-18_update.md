# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-05-18

**Date :** 2026-05-18
**Type :** Mise à jour technique post-pipeline quotidien
**Analyse précédente :** [SPCX_2026-05-18_preview.md](./SPCX_2026-05-18_preview.md)

---

## Résumé des changements depuis l'analyse précédente

L'analyse précédente était un template `preview` pour earnings (placeholders non remplis). Ce format était **inapproprié** : SPCX est un ETF dédié aux SPACs (Asset Management), sans earnings individuel au sens classique. Ce fichier constitue le **premier snapshot technique et scoring réel** du ticker.

| Donnée | Précédent (template) | Actuel 2026-05-18 | Changement |
|--------|-------------------|-------------------|------------|
| Cours close | N/A | $22.005 | — |
| Change | N/A | +0.07% | — |
| RSI 14j | N/A | 48.93 | Zone neutre |
| ATR 14j | N/A | $0.25 | Volatilité très faible |
| MM 50j | N/A | $21.97 | Cours au-dessus |
| MM 200j | N/A | N/A | Non disponible |
| Volume | N/A | 2 670 | 1.28× moy. 20j (2 091) |
| 52w range | N/A | $21.32 – $26.61 | Proche du 52w low |

---

## Mise à jour technique

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 48.93 | Neutre — ni surachat ni survente |
| Position vs MM50j | $22.005 > $21.97 | Au-dessus — tendance haussière micro |
| Position vs MM200j | N/A | Non disponible dans le snapshot |
| Volume vs moy. 20j | 1.28× | Légèrement supérieur, intérêt modéré |
| ATR 14j | $0.25 | Volatilité extrêmement faible (range étroit) |
| 52w low / high | $21.32 / $26.61 | Cours à -17.3% du 52w high, +3.2% du 52w low |

**Niveaux clés :**
- Support immédiat : $21.97 (MM50)
- Support majeur : $21.32 (52w low)
- Résistance : $22.08 (high du jour)

**Verdict timing :** Neutre à légèrement favorable. Le cours tient au-dessus de la MM50 malgré la proximité du 52w low. La volatilité très faible (ATR $0.25) indique un marché endormi — tout catalyseur sectoriel (ex. reprise SPAC, fusion majeure) pourrait provoquer un gap significatif.

---

## Mise à jour fondamentale

SPCX n'est pas une entreprise mais un ETF (SPACs & Recent IPOs). Le Filtre Qualité 6 critères **ne s'applique pas** à ce véhicule.

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| P/E | N/A | ETF — non applicable |
| Forward P/E | N/A | ETF — non applicable |
| Market cap | N/A | ETF — non applicable |
| Beta | N/A | Non calculé dans le snapshot |
| Dividend yield | N/A | Non distribué |
| Sector | Financial Services | Asset Management |

**Thèse ETF :** SPCX offre une exposition diversifiée au compartiment SPAC/post-IPO. La décote actuelle (-17% vs 52w high) reflète la fatigue du marché SPAC depuis 2021. Un catalyseur sectoriel (reprise M&A, marché primaire actif) serait nécessaire pour un rebond de significativité.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | Aucun événement corporate détecté (`data/events_latest.json` vide) |
| Social sentiment | No data | 0 mention Reddit, sentiment 0/10 (`social_sentiment_latest.json`) |
| Options | Non disponible | Bloc options vide dans `latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable à un ETF thématique |

**Conclusion sentiment :** Pas de signal. Pas de bruit retail, pas d'activité options inhabituelle, pas d'insider trades.

---

## Scoring global (agents pipeline 2026-05-18)

| Axe | Score | Commentaire |
|-----|-------|-------------|
| Score Catalyseur | 6.5/10 | Modéré — absence de catalyseur immédiat mais exposition optionnelle sectorielle |
| Score Valorisation | 5.0/10 | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 7.0/10 | Haussier — cours au-dessus MM50, volume légèrement supérieur |
| **Score Opportunité** | **6.0/10** | Pondération régime : C×35% + V×40% + M×25% |
| **Score Global** | **60.2/100** | Avant ajustements |
| **Score Global Ajusté** | **65.2/100** | — |

**Malus / Bonus appliqués :**
- Accounting : N/A (fichier absent — ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (exposition 25%, 🟢 aligned)
- Event : 0 (aucun événement corporate)
- Social : 0 (no data)
- Quant : 0 (pas assez de signaux historiques — calibration en cours)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé.

---

## Révision des niveaux SL / TP

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix entrée suggéré | $22.00 | Close du jour |
| Stop-loss | $21.50 | Close − 2×ATR = $22.00 − $0.50 |
| Take-profit | $22.75 | Close + 3×ATR = $22.00 + $0.75 |
| Ratio R/R | 1.5× | Gain $0.75 / Perte $0.50 |

**Verdict sizing :** Réduit — volatilité faible offre un SL serré, mais le potentiel de gain est limité (3.4% upside jusqu'au TP) sans catalyseur externe.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟡 Thèse INITIALISÉE (première analyse réelle)

Aucune analyse technique préalable n'existait pour SPCX. Le template `preview` précédent est obsolète et non pertinent pour un ETF. La thèse naissante se résume comme suit :

- **Confirmation :** Le cours tient au-dessus de la MM50 ($21.97), momentum haussier micro confirmé.
- **Nuances :** Pas de catalyseur identifié, volatilité extrêmement faible, absence de flux/options/news. L'ETF est proche de son 52w low — risque de cassure si le secteur SPAC reste endormi.
- **Invalidation :** Une clôture sous $21.32 (52w low) invaliderait le momentum haussier et justifierait un reclassement en SURVEILLER.

**Recommandation :** **ACHETER (Réduit)**
**Prix cible :** $22.75
**Stop-loss :** $21.50
**Horizon :** 1–3 mois
**Conviction :** Faible à Modérée — le setup technique est valide mais le manque de catalyseur limite l'upside.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 1.28× moy. 20j | Léger | Neutre — pas d'accumulation ni de distribution flagrante |
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
| Cassure du 52w low ($21.32) | Immédiat | — | -3–5% supplémentaires |
| Volume >2× moyenne | 1–5j | Accumulation détectée | Distribution détectée |
| News macro favorable (taux en baisse) | Variable | Soutien aux SPACs | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente (template) : [SPCX_2026-05-18_preview.md](./SPCX_2026-05-18_preview.md)
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : N/A
- Prix cible révisé : $22.75
- Recommandation : ACHETER (Réduit) (initialisée)
- Raison principale : Premier snapshot technique réel — momentum haussier micro au-dessus MM50, volatilité faible, SL serré
- Thèse : 🟡 Initialisée
