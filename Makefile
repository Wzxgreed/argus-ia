.PHONY: help install test lint format pipeline clean push status wait-pipeline dashboard analyse agent-news agent-watchman agent-geo agent-crypto agent-accounting agent-sector agent-social agent-fx agent-event agent-reco group-a group-b group-c group-d pipeline-make proxy-start proxy-stop proxy-status proxy-ask

help:
	@echo "Argus-IA — Commandes disponibles"
	@echo ""
	@echo "  make install      → Créer venv + installer dépendances"
	@echo "  make test         → Exécuter la suite de tests"
	@echo "  make lint         → Vérifier le linting (Ruff)"
	@echo "  make format       → Formater le code (Black)"
	@echo "  make pipeline     → Lancer le pipeline du matin (orchestrator DAG)"
	@echo "  make status       → Voir l'avancement du pipeline en cours"
	@echo "  make wait-pipeline → Attendre la fin du pipeline + notification"
	@echo "  make dashboard    → Générer le dashboard HTML depuis le dernier rapport"
	@echo "  make clean        → Nettoyer les fichiers temporaires"
	@echo "  make push         → Linter, tester, puis push sur GitHub"
	@echo "  make analyse      → Analyser un nouveau ticker (ajout watchlist + fetch + données)"
	@echo ""
	@echo "  Groupes (Makefile natif — utilisent l'orchestrator):"
	@echo "  make group-a      → Phase A : agents indépendants (parallel)"
	@echo "  make group-b      → Phase B : fetch données brutes (sequential)"
	@echo "  make group-c      → Phase C : agents dépendants (parallel)"
	@echo "  make group-d      → Phase D : agrégation finale (sequential)"
	@echo ""
	@echo "  Agents individuels (via orchestrator --agent):"
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
	source .venv/bin/activate && ruff check scripts/ agents/ tests/
	@echo ""
	source .venv/bin/activate && black --check scripts/ agents/ tests/

format:
	source .venv/bin/activate && black scripts/ agents/ tests/
	source .venv/bin/activate && ruff check --fix scripts/ agents/ tests/

pipeline:
	./scripts/run_morning.sh

status:
	@./scripts/pipeline_status.sh

wait-pipeline:
	@./scripts/pipeline_status.sh --wait

dashboard:
	@echo "Generating dashboard from latest pipeline report..."
	@source .venv/bin/activate && python3 agents/dashboard.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov
	@echo "Clean done."

push: lint test
	@echo "Lint + tests OK. Pushing to GitHub..."
	git push origin main

analyse:
	@if [ -z "$(TICKER)" ]; then \
		echo "Usage: make analyse TICKER=XXX"; \
		echo "Example: make analyse TICKER=NOK"; \
		exit 1; \
	fi
	./scripts/analyse_ticker.sh $(TICKER)

# ── Groupes parallèles (délégués à l'orchestrator) ────────────────────────────
# L'orchestrator lit agents/pipeline.yaml et résout le DAG automatiquement.
# Les groupes Make sont gardés pour compatibilité mais utilisent l'orchestrator.

PYTHONPATH := $(shell pwd)/agents:$(shell pwd)/scripts:$(shell pwd)
export PYTHONPATH

PHASE_A_AGENTS = agents/learn_from_errors/agent.py agents/quant/agent.py agents/geo/agent.py
PHASE_B_AGENTS = agents/crypto/agent.py scripts/fetch_prices.py agents/data_quality_gate/agent.py scripts/fetch_macro.py scripts/fetch_calendar.py agents/news_fetcher/agent.py
PHASE_C_AGENTS = agents/watchman/agent.py agents/detect_major_events/agent.py agents/accounting/agent.py agents/sector_rotation/agent.py agents/social/agent.py agents/fx/agent.py agents/event_driven/agent.py agents/fetch_transcripts/agent.py
PHASE_D_AGENTS = scripts/validate.py agents/recommandation/agent.py agents/paper_trading/agent.py agents/update_context/agent.py

group-a:
	@echo "=== Phase A : Independent agents (parallel) ==="
	@source .venv/bin/activate && python3 agents/learn_from_errors/agent.py &
	@source .venv/bin/activate && python3 agents/quant/agent.py &
	@source .venv/bin/activate && python3 agents/geo/agent.py &
	@wait
	@echo "Phase A complete."

