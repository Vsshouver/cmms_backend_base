from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum

class PerfilEnum(str, enum.Enum):
    ADM = "ADM"
    SUPERVISOR = "SUPERVISOR"
    ALMOXARIFE = "ALMOXARIFE"
    PCM = "PCM"
    MECANICO = "MECANICO"
    VIEW = "VIEW"

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    perfil = Column(Enum(PerfilEnum), default=PerfilEnum.VIEW)