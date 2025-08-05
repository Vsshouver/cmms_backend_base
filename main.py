from fastapi import FastAPI
from routers import auth
from database import Base, engine

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CMMS API")

# Incluir rotas
app.include_router(auth.router)