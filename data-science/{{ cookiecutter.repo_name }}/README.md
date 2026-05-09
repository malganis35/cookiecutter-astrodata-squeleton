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

## 🚀 CI/CD Configuration

This project is pre-configured with a powerful GitLab CI/CD pipeline that handles testing, security scanning, and automated releases.

### Setting up Automated Releases

To allow the pipeline to automatically bump versions and push tags back to the repository (the `release` job), you must configure two environment variables in GitLab:

1. **`CI_GIT_USERNAME`**: The username that will appear in the automated commits.
2. **`CI_GIT_TOKEN`**: A secure token that gives the pipeline permission to push to your repository.

#### Step 1: Create a Project Access Token
1. In your GitLab project, go to **Settings > Access Tokens**.
2. Click **Add new token**.
3. **Name**: `GitLab CI Release Token` (or similar).
4. **Role**: Select **Maintainer** (required to push to protected branches).
5. **Scopes**: Select **`api`** and **`write_repository`**.
6. Click **Create project access token**.
7. **Important**: Copy the token immediately; you will not be able to see it again!

#### Step 2: Add the Variables to CI/CD
1. Go to **Settings > CI/CD** in your GitLab project.
2. Expand the **Variables** section.
3. Click **Add variable** for the username:
   - **Key**: `CI_GIT_USERNAME`
   - **Value**: `project_{project_id}_bot` (You can find the exact name in the Access Tokens page under "Active project access tokens") or simply your GitLab username.
   - **Type**: Variable
4. Click **Add variable** again for the token:
   - **Key**: `CI_GIT_TOKEN`
   - **Value**: `[Paste the token you copied in Step 1]`
   - **Type**: Variable
   - **Mask variable**: Checked (to hide it in logs).
   - **Protect variable**: Checked (if your `main` branch is protected).

Once configured, the `release` job will automatically trigger on every merge to the main branch, creating a new version, updating the changelog, and pushing a git tag.

## 📁 Project Structure

```text
├── app/                    # Streamlit application
├── dockerfiles/            # Multi-stage Dockerfile
├── docs/                   # Sphinx documentation and reports
├── data/                   # Data directories (tip: use DVC for large files)
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

## 💾 Data Management

By default, the `data/` directory contains subfolders for different stages of your pipeline:
- `raw/`: Original, immutable data dumps. Never modify these.
- `interim/`: Intermediate data that has been transformed.
- `processed/`: Final, canonical datasets ready for modeling.
- `external/`: Data from third party sources.

> **Note**: These directories are ignored by Git (via `.gitignore`) to prevent committing large datasets or sensitive information. We highly recommend using [DVC (Data Version Control)](https://dvc.org/) to version and track your datasets alongside your code.

## 🤝 Contributing
1. Create a feature branch.
2. Follow **Conventional Commits** (`feat:`, `fix:`, `docs:`, etc.).
3. Ensure `make check` passes.
4. Submit a Pull Request.

## 📄 License
This project is licensed under the **{{ cookiecutter.open_source_license }}** license. See the [LICENSE](LICENSE) file for details.
