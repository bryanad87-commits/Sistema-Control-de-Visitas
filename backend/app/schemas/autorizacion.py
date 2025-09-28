from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class AutorizacionBase(BaseModel):
    visitado_id: int
    visitante_id: int
    tipo: str
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None

class AutorizacionCreate(AutorizacionBase):
    pass

class AutorizacionOut(AutorizacionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
