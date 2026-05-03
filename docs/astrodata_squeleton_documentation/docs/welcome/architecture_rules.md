# Architecture & Design Rules

This project follows strict design patterns to ensure scalability, reproducibility, and ease of collaboration.

---

## 📂 Project Structure

A typical AstroData project is organized as follows:

```text
my_project/
├── app/                  # Dashboard (Streamlit)
├── api/                  # Backend (FastAPI)
├── data/                 # Data storage (Git-ignored)
│   ├── raw/              # Immutable source data
│   └── processed/        # Cleaned/Model-ready data
├── src/                  # Reusable Python package
│   └── my_project_pkg/   # Your core logic
└── pyproject.toml        # Dependency management (uv)
```

---

## ⚖️ Core Design Decisions

### 1. `uv` as the Single Source of Truth
- **Rule**: Never use `pip` or `conda` manually.
- **Why**: `uv` ensures that every team member has the exact same environment via `uv.lock`.

### 2. Immutable Raw Data
- **Rule**: Data in `data/raw/` must never be modified or overwritten.
- **Why**: Ensures that experiments can be reproduced from the original source.
- **Workflow**: `raw` → `cleaning script` → `processed`.

### 3. Centralized Path Management
- **Rule**: Avoid hardcoded strings like `"../../data"`.
- **Why**: Code must run identically in a Notebook, a local terminal, or a Docker container.
- **How**:
  ```python
  from my_project_pkg.core.utils.paths import RAW_DATA_DIR
  ```

### 4. Notebooks vs. Source Code
- **Rule**: Use Notebooks for exploration; move tested logic to `src/`.
- **Why**: Notebooks are difficult to version and test. Reusable code belongs in the package.

### 5. Conventional Commits
- **Rule**: Commits must follow the `type: description` format (e.g., `feat:`, `fix:`).
- **Why**: Enables automated changelog generation and versioning.
