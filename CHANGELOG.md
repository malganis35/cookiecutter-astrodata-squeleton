## v0.3.0 (2026-05-27)

### Feat

- implement post-generation dependency installation and cleanup using uv
- add CI/CD configuration section to README for automated releases
- add pip-licences to depedency-groups packages
- **trivy**: add .trivyignore file to manage CVEs for Debian 12
- **ci**: enhance GitLab CI configuration with improved rules, added security scans, and refined job stages
- **ci**: update GitLab CI configuration to enhance release rules and improve Trivy scan integration
- **ci**: enhance GitLab CI configuration with security scans and type checking
- add customizable VSCode color themes and reorder CI pipeline stages
- remove documentation CI/CD files when Sphinx is disabled
- add automated Sphinx documentation workflows for both GitHub Actions and GitLab CI/CD
- initialize astrodata documentation skeleton with Sphinx configuration, GitLab templates, and CI/CD workflows
- implement centralized project versioning utility and display version in Streamlit app
- add OCI build labels and dynamic build arguments to Docker configuration
- add function to copy .env file during project initialization

### Fix

- **commitizen**: remove [skip ci] from bump_message in pyproject.toml for data-science
- **init_git**: update initial commit message to follow convention
- **commitizen**: remove [skip ci] from bump_message in pyproject.toml
- **dependencies**: update setuptools and wheel versions in pyproject.toml
- **docker**: update uv version in Dockerfile and optimize package installation
- **ci**: streamline CI pipeline by removing unnecessary build-devcontainer stage and updating Docker images
- **commitizen**: add [skip ci] to bump message for versioning
- add JUnit XML report option to pytest and set version for commitizen
- **docs**: remove unnecessary --frozen flag from uv sync command in build_docs stage
- **ci**: install git in documentation runner and update pages deployment script
- append -docs suffix to sphinx project repo name to prevent uv workspace conflicts
- set GIT_DEPTH to 0 and update documentation build commands to use project-specific uv environments

### Refactor

- improve readability of docker build command in GitLab CI configuration
- simplify CI matrix configurations to use the configured cookiecutter python version directly
- inline python version matrix generation into CI workflow templates
- decompose python version logic into separate major and minor variables in cookiecutter.json
- remove python_interpreter field and dynamically generate python_matrix based on python_version
- update st.dataframe width parameter to use_container_width in Streamlit app

## v0.2.0 (2026-04-03)

### Feat

