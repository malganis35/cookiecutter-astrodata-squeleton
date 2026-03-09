from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to my API!"}