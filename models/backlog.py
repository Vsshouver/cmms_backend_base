from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Backlog(Base):
    __tablename__ = "backlogs"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    prioridade = Column(String, default="Média")
    status = Column(String, default="Aguardando")
    responsavel = Column(String, nullable=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"), nullable=True)
    processo_compra = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento", backref="backlogs")