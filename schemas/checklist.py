from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChecklistBase(BaseModel):
    equipamento_id: int
    nome: str
    itens: str  # Separados por linha

class ChecklistCreate(ChecklistBase):
    pass

class ChecklistUpdate(BaseModel):
    nome: Optional[str] = None
    itens: Optional[str] = None

class Checklist(ChecklistBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True