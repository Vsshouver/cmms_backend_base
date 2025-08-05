from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GrupoItemBase(BaseModel):
    nome: str
    codigo: str

class GrupoItemCreate(GrupoItemBase):
    pass

class GrupoItem(GrupoItemBase):
    id: int
    class Config:
        orm_mode = True

class ItemEstoqueBase(BaseModel):
    numero_item: str
    descricao_item: str
    grupo_codigo: str
    unidade_medida: str
    quantidade_atual: float = 0
    quantidade_minima: float = 0

class ItemEstoqueCreate(ItemEstoqueBase):
    pass

class ItemEstoque(ItemEstoqueBase):
    id: int
    class Config:
        orm_mode = True

class MovimentacaoEstoqueBase(BaseModel):
    item_id: int
    tipo: str  # "entrada" ou "saida"
    quantidade: float
    observacao: Optional[str] = None

class MovimentacaoEstoqueCreate(MovimentacaoEstoqueBase):
    pass

class MovimentacaoEstoque(MovimentacaoEstoqueBase):
    id: int
    data_movimentacao: datetime
    class Config:
        orm_mode = True