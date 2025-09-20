from fastapi import APIRouter

usuario_router = APIRouter()

@usuario_router.get("/")
def read_root():
    return {"Hello": "World"}
