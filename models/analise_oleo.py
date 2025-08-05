from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class AnaliseOleo(Base):
    __tablename__ = "analises_oleo"

    id = Column(Integer, primary_key=True, index=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"), nullable=False)
    data_coleta = Column(DateTime, default=datetime.utcnow)
    horimetro = Column(Float, nullable=True)
    resultado = Column(Text, nullable=True)
    acoes_recomendadas = Column(Text, nullable=True)
    observacoes = Column(Text, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento", backref="analises_oleo")