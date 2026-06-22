# CONTEXT — AAL — Dernière mise à jour : 2026-06-22

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE — BIAIS HAUSSIER LÉGÈREMENT RENFORCÉ (snapshot 13h UTC : rally +3.7% sur volume 1.16× moyenne, remontée des highs $16.055 → $16.07, scores améliorés Global 55.0/100, options corrigées Max Pain $13.50)
- **Prix cible :** Suspendu — attente cassure 52W high $16.50 sur volume > 120M confirmé en close ou réévaluation post-earnings
- **Stop-loss :** $14.63 (2×ATR $0.68)
- **Take-profit :** $18.03 (3×ATR $0.68)
- **Ratio R/R :** 1.5
- **Upside/Downside :** +3.3% (consensus $16.51) / −8.5% (SL)
- **Derniere mise a jour :** 2026-06-22 (snapshot 13h UTC, data options corrigée)

American Airlines est une compagnie aerienne legacy fortement endettee (~$40B) avec aucun moat. Hors perimetre qualite (0-1/6). La session du 22/06 a clôturé à **$15.99 (+3.7%)** sur un volume en **expansion de 126.28M (1.16× moyenne 20j)**, vs 62.19M (0.60× moyenne) au snapshot précédent du 17/06. Le high du jour **$16.07** dépasse le high précédent **$16.055** = invalidation du signal de fatigue haussière. Le RSI est resté **inchangé à 61.34** malgré +3.7% = pas de surachat aggravé. Le cours se positionne à **3.1% du 52W high $16.50**.

Les scores de l'agent recommandation ont été **légèrement améliorés** : Score Opportunité **5.0/10** (was 4.9), Score Global ajusté **55.0/100** (was 53.8) — écart réduit par rapport au seuil d'achat (60). L'upside consensus s'est réduit mécaniquement à **+3.3%** (vs +4.2%) car le cours a monté plus vite que le consensus. Le Forward P/E est à **7.18**. Le short interest reste stable à **11.39%**. Le Filtre Qualité reste 0–1/6. XLI (Industriels) est dans le **top3 sector rotation** (#2, momentum_score 6.25).

**✅ Correction data quality :** Le snapshot 10h UTC affichait des options corrompues (Max Pain $5.00 aberrant). Le pipeline 13h UTC a restauré des données cohérentes : Max Pain **$13.50**, Put/Call **1.74**, Call OI **36.6%**, expiration 2026-06-26. Le Max Pain remonté à $13.50 réduit l'écart spot/Max Pain à **+18.4%** (vs +59.9% avec l'ancien Max Pain $10.00) = l'influence gamma mécanique devient **non négligeable**. Surveillance accrue si repli sous $15.00 avant expiration vendredi.

**Verdict institutionnel :** La thèse est **ATTENDRE — BIAIS HAUSSIER LÉGÈREMENT RENFORCÉ.** La consolidation reste saine (cours au-dessus MM50, gap tenu), et l'expansion volumétrique + la remontée des sommets indiquent un retour de conviction institutionnelle. Cependant, le Score Global 55.0/100 reste sous le seuil d'achat. La valorisation reste faible (upside +3.3%). Le bilan reste extrêmement fragile (current ratio 0.50, tangible asset value négatif, net debt/EBITDA 8.83x). Le 52W high n'est pas encore cassé. Le gamma landscape modifié (Max Pain $13.50) ajoute une variable de surveillance technique.

**Conditions de réactivation vers ACHETER (Sizing Réduit) :**
- Cours > $16.50 (cassure 52W high) sur volume > 120M confirmé en close
- Score Global ajusté ≥ 60

**Conditions de dégradation vers SURVEILLER :**
- Repli sous $15.46 (close du 16/06)
- Repli sous $14.63 (SL cassé)
- Repli sous $15.00 avant expiration 26/06 (risque gamma vers Max Pain $13.50)

**⚠️ Données partielles** — MM200 indisponible. Accounting risk indisponible. Quant report insuffisant. Social sentiment sans données Reddit. Transcripts NLP, insider trades détaillés, 13F complets, ETF flows, dark pool non disponibles.

---

## Actualites ayant impacte ce dossier
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $14.63
- **Statut thèse :** invalide
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- **2026-05-17** · earnings · Miss / Imprécis · Ligne:  | 2026-05-17 | AAL | `_init.md` | SURVEILLER | $14.00

---

## 🚨 Alertes actives

- Baisse — $11.41 (SL 2×ATR) — 🟢 Active
- Hausse — $14.00 (prix cible) — 🔴 Déclenchée (27/05)
- Volume — >2× moy. 20j (>XXM) — 🟢 Active

---

## 📅 Prochains événements

- Aucun événement à venir.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 61.34
- **MM 50j :** 13.07
- **MM 200j :** —
- **ATR 14j :** 0.68
- **Volume moy. 20j :** 108887230

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-22
- **Type :** update
- **Fichier :** `AAL_2026-06-22_update.md`
- **Conclusion :** **Date :** 2026-06-22 (snapshot 10h UTC, pre-session NY)

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*
