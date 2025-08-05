from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from database import Base

class StatusPneuEnum(str):
    EM_ESTOQUE = "em_estoque"
    EM_USO = "em_uso"
    DESCARTADO = "descartado"
    RECAPADO = "recapado"

class Pneu(Base):
    __tablename__ = "pneus"

    id = Column(Integer, primary_key=True, index=True)
    numero_serie = Column(String, unique=True, nullable=False)
    numero_fogo = Column(String, unique=True, nullable=True)
    dot = Column(String, nullable=True)
    marca = Column(String, nullable=True)
    fornecedor = Column(String, nullable=True)
    sulco_inicial = Column(Float, nullable=True)
    sulco_atual = Column(Float, nullable=True)
    status = Column(String, default="em_estoque")
    km_rodado = Column(Float, default=0)
    observacoes = Column(String, nullable=True)
    criado_em = Column(DateTime, server_default=func.now())