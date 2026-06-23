# AXA — Mise à jour Quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-23
> **Snapshot :** 2026-06-23T10:00:01 UTC
> **Type :** `_update.md`
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-22_update_21h.md` (snapshot 21h00 UTC, dernière update produite)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 22/06 21h | État 23/06 10h | Changement |
|---------|---------------|----------------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable — blocage structurel** |
| Erreur Yahoo | `No price history` | `No price history` | **Confirmé stable (25e snapshot consécutif)** |
| Tickers KO pipeline | 4 / 29 | 4 / 29 | **Stable (AXA, AST, QTBS, ASTSPACE)** |
| Fichier sectoriel JSON | Exploitable (11/11 secteurs OK) | **Exploitable (11/11 secteurs OK)** | **Stable** |
| XLF rang | 3e/11 | **3e/11** | **Stable** |
| XLF momentum | 5.08/10 | **5.45/10** | **+0.37 pt** |
| XLF RS 20j | +3.33% | **+3.69%** | **+0.36 pp** |
| XLF RS 60j | −4.79% | **−4.41%** | **+0.38 pp** |
| XLF return 20j | +3.81% | **+4.17%** | **+0.36 pp** |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable (placeholder)** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| Earnings FMP | J0 (2026-06-22) sans détails | **J0 (2026-06-23) sans détails** | **Glisse de 1 jour — 28e occurrence consécutive** |
| Dernier `_update.md` | 2026-06-22 21h | **2026-06-23 10h** | **Nouveau snapshot** |

**Verdict :** Données AXA toujours indisponibles. **Contexte sectoriel XLF en amélioration organique** : momentum +0.37 pt, RS 20j +0.36 pp, RS 60j +0.38 pp. Le secteur Financials confirme sa place dans le top 3 (rang 3e/11) avec une dynamique positive ce matin. Aucune anomalie JSON détectée. L'earnings J0 FMP reste sans estimates ni détails exploitables — **28e occurrence consécutive** sans résolution.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-23T10:00:01 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel XLF — amélioration organique confirmée :**
- Le fichier `data/sector_rotation_2026-06-23.json` (snapshot 10h) est **exploitable** (11/11 secteurs valides, aucune anomalie NaN).
- **XLF (Financials) :** rang **3e/11** (stable vs 21h), momentum **5.45/10** (vs 5.08/10), RS 20j **+3.69%** (vs +3.33%), RS 60j **−4.41%** (vs −4.79%), return 20j **+4.17%** (vs +3.81%).
- **Amélioration réelle du momentum :** les quatre métriques sectorielles affichent une amélioration simultanée ce matin. Le momentum progresse de +0.37 pt, la force relative 20j gagne +0.36 pp et la force relative 60j se redresse de +0.38 pp. Le return 20j progresse également de +0.36 pp. Cette amélioration est organique — pas un effet mécanique de sous-performance d'autres secteurs.
- **Régime macro :** reste `UNKNOWN` (stable depuis le 02/06).
- **Top3 sectors :** XLK (10.0/10), XLI (7.54/10), XLF (5.45/10). Financials confirme sa place dans le top 3 avec une dynamique positive.
- **Bottom3 sectors :** XLE (0.0/10), XLU (0.0/10), XLP (0.0/10). XLY et XLC également à 0.0/10.

**Conséquence pour l'analyse :** aucune donnée technique propre à AXA. Le scoring momentum reste un placeholder de 5.0/10. Le contexte sectoriel affiche une **amélioration organique nette** ce matin par rapport au close 22/06, qui constitue un vent arrière théorique marginalement positif pour AXA. En l'absence de données propres, le scoring ne peut pas être révisé à la hausse, mais le contexte sectoriel est désormais plus favorable qu'hier soir.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-23) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-23"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- Le preview `AXA_2026-06-23_preview.md` reste un template vierge (généré automatiquement ce matin).
- **Impact sur la thèse :** impossible à évaluer. **28e occurrence consécutive** sans résolution.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` **absent** — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-23.json`) | **Aucune** | AXA non listé ou vide — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-23.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-23.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérées |

**FX Exposure** (`fx_exposure_2026-06-23.json`) :
- Exposition FX : **25%** (classification générique par défaut — secteur "Non spécifié", primary_currency USD)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢 — stable
- **Note :** la classification FX pour AXA est un artefact de l'absence de données sectorielles propres. Pour un assureur français coté à Euronext Paris, l'exposition réelle est dominée en EUR, avec une sensibilité DXY/EUR inverse.

**Géopolitique** (`geo_risk_2026-05-17.json` — dernier fichier disponible) :
- AXA non listé dans le rapport géopolitique.
- Aucun événement géopolitique spécifique détecté.
- Flag : 🟢 — stable

**Social Sentiment** (`social_sentiment_2026-06-23.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.
- Alerte automatique `EXTREME_BEARISH` générée par le script (artefact dû à l'absence de données, pas un signal réel).

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 22/06 21h |
|-------|--------|---------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** Le fichier `data/sector_rotation_2026-06-23.json` est exploitable ce matin sans anomalie. XLF (Financials) affiche une **amélioration organique** par rapport au close 22/06 : momentum **5.45/10** (vs 5.08/10), RS 20j **+3.69%** (vs +3.33%), RS 60j **−4.41%** (vs −4.79%), return 20j **+4.17%** (vs +3.81%). Le rang reste stable à 3e/11. Cette amélioration sectorielle constitue un vent arrière théorique marginalement positif pour AXA, mais en l'absence de données propres, le scoring reste un placeholder.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🟡 Thèse ATTENDRE confirmée — DONNÉES AXA TOUJOURS MANQUANTES, CONTEXTE SECTORIEL XLF EN AMÉLIORATION ORGANIQUE

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Contexte sectoriel en amélioration organique.** Le fichier `data/sector_rotation_2026-06-23.json` est exploitable ce matin, et XLF (Financials) affiche une amélioration nette par rapport au close 22/06 : momentum **5.45/10** (vs 5.08/10), RS 20j **+3.69%** (vs +3.33%), RS 60j **−4.41%** (vs −4.79%), return 20j **+4.17%** (vs +3.81%). Le rang reste stable à 3e/11. Cette amélioration est organique (les quatre métriques progressent simultanément), pas mécanique. Elle constitue un vent arrière théorique marginalement positif pour un assureur, mais en l'absence de données propres à AXA, le scoring reste un placeholder.

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-23) mais sans estimates ni détails — **28e occurrence consécutive** sans résolution.

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-23T10:00:01 UTC*
