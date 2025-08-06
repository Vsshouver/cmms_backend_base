from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OrdemServicoBase(BaseModel):
    equipamento_id: int
    descricao: str
    tipo: Optional[str] = None
    prioridade: Optional[str] = None
    checklist: Optional[str] = None
    assinatura: Optional[str] = None
    mecanicos_ids: List[int] = []

class OrdemServicoCreate(OrdemServicoBase):
    pass

class OrdemServicoUpdate(BaseModel):
    status: Optional[str] = None
    data_fechamento: Optional[datetime] = None
    assinatura: Optional[str] = None
    mecanicos_ids: Optional[List[int]] = []

class OrdemServico(OrdemServicoBase):
    id: int
    status: str
    data_abertura: datetime
    data_fechamento: Optional[datetime] = None

    class Config:
        orm_mode = True