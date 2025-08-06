from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Table
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Tabela de associação OS <-> Mecânicos
os_mecanicos = Table(
    "os_mecanicos", Base.metadata,
    Column("os_id", Integer, ForeignKey("ordens_servico.id")),
    Column("mecanico_id", Integer, ForeignKey("usuarios.id"))
)

class OrdemServico(Base):
    __tablename__ = "ordens_servico"
    id = Column(Integer, primary_key=True, index=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id"), nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(String, default="aberta")  # aberta, andamento, finalizada, cancelada
    prioridade = Column(String)
    tipo = Column(String)
    data_abertura = Column(DateTime, default=datetime.utcnow)
    data_fechamento = Column(DateTime, nullable=True)
    checklist = Column(Text, nullable=True)
    assinatura = Column(Text, nullable=True)  # base64 ou referência para imagem

    equipamento = relationship("Equipamento", backref="ordens_servico")
    mecanicos = relationship("User", secondary=os_mecanicos, backref="os_mecanico")
    