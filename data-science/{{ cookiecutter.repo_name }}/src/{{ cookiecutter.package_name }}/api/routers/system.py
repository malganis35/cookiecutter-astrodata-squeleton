from fastapi import APIRouter, Request

router = APIRouter(tags=["system"])

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/version")
def version(request: Request):
    # Récupère dynamiquement la version définie dans api/main.py
    return {"version": request.app.version}