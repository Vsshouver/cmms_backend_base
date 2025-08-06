from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.item_estoque import ItemEstoque, GrupoItem
from app.schemas.item_estoque import ItemEstoqueCreate, ItemEstoqueRead, ItemEstoqueUpdate, GrupoItemCreate, GrupoItemRead
from typing import List

router = APIRouter(prefix="/estoque", tags=["Estoque"])

@router.post("/grupos", response_model=GrupoItemRead)
def criar_grupo(grupo: GrupoItemCreate, db: Session = Depends(get_db)):
    novo = GrupoItem(**grupo.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/grupos", response_model=List[GrupoItemRead])
def listar_grupos(db: Session = Depends(get_db)):
    return db.query(GrupoItem).all()

@router.post("/", response_model=ItemEstoqueRead)
def criar_item(item: ItemEstoqueCreate, db: Session = Depends(get_db)):
    novo = ItemEstoque(**item.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=List[ItemEstoqueRead])
def listar_estoque(db: Session = Depends(get_db)):
    return db.query(ItemEstoque).all()

@router.patch("/{item_id}", response_model=ItemEstoqueRead)
def atualizar_quantidade(item_id: int, dados: ItemEstoqueUpdate, db: Session = Depends(get_db)):
    item = db.query(ItemEstoque).filter(ItemEstoque.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    item.quantidade = dados.quantidade
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def deletar_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemEstoque).filter(ItemEstoque.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    db.delete(item)
    db.commit()
    return {"msg": "Item removido com sucesso"}
