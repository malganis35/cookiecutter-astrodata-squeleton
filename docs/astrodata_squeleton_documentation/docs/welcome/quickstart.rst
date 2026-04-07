Quickstart Guide
================

Ready to launch? This guide will take you from zero to a running project in minutes.

1. Prerequisites
----------------

Ensure you have the following installed:

*   **uv**: Installation guide: `curl -LsSf https://astral.sh/uv/install.sh | sh`
*   **Docker** (Optional, for production containers)

2. Project Generation
---------------------

Run the following command to generate a new project from the **AstroData Squeleton**:

.. code-block:: bash

   uv run --with cookiecutter cookiecutter git@github.com:malganis35/cookiecutter-astrodata-squeleton.git --directory="data-science"

3. Environment Setup
--------------------

Go to your new project directory and install the development environment:

.. code-block:: bash

   cd my-new-project
   make dev-install

This creates a virtual environment, installs dependencies, and ensures all project directories (`data/`, `models/`, `logs/`) exist.

4. Running the Dashboard
------------------------

To explore your data interactively using Streamlit:

.. code-block:: bash

   make app

5. Running the API
------------------

To serve your model internally:

.. code-block:: bash

   make api

Your API will be available at `http://localhost:8000/docs`.
