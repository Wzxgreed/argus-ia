# AXA — Mise a jour Quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-17
> **Snapshot :** 2026-06-17T10:00:01 UTC
> **Type :** `_update.md`
> **Analyste :** Desk Argus-IA
> **Ref. precedente :** `AXA_2026-06-16_update_17h.md` (snapshot 17h00 UTC)

---

## Resume des changements depuis l'analyse precedente

| Element | Etat 16/06 17h | Etat 17/06 10h | Changement |
|---------|---------------|----------------|------------|
| Cours AXA | `[DONNEES MANQUANTES]` | `[DONNEES MANQUANTES]` | **Stable — blocage structurel** |
| Erreur Yahoo | `No price history` | `No price history` | **Confirme stable (19e snapshot consecutif)** |
| Tickers KO pipeline | 4 / 29 | 4 / 29 | **Stable (AXA, AST, QTBS, ASTSPACE)** |
| Fichier sectoriel JSON | Exploitable (repare a 17h) | **Exploitable (11/11 secteurs OK)** | **Anomalie NaN absente ce matin** |
| XLF rang | 2e/11 | **4e/11** | **Degrade de 2 places** |
| XLF momentum | 6.68/10 | **5.32/10** | **-1.36 pt** |
| XLF RS 20j | +4.64% | **+3.46%** | **-1.18 pp** |
| XLF RS 60j | -2.76% | **-4.38%** | **-1.62 pp** |
| Score Opportunite | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable (placeholder)** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmee** |
| Timing | Neutre | **Neutre** | **Stable** |
| Earnings FMP | J0 (2026-06-16) sans details | **J0 (2026-06-17) sans details** | **Glisse d'un jour — 19e occurrence consecutive** |

**Verdict :** Donnees AXA toujours indisponibles. **Contexte sectoriel XLF legerement degrade** par rapport au close du 16/06 : rang 4e/11 (vs 2e/11), momentum 5.32/10 (vs 6.68/10), RS 20j +3.46% (vs +4.64%), RS 60j -4.38% (vs -2.76%). Aucune anomalie JSON detectee ce matin. L'earnings J0 FMP reste sans estimates ni details exploitables — **19e occurrence consecutive** sans resolution.

---

## Mise a jour technique

**[DONNEES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-17T10:00:01 UTC). `AXA` est liste dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel XLF — mutation negative par rapport au 16/06 :**
- Le fichier `data/sector_rotation_2026-06-17.json` (snapshot 10h) est **exploitable** (11/11 secteurs valides, aucune anomalie NaN).
- **XLF (Financials) :** rang **4e/11** (vs 2e/11 a 17h 16/06), momentum **5.32/10** (vs 6.68/10), RS 20j **+3.46%** (vs +4.64%), RS 60j **-4.38%** (vs -2.76%).
- **Degradation sectorielle nette :** le momentum XLF recule de -1.36 pt, la force relative 20j se degrade de -1.18 pp et la force relative 60j se creuse de -1.62 pp. XLF sort du top 3 pour la premiere fois depuis le 15/06 21h.
- **Regime macro :** reste `UNKNOWN` (stable depuis le 02/06).
- **Top3 sectors :** XLK (10.0/10), XLB (5.85/10), XLI (5.6/10). Financials n'est plus dans le top 3.
- **Bottom3 sectors :** XLU (0.0/10), XLP (0.0/10), XLC (0.0/10). XLE egalement a 0.0/10.

**Consequence pour l'analyse :** aucune donnee technique propre a AXA. Le scoring momentum reste un placeholder de 5.0/10. Le contexte sectoriel s'est legerement degrade par rapport au 16/06, ce qui constitue un vent de face theorique marginalement negatif pour AXA.

---

## Mise a jour fondamentale

**[DONNEES MANQUANTES]** Aucune donnee fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-17) :**
- Source FMP signale un earnings a J0 (`"date": "2026-06-17"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance detectee.
- Le preview `AXA_2026-06-17_preview.md` reste un template vierge (genere automatiquement ce matin).
- **Impact sur la these :** impossible a evaluer. **19e occurrence consecutive** sans resolution.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` **absent** — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise a jour sentiment / options / news

| Signal | Etat | Detail |
|--------|------|--------|
| News du jour (`news_2026-06-17.json`) | **Aucune** | AXA non liste ou vide — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-17.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Evenements corporate | 🟢 Aucun | `events_2026-06-17.json` → 0 evenement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNEES MANQUANTES]** | Non recuperees |
| Upgrades / downgrades | **[DONNEES MANQUANTES]** | Non recuperees |

**FX Exposure** (`fx_exposure_2026-06-17.json`) :
- Exposition FX : **25%** (export, primary currency USD — classification generique par defaut)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifie
- Divergence cours / modele FX : aligned
- Flag : 🟢 — stable

**Geopolitique** (`geo_risk_2026-05-17.json` — dernier fichier disponible) :
- AXA non liste dans le rapport geopolitique.
- Aucun evenement geopolitique specifique detecte.
- Flag : 🟢 — stable

**Social Sentiment** (`social_sentiment_2026-06-17.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump detecte.
- Alerte automatique `EXTREME_BEARISH` generee par le script (artefact due a l'absence de donnees, pas un signal reel).

---

## Scoring global (agents)

| Score | Valeur | Evolution vs snapshot 16/06 17h |
|-------|--------|-----------------------------------|
| Score Opportunite | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmee |
| Timing | **Neutre** | Stable |

**Ponderation regime macro :** Inconnue (`regime_macro: Unknown`) — poids par defaut C:35% V:40% M:25% appliques.

**Note sectorielle :** Le fichier `data/sector_rotation_2026-06-17.json` est exploitable ce matin sans anomalie. Cependant, XLF (Financials) affiche une degradation par rapport au 16/06 17h : rang 4e/11 (vs 2e/11), momentum 5.32/10 (vs 6.68/10), RS 20j +3.46% (vs +4.64%), RS 60j -4.38% (vs -2.76%). Le secteur Financials n'est plus dans le top 3. C'est un vent de face theorique marginalement negatif pour AXA, mais en l'absence de donnees propres, le scoring ne peut pas etre revise a la baisse.

---

## Revision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas etre calcules.

- **Prix actuel :** `[DONNEES MANQUANTES]`
- **Stop-loss suggere :** `[DONNEES MANQUANTES]`
- **Take-profit suggere :** `[DONNEES MANQUANTES]`
- **Ratio R/R :** `[DONNEES MANQUANTES]`

---

## Conclusion

### 🟡 These ATTENDRE confirmee — DONNEES AXA TOUJOURS MANQUANTES, CONTEXTE SECTORIEL XL F LEGEREMENT DEGRADE

**La these n'a pas change.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non cote US).

**Contexte sectoriel degrade.** Le fichier `data/sector_rotation_2026-06-17.json` est exploitable ce matin, mais XLF (Financials) affiche une degradation nette par rapport au 16/06 : rang **4e/11** (vs 2e/11), momentum **5.32/10** (vs 6.68/10), RS 20j **+3.46%** (vs +4.64%), RS 60j **-4.38%** (vs -2.76%). Le secteur Financials sort du top 3 pour la premiere fois depuis le 15/06 21h. C'est un vent de face theorique marginalement negatif pour un assureur, mais en l'absence de donnees propres, le scoring reste un placeholder.

**Earnings J0 glissant :** FMP signale un earnings a J0 (2026-06-17) mais sans estimates ni details — **19e occurrence consecutive** sans resolution.

**Action immediate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre a jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des donnees exploitables.
3. Jusqu'a resolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-17T10:00:01 UTC*
