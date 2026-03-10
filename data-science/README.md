# 🧪 AstroData - Data Science Squeleton

This directory contains a **Cookiecutter** template designed to jumpstart Data Science projects with best practices in mind. It provides a robust starting point with integrated API (FastAPI), Visualization (Streamlit), and modern environment management (UV).

## 🚀 Quick Start

To generate a new project using this template, ensure you have [uv](https://github.com/astral-sh/uv) and [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed.

Run the following command from your terminal:

```bash
uv tool run cookiecutter https://github.com/malganis35/cookiecutter-astrodata-squeleton.git --directory data-science
```

## 🛠️ Main Features

The generated project includes:
- **FastAPI**: A high-performance web API with automated documentation.
- **Streamlit**: A powerful dashboard for data exploration and visualizations.
- **UV Integration**: Lightning-fast dependency management and reproducibility.
- **Docker Support**: Multi-stage Dockerfile and Compose for easy containerization.
- **CI/CD Ready**: Pre-configured pipelines for GitLab CI and GitHub Actions.
- **Quality Tools**: Ruff for linting/formatting, MyPy for type checking, and Pytest for testing.

## 📁 Template Structure

- `{{ cookiecutter.repo_name }}/`: The project template itself.
- `cookiecutter.json`: Configuration for template variables.
- `hooks/`: Post-generation scripts to initialize Git and clean up optional files.
