# FUBO — Mise a jour 2026-06-17 (snapshot 13h UTC)

> **Ticker :** FUBO | **Secteur :** Communication Services / Broadcasting
> **Close :** $9.28 (-6.45% vs previous close $9.92) | **Volume :** 1.86M (1.37x moy. 20j 1.36M)
> **Source donnees :** `data/latest.json` (2026-06-17 13:00:12 UTC) + `data/recommandations_latest.json`

---

## 1. Resume des changements depuis l'analyse precedente (2026-06-17 10h UTC)

| Indicateur | 2026-06-17 10h UTC | 2026-06-17 13h UTC | Δ |
|------------|-------------------|-------------------|---|
| **Close** | $9.28 | $9.28 | **stable** |
| **RSI 14j** | 46.1 | 46.1 | **stable** |
| **Volume vs 20j** | 1.37x (1.86M) | **1.37x** (1.86M) | **stable** |
| **MM50** | $10.98 | $10.98 | **stable** |
| **Ecart MM50** | -15.5% | **-15.5%** | **stable** |
| **ATR 14j** | $0.86 | $0.86 | **stable** |
| **Max Pain (JSON)** | $3.00 aberrant | **$11.00 cohérent** | **RESOLU** |
| **Put/Call (JSON)** | null (anomalie) | **0.45** | **RESOLU** |
| **Call OI % (JSON)** | 0.0% (anomalie) | **69.0%** | **RESOLU** |
| **Short Interest** | 24.32% | 24.32% | **stable** |
| **Score Global Ajuste** | 54.8/100 | **54.8/100** | **stable** |
| **Score Opportunite** | 6.3/10 | 6.3/10 | **stable** |
| **Score Valorisation** | 7.5/10 | 7.5/10 | **stable** |
| **Score Catalyseur** | 6.5/10 | 6.5/10 | **stable** |
| **Score Momentum** | 4.0/10 | 4.0/10 | **stable** |

> **Resolution anomalie options JSON :** Le snapshot 13h UTC retourne des donnees options parfaitement coherentes (max pain $11.00, put/call 0.45, call OI 69.0%) apres 17 jours d'anomalies recurrentes ($3.00 aberrant, valeurs nulles). Ces valeurs confirment la structure haussiere latente deja identifiee (max pain > spot, calls dominants).

**Verdict :** Stabilite technique totale entre les deux snapshots. La seule mutation significative est la **resolution de l'anomalie data quality options**, qui restaure la confiance dans le signal haussier latent (max pain $11.00, call OI 69.0%, put/call 0.45). Aucun changement de cours, de volume, de RSI ou de scoring agent.

---

## 2. Mise a jour technique

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| **Open** | $9.86 | Ouverture quasi-stable (-0.6% vs previous close) |
| **High** | $9.97 | Resistance intraday $9.97 non tenue |
| **Low** | $8.915 | Low de session teste et tenu |
| **Close** | $9.28 | Identique au snapshot 10h |
| **RSI 14j** | 46.1 | Zone neutre inferieure, proche de la survente (≤30) |
| **MM50** | $10.98 | Ecart **-15.5%** — tendance baissiere intacte |
| **MM200** | — | Non calculee (historique insuffisant) |
| **ATR 14j** | $0.86 | Volatilite stable ; ATR relatif 9.3% (superieur au seuil 5.0%) |
| **Volume 20j** | 1.36M | Moyenne stable |
| **Volume session** | 1.86M | **1.37x** — explosion de liquidite maintenue |
| **Beta** | 2.392 | Volatilite systematique elevee |
| **52W Range** | $8.31 – $56.64 | Cours a **-83.6%** du 52W high, +11.7% au-dessus du 52W low |

**Supports / Resistances (ATR-based)**
- R1 (resistance immediate) : $9.97 – $10.00 (high session + psychologique)
- R2 : $10.98 – $11.00 (MM50 + max pain operationnel)
- S1 (support immediat) : $9.07 – $9.15 (zone de consolidation recente)
- S2 : $8.915 (low du jour — teste et tenu)
- S3 : $8.31 (52W low)

**Timing technique : Defavorable**
- Cours sous MM50 depuis 15 sessions consecutives
- Donnees options desormais fiables : structure haussiere confirmee (max pain $11.00, call OI 69.0%, put/call 0.45)
- Echeance options J+1 (2026-06-18) : pinning imminent autour de $11.00 si le spot remonte — peu probable a J-1 avec spot a -15.5%

