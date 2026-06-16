# AST — Preview Earnings (placeholder glissant)

> **Date :** 2026-06-16
> **Evenement :** Earnings (placeholder FMP)
> **Date prevue :** 2026-06-16 (J=0 glissant depuis 25/05, >22 jours de glissement non resolu)
> **Source :** fmp

---

## Statut du placeholder

Le placeholder FMP signale un earnings AST le 2026-06-16 avec `days_until: 0`. Cependant :
- AST n'a **aucune donnee de cours** dans les snapshots depuis >44 sessions consecutives (`No price history`).
- Il est **impossible de correler** un resultat earnings sans historique de prix.
- Le placeholder est **glissant** : la date J=0 n'a pas avance depuis le 25/05 (22+ jours de decalage non resolu).
- **Conclusion :** ce n'est pas un earnings verifiable. Il s'agit vraisemblablement d'une erreur de mapping FMP liee au ticker fantome AST.

---

## Note sur le proxy ASTS

ASTS (AST SpaceMobile — NASDAQ), probable doublon d'AST, a ses propres earnings programmes le **2026-08-10** (Q2 2026, 55 jours). Aucun earnings n'est attendu pour ASTS le 16/06.

---

## References

- `data/upcoming_events_latest.json` (2026-06-16) — AST: earnings 2026-06-16 (J=0 glissant)
- `data/latest.json` (2026-06-16) — AST: error "No price history" ; ASTS: close $87.57
