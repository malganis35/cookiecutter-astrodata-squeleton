# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **monorepo of three independent Cookiecutter templates**. There is almost no application code here — the "product" is the templates and their generation hooks. Each template is a top-level directory containing its own `cookiecutter.json`, a `{{ cookiecutter.repo_name }}/` payload directory, and a `hooks/` directory.

| Directory | Generates | Notes |
|---|---|---|
| `data-science/` | A Python data-science project (FastAPI + Streamlit + `src/` layout, uv, Docker, GitLab CI + GitHub Actions) | The core template; can recursively generate the docs template |
| `sphinx-docs/` | A standalone Sphinx documentation project (furo / sphinx_book_theme / alabaster) | Also invoked as a child by `data-science` |
| `claude-setup/` | A `.claude/` folder scaffold (settings, hooks, an agent, a skill, `.mcp.json`) | `repo_name` defaults to `.claude` |

`docs/astrodata_squeleton_documentation/` is **not a template** — it is a committed, generated instance of `sphinx-docs` that serves as the onboarding portal and is deployed to GitHub Pages by `.github/workflows/deploy-docs.yml` on changes under that path.

## Working on the templates

- Payload files are **Jinja2 templates**. Paths like `src/{{ cookiecutter.package_name }}/` are rendered at generation time. The `hooks/*.py` files are **themselves rendered** — you will see literals like `"{{ cookiecutter.open_source_license }}"` compared against strings inside Python code.
- Cookiecutter prompt choices are ordered lists in `cookiecutter.json`; the first entry is the default used by `--no-input`.
- After editing a template, regenerate to verify. There is no unit test suite for the templates.

```bash
make validate          # generates data-science with --no-input into ./tmp_test, then deletes it
```

```bash
# Generate any template locally with defaults, keeping the output for inspection:
uvx cookiecutter data-science --no-input -o ./tmp_test --overwrite-if-exists
uvx cookiecutter sphinx-docs  --no-input -o ./tmp_test --overwrite-if-exists
uvx cookiecutter claude-setup --no-input -o ./tmp_test --overwrite-if-exists
```

### Cross-template coupling (important)

`data-science/hooks/post_gen_project.py` → `generate_nested_project()` calls Cookiecutter **again on the `sphinx-docs` template, fetched from the public GitHub URL** (`https://github.com/malganis35/cookiecutter-astrodata-squeleton.git`, `--directory sphinx-docs`), not from the local checkout. Consequences:

- Local edits to `sphinx-docs/` are **not** reflected when generating `data-science` with Sphinx docs enabled until they are pushed to GitHub `main`.
- The child project's `repo_name` gets a `-docs` suffix (`generate_nested_project`) to avoid a `uv` workspace name collision with the parent package. The result is copied into `docs/project_documentation/` of the generated project.
- Generation must run in an environment where `cookiecutter` is importable at hook runtime (`uvx cookiecutter` / `uv run --with cookiecutter` provide this).

### What the `data-science` post-gen hook does (in order)

`remove_licence` → `remove_precommit` → `apply_vscode_color_theme` (rewrites `.vscode/settings.json`, maps theme name → hex) → `initiate_docs` (nested Sphinx gen if `initialize_sphinx_documentation == yes`) → `remove_docs_ci` → `install_dependencies` (parses `requirements.txt` / `requirements-dev.txt`, runs `uv add` / `uv add --dev`, then **deletes** those files) → `init_git` (`git init -b main`, `uv sync`, initial commit `feat: initial commit`) → `copy_env_file` (`.env.example` → `.env`).

`data-science/hooks/pre_gen_project.py` validates the `python_version` format (`X.Y.Z`) and aborts on mismatch.

`claude-setup/hooks/post_gen_project.py` moves the generated `.mcp.json` from `.claude/` up to the project root (Claude Code convention), unless one already exists there.

## Repo maintenance commands

This repo is versioned with Commitizen and **conventional commits are required** (enforced in generated projects' CI; follow the convention here too).

```bash
make bump       # uv run --with commitizen cz bump  (updates pyproject version + CHANGELOG.md)
make release    # git push origin main --follow-tags
make digest     # gitingest . (note: root Makefile also runs `explorer.exe .` — a WSL-ism)
make clean      # remove caches and .venv
```

## Commands inside a generated `data-science` project

These come from `data-science/{{ cookiecutter.repo_name }}/Makefile` — relevant when editing that template or debugging generated output:

```bash
make dev-install   # uv sync + pre-commit install
make lint          # ruff check + ruff format --check  (src/ tests/ app/)
make typecheck     # mypy --explicit-package-bases (strict mode, pydantic plugin)
make test          # pytest -v  (coverage gate: --cov-fail-under=80)
make test-fast     # pytest -x
make all / check   # lint + typecheck + test
make run           # streamlit run app/streamlit_app.py  (:8501)
make run_api       # <package>-api entrypoint  (:8000)
make up / down     # docker-compose
```

Run a single test in that project: `uv run pytest tests/unit_test/test_api.py::test_name -v`.

Ruff config there: line length 120; lint rule sets `F,E,W,B,I,UP,SIM,ERA,C,D,ANN` (docstrings and annotations enforced).

## Generated-project CI model (GitLab)

`data-science/{{ cookiecutter.repo_name }}/.gitlab-ci.yml` stages: `check` (ruff lint/format, mypy, `pip-licenses` copyleft gate, `cz check` on MRs) → `test` (pytest+coverage, multi-version pytest matrix, Trivy fs scan) → `release` (on `main`, `cz bump --yes --changelog`, pushes tag — skips its own bump commit to avoid loops) → tag-triggered `build-project` / `security-scan` / `push-project` (wheel + Docker image build, Trivy image scan, registry push, Cosign keyless signing, PyPI publish) → `deploy` (`pages` builds `docs/project_documentation/` with Sphinx).