- initialize project version and pyproject configuration files
- add bump and release targets to Makefile for automated versioning and deployment
- add conditional configuration for Furo theme options in Sphinx conf.py
- add python_interpreter and author_email fields to cookiecutter templates and update post-generation hooks
- initialize cookiecutter template for Sphinx documentation projects with CI/CD and issue templates
- add unit tests for directory initialization in paths utility
- implement dynamic project root discovery by searching for pyproject.toml
- cache CSS file loading in streamlit_app.py to optimize I/O performance
- add middleware to enforce maximum request upload size limit via environment configuration
- add validate target to Makefile for template generation testing
- export core utility constants and functions in package init file
- add EDA notebook template and configure nbstripout pre-commit hook
- centralize path management and automate project directory initialization on startup
- add Makefile for project ingestion and standardize editor configurations
- add regex validation for cookiecutter python version format in pre-gen hook
- add project_url variable to cookiecutter configuration and pyproject.toml template
- add author_email field to cookiecutter template and pyproject.toml
- implement global uv cache in GitLab CI and fix typo in ARCHITECTURE.md
- Run `uv sync` after git initialization, remove docs cleanup on error, and reduce Streamlit's `maxUploadSize` to 50.
- Implement dataframe sanitization to avoid Arrow serialization errors and update `st.dataframe` width and Pygwalker `themeKey` parameters.
- Update project configuration and dependencies in `pyproject.toml`.
- Add logic to detect new dataset uploads, reset the PyG renderer, and manage the current file object in session state.
- Add comprehensive architecture documentation including system overview, component breakdown, data flow, and technical stack.
- update GitLab CI jobs to use `uv run --group dev` instead of `--extra` for linting, formatting, and testing.
- add OS-aware `OPEN` command for cross-platform directory browsing in Makefile.
- add data science Cookiecutter template README.
- add `curl` as a system dependency in the Dockerfile
- Specify `ubuntu-latest` runner for the CI tests job.
- implement French greeting, improve version retrieval using package metadata, and configure base router with prefix and tags.
- Introduce multi-stage Dockerfile for API and Streamlit services and configure them in docker-compose.yml with health checks and development watches.
- Improve Dockerfile with multi-stage uv installation, reproducible dependency sync, non-root user, and healthcheck.
- improve consistency in import version on test files
- **pyproject**: reorganize package
- update version of precommit hook
- improve gitlab and github ci
- add data-science/{{ cookiecutter.repo_name }}/app/assets/pygwalker_config.json
- correct - in cookiecutter name from user
- add default goal in makefile to help
- improve makefile
- improve mypy
- add optimization on streamlit and docker and fastapi
- improve logic in routers, makefile and streamlit app
- add generic company logo
- remove __init__.py file from coverage report
- improve coverage test of actual code
- add version file
- add template for github/gitlab board
- implement initial Streamlit data studio application with PyGWalker integration and update pyproject.toml.
- add unit test for api
- add figure folder in docs/
- update readme
- update licence
- correct hooks
- improve data science squeleton with hooks
- initialize data science cookiecutter squeleton
- initialize readme
- add licence
- add pre-commit config
- add gitattributes
- add gitignore

### Fix

- ensure version string is explicitly cast to str when reading from file
- update PDF filename in Makefile to match documentation naming convention
- cast environment variable default to string to prevent type errors in upload size middleware
- improve error handling and reporting during documentation generation in post-gen hook
- escape python-version in ci.yml to ensure literal output in generated workflow.
- Update cookiecutter template URL from SSH to HTTPS for cloning.
- make `explorer.exe` call in `digest` Makefile target optional
- correct jinja variable
- optimize streamlit app and test fallback
- correct mismatch in jinja variable
- missing jinja variable
- missing jinja variable
- missing jinja variable
- correct meta data for streamlit app
- remove old config for streamlit
- docker compose
- correct unit test for api on package
- correct package relative import
- correct variable cookiecutter in dockerfile
- package name
- update `pyproject.toml`.
- update license variable name in README.

### Refactor

- remove trailing whitespace from project root test file
- clean up code formatting and imports across source and test files
- clean up imports and improve type hinting in API and utility modules
- improve code documentation and type hinting across middleware and utility modules
- add type hints and imports to LimitUploadSizeMiddleware dispatch and init methods
- migrate restart policy to deploy configuration in docker-compose.yml
- change .env.example filename
- encapsulate hook execution in main functions and update docker-compose restart policy configuration
- replace broad exception handling with specific error types in API versioning and file parsing
- use temporary directory for sphinx-docs generation to prevent path conflicts
- remove unused shutil import in post-generation hook
- simplify python_matrix structure in cookiecutter configuration
- update README with detailed features, streamlined installation/usage via Makefile, dedicated development section, and simplified project structure.
- Remove `isLastMessage` prop and `ContinueResponse` component from chat message actions.
- dynamically configure Python version matrix in CI/CD pipelines using a cookiecutter variable.
- translate comments in `test_version_fallback.py` from French to English.
- update `st.dataframe` width parameter from `width="stretch"` to `use_container_width=True`.
- replace `subprocess.call` with `subprocess.run` and add `check=True` for robust git initialization.
- Translate comments, documentation, and project instructions to English, and update API test paths and post-generation messages.
- rename functional folder
- ruff format correction
- remove .cz.yaml file
- package organization
