# AXA — Mise à jour quotidienne

> **Date :** 2026-06-29 (snapshot 10h00 UTC)
> **Fichier précédent :** `AXA_2026-06-23_update_17h.md`
> **Type :** Mise à jour quotidienne

---

## 1. Résumé des changements

| Indicateur | Avant (23/06 17h) | Aujourd'hui (29/06 10h) | Variation |
|-----------|-------------------|------------------------|-----------|
| Données prix AXA | Manquantes | **Manquantes** | — |
| Ticker KO / total | 4 / 29 | 4 / 29 (AXA, AST, QTBS, ASTSPACE) | Stable |
| Earnings J0 FMP | 2026-06-23 (sans détails) | **2026-06-29** (sans détails) | Glissement |
| XLF rang | 3e / 11 | **4e / 11** | −1 rang |
| XLF momentum | 6.23 / 10 | **8.40 / 10** | **+2.17 pt** |
| XLF RS 20j | +4.96 % | **+8.00 %** | **+3.04 pp** |
| XLF RS 60j | −4.36 % | **−3.50 %** | **+0.86 pp** |
| XLF return 20j | +4.10 % | **+4.85 %** | **+0.75 pp** |
| XLF return 60j | — | **+8.89 %** | — |
| Signal macro | UNKNOWN | **UNKNOWN** | Stable |
| Score Global AXA | 55.2 / 100 | **55.2 / 100** | Stable |
| Score Opportunité | 5.5 / 10 | **5.5 / 10** | Stable |
| Recommandation | ATTENDRE | **ATTENDRE** | Stable |
| Timing | Neutre | **Neutre** | Stable |

---

## 2. Mise à jour technique

**[DONNÉES MANQUANTES]** — Le ticker "AXA" retourne toujours `"error": true, "reason": "No price history"` dans `data/latest.json` (ligne 1849). Aucun cours, RSI, ATR, MM50/200 ni volume n'est disponible. C'est le **30e snapshot consécutif** sans mutation technique.

**Contexte sectoriel (XLF — Financials) :** Amélioration organique nette sur toutes les métriques :
- **Momentum** : 8.40/10 (+2.17 pt vs 23/06 17h, +3.95 pt vs 23/06 13h) — niveau le plus élevé observé depuis le début du suivi sectoriel mi-mai.
- **RS 20j** : +8.00% (+3.04 pp) — accélération de la rotation vers les Financials.
- **RS 60j** : −3.50% (+0.86 pp) — creusement atténué sur le moyen terme.
- **Return 20j** : +4.85% (+0.75 pp).
- **Return 60j** : +8.89%.

Le rang 4e/11 (vs 3e/11) est interprété comme une descente **mécanique** (XLK et XLV ont plus fortement surperformé SPY), pas comme une dégradation sous-jacente. Les métriques de momentum et de force relative confirment une dynamique **nettement plus positive** pour le secteur Financials.

---

## 3. Mise à jour fondamentale

Aucune nouvelle donnée fondamentale pour AXA. Le symbole n'est toujours pas reconnu par yfinance (instrument coté Euronext Paris, non-US). FMP ne fournit pas de consensus ni de ratios pour ce ticker.

---

## 4. Mise à jour sentiment / options / news

### Agent Sentiment
- **Social sentiment** (`data/social_sentiment_latest.json`) : mention_count = 0, sentiment_score = 0.0/10, pas de pump detecté.
- **News / upgrades-downgrades** : aucun signal détecté dans les rapports agents.

### Agent Event-Driven
- `data/events_latest.json` (2026-06-29) : **0 événement** détecté pour AXA.

### Agent Watchman
- **Earnings J0** (2026-06-29, source fmp) signalé dans `upcoming_events_latest.json` mais sans estimate EPS/Revenue — **pattern persistant** depuis mi-mai (30e occurrence consécutive de earnings FMP glissant sans détails exploitables).

### Agent FX Exposure
- Exposition FX : 25% (default), fx_impact_score = 0.0, direction_label = neutral. Aucun impact.

---

## 5. Scoring global

| Axe | Score | Commentaire |
|-----|-------|-------------|
| Catalyseur | 6.5 / 10 | Stable — absence de catalyseur spécifique à AXA, mais vent arrière sectoriel renforcé |
| Valorisation | 5.0 / 10 | Stable — sans données fondamentales, score par défaut |
| Momentum | 5.0 / 10 | Stable — sans données techniques, score par défaut |
| **Score Opportunité** | **5.5 / 10** | **(C×35% + V×40% + M×25%)** |
| **Score Global** | **55.2 / 100** | **Stable** |
| **Recommandation** | **ATTENDRE** | **Timing Neutre** |

**Règles de disqualification** : aucune (aucun score ≤ 2/10).

---

## 6. Révision des niveaux SL / TP

**Inchangés** — Aucun prix de clôture disponible pour AXA. Les niveaux SL/TP ne peuvent pas être recalculés sans cours et ATR.

| Niveau | Valeur |
|--------|--------|
| Prix actuel | [DONNÉES MANQUANTES] |
| Stop-loss | [DONNÉES MANQUANTES] |
| Take-profit | [DONNÉES MANQUANTES] |
| Ratio R/R | [DONNÉES MANQUANTES] |

---

## 7. Conclusion — Thèse

**La thèse est inchangée.**

AXA reste sans données de prix exploitables dans le pipeline Argus-IA (30e snapshot consécutif). La recommandation **ATTENDRE** (Score Global 55.2/100) est maintenue par défaut.

**Seul élément nouveau :** le vent arrière sectoriel XLF s'est **nettement renforcé** (momentum 8.4/10, RS 20j +8.00%). Si le ticker était correctement sourcé (ex: `CS.PA` ou `AXAHY`), ce contexte sectoriel constituerait un argument technique haussier. En l'état, il ne modifie pas la recommandation faute de données propres.

**Action prioritaire :** corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`), mettre à jour le secteur (Financials / Insurance) et relancer le fetch pour disposer enfin de données techniques et fondamentales exploitables.

---

*Format institutionnel — Données source : `data/latest.json`, `data/sector_rotation_latest.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`.*
