from fastapi import FastAPI
from {{ cookiecutter.package_name }}.api.routers import system, greetings, base
from pathlib import Path

def get_project_version() -> str:
    version_file = Path(__file__).resolve().parents[3] / "VERSION"
    return version_file.read_text().strip()


app = FastAPI(
    title="{{ cookiecutter.package_name }}",
    description="API for {{ cookiecutter.package_name }}",
    version=get_project_version(),
)


app.include_router(base.router)
app.include_router(system.router)
app.include_router(greetings.router)


def main():  # pragma: no cover
    import uvicorn
    uvicorn.run("{{ cookiecutter.package_name }}.api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
