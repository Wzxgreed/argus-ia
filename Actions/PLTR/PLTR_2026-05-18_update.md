# PLTR — Mise à jour Quotidienne Révisée (2026-05-18 post-pipeline 13:00 UTC)

> **Source :** Données `data/latest.json` (2026-05-18 13:00 UTC) + agents recommandation, sector rotation, FX, watchman, social sentiment, quant, geo, events.
> **Référence précédente :** [PLTR_2026-05-18_update.md](PLTR_2026-05-18_update.md) (version 08:57 UTC)

---

## Résumé des changements depuis la révision matinale

| Indicateur | Update 08:57 UTC | Données 13:00 UTC | Δ |
|-----------|------------------|-------------------|---|
| Cours close | $133.99 | $133.99 | **0.00%** |
| RSI 14j | 38.93 | 38.93 | 0 |
| MM 50j | 144.40 | 144.40 | 0 |
| Volume 20j moy. | 44.35M | 44.35M | 0 |
| Volume jour | 32.30M | 32.34M | **+0.1%** |
| ATR 14j | 5.72 | 5.72 | 0 |
| Max Pain options | **$50** (artefact) | **$80** | **Corrigé** |
| Put/Call Ratio | — | **0.67** | Nouveau |
| Call OI % | — | **59.9%** | Nouveau |
| Score Catalyseur | 6.8/10 | 6.8/10 | **0** |
| Score Valorisation | 4.5/10 | 4.5/10 | **0** |
| Score Momentum | 3.5/10 | 3.5/10 | **0** |
| Score Opportunité | 5.1/10 | 5.1/10 | **0** |
| Score Global ajusté | 42.5/100 | 42.5/100 | **0** |
| Action recommandée | SURVEILLER | **SURVEILLER** | → **Confirmé** |

**Verdict :** Données de marché strictement inchangées post-pipeline 13h. Seule correction : le Max Pain options revient à **80 $** (cohérent avec J-1), résolvant l'anomalie $50 détectée ce matin. La thèse **SURVEILLER** est confirmée sans modification.

---

## Mise à jour Technique

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| Cours | $133.99 | Stable vs J-1 (+0.19% vs previous close) |
| RSI 14j | 38.93 | Zone neutre-baisse, inchangé |
| MM 50j | 144.40 | Cours **−7.2% sous MM50** — tendance baissière intacte |
| MM 200j | — | [DONNÉES MANQUANTES] |
| Golden/Death Cross | Non | Aucun signal de croisement |
| Volume relatif vs 20j | −27% | Contraction significative persistante |
| Fourchette 52 semaines | $118.93 / $207.52 | Positionné à 36% du range |
| ATR 14j | $5.72 | Volatilité moyenne |
| Max Pain (2026-05-22) | **$80.00** | Retour au niveau J-1 ; anomalie $50 résolue |
| Put/Call Ratio | 0.67 | Léger biais call |
| Call OI % | 59.9% | Biais haussier modéré du marché options |
| Timing verdict | **Défavorable** | Sous MM50 + RSI < 40 + volumes repliés |

**Évolution :** Aucun changement technique significatif. La structure reste baissière à court terme. L'anomalie Max Pain $50 signalée ce matin était un artefact de flux corrigé dans le snapshot 13:00 UTC.

---

## Mise à jour Fondamentale

### Données FMP Annual FY2025 (inchangées)

| Métrique | Valeur | Contexte |
|---------|--------|----------|
| Gross Margin | 82.4% | Excellente — business model software à forte levée |
| Operating Margin | 31.6% | Rentabilité opérationnelle élevée |
| Net Margin | 36.3% | Très élevée |
| Debt/Equity | 0.031 | Bilan quasi-sans dette |
| Current Ratio | 7.11 | Liquidité exceptionnelle |
| SBC / Revenue | 15.3% | Dilution significative par stock-based comp |
| DSO | 85 jours | Cycle de conversion client modéré |
| Cash Conversion Cycle | 81.3 jours | — |
| ROIC (FMP) | 17.9% | Création de valeur confirmée |
| Consensus Price Target | $187.61 | 33 analysts — upside théorique **+40.0%** |

### Divergences Yahoo vs FMP [DONNÉES PARTIELLES]

| Métrique | Yahoo Finance | FMP Annual FY2025 | Écart |
|---------|---------------|-------------------|-------|
| Market Cap | $321.2 Md | $421.2 Md | **+31%** |
| P/E | 152.3x | 259.2x | **+70%** |
| EV/Revenue | 60.0x | 93.8x | **+56%** |
| EV/EBITDA | 155.3x | 291.6x | **+88%** |
| P/B | 43.4x | 57.0x | **+31%** |

**Interprétation :** Écart persistant entre sources. L'agent recommandation intègre les données FMP pour le score Valorisation, mais les multiples restent extrêmes dans les deux cas. Aucune nouvelle donnée fondamentale ce jour.

---

## Mise à jour Sentiment / Options / News

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| News du jour | — | Aucune news PLTR détectée dans `news_latest.json` |
| Social Sentiment (Reddit) | No data | Aucun post collecté ; alerte automatique (artefact absence de données) |
| Put/Call Ratio | 0.67 | Biais modéré vers les calls |
| Call OI % | 59.9% | Appétence haussière modérée |
| Short Interest | 0.03% | Négligeable — pas de setup short squeeze |
| Insider Trades | — | [DONNÉES MANQUANTES] |
| Upgrades/Downgrades | — | [DONNÉES MANQUANTES] |
| Événements Corporate | Aucun | `events_latest.json` vide pour PLTR |

