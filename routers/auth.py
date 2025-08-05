from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from passlib.context import CryptContext
from pydantic import BaseModel
from enum import Enum

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class NivelAcesso(str, Enum):
    ADM = "ADM"
    SUPERVISOR = "SUPERVISOR"
    ALMOXARIFE = "ALMOXARIFE"
    PCM = "PCM"
    MECANICO = "MECANICO"
    VIEW = "VIEW"

class UsuarioLogin(BaseModel):
    username: str
    password: str

class Usuario(BaseModel):
    id: int
    username: str
    nivel_acesso: NivelAcesso

    model_config = {
        "from_attributes": True
    }

fake_users_db = {
    "admin": {
        "id": 1,
        "username": "admin",
        "hashed_password": pwd_context.hash("admin123"),
        "nivel_acesso": "ADM"
    },
    "mecanico": {
        "id": 2,
        "username": "mecanico",
        "hashed_password": pwd_context.hash("mecanico123"),
        "nivel_acesso": "MECANICO"
    }
}

@router.post("/login", response_model=Usuario)
def login(user: UsuarioLogin, db: Session = Depends(get_db)):
    db_user = fake_users_db.get(user.username)
    if not db_user or not pwd_context.verify(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
    return Usuario(**db_user)