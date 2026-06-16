# AXA — Mise à jour Quotidienne (snapshot 10h00 UTC)

> **Date :** 2026-06-16
> **Snapshot :** 2026-06-16T10:00:01 UTC
> **Type :** `_update.md`
> **Analyste :** Desk Argus-IA
> **Réf. précédente :** `AXA_2026-06-15_update_21h.md` (snapshot 21h00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Élément | État 15/06 21h | État 16/06 10h | Changement |
|---------|---------------|----------------|------------|
| Cours AXA | `[DONNÉES MANQUANTES]` | `[DONNÉES MANQUANTES]` | **Stable — blocage structurel** |
| Erreur Yahoo | `No price history` | `No price history` | **Confirmé stable (16e snapshot consécutif)** |
| Tickers KO pipeline | 4 / 29 | 4 / 29 | **Stable (AXA, AST, QTBS, ASTSPACE)** |
| Score Opportunité | 5.5/10 (C:6.5 V:5.0 M:5.0) | **5.5/10** (C:6.5 V:5.0 M:5.0) | **Stable (placeholder)** |
| Score Global | 55.2/100 | **55.2/100** | **Stable** |
| Recommandation | ATTENDRE | **ATTENDRE** | **Confirmée** |
| Timing | Neutre | **Neutre** | **Stable** |
| Anomalie JSON sectoriel | Mutation mécanique XLF (rangs 2e/11) | **Anomalie JSON récurrente** (NaN + momentum 10.0 uniforme) | 🔴 **Dégradation fichier sectoriel** |
| Earnings FMP | J0 (2026-06-15) sans détails | **J0 (2026-06-16) sans détails** | **Glissement d'un jour** |

**Verdict :** Données AXA toujours indisponibles. **Anomalie JSON sectorielle de retour** dans `data/sector_rotation_2026-06-16.json` (NaN + momentum 10.0 uniforme pour tous les secteurs) — déjà observée le 10/06. Le dernier contexte sectoriel fiable reste le snapshot 21h du 15/06. L'earnings J0 glissant a reculé d'une journée (15→16) sans résolution.

---

## Mise à jour technique

**[DONNÉES MANQUANTES]** Aucun cours, volume, RSI, ATR ou moyenne mobile disponible pour AXA dans `data/latest.json` (snapshot 2026-06-16T10:00:01 UTC). `AXA` est listé dans `tickers_ko` avec raison `"No price history"`.

**Contexte sectoriel XLF — anomalie JSON détectée :**
- Le fichier `data/sector_rotation_2026-06-16.json` présente une **anomalie structurelle récurrente** : `return_20d`, `return_60d`, `rs_20d`, `rs_60d` = `NaN` pour 10 secteurs sur 11, `momentum_score` = **10.0 uniforme** pour tous les secteurs, et `regime` = `UNKNOWN`.
- Cette anomalie a déjà été observée le 2026-06-10 et classée comme faux positif technique (données sectorielles corrompues ou placeholders).
- **Dernier contexte sectoriel fiable :** snapshot 2026-06-15 21h00 UTC : XLF rang **2e/11**, momentum **4.69/10**, RS 20j **+2.70%**, RS 60j **−4.82%**, signal macro `UNKNOWN`.
- **Interprétation :** l'amélioration du rang 2e/11 au 15/06 était mécanique (dégradation relative d'autres secteurs), pas organique. Le momentum propre de XLF avait baissé de 5.12 à 4.69 (−0.43 pt) entre 17h et 21h. En l'absence de données propres à AXA, ce contexte sectoriel reste le seul élément observable.

**Conséquence pour l'analyse :** aucune donnée technique propre à AXA. Le scoring momentum reste un placeholder de 5.0/10.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES]** Aucune donnée fondamentale (P/E, EPS, consensus analystes, marges, dette) disponible pour AXA dans `data/latest.json`.

**Earnings J0 glissant (2026-06-16) :**
- Source FMP signale un earnings à J0 (`"date": "2026-06-16"`, `"days_until": 0`) mais sans estimates EPS/Revenue (`"details": "Earnings "`).
- Aucune variance table, aucun transcript NLP, aucune guidance détectée.
- Le preview `AXA_2026-06-16_preview.md` est un template vierge (généré automatiquement ce matin).
- **Impact sur la thèse :** impossible à évaluer. **16e occurrence consécutive** sans résolution. Le J0 glissant a simplement reculé d'une journée.

**Accounting Risk :** Fichier `data/accounting_risk_latest.json` **absent** — aucun M-Score, Z-Score, F-Score ou Sloan Ratio disponible.

---

## Mise à jour sentiment / options / news

