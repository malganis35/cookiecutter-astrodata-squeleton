from fastapi import APIRouter

router = APIRouter(tags=["greetings"])


@router.get("/hello")
def say_hello() -> dict[str, str]:
    """Return a hello world message in English."""
    return {"message": "Hello world!"}


@router.get("/bonjour")
def say_bonjour() -> dict[str, str]:
    """Return a hello world message in French."""
    return {"message": "Bonjour le monde !"}
