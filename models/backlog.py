from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class BacklogItem(Base):
    __tablename__ = "backlog"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    prioridade = Column(String, default="MÉDIA")  # ALTA, MÉDIA, BAIXA
    status = Column(String, default="ABERTO")  # ABERTO, EM ANDAMENTO, CONCLUÍDO
    numero_processo = Column(String, nullable=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"))
    data_criacao = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento")
