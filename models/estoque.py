from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
from datetime import datetime

class GrupoItem(Base):
    __tablename__ = "grupos_item"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    codigo = Column(String, nullable=False, unique=True)

class ItemEstoque(Base):
    __tablename__ = "itens"
    id = Column(Integer, primary_key=True, index=True)
    numero_item = Column(String, nullable=False, unique=True)
    descricao_item = Column(String, nullable=False)
    grupo_codigo = Column(String, ForeignKey("grupos_item.codigo"))
    unidade_medida = Column(String, nullable=False)
    quantidade_atual = Column(Float, default=0.0)
    quantidade_minima = Column(Float, default=0.0)
    grupo = relationship("GrupoItem", backref="itens")

class TipoMovimentacaoEnum(str, enum.Enum):
    entrada = "entrada"
    saida = "saida"

class MovimentacaoEstoque(Base):
    __tablename__ = "movimentacoes_estoque"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("itens.id"), nullable=False)
    tipo = Column(Enum(TipoMovimentacaoEnum), nullable=False)
    quantidade = Column(Float, nullable=False)
    observacao = Column(String)
    data_movimentacao = Column(DateTime, default=datetime.utcnow)