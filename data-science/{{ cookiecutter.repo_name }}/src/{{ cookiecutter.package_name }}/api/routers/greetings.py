from fastapi import APIRouter

router = APIRouter(tags=["greetings"])

@router.get("/hello")
def say_hello():
    return {"message": "Hello world!"}

@router.get("/bonjour")
def say_bonjour():
    return {"message": "Hello world!"}
