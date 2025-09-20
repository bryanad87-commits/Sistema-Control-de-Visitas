import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Autorizacion(Base):
    __tablename__ = "autorizaciones"

    id = Column(Integer, primary_key=True, index=True)
    visitado_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    visitante_id = Column(Integer, ForeignKey("visitantes.id"), nullable=False)
    tipo = Column(String(20), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    
    visitado = relationship("Usuario", back_populates="autorizaciones")
    visitante = relationship("Visitante", back_populates="autorizaciones")
    visitas = relationship("Visita", back_populates="autorizado")