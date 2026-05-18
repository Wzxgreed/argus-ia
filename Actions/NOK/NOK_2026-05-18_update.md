# NOK — Mise à Jour Quotidienne (2026-05-18 22:34 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Communication Equipment / 5G Infrastructure
> Date analyse : 2026-05-18 | Données source : `data/latest.json` (snapshot 2026-05-18T22:35 UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-18 21:00 UTC)

| Indicateur | Update 21:00 UTC | Snapshot 22:35 UTC | Variation | Signal |
|-----------|-----------------|-------------------|-----------|--------|
| Cours close | $13.74 | **$13.74** | $0.00 | Stable |
| RSI 14j | 64.63 | **64.63** | 0.00 pt | Inchangé — zone saine |
| ATR 14j | $0.97 | **$0.97** | $0.00 | Volatilité stable |
| Volume relatif | 0.70× | **0.70×** | 0.00× | Liquidité inchangée, reste faible |
| MM 50j | $10.29 | $10.29 | $0.00 | Support structurel stable |
| P/E (TTM) | 85.875 | **85.875** | 0.000 pt | Multiple inchangé |
| Forward P/E | 28.32 | **28.32** | 0.00 pt | Attente de normalisation inchangée |
| P/B | 3.093 | **3.093** | 0.000 | Stable |
| Premium vs consensus $9.26 | +48.4 % | **+48.4 %** | 0.0 pp | Surévaluation persistante |
| Short interest | 0.012 % | 0.012 % | 0.0 pp | Pression short nulle |
| Dividend yield | 1.17 % | 1.17 % | 0.0 pp | Rendement inchangé |

**Événement majeur du snapshot 22:35 UTC :** aucun événement corporate détecté (`events_latest.json` vide pour NOK). Aucune news structurante post-21:00 UTC, aucun mouvement d'options ou d'insiders. Le cours de clôture est confirmé à **$13.74** (repli de **−1.51 %** vs la clôture précédente à $13.95).

**Trigger technique :** `ATR_SPIKE` (medium) — ATR relatif 7.06 % (seuil 5.0 %). Évalué comme un **faux positit technique** : aucune rupture de support, pas de gap, fondamentaux inchangés. La volatilité reflète le range intraday ($13.50–$14.48) sur une liquidité réduite, pas un changement de régime. Les DRAFT_refresh générés par ce trigger sont archivés comme non matérialisés (voir `REFRESH_LOG.md`).

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Cours close | $13.74 | −1.51 % vs clôture précédente ($13.95) ; stable vs snapshot 21:00 UTC |
| RSI 14j | 64.63 | Zone saine, légèrement sous le seuil 70 |
| ATR 14j | $0.97 | 7.06 % du cours — volatilité marginale, au-dessus de la moyenne historique |
| MM 50j | $10.29 | Cours +33 % au-dessus du support structurel |
| MM 200j | N/A | Non disponible |
| Volume | 87,856,439 | **0.70× moyenne 20j (124,783,956)** — liquidité faible, pas d'accélération |
| Beta | 0.765 | Faible sensibilité au marché |

**Niveaux clés :**
- Support immédiat : $11.80 (cours − 2×ATR)
- Support structurel : MM50 à $10.29
- Résistance 52 semaines : $15.19 (+10.7 %)
- Max pain options : $15.00 (expiration 2026-05-22) — aligné sur l'historique NYSE

**Verdict timing :** **Favorable** (cours > MM50) mais le volume réduit (0.70×) et l'absence de catalyseur acheteur en fin de séance limitent la conviction.

**Score Momentum :** 6.5/10 — inchangé. Cours au-dessus de la MM50, RSI dans la zone saine, mais le volume faible et l'absence de catalyseur limitent la conviction.

---

## 3. Mise à Jour Fondamentale

### Données de valorisation (Yahoo Finance — ADR NYSE)

| Multiple | Valeur | Contexte |
|----------|--------|----------|
| Market Cap | $76.7 B | Stable vs snapshot 21:00 |
| P/E (TTM) | 85.875 | 🔴 Extrêmement élevé |
| Forward P/E | 28.32 | Élevé mais reflète attente de normalisation EPS |
| EV/EBITDA | 29.80 | Premium sectoriel |
| P/B | 3.093 | Premium vs book |
| Dividend yield | 1.17 % | Support de rendement |

**Données opérationnelles FMP (FY 2025) :** inchangées vs snapshot 21:00. Ratios opérationnels : gross margin 43.5 %, operating margin 3.9 %, net margin 3.3 %, ROE indisponible, ROIC indisponible (fmp_ratios), ROIC 1.9 % (fmp_key_metrics), net cash (D/E 0.25, current ratio 1.58). Aucune donnée nouvelle ne modifie ce profil.

