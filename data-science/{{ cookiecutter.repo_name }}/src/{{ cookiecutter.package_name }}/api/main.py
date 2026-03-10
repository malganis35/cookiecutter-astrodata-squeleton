from pathlib import Path

from fastapi import FastAPI

from {{ cookiecutter.package_name }}.api.routers import base, greetings, system


def get_project_version() -> str:
    """Get the project version from package metadata or fallback to VERSION file."""
    import importlib.metadata

    try:
        return importlib.metadata.version("{{ cookiecutter.package_name }}")
    except importlib.metadata.PackageNotFoundError:
        version_file = Path(__file__).resolve().parents[3] / "VERSION"
        try:
            return version_file.read_text().strip()
        except Exception:
            return "0.1.0"


app = FastAPI(
    title="{{ cookiecutter.package_name }}",
    description="API for {{ cookiecutter.package_name }} package",
    version=get_project_version(),
)


app.include_router(base.router)
app.include_router(system.router)
app.include_router(greetings.router)


def main() -> None:  # pragma: no cover
    """Run the FastAPI application using uvicorn."""
    import uvicorn

    uvicorn.run("{{ cookiecutter.package_name }}.api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
