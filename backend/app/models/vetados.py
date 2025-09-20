import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Vetado(Base):
    __tablename__ = "vetados"

    id = Column(Integer, primary_key=True, index=True)
    visitado_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    visitante_id = Column(Integer, ForeignKey("visitantes.id"), nullable=False)
    motivo = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    
    visitado = relationship("Usuario", back_populates="vetados")
    visitante = relationship("Visitante", back_populates="vetados")