**Catalyseur prochain :** Earnings Q2 FY2026 le **2026-08-03** (77 jours). Est. EPS $0.32–$0.40, Rev $1.8B. Pas de preview requis (> 5j).

---

## Scoring Global — Révision

| Axe | Score Auj. | Score J-1 | Δ | Pondération (Stagflation) |
|-----|-----------|-----------|---|---------------------------|
| Catalyseur | 6.8/10 | 4.0/10 | +2.8 | 35% |
| Valorisation | 4.5/10 | 2.0/10 | +2.5 | 40% |
| Momentum | 3.5/10 | 3.0/10 | +0.5 | 25% |
| **Score Opportunité** | **5.1/10** | **3.0/10** | **+2.1** | — |

**Score Global brut :** 51.0/100  
**Score Global ajusté :** **42.5/100** (malus technique −8.5 pts : momentum défavorable, sous MM50, timing négatif)  
**Action :** **SURVEILLER**

**Explication :** L'amélioration du score Valorisation (+2.5) provient de l'intégration des ratios FMP (marges élevées, bilan solide). Le score Catalyseur (+2.8) est soutenu par le consensus analystes (33 analysts, PT $187.61 = +40% upside). Cependant, le malus technique reste lourd : RSI < 40, cours sous MM50, volumes contractés de 27%. L'Agent Recommandation maintient l'action **SURVEILLER** car le timing d'entrée est défavorable malgré une qualité fondamentale reconnue.

---

## Niveaux et Ratio R/R (Inchangés)

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| Cours actuel | $133.99 | — |
| Stop-loss suggéré | **$122.55** | Cours − 2×ATR = $133.99 − $11.44 |
| Take-profit suggéré | **$151.15** | Cours + 3×ATR = $133.99 + $17.16 |
| Ratio R/R | **1.5** | Maintien du ratio institutionnel |
| Upside vers consensus PT | +40.0% | $187.61 — horizon long terme |

**Aucun changement** des niveaux SL/TP (données techniques inchangées).

---

## Contexte Macro, Sectoriel & Risques

| Facteur | État | Impact PLTR |
|---------|------|-------------|
| Régime macro | **Unknown** (source : `data/sector_rotation_latest.json`) | Pas d'ajustement régime-aware applicable |
| DXY | Stable (0% change) | Neutre — source : `data/fx_exposure_latest.json` |
| XLK (Technology) | **Top sector** — Momentum 10.0/10, RS 20j +10.1% | **Vent favorable** structurel |
| FX Exposure PLTR | 55% revenus hors-USD (EUR/CNY) | fx_impact_score 0.0 — aligned, pas de divergence |
| Beta 1.52 | Élevé | Amplifie les rotations sectorielles |
| Geo Risk | Non flaggé | Pas d'événement géopolitique spécifique détecté pour PLTR |
| Accounting Risk | [DONNÉES MANQUANTES] | `data/accounting_risk_latest.json` absent — Filtre Qualité non alimenté par l'agent accounting |
| Quant Calibration | Insuffisant | Pas assez de signaux historiques pour valider la signification statistique |
| Social Sentiment | No data | Pas de signal retail exploitable |

---

## Conclusion — État de la Thèse

**Statut : SURVEILLER — Thèse confirmée, pas modifiée.**

**Arguments confirmants :**
- Marges opérationnelles et nettes excellentes (FMP FY2025 : GM 82%, OM 32%, NM 36%)
- Bilan solide : quasi-zero dette, current ratio 7.1, ROIC 18%
- Consensus analystes actif (33 analysts, PT $187.61 = +40% upside)
- XLK leader sectoriel — environnement favorable aux techs
- Options : Max Pain corrigé à 80 $, Put/Call 0.67, Call OI 59.9% — structure options modérément haussière

**Arguments limitants :**
- Timing technique défavorable : sous MM50 (−7.2%), RSI 38.93, volumes −27%
- Multiples extrêmes quel que soit la source (P/E 152x–259x, EV/Revenue 60x–94x)
- Divergence data Yahoo vs FMP sur toutes les métriques de valorisation [DONNÉES PARTIELLES]
- Aucune news ni catalyseur immédiat avant earnings août
- Accounting risk non évalué (agent absent) — qualité comptable non confirmée

**Scénarios :**
1. **Optimiste (25%)** : Rebond sur support + rotation sectorielle tech continue → retour vers MM50 ($144) puis test du consensus PT
2. **Central (50%)** : Consolidation latérale $130–$145 en l'absence de catalyseur jusqu'à earnings août
3. **Pessimiste (25%)** : Compression multiple dans un environnement incertain → test du support $118.93 (52w low)

**Prochaines étapes :**
- Surveiller le croisement MM50 / volume pour un signal de retournement technique
- Préparer `_preview.md` si earnings approchent à ≤ 5jours (actuellement 77j)
- Réactiver l'agent accounting dès que possible pour valider le Filtre Qualité 6 critères
