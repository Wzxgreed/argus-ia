# AXA — Index du Dossier

> **Dernière mise à jour :** 2026-06-17 (snapshot 13h UTC)
> **Statut :** 🟡 DONNÉES MANQUANTES — ticker à corriger (`CS.PA` ou `AXAHY`) + earnings J0 FMP glissant sans détails (20e jour consécutif). **STABILITÉ TOTALE MÉCANIQUE** entre snapshot 10h et 13h : scores, sectoriel XLF, FX, geo, news, sentiment strictement inchangés. SCORING STABLE. **FICHIER SECTORIEL EXPLOITABLE** : `data/sector_rotation_2026-06-17.json` valide — XLF rang 4e/11, momentum 5.32/10, RS 20j +3.46%, RS 60j −4.38%.

---

## 📌 Thèse courante

**Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 13h du 17/06 — fichier exploitable) :** Le fichier `data/sector_rotation_2026-06-17.json` est valide ce matin et strictement inchangé entre 10h et 13h (11/11 secteurs OK, aucune anomalie NaN). XLF (Financials) au rang **4e/11**, momentum **5.32/10**, RS 20j **+3.46%**, RS 60j **−4.38%**. C'est une **légère dégradation** vs le close du 16/06 (momentum −1.36 pt, RS 20j −1.18 pp, RS 60j −1.62 pp) mais **stabilité totale mécanique** en séance. XLF reste hors du top 3 (XLK, XLB, XLI). Le signal macro reste `UNKNOWN` (stable depuis le 02/06).

**Action immédiate :** corriger le symbole dans `config/watchlist.json` (`CS.PA` ou `AXAHY`), mettre à jour le secteur (Financials / Insurance) et relancer le fetch.

---

## 📜 Historique des analyses

