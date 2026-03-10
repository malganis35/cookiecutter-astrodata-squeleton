# {{ cookiecutter.project_name }}

[![CI](https://github.com/<name>/<repo_name>/actions/workflows/ci.yml/badge.svg)](https://github.com/<name>/<repo_name>/actions)
[![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![License: {{ cookiecutter.open_source_license }}](https://img.shields.io/badge/License-{{ cookiecutter.open_source_license }}-yellow.svg)](LICENSE)

## 📝 Description
{{ cookiecutter.description }}

## 🚀 Key Features
- **FastAPI Backend**: High-performance REST API with automated OpenAPI documentation.
- **Streamlit Frontend**: Interactive dashboard for data exploration and visualization.
- **UV Powered**: Lightning-fast dependency management and reliable reproducibility.
- **Dockerized**: Multi-stage Dockerfile and Compose setup for seamless deployment.
- **CI/CD Ready**: Pre-configured pipelines for both GitHub Actions and GitLab CI.
- **Quality Ensured**: Integrated with Ruff (linting), MyPy (typing), and Pytest (testing).

## 🏗️ Architecture
Detailed architectural information can be found in the [ARCHITECTURE.md](ARCHITECTURE.md) file.

## 🛠️ Getting Started

### Prerequisites
- [uv](https://github.com/astral-sh/uv) (version 0.5+)
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) (optional, for containerization)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <YOUR_REPO_URL>
   cd {{ cookiecutter.repo_name }}
   ```

2. **Initialize the project**:
   Use the Makefile to set up your environment (creates venv and installs hooks):
   ```bash
   make dev-install
   ```

3. **Configure the environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your specific configurations
   ```

## 📖 Usage

### Running Locally
You can run the Streamlit app or the API separately using `uv` or the provided Makefile shortcuts:

- **Launch Streamlit**: `make run` (serves at http://localhost:8501)
- **Launch API**: `make run_api` (serves at http://localhost:8000)

### Running with Docker
To launch both services (API + Streamlit) concurrently in containers:
```bash
make up
```
- **Streamlit App**: http://localhost:8501
- **FastAPI Docs**: http://localhost:8000/docs

To stop the services:
```bash
make down
```

## 🧪 Development & Quality

Maintain high code standards using the following commands:

- **Run all checks**: `make check` (Lint + Type + Test)
- **Format code**: `make format`
- **Run tests only**: `make test`
- **Stop on first test failure**: `make test-fast`

## 📁 Project Structure

```text
├── app/                    # Streamlit application
├── dockerfiles/            # Multi-stage Dockerfile
├── docs/                   # Sphinx documentation and reports
├── src/                    # Main source code
│   └── {{ cookiecutter.package_name }}/
│       ├── api/            # FastAPI implementation
│       ├── data/           # ETL / Data processing
│       ├── features/       # Feature engineering
│       ├── models/         # Model training/inference
│       └── visualization/  # Plotting utilities
├── tests/                  # Unit and integration tests
├── .env.example            # Environment variables template
├── docker-compose.yml      # Orchestration for API & App
├── Makefile                # Useful development shortcuts
└── pyproject.toml          # Project metadata and tool config
```

## 🤝 Contributing
1. Create a feature branch.
2. Follow **Conventional Commits** (`feat:`, `fix:`, `docs:`, etc.).
3. Ensure `make check` passes.
4. Submit a Pull Request.

## 📄 License
This project is licensed under the **{{ cookiecutter.open_source_license }}** license. See the [LICENSE](LICENSE) file for details.
