from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AnaliseOleoBase(BaseModel):
    equipamento_id: int
    data_coleta: Optional[datetime] = None
    horimetro: Optional[float] = None
    resultado: Optional[str] = None
    acoes_recomendadas: Optional[str] = None
    observacoes: Optional[str] = None

class AnaliseOleoCreate(AnaliseOleoBase):
    pass

class AnaliseOleoUpdate(BaseModel):
    horimetro: Optional[float]
    resultado: Optional[str]
    acoes_recomendadas: Optional[str]
    observacoes: Optional[str]

class AnaliseOleo(BaseModel):
    id: int
    equipamento_id: int
    data_coleta: datetime
    horimetro: Optional[float]
    resultado: Optional[str]
    acoes_recomendadas: Optional[str]
    observacoes: Optional[str]
    criado_em: datetime

    class Config:
        orm_mode = True