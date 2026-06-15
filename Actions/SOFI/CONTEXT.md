# CONTEXT — SOFI — Dernière mise à jour : 2026-06-15

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
**Prix cible :** $19.82 (cours + 3×ATR)
**Stop-loss :** $14.42 (cours − 2×ATR)
**Upside/Downside :** +19.5% / −12.4%
**Dernière mise à jour :** 2026-06-15 (snapshot 10:00 UTC — données techniques complètes, scores révisés, volume en retrait, anomalie options)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le charter bancaire 2022 crée une barrière réglementaire modérée vs les fintechs non-banques. Le snapshot du **2026-06-15 à 10h UTC** apporte un **rétablissement des données techniques** après plusieurs snapshots partiels : ATR **$1.08** et MM50 **$16.83** sont désormais disponibles. Le cours à **$16.58** progresse de +0.48% vs le 10/06 mais reste **−1.49% sous la MM50**, confirmant le timing **Défavorable**. Le **Score Global ajusté progresse à 52.3/100** (+0.8 pt), toujours en zone **ATTENDRE**, à **2.3 pt du seuil SURVEILLER** (<50). Les scores agents ont été **révisés à la hausse** : Catalyseur **6.8/10** (+1.5), Valorisation **6.0/10** (+1.5), mais Momentum **5.0/10** (−1.0). Le RSI a reculé à **55.69** (zone neutre). Le volume à **0.69×** est en **retrait significatif** (−37% relatif), indiquant un assèchement de la participation institutionnelle. Le short interest reste élevé à **14.71%** — niveau critique qui crée un **setup asymétrique squeeze/pression vendeuse**. [ALERTE DATA QUALITY] Les données options dans `data/latest.json` sont corrompues (Max Pain $1.00 aberrant, Put/Call et Call OI null) — valeurs historiques du 10/06 conservées : Max Pain **$17.00**, Put/Call **0.48**, Call OI **67.7%**. La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro majeurs. Le Forward P/E **21.25** reste mécaniquement attractif. Le consensus PT **$25.41** (+53.3% upside) est inchangé. Le Filtre Qualité **4/6** (Quality Partielle) n'est pas remis en cause. Earnings Q2 dans **43j** (28 juillet, estimates EPS $0.10–$0.11, Rev $1.1B). XLF (Financials) #2 sector rotation (momentum 6.73) — léger vent de poupe sectoriel. ⚠️ Cours sous MM50 ($16.83) + volume faible (0.69×) = timing Défavorable. Attendre reclaim MM50 $16.83 en close avec volume >1.0× ou breakout $17.00 pour réactiver la thèse haussière. Surveiller le support $16.23 (low du jour) — une cassure ouvrirait le retour à $15.651. Attention au short interest 14.71% qui crée un setup asymétrique squeeze/pression.
**Score 6.0/10. Score Global 52.3/100. ATTENDRE — Aucune entrée.**

**Données complètes** — Cours, RSI, P/E, beta, ATR, MM50 disponibles dans `data/latest.json` (snapshot 2026-06-15T10:00 UTC). Options : [ALERTE DATA QUALITY] Max Pain $1.00 aberrant — historique $17.00 conservé. Expiration prochaine 2026-06-18 (3 jours ouvrés).

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $19.56
- **Stop-loss :** $14.46
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Baisse — $13.78 (SL 2×ATR) — 🟢 Active
- Hausse — $18.88 (prix cible) — 🟢 Active
- Volume — >2× moy. 20j (>140.7M) — 🟢 Active

---

## 📅 Prochains événements

- Aucun événement à venir.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 55.69
- **MM 50j :** 16.83
- **MM 200j :** —
- **ATR 14j :** 1.08
- **Volume moy. 20j :** 72746545

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-15
- **Type :** update
- **Fichier :** `SOFI_2026-06-15_update.md`
- **Conclusion :** Données techniques complètes (ATR $1.08, MM50 $16.83), scores révisés à la hausse (Catalyseur 6.8, Valorisation 6.0), Momentum en retrait (5.0), volume faible (0.69×). Thèse ATTENDRE confirmée, timing Défavorable (sous MM50). [ALERTE DATA QUALITY] Options corrompues.

---

## 🔄 Triggers détectés (full refresh)

- **ATR_SPIKE** (medium) — ATR relatif 6.51% (seuil 5.0%)

---

*Généré automatiquement — ne pas éditer manuellement.*
