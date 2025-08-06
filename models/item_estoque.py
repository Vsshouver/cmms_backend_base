from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base

class GrupoItem(Base):
    __tablename__ = "grupos_item"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    codigo = Column(String, nullable=False, unique=True)

    itens = relationship("ItemEstoque", back_populates="grupo")

class ItemEstoque(Base):
    __tablename__ = "itens_estoque"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    grupo_id = Column(Integer, ForeignKey("grupos_item.id"))
    unidade = Column(String)
    quantidade = Column(Float, default=0)

    grupo = relationship("GrupoItem", back_populates="itens")
