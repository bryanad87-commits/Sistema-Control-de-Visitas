from fastapi import FastAPI
from app.routes.usuario_router import usuario_router

def register_routes(app: FastAPI):
    app.include_router(usuario_router)