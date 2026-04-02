"""Main entry point for the FastAPI application."""

from fastapi import FastAPI

from {{ cookiecutter.package_name }}.api.middlewares import LimitUploadSizeMiddleware
from {{ cookiecutter.package_name }}.api.routers import base, greetings, system
from {{ cookiecutter.package_name }}.core.utils import PROJECT_ROOT, ensure_dirs_exist


def get_project_version() -> str:
    """Get the project version from package metadata or fallback to VERSION file."""
    import importlib.metadata

    try:
        return importlib.metadata.version("{{ cookiecutter.package_name }}")
    except importlib.metadata.PackageNotFoundError:
        version_file = PROJECT_ROOT / "VERSION"
        try:
            return version_file.read_text().strip()
        except (FileNotFoundError, PermissionError):
            return "0.1.0"


# Initialize project directories on startup
ensure_dirs_exist()

app = FastAPI(
    title="{{ cookiecutter.package_name }}",
    description="API for {{ cookiecutter.package_name }} package",
    version=get_project_version(),
)

# Global upload size limit middleware
app.add_middleware(LimitUploadSizeMiddleware)


app.include_router(base.router)
app.include_router(system.router)
app.include_router(greetings.router)


def main() -> None:  # pragma: no cover
    """Run the FastAPI application using uvicorn."""
    import uvicorn

    uvicorn.run("{{ cookiecutter.package_name }}.api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
