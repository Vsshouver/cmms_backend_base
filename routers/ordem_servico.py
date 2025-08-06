from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ordem_servico import OrdemServico, ItemOrdemServico
from app.models.equipamento import Equipamento
from app.models.user import User
from app.schemas.ordem_servico import OrdemServicoCreate, OrdemServicoRead, OrdemServicoUpdate, OrdemServicoStatusUpdate
from app.schemas.user import UserRead
from app.schemas.equipamento import EquipamentoRead
from app.schemas.ordem_servico import ItemOrdemServicoCreate
from typing import List
from datetime import datetime

router = APIRouter(prefix="/ordens_servico", tags=["Ordem de Serviço"])

@router.post("/", response_model=OrdemServicoRead)
def criar_ordem_servico(ordem: OrdemServicoCreate, db: Session = Depends(get_db)):
    nova_os = OrdemServico(
        descricao=ordem.descricao,
        status=ordem.status,
        prioridade=ordem.prioridade,
        data_criacao=datetime.utcnow(),
        equipamento_id=ordem.equipamento_id,
        mecanicos=ordem.mecanicos
    )
    db.add(nova_os)
    db.commit()
    db.refresh(nova_os)

    for item in ordem.itens:
        item_os = ItemOrdemServico(
            ordem_servico_id=nova_os.id,
            item_id=item.item_id,
            quantidade=item.quantidade
        )
        db.add(item_os)
    db.commit()
    return nova_os

@router.get("/", response_model=List[OrdemServicoRead])
def listar_ordens_servico(db: Session = Depends(get_db)):
    return db.query(OrdemServico).all()

@router.get("/{ordem_id}", response_model=OrdemServicoRead)
def obter_ordem(ordem_id: int, db: Session = Depends(get_db)):
    os = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    if not os:
        raise HTTPException(status_code=404, detail="Ordem de serviço não encontrada")
    return os

@router.patch("/{ordem_id}/add_peca")
def adicionar_peca(ordem_id: int, item: ItemOrdemServicoCreate, db: Session = Depends(get_db)):
    os = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    if not os:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")

    item_os = ItemOrdemServico(
        ordem_servico_id=ordem_id,
        item_id=item.item_id,
        quantidade=item.quantidade
    )
    db.add(item_os)
    db.commit()
    return {"msg": "Peça adicionada com sucesso"}

@router.post("/{ordem_id}/finalizar")
def finalizar_ordem(ordem_id: int, db: Session = Depends(get_db)):
    os = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    if not os:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    os.status = "FINALIZADA"
    os.data_finalizacao = datetime.utcnow()
    db.commit()
    return {"msg": "Ordem de serviço finalizada com sucesso"}
