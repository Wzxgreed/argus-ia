# AXA — Mise à jour Quotidienne (Snapshot 17h00 UTC)

> **Date :** 2026-05-27
> **Snapshot :** 2026-05-27T17:00:02 UTC
> **Type :** `_update.md` (post-pipeline matin)
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-05-27_update.md` (snapshot 13h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 2026-05-27 13h00 | État 2026-05-27 17h00 | Changement |
|---------|----------------------|----------------------|------------|
| Cours | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| RSI 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| ATR 14j | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Volume | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable** |
| Tickers KO pipeline | 3 / 26 | **3 / 26** | Stable (AXA, AST, QTBS) |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| XLF return 20j | +0.08% | **−0.96%** | 🔴 **Dégradation −1.04pp** |
| XLF return 60j | +1.33% | **+0.61%** | 🔴 **Dégradation −0.72pp** |
| XLF RS 20j vs SPY | −4.88% | **−6.33%** | 🔴 **Dégradation −1.45pp** |
| XLF RS 60j vs SPY | −8.38% | **−8.93%** | 🔴 **Dégradation −0.55pp** |
| XLF momentum score | 0.0/10 | **0.0/10** | Stable |
| Earnings FMP | J0 (2026-05-27) | **J0 (2026-05-27)** | Date calendrier glissante, toujours sans détails |

**Verdict :** 18e snapshot consécutif sans mutation des données AXA. Le symbole "AXA" reste non reconnu par yfinance (instrument non coté US). **Mutation sectorielle XLF détectée** entre 13h00 et 17h00 UTC : dégradation relative et absolue du secteur Financials en séance, avec le return 20j basculant en territoire négatif (−0.96%) et le RS 20j vs SPY creusant à −6.33% (vs −4.88% à 13h00). C'est la première mutation sectorielle observée depuis le snapshot 17h00 UTC du 26/05.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-05-27T17:00:02 UTC).

**Contexte sectoriel (XLF) — mutation détectée vs snapshot 13h00 UTC :**
- Return 20j : −0.96% (vs SPY +5.36%)
- Return 60j : +0.61% (vs SPY +9.54%)
- RS 20j vs SPY : −6.33% (dégradation de 1.45pp vs 13h00)
- RS 60j vs SPY : −8.93% (dégradation de 0.55pp vs 13h00)
- Momentum score : 0.0/10 (stable)
- Rang sectoriel : 5e/11 (hors top 3 et bottom 3)

**Interprétation :** Le secteur financier a subi une dégradation technique en séance US entre 13h00 et 17h00 UTC, après une stabilité totale entre 10h00 et 13h00. Le return 20j est repassé en négatif (−0.96%) et le sous-performance relative vs SPY s'est accentuée (−6.33% sur 20j, −8.93% sur 60j). Cette mutation est cohérente avec la rotation sectorielle observée depuis plusieurs jours au profit de la Tech (XLK return 20j +16.45%, momentum 10.0/10). Sans données AXA, on ne peut évaluer si le titre sur/sous-performe son secteur, mais le headwind sectoriel s'est renforcé en fin de séance. Si les données AXA étaient disponibles, ce détérioration sectoriel pourrait justifier un ajustement à la marge du score Momentum (actuellement 5.0/10 par défaut).

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 (2026-05-27) :**
- Source FMP signale un earnings à J0 mais sans estimates EPS/Revenue (`"details": "Earnings "`, `"severity": "high"`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- **Impact sur la thèse :** impossible à évaluer sans données.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-05-27.json`) | **Aucune** | `AXA: []` — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-05-27.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-05-27.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-05-27.json`) :
- Exposition FX : **25%** (export, primary currency USD)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned

**Géopolitique** (`geo_risk_latest.json`) :
- Aucun événement géopolitique spécifique à AXA détecté.
- Score politique global : 2/10 (🟢 bas), non exposé.

**Social Sentiment** (`social_sentiment_2026-05-27.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot précédent |
|-------|--------|--------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | Neutre | Stable |

