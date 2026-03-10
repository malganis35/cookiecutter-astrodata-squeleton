# {{ cookiecutter.project_name }}

[![CI](https://github.com/<name>/<repo_name>/actions/workflows/ci.yml/badge.svg)](https://github.com/<name>/<repo_name>/actions)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
{{ cookiecutter.description }}

## 🚀 Features
Here are the main features of this package:
- feature 1
- feature 2

## 🏗️ Architecture
Additionnal information can be found in the [ARCHITECTURE.md](ARCHITECTURE.md) file.

## 🛠️ Installation

1. Clone the repository :
```bash
git clone <GITHUB URL>
cd {{ cookiecutter.repo_name }}
```

2. Install dependencies with [uv](https://github.com/astral-sh/uv):
```bash
uv sync
```

3. Copy the .env.example file to .env and fill it with your values:
```bash
cp .env.example .env
```

## 📖 Usage

1. Launch the application :
```bash
make run
```

2. Webservices: Streamlit & FastAPI (with docker): We provide also for Streamlit and FastAPI a Dockerfile and Docker Compose file.

1. You can launch the webservices with:

```
docker-compose up -d
```

The services are served by default:

- Streamlit App: http://localhost:8501
- FastAPI App: http://localhost:8000

2. You can shut down the services with:

```
docker-compose down
```

## 🛠️ Technological Stack
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![fastapi](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![docker](https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white)

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](#)

![streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![sphinx](https://img.shields.io/badge/Sphinx-F7C942?style=flat&logo=sphinx&logoColor=white)

## 👨💻 Development

Additionnal commands to contribute to the project can be found in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

1. Initialize the development environment:
```bash
make dev
```

2. Verify code quality (Lint/Type/Test):
```bash
make all
```

3. Launch tests quickly:
```bash
make test-fast
```

Project Organization
--------------------

    ├── docker-compose          <- Docker Compose to expose Streamlit and FastAPI as webservices
    ├── LICENSE                 <- Open- or closed-source license if one is chosen
    ├── Makefile                <- Makefile with commands like `make run` or `make run_app`
    ├── README.md               <- The top-level README for developers using this project.
    │
    ├── data
    │   ├── external            <- Data from third party sources.
    │   ├── interim             <- Intermediate data that has been transformed.
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   └── raw                 <- The original, immutable data dump.
    │
    ├── dockerfiles             <- Dockerfile to install the project
    │
    ├── docs                    <- A default Sphinx project; see sphinx-doc.org for details
    │   ├── references          <- Data dictionaries, manuals, and all other explanatory materials.
    │   ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting
    │
    ├── models                  <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                            the creator's initials, and a short `-` delimited description, e.g.
    │                            `1.0-jqp-initial-data-exploration`.
    │
    ├── pyproject.toml          <- Project configuration file with package metadata for
    │                            {{ cookiecutter.package_name }} and configuration for tools like ruff
    │
    ├── src                     <- Source code for use in this project.
    │   │
    │   ├──{{cookiecutter.package_name}}   <- Name of your package
    │   │   ├── __init__.py     <- Makes the package a Python module
    │   │   │
    │   │   ├── data            <- Module to extract / transform / load data
    │   │   │
    │   │   ├── features        <- Module to turn raw data into features for modeling
    │   │   │
    │   │   ├── models          <- Module to train models and then use trained models to make
    │   │   │                    predictions
    │   │   │
    │   │   ├── utils           <- Module for utility functions
    │   │   │
    │   │   └── visualization   <- Module to create exploratory and results oriented visualizations
    │
    ├── .env.template           <- .env file template for credentials
    ├── .gitignore              <- Standard gitignore file for DS project
    ├── .gitlab-ci.yml          <- CI/CD for Gitlab
    └── .pre-commit-config.yaml <- pre-commit config file


## 🤝 Contribution
1. Create a new branch (`git checkout -b feature/my-feature`).
2. Use **Conventional Commits** (`feat:`, `fix:`, `docs:`, etc.).
3. Verify that `make check` passes at 100%.
4. Open a Pull Request.

## 📄 License
This project is under the {{ cookiecutter.open_source_license }} license.
Additionnal information can be found in the [LICENSE](LICENSE) file.
