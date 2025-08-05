from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.plano_preventivo import PlanoPreventivo
from schemas.plano_preventivo import *

router = APIRouter(prefix="/planos_preventivos", tags=["Planos Preventivos"])

@router.post("/", response_model=PlanoPreventivo)
def criar_plano(plano: PlanoPreventivoCreate, db: Session = Depends(get_db)):
    novo = PlanoPreventivo(**plano.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[PlanoPreventivo])
def listar_planos(db: Session = Depends(get_db)):
    return db.query(PlanoPreventivo).all()

@router.get("/{plano_id}", response_model=PlanoPreventivo)
def buscar_plano(plano_id: int, db: Session = Depends(get_db)):
    plano = db.query(PlanoPreventivo).filter(PlanoPreventivo.id == plano_id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return plano

@router.put("/{plano_id}", response_model=PlanoPreventivo)
def atualizar_plano(plano_id: int, dados: PlanoPreventivoUpdate, db: Session = Depends(get_db)):
    plano = db.query(PlanoPreventivo).filter(PlanoPreventivo.id == plano_id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    for field, value in dados.dict(exclude_unset=True).items():
        setattr(plano, field, value)
    db.commit()
    db.refresh(plano)
    return plano

@router.delete("/{plano_id}")
def deletar_plano(plano_id: int, db: Session = Depends(get_db)):
    plano = db.query(PlanoPreventivo).filter(PlanoPreventivo.id == plano_id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    db.delete(plano)
    db.commit()
    return {"detail": "Plano excluído com sucesso"}