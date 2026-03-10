from fastapi import APIRouter

router = APIRouter(prefix="/base", tags=["base"])


@router.get("/")
def home() -> dict[str, str]:
    """Return a welcome message."""
    return {"message": "Welcome to my API!"}
