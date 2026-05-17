# Workflow de Revue Hebdomadaire

**Fréquence :** Chaque lundi matin, avant le bulletin quotidien
**Durée estimée :** 20-30 minutes de travail agent
**Commande :** `Lance la revue hebdomadaire du portefeuille et de la watchlist`

> Ce workflow complète les bulletins quotidiens par une vue de plus long terme.
> Il garantit que le système ne reste pas bloqué dans l'urgence quotidienne et maintient la cohérence stratégique de l'ensemble du portefeuille.

---

## Séquence hebdomadaire — 6 phases

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE H0 — MÉMOIRE & SUIVI (5 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Lire Agents/APPRENTISSAGES.md (règles actives + nouvelles règles de la semaine)
2. Vérifier les 3 fichiers de suivi pour toutes les fenêtres à clôturer :
   → Opportunités/BACKTESTING.md (J+5, J+20, J+60)
   → Actions/SUIVI_PRIX_CIBLES.md (J+30, J+90, J+180)
   → Actions/SUIVI_EARNINGS_PREDICTIONS.md (résultats parus la semaine dernière)
3. Pour chaque fenêtre échue : récupérer cours via `quote` + enregistrer verdict
4. Déclencher les post-mortems si Miss ou Imprécis détectés

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE H1 — PORTEFEUILLE (5 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. Lire Portefeuille/POSITIONS.md
6. Pour chaque position ouverte :
   a. Récupérer le cours actuel via `quote`
   b. Calculer P&L actualisé + P&L en % depuis entrée
   c. Recalculer l'ATR 14j via `technicalIndicators`
   d. Réviser le stop-loss ATR = cours actuel − 2×ATR (ou cours d'achat si plus favorable)
   e. Vérifier si le stop-loss actuel est cohérent avec le nouveau niveau ATR
7. Mettre à jour POSITIONS.md avec les stops révisés + P&L du jour
8. Si une position est en perte > 15% → déclencher automatiquement un _update.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE H2 — RISQUE PORTEFEUILLE (5 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. Lire Portefeuille/MODULE_RISQUE_PORTEFEUILLE.md
10. Recalculer la matrice de corrélation (30j) via CORRELATIONS_WATCHLIST.md
11. Identifier les paires sur-corrélées (> 0.7) avec exposition > 25%
12. Calculer la concentration sectorielle / factorielle actuelle
13. Effectuer les 7 stress tests (lire les résultats précédents pour tracking)
14. Calculer la VaR hebdomadaire
15. Si VaR > 8% du portefeuille → alerte + recommandation de réduction

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE H3 — WATCHLIST & PRIX CIBLES (5 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
16. Recalculer la matrice de corrélations (CORRELATIONS_WATCHLIST.md)
17. Mettre à jour WATCHLIST_SCORES.md :
    → Recalculer les 3 scores pour chaque ticker (depuis les derniers _update.md)
    → Mettre à jour le prochain catalyseur
    → Identifier les tickers dont le score a le plus évolué cette semaine
18. Pour chaque prix cible en cours dans SUIVI_PRIX_CIBLES.md :
    → Le consensus analyste a-t-il changé cette semaine ?
    → Le cours a-t-il franchi un niveau technique important ?
    → Si oui → réviser le prix cible et créer un _update.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE H4 — CALENDRIER & PREVIEWS (3 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
19. Lire Actualités/CALENDRIER_EARNINGS.md
20. Identifier les earnings des 7 prochains jours
21. Pour chaque ticker watchlist avec earnings dans ≤ 5 jours :
    → Vérifier si un _preview.md existe déjà
    → Si non → créer automatiquement [TICKER]_YYYY-MM-DD_preview.md
    → Enregistrer dans SUIVI_EARNINGS_PREDICTIONS.md
22. Lire Alertes/ALERTES.md → vérifier la pertinence des alertes actives
    → Supprimer les alertes obsolètes (position fermée, niveau hors de portée)
    → Ajouter les alertes composites pertinentes basées sur les configurations actuelles

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE H5 — RAPPORT HEBDOMADAIRE (5 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
23. Créer Actualités/Semaines/[YYYY-WXX].md avec :
    → Performance portefeuille sur la semaine (% vs S&P 500)
    → Top 3 et Flop 3 de la watchlist sur la semaine
    → Signaux importants détectés (supply chain, insiders, révisions)
    → Thème dominant de la semaine
    → Agenda de la semaine à venir (earnings, FOMC, data macro clés)
    → Patterns détectés dans PATTERNS_HISTORIQUES.md
24. Mettre à jour Portefeuille/PERFORMANCE.md avec les trades de la semaine
```

---

## Rapport hebdomadaire — Format standard

```markdown
# Revue Hebdomadaire — Semaine [W-XX] — Du [DATE] au [DATE]

## Performance portefeuille
| Métrique | Cette semaine | Depuis le début |
|----------|--------------|----------------|
| P&L total | +/-X% | +/-X% |
| vs S&P 500 | Alpha +/-X% | Alpha +/-X% |
| Positions actives | X | — |
| Drawdown max sur la semaine | X% | — |

## Watchlist — Mouvements notables
| Ticker | Perf. semaine | Score actuel | Variation score | Signal dominant |
|--------|--------------|-------------|----------------|----------------|
| | +/-X% | X/10 | +/- vs J-7 | |

**Top performer :** [TICKER] +X% — [Raison]
**Worst performer :** [TICKER] −X% — [Raison]

## Signaux supply chain détectés cette semaine
| Ticker | Entité | Événement | Impact estimé | Traité dans |
|--------|--------|-----------|--------------|-------------|
| | | | | _update.md |

## EPS Revision Momentum — Évolution hebdo
| Ticker | Solde révisions J-7 à J-0 | Tendance | Signal |
|--------|--------------------------|----------|--------|
| | | | |

## Alertes déclenchées ou approchées
| Ticker | Type | Statut | Action prise |
|--------|------|--------|-------------|
| | | 🔴 Déclenchée / 🟡 Proche | |

## Risque portefeuille
| Métrique | Valeur | Statut |
|----------|--------|--------|
| Corrélation max entre positions | X.X | 🟢/🟡/🔴 |
| Concentration sectorielle max | XX% | 🟢/🟡/🔴 |
| VaR 95% (7 jours) | -X% | 🟢/🟡/🔴 |

## Agenda de la semaine suivante
| Date | Ticker/Événement | Type | Impact attendu |
|------|-----------------|------|---------------|
| | | Earnings / FOMC / CPI / NFP | 🔴🟡🟢 |

## Patterns récurrents détectés
> [Lire PATTERNS_HISTORIQUES.md — y a-t-il une configuration actuelle similaire à une passée ?]

## Décision rebalancement (si applicable)
- [ ] Réduire position sur [TICKER] (raison : sur-corrélation / stop atteint / score dégradé)
- [ ] Renforcer position sur [TICKER] (raison : score en hausse / ATR favorable / catalyseur)
- [ ] Aucun rebalancement nécessaire
```

---

## Stop-loss ATR — Révision hebdomadaire

```
RÈGLE DE RÉVISION DES STOPS :

Pour chaque position ouverte :
→ ATR 14j actuel via `technicalIndicators`
→ Nouveau stop = MAX(cours d'achat × 0.90, cours actuel − 2 × ATR 14j)
   [on ne baisse jamais le stop, on ne le monte que si le cours monte]

TRAILING STOP (si position en profit > 20%) :
→ Stop trailing = cours actuel − 1.5 × ATR 14j (resserrement)
→ Permet de laisser courir les gains tout en protégeant

STOP FAST-TRACK (si position en profit > 50%) :
→ Stop trailing = cours actuel − 1 × ATR 14j (très serré)
→ Priorité à la protection des gains sur le potentiel résiduel
```

---

## Calendrier d'exécution

| Tâche | Fréquence | Priorité |
|-------|-----------|----------|
| Vérification fenêtres backtesting + prix cibles | Hebdomadaire (lundi) | 🔴 Critique |
| Révision stop-loss ATR | Hebdomadaire (lundi) | 🔴 Critique |
| Recalcul matrice corrélations | Hebdomadaire (lundi) | 🟡 Important |
| Mise à jour WATCHLIST_SCORES.md | Quotidien | 🔴 Critique |
| Calibration automatique des scores | Trimestriel | 🟡 Important |
| Révision des règles APPRENTISSAGES.md | Trimestriel | 🟡 Important |
| Génération _preview.md earnings | À 5 jours avant | 🔴 Critique |
| Rapport performance | Hebdomadaire (vendredi) | 🟢 Standard |
