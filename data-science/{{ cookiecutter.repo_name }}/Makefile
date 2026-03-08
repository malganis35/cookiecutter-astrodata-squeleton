# Makefile pour le projet CleanMatch

.PHONY: help install dev format lint typecheck test test-fast all check run clean

help: ## Affiche cette aide
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Installe les dépendances via uv (prod + dev)
	uv sync

dev: install ## Installe les dépendances et les hooks de pre-commit
	uv run pre-commit install

format: ## Formate le code avec ruff
	uv run ruff format src/ tests/ app/

lint: ## Vérifie la propreté du code avec ruff (check + format)
	uv run ruff check src/ tests/ app/
	uv run ruff format --check src/ tests/ app/

typecheck: ## Vérifie la validité des types stricts avec mypy
	uv run mypy --explicit-package-bases src/ app/

test: ## Lance les tests unitaires avec couverture complète
	uv run pytest tests/ -v --cov=src/cleanmatch --cov-report=term-missing --cov-fail-under=80

test-fast: ## Lance les tests et s'arrête au premier échec
	uv run pytest tests/ -x

all: lint typecheck test ## Enchaîne lint, typecheck et tests

check: all ## Alias pour 'all' (CI locale)

run: ## Lance l'application Web locale (Streamlit)
	CLEANMATCH_PRO_MODE=True uv run streamlit run app/streamlit_app.py

run-free: ## Lance l'application Web locale (Streamlit) en mode freemium
	uv run streamlit run app/streamlit_app.py

clean: ## Supprime les fichiers temporaires et les caches
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov .coverage coverage.xml dist/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

digest: ## Génère le digest du projet
	@echo "Génération du digest du projet..."
	uv run --with gitingest gitingest .
	explorer.exe .
