from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.visita import Visita
from app.schemas.visita import VisitaOut, VisitaCreate

router = APIRouter(prefix="/visitas", tags=["Visitas"])
# Crear una nueva visita
@router.post("/", response_model=VisitaOut, status_code=status.HTTP_201_CREATED)
def crear_visita(visita: VisitaCreate, db: Session = Depends(get_db)):
    nueva_visita = Visita(
        visitante_id=visita.visitante_id,
        autorizado_id=visita.autorizado_id,
        portero_id=visita.portero_id,
        estado=visita.estado,
        observacion=visita.observacion,
    )
    db.add(nueva_visita)
    db.commit()
    db.refresh(nueva_visita)
    return nueva_visita

# Obtener una visita por ID
@router.get("/{visita_id}", response_model=VisitaOut)
def obtener_visita(visita_id: int, db: Session = Depends(get_db)):
    visita = db.query(Visita).filter(Visita.id == visita_id).first()
    if not visita:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Visita no encontrada")
    return visita

# Listar todas las visitas
@router.get("/", response_model=list[VisitaOut])
def listar_visitas(db: Session = Depends(get_db)):
    visitas = db.query(Visita).all()
    return visitas
