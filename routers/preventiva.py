from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.preventiva import PlanoPreventiva, ChecklistItem
from app.schemas.preventiva import PlanoPreventivaCreate, PlanoPreventivaRead
from typing import List

router = APIRouter(prefix="/preventiva", tags=["Planos de Preventiva"])

@router.post("/", response_model=PlanoPreventivaRead)
def criar_plano(plano: PlanoPreventivaCreate, db: Session = Depends(get_db)):
    novo = PlanoPreventiva(
        nome=plano.nome,
        frequencia_dias=plano.frequencia_dias,
        equipamento_id=plano.equipamento_id
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)

    for item in plano.checklist:
        checklist = ChecklistItem(
            descricao=item.descricao,
            plano_id=novo.id
        )
        db.add(checklist)

    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=List[PlanoPreventivaRead])
def listar_planos(db: Session = Depends(get_db)):
    return db.query(PlanoPreventiva).all()

@router.get("/{plano_id}", response_model=PlanoPreventivaRead)
def obter_plano(plano_id: int, db: Session = Depends(get_db)):
    plano = db.query(PlanoPreventiva).filter(PlanoPreventiva.id == plano_id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return plano
