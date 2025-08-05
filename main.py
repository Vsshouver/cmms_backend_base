from fastapi import FastAPI
from database import Base, engine
from routers import auth, equipamentos
from init_db import run_migrations

run_migrations()

app = FastAPI(title="CMMS API")

app.include_router(auth.router)
app.include_router(equipamentos.router)