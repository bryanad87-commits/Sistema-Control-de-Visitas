from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.vetados import Vetado
from app.schemas.vetado import VetadoCreate, VetadoOut

router = APIRouter(prefix="/vetados", tags=["Vetados"])

# Crear un nuevo vetado
@router.post("/", response_model=VetadoOut, status_code=status.HTTP_201_CREATED)
def crear_vetado(vetado: VetadoCreate, db: Session = Depends(get_db)):
    nuevo_vetado = Vetado(
        visitado_id=vetado.visitado_id,
        visitante_id=vetado.visitante_id,
        motivo=vetado.motivo
    )
    db.add(nuevo_vetado)
    db.commit()
    db.refresh(nuevo_vetado)
    return nuevo_vetado

# Obtener un vetado por ID
@router.get("/{vetado_id}", response_model=VetadoOut)
def obtener_vetado(vetado_id: int, db: Session = Depends(get_db)):
    vetado = db.query(Vetado).filter(Vetado.id == vetado_id).first()
    if not vetado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vetado no encontrado")
    return vetado

# Listar todos los vetados
@router.get("/", response_model=list[VetadoOut])
def listar_vetados(db: Session = Depends(get_db)):
    vetados = db.query(Vetado).all()
    return vetados

# Eliminar un vetado
@router.delete("/{vetado_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_vetado(vetado_id: int, db: Session = Depends(get_db)):
    vetado = db.query(Vetado).filter(Vetado.id == vetado_id).first()
    if not vetado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vetado no encontrado")
    db.delete(vetado)
    db.commit()
    return