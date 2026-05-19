# ASTS — Mise à Jour Post-Pipeline (2026-05-19)

> Snapshot post-pipeline 13:00 UTC. Données de prix stables vs close 2026-05-18. **Correction majeure des données options** par rapport au snapshot 10:00 UTC — Max Pain révisé de $40.0 (artéfact) à $85.0, put/call ratio et call OI désormais disponibles.

---

## Résumé des Changements depuis l'Analyse Précédente

| Indicateur | Précédent (2026-05-18) | Actuel (2026-05-19) | Delta |
|-----------|------------------------|---------------------|-------|
| Cours | $86.83 | $86.83 | — |
| Change | +3.78% | +3.78% | — |
| RSI 14j | 60.85 | 60.85 | — |
| ATR 14j | $7.39 | $7.39 | — |
| Volume rel. | 1.21x | 1.26x | +0.05x |
| MM50 | $83.66 | $83.66 | — |
| MM200 | N/A | N/A | — |
| EV/Revenue | 300.69x | 311.81x | +3.7% |
| EV/EBITDA | -80.72 | -83.70 | -3.7% |
| **Max Pain** | **$90.00** | **$85.00** | **-5.6%** |
| **Put/Call Ratio** | **0.58** | **0.59** | **+0.01** |
| **Call OI %** | **63.40%** | **63.00%** | **-0.4pp** |
| Score Opportunité | 5.5/10 | 5.5/10 | — |
| Score Global | 54.8 | 54.8 | — |

**Verdict :** aucun changement de prix ni de métrique technique vs l'analyse précédente. Volume relatif révisé à la hausse (+1.26x). Multiples fondamentaux révisés marginalement (EV/Revenue +3.7%). **Données options corrigées** : Max Pain $85.0 (cohérent avec le cours, vs $40.0 artéfact du snapshot 10:00 UTC), put/call 0.59 et call OI 63% confirmés. Thèse inchangée.

---

## Mise à Jour Technique

- **RSI 14j :** 60.85 — zone neutre haussière, sous le seuil de surachat (70)
- **ATR 14j :** $7.39 (ATR relatif 8.51% du cours) — **[TRIGGER MEDIUM]** ATR_SPIKE persistant (seuil 5.0%). Volatilité intraday élevée : range $81.83–$89.96 (~9.3%)
- **MM50 :** $83.66 — cours +3.8% au-dessus, support dynamique intact
- **MM200 :** N/A — croisement non confirmable
- **Volume :** 24.96M vs moy. 20j 19.78M (+26.2%) — volume supérieur à la moyenne confirme l'intérêt
- **Supports clés :** MM50 $83.66 ; low intraday $81.83
- **Résistances clés :** Max Pain options $85.0 ; 52W high $129.89
- **Timing verdict :** Favorable (tendance haussière court terme au-dessus MM50, RSI neutre)
- **Score Momentum :** 7.0/10 — inchangé

---

## Mise à Jour Fondamentale

Aucune nouvelle donnée comptable ni revision d'estimations depuis l'analyse précédente.

- **Market Cap :** $33.7B
- **Forward P/E :** -292.23 (profil non rentable)
- **EV/EBITDA :** -83.70
- **EV/Revenue :** 311.81x — multiple spéculatif extrême, en légère hausse
- **P/B :** 12.46x
- **Beta :** 2.60 — sensibilité au marché très supérieure à la moyenne
- **Short Interest :** 0.18% (très faible)
- **Consensus analystes :** Price target moyen $92.25 (10 analystes, 4 couverts le mois dernier) — upside +6.3% vs cours actuel
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, données comptables détaillées (M-Score, Z-Score, F-Score, Sloan) non disponibles dans le snapshot

