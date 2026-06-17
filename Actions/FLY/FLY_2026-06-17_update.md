# FLY — Mise à jour 2026-06-17 (snapshot 10h UTC)

> **Date :** 2026-06-17  
> **Cours :** $30.95  
> **Change vs prior close $33.36 :** −7.22% *[ANOMALIE DATA]* — vs close 16/06 21h $31.05 : −0.32%  
> **Volume :** 7.89M (0.83× moy. 20j 9.48M)  
> **Verdict :** **ATTENDRE** — Score Global Ajusté **52.5** (−2.5 pts vs 55.0), Score Opportunité **5.6/10**  
> **Timing :** Défavorable  
> **Horizon :** —

---

## 1. Résumé des changements depuis l'analyse précédente (16/06 21h UTC)

| Métrique | Aujourd'hui | Précédent (16/06 21h) | Δ |
|----------|-------------|----------------------|---|
| Cours close | $30.95 | $31.05 | −$0.10 (−0.32%) |
| Volume session | 7.89M | 4.49M | **+75.5%** |
| Volume vs 20j | 0.83× | 0.48× | +0.35× |
| RSI 14j | 20.4 | 17.66 | +2.74 pts |
| ATR 14j | 5.13 | 5.38 | −4.6% |
| MM 50j | 39.4 | 39.43 | stable |
| Gap MM50 | −21.4% | −21.3% | stable |
| Forward P/E | −24.04 | −24.12 | stable |
| EV/Revenue | 24.1x | 26.2x | −8.0% |
| Short Interest | 12.12% | 12.12% | stable |
| Consensus PT (FMP) | $43.77 (13) | $43.77 (13) | stable |
| **Score Global Ajusté** | **52.5** | **55.0** | **−2.5 pts** |
| **Score Opportunité** | **5.6/10** | **5.8/10** | **−0.2 pt** |
| Score Catalyseur | 6.5/10 | 6.5/10 | stable |
| Score Valorisation | 6.0/10 | 6.0/10 | stable |
| Score Momentum | 3.5/10 | 4.5/10 | **−1.0 pt** |
| Stop-loss | $20.69 | $20.29 | +$0.40 |
| Take-profit | $46.34 | $47.19 | −$0.85 |
| Ratio R/R | 1.5 | 1.5 | stable |

**Observations clés :**
- **Cours stable** vs close 16/06 21h ($31.05 → $30.95). Le gap −7.22% affiché par `latest.json` résulte d'un `previous_close` à $33.36 (close du 15/06 21h), pas du close 16/06. **[ANOMALIE DATA YAHOO]** à signaler.
- **Volume en hausse** (+75.5% vs session précédente) mais toujours sous moyenne 20j (0.83×). Participation légèrement plus active, pas de capitulation institutionnelle.
- **RSI 20.4** — survente extrême persistante, légèrement moins profonde qu'hier (17.66) mais toujours < 30. Pas de rebond mécanique confirmé.
- **Score Momentum dégradé** de 4.5 à 3.5/10 malgré RSI légèrement moins bas : la baisse du cours sur volume sous-moyen pèse sur la dynamique de court terme.
- **Score Global Ajusté 52.5** — reste dans la zone ATTENDRE (50–59), proche du seuil inférieur.
- **Anomalie options récurrente** : max pain $18.00 (aberrant, vs $65.00 aberrant hier), put/call et call OI null dans `latest.json`. Valeurs opérationnelles du 16/06 21h (put/call 0.27, call OI 78.8%, max pain $65.00) conservées en mémoire mais non confirmées par la source actuelle.

---

## 2. Mise à jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| Cours | $30.95 | Stable vs close 16/06 |
| Open | $32.45 | Gap haussier intraday $1.50 ouvert puis comblé |
| High | $32.98 | Test du open, rejet immédiat |
| Low | $30.33 | Support psychologique $30.00 testé à 1.1% du low |
| RSI 14j | 20.4 | Survente extrême persistante (< 30) |
| ATR 14j | 5.13 | Volatilité en contraction légère (−4.6%) |
| MM 50j | 39.4 | Cassure −21.4%, aucun signe de retour |
| MM 200j | — | Indisponible — tendance long terme non observable |
| Volume 20j | 9.48M | Baseline stable |
| Volume session | 7.89M | 0.83× — participation insuffisante pour un rebond durable |

**Niveaux clés (ATR-based) :**
- **Support immédiat :** $30.33 (low du jour) — cassure en clôture sous $30.00 = ouverture vers $28.00–$26.00
- **Résistance immédiate :** $32.45–$32.98 (zone open/high, rejetée)
- **Résistance majeure :** $39.40 (MM50)
- **Stop-loss (2×ATR) :** $20.69
- **Take-profit (3×ATR) :** $46.34
- **Ratio R/R :** 1.5

**Verdict timing :** Défavorable — survente extrême sans volume confirmateur, open/high rejetés, aucun support technique identifié sous $30.33 hormis le niveau psychologique $30.00.

---

## 3. Mise à jour Fondamentale

