from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class TipoEquipamento(Base):
    __tablename__ = "tipos_equipamento"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)

class Equipamento(Base):
    __tablename__ = "equipamentos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    tipo_id = Column(Integer, ForeignKey("tipos_equipamento.id"), nullable=False)
    fabricante = Column(String)
    modelo = Column(String)
    numero_serie = Column(String)
    codigo_interno = Column(String, unique=True)
    status = Column(String, default="ATIVO")