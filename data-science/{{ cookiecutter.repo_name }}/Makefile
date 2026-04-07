# Makefile for the {{ cookiecutter.project_name }} project

.PHONY: help install dev-install format lint typecheck test test-fast all check run clean up down digest bump release

.DEFAULT_GOAL := help

###################################################################
# SETUP
###################################################################

install: ## Install dependencies via uv (prod + dev)
	uv sync

dev-install: install ## Install dependencies and pre-commit hooks
	uv run pre-commit install

###################################################################
# RUN
###################################################################

run: ## Launch the local web application (Streamlit)
	uv run streamlit run app/streamlit_app.py

run_api: ## Launch the API
	uv run {{ cookiecutter.package_name }}-api

up: ## Start the API and Streamlit app concurrently
	docker-compose up -d

down: ## Stop the API and Streamlit app
	docker-compose down

docker-build: ## Build Docker images with OCI labels
	BUILD_VERSION=$$(cat VERSION) \
	BUILD_REVISION=$$(git rev-parse HEAD 2>/dev/null || echo "unknown") \
	BUILD_DATE=$$(date -u +%Y-%m-%dT%H:%M:%SZ) \
	docker-compose build

docker-inspect: ## Inspect OCI labels of the built image
	@docker inspect --format='{{"{{"}}json .Config.Labels{{"}}"}}' {{ cookiecutter.repo_name }}-api | python3 -m json.tool

###################################################################
# CODE QUALITY
###################################################################

all: lint typecheck test ## Run lint, typecheck, and tests in sequence

check: all ## Alias for 'all' (local CI)

format: ## Format the code with ruff
	uv run ruff check --fix src/ tests/ app/
	uv run ruff format src/ tests/ app/

lint: ## Check code cleanliness with ruff (check + format)
	uv run ruff check src/ tests/ app/
	uv run ruff format --check src/ tests/ app/

typecheck: ## Check strict type validity with mypy
	uv run mypy --explicit-package-bases src/ app/

test: ## Run unit tests with full coverage
	uv run pytest tests/ -v

test-fast: ## Run tests and stop at the first failure
	uv run pytest tests/ -x

###################################################################
# DEV
###################################################################

clean: ## Remove temporary files and caches
	rm -rf .venv
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov .coverage coverage.xml dist/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Cleaned environment caches and .venv"

digest: ## Generate the project digest
	@echo "Generating project digest..."
	uv run --with gitingest gitingest .
	@$(OPEN) .

bump: ## Bump the project version (using commitizen)
	uv run cz bump

release: ## Push the latest commits and tags to origin main
	git push origin main --follow-tags
	git push --tags

###################################################################
# HELP
###################################################################

help: ## Display this help
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

###################################################################
# UTILS
###################################################################

# 1. Detect the OS
ifeq ($(OS),Windows_NT)
    OPEN := explorer.exe
else
    # 2. If Linux, check if it's WSL
    UNAME_S := $(shell uname -s)
    IS_WSL := $(shell grep -i microsoft /proc/version 2>/dev/null)

    ifeq ($(UNAME_S),Darwin)
        OPEN := open
    else ifneq ($(IS_WSL),)
        # If WSL, we can use the explorer from Windows
        OPEN := explorer.exe
    else
        OPEN := xdg-open
    endif
endif