from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.estoque import GrupoItem, ItemEstoque, MovimentacaoEstoque, TipoMovimentacaoEnum
from schemas.estoque import *

router = APIRouter(prefix="/estoque", tags=["Estoque"])

# Grupos
@router.post("/grupos", response_model=GrupoItem)
def criar_grupo(grupo: GrupoItemCreate, db: Session = Depends(get_db)):
    novo = GrupoItem(**grupo.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/grupos", response_model=list[GrupoItem])
def listar_grupos(db: Session = Depends(get_db)):
    return db.query(GrupoItem).all()

# Itens
@router.post("/itens", response_model=ItemEstoque)
def criar_item(item: ItemEstoqueCreate, db: Session = Depends(get_db)):
    novo = ItemEstoque(**item.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/itens", response_model=list[ItemEstoque])
def listar_itens(db: Session = Depends(get_db)):
    return db.query(ItemEstoque).all()

# Movimentações
@router.post("/movimentacoes", response_model=MovimentacaoEstoque)
def movimentar(mov: MovimentacaoEstoqueCreate, db: Session = Depends(get_db)):
    item = db.query(ItemEstoque).filter(ItemEstoque.id == mov.item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    if mov.tipo == "saida" and item.quantidade_atual < mov.quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    if mov.tipo == "entrada":
        item.quantidade_atual += mov.quantidade
    else:
        item.quantidade_atual -= mov.quantidade

    nova = MovimentacaoEstoque(**mov.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/movimentacoes", response_model=list[MovimentacaoEstoque])
def listar_movimentacoes(db: Session = Depends(get_db)):
    return db.query(MovimentacaoEstoque).all()