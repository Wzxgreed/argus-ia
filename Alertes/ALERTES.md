# Alertes sur seuils — Suivi actif

Fichier lu automatiquement à chaque session. Si un seuil est franchi, un `_update.md` est généré et le déclenchement est loggué ci-dessous.

---

## Alertes simples actives

| Ticker | Type | Seuil | Cours réf. | Statut | Créée le |
|--------|------|-------|------------|--------|----------|
| **IREN** | Baisse | $45.00 | $52.94 | 🟢 Active | 2026-05-17 |
| **IREN** | Hausse | $65.86 | $52.94 | 🟢 Active | 2026-05-17 |
| **IREN** | Volume | >2× moy. 20j (>104.9M) | 52.4M moy. | 🟢 Active | 2026-05-17 |

> **Types d'alerte simples disponibles :**
> - `Baisse` — cours franchit un seuil à la baisse
> - `Hausse` — cours franchit un seuil à la hausse
> - `Volume` — volume journalier > N× la moyenne 20 jours
> - `Short interest` — short interest augmente de > X% en 2 semaines
> - `Insider` — achat ou vente insider > $500k
> - `Rating` — changement de recommandation analyst (upgrade/downgrade)
> - `Supply chain` — news significative sur un fournisseur/client critique

---

## 🆕 Alertes composites actives

> Les alertes composites combinent plusieurs conditions avec des opérateurs logiques.
> Elles filtrent le bruit et ne se déclenchent que lorsque **plusieurs signaux convergent simultanément**.

### Syntaxe des alertes composites

```
ALERTE COMPOSITE [ID] — [TICKER]
CONDITIONS : [Condition1] ET/OU [Condition2] ET/OU [Condition3]
SEUIL DE DÉCLENCHEMENT : Toutes (ET) / Au moins N sur X (OU)
ACTION : [Ce qui se passe si l'alerte se déclenche]
```

**Opérateurs disponibles :**
- `ET` — toutes les conditions doivent être vraies simultanément
- `OU` — au moins une condition suffit
- `ET_DANS(Nj)` — conditions doivent être vraies dans une fenêtre de N jours
- `SAUF` — condition d'exclusion (si vraie, alerte annulée)

**Variables disponibles dans les conditions :**
- `COURS` — cours actuel
- `RSI(N)` — RSI sur N jours
- `VOLUME` — volume du jour
- `VOL_MOY(N)` — volume moyen sur N jours
- `MM(N)` — moyenne mobile sur N jours
- `SHORT_INT` — short interest en % du float
- `IV_RANK` — IV Rank du titre
- `EPS_REV(Nj)` — solde de révisions EPS sur N jours (+ = hausse, - = baisse)
- `INSIDER_NET(Nj)` — net achats insiders sur N jours (en $)
- `GEX` — Gamma Exposure (POS = stabilisant, NEG = amplifiant)

---

### Exemples d'alertes composites

**COMPOSITE-001 — Setup short squeeze**
```
CONDITIONS : SHORT_INT > 15%
         ET VOLUME > VOL_MOY(20) × 2
         ET COURS > MM(50)
         ET GEX = NEG
DÉCLENCHEMENT : Toutes (ET)
ACTION : Alerte "Short squeeze potentiel" → _update.md + section Opportunités
PRIORITÉ : 🔴 Haute
```

**COMPOSITE-002 — Signal de sortie silencieux**
```
CONDITIONS : EPS_REV(30j) < -3
         ET INSIDER_NET(60j) < -$1M
         ET COURS < MM(50)
DÉCLENCHEMENT : Au moins 2 sur 3 (OU)
ACTION : Alerte "Dégradation multi-signaux" → _update.md immédiat
PRIORITÉ : 🔴 Haute
```

**COMPOSITE-003 — Opportunité contrarian post-capitulation**
```
CONDITIONS : COURS < MM(200) × 0.85
         ET RSI(14) < 30
         ET IV_RANK > 75
         ET SHORT_INT > 10%
DÉCLENCHEMENT : Au moins 3 sur 4 (OU)
ACTION : Alerte "Potentiel point bas technique" → ajouter à l'analyse du matin
PRIORITÉ : 🟡 Modérée
```

**COMPOSITE-004 — Breakout de qualité**
```
CONDITIONS : COURS > MM(200)
         ET COURS > MM(50)
         ET VOLUME > VOL_MOY(20) × 1.5
         ET EPS_REV(30j) > 0
         ET RSI(14) > 50 ET RSI(14) < 70
DÉCLENCHEMENT : Toutes (ET)
ACTION : Alerte "Breakout confirmé multi-signaux" → rapport Opportunités
PRIORITÉ : 🟢 Standard
```

---

### Alertes composites actives — [Mes tickers]

| ID | Ticker | Conditions | Seuil déclench. | Statut | Créée le |
|----|--------|-----------|----------------|--------|----------|
| COMP-001 | | Voir template ci-dessus | Toutes (ET) | 🟢 Active | |

> **Ajouter une alerte composite :** `Ajoute une alerte composite sur [TICKER] : [condition1] ET/OU [condition2]`

---

## 📋 Log des déclenchements

| Date | Ticker | Type | Conditions remplies | Cours au déclenchement | Fichier généré |
|------|--------|------|--------------------|-----------------------|----------------|
| 2026-05-11 | IREN | Vérification | Aucun seuil franchi · Cours ~$61.20 (baisse $54.20 ✅ · hausse $85 ✅) | $61.20 | Aucun — alertes actives |
| 2026-05-11 | IREN | **⚠️ Volume DÉCLENCHÉ** | Volume 108M (seuil 72.8M) · 187% au-dessus moy. 20j · $2B convertible note annonce | $55.15 (close) | [IREN_2026-05-12_update.md](../Actions/IREN/IREN_2026-05-12_update.md) |
| 2026-05-11 | IREN | **⚠️ Baisse INTRADAY** | Low $52.36 < seuil $54.20 · Close $55.15 (rebond au-dessus) · Attention : seuil très proche | $52.36 (low) | Inclus dans IREN_2026-05-12_update.md · Surveiller clôture |

---

## Protocole d'évaluation quotidienne

```
CHAQUE MATIN — AVANT le bulletin (Phase 0) :

ALERTES SIMPLES :
1. Pour chaque alerte active → récupérer cours actuel via `quote`
2. Si seuil franchi → déclencher l'action définie + logger

ALERTES COMPOSITES :
1. Pour chaque alerte composite active :
   a. Évaluer chaque condition individuellement via les sources appropriées
      → COURS, MM : `quote` + `technicalIndicators`
      → RSI : `technicalIndicators`
      → SHORT_INT : `quote`
      → IV_RANK : `quote` options chain
      → EPS_REV : `analyst`
      → INSIDER_NET : `insiderTrades`
      → GEX : estimation via `quote` options
   b. Appliquer l'opérateur (ET / OU / seuil N sur X)
   c. Si déclenchement → action définie + logger dans "Log des déclenchements"
   d. Mettre à jour WATCHLIST_SCORES.md section "Alertes actives du jour"

AVANTAGE CLÉ :
→ Alertes composites = beaucoup moins de faux positifs
→ Un titre peut franchir sa MM50 sans déclencher d'alerte si le volume est normal
→ L'alerte se déclenche uniquement quand le signal est vraiment significatif
```

---

## Alertes désactivées / archivées

| Ticker | Type | Conditions | Déclenchée le | Raison désactivation |
|--------|------|-----------|---------------|----------------------|
| | Simple / Composite | | | Seuil atteint / Position clôturée / Obsolète |
