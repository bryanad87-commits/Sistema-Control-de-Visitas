from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.autorizaciones import Autorizacion
from app.schemas.autorizacion import AutorizacionCreate, AutorizacionOut

router = APIRouter(prefix="/autorizaciones", tags=["Autorizaciones"])

# Crear una nueva autorización
@router.post("/", response_model=AutorizacionOut, status_code=status.HTTP_201_CREATED)
def crear_autorizacion(autorizacion: AutorizacionCreate, db: Session = Depends(get_db)):
    nueva_autorizacion = Autorizacion(
        visitado_id=autorizacion.visitado_id,
        visitante_id=autorizacion.visitante_id,
        tipo=autorizacion.tipo,
        fecha_inicio=autorizacion.fecha_inicio,
        fecha_fin=autorizacion.fecha_fin
    )
    db.add(nueva_autorizacion)
    db.commit()
    db.refresh(nueva_autorizacion)
    return nueva_autorizacion

# Obtener una autorización por ID
@router.get("/{autorizacion_id}", response_model=AutorizacionOut)
def obtener_autorizacion(autorizacion_id: int, db: Session = Depends(get_db)):
    autorizacion = db.query(Autorizacion).filter(Autorizacion.id == autorizacion_id).first()
    if not autorizacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Autorización no encontrada")
    return autorizacion

# Listar todas las autorizaciones
@router.get("/", response_model=list[AutorizacionOut])
def listar_autorizaciones(db: Session = Depends(get_db)):
    autorizaciones = db.query(Autorizacion).all()
    return autorizaciones

 