from pydantic import BaseModel
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    email: str
    departamento: str
    telefono: str | None = None
    rol: str
    
    class Config:
        orm_mode = True
        
class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True