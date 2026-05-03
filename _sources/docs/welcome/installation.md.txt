# Installation & Prerequisites

To work on an AstroData project, you need a few core tools installed on your machine. This guide ensures you have everything required to start developing in minutes.

---

## 🛠️ Required Tools

### 1. Git
The version control system used to track changes and collaborate.
- **Install**: [git-scm.com](https://git-scm.com/downloads)

### 2. uv (Min version 0.1.0)
**Your primary tool.** `uv` is an ultra-fast Python package and project manager that replaces `pip`, `virtualenv`, and `pyenv`.
- **Install**:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Verification**: Restart your terminal and run `uv --version`.

### 3. Docker & Docker Compose (Optional)
Used for running your project in isolated containers that match production environments.
- **Install**: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

---

## ⚡ Quick Setup Sequence

Once the tools are installed and you have cloned your project repository:

1. **Install dependencies**:
   ```bash
   make dev-install
   ```
2. **Configure secrets**:
   ```bash
   cp .env.example .env
   # Open .env and add your private keys/tokens
   ```
3. **Verify the installation**:
   ```bash
   make check
   ```
