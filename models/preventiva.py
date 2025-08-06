from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class PlanoPreventiva(Base):
    __tablename__ = "planos_preventiva"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    frequencia_dias = Column(Integer, nullable=False)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"))
    data_criacao = Column(DateTime, default=datetime.utcnow)

    equipamento = relationship("Equipamento")
    checklists = relationship("ChecklistItem", back_populates="plano")

class ChecklistItem(Base):
    __tablename__ = "checklist_itens"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    plano_id = Column(Integer, ForeignKey("planos_preventiva.id"))

    plano = relationship("PlanoPreventiva", back_populates="checklists")
