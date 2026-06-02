# AXA — Index du Dossier

> **Dernière mise à jour :** 2026-06-02 (snapshot 21h00 UTC)
> **Statut :** 🔴 DONNÉES MANQUANTES — ticker à corriger (`CS.PA` ou `AXAHY`) + earnings J0 FMP glissant sans détails (10e jour consécutif)

---

## 📌 Thèse courante

**Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale reste impossible.

**Contexte sectoriel (snapshot 2026-06-02 21h00 UTC) :** Le secteur Financials (XLF) affiche une **dégradation marginale** par rapport au snapshot 17h00 : return 20j −0.23% (vs −0.17%), return 60j +2.28% (vs +2.34%), RS 20j −6.02% (vs −5.99%), RS 60j −10.99% (vs −10.96%). Ces variations (−3 bp à −6 bp) sont d'amplitude négligeable et ne modifient pas l'interprétation : le secteur reste en sous-performance structurelle vs le broad market (SPY +5.79% sur 20j, +13.28% sur 60j) et le momentum score reste à 0.0/10. Le signal macro `NEUTRAL` est inchangé. XLF reste classé 3e/11, en distribution relative vs le marché. Le snapshot confirme que les données de prix US sont bien récupérées (24 tickers OK sur 29), isolant AXA comme l'un des 5 tickers structurellement KO sur 29. Si les données AXA étaient disponibles, le headwind sectoriel persistant justifierait un ajustement à la baisse du placeholder Momentum (actuellement 5.0/10).

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
| `AXA_2026-05-25_update.md` | 2026-05-25 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — 10e snapshot sans mutation ; earnings J0 FMP (2026-05-25) sans détails ; headwind sectoriel XLF stable (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) |
| `AXA_2026-05-25_update.md` | 2026-05-25 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — 11e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-25) sans détails ; headwind sectoriel XLF stable (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) ; marché fermé Memorial Day |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — 12e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-26) sans détails ; headwind sectoriel XLF stable (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) ; marché rouvert post-Memorial Day sans résolution du sourcing |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — 13e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-26) sans détails ; headwind sectoriel XLF strictement inchangé (RS 20j −3.43%, return 20j +1.01%, momentum 0.0/10) ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — 14e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-26) sans détails ; **mutation sectorielle XLF** détectée entre 13h00 et 17h00 (RS 20j −3.43% → −4.74%, return 20j +1.01% → 0.00%, return 60j −0.56% → +1.26%) ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-05-26_update.md` | 2026-05-26 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — 15e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-26) sans détails ; **dégradation sectorielle marginale XLF** entre 17h00 et 21h00 (RS 20j −4.74% → −4.88%, RS 60j −8.24% → −8.38%, return 20j 0.00% → +0.08%, return 60j +1.26% → +1.33%) ; marché close sans résolution du sourcing |
| `AXA_2026-05-27_update.md` | 2026-05-27 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — 16e snapshot consécutif sans mutation ; earnings J0 FMP (2026-05-27) sans détails ; **stabilité totale sectorielle XLF** vs close 26/05 (RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10) ; marché pre-market sans résolution du sourcing |
| `AXA_2026-05-27_update.md` | 2026-05-27 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — **17e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-05-27) sans détails exploitables ; **stabilité totale sectorielle XLF** en séance (RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10) ; marché actif en séance sans résolution du sourcing |
| `AXA_2026-05-27_update.md` | 2026-05-27 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — **18e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-05-27) sans détails exploitables ; **mutation sectorielle XLF** détectée entre 13h00 et 17h00 UTC (RS 20j −4.88% → −6.33%, return 20j +0.08% → −0.96%, return 60j +1.33% → +0.61%) ; marché actif en séance sans résolution du sourcing |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — **19e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-06-01) sans détails exploitables ; headwind sectoriel XLF stable à 20j (−6.32%) mais creusé à 60j (−10.05%), momentum 0.0/10 ; signal macro ROTATION_TO_DEFENSIVE ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — **20e snapshot consécutif sans mutation** ; aucune variation inter-snapshot vs 10h00 ; earnings J0 FMP (2026-06-01) sans détails exploitables ; headwind sectoriel XLF stable (RS 20j −6.32%, RS 60j −10.05%, return 20j −1.06%, return 60j +0.67%, momentum 0.0/10) ; signal macro ROTATION_TO_DEFENSIVE inchangé |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — **21e snapshot consécutif sans mutation** ; earnings J0 FMP (2026-06-01) sans détails exploitables ; **mutation signal macro** détectée entre 13h00 et 17h00 UTC (`ROTATION_TO_DEFENSIVE` → `ROTATION_TO_CYCLICAL`) portée par XLK et crossover XLE ; headwind sectoriel XLF creusé à 60j (RS −10.81% vs −10.05% à 13h00, return 20j −1.13%, momentum 0.0/10) ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-06-01_update.md` | 2026-06-01 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — **22e snapshot consécutif sans mutation** ; aucune variation inter-snapshot vs 17h00 ; earnings J0 FMP (2026-06-01) sans détails exploitables ; signal macro `ROTATION_TO_CYCLICAL` stable ; headwind sectoriel XLF légèrement atténué (RS −10.73% vs −10.81% à 17h00, return 20j −0.94% vs −1.13%, momentum 0.0/10) ; marché close sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 10h00 UTC) | Données manquantes persistantes — **23e snapshot consécutif sans mutation** ; stabilité totale sectorielle XLF vs close 01/06 (RS 20j −6.20%, RS 60j −10.73%, return 20j −0.94%, return 60j +0.91%, momentum 0.0/10) ; earnings J0 FMP (2026-06-02) sans détails exploitables — 7e jour consécutif ; signal macro `ROTATION_TO_CYCLICAL` stable ; marché pre-market sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 13h00 UTC) | Données manquantes persistantes — **24e snapshot consécutif sans mutation** ; stabilité totale sectorielle XLF vs snapshot 10h00 (RS 20j −6.20%, RS 60j −10.73%, return 20j −0.94%, return 60j +0.91%, momentum 0.0/10) ; earnings J0 FMP (2026-06-02) sans détails exploitables — 8e jour consécutif ; signal macro `ROTATION_TO_CYCLICAL` stable ; marché actif et liquide sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 21h00 UTC) | Données manquantes persistantes — **26e snapshot consécutif sans mutation** ; dégradation marginale du contexte sectoriel XLF entre 17h00 et 21h00 (RS 20j −6.02% vs −5.99%, RS 60j −10.99% vs −10.96%, return 20j −0.23% vs −0.17%) ; signal macro `NEUTRAL` inchangé ; earnings J0 FMP (2026-06-02) sans détails exploitables — **10e jour consécutif** ; marché close sans résolution du sourcing |
| `AXA_2026-06-02_update.md` | 2026-06-02 | Mise à jour quotidienne (snapshot 17h00 UTC) | Données manquantes persistantes — **25e snapshot consécutif sans mutation** ; **mutation significative du contexte sectoriel** : signal macro neutralisé `NEUTRAL` (was `ROTATION_TO_CYCLICAL`), XLF return 20j amélioré −0.17% (vs −0.94%), return 60j +2.34% (vs +0.91%), RS 60j dégradé −10.96% (vs −10.73%) ; earnings J0 FMP (2026-06-02) sans détails exploitables — 9e jour consécutif ; marché actif et liquide sans résolution du sourcing |

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
| 2026-06-02 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-01 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-01 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-01 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-01 (10h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-05-27 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-02 (13h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-02 (21h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |
| 2026-06-02 (17h00) | 5.5/10 (C:6.5 V:5.0 M:5.0) | 55.2/100 | ATTENDRE | Neutre |

---

## 🗓️ Agenda des prochains événements

| Événement | Date | Statut |
|-----------|------|--------|
| Earnings | 2026-05-20 | **J0 — non suivi (données manquantes)** |
| Earnings | 2026-05-25 | **J0 FMP — sans détails exploitables (données manquantes)** |
| Earnings | 2026-05-26 | **J0 FMP — sans détails exploitables (données manquantes)** |
| Earnings | 2026-06-01 | **J0 FMP — sans détails exploitables (données manquantes)** |
| Earnings | 2026-06-02 | **J0 FMP — sans détails exploitables (données manquantes)** |
| Earnings | 2026-05-27 | **J0 FMP — sans détails exploitables (données manquantes)** |

---

## ⚠️ Alertes actives

- **[CRITICAL]** Pas de données de prix pour AXA — ticker probablement incorrect
- **[WARNING]** Earnings J0 (2026-06-02) sans consensus ni résultats exploitables — **10e jour consécutif**
- **[INFO]** Headwind sectoriel XLF persistant : RS 20j −6.02%, RS 60j −10.99%, return 20j −0.23%, return 60j +2.28%, momentum 0.0/10 ; signal macro `NEUTRAL`

---

## 🔗 Liens utiles

- [Actualités/WATCHLIST.md](../../Actualités/WATCHLIST.md)
- [Actions/WATCHLIST_SCORES.md](../../Actions/WATCHLIST_SCORES.md)
- [Alertes/UPCOMING_EVENTS.md](../../Alertes/UPCOMING_EVENTS.md)
