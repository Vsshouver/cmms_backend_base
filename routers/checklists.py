from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.checklist import ChecklistEquipamento
from schemas.checklist import *

router = APIRouter(prefix="/checklists", tags=["Checklists"])

@router.post("/", response_model=Checklist)
def criar_checklist(checklist: ChecklistCreate, db: Session = Depends(get_db)):
    novo = ChecklistEquipamento(**checklist.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[Checklist])
def listar_checklists(db: Session = Depends(get_db)):
    return db.query(ChecklistEquipamento).all()

@router.get("/{checklist_id}", response_model=Checklist)
def buscar_checklist(checklist_id: int, db: Session = Depends(get_db)):
    checklist = db.query(ChecklistEquipamento).filter(ChecklistEquipamento.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")
    return checklist

@router.put("/{checklist_id}", response_model=Checklist)
def atualizar_checklist(checklist_id: int, dados: ChecklistUpdate, db: Session = Depends(get_db)):
    checklist = db.query(ChecklistEquipamento).filter(ChecklistEquipamento.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")
    for field, value in dados.dict(exclude_unset=True).items():
        setattr(checklist, field, value)
    db.commit()
    db.refresh(checklist)
    return checklist

@router.delete("/{checklist_id}")
def deletar_checklist(checklist_id: int, db: Session = Depends(get_db)):
    checklist = db.query(ChecklistEquipamento).filter(ChecklistEquipamento.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")
    db.delete(checklist)
    db.commit()
    return {"detail": "Checklist excluído com sucesso"}