**Risque sectoriel :** ASTS est classé dans Communication Equipment. L'Agent Sector Rotation place XLC (Communication Services) dans le **bottom 3** des secteurs (momentum score 0.0), bien que XLK (Technology) soit en tête du classement (momentum 10.0). Cette divergence au sein du secteur tech/communication renforce la prudence sur le positionnement relatif d'ASTS.

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** [DONNÉES MANQUANTES] — pas d'upgrade/downgrade signalé dans le pipeline
- **Options :** Max Pain **$85.0** (vs $90.0 le 18 mai, corrigé du snapshot 10:00 UTC qui affichait $40.0 artéfact). Put/Call Ratio **0.59** ; Call OI **63.0%** — positionnement call dominante, sentiment options haussier modéré. Nearest expiry : **2026-05-22 (3 jours)**. Le cours actuel $86.83 est à +2.2% du Max Pain $85.0 : pinning autour de $85 possible à l'approche de l'expiration.
- **Social Sentiment :** 0 mention Reddit ; Score 0.0/10 (no data) ; Pump detected : False
- **Event-Driven :** aucun événement corporate (M&A, buyback, activism, guidance change) détecté pour ASTS
- **Géopolitique :** ASTS non flaggé dans geo_risk_latest.json (score politique faible ou nul)
- **FX Exposure :** Exposition 25%, direction export, devise principale USD. FX Impact Score 0.0/10 — impact neutre

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+83) — Est. EPS $-0.29 à $-0.17, Revenus $0.0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-05-22** (J+3) — Max Pain $85.0, call OI dominante

---

## Scoring Global — Post-Pipeline

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 5.5/10 | 35% | Aucun catalyseur imminent, earnings dans 83j |
| Valorisation | 4.5/10 | 40% | Multiples spéculatifs extrêmes, profil non rentable |
| Momentum | 7.0/10 | 25% | Cours > MM50, RSI neutre haussier, volume élevé |
| **Score Opportunité** | **5.5/10** | | |

**Malus / Bonus appliqués :**
- Malus sectoriel (XLC bottom 3) : contexte défavorable pour le sous-secteur communication
- Malus ATR_SPIKE : volatilité intraday élevée (8.51% du cours), élargit le risque de stop
- Aucun malus comptable (données indisponibles)
- Aucun malus géopolitique
- Aucun malus FX (score 0.0/10)
- Aucun bonus event-driven

**Score Global Composite :** 54.8/100 (ajusté 59.8)

---

## Niveaux et Ratio R/R — Validés

- **Cours actuel :** $86.83
- **Stop-loss :** $72.05 (cours − 2×ATR = $86.83 − $14.78)
- **Take-profit :** $109.00 (cours + 3×ATR = $86.83 + $22.17)
- **Ratio R/R :** 1.5:1

**Révision :** niveaux inchangés. Le Max Pain corrigé à $85.0 est désormais cohérent avec le cours ($86.83, +2.2%). Le SL à $72.05 reste sous le low intraday du jour ($81.83) et la MM50 ($83.66). Le pinning autour de $85 à l'expiration du 22 mai est un risque à surveiller mais n'impacte pas les nivements de SL/TP.

---

## Conclusion

**Thèse confirmée : ATTENDRE**

L'analyse post-pipeline du 2026-05-19 (snapshot 13:00 UTC) confirme intégralement la thèse. La correction des données options (Max Pain $85.0, put/call 0.59, call OI 63%) valide le positionnement call dominante et le risque de pinning à l'expiration du 22 mai. Aucun nouvel élément fondamental, technique ou sentiment n'oblige à réviser le verdict. Le profil reste celui d'une valorisation spéculative extrême (EV/Revenue 312x) sur un business non rentable (EPS estimé négatif), avec un momentum technique favorable mais insuffisant pour compenser le risque de valorisation.

**Points de vigilance :**
1. **Expiration options 2026-05-22 (J+3)** — Max Pain $85.0, call OI dominante (63%). Le cours $86.83 est proche du Max Pain : un pinning autour de $85 est plausible. Risque de compression du gamma
2. **ATR_SPIKE** — volatilité intraday élevée persistante (8.51%), risque de whipsaw accru
3. **Multiples révisés à la hausse** — EV/Revenue +3.7% à 311.8x, renforçant le caractère spéculatif
4. **Secteur Communication Services** — bottom 3 du classement sectoriel (momentum 0.0)

**Prochaines étapes :**
- Surveiller le comportement autour du Max Pain $85 à l'approche de l'expiration du 22 mai
- Revoir le scoring si earnings preview à générer (dans ~80j)
- Attendre une correction vers MM50 ($83.66) ou mieux pour améliorer le ratio R/R avant toute entrée

---

*Généré par le système Argus-IA — Snapshot 2026-05-19 13:00 UTC*
