from pydantic import BaseModel
from datetime import datetime

class VetadoBase(BaseModel):
    visitado_id: int
    visitante_id: int
    motivo: str

class VetadoCreate(VetadoBase):
    pass

class VetadoOut(VetadoBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
