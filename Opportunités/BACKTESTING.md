# Backtesting — Performance des signaux & Boucle d'apprentissage

Ce fichier trace la performance réelle de chaque opportunité signalée **et déclenche automatiquement un post-mortem sur chaque erreur**. L'objectif n'est pas seulement de mesurer — c'est de comprendre pourquoi le système s'est trompé et de ne pas reproduire l'erreur.

**Mise à jour :** Automatiquement à J+5, J+20, et J+60 après chaque signal. À lire lors du workflow du matin pour vérifier les fenêtres de suivi ouvertes.

**Fichier lié :** `Agents/APPRENTISSAGES.md` — reçoit toutes les règles extraites des post-mortems.

---

## Règles de suivi

1. **Toute opportunité publiée dans un rapport `Opportunités/YYYY-MM-DD.md`** avec un score ≥ 6/10 est automatiquement enregistrée ici.
2. **Suivi à 3 horizons :** J+5 (réaction court terme), J+20 (confirmation thèse), J+60 (validation long terme)
3. **Verdict :** ✅ Hit (cours > +2%), ❌ Miss (cours < −2%), ⚪ Scratch (±2%), 🔄 Invalidé (événement externe)
4. **Post-mortem obligatoire :** Tout Miss à J+20 ou J+60 déclenche automatiquement un post-mortem complet (voir protocole ci-dessous).
5. **Révision automatique :** Si le signal est invalidé par un événement externe imprévisible (black swan, earnings surprise majeure non modélisable), noter "Invalidé — raison externe" MAIS réaliser quand même un post-mortem allégé pour vérifier si un signal d'alerte existait.

---

## Journal des signaux

| Date signal | Ticker | Score | Type signal | Cours signal | J+5 | J+20 | J+60 | Verdict |
|------------|--------|-------|-------------|-------------|-----|------|------|---------|
| 2026-05-10 | INOD | 7.2/10 | Earnings beat + Big Tech deal | $84.89 | ✅ Hit (+13.0%) | ⏳ 2026-05-30 | ⏳ 2026-07-09 | ⏳ En cours |
| 2026-05-10 | BA | 7.0/10 | Catalyseur événementiel (summit) | $237.36 | ❌ Miss (-7.0%) | ⏳ 2026-05-30 | ⏳ 2026-07-09 | ⏳ En cours |
| 2026-05-10 | INTC | 6.7/10 | Rotation sectorielle IA | $124.92 | ❌ Miss (-13.0%) | ⏳ 2026-05-30 | ⏳ 2026-07-09 | ⏳ En cours |
| 2026-05-11 | BA | 7.5/10 | Sommet Trump-Xi · CEO + commandes | ~$237 | ❌ Miss (-7.0%) | ⏳ 2026-05-31 | ⏳ 2026-07-10 | ⏳ En cours |
| 2026-05-11 | INTC | 6.7/10 | IA CPU demand · Apple chip talks | ~$126 | ❌ Miss (-14.0%) | ⏳ 2026-05-31 | ⏳ 2026-07-10 | ⏳ En cours |
| 2026-05-11 | RKLB | 6.5/10 | Space infra · Q1 record earnings | ~$105 | ✅ Hit (+19.0%) | ⏳ 2026-05-31 | ⏳ 2026-07-10 | ⏳ En cours |
| 2026-05-12 | XOM | 7.35/10 | Énergie · Crise Iran/Hormuz · oil $100 · Stagflation | ~cours mkt | ⏳ 2026-05-17 | ⏳ 2026-06-01 | ⏳ 2026-07-11 | ⏳ En cours |
| 2026-05-12 | RTX | 6.95/10 | Défense · Guerre Iran · Réarmement OTAN · Stagflation | ~cours mkt | ⏳ 2026-05-17 | ⏳ 2026-06-01 | ⏳ 2026-07-11 | ⏳ En cours |
| 2026-05-12 | VRT | 6.45/10 | Infrastructure IA · Refroidissement DC · Stagflation | ~cours mkt | ⏳ 2026-05-17 | ⏳ 2026-06-01 | ⏳ 2026-07-11 | ⏳ En cours |

> *Ce tableau se remplit au fil des opportunités détectées.*

---

## Performance agrégée

### Par horizon de temps
| Horizon | Signaux totaux | Hits | Misses | Scratch | Win rate | Gain moyen | Perte moyenne |
|---------|--------------|------|--------|---------|---------|-----------|--------------|
| J+5 | 0 | 0 | 0 | 0 | — | — | — |
| J+20 | 0 | 0 | 0 | 0 | — | — | — |
| J+60 | 0 | 0 | 0 | 0 | — | — | — |