group-b:
	@echo "=== Phase B : Raw data fetch (sequential) ==="
	@source .venv/bin/activate && python3 agents/crypto/agent.py
	@source .venv/bin/activate && python3 scripts/fetch_prices.py
	@source .venv/bin/activate && python3 agents/data_quality_gate/agent.py
	@source .venv/bin/activate && python3 scripts/fetch_macro.py
	@source .venv/bin/activate && python3 scripts/fetch_calendar.py
	@source .venv/bin/activate && python3 agents/news_fetcher/agent.py
	@echo "Phase B complete."

group-c:
	@echo "=== Phase C : Dependent agents (parallel) ==="
	@source .venv/bin/activate && python3 agents/watchman/agent.py &
	@source .venv/bin/activate && python3 agents/detect_major_events/agent.py &
	@source .venv/bin/activate && python3 agents/accounting/agent.py ; true &
	@source .venv/bin/activate && python3 agents/sector_rotation/agent.py ; true &
	@source .venv/bin/activate && python3 agents/social/agent.py ; true &
	@source .venv/bin/activate && python3 agents/fx/agent.py ; true &
	@source .venv/bin/activate && python3 agents/event_driven/agent.py ; true &
	@source .venv/bin/activate && python3 agents/fetch_transcripts/agent.py ; true &
	@wait
	@echo "Phase C complete."

group-d:
	@echo "=== Phase D : Final aggregation (sequential) ==="
	@source .venv/bin/activate && python3 scripts/validate.py
	@source .venv/bin/activate && python3 agents/recommandation/agent.py
	@source .venv/bin/activate && python3 agents/paper_trading/agent.py ; true
	@echo "Phase D complete."

# Pipeline complet via Makefile (4 phases)
pipeline-make: group-a group-b group-c group-d
	@echo "Pipeline complete via Makefile."

# ── Agents individuels avec auto-push ─────────────────────────────────────────

agent-news:
	@echo "Running unified news fetcher..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=news_fetcher
	@./scripts/auto_push.sh "News fetcher snapshot"

agent-watchman:
	@echo "Running Watchman agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=watchman
	@./scripts/auto_push.sh "Watchman agent snapshot"

agent-geo:
	@echo "Running Geopolitical agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=geo
	@./scripts/auto_push.sh "Geopolitical agent snapshot"

agent-crypto:
	@echo "Running Crypto-correlation agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=crypto
	@./scripts/auto_push.sh "Crypto agent snapshot"

agent-accounting:
	@echo "Running Accounting risk agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=accounting
	@./scripts/auto_push.sh "Accounting agent snapshot"

agent-sector:
	@echo "Running Sector rotation agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=sector_rotation
	@./scripts/auto_push.sh "Sector rotation agent snapshot"

agent-social:
	@echo "Running Social sentiment agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=social
	@./scripts/auto_push.sh "Social sentiment agent snapshot"

agent-fx:
	@echo "Running FX exposure agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=fx
	@./scripts/auto_push.sh "FX exposure agent snapshot"

agent-event:
	@echo "Running Event-Driven agent..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=event_driven
	@./scripts/auto_push.sh "Event-Driven agent snapshot"

agent-reco:
	@echo "Running Recommendation engine..."
	@source .venv/bin/activate && python3 agents/orchestrator.py --agent=recommandation
	@./scripts/auto_push.sh "Recommendation engine snapshot"

# ── LLM Proxy ─────────────────────────────────────────────────────────────────

proxy-start:
	@echo "Starting LLM proxy on localhost:11435..."
	@source .venv/bin/activate && python3 scripts/llm_proxy.py --daemon

proxy-stop:
	@echo "Stopping LLM proxy..."
	@source .venv/bin/activate && python3 scripts/llm_proxy.py --stop

proxy-status:
	@source .venv/bin/activate && python3 scripts/llm_proxy.py --status

proxy-ask:
	@if [ -z "$(PROMPT)" ]; then \
		echo "Usage: make proxy-ask PROMPT='Hello' [MODEL=kimi-k2.6]"; \
		exit 1; \
	fi
	@source .venv/bin/activate && python3 scripts/ask_llm.py --prompt "$(PROMPT)" --model "$(MODEL)" 2>/dev/null || echo "Proxy non démarré — lancez 'make proxy-start'"
