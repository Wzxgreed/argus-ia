# AXA — Mise à jour quotidienne

> **Date :** 2026-05-25 (snapshot 13h00 UTC)
> **Type :** Mise à jour post-earnings (J0 selon FMP)
> **Statut :** 🔴 DONNÉES MANQUANTES — ticker à corriger (`CS.PA` ou `AXAHY`)

---

## Résumé des changements depuis l'analyse précédente (2026-05-25 10h00 UTC)

| Indicateur | 10h00 UTC | 13h00 UTC | Changement |
|-----------|-----------|-----------|------------|
| **Données prix** | Indisponible | Indisponible | **Stable** |
| **RSI 14j** | — | — | — |
| **ATR 14j** | — | — | — |
| **Volume relatif** | — | — | — |
| **XLF return 20j** | +1.01% | +1.01% | **Stable** |
| **XLF RS 20j vs SPY** | −3.43% | −3.43% | **Stable** |
| **XLF momentum score** | 0.0/10 | 0.0/10 | **Stable** |
| **Score Global** | 55.2/100 | 55.2/100 | **Stable (placeholder)** |
| **Recommandation** | ATTENDRE | ATTENDRE | **Stable** |

**Verdict :** 10e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale est impossible. Les métriques sectorielles XLF sont inchangées entre 10h00 et 13h00 UTC (return 20j +1.01%, RS 20j −3.43%, momentum 0.0/10). L'earnings signalé J0 par FMP (2026-05-25) n'a toujours pas de détails exploitables (EPS/Revenue manquants).

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 13h00 UTC).

**Contexte sectoriel (XLF) :**
- Return 20j : +1.01% (vs SPY +4.44%)
- Return 60j : −0.56% (vs SPY +8.47%)
- RS 20j vs SPY : −3.43% (stable vs 10h00)
- RS 60j vs SPY : −9.03% (stable vs 10h00)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 5e/11 (ni top 3 ni bottom 3)

**Interprétation :** Le secteur financier est stable entre les deux snapshots du jour. Sans données AXA, on ne peut évaluer si le titre sur/sous-performe son secteur. Le headwind sectoriel persiste : SPY surperforme XLF de +3.4pp sur 20j.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-05-25) :**
- Source FMP signale un earnings à J0 mais sans estimates EPS/Revenue (`"details": "Earnings "`, `"severity": "high"`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

**Sentiment Retail :** Aucune mention Reddit (0 posts, 0 sentiment) — AXA n'est pas discuté sur les forums US.

**Options :** Aucune donnée options (max pain, put/call ratio, OI) disponible pour AXA.

**News / Upgrades-Downgrades :** Aucun événement corporate détecté dans `data/events_latest.json` (total_events: 0). Aucun upgrade/downgrade massif signalé dans `data/upcoming_events_latest.json`.

**Géopolitique :** AXA non cartographié dans `data/geo_risk_latest.json` (date 2026-05-17).

**FX Exposure :** `data/fx_exposure_latest.json` liste AXA avec exposition 25% (placeholder), FX impact score 0.0, direction neutral. Pas d'anomalie détectée. Données stables vs 10h00.

---

## Scoring global

| Axe | Score | Commentaire |
|-----|-------|-------------|
| **Catalyseur** | 6.5/10 | Placeholder — aucun catalyseur identifié faute de données |
| **Valorisation** | 5.0/10 | Placeholder — aucun multiple disponible |
| **Momentum** | 5.0/10 | Placeholder — aucun cours disponible |
| **Score Opportunité** | 5.5/10 | = (6.5×35%) + (5.0×40%) + (5.0×25%) |
| **Malus / Bonus** | 0 | Aucun malus/bonus applicable (pas de données) |
| **Score Global** | **55.2/100** | **ATTENDRE** — non opérationnel |

**Rappel :** Ce score est un placeholder algorithmique. Il ne reflète pas une analyse réelle et ne doit pas servir de base à une décision d'investissement tant que les données prix ne sont pas disponibles.

---

## Niveaux SL / TP

**Impossibles à calculer** — aucun cours de clôture ni ATR 14j disponible.

---

## Conclusion

### 🎯 Thèse : ATTENDRE (données manquantes)

**La thèse est inchangée depuis le snapshot 10h00 UTC et depuis le 2026-05-20.**

1. **Données :** Le ticker "AXA" reste non résolu par yfinance. Aucun progrès sur la résolution du fetch après 10 snapshots consécutifs.
2. **Secteur :** XLF stable entre 10h00 et 13h00 (return 20j +1.01%, RS 20j −3.43%, momentum 0.0/10). Le secteur financier reste en sous-performance relative vs SPY. Si les données AXA étaient disponibles, ce headwind sectoriel atténué serait légèrement moins pénalisant pour le score Momentum qu'en mi-mai, mais reste un facteur négatif.
3. **Earnings :** J0 signalé par FMP (2026-05-25) sans détails. L'événement n'est pas exploitable.

**Action immédiate recommandée :**
- Corriger le symbole dans `config/watchlist.json` (`CS.PA` pour Euronext Paris ou `AXAHY` pour ADR US)
- Relancer `scripts/fetch_prices.py --tickers [SYMBOLE_CORRIGÉ]`
- Si correction effectuée : générer un `_init.md` complet avec Market Researcher + Filtre Qualité 6 critères

---

*Document généré par Argus-IA — Données : `data/latest.json` (2026-05-25T13:00 UTC).*