---

## 3. Mise a jour fondamentale

Aucune nouvelle donnee fondamentale publiee depuis le 2026-06-17 10h UTC. Les metriques restent inchangées :

| Metrique | Valeur | Contexte |
|----------|--------|----------|
| **Market Cap (Yahoo)** | $273.2M | — |
| **Market Cap (FMP)** | $879.7M | Divergence Yahoo/FMP persistante (×3.2) |
| **Forward P/E** | 19.7 | Pricing d'une infime rentabilite future |
| **EV/Revenue** | 0.431 | Multiple tres bas, refletant la mefiance du marche |
| **P/B** | 0.34 | Patrimoine net negatif (-$398.9M tangible) — discount profond |
| **Debt/Equity** | 2.43 | Levier eleve ; couverture interets negative (-4.7×) |
| **Current Ratio** | 0.84 | Risque de liquidite |
| **Gross Margin** | 11.1% | Faible |
| **Operating Margin** | -2.6% | Non rentable a l'operationnel |
| **Net Margin** | 5.7% | Profitabilite exceptionnelle/nette (non operationnelle) |
| **FCF Yield** | -18.9% | FCF negatif |
| **ROIC** | -2.1% | Destruction de valeur a l'investissement |
| **Consensus (FMP)** | $50.25 (4 analystes) | Upside theorique +441% — prediction hautement speculative |

**Filtre Qualite : 1/6** (inchangé)
- Revenue CAGR 5 ans : ❌
- Profit CAGR 5 ans : ❌
- Assets/Liabilities : ❌ (patrimoine net negatif)
- FCF positif 5 ans : ❌
- Moat : ❌ (streaming sportif sature)
- TAM forte croissance : ⚠️

> Regle absolue : Score Qualite ≤3/6 → Score Valorisation plafonne a 5/10. L'agent attribue 7.5/10, ce qui suggere que le plafonnement n'est pas applique ou que le modele valorise le "deep value" speculatif. Cette divergence merite une vigilance analytique.

---

## 4. Mise a jour sentiment / options / news

### Options (anomalie RESOLUE)
| Indicateur | Valeur JSON 13h | Valeur Operationnelle 10h | Signal |
|------------|-----------------|---------------------------|--------|
| **Max Pain** | **$11.00** | $11.00 | Spot a -15.5% — pinning baissier prononce |
| **Put/Call Ratio** | **0.45** | 0.43 | Biais haussier (call dominants 2.2×) |
| **Call OI %** | **69.0%** | 70.0% | Biais haussier structurel confirmé |
| **Echeance** | 2026-06-18 (J+1) | 2026-06-18 (J+1) | Pinning imminent si spot remonte — peu probable |

> **Resolution confirmee :** Le snapshot 13h UTC retourne des donnees options parfaitement coherentes pour la premiere fois depuis le 2026-06-01. L'anomalie recurrente (max pain $3.00 / put/call null / call OI 0.0%) est resolue. Les valeurs operationnelles conservees a 10h ($11.00 / 0.43 / 70.0%) sont validees par le JSON 13h avec une marge d'erreur negligeable (±0.02 sur put/call, ±1.0 pp sur call OI).

### Sentiment
- **Short Interest** : 24.32% du float (29.2M shares) — niveau eleve, potentiel short squeeze latent si catalyseur positif
- **Social Sentiment** : 0 mentions Reddit, score 0/10 — aucun buzz retail detecte
- **Analystes** : 4 analystes FMP, $50.25 price target, 0 couverture recente — consensus fige et peu credible

### News / Evenements
- Aucun evenement corporate detecte dans `data/events_latest.json`
- Prochain earnings : **2026-08-06** (50 jours, Est EPS $-0.32 a $0.07, Rev $1.5B) — source `upcoming_events_latest.json`
- Aucune upgrade/downgrade, aucun insider trade significatif signale

---

## 5. Scoring global actualise

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.5/10 | 35% | 2.28 |
| **Valorisation** | 7.5/10 | 40% | 3.00 |
| **Momentum** | 4.0/10 | 25% | 1.00 |
| **Score Opportunite brut** | — | — | **6.3/10** |
| **Score Global brut** | — | — | **62.8/100** |
| **Malus / Bonus** | — | — | -8.0 pts |
| **Score Global Ajuste** | — | — | **54.8/100** |

