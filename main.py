from fastapi import FastAPI
from init_db import run_migrations
from routers import auth
from database import Base, engine
from routers import equipamentos

run_migrations()
# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CMMS API")

# Incluir rotas
app.include_router(auth.router)
app.include_router(equipamentos.router)