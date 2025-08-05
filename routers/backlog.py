from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.backlog import Backlog
from schemas.backlog import *

router = APIRouter(prefix="/backlog", tags=["Backlog"])

@router.post("/", response_model=Backlog)
def criar_backlog(registro: BacklogCreate, db: Session = Depends(get_db)):
    novo = Backlog(**registro.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[Backlog])
def listar_backlog(db: Session = Depends(get_db)):
    return db.query(Backlog).all()

@router.get("/{item_id}", response_model=Backlog)
def buscar_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Backlog).filter(Backlog.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.put("/{item_id}", response_model=Backlog)
def atualizar_item(item_id: int, dados: BacklogUpdate, db: Session = Depends(get_db)):
    item = db.query(Backlog).filter(Backlog.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    for field, value in dados.dict(exclude_unset=True).items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def deletar_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Backlog).filter(Backlog.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    db.delete(item)
    db.commit()
    return {"detail": "Item excluído com sucesso"}