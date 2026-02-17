from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Calibracao, Instrumento
from .pdf import gerar_pdf_calibracao


def pdf_calibracao(request, calibracao_id):
    calibracao = get_object_or_404(Calibracao, id=calibracao_id)

    buffer = gerar_pdf_calibracao(calibracao)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename=f"calibracao_{calibracao.instrumento.codigo}.pdf"
    )


def instrumento_snapshot(request, instrumento_id):
    instrumento = get_object_or_404(Instrumento, id=instrumento_id)

    return JsonResponse({
        "descricao": instrumento.descricao,
        "marca": instrumento.marca,
        "modelo": instrumento.modelo,
        "tipo": instrumento.tipo,
        "numero_serie": instrumento.numero_serie or "",
    })

