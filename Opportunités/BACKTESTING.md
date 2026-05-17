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
| — | — | — | — | — | — | — | — | — |

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
| — | — | — | — | — | — |

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
| 9.0-10.0 | 0 | — | — | 0 |
| 8.0-8.99 | 0 | — | — | 0 |
| 7.0-7.99 | 0 | — | — | 0 |
| 6.0-6.99 | 0 | — | — | 0 |

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