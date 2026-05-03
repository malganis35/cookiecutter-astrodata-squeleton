# Daily Workflow & Commands

This guide covers the most frequent tasks you will perform while developing on this project.

---

## 🚀 Running the Project

### Local Development
- **Dashboard**: `make run` (Streamlit visualization).
- **API**: `make run_api` (FastAPI backend).
- **Notebooks**: Launch your preferred IDE (VS Code, Cursor) and open any file in `notebooks/`.

### Docker (Production-like)
```bash
make docker-build  # Build images
make up            # Start all services
make down          # Stop all services
```

---

## 🧪 Quality Control

Before pushing any code, ensure it meets the project standards:

| Command | Purpose |
| :--- | :--- |
| `make format` | Automatically fix linting and formatting issues. |
| `make check` | Run all tests, type checks, and linters. |
| `make test` | Run only the unit tests. |

---

## 🤝 Contribution Process

1. **Create an Issue**: Use our GitLab templates to describe the task.
2. **Branching**: `git checkout -b feat/your-feature-name`.
3. **Commit**: Use `feat:` or `fix:` prefixes (or run `uv run cz c`).
4. **Merge Request**: Push your branch and open an MR using the **MR Template**. It includes a checklist and Mermaid diagram support.
