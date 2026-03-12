"""System-related routes for the API, such as health and version checks."""

from fastapi import APIRouter, Request

router = APIRouter(tags=["system"])


@router.get("/health")
def health() -> dict[str, str]:
    """Return the health status of the API."""
    return {"status": "ok"}


@router.get("/version")
def version(request: Request) -> dict[str, str]:
    """Return the current version of the application."""
    return {"version": request.app.version}
