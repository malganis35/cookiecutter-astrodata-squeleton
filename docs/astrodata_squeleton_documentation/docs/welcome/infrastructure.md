# Infrastructure & Data Access

This project relies on several external services for data management and computation. This guide explains how to get access.

---

## 💾 Data Management (DVC)

We use **DVC (Data Version Control)** for large files that should not be stored in Git.

- **Storage**: Data is stored in [S3/Azure Blob/Local Remote].
- **Authentication**:
  - [Instructions for `dvc remote modify --local` login].
- **Common commands**:
  ```bash
  dvc pull   # Download data for the current branch
  dvc status # Check if your local data is up to date
  ```

---

## 🚀 Computation (Databricks)

For heavy workloads, the project is configured to interact with Databricks.

- **Token**: You need a Personal Access Token (PAT).
- **Setup**:
  1. Go to Databricks → User Settings → Developer.
  2. Generate a token.
  3. Add it to your `.env` file: `DATABRICKS_TOKEN=dapi_xxxx...`.

---

## ⚙️ Environment Variables

The project uses a `.env` file for local configuration. Never commit this file to Git.

| Variable | Required? | Description |
| :--- | :--- | :--- |
| `DATABRICKS_TOKEN` | No | Required for remote execution. |
| `API_MAX_UPLOAD_SIZE` | No | Limits technical payloads for the FastAPI. |
| `GITHUB_TOKEN` | Yes | Required for certain CI/CD actions. |
