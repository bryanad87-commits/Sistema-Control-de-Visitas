from fastapi import FastAPI
from app.database import init_db
from .api import register_routes

app = FastAPI(title="Sistema de Control de Visitas", version="1.0.0") 

init_db()

# Registro de rutas
register_routes(app)