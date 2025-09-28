from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.visitante import Visitante
from app.schemas.visitante import VisitanteCreate, VisitanteOut

router = APIRouter(prefix="/visitantes", tags=["Visitantes"])

# Crear un nuevo visitante
@router.post("/", response_model=VisitanteOut, status_code=status.HTTP_201_CREATED)
def crear_visitante(visitante: VisitanteCreate, db: Session = Depends(get_db)):
    nuevo_visitante = Visitante(
        nombre=visitante.nombre,
        apellido=visitante.apellido,
        dni=visitante.dni
    )
    db.add(nuevo_visitante)
    db.commit()
    db.refresh(nuevo_visitante)
    return nuevo_visitante

# Obtener un visitante por ID
@router.get("/{visitante_id}", response_model=VisitanteOut)
def obtener_visitante(visitante_id: int, db: Session = Depends(get_db)):
    visitante = db.query(Visitante).filter(Visitante.id == visitante_id).first()
    if not visitante:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Visitante no encontrado")
    return visitante

# Listar todos los visitantes
@router.get("/", response_model=list[VisitanteOut])
def listar_visitantes(db: Session = Depends(get_db)):
    visitantes = db.query(Visitante).all()
    return visitantes

