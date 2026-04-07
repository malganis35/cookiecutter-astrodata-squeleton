Best Practices
==============

AstroData Squeleton is built for **maintainable, testable, and robust** code. Following these practices will help you keep your projects healthy.

1. Dependency Management
------------------------

-   Always use `uv` instead of standard `pip`.
-   Commit `uv.lock` to ensure all developers use identical dependencies.
-   Add dependencies with `uv add` to automatically keep `pyproject.toml` updated.

2. Code Quality
---------------

The project uses **Ruff** for high-performance linting and formatting. Run it often with:

.. code-block:: bash

   make check

3. Type Checking
----------------

Maintain type annotations for your functions to catch errors early. **Mypy** checks your code statically:

.. code-block:: bash

   make typecheck

4. Testing
----------

-   Place tests in the `tests/` directory.
-   Use `pytest` for all project-level tests.
-   Ensure high coverage for `src/` logic.
-   Run tests manually with `make test`.

5. Environment Variables
------------------------

-   External configuration (database URLs, API keys) should go into a `.env` file (not committed to Git).
-   Use `os.getenv()` or `pydantic-settings` to load them in your app.

6. Commit Standards
-------------------

-   Use a consistent commit message format (e.g., Conventional Commits).
-   Run pre-commit hooks before pushing: `make pc`.
