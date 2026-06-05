# CONTEXT — SOFI — Dernière mise à jour : 2026-06-05

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ACHETER — Sizing réduit
**Prix cible :** $20.47 (cours + 3×ATR)
**Stop-loss :** $15.92 (cours − 2×ATR)
**Upside/Downside :** +15.4% / −10.3%
**Dernière mise à jour :** 2026-06-03 (snapshot 13:00 UTC — stabilité totale vs close 02/06, anomalie options JSON résolue)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le charter bancaire 2022 crée une barrière réglementaire modérée vs les fintechs non-banques. Le snapshot du **2026-06-03 13h UTC** confirme la **stabilité totale** des prix depuis le close du 02/06 : cours **$17.74**, RSI **63.90**, ATR **$0.91**, MM50 **$16.76** (+5.8%). Le volume final de **76.76M (1.13× moy. 20j)** confirme la distribution partielle active lors du pullback −4.52% du 02/06. **[RÉSOLU]** Les données options corrompues du snapshot 10h UTC (Max Pain $5.00 aberrant, Put/Call et Call OI `null`) ont été corrigées dans `data/latest.json` : Max Pain confirmé à **$20.00**, Put/Call **0.54** (+0.06 vs 02/06, légèrement moins bullish mais reste haussier), Call OI **65.0%** (−2.4 pts vs 02/06, légère prise de profit sur calls post-gap). Le support immédiat est le low du 02/06 à **$17.46**, suivi de la MM50 à **$16.76**. La résistance immédiate est le close du 01/06 à **$18.58**, puis **$19.00** (psychologique) et **$20.00** (Max Pain confirmé). La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro majeurs. Le Forward P/E **22.74** est stable. Le Score Opportunité reste à **6.1/10**, et le Score Global Composite en zone **ACHETER (60.8/100, ajusté 65.8)**. Le short interest à **13.68%** laisse un potentiel de squeeze si un rebond se matérialise. Le secteur financier (XLF) reste sous-performant SPY (RS20 −6.0%, momentum 0.0/10) — headwind sectoriel à surveiller. Earnings Q2 dans **55j** (28 juillet, estimates EPS $0.10–$0.11, Rev $1.1B). ⚠️ Clôture proche du low du 02/06 ($17.46) + volume supérieur à la moyenne (1.13×) = signal de distribution à très court terme. Attendre un rebond au-dessus de $18.00 avec volume >1.0× acheteur pour confirmer la fin de la distribution.
**Score 6.1/10. Score Global 60.8/100 (ajusté 65.8). ACHETER — Sizing réduit.**

**Données complètes** — Cours, RSI, ATR, P/E, beta disponibles dans `data/latest.json` (snapshot 2026-06-03T13:00 UTC). Options : Max Pain $20.00, Put/Call 0.54, Call OI 65.0%. Expiration prochaine 2026-06-05 (2 jours ouvrés).

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $20.47
- **Stop-loss :** $15.92
- **Statut thèse :** invalide
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Baisse — $13.97 (SL 2×ATR) — 🟢 Active
- Hausse — $19.51 (prix cible) — 🟢 Active
- Volume — >2× moy. 20j (>XXM) — 🟢 Active

---

## 📅 Prochains événements

- Aucun événement à venir.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 52.85
- **MM 50j :** 16.75
- **MM 200j :** —
- **ATR 14j :** 0.97
- **Volume moy. 20j :** 67820741

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-05
- **Type :** full refresh
- **Fichier :** `SOFI_2026-06-05_DRAFT_refresh.md`
- **Conclusion :** > **Date :** 2026-06-05

---

## 🔄 Triggers détectés (full refresh)

- **PRICE_GAP** (medium) — Gap -7.00% overnight (seuil ±5.0%)
- **ATR_SPIKE** (medium) — ATR relatif 6.14% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
