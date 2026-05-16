.PHONY: help install test lint format pipeline clean push agent-watchman agent-geo agent-crypto agent-accounting agent-sector agent-social agent-fx agent-event

help:
	@echo "Argus-IA — Commandes disponibles"
	@echo ""
	@echo "  make install   → Créer venv + installer dépendances"
	@echo "  make test      → Exécuter la suite de tests"
	@echo "  make lint      → Vérifier le linting (Ruff)"
	@echo "  make format    → Formater le code (Black)"
	@echo "  make pipeline  → Lancer le pipeline du matin"
	@echo "  make clean     → Nettoyer les fichiers temporaires"
	@echo "  make push      → Linter, tester, puis push sur GitHub"
	@echo ""
	@echo "  Agents individuels :"
	@echo "  make agent-watchman  → Watchman scan"
	@echo "  make agent-geo       → Géopolitique"
	@echo "  make agent-crypto    → Crypto-correlation"
	@echo "  make agent-accounting → Scan comptable"
	@echo "  make agent-sector    → Rotation sectorielle"
	@echo "  make agent-social    → Sentiment retail"
	@echo "  make agent-fx        → Exposition FX"
	@echo "  make agent-event     → Event-Driven (M&A, buybacks, activism)"

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

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov
	@echo "Clean done."

push: lint test
	@echo "Lint + tests OK. Pushing to GitHub..."
	git push origin main

# ── Agents individuels avec auto-push ────────────────────────────────────────

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
