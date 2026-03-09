from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to my API!"}


@router.get("/hello")
def say_hello():
    return {"message": "Hello world!"}


@router.get("/bonjour")
def say_bonjour():
    return {"message": "Hello world!"}
