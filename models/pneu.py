from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Pneu(Base):
    __tablename__ = "pneus"

    id = Column(Integer, primary_key=True, index=True)
    numero_fogo = Column(String, unique=True, nullable=False)
    dot = Column(String, nullable=True)
    marca = Column(String, nullable=True)
    fornecedor = Column(String, nullable=True)
    profundidade_sulco = Column(Float, nullable=True)
    status = Column(String, default="DISPONIVEL")  # DISPONIVEL, EM USO, DESCARTADO
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"), nullable=True)
    posicao = Column(String, nullable=True)
    data_cadastro = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento")
