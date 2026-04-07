Docker & CI/CD
==============

The AstroData Squeleton is built for **continuous integration and delivery** (CI/CD). Using Docker, you can ensure your project runs exactly the same in development, staging, and production.

Dockerization
-------------

Our `Dockerfile` follows **OCI (Open Container Initiative) standards** for image traceability.

-   **Multi-stage builds**: Keep production images slim.
-   **Traceability labels**: Metadata about the project version, build date, and git revision are embedded into the image.

Building the image:

.. code-block:: bash

   make docker-build

Inspecting labels:

.. code-block:: bash

   make docker-inspect

CI/CD Pipelines
---------------

The template includes pre-configured CI/CD workflows for both **GitLab** and **GitHub**.

GitLab CI (.gitlab-ci.yml)
---------------------------

-   **Test Stage**: Runs Ruff, Mypy, and Pytest.
-   **Release Stage**: Builds a production Docker image and pushes it to your GitLab Container Registry.
-   **Auto-tagging**: The image is automatically tagged with the branch name or commit SHA.

GitHub Actions (.github/workflows/ci.yml)
-----------------------------------------

-   **Lint & Type**: Automated quality checks on every PR.
-   **CI Workflow**: Automated testing and Docker builds.
-   **GitHub Packages**: Publishes production images to GHCR (GitHub Container Registry).

Continuous deployment or specialized infrastructure (Azure, AWS) can be configured within these templates.