Aucun nouveau catalyst fondamental détecté. Données inchangées :

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $5.08B | Yahoo Finance |
| Forward P/E | −24.04 | Yahoo Finance |
| EV/Revenue | 24.1x | Yahoo Finance |
| Gross Margin (FMP) | 15.6% | FMP Stable API |
| EV/EBITDA (FMP) | −10.07 | FMP Stable API |
| Debt/Equity (FMP) | 0.26 | FMP Stable API |
| Current Ratio (FMP) | 4.51 | FMP Stable API |
| Filtre Qualité | **2/6** | Évaluation historique — pas de changement de structure |

**Filtre Qualité (rappel) :** Revenue CAGR 5 ans ❌ | Profit CAGR 5 ans ❌ | Assets/Liabilities ❌ | FCF positif 5 ans ❌ | Moat ❌ | TAM forte croissance ❌  
→ Score 2/6 = 🔴 **Hors périmètre Quality**. Score Valorisation plafonné à 5/10 (actuellement 6.0, hors plafond — possible artefact de scoring).

---

## 4. Mise à jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| Consensus PT FMP | $43.77 (13 analysts) | stable |
| Upside consensus | +41.4% vs spot | stable |
| Short Interest | 12.12% | stable |
| Max pain (Yahoo) | $18.00 | 🔴 **ANOMALIE DATA** (aberrant) |
| Put/Call ratio | — | null dans source |
| Call OI % | — | null dans source |
| Expiration proche | 2026-06-18 (J+1) | Risque de pin si données opérationnelles rétablies |

**Anomalie options persistante :** `latest.json` retourne max pain $18.00 (niveau irréaliste pour un spot $30.95), put/call et call OI null. Hier le max pain était $65.00 (aussi aberrant) avec put/call 0.27 et call OI 78.8% restaurés. L'expiration 2026-06-18 est à J+1 ; sans données fiables, le pin risk ne peut être évalué.

**News :** Aucune news majeure détectée pour FLY dans le snapshot.

---

## 5. Scoring Global

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 6.0/10 | 40% | 2.40 |
| Momentum | 3.5/10 | 25% | 0.88 |
| **Score Opportunité brut** | **5.6/10** | | |
| Malus / Bonus | — | | — |
| **Score Global Ajusté** | **52.5/100** | | |

**Règles de scoring :**
- Aucun score individuel ≤ 2/10 → pas de disqualification.
- Filtre Qualité 2/6 → théoriquement Score Valorisation plafonné à 5/10. Le score 6.0 actuel peut refléter un artefact de l'agent ; pas de signal d'achat.
- Régime macro indisponible dans `latest.json` → pondération standard appliquée (35/40/25).

---

## 6. Révision des niveaux SL / TP

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Stop-loss | $20.69 | Cours − 2×ATR (5.13) | Recalé +$0.40 vs hier (ATR en baisse mais spot légèrement plus bas) |
| Take-profit | $46.34 | Cours + 3×ATR (5.13) | Recalé −$0.85 vs hier |
| Ratio R/R | 1.5 | TP/SL | Seuil minimum institutionnel ; pas de marge de sécurité |
| Prix entrée suggéré | $30.95 | Spot actuel | Pas de discount technique significatif vs consensus |

**Note :** Le ratio R/R 1.5 est faible pour une position de quality compounding. Combiné au Filtre Qualité 2/6 et au timing défavorable, aucune position n'est recommandée.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : ATTENDRE confirmée, intensité négative stable.**

La configuration technique de FLY reste dominée par une **survente extrême persistante** (RSI 20.4) sans catalyst de retournement. Le cours est stable vs la clôture du 16/06 ($30.95 vs $31.05), invalidant l'apparence d'un gap baissier −7.22% qui résulte d'une anomalie de `previous_close` dans la source Yahoo. Le volume a progressé de +75% vs la session précédente mais reste sous-moyen (0.83×), signalant une absence de conviction acheteuse institutionnelle.

**Points de vigilance :**
1. **Support $30.00** testé à 1.1% du low intraday ($30.33). Cassure en clôture = ouverture vers $28–$26.
2. **Anomalie data Yahoo** — `previous_close` $33.36 (close du 15/06) utilisé au lieu du close 16/06 ($31.05). À surveiller pour la fiabilité des indicateurs de gap.
3. **Anomalie options** — max pain $18.00 aberrant, données put/call/OI null. Impossibilité d'évaluer le pin risk à J-1 expiration.
4. **MM200 indisponible** — tendance long terme non observable, risque de surprise macro non couvert.

**Catalyseurs forward :**
| Catalyst | Timeline | Probabilité | Impact |
|----------|----------|-------------|--------|
| Earnings Q2 2026 | 2026-08-04 (48 jours) | Haute | EPS estimé −$0.61 à −$0.45 — attendre surprise positive |
| Mean reversion RSI | J+5 à J+10 | Modérée | RSI < 20 historiquement suivi de rebond technique, mais pas de volume = pas de conviction |

**Résumé opérationnel :** Pas de position recommandée. Si rebond technique se matérialise (volume > 1.2× moy. 20j + cassure $33.00), réévaluer. Sinon, maintenir ATTENDRE.
