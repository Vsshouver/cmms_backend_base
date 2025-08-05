from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.pneu import Pneu
from schemas.pneu import *

router = APIRouter(prefix="/pneus", tags=["Pneus"])

@router.post("/", response_model=Pneu)
def criar_pneu(pneu: PneuCreate, db: Session = Depends(get_db)):
    novo = Pneu(**pneu.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[Pneu])
def listar_pneus(db: Session = Depends(get_db)):
    return db.query(Pneu).all()

@router.get("/{pneu_id}", response_model=Pneu)
def buscar_pneu(pneu_id: int, db: Session = Depends(get_db)):
    pneu = db.query(Pneu).filter(Pneu.id == pneu_id).first()
    if not pneu:
        raise HTTPException(status_code=404, detail="Pneu não encontrado")
    return pneu

@router.put("/{pneu_id}", response_model=Pneu)
def atualizar_pneu(pneu_id: int, dados: PneuUpdate, db: Session = Depends(get_db)):
    pneu = db.query(Pneu).filter(Pneu.id == pneu_id).first()
    if not pneu:
        raise HTTPException(status_code=404, detail="Pneu não encontrado")
    for field, value in dados.dict(exclude_unset=True).items():
        setattr(pneu, field, value)
    db.commit()
    db.refresh(pneu)
    return pneu

@router.delete("/{pneu_id}")
def deletar_pneu(pneu_id: int, db: Session = Depends(get_db)):
    pneu = db.query(Pneu).filter(Pneu.id == pneu_id).first()
    if not pneu:
        raise HTTPException(status_code=404, detail="Pneu não encontrado")
    db.delete(pneu)
    db.commit()
    return {"detail": "Pneu excluído com sucesso"}