| Fichier | Date | Type | Résumé |
|---------|------|------|--------|
| `AXA_2026-05-18_preview.md` | 2026-05-18 | Preview earnings (template) | Earnings J0 — template vierge, prédictions non remplies |
| `AXA_2026-05-18_update.md` | 2026-05-18 | Mise à jour quotidienne | Identifie le blocage données + earnings J0 non suivis |
| `AXA_2026-05-19_preview.md` | 2026-05-19 | Preview earnings (template) | Earnings J0 — template vierge, données toujours manquantes |
| `AXA_2026-05-19_update.md` | 2026-05-19 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes ; earnings J0 non résolus ; headwind sectoriel XLF confirmé (RS 20j −6.06%) |
| `AXA_2026-05-19_update.md` | 2026-05-19 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes ; earnings J0 non résolus ; headwind sectoriel XLF légèrement accentué (RS 20j −6.51% vs −6.06% à 17h00, return 20j −2.29% vs −1.52%) |
| `AXA_2026-05-20_update.md` | 2026-05-20 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes ; earnings J0 (2026-05-20) non résolus ; headwind sectoriel XLF stable (RS 20j −6.51%, return 20j −2.29%, momentum 0.0/10) |
| `AXA_2026-05-25_update.md` | 2026-05-25 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes ; earnings J0 FMP (2026-05-25) sans détails ; headwind sectoriel XLF atténué (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) |
| `AXA_2026-05-25_update.md` | 2026-05-25 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — 10e snapshot sans mutation ; earnings J0 FMP (2026-05-25) sans détails exploitables ; headwind sectoriel XLF stable (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) |
| `AXA_2026-05-25_update.md` | 2026-05-25 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — 11e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-25) sans détails exploitables ; headwind sectoriel XLF stable (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) ; marché fermé Memorial Day |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — 12e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-26) sans détails exploitables ; headwind sectoriel XLF stable (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) ; marché rouvert post-Memorial Day sans résolution du sourcing |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — 13e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-26) sans détails exploitables ; headwind sectoriel XLF strictement inchangé (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — 14e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-26) sans détails exploitables ; **mutation sectorielle XLF** détectée entre 13h00 et 17h00 (RS 20j −3.43% → −4.74%, return 20j +1.01% → 0.00%, return 60j −0.56% → +1.26%) ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — 15e snapshot consécutif sans mutation ; **dégradation sectorielle marginale XLF** entre 17h00 et 21h00 (RS 20j −4.74% → −4.88%, RS 60j −8.24% → −8.38%, return 20j 0.00% → +0.08%, return 60j +1.26% → +1.33%) ; marché close sans résolution du sourcing |
| `AXA_2026-05-27_update.md` | 2026-05-27 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — 16e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-27) sans détails exploitables ; **stabilité totale sectorielle XLF** vs close 26/05 (RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10) ; marché pre-market sans résolution du sourcing |
| `AXA_2026-05-27_update.md` | 2026-05-27 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — **17e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-05-27) sans détails exploitables ; **stabilité totale sectorielle XLF** en séance (RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10) ; marché actif en séance sans résolution du sourcing |
| `AXA_2026-05-27_update.md` | 2026-05-27 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — **18e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-05-27) sans détails exploitables ; **mutation sectorielle XLF** détectée entre 13h00 et 17h00 UTC (RS 20j −4.88% → −6.33%, return 20j +0.08% → −0.96%, return 60j +1.33% → +0.61%) ; marché actif en séance sans résolution du sourcing |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — **19e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-06-01) sans détails exploitables ; headwind sectoriel XLF stable à 20j (−6.32%) mais creusé à 60j (−10.05%), momentum 0.0/10 ; signal macro ROTATION_TO_DEFENSIVE ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — **20e snapshot consécutif sans mutation** ; aucune variation inter-snapshot vs 10h00 ; earnings J0 FMP (2026-06-01) sans détails exploitables ; headwind sectoriel XLF stable (RS 20j −6.32%, RS 60j −10.05%, return 20j −1.06%, return 60j +0.67%, momentum 0.0/10) ; signal macro ROTATION_TO_DEFENSIVE inchangé |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — **21e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-06-01) sans détails exploitables ; **mutation signal macro** détectée entre 13h00 et 17h00 UTC (`ROTATION_TO_DEFENSIVE` → `ROTATION_TO_CYCLICAL`) portée par XLK et crossover XLE ; headwind sectoriel XLF creusé à 60j (RS −10.81% vs −10.05% à 13h00, return 20j −1.13%, momentum 0.0/10) ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — **22e snapshot consécutif sans mutation** ; aucune variation inter-snapshot vs 17h00 ; earnings J0 FMP (2026-06-01) sans détails exploitables ; signal macro `ROTATION_TO_CYCLICAL` stable ; headwind sectoriel XLF légèrement atténué (RS −10.73% vs −10.81% à 17h00, return 20j −0.94% vs −1.13%, momentum 0.0/10) ; marché close sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — **23e snapshot consécutif sans mutation** ; stabilité totale sectorielle XLF vs close 01/06 (RS 20j −6.20%, RS 60j −10.73%, return 20j −0.94%, return 60j +0.91%, momentum 0.0/10) ; signal macro `ROTATION_TO_CYCLICAL` stable ; marché pre-market sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — **24e snapshot consécutif sans mutation** ; stabilité totale sectorielle XLF vs snapshot 10h00 (RS 20j −6.20%, RS 60j −10.73%, return 20j −0.94%, return 60j +0.91%, momentum 0.0/10) ; earnings J0 FMP (2026-06-02) sans détails exploitables — 8e jour consécutif ; signal macro `ROTATION_TO_CYCLICAL` stable ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — **25e snapshot consécutif sans mutation** ; **mutation significative du contexte sectoriel** : signal macro neutralisé `NEUTRAL` (was `ROTATION_TO_CYCLICAL`), XLF return 20j amélioré −0.17% (vs −0.94%), return 60j +2.34% (vs +0.91%), RS 60j dégradé −10.96% (vs −10.73%) ; earnings J0 FMP (2026-06-02) sans détails exploitables — 9e jour consécutif ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — **26e snapshot consécutif sans mutation** ; dégradation marginale du contexte sectoriel XLF entre 17h00 et 21h00 (RS 20j −6.02% vs −5.99%, RS 60j −10.99% vs −10.96%, return 20j −0.23% vs −0.17%) ; signal macro `NEUTRAL` inchangé ; earnings J0 FMP (2026-06-02) sans détails exploitables — **10e jour consécutif** ; marché close sans résolution du sourcing |
| `AXA_2026-06-03_update.md` | 2026-06-03 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — **27e snapshot consécutif sans mutation** ; **stabilité totale sectorielle XLF** vs close 02/06 (RS 20j −6.02%, RS 60j −10.99%, return 20j −0.23%, return 60j +2.28%, momentum 0.0/10) ; signal macro `NEUTRAL` inchangé ; earnings J0 FMP (2026-06-03) sans détails exploitables — **11e jour consécutif** ; marché pre-market sans résolution du sourcing |
| `AXA_2026-06-08_update.md` | 2026-06-08 | Mise à jour quotidienne (snapshot 13h00 UTC) | **Stabilité totale** vs snapshot 10h — données manquantes persistantes (4 tickers KO sur 29), contexte sectoriel XLF strictement inchangé (RS 20j +0.64%, RS 60j −3.45%, return 20j +1.45%, momentum 4.0/10), signal macro `NEUTRAL` stable, earnings J0 FMP (2026-06-08) sans détails exploitables |
| `AXA_2026-06-08_update.md` | 2026-06-08 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — 4 tickers KO sur 29 (SPCX résolu) ; **amélioration significative du contexte sectoriel XLF** (RS 20j −6.02% → +0.64%, RS 60j −10.99% → −3.45%, return 20j −0.23% → +1.45%, momentum 0.0/10 → 4.0/10) ; signal macro `NEUTRAL` stable ; earnings J0 FMP (2026-06-08) sans détails exploitables — pattern persistant depuis mi-mai |
| `AXA_2026-06-08_update_17h.md` | 2026-06-08 | Mise à jour quotidienne (snapshot 17h00 UTC) | Scoring stable — données manquantes persistantes (4 tickers KO sur 29) ; contexte sectoriel XLF légèrement mixte (return 20j +1.76% vs +1.45% à 13h, RS 20j +1.20% vs +0.64%, RS 60j −4.34% vs −3.45%), momentum 3.99/10 stable ; signal macro `NEUTRAL` inchangé ; earnings J0 FMP (2026-06-08) sans détails exploitables |
| `AXA_2026-06-09_update.md` | 2026-06-09 | Mise à jour quotidienne (snapshot 13h00 UTC) | **Stabilité totale** vs snapshot 10h — données manquantes persistantes (4 tickers KO sur 29) ; contexte sectoriel XLF strictement inchangé (RS 20j +1.21%, RS 60j −4.31%, return 20j +1.42%, momentum 4.0/10) ; signal macro `NEUTRAL` stable ; earnings J0 FMP (2026-06-09) sans détails exploitables |
| `AXA_2026-06-09_update_21h.md` | 2026-06-09 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **mutation sectorielle XLF positive** entre 13h00 et 21h00 UTC (RS 20j +1.21% → +2.81%, return 20j +1.42% → +2.50%, momentum 4.0/10 → 5.19/10, rang 4e/11 → 3e/11) ; signal macro `NEUTRAL` inchangé ; earnings J0 FMP (2026-06-09) sans détails exploitables |
| `AXA_2026-06-09_update.md` | 2026-06-09 | Mise à jour quotidienne (snapshot 10h00 UTC) | **Stabilité globale** vs close 08/06 — données manquantes persistantes (4 tickers KO sur 29) ; contexte sectoriel XLF légèrement dégradé (return 20j +1.42% vs +1.76%, return 60j +6.98% vs +7.33%, recul au rang 4e/11), RS et momentum stables ; signal macro `NEUTRAL` inchangé ; earnings J0 FMP (2026-06-09) sans détails exploitables — **12e jour consécutif** |
| `AXA_2026-06-10_update.md` | 2026-06-10 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **anomalie JSON majeure** dans `data/sector_rotation_2026-06-10.json` (NaN + momentum 10.0 uniforme pour tous les secteurs) — dernier contexte fiable : 09/06 21h (XLF rang 3e/11, momentum 5.19/10, RS 20j +2.81%) ; signal macro `NEUTRAL` inchangé ; earnings J0 FMP (2026-06-10) sans détails exploitables — **13e jour consécutif** |
| `AXA_2026-06-15_update.md` | 2026-06-15 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **récupération du fichier sectoriel** (XLF rang 2e/11, momentum 6.73/10, RS 20j +4.85%) — amélioration continue vs 09/06 ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-15) sans détails exploitables — **14e jour consécutif** |
| `AXA_2026-06-15_update_17h.md` | 2026-06-15 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **divergence sectorielle XLF** détectée entre snapshot 10h et JSON 17h (rang 3e/11 vs 2e/11, momentum 5.12 vs 6.73, RS 20j +3.13% vs +4.85%) ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-15) sans détails exploitables — **14e jour consécutif** |
| `AXA_2026-06-15_update_21h.md` | 2026-06-15 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **mutation sectorielle mécanique XLF** entre 17h et 21h (rang 2e/11 vs 3e/11, momentum 4.69 vs 5.12, RS 20j +2.70% vs +3.13%) — retour au rang 2e mécanique, pas organique ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-15) sans détails exploitables — **15e jour consécutif** |
| `AXA_2026-06-16_update.md` | 2026-06-16 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **anomalie JSON sectorielle récurrente** dans `data/sector_rotation_2026-06-16.json` (NaN + momentum 10.0 uniforme — déjà observé le 10/06) — fichier classé inexploitable ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-16) sans détails exploitables — **16e jour consécutif** |
| `AXA_2026-06-16_update_13h.md` | 2026-06-16 | Mise à jour quotidienne (snapshot 13h00 UTC) | **Stabilité totale** vs snapshot 10h — données manquantes persistantes (4 tickers KO sur 29) ; **anomalie JSON sectorielle persistante** identique au snapshot 10h (NaN + momentum 10.0 uniforme) — fichier classé inexploitable ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-16) sans détails exploitables — **17e jour consécutif** |
| `AXA_2026-06-16_update_17h.md` | 2026-06-16 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **fichier sectoriel réparé à 17h** — XLF rang 2e/11, momentum 6.68/10 (+1.99 pt vs 15/06 21h), RS 20j +4.64% (+1.94 pp), RS 60j −2.76% (+2.06 pp) ; amélioration sectorielle nette ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-16) sans détails exploitables — **18e jour consécutif** |
| `AXA_2026-06-17_update.md` | 2026-06-17 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes (4 tickers KO sur 29) ; **fichier sectoriel exploitable ce matin** — XLF rang 4e/11 (vs 2e/11), momentum 5.32/10 (vs 6.68/10), RS 20j +3.46% (vs +4.64%), RS 60j −4.38% (vs −2.76%) ; légère dégradation sectorielle ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-17) sans détails exploitables — **19e jour consécutif** |
| `AXA_2026-06-17_update_13h.md` | 2026-06-17 | Mise à jour quotidienne (snapshot 13h00 UTC) | **Stabilité totale mécanique** vs snapshot 10h — données manquantes persistantes (4 tickers KO sur 29) ; fichier sectoriel strictement inchangé (XLF rang 4e/11, momentum 5.32/10, RS 20j +3.46%, RS 60j −4.38%) ; signal macro `UNKNOWN` stable ; earnings J0 FMP (2026-06-17) sans détails exploitables — **20e jour consécutif** |

