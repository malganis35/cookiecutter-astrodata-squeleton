Data Science Template
======================

The `data-science` template is the core of this meta-project. It follows a modular structure inspired by best industry practices.

Folder Structure
----------------

.. code-block:: text

    ├── .github/          # GitHub Actions CI/CD workflows
    ├── .gitlab/          # GitLab CI/CD pipelines
    ├── app/              # Streamlit dashboard
    ├── api/              # FastAPI model serving
    ├── data/             # Local data storage (Git ignored)
    │   ├── external/
    │   ├── interim/
    │   ├── processed/
    │   └── raw/
    ├── dockerfiles/      # Optimized Docker images
    ├── models/           # Trained models (Git ignored)
    ├── notebooks/        # Jupyter notebooks for EDA and experimentation
    ├── src/              # Main project source code
    │   └── {{ package_name }}/
    │       ├── core/     # Core logic and utilities
    │       ├── model/    # Model training and prediction
    │       └── ...
    ├── tests/            # Pytest test suite
    ├── Makefile          # Automation tasks
    ├── pyproject.toml    # Dependency management
    └── README.md         # Project documentation

Core Concepts
-------------

-   **Separation of Concerns**: Logic is in `src/`, UI is in `app/`, API is in `api/`.
-   **Reproducible Environment**: `uv.lock` ensures every developer uses the exact same versions.
-   **Docker Ready**: Multi-stage Dockerfiles for optimized production builds.

The Makefile
------------

The `Makefile` is your main entry point for automation:

-   `make dev-install`: Setup virtual env and project dirs.
-   `make check`: Run Ruff (lint) and Mypy (types).
-   `make test`: Run all tests with coverage.
-   `make api`: Launch the FastAPI server.
-   `make app`: Launch the Streamlit dashboard.
