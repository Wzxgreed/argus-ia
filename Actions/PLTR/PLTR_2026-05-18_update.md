# PLTR — Mise à jour Quotidienne (2026-05-18)

> **Source :** Données exclusives `data/latest.json` (2026-05-18 08:44 UTC) + agents recommandation, sector rotation, FX, watchman, social sentiment.
> **Référence précédente :** [PLTR_2026-05-17_init.md](PLTR_2026-05-17_init.md)

---

## Résumé des changements depuis J-1

| Indicateur | J-1 (2026-05-17) | Aujourd'hui (2026-05-18) | Δ |
|-----------|------------------|--------------------------|---|
| Cours close | $133.99 | $133.99 | 0.00% |
| Change vs previous close | — | +0.19% | — |
| RSI 14j | 38.93 | 38.93 | 0 |
| MM 50j | 144.40 | 144.40 | 0 |
| Volume 20j moy. | 44.35M | 44.35M | 0 |
| Volume jour | 32.30M | 32.34M | — |
| ATR 14j | 5.72 | 5.72 | 0 |
| Max Pain options | $80 | **$50** | **−37.5%** |
| Score Catalyseur | 4.0/10 | **6.8/10** | **+2.8** |
| Score Valorisation | 2.0/10 | **4.5/10** | **+2.5** |
| Score Momentum | 3.0/10 | **3.5/10** | **+0.5** |
| Score Opportunité | 3.0/10 | **5.1/10** | **+2.1** |
| Score Global ajusté | — | **42.5/100** | — |
| Action recommandée | SURVEILLER | **SURVEILLER** | → Confirmé |

**Verdict :** Données de marché inchangées, mais recalcul des scores agents après intégration des ratios FMP annual FY2025. La thèse **SURVEILLER** est confirmée malgré une amélioration des scores fondamentaux.

---

## Mise à jour Technique

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| Cours | $133.99 | Stable vs J-1 |
| RSI 14j | 38.93 | Zone neutre-baisse, inchangé |
| MM 50j | 144.40 | Cours **−7.2% sous MM50** — tendance baissière intacte |
| MM 200j | — | [DONNÉES MANQUANTES] |
| Golden/Death Cross | Non | Aucun signal de croisement |
| Volume relatif vs 20j | −27% | Contraction significative persistante |
| Fourchette 52 semaines | $118.93 / $207.52 | Positionné à 36% du range |
| ATR 14j | $5.72 | Volatilité moyenne |
| Max Pain (2026-05-22) | **$50.00** | [ANOMALIE DATA] — divergence de 63% sous le spot vs $80 J-1. Données options inconsistantes ; ne pas utiliser pour le positionnement. |
| Timing verdict | **Défavorable** | Sous MM50 + RSI < 40 + volumes repliés |

**Évolution :** Aucun changement technique significatif. La structure reste baissière à court terme. Le max pain à $50 est une anomalie flagrante (changement de 37.5% en 24h sans justification) — probable erreur de flux options ou expiration proche (2026-05-22) créant un artefact.

---

## Mise à jour Fondamentale

### Données FMP Annual FY2025 (nouvellement intégrées)

| Métrique | Valeur | Contexte |
|---------|--------|----------|
| Gross Margin | 82.4% | Excellente — business model software à forte levée |
| Operating Margin | 31.6% | Rentabilité opérationnelle élevée |
| Net Margin | 36.3% | Très élevée (bénéfice > CA après adjustments) |
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

**Interprétation :** FMP utilise des données FY2025 annualisées avec une capitalisation boursière plus élevée, tandis que Yahoo rapporte des métriques TTM / close actuel. L'écart massif sur le P/E (152x vs 259x) suggère que le bénéfice FY2025 FMP est inférieur au bénéfice TTM Yahoo — probablement dû à des charges extraordinaires ou SBC non ajustées. **L'agent recommandation a probablement intégré les données FMP pour rehausser le score Valorisation**, mais cette amélioration doit être prise avec prudence compte tenu des multiples extrêmes dans les deux cas.

