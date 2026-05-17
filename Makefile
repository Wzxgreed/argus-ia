.PHONY: help install test lint format pipeline clean push status agent-watchman agent-geo agent-crypto agent-accounting agent-sector agent-social agent-fx agent-event agent-reco agent-news group-a group-b group-c

help:
	@echo "Argus-IA — Commandes disponibles"
	@echo ""
	@echo "  make install   → Créer venv + installer dépendances"
	@echo "  make test      → Exécuter la suite de tests"
	@echo "  make lint      → Vérifier le linting (Ruff)"
	@echo "  make format    → Formater le code (Black)"
	@echo "  make pipeline  → Lancer le pipeline du matin (20 étapes)"
	@echo "  make status    → Voir l'avancement du pipeline en cours"
	@echo "  make wait-pipeline → Attendre la fin du pipeline + notification"
	@echo "  make clean     → Nettoyer les fichiers temporaires"
	@echo "  make push      → Linter, tester, puis push sur GitHub"
	@echo ""
	@echo "  Groupes parallèles (Makefile natif):"
	@echo "  make group-a   → Agents indépendants (learn_from_errors, quant, geo)"
	@echo "  make group-b   → Fetch données brutes (crypto, prices, macro, calendar, news)"
	@echo "  make group-c   → Agents dépendants (8 agents en parallèle)"
	@echo ""
	@echo "  Agents individuels :"
	@echo "  make agent-news      → Fetch unifié des news"
	@echo "  make agent-watchman  → Watchman scan"
	@echo "  make agent-geo       → Géopolitique"
	@echo "  make agent-crypto    → Crypto-correlation"
	@echo "  make agent-accounting → Scan comptable"
	@echo "  make agent-sector    → Rotation sectorielle"
	@echo "  make agent-social    → Sentiment retail"
	@echo "  make agent-fx        → Exposition FX"
	@echo "  make agent-event     → Event-Driven (M&A, buybacks, activism)"
	@echo "  make agent-reco      → Recommandations (acheter/conserver/vendre)"

install:
	python3 -m venv .venv
	source .venv/bin/activate && pip install --upgrade pip
	source .venv/bin/activate && pip install -r requirements.txt
	source .venv/bin/activate && pip install -e ".[dev]"

test:
	source .venv/bin/activate && pytest tests/ -v -m "not integration and not slow" --tb=short

lint:
	source .venv/bin/activate && ruff check scripts/ tests/
	@echo ""
	source .venv/bin/activate && black --check scripts/ tests/

format:
	source .venv/bin/activate && black scripts/ tests/
	source .venv/bin/activate && ruff check --fix scripts/ tests/

pipeline:
	./scripts/run_morning.sh

status:
	@./scripts/pipeline_status.sh

wait-pipeline:
	@./scripts/pipeline_status.sh --wait

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov
	@echo "Clean done."

push: lint test
	@echo "Lint + tests OK. Pushing to GitHub..."
	git push origin main

# ── Groupes parallèles (Makefile natif) ──────────────────────────────────────
# Phase A : agents indépendants (pas besoin de latest.json)
group-a:
	@echo "=== Phase A : Independent agents (parallel) ==="
	@source .venv/bin/activate && python3 scripts/learn_from_errors.py &
	@source .venv/bin/activate && python3 scripts/agent_quant.py &
	@source .venv/bin/activate && python3 scripts/agent_geo.py &
	@wait
	@echo "Phase A complete."

# Phase B : fetch données brutes (séquentiel, produit latest.json)
group-b:
	@echo "=== Phase B : Raw data fetch (sequential) ==="
	@source .venv/bin/activate && python3 scripts/agent_crypto.py
	@source .venv/bin/activate && python3 scripts/fetch_prices.py
	@source .venv/bin/activate && python3 scripts/fetch_macro.py
	@source .venv/bin/activate && python3 scripts/fetch_calendar.py
	@source .venv/bin/activate && python3 scripts/agent_news_fetcher.py
	@echo "Phase B complete."

# Phase C : agents dépendants (parallèle, lisent latest.json)
group-c:
	@echo "=== Phase C : Dependent agents (parallel) ==="
	@source .venv/bin/activate && python3 scripts/agent_watchman.py &
	@source .venv/bin/activate && python3 scripts/detect_major_events.py &
	@source .venv/bin/activate && python3 scripts/agent_accounting.py ; true &
	@source .venv/bin/activate && python3 scripts/agent_sector_rotation.py ; true &
	@source .venv/bin/activate && python3 scripts/agent_social.py ; true &
	@source .venv/bin/activate && python3 scripts/agent_fx.py ; true &
	@source .venv/bin/activate && python3 scripts/agent_event_driven.py ; true &
	@source .venv/bin/activate && python3 scripts/fetch_transcripts.py ; true &
	@wait
	@echo "Phase C complete."

# Phase D : agrégation finale (séquentielle)
group-d:
	@echo "=== Phase D : Final aggregation (sequential) ==="
	@source .venv/bin/activate && python3 scripts/validate.py
	@source .venv/bin/activate && python3 scripts/agent_recommandation.py
	@source .venv/bin/activate && python3 scripts/paper_trading.py ; true
	@echo "Phase D complete."

# Pipeline complet via Makefile (4 phases)
pipeline-make: group-a group-b group-c group-d
	@echo "Pipeline complete via Makefile."

# ── Agents individuels avec auto-push ────────────────────────────────────────

agent-news:
	@echo "Running unified news fetcher..."
	@source .venv/bin/activate && python3 scripts/agent_news_fetcher.py
	@./scripts/auto_push.sh "News fetcher snapshot"

agent-watchman:
	@echo "Running Watchman agent..."
	@source .venv/bin/activate && python3 scripts/agent_watchman.py
	@./scripts/auto_push.sh "Watchman agent snapshot"

agent-geo:
	@echo "Running Geopolitical agent..."
	@source .venv/bin/activate && python3 scripts/agent_geo.py
	@./scripts/auto_push.sh "Geopolitical agent snapshot"

agent-crypto:
	@echo "Running Crypto-correlation agent..."
	@source .venv/bin/activate && python3 scripts/agent_crypto.py
	@./scripts/auto_push.sh "Crypto agent snapshot"

agent-accounting:
	@echo "Running Accounting risk agent..."
	@source .venv/bin/activate && python3 scripts/agent_accounting.py
	@./scripts/auto_push.sh "Accounting agent snapshot"

agent-sector:
	@echo "Running Sector rotation agent..."
	@source .venv/bin/activate && python3 scripts/agent_sector_rotation.py
	@./scripts/auto_push.sh "Sector rotation agent snapshot"

agent-social:
	@echo "Running Social sentiment agent..."
	@source .venv/bin/activate && python3 scripts/agent_social.py
	@./scripts/auto_push.sh "Social sentiment agent snapshot"

agent-fx:
	@echo "Running FX exposure agent..."
	@source .venv/bin/activate && python3 scripts/agent_fx.py
	@./scripts/auto_push.sh "FX exposure agent snapshot"

agent-event:
	@echo "Running Event-Driven agent..."
	@source .venv/bin/activate && python3 scripts/agent_event_driven.py
	@./scripts/auto_push.sh "Event-Driven agent snapshot"

agent-reco:
	@echo "Running Recommendation engine..."
	@source .venv/bin/activate && python3 scripts/agent_recommandation.py
	@./scripts/auto_push.sh "Recommendation engine snapshot"
