# FUBO

## Thèse courante
**SURVEILLER** — Score Opportunité ajusté ~4,2/10 (plafonné Qualité 1/6 + malus sectoriel + liquidité critique + timing + earnings manquants), Score Global ajusté ~42/100 (2026-05-26 snapshot 17:00 UTC)

Thèse d'investissement : FUBO est un titre spéculatif du secteur Communication Services (streaming sportif live) avec un profil fondamental dégradé inchangé (Score Qualité 1/6, FCF négatif, current ratio 0,84, debt/equity 2,43, patrimoine net négatif −$398,9M). La divergence Yahoo/FMP persiste (market cap $281,4M vs ~$3,27B — ×11,6), rendant toute valorisation fiable impossible. Le snapshot 2026-05-26 (17:00 UTC) enregistre une **dégradation de la liquidité** : close **$9,56** (−1,95% vs previous), volume **517 593** (0,37× moyenne 20j), RSI **21,26** (survente extrême). Le scoring agent recule légèrement : Score Global **67,2/100** (ajusté **64,2/100**), Score Momentum **4,5/10** (−0,5 pt vs 13:00 UTC), action **ACHETER (Réduit, timing Défavorable)**. **Cependant**, l'ajustement analyste selon les règles Argus-IA ramène le Score Opportunité à **~4,2/10** (plafonnement Valorisation à 5/10 pour Qualité ≤ 3/6, malus sectoriel XLC bottom 3 −0,5 pt, malus liquidité critique 0,37× −0,5 pt, malus timing défavorable −0,3 pt, malus données earnings Q1 manquantes −0,5 pt), soit un Score Global **~42/100** — maintenant la recommandation en **SURVEILLER** (zone 35–49). Le setup short squeeze latent (short interest 22,84% + call OI dominant 62,3%) persiste, mais sans fondement qualitatif ni volume de suivi. Le max pain **$10,00** place le spot sous pression de pinning baissier (écart −4,4%) en échéance J+3 (2026-05-29). **Anomalie calendrier** : `upcoming_events_latest.json` place l'earnings au **2026-05-26** (jour J) — aucun résultat Q1 visible après 7 jours d'attente. **Pas de position longue recommandée.**