### Par fourchette de score
| Score signal | Signaux | Win rate J+20 | Gain moyen J+20 |
|-------------|---------|--------------|----------------|
| 9–10 | 0 | — | — |
| 7–8 | 0 | — | — |
| 6–7 | 0 | — | — |

### Par type de catalyseur
| Type catalyseur | Signaux | Win rate J+20 |
|----------------|---------|--------------|
| Earnings beat | 0 | — |
| Upgrade analyste | 0 | — |
| Insider buying | 0 | — |
| Short squeeze | 0 | — |
| Macro favorable | 0 | — |
| Breakout technique | 0 | — |

---

## Signaux en cours de suivi

> Tableau mis à jour chaque matin. Vérifier les fenêtres ouvertes.

| Ticker | Date signal | Score | Cours signal | Fenêtres ouvertes | Action requise |
|--------|------------|-------|-------------|------------------|----------------|
| INOD | 2026-05-10 | 7.2/10 | $84.89 | J+5: 2026-05-15 · J+20: 2026-05-30 · J+60: 2026-07-09 | Vérifier cours le 2026-05-15 |
| BA | 2026-05-10 | 7.0/10 | $237.36 | J+5: 2026-05-15 · J+20: 2026-05-30 · J+60: 2026-07-09 | Vérifier cours le 2026-05-15 (post-summit) |
| INTC | 2026-05-10 | 6.7/10 | $124.92 | J+5: 2026-05-15 · J+20: 2026-05-30 · J+60: 2026-07-09 | Vérifier cours le 2026-05-15 |
| BA | 2026-05-11 | 7.5/10 | ~$237 | J+5: 2026-05-16 · J+20: 2026-05-31 · J+60: 2026-07-10 | Vérifier cours le 2026-05-16 (post-summit résultats) |
| INTC | 2026-05-11 | 6.7/10 | ~$126 | J+5: 2026-05-16 · J+20: 2026-05-31 · J+60: 2026-07-10 | Vérifier le 2026-05-16 ⚠️ RSI overbought |
| RKLB | 2026-05-11 | 6.5/10 | ~$105 | J+5: 2026-05-16 · J+20: 2026-05-31 · J+60: 2026-07-10 | Vérifier cours le 2026-05-16 |

---

## Règles de mise à jour automatique

```
CHAQUE MATIN — avant le workflow principal :
1. Lire Agents/APPRENTISSAGES.md (règles actives à charger)
2. Lire ce fichier
3. Identifier les signaux dont la fenêtre J+5 / J+20 / J+60 tombe aujourd'hui ou dans les 2 prochains jours
4. Pour chaque fenêtre ouverte :
   → Récupérer le cours actuel via `quote`
   → Calculer la performance depuis le cours signal
   → Enregistrer dans le journal
   → Calculer le verdict (✅ Hit / ❌ Miss / ⚪ Scratch / 🔄 Invalidé)
5. Mettre à jour les tableaux de performance agrégée
6. Si verdict = ❌ Miss sur J+20 ou J+60 → DÉCLENCHER LE POST-MORTEM AUTOMATIQUEMENT (voir protocole)
7. Si win rate J+20 < 50% sur les 20 derniers signaux → révision globale du scoring
```

---

## Protocole Post-Mortem — Déclenché automatiquement sur chaque Miss J+20 ou J+60

```
ÉTAPE 1 — COLLECTE DES FAITS
→ Lire Actions/[TICKER]/[TICKER]_YYYY-MM-DD_[type].md (fichier source du signal)
→ Lire Actions/[TICKER]/INDEX.md (contexte et thèse au moment du signal)
→ Récupérer le cours day-by-day entre la date signal et aujourd'hui via `quote`
→ Récupérer les news majeures sur [TICKER] sur cette période via `news`
→ Identifier l'événement déclencheur de la baisse

ÉTAPE 2 — DIAGNOSTIC
→ Comparer le score original (Catalyseur/Valorisation/Momentum) avec les données actuelles
→ Identifier l'agent responsable de l'erreur principale :
   - Agent Macro : mauvais régime identifié ? pondération incorrecte ?
   - Agent Flux : signal 13F/ETF ignoré ? short squeeze manqué ?
   - Agent Technique : force relative déjà dégradée ? timing erroné ?
   - Agent Fondamental : hypothèses DCF trop optimistes ? qualité bénéfices non vérifiée ?
   - Agent Sentiment : analyste peu fiable ? catalyseur surévalué ? IV signal ignoré ?
→ Identifier si un signal d'alerte était présent mais sous-pondéré dans l'analyse originale

ÉTAPE 3 — EXTRACTION DE LA RÈGLE
→ Formuler UNE règle claire et actionnable pour ne pas reproduire cette erreur
→ La règle doit être universelle (applicable à tous les tickers, pas juste [TICKER])
→ Exemples de formulation correcte :
   "Si régime Risk-off ET ticker cyclique → plafonner Score Catalyseur à 6/10 max"
   "Si force relative vs secteur < 0.90 depuis 4 semaines → pénaliser Momentum de −1 pt"
   "Upgrade d'analyste sans vérification track record → ×0.7 sur contribution au score"

ÉTAPE 4 — DOCUMENTATION
→ Écrire le post-mortem complet dans Agents/APPRENTISSAGES.md (section Journal)
→ Ajouter la règle dans "Règles actives" de Agents/APPRENTISSAGES.md
→ Mettre à jour le tableau Track Record si un analyste est en cause
→ Mettre à jour la colonne "Post-mortem" du journal des signaux ci-dessous
→ Logger la date dans "Statistiques d'apprentissage"
```

