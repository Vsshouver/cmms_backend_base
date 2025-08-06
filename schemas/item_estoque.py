from pydantic import BaseModel
from typing import Optional

class GrupoItemBase(BaseModel):
    nome: str
    codigo: str

class GrupoItemCreate(GrupoItemBase):
    pass

class GrupoItemRead(GrupoItemBase):
    id: int
    class Config:
        from_attributes = True

class ItemEstoqueBase(BaseModel):
    descricao: str
    grupo_id: int
    unidade: Optional[str] = None
    quantidade: Optional[float] = 0

class ItemEstoqueCreate(ItemEstoqueBase):
    pass

class ItemEstoqueUpdate(BaseModel):
    quantidade: float

class ItemEstoqueRead(ItemEstoqueBase):
    id: int
    grupo: Optional[GrupoItemRead]

    class Config:
        from_attributes = True
