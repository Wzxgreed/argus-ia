# AXA — Mise à jour Quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-22
> **Snapshot :** 2026-06-22T10:00:01 UTC
> **Type :** `_update.md`
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-17_update.md` (snapshot 10h00 UTC, dernière update produite)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 17/06 10h | État 22/06 10h | Changement |
|---------|---------------|----------------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable — blocage structurel** |
| Erreur Yahoo | `No price history` | `No price history` | **Confirmé stable (24e snapshot consécutif)** |
| Tickers KO pipeline | 4 / 29 | 4 / 29 | **Stable (AXA, AST, QTBS, ASTSPACE)** |
| Fichier sectoriel JSON | Exploitable (11/11 secteurs OK) | **Exploitable (11/11 secteurs OK)** | **Stable** |
| XLF rang | 4e/11 | **3e/11** | **+1 place (mécanique, pas organique)** |
| XLF momentum | 5.32/10 | **4.25/10** | **−1.07 pt** |
| XLF RS 20j | +3.46% | **+2.70%** | **−0.76 pp** |
| XLF RS 60j | −4.38% | **−5.91%** | **−1.53 pp** |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable (placeholder)** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| Earnings FMP | J0 (2026-06-17) sans détails | **J0 (2026-06-22) sans détails** | **Glisse de 5 jours — 24e occurrence consécutive** |
| Dernier `_update.md` | 2026-06-17 | **2026-06-22** | **5 jours sans update intermédiaire** |

**Verdict :** Données AXA toujours indisponibles. **Contexte sectoriel XLF mixte** : rang mécaniquement amélioré (3e/11 vs 4e/11) car d'autres secteurs ont sous-performé davantage, mais momentum et forces relatives se dégradent (momentum −1.07 pt, RS 20j −0.76 pp, RS 60j −1.53 pp). Aucune anomalie JSON détectée. L'earnings J0 FMP reste sans estimates ni détails exploitables — **24e occurrence consécutive** sans résolution.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-22T10:00:01 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel XLF — dégradation sous-jacente masquée par le rang :**
- Le fichier `data/sector_rotation_2026-06-22.json` (snapshot 10h) est **exploitable** (11/11 secteurs valides, aucune anomalie NaN).
- **XLF (Financials) :** rang **3e/11** (vs 4e/11 le 17/06), momentum **4.25/10** (vs 5.32/10), RS 20j **+2.70%** (vs +3.46%), RS 60j **−5.91%** (vs −4.38%).
- **Dégradation réelle du momentum :** bien que le rang remonte d'une place, c'est un effet mécanique dû à la sous-performance relative d'autres secteurs (XLB, XLY). Le momentum propre de XLF recule de −1.07 pt, la force relative 20j se dégrade de −0.76 pp et la force relative 60j se creuse de −1.53 pp.
- **Régime macro :** reste `UNKNOWN` (stable depuis le 02/06).
- **Top3 sectors :** XLK (10.0/10), XLI (6.25/10), XLF (4.25/10). Financials réintègre le top 3 par défaut, pas par force.
- **Bottom3 sectors :** XLE (0.0/10), XLU (0.0/10), XLP (0.0/10). XLC également à 0.0/10.

**Conséquence pour l'analyse :** aucune donnée technique propre à AXA. Le scoring momentum reste un placeholder de 5.0/10. Le contexte sectoriel affiche une dégradation sous-jacente (momentum et RS en baisse) qui constitue un vent de face théorique marginalement négatif pour AXA.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-22) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-22"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- Le preview `AXA_2026-06-22_preview.md` reste un template vierge (généré automatiquement ce matin).
- **Impact sur la thèse :** impossible à évaluer. **24e occurrence consécutive** sans résolution.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` **absent** — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-22.json`) | **Aucune** | AXA non listé ou vide — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-22.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-22.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérées |

**FX Exposure** (`fx_exposure_2026-06-22.json`) :
- Exposition FX : **25%** (export, primary currency USD — classification générique par défaut)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢 — stable

**Géopolitique** (`geo_risk_2026-05-17.json` — dernier fichier disponible) :
- AXA non listé dans le rapport géopolitique.
- Aucun événement géopolitique spécifique détecté.
- Flag : 🟢 — stable

**Social Sentiment** (`social_sentiment_2026-06-22.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.
- Alerte automatique `EXTREME_BEARISH` générée par le script (artefact dû à l'absence de données, pas un signal réel).

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 17/06 10h |
|-------|--------|---------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** Le fichier `data/sector_rotation_2026-06-22.json` est exploitable ce matin sans anomalie. Cependant, XLF (Financials) affiche une dégradation sous-jacente par rapport au 17/06 : momentum 4.25/10 (vs 5.32/10), RS 20j +2.70% (vs +3.46%), RS 60j −5.91% (vs −4.38%). Le rang remonte mécaniquement à 3e/11 (vs 4e/11) car XLB et XLY ont sous-performé davantage, mais ce n'est pas une amélioration organique du secteur. C'est un vent de face théorique marginalement négatif pour AXA, mais en l'absence de données propres, le scoring ne peut pas être révisé à la baisse.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🟡 Thèse ATTENDRE confirmée — DONNÉES AXA TOUJOURS MANQUANTES, CONTEXTE SECTORIEL XLF EN DÉGRADATION SOUS-JACENTE

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Contexte sectoriel dégradé sous-jacent.** Le fichier `data/sector_rotation_2026-06-22.json` est exploitable ce matin, mais XLF (Financials) affiche une dégradation nette par rapport au 17/06 : momentum **4.25/10** (vs 5.32/10), RS 20j **+2.70%** (vs +3.46%), RS 60j **−5.91%** (vs −4.38%). Le rang mécanique remonte à 3e/11 (vs 4e/11) par défaut d'autres secteurs, pas par force propre. C'est un vent de face théorique marginalement négatif pour un assureur, mais en l'absence de données propres, le scoring reste un placeholder.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-22) mais sans estimates ni détails — **24e occurrence consécutive** sans résolution.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-22T10:00:01 UTC*
