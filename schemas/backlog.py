from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BacklogBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    prioridade: Optional[str] = "Média"
    status: Optional[str] = "Aguardando"
    responsavel: Optional[str] = None
    equipamento_id: Optional[int] = None
    processo_compra: Optional[str] = None

class BacklogCreate(BacklogBase):
    pass

class BacklogUpdate(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    prioridade: Optional[str]
    status: Optional[str]
    responsavel: Optional[str]
    equipamento_id: Optional[int]
    processo_compra: Optional[str]

class Backlog(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    prioridade: Optional[str]
    status: Optional[str]
    responsavel: Optional[str]
    equipamento_id: Optional[int]
    processo_compra: Optional[str]
    criado_em: datetime

    class Config:
        orm_mode = True