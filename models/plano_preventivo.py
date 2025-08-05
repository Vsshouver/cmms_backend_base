from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, Interval
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class PlanoPreventivo(Base):
    __tablename__ = "planos_preventivos"
    id = Column(Integer, primary_key=True, index=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"), nullable=False)
    nome = Column(String, nullable=False)
    frequencia_dias = Column(Integer, nullable=True)
    frequencia_horimetro = Column(Integer, nullable=True)
    checklist = Column(Text, nullable=True)
    itens_necessarios = Column(Text, nullable=True)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento", backref="planos_preventivos")