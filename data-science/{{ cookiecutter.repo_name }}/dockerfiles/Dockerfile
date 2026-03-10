FROM python:{{ cookiecutter.python_version }}-slim

# Install uv from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Install dependencies first to optimize Docker layer caching
# We use uv sync --frozen for reproducibility
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Add a non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONPATH=/app/src
# Ensure the virtualenv created by uv is used
ENV PATH="/app/.venv/bin:$PATH"

# Healthcheck to monitor container status
# Assumes the API has a /health endpoint (confirmed in src/{{ cookiecutter.package_name }}/api/routers/system.py)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the API
CMD ["uvicorn", "{{ cookiecutter.package_name }}.api.main:app", "--host", "0.0.0.0", "--port", "8000"]