## Historique
| Date | Fichier | Type |
|------|---------|------|
| 2026-05-17 | [FUBO_2026-05-17_claude.md](FUBO_2026-05-17_claude.md) | Analyse approfondie (LLM) |
| 2026-05-17 | [FUBO_2026-05-17_preview.md](FUBO_2026-05-17_preview.md) | Preview pré-earnings |
| 2026-05-18 | [FUBO_2026-05-18_update.md](FUBO_2026-05-18_update.md) | Mise à jour post-pipeline 22:35 UTC — close final $9.38 (-2.49%), volume 0.62×, snapshot stable vs 21h UTC, earnings Q1 en attente, thèse ATTENDRE confirmée |
| 2026-05-18 | [FUBO_2026-05-18_init.md](FUBO_2026-05-18_init.md) | FULL REFRESH — ATR_SPIKE 8,53%, thèse confirmée ATTENDRE (close final $9.38) |
| 2026-05-18 | [FUBO_2026-05-18_preview.md](FUBO_2026-05-18_preview.md) | Preview pré-earnings |
| 2026-05-20 | [FUBO_2026-05-20_update.md](FUBO_2026-05-20_update.md) | Mise à jour snapshot 13:00 UTC — close stable $9.20 (−1.92%), volume 1 035 600 (0.69×), RSI 32.26 inchangé, **anomalie options RÉSOLUE** (max pain $10.00, put/call 0.59, call OI 62.9%), earnings Q1 JOUR J toujours non résolus, thèse ATTENDRE confirmée |
| 2026-05-19 | [FUBO_2026-05-19_update.md](FUBO_2026-05-19_update.md) | Mise à jour snapshot final 21:00 UTC — close $9.20 (−1.92% session), volume corrigé à 945 778 (0.63×), RSI 32.26 proche survente, earnings Q1 JOUR J toujours non observables, thèse ATTENDRE confirmée |
| 2026-05-20 | [FUBO_2026-05-20_init.md](FUBO_2026-05-20_init.md) | FULL REFRESH — ATR_SPIKE 8.48%, thèse confirmée ATTENDRE (close stable $9.20, volume 0.69×, anomalie max pain $21.00 vs $10.00 historique, earnings Q1 JOUR J non résolus) |
| 2026-05-19 | [FUBO_2026-05-19_init.md](FUBO_2026-05-19_init.md) | FULL REFRESH — ATR_SPIKE 8.48%, thèse confirmée ATTENDRE (snapshot final $9.20, volume 0.63×) |
| 2026-05-25 | [FUBO_2026-05-25_update.md](FUBO_2026-05-25_update.md) | Mise à jour snapshot 13:00 UTC — **données stables** vs 10:00 UTC (close $9.75, RSI 20.19, max pain $9.00 inchangés), scoring agent stable ACHETER Réduit (65.5/100), ajustement analyste maintient SURVEILLER (~52/100), fondamental dégradé 1/6, earnings Q1 toujours non résolus. DRAFT_refresh archivé (triggers déjà couverts) |
| 2026-05-25 | [FUBO_2026-05-25_update.md](FUBO_2026-05-25_update.md) | Mise à jour snapshot **17:00 UTC** — **stabilité totale** vs 13:00 UTC (marché fermé Memorial Day), toutes les métriques inchangées, anomalie calendrier earnings détectée (FMP place l'earnings au 2026-05-25, jour J, mais aucun résultat visible), thèse SURVEILLER confirmée, DRAFT_refresh (17:00) archivé |
| 2026-05-25 | [FUBO_2026-05-25_update.md](FUBO_2026-05-25_update.md) | Mise à jour snapshot **21:00 UTC** — **stabilité totale** vs 17:00 UTC (marché fermé Memorial Day), 12e snapshot consécutif identique (close $9.75, RSI 20.19, max pain $9.00), earnings Q1 J=0 non résolu après 5 jours d'attente, thèse SURVEILLER confirmée |
| 2026-05-26 | [FUBO_2026-05-26_update.md](FUBO_2026-05-26_update.md) | Mise à jour snapshot **13:00 UTC** — stabilité totale vs 10:00 UTC (pre-market), **anomalie options JSON RÉSOLUE** (max pain $10.00, put/call 0.60, call OI 62.3%) — valeurs cohérentes remplaçant l'artefact 10:00 UTC, max pain remonté au-dessus du spot (pinning baissier J+3), earnings Q1 J=0 non résolu après 7 jours, thèse SURVEILLER confirmée |
| 2026-05-26 | [FUBO_2026-05-26_update.md](FUBO_2026-05-26_update.md) | Mise à jour snapshot **17:00 UTC** — cours **$9.56** (−1.95%), **volume effondré à 0.37×** (517k vs moy. 20j 1.41M), RSI 21.26 survente extrême, max pain $10.00 pinning baissier intensifié (−4.4%), momentum agent retrait à 4.5/10, Score Global ajusté agent 64.2/100, ajustement analyste **SURVEILLER (~42/100)** sur base liquidité critique + earnings Q1 J=0 non résolu après 7 jours |

## Agenda
- **Earnings Q1 2026 :** anomalie calendrier — `upcoming_events_latest.json` (2026-05-25) place l'earnings au **2026-05-25** (jour J, `days_until: 0`) alors que le marché est fermé Memorial Day. Aucun résultat (EPS, revenue, guidance) n'est visible dans `data/latest.json` au snapshot 17:00 UTC. **Vérification impérative à la réouverture du marché (2026-05-26).**
- Échéance options : 2026-05-29 (J+4 — max pain $9,00, put/call 0,65, call OI 60,6%)
- Prochaine échéance earnings Q2 : ~août 2026

## Alertes actives
- **PRICE_GAP** (medium) — Gap +6.67% overnight (seuil ±5.0%) — 2026-05-25
- **ATR_SPIKE** (medium) — ATR relatif 6,46% (seuil 5,0%) — persistant depuis 2026-05-17
- **RSI SURVENTE EXTRÊME** — RSI 20.19 (seuil 30) — 2026-05-25
- **Earnings Q1 2026 en attente** — anomalie calendrier : `upcoming_events_latest.json` place l'earnings au **2026-05-26** (jour J), mais aucun résultat visible dans `data/latest.json` au snapshot 10:00 UTC — vérification impérative au prochain snapshot
- **Divergence Yahoo/FMP Market Cap** — ×11,4 d'écart entre sources ($287,0M vs ~$3,27B)
- **Sector Rotation XLC Bottom 3** — malus sectoriel actif (snapshot 2026-05-26 : momentum score 0.0 / 10)
- **Options Spot/Max Pain Divergence** — spot $9.75 vs max pain confirmé $9.00 (écart +8.3%) ; call OI dominant 60,6%
- **Anomalie Options JSON RÉSOLUE** — snapshot 2026-05-26 13:00 UTC retourne max_pain $10.00, put/call 0.60, call OI 62.3% (valeurs cohérentes remplaçant l'artefact 10:00 UTC) ; max pain au-dessus du spot = pinning baissier J+3
- **Liquidité réduite** — volume 0.75× moyenne 20j (1,10M vs 1,46M) — risque de slippage majeur
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif
- **Short Squeeze Setup (latent)** — short interest 22,84% + call OI dominant 60,6% = risque de squeeze technique si catalyseur positif
