from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.backlog import BacklogItem
from app.schemas.backlog import BacklogCreate, BacklogRead, BacklogUpdate
from typing import List

router = APIRouter(prefix="/backlog", tags=["Backlog"])

@router.post("/", response_model=BacklogRead)
def criar_backlog(item: BacklogCreate, db: Session = Depends(get_db)):
    novo = BacklogItem(**item.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=List[BacklogRead])
def listar_backlog(db: Session = Depends(get_db)):
    return db.query(BacklogItem).all()

@router.get("/{item_id}", response_model=BacklogRead)
def obter_backlog(item_id: int, db: Session = Depends(get_db)):
    item = db.query(BacklogItem).filter(BacklogItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.patch("/{item_id}", response_model=BacklogRead)
def atualizar_status(item_id: int, dados: BacklogUpdate, db: Session = Depends(get_db)):
    item = db.query(BacklogItem).filter(BacklogItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    item.status = dados.status
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def deletar_backlog(item_id: int, db: Session = Depends(get_db)):
    item = db.query(BacklogItem).filter(BacklogItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    db.delete(item)
    db.commit()
    return {"msg": "Item do backlog removido com sucesso"}
