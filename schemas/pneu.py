from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PneuBase(BaseModel):
    numero_fogo: str
    dot: Optional[str] = None
    marca: Optional[str] = None
    fornecedor: Optional[str] = None
    profundidade_sulco: Optional[float] = None
    status: Optional[str] = "DISPONIVEL"
    equipamento_id: Optional[int] = None
    posicao: Optional[str] = None

class PneuCreate(PneuBase):
    pass

class PneuUpdate(BaseModel):
    status: Optional[str] = None
    equipamento_id: Optional[int] = None
    posicao: Optional[str] = None

class PneuRead(PneuBase):
    id: int
    data_cadastro: datetime

    class Config:
        from_attributes = True
