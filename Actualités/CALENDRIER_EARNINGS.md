# Calendrier Earnings — 30 prochains jours

**Mis à jour le :** 2026-05-26
**Prochaine mise à jour :** 2026-05-27 (revue quotidienne Phase 0)

> Ce fichier est lu automatiquement chaque matin (Phase 0 du bulletin).
> Si un ticker watchlist a des earnings dans **≤ 5 jours** → `_preview.md` généré automatiquement.
> Si un ticker watchlist a des earnings dans **≤ 2 jours** → régime "Pré-earnings" activé (pondération 50/30/20).

---

## 🔴 Earnings dans ≤ 5 jours — ACTION IMMÉDIATE

| Date | Ticker | Nom | Heure | Trimestre | Consensus EPS | Consensus Rev. | Preview créé | Prédiction |
|------|--------|-----|-------|-----------|--------------|----------------|-------------|-----------|
| Aucun ticker watchlist | — | — | — | — | — | — | — | — |

> **AMC** = After Market Close · **BMO** = Before Market Open

---

## 🟡 Earnings dans 6–14 jours — Surveillance active

| Date | Ticker | Nom | Heure | Trimestre | Consensus EPS | Consensus Rev. | Preview à créer le |
|------|--------|-----|-------|-----------|--------------|----------------|--------------------|
| 2026-05-20 | NVDA* | NVIDIA Corp | AMC | Q1 FY27 | ~$0.93 | ~$43.3B | 2026-05-15 (J−5) |

*NVDA non encore sur watchlist formelle. Impact indirect fort sur IREN (deal $3.4B/an). Considérer ajout watchlist.

---

## 🟢 Earnings dans 15–30 jours — À l'horizon

| Date | Ticker | Nom | Heure | Trimestre | Consensus EPS | Consensus Rev. | Notes |
|------|--------|-----|-------|-----------|--------------|----------------|-------|
| YYYY-MM-DD | | | AMC / BMO | QX 20XX | $X.XX | $Xb | |

---

## 📋 Earnings passés ce mois — Résultats & Liens

| Date | Ticker | Trimestre | EPS réel vs consensus | Rev. réelle vs consensus | Réaction cours | Analyse |
|------|--------|-----------|----------------------|--------------------------|---------------|---------|
| 2026-05-17 | IREN | Q4 FY26 / Q1 FY27 | ⏳ En attente | ⏳ En attente | −9.35% (pre-market) | [IREN_2026-05-17_earnings.md](../Actions/IREN/IREN_2026-05-17_earnings.md) |
| 2026-05-26 | CTMX | À confirmer | — | — | −4.26% | [CTMX_2026-05-26_init.md](../Actions/CTMX/CTMX_2026-05-26_init.md) · Date FMP héritée du symbole erroné CYTOMX, earnings réel à vérifier |

---

## 🗓️ Saisons d'earnings — Rappel calendrier annuel

| Trimestre | Période de publication | Mois de pic |
|-----------|----------------------|-------------|
| Q1 (Jan–Mars) | Mi-avril à mi-mai | Avril |
| Q2 (Avr–Juin) | Mi-juillet à mi-août | Juillet |
| Q3 (Juil–Sept) | Mi-octobre à mi-novembre | Octobre |
| Q4 (Oct–Déc) | Mi-janvier à mi-février | Janvier |

**Prochaines saisons :**
- Q1 2026 : En cours (mai 2026)
- Q2 2026 : Juillet–Août 2026
- Q3 2026 : Octobre–Novembre 2026

---

## 🔔 Alertes automatiques earnings

> Ces alertes se déclenchent dès que les conditions sont remplies lors du bulletin du matin.

| Condition | Action automatique |
|-----------|-------------------|
| Earnings watchlist dans ≤ 5 jours ET preview absent | Créer `[TICKER]_preview.md` + enregistrer dans SUIVI_EARNINGS_PREDICTIONS.md |
| Earnings watchlist dans ≤ 2 jours | Activer régime Pré-earnings (pondération 50/30/20) |
| IV Rank > 70 dans J−7 avant earnings | Alerte "options chères pré-earnings" dans bulletin |
| Volume > 2× dans J−3 avant earnings | Alerte "positionnement pré-earnings inhabituel" |

---

## Protocole de mise à jour

```
CHAQUE LUNDI MATIN (Phase H4 de WORKFLOW_SEMAINE.md) :
1. Déplacer les earnings passés dans "Earnings passés ce mois"
2. Ajouter les nouveaux earnings via `calendar` ou `news`
3. Vérifier les dates pour tous les tickers de la watchlist
4. Mettre à jour les colonnes "Consensus EPS" et "Consensus Rev." via `analyst`

CHAQUE MATIN (Phase 0 du bulletin) :
1. Lire ce fichier
2. Si earnings ≤ 5 jours ET preview absent → générer automatiquement
3. Si earnings ≤ 2 jours → activer régime Pré-earnings pour ce ticker
```
