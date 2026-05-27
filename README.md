# Astrodata Squeleton (Cookiecutter)

> **A professional, opinionated collection of project templates for Data Science and Documentation.**

This repository provides a standardized, robust starting point for your work, ensuring best practices (linting, tests, containerization) from day one.

---

## 🚀 How to start a new project

We use **`uv`** to run Cookiecutter without installing it globally. Choose the template that matches your needs:

### 1. Data Science Project (The Core)
Includes FastAPI, Streamlit, DVC, and structured `src/` folder.

```bash
uv run --with cookiecutter cookiecutter https://github.com/malganis35/cookiecutter-astrodata-squeleton.git --directory="data-science"
```

### 2. Standalone Documentation
Optimized project for Sphinx documentation only (no data science code).

```bash
uv run --with cookiecutter cookiecutter https://github.com/malganis35/cookiecutter-astrodata-squeleton.git --directory="sphinx-docs"
```

---

## 🛠️ Requirements

- **[uv](https://github.com/astral-sh/uv)**: The ultra-fast Python project manager.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 📖 Full Documentation

For more detailed guides on core design decisions, daily workflows, and troubleshooting, visit our **[Onboarding Portal](docs/astrodata_squeleton_documentation/index.rst)**.

---

## 💡 Quick Tips

You can add aliases to your shell (`.bashrc` or `.zshrc`) for even faster generation:

```bash
alias ds-make='uv run --with cookiecutter cookiecutter https://github.com/malganis35/cookiecutter-astrodata-squeleton.git --directory="data-science"'
alias docs-make='uv run --with cookiecutter cookiecutter https://github.com/malganis35/cookiecutter-astrodata-squeleton.git --directory="sphinx-docs"'
```

