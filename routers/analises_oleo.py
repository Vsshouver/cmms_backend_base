from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.analise_oleo import AnaliseOleo
from schemas.analise_oleo import *

router = APIRouter(prefix="/analises-oleo", tags=["Análise de Óleo"])

@router.post("/", response_model=AnaliseOleo)
def criar_analise(analise: AnaliseOleoCreate, db: Session = Depends(get_db)):
    nova = AnaliseOleo(**analise.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/", response_model=list[AnaliseOleo])
def listar_analises(db: Session = Depends(get_db)):
    return db.query(AnaliseOleo).all()

@router.get("/{analise_id}", response_model=AnaliseOleo)
def buscar_analise(analise_id: int, db: Session = Depends(get_db)):
    analise = db.query(AnaliseOleo).filter(AnaliseOleo.id == analise_id).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    return analise

@router.put("/{analise_id}", response_model=AnaliseOleo)
def atualizar_analise(analise_id: int, dados: AnaliseOleoUpdate, db: Session = Depends(get_db)):
    analise = db.query(AnaliseOleo).filter(AnaliseOleo.id == analise_id).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    for field, value in dados.dict(exclude_unset=True).items():
        setattr(analise, field, value)
    db.commit()
    db.refresh(analise)
    return analise

@router.delete("/{analise_id}")
def deletar_analise(analise_id: int, db: Session = Depends(get_db)):
    analise = db.query(AnaliseOleo).filter(AnaliseOleo.id == analise_id).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    db.delete(analise)
    db.commit()
    return {"detail": "Análise excluída com sucesso"}