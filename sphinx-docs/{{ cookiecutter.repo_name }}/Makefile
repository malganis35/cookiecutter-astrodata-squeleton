# Minimal makefile for Sphinx documentation

# Put it first so that "make" without argument is like "make help".
help_sphinx:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help_sphinx Makefile

#################################################################################
# GLOBALS                                                                       #
#################################################################################
# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

PYTHON_VERSION= 3.12
PROJECT_NAME= kdoc

# Source for a good Python Makefile: https://gist.github.com/genyrosk/2a6e893ee72fa2737a6df243f6520a6d

# Colors for echos
ccend=$(shell tput sgr0)
ccbold=$(shell tput bold)
ccgreen=$(shell tput setaf 2)
ccred=$(shell tput setaf 1)
ccso=$(shell tput smso)

#################################################################################
# HELP (default) - shows all available make commands
#################################################################################
.PHONY: help .env
help: .env
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## ' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

#################################################################################
# COMMANDS (SETUP)                                                            #
#################################################################################

check-env: ## Check if uv and xelatex are installed
	@echo "$(ccso)--> Checking environment dependencies...$(ccend)"
	@command -v uv >/dev/null 2>&1 || { echo "$(ccred)ERROR: uv is not installed. Please install it first.$(ccend)"; exit 1; }
	@command -v xelatex >/dev/null 2>&1 || { echo "$(ccred)ERROR: xelatex is not installed. PDF builds will fail. Please run 'make latex_setup'.$(ccend)"; exit 1; }
	@echo "$(ccgreen)Environment check passed. Ready to build!$(ccend)"

dev-install: ## Install Python Dependencies (Dev)
	@echo "$(ccso)--> Install Python Dependencies (Dev)$(ccend)"
	uv sync

## Install latex dependencies
latex_setup:
	sudo apt update
	sudo apt install texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk
	sudo apt install fontconfig
	sudo apt install fonts-liberation
 ## Install Devbox (https://devbox.sh/)
devbox-install:
	@echo "$(ccso)--> Install Devbox$(ccend)"
	curl -fsSL https://get.jetify.com/devbox | bash

## Install uv
uv-install:
	@echo "$(ccso)--> Install uv$(ccend)"
	curl -LsSf https://astral.sh/uv/install.sh | sh
	@echo "Note: restart your terminal or run: source ~/.bashrc or source ~/.zshrc"

install: devbox-install uv-install ## Install Devbox, uv
	@echo "$(ccso)--> Initiating isolated shell dev environment$(ccend)"
	devbox shell

#################################################################################
# COMMANDS (SPHINX)                                                         #
#################################################################################

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@uv run $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

## Delete all compiled _build/ folder
clean:
	@echo "Delete _build directory"
	-rm -r "$(BUILDDIR)"
	-find . -type f -name "*.py[co]" -delete
	-find . -type d -name "__pycache__" -delete
	-find . -name '*.egg-info'  -type d -exec rm -rf {} +
	-rm -rf .venv/
	-rm -rf _artifact/ .devbox/ .pytest_cache/ .ruff_cache/ node_modules/
	-rm .coverage package.json package-lock.json digest.txt zz_git-diff.txt

## Automatically generate HTML documentation
livehtml:
	@uv run sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) --port=8001

## PDF Build with LateX
pdf_build: check-env
	- echo "$(ccso)--> Building PDF with LaTeX$(ccend)"
	- make latexpdf LATEXMKOPTS="-interaction=nonstopmode"
	- cp ./_build/latex/astrodata_documentation.pdf ./_build/

## PDF Build with SimplePDF
simplepdf_build:
	- make simplepdf

#################################################################################
# COMMANDS (CODE QUALITY & BUILD)                                               #
#################################################################################

bump: ## Bump the version using commitizen
	@echo "$(ccso)--> Bump the version using commitizen$(ccend)"
	@uv run cz bump
	@echo "Note: don't forget to push the new tag to the remote repo with: git push --tags"

cz-commit: ## Commit your changes using commitizen
	@echo "$(ccso)--> Commit your changes using commitizen$(ccend)"
	@uv run cz commit

pc: ## Run pre-commit hooks
	@echo "$(ccso)--> Run pre-commit hooks$(ccend)"
	@uv run pre-commit run --all-files

digest: ## Generate a digest of the repository
	@echo "$(ccso)--> Generate a digest of the repository$(ccend)"
	@uv run --with gitingest gitingest .
	@echo "Digest saved to digest.txt"

#################################################################################
# Reporting Author Articles                                                     #
#################################################################################

## Extract reporting author articles
extract_reporting:
	- echo "$(ccso)--> Extracting reporting author articles$(ccend)"
	- python extract_authors.py
