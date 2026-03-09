from fastapi import FastAPI
from {{ cookiecutter.package_name }}.app.routes import router
from pathlib import Path

def get_project_version() -> str:
    version_file = Path(__file__).resolve().parents[3] / "VERSION"
    return version_file.read_text().strip()


app = FastAPI(
    title="{{ cookiecutter.package_name }}",
    description="API for {{ cookiecutter.package_name }}",
    version=get_project_version(),
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": Path("VERSION").read_text().strip()}


app.include_router(router)