**Divergence Yahoo (ADR) vs FMP (sous-jacent) :** inchangée. Le consensus analystes ($9.26 sur 6 brokers) est calibré sur l'ADR, et le premium de +48.4 % reste l'ancrage de référence. Les multiples FMP (P/E 45.8, EV/EBITDA 13.1) reflètent le titre Helsinki et ne changent pas le verdict consensus ADR.

### Filtre Qualité (6 critères)

Aucune donnée nouvelle dans `data/latest.json` pour réviser le filtre qualité. Le dernier verdict connu reste **2.5/6 — 🔴 Hors périmètre compounding**. Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (operating margin 3.9 %, net margin 3.3 %) incompatible avec un profil compounding.

**Score Valorisation :** 3.5/10 — inchangé (premium +48.4 % vs consensus, P/E 86).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | `recommandations_latest.json` |
| Put/Call ratio | 0.34 | Yahoo Finance — léger biais call (74.6 % OI calls) |
| Max pain | $15.00 | Yahoo Finance — cohérent historique NYSE |
| Short interest | 0.012 % | Yahoo Finance — quasi nulle |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` — aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK |

**Upcoming events :**
- Earnings Q2 FY2026 confirmé au **2026-07-23** (dans **66 jours**)
- Estimates EPS : $0.06–$0.08 | Revenus : $4.8 B
- Pas de preview requis (≥ 30 jours)

**Score Catalyseur :** 4.0/10 — inchangé (aucun catalyseur nouveau ; earnings éloignés ; options biaisées calls sans conviction institutionnelle).

---

## 5. Scoring Global

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4.0/10 | 35 % | Aucun catalyseur ; earnings dans 66 jours |
| Valorisation | 3.5/10 | 40 % | Premium +48.4 % vs consensus ; P/E 86 |
| Momentum | 6.5/10 | 25 % | Cours > MM50 ; RSI 64.6 zone saine, volume faible |
| **Score Opportunité** | **4.4/10** | | Inchangé vs snapshot 21:00 |
| **Score Global** | **44.2** | | Inchangé |
| **Score Global Ajusté** | **49.2** | | Malus sectoriel marginal (XLC bottom 3) non matérialisé |

**Action recommandée :** **SURVEILLER** — Pas de position.

---

## 6. Niveaux et Ratio R/R

| Niveau | Valeur | Calcul |
|--------|--------|--------|
| Cours actuel | $13.74 | — |
| Stop-loss | $11.80 | $13.74 − 2×$0.97 |
| Take-profit | $16.65 | $13.74 + 3×$0.97 |
| Ratio R/R | **1.5 : 1** | Gain $2.91 / Perte $1.94 |

Niveaux inchangés vs snapshot 21:00 UTC. Le SL à $11.80 reste valide.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0 | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 0 | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Sector Rotation** | XLC bottom 3 | Headwind sectoriel marginal. RS 20j/60j négatif vs SPY. |
| **Agent FX Exposure** | Score 0.0/10 | Exposition 25 %, direction export USD. Divergence alignée. |
| **Agent Social Sentiment** | 0 mention | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |

---

## 8. Conclusion

**Thèse confirmée — SURVEILLER.**

Le snapshot 22:35 UTC confirme intégralement les lectures du snapshot 21:00 UTC. Le cours de clôture officiel est stable à $13.74 (repli −1.51 % vs clôture précédente $13.95) sur un volume inchangé et réduit (0.70× moyenne 20j). Le RSI (64.63) et l'ATR ($0.97) sont strictement inchangés. Aucun événement corporate, aucune news structurante, aucun mouvement d'options ou d'insiders n'est survenu post-21:00 UTC.

Les fondamentaux restent identiques : quality hors périmètre (2.5/6), rentabilité anémique (operating margin 3.9 %, net margin 3.3 %), bilan solide (net cash, D/E 0.25) mais insuffisant pour justifier un profil compounding. La divergence structurelle Yahoo/FMP sur les multiples persiste. Le consensus à $9.26 laisse un premium de +48.4 % qui continue de plafonner le score valorisation à 3.5/10.

Le trigger `ATR_SPIKE` (7.06 %) reste un **faux positit technique** : aucun gap, aucune rupture de support, aucun catalyseur. La volatilité relative reflète uniquement le range intraday ($13.50–$14.48) sur une liquidité réduite. Les DRAFT_refresh successifs générés par ce trigger sont archivés comme non matérialisés.

NOK reste un **value trap technique** : momentum de court terme soutenu par la MM50 ($10.29) mais valorisation dissuasive et qualité fondamentale hors périmètre. Le secteur Communication Services (XLC) reste dans le bottom 3 de la rotation sectorielle, ajoutant un headwind macro marginal.

**Prochain point de contrôle :** preview earnings si approche à ≤ 30 jours du 2026-07-23, ou sur franchissement technique du SL à $11.80.
