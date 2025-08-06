from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ordem_servico import OrdemServico
from app.models.preventiva import ChecklistItem
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

router = APIRouter(prefix="/impressao", tags=["Impressão"])

@router.get("/ordem_servico/{ordem_id}/pdf")
def gerar_pdf_ordem(ordem_id: int, db: Session = Depends(get_db)):
    os = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    if not os:
        raise HTTPException(status_code=404, detail="Ordem de serviço não encontrada")

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, height - 50, f"Ordem de Serviço #{os.id}")
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 80, f"Descrição: {os.descricao}")
    p.drawString(50, height - 100, f"Status: {os.status}")
    p.drawString(50, height - 120, f"Prioridade: {os.prioridade}")
    p.drawString(50, height - 140, f"Data: {os.data_criacao.strftime('%d/%m/%Y')}")

    p.drawString(50, height - 180, "Checklist:")
    y = height - 200
    checklists = db.query(ChecklistItem).join(OrdemServico.equipamento).filter(
        ChecklistItem.plano.has(equipamento_id=os.equipamento_id)
    ).all()

    if checklists:
        for item in checklists:
            p.drawString(70, y, f"- {item.descricao}")
            y -= 20
            if y < 50:
                p.showPage()
                y = height - 50
    else:
        p.drawString(70, y, "Nenhum checklist associado ao equipamento.")

    p.drawString(50, y - 30, "Assinatura do Mecânico: __________________________")
    p.showPage()
    p.save()

    buffer.seek(0)
    return Response(buffer.read(), media_type="application/pdf",
                    headers={"Content-Disposition": f"inline; filename=ordem_servico_{ordem_id}.pdf"})
