from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VisitaBase(BaseModel):
    visitante_id: int
    autorizado_id: Optional[int] = None
    portero_id: int
    estado: str
    observacion: Optional[str] = None

    class Config:
        orm_mode = True

# Esquema para crear una visita (sin campos auto-generados)
class VisitaCreate(VisitaBase):
    pass

# Esquema para respuesta (incluye campos auto-generados)
class VisitaOut(VisitaBase):
    id: int
    fecha_ingreso: datetime
    fecha_salida: Optional[datetime] = None

    class Config:
        orm_mode = True
