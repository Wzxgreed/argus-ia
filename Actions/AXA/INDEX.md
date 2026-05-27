# AXA — Index du Dossier

> **Dernière mise à jour :** 2026-05-27 (snapshot 10h00 UTC)
> **Statut :** 🔴 DONNÉES MANQUANTES — ticker à corriger (`CS.PA` ou `AXAHY`) + stabilité totale sectorielle XLF vs close 26/05 (RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10), 3e jour consécutif earnings J0 FMP sans détails exploitables

---

## 📌 Thèse courante

**Recommandation :** ATTENDRE (Score Global 55.2/100)

AXA est un assureur-français mondial coté à Euronext Paris. À ce stade, **aucune donnée de prix n'est disponible** dans le pipeline Argus-IA car le symbole "AXA" n'est pas reconnu par yfinance (instrument non coté US). L'analyse technique et fondamentale est impossible.

**Contexte sectoriel (snapshot 10h00 UTC) :** Le secteur Financials (XLF) sous-performe le S&P 500 de −4.88% sur 20j et −8.38% sur 60j, avec un momentum score de 0.0/10. Le secteur affiche un return 20j de +0.08% et un return 60j de +1.33%. Les métriques sectorielles sont strictement identiques à celles du snapshot 21h00 UTC du 26/05 : aucune mutation technique sectorielle n'est survenue entre la close US du 26/05 et le pre-market du 27/05. Le secteur financier reste en phase de distribution relative vs le marché (SPY surperforme de +4.87pp sur 20j), sous le coup de la rotation sectorielle vers la Tech (XLK return 20j +15.3%, momentum 10.0/10). Le snapshot pre-market du 27/05 confirme que les données de prix US sont bien récupérées (AAPL 47.9M, NOK 188.9M, RKLB 32.8M), isolant AXA comme l'un des 3 tickers structurellement KO sur 26. Si les données AXA étaient disponibles, cette stabilité sectorielle laisserait le score Momentum inchangé.

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

---

## 🗓️ Agenda des prochains événements

| Événement | Date | Statut |
|-----------|------|--------|
| Earnings | 2026-05-20 | **J0 — non suivi (données manquantes)** |
| Earnings | 2026-05-25 | **J0 FMP — sans détails exploitables (données manquantes)** |
| Earnings | 2026-05-26 | **J0 FMP — sans détails exploitables (données manquantes)** |
| Earnings | 2026-05-27 | **J0 FMP — sans détails exploitables (données manquantes)** |

---

## ⚠️ Alertes actives

- **[CRITICAL]** Pas de données de prix pour AXA — ticker probablement incorrect
- **[WARNING]** Earnings J0 (2026-05-27) sans consensus ni résultats exploitables — 3e jour consécutif
- **[INFO]** Stabilité totale sectorielle XLF vs close 26/05 : RS 20j −4.88%, RS 60j −8.38%, return 20j +0.08%, return 60j +1.33%, momentum 0.0/10

---

## 🔗 Liens utiles

- [Actualités/WATCHLIST.md](../../Actualités/WATCHLIST.md)
- [Actions/WATCHLIST_SCORES.md](../../Actions/WATCHLIST_SCORES.md)
- [Alertes/UPCOMING_EVENTS.md](../../Alertes/UPCOMING_EVENTS.md)
