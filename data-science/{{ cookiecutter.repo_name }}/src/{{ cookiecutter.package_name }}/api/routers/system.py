from fastapi import APIRouter
from pathlib import Path

router = APIRouter(tags=["system"])

def get_project_version() -> str:
    # Adjusting path to find VERSION at project root
    version_file = Path(__file__).resolve().parents[5] / "VERSION"
    try:
        return version_file.read_text().strip()
    except Exception:
        return "0.1.0"

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/version")
def version():
    return {"version": get_project_version()}
