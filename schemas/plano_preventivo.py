from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PlanoPreventivoBase(BaseModel):
    equipamento_id: int
    nome: str
    frequencia_dias: Optional[int] = None
    frequencia_horimetro: Optional[int] = None
    checklist: Optional[str] = None
    itens_necessarios: Optional[str] = None
    ativo: Optional[bool] = True

class PlanoPreventivoCreate(PlanoPreventivoBase):
    pass

class PlanoPreventivoUpdate(BaseModel):
    nome: Optional[str] = None
    frequencia_dias: Optional[int] = None
    frequencia_horimetro: Optional[int] = None
    checklist: Optional[str] = None
    itens_necessarios: Optional[str] = None
    ativo: Optional[bool] = None

class PlanoPreventivo(PlanoPreventivoBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True