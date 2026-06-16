# CTMX — Mise à Jour — Snapshot 2026-06-16 10h UTC

> **Société :** CytomX Therapeutics, Inc.
> **Secteur :** Healthcare / Biotechnology — Probody therapeutics
> **Exchange :** NASDAQ
> **Date :** 2026-06-16
> **Snapshot :** 10:00 UTC (pré-ouverture US)
> **Analyste :** Desk Argus-IA

---

## Résumé Exécutif

**Stabilité mécanique totale** vs snapshot 21h UTC 2026-06-15. Le **close reste à $3.04** sur le snapshot 10h UTC, avec l'ensemble des données techniques inchangées : RSI 25.93, ATR $0.18, MM50 $3.90, volume 0.87× moyenne 20j. Aucune mutation de cours, de momentum ou de structure n'est détectée sur ce snapshot pré-ouverture.

**Anomalie options JSON 6e occurrence** détectée et traitée : max pain $6.00 (aberrant, conservé à $4.00), put/call ratio 0.0 (aberrant, conservé à 0.14), call OI 100.0% (aberrant, conservé à 87.8%). L'expiration demain (2026-06-18) maintient le pin risk haussier vers $4.00.

**DRAFT_refresh classé faux positif** : le trigger `ATR_SPIKE` (5.92%) a été déclenché par `agents/detect_major_events/agent.py` mais l'ATR n'a pas muté ($0.18 stable vs snapshot précédent). Aucun événement majeur ne confirme, modifie ou invalide la thèse.

Le **Score Global Ajusté reste à 55.0/100** et le **Score Opportunité à 5.8/10** (C:6.5 V:6.0 M:4.5). La recommandation reste **ATTENDRE**. Le timing reste **Défavorable**.

---

## Changements depuis l'Analyse Précédente (Snapshot 2026-06-15 21h UTC)

### 1. Technique — Stabilité totale

| Indicateur | 15/06 21h UTC | 16/06 10h UTC | Signal |
|---|---|---|---|
| Cours close | **$3.04** | **$3.04** | **Inchangé** |
| Previous close | $3.01 | **$3.01** | — |
| Open / High / Low | 3.05 / 3.13 / 2.98 | **3.05 / 3.13 / 2.98** | Inchangé |
| Volume | 2,921,174 | **2,921,200** | **Stable** (diff. < 0.001%) |
| Volume rel. 20j | 0.87× | **0.87×** | **Inchangé** |
| RSI 14j | 25.93 | **25.93** | **Inchangé** — survente extrême persistante |
| ATR 14j | $0.18 | **$0.18** | **Inchangé** |
| MM 50j | $3.90 | **$3.90** | **Stable** |
| MM 200j | null | **null** | [DONNÉES PARTIELLES] |
| Short Interest | 14.97% | **14.97%** | **Stable** |
| 52W High / Low | $8.21 / $1.72 | **$8.21 / $1.72** | — |

**Verdict technique :** Aucune mutation technique. Le snapshot 10h UTC du 16/06 reproduit mécaniquement les données du close 21h UTC du 15/06 (pré-ouverture US). Le RSI à 25.93 reste en survente extrême. L'écart MM50 est stable à **−22.1%**. Le support $2.98 (low) n'a pas été retesté. Le timing reste **Défavorable** — position sous MM50 et tendance baissière persistante.

### 2. Options — Anomalie JSON 6e occurrence, valeurs opérationnelles conservées

| Indicateur | 15/06 21h UTC | 16/06 10h UTC (JSON brut) | Valeur conservée | Signal |
|---|---|---|---|---|
| Max Pain | $4.00 | **$6.00** | **$4.00** | Anomalie JSON 6e occurrence — valeur aberrante rejetée |
| Put/Call Ratio | 0.14 | **0.00** | **0.14** | Anomalie JSON — cohérence interne rejetée |
| Call OI % | 87.8% | **100.0%** | **87.8%** | Anomalie JSON — cohérence interne rejetée |
| Expiration proche | 2026-06-18 | **2026-06-18** | **Demain** (~1 jour) | Inchangé |

**Verdict options :** La structure options reste **très haussière** sur la base des valeurs opérationnelles conservées ($4.00 / 0.14 / 87.8%). L'anomalie JSON récurrente (max pain aberrant, put/call nul, call OI 100%) est un artefact de parsing sans impact sur l'interprétation. Le spot à $3.04 est sous le max pain $4.00 avec expiration demain — le pin risk haussier reste actif.

### 3. Fondamental — Aucun changement

Données FMP FY2025 inchangées. Pas de nouveau filing SEC, pas de guidance update, pas de nouvelles collaborations annoncées.

| Métrique | Valeur | Statut |
|----------|--------|--------|
| Market Cap (Yahoo) | **$661.8M** | Stable |
| Market Cap (FMP) | $587.6M | — |
| EV/Revenue | 8.946 (Yahoo) / 7.60 (FMP) | Élevé pour biotech pré-commercial |
| Forward P/E | −6.26 | Pertes attendues |
| Short Interest | **14.97%** | Stable |
| Current Ratio | 3.09 | Trésorerie confortable |
| Cash / Working Capital | $97.3M / $97.3M | Runway ~2–3 ans |
| Filtre Qualité | **2/6** | Hors périmètre (inchangé) |

