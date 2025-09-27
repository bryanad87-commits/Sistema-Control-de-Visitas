from fastapi import FastAPI
from app.database import Base,engine
from app.routes import usuario
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Control de Visitas", version="1.0.0")

listaRutas = [usuario.router]

for ruta in listaRutas:
    app.include_router(ruta)