---

## Mise à jour Sentiment / Options / News

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| News du jour | — | Aucune news PLTR détectée dans `news_latest.json` |
| Social Sentiment (Reddit) | No data | Aucun post collecté ; alerte EXTREME_BEARISH automatique (artefact d'absence de données) |
| Put/Call Ratio | — | [DONNÉES MANQUANTES] |
| Call OI % | — | [DONNÉES MANQUANTES] |
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

**Explication du réajustement :** L'amélioration du score Valorisation (+2.5) provient de l'intégration des ratios FMP (marges élevées, bilan solide). Le score Catalyseur (+2.8) est soutenu par le consensus analystes (33 analysts, PT $187.61 = +40% upside). Cependant, le malus technique reste lourd : RSI < 40, cours sous MM50, volumes contractés de 27%. L'Agent Recommandation maintient l'action **SURVEILLER** car le timing d'entrée est défavorable malgré une qualité fondamentale reconnue.

---

## Niveaux et Ratio R/R (Révision)

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| Cours actuel | $133.99 | — |
| Stop-loss suggéré | **$122.55** | Cours − 2×ATR = $133.99 − $11.44 |
| Take-profit suggéré | **$151.15** | Cours + 3×ATR = $133.99 + $17.16 |
| Ratio R/R | **1.5** | Maintien du ratio institutionnel |
| Upside vers consensus PT | +40.0% | $187.61 — horizon long terme |

**Aucun changement** des niveaux SL/TP vs J-1 (données techniques inchangées).

---

## Contexte Macro & Sectoriel

| Facteur | État | Impact PLTR |
|---------|------|-------------|
| Régime macro | Stagflation (CPI 3.8%, 10Y 4.595%, pétrole $105+) | Pénalisant pour les multiples de croissance élevés |
| DXY | Stable (0% change) | Neutre |
| XLK (Technology) | **Top sector** — Momentum 10.0/10, RS 20j +10.1% | **Vent favorable** structurel |
| FX Exposure PLTR | 55% revenus hors-USD (EUR/CNY) | fx_impact_score 0.0 — aligned, pas de divergence |
| Beta 1.52 | Élevé | Amplifie les rotations sectorielles |

---

## Conclusion — État de la Thèse

**Statut : SURVEILLER — Thèse confirmée, pas modifiée.**

**Arguments confirmants :**
- Marges opérationnelles et nettes excellentes (FMP FY2025 : GM 82%, OM 32%, NM 36%)
- Bilan solide : quasi-zero dette, current ratio 7.1, ROIC 18%
- Consensus analystes actif (33 analysts, PT $187.61 = +40% upside)
- XLK leader sectoriel — environnement favorable aux techs

**Arguments limitants :**
- Timing technique défavorable : sous MM50 (−7.2%), RSI 38.93, volumes −27%
- Multiples extrêmes quel que soit le source (P/E 152x–259x, EV/Revenue 60x–94x)
- Divergence data Yahoo vs FMP sur toutes les métriques de valorisation [DONNÉES PARTIELLES]
- Anomalie Max Pain $50 (63% sous spot) — données options non fiables à court terme
- Aucune news ni catalyseur immédiat avant earnings août

**Scénarios :**
1. **Optimiste (25%)** : Rebond sur support + rotation sectorielle tech continue → retour vers MM50 ($144) puis test du consensus PT
2. **Central (50%)** : Consolidation latérale $130–$145 en l'absence de catalyseur jusqu'à earnings août
3. **Pessimiste (25%)** : Compression multiple dans un environnement stagflationniste → test du support $118.93 (52w low)

**Prochaines étapes :**
- Surveiller le croisement MM50 / volume pour un signal de retournement technique
- Vérifier la cohérence du Max Pain à la prochaine expiration (2026-05-22)
- Préparer `_preview.md` si earnings approchent à ≤ 5jours (actuellement 77j)