**Consensus Analystes (FMP) :**
- Price target moyen : **$9.05** (+198% upside vs $3.04)
- Nombre d'analystes : **11** (1 ce mois, 4 ce trimestre)
- Sources : TheFly, StreetInsider, Benzinga

### 4. Sentiment / News / Social

| Indicateur | 15/06 21h UTC | 16/06 10h UTC | Signal |
|---|---|---|---|
| News pipeline | Aucune | **Aucune** | — |
| Social Sentiment | 0/10 | **0/10** | Aucun intérêt retail |
| Pump detection | Non | **Non** | — |

**Verdict sentiment :** Neutre à baissier. Aucune news, aucun intérêt retail. Le consensus analystes reste le seul soutien haussier structurel (PT +198%). Le short interest stable à 14.97% maintient le potentiel de short squeeze, mais aucun catalyseur déclencheur n'est visible.

---

## Contexte Sectoriel & Macro

| Facteur | Impact | Détail |
|---------|--------|--------|
| **XLV (Healthcare)** | Défensif | `data/sector_rotation_latest.json` (2026-06-16) : régime UNKNOWN, données RS non exploitables (NaN). XLV momentum_score 10.0 (artefact — pas de donnée réelle). |
| **Biotech spécifique** | Risque élevé | Sous-secteur biotech early-stage reste pénalisé. Pas de rotation sectorielle détectée. |
| **DXY / FX** | Neutre | `data/fx_exposure_latest.json` (2026-06-16) : CTMX exposure ~55% EUR/CNY, FX Impact Score **0.0** — aucun headwind/tailwind. |
| **Geo risk** | Non flaggé | `data/geo_risk_latest.json` (2026-05-17) : CTMX non présent, aucun risque géo détecté. |
| **Accounting risk** | Scan indisponible | `data/accounting_risk_latest.json` absent — pas de M-Score/Z-Score. |
| **Event-driven** | Aucun | `data/events_latest.json` (2026-06-16) : 0 événement corporate détecté pour CTMX. |
| **Earnings** | J+51 | Earnings confirmé le **2026-08-06** (Est EPS $−0.13 à $−0.07, Rev $0.0B). Pas de preview requis. |
| **Quant** | Calibration en cours | `data/quant_report_latest.json` (2026-05-17) : 0 signaux, p-value null — pas assez d'historique. |
| **Social Sentiment** | Aucun | `data/social_sentiment_latest.json` (2026-06-16) : CTMX 0 mentions, sentiment 0/10, pump non détecté. |
| **Validation** | OK | `data/validation_report.txt` (2026-06-16) : 0 CRITICAL, CTMX non concerné par les 5 errors / 2 warnings. |

---

## Scoring Global (Agents)

| Axe | Score | Pondération Régime Normal | Contribution | Justification |
|-----|-------|---------------------------|------------|---------------|
| Catalyseur | **6.5/10** | 35% | 2.28 | Pipeline Probody + partenariats majeurs. Structure options très haussière (call OI 87.8%) avec expiration demain — pin risk haussier. Volume normalisé (0.87×). |
| Valorisation | **6.0/10** | 40% | 2.40 | Biotech pré-profit, PT consensus +198% offre upside asymétrique. Plafonné par Filtre Qualité 2/6. |
| Momentum | **4.5/10** | 25% | 1.13 | RSI 25.93 survente extrême. Volume normalisé 0.87×, mais cours sous MM50 ($3.90, écart −22.1%) et tendance baissière persistante. |
| **Score Opportunité** | **5.8/10** | — | — | **Inchangé** vs snapshot 21h UTC 15/06 |
| **Malus** | | | −3.0 | Biotech pre-revenue + pertes (Filtre Qualité ≤ 3/6) |
| **Bonus** | | | +0.0 | Aucun bonus détecté |
| **Score Global** | **58.0/100** | | | Inchangé vs snapshot 21h UTC 15/06 |
| **Score Global Ajusté** | **55.0/100** | | | **Inchangé** — reste au-dessus du seuil institutionnel (50) |

**Action recommandée :** **ATTENDRE** *(inchangée)*
**Timing :** Défavorable *(inchangé)*
**Sizing :** — (pas de position recommandée)

**Note de fiabilité :** Score Global Ajusté 55.0/100 — au-dessus du seuil institutionnel. Aucune mutation technique ou fondamentale depuis le snapshot précédent. L'expiration options demain (2026-06-18) reste le catalyseur technique court terme le plus proche. Le DRAFT_refresh est un faux positif — pas de réécriture de thèse nécessaire.

---

## Révision des Niveaux SL / TP

