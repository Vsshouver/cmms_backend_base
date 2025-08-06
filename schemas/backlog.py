from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BacklogBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    prioridade: Optional[str] = "MÉDIA"
    status: Optional[str] = "ABERTO"
    numero_processo: Optional[str] = None
    equipamento_id: Optional[int] = None

class BacklogCreate(BacklogBase):
    pass

class BacklogUpdate(BaseModel):
    status: str

class BacklogRead(BacklogBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True
