import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Visita(Base):
    __tablename__ = "visitas"

    id = Column(Integer, primary_key=True, index=True)
    visitante_id = Column(Integer, ForeignKey("visitantes.id"))
    autorizado_id = Column(Integer,ForeignKey("autorizaciones.id"))
    portero_id = Column(Integer, ForeignKey("usuarios.id"))
    estado = Column(String(20), nullable=False)
    fecha_ingreso = Column(DateTime, default=datetime.datetime.now)
    fecha_salida = Column(DateTime, nullable=True)
    observacion = Column(Text, nullable=True)
    
    portero = relationship("Usuario", back_populates="visitas")
    visitante = relationship("Visitante", back_populates="visitas")
    autorizado = relationship("Autorizacion", back_populates="visitas")