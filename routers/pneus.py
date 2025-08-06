from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pneu import Pneu
from app.schemas.pneu import PneuCreate, PneuRead, PneuUpdate
from typing import List

router = APIRouter(prefix="/pneus", tags=["Pneus"])

@router.post("/", response_model=PneuRead)
def cadastrar_pneu(pneu: PneuCreate, db: Session = Depends(get_db)):
    novo = Pneu(**pneu.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=List[PneuRead])
def listar_pneus(db: Session = Depends(get_db)):
    return db.query(Pneu).all()

@router.get("/{pneu_id}", response_model=PneuRead)
def obter_pneu(pneu_id: int, db: Session = Depends(get_db)):
    pneu = db.query(Pneu).filter(Pneu.id == pneu_id).first()
    if not pneu:
        raise HTTPException(status_code=404, detail="Pneu não encontrado")
    return pneu

@router.patch("/{pneu_id}", response_model=PneuRead)
def atualizar_pneu(pneu_id: int, dados: PneuUpdate, db: Session = Depends(get_db)):
    pneu = db.query(Pneu).filter(Pneu.id == pneu_id).first()
    if not pneu:
        raise HTTPException(status_code=404, detail="Pneu não encontrado")
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(pneu, key, value)
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
    return {"msg": "Pneu removido com sucesso"}
