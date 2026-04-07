# AstroData Onboarding Guide

Welcome to the team! This guide will take you from "I just cloned the repo" to "I generated my first project and ran it" in under 30 minutes, without any side-channel help.

## 👋 1. What is cookiecutter-astrodata-squeleton?

The **AstroData Squeleton** is a **TEMPLATE GENERATOR**, not a project itself. Its purpose is to provide you with a professional, production-ready starting point for data science applications. Think of it as a "blueprint": you run the skeleton once to generate a new project folder (the "generated project"), and then you spend 100% of your time working inside that new folder.

This repository contains two independent templates:
- **`data-science/`**: Use this for 95% of your work. It creates a full environment with a FastAPI backend, a Streamlit dashboard, and a robust data science module.
- **`sphinx-docs/`**: Use this ONLY if you need a separate, standalone documentation website without any data science or API code.

---

## 🛠️ 2. Prerequisites

Before you start, you must have these tools installed on your computer.

- **Git**: The version control system used to track your code changes. [Install here](https://git-scm.com/downloads).
- **uv (Min version 0.1.0)**: An ultra-fast Python package and project manager written in Rust. It replaces `pip`, `virtualenv`, and `pyenv` in one tool. **This is your primary tool.** 
  - Install: `$ curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Docker & Docker Compose (Optional)**: Used to run your project in isolated "containers" that match production perfectly. [Install Desktop here](https://www.docker.com/products/docker-desktop/).
- **Cookiecutter**: You do **not** need to install this separately. It will be invoked automatically through `uv`.

---

## 🏗️ 3. Generating a new Data Science project (step by step)

Follow these 6 steps to create `my_project` from scratch:

**Step 1: Run the skeleton command**
```bash
$ uv run --with cookiecutter cookiecutter git@github.com:malganis35/cookiecutter-astrodata-squeleton.git --directory="data-science"
```
*Why: This downloads the latest template and starts the interactive setup without installing anything permanently on your system.*

**Step 2: Answer the interactive prompts**
Use these values for your first run:
- `project_name`: My Project
- `repo_name`: `my_project`
- `package_name`: `my_project_pkg`
- `author_name`: Your Name
- `author_email`: your.email@example.com
- `install_precommit`: yes
- `initialize_sphinx_documentation`: yes
*Why: This configures your project identity and enables quality controls like linting and automated documentation.*

**Step 3: Post-generation automation**
The hook automatically performs these 5 actions for you:
1. Removes the `LICENSE` file if "No license" was chosen.
2. Removes `.pre-commit-config.yaml` if you opted out of pre-commits.
3. Generates a Sphinx documentation sub-project in `docs/project_documentation/`.
4. Initializes Git, runs `uv sync` to install dependencies, and makes the initial commit.
5. Copies `.env.example` to `.env` for your local settings.
*Why: This ensures you start with a "ready-to-code" project folder already under version control.*

**Step 4: Navigate into the generated project**
```bash
$ cd my_project
```
*Why: You must always run project commands from the root of your newly generated folder.*

**Step 5: Connect to your remote repository**
```bash
# For GitHub
$ git remote add origin https://github.com/your-org/my_project.git
$ git push -u origin main
```
*Why: This backs up your code and allows collaboration with your team.*

**Step 6: Verify the setup**
```bash
$ make check
```
*Why: This runs all quality checks (linting, types, tests) to confirm the project is correctly configured.*

---

## 📖 4. Generating a new Sphinx Documentation project

If you only need a standalone documentation site (without any Data Science code):

```bash
$ uv run --with cookiecutter cookiecutter git@github.com:malganis35/cookiecutter-astrodata-squeleton.git --directory="sphinx-docs"
```
*Why: This uses a different template optimized for text and diagrams. In a standard Data Science project, a `docs/` folder is already generated for you.*

---

## 📂 5. Generated project structure — annotated

Here is what your `my_project` folder structure looks like:

```text
my_project/
├── .github/              # GitHub Actions CI/CD workflows
├── .gitlab/              # GitLab CI/CD pipelines
├── app/                  
│   └── streamlit_app.py  # Your Dashboard (Streamlit)
├── api/                  
│   └── main.py           # Your Backend (FastAPI)
├── data/                 # Raw/Processed data (Git ignored)
│   ├── raw/              # Source data
│   └── processed/        # Model-ready data
├── dockerfiles/          # Recipes for production images
├── src/                  
│   └── my_project_pkg/   # Your reusable Python code
│       ├── core/         # Paths, versioning, and shared logic
│       ├── data_io/      # Loading/saving logic
│       └── models/       # Training/inference logic
├── Makefile              # Your command shortcuts
└── pyproject.toml        # Master dependency list (managed by uv)
```

| Path | Role & Newcomer Notes |
| :--- | :--- |
| `src/my_project_pkg/` | The core package. Any code here is importable in notebooks or APIs. |
| `app/` | The Streamlit data studio. Run it with `make run`. |
| `api/` | The FastAPI server. Access interactive docs at `http://localhost:8000/docs`. |
| `data/raw/` | **Immutable source data**. Never modify files here manually. |
| `.env` | Your private keys and secrets. Never commit this to Git. |
| `Makefile` | The entry point for all dev tasks. Run `make` to see help. |

---

## 🎨 6. Core design decisions

### a. uv as the single dependency manager
- **Rule**: No `pip`, no `conda`, no `virtualenv`.
- **Why**: `uv` is 10x faster and uses `uv.lock` to ensure deterministic builds.
- **Example**: `uv add pandas` updates both your project and your lockfile.
- **Failure**: Using `pip` manually leads to version mismatches across the team.

### b. Immutable raw data pipeline
- **Rule**: Data flows one-way: `raw` → `interim` → `processed`.
- **Why**: Ensures your data science experiments are reproducible.
- **Example**: Use a script to clean `raw` files and save them into `processed`.
- **Failure**: Overwriting raw data means you can never re-verify your source.

### c. Centralized path management
- **Rule**: Never hardcode strings like `"../../data/raw"` or use `os.getcwd()`.
- **Why**: Code should run the same from a notebook, a terminal, or a Docker container.
- **Example**: Use `from my_project_pkg.core.utils.paths import RAW_DATA_DIR`.
- **Failure**: Your code works in Jupyter but crashes in the production API.

### d. Notebooks vs. Source Code
- **Rule**: Notebooks are for exploration; `src/` is for reusable tested code.
- **Why**: Notebooks are hard to test and version. Code in `src/` is clean and professional.
- **Example**: Prototype a model in a notebook, then move the class to `src/my_project_pkg/models/`.
- **Failure**: You end up with 50 undocumented notebooks and no clear model pipeline.

### e. Conventional Commits + Commitizen
- **Rule**: Every commit must start with a type (e.g., `feat:`, `fix:`, `docs:`).
- **Why**: Allows automated generation of the CHANGELOG and version numbers.
- **Example**: `feat: add xgboost model to pipeline`.
- **Failure**: You lose track of which version contains which feature.

---

## 🛠️ 7. Day-to-day workflows

### 7.1 Clone and Setup
```bash
$ git clone <repo_url>
$ make dev-install
$ cp .env.example .env  # Then edit .env with your keys
```

### 7.2 Running Locally
- **Dashboard**: `$ make run` (Visualization and demo).
- **API**: `$ make run_api` (Serving models).

### 7.3 Running with Docker
```bash
$ make docker-build
$ make up
# Explore at http://localhost:8501 (App) and http://localhost:8000/docs (API)
$ make down
```

### 7.4 Working with Data
- Source files go to `data/raw/`.
- Large files (>10MB) should be tracked with **DVC (Data Version Control)**.

### 7.5 Import Pattern in Notebooks
Always use this pattern to access your project code:
```python
from my_project_pkg.core.utils.paths import PROJECT_ROOT, RAW_DATA_DIR
from my_project_pkg.core.data_io import loaders
```

### 7.6 Quality Checks
Run these before every commit:
```bash
$ make format  # Prettifies code
$ make check   # Runs linting, type checks, and tests
```

---

## 📋 8. All Makefile commands — reference table

| Command | What it does | When to use it |
| :--- | :--- | :--- |
| `make install` | `uv sync` (Prod + Dev) | Basic environment setup. |
| `make dev-install` | `uv sync` + pre-commit | First time onboarding. |
| `make run` | Launch Streamlit | Exploring data. |
| `make run_api` | Launch FastAPI | Testing endpoints. |
| `make check` | Full QA (Lint + Type + Test) | Before every push. |
| `make bump` | Version bump (`cz bump`) | Preparing a release. |

---

## 🔐 9. Environment variables reference

| Variable | Required? | Default | Description |
| :--- | :--- | :--- | :--- |
| `API_MAX_UPLOAD_SIZE` | No | 52428800 | Max upload size (50MB) for API files. |
| `GITHUB_TOKEN` | Yes | - | Used by CI/CD workflows. |
| `DATABRICKS_TOKEN` | No | - | Access to remote Databricks clusters. |

---

## ❓ 10. Troubleshooting / FAQ

**Q1: Did the generation work?**
A: Check if `my_project` exists. Move into it and run `ls -a`. If no error appeared at the end of the command, it worked.

**Q2: uv is not found**
A: Restart your terminal. If it still fails, ensure your `~/.local/bin` is in your PATH.

**Q3: Import error in Notebook**
A: Ensure you ran `make dev-install` and restarted your Jupyter kernel.

**Q4: API returns 500 errors**
A: Check terminal logs. Ensure your `.env` is correctly filled and data is in `data/raw/`.

**Q5: Data files are too large**
A: These are ignored by Git. Use DVC or a shared bucket for large datasets.

---

## 🤝 11. Contributing to the skeleton
To improve the skeleton itself:
- **Validate**: `$ make validate` (generates a test project).
- **Digest**: `$ make digest` (creates context for LLMs).
- **Release**: `$ make bump` then `$ make release`.