Aucune révision nécessaire. SL/TP conservés sur base ATR $0.18 et close $3.04.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix de référence | **$3.04** | Close 2026-06-16 10h UTC |
| Stop-loss suggéré | **$2.68** | Cours ref − 2×ATR ($3.04 − $0.36) — aligné avec agent Recommandation |
| Take-profit technique | **$3.58** | Cours ref + 3×ATR ($3.04 + $0.54) — aligné avec agent Recommandation |
| Take-profit consensus | **$9.05** | Price target moyen analystes |
| Ratio R/R (technique) | **1.5** | $0.54 / $0.36 — aligné avec agent Recommandation |
| Ratio R/R (consensus) | **15.9** | $6.01 / $0.38 |
| Ratio R/R (max pain) | **2.7** | $0.96 / $0.36 | $4.00 max pain vs close $3.04 |

---

## Conclusion

**Thèse : NON ÉTABLIE — PROFIL SPÉCULATIF BIOTECH — ATTENDRE (INCHANGÉE)**

Le snapshot 10h UTC du 2026-06-16 enregistre une **stabilité mécanique totale** vs le snapshot 21h UTC du 15/06. Le **close reste à $3.04**, le **RSI à 25.93** (survente extrême), l'**ATR à $0.18**, la **MM50 à $3.90** (écart −22.1%) et le **volume à 0.87×** moyenne 20j. Aucune mutation de cours, de momentum ou de structure n'est détectée.

**Le développement clé est l'absence de changement** — le marché est en standby pré-ouverture US. La **structure options très haussière** (put/call 0.14, call OI 87.8%, max pain $4.00) avec expiration demain (2026-06-18) reste le catalyseur technique dominant. Le pin risk haussier vers $4.00 persiste.

Le **Score Global Ajusté reste à 55.0/100** et le **Score Opportunité à 5.8/10**. La recommandation reste **ATTENDRE**. Le timing reste **Défavorable** (inchangé) en raison de la position sous MM50 et de la tendance baissière persistante.

**Ce qui a changé depuis le snapshot 2026-06-15 21h UTC :**
- 🟡 Cours : **$3.04** (inchangé)
- 🟡 Volume : **0.87×** (inchangé)
- 🟡 RSI : **25.93** (inchangé, survente extrême persistante)
- 🟡 ATR : **$0.18** (inchangé)
- 🟡 MM50 : **$3.90** (stable)
- 🟢 Options : **anomalie JSON 6e occurrence traitée** (valeurs opérationnelles conservées : max pain $4.00, put/call 0.14, call OI 87.8%)
- 🟡 Short interest : **14.97%** (stable)
- 🟡 Timing : **Défavorable** (inchangé)
- 🟡 SL/TP : conservés **$2.68 / $3.58**
- 🟡 DRAFT_refresh : **classé faux positif** (ATR_SPIKE sans mutation — données identiques close 21h UTC 15/06)
- ❌ Aucune news majeure

**Conditions de passage à ACHETER :**
1. Consolidation au-dessus de $3.05 avec volume > 0.8× moyenne (confirmation du rebond)
2. Clôture au-dessus du max pain $4.00 post-expiration (2026-06-18)
3. Data readout positif CX-2029 ou CX-904 (catalyseur clinique majeur)
4. Nouveau partenariat avec upfront significatif (> $100M)

**Conditions de passage à SURVEILLER (dégradation) :**
1. Retour sous $2.98 avec volume > 0.8× moyenne (support cassé)
2. Clôture sous $2.90
3. Volume s'effondrant sous 0.4× moyenne sur rebond (pas de conviction)

**Conditions de passage à ÉVITER :**
1. Échec clinique majeur (stop essai)
2. Dilution capitale > 20% sans catalyseur
3. Perte d'un partenariat stratégique (AbbVie/BMS)
4. Break sous $2.80 avec volume > 0.8× moyenne

**Alertes actives :**
- 🟡 Cours $3.04 — stable vs close 21h UTC 15/06
- 🟡 Volume 0.87× — normalisation maintenue
- 🔴 RSI 25.93 — survente extrême persistante
- 🟢 Short interest 14.97% — stable, potentiel short squeeze si catalyseur
- 🔴 Cours sous MM50 ($3.90) avec écart −22.1%
- 🟡 Score Global Ajusté 55.0/100 — au-dessus du seuil institutionnel (50) mais stable
- 🟡 Recommandation ATTENDRE — zone de risque technique accru
- 🟢 Options — **structure très haussière** (max pain $4.00, put/call 0.14, call OI 87.8%), expiration demain
- 🟢 Anomalie options JSON **traitée** (6e occurrence — valeurs opérationnelles conservées)
- [INFO] DRAFT_refresh classé **faux positif** — pas de réécriture de thèse nécessaire
- [WARNING] Données MM200 manquantes
- [WARNING] Biotech pré-revenue — scoring standard peu fiable
- [INFO] Earnings confirmé le 2026-08-06 (J+51) — Est EPS $−0.13 à $−0.07
- [INFO] Expiration options **demain** (2026-06-18) — volatilité potentielle, pin risk vers $4.00

---

*Rapport généré automatiquement — snapshot 2026-06-16 10:00 UTC.*
*Analyse précédente : `CTMX_2026-06-15_update.md` (snapshot 21h UTC) — close $3.04, ATTENDRE.*