**Pondération appliquée :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime macro inconnu → poids par défaut).

> **Règle de disqualification :** aucun score individuel ≤ 2/10 → le ticker n'est pas exclu du rapport, mais le manque de données empêche tout positionnement.

> **Note sur la significativité :** `quant_report_latest.json` indique 0 signaux historiques avec verdict, p-value = 1.0 → `[SIGNAUX NON SIGNIFICATIFS]`. Le score 55.2/100 est un placeholder algorithmique basé sur des valeurs par défaut (RSI 50, scores moyens) et ne constitue pas une recommandation investissable.

---

## Niveaux suggérés

**[NON CALCULABLES — MANQUE DE DONNÉES]**

- Prix actuel : `null`
- Prix d'entrée suggéré : `null`
- Stop-loss : `null`
- Take-profit : `null`
- Ratio R/R : `null`

Sans cours ni ATR, aucun niveau technique ne peut être établi de manière fiable.

---

## Conclusion — Thèse

| Verdict | Statut |
|---------|--------|
| **Thèse initiale** | Aucune — pas d'`_init.md` préalable |
| **Évolution** | **Non évaluable** (données de prix absentes + mutation sectorielle XLF en séance entre 13h00 et 17h00 UTC) |
| **Action recommandée** | **ATTENDRE** — résoudre le sourcing des données avant toute analyse technique ou fondamentale |

**Synthèse desk :**
1. **Problème de symbole persistant :** "AXA" n'est pas un ticker Yahoo Finance US valide. Le pipeline doit être configuré avec `CS.PA` (Euronext Paris) ou `AXAHY` (ADR US) pour obtenir des données de cours, RSI, volumes et fondamentaux. `config/watchlist.json` liste toujours AXA avec exchange "NASDAQ" et secteur "Non spécifié" — cette configuration est incorrecte.
2. **Mutation sectorielle en séance :** Après une stabilité totale entre 10h00 et 13h00 UTC, le secteur Financials (XLF) s'est dégradé entre 13h00 et 17h00 UTC : return 20j +0.08% → −0.96%, RS 20j vs SPY −4.88% → −6.33%, RS 60j vs SPY −8.38% → −8.93%. C'est la première mutation sectorielle observée depuis le snapshot 17h00 UTC du 26/05. Le secteur Financials reste en phase de distribution relative vs le marché, sous le coup de la rotation sectorielle vers la Tech (XLK return 20j +16.45%, momentum 10.0/10).
3. **Earnings J0 non résolu :** L'événement earnings du 2026-05-27 est répertorié dans le calendrier FMP mais sans données de consensus ni résultats. L'impact sur le cours ne peut être mesuré. C'est le 5e jour consécutif où le calendrier FMP glisse la date J0 sans fournir de détails exploitables.
4. **Marché actif en séance :** Le snapshot 17h00 UTC confirme que les données de prix US (VRT 3.1M, IREN 46.0M, NOK 90.9M) sont bien récupérées, isolant AXA comme l'un des 3 tickers structurellement KO sur 26.
5. **Qualité des données :** AXA fait toujours partie des 3 tickers KO sur 26. Tout scoring est non fiable.
6. **Next steps (inchangés) :**
   - Corriger `config/watchlist.json` pour utiliser `CS.PA` ou `AXAHY`
   - Mettre à jour le secteur (Financials / Insurance)
   - Relancer `scripts/fetch_prices.py` pour ce ticker
   - Compléter `AXA_YYYY-MM-DD_init.md` dès que les données seront disponibles

---

*Rapport généré automatiquement par le desk Argus-IA. Données sources : `data/latest.json` (fetched_at 2026-05-27T17:00:02 UTC), `data/recommandations_2026-05-27.json`, `data/fx_exposure_2026-05-27.json`, `data/upcoming_events_2026-05-27.json`, `data/social_sentiment_2026-05-27.json`, `data/events_2026-05-27.json`, `data/sector_rotation_2026-05-27.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`.*
