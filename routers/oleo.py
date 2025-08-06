from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.analise_oleo import AnaliseOleo
from app.schemas.analise_oleo import AnaliseOleoCreate, AnaliseOleoRead
from typing import List

router = APIRouter(prefix="/analises_oleo", tags=["Análises de Óleo"])

@router.post("/", response_model=AnaliseOleoRead)
def cadastrar_analise(analise: AnaliseOleoCreate, db: Session = Depends(get_db)):
    nova = AnaliseOleo(**analise.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/", response_model=List[AnaliseOleoRead])
def listar_analises(db: Session = Depends(get_db)):
    return db.query(AnaliseOleo).all()

@router.get("/{analise_id}", response_model=AnaliseOleoRead)
def obter_analise(analise_id: int, db: Session = Depends(get_db)):
    analise = db.query(AnaliseOleo).filter(AnaliseOleo.id == analise_id).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    return analise
