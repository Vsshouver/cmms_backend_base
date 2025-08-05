from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class ChecklistEquipamento(Base):
    __tablename__ = "checklists"
    id = Column(Integer, primary_key=True, index=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"), nullable=False)
    nome = Column(String, nullable=False)
    itens = Column(Text, nullable=False)  # Lista separada por quebra de linha
    criado_em = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento", backref="checklists")