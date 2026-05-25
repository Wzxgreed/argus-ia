# FUBO

## Thèse courante
**SURVEILLER** — Score Opportunité ajusté ~5,2/10 (plafonné Qualité 1/6 + malus sectoriel + liquidité + timing), Score Global ajusté ~52/100 (2026-05-25 snapshot 10:00 UTC)

Thèse d'investissement : FUBO est un titre spéculatif du secteur Communication Services (streaming sportif live) avec un profil fondamental dégradé inchangé (Score Qualité 1/6, FCF négatif, current ratio 0,84, debt/equity 2,43, patrimoine net négatif −$398,9M). La divergence Yahoo/FMP persiste (market cap $287,0M vs ~$3,27B — ×11,4), rendant toute valorisation fiable impossible. Le snapshot 2026-05-25 affiche un **gap haussier +6,67%** à $9,75 sans catalyseur identifiable, accompagné d'une **survente extrême (RSI 20,19)** — configuration technique ambivalente. Le scoring agent livre un Score Global 65,5/100 et une action **ACHETER (Réduit, timing Défavorable)**, portée par un Catalyseur 8,0/10 et une Valorisation 7,0/10. **Cependant**, l'ajustement analyste selon les règles Argus-IA ramène le Score Opportunité à ~5,2/10 (plafonnement Valorisation à 5/10 pour Qualité ≤ 3/6, malus sectoriel XLC bottom 3 −0,5 pt, malus liquidité 0,75× −0,3 pt, malus timing défavorable −0,3 pt, malus données earnings Q1 manquantes −0,5 pt), soit un Score Global ~52/100 — maintenant la recommandation en **SURVEILLER**. Le max pain est corrigé à $9,00 (cohérent avec le spot monté), le put/call remonte à 0,65 (plus défensif), le call OI recule à 60,6% (−2,3 pp). Le setup short squeeze latent (short interest 22,84% + call OI dominant) persiste, mais sans fondement qualitatif. Le volume reste faible (0,75×). Les résultats Q1 2026 attendus le **2026-05-20** sont toujours non visibles au snapshot 2026-05-25 — retard API ou report probable. **Pas de position longue recommandée.**

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

## Agenda
- **Earnings Q1 2026 :** 2026-05-20 (JOUR J — résultats en attente de confirmation / publication post-close probable ou retard API)
- Échéance options : 2026-05-22 (J-1 — max pain crédible $10,00, put/call 0,65, call OI 60,6%)
- Prochaine échéance earnings Q2 : ~août 2026

## Alertes actives
- **ATR_SPIKE** (medium) — ATR relatif 8,5% (seuil 5,0%) — persistant depuis 2026-05-17
- **Earnings jour J en attente** — résultats Q1 2026 non visibles au snapshot 10:00 UTC 2026-05-20 → vérifier prochaine session impérativement
- **Divergence Yahoo/FMP Market Cap** — ×12,1 d'écart entre sources
- **Sector Rotation XLC Bottom 3** — malus sectoriel actif
- **Options Spot/Max Pain Divergence** — spot $9.20 vs max pain crédible $10.00 (écart 8.0%) à J-1 échéance 2026-05-22 ; call OI dominant 60,6%
- **Anomalie Data Quality Options** — max pain brut API $21.00 (incohérent vs historique $10.00) — signalé comme artefact data quality, non pris en compte dans le scoring
- **Liquidité réduite** — volume 0.69× moyenne 20j (1,04M vs 1,50M) — risque de slippage majeur
- **Qualité dégradée** — Score Qualité 1/6, patrimoine net négatif, FCF négatif
- **Short Squeeze Setup (latent)** — short interest 22,84% + call OI dominant + échéance imminente = risque de squeeze technique si catalyseur positif
