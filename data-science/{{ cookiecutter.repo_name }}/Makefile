# Makefile for the CleanMatch project

.PHONY: help install dev format lint typecheck test test-fast all check run clean

help: ## Display this help
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies via uv (prod + dev)
	uv sync

dev: install ## Install dependencies and pre-commit hooks
	uv run pre-commit install

format: ## Format the code with ruff
	uv run ruff format src/ tests/ app/

lint: ## Check code cleanliness with ruff (check + format)
	uv run ruff check src/ tests/ app/
	uv run ruff format --check src/ tests/ app/

typecheck: ## Check strict type validity with mypy
	uv run mypy --explicit-package-bases src/ app/

test: ## Run unit tests with full coverage
	uv run pytest tests/ -v --cov=src/project_name --cov-report=term-missing --cov-fail-under=80

test-fast: ## Run tests and stop at the first failure
	uv run pytest tests/ -x

all: lint typecheck test ## Run lint, typecheck, and tests in sequence

check: all ## Alias for 'all' (local CI)

run: ## Launch the local web application (Streamlit)
	uv run streamlit run app/streamlit_app.py

run_api: ## Launch the API
	uv run {{ cookiecutter.package_name }}-api

clean: ## Remove temporary files and caches
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov .coverage coverage.xml dist/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

digest: ## Generate the project digest
	@echo "Generating project digest..."
	uv run --with gitingest gitingest .
	explorer.exe .