| Signal | État | Détail |
|--------|------|--------|
| News du jour (`news_2026-06-16.json`) | **Aucune** | AXA non listé ou vide — 0 article |
| Sentiment retail (Reddit) | **No data** | 0 mentions, score 0/10 (`social_sentiment_2026-06-16.json`) |
| Pump / dump detection | 🟢 Aucun | `pump_detected: false` |
| Événements corporate | 🟢 Aucun | `events_2026-06-16.json` → 0 événement AXA |
| Options (max pain, GEX, IV Rank) | **[DONNÉES MANQUANTES]** | Non récupérées |
| Upgrades / downgrades | **[DONNÉES MANQUANTES]** | Non récupérés |

**FX Exposure** (`fx_exposure_2026-06-16.json`) :
- Exposition FX : **25%** (export, primary currency USD — classification générique par défaut)
- FX Impact Score : **0.0/10** — direction neutre
- DXY change : 0% → pas de headwind/tailwind identifié
- Divergence cours / modèle FX : aligned
- Flag : 🟢 — stable

**Géopolitique** (`geo_risk_2026-05-17.json` — dernier fichier disponible) :
- AXA non listé dans le rapport géopolitique.
- Aucun événement géopolitique spécifique détecté.
- Flag : 🟢 — stable

**Social Sentiment** (`social_sentiment_2026-06-16.json`) :
- AXA mention count : 0
- Sentiment score : 0.0/10
- Label : "No data"
- Pas de mention spike, pas de pump détecté.

---

## Scoring global (agents)

| Score | Valeur | Évolution vs snapshot 15/06 21h |
|-------|--------|---------------------------------|
| Score Opportunité | **5.5/10** | Stable |
| — Catalyseur | 6.5/10 | Stable |
| — Valorisation | 5.0/10 | Stable |
| — Momentum | 5.0/10 | Stable (placeholder) |
| Score Global | **55.2/100** | Stable |
| Recommandation | **ATTENDRE** | Confirmée |
| Timing | **Neutre** | Stable |

**Pondération régime macro :** Inconnue (`regime_macro: Unknown`) — poids par défaut C:35% V:40% M:25% appliqués.

**Note sectorielle :** L'anomalie JSON `data/sector_rotation_2026-06-16.json` (NaN + momentum 10.0 uniforme) rend le contexte sectoriel du jour **inexploitable**. Le dernier snapshot fiable reste le 15/06 21h (XLF rang 2e/11, momentum 4.69/10, RS 20j +2.70%) avec la mise en garde que ce rang était mécanique (dégradation relative d'autres secteurs), pas organique.

---

## Révision des niveaux SL / TP

**[IMPOSSIBLE]** Aucun cours ni ATR disponible. Les niveaux de stop-loss et take-profit ne peuvent pas être calculés.

- **Prix actuel :** `[DONNÉES MANQUANTES]`
- **Stop-loss suggéré :** `[DONNÉES MANQUANTES]`
- **Take-profit suggéré :** `[DONNÉES MANQUANTES]`
- **Ratio R/R :** `[DONNÉES MANQUANTES]`

---

## Conclusion

### 🟡 Thèse ATTENDRE confirmée — DONNÉES AXA TOUJOURS MANQUANTES, ANOMALIE SECTORIELLE RÉCURRENT

**La thèse n'a pas changé.** AXA reste l'un des 4 tickers structurellement KO sur 29 (AXA, AST, QTBS, ASTSPACE), avec un blocage de sourcing persistant. Le symbole "AXA" n'est pas reconnu par yfinance (instrument Euronext Paris, non coté US).

**Anomalie JSON sectorielle de retour.** Le fichier `data/sector_rotation_2026-06-16.json` présente la même anomalie technique que le 10/06 (NaN + momentum 10.0 uniforme pour tous les secteurs). Ce fichier est classé comme inexploitable. Le dernier contexte sectoriel fiable reste le snapshot 21h du 15/06 (XLF rang 2e/11 mécanique, momentum 4.69/10).

**Earnings J0 glissant :** FMP signale un earnings à J0 (2026-06-16) mais sans estimates ni détails — **16e occurrence consécutive** sans résolution. Le J0 a simplement glissé d'une journée (15→16).

**Action immédiate :**
1. Corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`) et mettre à jour le secteur (Financials / Insurance).
2. Relancer le fetch (`make pipeline` ou `./scripts/analyse_ticker.sh AXA`) pour obtenir des données exploitables.
3. Jusqu'à résolution, AXA reste en **ATTENDRE** avec un score placeholder de 55.2/100.

---

*Desk Argus-IA — Snapshot 2026-06-16T10:00:01 UTC*