---

## 📊 Scores historiques

| Date | Score Opportunité | Score Global | Recommandation | Timing |
|------|-------------------|--------------|----------------|--------|
| 2026-05-18 | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-19 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-19 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-20 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-25 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-25 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-25 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-26 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-26 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-26 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-26 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-27 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-27 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-01 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-01 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-01 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-02 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-02 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-02 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-02 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-03 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-08 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-08 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-09 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-09 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-09 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-10 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-15 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-15 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-15 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-16 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-16 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-16 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-17 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-17 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |

---

## 🗓️ Agenda des prochains événements

| Événement | Date | Statut |
|-----------|------|--------|
| Earnings | 2026-06-17 | **J0 FMP — sans détails exploitables (données manquantes)** |

---

## ⚠️ Alertes actives

- **[CRITICAL]** Pas de données de prix pour AXA — ticker probablement incorrect
- **[WARNING]** Earnings J0 (2026-06-17) sans consensus ni résultats exploitables — pattern persistant depuis mi-mai (19e occurrence consécutive)
- **[INFO]** **Fichier sectoriel exploitable** : `data/sector_rotation_2026-06-17.json` valide — XLF rang 4e/11, momentum 5.32/10, RS 20j +3.46%, RS 60j −4.38%. **Stabilité totale mécanique** entre 10h et 13h, signal macro `UNKNOWN` stable

---

## 🔗 Liens utiles

- [Actualités/WATCHLIST.md](../../Actualités/WATCHLIST.md)
- [Actions/WATCHLIST_SCORES.md](../../Actions/WATCHLIST_SCORES.md)
- [Alertes/UPCOMING_EVENTS.md](../../Alertes/UPCOMING_EVENTS.md)
