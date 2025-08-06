from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class AnaliseOleo(Base):
    __tablename__ = "analises_oleo"

    id = Column(Integer, primary_key=True, index=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"))
    resultado = Column(String, nullable=False)
    viscosidade = Column(Float, nullable=True)
    contaminacao = Column(String, nullable=True)
    tratativa = Column(String, nullable=True)
    data_analise = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento")
