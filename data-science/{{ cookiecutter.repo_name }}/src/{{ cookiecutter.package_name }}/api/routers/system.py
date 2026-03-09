from fastapi import APIRouter, Request

router = APIRouter(tags=["system"])

@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/version")
def version(request: Request) -> dict[str, str]:
    return {"version": request.app.version}
