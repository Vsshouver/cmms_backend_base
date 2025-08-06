from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AnaliseOleoBase(BaseModel):
    equipamento_id: int
    resultado: str
    viscosidade: Optional[float] = None
    contaminacao: Optional[str] = None
    tratativa: Optional[str] = None

class AnaliseOleoCreate(AnaliseOleoBase):
    pass

class AnaliseOleoRead(AnaliseOleoBase):
    id: int
    data_analise: datetime

    class Config:
        from_attributes = True
