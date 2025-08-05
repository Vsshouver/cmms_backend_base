from pydantic import BaseModel
from typing import Optional

class TipoEquipamentoBase(BaseModel):
    nome: str

class TipoEquipamentoCreate(TipoEquipamentoBase):
    pass

class TipoEquipamento(TipoEquipamentoBase):
    id: int
    class Config:
        orm_mode = True

class EquipamentoBase(BaseModel):
    nome: str
    tipo_id: int
    fabricante: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    codigo_interno: Optional[str] = None
    status: Optional[str] = "ATIVO"

class EquipamentoCreate(EquipamentoBase):
    pass

class Equipamento(EquipamentoBase):
    id: int
    class Config:
        orm_mode = True