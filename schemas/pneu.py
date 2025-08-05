from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PneuBase(BaseModel):
    numero_serie: str
    numero_fogo: Optional[str] = None
    dot: Optional[str] = None
    marca: Optional[str] = None
    fornecedor: Optional[str] = None
    sulco_inicial: Optional[float] = None
    sulco_atual: Optional[float] = None
    status: Optional[str] = "em_estoque"
    km_rodado: Optional[float] = 0
    observacoes: Optional[str] = None

class PneuCreate(PneuBase):
    pass

class PneuUpdate(BaseModel):
    dot: Optional[str] = None
    marca: Optional[str] = None
    fornecedor: Optional[str] = None
    sulco_atual: Optional[float] = None
    status: Optional[str] = None
    km_rodado: Optional[float] = None
    observacoes: Optional[str] = None

class Pneu(PneuBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True