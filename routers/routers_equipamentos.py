from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.equipamento import Equipamento, TipoEquipamento
from schemas.equipamento import EquipamentoCreate, Equipamento, TipoEquipamentoCreate, TipoEquipamento

router = APIRouter(prefix="/equipamentos", tags=["Equipamentos"])

# Tipos de Equipamento
@router.post("/tipos", response_model=TipoEquipamento)
def criar_tipo(tipo: TipoEquipamentoCreate, db: Session = Depends(get_db)):
    novo = TipoEquipamento(**tipo.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/tipos", response_model=list[TipoEquipamento])
def listar_tipos(db: Session = Depends(get_db)):
    return db.query(TipoEquipamento).all()

# Equipamentos
@router.post("/", response_model=Equipamento)
def criar_equipamento(eq: EquipamentoCreate, db: Session = Depends(get_db)):
    novo = Equipamento(**eq.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[Equipamento])
def listar_equipamentos(db: Session = Depends(get_db)):
    return db.query(Equipamento).all()

@router.get("/{id}", response_model=Equipamento)
def get_equipamento(id: int, db: Session = Depends(get_db)):
    equipamento = db.query(Equipamento).filter(Equipamento.id == id).first()
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    return equipamento

@router.put("/{id}", response_model=Equipamento)
def atualizar_equipamento(id: int, eq: EquipamentoCreate, db: Session = Depends(get_db)):
    equipamento = db.query(Equipamento).filter(Equipamento.id == id).first()
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    for campo, valor in eq.dict().items():
        setattr(equipamento, campo, valor)
    db.commit()
    db.refresh(equipamento)
    return equipamento

@router.delete("/{id}")
def deletar_equipamento(id: int, db: Session = Depends(get_db)):
    equipamento = db.query(Equipamento).filter(Equipamento.id == id).first()
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    db.delete(equipamento)
    db.commit()
    return {"ok": True}