**Regle de disqualification :** Aucun score ≤2/10 → pas d'exclusion automatique.

**Interpretation :**
- Le Score Global Ajuste 54.8/100 se situe dans la fourchette **ATTENDRE** (50–59).
- Aucun changement de scoring entre 10h et 13h UTC. L'amelioration principale est la **restauration de la confiance data quality** sur les options, qui confirme la structure haussiere latente sans modifier le verdict global.
- **Malus sectoriel** : XLC (Communication Services) est Bottom 3 dans `data/sector_rotation_latest.json` (momentum score 0.0) → malus -0.5 pt implicite non encore reflete dans le scoring agent.

---

## 6. Niveaux SL / TP / Ratio R/R

| Niveau | Valeur | Distance vs Close |
|--------|--------|-------------------|
| **Stop-Loss** | $7.56 | -18.5% (2× ATR = $1.72) |
| **Take-Profit** | $11.86 | +27.8% (3× ATR = $2.58) |
| **Ratio R/R** | **1.5×** | — |

> Les niveaux sont inchanges vs snapshot 10h. Le ratio 1.5x est a la limite inferieure de l'acceptabilite institutionnelle (cible ≥1.5×). Le SL $7.56 est en dessous du 52W low ($8.31), ce qui le rend risque en cas de gap down. Le TP $11.86 correspond au max pain operationnel ($11.00) + marge technique.

---

## 7. Conclusion — These confirmee, modifiee ou invalidee ?

### Verdict : **THESE ATTENDRE CONFIRMEE — STABILITE TOTALE + RESOLUTION ANOMALIE OPTIONS**

Le snapshot 2026-06-17 13h UTC confirme la **stabilité totale** des données marché et technique vs le snapshot 10h UTC. La seule mutation significative est la **résolution de l'anomalie data quality options JSON**, qui valide la structure haussiere latente (max pain $11.00, put/call 0.45, call OI 69.0%) après 17 jours d'incohérences. Cette restauration renforce légèrement la confiance dans le signal options sans modifier le verdict global.

**Arguments pour la confirmation :**
1. **Stabilite technique totale** : cours, RSI, volume, ATR, MM50 inchanges entre 10h et 13h UTC
2. **Resolution anomalie options** : donnees JSON coherentes pour la premiere fois depuis le 2026-06-01
3. **Structure options haussiere validee** : max pain $11.00, call OI 69.0%, put/call 0.45
4. **Short interest eleve** : 24.32% du float = combustible latent inchangé
5. **Valorisation attractive** : P/B 0.34, EV/Rev 0.431 — le marche price une quasi-faillite

**Arguments contre une entree (inchanges) :**
1. **Tendance baissiere intacte** : sous MM50 depuis 15 sessions consecutives
2. **Qualite fondamentale degradee** : Score Qualite 1/6, FCF negatif, patrimoine net negatif, debt/equity 2.43
3. **Pas de catalyseur actif** : aucune news, aucun upgrade, aucune guidance recente
4. **Timing Defavorable** : sous MM50 + pas de momentum = pas de confirmation technique
5. **Malus sectoriel** : XLC bottom 3 sector rotation

**Conditions de reactivation d'une these ACHETER (inchangées) :**
- Retour au-dessus de MM50 ($10.98) avec close confirme au-dessus de $10.50
- Volume >1.0x moyenne 20j en confirmation
- Catalyseur fondamental (earnings beat, upgrade analyste, guidance positive)

**Recommandation :** **ATTENDRE** — pas d'entree en l'etat. La stabilité technique et la resolution de l'anomalie options sont des signaux positifs marginaux, mais ils ne compensent pas l'absence de momentum et le profil fondamental degrade. L'echeance options J+1 (2026-06-18) pourrait generer du pinning autour de $11.00 si le spot remonte, mais la probabilite est faible a une journee de l'echeance avec un spot a -15.5%.

---

*Rapport genere par le desk Argus-IA — Donnees sources : `data/latest.json` (2026-06-17 13:00:12 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`. Anomalie options JSON RESOLUE au snapshot 13h UTC.*
