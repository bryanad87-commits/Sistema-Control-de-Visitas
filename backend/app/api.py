from fastapi import FastAPI
from backend.app.routes.usuario import usuario_router

def register_routes(app: FastAPI):
    app.include_router(usuario_router)