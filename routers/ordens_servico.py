from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.ordem_servico import OrdemServico, os_mecanicos
from models.user import User
from schemas.ordem_servico import *

router = APIRouter(prefix="/ordens_servico", tags=["Ordens de Serviço"])

@router.post("/", response_model=OrdemServico)
def criar_ordem(ordem: OrdemServicoCreate, db: Session = Depends(get_db)):
    nova_os = OrdemServico(
        equipamento_id=ordem.equipamento_id,
        descricao=ordem.descricao,
        tipo=ordem.tipo,
        prioridade=ordem.prioridade,
        checklist=ordem.checklist,
        assinatura=ordem.assinatura,
    )

    if ordem.mecanicos_ids:
        mecanicos = db.query(User).filter(User.id.in_(ordem.mecanicos_ids)).all()
        nova_os.mecanicos = mecanicos

    db.add(nova_os)
    db.commit()
    db.refresh(nova_os)
    return nova_os

@router.get("/", response_model=list[OrdemServico])
def listar_ordens(db: Session = Depends(get_db)):
    return db.query(OrdemServico).all()

@router.get("/{ordem_id}", response_model=OrdemServico)
def buscar_ordem(ordem_id: int, db: Session = Depends(get_db)):
    ordem = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    if not ordem:
        raise HTTPException(status_code=404, detail="OS não encontrada")
    return ordem

@router.put("/{ordem_id}", response_model=OrdemServico)
def atualizar_ordem(ordem_id: int, dados: OrdemServicoUpdate, db: Session = Depends(get_db)):
    ordem = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    if not ordem:
        raise HTTPException(status_code=404, detail="OS não encontrada")

    for field, value in dados.dict(exclude_unset=True).items():
        setattr(ordem, field, value)

    if dados.mecanicos_ids is not None:
        ordem.mecanicos = db.query(User).filter(User.id.in_(dados.mecanicos_ids)).all()

    db.commit()
    db.refresh(ordem)
    return ordem