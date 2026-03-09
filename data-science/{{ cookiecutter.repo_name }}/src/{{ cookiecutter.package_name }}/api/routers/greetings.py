from fastapi import APIRouter

router = APIRouter(tags=["greetings"])

@router.get("/hello")
def say_hello() -> dict[str, str]:
    return {"message": "Hello world!"}

@router.get("/bonjour")
def say_bonjour() -> dict[str, str]:
    return {"message": "Hello world!"}