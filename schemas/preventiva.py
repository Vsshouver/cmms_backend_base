from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChecklistItemBase(BaseModel):
    descricao: str

class ChecklistItemCreate(ChecklistItemBase):
    pass

class ChecklistItemRead(ChecklistItemBase):
    id: int
    class Config:
        from_attributes = True

class PlanoPreventivaBase(BaseModel):
    nome: str
    frequencia_dias: int
    equipamento_id: int

class PlanoPreventivaCreate(PlanoPreventivaBase):
    checklist: List[ChecklistItemCreate]

class PlanoPreventivaRead(PlanoPreventivaBase):
    id: int
    data_criacao: datetime
    checklist: List[ChecklistItemRead]

    class Config:
        from_attributes = True
