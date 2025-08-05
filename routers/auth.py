from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User, PerfilEnum
from auth.utils import gerar_hash, verificar_hash, criar_token
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginData(BaseModel):
    email: str
    senha: str

class CreateUser(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: PerfilEnum

@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verificar_hash(data.senha, user.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"sub": user.email, "perfil": user.perfil})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register")
def register(data: CreateUser, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    novo = User(nome=data.nome, email=data.email, senha=gerar_hash(data.senha), perfil=data.perfil)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"id": novo.id, "email": novo.email, "perfil": novo.perfil}