---

## Journal des signaux (avec suivi post-mortem)

| Date signal | Ticker | Score | Type signal | Cours signal | J+5 | J+20 | J+60 | Verdict | Post-mortem |
|------------|--------|-------|-------------|-------------|-----|------|------|---------|-------------|
| — | — | — | — | — | — | — | — | — | — |

> *Ce tableau se remplit au fil des opportunités détectées.*

---

## Performance agrégée

### Par horizon de temps
| Horizon | Signaux totaux | Hits | Misses | Scratch | Invalidés | Win rate | Gain moyen | Perte moyenne |
|---------|--------------|------|--------|---------|-----------|---------|-----------|--------------|
| J+5 | 0 | 0 | 0 | 0 | 0 | — | — | — |
| J+20 | 0 | 0 | 0 | 0 | 0 | — | — | — |
| J+60 | 0 | 0 | 0 | 0 | 0 | — | — | — |

### Par fourchette de score
| Score signal | Signaux | Win rate J+20 | Gain moyen J+20 | Post-mortems |
|-------------|---------|--------------|----------------|--------------|
| 9–10 | 0 | — | — | 0 |
| 7–8 | 0 | — | — | 0 |
| 6–7 | 0 | — | — | 0 |

### Par type de catalyseur
| Type catalyseur | Signaux | Win rate J+20 | Tendance |
|----------------|---------|--------------|---------|
| Earnings beat | 0 | — | — |
| Upgrade analyste | 0 | — | — |
| Insider buying | 0 | — | — |
| Short squeeze | 0 | — | — |
| Macro favorable | 0 | — | — |
| Breakout technique | 0 | — | — |
| Flux 13F accumulation | 0 | — | — |
| Unusual options activity | 0 | — | — |

### Par cause racine d'erreur (post-mortems)
| Cause racine | Occurrences | % des Misses | Règle corrective active |
|-------------|------------|--------------|------------------------|
| Macro ignorée | 0 | — | Non |
| Catalyseur surévalué | 0 | — | Non |
| Analyste peu fiable | 0 | — | Non |
| Force relative ignorée | 0 | — | Non |
| Timing erroné | 0 | — | Non |
| Risque non modélisé | 0 | — | Non |
| Valorisation agressive | 0 | — | Non |
| Qualité bénéfices | 0 | — | Non |
| Short interest ignoré | 0 | — | Non |

---

## Alertes de calibration

| Condition | Action |
|-----------|--------|
| Win rate J+20 < 50% sur 20 derniers signaux | Révision globale du scoring + relecture de APPRENTISSAGES.md |
| Win rate J+20 > 70% sur 20 derniers signaux | Documenter les patterns gagnants dans APPRENTISSAGES.md (section bonus) |
| 3 misses consécutifs sur même type de catalyseur | Post-mortem groupé + pénalité −0.5 pt sur ce type |
| 3 hits consécutifs sur même type de catalyseur | Bonus +0.3 pt empirique, noter dans APPRENTISSAGES.md |
| Score > 8 mais miss systématique | Hypothèses de valorisation trop optimistes — réviser DCF defaults |
| Même cause racine dans ≥ 3 post-mortems | Règle corrective à "Forte confiance" — appliquer systématiquement |
| Règle active depuis 3 mois sans impact mesurable | Réévaluer ou supprimer la règle |

---

## Signaux en cours de suivi

| Ticker | Date signal | Score | Cours signal | J+5 prévu | J+20 prévu | J+60 prévu | Statut |
|--------|------------|-------|-------------|----------|-----------|-----------|--------|
| — | — | — | — | — | — | — | — |